# Claims and evidence — P108

Status: **CROSS-HOSTILE A/B PASS / FINAL MECHANICAL QA PASS / EXTERNAL HOLD**.

| Claim | Infinite-family proof | Independent exact control |
|---|---|---|
| exact capped Fibonacci iterate | induction using `min(a,min(a,u)+min(a,v))=min(a,u+v)` | literal update versus the formula at every registered state/time |
| only `(0,0)` and `(a,a)` recurrent | fixed equation plus growth of the two Fibonacci forms | literal recurrent depth for every state through cap 220 |
| pointwise half-plane hitting time | the first iterate coordinate is the smaller Fibonacci form | observed first arrival versus the formula |
| exact transient CDF | integer lattice points above a weighted line | complete depth histograms versus the floor/ceiling sum |
| sharp depth `1+min{k:F_k>=a}` | `(1,0)` is slowest and attains the coefficient lower bound | maximum observed depth at every cap |
| image, fibre sizes, and Garden-of-Eden count | solve `y=u`, `min(a,x+u)=v` directly | reverse table built from every input state |
| zeta `(1-z)^-2` | all nonzero nonfixed states absorb at `(a,a)` | fixed counts along registered trajectories |

## Ownership boundary

Fibonacci recurrences/matrices, Binet estimates, saturated-system
background, and Artin–Mazur zeta are established material and receive no
novelty credit.  The bounded residual is the complete finite dynamics of the
specific capped map.  External release and priority language remain **HOLD**.

Internally, P83 concerns countable Catalan renewal shifts, P89 uses an iid
reset/golden-mean matrix environment, and P101 composes random cap and floor
maps on `[0,1]`.  P108 instead iterates one deterministic saturated
second-order rule on a finite integer square.  Within P107--P111, P107 acts
on ideals by annihilator and power, P109 acts on subspaces by a nilpotent
image, P110 joins translated partitions, and P111 multiplies random
Heisenberg generators.  None shares P108's phase space or update rule.
