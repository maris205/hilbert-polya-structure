# P203 Round0 author verifier replays

Date: 2026-09-05 UTC. **AUTHOR_PASS / MANUSCRIPT_REVIEWS_PENDING / HOLD_EXTERNAL**.
These are two physical fresh processes, not independent reviews.

## Code and command

From the workspace root:

```sh
python -B papers/203-monochromatic-triangle-complementation/verify_p203.py
```

Unchanged paper-local code SHA-256:
`77e7be9b6dc57a156010c6543ff41415415f833119e5a7116ffcef53cc5e1d7d`.
This script is physically present and needs no upstream file. Its engine
comes from the authentic final author candidate program, not the missing
intermediate version or either independent gate program.

## Replay 1

New process launch receipt b7441f, session98831; completion receipt7456f6,
exit0. Complete stdout reports 374,812 assertions and
`PASS_AUTHOR_BOUNDED_CHECKS / ALL_N_THEOREMS_REQUIRE_PROOFS`.

## Replay 2

Different new process launch receipt a5196c, session49551; completion
receipt6d26da, exit0. It reports the same assertions and PASS footer.
No code edit occurred between these processes.

## Byte comparison

Both full stdout strings were retained by the orchestration layer and
directly compared; equality returned true. They are byte-identical ASCII.
CANONICAL.txt preserves that output with its final newline. Its SHA-256 is
`6a672bcfa97f09c1575aa89bb4e2ca52aa8284315706ec90abbd6d35995dbf00`.

Each run enumerates all 33,868 states across n=0,…,6. Pair masks and a
dense adjacency-matrix literal control agree. Direct orbit paths test
periods, entrance time, anchor stabilization and every strict no-return
step. Actual predecessor sets are compared with both inverse-flip/prefix
and target-only D/C parsers. Recurrent iff, empty and fixed self-fibres,
every star/K4 certificate and every maximum target are checked. Formula
witnesses are checked within the same n≤6 cap. No larger complete carrier
or finite-to-all-n inference is used.
