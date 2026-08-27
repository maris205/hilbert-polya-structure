# P25 experiment status — Round 2 complete

The internally prespecified grid `d/a in {5.8,6.0,6.2}` and topological word
length `<=12` has been executed.  The exact symbolic cutoff contains 747
oriented primitive classes; all 2,241 geometry rows passed the actual-orbit
residual contract.  The reproducibility receipt and full validation report are
`round2_receipt.json` and `round2_validation.md`.

Executed controls include:

- neighboring geometry with identical word/cutoff schema;
- period shuffle within fixed topological length;
- SHA-256 deterministic random phase and random stability;
- rank-integer, guaranteed-composite, and deterministic random-integer labels;
- explicit comparison of physical flight length with the center-polygon proxy.

No prime or Riemann-zero table participates.  The two neighboring log
half-density correlations are `0.999998520` and `0.999998755`, above the frozen
`0.98` stop threshold.  The statistic-level result is therefore
`[NUMERICAL_OBSERVATION]` and `[STOP_SCOPED] / PROVES_TOO_MUCH` for arithmetic
interpretation.  The formal Route-A tuple remains unassigned.
