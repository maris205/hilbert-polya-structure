# Witt product-coordinate feedback: bounded negative proof package

## Claim and status

The prospective claim that this literal supplies two independent valued
research axes is **NOT CURRENTLY JUSTIFIED**. The weaker statements below
are **PROVABLE AS STATED**. They give a complete elementary closure reason,
not an admission contract or all-cycle theorem.

## Assumptions and notation

Let $p$ be a prime, $e\ge1$, $q=p^e$, $K=\mathbf F_q$, and $N\ge0$.
The finite carrier is $X_N=K^N$. Let
$R_N=K[x]/(x^{N+1})$. A series with constant coefficient one is a unit in
$R_N$. Write $[x^k]f$ for its coefficient of degree $k$.

Define the autonomous self-map $T_N:X_N\to X_N$ by

$$T_N(a)_k=[x^k]\prod_{d=1}^N(1-a_dx^d)^{-1},\qquad 1\le k\le N.$$

All operations are in $R_N$. In particular, $a_d$ is a field coefficient
inside the factor, not an integer exponent. When $N=0$, the carrier consists
of the empty tuple and $T_0$ fixes it. An orbit's depth is its entrance time
into the periodic core; its strict period is its least positive period once
periodic.

## Statements actually proved

1. $T_N$ is a bijection. Every state is periodic and has depth zero. At every
   time $t\ge0$, every target has exactly one time-$t$ predecessor.
2. For $N\ge1$, $T_N^{p^{N-1}}=\mathrm{id}$. Thus every strict period is a
   power of $p$ dividing $p^{N-1}$. This is a coarse general triangular bound,
   not a claim of sharpness or a cycle census.
3. The fixed locus and its cardinality are exactly

   $$\mathrm{Fix}(T_N)=\{a\in K^N:a_1=\cdots=a_{\lfloor N/2\rfloor}=0\},
   \qquad |\mathrm{Fix}(T_N)|=q^{\lceil N/2\rceil}.$$

   The same formula includes $N=0$.
4. The literal is different from the old ELD and USS maps at the explicitly
   stated finite controls below. No full-carrier conjugacy or factor theorem
   between those maps is asserted.

## Strategy and dependency map

Factor expansion gives the lower-triangular coefficient formula. Recursive
inversion proves bijectivity. A coordinate-by-coordinate characteristic-$p$
argument proves the coarse period bound for any unitriangular map with first
coordinate fixed. The least nonzero index identifies the first unavoidable
quadratic coefficient and hence the fixed locus. Direct symbolic evaluation
distinguishes ELD/USS. No finite experiment, stored pilot, inductive data fit,
or source-search non-hit is a proof premise.

The static coordinate bijection is explicitly present in Lenstra's
*Construction of the ring of Witt vectors*, Lemma 5. The old ELD proof
already reproduces its recursive factorization, and the old USS proof
already spends triangular bijectivity and singleton fibres. These mechanisms
are subtracted even though the literal updates are different.

## Proof

### Step 1. Closure and triangular coefficients

Each inverse factor is the finite truncation of the geometric series

$$ (1-a_dx^d)^{-1}=\sum_{r\ge0}a_d^r x^{dr}\pmod{x^{N+1}}.$$

It is defined over $K$ with no choice of integer lift. Expanding the finite
product gives

$$T_N(a)_k=
\sum_{\substack{r_1,\ldots,r_k\ge0\\\sum_{d=1}^k dr_d=k}}
\prod_{d=1}^k a_d^{r_d}.
\tag{1}$$

Only finitely many tuples occur. The unique summand involving $a_k$ has
$r_k=1$ and all other $r_d=0$; every other summand uses indices below $k$.
Consequently there is a polynomial $P_k$ over $K$ such that

$$T_N(a)_k=a_k+P_k(a_1,\ldots,a_{k-1}),\qquad P_1=0.
\tag{2}$$

Equation (1) also proves autonomy and carrier closure for every parameter.

### Step 2. Every target and every time have a singleton fibre

Given $b\in K^N$, set $a_1=b_1$, then for each $k=2,\ldots,N$ set

$$a_k=b_k-P_k(a_1,\ldots,a_{k-1}).\tag{3}$$

Each step uses already uniquely determined coefficients. Substitution in
(2) proves that this tuple maps to $b$; any predecessor is forced to have
these coordinates in the same order. Thus $T_N$ is bijective. A bijection
of a finite set has no nonperiodic state: for any $a$, a repeated pair
$T_N^i(a)=T_N^j(a)$ with $i<j$ can be pulled back by $T_N^{-i}$, giving
$a=T_N^{j-i}(a)$. Therefore every depth is zero. A composition of $t$
bijections, including $t=0$, is a bijection, proving the time-$t$ fibre claim.

This is precisely the coordinate-bijection / generic triangular inverse
mechanism. Formula (3) is not counted as a new independent inverse theorem.

### Step 3. Generic characteristic-$p$ period bound

We prove a more general induction. For any maps of the form (2), with
$P_1=0$, the first $k$ coordinates return identically after $p^{k-1}$ steps.
For $k=1$, the first coordinate is fixed, giving the base case.

Assume the claim for the first $k-1$ coordinates and put $M=p^{k-2}$.
During a block of $M$ updates, the first $k-1$ coordinates traverse a
deterministic closed sequence, independent of the initial $k$-th coordinate.
By (2), the net change of that coordinate over the block is a field element
$C$ depending only on those lower coordinates. At the start of the next
block the lower coordinates are the same; its net increment is again $C$.
After $p$ blocks the increment is $pC=0$ in characteristic $p$. Lower
coordinates also return. This proves the induction at $k$ and, at $k=N$,
the claimed identity for $N\ge1$.

If $a$ has strict period $\ell$, an identity iterate of exponent $M$ implies
$\ell\mid M$: write $M=u\ell+r$ with $0\le r<\ell$, then
$a=T_N^M(a)=T_N^r(a)$, so minimality forces $r=0$. The divisors of
$p^{N-1}$ are exactly powers of $p$. This bound uses no product-specific
structure beyond (2), so receives zero residual temporal credit.

### Step 4. Exact fixed locus

Suppose $a$ is nonzero and let $m$ be its least nonzero index. If
$2m\le N$, consider degree $2m$ in (1). All nonzero-index factors have
degree at least $m$. A contribution with two or more selected factors,
counting multiplicity, can have total degree $2m$ only by taking degree
$m$ twice; a factor of degree strictly between $m$ and $2m$ cannot be paired
with a positive degree below $m$. Three selections have degree at least
$3m>2m$. Thus

$$T_N(a)_{2m}=a_{2m}+a_m^2.\tag{4}$$

Because $K$ is a field and $a_m\ne0$, its square is nonzero. Equation (4)
shows $T_N(a)\ne a$. Therefore every fixed tuple has no nonzero coordinate
at or below $\lfloor N/2\rfloor$.

Conversely, assume all those coordinates vanish. Every remaining index is
strictly greater than $N/2$. A product involving two such positive degrees,
including a repeated index, has degree greater than $N$, so it vanishes
after truncation. The defining product is then

$$\prod_{d=1}^N(1-a_dx^d)^{-1}
=1+\sum_{d=1}^N a_dx^d\pmod{x^{N+1}},$$

and $a$ is fixed. Exactly $N-\lfloor N/2\rfloor=\lceil N/2\rceil$
coordinates are free, yielding the stated count. The zero tuple and empty
tuple satisfy the converse as well. The field assumption matters here;
nonzero square-zero coefficients in a general ring would defeat (4).

This fixed-locus computation is a property of the same recurrent map. It
does not furnish a second independent inverse, extremal or enumerative
mechanism after singleton fibres have been deducted.

### Step 5. Exact old-literal distinctions, not novelty claims

The old ELD carrier has $f=1+\sum_{k=1}^{m-1}a_kx^k$ and update
$f\mapsto1+xf'/f\pmod{x^m}$. At $K=\mathbf F_2$, $m=3$, its coefficient
map is $(a_1,a_2)\mapsto(a_1,a_1)$: $f'=a_1$ and the coefficient of $x$
in $f^{-1}$ is $a_1$. Its image has two states. In contrast,
$T_2(a_1,a_2)=(a_1,a_2+a_1^2)$ has four image states. These two finite
maps are not conjugate in this parameter control. This does not prove
any general separation theorem, and the shared factor-coordinate primitive
still receives zero credit.

The old USS map is $f\mapsto f(xf(x))\pmod{x^{N+1}}$. At $K=\mathbf F_2$,
$N=3$, and $f=1+x$, USS gives $1+x+x^2$, whereas the product-coordinate
feedback gives $(1-x)^{-1}=1+x+x^2+x^3\pmod{x^4}$. Thus the literal
updates differ at that input. No statement about their conjugacy is inferred
from a single different value. The generic triangular inverse proof is
nonetheless exactly the old USS mechanism.

These are hand computations, not executed test boxes. No scientific
execution or runtime authorization is inferred from having written them.

## Corrections, limits and disposition

The exponent $p^{N-1}$ is only a general bound. This desk has not proved
which higher powers of $p$ occur, their complete cycle census, an all-size
sharp order or an independently evaluated enumeration of higher-period
strata. It does not claim Lenstra studied this feedback's iteration: his
Lemma 5 owns the static bijection, whose output is identified with the
coordinate carrier here. The internal search is bounded, not exhaustive.

The singleton fibres and generic permutation core cannot rescue the missing
second axis. The exact fixed locus remains useful author deduction but does
not change that decision. Therefore close this one literal desk attempt as
`CLOSE_SOURCE_PRIMITIVE_TRIANGULAR_SINGLETON`, with zero pilots, scientific
runs, nominations, reserves or paper IDs. No larger cutoff or automatically
reopened variant is requested. $\square$
