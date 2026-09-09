# R2-PC-L: scheme-level trace detection and the remaining radical gap

## Claim

Retain the [frozen original question](FROZEN_CONTRACTS.md): for every
odd prime $p$, every $c\in k=\overline{\mathbb F}_p$, and every
$h\in k[x]$, is vanishing of all ordinary primitive $f_c$-orbit sums
equivalent to $h=Q\circ f_c-Q$ for one $Q\in k[x]$, where
$f_c(x)=x^2+c$? If not, the alternative requires a complete uniform
description of the defect $K_c/B_c$.

## Status

**NOT CURRENTLY JUSTIFIED for the original complete question.**
The full quantifiers have not been weakened. This package proves a new
all-parameter scheme-level detection lemma, formulates the exact residual
nilpotence issue, derives the coordinator's sufficient multiplicity
criterion, and checks why a first Jacobian shortcut does not close it.
A rational-transfer regularity lemma is also proved, but no rational
transfer is constructed from ordinary orbit data.

These are current-team hand proofs, not a paper admission or a formal
evaluation. No mathematical program, finite-field census or old
certificate was run. The earlier set-function, interpolation,
normal-form and Frobenius helpers are inputs, not new results here.

## Assumptions and notation

- $p$ is odd, $k=\overline{\mathbb F}_p$ and $c\in k$ throughout.
- All polynomial coefficients belong to $k$, with no degree bound on
  the original $h$.
- $\Delta_cQ=Q\circ f_c-Q$, and $K_c,B_c$ have exactly the meanings
  in the frozen contract; primitive sums count distinct ordinary points.
- The [previous proof package, Step 4](../../positive_characteristic/PROOF_PACKAGE.md)
  gives the vector-space decomposition
  $$
  k[x]=B_c\oplus V,\qquad V=k\oplus xk[x^2].
  $$
  Write $h=\Delta_cQ+v$ with this unique $v\in V$.
- For an integer $n\geq1$, put
  $$
  F_n(x)=f_c^{\circ n}(x)-x,\qquad
  H_n(h)(x)=\sum_{i=0}^{n-1}h(f_c^{\circ i}(x)).
  $$
  The integer $n$ in a scalar coefficient is interpreted in $k$.

## Proof strategy

Use the full cyclic complete-intersection algebra before passing to its
reduction. Its squarefree monomial basis makes the leading binary
support of an odd-degree polynomial visible uniformly in $c$.
Ordinary orbit data then places the nonzero trace in the nilradical,
which is the step that remains unresolved. Separately, pole propagation
rules out poles in any rational solution that actually exists.

## Dependency map

1. The cyclic algebra is a univariate iterate quotient by elimination.
2. Degree-lowering square reductions and its known dimension give the
   complete squarefree basis, without a radicality assumption.
3. A weighted local reduction and separation of circular windows prove
   nonvanishing of a trace with a nonzero odd leading term.
4. Ordinary-root vanishing is equivalent to nilpotence in the finite
   iterate quotient, not zero in that quotient.
5. Frobenius kills each nilpotent trace once its exponent reaches the
   maximum root multiplicity, giving an exponential necessary lower
   bound if a nonzero defect exists.
6. Derivative annihilation is necessary for root vanishing, but its
   converse can fail at multiplicities divisible by $p$.
7. Rational regularity uses finite polar divisors and the degree-two
   pullback, independently of the unproved existence implication.

## Proof

### Step 1. The full cyclic algebra and its basis

Let indices below be taken modulo $n$, and define
$$
A_n=
k[X_0,\ldots,X_{n-1}]/
(X_i^2+c-X_{i+1}:0\leq i<n).
$$
There is an isomorphism
$$
A_n\simeq k[x]/(F_n),\qquad X_i\longmapsto f_c^{\circ i}(x).
\tag{1}
$$
Indeed, the first $n-1$ relations express every $X_i$ as
$f_c^{\circ i}(X_0)$, and the final relation is precisely $F_n(X_0)=0$.
The indicated substitution and $x\mapsto X_0$ give inverse maps.
Since $F_n$ is monic of degree $2^n$, $\dim_k A_n=2^n$.

The $2^n$ squarefree monomials
$$
X^E=\prod_{j\in E}X_j,\qquad E\subseteq\{0,\ldots,n-1\},
\tag{2}
$$
form a basis. To prove spanning, replace any factor $X_i^2$ by
$X_{i+1}-c$. Each resulting term has strictly smaller ordinary total
degree than the term replaced, including when the index wraps from
$n-1$ to $0$. Repeated replacement terminates at squarefree monomials.
There are exactly $2^n$ of them, equal to the dimension from (1), so
spanning also proves linear independence. This argument concerns the
full algebra, not its reduced quotient.

Under (1), the class of $H_n(h)$ is
$\sum_{i=0}^{n-1}h(X_i)$. Also
$$
H_n(\Delta_cQ)=Q(f_c^{\circ n}(x))-Q(x)\equiv0\pmod{F_n}.
\tag{3}
$$
Consequently the class of $H_n(h)$ in $A_n$ depends only on $v$.

### Step 2. The all-parameter binary-support lemma

**Lemma.** Suppose
$$
v(x)=a_0+\sum_{\substack{1\leq d\leq D\\d\text{ odd}}}a_dx^d,
\qquad a_D\ne0,
$$
so $D\geq1$ is odd. Put $m=\lfloor\log_2D\rfloor$.
For every integer $n>2m$, every allowed $p$ and every $c\in k$,
$$
\sum_{i=0}^{n-1}v(X_i)\ne0\quad\text{in }A_n.
\tag{4}
$$
No condition $p\nmid n$ or squarefreeness of $F_n$ is needed.

**Proof.** First fix a starting index $i$. Reduce $X_i^d$, with
$d\leq D<2^{m+1}$, in the unwrapped window
$$
X_i,X_{i+1},\ldots,X_{i+m}.
$$
Give $X_{i+j}$ weight $2^j$. Replacing
$X_{i+j}^2$ by $X_{i+j+1}$ preserves weight, whereas choosing the
constant term $-c$ strictly decreases it. Every term at every stage
therefore has weight at most $d$. A square of the final variable
$X_{i+m}$ would have weight at least $2^{m+1}>d$ and cannot occur.
Thus this reduction never leaves the indicated window or wraps back
to its beginning. The assumption $n>2m$ ensures the window has distinct
variables, except that $m=0$ is already the single-variable case.

Choose a deterministic square-reduction order, for example the smallest
local index with exponent at least two. The unique branch that never
chooses a constant term performs ordinary binary carries on $d$ and
ends at
$$
\prod_{j\in E_d}X_{i+j},\qquad
E_d=\{j:\text{the }j\text{th binary digit of }d\text{ is }1\},
\tag{5}
$$
with coefficient $1$ and weight $d$. Every other branch has strictly
smaller weight. This proves that (5) is the unique weight-$d$ term in
the reduced expression for $X_i^d$, even when some lower coefficients
cancel in characteristic $p$.

Now examine the coefficient of the target squarefree monomial
$$
M_D=\prod_{j\in E_D}X_j
\tag{6}
$$
in the complete sum in (4). As $D$ is odd, $0\in E_D$, and by the
choice of $m$, $m\in E_D$. For $m\geq1$, the support thus contains
both endpoints $0$ and $m$. Among circular intervals of $m+1$
consecutive indices, only the interval $0,1,\ldots,m$ contains both:
the other directed distance between these endpoints is $n-m>m$.
Hence the only local window capable of contributing (6) is the one
starting at $i=0$. When $m=0$, the target is $X_0$ and the same
uniqueness holds because each window consists of a single index.

Within that window, $M_D$ has weight $D$. Terms from smaller exponents
have weight strictly below $D$; the reduction of $a_DX_0^D$ contributes
exactly $a_D$. The constant term contributes only to the empty-support
basis element. Thus the coefficient of $M_D$ in (4) is $a_D\ne0$.
Linear independence in (2) proves the lemma. $\square$

This proves nonvanishing for **every parameter $c$ and every polynomial
degree**, in the full algebra. It is not merely the monomial-map
necklace argument at $c=0$: all lower terms produced by $c$ were included
and controlled by their weight. It is also not yet ordinary-point
nonvanishing.

### Step 3. Exact conversion of ordinary orbit data

Let $\operatorname{Nil}(A_n)$ denote the nilradical of $A_n$, and let
$\operatorname{rad}(F_n)$ be the monic product of the distinct linear
factors of $F_n$ over $k$. Then
$$
h\in K_c
\quad\Longleftrightarrow\quad
\operatorname{rad}(F_n)\mid H_n(h)\text{ for every }n\geq1
\quad\Longleftrightarrow\quad
[H_n(h)]\in\operatorname{Nil}(A_n)\text{ for every }n\geq1.
\tag{7}
$$
For the first equivalence, a root of $F_n$ has some primitive period
$r\mid n$, and its $n$-step sum is $(n/r)S_h(O)$. If all primitive
sums vanish, every such value vanishes. Conversely, take $n=r$ for each
primitive orbit. The coefficient is then $1$, also when $p\mid r$;
no division by its period occurs.

For the second equivalence, factor
$F_n=\prod_a(x-a)^{e_a}$. A class of a polynomial $W$ is nilpotent
exactly when $W(a)=0$ for every root: necessity follows by evaluating
a power of $W$ at $a$; for sufficiency, $W^{\max_a e_a}$ is divisible
by $F_n$. This proves (7) without replacing ordinary points by scheme
lengths.

Combining (3), (4) and (7) gives the following **necessary condition
for a defect**. If $h\in K_c\setminus B_c$, its normal representative
cannot be a nonzero constant, since $f_c$ has a fixed point over $k$.
It therefore has a positive odd leading degree $D$, and
$$
0\ne[H_n(v)]\in\operatorname{Nil}(A_n)
\quad\text{for every }n>2\lfloor\log_2D\rfloor.
\tag{8}
$$
In particular, $F_n$ must be non-squarefree for every such $n$.

A conditional consequence is: **if $F_n$ is squarefree for arbitrarily
large $n$, then $K_c=B_c$**. Given a nonzero positive-degree normal
representative, choose one of those $n$ beyond the bound in (8); its
algebra is reduced, contradicting (8). Constants were already excluded.

The additional squarefreeness hypothesis is not established for all
$c$, and cannot simply be imposed on the frozen problem. For example,
at $c=1/4$ the fixed point $a=1/2$ has multiplier $1$. Thus
$F_n(a)=F_n'(a)=0$ for every $n$, so no full iterate polynomial in this
subfamily is squarefree. This observation does not demonstrate a defect;
it demonstrates the limitation of this sufficient condition.

### Step 4. A multiplicity criterion supplied by the coordinator's route

The coordinator suggested applying Frobenius after killing the nilradical.
The following is the exact implication; no general multiplicity estimate
is assumed. Let $M_n=\max_a e_a$ be the largest ordinary root multiplicity
of $F_n$, and let
$$
q_n=p^{\lceil\log_p M_n\rceil}.
$$
Thus $M_n\leq q_n<pM_n$, including $M_n=1$.

If $v\in K_c$ has positive odd degree $D$, (7) implies
$[H_n(v)]^{q_n}=0$ in $A_n$. In characteristic $p$,
$$
H_n(v)^{q_n}=H_n(v^{q_n}).
$$
The polynomial $v^{q_n}$ still belongs to $V$, since $q_n$ is odd,
and its degree is exactly $Dq_n$. No second polynomial reduction or
transfer-degree estimate is needed. Step 2 would contradict its zero
trace whenever $n>2\lfloor\log_2(Dq_n)\rfloor$. Consequently any
nonzero defect would require, for every $n\geq1$,
$$
Dq_n\geq 2^{\lceil n/2\rceil},\qquad
M_n>\frac{2^{\lceil n/2\rceil}}{pD}.
\tag{9}
$$

In particular, the following sufficient condition would close the
original equality for a given $p,c$:
$$
\liminf_{n\to\infty}\frac{M_n}{2^{n/2}}=0.
\tag{10}
$$
If (10) holds, choose a sufficiently large $n$ with
$pD M_n<2^{n/2}\leq2^{\lceil n/2\rceil}$, contradicting (9).
The case of a constant normal representative is already excluded by a
fixed point. This proves the conditional implication, not (10).

A uniform characteristic-zero parabolic-petal estimate is not imported
into positive characteristic. An actual suitable multiplicity bound
for every allowed $p,c$, or a different reduced detection argument,
remains necessary. This route also does not require that the full
iterate polynomial ever be squarefree.

### Step 5. A necessary Jacobian condition and its actual failure mode

If $W$ vanishes at every root of $F_n$, then
$$
F_n\mid F_n'W.
\tag{11}
$$
At a root of multiplicity $e$, differentiation gives vanishing order
at least $e-1$ for $F_n'$, even if $e$ becomes zero as a scalar in $k$.
Multiplication by $W$, whose order is at least one, reaches order $e$.
This proves (11) separately at every root.

By the chain rule, under (1) the derivative is
$$
J_n=2^n\prod_{i=0}^{n-1}X_i-1.
$$
Thus the original orbit condition implies
$$
J_n\sum_{i=0}^{n-1}v(X_i)=0\quad\text{in }A_n
\quad\text{for every }n.
\tag{12}
$$
This suggests studying multiplication by the full product on the local
binary-support trace subspace. No proof excluding a nonzero normal
representative from all the kernels in (12) is established here.

More importantly, (11) is not an equivalent replacement for ordinary-root
vanishing at a fixed level. A complete hand example is
$p=3$, $c=0$, $n=6$, $h(x)=x$. In this case
$$
F_6=x^{64}-x=x(x^7-1)^9,\qquad
F_6'=x^{63}-1=(x^7-1)^9.
$$
Since $H_6(x)=\sum_{i=0}^{5}x^{2^i}$ is divisible by $x$,
$F_6\mid F_6'H_6$. Nevertheless $H_6$ does not vanish at every root.
The six nontrivial seventh roots of unity are distinct in characteristic
three and form two primitive length-three orbits under squaring, because
$2$ has order $3$ modulo $7$. Their two orbit sums add to $-1\ne0$,
so at least one has nonzero sum. On that orbit the six-step sum is twice
the primitive sum and is nonzero in characteristic three.

Consequently the Jacobian can annihilate a nonnilpotent trace. This
refutes the single-level implication from (12) back to (7), not the
possibility that an additional all-level argument might still work.
The example is not a candidate defect in $K_c/B_c$ and was not produced
by a program.

### Step 6. Rational transfers, if supplied, have no finite poles

**Lemma.** If $Q\in k(x)$ and $Q\circ f_c-Q\in k[x]$, then
$Q\in k[x]$.

**Proof.** Let $D_Q$ be the effective divisor of finite poles of $Q$,
with each pole counted with its positive order. Because $f_c$ is a
polynomial, every preimage of a finite point is finite, and the finite
polar divisor of $Q\circ f_c$ is $f_c^*D_Q$.

At each finite point, the difference has no pole. If one summand had a
pole and the other did not, or if their pole orders differed, its
highest negative Laurent term could not cancel. Thus their finite
pole orders agree pointwise, giving $f_c^*D_Q=D_Q$.
Taking degrees and counting preimages with their local multiplicities
gives $2\deg D_Q=\deg D_Q$. Hence $D_Q=0$. A rational function with
no finite pole over an algebraically closed field is a polynomial:
in a coprime numerator/denominator representation any nonconstant
denominator would have a finite root. $\square$

This handles all $c$, including exceptional finite backward orbits,
without silently assuming poles avoid the critical point. It does not
construct $Q$. The missing implication is still that the orbitwise
condition yields some rational or polynomial transfer at all.

## Corrections or missing assumptions

The unresolved statement in the new route is the impossibility of (8)
for one nonzero $v\in V$ simultaneously at all sufficiently large
levels, together with the original smaller-level orbit conditions.
The proven binary-support lemma detects a nonzero class before reduction;
the problem requires detecting a nonzero value at an ordinary point.
Neither dimension counting, the Jacobian's necessary annihilation
condition, nor the rational-pole lemma supplies that passage. The
coordinator's Frobenius route reduces a possible closure to a sufficient
root-multiplicity bound such as (10), but that bound has not been proved
here for the complete family.

No assertion of a uniform transfer-degree bound, full reduced-root
detection, global squarefreeness or complete defect classification is
made. No special $c$, bounded degree, prime-to-$p$ period range or finite
field replaces the original quantifiers. The optional second question
remains unused while this exact continuation is handed to the coordinator.

## Open risks and ownership

The original equality may be true or false; the package does not decide
it. The new finite cyclic-algebra argument and its elementary diagnostic
are auxiliary, not enough for the paper-level gate. The external source
audit checks nearby cohomological analogies separately; none is invoked
as an unseen positive-characteristic regularity theorem in this proof.
Nonauthor review and any contract admission remain coordinator gates.
There is no target Euler-factor, root-number, automorphy, target-zero
or Hilbert–Pólya claim.
