# Proof package: periodic delta-comb band-gap atlas

## Claim and status

For every `a>0` and `g in R`, the form

\[
\mathfrak h_{a,g}[u]=\int_{\mathbb R}|u'|^2dx+
g\sum_{n\in\mathbb Z}|u(na)|^2,
\qquad \operatorname{dom}\mathfrak h_{a,g}=H^1(\mathbb R),
\]

is closed and lower semibounded.  Its self-adjoint operator is free off
`a Z`.  Its domain consists of `u in H1(R)` that are cellwise `H2`, have
`u'' in L2(R minus aZ)` globally, and satisfy

\[
u'(na+)-u'(na-)=g u(na).
\]

With `E=k^2>0`, its discriminant is

\[
\Delta(E)=\cos(ka)+\frac{g}{2k}\sin(ka),
\]

continued by `Delta(0)=1+ga/2` and, at `E=-kappa^2`, by replacing trigonometric
functions with their hyperbolic continuations.  The spectrum is exactly
`|Delta|<=1` and is purely absolutely continuous.  The full theorem includes
the complete sign-dependent band atlas, edge multiplicities, open-gap
theorem, controlled gap asymptotic, and IDS/DOS formulas below.

**Status:** PROVABLE AS STATED.

## Assumptions and conventions

- Kinetic coefficient is one.
- The jump sign is `right derivative - left derivative = g u`.
- `Delta` is half, not all, of the monodromy trace.
- `q=ga` and `z=Ea^2` are dimensionless.
- Bands are enumerated from the spectral bottom, including the negative first
  band when `g<0`.
- IDS is per unit physical length.

## Dependency map

1. A periodized trace inequality closes the form and identifies its operator.
2. Free propagation and one delta jump give a determinant-one monodromy.
3. Floquet decomposition gives `Delta(E)=cos(theta)`, spectral type, and
   multiplicity.
4. Two hyperbolic factorizations give the complete negative/zero atlas.
5. Two trigonometric factorizations give a parity-free positive edge equation
   and the exact band ordering.
6. Analytic inversion of the edge equation gives the controlled gap width.
7. Unwrapping the alternating Floquet phase gives IDS and DOS.

## Proof

### 1. Form and matching operator

Partition the line into centered cells `I_n`.  For every `epsilon>0`, the
one-dimensional trace inequality, rescaled to a cell of length `a`, gives

\[
|u(na)|^2\leq\epsilon\|u'\|_{L^2(I_n)}^2+
C_{a,\epsilon}\|u\|_{L^2(I_n)}^2.
\]

Summing over disjoint cells makes the sampling term infinitesimally form
bounded relative to the kinetic form.  The form perturbation theorem proves
closure and lower semiboundedness for either sign of `g`.  Integration by
parts in the representation identity gives the free differential expression,
continuity, and the stated derivative jumps.  Thus the operator owner is not
a formal multiplication by a distribution.

### 2. Transfer matrix and Floquet criterion

For the state vector `(u,u')`, free propagation over one cell and a jump give

\[
M(E)=\begin{pmatrix}1&0\\g&1\end{pmatrix}
\begin{pmatrix}\cos(ka)&\sin(ka)/k\\-k\sin(ka)&\cos(ka)\end{pmatrix}.
\]

Both factors have determinant one, and multiplication gives
`tr(M)/2=Delta(E)`.  The limits at zero and negative energy are immediate from
the power series and `k=i kappa`.

Floquet fibres on one centered cell have quasi-periodic boundary conditions
with angle `theta` and the delta jump at the cell centre.  A fibre eigenvalue
exists exactly when `M` has multiplier `exp(i theta)`.  Unimodularity makes
this equivalent to

\[
\Delta(E)=\cos\theta,
\]

so the full-line spectrum is `|Delta|<=1`.  Compact fibre spectra form
nonconstant real-analytic branches, locally relabelled at crossings.  Their
critical points are isolated, so the pushforward of Lebesgue measure in the
Bloch angle is absolutely continuous; this is also the periodic-singular
Floquet theorem cited in the source audit.  Their direct integral has neither
point nor singular-continuous part.  In a band interior, `theta` and `-theta`
give multiplicity two.

At an edge, fibre multiplicity is `dim ker(M-I)` or `dim ker(M+I)`.  When
`g!=0`, `M` is never `+I` or `-I`: at a positive Bragg point the jump factor
is nontrivial; at every other edge the free matrix has nonzero upper-right
entry.  This also covers negative and zero edges.  Hence all nonzero-coupling
edges are simple.  At `g=0`, positive Bragg monodromy is `(-1)^n I`, yielding
double folded contacts; the free bottom at zero is simple.

### 3. Negative and zero-energy atlas

For attraction put `h=-ga>0` and `y=kappa a`.  Direct half-angle factoring
gives

\[
\Delta_-(y)-1=2\sinh(y/2)
\left(\sinh(y/2)-\frac{h}{2y}\cosh(y/2)\right),
\]

\[
\Delta_-(y)+1=2\cosh(y/2)
\left(\cosh(y/2)-\frac{h}{2y}\sinh(y/2)\right).
\]

Thus the `+1` edge equation is

\[
h=2y_+\tanh(y_+/2),
\]

with one solution for every `h>0`.  The `-1` edge equation is

\[
h=2y_-\coth(y_-/2).
\]

The first right-hand side increases from zero to infinity.  For the second,
multiplying its derivative by `sinh^2(y/2)` yields `sinh(y)-y>0`, and its
left limit is four.  Therefore the second root exists exactly for `h>4`, and
then `y_-<y_+`.

The factor signs now give:

- `g>0`: no nonpositive spectrum.
- `g=0`: the spectrum begins at zero.
- `-4<ga<0`: the first band starts at `-y_+^2/a^2` and crosses zero in its
  interior.
- `ga=-4`: the first band is `[-y_+^2/a^2,0]`, with zero a simple
  antiperiodic upper edge.
- `ga<-4`: the first band is
  `[-y_+^2/a^2,-y_-^2/a^2]`, followed by a gap across zero.

### 4. Positive bands and gaps

Let `x=a sqrt(E)>0` and `q=ga`.  The factorizations

\[
\Delta-1=2\sin(x/2)\left(\frac{q}{2x}\cos(x/2)-\sin(x/2)\right),
\]

\[
\Delta+1=2\cos(x/2)\left(\cos(x/2)+\frac{q}{2x}\sin(x/2)\right)
\]

show that `x=n pi` is always an edge and that its nonfixed same-sign partner
obeys

\[
q=2x_n\tan((x_n-n\pi)/2).
\]

The derivative of the right side is

\[
\frac{x+\sin(x-n\pi)}{\cos^2((x-n\pi)/2)}>0
\]

on every relevant cell.  It ranges from zero to infinity on the right cell
and from minus infinity to zero on a left cell, except that the first left
cell has limiting value `-4` at zero.  The factor signs prove the following
complete list.

- If `q>0`, there is a unique `x_n in (n pi,(n+1) pi)` for every `n>=0`.
  Bands are `[x_n^2/a^2,((n+1)pi/a)^2]`; the adjacent interval on the left of
  each `x_n` is a gap.
- If `q=0`, the spectrum is `[0,infinity)` and every folded Bragg gap is
  closed.
- If `-4<q<0`, the first band ends at `x_1^2/a^2`, where
  `x_1 in (0,pi)`.  If `q=-4`, take `x_1=0`.  If `q<-4`, no positive `x_1`
  exists and the first gap begins at the negative upper edge.
- For every `q<0` and `n>=1`, a unique
  `x_{n+1} in (n pi,(n+1)pi)` exists and the positive band is
  `[(n pi/a)^2,x_{n+1}^2/a^2]`.  Later gaps lie between `x_n` and `n pi`.

Since a partner can equal the fixed edge only when `q=0`, every Bragg gap is
open for nonzero coupling.

### 5. Controlled high-energy width

Write `N=n pi` and `x_n=N+delta_n`.  The edge equation becomes

\[
q=2(N+\delta_n)\tan(\delta_n/2).
\]

Set `u=N^{-1}` and `delta_n=u v`.  After continuous extension to `u=0`, this
is an analytic equation with value `v-q` and `v`-derivative one.  The analytic
implicit-function theorem gives a convergent local expansion and therefore a
bounded Taylor remainder.  Coefficient comparison yields

\[
\delta_n=\frac qN-\frac{q^2+q^3/12}{N^3}+O_q(N^{-5}).
\]

Consequently the gap width in physical energy is

\[
|G_n|=\frac{2|g|}{a}
-\frac{\operatorname{sgn}(q)(q^2+q^3/6)}{(n\pi)^2a^2}
+O_q(n^{-4}a^{-2}).
\]

Analyticity supplies computable `n_0(q)` and `C(q)` bounding the last term by
`C(q)/(n^4 a^2)`.  This is the controlled remainder; finite receipts do not
establish it.

### 6. IDS and DOS

Enumerate bands increasingly as `B_j`, starting at `j=0`.  Their lower and
upper discriminants are `(-1)^j` and `(-1)^(j+1)`.  On `B_j`, set

\[
K(E)=\frac{j\pi+\arccos((-1)^j\Delta(E))}{a}.
\]

Each fibre band contributes one state per period, so

\[
N(E)=\frac{K(E)}\pi
=\frac1a\left(j+\frac1\pi\arccos((-1)^j\Delta(E))\right).
\]

Below `B_0`, the IDS is zero; in the gap after `B_j`, it is `(j+1)/a`.
These values match at every endpoint.  Differentiating inside a band gives

\[
\rho(E)=\frac{|\Delta'(E)|}{\pi a\sqrt{1-\Delta(E)^2}},
\]

where, for `E=k^2>0`,

\[
\Delta'(E)=-\frac{a\sin(ka)}{2k}
+\frac{g(ak\cos(ka)-\sin(ka))}{4k^3},
\quad
\Delta'(0)=-\frac{a^2}{2}-\frac{ga^3}{12}.
\]

Nonzero-coupling edge simplicity makes `Delta'(E_*)` nonzero, hence the
one-sided inverse-square-root DOS law.  At `g=0`, cancellation at folded
contacts gives the continuous free formulas `N(E)=sqrt(E)/pi` and
`rho(E)=1/(2pi sqrt(E))` for `E>0`.

## Evidence boundary and open risks

- The JSON grid samples threshold, scale, band index, transfer, and asymptotic
  behavior.  It is regression evidence, not the proof of form closure, pure
  absolute continuity, monotonicity, or the asymptotic remainder.
- The first attractive gap for `ga<-4` crosses zero.  Its recorded
  `positive_axis_gap_portion` is explicitly not mislabeled as the full gap
  width.
- Kronig--Penney, point-interaction, and periodic-singular-operator results
  have prior owners.  This package makes no literature-priority claim.
- The transfer determinant and Bloch phase have no target arithmetic meaning.
  `A4_NATURAL_QUANTIZATION` cannot be promoted to Route-B readiness.
