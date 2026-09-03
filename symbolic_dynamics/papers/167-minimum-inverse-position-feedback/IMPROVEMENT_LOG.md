# P167 improvement log

## Review A repair

Hostile Review A returned `0 Critical / 0 Major / 1 Minor`.

- Corrected the Flajolet--Odlyzko Springer chapter publication year from
  1989 to 1990.  The proceedings title remains *EUROCRYPT '89*, and the
  stable BibTeX key remains `FlajoletOdlyzko1989`.
- Added an explicit conference-year/publication-year note to
  `SOURCE_VERIFICATION.md`.
- Replaced the visible author-round label in the live manuscript by the
  round-independent phrase “anonymous internal manuscript”; the preserved
  `main_round0_original.pdf` remains the exact author freeze.

No theorem, proof, formula, verifier, claim ceiling, ownership decision, or
external lifecycle status changed.  The repaired source is the input to
Hostile Review B and remains `HOLD_EXTERNAL`.

## Review B closeout

Hostile Review B returned `0 Critical / 0 Major / 1 Minor` and independently
classified every theorem as `PROVABLE AS STATED`.  Its separate verifier
made 1,670,407 exact assertions and its two fresh executions were
byte-identical.

The sole finding was a packaging mismatch: historical Round-0 prose and the
old paper-local checksum manifest still described the mutable `main.pdf` as
the author artifact.  The closeout therefore:

- labels `main_round0_original.pdf` as the immutable author freeze;
- freezes the repaired PDF as `main_round1.pdf`, `main_round2.pdf`, and the
  live `main.pdf` under the repaired hash;
- updates `README.md`, `SELF_QA.md`, and `BUILD.md` to distinguish historical
  and live artifacts; and
- regenerates `SHA256SUMS` only after the complete dual-review package is
  frozen.

This is documentation and integrity packaging only.  No manuscript source,
theorem, proof, formula, verifier, ownership conclusion, or lifecycle status
changed in response to Review B.  External status remains `HOLD_EXTERNAL`.
