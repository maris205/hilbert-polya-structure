# HCS-C51 exact code lane

This directory implements the fail-closed certificate for the Hénon
`mu_3` weight/clock bifurcation.

The producer source-locks C47--C50, replays all eleven common split-prime
moment controls, recomputes the rank identities for `2 <= n <= 20`, builds
the exact denominator-clock center spectrum for `1 <= j <= 4`, checks Tate
relabel invariance, and reconstructs the `n=4` Hodge ledger.

The checker is independent of the producer: in particular, it recomputes
the Chern coefficients by direct binomial/generating-function sums rather
than by the producer's truncated series division. It independently derives
the `n=4` `chi_y` polynomial by an exact Hirzebruch--Riemann--Roch power-series
expansion and interpolation. It also locks the full recursive payload shape
and exact leaf types.

Run the frozen pre-release closure with:

```bash
./code/run_c51.sh
```

Refresh code/results artifacts only after the producer, checker, all
mutation tests, and a staged manifest have succeeded:

```bash
./code/run_c51.sh --refresh-results --refresh-manifest
```

The release manifest covers the complete project: root research documents,
both Route-A copies, all paper sources, the clean PDF and compilation report,
code, results, and the integrity report. Unknown persistent files, missing
required files, or digest changes fail closed.

The three refreshed result artifacts are promoted as a rollback-safe group.
Injected failures after the second and third move are covered by isolated
tests and leave all old targets byte-identical.
