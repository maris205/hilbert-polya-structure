# TR8: explicit outer parameter regions and the exceptional-curve reduction

2026-09-08 UTC. Author proof, submitted for bounded independent review.
This is subordinate to the unchanged [TR7 contract](../../continuation_round7/arithmetic_scout/SCOUT_REPORT.md)
and [frozen attempt](FROZEN_ATTEMPT.md). It is not a full-claim admission.

## 1. Result and precise limitation

For $c\in\mathbb Q$ let

$$
F_c(x,y)=(y,y^2+c-x),\qquad F_c^{-1}(x,y)=(x^2+c-y,x),
$$

and retain the absolute logarithmic projective height
$h(x,y)=h([x:y:1])$. Define, without a change of iterate clock,

$$
\widehat h_c^\pm(P)=\lim_{n\to\infty}2^{-n}h(F_c^{\pm n}P),\quad
H_c(P)=\widehat h_c^+(P)+\widehat h_c^-(P),\quad
b(c)=\inf_{P\in(\mathbb Q^{\rm tr})^2\setminus\operatorname{Per}(F_c)}H_c(P).
$$

The hand proofs below establish the following helper statements.

1. For every rational $c\le-16$, $b(c)=0$, with a terminating exact
   procedure producing distinct nonperiodic totally-real $Q_j$ such that
   $0<H_c(Q_j)\le2^{-j}$.
2. For every rational $c>1$, all totally-real affine points, with no
   degree or denominator restriction, satisfy $H_c(P)\ge\epsilon(c)>0$.
   An explicit rational choice is given in Section 5.
3. For any fixed rational $c$, $b(c)=0$ forces every small-height
   sublevel set of nonperiodic totally-real points to be Zariski dense.
   Consequently the archimedean equilibrium measure must be supported
   on the real plane. This is qualitative and supplies no general
   effective lower bound or converse.

The entire remaining interval $-16<c\le1$ is **not classified here**.
Statement 3 is a classical-input reduction, not a substitute for the
full decision problem. No mathematical program has been executed.

## 2. Heights, local normalization, and uniform elementary estimates

For a number field $K$ containing the coordinates of $P$, normalize each
absolute value to extend the usual one on $\mathbb Q$ and put
$n_v=[K_v:\mathbb Q_v]/[K:\mathbb Q]$. At an archimedean place use the
usual modulus, with weight two at a complex place. Then

$$
h(P)=\sum_{v\in M_K}n_v\log\max(1,|x|_v,|y|_v),\quad
G_{c,v}^{\pm}(P)=\lim_{n\to\infty}2^{-n}
 \log\max(1,\|F_c^{\pm n}P\|_v).
$$

These limits exist, are nonnegative, and
$\widehat h_c^\pm(P)=\sum_v n_vG_{c,v}^\pm(P)$.
The local existence is the standard Hénon height construction; an
applicable primary statement is Ingram, Section 2, Lemma 2.1, with
$\varphi(x,y)=(-y,x+y^2+c)$ and the height-isometric conjugacy
$L(x,y)=(-x,y)$, so $L F_c L=\varphi$.
This uses his arbitrary nonzero coefficient case, not a theorem restricted
to $\varphi(x,y)=(y,x+f(y))$. For the local-to-global equality, outside
finitely many places both $P$ and $c$ are integral and both integral
maps preserve the unit bidisk, so all terms in every iterate height vanish
there; interchanging the limit and the remaining finite sum is valid.
See the [source audit](SOURCE_AUDIT.md).

The defining limits give exactly

$$
\widehat h_c^+(F_cP)=2\widehat h_c^+(P),\qquad
\widehat h_c^-(F_cP)=\tfrac12\widehat h_c^-(P),
$$

and the analogous identities locally. In particular, for any integer $t$,
$H_c(F_c^tP)\le2^{|t|}H_c(P)$ and
$g_c(F_c^tP)\le2^{|t|}g_c(P)$, where $g_c=G_{c,\infty}^++G_{c,\infty}^-$.
At each place, the triangle or ultrametric inequality gives

$$
h(F_c^{\pm1}R)\le2h(R)+C_c,\qquad C_c=h(c)+\log3.
$$

Iteration and division by $2^n$ therefore yield the explicit bound

$$
\widehat h_c^\pm(R)\le h(R)+C_c. \tag{2.1}
$$

Only an upper bound is claimed in (2.1); no unproved uniform lower
comparison with the naive height is used.

## 3. Kicked cyclic roots: all conjugates, not one real branch

Write $c=-a=-A/D\le-16$, where $A,D$ are coprime positive integers.
Fix any integer $N\ge3$. Indices below are modulo $N$, and consider

$$
 x_i^2=a+x_{i-1}+x_{i+1}+\delta_{i0},\qquad 0\le i<N. \tag{3.1}
$$

Put $r=\sqrt a$, $B=r+2$ and $\beta=\sqrt{a-2B}$. Since $r\ge4$,
$a-2B=r^2-2r-4\ge4$ and $\beta\ge2$.
For each sign vector $\sigma\in\{-1,1\}^N$, define on $[-B,B]^N$

$$
(T_\sigma u)_i=\sigma_i\sqrt{a+u_{i-1}+u_{i+1}+\delta_{i0}}.
$$

Every radicand is at least $a-2B\ge4$ and at most $a+2B+1<B^2$,
the latter because $B^2-(a+2B+1)=2r-1>0$.
Thus $T_\sigma$ maps this complete cube to itself. Moreover,

$$
\|T_\sigma u-T_\sigma v\|_\infty
 \le\beta^{-1}\|u-v\|_\infty\le\tfrac12\|u-v\|_\infty. \tag{3.2}
$$

The square-root identity proves this bound: the numerator is at most
$2\|u-v\|_\infty$ and the sum of square roots is at least $2\beta$.
The contraction theorem gives one fixed point for each sign vector.
Its coordinates have the prescribed nonzero signs, so these are $2^N$
distinct real solutions.

Here is a complete algebraic exhaustion. Let $I_N$ be the ideal of (3.1)
in $\mathbb Q[X_0,\ldots,X_{N-1}]$. In its quotient, replacing $X_i^2$
by its affine-linear right side lowers total degree. Hence the squarefree
monomials span the quotient and its dimension is at most $2^N$.
After scalar extension to $\mathbb C$, evaluation at the $2^N$ already
constructed distinct solutions is surjective onto $\mathbb C^{2^N}$
(equivalently, use the distinct maximal ideals and the Chinese remainder
theorem). The dimension is therefore exactly $2^N$, and evaluation is
an isomorphism. Consequently there are no additional complex roots and
no multiplicities; the quotient is finite and reduced. Its multiplication
matrices also show that every coordinate is algebraic.

Every embedding of a solution's coordinate field maps it to a solution
of the same rational equations. All solutions have just been proved
real. Thus every coordinate field is totally real. This conclusion does
not assume that the $2^N$ solutions form one Galois orbit.

For $P_N=(x_0,x_1)$, the native unforced recurrence in (3.1) at
$i=1,\ldots,N-1$ gives $x_N=x_0$, and the equation at $i=0$ gives
$x_{N+1}=x_1+1$. Therefore

$$
F_c^N(P_N)=(x_0,x_1+1)=P_N+(0,1). \tag{3.3}
$$

All remaining $x_i$ are obtained from $(x_0,x_1)$ by the rational native
recurrence, so the tuple field equals $\mathbb Q(x_0,x_1)$.

## 4. Effective nonperiodic small-height witnesses for $c\le-16$

### 4.1 All-place height bound uniform in the segment length

At any nonarchimedean place of a solution field, put $M_v=\max_i|x_i|_v$.
Taking a coordinate attaining the maximum in (3.1) gives

$$
M_v^2\le\max(|a|_v,M_v,1),\qquad
M_v\le\max(1,|a|_v^{1/2}). \tag{4.1}
$$

The second implication follows by contradiction if $M_v$ exceeded its
right side. Adding the integral kick $1$ preserves this same bound.
At every archimedean embedding, Section 3 gives $|x_i|\le B$, and the
endpoint (3.3) has both coordinates at most $B+1$ in modulus. Hence,
for every $0\le k\le N$,

$$
h(F_c^kP_N)\le H_a:=\log(B+1)+\tfrac12\log D. \tag{4.2}
$$

Indeed, $\sum_{v\nmid\infty}n_v\log\max(1,|a|_v)=\log D$, regardless
of the degree of the totally-real solution field; the archimedean weights
sum to one. Equation (4.2) includes every conjugate and every finite place.

Let $m=\lfloor N/2\rfloor$ and $Q_N=F_c^mP_N$. By (2.1), (3.3), (4.2)
and the exact scaling identities,

$$
\begin{aligned}
H_c(Q_N)
 &=2^{-(N-m)}\widehat h_c^+(F_c^NP_N)
   +2^{-m}\widehat h_c^-(P_N)\\
 &\le(H_a+C_c)\bigl(2^{-(N-m)}+2^{-m}\bigr)\\
 &\le2(H_a+C_c)2^{-\lfloor N/2\rfloor}. \tag{4.3}
\end{aligned}
$$

Here $C_c=\log A+\log3$, since $A\ge16D$.
For a certificate using only integer arithmetic, take

$$
K_a=3A+D+10>H_a+C_c. \tag{4.4}
$$

For example, $\log(B+1)=\log(\sqrt a+3)\le A+3$,
$\frac12\log D\le D/2$, $\log A\le A$ and $\log3<2$, which prove
(4.4). Sharp constants are not needed.

### 4.2 The positive branch is nonperiodic and has positive height

Choose the unique all-positive solution of (3.1). Set
$\alpha=1+\sqrt{a+1}$, so $\alpha^2=a+2\alpha$ and $\alpha<B$.
The map $T_+$ is coordinatewise monotone. Starting its iteration from
the constant vector $\alpha$ gives a nondecreasing sequence in the cube,
with the zeroth coordinate strictly increased on its first step.
Convergence to the unique fixed point implies $x_i\ge\alpha$ for all $i$
and, by its zeroth equation, $x_0>\alpha$.

Let $M=\max_i(x_i-\alpha)$. At a maximizing index (3.1) gives

$$
(\alpha+M)^2\le a+2(\alpha+M)+1,
\quad M(2\alpha+M-2)\le1,
\quad M\le\frac1{2\alpha-2}<1. \tag{4.5}
$$

At the endpoint (3.3), write $(u,v)=(x_0,x_1+1)$. Then
$\alpha<u<\alpha+1\le v$, so $v>u>\alpha$. Its next native coordinate
satisfies

$$
w=v^2-a-u>v^2-a-v>v,
$$

since $v>\alpha$ implies $v^2-2v-a>0$. This argument iterates: the
forward real coordinates strictly increase. If they had a finite limit
$L>\alpha$, the recurrence would imply $L^2-2L-a=0$, a contradiction.
Thus the forward orbit is unbounded, and neither $P_N$ nor $Q_N$ is periodic.

There is also positive, not merely nonzero-orbit, height. Once a successive
coordinate $v$ exceeds $\max(4,2\sqrt a)$ and its predecessor is smaller,
the new coordinate is at least $v^2-v-a\ge v^2/2$. This escape region is
forward invariant; iteration gives $G_{c,\infty}^+\ge\log v-\log2>0$
at that iterate. Exact local scaling transfers positivity back to $P_N$
and $Q_N$. This chosen real embedding has positive global weight and all
other local heights are nonnegative. Therefore $H_c(Q_N)>0$.

### 4.3 Terminating exact construction and distinctness

The following procedure is an existence-level exact algebraic algorithm;
no polynomial-time or practical complexity claim is made.

1. On input $c=-A/D\le-16$, compute $K_a$ from (4.4), and an integer
   $r_0\ge0$ with $2^{r_0}\ge2K_a$.
2. For requested index $j\ge1$, enumerate even integers
   $N\ge\max(4,2(j+r_0))$, in increasing order, beyond any previously
   inspected value if desired. Form the rational system (3.1).
3. Compute its finite rational quotient by exact polynomial algebra and
   its multiplication matrices. Enumerate rational linear forms until
   one has squarefree characteristic polynomial of degree $2^N$; such
   a separating form exists because this finite algebra is reduced in
   characteristic zero. Recover every coordinate as a polynomial in
   that primitive element, using exact linear algebra.
4. Use rational real-root isolation and exact algebraic sign determination
   to select the unique solution with every $x_i>0$. These operations
   terminate because all roots are simple and no coordinate is zero.
   Return the corresponding real algebraic presentation of
   $Q_N=F_c^{N/2}(x_0,x_1)$ if it differs from every earlier returned point;
   otherwise continue enumerating $N$. Equality of algebraic coordinates
   is decidable exactly. Retain the defining system, real-root isolating
   data and the integer inequality $2K_a2^{-N/2}\le2^{-j}$ as a certificate.

Each individual algebraic step terminates. The rejection filter terminates
as well: each previously returned point has strictly positive height by
Section 4.2, whereas the upper bound for the candidates tends to zero as
$N\to\infty$. Eventually no candidate can equal any member of that finite
list. This argument does not require computing a previous point's exact
canonical height. The outputs are thus distinct, nonperiodic, totally
real, and meet the original total-height error bound. In particular $b(c)=0$.

## 5. Explicit positive gap for every rational $c>1$

Set $d=c-1>0$ and choose integers

$$
R=2\lceil c\rceil+4,\qquad
M=\min\{m\in\mathbb Z_{\ge1}:dm^2>4R\},\qquad
\epsilon(c)=2^{-(M+1)}. \tag{5.1}
$$

These are computable from rational $c$, and $R\ge\max(4,2\sqrt c)$.
First consider any complex pair of norm $T=\max(|x|,|y|)\ge R$.
If $|y|=T$, its new forward coordinate satisfies

$$
|y^2+c-x|\ge T^2-T-c\ge T^2/2\ge T.
$$

If $|x|=T$, use the identical estimate for the inverse map.
The corresponding dominant-coordinate region is invariant, and iteration
of $T_{n+1}\ge T_n^2/2$ proves that the corresponding local Green function
is at least $\log T-\log2$. Thus

$$
\max(|x|,|y|)\ge R\quad\Longrightarrow\quad
g_c(x,y)\ge\log(R/2). \tag{5.2}
$$

Suppose a real $P=(x_0,x_1)$ satisfied
$g_c(P)<2^{-M}\log(R/2)$. By the local scaling inequalities, all
$F_c^nP$ with $|n|\le M$ would have local total Green function less than
$\log(R/2)$. Equation (5.2) then bounds every $|x_i|<R$ for
$-M\le i\le M$ in its bi-infinite native real recurrence.
But that recurrence has the exact identity

$$
x_{i+1}-2x_i+x_{i-1}=x_i^2-2x_i+c=(x_i-1)^2+d\ge d.
$$

Summing with the triangular weights gives

$$
x_M+x_{-M}-2x_0
=\sum_{i=-M+1}^{M-1}(M-|i|)(x_{i+1}-2x_i+x_{i-1})
\ge dM^2>4R. \tag{5.3}
$$

The coordinate bounds give the strict opposite inequality. This
contradiction proves $g_c(P)\ge2^{-M}\log(R/2)$ for every real $P$.
Since $R\ge4$ and $\log2>1/2$, this is strictly larger than
$\epsilon(c)$ in (5.1).

Finally, every archimedean conjugate of a totally-real algebraic point
is a real point, with the same rational parameter $c$. The archimedean
weights sum to one and the finite local heights are nonnegative. Hence

$$
H_c(P)\ge2^{-M}\log(R/2)>\epsilon(c),
\qquad P\in(\mathbb Q^{\rm tr})^2. \tag{5.4}
$$

This bound has no degree, denominator, curve, or nonzero-coordinate
restriction. In particular it supplies the required positive answer on
the entire region $c>1$, without using an ineffective equidistribution
contradiction. It also rules out totally-real periodic points there.

## 6. Exceptional curves: saturation removes the qualitative obstruction

Fix any rational $c$ and suppose $b(c)=0$. Put, for integers $j\ge1$,

$$
E_j=\{P\in(\mathbb Q^{\rm tr})^2\setminus\operatorname{Per}(F_c):
                     H_c(P)<2^{-j}\},\qquad
Z_j=\overline{E_j}^{\rm Zar}\subset\mathbb A^2_{\overline{\mathbb Q}}.
$$

Each $E_j$ is nonempty. The closed sets $Z_j$ descend, so Noetherianity
gives a stable nonempty $Z=Z_j$ for all sufficiently large $j$.
Rational forward and inverse maps preserve total reality and
nonperiodicity, and the exact height inequalities give
$F_c(E_{j+1})\subset E_j$ and $F_c^{-1}(E_{j+1})\subset E_j$.
Taking closures, using that $F_c$ is an algebraic automorphism, gives
$F_c(Z)\subset Z$ and $F_c^{-1}(Z)\subset Z$. Therefore $F_c(Z)=Z$.

A Hénon-type polynomial automorphism has no invariant algebraic curve;
apply the same fact to every positive iterate to exclude periodic curves.
The relevant primary formulation is Dujardin--Favre, Proposition 1.7,
which credits Bedford--Smillie. If $Z$ were proper and contained a
one-dimensional component, the automorphism would permute its finitely
many one-dimensional components, producing such a periodic curve.
Thus a proper $Z$ would be finite. Its points would be permuted by $F_c$
and hence all periodic, contradicting its containment of a nonempty
$E_j$. We conclude that $Z=\mathbb A^2$.

Every $Z_j$ is consequently $\mathbb A^2$, including the earlier ones.
In particular an exceptional diagonal, or any fixed algebraic curve,
cannot contain all sufficiently small nonperiodic totally-real points
when the infimum is zero. Enumerate the nonzero nonconstant polynomials
over the countable field $\overline{\mathbb Q}$. For each $j$, choose
$P_j\in E_j$ avoiding the zero sets of the first $j$ polynomials and the
finitely many earlier chosen points. Density permits this choice. The
resulting distinct sequence is generic and $H_c(P_j)\to0$.
This extraction is qualitative, not a terminating choice algorithm.

## 7. What equidistribution now does, and does not, prove

To avoid a normalization substitution, put

$$
G_{c,v}=\max(G_{c,v}^+,G_{c,v}^-),\qquad
h_{G_c}(P)=\sum_vn_vG_{c,v}(P).
$$

Pointwise nonnegativity gives the exact inequalities

$$
h_{G_c}(P)\le H_c(P)\le2h_{G_c}(P), \tag{7.1}
$$

with no additive error. The max height is the semipositive adelic
$\mathcal O_{\mathbb P^2}(1)$ height constructed for the regular pair
$\{F_c,F_c^{-1}\}$ by Lee, Theorem 6.5: its approximating maps are
$P\mapsto(F_c^nP,F_c^{-n}P)$, of degree $2^n$, and the sup-norm
limit on the affine chart is precisely $G_{c,v}$.
The two maps have degree two, are algebraically stable, commute with
composition the identity, and have disjoint indeterminacy points
$[1:0:0]$ and $[0:1:0]$; they are regular polynomial automorphisms,
so the finiteness condition in that theorem also holds.
Lee's Corollary 7.5 gives the variety height zero, and Theorem B applies
to generic sequences whose max height tends to zero. The archimedean
limit measure is the Hénon equilibrium probability measure $\mu_c$,
identified in his final regular-automorphism discussion; it has no mass
on the line at infinity. These are classical inputs, not proved anew here.

Apply this to the sequence in Section 6 using (7.1). Each of its Galois
orbit probability measures is supported in the closed set
$\mathbb P^2(\mathbb R)\subset\mathbb P^2(\mathbb C)$. Any weak limit
is supported there as well, and $\mu_c$ has no mass at infinity. Thus

$$
b(c)=0\quad\Longrightarrow\quad\mu_c(\mathbb R^2)=1;
\qquad
\mu_c(\mathbb R^2)<1\quad\Longrightarrow\quad b(c)>0. \tag{7.2}
$$

This last implication concerns all nonperiodic totally-real points,
not only a previously assumed generic family. Its Noetherian and
equidistribution proof is ineffective: it neither returns a rational
lower bound for a given parameter nor decides the support condition for
every rational parameter. The converse in (7.2) is not asserted.
Sections 3--5 establish their explicit regions independently of this
equidistribution reduction.

## 8. Ownership, review gates, and full-question disposition

Canonical heights, no periodic algebraic curves, the max adelic metric,
and generic equidistribution are existing tools; Section 7 is an explicit
application, not a claimed new general theorem. The local P62 package
already owns a full periodic real-root exhaustion at its horseshoe
parameter. Periodic points have height zero and do not meet TR7's
nonperiodic witness clause. Here the fixed nonzero kick, actual escape,
uniform finite-place estimate and midpoint clock are essential to the
nonperiodic helper. No worldwide novelty clearance is claimed.

Independent review should specifically check the complete quotient
dimension/root count, the sign of the kick in (3.3), the finite-place
denominator term in (4.2), both exponents in (4.3), nonperiodicity and
filter termination, the escape threshold and triangular sum in Section 5,
and the max/sum normalization plus the smallness hypothesis in Section 7.

Disposition of the original TR7 question: **NOT CURRENTLY JUSTIFIED**.
The explicit outer regions and qualitative saturation are substantial
progress within it, but no all-rational-parameter zero locus or terminating
full decision procedure has been proved. No original contract is renamed,
shrunk or admitted by this helper package. Mathematical executions: zero.
No old proof/program rerun, GPU, paid model, manuscript/PDF, Git mutation,
or global-index write. NO_BAD_EULER_OR_ROOT_NUMBER is preserved.
