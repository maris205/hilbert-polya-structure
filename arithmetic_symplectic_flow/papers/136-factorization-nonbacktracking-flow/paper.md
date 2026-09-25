# Ordered factorization paths discard the prime components

**Paper ID:** 136-factorization-nonbacktracking-flow.  
**Candidate ID:** ANG-20260914-FAC01.  
**Date:** 2026-09-14.  
**Evidence:** exact elementary construction and scoped negative result.  
**Status:** STOP — PRIME-PRODUCT COMPONENTS HAVE NO PATHS.  
**Route state:** broadened T0--T2 owner audit only; T3 NOT EVALUATED;
classical A0/A1/A2 NOT APPLICABLE; Route B NOT INVOKED.

## Abstract

The candidate replaces divisibility-based prime/composite recognition by
ordered multiplicative refinements and then by the reversible shift on
two-sided nonbacktracking paths. Its arithmetic graph and complete unit-roof
suspension are well defined in the authorized groupoid category. However, the
same multiplicative indecomposability that recognizes a prime leaves its
component with one isolated vertex and no path. This proves failure of the
frozen proposal to turn prime-product components into periodic packets. The
product-8 component is exactly a four-cycle, giving two oriented primitive
packets of length 4 and repetitions of length 4r. No determinant calculation,
geometric lift, or formal Route evaluation is undertaken after the decisive
prime-packet stop.

## 1. Candidate identity and same-object ownership

The [version-1 card](candidate-card.md) was frozen before this audit. No field
is changed to obtain the result.

| Item | Frozen definition and owner | Audit status |
| --- | --- | --- |
| Arithmetic carrier | Disjoint union of all ordered-factorization graphs Gamma_n, n>=2 | Defined by integer multiplication, without a prime table |
| Dynamical state X | All two-sided nonbacktracking oriented-edge paths in that graph, with the discrete-alphabet product topology | Locally compact Hausdorff; Proposition 1 |
| Action | Left shift sigma on X | Homeomorphism of the complete path state |
| Broadened owner | Transformation groupoid X crossed with Z | Locally compact Hausdorff étale groupoid |
| Clock and flow | Unit roof and its suspension under sigma | Positive, complete; Proposition 2 |
| Arithmetic proposal | Prime products detected by multiplicative indecomposability become packets of the same action | Scoped failure; Proposition 3 |
| Packets and repetitions | Least shift period, cyclic phase quotient; reverse orientation retained unless a shift identifies it | Proposition 2; complete product-8 control in Proposition 4 |
| Analytic object | Ordinary unweighted primitive product proposed only if defined | NOT EVALUATED; no operator, determinant, or convergence assertion |
| Classical geometry | Positive-dimensional symplectic map, symplectic form, Hamiltonian/contact lift | NOT APPLICABLE / no construction supplied |

The groupoid is the broadened carrier. The graph relation is not being called
a deterministic map, and the symbolic suspension is not being called a
suspension over a finite-dimensional symplectic base.

## 2. Question and precise lineage

The prior-work guide places prime/composite observables and symbolic
admissibility at the origin of the search. This construction realizes the
specific replacement

```text
divisibility-based prime/composite recognition
    -> admissible ordered factor splitting/merging words
    -> reversible nonbacktracking edge-path shift and its groupoid.
```

The preserved arithmetic test is exact: an integer n>=2 is prime if and only
if it has no ordered decomposition n=ab with a,b>=2. This is a stated
replacement of the sieve-symbolic source by multiplicative refinement, not
an intertwinement with an earlier chronological sieve update. No assertion
is made that it realizes the later Logistic/Hénon or symplectic arrow.

The first question is whether the prime components survive as packets under
the frozen path convention. The strongest supported conclusion is that they
do not: X_p is empty for every prime p. This scope matters. Composite-product
paths may contain prime factor entries, and the theorem does not say all
prime-related observables vanish. Such entries do not establish a canonical
prime-to-packet map or a prime-power repetition law.

## 3. Definitions, permitted data, and normalization

For each integer n>=2, let V_n consist of all finite ordered words
(a_1,...,a_k), where k>=1, a_i>=2, and their product is n. Join two words by
one undirected edge when one is obtained from the other by replacing a
single entry ab by the adjacent pair (a,b), or by merging that pair. The graph
Gamma_n is simple: no self-loops and no labelled parallel edges. Keep every
n>=2, and take the disjoint union Gamma.

For an oriented edge e, write i(e), t(e), and bar(e) for its initial vertex,
terminal vertex, and reverse. Let X consist of sequences (e_t) indexed by all
integers with

\[
t(e_t)=i(e_{t+1}),\qquad e_{t+1}\ne\overline{e_t}.
\]

Set (sigma z)_t=e_{t+1}. All edges of z lie in a common Gamma_n, because each
allowed move preserves product. Denote this invariant, continuous product
observable by N(z)=n and its fibre by X_n. An empty X_n is allowed; in
particular, no constant path at an isolated vertex is added.

For explicit groupoid conventions, an arrow (z,k) has source z and range
sigma^k z. The arrows have topology X times discrete Z. The suspension is

\[
S=(X\times[0,1])/((z,1)\sim(\sigma z,0)),
\]

with time translation across the glued endpoints. One edge shift consumes
one time unit. No probability measure, quantum owner, or function-space
operator is asserted. Integer multiplication, all positive product labels
n>=2, and the fixed split/merge rule are the only arithmetic inputs. No
selected prime component, prime table, fitted length, zero data, or weights
enter the construction.

## 4. Exact proofs

### Proposition 1 — Carrier and action

Every Gamma_n is a finite connected graph. Each X_n is a compact-open
subspace of X, possibly empty, and X is their countable topological disjoint
union. In particular X is locally compact Hausdorff and second countable,
sigma is a homeomorphism, and its transformation groupoid is locally compact
Hausdorff and étale.

**Proof.** If a word has length k, then 2^k<=n, so k<=floor(log_2 n).
Each entry lies between 2 and n. There are finitely many possible words,
hence finitely many vertices and edges. Successive merges connect every
vertex to the one-entry word (n), proving connectedness.

The directed-edge alphabet of Gamma_n is finite. Its full two-sided product
is compact, and the adjacency and nonbacktracking conditions define a closed
subset: failure is witnessed at two consecutive coordinates. Thus X_n is
compact. In X the condition that e_0 belongs to Gamma_n defines X_n and is
open; its complement is the union of the analogous open conditions for the
other components. Hence X_n is also closed. Every path has one product n,
so these sets exhaust X. The countable discrete alphabet has a countable
finite-cylinder basis, giving second countability and the asserted local
topology.

Shifting coordinates and shifting them back preserve both path conditions
and are continuous inverse maps. On each slice X times {k}, the groupoid
source map is the identity on X and its range map is sigma^k, both local
homeomorphisms. The remaining topology assertions follow directly from the
product with discrete Z. This proof does not require a finite alphabet for
the whole union. QED.

### Proposition 2 — Clock, primitive packets, and repetitions

The unit-roof suspension is complete in both time directions. Its closed
orbits are in bijection with periodic sigma-orbits. If a path has least
positive shift period m, its suspended orbit has primitive time length m;
its r-fold traversal has length rm.

**Proof.** For a representative (z,u) with 0<=u<1, after real time t use
k=floor(u+t), state sigma^k z, and height u+t-k. This expression exists for
every real t because sigma is invertible and the roof is identically 1.
No infinite number of roof crossings occurs in finite time.

Returning to the same height requires the elapsed time to be an integer m.
Returning also to the same state is exactly sigma^m z=z. The least positive
such integer therefore agrees with the primitive flow period. Changing the
phase of a periodic path gives the same orbit. Traversing it r times simply
adds m a total of r times. Reversed paths are not identified by this quotient
unless a shift already identifies them, as specified in the card. QED.

This is a same-object repetition law for graph paths. It is not a
prime-power law merely because the graph uses integer factors.

### Proposition 3 — Prime products disappear from the path carrier

For every prime p, V_p consists only of (p), Gamma_p has no edges, and
X_p is empty. Therefore the frozen suspension has no packet, periodic or
otherwise, over product p.

**Proof.** A word of length at least two would express p as the product of
its first entry and the product of its remaining entries, both at least 2,
contradicting primality. The unique one-entry word has no possible split,
and the graph convention supplies no self-loop. A path requires an oriented
edge in each coordinate, so no such path exists in Gamma_p. QED.

Conversely, an isolated one-entry vertex (n) implies n is prime, since a
composite decomposition n=ab would supply an incident split edge. Thus the
static graph retains exact prime recognition precisely at vertices excluded
from this path space. This is the direct stop condition of the frozen card.

### Proposition 4 — A complete composite control at product 8

Gamma_8 is exactly the four-cycle

\[
(8)\; -\; (2,4)\; -\; (2,2,2)\; -\; (4,2)\; -\; (8).
\]

Its path shift has eight points, each of least period 4. There are exactly
two primitive sigma-orbits and two primitive suspended orbits, one for each
orientation, each of length 4.

**Proof.** The only possible words have lengths 1, 2, or 3. They are exactly
the four displayed words: the only two-factor decompositions are 2 times 4
and 4 times 2, and the only three-factor decomposition is 2 times 2 times 2.
Splitting or merging changes word length by one. The rule gives precisely
the four displayed edges and no others. Every vertex has degree two. Once
one oriented edge is chosen, the nonbacktracking rule uniquely forces the
next and preceding edges, so the path traverses the cycle forever in the
chosen orientation. There are eight initial oriented edges, giving eight
paths. Four successive shifts cycle through one orientation; no shorter
shift fixes a path because its four directed edges are distinct. The reverse
orientation uses the oppositely directed edges and is not a cyclic shift of
the first. Proposition 2 now gives lengths 4 and repetitions 4r. QED.

This is a complete component calculation, not an enumeration of all Gamma_n
or a classification of all periodic paths in X.

## 5. Controls and scope limits

| Control | Exact observation | Consequence |
| --- | --- | --- |
| Prime product | Every Gamma_p is an isolated vertex | Arithmetic recognition does not yield a dynamical packet |
| Small composite | Gamma_4 is the single edge between (4) and (2,2) | Allowing nonbacktracking paths still does not make every composite fibre nonempty |
| Genuine composite cycle | Complete Gamma_8 has two oriented primitive length-4 packets | Recurrence is present, but it belongs to composite multiplicative refinements |
| Backtracking convention | Alternating the edge of Gamma_4 violates the frozen nonbacktracking rule | Counting that two-step walk would change the state space |
| Vertex stasis | Adding a constant path or a loop at (p) is excluded | A prime fixed packet obtained that way belongs to a new candidate |
| Prime factor entries | Product-8 words include the prime 2 | The negative theorem concerns prime products, not absence of all prime-valued labels |
| Ownership and clock | All packets and time lengths come from sigma and roof 1 | No geometric or arithmetic clock is borrowed |
| PROVES_TOO_MUCH | The period law of Proposition 2 applies to any graph edge shift with roof 1 | That generic law supplies no prime-specific evidence |

The arithmetic recognition is invariant under graph isomorphism but not an
arbitrary arithmetic claim attached to a relabelled recurrent graph. No
shuffled-label experiment is needed to prove the exact empty-prime-fibre
obstruction. No floating-point precision, truncation limit, or fitted
parameter enters any theorem. All n are covered only by Propositions 1 and
3; the complete positive orbit count is restricted to n=8.

## 6. Gate assessment and decision

| Audit | Evidence for ANG-20260914-FAC01 | Status |
| --- | --- | --- |
| Lineage | Specific replacement of divisibility recognition by factor-refinement admissibility | Direct early symbolic arrow documented; no claimed Hénon/symplectic realization |
| T0 | Full carrier, invertible shift, groupoid, topology, unit roof and complete flow | ESTABLISHED at the stated broadened type |
| T1 | Intrinsic multiplication recognizes prime products; all corresponding path fibres are empty | Static arithmetic recognition established; proposed prime-packet mechanism scoped FAIL; clock fixed and owned |
| T2 | Same-flow primitive/repetition law; no prime-product packets; exact composite packets at n=8 | General convention ESTABLISHED; prime-product packet target scoped FAIL |
| T3 | First prime-packet test already stops the candidate | NOT EVALUATED; no global unweighted-product claim |
| Classical A0/A1/A2 | No finite-dimensional symplectic base map in the frozen carrier | NOT APPLICABLE |
| Formal Route coordinates | None assessed | UNASSIGNED |
| Route B | No evaluation requested or performed | NOT INVOKED |

**Decision: stop this candidate; portfolio fork.** The decisive reason is
that prime indecomposability produces an edge-free component and the frozen
flow is built exclusively from edges. A different object that keeps terminal
vertices, supplies new loops, or changes the path relation would require a
fresh card and cannot inherit this object's packet or clock claims. No such
repair is undertaken here. The broader search remains open.

## Evidence index

The [candidate card](candidate-card.md), [claim ledger](claim-ledger.md), and
[evidence record](evidence/README.md) preserve the object, proof scope,
controls, and stop. Definitions and gate interpretation follow the
[local plan](../../plan.md); intellectual ancestry is stated against the
[prior-work guide](../../docs/prior_work/README.md). No external graph-zeta
formula is used in this paper.
