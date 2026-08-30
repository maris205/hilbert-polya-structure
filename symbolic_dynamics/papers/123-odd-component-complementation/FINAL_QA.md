# Final QA — P123

Status: **PASS / GO_INTERNAL / EXTERNAL HOLD**.

- Review A: 0 critical, 0 major, 2 minor; repaired in round one.
- Review B: 0 critical, 0 major, 3 support minors; repaired in round two.
- Canonical verifier: PASS, **203,244 assertions**; fresh stdout is
  byte-identical to `code/verify_odd_component_complementation.out`.
- Review-side controls: 101,604 pointwise assertions in Review A; random
  graphs through order ten, witness depth through order fourteen, and EGF
  coefficients through order twelve in Review B; all PASS.
- Isolated four-stage build: PASS `0/0/0/0`; settled warnings, undefined
  references/citations, boxes, and rerun requests: zero.
- Current `main.pdf`, `main_round1.pdf`, and support-only
  `main_round2.pdf`: byte-identical, **4 A4 pages, 281,582 bytes**, SHA-256
  `6c78410d7689a7e5f057413ef5256a26885a86a2b9653e3b2581ede30b46c9c1`.
- The original round-zero PDF remains preserved at SHA-256
  `e7a5138e142ef89402668e4eca4e86ea804672b080bfdcce3fe33f7fa074f68d`.
- Bibliography: 8/8 cited entries resolved; all fonts embedded/subsetted with
  Unicode maps; anonymous metadata; no form, JavaScript, encryption, or
  embedded file.
- Every page was independently raster-inspected in both reviews.
- Owner risk remains medium-high and only bounded. External release, novelty,
  priority, and submission remain HOLD.
