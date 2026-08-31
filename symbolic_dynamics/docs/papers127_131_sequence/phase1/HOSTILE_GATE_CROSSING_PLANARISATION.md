# Hostile gate: MT2 rooted crossing-component planarisation

**Role:** independent nonauthor theorem/owner gate.  **Audit date:**
2026-08-31.  **External status:** `HOLD_EXTERNAL`.  **Hard verdict:**
**REWRITE / GO_IF_REPAIRED**, not yet a paper freeze.

The literal rooted map is well-defined, idempotent, and exhaustively supports
the proposed pointwise fibres through seven chords.  The current proof,
however, leaves its decisive all-size sibling inverse as a sketch, contains a
wrong author attribution for a direct uncrossing paper, and misses two much
closer owners: Kiyoshi Igusa's 2025 parallel-part machinery and
Alman--Lian--Tran's exact ownership of the proposed largest-fibre sequence
\(1,1,2,8,52,464,\ldots\).  After zero-credit subtraction, the temporal part is
only a one-step retraction.  The candidate is paper-scale only if the fully
proved **target-wise** inverse/product and unique-maximal-fibre theorem remain
as the explicit residual; coefficients, transforms, components, Catalan
image, and generic uncrossing cannot carry value.

## 1. Evidence reviewed and fresh control

| file | SHA-256 |
|---|---|
| `scouting/combinatorial/SCOUT.md` | `8a7ef85bd2f643dcd1fae20b926e435cc2dda040b9507ba9038616247164cbde` |
| `scouting/combinatorial/pilot_contracts.py` | `9cdbd94b96e341909e4a0abcf886e3702b39c9bcc281c28251236ed49d9bb477` |
| `scouting/combinatorial/pilot_contracts_output.txt` | `d95baeaaeb674827c6b116a2d4a788d77574b4761acb1bfee7635b40a7e3e542` |
| `phase1/SYSTEM_COLLISION_FIREWALL.md` | `84ed6ed93d308bc9565ba7d7d3629469358ad29287b0dc5fbe69f41eec6e55fc` |

I reran the focused script into a temporary file and byte-compared it with
the canonical stdout.  The comparison passed and both outputs have SHA-256
`d95baeaaeb674827c6b116a2d4a788d77574b4761acb1bfee7635b40a7e3e542`.
The full script reports 8,297,317 assertions because it also runs PO2.  The
MT2 block itself makes **293,872 assertions**, enumerating **146,599** rooted
matchings through \(n=7\) and all **625** noncrossing targets.  It checks every
target fibre, not just aggregate counts.  This is excellent counterexample
pressure but not a proof of the sibling inverse for all \(n\).

## 2. Literal map and basic dynamics

Fix the linear order \(1<\cdots<2n\), or equivalently a cut before endpoint
1 on a labelled circle.  The state space is the set \(\mathcal M_n\) of perfect
matchings on these endpoints.  The crossing graph has one vertex per chord
and an edge when two chords alternate.  For each crossing-graph component
\(K\), sort its support as
\(s_1<\cdots<s_{2k}\) and replace its chords by

\[
(s_1,s_2),(s_3,s_4),\ldots,(s_{2k-1},s_{2k}),
\]

simultaneously for all components.  Call the result \(\Phi_n(M)\).

The fixed cut is indispensable.  “Rooted” must mean this linear/cut data,
not a distinguished chord.  The operation is not rotation-equivariant and
“planarisation” must not be confused with graph planarization or with a
canonical map on unrooted chord diagrams.

Let \(\pi(M)\) be the endpoint partition into supports of crossing components,
and let \(s(P)\) pair successive elements inside every block of an even-block
noncrossing partition \(P\).  The classical component theorem gives
\(\pi(M)\) noncrossing, so

\[
\Phi_n=s\circ\pi.
\]

The section \(s(P)\) is noncrossing.  Conversely every noncrossing matching
\(T\) has singleton crossing components and is fixed by the operation.
Therefore the map is a retraction onto the noncrossing matchings:

\[
\Phi_n^2=\Phi_n,\qquad
\operatorname{im}\Phi_n=\operatorname{Fix}\Phi_n=NC_2(n).
\]

Thus image and fixed-set size are \(\operatorname{Cat}_n\), every nonfixed
state has exact depth one, and every nonfixed state has indegree zero.  The
last assertion follows from idempotence: if \(\Phi(z)=x\ne\Phi(x)\), then
\(\Phi^2(z)=\Phi(x)\ne x=\Phi(z)\), a contradiction.  With “Garden state”
defined as indegree zero, their number is
\((2n-1)!!-\operatorname{Cat}_n\), and

\[
\zeta_{\Phi_n}(z)=(1-z)^{-\operatorname{Cat}_n}.
\]

These identities are correct but almost entirely formal consequences of a
one-step retraction; they are not enough on their own for paper value.

## 3. The decisive inverse lemma: plausible, tested, not yet proved

For a noncrossing target \(T\), orient its nesting forest from a virtual root
\(\widehat0\).  Let \(d_T(v)\) be the number of immediate child chords of
\(v\), including top-level chords as children of \(\widehat0\).  Put

\[
c_k=\#\{\text{crossing-connected \(k\)-chord diagrams}\},
\]

and

\[
a_d=\sum_{\rho\in NC(d)}\prod_{B\in\rho}c_{|B|}.
\]

The claimed inverse says that a source over (T) is equivalent to choosing,
independently for every (v), a noncrossing partition of the ordered sibling
list of length \(d_T(v)\), then decorating each block of \(k\) siblings by a
crossing-connected \(k\)-chord diagram.  If and only if that bijection is
proved, the pointwise formula

\[
|\Phi_n^{-1}(T)|=
\prod_{v\in V(T)\cup\{\widehat0\}}a_{d_T(v)}
\]

follows.

The scouting paragraph does not yet prove the required forward and converse
directions.  A paper proof must establish all of the following explicitly.

1. If \(P=\pi(M)\) and \(s(P)=T\), then the \(T\)-chords whose endpoints lie
   in one block of \(P\) are immediate siblings under one common parent (or
   under the virtual root).  Ancestor--descendant chords cannot share such a
   block because successive pairing would change their endpoints.
2. For each ordered sibling list, its induced groups form a noncrossing
   partition of the sibling indices.  Blocks may be nested in index order;
   they need not be intervals.
3. Conversely, arbitrary independent noncrossing partitions of all sibling
   lists, with connected decorations, produce crossing components exactly
   equal to the chosen blocks.  In particular, re-pairing sibling endpoints
   cannot cross and merge a component living inside a descendant interval.
4. The construction and extraction are mutual inverses, including repeated
   block sizes and the virtual-root case.

The \(n\le7\) pointwise comparison is consistent with all four statements,
but it does not replace them.  Igusa's 2025 definition of parallel parts is
very close to items 1--2 and must be used for subtraction, not presented as a
new sibling principle.

## 4. Generating series and extremal fibre audit

The noncrossing-partition transform gives the **formal ordinary power-series**
identity

\[
C(u)=\sum_{k\ge1}c_k u^k,
\qquad
A(u)=\sum_{d\ge0}a_d u^d=1+C(uA(u)).
\]

“Formal” is essential: the connected chord counts have factorial growth, so
no analytic radius or singularity claim follows.  The initial terms

\[
(c_1,\ldots,c_7)=(1,1,4,27,248,2830,38232)
\]

and

\[
(a_0,\ldots,a_7)=(1,1,2,8,52,464,5184,68928)
\]

are correct.  They are not new data.

For \(i,j>0\), juxtaposition injects an \(a_i\)-object and an \(a_j\)-object
into an \(a_{i+j}\)-object.  A one-block object lies outside this image, and
\(c_{i+j}>0\): the matching pairing \(q\) with \(q+i+j\) gives an all-crossing
connected example.  Hence

\[
a_i a_j<a_{i+j}.
\]

Since \(\sum_v d_T(v)=n\), repeated merging gives a strict inequality unless
only one vertex has positive child degree.  Such a degree-\(n\) vertex must be
the virtual root; a noncrossing matching with all chords top-level is uniquely
\((1,2)(3,4)\cdots(2n-1,2n)\).  Conditional on the inverse lemma, this proves
the claimed unique largest fibre \(a_n\).  These missing justifications are
short, but all must be visible; “a connected decoration lies outside” alone
does not prove positivity for every \(i+j\) or uniqueness of the target.

The empty case should be explicit:
\(\mathcal M_0=\{\varnothing\}\), \((-1)!!=\operatorname{Cat}_0=a_0=1\),
and the empty matching is fixed.  The case \(n=1\) is then automatic.

## 5. Severity-ranked objections

### CRITICAL

None is yet a demonstrated counterexample to the literal map or the proposed
product.  The absence of a complete all-size inverse proof, however, prevents
`GO` at this stage.

### MAJOR (mathematics)

1. **The sibling-list bijection is the only substantive residual and is only
   sketched.**  Supply the four-part forward/converse proof in Section 3.
   Failure of any one part kills the pointwise product and therefore the
   candidate.
2. **The extremal proof omits two logical steps.**  Exhibit a connected
   \(k\)-chord diagram for every \(k\ge2\), and prove that one positive degree
   forces that vertex to be the virtual root and the target to be the
   consecutive matching.
3. **State explicitly that \(A=1+C(uA)\) is a formal OGF.**  No convergence,
   asymptotic, or analytic-combinatorics conclusion is permitted from this
   identity alone.
4. Define the \(n=0\) conventions and “Garden state”; do not let
   \((-1)!!\) or the virtual-root product remain implicit.

### MAJOR (owner scope and bibliographic correctness)

1. **The uncrossing citation is misattributed.**  arXiv
   [1406.5671](https://arxiv.org/abs/1406.5671) and DOI
   [10.1016/j.jcta.2015.04.004](https://doi.org/10.1016/j.jcta.2015.04.004)
   are Thomas Lam's *The uncrossing partial order on matchings is Eulerian*,
   not a paper by Alman, Lian, and Tran.  Correct this before the source can
   be trusted.
2. **The exact largest-fibre sequence is directly owned.**  Alman, Lian, and
   Tran's primary paper
   [*Circular Planar Electrical Networks: Posets and Positivity*](https://joshalman.com/AlmanLianTran.pdf),
   Theorems 4.1.6 and 4.1.8, enumerates full wiring diagrams by exactly OEIS
   [A111088](https://oeis.org/A111088), with initial values
   \(1,1,2,8,52,464,\ldots\), an explicit recurrence and power-coefficient
   identity.  OEIS is only a discovery pointer; the paper is the primary
   owner.  The sequence, recurrence, OGF identities, and any asymptotic are
   zero-credit.  The residual may say that the largest fibre is counted by an
   already-owned sequence, not that the sequence was obtained here.
3. **The sibling mechanism has a current direct neighbor.**  Kiyoshi Igusa's
   2025 [*A Category of Noncrossing Partitions*](https://doi.org/10.1007/s10485-025-09838-8)
   defines vertical/lateral orders and maximal parallel sets of parts, and
   proves when parts may be merged without introducing a crossing.  On a
   matching, the relevant parallel sets specialize closely to the ordered
   sibling lists.  The paper does not state this temporal section in the
   bounded audit, but the parallel/sibling grouping principle is zero-credit
   and needs a proposition-by-proposition comparison.
4. Component supports and their decorated noncrossing partition are already
   owned in the chord-diagram literature.  Zero-credit sources must include
   Flajolet--Noy's
   [connected-component equation](https://doi.org/10.1007/978-3-662-04166-6_17),
   Nabergall's primary
   [decorated even-block decomposition](https://uwspace.uwaterloo.ca/items/51239c85-b044-4e6b-97c6-710332c37c93),
   Acan's [intersection-graph treatment](https://arxiv.org/abs/1501.01489),
   and Callan's
   [generic noncrossing-partition transform](https://cs.uwaterloo.ca/journals/JIS/VOL11/Callan/callan412.html).
   Kreweras owns the classical noncrossing-partition lattice and Lam owns the
   uncrossing poset.  Catalan image counts, \(c_k\), and the transform itself
   are therefore not contributions.
5. The bounded 2025--2026 audit found no primary source stating the literal
   consecutive-pair section together with the target-wise product.  This is a
   bounded non-hit only.  It cannot be turned into “new,” “first,” or
   “canonical” priority language.

### MINOR

1. Say “cut-dependent consecutive-pair section” rather than unqualified
   “canonical planarisation.”
2. Distinguish the crossing graph from the geometric chord diagram at every
   use of “component.”
3. Record that a fibre is not determined by \(n\) alone; the consecutive and
   rainbow targets already differ at \(n=2\).
4. Do not call \(A=1+C(uA)\) “the” chord-diagram component equation; the owned
   full-diagram equation is \(D=1+C(uD^2)\).
5. Keep exact enumerator totals separate: 293,872 MT2 assertions versus
   8,297,317 assertions for the combined PO2/MT2 script.

## 6. Internal collision firewall through P126

There is no literal internal owner, but the collision load is not low.

- P110 uses chord edges inside partition shift--join dynamics; its update and
  temporal law differ, so no theorem transfers.
- P123 acts by complementation on actual graph components and uses cotrees;
  MT2 instead derives a crossing graph from a matching and immediately
  retracts.  “Componentwise” results receive no portfolio credit by itself.
- P120 uses a plane-tree nesting coordinate for an involution.  MT2's nesting
  forest is a static inverse coordinate, not a tree dynamical carrier.
- P105's matching/fibre language is permutation-threshold based, and
  P117/P122/P126 are run/composition dynamics.  Period and depth profiles
  rule out conjugacy.
- The same scouting history already contains killed local crossing rotors and
  an odd-component reflection reserve.  This makes another chord-component
  paper costly.  MT2 survives only if its target-wise fibre theorem is
  presented as the residual; the component carrier and idempotence add no
  value.

## 7. Allowed claim ceiling and mandatory rewrite

If repaired, the maximum admissible claim set is:

1. the literal cut-dependent map \(\Phi_n=s\circ\pi\);
2. its retraction/image/fixed/Garden/zeta consequences, explicitly labelled
   low-credit;
3. the fully proved target-wise sibling-decoration bijection;
4. the resulting pointwise fibre product;
5. strict supermultiplicativity and the unique consecutive-target maximum,
   whose value is the already-owned sequence A111088;
6. the total-mass identity obtained by summing the fibres, as a consistency
   corollary.

Forbidden claims include novelty or priority, a new noncrossing transform, a
new enumeration of connected chord diagrams or A111088, rotation
equivariance, a nontrivial transient hierarchy, generic uncrossing,
asymptotics, or a result for unrooted diagrams.

**Mandatory repairs before re-gate:** give the complete sibling inverse;
correct Lam's attribution; add Igusa and Alman--Lian--Tran with explicit
zero-credit subtraction; label the series formal and A111088 owned; prove all
steps of the strict maximum; control \(n=0,1\), the cut, and Garden-state
terminology; and strengthen the internal chord-carrier firewall.

If the inverse proof closes exactly and the manuscript centers only the
target-wise product plus extremum, the verdict may advance to
`GO_INTERNAL_AFTER_REPAIR`.  If the inverse reduces verbatim to an existing
parallel-part/fibre theorem, or if the project requires A111088 or the
one-step dynamics as its headline value, **KILL**.  For now the correct gate
is **REWRITE**, and external dissemination remains **HOLD**.
