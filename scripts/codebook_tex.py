"""Render codebook.md as the two LaTeX tables of Appendix C (facets A-D and E-H).

Usage: python3 -I codebook_tex.py <codebook.md> <out.tex>
"""
import re
import sys

REPL = [("&", r"\&"), ("%", r"\%"), ("#", r"\#"), ("_", r"\_"), ("→", r"$\rightarrow$"), ("≥", r"$\geq$"),
        ("≤", r"$\leq$"), ("∈", r"$\in$"), ("⊆", r"$\subseteq$"), ("…", r"\dots{}"), ("—", "---"), ("–", "--"),
        ("×", r"$\times$"), ("ι", r"$\iota$"), ("θ", r"$\theta$"), ("Ω", r"$\Omega$"), ("Ŷ", r"$\hat{Y}$")]


def tex(s):
    s = s.strip()
    for a, b in REPL:
        s = s.replace(a, b)
    s = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", s)
    s = re.sub(r"\*(.+?)\*", r"\\emph{\1}", s)
    s = re.sub(r"`([^`]+)`", r"\1", s)
    s = re.sub(r'"([^"]+)"', r"``\1''", s)
    s = s.replace("R*", r"$R^\ast$").replace("|R*|", r"$|R^\ast|$")
    return s


def parse(md):
    facets = {}
    cur = None
    for line in md.splitlines():
        m = re.match(r"## Facet ([A-H]) — (.+)", line)
        if m:
            cur = m.group(1)
            facets[cur] = {"title": re.sub(r"\s*\(.*\)$", "", m.group(2)), "rows": []}
            continue
        if line.startswith("## ") and not line.startswith("## Facet"):
            cur = None
            continue
        if cur is None:
            continue
        if line.startswith("|") and not re.match(r"\|\s*-", line) and not line.startswith("| Value"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rule = cells[2] if len(cells) > 2 else ""
            facets[cur]["rows"].append((cells[0], cells[1], rule))
        m = re.match(r"\d+\.\s+(.+)", line)
        if m and cur == "E":
            body = m.group(1)
            for part in re.split(r"(?<=\.)\s+(?=`)", body):
                mm = re.match(r"`([^`]+)`\s*[—-]\s*(.+)", part)
                if mm:
                    facets[cur]["rows"].append((mm.group(1), mm.group(2)[0].upper() + mm.group(2)[1:], ""))
    return facets


def table(facets, letters, caption, label):
    out = [r"\begin{table*}[p]", f"\\caption{{{caption}}}", f"\\label{{{label}}}", r"\centering\scriptsize",
           r"\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{3.0cm} Y@{}}", r"\toprule",
           r"Value & Definition and decision rules\\", r"\midrule"]
    for i, L in enumerate(letters):
        f = facets[L]
        if i:
            out.append(r"\midrule")
        out.append(f"\\multicolumn{{2}}{{@{{}}l}}{{\\textbf{{{L}\\quad {tex(f['title'])}}}}}\\\\")
        for v, d, r in f["rows"]:
            text = tex(d) + (" " + tex(r) if r else "")
            out.append(f"{tex(v).replace('/', '/\\allowbreak{}')} & {text}\\\\")
    out += [r"\bottomrule", r"\end{tabularx}", r"\end{table*}", ""]
    return "\n".join(out)


def main():
    facets = parse(open(sys.argv[1]).read())
    assert set(facets) == set("ABCDEFGH"), facets.keys()
    assert len(facets["E"]["rows"]) == 11, facets["E"]["rows"]
    s = table(facets, "ABCD", "Codebook, part 1: facets A--D (multi-label). Values are coded from what a paper does, not from its related-work discussion.", "tab:codebook1")
    s += table(facets, "EFGH", "Codebook, part 2: facets E--H. Facet E is single-label and is assigned by the first matching rule, in the order listed; F--H are multi-label.", "tab:codebook2")
    open(sys.argv[2], "w").write(s)
    print("wrote", sys.argv[2], {k: len(v["rows"]) for k, v in facets.items()})


if __name__ == "__main__":
    main()
