# Graph / relation lane: eight bounded probes, no admission

2026-09-05 UTC. STAGE1_SCOUTING / NO_ADMISSION / HOLD_EXTERNAL.
Owner: batch197_fifth_scout. No formal paper numbers are assigned here.

## Literal definitions fixed before the pilot

The first four carriers are every family H of subsets of [n], including the
empty family and the empty member; repetitions of a subset are not allowed.
The next three carriers are every binary relation on [n], with loops allowed.
The last carrier is every labelled simple undirected graph on [n]. All
updates read the entire old state before producing the next one.

| ID | Exact update | Precommitted full carrier bound |
|---|---|---|
| DI | H -> {A intersection B: A,B in H, A != B}. No diagonal pair is admitted. | n=0,...,4 |
| DR | H -> {A minus B: A,B in H, A != B}, using ordered pairs. | n=0,...,4 |
| SX | H -> {A symmetric-difference B: distinct A,B in H}. | n=0,...,4 |
| M3 | H -> {(A intersection B) union (A intersection C) union (B intersection C): A,B,C distinct members of H}. | n=0,...,4 |
| BRC | R -> R composed with complement(R); ij is present iff some k has ik in R and kj not in R. Complement is in [n] squared. | n=0,...,4 |
| ECP | R -> R symmetric-difference (R composed with R), with ordinary Boolean relation composition, not GF(2) multiplication. | n=0,...,4 |
| DCR | R -> (R composed with complement(R)) minus (complement(R) composed with R). | n=0,...,4 |
| SND | uv is an output edge iff the old open neighborhoods N(u),N(v) are distinct and comparable by inclusion. | n=0,...,6 |

All eight are bounded probes, not claims of separated accepted mechanisms.
In particular, set operations and Boolean products are classical inputs.
SX must face the occupied sumset/span engine; DI must face meet closure and
finite semilattice normalization; a canonical-statistic collapse would kill
SND. No candidate is promoted on a short-cycle histogram alone.

## Historical desk exclusions (not eight extra current attempts)

- Source/sink reversal: docs/papers107_111_sequence/scouting/COMBINATORIAL_SCOUT.md,
  Section9 C6, explicitly owns parallel source-to-sink via clicks/Coxeter
  dynamics; docs/papers187_191_sequence/scouting/graph_lane/replacement/
  HISTORICAL_COLLISION_SEARCH.md also desk-kills RX04. No new pilot here.
- Biconnected-block complementation: docs/papers122_126_sequence/scouting/
  combinatorial/SCOUT.md C06 already reserves the odd-order block version.
  Replacing connected blocks by 2-connected blocks is not an automatic new
  mechanism; no proposed replacement is credited or enlarged here.
- Clutter blocker: exact old S02/H01/HBN controls in P142--146, P167--171 and
  P182--186. Classical blocker duality is not reopened.
- Chord uncrossing: old P130 and P147--151 M01 occupy the local and component
  engines. No uncrossing variant is counted here.
- Exact-distance-two graph: old P187--191 G07 and previous batch D2G; the
  metamour operator has a direct external owner. No new attempt here.
- MCT / least-triangle, Ryser switch, Gram/ordinary closure, erasure and old
  component-collapse mechanisms are excluded by the current assignment.

## Actual bounded results and decisions

Here H denotes maximum transient depth, not a set family. Entries list all
precommitted sizes in ascending order; no larger full carrier was added.

| ID | H profile | Largest-box image / maximum fibre | Current decision |
|---|---|---|---|
| DI | 1,2,3,4,5 | 2941 / 2606 | KILL_GENERIC_EROSION_AND_NO_SECOND_AXIS |
| DR | 1,1,1,3,4 | 1671 / 3846 | KILL_GENERIC_DIFFERENCE_CLOSURE |
| SX | 1,2,2,2,2 | 880 / 41341 | KILL_OCCUPIED_SUMSET_SPAN_ENGINE |
| M3 | 1,1,2,2,3 | 4146 / 15159 | KILL_NO_ALL_PARAMETER_TWO_AXIS_PACKAGE |
| BRC | 0,1,2,3,5 | 8043 / 782 | KILL_NO_ALL_PARAMETER_TWO_AXIS_PACKAGE |
| ECP | 0,1,2,4,10 | 17784 / 2360 | KILL_NO_RIGID_SPINE |
| DCR | 0,1,1,3,5 | 3003 / 1099 | KILL_NO_ALL_PARAMETER_TWO_AXIS_PACKAGE |
| SND | 0,0,1,2,3,4,5 | 4832 / 2100 | KILL_NO_SECOND_AXIS_AND_RESIDUAL_OWNER_EXPOSURE |

These are gate decisions for this round, not impossibility theorems about
future research. In particular, growing H in a small box is not evidence
that a sharp global clock or a nontransferable inverse theorem exists.

DI has a proved sharp all-parameter bound H=n+1, but its proof is finite
maximal-layer erosion (PROOF_PACKAGE.md), a zero-credit mechanism already
exposed by the old maximal-element/facet peeling lanes. The interesting
largest-fibre targets at n=3,4 are respectively all subsets of sizes at most
1,2. No general extremal theorem has been proved. A generic meet-coloured
clique or inclusion--exclusion encoding would not supply the missing axis.

DR is inflationary after one step, by the elementary reverse-difference
witness in SOURCE_AND_COLLISION.md; SX becomes punctured additive closure
after one step except for the explicitly degenerate small families. These
facts explain fixed-only recurrence without giving a new dynamical engine.

M3 has a strict two-cycle already at n=3 and twenty strict two-cycles at n=4.
BRC and DCR have only periods one and two in their bounded boxes, but neither
has a proved global recurrence classification or target-resolved inverse.
ECP has periods one, two and four at n=4, and depth ten. We do not infer a
global period restriction from these observations.

SND has only the empty graph recurrent through n=6. Its largest fibre is
uniquely the empty target for 2<=n<=6. Neither statement is promoted to an
all-n theorem. Its exact one-step factor through P143 is recorded separately;
the altered update is not conjugate to the old cubic map merely by changing
notation, but this difference does not itself meet the second-axis gate.

## Evidence state and handoff

The original paper-independent pilot is pilot.py. It computes every target's
indegree and every source's orbit depth/period on the complete carriers, then
prints a compact functional-graph profile. Two actual fresh subprocesses
returned code zero, with empty stderr and byte-identical raw stdout. Each run
made 1,981,384 consistency assertions. CANONICAL.txt is the saved raw output:
9981 bytes, SHA-256
`bd75769c64bb40a24aea633b5a14dbcf540273e10bd6b8eb0cac86642d3b163d`.
See REPLAY_LOG.md for the actual receipt and commands.

The pilot's frozen final line says no theorem was claimed at pilot time;
the later zero-credit DI proof is separate and does not retroactively alter
that transcript. No independent manuscript review, source-owner clearance,
formal paper number or admitted survivor is claimed.

Lane outcome: **NO_ADMISSION / 8 CURRENT PROBES CLOSED / HOLD_EXTERNAL**.
Proof authorship for the zero-credit notes: batch197_fifth_scout only.
