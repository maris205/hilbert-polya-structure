# P25 experiment status — Rounds 2 through 7 complete

## Round 7

`./experiments/reproduce_round7.sh` runs twelve tests, builds two independent
artifact trees, requires byte identity, and verifies the checked-in outputs.
The finite exact replay has 84 trace/count rows and 182 coefficient rows with
zero mismatches.  Core SHA-256 is
`9c3daaa1feffa23090cc4edf5c3cdf0398389f814ef4f0f6b14cad254f23d4d9`.
The default mode is read-only verification; `--refresh` is explicit.  No
physical, prime, zero, or resonance data are consumed.

## Round 6

`./experiments/reproduce_round6.sh` runs ten tests, builds two independent
artifact trees, requires byte identity, and verifies the checked-in results.
Core SHA-256 is
`003321db003a71ae2713400e553701ad75db26c22655cff99cbbb25bcf2d1f77`.
The exact replay has 747 owners and zero mismatches among all three coefficient
paths.  Its tuple belongs only to the unit-roof symbolic suspension; the
physical flow remains unassigned and Route B remains closed.

## Round 4

`./experiments/reproduce_round4.sh` runs eight independent tests and two
byte-identical builds of the conditioning audit.  It records 2,202 direct-Newton
rows and 39 stationarity-fallback rows, with a combined artifact SHA-256 of
`85566062639b3e42efb4ae47816be5a967e8948233727fc1d0ef24bdeb432265`.
The audit is post-hoc and descriptive; it generates no new orbit or target data
and makes no unbiasedness claim.

## Round 5

`./experiments/reproduce_round5.sh` runs ten theorem/ledger tests, builds the
three Round-5 artifacts twice, requires byte identity, compares them with the
committed results, and refreshes `round5_reproducibility_receipt.json`.  It does
not rerun orbit solving or read target data.

## Rounds 2 and 3

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

Round 3 executes a separate 100-digit, multiscale direct return-map validation.
It expands the independent stability subset from 9 to 2,241 rows and leaves 0
open rows at the frozen cutoff.  The exact replay artifacts are
`round3_receipt.json` and `round3_validation.md`.  This numerical closure does
not change the `STOP_SCOPED / PROVES_TOO_MUCH` arithmetic interpretation or
authorize A2/Route B.
