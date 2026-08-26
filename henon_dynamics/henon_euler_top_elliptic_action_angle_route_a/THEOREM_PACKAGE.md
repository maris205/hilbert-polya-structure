# C186 theorem package: the triaxial Euler top on every energy layer

## Frozen setting

Let \(0<I_1<I_2<I_3\), put
\[
a=I_1^{-1}>b=I_2^{-1}>c=I_3^{-1},
\]
and fix angular-momentum magnitude \(G>0\). On the coadjoint sphere \(S_G^2\), write \(m=M/G\). The reduced Euler equation and normalized energy are
\[
\dot m=Gm\times\operatorname{diag}(a,b,c)m,
\qquad
e=\frac{2E}{G^2}=am_1^2+bm_2^2+cm_3^2.
\]
Thus \(c\le e\le a\). The statement below is classical integrable mechanics in one fixed convention; the exact Route-A synthesis and certificate are the package-level output.

## Main theorem

For every frozen \((a,b,c,G)\) above, the following statements hold.

### 1. Complete topology and axial stability

- At \(e=c\) the energy set consists of \(\pm e_3\); at \(e=a\) it consists of \(\pm e_1\). These four rotations are elliptic on the sphere.
- For \(c<e<b\), the energy set is two periodic circles, distinguished by the sign of \(m_3\).
- For \(b<e<a\), it is two periodic circles, distinguished by the sign of \(m_1\).
- At \(e=b\), the two points \(\pm e_2\) are hyperbolic and the remaining set is four heteroclinic branches joining them.

The squared nonzero tangent rates at either sign of the three axes are, respectively,
\[
-G^2(a-b)(a-c),\qquad
 G^2(a-b)(b-c),\qquad
-G^2(a-c)(b-c).
\]

### 2. Low-energy Jacobi chart

For \(c<e<b\), define
\[
 A^2=\frac{e-c}{a-c},\quad
 B^2=\frac{e-c}{b-c},\quad
 C^2=\frac{a-e}{a-c},
\]
\[
 k^2=\frac{(a-b)(e-c)}{(b-c)(a-e)},
 \qquad
 \Omega^2=G^2(b-c)(a-e).
\]
Then \(0<k<1\). Every regular orbit in this regime is, for one \(\sigma\in\{\pm1\}\) and phase \(t_0\),
\[
 m_1=A\operatorname{cn}(u,k),\quad
 m_2=B\operatorname{sn}(u,k),\quad
 m_3=\sigma C\operatorname{dn}(u,k),
 \qquad u=\sigma\Omega(t-t_0).
\]
Its minimal period is
\[
T_3(e)=\frac{4K(k)}{G\sqrt{(b-c)(a-e)}}.
\]

### 3. High-energy Jacobi chart

For \(b<e<a\), define
\[
 A^2=\frac{e-c}{a-c},\quad
 B^2=\frac{a-e}{a-b},\quad
 C^2=\frac{a-e}{a-c},
\]
\[
 k^2=\frac{(b-c)(a-e)}{(a-b)(e-c)},
 \qquad
 \Omega^2=G^2(a-b)(e-c).
\]
Every regular orbit is
\[
 m_1=\sigma A\operatorname{dn}(u,k),\quad
 m_2=B\operatorname{sn}(u,k),\quad
 m_3=C\operatorname{cn}(u,k),
 \qquad u=\sigma\Omega(t-t_0),
\]
with minimal period
\[
T_1(e)=\frac{4K(k)}{G\sqrt{(a-b)(e-c)}}.
\]

### 4. Singular and small-oscillation limits

At \(e=b\), let
\[
A_s^2=\frac{b-c}{a-c},\quad C_s^2=\frac{a-b}{a-c},
\quad \rho=G\sqrt{(a-b)(b-c)}.
\]
The four heteroclinic branches are
\[
m_1=\varepsilon A_s\operatorname{sech}u,\quad
m_2=\tanh u,\quad
m_3=\varepsilon\sigma C_s\operatorname{sech}u,\quad
u=\sigma\rho(t-t_0),
\]
with \(\varepsilon,\sigma\in\{\pm1\}\). Both regular periods diverge as \(e\to b\). At the stable endpoints,
\[
T_3(c)=\frac{2\pi}{G\sqrt{(b-c)(a-c)}},\qquad
T_1(a)=\frac{2\pi}{G\sqrt{(a-b)(a-c)}}.
\]

### 5. Exact action--angle atlas

Freeze the right Lie--Poisson convention
\[
\{F,H\}=-M\mathbin{\cdot}(\nabla F\mathbin{\times}\nabla H),
\qquad \dot F=\{F,H\},
\]
so \(\dot M=M\times\nabla H\).  On a positive low-energy component use
\(q=\arg(M_1+iM_2)\) and the cap momentum \(P_3=G-M_3\), for which
\(\{q,P_3\}=1\). With \(A_q=a\cos^2q+b\sin^2q\), the unsigned KKS cap
action is
\[
J_3(e)=G\left[1-\frac1{2\pi}\int_0^{2\pi}
\sqrt{\frac{A_q-e}{A_q-c}}\,dq\right].
\]
On a positive high-energy component use \(q=\arg(M_2+iM_3)\) and
\(P_1=G-M_1\), so \(\{q,P_1\}=1\).  Set
\(B_q=b\cos^2q+c\sin^2q\), and obtain
\[
J_1(e)=G\left[1-\frac1{2\pi}\int_0^{2\pi}
\sqrt{\frac{e-B_q}{a-B_q}}\,dq\right].
\]
The negative components have the same unsigned actions. With the natural orientation,
\[
\left|\frac{dJ}{dE}\right|=\frac{T(E)}{2\pi}.
\]
The Jacobi phase gives \(\theta=\pi u/(2K(k))\pmod{2\pi}\), so \(\dot\theta=\pm2\pi/T(E)\).

### 6. Sampled-time fixed sets and the zeta stop

Let \(\Phi_\tau\) be the time-\(\tau\) map with \(\tau>0\). Its \(n\)-th iterate fixes every axial equilibrium. A regular component of energy \(e\) is fixed pointwise exactly when
\[
n\tau=qT(e)\quad\text{for some integer }q\ge1.
\]
No interior point of a heteroclinic branch is fixed. Since each regular period is continuous, finite at its stable endpoint, and divergent at the separatrix, every \(\tau>0\) has positive-dimensional fixed circles for all sufficiently large iterates. Consequently the ordinary Artin--Mazur series based on finite isolated fixed-point cardinalities is not defined on the full sphere.

The KKS area is invariant, so \(U_t f=f\circ\Phi_t\) is a canonical unitary Koopman group. Away from the measure-zero equilibria and separatrix it decomposes into the two energy regimes, two components per energy, and circle Fourier modes with multipliers \(\exp(2\pi i\ell t/T(e))\). This is a natural quantization coordinate, not a Hilbert--Pólya construction.

## Proof

The two quadratic first integrals follow by taking scalar products of \(M\times I^{-1}M\) with \(M\) and \(I^{-1}M\). The restriction of the energy quadratic form to the sphere has exactly the six axial critical points; elementary Lagrange multipliers give the stated regular level topology. Linearizing the two tangent coordinates at each axis yields the three squared rates displayed above.

For the low chart, insert \(\operatorname{cn}^2=1-\operatorname{sn}^2\) and \(\operatorname{dn}^2=1-k^2\operatorname{sn}^2\). The constant and \(\operatorname{sn}^2\) coefficients in both first integrals vanish with the stated \(A,B,C,k\). The derivative rules
\[
\operatorname{sn}'=\operatorname{cn}\operatorname{dn},\quad
\operatorname{cn}'=-\operatorname{sn}\operatorname{dn},\quad
\operatorname{dn}'=-k^2\operatorname{sn}\operatorname{cn}
\]
reduce the three Euler equations to the stated \(\Omega^2\). The high chart is verified identically after permuting which component carries `dn`. The common vector period is \(4K(k)\), because `sn` and `cn` change sign after \(2K\).

As \(e\to b\), both moduli tend to one and \(\operatorname{sn}(u,1)=\tanh u\), \(\operatorname{cn}(u,1)=\operatorname{dn}(u,1)=\operatorname{sech}u\), giving the four singular branches. The logarithmic divergence of \(K(k)\) proves the period limit. At the stable endpoints \(k=0\) and \(K(0)=\pi/2\).

For the frozen bracket, direct differentiation gives
\(\{\arg(M_1+iM_2),M_3\}=-1\) and
\(\{\arg(M_2+iM_3),M_1\}=-1\).  Since \(G=|M|\) is a Casimir, the two
cap momenta above therefore have bracket \(+1\) with their angles. Solving
the energy equation for \(M_3/G\) or \(M_1/G\) yields the two displayed
cap-area integrals. The standard one-degree-of-freedom area--period identity
follows by differentiating the enclosed symplectic area; orientation accounts
for the absolute value. Finally, on a periodic circle a time map is a rigid
angle rotation, which proves the resonance criterion. Continuity plus
divergence supplies fixed circles at large iterates and closes the zeta
obstruction.

## Degenerate boundaries and nonclaims

- \(G=0\) is the single stationary origin and is outside the regular sphere theorem.
- Spherical and symmetric tops violate \(a>b>c\); their equilibrium manifolds and elementary periods require separate formulas.
- The regular Jacobi expressions are not analytically continued through \(k=1\) as if the separatrix had finite period.
- The package claims neither arithmetic semantics for \((I,E,G)\) nor a target divisor, functional equation, prime clock, Hilbert--Pólya operator, Route B, universal novelty, or external peer review.
