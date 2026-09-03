# Proof Package

## Claim

Let `z=(z1,z2,z3)` lie in `C^3`, equip complex coordinates with

$$
\{f,g\}=-i\sum_{j=1}^3
\left(\partial_{z_j}f\,\partial_{\bar z_j}g-
\partial_{\bar z_j}f\,\partial_{z_j}g\right),
$$

and set

$$
H=z_1z_2\bar z_3+\bar z_1\bar z_2z_3.
$$

Then Hamilton's equations are

$$
i\dot z_1=\bar z_2z_3,
\qquad i\dot z_2=\bar z_1z_3,
\qquad i\dot z_3=z_1z_2. \tag{1}
$$

Every solution is global.  The functions

$$
N_1=|z_1|^2+|z_3|^2,
\qquad N_2=|z_2|^2+|z_3|^2,
\qquad H
$$

are commuting first integrals and are independent on an open dense set.  For `x=|z3|^2`,

$$
\dot x^2=4x(N_1-x)(N_2-x)-H^2. \tag{2}
$$

The following clauses exhaust the dynamics on every joint invariant level.

1. If `0<|H|<Hmax`, the cubic in (2) has roots
   `0<r1<r2<Nminus<=Nplus<r3`, where `Nminus=min(N1,N2)`, and
   every intensity orbit is
   $$
   x(t)=r_1+(r_2-r_1)\operatorname{sn}^2
   \left(\sqrt{r_3-r_1}(t-t_0)\mid m\right),
   \qquad m=\frac{r_2-r_1}{r_3-r_1}. \tag{3}
   $$
   Its least intensity period is
   $$T_x=\frac{2K(m)}{\sqrt{r_3-r_1}}.$$
2. In the same regular chamber, the phase increments over `Tx` are
   $$
   \Delta_j=-\frac{H}{\sqrt{r_3-r_1}(N_j-r_1)}
   \Pi\left(\frac{r_2-r_1}{N_j-r_1}\mid m\right),
   \qquad j=1,2. \tag{4}
   $$
   The full complex orbit is periodic exactly when both
   `Delta1/(2*pi)` and `Delta2/(2*pi)` are rational.
3. If `H=0` and `0<Nminus<Nplus`, every non-equilibrium orbit is, up to the two phase symmetries and exchange of modes 1 and 2,
   $$
   \begin{aligned}
   z_1&=\sqrt{N_-}\,\operatorname{cn}(u\mid m)e^{i\alpha},\\
   z_2&=\sqrt{N_+}\,\operatorname{dn}(u\mid m)e^{i\beta},\\
   z_3&=-i\sqrt{N_-}\,\operatorname{sn}(u\mid m)e^{i(\alpha+\beta)},
   \end{aligned} \tag{5}
   $$
   where `u=sqrt(Nplus)(t-t0)` and `m=Nminus/Nplus`.  The intensity period is `2K(m)/sqrt(Nplus)` and the least full-state period is twice that value.
4. If `H=0` and `N1=N2=N>0`, (5) limits to the heteroclinic
   $$
   \sqrt N\bigl(\operatorname{sech}u\,e^{i\alpha},
   \operatorname{sech}u\,e^{i\beta},
   -i\tanh u\,e^{i(\alpha+\beta)}\bigr),
   \qquad u=\sqrt N(t-t_0), \tag{6}
   $$
   between opposite points of the `z3`-axis equilibrium family.
5. The maximal value of `|H|` on fixed positive `N1,N2` is attained at
   $$
   x_*=\frac{N_1+N_2-sqrt{N_1^2-N_1N_2+N_2^2}}{3},
   \qquad H_{\max}=2\sqrt{x_*(N_1-x_*)(N_2-x_*)}. \tag{7}
   $$
   Equality gives a constant-intensity relative equilibrium with
   $$
   \omega_1=-\frac{H}{2(N_1-x_*)},\quad
   \omega_2=-\frac{H}{2(N_2-x_*)},\quad
   \omega_3=-\frac{H}{2x_*}=\omega_1+\omega_2. \tag{8}
   $$
   Its full state is periodic exactly when `omega1/omega2` is rational.
6. The origin and three complex coordinate axes are equilibrium families.  Vanishing coupling gives the identity flow; every nonzero real coupling is obtained from (1) by time rescaling, with a negative coupling reversing time.

## Status

PROVABLE AS STATED.

## Assumptions

- The bracket, Hamiltonian, and coefficient-one time normalization above are frozen.
- `K(m)` and `Pi(n|m)` are complete elliptic integrals in the Jacobi parameter convention, not the modulus convention.
- Clauses (3)--(4) concern nonconstant regular levels with `H` nonzero.  Zero-Hamiltonian chart crossings and double roots are handled separately.
- “Periodic full state” means equality of all three complex amplitudes after a positive source time, not merely return of their moduli.

## Notation

Write `Ij=|zj|^2`, `w=z1*z2*conjugate(z3)`, and `Psi=phi1+phi2-phi3` wherever all amplitudes are nonzero.  Thus `H=w+conjugate(w)=2*sqrt(I1 I2 I3)*cos(Psi)`, `I1=N1-x`, `I2=N2-x`, and `I3=x`.

## Proof Strategy

First derive the invariant reduction directly from the complex Hamiltonian.  Analyze the scalar cubic globally before introducing elliptic functions.  Reconstruct the two cyclic phases on the nonzero-amplitude chamber.  Finally solve separately the two singular faces that the phase chart cannot cover: `H=0` and the maximal-H double root.

## Dependency Map

1. Global existence depends on the Manley--Rowe invariants and local polynomial ODE theory.
2. Liouville integrability depends on the bracket calculation and generic rank.
3. The Jacobi formula depends on the three-root chamber and the differential identity for `sn`.
4. Full-state closure depends on both phase increments, not on the scalar cubic alone.
5. The zero-Hamiltonian and relative-equilibrium claims are direct substitutions and do not use a singular limiting phase integral.

## Proof

### Step 1: equations, conservation, and global existence

The bracket gives `dot(zj)={zj,H}=-i partial_(conjugate(zj)) H`, which is exactly (1).  Direct differentiation gives

$$
\dot I_1=\dot I_2=-2\operatorname{Im}w,
\qquad \dot I_3=2\operatorname{Im}w.
$$

Hence `N1` and `N2` are conserved; `H` is conserved because the flow is Hamiltonian.  The same bracket calculation gives

$$
\{N_1,N_2\}=\{N_1,H\}=\{N_2,H\}=0.
$$

On a common level, `0<=I3<=min(N1,N2)`, `I1=N1-I3`, and `I2=N2-I3`.  Thus every component remains bounded.  The polynomial vector field is locally Lipschitz, and a bounded maximal solution cannot escape in finite time, so the solution extends to all real times.

On the open set with all `Ij>0` and `sin(Psi)` nonzero, `N1,N2` have independent action differentials, while `partial H/partial Psi=-2*sqrt(I1 I2 I3)*sin(Psi)` is nonzero.  Therefore `(N1,N2,H)` has rank three there.  This proves generic independence and Liouville integrability of the three-degree-of-freedom system.

### Step 2: scalar cubic and its complete root chamber

Since `dot(x)=2 Im(w)` and `|w|^2=I1 I2 I3=x(N1-x)(N2-x)`, one has

$$
\dot x^2=4|w|^2-(w+\bar w)^2,
$$

which is (2).  Let `f(x)=x(N1-x)(N2-x)` on `[0,Nminus]`.  For positive `N1,N2`, `f` is positive in the interior, zero at both ends, and has one interior maximum.  Solving `f'(x)=0` gives (7).  Therefore admissibility is precisely `|H|<=Hmax`.

If `0<|H|<Hmax`, the polynomial `P(x)=4f(x)-H^2` is negative at `0`, positive near its unique interior maximum, and negative at `Nminus`.  It therefore has exactly two roots `r1,r2` in `(0,Nminus)`.  Between `Nminus` and `Nplus` the product `f` is nonpositive.  Above `Nplus`, `P` grows from a negative value to positive infinity, yielding one more root `r3>Nplus`.  A cubic has no further roots, and

$$
P(x)=4(x-r_1)(x-r_2)(x-r_3)
=4(x-r_1)(r_2-x)(r_3-x)
$$

on the accessible interval.  Comparison of coefficients yields

$$
r_1+r_2+r_3=N_1+N_2,\quad
r_1r_2+r_1r_3+r_2r_3=N_1N_2,\quad
r_1r_2r_3=H^2/4. \tag{9}
$$

### Step 3: Jacobi integration

Set `d=r2-r1`, `g=r3-r1`, `m=d/g`, and `x=r1+d sn^2(u|m)`.  The identity

$$
\left(\frac{d}{du}\operatorname{sn}u\right)^2
=(1-\operatorname{sn}^2u)(1-m\operatorname{sn}^2u)
$$

shows that (2) holds when `u=sqrt(g)(t-t0)`.  Since `sn^2` has least real period `2K(m)` for `0<m<1`, (3) and the asserted intensity period follow.  A time translation accounts for either initial sign of `dot(x)`.

### Step 4: two phase increments and full-state return

For nonzero `H`, no amplitude can vanish because `H^2<=4I1I2I3`.  The amplitude-phase chart is therefore global on the orbit.  Division of (1) by `zj` gives

$$
\dot\phi_1=-\frac{H}{2I_1},\qquad
\dot\phi_2=-\frac{H}{2I_2},\qquad
\dot\phi_3=-\frac{H}{2I_3}. \tag{10}
$$

Integrating the first two equations over one intensity period and using

$$
\int_0^{2K(m)}\frac{du}{1-n\operatorname{sn}^2(u\mid m)}=2\Pi(n\mid m)
$$

gives (4).  At the end of one intensity period, both `x` and `dot(x)` return.  The two values determine `exp(i Psi)` through the real and imaginary parts of `w`; hence `Psi` returns modulo `2*pi`, and the third phase increment is congruent to `Delta1+Delta2` modulo `2*pi`.

Any return of the full nonconstant state must occur after an integer multiple of the least intensity period.  Such a multiple returns all three phases exactly when the same integer clears the denominators of both `Delta1/(2*pi)` and `Delta2/(2*pi)`.  This proves necessity and sufficiency of the two rationality conditions.

### Step 5: the zero-Hamiltonian chart crossings

Assume first `0<N1<N2`; the other ordering follows by exchanging modes 1 and 2.  Put `A=sqrt(N1)`, `B=sqrt(N2)`, `m=A^2/B^2`, and `u=B(t-t0)`.  Substitution of

$$
\operatorname{sn}'=\operatorname{cn}\operatorname{dn},\quad
\operatorname{cn}'=-\operatorname{sn}\operatorname{dn},\quad
\operatorname{dn}'=-m\operatorname{sn}\operatorname{cn}
$$

into (5) proves all three equations (1).  The identities `sn^2+cn^2=1` and `dn^2+m sn^2=1` give `N1,N2`, and the cubic monomial is purely imaginary, so `H=0`.  The two torus phases and a time shift supply every non-equilibrium point of this joint level.

The squared amplitudes use `sn^2`, `cn^2`, and `dn^2`, hence have period `2K/B`.  Translation by `2K` changes the signs of `sn` and `cn` but not `dn`; therefore the complex state has not returned.  Translation by `4K` returns all three functions.  This proves the factor-two claim.  The zeros are harmless because (5), unlike (10), is smooth there.

If `N1=N2=N`, then `m` tends to one and `sn(u|1)=tanh u`, `cn(u|1)=dn(u|1)=sech u`.  Formula (6) follows and approaches opposite `z3`-axis equilibria as `t` tends to the two infinities.  Thus its period is infinite.

### Step 6: the double root and equilibrium boundaries

At `|H|=Hmax`, the accessible roots coalesce at `xstar`.  Equation (2) is nonnegative nowhere else in `[0,Nminus]`, so `x` is constant.  Equality in `|H|<=2 sqrt(I1 I2 I3)` forces `Psi` to be `0` or `pi`.  Formula (10) then gives (8).  The critical equation

$$3x_*^2-2(N_1+N_2)x_*+N_1N_2=0$$

is equivalent to

$$\frac1{x_*}=\frac1{N_1-x_*}+\frac1{N_2-x_*},$$

and hence `omega3=omega1+omega2`; the relative phase stays locked.  Because the third frequency is the sum of the first two, the three complex amplitudes return together exactly when `omega1/omega2` is rational.  For `N1=N2`, the first two frequencies agree.  The asymmetric witness `(N1,N2)=(5,8)` has `xstar=2`, `Hmax=12`, and absolute frequencies `(2,1,3)`.

If either Manley--Rowe invariant vanishes, two amplitudes vanish and the remaining point lies on a coordinate-axis equilibrium family.  Direct substitution handles all three axes and the origin.  Finally, inserting a real coupling `g` multiplies the vector field by `g`: `g=0` gives the identity flow, while `tau=g*t` reduces every nonzero case to (1).  This completes every clause.  QED.

## Corrections or Missing Assumptions

None.  The theorem explicitly separates regular nonzero-Hamiltonian orbits from the charts where a phase denominator vanishes.

## Open Risks

- The two phase integrals use the Jacobi parameter convention `m`; changing to a modulus convention without squaring it would change every receipt.
- The formal cubic bosonic analogy has no operator-domain theorem here and remains `A4_FORMAL_HINT`.
- No claim is made that the continuously selected periodic states form a hyperbolic or arithmetic orbit ledger.
