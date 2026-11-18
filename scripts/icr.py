"""Inter-coder agreement between the database coding (coder 1) and the blind re-coding (coder 2).

Usage: python3 -I icr.py <literature_db.jsonl (coder 1)> <recode.jsonl (coder 2)> <out_dir>

Multi-label facets (A-D, F-H): every (work, value) pair of the facet vocabulary is a binary decision;
Cohen's kappa is computed on the pooled 2x2 table ("pooled binary kappa"), and the mean per-work
Jaccard index is reported alongside. Facet E (single label): Cohen's kappa over works.
Writes agreement.csv, disagreements.md and a LaTeX table body (icr_table.tex).
"""
import json
import os
import sys
from collections import Counter

VOCAB = {
    "A_query": ["phrase/class name", "referring expression", "implicit instruction", "speech", "non-speech sound",
                "visual exemplar", "visual prompt", "gesture/gaze", "composite"],
    "B_target": ["image", "silent video", "audio-visual video", "audio-only", "rgb-d", "point cloud",
                 "radiance field/3dgs", "lidar/radar/thermal", "remote sensing", "medical"],
    "C_referent": ["object instance", "part", "stuff/region", "set (0..k)", "event/action", "sound source",
                   "relation/interaction", "affordance"],
    "D_output": ["point/heatmap", "2d box", "rotated box", "mask", "temporal interval", "tube/track", "3d box",
                 "3d mask", "grounded text"],
    "F_supervision": ["full", "weak", "self-supervised correspondence", "semi-supervised", "zero-shot/training-free",
                      "synthetic/llm-generated", "rl verifiable reward"],
    "G_conditions": ["nominal", "missing modality", "degraded/noisy modality", "conflicting modalities",
                     "ambiguity/distractors", "absent target/false premise", "multi-target", "domain/sensor shift",
                     "novel categories/compositions", "adversarial", "long-horizon drift"],
    "H_verification": ["none", "existence/abstention head", "calibrated confidence", "cycle/reg consistency",
                       "temporal/cross-view consistency", "self-verification/re-grounding", "external verifier",
                       "traceable evidence", "interactive clarification"],
}
NAMES = {"A_query": "A Query modality", "B_target": "B Target context", "C_referent": "C Referent type",
         "D_output": "D Output representation", "E_paradigm": "E Architecture paradigm",
         "F_supervision": "F Supervision", "G_conditions": "G Reliability condition",
         "H_verification": "H Verification mechanism"}


def norm_set(field, vals):
    out = set()
    for v in vals or []:
        v = v.strip().lower().replace(" / ", "/")
        out.add(v)
    return out


def norm_e(v):
    v = (v or "").strip().lower()
    return v.split()[0].upper() if v[:1] == "e" and v[1:2].isdigit() else v


def kappa(pairs):
    n = len(pairs)
    if not n:
        return float("nan"), float("nan")
    po = sum(a == b for a, b in pairs) / n
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / n / n
    return po, (po - pe) / (1 - pe) if pe < 1 else float("nan")


def main():
    db = {json.loads(l)["key"]: json.loads(l) for l in open(sys.argv[1])}
    rc = [json.loads(l) for l in open(sys.argv[2]) if l.strip()]
    rc = {r["key"]: r for r in rc}
    keys = [k for k in rc if k in db]
    os.makedirs(sys.argv[3], exist_ok=True)
    rows, dis = [], []
    off_vocab = Counter()
    for field in ["A_query", "B_target", "C_referent", "D_output", "E_paradigm", "F_supervision", "G_conditions",
                  "H_verification"]:
        if field == "E_paradigm":
            pairs = [(norm_e(db[k][field]), norm_e(rc[k].get(field))) for k in keys]
            po, k_ = kappa(pairs)
            rows.append((field, len(keys), po, k_, po))
            for k, (a, b) in zip(keys, pairs):
                if a != b:
                    dis.append((k, field, a, b, rc[k].get("evidence", {}).get("E", "")))
            continue
        voc = VOCAB[field]
        pairs, jac = [], []
        for k in keys:
            s1, s2 = norm_set(field, db[k].get(field)), norm_set(field, rc[k].get(field))
            for v in s2 - set(voc):
                off_vocab[(field, v)] += 1
            for v in voc:
                pairs.append((v in s1, v in s2))
            u = s1 | s2
            jac.append(len(s1 & s2) / len(u) if u else 1.0)
            if s1 != s2:
                dis.append((k, field, sorted(s1), sorted(s2), rc[k].get("evidence", {}).get(field[0], "")))
        po, k_ = kappa(pairs)
        rows.append((field, len(keys), po, k_, sum(jac) / len(jac)))
    with open(os.path.join(sys.argv[3], "agreement.csv"), "w") as f:
        f.write("facet,n_works,observed_agreement,cohen_kappa,mean_jaccard_or_exact\n")
        for r in rows:
            f.write(f"{r[0]},{r[1]},{r[2]:.3f},{r[3]:.3f},{r[4]:.3f}\n")
    with open(os.path.join(sys.argv[3], "disagreements.md"), "w") as f:
        f.write(f"# Disagreements (coder 1 = database, coder 2 = blind re-coding); {len(keys)} works\n\n")
        for k, field, a, b, ev in dis:
            f.write(f"- **{k}** {field}: db={a} | recode={b} | evidence: {ev}\n")
        if off_vocab:
            f.write("\n## Off-vocabulary values used by coder 2\n")
            for (fld, v), n in off_vocab.items():
                f.write(f"- {fld}: {v!r} x{n}\n")
    with open(os.path.join(sys.argv[3], "icr_table_rows.tex"), "w") as f:
        for field, n, po, k_, j in rows:
            last = f"{j:.2f}" if field != "E_paradigm" else "--"
            f.write(f"{NAMES[field]} & {po:.3f} & {k_:.2f} & {last}\\\\\n")
    for r in rows:
        print(f"{r[0]:15s} n={r[1]} po={r[2]:.3f} kappa={r[3]:.2f} jac/exact={r[4]:.2f}")
    print(f"{len(dis)} facet-level disagreements; off-vocabulary values: {sum(off_vocab.values())}")


if __name__ == "__main__":
    main()
