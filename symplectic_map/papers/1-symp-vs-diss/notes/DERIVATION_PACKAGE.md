# Derivation Package

## Target

Organize the exact geometric identities for the Hénon homotopy, the obstruction
to a regular projection-preserving lift of the critical quadratic map, and the
conditional connection between unstable multipliers and an Euler product.

## Status

COHERENT AFTER REFRAMING / EXTRA ASSUMPTION

The geometry is exact. The arithmetic Euler-product interpretation is a
falsifiable hypothesis, not a derived fact.

## Invariant objects

The geometric invariant is the pullback of the standard two-form. The
arithmetic diagnostic uses the unstable multiplier of a primitive hyperbolic
orbit; it does not identify iteration period with \(\log p\).

## Assumptions and notation

- \(H_{a,\rho}(x,y)=(1-a x^2-\rho y,x)\), with \(a>0\) and \(0\leq\rho\leq1\).
- \(\Omega=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\).
- A primitive period-\(n\) orbit is \(\gamma=(z_0,\ldots,z_{n-1})\), with
  \(H(z_j)=z_{j+1\bmod n}\) and no smaller period.
- \(M_\gamma=DH(z_{n-1})\cdots DH(z_0)\).
- A hyperbolic orbit has an eigenvalue \(\Lambda_{u,\gamma}\) with modulus
  greater than one; set \(\ell_\gamma=\log|\Lambda_{u,\gamma}|\).

## Derivation map

1. Differentiate the homotopy to obtain the exact conformal factor.
2. Multiply determinants along an orbit to obtain the monodromy determinant.
3. At \(\rho=1\), derive a type-1 generating function and periodic action.
4. Apply the chain rule and the symplectic determinant condition to a putative
   projection-preserving lift.
5. Expand a preregistered unstable-multiplier Euler product. Only a subsequent
   prime-multiplier correspondence could turn it into a rational-prime Euler
   product.

## Main derivation

### 0. Exact status of the inherited parameter

The frozen value (u_c=1.5436890126920763\ldots) is the positive real root of

\[
u^3-2u^2+2u-2=0.
\]

For (f_u(x)=1-u x^2), this identity gives the exact post-critical itinerary

\[
0\mapsto1\mapsto1-u\mapsto u-1\mapsto u-1.
\]

Indeed (1-u(u-1)^2=u-1) is equivalent to the cubic above.  The terminal
fixed point is repelling because its multiplier is
\(-2u(u-1)=-1.67857\ldots).  Thus the inherited endpoint is a
post-critically finite/Misiurewicz parameter, not a generic fitted decimal.
This exact provenance does not by itself make its symbolic language specific
to rational primes.

### 1. Conformal symplectic identity

The Jacobian is

\[
DH_{a,\rho}(x,y)=
\begin{pmatrix}-2ax&-\rho\\1&0\end{pmatrix},
\qquad \det DH_{a,\rho}=\rho.
\]

For every real \(2\times2\) matrix \(A\),
\(A^\mathsf T\Omega A=(\det A)\Omega\). Therefore

\[
DH_{a,\rho}^{\mathsf T}\Omega DH_{a,\rho}=\rho\Omega.
\]

This is an identity. Thus \(\rho=1\) is symplectic, \(0<\rho<1\) is
conformally symplectic, and \(\rho=0\) is singular.

Along a period-\(n\) orbit,

\[
\det M_\gamma=\prod_{j=0}^{n-1}\det DH(z_j)=\rho^n.
\]

At \(\rho=1\), the two multipliers multiply to one. This reciprocal pairing is
geometric evidence only.

### 2. Generating function and action at the symplectic endpoint

Use old coordinates \((q,p)=(x,y)\) and new coordinates
\((Q,P)=H_{a,1}(q,p)\). Then

\[
Q=1-aq^2-p,\qquad P=q.
\]

The type-1 generating function

\[
S_a(q,Q)=qQ-q+\frac a3 q^3
\]

satisfies

\[
p=-\partial_qS_a(q,Q)=1-aq^2-Q,
\qquad P=\partial_QS_a(q,Q)=q.
\]

The periodic action

\[
\mathcal A_\gamma=\sum_{j=0}^{n-1}S_a(q_j,q_{j+1})
\]

is consequently intrinsic to the same symplectic map. No corresponding
canonical action is asserted for \(\rho<1\).

### 3. Projection-preserving lift obstruction

Let \(f\colon I\to I\) be \(C^1\) and suppose a \(C^1\) planar map has the
triangular form

\[
F(q,p)=(f(q),P(q,p)).
\]

Then

\[
\det DF(q,p)=f'(q)\,\partial_pP(q,p).
\]

If \(F\) is symplectic near \((q,p)\), the determinant equals one. Hence a
finite \(\partial_pP\) requires \(f'(q)\neq0\). For
\(f_a(q)=1-aq^2\), \(f_a'(0)=0\), so no \(C^1\) symplectic map of this form
is defined on a neighborhood containing \(q=0\).

More invariantly, if a smooth submersion \(\pi\) and a diffeomorphism \(F\)
satisfy \(\pi\circ F=f\circ\pi\), differentiation gives

\[
D\pi_{F(z)}DF_z=Df_{\pi(z)}D\pi_z.
\]

At a point with \(Df=0\), the right-hand side has rank zero. The left-hand
side is surjective because \(D\pi\) is surjective and \(DF\) invertible, a
contradiction. This standard obstruction excludes a smooth submersion factor;
it does not exclude inverse-limit or branch-extended topological realizations.

The ordinary Hénon map evades the contradiction because its first coordinate
depends on the memory variable \(y\), but then its projection is not
semiconjugate to \(f_a\). Arithmetic information must therefore be re-tested.

### 4. Conditional unstable-multiplier Euler product

For a frozen primitive hyperbolic ledger, define provisionally

\[
Z_u(s)=\prod_{\gamma}
\left(1-|\Lambda_{u,\gamma}|^{-s}\right)^{-1}
\]

where the product is considered only in a half-plane in which it converges.
Termwise logarithmic differentiation, when justified by absolute convergence,
gives

\[
-\frac{Z_u'(s)}{Z_u(s)}
=\sum_\gamma\sum_{r\geq1}
\ell_\gamma |\Lambda_{u,\gamma}|^{-rs}.
\]

Repetitions automatically scale the length by \(r\). If, and only if, the
primitive unstable multipliers are intrinsically the rational primes with the
right multiplicities, this ledger becomes

\[
\sum_p\sum_{r\geq1}(\log p)p^{-rs}.
\]

That correspondence is the experiment's high-risk A0 hypothesis. It is not a
consequence of symplecticity or generic prime-orbit counting.

### 5. Separation from semiclassical stability weights

For a two-dimensional symplectic hyperbolic orbit with positive unstable
multiplier \(\Lambda\),

\[
|\det(M^r-I)|^{1/2}
=|\Lambda^{r/2}-\Lambda^{-r/2}|.
\]

Thus a Gutzwiller-type stability factor contains

\[
\frac1{|\det(M^r-I)|^{1/2}}
=\frac{\Lambda^{-r/2}}{|1-\Lambda^{-r}|},
\]

not exactly \(\Lambda^{-r/2}\). The provisional Euler product and a
semiclassical trace formula are different objects and will not be combined.

### 6. Fixed-point multiplier sanity check

At \(\rho=1\), fixed points obey

\[
a x^2+2x-1=0,
\qquad x_\pm=\frac{-1\pm\sqrt{1+a}}{a}.
\]

The negative fixed point has trace

\[
\tau=-2ax_-=2+2\sqrt{1+a},
\]

and its unstable multiplier solves \(\Lambda+\Lambda^{-1}=\tau\).  At the
frozen (u_c), \(\Lambda=4.98936295\ldots), superficially close to (5).
This is not arithmetic evidence: solving \(\Lambda=m\) for any chosen
\(m>1\) gives

\[
a_m=\frac{(m-1)^4}{4m^2}-1.
\]

In particular, (a_5=1.56) has the *exact* multiplier (5).  The preregistered
neighbor (a=1.56) therefore supplies an analytic proves-too-much control:
one prime-valued fixed-point multiplier can be created by a one-parameter
algebraic coincidence and cannot support the primitive-prime hypothesis.

## Boundaries and non-claims

- The obstruction is a standard rank fact, not a novel Hilbert--Pólya result.
- A Hénon orbit ledger does not prove that logistic arithmetic survives.
- A prime-orbit theorem of the form \(N(T)\sim e^{hT}/(hT)\) is not a
  rational-prime correspondence.
- No convergence or analytic continuation of \(Z_u\) is currently claimed.
- No Riemann-zero comparison is permitted at this stage.

## Open risks

- The inherited parameter lies in a nonuniform, strongly escaping regime, so
  complete orbit enumeration is difficult.
- Existing literature already provides sophisticated Hénon symbolic ledgers
  and determinants in hyperbolic regimes; novelty can only come from the
  frozen arithmetic-survival question or a decisive obstruction.
- The multiplier-prime hypothesis may fail immediately; this is an intended
  and publishable stopping outcome if the controls are rigorous.
