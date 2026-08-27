# C202 theorem package: the all-speed Fisher--KPP wave atlas

## 1. Frozen model and normalization

Fix `D,r>0`, put `z=x-c t`, and write `u(x,t)=U(z)`.  Then

\[
D U''+cU'+rU(1-U)=0.
\]

With

\[
\xi=\sqrt{r/D}\,z,\qquad s=c/\sqrt{Dr},
\]

the profile system is

\[
U'=V,\qquad V'=-sV-U(1-U).                     \tag{1}
\]

Primes now denote `xi` derivatives.

## 2. Complete front classification

For every `s>=2`, system (1) has exactly one orbit, modulo translation in
`xi`, satisfying

\[
0<U<1,\quad V<0,\quad (U,V)(-\infty)=(1,0),
\quad (U,V)(+\infty)=(0,0).                    \tag{2}
\]

Equivalently, positive decreasing physical fronts exist exactly for
`c>=2 sqrt(D r)`.  If `c<=-2 sqrt(D r)`, spatial reflection of the unique
`|c|` profile gives the unique increasing front from `0` to `1`.

For `0<|c|<2 sqrt(D r)`, no `[0,1]` front exists: the eigenvalues at the zero
state are a nonreal conjugate pair, so every nontrivial tail approaching zero
has an oscillating leading term and changes sign.  At `c=0`, the conserved
Hamiltonian has periodic ovals around `(0,0)`, but its endpoint values

\[
H(1,0)=r/6,\qquad H(0,0)=0
\]

exclude a `1`-to-`0` heteroclinic.

## 3. Trapping proof and translation uniqueness

Let `s>=2` and

\[
q=\frac{s-\sqrt{s^2-4}}2,qquad q^2-sq+1=0.
\]

The triangle

\[
\mathcal T_q=\{0\le U\le1,\ -qU\le V\le0\}
\]

is forward invariant.  On `V=0`, one has `V'=-U(1-U)<0`; on the vertical
edge `U=1`, one has `U'=V<=0`; and on `G=V+qU=0`, direct substitution gives

\[
G'=U^2>0.
\]

The decreasing branch of the one-dimensional unstable manifold of the saddle
`(1,0)` enters the triangle.  The divergence is the negative constant `-s`,
so there is no periodic omega limit.  Energy is nonincreasing and cannot stay
constant along a nonstationary orbit; in particular the branch cannot return
to `(1,0)`.  The planar omega-limit alternative therefore leaves only
`(0,0)`.  This proves existence.  Any front with the limits (2) must be the
same unstable-manifold branch; changing its origin in `xi` is the sole
freedom.

## 4. Energy, cycles and all tail regimes

In physical variables,

\[
E=\frac D2(U')^2+r\left(\frac{U^2}{2}-\frac{U^3}{3}\right),
\qquad E'=-c(U')^2.                             \tag{3}
\]

Thus no nonconstant periodic profile exists for `c!=0`; this agrees with the
Bendixson divergence test.  For `c>0`, the back of every front satisfies

\[
1-U(z)\sim C e^{\alpha z},\qquad C>0,
\alpha=\frac{\sqrt{c^2+4Dr}-c}{2D}>0
\quad(z\to-\infty).
\]

At the leading edge `z->+infinity`:

- if `c>2 sqrt(Dr)`,
  \[
  U(z)\sim B e^{\lambda_+z},\qquad B>0,
  \lambda_+=\frac{-c+\sqrt{c^2-4Dr}}{2D};
  \]
- if `c=2 sqrt(Dr)`,
  \[
  U(z)\sim(Az+B)e^{-\sqrt{r/D}\,z},\qquad A>0;
  \]
- if `0<c<2 sqrt(Dr)`, every nonzero zero-state tail is
  \[
  e^{-cz/(2D)}\{A\cos(\omega z)+B\sin(\omega z)+o(1)\},
  \quad \omega=\frac{\sqrt{4Dr-c^2}}{2D},
  \]
  where $(A,B)\ne(0,0)$, hence cannot remain nonnegative.

Negative-speed statements follow by `z->-z`.

## 5. Exact Ablowitz--Zeppetella control

At

\[
c=5\sqrt{Dr/6},\qquad k=\sqrt{r/(6D)},
\]

the source-owned profile

\[
U(z)=\left(1+e^{k(z-z_0)}\right)^{-2}
\]

is an exact member of the supercritical family.  Direct differentiation
annuls the ODE and provides a strong sign/factor regression control; it is not
used to infer existence at other speeds.

## 6. Route-A verdict

The exact tuple is

`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`.

The continuous coefficients have no intrinsic rational-prime origin; the
fronts are heteroclinic translation classes rather than primitive periodic
orbits; there is no source zeta or target divisor; and the dissipative profile
flow supplies no relevant same-clock unitary lift.  Overall:
`ROUTE_A_REJECTED`; Route B is false.
