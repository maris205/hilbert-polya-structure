# GPT-5.4 XHigh Round 1 resolution

## Provenance and status

- Review: `GPT54_XHIGH_ROUND1_HOSTILE_REVIEW.md`.
- Reviewer provenance: `gpt-5.4 xhigh`, as recorded in the review supplied by
  the coordinator.
- Baseline: `main_pre_gpt54_round1.pdf`, SHA-256
  `7bf54d3b56530decc051f56cfedc38684d432fca8c73474347d2ab33546bda7d`.
- Disposition: all three verified Round-1 items resolved.
- Official GPT-5.4 Round 2: **not yet run**.
- External release: **HOLD**.

## Fixes implemented

1. **M1 — malformed evaluation-map display: RESOLVED.**
   In `sections/1_introduction.tex`, changed
   `x_n,qquad n\in F` to `x_n,\qquad n\in F`.  The extracted PDF text no
   longer contains the leaked `qquad` token.
2. **M2 — undefined `V_r` in Table 1: RESOLVED.**
   In `sections/5_rectangles.tex`, replaced
   `sum_r(|V_r|-c_r)` by the previously defined
   `sum_r(|I_r|+|J_r|-c_r)`.
3. **M3 — malformed claims/evidence row C9: RESOLVED.**
   In `CLAIMS_EVIDENCE.md`, replaced the evidence cell `C7--C8` by
   `entropy additivity together with graphic-matroid acyclicity`, retaining
   dependencies `C7, C8` in the dependency column.

No theorem statement, proof assumption, source claim, or control algorithm
was otherwise changed.

## Verification

- Deterministic controls: `ALL CHECKS PASS`.
- Live control output equals both frozen receipts byte-for-byte.
- Stable `pdflatex -> bibtex -> pdflatex x2` build: PASS.
- Final log scan: zero undefined citations/references, rerun requests,
  multiply-defined labels, overfull boxes, underfull boxes, or badness
  warnings.
- Revised PDF: 11 A4 pages.
- `main.pdf` and `main_gpt54_round1.pdf`: byte-identical.
- Revised PDF SHA-256:
  `48c3688f29062934ceb81f0b2077555b24ea23716e5224bd28ef5af7ae84729e`.

The package is frozen for official GPT-5.4 XHigh Round 2 review.  No Round-2
verdict is claimed here.

