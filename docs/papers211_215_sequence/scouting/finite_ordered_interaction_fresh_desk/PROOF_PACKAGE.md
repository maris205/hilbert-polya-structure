# GBPR proof package

Author: `round211_rational_scout`, 2026-09-08 UTC.

## Claim

For the literal GBPR map in [REPORT.md](REPORT.md), the endpoint, exact
time, deepest-state classification and count, every-target one-step fibre,
image and unique maximum claimed there hold for every integer $n\ge1$.

## Status

**PROVABLE AS STATED — complete author proof; no independent acceptance.**
The value decision is separately **NO_PROMOTION_VALUE**. A correct proof
does not imply a new paper-worthy mechanism.

## Assumptions and notation

Let $V=[2n]$, $n\ge1$, and let $\mathcal M_n$ be all perfect matchings of
the complete simple graph on $V$. Each vertex has exactly one partner,
denoted $M(v)$. There are no self-pairs or parallel edges in a state. For
the literal rule, the strict edge order is the lexicographic order of
$\rho(\{i,j\})=(j-i,i,j)$ with $i<j$.

The following more general normalization is only a proof device: let
$\prec$ be **any strict total order** on the unordered pairs of $V$.
For $\{a,b\}\notin M$, call it blocking if

$$
\{a,b\}\prec\{a,M(a)\},\qquad
\{a,b\}\prec\{b,M(b)\}.
$$

If there is a blocking edge, choose the $\prec$-least one. Put
$c=M(a)$ and $d=M(b)$ and define

$$
T_\prec(M)=
\bigl(M\setminus\{\{a,c\},\{b,d\}\}\bigr)
\cup\{\{a,b\},\{c,d\}\}.
$$

With no blocking edge, set $T_\prec(M)=M$. The four vertices are distinct:
the absence of $\{a,b\}$ excludes $c=b$ and $d=a$, the no-loop rule
excludes $c=a$ and $d=b$, and $c=d$ would give that vertex two partners.
Thus the update is a deterministic self-map of the finite carrier.

Construct ordered edges $e_1,\ldots,e_n$ greedily: $e_i$ is the least edge
on the vertices not covered by $e_1,\ldots,e_{i-1}$. Put
$G=\{e_1,\ldots,e_n\}$. For $M\ne G$ write
$r(M)=\min\{i:e_i\notin M\}$. Two perfect matchings cannot differ in just
one edge, so $1\le r(M)\le n-1$.

In the overlay of $M$ and $G$, give their edges separate colours and retain
both copies of a common edge. Every vertex has one incident edge of each
colour, so every connected component is an alternating even cycle,
including a common edge as a cycle with two parallel coloured edges. Let
$c(M,G)$ be its number of components. Define
$h(M)=\min\{t\ge0:T_\prec^t(M)=G\}$ once existence is proved.
The double factorial conventions are $(-1)!!=0!!=1$.

## Strategy and dependency map

1. A forced greedy prefix identifies the selected blocking edge exactly;
   this uses strict global order and perfectness, not planar geometry.
2. Inserting that missing target edge splits one overlay cycle into two.
   Its unit component increment proves the exact clock and rigidity.
3. For a fixed target, reverse each possible insertion; earliest missing
   indices separate the cases, and a two-pair crossing choice counts them.
4. Evaluate the resulting finite sum and check the one-pair boundary.

No external theorem is required for these deductions. The source ownership
of the primitives and clock is documented in the report; this proof is not
an assertion of originality.

## Proof

### Step 1. The globally best blocking pair is the first missing greedy edge

First suppose a state $M$ contains $e_1,\ldots,e_{r-1}$. No blocking edge
can touch a vertex in this prefix. To prove this, take any nonmatching edge
$f$ touching the prefix, and choose the smallest $j<r$ for which an endpoint
of $f$ belongs to $e_j$. Both endpoints of $f$ were still present when
$e_j$ was chosen: the other endpoint cannot belong to an earlier prefix
edge by minimality of $j$. It is not the other endpoint of $e_j$, since
then $f=e_j\in M$. By the strict minimality defining $e_j$, we have
$e_j\prec f$. Its endpoint on $e_j$ therefore prefers its current partner
to $f$, so $f$ is not blocking.

If $M\ne G$, set $r=r(M)$. The endpoints $a,b$ of $e_r$ lie in the
residual vertex set, and all their current partners also lie there because
the prefix is matched internally. The edge $e_r$ is absent and is the
least edge of that residual complete graph. Its two current incident edges
are distinct from it and hence worse. Consequently $e_r$ blocks. All other
blocking edges must lie in the residual graph by the preceding paragraph,
so none can precede $e_r$. Therefore $T_\prec$ inserts exactly $e_r$.

The removed state edges cannot be any edge of $G$ already present in $M$:
each touches an endpoint of $e_r$, whereas the other edges of $G$ are
vertex-disjoint from $e_r$. Hence every already correct greedy edge is
preserved. If $M=G$, the first paragraph, applied with the whole greedy
matching, excludes every possible blocking edge. We have proved the exact
equivalent update:

$$
M\ne G:\quad T_\prec(M)\text{ inserts }e_{r(M)}
\text{ and repairs its displaced partners};\qquad T_\prec(G)=G.
$$

For the original line-distance order, the least edge on
$\{2i-1,\ldots,2n\}$ is $\{2i-1,2i\}$. Induction therefore gives exactly
$e_i=\{2i-1,2i\}$ as asserted in the literal statement.

There is also an explicit conjugacy for the general normalization. Orient
each greedy pair as $e_i=\{a_i,b_i\}$ in either fixed manner and let the
vertex permutation $\phi$ satisfy $\phi(a_i)=2i-1$ and $\phi(b_i)=2i$.
Its induced bijection on matchings preserves the first absent greedy index
and commutes with displaced-partner repair. Step 1 then gives
$\phi T_\prec=T_\rho\phi$ on the whole state space. Thus a different
strict global order supplies no new functional-graph deformation.

### Step 2. Exact clock, recurrence and extremal rigidity

Let $M\ne G$ and let the inserted edge be $e_r=\{a,b\}$. Its endpoints
belong to one alternating overlay cycle $C$, because $e_r$ is a $G$-edge.
This component has at least four vertices because $e_r$ is missing from
$M$. Write its $M$-edges incident with $a,b$ as $\{a,c\},\{b,d\}$.
Deleting these two edges and the $G$-edge $\{a,b\}$ from the cycle leaves
an alternating path from $c$ to $d$, together with isolated $a,b$.
After repair, $\{a,b\}$ is a two-coloured common edge, and the new
$M$-edge $\{c,d\}$ closes that path to a second alternating cycle.
For a four-vertex $C$, the path is the single $G$-edge $\{c,d\}$, giving
two common-edge components. No other component changes. Therefore

$$
c(T_\prec(M),G)=c(M,G)+1\qquad(M\ne G).
$$

Every component uses at least one $G$-edge, so $1\le c(M,G)\le n$;
equality $c=n$ holds exactly when each component is a common edge, that
is, $M=G$. Each nonfixed step increases this integer by exactly one.
The process must therefore first reach $G$ after exactly

$$
h(M)=n-c(M,G)
$$

steps, including $h(G)=0$. It follows that $G$ is the unique fixed and
recurrent state, all cycles have length one, and every state belongs to
its basin. The carrier size, and therefore that basin size, is
$(2n-1)!!$: choose the partner of the least remaining vertex in
$2n-1,2n-3,\ldots,1$ choices successively.

The upper bound $h(M)\le n-1$ is attained exactly for $c(M,G)=1$.
For $n\ge2$, writing $e_i=\{a_i,b_i\}$, the matching

$$
\{\{b_i,a_{i+1}\}:1\le i<n\}\cup\{\{b_n,a_1\}\}
$$

has a single alternating cycle and attains the bound. For $n=1$ the only
state $G$ also has one overlay component and attains the bound zero.

To count all deepest states, fix an orientation $a_1\to b_1$ of $e_1$.
In any single alternating cycle, begin with that oriented $G$-edge and
then follow alternately $M$- and $G$-edges. The remaining greedy edges
are encountered in a permutation of $\{e_2,\ldots,e_n\}$, each in one of
two orientations. Conversely, any such ordered and oriented list specifies
the intervening $M$-edges and closes the traversal to $a_1$, producing a
perfect matching with one overlay cycle. Fixing the initial directed edge
prevents the reverse traversal from being counted again. This is a
bijection, so the number is $2^{n-1}(n-1)!$, also one at $n=1$.

### Step 3. A complete disjoint parametrization of each inverse fibre

Fix any target $Y\in\mathcal M_n$. First suppose $Y\ne G$, and put
$r=r(Y)$. Any preimage $M$ is nonfixed. Let $i=r(M)$ be its selected
insertion index. Step 1 shows that $Y$ contains $e_1,\ldots,e_i$, so
$i<r$. If $Y=G$, the self-preimage $M=G$ exists separately; every other
preimage has an insertion index $1\le i\le n-1$.

For any allowed index $i$, the target contains $e_1,\ldots,e_i$. Choose
one of its edges

$$
f\in Y\setminus\{e_1,\ldots,e_i\}.
$$

There are $n-i$ choices. Write $e_i=\{a,b\}$ and $f=\{c,d\}$, with
any fixed orientations for the purpose of the following display. Define
two matchings by deleting $e_i,f$ from $Y$ and adding, respectively,

$$
\{a,c\},\{b,d\}\qquad\text{or}\qquad
\{a,d\},\{b,c\}.
$$

Each preserves all $e_j$ with $j<i$ and lacks $e_i$. Its first missing
index is therefore $i$, so Step 1 inserts $e_i$ and pairs the displaced
partners back to $f$. Both constructions are preimages of $Y$.

Conversely, take any nonfixed preimage $M$. Its forward repair inserts
$e_i$ and a second edge $f$ on the displaced partners. That edge cannot
be a prefix edge because those vertices were already paired internally
and unchanged. Hence $f$ belongs to exactly the target-edge set displayed
above. Reversing the two-edge replacement produces precisely one of the
two displayed pairings.

There is no multiplicity in this parametrization. Different $i$ give
different first missing indices of $M$. For fixed $i$, the partner pair
removed from $Y$ other than $e_i$ is recovered as the unique edge $f$ in
$Y\setminus M$ other than $e_i$. The two pairings for fixed $i,f$ are
different because $a,b,c,d$ are distinct. Thus every allowed $i$ yields
exactly $2(n-i)$ preimages, and all these classes are disjoint.

### Step 4. Evaluate the inverse law, image and maximum

For $Y\ne G$, Step 3 gives the evaluated polynomial

$$
|T_\prec^{-1}(Y)|
=\sum_{i=1}^{r-1}2(n-i)
=2n(r-1)-r(r-1)
=(r-1)(2n-r).
$$

For $Y=G$, add its self-preimage:

$$
|T_\prec^{-1}(G)|
=1+\sum_{i=1}^{n-1}2(n-i)=1+n(n-1).
$$

All images contain $e_1$. Conversely, a nonfixed target containing $e_1$
has $r\ge2$, so its fibre is positive by the displayed formula. The
fixed target $G$ has a positive fibre as well. The image is therefore
exactly the targets containing $e_1$. Removing that fixed pair identifies
the image with all perfect matchings on $2n-2$ vertices, so its cardinality
is $(2n-3)!!$; when $n=1$, the residual carrier has one empty matching.

For $n\ge2$ and any nonfixed target, $r\le n-1$, and the disjoint-sum
formula bounds its fibre by

$$
\sum_{i=1}^{n-2}2(n-i)=n(n-1)-2.
$$

This is three less than the fibre of $G$. Consequently $G$ is the unique
maximum. At $n=1$ there is one state and one self-preimage, so the same
uniqueness statement holds without using a nonfixed-target bound.
All claims follow. $\square$

## Corrections or missing assumptions

None are needed for the literal statement. Strictness of the global order,
complete availability of all pairs, perfect states and the explicit
displaced-partner repair are essential stated assumptions. Keeping ties,
restricting allowed pairs, dropping the repair, changing to simultaneous
updates or making the order state-dependent is outside this proof.

## Open risks and credit

No mathematical step is left as a conjecture in this author package.
However, no independent reviewer or scientific program has tested it.
The source subtraction in the report prevents rebranding a known
edge-insertion/geodesic construction as a new two-axis paper. In
particular, a degree count refined by first-missing index is a separate
inverse calculation, not evidence of a separate paper-scale mechanism.
