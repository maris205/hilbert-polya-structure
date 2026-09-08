# AY8 single-diagnostic execution receipt

2026-09-08 UTC. The [protocol](DIAGNOSTIC_PROTOCOL.md) and
[implementation](diagnostic.py) were written before execution.

Actual mathematical executions: **1**. Command from repository root:

```text
python3 henon_dynamics/research_c419_c423/continuation_round8/adler_yamilov/diagnostic.py
```

The process returned exit status $0$, without timeout or memory failure.
The script imposed 60-second CPU and 256-MiB address-space limits through
`resource.setrlimit`; no actual peak-memory measurement or independent
timing claim is made. All twelve frozen parameter inputs completed.
There was no repair execution, rerun, parameter extension, old-program
invocation or period cutoff.

## Exact stdout summary

The positive and negative signs of each listed parameter had identical
counts in the actual output. The table retains both inputs explicitly.
Counts are directed cycles, not numbers of periodic states.

| Parameters $k$ | $C_k$ | Ordinary box vertices, each sign | Retained edges, each sign | Cycles by least native period, each sign |
| --- | ---: | ---: | ---: | --- |
| $-1,1$ | 4 | 6241 | 1167 | $1:1,\ 3:4,\ 6:2$ |
| $-2,2$ | 4 | 6241 | 1059 | $1:1,\ 3:4,\ 6:2$ |
| $-3,3$ | 4 | 6241 | 909 | $1:1,\ 3:8,\ 6:4$ |
| $-4,4$ | 5 | 14161 | 1491 | $1:1,\ 3:4,\ 6:2,\ 8:2$ |
| $-5,5$ | 6 | 27889 | 2223 | $1:1,\ 3:8,\ 6:4$ |
| $-6,6$ | 7 | 49729 | 3733 | $1:1,\ 3:4,\ 6:2$ |

For example, the actual emitted nonzero witness at $k=2$ was
$$
(-3,0,2,1),\ (-1,1,-3,-1),\ (-2,-1,-1,0),
$$
$$
(3,0,-2,-1),\ (1,-1,3,1),\ (2,1,1,0).
$$
The [proof package](PROOF_PACKAGE.md) hand-replays its whole-parameter
six-cycle extension, including $k=\pm1$, and a separate $k=4$
eight-cycle control. The latter was derived by hand after the program
reported an eight-cycle count; the program was not rerun to extract it.

## Interpretation

The proposed origin-only rigidity is false. The counts by themselves do
not prove a structural atlas beyond the twelve fixed parameters, and
they have not received independent computational certification. The
global period-bound proof uses no diagnostic count. It closes neither
the all-parameter integral family decomposition nor the remaining
period possibilities. No mathematical execution allowance remains in
this AY eighth-pass lane.
