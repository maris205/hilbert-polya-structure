# Improvement log — P176

## Author Round 0

- PDF SHA-256:
  `5a8977524f5f7f5f654442bb3ac98cf74872de297277e9ffb0ff5c23878e69ba`.
- Standalone author/scout-derived regression control: 2,828,503 assertions,
  `RESULT PASS`.

## Hostile Review A and Round 1

Review A returned `0 Critical / 0 Major / 1 Minor` while accepting every
mathematical claim.

- `P176-A-m01` closed: README, narrative, claim ledger, and self-QA now
  identify the paper-local executable as scout-derived rather than
  implementation-independent.
- The Review-A bit-mask implementation is recorded as the independent
  cross-check; it passed 14,407,195 assertions through `n=19`.
- `main.tex` required no change.  Therefore `main_round1.pdf` is
  byte-identical to `main_round0_original.pdf`.
- The status remains `AMBER_INTERNAL_NEAR_P166 / HOLD_EXTERNAL`.

## Hostile Review B and Round 2

Review B returned `0 Critical / 0 Major / 2 Minor` and judged every theorem
`PROVABLE AS STATED`.

- `P176-B-m01` implemented: Høyer--Špalek is restricted to quantum phase
  rotation; Grošek--Hromada and Gupta et al. are added as the closer
  coordinate-rotation background, assigned zero contribution credit, and
  explicitly separated from the adaptive map.
- `P176-B-m02` implemented: the live author program, transcript, plan,
  README, claims ledger, narrative, and self-QA now consistently label the
  control author/scout-derived.  The repaired verifier and transcript hashes
  are `2dd56b882925...` and `3d0947a4df32...`.
- Review B's independent string-state/Brent/direct-component verifier passed
  19,758,014 assertions.
- The source repair produced a four-page Round-2 PDF with SHA-256
  `c13ca3f5e3673bb5dd9c01bdf7c8913f78425cdbfeb2a52e2d9b096a34122db4`.
  Two final source-only cold builds reproduce it byte for byte, and all 31
  font rows are embedded, subsetted, and Unicode mapped.
- Reviewer B rechecked both repairs, the new author transcript, Round-2 PDF,
  cold builds, source boundary, and live manifest; it marked both findings
  `CLOSED`, with zero open findings.  The lifecycle remains
  `AMBER_INTERNAL_NEAR_P166 / HOLD_EXTERNAL`.
