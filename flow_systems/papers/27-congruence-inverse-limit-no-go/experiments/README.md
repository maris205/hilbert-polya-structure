# P27 experiment status

## Round 4

Run `bash experiments/reproduce_round4.sh`.  It checks the 24-row frozen input,
all 21 order-divisibility transitions, the exact three order sequences, period
ratios, owner firewalls, and two byte-identical builds.  Eight tests pass and
the combined output SHA-256 is
`2fcf33ed6c458339ac808d7b7007a240b7a588b0093249a90a35559f1ef2aa22`.

The finite rows illustrate the proved group-theoretic closing-time escape
theorem for whole traversals of a selected `g`-loop; they are not used to infer
asymptotic divergence, primitive minimal periods, or inverse-limit periodic-
orbit credit.

## Round 2

Round-2 finite-level diagnostics are complete.  Run:

```bash
bash experiments/reproduce.sh
```

The entry point performs two complete generations, verifies each manifest,
runs five unit tests, and demands byte identity for the CSV, metrics JSON,
experiment receipt, and manifest.  Current receipt:

```text
ROWS=24
ELEMENTS=3
LEVELS=8/8
ORDER_CROSSCHECKS=24/24
UNIT_TESTS=5/5
TWO_RUN_BYTE_IDENTITY=4/4
STATUS=PASS
```

See `round2_reproducibility_receipt.md` for hashes and the owner boundary.  The
trivial-product and cocompact-tower structural controls remain `[OPEN]`; the
executed finite quotient table is not one of those theorem-level controls.
