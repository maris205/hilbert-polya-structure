# Ninth-lane proof and adapter notes

Author: `batch197_fosp_gate`, 2026-09-06 UTC. These are scouting deductions,
not an admitted contract or independent review. Literal carriers and all
boundary conventions are in [INTAKE](INTAKE.md); its historical LV label
is superseded by [the preserved correction](CORRECTIONS_AND_FOLLOWUP.md).

## Claim, status, assumptions and dependency map

**Claim being evaluated:** each literal has a substantive all-parameter
temporal/recurrent theorem and a separate valued inverse/extremal theorem,
after deducting known static primitives and their immediate dynamics.

**Status: NOT CURRENTLY JUSTIFIED for every prospective two-axis contract.**
The weaker propositions below are provable as stated. No finite observation
is used as an induction hypothesis. All primes are genuine primes, all
matching labels are distinct integers, and all integer-array bounds are
finite nonnegative integers with the positive-composition restrictions
from the intake. Height means the first entrance time into the periodic
core, not the length of an arbitrarily displayed orbit.

Dependency map:

1. ELD: truncated Euler differentiation and multiplicative series
   coordinates -> ghost image/fibres -> triangular permutation on image.
2. VDF: literal products -> duplicate locks and the two-coordinate linear
   slice; there is no general-prime temporal classification.
3. RHA: exact quota arithmetic -> closure; continuous reciprocal
   normalization is an involution, but does not prove rounded dynamics.
4. EPN: odd-cut matching lower bounds -> strict potential -> generic
   height bound; length-coloured target classes -> static inverse decoder.
5. QRM: extremal equality in a mean of squares -> two-step maximum drop
   -> generic consensus bound; square-sum conditioning -> encoding only.
6. QEF: linear elimination at fixed third coordinate -> degree-five
   polynomial plus singular quadratic branches -> sharp static maximum;
   diagonal restriction leaves an unclosed scalar-quadratic temporal slice.

## 1. ELD: complete ghost adapter, no independent static axis

Write $f=1+\sum_{k=1}^{m-1}a_kt^k$ over $\mathbf F_p$, and
$T(f)=1+\sum_{k=1}^{m-1}b_kt^k$. Applying $tD$ to a multiple of $t^m$
again gives a multiple of $t^m$, so the literal is independent of the
representative. The constant coefficient of $f$ is one, hence its inverse
exists in the quotient.

Step 1. Every such $f$ has a unique factorization

$$f=\prod_{d=1}^{m-1}(1-u_dt^d)^{-1}\pmod {t^m}.$$

Indeed, after choosing $u_1,\ldots,u_{k-1}$ to match all coefficients
below degree $k$, the degree-$k$ coefficient is the current value plus
$u_k$. This chooses $u_k$ uniquely, successively through degree $m-1$.
Logarithmic differentiation therefore gives

$$b_k=\sum_{d\mid k}d\,u_d^{k/d}.$$

This is the classical ghost-component coordinate change, not a new static
map. Terms with $p\mid d$ vanish; Frobenius over $\mathbf F_p$ yields
$b_{pk}=b_k$ whenever $pk<m$.

Step 2. Conversely choose the coefficients $b_k$ freely when $p\nmid k$,
and impose those equalities at all remaining indices. For $p\nmid k$ the
formula has the term $k u_k$ with nonzero coefficient, and all other terms
involve smaller $d$. Hence it determines $u_k$ successively. The $u_d$
with $p\mid d$ never appear and are arbitrary. The image is exactly

$$\mathcal G=\{1+b:b_{pk}=b_k\ (pk<m)\},$$

and every nonempty fibre has cardinality $p^{\lfloor(m-1)/p\rfloor}$.
This is a fully exposed classical adapter, not an independent valued axis.

Step 3. Comparing coefficients in $(T(f)-1)f=tf'$ gives

$$b_k=k a_k-\sum_{i=1}^{k-1}b_i a_{k-i}.$$

On $\mathcal G$, the free input coordinates are precisely the $a_k$ with
$p\nmid k$; the other coordinates are determined at smaller indices.
At each free index this equation is triangular with invertible diagonal
$k$. Therefore $T|_{\mathcal G}$ is bijective. The periodic core is all
of $\mathcal G$ and the height is zero when $m\le p$, and one when
$m>p$. This does not classify its cycles individually. For example the
fixed boxes already contain periods $6$ at $p=3$ and $20$ at $p=5$.

**Open risk / disposition:** no separate static residual survives the ghost
adapter; no all-$m,p$ individual-cycle census was proved. `NO_PROMOTION`.

## 2. VDF: elementary collision strata, no complete temporal theorem

Step 1. If $x_i=x_j$ for $i\ne j$, each corresponding product contains
a zero factor, so both output coordinates are zero. If two specified
coordinates are already zero, they stay zero at all later times. This is
a lock, not a classification of the remaining coordinates.

Step 2. At $n=1$ the map is the constant one. At $n=2$, put $d=x_1-x_2$.
The first output is $(d,-d)$, and subsequent differences obey multiplication
by $2$. Each first-image point has exactly $p$ predecessors. For odd $p$
the line is a permutation core; nonzero cycles have length
$\operatorname{ord}_{\mathbf F_p^*}(2)$ and zero is fixed. For $p=2$
the second image is zero and the maximum height is two. These are ordinary
linear/scalar dynamics, fully deducted.

Step 3. The expression is evaluation of the derivative of
$\prod_j(t-x_j)$ at its current roots, with multiplicities allowed.
Coefficient/root identities do not give a target-resolved inverse count
for arbitrary labelled targets. No transfer from canonical polynomial
derivative feedback is justified.

**Open risk / disposition:** neither general recurrence nor a separate
valued inverse/extremum is closed. Small-prime short cycles are observations
only. `NO_PROMOTION`.

## 3. RHA: exact closure does not transfer continuous involutivity

Let $K=N-n\ge0$, $w_i=1/x_i$, and
$q_i=K w_i/\sum_jw_j$. Then $q_i\ge0$ and $\sum_iq_i=K$. If
$r=K-\sum_i\lfloor q_i\rfloor$, then $r$ is an integer in
$\{0,\ldots,n-1\}$. Adding one to the $r$ largest fractional parts
(with fixed index ties) produces nonnegative integers summing to $K$.
Adding the reserved one to every coordinate proves positivity and total
$N$; the literal is autonomous and closed even when $K=0$.

On the *continuous* probability simplex, the map
$\Phi(u)_i=(1/u_i)/\sum_j(1/u_j)$ satisfies $\Phi^2(u)=u$: if
$S=\sum_j1/u_j$, then $1/\Phi(u)_i=S u_i$, and normalizing cancels $S$.
RHA includes reserved units and state-dependent rounding, so this identity
does not establish $T^2=\mathrm{id}$ or eventual two-periodicity for RHA.
Indeed the pilot has positive heights, including height ten at
$(n,N)=(3,17)$. All observed cycles have length one or two, but no
all-$n,N$ proof of that observation was found.

**Open risk / disposition:** Hamilton's static allocation rule is entirely
classical; no rounded all-parameter clock or evaluated inverse extremum is
proved. `NO_PROMOTION`.

## 4. EPN: generic descent and static coloured decoder

### 4.1 Strict length potential

Fix a length class and list its $2k$ vertices as
$s_1<\cdots<s_{2k}$. For any matching on these vertices, let $c_j$ be the
number of edges crossing the cut after $s_j$. Then its total length is
$\sum_{j=1}^{2k-1}c_j(s_{j+1}-s_j)$. Counting vertices on the left gives
$c_j\equiv j\pmod2$. Thus every odd-indexed cut has $c_j\ge1$; every
even-indexed cut has $c_j\ge0$. Pairing consecutive vertices realizes
exactly these lower bounds.

Equality forces no edge across any even cut. The first two vertices must
therefore be paired; removing them and continuing forces every consecutive
pair. Since all gaps are positive, this is the unique minimizer. If the
old matching differs inside any class, its replacement has strictly
smaller total length. The new global matching is the union of these class
replacements because every class has even cardinality.

For a matching on $2n$ consecutive integer labels, its length $L$ satisfies
$n\le L\le n^2$. The lower bound uses $n$ positive edge lengths. For the
upper bound, write $L$ as the sum of high endpoints minus low endpoints;
this is at most the sum of the largest $n$ labels minus the smallest $n$,
which is $n^2$. Also
$L\equiv\sum_{v=0}^{2n-1}v\equiv n\pmod2$. Each nonfixed update
therefore drops $L$ by at least two. All recurrence is fixed and

$$h(M)\le\frac{L(M)-n}{2}\le\binom n2.$$

This is generic repeated within-class minimum matching, not a sharp clock.

### 4.2 Exact inverse decoder, not an evaluated extremum

For a fixed target matching $Y$, assign a label
$\ell(e)\in\{1,\ldots,2n-1\}$ to each target edge. For every label
$\ell$, let $S_\ell$ be the union of the endpoints of edges assigned
$\ell$. Impose two tests:

1. The assigned target edges are precisely the consecutive pairs of the
   increasing list $S_\ell$.
2. The graph on $S_\ell$ with edges $\{u,v\}$ satisfying
   $|u-v|=\ell$ has every connected component of even order.

That graph is a disjoint union of paths: within each residue modulo
$\ell$, successive present vertices at gap $\ell$ form a path, with
missing positions breaking paths. An even path has exactly one perfect
matching, forced successively at its endpoints. Hence each passing colour
assignment gives exactly one old matching, formed by these path matchings.
Its edges have exactly their assigned lengths, so the forward map returns
$Y$. Conversely every predecessor supplies its own unique old length to
both endpoints of each target edge and therefore passes these tests.

Consequently the full fibre size is the number of passing assignments.
This is a static length-coloured matching decoder with as many as
$(2n-1)^n$ assignments; no evaluated all-$n$ extremum follows.

### 4.3 Exact nearby static overlap

Let $E(M)$ be the historical EDR rank-relabelled old matching and let
$I=\{\{0,1\},\{2,3\},\ldots\}$. Then

$$T_{\rm EPN}(M)=M\quad\Longleftrightarrow\quad E(M)=I.$$

Both statements say that every old edge joins consecutive vertices in the
global list sorted by old edge length and then vertex. This is a direct
static adapter for the EPN fixed-set census. It is not claimed to conjugate
the two full dynamics. The finite value $3871$ at $n=6$ belongs to this
old EDR identity-fibre statistic, so it receives no independent credit.

**Open risk / disposition:** the observed heights $0,1,1,2,3,4$ and
maximum fibres $1,2,5,12,33,95$ are not all-$n$ formulas. Generic descent,
an unevaluated coloured decoder, and a transferred fixed census do not
provide two valued axes. `NO_PROMOTION`.

## 5. QRM: generic quantized consensus and square-sum encoding

For $n=1$ the map is identity. For $n=2$ it swaps the coordinates exactly.
Assume $n\ge3$. If $a=\min_i x_i$ and $b=\max_i x_i$, then each
average of squares lies in $[a^2,b^2]$. Therefore all outputs lie in
$[a,b]$; the minimum cannot decrease and the maximum cannot increase.

An output coordinate can equal $b$ only if all of its $n-1$ input
neighbors equal $b$: one smaller square makes the mean strictly below
$b^2$, and its square-root floor is at most $b-1$. If at least two input
coordinates are below $b$, every output is below $b$. If exactly one is
below $b$, only that index can have output $b$; all other $n-1\ge2$
outputs are below $b$, so the following step has maximum below $b$.
Thus every nonconstant configuration loses at least one unit of maximum
within two steps. Constants are fixed, and

$$h(x)\le2(\max_i x_i-\min_i x_i)\le2M.$$

For a target $y$, conditioning on $S=\sum_i x_i^2$ gives the exact
but unevaluated encoding

$$|T^{-1}(y)|=\sum_{S=0}^{nM^2}[z^S]
\prod_{i=1}^n\left(
\sum_{\substack{0\le u\le M\\
(n-1)y_i^2\le S-u^2<(n-1)(y_i+1)^2}}z^{u^2}\right).$$

Every monomial chosen in the product has total exponent $S$ exactly when
the selected coordinates have the conditioned square sum. The inequalities
are precisely the definition of the output floors. This proves the
encoding, not a uniform closed form or maximizing-target theorem.

**Open risk / disposition:** convergence uses the generic loss of an
extremal quantized mean; neither a sharp clock nor an evaluated inverse
extremum was established. `NO_PROMOTION`.

## 6. QEF: a sharp static inverse survives; temporal axis does not

### 6.1 Complete inverse formula for odd primes

Fix output $(a,b,c)$. For a proposed third input coordinate $z$, the first
two equations are $x+zy=a$, $zx+y=b$.
When $z\ne\pm1$, their determinant is $1-z^2\ne0$, so

$$x=\frac{a-zb}{1-z^2},\qquad
y=\frac{b-za}{1-z^2}.$$

The remaining equation is equivalent to

$$P(z)=(c-z)(1-z^2)^2-(a-zb)(b-za)=0.$$

This polynomial has degree exactly five, with leading coefficient $-1$.
At $z=r\in\{1,-1\}$, consistency requires $b=ra$. In that case
$y=r(a-x)$ and the last equation is

$$x^2-a x+rc-1=0.$$

With $\chi$ the quadratic character of $\mathbf F_p$, including
$\chi(0)=0$, the complete fibre formula is

$$|T^{-1}(a,b,c)|=
\#\{z\notin\{1,-1\}:P(z)=0\}
 +\mathbf1_{b=a}(1+\chi(a^2-4c+4))
 +\mathbf1_{b=-a}(1+\chi(a^2+4c+4)).$$

If $b=ra$, both terms in $P$ are divisible by $(z-r)^2$. Therefore
each consistent singular branch uses at least two of the five root
multiplicities of $P$ and supplies at most two predecessors. Each regular
root uses at least one multiplicity and supplies exactly one predecessor.
Inconsistent singular branches supply none and are not roots of $P$.
The sum of the used multiplicities is at most five, proving

$$|T^{-1}(a,b,c)|\le5.$$

At the zero target, $P(z)=-z(1-z^2)^2$. The regular root $z=0$
gives $(0,0,0)$; each singular branch has quadratic $x^2-1=0$ and
gives two points. Equivalently the four nonzero predecessors are the sign
triples in $\{1,-1\}^3$ with product $-1$. Hence the maximum is exactly
five over **every odd prime field**.

The formula also characterizes equality without pretending to enumerate
all maximizing targets in closed form: every regular root of $P$ must
be simple and rational; each singular root must have multiplicity exactly
two and its branch quadratic must have two distinct rational roots; all
five root multiplicities must be accounted for. These conditions are
necessary by the multiplicity bound and sufficient by the formula.

### 6.2 Characteristic two and temporal limitations

Over $\mathbf F_2$, the zero vector and all three weight-one vectors
are fixed. Every weight-two vector maps to $(1,1,1)$, which maps to zero.
Thus the maximum fibre is three, uniquely at $(1,1,1)$, and the height
is two. This is a full eight-state elementary boundary analysis.

For any prime, a fixed point satisfies $yz=xz=xy=0$, so at most one
coordinate is nonzero. There are exactly $3p-2$ fixed points. Also

$$T_1-T_2=(x-y)(1-z),$$

which is only a pair-difference factor. Crucially the invariant diagonal
satisfies

$$T(t,t,t)=(t+t^2,t+t^2,t+t^2).$$

It already contains the ordinary scalar quadratic iteration over every
prime field. No proof here classifies the full-core periods or heights,
including that diagonal stratum. Fixed counts and a complete static
degree-five elimination do not supply the missing all-prime temporal axis.
The inverse maximum uses generic elimination/root multiplicity plus an
elementary zero-target witness; global priority is not claimed.

**Open risk / disposition:** `NO_PROMOTION`. The new static deduction was
checked by a separately written decoder only in the original six fields;
its all-prime proof is the argument above, not the finite checks.

## Final feasibility conclusion

All six proposed two-axis claims are **NOT CURRENTLY JUSTIFIED**. We have
not disproved that some future substantially different theorem could be
proved for these literals. We have closed this bounded intake without
reserves or admissions. Sharp matching clocks, rounded reciprocal
two-periodicity and uniform QRM extrema remain unproved and are not
promised as future paper contracts.
