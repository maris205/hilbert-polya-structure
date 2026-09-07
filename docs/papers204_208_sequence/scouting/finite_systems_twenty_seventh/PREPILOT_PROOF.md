# Pre-pilot proof boundary

Author deductions, not independent acceptance. These statements precede
the only declared pilot. Literal definitions are in INTAKE.md.

## Status and dependency map

**PROVABLE AS STATED:** SRT's all-state symmetric-threshold representation;
GCF0 closure, mass conservation, hereditary zero coordinates, invariant
positive carrier, fixed-current criterion and zero-boundary convergence.
**NOT CURRENTLY JUSTIFIED:** GCF0's complete all-parameter recurrent atlas,
any sharp global clock, or a structurally evaluated all-target inverse
extremum. Finite data are not a premise of these deductions.

Dependencies: orientation incidence identity -> symmetric threshold
adapter; bounded gcd currents -> conservation and zero barrier -> weighted
directed transport potential. No imported P208/P209 proof.

## SRT: a complete classical threshold adapter

For each pair $e=\{u,v\}$ with $u<v$, let $b_e$ have entries $+1$ at
$u$, $-1$ at $v$, zero elsewhere, and let $B$ be the matrix of these
columns. Encode the edge by $s_e=1$ for $u\to v$ and $-1$ for $v\to u$.
This is a bijection on the entire labelled tournament carrier. Its
outdegree vector is $d=((n-1)\mathbf1+Bs)/2$. Consequently
$B^{\mathsf T}Bs$ has edge coordinate $2(d_u-d_v)$.

SRT's exact update is
$$s'=\operatorname{sign}\bigl((B^{\mathsf T}B-\tfrac12 I)s\bigr).$$
If the degree difference is nonzero, its even integer term has absolute
value at least two, so the sign points from larger to smaller degree. If
the degrees tie, the remaining term is $-s_e/2$, which reverses the edge.
There is no zero sign input. The weight matrix is symmetric. Conversion
to binary bits $(s+\mathbf1)/2$ preserves symmetry, shifting only thresholds.
This is the sign-reversed version of the complete old DGO incidence
adapter in `graph_relation_second/GENERIC_PROOFS.md`, not a conjugacy
between SRT and P112 or DGO. Symmetric-threshold dynamics consumes the
proposed short-period axis. No SRT pilot or independent inverse is pursued.

P112 supplies a second mechanism warning: the first SRT image is an
ordinal sum of reversals of the original equal-score induced tournaments.
Within each old class, all external wins contribute the same offset, and
distinct old-class score intervals stay disjoint. This is P112's permanent
score-block mechanism with reversed internal blocks, not a claimed equality
of pointwise clocks or of the two full maps. The threshold adapter alone
already decides rejection, without asserting a new refinement theorem.

## GCF0: complete elementary boundary

For every $i$, $0\le g_i\le x_i$. Hence
$T(x)_i=x_i-g_i+g_{i-1}\ge0$. Summing cancels all currents, so the
total stays $N$ and the finite carrier is invariant. For $x_i=0$ both
adjacent currents vanish, so $T(x)_i=0$. Thus zero coordinates are
permanent. If every coordinate is positive, then $g_{i-1}\ge1$ and
$T(x)_i\ge g_{i-1}\ge1$, proving that GCF+ is exactly an invariant
restriction. The formulas imply $T(x)=x$ if and only if
$g_0=g_1=\cdots=g_{n-1}$, including $n=1$.
At $n=2$, the two currents are equal by symmetry of gcd and of its zero
guard, so every state is fixed.

Now assume $n\ge3$ and a coordinate $x_j=0$. It remains zero forever.
Write the remaining cyclically ordered sites as $j+1,\ldots,j+n-1$ and
define $W(x)=\sum_{k=1}^{n-1}k x_{j+k}$. The boundary currents out of
$j$ and into $j$ both vanish. Directly collecting each internal current's
coefficient gives
$$W(Tx)-W(x)=\sum_{k=1}^{n-2}g_{j+k}(x)\ge0.$$
The increase is zero exactly when every current vanishes, which is
equivalent to $T(x)=x$ because a zero coordinate already forces at least
one current to vanish. Since $0\le W\le(n-1)N$, every such state
converges to a fixed state in at most $(n-1)N-W(x)$ updates.
This is a nonsharp ordinary transport-potential bound, not a new global
clock. In this zero-boundary sector fixed support is exactly an independent
set of the cyclic adjacency relation: adjacent positive coordinates give
a positive gcd current, and every other edge has zero current.

No such boundary cut exists on the all-positive stratum. The argument
therefore does not establish all-state convergence. Even a fixed-only
original pilot would not close that gap. Conservation, a local fixed
criterion, a proper invariant restriction and a generic zero-boundary
potential cannot fill a paper seat.

## Literal/proof subtraction against earlier arithmetic rules

Old CSGD is the unguarded subtract-only $x_i-\gcd(x_i,x_{i+1})$ on a
box containing zero; it already failed carrier invariance. GCF0 has a
different, conservative incoming-minus-outgoing local rule, and a zero
guard declared before this pilot. Totality repair by itself carries no
value. Old divisor quotient $x_i/\gcd(x_i,x_{i+1})$ becomes coordinatewise
positive differences under prime valuations; GCF0 mixes additive incoming
currents and does not obey that displayed quotient identity. For example,
$T(2,3,4)=(3,3,3)$, while the quotient rule gives $(2,3,2)$, and the gcd
meet gives $(1,1,2)$. These substitutions show literal differences only;
they do not disprove every possible factor or certify novelty.

The initial global gcd need not remain fixed: the same conservative arrow
changes it from one to three. Therefore a claimed fixed-global-gcd
stratification would already be false. No alternative fixed-stratum
linearization is asserted or ruled out universally.
