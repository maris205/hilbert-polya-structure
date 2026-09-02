# Proof Package — HCS-C300

## Claim

Fix a sound speed `a>0`.  For every pair of Riemann states
`(rho_L,u_L),(rho_R,u_R)` with `rho_L,rho_R>0`, the one-dimensional
isothermal Euler system

`rho_t+(rho u)_x=0`,

`(rho u)_t+(rho u^2+a^2 rho)_x=0`

has one self-similar Lax entropy solution made from a 1-wave, one positive
intermediate state, and a 2-wave.  One strictly increasing scalar equation
determines the intermediate density.  It simultaneously gives all four
shock/rarefaction patterns, their exact profiles and speeds, vanishing-wave
boundaries, and the fact that finite positive-density data never create an
isothermal vacuum.  The pressureless limit is singular and is not included
in the theorem.

## Status

**PROVABLE AS STATED.**  Frozen obstruction record: `HEN-O284`.

## Assumptions and notation

- `a>0`, `rho_L>0`, `rho_R>0`, and `u_L,u_R` are finite real numbers.
- `m=rho u`; the conserved state and flux are
  `U=(rho,m)` and `F(U)=(m,m^2/rho+a^2 rho)`.
- A discontinuity at speed `s` is oriented from its left trace to its right
  trace.  Rarefactions are centered self-similar fans with `xi=x/t`.
- Equality at a branch point means a wave of zero strength, not both a shock
  and a rarefaction.

For a reference density `rho_0>0`, define

`f(rho;rho_0)=a log(rho/rho_0)` for `0<rho<=rho_0`,

`f(rho;rho_0)=a(rho-rho_0)/sqrt(rho rho_0)` for `rho>=rho_0`.

The formulas agree with the same first derivative at `rho=rho_0`.

## Main theorem

There is a unique `rho_*>0` satisfying

`f(rho_*;rho_L)+f(rho_*;rho_R)+u_R-u_L=0`.                 (1)

Set

`u_*=u_L-f(rho_*;rho_L)=u_R+f(rho_*;rho_R)`.              (2)

The 1-wave connects `(rho_L,u_L)` to `(rho_*,u_*)` and is a
rarefaction, zero wave, or Lax shock according as `rho_*<rho_L`,
`rho_*=rho_L`, or `rho_*>rho_L`.  The 2-wave connects the intermediate state
to `(rho_R,u_R)` and has the analogous classification relative to `rho_R`.
Thus the signs of `rho_*-rho_L` and `rho_*-rho_R` give all four nondegenerate
wave patterns.

If the 1-wave is a rarefaction, its fan occupies

`u_L-a <= xi <= u_*-a`,

and inside it

`u(xi)=xi+a`, `rho(xi)=rho_L exp((u_L-u(xi))/a)`.           (3)

If it is a shock and `r_L=rho_*/rho_L>1`, its speed is

`s_1=u_L-a sqrt(r_L)=u_*-a/sqrt(r_L)`.                    (4)

If the 2-wave is a rarefaction, its fan occupies

`u_*+a <= xi <= u_R+a`,

and inside it

`u(xi)=xi-a`, `rho(xi)=rho_R exp((u(xi)-u_R)/a)`.          (5)

If it is a shock and `r_R=rho_*/rho_R>1`, its speed is

`s_2=u_R+a sqrt(r_R)=u_*+a/sqrt(r_R)`.                    (6)

The constant intermediate state fills the interval between the two waves.

## Proof

### 1. Strict hyperbolicity and integral curves

On `rho>0`, the flux Jacobian has eigenvalues

`lambda_1=u-a`, `lambda_2=u+a`.

They are distinct for `a>0`, and both fields are genuinely nonlinear.  Along
a 1-integral curve, `du=-a d rho/rho`; along a 2-integral curve,
`du=+a d rho/rho`.  Integrating from a reference state gives the logarithmic
branches of `f`.  In particular, a 1-rarefaction toward smaller density has
`u=u_0-a log(rho/rho_0)`, while a 2-rarefaction read backward from the right
state has `u=u_0+a log(rho/rho_0)`.

For a shock joining states `(rho_0,u_0)` and `(rho,u)`, eliminate the shock
speed from the two Rankine--Hugoniot relations.  The result is

`(u-u_0)^2=a^2(rho-rho_0)^2/(rho rho_0)`.                 (7)

The Lax sign is negative for the 1-family and positive for the 2-family.
This gives the second branch of `f`, and equations (1)--(2) are exactly the
intersection of the forward 1-wave curve from the left state and the
backward 2-wave curve from the right state.

### 2. Existence and uniqueness of the intermediate state

For fixed `rho_0`, the function `f(.;rho_0)` is continuous and `C^1`: the
two derivatives are `a/rho` and
`a(rho+rho_0)/(2 rho sqrt(rho rho_0))`, both positive and both equal to
`a/rho_0` at the branch point.  Its rarefaction branch tends to `-infinity`
as `rho` decreases to zero, and its shock branch tends to `+infinity` as
`rho` tends to infinity.  Therefore

`Phi(rho)=f(rho;rho_L)+f(rho;rho_R)+u_R-u_L`

is continuous, strictly increasing, and has limits `-infinity,+infinity` at
the two ends of its domain.  It has exactly one positive zero.  Formula (2)
then gives one and only one intermediate velocity.

This argument also proves the no-vacuum assertion: for every finite velocity
jump the root lies strictly inside `(0,infinity)`.  A sequence of data can
drive it toward zero, but no member of the declared finite-data chamber has
`rho_*=0`.

### 3. Fans, shocks, and Lax inequalities

Inside a centered rarefaction, set `xi=lambda_i`.  Preserving the appropriate
Riemann invariant gives (3) and (5); their endpoint values are precisely the
constant traces.  Their characteristic speed increases from left to right,
so the fans are expansive.

For a 1-shock let `r_L>1`.  Substituting the negative sign from (7) in the
mass jump gives (4), and direct subtraction yields

`u_*-a < s_1 < u_L-a`.

For a 2-shock the positive sign gives (6) and

`u_R+a < s_2 < u_*+a`.

These are exactly the strict Lax inequalities in the chosen orientation.
Moreover a 1-wave has speed below `u_*`, while a 2-wave has speed above
`u_*`; hence the two waves are correctly ordered and leave one constant
intermediate sector.  Equality `rho_*=rho_i` collapses the corresponding fan
or shock continuously to zero strength.

### 4. Entropy selection

In conservative variables the mechanical entropy pair is

`eta(rho,m)=m^2/(2rho)+a^2 rho log rho`,

`q(rho,m)=u(eta+a^2 rho)`.                                (8)

The Hessian of `eta` is positive definite for `rho>0`: its lower-right entry
is `1/rho` and its determinant is `a^2/rho^2`.  Smooth solutions conserve
(8).  For either shock, let `r>1` be the compressed-to-outer density ratio
and let `rho_0` denote that outer, lower density.  Substitution of the
Rankine--Hugoniot formulas gives the common oriented production

`[q]-s[eta]=a^3 rho_0 sqrt(r)[log r-(r-r^{-1})/2]<0`.      (9)

Indeed, `h(r)=(r-r^{-1})/2-log r` has `h(1)=0` and
`h'(r)=(r-1)^2/(2r^2)>0` for `r>1`.  Thus the Lax orientations above are
strictly entropy admissible; the opposite algebraic roots are expansive and
violate the Lax condition.  Rarefactions are smooth entropy equalities away
from their two Lipschitz edges.  The assembled self-similar solution is
therefore the Lax entropy solution.

### 5. Complete boundary atlas

- If `rho_*=rho_L` or `rho_*=rho_R`, the corresponding wave has zero
  strength; if both hold, the two states are identical and the solution is
  constant.
- Arbitrarily small positive input densities remain in the theorem, but
  zero-density input traces are excluded because `log rho` and strict
  hyperbolicity at the conservative boundary require a separate theory.
- Multiplying all three densities by one positive constant preserves every
  velocity and wave speed and scales the conservative solution accordingly.
- The limit `a -> 0+` is not uniform.  Eigenvalues coalesce, the monotone
  equation loses coercivity, separating data may create vacuum, and
  compressive data may require concentration/delta shocks in pressureless
  Euler.  Explicitly, for `rho_L=rho_R=1` and `u_R-u_L=1`,
  `rho_*=exp[-1/(2a)] -> 0`; for the reversed jump, `rho_*=y^2` with
  `y-y^{-1}=1/(2a)`, hence `rho_* -> infinity`.  No pressureless solution
  conclusion is inferred from (1)--(9).

## Collision and Route-A boundary

C195 owns a scalar, periodic, viscous Burgers flow.  C300 owns the full
positive-density Riemann solver for a two-component inviscid hyperbolic
system, including two characteristic families and four wave combinations.
The state space, clock, entropy mechanism and theorem are different.

The strict tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` and the overall verdict is
`ROUTE_A_REJECTED`.  A finite self-similar entropy fan is not a recurrent
primitive-orbit system; its continuous density and sound-speed parameters
give no arithmetic local owner or logarithmic-prime clock; the scalar root
equation is not a target determinant; and the dissipative weak solution has
no same-clock self-adjoint lift.  Route B remains locked under
`NO_BAD_EULER_OR_ROOT_NUMBER`.

Finite exact/rational cases in the evidence artifact regress branch signs,
wave speeds and residuals.  They do not replace the monotonicity, Lax or
entropy proof above.

## Open risks deliberately excluded

- Vacuum initial traces and measure-valued pressureless limits.
- Interactions among more than the two elementary waves generated by a
  single Riemann discontinuity.
- Non-isothermal equations of state, contact waves, viscosity and heat
  conduction.
- A uniqueness claim outside the standard self-similar Lax entropy class.
