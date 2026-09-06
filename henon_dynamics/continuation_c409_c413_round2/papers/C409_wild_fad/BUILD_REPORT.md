# Author first-build report — C409

Current author snapshot: the post-review rebuild below supersedes the
initial PDF hash, while the initial snapshot is retained for review provenance.
The non-author full review and its R1–R2 affected-passage confirmation are
now complete, with no remaining requested repair; see the final paragraph.

Status: COMPLETE MANUSCRIPT / AUTHOR INITIAL BUILD PASS / NON-AUTHOR MANUSCRIPT
REVIEW PENDING. Date: 2026-09-06.

## Artifact and scope

- Anonymous English article, 11pt, one-inch margins, Latin Modern scalable
  fonts; 11 PDF pages, including references.
- Actual main.tex, seven complete section files, seven cited and
  metadata-verified BibTeX entries, PAPER_PLAN.md and CITATION_METADATA.md.
- Complete AF, Fourier norm, conductor-grid, actual-measure, radial-limit,
  rational-alternative and realized FAD proofs are in the manuscript.
- R1 is reflected throughout: finite primes and phase set, unit-modulus
  phases, periodic nonnegative real exponents. No unspecified sign or
  infinite-prime extension is used.
- The no-wild BHN deduction is explicit, not claimed as new. The wild
  realized example and both failed sufficient hypotheses are proved.
- No frozen research input, old experiment, registry, ledger or Git state
  was altered. No old mathematical test was re-run.

## Initial build

Toolchain: pdfTeX 1.40.22 / TeX Live 2022-dev Debian; Latexmk 4.76; BibTeX 0.99d.

Command in this directory:

~~~sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex
~~~

The first attempt encountered the installed T1 Computer Modern bitmap-font
limitation with microtype font expansion. Adding the available lmodern
package fixed it without changing mathematics. A single underfull table
cell was resolved by ragged-right paragraph columns. The final local build
exited 0 and Latexmk reported all targets up to date.

Final main.log and main.blg search:

- 0 undefined citations or references;
- 0 multiply defined labels;
- 0 overfull or underfull boxes;
- 0 remaining Warning lines.

pdfinfo: 11 pages, 326636 bytes, letter page size, unencrypted, blank Author.
pdftotext extraction was inspected for section progression, equations,
theorem labels and the seven-entry bibliography. The title page was also
rendered and visually inspected at 1400-pixel height: readable mathematics,
no clipping, no author identity. This is a representative author check,
not an all-page visual certificate.

## Snapshot for independent manuscript review

- main.tex SHA-256:
  9fc2031fd6186f8f890d901175fbc7f8129775ddfabd4141869b756bb425f186
- main.pdf SHA-256:
  4590f84523255ad3aa345edcae4ae84f22c9fea5a6df602abb1d65a4f0603bbe
- references.bib SHA-256:
  f45cb625f171cabc3b862ebd5512befa6599b174fa50ea57b77709e3e110c053

There is no known unresolved author-side mathematical or LaTeX error.
The independent reviewer must assess the actual full draft, especially
the conductor orbit and post-aggregation measure, the FAD positivity/CRT
argument, the no-wild deduction, and the example's field-embedding comparison.
This author report does not substitute for that review.

The root coordinator owns formal Route-A assessment, final independent
two-directory deterministic builds, all-page visual inspection and global
registration. This initial PDF is not a deterministic-build attestation.

## Post-review rebuild — R1 and R2

The complete non-author review was read, and the actual changes are recorded
in REVISION_NOTES.md. The cited realizability propositions were separated
and the introductory conductor quantifier narrowed to supported conductors.
The empty-S periodic edge case in the same deduction was clarified.

The same Latexmk command exited 0 after these source changes. The resulting
main.log/main.blg again contain zero Warning, undefined, multiply-defined,
overfull or underfull matches. The rebuilt PDF has 11 pages and 326890 bytes.
The main preamble and bibliography did not change.

Revised snapshot:

~~~text
cd39541113b917b391dabdc37b24335f5c439b5578ca4c3456b32a059fa17c7c  main.pdf
9331b86c333f1511d17327f8a9feec1c49ae164e638c2d64ec8964406b97ffc4  sections/01_introduction.tex
c928ffb04b0ddd6c09196a091ce9d1fd19f34924583e76b519566fc54ee9e8c8  sections/05_dynamics.tex
13f5b4339bd6c6b8a0f3c94874591ce6d26159432754ebbe6812d3911550e6ff  CITATION_METADATA.md
~~~

The same non-author reviewer has now read the actual affected passages,
updated provenance and rebuilt PDF text and appended a confirmation to
../../positive_characteristic/REVIEW_C409_MANUSCRIPT.md. R1, R2 and the
empty-S clarification passed; no requested mathematical or locator repair
remains. This is targeted follow-up to the full draft review, not a second
full review. Root-coordinated final deterministic builds and all-page visual
checks remain separate gates.
