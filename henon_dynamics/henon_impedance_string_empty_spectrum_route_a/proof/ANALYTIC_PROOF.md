# C396 complete proof: impedance absorption and empty spectrum

## Claim and status

PROVABLE AS STATED, for $L,c>0$ and **finite** $\eta\geq0$.
The theorem concerns the autonomous wave equation $u_{tt}=c^2u_{xx}$ on
$(0,L)$, with $u(0,t)=0$ and $u_x(L,t)+(\eta/c)u_t(L,t)=0$.
It gives the exact physical-time semigroup, every generator spectral point,
the transparent-case resolvent norm and all its pseudospectra, and the precise
Schatten/determinant boundary. No arithmetic or target spectral theorem follows.

## Assumptions and notation

Work over complex scalars. Write $v=u_t$, $p=cu_x$, $\ell=L/c$,
$\tau=2\ell$ and $q=(\eta-1)/(\eta+1)\in[-1,1)$.
The Hilbert space is
$$\mathcal H=\{u\in H^1(0,L):u(0)=0\}\times L^2(0,L),\qquad
\|(u,v)\|_E^2=\int_0^L(c^2|u_x|^2+|v|^2)\,dx.$$
The physical energy is one half of this norm squared. The generator is
$$G_\eta(u,v)=(v,c^2u_{xx}),$$
$$D(G_\eta)=\{(u,v):u\in H^2(0,L),\ v\in H^1(0,L),\ u(0)=v(0)=0,
u_x(L)+(\eta/c)v(L)=0\}.$$
The resolvent convention is $R(z,A)=(zI-A)^{-1}$. Pseudospectra use the
strict convention $\sigma_\varepsilon(A)=\sigma(A)\cup
\{z\in\rho(A):\|R(z,A)\|>1/\varepsilon\}$, for $\varepsilon>0$.
The point $\eta=\infty$ is not part of this theorem.

## Strategy and dependency map

1. An explicit unitary map sends the full physical energy space and domain to
   a derivative with one scalar boundary condition.
2. Characteristics prove generation and exact norm; a first-order boundary
   value calculation proves the full resolvent and spectrum.
3. At transparency, singular-value minimization gives a regular separated
   Sturm--Liouville problem, hence an exact norm and half-plane pseudospectra.
4. Explicit Volterra kernels prove the operator-ideal and determinant claims.

Only elementary Sobolev traces, compactness of the interval $H^1$ embedding,
the Fourier orthonormal basis, and the Rayleigh variational principle are used.
The regularized determinant is explicitly defined below; no trace is inserted
for an operator outside its ideal.

## 1. Exact unitary unfolding, including the domain

Define $U:\mathcal H\to L^2(0,\tau)$ by
$$U(u,v)(s)=\sqrt{c/2}\begin{cases}
(p-v)(L-cs),&0<s<\ell,\\
(p+v)(c(s-\ell)),&\ell<s<\tau.
\end{cases}$$
Changing variables on the two halves and using
$|p-v|^2+|p+v|^2=2(|p|^2+|v|^2)$ proves that $U$ is an isometry.
For any $w\in L^2(0,\tau)$ its inverse is
$$p(x)=\frac{w(\ell+x/c)+w(\ell-x/c)}{\sqrt{2c}},\qquad
v(x)=\frac{w(\ell+x/c)-w(\ell-x/c)}{\sqrt{2c}},\qquad
u(x)=c^{-1}\int_0^x p(y)\,dy.$$
These formulas lie in $\mathcal H$ and recover $w$, proving surjectivity.
For domain vectors the two traces at $s=\ell$ agree exactly because $v(0)=0$.
The right boundary gives $p(L)=-\eta v(L)$ and therefore
$w(\tau)=q w(0)$, including $\eta=1$, without dividing by $q$.
Conversely, these two identities recover both physical boundary conditions.
The chain rule on each half gives
$$UG_\eta U^{-1}=A_q,\qquad A_qw=w',\qquad
D(A_q)=\{w\in H^1(0,\tau):w(\tau)=q w(0)\}.$$
The parameter $s$ has units of time. There has been no target-dependent clock
change. Integration by parts also gives
$$\operatorname{Re}\langle A_qw,w\rangle
=\tfrac12(q^2-1)|w(0)|^2=-c\eta|v(L)|^2,$$
which is the physical energy dissipation identity.

## 2. Complete physical-time evolution and exact norm

For $t\geq0$ and almost every $s\in(0,\tau)$ let
$k=\lfloor(s+t)/\tau\rfloor$ and $r=s+t-k\tau\in[0,\tau)$.
Set
$$S_q(t)w(s)=q^k w(r).$$
For $q=0$ this means coefficient $1$ if $k=0$ and $0$ if $k\geq1$.
The floor-addition identity proves the semigroup law. Translation continuity,
first for smooth functions supported away from the endpoints and then by
density using the contraction bound, proves strong continuity. For a domain
vector the difference quotient tends to $w'$ in $L^2$; conversely the
distributional derivative of a generator vector lies in $L^2$, and the wrapped
endpoint difference would have order $t^{-1/2}$ unless $w(\tau)=qw(0)$.
Thus its generator has exactly the stated domain. Alternatively the resolvent
in Section 3 identifies the generator domain without this difference-quotient
characterization.

Write $t=n\tau+a$, $n\geq0$ integer and $0\leq a<\tau$. On $(0,\tau-a)$
the multiplier is $q^n$; on $(\tau-a,\tau)$ it is $q^{n+1}$.
The translated input intervals are disjoint, so
$$\boxed{\|S_q(t)\|=|q|^{\lfloor t/\tau\rfloor}.}$$
The upper bound follows by integration; equality follows by choosing an
arbitrary nonzero input supported on the first translated interval, which has
positive measure even at $a=0$. In particular,
$$\|S_0(t)\|=1\ (0\leq t<\tau),\qquad S_0(t)=0\ (t\geq\tau).$$
No smaller uniform extinction time is possible. The energy norm squared has
the square of this decay factor. At $\eta=0$, $q=-1$, the group is unitary.
For $q\ne0$ the same translation rule extends to negative times, giving a
bounded operator at each fixed time, although the group need not be uniformly
bounded as time tends to minus infinity.

## 3. Full resolvent, spectrum and Riesz basis

Solving $zw-w'=f$ with $w(\tau)=qw(0)$ yields, if $e^{z\tau}\ne q$,
$$R(z,A_q)f(s)=\int_0^\tau e^{z(s-r)}
\left[\frac{e^{z\tau}}{e^{z\tau}-q}-{\bf1}_{r<s}\right]f(r)\,dr.$$
This kernel is bounded on the square and maps $L^2$ to $D(A_q)$ by the
differential equation. Substitution verifies both left and right inverse.
For $q\ne0$ choose any argument $\arg q$ and define
$$\alpha=\frac{\log|q|+i\arg q}{\tau},\qquad
\lambda_n=\alpha+\frac{2\pi in}{\tau},\quad n\in\mathbb Z.$$
At these points $e^{\lambda_ns}$ is a nonzero eigenvector, and at every other
point the displayed inverse exists. Hence this list is the **entire** spectrum.
Multiplication $M_\alpha f(s)=e^{\alpha s}f(s)$ is bounded and boundedly
invertible, maps the periodic $H^1$ domain onto $D(A_q)$, and conjugates the
periodic derivative plus $\alpha$ to $A_q$. The Fourier basis therefore gives
a complete Riesz basis $\tau^{-1/2}e^{\lambda_ns}$. All eigenvalues are
algebraically simple, with no generalized vectors, by this similarity to a
diagonal operator. The condition number of this specified multiplication
similarity is $\|M_\alpha\|\|M_\alpha^{-1}\|=1/|q|$.
It is not asserted to be an optimal basis-condition invariant.

For $q=0$ the same formula is valid for **every** $z\in\mathbb C$ and reduces to
$$\boxed{R(z,A_0)f(s)=\int_s^\tau e^{z(s-r)}f(r)\,dr.}$$
It is entire in the bounded-operator norm by the locally uniform exponential
series. Thus $\sigma(A_0)=\varnothing$. Compact resolvent does not force a
nonempty spectrum for this non-self-adjoint unbounded generator. There is no
contradiction with nonempty spectrum for bounded complex operators.

## 4. Transparent resolvent norm and all pseudospectra

Write $z=x+iy$, with $x,y$ real. Multiplication by $e^{iys}$ is unitary and
conjugates $R(x,A_0)$ to $R(z,A_0)$, so the norm depends only on $x$.
By invertibility, the reciprocal squared norm is
$$\mu_0(x)=\inf_{0\ne u\in H^1,\ u(\tau)=0}
\frac{\int_0^\tau|xu-u'|^2\,ds}{\int_0^\tau|u|^2\,ds}.$$
The numerator is
$\int(|u'|^2+x^2|u|^2)\,ds+x|u(0)|^2$.
Compact interval embedding and this closed semibounded form give a least
eigenfunction. Variation yields
$$-u''+x^2u=\mu u,\qquad u(\tau)=0,\qquad u'(0)=xu(0).$$
For $x\tau>-1$, the unique $\theta\in(0,\pi)$ satisfying
$$x\tau=-\theta\cot\theta$$
gives the positive interior eigenfunction
$u(s)=\sin(\theta(1-s/\tau))$. The map $-\theta\cot\theta$ increases
strictly from $-1$ to infinity: its derivative has numerator
$\theta-\sin\theta\cos\theta>0$, since this numerator has derivative
$2\sin^2\theta$ and vanishes at zero. Its eigenvalue is
$\theta^2/(\tau^2\sin^2\theta)$.
For $x\tau<-1$, the unique $h>0$ satisfying
$$x\tau=-h\coth h$$
gives $u(s)=\sinh(h(1-s/\tau))$ and eigenvalue
$h^2/(\tau^2\sinh^2h)$. Strict monotonicity of $h\coth h$ follows from
$\sinh h\cosh h-h>0$. At $x\tau=-1$, take $u(s)=\tau-s$ and
$\mu=1/\tau^2$. Each displayed eigenfunction is strictly positive in the
interior. It is the lowest eigenfunction: minimizing the Rayleigh quotient
allows a nonnegative minimizer; its ODE and uniqueness imply strict positivity,
and two positive eigenfunctions with different eigenvalues cannot be
orthogonal. This establishes that no unlisted smaller root controls the norm.
Consequently
$$\boxed{\rho_\tau(x):=\|R(x+iy,A_0)\|=
\begin{cases}\tau\sin\theta/\theta,&x\tau>-1,\\
\tau,&x\tau=-1,\\
\tau\sinh h/h,&x\tau<-1.
\end{cases}}$$
The first branch strictly decreases with $\theta$, and $\theta$ increases
with $x$; the second strictly increases with $h$, while $h$ decreases with $x$.
The two one-sided limits are $\tau$. Hence $\rho_\tau$ is continuous and
strictly decreasing from infinity to zero as $x$ goes from minus to plus
infinity. For each $\varepsilon>0$ there is exactly one $a_\varepsilon$ with
$\rho_\tau(a_\varepsilon)=1/\varepsilon$, and
$$\sigma_\varepsilon(A_0)=\{z:\operatorname{Re}z<a_\varepsilon\}.$$
For example $\rho_\tau(0)=2\tau/\pi$ and
$a_{\pi/(2\tau)}=0$. The strict inequality is part of our convention.

## 5. Schatten ideals, trivial regularized determinant, and noncompact evolution

At $z=0$ the singular values of $R(0,A_0)$ follow from the preceding separated
problem with $x=0$, now including every eigenvalue:
$$s_n(R(0,A_0))=\frac{\tau}{\pi(n+1/2)},\qquad n=0,1,2,\ldots.$$
The sine/cosine half-integer bases are complete by reflection to the ordinary
Fourier basis. Thus the operator is Hilbert--Schmidt but not trace class.
For every complex $z$, $R(z,A_0)=M_zR(0,A_0)M_z^{-1}$ with bounded invertible
multiplication on the finite interval. The two-sided ideal property implies
the same ideal membership for all $z$; this is not a unitary similarity unless
$\operatorname{Re}z=0$, and no equality of all singular values is claimed.
Direct integration also gives
$$\|R(x+iy,A_0)\|_{\mathrm{HS}}^2
=\int_0^\tau(\tau-d)e^{-2xd}\,dd
=\begin{cases}\dfrac{\tau}{2x}-\dfrac{1-e^{-2x\tau}}{4x^2},&x\ne0,\\
\tau^2/2,&x=0.\end{cases}$$
The $n$-th power has kernel
$e^{z(s-r)}(r-s)^{n-1}/(n-1)!$ for $r>s$ and zero otherwise.
Young's convolution inequality gives
$\|R(z,A_0)^n\|\leq e^{|x|\tau}\tau^n/n!$.
The spectral-radius formula therefore gives radius zero. Define the order-two
regularized determinant of a Hilbert--Schmidt compact operator $K$ by its
canonical product
$\det_2(I-wK)=\prod_j(1-w\lambda_j(K))e^{w\lambda_j(K)}$,
with nonzero eigenvalues repeated by algebraic multiplicity. Here there are
no nonzero eigenvalues, so
$$\det_2(I-wR(z,A_0))=1\quad\text{for every }w,z\in\mathbb C.$$
This is a statement about an explicitly named regularization, not an ordinary
trace-class Fredholm determinant. The latter is unavailable for $R(z,A_0)$.
The entire scalar $1-qe^{-z\tau}$ records the generator's eigenvalue equation
when $q\ne0$; it is not thereby an ordinary operator determinant.

For $0\leq t<\tau$, $S_0(t)$ is isometric on the infinite-dimensional subspace
of inputs supported on $(t,\tau)$. An orthonormal sequence in that subspace
has orthonormal images, so $S_0(t)$ is not compact. For $t\geq\tau$ it is zero.
For $q\ne0$, $S_q(t)$ has a bounded inverse at each fixed time; a compact
operator cannot have a bounded inverse on this infinite-dimensional space.
Thus it is not compact at any time. In particular no ordinary semigroup trace
is available before transparent extinction, and afterwards the trace is zero.

## 6. Parameter controls and Route-A boundary

For $\eta>0$, $q(1/\eta)=-q(\eta)$. The paired systems have exactly the same
semigroup norm but their nonzero spectra are shifted by $i\pi/\tau$ modulo
$2\pi i/\tau$. At $\eta\to1$ all eigenvalue real parts tend to minus infinity
while the specified Riesz-similarity condition number diverges; the norm stays
one for $t<\tau$. This is a singular spectral limit, not evidence of a missing
finite spectral cutoff. The physical involution $(u,v)\mapsto(u,-v)$ maps
the impedance domain for $\eta$ to that for $-\eta$; for positive damping it
does not preserve the frozen dissipative family. At $\eta=0$ it is the usual
time reversal of the conservative source. No claim about arbitrary abstract
antiunitaries is made.

The tuple is $(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
\mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT})$, overall
`ROUTE_A_REJECTED`. The wave source and its natural generator are concrete;
there is no rational-prime owner, primitive arithmetic correspondence,
target divisor or functional equation, or Hilbert--Pólya identification.
`NO_BAD_EULER_OR_ROOT_NUMBER`; all nine target/Route-B flags are false.

## Ownership, corrections, and open risks

Driscoll and Trefethen, *Pseudospectra for the wave equation with an absorbing
boundary*, J. Comput. Appl. Math. 69 (1996), 125--142,
DOI 10.1016/0377-0427(95)00021-6, owns the classical absorbing-wave spectral,
extinction and pseudospectral mechanism. This package makes no priority claim.
The proof above is self-contained, and the package increment is a complete
domain/clock/ideal boundary joined to independently recomputable evidence.
The author's website PDF returned 404, but the same PDF was successfully
retrieved from the author's GitHub repository and its extracted text read in
this turn. Its SHA-256 is
`3508aa95de58561226b784ceae03119d2c5d579893c5f504d9872ba446538166`.
Equations (14)--(19), (25), and Theorem 1 substantiate the source ownership.
The paper's Theorem 1 gives bounds and invariances, not the exact three-branch
Sturm--Liouville norm formula derived here. No literature priority is asserted
for that derivation. The optional PDF structural preflight returned UNAVAILABLE
because pypdf is absent; equation identifiers are used rather than certified
local-page anchors. No source is marked human-read.

There is no unresolved mathematical step within the frozen parameter range.
Variable coefficients, interior damping, infinite impedance, target arithmetic,
and other regularizations remain outside scope. Finite numerical checks are
regression, not interval certification or a substitute for the infinite theorem.
