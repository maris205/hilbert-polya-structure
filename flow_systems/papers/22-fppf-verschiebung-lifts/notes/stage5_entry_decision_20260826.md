# Paper 22 Stage-5 entry decision

Date: **2026-08-26**  
Pipeline transition: **Stage 4.5 exact PASS -> Stage 5 FINALIZE**  
State after this decision: **Stage 5 in progress**

## Scholar decision

Exact user instruction:

> 确认进入 Stage 5，引用格式保持当前 plainnat 数字制。

This satisfies the mandatory Stage-5 entry gate and records the finalization
citation-style decision.

## Frozen citation profile

The accepted LaTeX source is to retain both of the following declarations
without conversion:

```latex
\usepackage[numbers,sort&compress]{natbib}
\bibliographystyle{plainnat}
```

The resulting style is the manuscript's existing generic mathematical numeric
style.  It must not be relabelled as IEEE or Vancouver compliance.

## Output and scope contract

- Authoritative manuscript formats follow the confirmed Stage-2 Paper
  Configuration Record: LaTeX, BibTeX, a PDF compiled from LaTeX, and Markdown
  audit sidecars.
- Stage 5 is format-only.  The scientific text, claims, citations, author
  declarations, and Route A/Route B classifications are frozen to the exact
  Stage-4.5 accepted bytes.
- The final PDF is compiled only after the in-stage content confirmation.
- DOCX is not a configured authoritative output.  A Pandoc-derived DOCX may be
  emitted only if it passes the same content-preservation gate; otherwise it is
  withheld rather than presented as an equivalent manuscript.
- This decision does not authorize submission, public release, Git action,
  source-author contact, venue-readiness claims, or Route advancement.

## Pending in-stage decision

The scholar must confirm that the byte-locked content proof is correct before
the final PDF and completed Stage-5 package are emitted.
