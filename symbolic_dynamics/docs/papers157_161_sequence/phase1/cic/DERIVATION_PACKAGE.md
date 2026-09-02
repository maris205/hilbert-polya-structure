# Derivation Package — cut-intersection collapse

## Target

Derive an exact all-time absorption law and a logically stronger, complete
labelled image and inverse-fibre atlas for repeated intersections of
independent fair vertex cuts of $K_n$.

## Status

**COHERENT AFTER BOUNDARY REPAIR.** The initial scout omitted the exceptional
case $r=R,z>0$ from its prose image criterion. The fibre formula was already
correct because $A_0(z)=0$ for $z>0$. The theorem statement is now repaired.

## Invariant Object

The invariant object is the complementary-pair occupancy profile of the
length-$t$ vertex histories. An edge survives precisely across the two sides
of one occupied complementary pair. Temporal absorption asks whether every
pair is one-sided; the inverse problem fixes several two-sided pairs and asks
the same avoidance question on the unused pairs.

## Assumptions

- $n\ge2$ and $t\ge1$.
- Vertices are labelled.
- All $tn$ sampled bits are independent and fair.
- A nontrivial complete bipartite component has both sides nonempty.
- An isolated vertex is a component of order one, not a degenerate
  complete-bipartite component.
- Exhaustive enumeration is not a proof premise.

## Notation

- $W_t=\{0,1\}^t$.
- $\bar w$ is the bitwise complement of $w$.
- $R=2^{t-1}$ is the number of unordered pairs $\{w,\bar w\}$.
- $A_R(m)$ counts assignments of $m$ labelled vertices to $2R$ words for
  which no complementary pair is occupied on both sides.
- $(R)_r$ is the falling factorial.

## Derivation Strategy

Encode all cuts at once by one history word per vertex. This converts edge
survival into the deterministic complement relation. Count one-sided
occupancies by labelled exponential generating functions or
inclusion--exclusion. For a fixed target graph, assign a distinct
complementary pair and an orientation to every nontrivial component; then
count isolated vertices on the unused pairs by the same avoidance function.

## Derivation Map

1. Intersecting the epoch cuts gives the pathwise complement identity.
2. Empty graphs correspond exactly to one-sided occupancy in every
   complementary pair.
3. The labelled set construction for one pair has EGF $2e^x-1$.
4. Nonempty connected components are exactly the occupied two-sided pairs and
   hence complete bipartite.
5. A fixed component consumes one pair and has two orientations.
6. Isolates cannot use any consumed pair; the remaining assignment is an
   $A_{R-r}(z)$ avoidance problem.
7. The unused-pair boundary yields the corrected attainability condition.

## Main Derivation

### Step 1 — collapse all time coordinates into history words

An edge $uv$ is retained at every epoch up to $t$ exactly when

\[
b_s(u)\ne b_s(v)\qquad(1\le s\le t).
\]

Coordinatewise inequality of binary words is equivalent to bitwise
complementation, so

\[
uv\in E(G_t)\iff c_t(u)=\overline{c_t(v)}.
\]

This identity is pathwise and loses no probability information: a cut history
is the same data as the word assignment $v\mapsto c_t(v)$.

### Step 2 — one-sided complementary-pair occupancy

For one complementary pair, an admissible labelled set of vertices is either
empty, a nonempty set using the first word, or a nonempty set using the second
word. Its labelled EGF is

\[
1+2(e^x-1)=2e^x-1.
\]

For $R$ independent pairs, the EGF is $(2e^x-1)^R$. Therefore

\[
A_R(m)=m![x^m](2e^x-1)^R.
\]

Expanding the power gives

\[
A_R(m)=\sum_{j=0}^R(-1)^{R-j}\binom Rj2^j j^m.
\]

The EGF directly fixes all empty-carrier boundaries, including
$A_0(0)=1$ and $A_0(m)=0$ for $m>0$.

### Step 3 — temporal law

The graph is empty at time $t$ exactly when no complementary pair has both
sides occupied. There are $2^{tn}$ word assignments, hence

\[
\Pr(T\le t)=\Pr(G_t=\varnothing)
=\frac{A_{2^{t-1}}(n)}{2^{tn}}.
\]

Since the graphs form a decreasing edge sequence, consecutive CDF
differences give the first-hit distribution.

For a fixed edge, the second history word must be the unique complement of
the first, so its survival probability is $2^{-t}$. A union bound gives

\[
\Pr(T>t)\le\binom n2 2^{-t}.
\]

This proves almost-sure absorption and convergence of the displayed exact
mean series.

### Step 4 — classify positive-time images

For each complementary pair $\{w,\bar w\}$, the vertices using $w$ are
adjacent to all vertices using $\bar w$ and to no others. If both sides are
nonempty, they form one connected complete bipartite component. If only one
side is occupied, all its vertices are isolated. Different complementary
pairs have no edges between them.

Thus every image is a disjoint union of nontrivial complete bipartite
components and isolates. Conversely, give each nontrivial component a
distinct complementary pair and send its two unique bipartition classes to
the two words. Remaining isolates may be assigned to unused word pairs as
long as no pair is used on both sides.

### Step 5 — fixed-target fibre

Let the fixed target have $r$ nontrivial components and $z$ isolates.
The complete bipartition of a connected complete bipartite graph is unique up
to swapping its sides. Therefore:

- $(R)_r$ injectively assigns complementary pairs to the labelled
  components;
- $2^r$ orients their two bipartition classes;
- $A_{R-r}(z)$ assigns the labelled isolates on unused pairs without
  accidentally creating an edge.

Multiplication gives

\[
(R)_r2^rA_{R-r}(z).
\]

An isolate cannot use a word in a consumed pair: whichever side it chooses,
it becomes adjacent to the nonempty opposite side of that component. This is
the point that makes the factorization exact.

The labelled EGF of one nontrivial connected complete bipartite graph is

\[
B(x)=\frac{(e^x-1)^2}{2},
\]

because its two nonempty colour classes are unordered. Components form a
labelled set. Allowing arbitrary isolates for $r<R$, but no isolate for
$r=R$, gives the independent image census

\[
n![x^n]\left[
e^x\sum_{r=0}^{R-1}\frac{B(x)^r}{r!}
+\frac{B(x)^R}{R!}\right].
\]

### Step 6 — corrected attainability boundary

The fibre is positive precisely when the graph has the stated component
class, $r\le R$, and $A_{R-r}(z)>0$. The last condition is automatic for
$z=0$. For $z>0$, it is equivalent to $R-r\ge1$. Hence the exact image
condition is

\[
r\le R\quad\hbox{and}\quad(z=0\ \hbox{or}\ r<R).
\]

At $n=5,t=2$, two independent edges plus one isolate violate this condition.
This counterexample is included in the frozen theorem contract.

## Remarks and Interpretation

- The absorption formula is the zero-component specialization of a broader
  labelled inverse atlas, but its all-time interpretation and tail control
  remain a distinct temporal theorem axis.
- The process is not a generic random intersection graph: shared labels do
  not create edges; exact complementary histories retain them.
- The image class is static and elementary after the encoding. The residual
  paper value lies only in its conjunction with the stochastic process,
  all-time law, and every-target history fibres.

## Boundaries and Non-Claims

- No credit is assigned to graph cuts, binary word coding, complete
  bipartite graph terminology, labelled EGFs, or inclusion--exclusion.
- The fair-bit model is frozen; biased or correlated cuts are not claimed.
- The graph is labelled; no quotient by graph automorphisms occurs.
- A bounded literature non-hit is not novelty evidence.
- The verifier checks finite windows only.

## Open Risks

- A direct source may use different language such as antipodal word graph,
  bipartite cluster graph, separating family, or cut-space intersection.
- Hostile review must check whether the full fibre conjunction, rather than
  only the component classification, has a direct owner.
- Any manuscript compression that drops $A_0(z)$ or the $r=R,z>0$ example
  can reintroduce the repaired error.
