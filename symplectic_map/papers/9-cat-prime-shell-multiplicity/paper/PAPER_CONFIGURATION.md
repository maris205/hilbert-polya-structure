# Paper Configuration

- Candidate: `cat_prime_shell_multiplicity_obstruction_v1`.
- Title: *A Multiplicity Audit for Prime-Torsion Euler Products of the Cat
  Map* (the independently approved safe title).
- Format: anonymous specialist mathematical note, 11 pt, single column;
  no venue, page-limit, acceptance, or priority claim is made.
- Document date: 2026-08-15 Round-1 bounded revision.
- Length: 15 pages including three appendices and 11 references.
- Build: `paper/build.sh` fixes `SOURCE_DATE_EPOCH`, `FORCE_SOURCE_DATE`,
  `TZ`, and `LC_ALL`, then uses `pdflatex -> bibtex -> pdflatex x3`.
- Revised source: `paper/manuscript.tex`, SHA-256
  `fb54cb9273c89ad5f76a9485d67a815555050b3c71e630e47d367b043ae6e26c`.
- Round-1 revision PDF: `paper/paper_round1_revision.pdf`, SHA-256
  `96a560712ae7fb34e1d0ecfcd59e9b2c210ad61fe8ee0537c3a5ff5c860b4cd6`;
  it is byte-identical to the current `paper/manuscript.pdf`.
- Independent Round-2 review: `paper/reviews/round2_review.md`, SHA-256
  `32cc795c358d979988673658398dd4dbf2768cd9f1b38464b9b438703c2ebd23`,
  verdict `PASS -- MAY FINALIZE`, score `8.5/10`, with zero Critical, Major,
  or Minor finding.
- Final PDF: `paper/paper_final.pdf`, SHA-256
  `96a560712ae7fb34e1d0ecfcd59e9b2c210ad61fe8ee0537c3a5ff5c860b4cd6`.
  It is byte-identical to the independently approved Round-1 revision PDF.
- Historical pre-review PDF: `paper/paper_pre_review.pdf`, SHA-256
  `9b63f190e7c751c27682d1a9cc9246f0153edddfec61d4539c573ab70070d51c`;
  it remains byte-unchanged.
- Bibliography: numerical `natbib`; the 11 cited keys are exactly the 11
  independently verified entries in `paper/references.bib`.
- Figures: the three frozen vector PDF masters are included in the approved
  order, with SVG and 300 dpi PNG companions retained in the asset package.
- Review state: `COMPLETE_LOCAL_FINAL_REVIEW_PASS`.  Independent Round 2
  authorized finalization; terminal finalization was mechanical and changed
  no manuscript source, scientific content, reference, figure, source lock,
  code, or result artifact.

## Scientific boundary

The note re-derives the classical split, inert, binary, and ramified shell
profiles for the standard cat map, separates raw-return from one-time
orbit-label products, and proves only a finite pure-denominator obstruction
for fixed nonzero scalar coefficients independent of the local variable.
It records the exact zero-weight boundary, equal-weight repeat failure,
fractional shell identity, selector cost, and safe convergence strips.  Its
novelty is deliberately described as a low-novelty synthesis and audit, and
direct prior-art collisions are stated in the manuscript.  No numerical
novelty score appears in the public manuscript package.

The all-prime classification and global analytic strips are proof-only.
The registered rows at `p={2,3,5,7,11}` were development-seen exact
falsification controls, not blind or all-prime evidence.  No result is made
for `2 < Re(s) <= 3`; no exact abscissa, continuation, zero statement,
prime correspondence, quantization, or priority claim is made.  Matrix,
numerator, alternating, transfer/Fredholm, cohomological, enriched-selector,
and centralizer mechanisms remain outside the scalar theorem.  The
centralizer route is reserved for later work and was not computed here.

## Frozen authorities

- Revised plan: `PAPER_PLAN.md`, SHA-256
  `41a1e6e9356c3820c3890fca232b60302673c1a28a83d8ba26f932eec5f73e3e`.
- Source lock: `experiments/source_lock.json`, SHA-256
  `662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49`.
- Proof package: `notes/PROOF_PACKAGE.md`, SHA-256
  `47216ad4021d3476bfd0850ebec24c9ceafb5af8c0573214182fd2d0da7b2daa`.
- Result manifest: `results/result_manifest.json`, SHA-256
  `8ca12744638a47b6e4fa3239a60a19d79229d2b9596ae4fe4b2f66a399618f92`.
- Independent result integrity: SHA-256
  `aa0c7db555f11920c7305be508f6cfff62375970e112e9f720111831da20b3bd`.
- Independent plan/figure/citation gate: SHA-256
  `f8c22bfba9299230a8e2051c089863bf6603ebcb84e5e42955ecbf36a874ec06`.
- Historical pre-review 24-path asset tree: SHA-256
  `312c4b095b58acb9e8047d7113308d28870e3db7633f37d17bd904ca2c7ebfaa`.
  The Round-1 revision uses the same explicit 24-path allowlist and framing,
  with revision digest
  `0526235c1b3581aba830e054d1f883fd677cb7a752180bb8a0eeb0dbab7a862e`.
  Neither value is a dynamic scan of the expanded `paper/` directory.

- Independent Round-1 review: `paper/reviews/round1_review.md`, SHA-256
  `dc34ea65a091680e3a2e0f89b15f804f45b3a7be7ae11502d82c668ec6d58ed8`.

The approved source and PDF retain any historical pre-review lifecycle
labels embedded before Round 2.  They were not edited because the final PDF
must remain byte-identical to the approved artifact.  This configuration and
the terminal manifests are authoritative for the current lifecycle state.
Two isolated clean builds reproduced the approved digest, and
`paper_final.pdf` is its exact release copy.  Terminal status:
`COMPLETE_LOCAL_FINAL_REVIEW_PASS`.
