# P25 pipeline state

Date: **2026-08-27**

| Item | Status |
|---|---|
| ARS Stage 1 | **IN PROGRESS** |
| Continuous-time object | **FROZEN** — equilateral three-disk exterior billiard |
| No-eclipse condition | **`[PROVED]`** for `d=6a` |
| Clock / primitive / repetition | **FROZEN** — flight length / cyclic primitive word / traversal powers |
| Exact versus semiclassical surface | **SEPARATED** |
| A0 arithmetic source | **`[MODELING_CHOICE] ABSENT_BY_CONSTRUCTION`** |
| Symbolic cutoff | **PROVED** — all 747 oriented primitive cyclic words through length 12 |
| Actual orbit solutions | **NUMERICALLY_CERTIFIED** — 2,241/2,241 rows pass two-solver, reflection, visibility, and length checks |
| Center-polygon proxy | **MODELING_CHOICE** — retained separately and never called an orbit |
| Stability half-density | **NUMERICAL_OBSERVATION** — 80-digit analytic monodromy with binary64 trace cross-check on 2,241 rows; independent finite-difference cross-check certified for 9 and open for 2,232 |
| Half-density kill control | **EXECUTED** — 747 complete neighboring-parameter triplets plus shuffled/random/composite controls |
| `PROVES_TOO_MUCH` verdict | **`[STOP_SCOPED]`** for half-density persistence as arithmetic evidence |
| Proposal stage | Stage 1 / A0--A1 negative control |
| Formal Route-A tuple | UNASSIGNED |
| Route-B evaluation | NOT RUN |
| Route-B invocation allowed | `false` |
| Manuscript | NOT STARTED |

The A0-source absence is fixed by the control design.  It is not an inference
from the separate half-density experiment.  The Round-2 control now shows that
the chosen half-density structure persists almost unchanged under neighboring
non-arithmetic geometries, so that statistic is stopped as arithmetic evidence.
The next gate is either a different source-derived observable with an explicit
arithmetic owner or closure of the 2,232 open finite-difference stability
cross-checks for a purely dynamical calibration; neither authorizes A2.

Evidence tokens are limited to the vocabulary in
`skills/route-a-evaluator.md`; `UNASSIGNED` is a pipeline state.
