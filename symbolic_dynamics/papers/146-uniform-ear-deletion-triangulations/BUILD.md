# Initial build record — P146

- Engine: pdfTeX 1.40.22 / LaTeX2e 2021-11-15.
- Sequence: `pdflatex -> bibtex -> pdflatex -> pdflatex`.
- Result: success, 3 A4 pages, 293,034 bytes.
- Bibliography: 3/3 entries cited and resolved.
- References/citations: no unresolved entries after settling.
- Bad boxes: none.
- PDF: version 1.5, unencrypted, identifying author metadata blank.
- Exact control: 6,609 assertions over all 68,185 histories through `n=9`, all passed.
- Round-0 SHA-256: `60d29efdca38b64fe8721a0e6d20fe9996b3da24f3d2e397628f64fc702595ca`.
- External status: `HOLD_EXTERNAL`.

## Repaired round-1 build

- Review input: HOSTILE_REVIEW_A.md, verdict REVISE.
- Result: success, 3 A4 pages, 344,336 bytes.
- Current and main_round1 SHA-256:
  `c84500da478cec5b6b29dd1542b865b711bdd7da83887412574984495c41029d`.
- Round-0 remains immutable at its original hash and visibly contains the two
  equation-source corruption defects documented by review A.
- Bibliography: 3/3 entries cited; both journal DOIs and arXiv:1311.1955 are
  printed in the PDF.
- Exact control: 9,562 assertions, canonical stdout comparison pass.
- Settled citations/references and bad boxes: zero warnings.
- Fonts: all embedded.
- Reproducibility: volatile PDF dates/trailer IDs suppressed; two fresh clean
  builds are byte-identical, and the isolated PDF equals current main.pdf.
- Visual check: corrected equation (6) and the induction inequality on page 2
  render without the former literal word or comma defect.

## Accepted round-2 build

- Hostile review B: `ACCEPT`, with 0 critical, 0 major, and 2 nonblocking
  minor findings; both minors were closed before freeze.
- Printed bibliography: 4/4 cited entries, including the explicitly
  different-carrier Coronado--Pons--Riera analogue.
- Result: 3 A4 pages, 345,511 bytes.
- Current and `main_round2.pdf` SHA-256:
  `a0a6145009b4882150489b43fe403a3d76be02725621afa358d678fb3cd02517`.
- Canonical exact control remains 9,562 assertions with byte-identical stdout.
- Source-only isolated build in `/tmp/p146-round2-3o0USX` is byte-identical to
  current `main.pdf`.
- Final log has no unresolved citations/references, bad boxes, or rerun
  request; the reproducible pdfTeX font-expansion ordering notice is harmless.
- All font rows are embedded, subsetted, and Unicode-mapped; all three pages
  were rerasterized and visually accepted after the citation addition.
- External status remains `HOLD_EXTERNAL`.
