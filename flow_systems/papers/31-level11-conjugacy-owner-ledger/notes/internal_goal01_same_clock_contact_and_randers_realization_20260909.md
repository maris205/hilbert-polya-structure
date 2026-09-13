# Internal Goal01: same-clock contact and Randers realization

Date: 2026-09-09.
Status: a proved classical geometric identification of the existing P31 flow.
This note does not create a new flow family, a quantum operator, a Route-B
assessment, a spectral claim, or a canonical manuscript revision.

## 1. Fixed object and conclusion

Let \(Y=Y_0(11)\) carry its complete hyperbolic metric \(g\), let
\(M=S_gY=T^1Y\), and let \(\pi:M\to Y\) be the projection.
Keep the inherited P26/P31 normalization

\[
\omega=2\pi i f(z)\,dz,\qquad
\alpha=\operatorname{Re}\omega,\qquad
\beta=\varepsilon\alpha,\qquad \varepsilon\in\mathbb R.
\tag{1}
\]

Here \(\alpha\) is a globally defined smooth closed real one-form.
The existing physical clock is

\[
\rho(x,u)=1+\beta_x(u)\ge c_0>0
\quad\text{for every }(x,u)\in S_gY,\qquad
X_\varepsilon=\frac{X_{\rm geo}}{\rho}.
\tag{2}
\]

These are the frozen definitions in the
[P26 README](../../26-level11-newform-time-change/README.md#frozen-dynamical-system).
In particular, \(\rho\) is a slowness factor, not a speed multiplier.

Define the standard geodesic contact form and its closed-form perturbation by

\[
(\lambda_{\rm geo})_{(x,u)}(\xi)
 =g_x(u,d\pi\,\xi),\qquad
\lambda_\varepsilon=\lambda_{\rm geo}+\pi^*\beta.
\tag{3}
\]

Also define, on all of \(TY\),

\[
F(x,v)=|v|_g+\beta_x(v),\qquad F(x,0)=0.
\tag{4}
\]

**Theorem.** Under (1)--(2), \(F\) is a smooth strongly convex Randers
metric away from the zero section. The Reeb vector field of
\(\lambda_\varepsilon\) is exactly \(X_\varepsilon\), and

\[
\lambda_\varepsilon\wedge d\lambda_\varepsilon
 =\rho\,\lambda_{\rm geo}\wedge d\lambda_{\rm geo}.
\tag{5}
\]

The map

\[
\Psi:S_gY\longrightarrow S_FY,\qquad
\Psi(x,u)=\left(x,\frac{u}{\rho(x,u)}\right)
\tag{6}
\]

is a smooth, time-preserving conjugacy from \(X_\varepsilon\) to the
unit-speed \(F\)-geodesic flow. It also pulls the \(F\)-Hilbert contact
form back to \(\lambda_\varepsilon\). Both flows are complete, and their
primitive oriented orbits have exactly the existing physical periods
\(T_\varepsilon(P)=\ell_g(P)+\varepsilon I(P)\).

No global exactness of \(\alpha\), compactness of \(Y\), or additional
curvature assumption is needed for this theorem.

## 2. All-direction positivity implies strong convexity

Apply (2) to \(u\) and \(-u\). For every \(g\)-unit vector,

\[
c_0-1\le\beta_x(u)\le 1-c_0.
\]

Consequently \(0<c_0\le1\) and

\[
\|\beta_x\|_g\le1-c_0<1,\qquad
c_0|v|_g\le F(x,v)\le(2-c_0)|v|_g.
\tag{7}
\]

Thus (4) is positive off the zero section, positively homogeneous,
continuous at zero, and smooth on the slit tangent bundle.
The norm bound is a consequence of the original all-unit-vector hypothesis;
it is not a new smallness assumption on the flow.

For strong convexity, fix \(x\), take \(v\ne0\), and put
\(r=|v|_g\), \(u=v/r\). For any \(w\in T_xY\),

\[
D_vF(w)=\langle u,w\rangle_g+\beta_x(w),\qquad
D_v^2F(w,w)=
\frac{|w|_g^2-\langle u,w\rangle_g^2}{r}.
\]

Hence the fundamental quadratic form is exactly

\[
\begin{aligned}
D_v^2\!\left(\frac12F^2\right)(w,w)
={}&\bigl(\langle u,w\rangle_g+\beta_x(w)\bigr)^2\\
&+\frac{F(x,v)}{|v|_g}
\bigl(|w|_g^2-\langle u,w\rangle_g^2\bigr).
\end{aligned}
\tag{8}
\]

If \(w\ne0\) has a nonzero component perpendicular to \(u\), the second
term is strictly positive by (7). If \(w=a u\ne0\), the first term equals
\(a^2(1+\beta_x(u))^2\ge a^2c_0^2>0\).
This proves positive definiteness, not merely weak convexity.

## 3. Exact Reeb field and contact volume

The standard unit-speed geodesic field satisfies

\[
\lambda_{\rm geo}(X_{\rm geo})=1,\qquad
\iota_{X_{\rm geo}}d\lambda_{\rm geo}=0.
\]

Since \(d\beta=0\), (3) gives

\[
d\lambda_\varepsilon=d\lambda_{\rm geo},\qquad
\lambda_\varepsilon(X_{\rm geo})=\rho.
\tag{9}
\]

To check contactness without assuming it, evaluate both top forms in (5)
on a basis \((X_{\rm geo},e_1,e_2)\).
The terms with \(d\lambda_{\rm geo}(X_{\rm geo},\cdot)\) vanish, and the
remaining coefficient is respectively \(\rho\) and \(1\).
This proves (5). Since \(\rho>0\), \(\lambda_\varepsilon\) is a contact
form with the same contact-volume orientation as \(\lambda_{\rm geo}\).

Equations (9) now imply

\[
\lambda_\varepsilon(X_\varepsilon)=1,\qquad
\iota_{X_\varepsilon}d\lambda_\varepsilon=0.
\tag{10}
\]

Uniqueness in the definition of a Reeb field proves the claimed equality.
Notice that the contact form here is
\(\lambda_{\rm geo}+\pi^*\beta\), not \(\rho\lambda_{\rm geo}\).
Multiplying a contact form by a function generally introduces a
\(d\rho\wedge\lambda_{\rm geo}\) term and is a different construction.

Cartan's formula and (10) give
\(\mathcal L_{X_\varepsilon}\lambda_\varepsilon=0\).
Thus the flow preserves its contact volume.
If the convention for geodesic Liouville measure is
\(d\mu_{\rm geo}=C\lambda_{\rm geo}\wedge d\lambda_{\rm geo}\),
then the corresponding unnormalized physical invariant measure is
\(\rho\,d\mu_{\rm geo}\), not \(\rho^{-1}d\mu_{\rm geo}\).
Its probability normalization, when desired, is
\(Z^{-1}\rho\,d\mu_{\rm geo}\), where \(Z=\int_M\rho\,d\mu_{\rm geo}\)
is finite because \(Y\) has finite hyperbolic area and (7) bounds \(\rho\).

## 4. Closedness gives the same unparameterized geodesics

Let \(x_s:[a,b]\to Y\) be a smooth variation of a regular curve with
fixed endpoints, and write \(V=\partial_s x_s|_{s=0}\).
Direct variation of the one-form integral gives

\[
\left.\frac{d}{ds}\right|_{s=0}
\int_a^b\beta_{x_s(t)}(\dot x_s(t))\,dt
=[\beta(V)]_a^b+
\int_a^b d\beta(V,\dot x_0)\,dt=0.
\tag{11}
\]

Therefore the first variations of \(F\)-length and \(g\)-length coincide.
Their regular stationary curves are the same oriented, unparameterized
geodesics. This closed-form observation also appears explicitly in
Matveev--Saberali,
[Example 1.1](https://link.springer.com/article/10.1007/s00013-020-01533-5)
(DOI: 10.1007/s00013-020-01533-5).

Equation (11) does not assert that the one-form integral has the same
value on arbitrary paths with the same endpoints.
It is constant under fixed-endpoint homotopies, but different relative
homotopy classes can have different values when \(\beta\) is not exact.
In particular, closedness does not make the physical closed-orbit
periods equal to their original \(g\)-lengths.

The parameter matters as well. With the convention
\(\mathrm{EL}(L)=\frac{d}{dt}\partial_vL-\partial_xL\), one has

\[
\mathrm{EL}\!\left(\frac12F^2\right)
=F\,\mathrm{EL}(F)+\frac{dF}{dt}\,\partial_vF.
\tag{12}
\]

Thus a stationary regular \(F\)-length curve with constant \(F\)-speed
solves the regular energy geodesic equation. In particular, its
\(F\)-unit-speed parametrization is the geodesic-flow parametrization.
Strong convexity from (8) supplies the regularity of that equation.

## 5. Hilbert-form pullback and same-time conjugacy

The \(F\)-Hilbert form on \(S_FY=\{F=1\}\) is

\[
(\lambda_F)_{(x,v)}(\zeta)
=D_vF(x,v)[d\pi_F\,\zeta]
=g_x\!\left(\frac{v}{|v|_g},d\pi_F\,\zeta\right)
 +\beta_x(d\pi_F\,\zeta).
\tag{13}
\]

Here \(\pi_F:S_FY\to Y\) is the base projection.
The standard Hilbert-form/Reeb convention used in (13) is recorded in
Barthelmé,
[arXiv:1410.1069v2, §1](https://arxiv.org/pdf/1410.1069).
That paper's Lemma 8 gives the additive Hilbert-form transformation,
and Lemma 11(1) gives the closed-form time-change criterion.
Only these classical geometric passages are used here, not its spectral
results or its separate assertions under compactness or exactness.

For \(u\in S_gY\), homogeneity gives \(F(u/\rho(u))=1\), so (6) is
well-defined. Its inverse is

\[
\Psi^{-1}(x,v)=\left(x,\frac{v}{|v|_g}\right),\qquad v\in S_FY.
\tag{14}
\]

Indeed, if \(u=v/|v|_g\), then \(1=F(v)=|v|_g\rho(u)\).
Both maps are smooth. Since \(\pi_F\circ\Psi=\pi\) and
\((u/\rho)/|u/\rho|_g=u\), (13) directly yields

\[
\boxed{\Psi^*\lambda_F=\lambda_\varepsilon.}
\tag{15}
\]

Thus this is a strict contact-form identification, not just an
identification of contact distributions.

For an explicit check of time, let \((x(\tau),u(\tau))\) be an original
unit-speed \(g\)-geodesic trajectory, and put

\[
t(\tau)=\int_0^\tau\rho(x(\sigma),u(\sigma))\,d\sigma.
\tag{16}
\]

Then \(d\tau/dt=1/\rho\). The trajectory on \(S_gY\), viewed at time \(t\),
is precisely a trajectory of \(X_\varepsilon\), while its base velocity is

\[
\frac{dx}{dt}=\frac{u}{\rho},\qquad
F\!\left(x,\frac{dx}{dt}\right)=1.
\tag{17}
\]

Sections 4 and (12) show that this is the \(F\)-unit-speed geodesic with
initial vector \(\Psi(x(0),u(0))\).
Uniqueness of the energy geodesic equation proves

\[
\boxed{\Psi\circ\Phi_\varepsilon^t=\Phi_F^t\circ\Psi.}
\tag{18}
\]

There is no additional time change in (18). Equivalently, (15) carries
the Reeb field in (10) to the Reeb field of \(\lambda_F\).
This statement does not assert a time-preserving conjugacy between the
original \(X_{\rm geo}\) and \(X_\varepsilon\).

Since \(g\) is complete and \(dt/d\tau\ge c_0>0\), (16) maps the whole
real \(\tau\)-axis onto the whole real \(t\)-axis.
Consequently both flows in (18) are complete, including in the cusps.
No global derivative bound on \(\beta\) or compactness argument is needed.

## 6. Primitive periods and nonreversibility

Let \(P\) be a primitive oriented \(g\)-geodesic of length \(\ell_g(P)\).
Since (16) is strictly increasing, its first return under the physical
flow occurs after precisely one original traversal:

\[
\begin{aligned}
T_\varepsilon(P)
&=\int_0^{\ell_g(P)}\rho(x(\tau),u(\tau))\,d\tau\\
&=\ell_g(P)+\int_P\beta
 =\ell_g(P)+\varepsilon I(P).
\end{aligned}
\tag{19}
\]

A shorter physical return would give a shorter original return, contrary
to primitivity. The diffeomorphism and same-time identity (18) therefore
preserve primitivity and this numerical period. Also,

\[
\int_{\text{physical orbit}}\lambda_\varepsilon
=T_\varepsilon(P)=\ell_F(P),\qquad
T_\varepsilon(P^r)=rT_\varepsilon(P)\quad(r\ge1).
\tag{20}
\]

The new metric is reversible exactly when \(\beta\equiv0\), because

\[
F(x,v)-F(x,-v)=2\beta_x(v).
\tag{21}
\]

For the actual nonzero \(\alpha\), every \(\varepsilon\ne0\) in the
positivity interval therefore gives a nonreversible metric, not a
Riemannian norm. At \(\varepsilon=0\) it reduces to \(|v|_g\).
Nonzero \(\alpha\) and its nonzero period class were established in the
[nonzero-period note](internal_goal01_nonzero_period_and_exact_unitarizability_boundary_20260909.md).
Although reversed paths are still unparameterized geodesics, their periods
are in general different:

\[
T_\varepsilon(P^{-1})
=\ell_g(P)-\varepsilon I(P)
=T_{-\varepsilon}(P).
\tag{22}
\]

No orientation quotient or reversible-clock replacement is made.

## 7. Scope, evidence, and actions

The theorem is a direct calculation for the existing clock.
The cited primary sources corroborate the standard geometric interface;
the strong-convexity formula, volume identity, explicit map, and time
normalization are written out above and are not inferred from a source title.
The source passages were inspected on 2026-09-09; the Barthelmé source
used is the author preprint v2, dated 2015-06-22.

This note establishes neither constant flag curvature nor any prescribed
Finsler curvature, spectral identity, determinant realization, quantization,
operator domain, self-adjointness result, or Route verdict.
It does not expand the separate cotangent/Hamiltonian calculation.
The noncompact flow is handled only to the extent needed for the stated
global same-time conjugacy and finite invariant measure.

This is an AI-assisted internal proof note. A bounded second-agent paper
check agreed on (7)--(8), the variational distinction, and (18); that
agreement is not independent external mathematical evidence.
The authorized repository action is this one new note only.
No scientific program, orbit census, experiment, locked input, earlier note,
README, canonical manuscript, or Route state is changed.
