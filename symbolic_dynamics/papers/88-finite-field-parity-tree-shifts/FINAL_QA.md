# Final QA — Two-Round Hostile Audit

Release audit date: 2026-08-28 UTC.

## Result

- Decision: **GO; INTERNAL FREEZE; EXTERNAL HOLD**
- Hostile rounds: 2 completed; both pass after bounded repairs
- Exact control: `ALL EXACT CONTROLS PASSED`
- Control ledger: 8,315 blocks, 811 exhaustive proper subsets, 567 rank
  observation certificates, 19,764 assertions
- Build: explicit `pdflatex / bibtex / pdflatex / pdflatex` completed
- PDF: `main.pdf`, 7 pages, 370,404 bytes, A4, PDF 1.5
- Undefined references/citations: 0/0
- LaTeX, package, BibTeX, and pdfTeX warnings: 0
- Overfull/underfull boxes: 0/0
- Fonts: 28/28 embedded, subsetted, and Unicode-mapped
- Drafting/verification markers: 0
- Bibliography: 9 cited keys and exactly 9 entries
- Anonymity: author is `Anonymous`; PDF author metadata is empty; no
  affiliations, grants, acknowledgements, or repository identity
- Visual inspection: all seven rendered pages checked after the final
  layout repair; no clipping, collisions, broken tables, displaced equation
  tags, missing glyphs, or orphaned bibliography page
- PDF SHA-256:
  `bf484b89fc3a319c2b00afa2d0b2b3789edaae83a584b54e006b2db09c808aa2`

## Mathematical release checks

- The finite-height block set is defined as restrictions of infinite legal
  trees, and the boundary-surjectivity proof explicitly extends every finite
  block to infinite depth.
- The terminal bijection and the independent constraint-rank calculation
  both give dimension `d^h`.
- The boundary and site formulas are quantified for `h >= 0`; the
  double-log formula is correctly restricted to `h >= 1`.
- Projective compatibility uses an exact constant fiber count, not an
  informal boundary limit.
- Shift invariance is proved at every rooted subtree through uniform
  terminal marginals.
- The joint-offspring formula is quantified for `h >= 1`, and its root-only
  `h=0` case is stated separately.
- The affine-hyperplane kernel is normalized, and its product gives exactly
  the uniform cylinder mass.
- The iid-ray theorem has both a block-kernel proof and an independent
  full-rank linear-form derivation in the hostile audit.
- Every proper boundary coordinate subset misses a nonzero root coefficient,
  giving exact independence; the full boundary gives pointwise
  reconstruction.
- The failure modes at `d=1` and at a zero coefficient are stated and now
  checked by explicit negative controls.
- All-prime-power scope is algebraic. The new exhaustive `F_4` lane is a
  regression fixture, not a substitute for the proof.

## Control and reproducibility checks

- The control program compiles with `python3 -m py_compile` and uses only
  the Python standard library.
- Prime-field enumeration, independent modular-rank checks, and the
  separately implemented `F_4` enumeration all pass.
- The `F_4` lane validates its arithmetic tables before using them as an
  oracle and then exhausts all 256 terminal assignments at `d=2`, `h=2`.
- No random seed, network service, floating-point tolerance, or unstated
  external dataset enters the result.
- Recorded output in `CONTROL_RESULTS.md` matches the final run exactly.
- The four-stage build is deterministic under the manuscript's suppressed
  PDF dates and trailer ID; the final package checksum file validates every
  listed artifact.

## Ownership and overstatement checks

- Tree SFTs are assigned to Aubrun–Béal; SNRE and double-log entropy to
  Ban–Chang; site-normalized entropy to Petersen–Salama.
- Tree-indexed Markov chains are assigned to Benjamini–Peres; binary joint
  sibling kernels to Guyon; block Markov chains to Souissi.
- Tree broadcasting/root reconstruction is assigned to
  Evans–Kenyon–Peres–Schulman.
- Perfect threshold secret sharing is assigned independently to Blakley and
  Shamir. The title and theorem scope now say coordinate-deletion
  reconstruction and make no claim to invent the access structure or
  additive mechanism.
- The P49 and P77 internal firewalls remain explicit, and a bounded P01–P87
  source scan found no exact internal theorem collision.
- The negative literature statement is explicitly bounded by date and does
  not establish absolute priority.

## Page audit

- Page 1: title, abstract, metadata, and opening ownership discussion clear.
- Page 2: theorem summary, control scope, internal firewall, and setup clear.
- Page 3: boundary theorem, proof, recurrence, and normalization start clear.
- Page 4: normalization table/theorem and projective law clear.
- Page 5: kernel, iid-ray result, secret-sharing subtraction, and threshold
  theorem start clear.
- Page 6: threshold theorem completes before the fixed owner table; formula
  tags (19)–(21) are correctly aligned.
- Page 7: scope, controls, conclusion, and all nine references fit cleanly.

Public posting, submission, venue selection, author contact, and absolute
priority language remain unauthorized and **HOLD**.
