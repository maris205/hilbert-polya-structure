# Replacement graph / relation / hypergraph denominator

Status: scouting only.  The labels `RX01`--`RX12` are local candidate IDs and
allocate none of P187--P191.  The denominator was frozen after the documented
P1--P186 formula search in `HISTORICAL_COLLISION_SEARCH.md` and before the
exact pilot was written.

## Exact conventions

Every carrier is labelled by `[n]={0,...,n-1}` with the displayed integer
order.  A deterministic update has scheduler denominator `D_n=1`.  A
random-local kernel uses

`K(x,y)=#{scheduler labels a : F_a(x)=y}/D_n`,

so lazy collisions retain multiplicity and no row is renormalised by its
number of distinct successors.  Distances are ordinary unweighted graph
distances within a connected component.  All ties are broken by the least
displayed label.

The fixed denominator contains exactly **12 fresh literal updates** across
rooted undirected trees, directed acyclic graphs, strict relations/posets,
arbitrary binary relations, hypergraphs, and random-local graph/hypergraph
kernels.

| ID | Carrier | Literal update | Scheduler / fixed denominator | Pre-pilot gate |
|---|---|---|---|---|
| **RX01 LAR** | A labelled tree `T` with distinguished root `r` | Let `a_T(r)=min argmax_v d_T(r,v)` and set `F(T,r)=(T,a_T(r))`. | Deterministic; `D_n=1`. | **ADVANCE**: no internal literal/formula collision found. |
| **RX02 NLR** | A labelled tree `T` with distinguished root `r` | Reroot at the least leaf minimising `d_T(r,v)`; the sole vertex is a leaf when `n=1`. | Deterministic; `D_n=1`. | **KILL_SHALLOW**: nearest-leaf projection; no second temporal axis. |
| **RX03 AGP** | A labelled tree `T` with distinguished root `r` | Find `a_T(r)` as in RX01 and move the root one edge along the unique `r`--`a_T(r)` geodesic (hold only at `n=1`). | Deterministic; `D_n=1`. | **KILL_OWNER_WEAK**: geodesic pursuit/rootward-path shadow; no clean uniform second axis. |
| **RX04 DSC** | A loopless labelled DAG | Choose its least source and reverse every arc leaving that source; an edgeless choice holds. | Deterministic; `D_n=1`. | **KILL_SWITCHING**: literal source-to-sink click process. |
| **RX05 PES** | A strict labelled partial order `R` | Retain `xRy` exactly when `x` is source-minimal and `y` is source-maximal. | Deterministic; `D_n=1`. | **KILL_CLOSURE**: idempotent extremal-skeleton projection. |
| **RX06 EOG** | A looped binary relation `A` | Set `F(A)_{ij}=1` exactly when rows `i,j` have exactly one common `1`: `sum_k A_ik A_jk=1`. | Deterministic; `D_n=1`. | **KILL_ROW_GRAM**: exact-one Gram/row-overlap statistic transfer. |
| **RX07 E2C** | A looped binary relation `A` | Set `F(A)_{ij}=1` exactly when there is exactly one two-step witness: `sum_k A_ik A_kj=1`. | Deterministic; `D_n=1`. | **KILL_RELATION_POWER**: unique-witness relation-square shadow. |
| **RX08 ETH** | An arbitrary hypergraph `H subseteq P([n])`, empty edges allowed | Output every `S subseteq [n]` satisfying `|S intersect E|=1` for every `E in H`. | Deterministic; `D_n=1`. | **KILL_POLARITY**: common-neighbour operator for the symmetric exact-one incidence relation. |
| **RX09 UCH** | An arbitrary hypergraph `H subseteq P([n])` | Output every `S subseteq [n]` containing exactly one source edge: `#{E in H:E subseteq S}=1`. | Deterministic; `D_n=1`. | **KILL_ROW_STATISTIC**: containment-zeta row statistic with no independent axis. |
| **RX10 PHS** | A simple undirected graph | Choose an ordered distinct triple `(a,b,c)`; if `bc` is an edge, swap the two edge indicators `ab` and `ac`, otherwise hold. | Uniform ordered distinct triple; `D_n=n(n-1)(n-2)`, `n>=3`. | **KILL_SWITCHING**: state-dependent path-hinge switch. |
| **RX11 HHE** | A 3-uniform hypergraph | Choose a two-set `B` and a two-set `{u,v}` disjoint from `B`; swap membership of `B union {u}` and `B union {v}`. | Uniform `(B,{u,v})`; `D_n=binom(n,2)binom(n-2,2)`, `n>=4`. | **KILL_EXCLUSION**: coordinate transpositions on fixed-size edge subsets. |
| **RX12 MEG** | A simple undirected graph, components treated separately | Join distinct `u,v` in the output exactly when they are mutually eccentric in their source component: `d(u,v)=ecc(u)=ecc(v)`; isolates emit no edge. | Deterministic; `D_n=1`. | **KILL_DIRECT_OWNER**: standard eccentric/strong-resolving graph operator. |

## Pilot contract

The exact verifier exhausts bounded labelled carriers and always checks
closure (or output membership) and deterministic functionality / exact kernel
row mass.  Candidate-specific sentinels then check idempotence, cubic
polarity, symmetry, conserved layers, functional-graph cycles, images, fibres,
or endpoint structure.  Pre-killed rows remain in the pilot only as negative
controls; finite data cannot revive them.

Promotion requires two axes that do not reduce to the same functional-graph
observation.  For RX01 the target contract is:

1. for every `n>1` and every labelled tree, a canonical diameter pair gives
   the complete all-time orbit and unique two-cycle; and
2. all target fibres are exact metric halfspaces across the diameter centre,
   with per-tree spectrum `{1,-1,0^(n-2)}`.

An external non-hit will leave this at `OWNER_AMBER / HOLD_EXTERNAL`; it will
not establish novelty.
