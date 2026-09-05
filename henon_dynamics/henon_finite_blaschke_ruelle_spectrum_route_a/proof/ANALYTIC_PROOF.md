# Proof package: nonlinear Blaschke dynamics and exact transfer determinant

## Claim and status

Status: **PROVABLE AS STATED** for the corrected contract below. The initial
phrase “analytic inverse branches on an annulus” means local branches with a
single-valued branch sum. A degree-two annulus covering has no global inverse
branch. The complete spectral mechanism has the prior owner Bandtlow, Just
and Slipantschuk (2017), Theorem 5.4, DOI 10.1016/j.anihpc.2015.08.004.
This package proves a real-parameter specialization, an explicit annulus
certificate, all-period multiplier identity, and quantitative determinant
truncation and collision boundaries. It makes no literature-priority claim.

## Assumptions and notation

Let $0\leq a<1$, $B_a(z)=z(z-a)/(1-az)$, and let $\tau_a$ be its restriction
to $\mathbb T=\{|z|=1\}$. Time is integer iteration. For $a>0$ put
$r=(1+a)/2$; for $a=0$ use $r=1/2$. Write $A_r=\{r<|z|<r^{-1}\}$.
Its Hardy space has Laurent norm
$\|f\|^2=\sum_{m\in\mathbb Z}|f_m|^2(r^{2m}+r^{-2m})$.
The angular Perron operator is
$$
(\mathcal P_a f)(w)=\sum_{B_a(z)=w}\frac{w}{zB_a'(z)}f(z).
$$
The two local summands are permuted by analytic continuation. The derivative
transfer operator $\mathcal L_a g=\sum g(z)/B_a'(z)$ is similar to
$\mathcal P_a$: $\mathcal P_a=M_z\mathcal L_a M_z^{-1}$ on the annulus.

## Strategy and dependencies

1. The Blaschke identity gives angular expansion and strict disk contraction.
2. A degree-two expanding lift gives exactly $2^n-1$ circle fixed points.
3. Extension to a larger annulus and a summable Laurent restriction give
   trace class. A Fourier change of variables gives invariant polynomial
   sections, exhausting the nonzero spectrum through trace-norm convergence.
4. The rational fixed-point residue formula independently determines all
   periodic weighted traces, giving the Fredholm primitive product.
5. Geometric-series estimates give an explicit uniform determinant tail.

## Proof

### 1. Expansion, phase, and every periodic point

Writing $z=e^{i\theta}$ and $B_a(z)=e^{i\psi(\theta)}$ gives
$$
\psi'(\theta)=1+\frac{1-a^2}{1-2a\cos\theta+a^2},\qquad
\frac{2}{1+a}\leq\psi'(\theta)\leq\frac{2}{1-a}.
$$
These follow by differentiating the logarithm of the two Blaschke factors.
Both inequalities are attained, at $z=-1$ and $z=1$, respectively.
The increasing lift satisfies $\psi(\theta+2\pi)=\psi(\theta)+4\pi$.
For its $n$th iterate the difference $\psi_n(\theta)-\theta$ is strictly
increasing and changes by $2\pi(2^n-1)$ across a half-open fundamental cell.
It therefore meets exactly $2^n-1$ multiples of $2\pi$ there, each once.
Consequently
$$ F_n=2^n-1,\qquad
P_n=\frac1n\sum_{d\mid n}\mu(n/d)(2^d-1)
$$
are the fixed-point and primitive-orbit counts for every $n\geq1$.
The latter follows because a cycle of least length $d$ contributes $d$
fixed points precisely when $d\mid n$.

For a primitive orbit $\gamma$ of period $p$, define
$\Lambda_\gamma=\prod_{j=0}^{p-1}\psi'(\theta_j)>1$. The multiplier of
the $s$th repetition is exactly $\Lambda_\gamma^s$ by the chain rule.
Every orbit preserves orientation, every weight is positive, and the phase
is zero in this real unweighted model. Complex conjugation commutes with
$B_a$ and pairs or fixes orbits with equal multipliers. It is not a time
reversor: a noninjective degree-two map cannot be conjugate to an inverse
function on the same circle.

The two off-circle fixed points are $0$ and $\infty$ with local multipliers
$-a$. There are no further off-circle periodic points. Indeed, for $0<s<1$,
$$ |B_a(z)|\leq q_a(s)=s\frac{s+a}{1+as}<s\quad(|z|\leq s), $$
so every interior nonzero point strictly approaches zero. Reflection
$B_a(1/\bar z)=1/\overline{B_a(z)}$ gives the corresponding exterior
statement. Thus all circle fixed points are simple and the multiplier of
$B_a^n$ there is the positive real angular multiplier (the endpoint factors
$B_a^n(z)/z$ cancel).

### 2. Explicit annular trace-class certificate

We have $a<r<1$ for $a>0$, and $q_a(r)<r$. Choose
$t=(q_a(r)+r)/2$. There is $s>r$, $s<1$, with $q_a(s)<t$ by continuity.
For every $w\in\overline {A_t}$, each preimage of $w$ lies in
$s<|z|<s^{-1}$. The disk bound and its reflected exterior bound prove this.
The finite critical point inside the disk is
$c=a/(1+\sqrt{1-a^2})<a<r$; the other is $1/c$.
Their critical values are outside $\overline {A_t}$. When $a=0$, the
critical points are $0,\infty$ and the same conclusion holds.
Hence all local branches are regular near that compact target annulus.
Their weights are uniformly bounded, and evaluation of a Hardy function on
the compact source subannulus is bounded by its Hardy norm, by
Cauchy--Schwarz applied to its Laurent series. It follows that
$\mathcal P_a:H^2(A_r)\to H^2(A_t)$ is bounded.

Restriction $J:H^2(A_t)\to H^2(A_r)$ is diagonal in normalized Laurent
bases. Its singular values are
$$ s_m(J)=\left(\frac{r^{2m}+r^{-2m}}{t^{2m}+t^{-2m}}\right)^{1/2}
\leq\sqrt2(t/r)^{|m|}\quad(m\ne0),\qquad s_0=1. $$
Their sum is finite, so $J$ and therefore $\mathcal P_a=J\widetilde
\mathcal P_a$ are trace class. No finite-section eigenvalue observation is
used to establish compactness or nuclearity.

### 3. Exact finite sections, spectrum, and determinant

Because $B_a(0)=0$, Lebesgue measure on the circle is invariant: for every
nonzero integer $k$, the mean of $B_a(z)^k$ is zero, by the mean-value
formula in the disk or by conjugation. Thus $\mathcal P_a1=1$.
For positive integers $m,k$, change of variables on the two branches yields
$$ [z^k]\mathcal P_a z^m=[z^m]B_a(z)^k. $$
There is no constant or negative-frequency term. In detail, negative output
frequency $-k$ requires the mean of $z^m B_a(z)^k$, which is zero; the
positive coefficient equals the mean of $z^m\overline{B_a(z)^k}$, and the
Taylor coefficients are real. The coefficient vanishes for $k>m$ because
$B_a(z)^k$ vanishes to order at least $k$ at zero. Its diagonal equals
$(-a)^m$. Negative frequencies give an identical real block.

Thus $V_N=\operatorname{span}\{z^{-N},\ldots,z^N\}$ is invariant, with
diagonal entries $1$ once and $(-a)^k$ twice, $1\leq k\leq N$.
For orthogonal Laurent projections $Q_N$, the trace-class property gives
$\|\mathcal P_a-Q_N\mathcal P_aQ_N\|_1\to0$. One proof is to approximate
$\mathcal P_a$ by a finite sum of rank-one operators and use strong
convergence of $Q_N$ on each of their vectors; the uniformly bounded
projections control the remainder. Fredholm determinant continuity then
gives the locally uniform limit
$$ D_a(u)=\det(I-u\mathcal P_a)
=(1-u)\prod_{k=1}^{\infty}(1-(-a)^k u)^2. $$
For $0<a<1$, the nonzero spectrum is $1$ (algebraic multiplicity one) and
$(-a)^k$ (algebraic multiplicity two); the determinant has a simple zero at
$1$ and double zeros at $(-a)^{-k}$. It has no other zeros. Zero belongs
to the spectrum because the operator is compact on an infinite-dimensional
space. At $a=0$, the only nonzero eigenvalue is $1$ and $D_0=1-u$;
the operator is not rank one: $\mathcal P_0 z^{2m}=z^m$.
For every $n\geq1$,
$$ \operatorname{Tr}\mathcal P_a^n
=1+2\sum_{k\geq1}(-a)^{kn}
=\frac{1+(-a)^n}{1-(-a)^n}. $$
With $q=-a$, $D_a(qu)=D_a(u)/((1-u)(1-qu))$, interpreted as an entire
identity after multiplying denominators, including $q=0$.

### 4. Periodic multiplier trace and primitive product

For a rational map $R$ of degree at least two with simple fixed points,
the fixed-point index formula on the sphere is
$\sum_{R(z)=z}(1-R'(z))^{-1}=1$, with the derivative in a local coordinate
at infinity. It follows directly by summing residues of $dz/(z-R(z))$;
the term at infinity is evaluated using $v=1/z$.
Apply it to $R=B_a^n$. The two off-circle multipliers are $q^n$, so
$$ \sum_{\tau_a^n x=x}\frac1{(\tau_a^n)'(x)-1}
=\frac{2}{1-q^n}-1=\operatorname{Tr}\mathcal P_a^n. $$
Every denominator is positive. Hence for $|u|<1$ the logarithmic series
is absolutely convergent and can be grouped by primitive orbits and powers:
$$ D_a(u)=\prod_{\gamma\ {\rm primitive}}\prod_{j=1}^{\infty}
\left(1-\frac{u^{p_\gamma}}{\Lambda_\gamma^j}\right). $$
Indeed $1/(\Lambda^s-1)=\sum_{j\geq1}\Lambda^{-js}$ and each primitive
orbit supplies $p_\gamma$ fixed points at iterate $sp_\gamma$. The log
series therefore agrees term by term with $-\sum_n u^n\operatorname{Tr}
\mathcal P_a^n/n$. The entire continuation is supplied by the spectral
product, not by an assertion of primitive-product convergence everywhere.
The unweighted Artin--Mazur zeta is instead
$\zeta_{\rm AM}(u)=(1-u)/(1-2u)$: it has no dependence on $a$.

### 5. Quantitative truncation and singular parameter boundary

Let $D_{a,N}(u)=(1-u)\prod_{k=1}^{N}(1-q^k u)^2$. For $|u|\leq R$ and
$R a^{N+1}<1$, the tail is a nonzero analytic function and a logarithm
vanishing at zero satisfies
$$ \left|\log\frac{D_a(u)}{D_{a,N}(u)}\right|
\leq E=\frac{2R a^{N+1}}{(1-a)(1-Ra^{N+1})}. $$
At zeros of the finite product the quotient means its unique analytic
extension, namely the omitted infinite product. The bound follows from
$|\log(1-v)|\leq |v|/(1-|v|)$ and the geometric tail. Consequently the
relative tail error is at most $e^E-1$. This is a spectral finite-section
bound, not a general numerical root-fitting certificate.

For $0<a<1$ and $R\geq1$, the number of zeros in $|u|\leq R$, with
multiplicity, is $1+2\lfloor\log R/(-\log a)\rfloor$; the equivalent
definition counts precisely the integers $k\geq1$ satisfying $a^{-k}\leq R$
and avoids floating boundary decisions. For $R<1$ it is zero. At $a=0$
there is only the simple zero at one.

As $a\uparrow1$, the lower angular expansion bound tends to one and the
annular certificate degenerates. At $a=1$ cancellation gives $B_1(z)=-z$
away from the removable point. The resulting order-two rotation has a
unitary, noncompact Perron operator and infinitely many fixed points at every
even iterate. The all-$a<1$ fixed census and trace-class determinant do not
extend to this boundary. At $a\downarrow0$, the determinant converges
locally uniformly to $1-u$ even though the zero-spectral part of the operator
does not disappear.

## Corrections and open risks

- The infinite product and spectral formula are established prior mechanisms;
  the package is a fully verified specialization and quantitative boundary
  analysis, not a claim of a new spectral theorem in the literature.
- Local inverse branches cannot be promoted to global annular inverses.
- The compact transfer operator is not a unitary time evolution. No quantum
  lift is supplied beyond an adjoint Koopman hint.
- Exact native A1 data and a source determinant do not produce rational-prime
  orbit semantics, Riemann target zeros or a target functional equation.
  The conservative strict tuple is A0 FAIL, A1 WEAK, A2 FAIL, A3 FAIL,
  A4 FORMAL_HINT; Route B is false.
