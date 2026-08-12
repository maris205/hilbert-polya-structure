# Compilation Report

## Final Round 2 checkpoint

- Status: **SUCCESS**
- Compiler: pdfTeX 3.141592653-2.6-1.40.22
- Build method:

  ```bash
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  bibtex main
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  ```

- Current PDF: `main.pdf`
- Preserved final revision: `main_round2.pdf`, byte-identical to `main.pdf`
- Pages: **10 total**
  - main body through Conclusion: **8 pages**
  - references and appendices: **2 pages**
- PDF size: **468,462 bytes**
- Round 2/final SHA-256:
  `a94598cb697d92bccca30b6e215ba23e3d02f5559fe94b1ad89964b4e2b85d8a`
- Round 1 SHA-256:
  `114783478bcd49700ee7b8dbf60c4495ade3d1f5d779c8eede5dbf2780494293`
- Round 0 SHA-256:
  `599ea7b30a5292e2bbc8a88a568948165537c7ce09056c65e64449c4fe3ad227`
- The three review checkpoints are pairwise distinct: **YES**
- Undefined references: **0**
- Undefined citations: **0**
- LaTeX warnings: **0**
- Overfull boxes: **0**
- Underfull boxes: **0**
- Fonts embedded and subset: **YES** for every font reported by `pdffonts`
- PDF metadata author: **Anonymous Authors**
- PDF encrypted: **NO**
- Page size: **A4**
- Heeren working-paper identifier visible in final bibliography:
  **SSRN 6015434 / DOI 10.2139/ssrn.6015434**

## Mathematical and scope verification

- the wheel recurrence, residue graph, prime-enumeration proof, grading, and
  exact clocks are self-contained;
- the direct-image decoder--fiber criterion needs no topology or locality;
- the closure theorem uses continuity plus explicit lag-pair diagonal
  separation and does not rely on sequences or metrizability;
- the real $q$ and $\log q$ lag-pair sets are locally finite, closed, and
  disjoint from the diagonal;
- the compact-target proposition is separated from periodicity and uses only
  compactness plus decoder continuity;
- clock erasure, discontinuous boundary labels, and clock compactification
  are retained as sharp controls, not arithmetic candidates;
- ordinary positive suspension roofs are explicitly outside the obstruction;
- no candidate ID or determinant is defined, and Route B remains locked.

## Improvement state

Two independent review rounds are complete.  Round 1 returned **6/10,
Revise** and prompted the claim-calibration and hierarchy corrections listed
in `PAPER_IMPROVEMENT_LOG.md`.  Round 2 rechecked the theorem chain and
returned **8/10, Weak Accept**, with no remaining Critical or Major issue.
