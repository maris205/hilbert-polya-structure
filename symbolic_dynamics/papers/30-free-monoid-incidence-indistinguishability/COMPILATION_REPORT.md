# Paper 30 compilation report

## Final deliverable

- Title: *Free-Monoid Indistinguishability at the Incidence Boundary: A No-Go for Divisibility Cumulant Selectors*
- Candidate: `SD-C32`
- PDF: `main.pdf`
- SHA-256: `8d7a170f187e3516286ee563fe610ebf3a9a906ef7b160fd52f8d4ec61825a9d`
- Size: 393862 bytes
- Extent: 15 pages, A4 (`595.276 x 841.89 pt`), PDF 1.5
- Engine: pdfTeX 1.40.22 / LaTeX2e (TeX Live 2022), BibTeX with `plainnat`
- Source lock SHA-256: `6a09c46e9c04326728cd838deb654e69529fc661cdb616e255fdb10910b5957e`

The complete build cycle was `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
After the last layout-only source edit, two further `pdflatex` passes produced
the frozen PDF.  `latexmk` was unavailable in the environment.  The final log
contains no LaTeX errors, undefined references or citations, rerun warnings,
overfull boxes, or underfull boxes.

## Manuscript inventory

- 238-word abstract and explicit research-status capsule.
- Eleven numbered sections including the two appendices.
- Ten theorem-style environments: three definitions, one lemma, three
  propositions, two theorems, and one corollary.
- Three in-source vector TikZ figures and three tables; the PDF contains no
  raster-image objects.
- Fifteen cited primary/official bibliography entries and fifteen bibliography
  keys, with no uncited entry or unresolved key.  The bibliography records
  thirteen DOI identifiers and three primary/official URL fields.

## Mechanical and visual audit

- `pdfinfo`: 15 pages, A4, unencrypted, no form, no JavaScript.
- `pdffonts`: 24 font resources, all embedded and subset Type 1; no Type 3
  font.
- `pdfimages -list`: no raster images.
- Text extraction found nonempty text on all 15 pages.
- Every page was visually inspected after rasterization at 110 dpi.  Equations,
  tables, citations, hyperlinks, headers, footers, and all three figures are
  legible and unclipped.  The final appendix reflow removes the previously
  isolated review-policy page; the closing declaration now occupies page 15
  with a normal lower margin.
- Source audit found no placeholder tokens, trailing whitespace, control
  bytes, unresolved references, or compile diagnostics.
- The source and extracted PDF both state `ROUTE_A_REJECTED` twice and lock
  Route B.  The route tuple is printed in the research-status capsule and the
  route-closure section.

## Scientific ownership audit

- The central theorem is the decorated-source isomorphism between integer
  divisibility and the transported free-commutative/UFD clone.  Its naturality
  consequence covers local and nonlocal finite-arity constructions rather
  than extrapolating from the finite audit.
- The normalized Boolean-join weight and the partition-lattice connected
  cumulant have distinct exact failure modes.  The stronger filtered
  rank-three contraction separates the named finite fixtures but is copied by
  every transported UFD clone.
- The pair-weighted mixed series is declared only as a new holomorphic scalar
  functional on `1 - 2 eta < Re(s) < 2 eta`; it is not claimed to be an
  ordinary trace, relative determinant, `det_2`, `det_3`, or another modified
  Fredholm determinant.
- The zero-diagonal matrix `H` belongs to a separate auxiliary construction.
  Its entrywise nuclear decomposition makes it trace class and licenses the
  honest ordinary determinant `det(I + zH)`, but neither that determinant nor
  exponentiation upgrades the inherited chiral object.
- No target zeros, printed integer labels, primality/factorization oracle,
  sampled ordinates, or fitting objective enters the argument.  Route B is
  locked.  A Paper 31 successor is restricted to independently motivated,
  source-derived nonmultiplicative data not transported by the valuation
  isomorphism.

The frozen route is

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,A1_FAIL,A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)
ROUTE_A_REJECTED
```

## Exact authority integration

The manuscript and source lock record the final independent authority:

- 28/28 tests pass.
- 1616/1616 evaluator checks pass.
- Two fresh runs reproduce 17 artifacts byte for byte.
- The canonical artifact ledger has 31 entries.
- Baseline subset rows: 241; finite-control subset rows: 118;
  free/UFD rows: 45; predicate-mask rows: 186; marker rows: 165.
- Integer full-five-predicate counts are `(5,10,10)`, `(7,21,35)`, and
  `(10,45,120)` at cutoffs 12, 18, and 30.
- The four finite fixtures have counts `(8,3,0)`, `(3,0,0)`, `(4,0,0)`, and
  `(5,0,0)`; the transported cutoff-30 free clone exactly reproduces
  `(10,45,120)`.
- The mutated-cover pair survivors are exactly `(2,5)`, `(2,7)`, and `(3,5)`.
- There are zero pair-separating predicate masks and 28 finite-triple
  separating masks; every such mask is cloned.

Frozen authority hashes:

```text
c9ca998826d8556c8c63c9f7c3dd029d03753bfc7366c982a2fa76ef7a0b1a1c  EXPERIMENT_REPORT.md
99be21c67f12234d5b5b6ae854bd2c6695aabebec953fa8fe217bce452045bd0  results/SHA256SUMS.txt
7eef85e74ec0785cf30b19e81aee35b1c9753ad1f51f5fca6ea65568466dea1c  results/double_run_certificate.json
48ed4bd36205888cac4b9200a93a78f78ae851ac9890f8e8d4f8eecc2bfd25b2  results/integrity_audit.json
5296832adbac5830089e75bb3711918d7ca665e031468326ae3308103aa84e35  results/evaluation.json
eccb97b47d5446b4279cce5df75de924ca3b16d401b8f1e2259edc58b86756ac  results/test_report.json
82ef019f1054ade3e3417fb3807e9663781094b077954139c6495273c508052d  results/clone_certificate.json
e27e9be1e6516a6bd009af1e6d919d91dbf20ca2a62c5c63e3d09eb75f8dcd4a  results/summary.json
b2ea8f6c6803ef5a0a01999452f7e68ed099ccb04f2e24c8592b97b5e1fef316  double-run aggregate
```

## Process boundary

No manuscript review loop was run, as requested.  Compilation, formula,
source, primary-citation, route, font, metadata, control-byte, and
full-document visual audits were retained.  Writer work did not modify the
experiment, code, results, evaluation, manifest, repository-level README,
plain mirror, or Git state.
