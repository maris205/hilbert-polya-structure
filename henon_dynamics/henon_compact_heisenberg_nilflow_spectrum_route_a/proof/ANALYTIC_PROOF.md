# Compact Heisenberg nilflows: every closed orbit and the complete spectrum

## Claim and status

**PROVABLE AS STATED.** The two-parameter family $W=X+\beta Y+\gamma Z$
on the left integer Heisenberg quotient has the complete closed-orbit atlas,
explicit Fourier–Schrödinger decomposition and same-clock reversor below.
The original physical time is retained. There are no nontrivial time changes
or claims about their mixing. The results are a source-local reconstruction
of classical nilflow mechanisms, not a literature-priority certificate.

## Assumptions and notation

Let $H=\mathbb R^3$ with
$$ (x,y,z)(x',y',z')=(x+x',y+y',z+z'+xy'), $$
$\Gamma=\mathbb Z^3$, and $M=\Gamma\backslash H$. Haar measure has mass
one on the unit cube. The left-invariant fields
$X=\partial_x$, $Y=\partial_y+x\partial_z$, $Z=\partial_z$ descend to
$M$. Fix arbitrary real $\beta,\gamma$ and $W=X+\beta Y+\gamma Z$.
For the Koopman group use $U_t f=f\circ\phi_t=e^{itA}f$ and $A=-iW$.
The torus Fourier convention is $e^{2\pi i(kx+ly)}$.

## Dependency map

1. Explicit group multiplication gives the flow and quotient return condition.
2. Primitive rational slope and the central return phase give all closed
   orbits, least periods and clean fixed tori.
3. A global cross-section gives a skew shift; a finite-difference Weyl argument
   proves unique ergodicity at every irrational slope.
4. Fourier expansion in the central and horizontal variables gives an explicit
   unitary decomposition, without assuming a representation-theory formula.
5. Chirp conjugation gives self-adjoint domains and the complete spectrum.
6. A source involution gives same-clock reversal; multiplication operators on
   a continuous spectral block prove the determinant obstructions.

## 1. The complete flow and its quotient convention

Integration of $\dot x=1$, $\dot y=\beta$, $\dot z=\gamma+\beta x$ gives
$$ \phi_t(x,y,z)=(x+t,y+\beta t,z+\gamma t+\beta xt+\beta t^2/2). \tag{1} $$
It is right multiplication by $(t,\beta t,\gamma t+\beta t^2/2)$ and
therefore is well-defined on the left quotient. It is a complete smooth
volume-preserving flow with no stationary point since its $x$ velocity is one.

Two representatives describe the same point if, for integers $r,s,k$,
$$ (x',y',z')=(x+r,y+s,z+k+r y). \tag{2} $$
Thus a nonzero return time must have $t\in\mathbb Z$ and $\beta t\in\mathbb Z$.
For irrational $\beta$, this excludes every nonzero return, for every point.
Each nonzero-time map then has no fixed point, so its ordinary fixed-cardinality
Artin–Mazur zeta is one. This is not a statement about spectral determinants.

## 2. Rational slopes: all primitive periods and clean tori

Let $\beta=p/q$ in lowest terms, with $q>0$; include $p=0,q=1$.
The first possible horizontal return is $q$. Define
$$ \theta(x,y)=\gamma q+p x-q y+pq/2\pmod1. \tag{3} $$
It is a well-defined smooth circle-valued function on $M$ by (2), independent
of $z$, and is constant along the flow since $p-q\beta=0$.
At time $dq$, subtracting the necessary integer horizontal displacement
in (2) leaves central displacement congruent to
$$ d\theta+pq\,d(d-1)/2\equiv d\theta\pmod1. \tag{4} $$
The last term is an integer. Therefore a point is closed exactly when
$\theta$ is rational. If its reduced denominator is $d\ge1$, its least
positive period is $dq$. If $\theta$ is irrational, it never closes.
This describes every point and every positive time, without a cutoff.

For $t=kq>0$, the fixed set is the union of the $k$ fibres
$\theta^{-1}(j/k)$, $0\le j<k$. Each is a connected two-torus: the primitive
integer form $p x-q y$ has connected circle fibres on the base torus, and
the restriction of the central circle bundle to such a circle is trivial.
The triviality can also be seen by choosing a continuous lift of that base
circle on an interval and absorbing the endpoint's central shift by a linear
central coordinate change. There are exactly $\varphi(d)$ connected two-tori
of points with least period $dq$, where $\varphi(1)=1$.
Each such torus contains continuously many closed flow orbits.

At a fixed point of time $t=kq$, use the integer identification in (2) as a
local chart transition. The return derivative is
$$ D\phi_t=\begin{pmatrix}1&0&0\\0&1&0\\\beta t&-t&1\end{pmatrix}. \tag{5} $$
Its difference from the identity has rank one and kernel equal to the tangent
plane of the fixed torus. Hence the return is clean, not isolated. All three
multipliers are one, and the transverse Poincaré map is a nontrivial unipotent
two-dimensional map. An isolated-orbit denominator $\det(I-D\phi_t)$ vanishes;
it cannot be repaired by enumerating a sample of the torus.

For a fixed strobe $h\ne0$ at rational $\beta$, if $h/q$ is irrational then
every positive iterate has no fixed point. If $h/q$ is rational, some
positive iterate has an uncountable fixed set. Its ordinary cardinality zeta
is consequently either one or undefined, not a finite orbit determinant.

## 3. Unique ergodicity without a Diophantine restriction

The section $x=0\pmod1$ is global with return time one. Its coordinates
$(y,z)\in\mathbb T^2$ obey, from (1) and (2),
$$ S(y,z)=(y+\beta,z-y+\gamma-\beta/2). \tag{6} $$
After $n$ returns,
$$ y_n=y+n\beta,\qquad z_n=z-ny+n\gamma-\beta n^2/2. \tag{7} $$
For a character indexed by $(k,l)\ne(0,0)$ its orbit phase is a constant
plus $n(k\beta-ly+l\gamma)-l\beta n^2/2$.
If $l=0$ and $\beta$ is irrational, the geometric-series average tends to
zero uniformly in the starting point. If $l\ne0$, for any fixed nonzero
lag $h$ the phase difference has irrational linear coefficient $-l\beta h$.
The van der Corput inequality bounds the limsup of the squared average by
$O(1/H)$ after taking $N\to\infty$ at fixed averaging-lag cutoff $H$;
each finite-lag geometric sum tends uniformly to zero. Sending $H\to\infty$
proves uniform convergence for that quadratic character. This order of limits
uses no uniform Diophantine bound over $\beta$.

Trigonometric approximation then gives uniform Birkhoff convergence for
every continuous function on the section, to its Haar integral. Any invariant
probability must have these same integrals, proving unique ergodicity of $S$.
The constant-roof suspension is the original flow, so $\phi_t$ is uniquely
ergodic for every irrational $\beta$. Rational $\beta$ has the nonconstant
invariant function (3), so it is not ergodic for Haar measure.
The time-one map on the whole three-manifold is not ergodic, even when
$\beta$ is irrational: the nonconstant function $e^{2\pi ix}$ is invariant
under $U_1$. The section map $S$ and the whole time-one map have different
phase spaces; neither this distinction nor the physical clock is suppressed.

## 4. A full explicit Hilbert-space decomposition

Expand a function first in the periodic central coordinate:
$f(x,y,z)=\sum_{m\in\mathbb Z}e^{2\pi imz}f_m(x,y)$.
The lattice convention gives
$$ f_m(x+r,y+s)=e^{-2\pi imr y}f_m(x,y). \tag{8} $$
For $m=0$ this is exactly $L^2(\mathbb T^2)$. For $m\ne0$ expand in $y$,
$f_m=\sum_k f_{m,k}(x)e^{2\pi iky}$; then
$f_{m,k}(x+1)=f_{m,k+m}(x)$. For every residue
$j\in\{0,\ldots,|m|-1\}$ put $k=j+m\ell$. Every such coefficient
has the unique form $f_{m,j+m\ell}(x)=g_j(x+\ell)$.
This gives the explicit transform
$$ (V_{m,j}g)(x,y,z)=e^{2\pi imz}
 \sum_{\ell\in\mathbb Z}g(x+\ell)e^{2\pi i(j+m\ell)y}. \tag{9} $$
Initially take Schwartz $g$. The series then defines a smooth lattice-invariant
function. Parseval on $y$ followed by the tiling $x+\ell$ of $\mathbb R$ proves
$\|V_{m,j}g\|_{L^2(M)}=\|g\|_{L^2(\mathbb R)}$. Orthogonality and the reverse
coefficient construction prove completeness, including negative $m$:
$$ L^2(M)=L^2(\mathbb T^2)\oplus
 \bigoplus_{m\ne0}\bigoplus_{j=0}^{|m|-1}V_{m,j}L^2(\mathbb R). \tag{10} $$

## 5. Domains, complete spectrum and correlations

On the torus block the character $(k,l)$ has generator eigenvalue
$2\pi(k+\beta l)$. On block $(m,j)$, (9) gives
$$ A_{m,j}=-i\frac d{du}+2\pi(\beta m u+\beta j+\gamma m). \tag{11} $$
Define $\psi_{m,j}(u)=\pi\beta m u^2+2\pi(\beta j+\gamma m)u$
and the unitary multiplication $C_{m,j}g=e^{-i\psi_{m,j}}g$.
Direct differentiation yields
$A_{m,j}C_{m,j}=C_{m,j}(-i\,d/du)$.
Consequently its self-adjoint domain is exactly $C_{m,j}H^1(\mathbb R)$.
On the torus block the domain consists of Fourier coefficients with
$\sum_{k,l}|2\pi(k+\beta l)|^2|\widehat f_{k,l}|^2<\infty$.
The full domain is the direct sum with square-summable graph norms.
These explicit self-adjoint operators are the generator of the original
Koopman group: equality holds on the dense smooth transformed cores and
the unitary groups agree there by integrating (11).

Thus the torus block is pure point. When $\beta$ is irrational, its
eigenvalues are simple and dense in $\mathbb R$; when $\beta=p/q$, they
are $2\pi\mathbb Z/q$, each with countably infinite multiplicity.
Every noncentral block has multiplicity-one Lebesgue spectrum, so the
noncentral subspace has countably infinite Lebesgue multiplicity.
There is no singular-continuous component. The spectrum of the whole
generator is $\mathbb R$ for all parameters.

On a noncentral block, Fourier transformation turns correlations into
Fourier transforms of $L^1$ products of two $L^2$ functions. They tend to
zero as $|t|\to\infty$ by the Riemann–Lebesgue lemma. Finite direct-sum
approximation and Cauchy–Schwarz extend this to the full noncentral
subspace. Nevertheless the flow is not weakly mixing on the whole space:
the nonconstant torus eigenfunction $e^{2\pi ix}$ exists for every parameter.
At irrational slope this coexists with unique ergodicity and no closed orbit.

## 6. Same-clock reversal and determinant obstructions

Right translation $T_c(x,y,z)=(x,y+c,z+cx)$ is well-defined on $M$ and
sends $W_\gamma$ to $W_{\gamma+c}$. The lattice-preserving group automorphism
$I(x,y,z)=(-x,-y,z)$ sends $W_0$ to $-W_0$. Therefore
$$ J_\gamma=T_\gamma I T_{-\gamma},\qquad
 J_\gamma(x,y,z)=(-x,-y+2\gamma,z-2\gamma x), \tag{12} $$
is a measure-preserving involution satisfying $J_\gamma\phi_tJ_\gamma=\phi_{-t}$.
The antiunitary $\Theta f=\overline{f\circ J_\gamma}$ obeys
$\Theta U_t\Theta=U_{-t}$ with exactly the original time. Complex conjugation
alone commutes with $U_t$ and is not substituted for this reversal.

The infinite-dimensional unitary $U_t$ is never compact. On even a single
noncentral block the resolvent $(A-i)^{-1}$ is unitarily equivalent to
multiplication by $(2\pi\xi-i)^{-1}$ on $L^2(\mathbb R)$, and
$e^{-tA^2}$ for $t>0$ to multiplication by $e^{-4\pi^2t\xi^2}$.
Choose infinitely many orthonormal functions supported on pairwise disjoint
positive-measure subsets of $[-1,1]$. Both multipliers have modulus bounded
away from zero there, so their images have no norm-convergent subsequence.
Neither operator is compact or in any finite Schatten class. The positive
heat operator has infinite extended trace by the same orthonormal sequence.
Here the heat parameter is auxiliary: this spectral function of $A$ is not
the original unitary evolution $U_t$ and does not replace its physical clock.
No ordinary global Fredholm determinant follows from these natural owners.

## Boundaries and evidence limitations

$\beta=0$ is included with $p=0,q=1$; $\gamma$ is arbitrary, not assumed
rational. Negative central modes and all rational-slope primitive periods
are included. A vanishing $X$ component is outside this family, rather than
silently normalized through a zero divisor. The family is not the discrete
Heisenberg automorphism of C146/C151/C156, nor the noncompact geodesic of C270.
Finite rational quotient returns, symbolic identities and exact signed-mode coefficients
audit formulas; the uniform orbit and spectral statements rely on the proofs.
Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; all nine target/Route-B flags are false.
