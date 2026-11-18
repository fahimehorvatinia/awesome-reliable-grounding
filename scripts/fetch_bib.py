"""Fetch registry-sourced BibTeX for a reading list.

Usage: python3 -I fetch_bib.py <list.tsv> <out.bib>

TSV columns: key, group, source. Source prefixes:
  doi:<DOI>      -> DOI content negotiation (Crossref/DataCite metadata)
  url:<.bib URL> -> official proceedings BibTeX file
  cvf:/ecva:/pmlr:<page URL> -> BibTeX block scraped from the official paper page
  arxiv:<id>     -> arXiv's own BibTeX export
Entries whose BibTeX cannot be fetched are written as comments flagged FETCH-FAILED,
so nothing is silently filled in from memory.
"""
import html
import re
import sys
import time
import urllib.error
import urllib.request

UA = "survey-bib-fetcher/1.0 (mailto:research@example.org)"


def get(url, accept=None, retries=4):
    for attempt in range(retries):
        headers = {"User-Agent": UA}
        if accept:
            headers["Accept"] = accept
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                return r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and attempt < retries - 1:
                time.sleep(8 * (attempt + 1))
                continue
            raise


def extract_bib_block(page):
    page = html.unescape(re.sub(r"<br\s*/?>", "\n", page))
    m = re.search(r"(@(?:inproceedings|InProceedings|article|Article|incollection)\s*\{.*?\n\s*\}\s*)", page, flags=re.S)
    if not m:
        return None
    return re.sub(r"<[^>]+>", "", m.group(1)).strip()


def rekey(bib, key):
    return re.sub(r"^(@\w+\s*\{)\s*[^,]*,", lambda m: m.group(1) + key + ",", bib.strip(), count=1)


def fetch(source):
    kind, _, ref = source.partition(":")
    if kind == "doi":
        return get("https://doi.org/" + ref, accept="application/x-bibtex; charset=utf-8")
    if kind == "url":
        return get(ref)
    if kind in ("cvf", "ecva", "pmlr"):
        return extract_bib_block(get(ref))
    if kind == "arxiv":
        return get("https://arxiv.org/bibtex/" + ref)
    raise ValueError(source)


def main():
    rows = [l.rstrip("\n").split("\t") for l in open(sys.argv[1]) if l.strip()][1:]
    out = []
    failed = []
    for key, group, source in rows:
        try:
            bib = fetch(source)
            if not bib or "@" not in bib:
                raise ValueError("no BibTeX block found")
            out.append(f"% group: {group} | source: {source}\n{rekey(bib, key)}\n")
            print(f"ok      {key}")
        except Exception as e:  # report and continue; never fabricate
            failed.append(key)
            out.append(f"% FETCH-FAILED {key} | {group} | {source} | {e}\n")
            print(f"FAILED  {key}: {e}")
        time.sleep(1.5)
    with open(sys.argv[2], "w") as f:
        f.write("% Registry-sourced BibTeX (DOI content negotiation / official proceedings pages).\n")
        f.write("% Generated for Stage 1 of 'Reliable Multimodal Grounding: A Survey'. Do not hand-edit metadata;\n")
        f.write("% fix the source and regenerate.\n\n")
        f.write("\n".join(out))
    print(f"\n{len(rows) - len(failed)}/{len(rows)} fetched; failed: {failed}")


if __name__ == "__main__":
    main()
