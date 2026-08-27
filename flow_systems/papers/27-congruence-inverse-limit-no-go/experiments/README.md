# P27 experiment status

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
