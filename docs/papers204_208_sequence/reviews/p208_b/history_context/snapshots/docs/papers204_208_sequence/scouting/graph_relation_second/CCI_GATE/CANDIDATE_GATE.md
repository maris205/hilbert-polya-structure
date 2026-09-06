# CCI independent candidate gate

2026-09-05 UTC. Reviewer: `/root/batch197_fosp_gate`.
Author: `/root/batch197_fifth_scout`.
Verdict: **MATH_VALID / GO_NARROW_THEOREM_CONTRACT / OWNER_AMBER / HOLD_EXTERNAL**.

This author-independent candidate assessment permits root to consider the
contract below for admission. It is not admission by itself, a numbered
paper, manuscript Review A/B, external expert review, or a priority claim.
Root must inspect this evidence and replay it before integrating a decision.

## Provenance and the exact object

The author's complete CCI_PROOF_PACKAGE.md was read after the author
confirmed its input package closed. The scientific proof pin is
`37b3c63545b13f56f9f41d658e71b4dd9d3b2ea948f89b638257bb57a44485e9`.
The reviewer did not author it, supplied no missing mathematical lemma or
manuscript text, and changed none of the author's files. The author's
canonical/source report were inspected, not treated as independent evidence.
The verifier here was written from scratch using only the standard library:
it neither imports nor reads author scripts, author canonical data, historical
code or other repository modules. Prior work by this reviewer concerned
unrelated combinatorial systems and the P204 outline, not CCI's proof.

Research-review's external MCP tools are unavailable. Under this batch's
explicit current-model/process-separated internal fallback, this existing
non-author process performs the review. No external model call, thread ID,
specialist review or model override is invented. The project workflow and
proof-writer checks organize the claim, assumptions and dependency audit.

Let $G=(V,E)$ be a finite simple undirected labelled graph, $n=|V|$, and
$q\ge3$. The literal synchronous update is
$$F(x)_v=x_v+\mathbf1\{\exists u\sim v:x_u=x_v\}\pmod q.$$
Isolates hold. Equality of old colours, not a successor colour or a threshold
count, triggers the increment. All results include disconnected and empty
graphs, with the stated empty-maximum convention.

## Narrow contract supported by this GO

1. Put $S(x)$ equal to the endpoints of the initial monochromatic edges,
   and give each directed old edge weight
   $w_x(u,v)=(x_v-x_u)\bmod q\in\{0,\ldots,q-1\}$.
   The first conflict time is precisely the directed shortest distance
   $d_x(v)$ from $S(x)$, or infinity if unreachable. Every iterate is
   $$F^t(x)_v=x_v+\max(0,t-d_x(v))\pmod q$$
   for finite distance, and is $x_v$ otherwise. The exact entrance is the
   largest finite distance, with empty maximum zero. A recurrent component
   is either proper and fixed, or every vertex has a same-coloured neighbor
   and the component rotates globally. Every nonfixed orbit has exact period
   $q$. The uniform sharp entrance maximum is zero for $n\le2$ and
   $(q-1)(n-2)$ for $n\ge3$.
2. For any target $y$, define its monochromatic graph $H_y$ and the arcs
   $u\to v$ with $y_v=y_u+1$ on edges of $G$. Every predecessor is uniquely
   $y-\mathbf1_A$, where $A$ covers $H_y$, $H_y[A]$ has no isolated vertex
   (empty $A$ allowed), and $A$ is predecessor-closed in this arc graph.
   This is a target-resolved inverse set, not a polynomial-time counting
   claim. The uniform maximum fibre is $1$ for $n\le2$, $4$ for $n=3$,
   and $2^{n-1}-1$ for $n\ge4$. For $n=3$ the exact maximizers are triangle
   graphs with constant targets; for $n\ge4$ they are spanning stars with
   constant targets.

No all-time inverse atlas, complete basin enumerator, recurrent-state
enumeration, efficient arbitrary-graph cover counting, new cover class,
independently new static graph extremal theorem or global novelty claim is
admitted. Shortest paths, monotone activation, binary branch reconstruction,
total covers and elementary independent-set bounds receive zero credit as
general methods. The static extremal lemma stays self-contained support for
the dynamical maximum and is not promoted as a separate new graph theorem.

## Mathematical dependency audit

**A. Permanent conflicts.** On an equal-colour edge both endpoints increment
in the same update, preserving their equality. This proves that the active
set grows and each vertex is stationary up to its first activation and
advances forever afterwards. It does not assume that all vertices of a
seeded component are active at time zero.

**B. Directed arrival.** At the first activation time $a$ of $u$, its colour
is still $x_u$. A stationary neighbor of initial colour $x_v$ meets that
clock after exactly $w_x(u,v)$ steps unless already activated earlier. This
gives the pathwise upper inequality. A first conflict at positive time $s$
cannot be between two newly active stationary vertices: their equality
would have been initial. Thus an earlier active neighbor exists; tracing
such neighbors backwards gives strictly decreasing first-conflict times
and a seed path whose summed weights equal $s$. These two inequalities
establish the shortest-distance equality, including ties and multiple seeds.
Zero-weight edges already have both endpoints seeded, so there is no
zero-cycle spontaneous activation. This closes the potential circularity
in using activation times to prove the distance formula.

**C. Entrance and sharpness.** At the last finite activation every seeded
component is wholly active; an unseeded component stays proper. Before then,
a future strict increase in the monotone active set excludes periodicity.
A shortest seed-to-nonseed path can be simple and have no later seed,
giving at most $n-2$ edges. The path source with first two colours zero and
then successive decrements has each forward weight $q-1$, so attains the
bound. The empty graph, a single vertex and a single edge have height zero.

**D. Independent inverse route.** The verifier and audit use the held set
$I=V\setminus A$: it must be independent in $H_y$, every vertex outside it
must have an outside $H_y$ neighbor, and $I$ must be successor-closed in the
arc graph. Edgewise old/target equalities prove necessity and sufficiency.
These conditions reconstruct the literal old conflict set, not merely an
overcount by arbitrary masks. Distinct masks give distinct sources. This
argument uses the target and local old-equality cases, not the arrival
distances; the two theorem axes do not collapse to one formula.

Each condition is necessary independently. Omitting cover admits active
mask $\varnothing$ for target $00$ on one edge; omitting internal neighbors
admits mask $\{0\}$ for target $01$; omitting predecessor closure admits
mask $\{1,2\}$ for target $011$ on the three-vertex path. At $q=3$, none
of their reconstructed sources has the stipulated image. All are explicit
negative controls in the verifier.

**E. Static support and equality transfer.** Let $T(H)$ count the indicated
2-total covers. The inverse yields $|F^{-1}(y)|\le T(H_y)$; a constant
target has no predecessor arcs and attains equality. The author's proof of
the universal bound is correct: a connected nonstar on at least four
vertices contains a four-vertex path; for $k\ge5$, a connected extension
excludes enough independent sets to give
$T(H)\le7\cdot2^{k-4}<2^{k-1}-1$. At $k=4$, direct independent-complement
enumeration gives star/path/paw/cycle/diamond/complete values
$7,4,6,5,6,5$. Products across components handle disconnected graphs and
forced-out isolates. At $k=3$, the triangle has four and the path three.
Finally a spanning monochromatic star (or triangle) forces the target
constant on all vertices, whence $H_y=G$; no hidden extra nonmonochromatic
edges survive in an equality case. This establishes all graph/target
maximizers. It does not establish a general counting algorithm.

## Source and value gate

[SOURCE_GATE.md](SOURCE_GATE.md) records direct primary-source passages,
literal separators and internal proof-transfer checks. It newly adds the
2018 Molinero–Riquelme–Serna total-cover counting source and explicitly
deducts it. The author accepted that boundary in
[AUTHOR_RESPONSE.md](AUTHOR_RESPONSE.md), without changing the frozen input.

The positive reason for GO is the residual conjunction: the literal
equality-triggered map has an exact source-colour-dependent activation
geometry with sharp entrance, and a separately proved target-colour mask
geometry yielding the sharp dynamical fibre and all maximizers. The known
conflict-detection model contains the update as one allowed local function,
but the inspected theorems concern a different randomized rule. CCA/GHM/FCA
do not supply these equality-triggered formulas by the tested direct
identifications. The internal equality/mex/ordered-reset/Bellman systems
also fail the explicit literal and recurrence transfer tests. This is not
GO because a search failed to find a title; it is GO on complete proofs and
surviving formula-level subtraction within the bounded owner audit.

The verdict remains modest: the static graph lemma is elementary and its
priority is not certified; the joint result may be unsuitable for a demanding
external venue. Internal short-theorem admission and external novelty are
different decisions. An exact earlier owner or a new full adapter would
reopen this gate immediately.

## Actual verification and finding census

The first independent execution passed **7,530,194 assertions**, covering
275,093 full dynamical sources with exact target source sets, 33,868 full
static graph instances and 117 sharp paths. All graph boxes are stated in
[verify_gate.py](verify_gate.py); the complete stdout is
[CANONICAL.json](CANONICAL.json). A second direct execution returned the
same full output. Two further fresh executions were compared with the saved
canonical using raw-byte `cmp`, both exit zero. Commands, interpreter,
canonical integrity and limitations are in [EXECUTION.md](EXECUTION.md).
No proof is inferred solely from the finite boxes.

Finding census: Critical 0; Major mathematical 0; one source/claim-framing
amendment accepted; current open candidate findings 0. The amendment is a
mandatory drafting boundary, not an unperformed mathematical repair.
Original theorem statements survive unchanged. The eleven workspace-root
input pins and this gate's complete nonself manifest must remain checked.
This closes only the candidate gate, not the later manuscript obligations.
