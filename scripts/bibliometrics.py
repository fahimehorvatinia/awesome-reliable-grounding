"""Reproducible publication-count protocol (Figure 2b, PRISMA identification counts).

Usage: python3 -I bibliometrics.py counts.csv samples.json

Queries the Semantic Scholar Graph API bulk search (title + abstract matching) per task family
and per year, restricted to fieldsOfStudy=Computer Science. Stores totals per (family, year) and
a sample of returned titles per family (2024) for manual precision estimation.
Query syntax: "phrase", + AND, | OR, - NOT, parentheses (Semantic Scholar bulk search).
"""
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"
FAMILIES_ALL = {
    "image": '("referring expression" | "phrase grounding" | "referring image segmentation" | "visual grounding" | "referring segmentation") -video -"3D" -audio',
    "video": '("temporal grounding" | "moment retrieval" | "temporal sentence grounding" | "video grounding" | "spatio-temporal video grounding" | "referring video object segmentation" | "referring multi-object tracking")',
    "audiovisual": '"audio-visual segmentation" | "visual sound source localization" | "visual sound localization" | "audio-visual source localization" | "sound source localization in visual scenes" | "localizing visual sounds" | "audio-visual grounding" | "referring audio-visual segmentation" | "text-to-audio grounding" | "sounding object localization"',
    "3d": '("3D visual grounding" | "3D referring" | "3D grounding" | "point cloud grounding" | "3D referring expression")',
    "mllm": '("visual grounding" | "referring expression comprehension" | "referring segmentation" | "pixel grounding" | "reasoning segmentation" | "grounded conversation") + ("large language model" | "multimodal large language model" | "MLLM" | "LVLM")',
    "reliability": '("visual grounding" | "referring expression" | "phrase grounding" | "temporal grounding" | "moment retrieval" | "audio-visual segmentation" | "3D visual grounding" | "referring segmentation" | "referring video object segmentation") + ("robustness" | "hallucination" | "missing modality" | "adversarial attack" | "no-target" | "false premise" | "out-of-distribution" | "uncertainty" | "calibration" | "dataset bias" | "shortcut" | "interpretability")',
}
FAMILIES = {k: v for k, v in FAMILIES_ALL.items() if k in (sys.argv[3].split(",") if len(sys.argv) > 3 else FAMILIES_ALL)}
YEARS = range(2014, 2027)


def call(params, retries=6):
    url = API + "?" + urllib.parse.urlencode(params)
    for k in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "survey-bibliometrics/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and k < retries - 1:
                time.sleep(5 * (k + 1))
                continue
            raise


def main():
    rows = ["family,year,total"]
    samples = {}
    for fam, q in FAMILIES.items():
        for y in YEARS:
            d = call({"query": q, "year": str(y), "fieldsOfStudy": "Computer Science", "fields": "title"})
            total = d.get("total", 0)
            rows.append(f"{fam},{y},{total}")
            print(fam, y, total, flush=True)
            if y == 2024:
                samples[fam] = [p.get("title", "") for p in d.get("data", [])[:60]]
            time.sleep(1.6)
    open(sys.argv[1], "w").write("\n".join(rows) + "\n")
    json.dump({"queries": FAMILIES, "fieldsOfStudy": "Computer Science", "api": API,
               "retrieved": time.strftime("%Y-%m-%d"), "samples_2024": samples},
              open(sys.argv[2], "w"), indent=1)


if __name__ == "__main__":
    main()
