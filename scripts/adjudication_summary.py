"""Summarise how sample disagreements were resolved: coder 1 kept, coder 2 adopted, or merged.

Usage: python3 -I adjudication_summary.py <stage2 db> <additions> <adjudicated db> <recode.jsonl> <excluded.jsonl> <out.csv>
"""
import json
import sys
from collections import Counter, defaultdict

sys.path.insert(0, __import__("os").path.dirname(__file__))
from icr import norm_e, norm_set  # noqa: E402

FIELDS = ["A_query", "B_target", "C_referent", "D_output", "E_paradigm", "F_supervision", "G_conditions", "H_verification"]


def load(*paths):
    d = {}
    for p in paths:
        for l in open(p):
            if l.strip():
                r = json.loads(l)
                d[r["key"]] = r
    return d


def val(r, f):
    return norm_e(r.get(f)) if f == "E_paradigm" else frozenset(norm_set(f, r.get(f)))


def main():
    c1 = load(sys.argv[1], sys.argv[2])
    adj = load(sys.argv[3])
    c2 = load(sys.argv[4])
    excl = {json.loads(l)["key"] for l in open(sys.argv[5]) if l.strip()}
    out = defaultdict(Counter)
    for k in c2:
        for f in FIELDS:
            a, b = val(c1[k], f), val(c2[k], f)
            if a == b:
                continue
            if k in excl:
                out[f]["work excluded"] += 1
                continue
            z = val(adj[k], f)
            out[f]["coder 1 kept" if z == a else "coder 2 adopted" if z == b else "merged / other"] += 1
    cols = ["coder 1 kept", "coder 2 adopted", "merged / other", "work excluded"]
    with open(sys.argv[6], "w") as fh:
        fh.write("facet," + ",".join(cols) + ",total\n")
        tot = Counter()
        for f in FIELDS:
            fh.write(f + "," + ",".join(str(out[f][c]) for c in cols) + f",{sum(out[f].values())}\n")
            tot.update(out[f])
        fh.write("all," + ",".join(str(tot[c]) for c in cols) + f",{sum(tot.values())}\n")
    print(open(sys.argv[6]).read())


if __name__ == "__main__":
    main()
