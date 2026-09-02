# Complete theorem package: constant-wind Zermelo navigation

Let \(d\ge1\) be any finite integer. Fix \(W\in\mathbb R^d\), \(c\ge0\),
and consider measurable controls \(u\) with \(|u(t)|\le c\) a.e. in
\[
\dot x=W+u,\qquad x(0)=0.
\]
For a target \(y\), put
\[
w=|W|,\qquad p=W\cdot y,\qquad r=|y|,
\qquad a=w^2-c^2,\qquad D=p^2-ar^2.
\]

## Theorem (all dimensions, winds, caps, and targets)

At exact time \(t\ge0\), the reachable set is
\[
\mathcal R(t)=Wt+ct\,\overline B.
\]
For \(y\ne0\), the reachability and minimum time are:

1. **Weak wind \(w<c\):** every target is reachable and
   \[
   T(y)=\frac{\sqrt{p^2+(c^2-w^2)r^2}-p}{c^2-w^2}.
   \]
   Its attainable times are \([T,\infty)\).
2. **Critical wind \(w=c>0\):** the target is reachable exactly when
   \(p>0\), and then
   \[
   T(y)=\frac{r^2}{2p},
   \]
   with attainable times \([T,\infty)\).
3. **Strong wind \(w>c\):** the target is reachable exactly when
   \(p>0\) and \(D\ge0\). Then
   \[
   T_-(y)=\frac{p-\sqrt D}{w^2-c^2},\qquad
   T_+(y)=\frac{p+\sqrt D}{w^2-c^2},
   \]
   the minimum is the smaller root \(T_-\), and the complete attainable-time
   set is the closed window \([T_-,T_+]\).

For every nonzero reachable target, the time-optimal control is unique up to
null sets and is constant:
\[
u_*(s)=\frac y{T(y)}-W,\qquad |u_*|=c.
\]
This includes \(c=0\), where the sole control is zero.

The value is rotation equivariant and satisfies, whenever defined,
\[
T_{QW,c}(Qy)=T_{W,c}(y),\quad
T_{W,c}(\lambda y)=\lambda T_{W,c}(y),\quad
T_{sW,sc}(y)=s^{-1}T_{W,c}(y)
\]
for orthogonal \(Q\), \(\lambda>0\), and \(s>0\). On the interior of its
finite-value domain away from \(y=0\), it is smooth and obeys
\[
W\cdot\nabla T+c|\nabla T|=1.
\]

The remaining faces are exact. If \(W=0<c\), \(T=r/c\). If \(c=0\), only
the nonnegative wind ray is reachable (and when \(W=0\), only zero is). For
\(y=0\), \(T=0\); all \(t\ge0\) are attainable iff \(w\le c\), while only
\(t=0\) is attainable if \(w>c\). For \(0<c<w\), the full finite-value
domain is the closed forward Mach cone
\[
\{0\}\cup\{y\ne0:p>0,\ p^2\ge(w^2-c^2)r^2\}.
\]
Equivalently it is \(p\ge\sqrt{w^2-c^2}\,r\), so the origin is included.
Its boundary \(D=0\), when nontrivial (in particular in dimensions at least
two), is a double-root boundary with square-root loss of regularity.

## Proof

Integration gives
\(x(t)=Wt+\int_0^t u(s)\,ds\). The averages of all admissible controls fill
\(c\overline B\), hence \(\mathcal R(t)=Wt+ct\overline B\). Thus \(y\) is
reachable at time \(t\) exactly when
\[
|y-Wt|^2\le c^2t^2,
\]
or
\[
f(t)=(w^2-c^2)t^2-2pt+r^2\le0. \tag{1}
\]

For \(y\ne0\), \(f(0)=r^2>0\). If \(a<0\), the quadratic opens downward,
has one negative and one positive root, and is nonpositive exactly after the
positive root; rationalizing it gives the weak formula. If \(a=0\), (1) is
linear and has a positive solution exactly when \(p>0\), with threshold
\(r^2/(2p)\). If \(a>0\), (1) has nonnegative-time solutions exactly when
\(p>0\) and \(D\ge0\); both roots are positive, and the inequality holds
precisely between them. This proves reachability, the smaller-root minimum,
and every time set. Substitution of \(y=0\) gives \(at^2\le0\), proving its
separate classification. Cauchy--Schwarz reduces the \(c=0\) condition to
the nonnegative wind ray.

At first contact, \(|y-WT|=cT\). Any optimal control satisfies
\[
\left|\frac1T\int_0^T u(s)\,ds\right|=c
\le\frac1T\int_0^T|u(s)|\,ds\le c.
\]
Equality in the strictly convex Euclidean triangle inequality forces
\(u(s)\) to equal the single vector \(y/T-W\) a.e.; for \(c=0\) this is
immediate. Hence the optimizer is unique.

Rotations and scalings follow either from the control system or directly
from the invariants \(p,r,w,c\). Suppose first that \(c>0\). In a smooth
finite-value interior, first contact satisfies
\(F(y,T)=|y-WT|^2-c^2T^2=0\). Implicit differentiation
gives
\[
\nabla T=\frac{y-WT}{p-(w^2-c^2)T}.
\]
The denominator is \(\sqrt D>0\) on the selected smooth root (and equals
\(p>0\) in the critical chamber). Since \(|y-WT|=cT\), dotting with \(W\)
and taking norms yields the HJB identity. If \(c=0\) and \(d>1\), the
reachable ray has empty Euclidean interior. If \(c=0\) and \(d=1\), on the
open ray in the direction of \(W\ne0\), writing
\(e=W/|W|\) and \(y=se\) gives \(T=s/|W|\),
\(\nabla T=e/|W|\), and \(W\cdot\nabla T=1\) directly. On a nontrivial
strong-wind cone boundary \(D=0\) with \(c>0\), the radical has the stated
square-root singularity.

## Evidence and limitations

The archive contains 29 cases, 12 HJB/scaling probes, eight boundary rows,
and 744 audited leaves. They exercise formulas but do not prove the
all-parameter theorem. Weak wind may be viewed as the gauge of a convex
velocity ball containing the origin; no global strong-wind Finsler norm is
claimed. Variable wind, obstacles, state constraints, and manifolds are
outside scope.

The closest repository controls remain distinct: C222 is a second-order
double-integrator bang--bang system; C270 uses Heisenberg sub-Riemannian
geometry; C268 is an uncontrolled constant-field Lorentz flow. C305 is the
first-order constant-drift Euclidean navigation atlas.

The Route-A tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, overall
`ROUTE_A_REJECTED`, with Route B locked.
