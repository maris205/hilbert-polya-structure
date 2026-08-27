# C189 theorem package: common first-harmonic forcing as one Möbius flow

## Frozen setting

Let `I` be an interval, let `f:I->R` and `H:I->C` be continuous, and let
`N>=3`.  Consider

\[
 \dot\theta_j=f(t)+\operatorname{Im}(H(t)e^{-i\theta_j}),
 \qquad z_j=e^{i\theta_j}\in S^1,\qquad 1\le j\le N.
\]

For four distinct points use the convention

\[
 [a,b;c,d]=\frac{(a-c)(b-d)}{(a-d)(b-c)}.
\]

## Main theorem

### 1. One `PSU(1,1)` flow for arbitrary common forcing

Every phase satisfies

\[
 \dot z=ifz+\frac12(H-\overline H z^2).                 \tag{1}
\]

Define

\[
 A(t)=\frac12\begin{pmatrix}if(t)&H(t)\\
                    \overline{H(t)}&-if(t)\end{pmatrix},
 \qquad J=\operatorname{diag}(1,-1).
\]

Then `tr A=0` and `A^*J+JA=0`.  If `G'=AG`, `G(t0)=I`, then
`G(t) in SU(1,1)` and, writing

\[
 G(t)=\begin{pmatrix}a(t)&b(t)\\
             \overline{b(t)}&\overline{a(t)}\end{pmatrix},
 \qquad |a|^2-|b|^2=1,
\]

all labelled phases obey the same projective map

\[
 z_j(t)=M_{t,t_0}(z_j(t_0)),\qquad
 M_{t,t_0}(z)=\frac{az+b}{\overline b z+\overline a}
 =e^{i\psi}\frac{z+\alpha}{1+\overline\alpha z},       \tag{2}
\]

where `alpha=b/a`, `|alpha|<1`, and `e^{i psi}=a/overline a`.

### 2. Generic cross-ratio foliation

Every Möbius cross ratio of four distinct labelled phases is constant.  On a
connected component of the distinct-point configuration space, fix labels
`1,2,3`.  The `N-3` real quantities

\[
 \chi_j=[z_j,z_1;z_2,z_3],\qquad j=4,\ldots,N,          \tag{3}
\]

are functionally independent and separate the diagonal `PSU(1,1)` orbits.
Thus a generic group orbit has dimension three and the quotient has dimension
`N-3`.

### 3. Collision and synchronization strata

Möbius maps are injective.  Hence

\[
 z_j(t)=z_k(t)\quad\Longleftrightarrow\quad
 z_j(t_0)=z_k(t_0),                                   \tag{4}
\]

and every labelled collision partition is invariant.  If a stratum contains
`m` distinct clusters, its diagonal group orbit has dimension

\[
 \dim\mathcal O=\begin{cases}1,&m=1,\\2,&m=2,\\3,&m\ge3,
 \end{cases}                                          \tag{5}
\]

and its quotient has `max(m-3,0)` local cross-ratio coordinates.  This
includes complete synchrony, two-cluster states, and all repeated-phase
boundaries without using a singular WS gauge.

### 4. Constant-generator trichotomy

Let `f=omega in R` and `H in C` be constant and set

\[
 A=\frac12\begin{pmatrix}i\omega&H\\\overline H&-i\omega\end{pmatrix},
 \qquad \Delta=\omega^2-|H|^2.
\]

Then

\[
 A^2=-\frac{\Delta}{4}I,                              \tag{6}
\]

and the following cases are exhaustive.

- If `(omega,H)=(0,0)`, the projective flow is the identity.
- If `Delta>0`, the flow is elliptic, has no boundary equilibrium, and every
  boundary orbit has minimal projected period
  \[
    T_{\rm ell}=\frac{2\pi}{\sqrt\Delta}.              \tag{7}
  \]
- If `Delta=0` and the generator is nonzero, the flow is parabolic and has
  one boundary equilibrium.
- If `Delta<0`, the flow is hyperbolic and has two boundary equilibria; every
  other boundary orbit is heteroclinic between them.

The equilibria are precisely the unit-modulus roots, counted without
multiplicity, of

\[
 \overline H z^2-2i\omega z-H=0.                      \tag{8}
\]

### 5. Sampled-time and Route-A boundary

In the constant elliptic case, if `tau/T_ell` is rational then some iterate
of the sampled map is the identity on every configuration stratum.  Its fixed
set is therefore positive-dimensional, not a finite set of isolated primitive
orbits.  Parabolic and hyperbolic generators have boundary fixed clusters but
no nonfixed periodic boundary orbit.  Arbitrary time-dependent forcing has no
intrinsic autonomous primitive-period ledger.

Consequently the strict Route tuple is

`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, overall
`ROUTE_A_REJECTED`, Route B false.

## Proof

Multiplying the phase equation by `i z` gives (1).  For a column represented
by `(z,1)^T`, projectivizing `v'=Av` gives

\[
 \dot z=A_{11}z+A_{12}-z(A_{21}z+A_{22}),
\]

which is exactly (1).  Direct matrix multiplication gives `A^*J+JA=0` and
`tr A=0`; differentiating `G^*JG` and `det G` therefore proves
`G(t) in SU(1,1)`.  Projectivization gives the first expression in (2).
The identities `|a|^2-|b|^2=1`, `alpha=b/a`, and
`e^{i psi}=a/overline a` give the second.

Fractional-linear transformations preserve cross ratios, so (3) is constant.
Four concyclic points have real cross ratio.  A boundary Möbius map is uniquely
determined by the images of three distinct boundary points.  After labels
`1,2,3` are normalized, the remaining normalized images are exactly the
cross ratios (3).  They therefore separate orbits and are independent on each
fixed circular-order component.  A projective transformation fixing three
distinct boundary points is the identity, proving the generic orbit dimension.

Equation (4) follows from injectivity.  The subgroup fixing one boundary point
has dimension two and the subgroup fixing two distinct labelled boundary
points has dimension one; fixing three has trivial stabilizer.  Subtracting
these stabilizer dimensions from `dim PSU(1,1)=3` proves (5) and the stated
stratum quotient dimensions.

For constant coefficients, direct multiplication gives (6).  If
`nu=sqrt(Delta)>0`,

\[
 e^{tA}=\cos(\nu t/2)I+\frac{2}{\nu}\sin(\nu t/2)A.
\]

At `t=2*pi/nu` this equals `-I`, which is the identity in `PSU(1,1)`;
no smaller positive projective time is the identity.  This proves (7).
For `Delta=0`, `e^{tA}=I+tA`; for `Delta<0` the same formula uses hyperbolic
functions.  Solving the stationary Riccati equation gives (8), whose boundary
root count is respectively zero, one, or two.  The standard one-parameter
subgroup phase portraits then yield the stated parabolic and hyperbolic
limits.  Finally, an elliptic rational strobe becomes the projective identity,
which proves the clean fixed-set obstruction.

## Degenerate boundaries and nonclaims

- The theorem requires common first-harmonic forcing.  Heterogeneous natural
  frequencies, oscillator-specific forcing, delay, or higher harmonics need
  not share one Riccati equation.
- Cross ratios are only written when their four arguments are distinct;
  collision strata use distinct cluster representatives.
- `SU(1,1)` matrix period and `PSU(1,1)` projective period differ by the
  central sign; (7) is the projected period.
- The zero generator is identity, not parabolic.
- No arithmetic semantics are assigned to phase labels, forcing parameters,
  discriminants, or periods.  No target divisor, Euler product, functional
  equation, Hilbert--Pólya operator, Route B, universal novelty, or external
  peer review is claimed.
