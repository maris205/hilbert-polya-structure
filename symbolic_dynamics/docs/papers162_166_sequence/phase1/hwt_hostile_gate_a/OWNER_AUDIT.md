# Bounded owner audit: Hamming-weight diagonal translation

Decision: `GREEN` after explicit subtraction  
External lifecycle: `HOLD_EXTERNAL`  
Search date: 2026-09-03

Failure to locate the literal family is not evidence of novelty or priority.

## 1. Search surface

Query families included:

- `x + wt(x) modulo n Hamming weight dynamics`
- `Hamming weight state-dependent diagonal translation`
- `add the Hamming weight to all coordinates modulo`
- `support size feedback finite abelian group map`
- `i+a_i mod n weak composition functional graph`
- `cyclic weak composition self-step map`
- `occupancy composition functional digraph Stirling periods`
- `inventory loops digit counts dynamics`
- `self descriptive sequence multiplicity vector dynamics`
- `parking function cyclic weak composition mapping`
- the same functional-graph/composition queries with 2024--2026 filters.

No inspected source defines the coupled family
$(\mathbb Z/n\mathbb Z)^n$ with update
$x\mapsto x+\operatorname{wt}(x)\mathbf1$, or its induced
$j\mapsto j+m_j$ phase graph.  This bounded non-hit is novelty-neutral.

## 2. Direct binary owner: mandatory zero credit

David A. Meyer and James Pommersheim, *Single-Query Learning from Abelian and
Non-Abelian Hamming Distance Oracles*, Chicago Journal of Theoretical
Computer Science (2010), arXiv:0912.0583,
<https://arxiv.org/pdf/0912.0583>.

On page 4 they define $\widehat x=x$ when $\operatorname{wt}(x)$ is even and
$\widehat x=\bar x$ when the weight is odd.  Over $\mathbb F_2$, this is
exactly

$$
\widehat x=x+(\operatorname{wt}(x)\bmod2)\mathbf1.
$$

Their purpose is a permutation used in a quantum-query algorithm, not an
iterated functional-graph analysis.  More importantly, their word length is
an independent parameter whereas the present family couples length and
alphabet modulus.  Within the literal coupled family the overlap is only
$n=2$, where all four states are recurrent and every fibre has size one.

Subtraction:

- binary weight-controlled complement/diagonal translation: zero credit;
- all claims at $n=2$: zero credit as a base member;
- the $n\ge3$ occupancy phase map, Stirling exact-period census, nonuniform
  fibre enumerator, and sharp $n-2$ tail: not present in the inspected paper.

## 3. Composition, parking, and inventory neighbours

| Source/area | What it owns | Why it is not a direct owner |
|---|---|---|
| Lackner and Panholzer, *Parking Functions for Mappings*, JCTA 142 (2016), DOI `10.1016/j.jcta.2016.03.001` | parking processes on arbitrary functional digraphs and their enumeration | it starts from a mapping as the road network; it does not construct $g_m(j)=j+m_j$ from an occupancy composition or iterate the present state map |
| Classical circular parking functions | weak compositions, cyclic rotation arguments, and parking counts | the update is sequential collision resolution, not simultaneous diagonal translation |
| Chase, *Inventory Loops (i.e. Counting Sequences) have Pre-period $2\max S_1+60$*, arXiv:2004.00209 | iteration of a digit-frequency description map | the multiplicity vector becomes the next state; here it is a static coordinate for motion inside a diagonal orbit |
| autobiographical/self-descriptive numbers | profiles satisfying “entry $i$ counts symbols $i$” | these are fixed-profile equations, not $j\mapsto j+m_j$ dynamics |
| Stirling numbers and ordered Bell/Fubini numbers | surjection and ordered-partition counts | (3.2)--(3.4) use these classical counts; the identities themselves receive zero credit |

Primary/author links inspected:

- Meyer--Pommersheim: <https://arxiv.org/abs/0912.0583>
- Lackner--Panholzer journal record:
  <https://doi.org/10.1016/j.jcta.2016.03.001>
- Inventory loops: <https://arxiv.org/abs/2004.00209>

## 4. Recent-search disposition

The 2024--2026 pass returned general functional-digraph generation, Hamming
weight functions of codes, quantum Hamming-weight computation, and digraph
composition papers.  None used the literal map or the occupancy phase graph.
These records provide no positive novelty certificate.

## 5. Contribution subtraction table

| Ingredient | Credit after audit |
|---|---:|
| Hamming weight/support-size definition | 0 |
| diagonal translation and free cyclic orbit | 0 as group-action vocabulary |
| binary parity/complement member | 0, Meyer--Pommersheim |
| weak compositions, multinomials, Stirling/Fubini identities | 0 |
| generic functional-graph cycle/tree facts | 0 |
| strict reduction of the coupled literal map to $g_m(j)=j+m_j$ | residual |
| forced gap-cycle classification and all exact-period counts | residual conjunction |
| sharp $n-2$ tail with witness | residual conjunction |
| every-target formula plus full indegree EGF and maximum | residual second axis |
| all-time target oracle | supporting only; not promoted as a closed census |

## 6. Owner verdict

`GREEN_OWNER_THIN`, not “novel.”  The binary mechanism is directly adjacent
and must be cited/subtracted.  No direct source located in this bounded pass
consumes the coupled $n\ge3$ theorem package.  The non-hit cannot authorize
external circulation; status remains `HOLD_EXTERNAL`.

