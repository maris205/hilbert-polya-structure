# Background obstruction package

## Claim

These are elementary exclusion facts, not a new candidate theorem. If a
finite-state map is a retraction, its transient depth is at most one. In a
finite regular-star semigroup, the known map $F(x)=xx^*$ is such a retraction
onto the projections. A bijection of a finite set has no transient states
and has singleton one-step fibres.

## Status

`PROVABLE AS STATED` under the assumptions below. These facts carry zero
new-science credit and do not assert a complete inverse enumeration for
arbitrary planar diagram dynamics.

## Assumptions

- $X$ is a finite set. For the retraction assertion, $B\subseteq X$, a
  function $R:X\to X$ satisfies $R(X)\subseteq B$, and $R(b)=b$ for every
  $b\in B$.
- For the folding assertion, $S$ is a finite semigroup with associative
  multiplication and an operation $x\mapsto x^*$ satisfying
  $x^{**}=x$, $(xy)^*=y^*x^*$, and $xx^*x=x$ for all $x,y\in S$.
  These are exactly the regular-star hypotheses stated in the
  [primary body, Section 2](https://arxiv.org/html/1507.04838).
- The final assertion assumes a function $T:X\to X$ is bijective. It does
  not assume that arbitrary semigroup multiplication by a fixed element
  is bijective.

## Notation

A projection of $S$ is an element $p$ such that $p^2=p=p^*$. A state is
recurrent if it belongs to a directed cycle. Its entry time is the least
number of iterations needed to reach a recurrent state. The fibre over $y$
is the set of states mapped to $y$ in one update.

## Proof strategy

Direct substitution, followed by finite bijectivity. No numerical evidence,
enumeration algorithm, embedding or conjectured conjugacy is needed.

## Dependency map

1. The retraction conclusion depends only on the two assumptions about $R$.
2. The fold conclusion uses only the three regular-star identities and
   associativity, then the retraction conclusion.
3. The reversible-action conclusion uses only finite bijectivity.

## Proof

**Step 1: retraction.** For each $x\in X$, put $b=R(x)$. Since $b\in B$
and $R$ fixes $B$, $R^2(x)=R(b)=b=R(x)$. Conversely every $b\in B$ belongs
to the image because $b=R(b)$; thus $R(X)=B$. Its fixed points are exactly
$B$: a fixed $x$ equals $R(x)$ and therefore lies in $B$. Every state enters
$B$ by time one, with entry time zero precisely for states of $B$. If
$x\notin B$, its fibre is empty since every image lies in $B$. Nothing here
evaluates the individual fibre sizes over $B$.

**Step 2: fold.** Put $p=xx^*$. The identities give

$$p^*=(xx^*)^*=x^{**}x^*=xx^*=p,$$

and associativity and regularity give

$$p^2=xx^*xx^*=(xx^*x)x^*=xx^*=p.$$

Hence $F(S)$ consists of projections. For a projection $p$,
$F(p)=pp^*=p^2=p$. Step 1 now proves that $F$ is a retraction onto all
projections. Also $J(x)=x^*$ satisfies $J^2(x)=x$; it is an involution.
These computations reproduce background algebra; they do not establish
that a different diagram fold has the same identities.

**Step 3: finite reversible actions.** Suppose $T$ is bijective. Every $y$
has exactly one preimage by the definition of bijectivity. For $x\in X$,
finiteness yields $T^i(x)=T^j(x)$ for some $0\leq i<j$. Applying the inverse
$T^{-i}$ gives $x=T^{j-i}(x)$, so every state is recurrent with entry time
zero. This applies to a fixed geometric relabelling only after that
relabelling has actually been shown to preserve the state space and have
an inverse there.

The empty-set case in Steps 1 and 3 is vacuous; Step 2 also holds vacuously
if an empty semigroup is allowed by convention. No positive-size exception
is needed. This completes the stated background facts.

## Corrections or missing assumptions

None for the stated facts. In particular, fixed multiplication by an
arbitrary diagram is not substituted for a geometric permutation. We do
not transfer the retraction claim to $x\mapsto x^2$, sandwich products, or
power/root maps.

## Open risks

An arbitrary novel rewiring rule could evade all of these facts; none is
excluded without an exact reduction. There is no new proposed rule with
a proved independent temporal and inverse conjunction in this packet.
This is an author proof note, not an independent review or global novelty
certificate.
