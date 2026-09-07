# Graph / relation / random-local breadth denominator

Status: scouting only.  The labels `G01`--`G16` are lane-local candidate
identifiers, **not paper numbers**.  Nothing in this file allocates any of
P187--P191.

## Frozen denominator and conventions

The denominator is exactly **16 literal updates**.  The carrier is labelled
throughout: `[n]={1,...,n}` with its displayed order.  A deterministic update
has scheduler denominator `D_n=1`.  For a random-local update, the scheduler
set is stated literally and the Markov kernel is

`K(x,y)=#{schedule labels a : F_a(x)=y}/D_n`.

Thus coincident lazy outcomes retain their scheduler multiplicity; there is no
renormalisation by the number of distinct successors.  Every operation is
synchronous unless a single selected local action is explicitly stated.  The
pilot uses exact integer transition multiplicities and never floating point.

| ID | Class and carrier | Literal natural update | Scheduler / fixed denominator |
|---|---|---|---|
| **G01 TRC** | Binary relations, `A in {0,1}^{n x n}` | Let `r_j(A)` be source row `j`'s sum.  Set `F(A)_{ij}=1` iff `i <= r_j(A)`: left-compress every source row, then transpose. | Deterministic synchronous; `D_n=1`. |
| **G02 ECSC** | Simple undirected graphs on `[n]` | For each component order `s`, take the union `U_s` of *all* source components of order `s`; output the disjoint union of the cliques on the nonempty `U_s`. | Deterministic simultaneous size-class update; `D_n=1`. |
| **G03 OCED** | Looped binary relations on `[n]` | Join ordered pair `(i,j)` in the output iff source rows `i,j` have equal outdegree.  The output is the equality relation of the outdegree statistic. | Deterministic synchronous; `D_n=1`. |
| **G04 ACD** | Loopless directed graphs | Put arc `i -> j` in the output iff the source contains `j -> i` but not `i -> j`; equivalently `F(A)=A^T\\A`. | Deterministic synchronous; `D_n=1`. |
| **G05 CSG** | Simple undirected graphs | Join `u,v` iff they lie in distinct connected components of the source. | Deterministic synchronous; `D_n=1`. |
| **G06 OTEG** | Simple undirected graphs | Join `u,v` iff their source open neighbourhoods are exactly equal. | Deterministic synchronous; `D_n=1`. |
| **G07 D2G** | Simple undirected graphs | Join `u,v` iff they are nonadjacent in the source and have a common source neighbour (equivalently, source distance exactly two). | Deterministic synchronous; `D_n=1`. |
| **G08 RWP** | Reflexive binary relations | Choose pivot `k`; add every `(i,j)` for which `(i,k)` and `(k,j)` are present, retaining all old pairs. | Uniform `k in [n]`; `D_n=n`. |
| **G09 CTR** | Tournaments | Choose an unordered vertex triple.  Reverse its three arcs exactly when it is a directed 3-cycle; otherwise hold. | Uniform `T in binom([n],3)`; `D_n=binom(n,3)` (`n>=3`). |
| **G10 CSC** | Orientations of the labelled cycle `C_n` | Choose vertex `v`; when both incident cycle edges point away from `v`, reverse both (source-to-sink click), otherwise hold. | Uniform `v in [n]`; `D_n=n`. |
| **G11 HDCC** | 3-uniform hypergraphs | Output a triple exactly when its three vertices have equal source hypergraph degree.  Original membership is otherwise ignored. | Deterministic synchronous; `D_n=1`. |
| **G12 SLU** | Hypergraphs with nonempty edges | For each edge cardinality `s`, replace the entire source `s`-edge layer by its vertex union as one hyperedge; coincident unions coalesce. | Deterministic simultaneous layer update; `D_n=1`. |
| **G13 HBD** | Clutters (antichains in `P([n])`) | Replace a clutter by its blocker: the clutter of inclusion-minimal hitting sets.  Empty family and `{emptyset}` use the same literal definition. | Deterministic synchronous; `D_n=1`. |
| **G14 RLC** | 3-uniform hypergraphs | Choose vertex `v` and toggle every triple containing `v` (complement the full 2-uniform link of `v`). | Uniform `v in [n]`; `D_n=n`. |
| **G15 RWC** | Simple undirected graphs | Choose a middle vertex `v` and an unordered pair `{u,w}` outside it; if `uv,vw` are present, add `uw`, otherwise hold. | Uniform `(v,{u,w})`; `D_n=n binom(n-1,2)`. |
| **G16 OES** | Orientations of the labelled cycle `C_n`, encoded by cyclic edge bits | Choose cycle edge-position `i`; swap bits in positions `i,i+1 (mod n)` when unequal, otherwise hold. | Uniform `i in Z/nZ`; `D_n=n`. |

## Breadth and exclusion check

The fixed denominator contains binary relations (`G01,G03,G08`), loopless
directed graphs/tournaments (`G04,G09`), simple undirected graphs
(`G02,G05,G06,G07,G15`), hypergraphs/clutters (`G11`--`G14`), cycle
orientations (`G10,G16`), and six genuinely local random kernels
(`G08`--`G10,G14`--`G16`).  These are more than the requested four classes.

The literal rules are not instances of cut evaluation, parity filtering,
degree pruning, coordinate copying, or singleton isolation.  Nevertheless,
the kill gate below removes candidates whose *analysis* collapses to an
occupied or classical mechanism.  In particular, a different carrier name is
not accepted as mathematical separation from P145/P159/P177/P179/P183.

## Mechanical test contract

`pilot.py` exhausts the finite carriers shown in `canonical_stdout.txt`.  It
checks carrier closure and kernel row mass for every candidate, and then at
least one of functional-graph depth/cycles/fixed points, absorbing states and
reachable endpoints, exact fibres, action components, or kernel symmetry.
Only a candidate with two separable uniform theorem axes can survive; an
interesting finite sequence alone is insufficient.  These bounded checks are
counterexample pressure, not proofs and not novelty clearance.
