# Proof Package — cut-intersection collapse

## Claim

For repeated independent fair vertex cuts of $K_n$, the exact absorption CDF,
first-hit law, almost-sure absorption, complete time-$t$ labelled image, every
target fibre, and labelled image-size EGF are the formulas frozen in
THEOREM_CONTRACT.md.

## Status

**PROVABLE AS REPAIRED.** The original scout's shorthand image condition
missed the case $r=R,z>0$. The proof below derives the stronger exact
condition and retains the zero-valued boundary in the fibre formula.

## Assumptions

- $n\ge2$ and $t\ge1$.
- All vertices and all time coordinates are distinguished.
- Bits are independent and fair.
- $A_R(m)$ uses the EGF boundary convention from the theorem contract.

## Notation

- $c_t(v)$ is the length-$t$ bit history of vertex $v$.
- $\bar w$ denotes bitwise complement.
- $R=2^{t-1}$.
- $r(H)$ and $z(H)$ count nontrivial complete-bipartite components and
  isolates.

## Proof Strategy

Replace the sequential intersection by an exact word representation. Prove a
labelled occupancy lemma for complementary word pairs. Use it first with no
two-sided pair to count absorption, and then after reserving oriented pairs
for the prescribed connected components to count an arbitrary target.

## Dependency Map

1. Lemma 1 is a pathwise identity and supplies the component geometry.
2. Lemma 2 is an independent labelled occupancy count.
3. The temporal theorem uses Lemmas 1--2 only at the empty target.
4. The fibre theorem also uses uniqueness of connected bipartitions and a
   no-reuse argument for isolated vertices.
5. The image-size EGF follows from the proved classification, not from the
   fibre formula or the verifier.

## Proof

### Lemma 1 — complement-history representation

For every $t\ge1$ and distinct vertices $u,v$,

\[
uv\in E(G_t)\quad\Longleftrightarrow\quad
c_t(u)=\overline{c_t(v)}.
\]

**Proof.** By the literal update, $uv$ survives through time $t$ if and only
if $b_s(u)\ne b_s(v)$ for each $s=1,\ldots,t$. Since the alphabet in each
coordinate is binary, coordinatewise inequality is exactly bitwise
complementation. $\square$

The correspondence between all cut bits and all vertex words is bijective:
both retain the same $tn$ labelled binary coordinates.

### Lemma 2 — one-sided occupancy count

Let $R$ disjoint unordered pairs of symbols be given. The number of functions
from an $m$-element labelled set to the $2R$ symbols such that no pair has
both symbols in the image is

\[
A_R(m)=m![x^m](2e^x-1)^R
=\sum_{j=0}^R(-1)^{R-j}\binom Rj2^j j^m.
\]

**Proof.** For one symbol pair, its inverse image is empty, or it is a
nonempty labelled set assigned wholly to the first symbol, or it is such a
set assigned wholly to the second. The labelled EGF is therefore

\[
1+2(e^x-1)=2e^x-1.
\]

The $R$ pairs are distinguished, so the product formula follows. Expanding
$(2e^x-1)^R$ and extracting the exponential coefficient gives the finite
sum. The same EGF gives $A_0(0)=1$, $A_0(m)=0$ for $m>0$, and $A_R(0)=1$.
$\square$

### Step 1 — temporal theorem

By Lemma 1, $G_t$ is empty if and only if no complementary word pair is
occupied on both sides. Lemma 2 counts the successful assignments, while all
$2^{tn}$ assignments are equiprobable. Since the edge sets decrease,
$\{T\le t\}=\{G_t=\varnothing\}$, and hence

\[
\Pr(T\le t)=\frac{A_{2^{t-1}}(n)}{2^{tn}}.
\]

Writing this CDF as $F_t$ and setting $F_0=0$ gives
$\Pr(T=t)=F_t-F_{t-1}$.

For any fixed edge $uv$, choose $c_t(u)$ arbitrarily. Exactly one of the
$2^t$ words for $v$ is its complement, so

\[
\Pr(uv\in E(G_t))=2^{-t}.
\]

The union bound yields

\[
\Pr(T>t)=\Pr(E(G_t)\ne\varnothing)
\le\binom n2 2^{-t}.
\]

Thus $T<\infty$ almost surely. The tail-sum identity for a positive
integer-valued random variable now gives

\[
\mathbb ET
=1+\sum_{t\ge1}
\left(1-\frac{A_{2^{t-1}}(n)}{2^{tn}}\right)
\le1+\binom n2.
\]

### Step 2 — necessity of the image class

Fix one complementary pair $\{w,\bar w\}$. Lemma 1 puts every possible edge
between the vertices with word $w$ and those with word $\bar w$, and puts no
edge within either class. If both classes are nonempty, their union is one
connected complete bipartite component. If only one class is nonempty, all
of its vertices are isolated.

There are no edges between vertices belonging to different complementary
pairs. Hence every nontrivial connected component of an image is complete
bipartite.

Two distinct nontrivial components cannot use the same complementary pair:
if they did, all cross edges between opposite sides of the proposed
components would be present and would join them. Thus their pair assignments
are injective and $r(H)\le R$.

Finally, if all $R$ pairs are consumed by nontrivial components, an additional
isolated vertex has no legal word. Using either word in a consumed pair joins
it to the nonempty opposite side. Therefore $r(H)=R$ forces $z(H)=0$.

### Step 3 — sufficiency and exact fibres

Suppose $H$ is a labelled disjoint union of $r$ nontrivial complete
bipartite components and $z$ isolates, with $r\le R$ and either $z=0$ or
$r<R$.

Each connected bipartite component has a unique bipartition up to exchanging
its two sides: graph distance from any chosen vertex determines the two
classes, and connectedness makes the determination global. Assign distinct
complementary pairs to the $r$ labelled vertex components. There are
$(R)_r$ choices. For every component, choose which colour class receives
which word of its assigned pair; there are $2^r$ choices.

No isolate may use a consumed pair, by the argument in Step 2. On the
remaining $R-r$ pairs, the isolate words must avoid occupying both sides of
any pair, since two isolates with complementary words would form an edge.
Lemma 2 gives exactly $A_{R-r}(z)$ choices.

Every assignment constructed this way yields exactly $H$ by Lemma 1.
Conversely, any word assignment yielding $H$ uniquely determines its
component-pair injection, its component orientations, and its isolate
assignment. Thus no assignment is missed or counted twice, and

\[
\#\{(b_s(v)):G_t=H\}=(R)_r2^rA_{R-r}(z).
\]

If $r=R,z>0$, this same expression is zero because $A_0(z)=0$. If the
component condition fails or $r>R$, Step 2 proves that the fibre is zero.
This establishes both the complete image characterization and every target
fibre.

### Step 4 — labelled image-size EGF

On a fixed labelled set of size $s\ge2$, the number of complete bipartite
graphs with two nonempty sides is

\[
\frac{2^s-2}{2}=2^{s-1}-1,
\]

because a nonempty proper subset chooses an ordered side and complementation
reverses the same bipartition. Therefore the labelled EGF of one nontrivial
connected component is

\[
B(x)=\frac{(e^x-1)^2}{2}.
\]

An unordered set of exactly $r$ such components has EGF $B(x)^r/r!$.
When $r<R$, any labelled set of isolates is allowed, contributing $e^x$.
When $r=R$, Step 2 permits only the empty isolate set. Summing the two
disjoint cases gives

\[
|\operatorname{im}(G_t)|
=n![x^n]\left[
 e^x\sum_{r=0}^{R-1}\frac{B(x)^r}{r!}
 +\frac{B(x)^R}{R!}\right].
\]

All claims in the frozen contract follow. $\square$

## Corrections or Missing Assumptions

- **Corrected:** $r\le R$ alone is not sufficient when isolates are present.
  The exact condition is $r\le R$ and $(z=0$ or $r<R)$.
- No further missing assumption is known.

## Open Risks

- The proof is elementary after the history encoding; ownership must be
  assessed on the exact process-and-fibre conjunction, not on proof length.
- The words labelled, nontrivial, and connected are essential to the
  $(R)_r2^r$ factor.
- The fair model makes all word assignments equiprobable. A biased model
  would require a weighted analogue and is outside this claim.
