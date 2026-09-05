# C381 proof: alpha-one intermittency, complete inducing and a nuclear return operator

## Claim and status

**PROVABLE AS STATED AFTER FIXING THE HALF-INTERVAL CONVENTION.** Let
$$
T(x)=\begin{cases}x+2x^2,&0\leq x\leq1/2,\\2x-1,&1/2<x\leq1.\end{cases}
$$
The left branch includes $1/2$. This is essential for literal return-branch
endpoints: $T(1/2)=1$, so a point hitting $1/2$ returns to the base on its
next iterate instead of falling onto the neutral point. The choice changes
only a countable orbit-boundary set compared with the other conventional
assignment, but must not be left implicit in an exact census.

There are exactly $2^n$ points fixed by $T^n$ for every $n\geq1$. All are
uniquely coded by binary words; only the all-zero orbit is neutral. Every
other primitive orbit corresponds bijectively to an orbit of the first
return map on $Y=(1/2,1]$. Its countable inverse branches extend to one fixed
complex disk, have a common strictly interior range and uniformly summable
derivatives. Consequently the derivative-weighted induced operator is trace
class on an explicitly fixed Hardy space for every return-clock parameter
$|\zeta|\leq1$, and its Fredholm determinant has an exact primitive product
near the origin. The original clock, induced clock and neutral obstruction
are separated. The uninduced Perron operator on $L^1$ is not compact and has
approximate eigenvalue one on the zero-integral subspace, excluding an
exponential operator-norm relaxation claim there.

## Assumptions and notation

The inverse branches are
$g(z)=(\sqrt{1+8z}-1)/4$ and $h(z)=(1+z)/2$, with the square root of positive
real part on $\Re z>0$. Set $Y=(1/2,1]$ and
$a_m=g^m(1/2)$ for integers $m\geq0$. The return time is
$\tau(y)=\min\{n\geq1:T^ny\in Y\}$ and $R=T^\tau$.
The $n$th inverse return branch is
$h_n(z)=(1+g^{n-1}(z))/2$, $n\geq1$.

The complex domain is the fixed disk
$\Omega=\{z:|z-1|<3/4\}$. Write $H^2(\Omega)$ for the Hardy Hilbert space
with normalized basis $e_k(z)=((z-1)/(3/4))^k$, $k\geq0$.
The two parameters in the determinant are $u$, counting returns to $Y$, and
$\zeta$, counting original iterations of $T$:
$$
\mathcal L_\zeta f(z)=\sum_{n\geq1}\zeta^n h_n'(z)f(h_n(z)),\qquad
\Delta(u,\zeta)=\det(I-u\mathcal L_\zeta).
$$
For a primitive induced orbit $p$, let $r_p$ be its return period,
$N_p$ its total original return time and $\Lambda_p>1$ its forward multiplier.
All weights are source derivatives; no target arithmetic is inserted.

## Dependency map

1. Monotonicity and inverse contraction yield the complete binary periodic
   census and hyperbolic/neutral split.
2. The exact inverse recurrence yields all return branches and return tails.
3. A right-half-plane and reciprocal-disk invariant yields a common complex
   domain for every inverse return branch.
4. A reciprocal growth estimate plus a telescoping derivative product gives
   uniform quadratic derivative decay. A Hardy monomial expansion then proves
   trace-class convergence without invoking an unchecked inducing theorem.
5. The weighted composition trace is a residue at its unique fixed point.
   Absolute convergence and primitive-power grouping give the determinant
   product.
6. Localized densities at the neutral point give independent noncompactness
   and no-uniform-gap statements for the uninduced $L^1$ operator.

## Proof

### 1. All-period symbolic coding

On $[0,1]$, $g$ and $h$ are increasing, with $0<g'\leq1$ and $h'=1/2$.
Their ranges are $[0,1/2]$ and $[1/2,1]$. A composition whose word contains
at least one $h$ is a contraction with Lipschitz constant at most $1/2$.
It therefore has a unique fixed point in $[0,1]$, by the contraction mapping
theorem. The all-$g$ composition has only fixed point zero: $g(x)<x$ for
$x>0$. The all-$h$ word has fixed point one.

For a mixed inverse-composition cycle, an intermediate value zero would
force that inverse branch to be $g$ with its input also zero. Repeating this
implication around the inverse cycle forces the all-$g$ word. An intermediate
value one forces $h$ with input one at every subsequent inverse position,
forcing the all-$h$ word. Hence a mixed inverse cycle has every coordinate
strictly between zero and one. The value $1/2$ can arise only as $g(1)$ or
$h(0)$, whose inputs have just been excluded. Thus it also avoids the
partition boundary before any forward-itinerary claim is used.
The inverse composition therefore realizes
the specified forward itinerary with no ambiguous boundary labels. Distinct
length-$n$ words cannot code the same based point, because the deterministic
forward map would then have two itineraries. Conversely every point fixed
by $T^n$ has a binary itinerary and solves its inverse composition equation.
This proves the exact fixed count $2^n$ and completeness.

The least period equals the least word period, since both directions of
coding hold at all periodic points. Primitive cycles are primitive necklaces,
with number
$$
P_n=\frac1n\sum_{d\mid n}\mu(d)2^{n/d}.
$$
The neutral orbit at zero has multiplier one. Every other periodic word
contains a right branch with derivative two, while all left derivatives are
$1+4x\geq1$. Its multiplier is at least two and is positive. Under the $k$th
power, period and clock multiply by $k$ and the multiplier becomes
$\Lambda^k$. There is no declared time-reversal symmetry for this
noninvertible interval map; orientation is positive on each branch.

### 2. Exact first-return branches and sharp return tail

Every $y\in Y$ maps first to $2y-1>0$. As long as the orbit remains in
$(0,1/2]$, the left branch strictly increases it. An orbit that never leaves
this interval would converge to a positive fixed point of $x+2x^2$, which
does not exist. Hence all $y\in Y$ have finite return time. For $n\geq1$,
$$
\{y:\tau(y)=n\}=h_n(Y),\qquad R\circ h_n=\mathrm{id}_Y.
$$
Indeed the $n-1$ inverse left iterates put every preceding point in
$(0,1/2]$, and the first inverse right iterate returns it to $Y$.
The intervals $h_n(Y)$ are left-open/right-closed and partition $Y$:
$h_{n+1}(1)=h_n(1/2)$, because $g(1)=1/2$.
The chosen assignment of $1/2$ to the left branch makes these shared upper
endpoints valid first-return endpoints.

For $n\geq1$,
$$
\operatorname{Leb}\{y\in Y:\tau(y)>n\}=\frac{a_{n-1}}2.
$$
For example, the first tail is $(1/2,3/4]$, of length $1/4$.
The exact recurrence is $a_{m-1}=a_m+2a_m^2$, giving
$$
\frac1{a_m}-\frac1{a_{m-1}}=\frac2{1+2a_m}.
$$
Since $0<a_m\leq1/2$, these increments lie between one and two.
Therefore $a_m\leq1/(m+2)$ and $a_m\geq1/(2m+2)$. Summing the sharper form
$2/(1+2a_m)=2-4a_m/(1+2a_m)$ yields
$a_m^{-1}=2m+O(\log(m+2))$; inversion gives
$$
a_m=\frac1{2m}+O\!\left(\frac{\log m}{m^2}\right),\qquad
\operatorname{Leb}\{\tau>n\}\sim\frac1{4n}.
$$
The tail under normalized Lebesgue measure on $Y$ is consequently
$\sim1/(2n)$. In particular its mean return time diverges. This last
statement is about this reference distribution; it is not an unproved
claim about a stationary induced density.

Every nonneutral primitive $T$ orbit meets $Y$. Its sequence of gaps between
successive right symbols gives an induced orbit, with original period the
sum of its return times and unchanged total multiplier. Conversely the
branches $h_n$ reconstruct that original orbit. Choosing another visit to
$Y$ rotates the induced word, so this correspondence is bijective at the
primitive-cycle level, without introducing a multiplicity equal to the
number of returns.

### 3. One complex domain for all return branches

For $\Re z>0$, the chosen square root satisfies
$\Re\sqrt{1+8z}>1$, hence $w=g(z)$ has positive real part and satisfies
$z=w(1+2w)$. Thus
$$
\frac1w=\frac1z+\frac2{1+2w}.
$$
The second term has positive real part. The disk $D(1,1)$ is exactly the set
of nonzero $z$ with $\Re(1/z)>1/2$. Therefore $g$ preserves that disk, as well
as the right half-plane. Since $\Omega\subset D(1,1)$, every iterate
$w_m=g^m(z)$ lies in $D(1,1)$ for $z\in\Omega$.

For $n\geq2$, this gives
$|h_n(z)-1|=|w_{n-1}-1|/2<1/2$. For $n=1$,
$|h_1(z)-1|=|z-1|/2<3/8$. Thus, uniformly for all branches,
$$
h_n(\Omega)\subset D(1,1/2)\Subset\Omega.
$$
All branches are holomorphic on a neighborhood of the closed disk
$\overline\Omega$, because that disk is inside the right half-plane.
Furthermore $|g'(z)|=|1+8z|^{-1/2}\leq1$ on the right half-plane, so
$|h_n'(z)|\leq1/2$ there. Convexity gives a common Lipschitz contraction
bound $1/2$ on $\overline\Omega$ for every branch.

### 4. Explicit uniform derivative summability and trace class

For $w_m\in D(1,1)$ we have $|w_m|\leq2$, $\Re w_m>0$ and
$$
\Re\frac2{1+2w_m}\geq\frac2{25}.
$$
On $\Omega$, $\Re(1/z)\geq4/7$. The reciprocal recurrence therefore gives
$$
|w_m|\leq\frac1{4/7+2m/25}\leq\frac{25}{2(m+1)}.
$$
The last bound is intentionally coarse but uniform in the complex disk.
Differentiating $w_{k-1}=w_k(1+2w_k)$ and telescoping gives the exact identity
$$
(g^m)'(z)=\left(\frac{w_m}{z}\right)^2
\prod_{k=1}^m\frac{(1+2w_k)^2}{1+4w_k}
=\left(\frac{w_m}{z}\right)^2
\prod_{k=1}^m\left(1+\frac{4w_k^2}{1+4w_k}\right).
$$
Because $|1+4w_k|\geq1$ and $|z|\geq1/4$, the product is at most
$\exp(4\sum_{k\geq1}|w_k|^2)$ in absolute value. The displayed reciprocal
bound makes this sum finite uniformly. For example, the explicit finite
constant
$$
C_*=1250\exp\left(\frac{625\pi^2}{6}\right)
$$
is sufficient for
$\sup_{\Omega}|h_n'|\leq C_*/n^2$ for every $n\geq1$.
Its large size is immaterial to convergence and is not used as a useful
numerical cutoff certificate. This is an all-branch proof, not a finite
branch extrapolation.

For $T_nf=h_n'f\circ h_n$ expand $f=\sum_{k\geq0}c_ke_k$ in the normalized
Hardy basis. The coefficient functional $f\mapsto c_k$ has norm one, and
$$
\|h_n'e_k\circ h_n\|_{H^2(\Omega)}
\leq \sup_\Omega|h_n'|(2/3)^k.
$$
This is a rank-one decomposition with summable norms, yielding
$\|T_n\|_1\leq3\sup|h_n'|\leq3C_*/n^2$.
Here the Hilbert-space nuclear norm is the trace norm. Consequently
$\mathcal L_\zeta=\sum_n\zeta^nT_n$ converges absolutely in trace norm for
$|\zeta|\leq1$, is trace-norm continuous on that closed disk and holomorphic
inside it. For each such $\zeta$, $\Delta(u,\zeta)$ is entire in $u$; it is
jointly holomorphic for $u\in\mathbb C$, $|\zeta|<1$ and continuous at the
return-clock boundary.

The absolute domain of this defining branch series is exact. At any fixed
$x\in[1/2,1]$, the reciprocal increment is at most two, so
$g^{n-1}(x)\geq1/(2n)$. In the derivative identity all real product factors
are at least one, hence $h_n'(x)\geq1/(8n^2)$. If $|\zeta|>1$, the terms
$\zeta^nh_n'(x)$ do not tend to zero, even on $f=1$. Thus the defining
series fails there. This is not a claim that no analytic continuation across
any part of the unit circle could exist.

### 5. Trace formula, determinant product and the neutral factor

Any composition $\chi=h_{n_1}\circ\cdots\circ h_{n_r}$ maps
$\overline\Omega$ into $D(1,1/2)$ with Lipschitz constant at most $2^{-r}$.
It has a unique fixed point $x_\chi$ by contraction. The real interval
$[1/2,1]$ is invariant, so this fixed point is real and corresponds to the
unique induced periodic itinerary. The weighted composition trace is
$$
\operatorname{tr}(\chi'\,C_\chi)
=\frac1{2\pi i}\int_{|z-1|=3/4}\frac{\chi'(z)}{z-\chi(z)}\,dz
=\frac{\chi'(x_\chi)}{1-\chi'(x_\chi)}.
$$
The first equality follows by summing the geometric series of Hardy
coefficient diagonal entries; uniform strict containment justifies the
sum under the contour integral. The second equality is the residue theorem:
there is exactly one zero of $z-\chi(z)$, it is simple because
$|\chi'|\leq2^{-r}<1$, and no other pole lies inside the contour.

For $|\zeta|\leq1$ let $K(\zeta)=\sum_n|\zeta|^n\sup_\Omega|h_n'|$.
It is finite. The trace sum over $r$-branch compositions is bounded by
$2K(\zeta)^r$. Therefore for $|u|K(\zeta)<1$ the logarithmic determinant
series and its absolute primitive regrouping converge, giving
$$
\Delta(u,\zeta)
=\prod_{p\text{ primitive induced}}
\prod_{k\geq1}
\left(1-\frac{u^{r_p}\zeta^{N_p}}{\Lambda_p^k}\right).
$$
For precision about the domain argument, the trace-log identity first holds
on $|u|\|\mathcal L_\zeta\|<1$. The absolutely convergent trace/product series
then extends it to $|u|K(\zeta)<1$ by the analytic identity theorem. We do not
identify $K(\zeta)$ with the Hardy-space operator norm.

To see the inner product, an $a$-fold repetition contributes
$\Lambda_p^{-a}/(1-\Lambda_p^{-a})=\sum_{k\geq1}\Lambda_p^{-ak}$
to its weighted trace, while its clocks are $(ar_p,aN_p)$.
Grouping the $r_p$ based phases and dividing by $ar_p$ in the logarithm
leaves exactly $1/a$. Exponentiation gives the factors above.
The determinant itself extends to all $u$ by trace class; no unrestricted
Euler-product convergence is inferred from that extension. At $u=1$ the
same product is initially valid for sufficiently small $|\zeta|$, since
$K(\zeta)\to0$ as $\zeta\to0$.

For comparison, the unweighted Artin–Mazur zeta is
$$
\exp\left(\sum_{n\geq1}\frac{2^nz^n}{n}\right)=\frac1{1-2z},
\qquad |z|<1/2.
$$
Removing the neutral primitive point multiplies it by $(1-z)$, yielding
$(1-z)/(1-2z)$. The renewal identity
$1-\sum_{n\geq1}z^n=(1-2z)/(1-z)$ reproduces this hyperbolic symbolic
factor with the original return clock. These unweighted factors are not
the derivative-weighted Fredholm determinant. In particular the neutral
point has multiplier one, making the would-be flat-trace denominator zero;
it cannot be inserted as an ordinary trace-class branch contribution.

### 6. The uninduced Perron boundary on the specified space

On Lebesgue $L^1([0,1])$, the uninduced Perron operator is
$$
\mathcal P f(x)=g'(x)f(g(x))+\tfrac12 f((x+1)/2).
$$
Endpoint values are irrelevant on $L^1$. The operator is a positive
mass-preserving contraction by change of variables on the two branches.
Choose pairwise disjoint intervals $I_j\subset(0,1/2)$ such that the intervals
$T(I_j)$ are pairwise disjoint, and let $f_j=\mathbf1_{I_j}/|I_j|$.
Their images have norm one and disjoint supports $T(I_j)$, hence pairwise
$L^1$ distance two. Thus $\mathcal P$ is not compact and not nuclear on this
specified Banach space. This noncompactness observation alone is not unique
to intermittent maps, so it is not advertised as a special intermittency
criterion.

The neutral point gives a stronger no-gap statement on the zero-integral
subspace. For $0<\epsilon<1/4$, set
$f_\epsilon=\epsilon^{-1}\mathbf1_{[0,\epsilon]}$.
Direct integration gives
$$
\|\mathcal P f_\epsilon-f_\epsilon\|_1
=2\left(1-\frac{g(\epsilon)}\epsilon\right)\leq4\epsilon.
$$
The equality uses $g'(x)\leq1$ on the common support and
$T(\epsilon)=\epsilon+2\epsilon^2$. Let
$v_\epsilon=f_\epsilon-f_{2\epsilon}$. It has zero integral and norm one,
while
$\|(\mathcal P-I)v_\epsilon\|_1\leq12\epsilon\to0$.
For every fixed integer $n\geq0$, contraction and telescoping imply
$\|(\mathcal P^n-I)v_\epsilon\|_1\leq12n\epsilon$. Taking $\epsilon\to0$
gives the lower bound one for the norm of $\mathcal P^n$ on the
zero-integral subspace, and contraction gives the matching upper bound.
Thus that restricted power norm is exactly one for every $n\geq0$.
In particular, one is an approximate eigenvalue of the restriction to the
zero-integral subspace. An estimate
$\|\mathcal P^n|_{\int f=0}\|\leq C\rho^n$ with $\rho<1$ would make
$I-\mathcal P$ invertible there by the norm-convergent Neumann series,
contradicting the approximate eigenvectors. No such uniform exponential
operator-norm decay is possible. We do not transfer this assertion to an
unstated anisotropic, analytic or bounded-variation space.

## Route-A boundary and open risks

The all-period source census and explicit nuclear induced determinant do
not carry rational-prime data. Strict tuple is
$(A0\_FAIL,A1\_WEAK,A2\_FAIL,A3\_FAIL,A4\_FAIL)$, overall
`ROUTE_A_REJECTED`, with `NO_BAD_EULER_OR_ROOT_NUMBER` and Route B false.
The source determinant is separate from target A2. No global literature
novelty is claimed for LSV intermittency or inducing; the package supplies a
single-domain complete proof with explicit complex summability and boundary
controls. No invariant-density theorem, target functional equation, full
uninduced Fredholm determinant or unproved boundary continuation is claimed.
