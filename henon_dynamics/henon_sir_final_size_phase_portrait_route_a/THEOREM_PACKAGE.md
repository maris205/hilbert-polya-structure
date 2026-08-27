# Theorem package

## Frozen model

Let `beta,gamma>0` and

```text
Sdot=-beta*S*I,
Idot=beta*S*I-gamma*I,
Rdot=gamma*I,
```

with `S0>0`, `I0,R0>=0`.  Physical time is retained.  Put

```text
kappa=gamma/beta,
x=S/kappa, y=I/kappa, z=R/kappa, tau=gamma*t.
```

Then `x'=-xy`, `y'=y(x-1)`, `z'=y`.

## Main theorem — all-parameter phase portrait

1. The nonnegative population simplex is forward invariant,
   `S+I+R=N` is constant, and the solution is global.
2. On every trajectory with `y0>0`,
   `H(x,y)=x+y-log x` is constant and
   `y(x)=y0+x0-x+log(x/x0)`.
3. If `x0>1`, infection grows until the unique crossing `x=1`, where
   `y_peak=y0+x0-1-log x0`; it then decreases.  If `x0<=1`, its maximum is the
   initial value (the `x0=1` derivative is initially zero and then negative).
4. Every `y0>0` trajectory satisfies `y(tau)->0` and
   `0<x_infinity<min(x0,1)`.  The unique forward limit is
   `x_infinity=-W_0(-x0 exp(-x0-y0))`.  The value from `W_{-1}` is the other,
   upper intersection of the same invariant curve and is not reached forward.
5. The physical-time solution is uniquely specified by the exact quadrature

   ```text
   tau = integral from x(tau) to x0 of
         du/[u*(y0+x0-u+log(u/x0))].
   ```
6. For `y0>0`, implicit differentiation gives
   `partial x_infinity/partial y0=x_infinity/(x_infinity-1)<0`.
7. On a fixed-population simplex, the disease-free equilibria are the line
   `I=0`.  At susceptible coordinate `S_star`, their tangential eigenvalue is
   zero and transverse eigenvalue is `beta*S_star-gamma`; the threshold is
   `S_star=kappa`.
8. There is no nonconstant recurrent or periodic orbit because `R` is strictly
   increasing wherever `I>0`.  Every trajectory converges to the equilibrium
   line.

If `I0=0`, the point is already an equilibrium and remains fixed.  In
particular, for `x0>1` its final value is `x0`, not the lower Lambert branch;
this boundary is never inferred by taking the positive-infection formula
without its hypothesis.

## Proof

The vector field is locally Lipschitz and points inward on the nonnegative
faces; conservation confines it to a compact simplex.  Direct differentiation
gives `H'=(-xy)(1-1/x)+y(x-1)=0`.  Since `x'=-xy<0` when `y>0` and
`y'=y(x-1)`, the peak classification follows immediately.

The removed coordinate is increasing and bounded, so its limit exists and
`integral I dt<infinity`.  Bounded derivatives imply `I(t)->0`.  Moreover
`S(t)=S0 exp(-beta integral I dt)`, hence `S_infinity>0`.  Substitution into the
first integral gives the final-size equation.  The function `x-log x`
decreases on `(0,1)` and increases on `(1,infinity)`; the forward monotonicity
of `x` selects its unique lower root.  Rewriting as
`x exp(-x)=x0 exp(-x0-y0)` identifies `W_0`, while `W_{-1}` owns the upper root.
Dividing `x'` by the phase curve gives the quadrature.  Differentiation and
linearization prove the remaining formulas; strict monotonicity of `R` excludes
recurrence.

## Evidence boundary

The finite ledger contains 24 positive-infection phase curves across
subcritical, threshold and supercritical initial states and four physical
scalings.  It certifies branch conventions but does not prove global existence
or convergence.  No clinical data are present.

## Route-A theorem

Strict monotonicity kills the nonconstant primitive-orbit layer, while the
rates and compartments have no intrinsic rational-prime semantics.  A Lambert
function is not a target dynamical determinant.  Therefore

```text
(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL),
ROUTE_A_REJECTED, Route B false.
```
