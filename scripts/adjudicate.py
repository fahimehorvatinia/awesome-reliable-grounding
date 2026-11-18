"""Write the adjudicated corrections (Stage 3 inter-coder study) as corrections.jsonl.

Usage: python3 -I adjudicate.py <stage2 literature_db.jsonl> <additions.jsonl> <out corrections.jsonl> <out excluded.jsonl>

Each decision is (key, field, new value, reason). "old" is read from the current record so the merge
script can verify that nothing changed in between. Decisions marked "sample" resolve a disagreement in
the 40-work sample; decisions marked "rule" apply a codebook v1.1 clarification to a record outside the
sample where the recorded metadata alone suffices to apply it.
"""
import json
import sys

E4 = "E4 open-set grounding pre-training / dual encoder"
E7 = "E7 MLLM embedding-as-mask ([SEG])"
E8 = "E8 agentic / tool-using / RL-trained reasoning grounder"
E9 = "E9 training-free composition"


def add(*v):
    return ("add", list(v))


def drop(*v):
    return ("drop", list(v))


def setv(v):
    return ("set", v)


DECISIONS = [
    # ---- facet A ----
    ("zhang2024groundhog", "A_query", add("phrase/class name"), "sample: phrase grounding (Flickr30k/PNG phrases) evaluated"),
    ("zhang2024omgllava", "A_query", setv(["referring expression"]), "sample: no reasoning benchmark evaluated; visual prompts only yield captions (fail C2), codebook A rule"),
    ("yuan2026sa2va", "A_query", setv(["referring expression", "implicit instruction"]), "sample: ReVOS reasoning queries evaluated; visual prompts only yield captions"),
    ("yang2022tubedetr", "A_query", add("implicit instruction"), "sample: VidSTG interrogative sentences evaluated (v1.1 A rule)"),
    ("jin2022embracing", "A_query", add("implicit instruction"), "sample: VidSTG interrogative sentences evaluated (v1.1 A rule)"),
    ("zhang2020vidstg", "A_query", add("implicit instruction"), "rule: VidSTG defines interrogative sentences (v1.1 A rule)"),
    ("du2025crab", "A_query", add("composite"), "sample: Ref-AVS requires joint expression+audio interpretation"),
    ("zhang2025enhancing", "A_query", add("referring expression"), "sample: GUI instructions name the target element (v1.1 A rule)"),
    ("lu2026segcompass", "A_query", add("referring expression"), "sample: RefCOCO/+/g and gRefCOCO expressions evaluated"),
    # ---- facet B ----
    ("ding2026grex", "B_target", add("silent video"), "sample: ReLA also evaluated on MeViS and Ref-YouTube-VOS"),
    ("liu2023polyformer", "B_target", add("silent video"), "sample: zero-shot Ref-DAVIS17 evaluation"),
    ("zhang2024omgllava", "B_target", setv(["image"]), "sample: grounding evaluated on images only"),
    ("bai2024one", "B_target", add("image"), "sample: ReasonSeg and RefCOCO image evaluations"),
    ("zhang2026seqalign3dvg", "B_target", add("silent video"), "sample: ordered posed RGB frame sequences (v1.1 B rule)"),
    # ---- facet C ----
    ("wang2025segllm", "C_referent", drop("relation/interaction"), "sample: relations identify objects/parts; the referent is not a relation"),
    ("du2025crab", "C_referent", add("set (0..K)"), "sample: Ref-AVS Null and AVSBench MS3 evaluated"),
    ("sun2023learning", "C_referent", add("set (0..K)"), "sample: AVSBench MS3 multi-source evaluated"),
    ("zhang2026medgrounder", "C_referent", add("stuff/region"), "sample: finding regions are amorphous"),
    ("kerr2023lerf", "C_referent", add("set (0..K)"), "sample: existence experiment includes absent queries"),
    ("lu2026segcompass", "C_referent", add("set (0..K)"), "sample: gRefCOCO multi-object expressions"),
    ("gavrilyuk2018actor", "C_referent", drop("event/action"), "rule: actor identified by its action is an object instance (v1.1 C rule)"),
    ("ding2023mevis", "C_referent", drop("event/action"), "rule: motion-defined referents are objects (v1.1 C rule)"),
    ("ding2025mevistpami", "C_referent", drop("event/action"), "rule: motion-defined referents are objects (v1.1 C rule)"),
    ("he2024decoupling", "C_referent", drop("event/action"), "rule: motion-defined referents are objects (v1.1 C rule)"),
    ("tang2022hcstvg", "C_referent", drop("event/action"), "rule: STVG referent is the object tube (v1.1 C rule)"),
    # ---- facet D ----
    ("ding2026grex", "D_output", drop("grounded text"), "sample: GREG outputs plain region descriptions, not grounded text"),
    ("zhang2024groundhog", "D_output", add("2D box"), "sample: Flickr30k boxes evaluated (R@1)"),
    ("yuan2026sa2va", "D_output", drop("tube/track"), "sample: video masks scored per frame (J&F), no association metric"),
    ("wang2022negative", "D_output", add("tube/track"), "sample: HC-STVG tubes evaluated with vIoU"),
    ("du2025crab", "D_output", add("2D box"), "sample: ARIG boxes emitted as text coordinates (v1.1 D rule)"),
    ("sun2023learning", "D_output", add("mask"), "sample: zero-shot AVSBench masks evaluated"),
    ("deruyttere2021giving", "D_output", drop("grounded text"), "sample: clarification questions are not grounded text"),
    ("lu2026segcompass", "D_output", drop("point/heatmap"), "sample: slot heatmaps are internal; only masks evaluated"),
    # ---- facet E ----
    ("kamath2021mdetr", "E_paradigm", setv(E4), "sample: large-scale grounding pre-training for transfer; E4 precedes E3"),
    ("zhang2024groundhog", "E_paradigm", setv(E7), "sample: MLLM grounding-token embeddings select mask proposals; E7 precedes E1 (v1.1 E rule)"),
    ("kerr2023lerf", "E_paradigm", setv(E9), "sample: per-scene distillation of frozen CLIP/DINO, no grounding training (v1.1 E rule)"),
    ("qin2024langsplat", "E_paradigm", setv(E9), "rule: per-scene distillation of frozen CLIP features, no grounding training (v1.1 E rule)"),
    ("lu2026segcompass", "E_paradigm", setv(E8), "sample: GRPO-trained reasoning; E8 precedes E7"),
    # ---- facet F ----
    ("zhang2024groundhog", "F_supervision", add("weak"), "sample: box-only data supervise masks through a projection loss"),
    ("zhu2025popen", "F_supervision", add("synthetic/LLM-generated"), "sample: ChatGPT-corrected responses used for training"),
    ("mo2022ezvsl", "F_supervision", setv(["self-supervised correspondence"]), "sample: contrastive MIL on natural audio-visual pairs, no labels"),
    ("tian2018ave", "F_supervision", add("self-supervised correspondence"), "sample: AVDLN trained on synchronised pairs"),
    ("zhang2026medgrounder", "F_supervision", add("synthetic/LLM-generated"), "sample: weak boxes cleaned with an LLM"),
    ("kerr2023lerf", "F_supervision", drop("self-supervised correspondence"), "sample: distillation of frozen features, no correspondence learning"),
    ("liu2024rotated", "F_supervision", add("synthetic/LLM-generated"), "sample: SAM-generated masks, manually refined (v1.1 F rule)"),
    ("huang2022multiview", "F_supervision", add("synthetic/LLM-generated"), "sample: template-generated Sr3D/Sr3D+ used for training"),
    ("zhang2026seqalign3dvg", "F_supervision", add("synthetic/LLM-generated"), "sample: MLLM-drafted, human-verified descriptions (v1.1 F rule)"),
    ("lu2026segcompass", "F_supervision", add("RL verifiable reward"), "sample: GRPO with mask-IoU and format rewards"),
    ("yuan2024rrsis", "F_supervision", add("synthetic/LLM-generated"), "rule: template-generated expressions recorded in datasets (v1.1 F rule)"),
    # ---- facet G ----
    ("liu2023polyformer", "G_conditions", setv(["domain/sensor shift"]), "sample: zero-shot cross-dataset evaluation (image to video)"),
    ("wang2024unires", "G_conditions", setv(["domain/sensor shift"]), "sample: zero-shot transfer to RefCOCO/+/g"),
    ("zhang2024persam", "G_conditions", add("novel categories/compositions"), "sample: one-shot segmentation of unseen classes"),
    ("kamath2021mdetr", "G_conditions", add("novel categories/compositions"), "sample: few-shot long-tailed LVIS rare categories"),
    ("wang2025segllm", "G_conditions", add("domain/sensor shift"), "sample: unseen question templates (v1.1 G rule)"),
    ("yuan2026sa2va", "G_conditions", setv(["domain/sensor shift"]), "sample: zero-shot Ref-SAV evaluation"),
    ("seo2020urvos", "G_conditions", add("domain/sensor shift"), "sample: Refer-DAVIS17 without fine-tuning"),
    ("bai2024one", "G_conditions", setv(["domain/sensor shift"]), "sample: zero-shot ReasonVOS evaluation"),
    ("gao2017tall", "G_conditions", setv(["novel categories/compositions"]), "sample: test-only complex multi-sentence query set"),
    ("mo2022ezvsl", "G_conditions", add("domain/sensor shift"), "sample: cross-dataset Flickr/VGG-SS tests"),
    ("du2025crab", "G_conditions", add("multi-target", "novel categories/compositions"), "sample: MS3 subset; Ref-AVS Unseen split"),
    ("sun2023learning", "G_conditions", add("domain/sensor shift", "multi-target"), "sample: cross-dataset tests; AVSBench MS3"),
    ("arandjelovic2018objects", "G_conditions", setv(["conflicting modalities"]), "sample: mismatched frame-audio pairs probed"),
    ("rohrbach2018chair", "G_conditions", add("novel categories/compositions"), "sample: robust compositional and novel-object splits"),
    ("cirik2018visual", "G_conditions", setv(["missing modality", "degraded/noisy modality"]), "sample: expression-free and shuffled/partial-expression inputs; no distractor analysis"),
    ("zhang2026seqalign3dvg", "G_conditions", drop("missing modality"), "sample: depth-free input is the task design, not a missing-modality test"),
    ("lu2026segcompass", "G_conditions", setv(["domain/sensor shift", "multi-target"]), "sample: zero-shot ReasonSeg; gRefCOCO multi-object"),
    ("zhao2024generating", "G_conditions", add("multi-target"), "rule: D3 contains multi-target descriptions (v1.1 G rule: benchmark-defined conditions)"),
    ("yuan2026sa2va", "G_conditions", add("multi-target"), "rule: MeViS contains multi-object expressions (v1.1 G rule: benchmark-defined conditions)"),
    ("jiang2025detect", "G_conditions", add("absent target/false premise"), "rule: HumanRef contains rejection (no-target) queries (v1.1 G rule: benchmark-defined conditions)"),
    ("munasinghe2025videoglamm", "G_conditions", add("multi-target"), "rule: MeViS contains multi-object expressions (v1.1 G rule: benchmark-defined conditions)"),
    ("yan2024visa", "G_conditions", add("multi-target"), "rule: MeViS contains multi-object expressions (v1.1 G rule: benchmark-defined conditions)"),
    ("cuttano2025samwise", "G_conditions", add("multi-target"), "rule: MeViS contains multi-object expressions (v1.1 G rule: benchmark-defined conditions)"),
    ("bai2024one", "G_conditions", add("multi-target"), "rule: MeViS contains multi-object expressions (v1.1 G rule: benchmark-defined conditions)"),
    ("zheng2025villa", "G_conditions", add("multi-target"), "rule: MeViS contains multi-object expressions (v1.1 G rule: benchmark-defined conditions)"),
    ("rong2025mpgsam2", "G_conditions", add("multi-target"), "rule: MeViS contains multi-object expressions (v1.1 G rule: benchmark-defined conditions)"),
    ("ying2025omniavs", "G_conditions", add("multi-target"), "rule: MeViS contains multi-object expressions (v1.1 G rule: benchmark-defined conditions)"),
    ("park2024clip", "G_conditions", add("multi-target"), "rule: AVSBench MS3 multi-source subset evaluated (v1.1 G rule: benchmark-defined conditions)"),
    ("zheng2025video3dllm", "G_conditions", add("absent target/false premise"), "rule: Multi3DRefer contains zero-target descriptions (v1.1 G rule: benchmark-defined conditions)"),
    ("li2026avsbenchrobust", "G_conditions", add("multi-target"), "rule: AVSBench-Robust MS3 multi-source subset evaluated (v1.1 G rule: benchmark-defined conditions)"),
    ("lee2026multiagent", "G_conditions", add("multi-target"), "rule: MeViSv2 contains multi-object expressions (v1.1 G rule: benchmark-defined conditions)"),
    # ---- facet H ----
    ("seo2020urvos", "H_verification", setv(["none"]), "sample: memory attention enforces coherence during prediction; no check (v1.1 H rule)"),
    ("jin2022embracing", "H_verification", setv(["none"]), "sample: template enforces consistency in prediction; no check (v1.1 H rule)"),
    ("guo2023viewrefer", "H_verification", setv(["none"]), "sample: multi-view fusion, no output check (v1.1 H rule)"),
    ("arandjelovic2018objects", "H_verification", setv(["existence/abstention head"]), "sample: trained correspondence score decides whether the sound is in view"),
    ("zhang2025enhancing", "H_verification", setv(["calibrated confidence"]), "sample: calibrated confidence reward; no abstention output"),
    ("deruyttere2021giving", "H_verification", add("calibrated confidence"), "sample: ensembles and temperature scaling estimate uncertainty"),
    ("zhang2023multi3drefer", "H_verification", drop("none"), "rule: 'none' cannot co-occur with a mechanism (consistency)"),
    ("julin2026anchor", "G_conditions", drop("nominal"), "rule: 'nominal' cannot co-occur with a condition (consistency)"),
    ("wang2025hiea2g", "doi", setv("10.1609/aaai.v39i8.32867"), "rule: DOI found by Crossref title search in Stage 7 (open item from Stage 2)"),
]
EXCLUDED = [("yuan2024osprey", "sample: fails C2 (mask region in, text out; no localisation output)")]


def main():
    recs = {}
    for path in sys.argv[1:3]:
        for line in open(path):
            if line.strip():
                r = json.loads(line)
                recs[r["key"]] = r
    cur = {k: {f: (list(v) if isinstance(v, list) else v) for f, v in r.items()} for k, r in recs.items()}
    out = []
    for key, field, (op, val), reason in DECISIONS:
        r = cur[key]
        old = r[field]
        if op == "set":
            new = val
        elif op == "add":
            new = list(old) + [v for v in val if v.lower() not in [x.lower() for x in old]]
            new = [x for x in new if not (x == "nominal" and len(new) > 1)] if field == "G_conditions" else new
        else:
            missing = [v for v in val if v not in old]
            assert not missing, (key, field, missing, old)
            new = [x for x in old if x not in val]
        assert new != old, (key, field, old, new)
        out.append({"key": key, "field": field, "old": old, "new": new, "reason": reason})
        r[field] = new
    with open(sys.argv[3], "w") as f:
        for c in out:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    with open(sys.argv[4], "w") as f:
        for k, why in EXCLUDED:
            f.write(json.dumps({"key": k, "title": recs[k]["title"], "reason": why}) + "\n")
    n_sample = sum(1 for c in out if c["reason"].startswith("sample"))
    print(f"{len(out)} corrections ({n_sample} from the sample, {len(out) - n_sample} rule-based); {len(EXCLUDED)} excluded")


if __name__ == "__main__":
    main()
