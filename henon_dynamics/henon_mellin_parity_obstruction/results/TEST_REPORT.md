# HCS-C36 test report

- Independent checker gates: **9/9 PASS**.
- Mutation and determinism tests: **25/25 PASS**.
- Arithmetic engine: `python-flint==0.9.0`, Arb precision set to 80 decimal
  digits with four guard bits.
- Producer/checker independence: the checker does not import producer code
  and separately reconstructs every registered complex enclosure.
- Parser policy: unknown keys, type confusion, noncanonical fractions, and
  duplicate JSON keys are rejected fail-closed.
- Freeze policy: `run_c36.sh` rebuilds into a temporary directory, compares
  byte-for-byte with checked-in results, and verifies every tracked project
  artifact against `ARTIFACT_HASHES.sha256`.

The exact test transcript is reproducible with:

```bash
./code/run_c36.sh
```
