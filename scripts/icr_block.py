"""Write the inter-coder reliability paragraph and table for Appendix C.

Usage: python3 -I icr_block.py <agreement.csv> <adjudication_summary.csv> <corrections.jsonl> <sample.tsv> <out.tex>
"""
import csv
import json
import sys

NAMES = {"A_query": "A Query modality", "B_target": "B Target context", "C_referent": "C Referent type",
         "D_output": "D Output representation", "E_paradigm": "E Architecture paradigm$^{\\dagger}$",
         "F_supervision": "F Supervision", "G_conditions": "G Reliability condition",
         "H_verification": "H Verification mechanism"}


def main():
    agr = {r["facet"]: r for r in csv.DictReader(open(sys.argv[1]))}
    adj = {r["facet"]: r for r in csv.DictReader(open(sys.argv[2]))}
    corr = [json.loads(l) for l in open(sys.argv[3]) if l.strip()]
    sample = {l.split("\t")[0] for l in open(sys.argv[4]).read().splitlines()[1:]}
    rule_out = {c["key"] for c in corr if c["reason"].startswith("rule") and c["key"] not in sample}
    tot = adj["all"]
    ks = {f: float(agr[f]["cohen_kappa"]) for f in agr}
    multi = [f for f in agr if f != "E_paradigm"]
    hi = [f for f in multi if f != "G_conditions"]
    rows = []
    for f in NAMES:
        a, d = agr[f], adj[f]
        j = "--" if f == "E_paradigm" else f"{float(a['mean_jaccard_or_exact']):.2f}"
        rows.append(f"{NAMES[f]} & {float(a['observed_agreement']):.3f} & {float(a['cohen_kappa']):.2f} & {j} & "
                    f"{d['total']} & {d['coder 1 kept']} & {d['coder 2 adopted']} & {d['merged / other']} & {d['work excluded']}\\\\")
    text = rf"""\paragraph{{Inter-coder reliability.}} To test whether the codebook can be applied reproducibly, a second coder re-coded a stratified random sample of 40 works (six from each task slice and ten from the reliability slice) from the papers themselves, using only codebook v1.0 and without access to the database. Thirty-eight works were coded from the full text, six of them through machine-generated summaries of the full text, and two closed-access works from their abstracts. For multi-label facets every (work, value) pair is one binary decision, and Cohen's $\kappa$ is computed on the pooled decisions; for the single-label facet E it is computed over works. Table~\ref{{tab:icr}} reports agreement before adjudication: $\kappa$ ranges from {min(ks[f] for f in hi):.2f} to {max(ks[f] for f in hi):.2f} for facets A--D, F and H, and is lower for the architecture paradigm E ($\kappa={ks['E_paradigm']:.2f}$) and the reliability condition G ($\kappa={ks['G_conditions']:.2f}$).

The {tot['total']} facet-level disagreements were adjudicated against the codebook: the database code was kept in {tot['coder 1 kept']}, the second coder's code adopted in {tot['coder 2 adopted']}, and a merged or revised code used in {tot['merged / other']}; {tot['work excluded']} concerned a region-captioning model whose output is text, which fails criterion C2 and was removed from the corpus. Most E disagreements came from three underspecified rules: whether a dataset paper that also contributes a model is coded by the model, whether DETR-style decoders without bipartite matching belong to E3, and how the precedence order treats grounding pre-training and RL-trained models. Most G disagreements were conditions that the first pass had not coded although an evaluated standard benchmark contains them (multi-target subsets) or a zero-shot cross-dataset evaluation tests them (domain shift). Codebook v1.1 resolves these ambiguities and is released with its change log. Where the recorded metadata sufficed, the clarified rules were also applied outside the sample, correcting {len(rule_out)} further records. Zero-shot cross-dataset evaluations cannot be identified from the metadata, so the domain-shift count in Fig.~\ref{{fig:taxonomy}} is a lower bound. In the sample, the condition codes added by adjudication were mostly common conditions; only three concerned missing, degraded or conflicting inputs, so the conclusion that these conditions are rarely studied does not depend on the correction.

\begin{{table*}}[!tbp]
\caption{{Inter-coder agreement on 40 randomly sampled works before adjudication (codebook v1.0), and how the disagreements were resolved. $p_o$: observed agreement over binary (work, value) decisions; $\kappa$: Cohen's kappa on the same decisions; $\bar{{J}}$: mean per-work Jaccard index between the two coders' value sets. Disagr.: works whose codes differ; kept, adopted, revised: resolved in favour of the database, of the second coder, or by a merged or revised code; excl.: the work failed admission and was removed. $^{{\dagger}}$Single-label facet: $p_o$ and $\kappa$ are over works.}}
\label{{tab:icr}}
\centering\footnotesize
\setlength{{\tabcolsep}}{{3.5pt}}
\begin{{tabular}}{{@{{}}l r r r r r r r r@{{}}}}
\toprule
Facet & $p_o$ & $\kappa$ & $\bar{{J}}$ & Disagr. & Kept & Adopted & Revised & Excl.\\
\midrule
""" + "\n".join(rows) + r"""
\bottomrule
\end{tabular}
\end{table*}
"""
    open(sys.argv[5], "w").write(text)
    print("wrote", sys.argv[5])


if __name__ == "__main__":
    main()
