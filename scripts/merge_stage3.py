"""Build the Stage 3 database: Stage 2 records + additions + adjudicated corrections.

Usage: python3 -I merge_stage3.py <stage2 literature_db.jsonl> <additions.jsonl> <corrections.jsonl> <excluded.jsonl> <out.jsonl>

excluded.jsonl: {"key", "reason"} for works removed after adjudication (failed admission).

corrections.jsonl: one object per line {"key", "field", "old", "new", "reason"}; "old" must match the
current value exactly, so a correction is never applied to a record that has changed since adjudication.
"""
import json
import sys


def main():
    recs = [json.loads(line) for line in open(sys.argv[1])]
    keys = {r["key"] for r in recs}
    for line in open(sys.argv[2]):
        if line.strip():
            r = json.loads(line)
            assert r["key"] not in keys, f"duplicate key {r['key']}"
            recs.append(r)
            keys.add(r["key"])
    by_key = {r["key"]: r for r in recs}
    n = 0
    try:
        lines = open(sys.argv[3]).read().splitlines()
    except FileNotFoundError:
        lines = []
    for line in lines:
        if not line.strip():
            continue
        c = json.loads(line)
        r = by_key[c["key"]]
        assert r.get(c["field"]) == c["old"], f"{c['key']}.{c['field']}: expected {c['old']!r}, found {r.get(c['field'])!r}"
        r[c["field"]] = c["new"]
        r.setdefault("stage3_corrections", []).append({"field": c["field"], "old": c["old"], "reason": c["reason"]})
        n += 1
    excluded = {json.loads(l)["key"] for l in open(sys.argv[4]) if l.strip()}
    recs = [r for r in recs if r["key"] not in excluded]
    with open(sys.argv[5], "w") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"{len(recs)} records, {n} corrections, {len(excluded)} excluded -> {sys.argv[5]}")


if __name__ == "__main__":
    main()
