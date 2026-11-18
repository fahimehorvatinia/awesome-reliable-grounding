"""Build protocol-matched benchmark tables from the merged database.

Usage: python3 -I build_tables.py <merged_dir> <out_dir> [spotcheck_results.csv]

* Normalises synonymous labels only (e.g. 'top-1 accuracy (%)', 'accuracy (IoU>0.5)' -> Acc@0.5 on RefCOCO-family
  REC; 'oIoU' == 'cIoU' for referring segmentation). Ambiguous labels (bare 'IoU') are kept separate.
* Groups rows by a setting class derived from each paper's own description of its setting.
* Drops values flagged MISMATCH by the independent spot-check (if a results file is given).
* Writes protocols.csv (everything, with source pointers) and tables.tex (LaTeX for the manuscript).
"""
import csv
import json
import os
import re
import sys
from collections import defaultdict

REFC = {"refcoco": "RefCOCO", "refcoco+": "RefCOCO+", "refcocog": "RefCOCOg"}


def canon(bench, metric, split):
    b = bench.strip()
    m = metric.strip()
    bl, ml, sl = b.lower(), m.lower(), split.strip()
    base = re.sub(r"\s*\((res|rec|grec|gres)\)\s*$", "", bl).strip()
    task_tag = re.search(r"\((res|rec|grec|gres)\)", bl)
    task_tag = task_tag.group(1) if task_tag else ""
    sl_norm = sl.replace("val (UMD)", "val").replace("test (UMD)", "test")
    sl_norm = re.sub(r"\s*\(umd\)", "", sl_norm, flags=re.I)
    if base in REFC:
        name = REFC[base]
        if task_tag in ("rec", "") and re.search(r"acc|top-1|precision@0\.5|p@0\.5", ml) and "iou" not in ml.replace("iou>0.5", "").replace("iou≥0.5", ""):
            return ("REC", name, sl_norm, "Acc@0.5")
        if task_tag == "res" or re.search(r"iou", ml):
            mm = re.sub(r"\s*\(.*\)", "", m).strip()
            if mm.lower() in ("oiou", "ciou", "overall iou", "cumulative iou"):
                return ("RES", name, sl_norm, "oIoU/cIoU")
            if mm.lower() == "miou":
                return ("RES", name, sl_norm, "mIoU")
            if mm.lower() == "giou":
                return ("RES", name, sl_norm, "gIoU")
            return ("RES", name, sl_norm, "IoU (unspecified)")
    if base == "grefcoco":
        if task_tag == "grec":
            return ("GREC", "gRefCOCO", sl_norm, m)
        mm = re.sub(r"\s*\(.*\)", "", m).strip()
        return ("GRES", "gRefCOCO", sl_norm, {"ciou": "cIoU", "giou": "gIoU", "n-acc": "N-acc", "n-acc.": "N-acc"}.get(mm.lower(), mm))
    if base == "reasonseg":
        return ("ReasonSeg", "ReasonSeg", sl_norm, re.sub(r"\s*\(.*\)", "", m).strip())
    return ("other", b, sl_norm, m)


def setting_class(rec, setting):
    s = setting.lower()
    blob = " ".join([s, str(rec.get("foundation_models", "")).lower(), str(rec.get("architecture", "")).lower()])
    if re.search(r"zero-shot|training-free|unsupervised|weakly", s):
        return "zero-shot / weak / training-free"
    if re.search(r"vicuna|llama|qwen|internvl|phi-|phi1|\\bmllm\\b|\\blmm\\b|large language|\\bllm\\b|gpt|mistral|minigpt|llava|cogvlm|grpo", blob):
        return "MLLM-based"
    if "mllm" in rec.get("slices", []) or re.search(r"extra pre-training data: yes|pre-trained then fine-tuned|pre-training data o365|in pre-training.*yes|jointly trained", s):
        return "with extra grounding pre-training (specialist or generalist)"
    return "specialist, no extra grounding pre-training"


def short_name(rec):
    t = rec.get("title", "")
    if ":" in t:
        head = t.split(":")[0].strip()
        if len(head) <= 20 and len(head.split()) <= 3:
            return head
    return None


def fmt(v):
    try:
        x = float(v)
    except (TypeError, ValueError):
        return str(v)
    return f"{x:.1f}" if x > 1.0 else f"{x:.3f}"


def main():
    mdir, outd = sys.argv[1], sys.argv[2]
    os.makedirs(outd, exist_ok=True)
    recs = {json.loads(l)["key"]: json.loads(l) for l in open(os.path.join(mdir, "literature_db.jsonl"))}
    alias = json.load(open(os.path.join(mdir, "key_alias.json")))
    bad = set()
    if len(sys.argv) > 3 and os.path.exists(sys.argv[3]):
        spot = list(csv.DictReader(open(sys.argv[3])))
        sample = {r["id"]: r for r in csv.DictReader(open(os.path.join(os.path.dirname(sys.argv[3]), "spotcheck_sample.csv")))}
        for r in spot:
            if r["verdict"].startswith("MISMATCH"):
                s = sample[r["id"]]
                bad.add((s["key"], s["benchmark"], s["split"], s["metric"], s["value"]))
    rows = list(csv.DictReader(open(os.path.join(mdir, "benchmark_results.csv"))))
    proto = defaultdict(list)
    dropped = 0
    with open(os.path.join(outd, "protocols.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["task", "benchmark", "split", "metric", "value", "key", "bibkey", "setting_class", "setting", "source", "venue", "status"])
        for r in rows:
            if (r["key"], r["benchmark"], r["split"], r["metric"], r["value"]) in bad:
                dropped += 1
                continue
            task, b, sp, m = canon(r["benchmark"], r["metric"], r["split"])
            rec = recs[r["key"]]
            cls = setting_class(rec, r["setting"])
            w.writerow([task, b, sp, m, r["value"], r["key"], alias.get(r["key"], r["key"]), cls, r["setting"], r["source"], r["venue"], r["status"]])
            proto[(task, b, m)].append((sp, r, cls))
    # ---------------- LaTeX: REC on RefCOCO family ----------------
    def method_cell(key, cls=None):
        rec = recs[key]
        bk = alias.get(key, key)
        nm = {"wang2022ofa": "OFA-Huge"}.get(key, short_name(rec))
        cell = (f"{nm}~\\citep{{{bk}}}" if nm else f"\\citet{{{bk}}}")
        if rec.get("status", "peer-reviewed") != "peer-reviewed":
            cell += "$^{\\dagger}$"
        if key == "jiang2026rexthinker" and cls == "zero-shot / weak / training-free":
            cell += "$^{\\ddagger}$"
        return cell

    tex = []
    cols = [("RefCOCO", "val"), ("RefCOCO", "testA"), ("RefCOCO", "testB"), ("RefCOCO+", "val"), ("RefCOCOg", "val"), ("RefCOCOg", "test")]

    def refc_table(task, metric, caption, label):
        table = defaultdict(dict)
        cls_of = {}
        for (t, b, m), lst in proto.items():
            if t != task or m != metric:
                continue
            for sp, r, cls in lst:
                for cb, cs in cols:
                    if b == cb and sp.lower() == cs.lower():
                        table[(r["key"], cls)].setdefault((cb, cs), r["value"])
                        cls_of[(r["key"], cls)] = cls
        keys = [k for k in table if len(table[k]) >= 2]
        order = ["specialist, no extra grounding pre-training", "with extra grounding pre-training (specialist or generalist)", "zero-shot / weak / training-free", "MLLM-based"]
        out = ["\\begin{table*}[p]", "\\caption{" + caption + "}", "\\label{" + label + "}", "\\centering\\scriptsize",
               "\\setlength{\\tabcolsep}{2pt}", "\\begin{tabular}{@{}l l *{6}{r}@{}}", "\\toprule",
               "Method & Venue & \\multicolumn{3}{c}{RefCOCO} & RefCOCO+ & \\multicolumn{2}{c}{RefCOCOg}\\\\",
               "\\cmidrule(lr){3-5}\\cmidrule(lr){6-6}\\cmidrule(lr){7-8}",
               " & & val & testA & testB & val & val & test\\\\", "\\midrule"]
        for grp in order:
            gk = sorted([k for k in keys if cls_of[k] == grp], key=lambda k: (recs[k[0]].get("year", 0), k[0]))
            if not gk:
                continue
            out.append("\\multicolumn{8}{@{}l}{\\emph{" + grp + "}}\\\\")
            for k in gk:
                vals = [fmt(table[k].get(c, "--")) if c in table[k] else "--" for c in cols]
                venue = re.sub(r"\s*\(.*$", "", recs[k[0]].get("venue", "")).replace("IEEE ", "").replace("&", "\\&")
                venue = re.sub(r"\s+(19|20)\d\d$", "", venue)  # year is already in the author-year citation
                out.append(f"{method_cell(k[0], k[1])} & {venue} & " + " & ".join(vals) + "\\\\")
        out += ["\\bottomrule", "\\end{tabular}", "\\end{table*}"]
        return out, len(keys)

    t1, n1 = refc_table("REC", "Acc@0.5",
                        "Referring expression comprehension on the RefCOCO family (Acc@0.5, \\%). Values are copied from each paper's own results table; the paper, arXiv version and table of every value are listed in the released \\texttt{protocols.csv}. Rows are grouped by setting as described by each paper; settings within a group can still differ in backbone and in whether the evaluation images overlap with pre-training data, so differences of a few points should not be read as rankings. Venue years equal the citation years. $^{\\dagger}$Preprint or workshop paper. $^{\\ddagger}$Uses detector box hints derived from the ground-truth category.",
                        "tab:rec-results")
    t2, n2 = refc_table("RES", "oIoU/cIoU",
                        "Referring expression segmentation on the RefCOCO family (overall/cumulative IoU, \\%; papers reporting only mIoU or an unspecified IoU are listed separately in \\texttt{protocols.csv}). Same conventions as Table~\\ref{tab:rec-results}.",
                        "tab:res-results")
    tex += t1 + [""] + t2 + [""]

    # ---------------- generic small tables ----------------
    def generic(spec, caption, label):
        # spec: list of (task, bench, metric, split, column header)
        table = defaultdict(dict)
        zs = set()
        for i, (task, b, m, sp, _) in enumerate(spec):
            for sp2, r, cls in proto.get((task, b, m), []):
                if sp is None or sp2.lower() == sp.lower():
                    table[r["key"]].setdefault(i, r["value"])
                    if "zero-shot" in r["setting"].lower() and table[r["key"]][i] == r["value"]:
                        zs.add((r["key"], i))
        keys = sorted(table, key=lambda k: (recs[k].get("year", 0), k))
        out = ["\\begin{table*}[p]", "\\caption{" + caption + "}", "\\label{" + label + "}", "\\centering\\scriptsize",
               "\\setlength{\\tabcolsep}{3pt}", "\\begin{tabular}{@{}l *{" + str(len(spec)) + "}{r}@{}}", "\\toprule",
               "Method & " + " & ".join(h for *_, h in spec) + "\\\\", "\\midrule"]
        for k in keys:
            out.append(method_cell(k) + " & " + " & ".join((fmt(table[k][i]) + ("$^{\\ast}$" if (k, i) in zs else "")) if i in table[k] else "--" for i in range(len(spec))) + "\\\\")
        out += ["\\bottomrule", "\\end{tabular}", "\\end{table*}"]
        return out, len(keys)

    def find(task, bench_sub, metric_sub):
        hits = [k for k in proto if k[0] == task and bench_sub.lower() == k[1].lower() and metric_sub.lower() == k[2].lower()]
        return hits[0] if hits else (task, bench_sub, metric_sub)

    gspec = [("GRES", "gRefCOCO", "cIoU", "val", "cIoU"), ("GRES", "gRefCOCO", "gIoU", "val", "gIoU"), ("GRES", "gRefCOCO", "N-acc", "val", "N-acc"),
             ("ReasonSeg", "ReasonSeg", "gIoU", "val", "RS gIoU"), ("ReasonSeg", "ReasonSeg", "cIoU", "val", "RS cIoU")]
    t3, n3 = generic(gspec, "Generalised referring segmentation on gRefCOCO (val) and reasoning segmentation on ReasonSeg (val, RS). N-acc is the accuracy on no-target expressions, a selectivity measure (P4). $^{\\ast}$Zero-shot on that benchmark: the model was not trained on it. $^{\\dagger}$Preprint or workshop paper. GRES and GREx report slightly different numbers for the same ReLA model; both are listed as published.", "tab:gres-results")
    tex += t3 + [""]
    summary = {"REC rows": n1, "RES rows": n2, "GRES/ReasonSeg rows": n3, "dropped by spot-check": dropped}
    open(os.path.join(outd, "tables.tex"), "w").write("\n".join(tex) + "\n")
    counts = defaultdict(int)
    for (t, b, m), lst in proto.items():
        counts[f"{t}|{b}|{m}"] = len(lst)
    with open(os.path.join(outd, "protocol_counts.csv"), "w") as f:
        f.write("protocol,n\n")
        for k, v in sorted(counts.items(), key=lambda x: -x[1]):
            f.write(f"\"{k}\",{v}\n")
    print(summary)


if __name__ == "__main__":
    main()
