# Claims and evidence — P105

| Claim | Infinite-family proof | Independent deterministic control |
|---|---|---|
| exact `t`-step normal form | induction on the surviving cyclic word of each original cycle | predecessor/successor surgery compared at every time with direct deletion of successive cycle minima for all permutations through `S_9` |
| cycle-type evolution | each original length `ell` contributes `min(t,ell-1)` new singletons and one part `max(ell-t,1)` | complete cycle-type comparison along every registered orbit |
| absorption time `L(pi)-1` | independent cycles finish after `ell-1` steps | all 409,113 registered permutations followed to the identity |
| unique recurrence, fixed counts, and zeta | the number of fixed labels strictly increases away from the identity | every iterate-fixed predicate through time `n+1`; exact Möbius and formal-zeta reconstruction through period 60 |
| exact depth layers | cumulative depth is the classical restriction `L(pi)<=t+1`; adjacent subtraction | literal depth histograms through `S_9` |
| restricted-cycle EGF | labelled exponential formula, explicitly owner-subtracted | independent cycle-containing-1 recurrence through `n=50` |
| sharp deepest and penultimate layers | direct `n`-cycle and `(n-1)`-cycle counts | endpoint coefficients through `n=50` |
| exact one-step fiber | eligible fixed-point matching, cyclic insertion positions, and an involution on unmatched fixed points | every literal indegree compared with the formula for all 409,113 states |
| Garden-of-Eden criterion | a threshold-ordered Ferrers matching exists iff `e_i>=i` for every nontrivial output cycle | zero and nonzero literal indegrees throughout the full enumerations |
| identity indegree `I_n` | its ancestors are exactly involutions | exact values `[1,2,4,10,26,76,232,764,2620]` for `n=1..9` |

## Owner-subtracted boundary

- Flajolet–Sedgewick and Stanley own the standard labelled-cycle/exponential
  enumeration background.
- Shepp–Lloyd own classical ordered and longest-cycle distribution results.
- Pitman is cited for adjacent random deletion-consistent combinatorial
  structures, not as an owner of the deterministic map used here.
- Artin–Mazur own the periodic-point zeta construction.

The residual package is the exact finite phase portrait of simultaneous
cycle-minimum pruning and its label-sensitive one-step fiber geometry.  It
does not claim new longest-cycle asymptotics or absolute novelty.  The map is
also separated internally from P100: it preserves the labelled ground set,
processes multiple permutation cycles in parallel, and has a nontrivial
threshold-matching inverse graph rather than a digit-sum coordinate descent.
External release remains **HOLD**.

Control-count convention: the reported 1,981,326 quantity counts literal
nontrivial trajectory-step evaluations over all starting permutations.  It
allows repeated traversal of a functional-graph edge and is not presented as
the number of distinct edges.
