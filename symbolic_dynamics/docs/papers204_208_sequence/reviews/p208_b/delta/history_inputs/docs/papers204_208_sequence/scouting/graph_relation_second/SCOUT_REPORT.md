# Graph/resource lane, second bounded intake

2026-09-05 UTC. Owner: `/root/batch197_fifth_scout`.
**Seven probes / six closed / one author theorem candidate awaiting gate /
zero papers admitted by this lane / HOLD_EXTERNAL.**

## Literal finite systems and fixed pilot bounds

The graph $G$ is finite, labelled, simple and undirected. It is a parameter
that never changes during any orbit. Every update below is synchronous.
The graph bitmask lists possible edges $(0,1),(0,2),\ldots$ lexicographically.
State count totals in the results table are disjoint sums over all graph
parameters and, for resources, all mass parameters in the stated box.

| ID | Literal rule | Complete initial pilot box |
|---|---|---|
| ECD | $x'_v=|\{u\sim v:x_u=x_v\}|$, equal-colour degree. | All graphs, $0\le n\le4$; all $q^n$ words with $q=\max(2,n)$. |
| LRC | $x'_v=|\{u\sim v:x_u<x_v\}|$, lower-neighbour count with multiplicity. | Same graph/word box as ECD. |
| CCI | $x'_v=x_v+1\pmod3$ if any neighbour has its old colour, otherwise $x'_v=x_v$. | All graphs, $0\le n\le4$; all ternary words. |
| MGE | Each vertex chooses its incident edge maximizing $(|x_u-x_v|,-\min(u,v),-\max(u,v))$. On mutually chosen pairs whose load gap is at least two, transfer one unit from richer to poorer. Other loads hold. | All graphs, $0\le n\le4$; all weak compositions of each total mass $0\le M\le6$. At $n=0$ only $M=0$. |
| RMA | Every vertex sends its whole old pile to the maximum of its closed neighbourhood under $(x_u,-u)$; all incoming piles are summed. | Same resource box as MGE. |
| GLD | Every vertex with a strictly less loaded neighbour sends one unit to the neighbour minimizing $(x_u,u)$ among those strictly lower neighbours. | Same resource box as MGE. |
| DGO | On orientations of a fixed graph, reverse $u\to v$ exactly when its old outdegree satisfies $d^+(u)>d^+(v)$; retain ties. | All graphs through $n=5$ and all orientations of every such graph. |

These differ from the first graph lane's DI/DR/SX/M3 set-family maps,
BRC/ECP/DCR relation products, and SND neighbourhood-comparability graph.
There is no mex, Galois/closure operation, triangle toggle, or graph-power
update in this intake. This does not certify seven independent new engines.
Minimum-preimage feedback was desk-excluded as exactly occupied by P167;
source/sink clicks, standard chip firing and ordinary cyclic predator automata
were not counted as new probes.

## Initial exact results and dispositions

The height lists cover all initial box sizes, beginning at $n=0$. Image,
recurrent, and fixed counts are totals over the largest-size parameter box.
The maximum fibre is the largest over a single fixed parameter component,
not an indegree after identifying distinct graphs or masses.

| ID | Heights | Largest-box states / image / recurrent / fixed | Periods in largest box | Max fibre | Decision |
|---|---|---|---|---|---|
| ECD | 0,1,2,2,4 | 16,384 / 459 / 204 / 136 | 1,2,3 | 256 | KILL_NO_UNIFORM_SPINE_OR_SECOND_AXIS |
| LRC | 0,1,1,3,5 | 16,384 / 1,468 / 800 / 800 | 1 | 256 | KILL_UNPROVED_CLOCK_AND_NO_INVERSE |
| CCI | 0,0,0,2,4 | 5,184 / 3,606 / 2,460 / 1,635 | 1,3 | 7 | AUTHOR_THEOREM_CANDIDATE_PENDING_INDEPENDENT_GATE |
| MGE | 0,0,3,4,6 | 13,440 / 6,794 / 3,448 / 3,448 | 1 | 15 | KILL_DIRECT_MATCH_AND_BALANCE_ENGINE |
| RMA | 0,0,1,2,3 | 13,440 / 5,714 / 5,135 / 5,135 | 1 | 26 | KILL_SUPPORT_EROSION_AND_STATIC_CENSUS |
| GLD | 0,0,3,4,11 | 13,440 / 7,600 / 3,004 / 808 | 1,2,3,4,6,8,9 | 10 | KILL_IRREGULAR_NO_TWO_AXIS_CONTRACT |
| DGO | 0,0,0,1,2,5 | 59,049 / 21,319 / 8,469 / 639 | 1,2 | 32 | KILL_SYMMETRIC_THRESHOLD_ADAPTER |

The ECD/LRC maximum 256 includes the edgeless graph's constant map and is
not an interesting extremal signal. LRC's fixed-only bounded recurrence
does not establish convergence for arbitrary graphs. ECD already has a
strict three-cycle on four vertices; GLD has unrelated periods even at
three vertices. Their bounds were not increased to repair weak signals.
MGE, RMA and DGO's deductions are in [GENERIC_PROOFS.md](GENERIC_PROOFS.md)
and receive zero promotion credit. DGO reverses the opposite score
inequality from P112; no false literal P112 collision is asserted.

## CCI: one bounded theorem follow-up

[CCI_PROOF_PACKAGE.md](CCI_PROOF_PACKAGE.md) supplies complete author proofs
for every finite graph and every $q\ge3$ of: the weighted first-activation
formula and every-time coordinates; exact recurrent component types and
periods $1,q$; global sharp entrance $(q-1)(n-2)$ for $n\ge3$; a complete
one-step source-mask decoder; and the uniform sharp maximum fibre
$2^{n-1}-1$ for $n\ge4$, attained only by a star with a constant target.
At $n=3$ the maximum is four, attained only by a triangle and a constant
target. Small sizes are explicit. There is no all-time fibre formula claim.

This is the only probe taken to a new two-axis proof package. Static total
vertex covers and shortest-path/activation methods are owned background,
not new primitives. The narrow conjunction needs an independent correctness,
source and value gate before any paper number. The author of this proof
cannot review a resulting manuscript. Its existence does not promote it.

The follow-up checker compares literal orbits with independently computed
Floyd--Warshall arrival times, compares every exact source set with the
total-cover/predecessor mask conditions, exhausts all graphs through six
vertices for the static extremum, and checks explicit sharp paths for
$2\le n\le20$, $3\le q\le9$. Full dynamical carriers stay at $n\le4$ with
$q=3,4,5$; this changes palette boundary checks for new proofs, not a weak
candidate's size cutoff. Its 1,029,769 assertions are author proof pressure,
not an independent review. See [CCI_CANONICAL.json](CCI_CANONICAL.json).

## Evidence and handoff

The initial pilot exhausts 140,982 states across 2,906 parameter components,
with 243,120 assertions. Both the pilot and CCI follow-up have actual fresh
two-process, raw-byte comparison receipts and saved complete stdout in
[REPLAY_LOG.md](REPLAY_LOG.md). Input code, proofs, source boundaries and
outputs are covered by a nonself directory-relative manifest.
No historical evidence, author NS file, central state, manuscript, Git ref,
or external service was modified. P204 manuscript review remains a separate
future assignment and was not started during this scout.
