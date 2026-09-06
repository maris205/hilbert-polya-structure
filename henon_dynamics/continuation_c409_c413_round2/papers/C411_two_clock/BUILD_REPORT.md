# Author first-build report — C411

Status: COMPLETE MANUSCRIPT / AUTHOR INITIAL BUILD PASS / NON-AUTHOR MANUSCRIPT
REVIEW PENDING. Date: 2026-09-06.

## Artifact and scope

- Anonymous English article, 11pt, one-inch margins, scalable Latin Modern;
  11 PDF pages including bibliography.
- main.tex, seven actual section files, seven cited metadata-verified BibTeX
  entries, PAPER_PLAN.md and CITATION_METADATA.md are present.
- Complete proofs cover both exact open convergence domains, bounded
  primitive-ray exponents, local normal meromorphic tails, the full actual
  polar divisor, nonzero slice residues, dense positive atomic slices,
  regularized-tail-envelope propagation, and the dependent threshold/pole
  split through every bidisc face and corner.
- R3 is explicit in the theorem, proof and concluding example: initial
  absolute-convergence domain is distinct from the terminal joint
  meromorphic domain D² and its boundary. Not every curved convergence
  boundary point is called singular; not every individual slice is asserted
  to have a natural boundary.
- The example at (i/sqrt(2), i/sqrt(2)) is a direct illustration of the proved
  a=b=2 polar divisor, with its short exact verification in the text. It is
  not a new experiment or a separate result.
- Frozen mathematical inputs and their prior checks remain unchanged. No
  old 784-kernel, 24624-coefficient or four-pole diagnostic was rerun.

## Initial build and checks

Toolchain: pdfTeX 1.40.22 / TeX Live 2022-dev Debian; Latexmk 4.76; BibTeX 0.99d.

Command in this directory:

~~~sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex
~~~

The first complete build succeeded, with normal BibTeX/cross-reference passes;
Latexmk exited 0 and reported all targets up to date.
Final main.log/main.blg contain:

- 0 undefined citations or references;
- 0 multiply defined labels;
- 0 overfull or underfull boxes;
- 0 remaining Warning lines.

pdfinfo: 11 pages, 318522 bytes, letter page size, unencrypted, blank Author.
The extracted text was inspected for theorem layout, proof sequence,
cross-references and the seven bibliography entries.
The title page was rendered at 1400-pixel height and visually inspected:
readable equations, no clipping or author identity. This is a representative
author inspection only, not all-page visual certification.

## Snapshot for independent manuscript review

- main.tex SHA-256:
  c8da445d09c3b9cae43650b7668c7a00f984b9f269fa030249b3638b5f751b8c
- main.pdf SHA-256:
  296c459bb6e3ef2029fe3128617fd81674f4ead1d1e998fb144bae4e1a31f8d8
- references.bib SHA-256:
  2d00c9175cf75d7d9c3344cfd6520b5dddf39408c2e0c3f6c0b695c2cd31b8d3

No known unresolved author-side mathematical or LaTeX error remains.
Non-author review should especially check the two-exponent CZ quantifier,
the axis/interior distinction, genuine polar components and slice residues,
the regularized tail envelopes, and the dependent 1/b threshold argument.

Formal Route-A evaluation, final independent two-directory deterministic
builds, all-page visual review and global state remain the root coordinator's
responsibility. This first-build receipt does not certify those later gates.
