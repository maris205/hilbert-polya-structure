# Third graph/geometry lane: closed without promotion

2026-09-05 UTC. Owner and proof author: `/root/batch197_fifth_scout`.
**NO_PROMOTION / seven probes plus one immediately rejected control /
zero reserves / zero formal paper IDs / HOLD_EXTERNAL.**

## Scope and literal maps

The graph carrier is every labelled simple graph on $[n]$, including the empty
carrier at $n=0$. Components are recomputed from each old state. No operator
connects distinct old components; isolates remain isolated. All predicates
below are for distinct vertices in one component. The geometry carrier is
every ordered triple in $(\mathbb F_p^2)^3$, with $p\equiv3\pmod4$ prime.
Every listed update is simultaneous and autonomous.

| ID | Literal update | Complete initial box |
|---|---|---|
| DIA | Join pairs at the old component's maximum graph distance. | All graphs, $n=0,\ldots,5$. |
| EVEN | Join pairs whose old shortest-path distance is even. | Same. |
| TWO | Join pairs with exactly two shortest paths in the old graph. Paths are counted, not walks or merely two-step witnesses. | Same. |
| MMD | Join $u,v$ iff all neighbors of $u$ are at distance at most $d(u,v)$ from $v$, and all neighbors of $v$ are at distance at most $d(u,v)$ from $u$. | Same. |
| RED | Replace each component by pairs maximizing its unit-resistor effective resistance. All resistance comparisons are exact rational comparisons. | Same. |
| PED | Replace each vertex by the perpendicular foot of the fixed origin on the opposite side. Projection onto a repeated side point is that point. | All triples at $p=3,7$. |
| REF | Reflect all three vertices in their old opposite lines; for a repeated side point, use reflection in that point. | Same. |
| ODD, negative control | Join pairs at odd shortest-path distance. Recognized as an immediate extensive retraction during implementation and killed; EVEN replaced its live seat. | Same bounded graph box, control only. |

Exact projection/reflection formulas and all boundary conventions are in
[PROOF_BOUNDARIES.md](PROOF_BOUNDARIES.md). Points are encoded as $x+py$;
triples $(a,b,c)$ as $a+p^2b+p^4c$. Graph bits list possible edges in
lexicographic order. Finite-field $p=3,7$ were both initial boxes, not a later
increase to rescue an unfavorable result.

Desk exclusions were not counted as extra probes: old RX12 mutually eccentric
graph (same literal predicate), this batch OT orthic-triangle update, exact
distance-two/metamour, ordinary graph powers, closure/bridge erasure, triangle
flips, least-choice dynamics, polarity and the CCI neighborhood. These old
facts were checked from the actual scout definitions. Naming MMD “strong
resolving” does not make it identical to RX12 MEG; their difference is proved.

## Results and gate decisions

For the graph rows, heights cover $n=0,\ldots,5$; other statistics use $n=5$.
The geometry rows show both complete prime boxes. Every number below is an
exact finite census, not an extrapolated theorem.

| Rule | Heights | Largest box: image / recurrent / fixed | Periods in that box | Max one-step fibre | Disposition |
|---|---|---|---|---|---|
| DIA | 0,0,0,1,2,3 | 369 / 64 / 52 | 1,2 | 38 | KILL_NO_FULL_CARRIER_TWO_AXIS; cycle restriction is ordinary modular multiplication. |
| EVEN | 0,0,1,2,3,4 | 368 / 13 / 1 | 1,2 | 52 | KILL_NO_FULL_CARRIER_TWO_AXIS; the tempting period-two inference already fails on $C_7$. |
| TWO | 0,0,1,1,2,2 | 96 / 1 / 1 | 1 | 599 | KILL_UNPROVED_CLOCK_AND_NO_INVERSE; no all-size nilpotence claim. |
| MMD | 0,0,0,1,1,2 | 244 / 64 / 52 | 1,2 | 27 | KILL_DIRECT_STATIC_OPERATOR_AND_NO_RESIDUAL_CONTRACT. |
| RED | 0,0,0,1,2,2 | 129 / 64 / 52 | 1,2 | 47 | KILL_NO_FULL_CARRIER_TWO_AXIS; shared cycle adapter with DIA/MMD. |
| PED, $p=3$ | 3 | 369 / 105 / 9 | 1,24 | 49 | KILL_CLASSICAL_ITERATION_NEIGHBOR_AND_NO_COMPLETE_FINITE_FIELD_CONTRACT. |
| PED, $p=7$ | 3 | 69,601 / 52,465 / 49 | 1,3,9,12,18,24,36,48,72,144 | 1,825 | Same; periods and height are only bounded observations. |
| REF, $p=3$ | 1 | 297 / 297 / 81 | 1,2 | 7 | KILL_CLASSICAL_ITERATION_NEIGHBOR_AND_NO_COMPLETE_FINITE_FIELD_CONTRACT. |
| REF, $p=7$ | 4 | 75,313 / 18,865 / 11,809 | 1,2 | 3 | Same; repeated-point convention is not the old real-paper convention. |
| ODD control | 0,0,0,0,1,1 | 604 / 604 / 604 | 1 | 19 | KILL_IMMEDIATE_RETRACTION; all-graph idempotence proved with zero credit. |

The transient/recurrent portrait alone supplied no independent inverse theorem.
The full proof of the zero-credit cycle adapter gives exact period $k$ for
DIA/MMD/RED on the labelled cycle with $2^k-1$ vertices, for every $k\ge3$.
A single proof-directed $C_7$ sentinel checks three-cycles for those three maps
and EVEN. This is not an enlarged exhaustive graph box. The regular family
is a scalar power system on units modulo sign and is explicitly deducted.
Bell fixed-point counts for DIA/MMD are likewise a static clique-partition
description, not a second contribution.

PED's classical third-pedal similarity and REF's classical forward/backward
triangle iteration are positive owner-neighborhood evidence. Neither source
is falsely claimed to prove the finite-field totalized dynamics. Conversely,
changing the carrier or completion cannot create a two-axis contract in the
absence of its proofs. No proof spike was promoted and no cutoff grew.

## Evidence and ownership

[pilot.py](pilot.py) is new author-side code using BFS shortest-path counts,
exact grounded-Laplacian inversion, literal field projections and a full
functional-graph walk. It imports no previous verifier. It exhausts 243,356
states across 40 boxes. Each final execution makes 513,700 consistency checks.
Two real subprocesses returned zero with empty stderr and identical raw stdout.
The complete 26,251-byte canonical is [CANONICAL.json](CANONICAL.json), SHA-256
`f738dbd448f3455f57821a20e65d81e05fcf54403027fef758bb54fe56d46cef`.

The log preserves the early manually interrupted inefficient reporting run;
it was not an assertion failure and is not counted as a passing replay.
The final two executions used the final code and include all declared rows,
depth/cycle distributions and the proof-directed sentinel traces. Source limits,
including failed full-PDF fetches, are in [SOURCE_AND_COLLISION.md](SOURCE_AND_COLLISION.md).
No independent acceptance review, original ownership clearance, manuscript,
central index, Git operation or external upload/contact is claimed. All new
files for this task are confined to this third-lane directory.
