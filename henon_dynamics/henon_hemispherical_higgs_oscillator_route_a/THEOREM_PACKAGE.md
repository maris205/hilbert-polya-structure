# Theorem package

## 1. Classical positive-coupling system

Fix (R>0), (omega>0), and (0\le\theta<\pi/2). With
(L=p_\phi), let

\[
H=\frac{p_\theta^2}{2R^2}
 +\frac{L^2}{2R^2\sin^2\theta}
 +\frac{\omega^2R^2}{2}\tan^2\theta .
\]

Positive coupling is essential: the potential diverges at the omitted
equator, so every finite-energy trajectory remains in a compact subregion of
a smooth polar-chart atlas. Define

\[
J=\sqrt{2R^2E+\omega^2R^4}.
\]

### Theorem 1: turning points and radial action

For a regular orbit (L\ne0), set (x=\sin^2\theta). The two turning points
(0<x_-<x_+<1) are the roots of

\[
J^2x^2-(2R^2E+L^2)x+L^2=0.                 \tag{1}
\]

The radial action and its inversion are

\[
I_r=\frac1{2\pi}\oint p_\theta\,d\theta
   =\frac12(J-|L|-\omega R^2),              \tag{2}
\]

\[
H(I_r,L)=
\frac{(2I_r+|L|+\omega R^2)^2-\omega^2R^4}{2R^2}.       \tag{3}
\]

The allowed chamber is

\[
E\ge \omega|L|+\frac{L^2}{2R^2},
\]

with equality exactly on the circular face (I_r=0).

### Proof of the action integral

From (H=E),

\[
p_\theta^2=2R^2E-\frac{L^2}{x}
 -\frac{\omega^2R^4x}{1-x}
=\frac{J^2(x-x_-)(x_+-x)}{x(1-x)}.
\]

Since (d\theta=dx/(2\sqrt{x(1-x)})),

\[
I_r=\frac{J}{2\pi}\int_{x_-}^{x_+}
\frac{\sqrt{(x-x_-)(x_+-x)}}{x(1-x)}\,dx.       \tag{4}
\]

For (0<a<b<1), the substitution
(x=a+(b-a)\sin^2u), followed by
(1/[x(1-x)]=1/x+1/(1-x)), gives

\[
\int_a^b\frac{\sqrt{(x-a)(b-x)}}{x(1-x)}\,dx
=\pi(1-\sqrt{ab}-\sqrt{(1-a)(1-b)}).           \tag{5}
\]

Vieta's formulas applied to (1) give

\[
x_-x_+=\frac{L^2}{J^2},\qquad
(1-x_-)(1-x_+)=\frac{\omega^2R^4}{J^2}.
\]

Substitution in (4) proves (2), and solving (2) for (J) proves (3). The
turning roots are distinct precisely above the displayed threshold.

### Corollary 1: exact frequencies and periods

On either signed chamber (L>0) or (L<0), with (I_\phi=L),

\[
\Omega_r=\frac{\partial H}{\partial I_r}=\frac{2J}{R^2},
\qquad
\Omega_\phi=\frac{\partial H}{\partial L}
=\operatorname{sgn}(L)\frac{J}{R^2}.          \tag{6}
\]

Every regular trajectory has radial period (T_r=\pi R^2/J) and primitive
phase-space period

\[
T=\frac{2\pi R^2}{J}.                         \tag{7}
\]

The latter is twice the radial period because the angular action advances by
only (pi\operatorname{sgn}(L)) during one radial return.

## 2. Classical boundary atlas

1. **Circular:** If (I_r=0), (L\ne0), then
   (J=|L|+\omega R^2), (1) has the double root

   \[
   \sin^2\theta_c=\frac{|L|}{|L|+\omega R^2},
   \]

   and the angular period is (2\pi R^2/J). The radial angle is not used.
2. **Meridional:** If (L=0), (I_r>0), the roots are (0) and
   (1-(\omega R^2/J)^2). The polar coordinate is singular at the north pole,
   but a Cartesian tangent chart continues the trajectory smoothly. Its
   unsigned radial coordinate has period (pi R^2/J); the phase-space orbit
   closes after (2\pi R^2/J).
3. **North equilibrium:** (I_r=L=0) gives (E=0) and a fixed point.
4. **Zero classical coupling:** At (omega=0), the equatorial barrier
   disappears. The open hemisphere is not complete for trajectories crossing
   the missing equator, so no complete open-hemisphere periodic-flow theorem
   is asserted there.

## 3. Friedrichs quantum theorem for nonnegative coupling

Allow (omega\ge0), retain (R,\hbar>0), and take the Friedrichs
realization on one hemisphere of

\[
\widehat H=-\frac{\hbar^2}{2R^2}
\left[\frac1{\sin\theta}\partial_\theta
(\sin\theta\,\partial_\theta)
+\frac1{\sin^2\theta}\partial_\phi^2\right]
+\frac{\omega^2R^2}{2}\tan^2\theta .          \tag{8}
\]

Here the first radial term means
((1/\sin\theta)\partial_\theta(\sin\theta\,\partial_\theta)). Define

\[
ν=\sqrt{(\omega R^2/\hbar)^2+\frac14}.
\]

### Theorem 2: complete separated spectrum

For (m\in\mathbb Z), (n_r\ge0), and (N=2n_r+|m|), an eigenfunction,
up to normalization, is

\[
\psi_{n_r,m}=e^{im\phi}(\sin\theta)^{|m|}
(\cos\theta)^{ν+1/2}P_{n_r}^{(|m|,ν)}(\cos2\theta),       \tag{9}
\]

with energy

\[
E_N=\frac{\hbar^2}{2R^2}(N+1)(N+1+2ν).         \tag{10}
\]

The one-hemisphere multiplicity is (N+1), and these modes form a complete
orthogonal basis for the Friedrichs realization.

### Proof

Separation by (e^{im\phi}) gives a singular Sturm--Liouville problem.
Factoring the north-pole behavior ((\sin\theta)^{|m|}) and the Friedrichs
equatorial behavior ((\cos\theta)^{ν+1/2}), then setting
(y=\cos2\theta), gives

\[
(1-y^2)v''+[ν-|m|-(|m|+ν+2)y]v'
+n_r(n_r+|m|+ν+1)v=0.                         \tag{11}
\]

This is the Jacobi equation. Polynomial termination gives (9) and (10).
Jacobi completeness with its positive weight, combined with the Fourier basis
in (phi), proves completeness. For fixed (N), the allowed (m) satisfy
(|m|\le N) and (N-|m|) even. Counting signs, with one copy at (m=0),
gives (N+1).

### Corollary 2: flat and zero-coupling limits

At fixed (N,omega,\hbar), as (R\to\infty),

\[
ν=\frac{\omega R^2}{\hbar}+o(R^2),\qquad
E_N\longrightarrow\hbar\omega(N+1).           \tag{12}
\]

At (omega=0), (ν=1/2), hence

\[
E_N=\frac{\hbar^2}{2R^2}(N+1)(N+2).
\]

Writing (l=N+1), these are the Dirichlet-hemisphere levels
(hbar^2l(l+1)/(2R^2)). Their multiplicity is (l), the equator-odd sector,
not the full-sphere multiplicity (2l+1).

## 4. Exact identity-revival theorem

Let $k=N+1\ge1$ and $\tau=\hbar t/(2R^2)$. The spectral phase is

\[
\exp[-i\tau(k^2+2νk)].                         \tag{13}
\]

### Theorem 3

The full propagator equals the identity at a positive time precisely when

\[
\tau=\pi M,\qquad M\in\mathbb Z_{>0},\qquad
M(3+2ν)\in2\mathbb Z.                          \tag{14}
\]

Such a time exists iff (2ν\in\mathbb Q). If (3+2ν=a/b) is reduced, then

\[
M_{\min}=\begin{cases}
b,&a\text{ even},\\
2b,&a\text{ odd},
\end{cases}
\qquad
t_{\min}=\frac{2\pi R^2}{\hbar}M_{\min}.       \tag{15}
\]

### Proof of necessity, sufficiency, and global phase

If all phases in (13) agree, every consecutive phase ratio is one. The
consecutive exponent difference is (2k+1+2ν). Subtracting its condition at
(k) from that at (k+1) gives (2\tau\in2\pi\mathbb Z), so
$\tau=\pi M$. The first gap, between $k=1$ and $k=2$, gives precisely
(M(3+2ν)\in2\mathbb Z). This proves necessity.

Conversely, under (14), every consecutive-gap exponent is

\[
M(2k+1+2ν)=M(3+2ν)+2M(k-1),
\]

an even integer, so all phases agree. Their common (k=1) exponent is

\[
M(1+2ν)=M(3+2ν)-2M,
\]

also even. Thus the common phase is exactly one, not merely an unspecified
scalar. Existence is equivalent to (2ν\in\mathbb Q). For reduced (a/b),
(b\mid M); the least multiple making (Ma/b) even is (b) for even (a)
and (2b) for odd (a), proving (15).

## 5. Exact receipt and Route-A boundary

The evidence exhausts 2,048 regular classical cells, all 8,385 quantum labels
through (N=128), 256 rational revival controls, 256 irrational controls, and
six boundary rows. An independent checker rebuilds every row. SymPy verifies
the action algebra, 81 symbolic Jacobi equations, 27 direct radial
Schrödinger substitutions, both limits, and the gap identities. These finite
checks are regression evidence only.

This system differs from C349 Neumann dynamics, C244 spherical-pendulum
monodromy, C313 free-sphere dynamics, and C221 nonlinear Schrödinger PDEs.
Rational revival is source commensurability, not arithmetic local data. No
target Euler factor, root number, automorphy, target divisor, functional
equation, target-zero match, or Hilbert--Pólya operator is claimed. Route B is
locked.

```text
(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)
overall: ROUTE_A_REJECTED
scope: NO_BAD_EULER_OR_ROOT_NUMBER
```

Primary lineage is Higgs DOI `10.1088/0305-4470/12/3/006`, Leemon DOI
`10.1088/0305-4470/12/4/009`, arXiv `1008.3865`, and arXiv
`quant-ph/9803085`. No literature-priority claim is made.
