# LNR author temporal proof pressure

2026-09-06 UTC. `verify_lnr_temporal.py` is newly authored, standalone,
standard-library-only, reads no file and imports no scouting/reviewer code.
It compares the literal map with a separate run-case terminal decoder,
the exact fixed language and the all-length sharp witness family.

Two separate actual `python -B` executions exited zero. The first wrote
`LNR_TEMPORAL_CANONICAL.json`; the second wrote
`/tmp/lnr_temporal_root_run2.stdout`. Actual complete raw `cmp` exited zero.
Each computed 1,127,472 assertions on all 88,560 source states at
$3\le n\le10$, and on the sharp witness at every $4\le n\le1000$.
The canonical is the complete computed stdout with its final newline,
not an invented expected transcript. All-size conclusions rest on the
separate deductive proof, not these bounds. This is author evidence only.

Verifier SHA-256:
`1c05b9febae1a83815577dbfdc6a57e082339c3df05dac6a4317d6c4ccea4831`.
Canonical and second stdout SHA-256:
`d7c8a81e65a3fcd16527211a3e659b476cf65b5bdf8c93e6e45cdf1d7ccf1962`.
No candidate admission, inverse theorem or independent review is implied.
