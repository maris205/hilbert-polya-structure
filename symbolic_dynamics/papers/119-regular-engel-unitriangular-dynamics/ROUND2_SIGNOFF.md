# P119 independent round-two signoff

**Role and scope.** I acted as a non-author round-two reviewer and checked
only the four repairs required by Hostile Review B, together with the frozen
verifier/PDF consistency needed to sign them off. I inspected `main.tex`,
`HOSTILE_REVIEW_B.md`, the verifier and canonical transcript,
`main.pdf`, and `main_round2.pdf`. I made no change to the manuscript,
bibliography, verifier, canonical artifacts, or PDFs. This signoff file is
the only added deliverable.

**Verdict: GO_INTERNAL; EXTERNAL HOLD.** All four required repairs are
resolved, and I found no new blocker within this narrow review scope.
Ownership, novelty, priority, specialist clearance, external circulation,
and submission remain on hold.

## Four-item repair audit

| Required B repair | Settled evidence | Resolution |
|---|---|---|
| Restrict the abstract fibre target to `Y in gamma_(k+1)` | The abstract now says that every target **in** `gamma_(k+1)` has exactly `q^(n-k)` predecessors in `gamma_k`. This agrees with Theorem 3.1, which separately assigns fibre size zero outside `gamma_(k+1)`. | RESOLVED |
| Qualify the abstract deepest-layer formula by `n>=2` | The abstract introduces the sharp height `n-1` and deepest-layer cardinality `(q-1)q^(binom(n,2)-1)` only after the explicit phrase “For `n>=2`.” The `n=1` singleton convention remains separately handled in Remark 2.1. | RESOLVED |
| Point to the proof of Bier's Theorem 1 | The introduction cites “Lemma 1 and the **proof of Theorem 1**” for the same convention, fixed regular `J`, restricted images, and iterated fixed-`J` images. The proof of Theorem 5.1 again attributes its image equality to the fixed-`J` construction “in the **proof of** Bier's Theorem 1,” or equivalently to iteration of Bier's restricted lemma. | RESOLVED |
| Keep Table 1 after Theorem 5.1 and its proof | In source, Theorem 5.1 occupies lines 342--381, its proof lines 383--408, and the table begins at line 410 with `[H]`. In the settled PDF, page 4 renders the complete theorem and proof first; Table 1 follows beneath the proof and before the explanatory row-sum paragraph. | RESOLVED |

## Exact-control and freeze evidence

Fresh command:

    PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py

Result: **PASS, 1,491,877 exact assertion executions**. Fresh stdout is
9 lines and 287 bytes and is byte-identical to
`code/verification_output.txt`; both have SHA-256
`d0a1247b6ac4848c56a8302da1b05300ff9c88db5856af347f88dde15047b267`.
The verifier also rebuilt and byte-checked the 43-row layer artifact.

I performed an isolated four-stage build from copies of only `main.tex` and
`references.bib` using `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`. Every
stage exited zero. The isolated PDF, current `main.pdf`, and
`main_round2.pdf` are byte-identical, with SHA-256
`8c18a551eead42c7dff56eef121a7cb3f1778c15c1e0c0d5dda1eeec326bebdc`.
The settled PDF is 6 A4 pages and 410,005 bytes; the settled log and BLG have
no errors, unresolved citations or references, box warnings, or rerun
request. All 32 font rows are embedded, subsetted, and Unicode mapped; Author
and Title metadata are empty, with no form, JavaScript, or encryption.

All six pages were rendered and inspected. In particular, page 4 confirms
that Table 1 no longer floats above the theorem defining `L_(k,t)`: it is
visibly below Theorem 5.1 and the proof-ending square. The table is complete
and legible, with no clipping, collision, missing glyph, or split caption.

## Final status

The four Hostile Review B repair gates are **RESOLVED**. P119 is signed off
as **GO_INTERNAL**. External ownership/novelty/priority assessment,
specialist clearance, circulation, and submission remain **HOLD**.
