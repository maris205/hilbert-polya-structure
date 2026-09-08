# CGM negative proof package

## Claim

The cyclically labelled floor-midpoint polygon map is the already-described
tagged lift of old MG. Its positive-gap factor is conservative half-sharing.
These identities hold on the whole stated carrier, not merely on its first
image or a recurrent subset. They suffice for `KILL_INTERNAL_MG_TAGGED_LIFT`.

## Status

`PROVABLE AS STATED` for the identities and distinctions below.
`NO_PROMOTION` is the author desk disposition, not manuscript acceptance.
No all-parameter sharp clock, complete recurrent classification, every-target
inverse theorem or maximum-fibre theorem is claimed or newly developed.

## Assumptions and notation

Fix integers $N\ge k\ge2$. The discrete circle is $\mathbb Z/N\mathbb Z$.
Let $X_{N,k}$ consist of tuples $(x_0,\ldots,x_{k-1})$ of distinct points
in the prescribed positive cyclic order, with labels retained. Indices are
modulo $k$. Let $g_i$ be the positive clockwise distance from $x_i$ to
$x_{i+1}$, so $g_i\ge1$ and $\sum_i g_i=N$.
Define the simultaneous map

$$T(x)_i=x_i+\lfloor g_i/2\rfloor\pmod N.$$

Let $a=x_0$ and let $\mathcal G_{N,k}$ be the positive integer compositions
of $N$ into $k$ cyclically indexed parts. Define

$$H(g)_i=\lceil g_i/2\rceil+\lfloor g_{i+1}/2\rfloor.$$

## Proof strategy and dependency map

1. Positive new gaps establish closure and preserved cyclic order.
2. The anchor/gap encoding is a full-carrier bijection and explicitly
   intertwines $T$ with a sharing map plus a translation cocycle.
3. Forgetting the label of the first point gives precisely old MG on its
   invariant cardinality-$k$ sector. Old MG's original already retains a
   tagged ancestral first point for exactly this calculation.
4. Direct substitutions distinguish the two nearest but unequal average
   rules. No unproved temporal statement is needed for the collision.

## Proof

### 1. Closure

Choose integer lifts with
$x_0<x_1<\cdots<x_{k-1}<x_0+N$ and $x_k=x_0+N$.
Subtract consecutive new lifts to obtain

$$x'_{i+1}-x'_i
=g_i+\lfloor g_{i+1}/2\rfloor-\lfloor g_i/2\rfloor
=H(g)_i.$$

The ceiling term is at least one and the floor term is nonnegative. Each
new gap is positive, and their sum telescopes to $N$. Thus the transformed
points are distinct and retain their cyclic order; $T$ is a literal finite
autonomous self-map on all of $X_{N,k}$.

### 2. Full anchor/gap coordinates

The map $x\mapsto(a,g)$ is a bijection
$X_{N,k}\longrightarrow(\mathbb Z/N\mathbb Z)\times\mathcal G_{N,k}$.
Indeed, its inverse is
$x_j=a+\sum_{i=0}^{j-1}g_i\pmod N$; positivity and total sum $N$ give
distinct points in the required order. Under this bijection,

$$T(a,g)=(a+\lfloor g_0/2\rfloor\pmod N,\ H(g)).$$

Consequently for every $t\ge0$,

$$T^t(a,g)=\left(a+\sum_{s=0}^{t-1}
\left\lfloor (H^s(g))_0/2\right\rfloor\pmod N,\ H^t(g)\right).$$

This iterate formula follows by induction from the displayed one-step
identity. It is a coordinate formula over an unspecified sharing orbit,
not an exact entrance-time theorem. The gap projection alone is many-to-one
(there are $N$ anchors), and must not be called a conjugacy to $H$.

### 3. Exact old-MG quotient and already-described lift

Let $U(x)=\{x_0,\ldots,x_{k-1}\}$. In the old MG source, each occupied
point $p$ is moved to $p+\lfloor g(p)/2\rfloor$, where $g(p)$ is the
clockwise gap to its next occupied point. Hence, point by point,

$$U\circ T=\mathrm{MG}\circ U.$$

Every $k$-point subset has exactly $k$ cyclic labelings in $X_{N,k}$,
one for each choice of $x_0$. Thus $U$ is a $k$-to-one factor map onto the
cardinality-$k$ invariant sector of MG, not a bijective conjugacy to all
old MG subsets. The old source is broader: it includes every cardinality,
the empty fixed state and the singleton rotation. Restricting to $k\ge2$
and adding persistent cyclic labels do not introduce a new local update.

Most importantly, old `algebra_fourth/OTHER_MAP_ADAPTERS.md`, MG section,
already explicitly used a tagged ancestral first point, its motion
$\lfloor g_0/2\rfloor$, and exactly $H$. The current full coordinates
therefore formalize that old adapter, rather than discover a residual
first-image or geometric time mechanism.

### 4. Correct distinctions from neighbouring literals

Old IAV is $A(g)_i=\lfloor(g_i+g_{i+1})/2\rfloor$. At the positive
two-part input $(1,2)$, $H(1,2)=(2,1)$ but $A(1,2)=(1,1)$.
In particular, $H$ conserves the total while IAV need not. No exact IAV
identity or conjugacy is asserted; only the quantized-averaging primitive
is nearby.

The old four-site CSH code keeps a floor half and receives a ceiling half
from the previous site. Its natural indexed expression is
$C(g)_i=\lfloor g_i/2\rfloor+\lceil g_{i-1}/2\rceil$.
If $L(g)_i=g_{i+1}$, direct substitution gives $H=L\circ C$, and
$C\circ L=L\circ C$. This is a commuting shift twist, not a claimed
conjugacy. The old code exhausts only its stated four-site mass-five box;
no general old experimental validation is inferred from the expression.

The Bal--DeGaetani candy rule redistributes equal shares and then adds
candy to restore divisibility. It is not the conservative $H$ rule. By
contrast, Riverbend's primary lesson explicitly gives a variation where
each person passes a floor half to the next person and keeps the ceiling
half. Numbering that receiving direction as decreasing index gives $H$
exactly. This owns the base rule, not any uninspected published theorem
about the complete labelled polygon lift.

The whole claimed collision and all stated distinctions now follow. ∎

## Corrections or missing assumptions

Do not replace an ancestral first-point label by the least current site:
crossing the cut changes which site is least and cyclically shifts gap
indices. Do not call the factor identity a first-image conjugacy or claim
that all old MG temporal theorems exist; its historical full-parameter
contract was explicitly unproved. No such theorem is required here.

## Open risks and value ceiling

This author is a proof contributor and cannot review a later CGM/MG-derived
manuscript. No new science, independent candidate gate, or global novelty
clearance occurred. The exact old lift and conservative-sharing base are
fully deducted. A hypothetical future inverse theorem cannot by itself
restore an independent new temporal mechanism for this candidate.
