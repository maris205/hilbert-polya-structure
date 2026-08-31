# Theorem package

## Frozen positive model

Let `D,S_in,mu_max,K,Y>0`, `S(0),X(0)>=0`, and

```text
mu(S)=mu_max S/(K+S),
S'=D(S_in-S)-mu(S)X/Y,
X'=(mu(S)-D)X.
```

Physical culture time is retained.  Put `x=X/Y` and `Q=S+x`.

## Complete threshold theorem

1. The nonnegative quadrant is forward invariant.  Moreover
   `Q'=D(S_in-Q)`, so
   `Q(t)=S_in+(Q(0)-S_in)e^{-Dt}`.  Solutions are global and bounded.
2. Write `Delta=mu(S_in)-D`.  If `Delta<0`, all states converge to washout
   `E0=(S_in,0)`.  If `Delta=0`, the same conclusion holds, but the biomass
   direction is nonhyperbolic.  If `Delta>0`, define
   `S*=DK/(mu_max-D)` and `X*=Y(S_in-S*)`.  Every state with `X(0)>0`
   converges to `E+=(S*,X*)`; the invariant face `X(0)=0` converges to `E0`.
3. At `E0` the eigenvalues are `-D` and `Delta`.  At `E+`, the triangular
   `(Q,x)` linearization has eigenvalues
   `-D` and `-(S_in-S*)mu'(S*)`.  The equality face is the transcritical
   exchange between the washout and positive branches.
4. The leaf `Q=S_in` is invariant.  With
   `A=mu_max-D` and `x*=S_in-S*`,

   ```text
   x'=A x(x*-x)/(K+S_in-x).
   ```

   For `x*!=0`, every non-equilibrium interval satisfies

   ```text
   [(K+S_in)/x*] log x
   -[(K+S*)/x*] log|x*-x| = A t+C.
   ```

   On the critical face `x*=0`,

   ```text
   (K+S_in)/x+log x=A t+C,
   x(t)~1/[mu'(S_in)t].
   ```
5. A periodic trajectory would make the exponentially relaxing coordinate
   `Q` periodic, hence constant and equal to `S_in`.  The residual scalar
   autonomous equation has no nonconstant cycle.  Thus every recurrent state
   is an equilibrium.

## Proof

The vector field points inward on `S=0`, while `X'=0` on `X=0`; positivity
follows by uniqueness.  Adding the equations after dividing biomass by `Y`
gives the exact equation for `Q`, which also bounds both coordinates.

For `X>0`, substitute `S=Q-x` into
`x'=[mu(Q-x)-D]x`.  Because `Q(t)->S_in` exponentially and `mu` is strictly
increasing, scalar upper and lower comparison with the autonomous equations
at `S_in+epsilon` and `S_in-epsilon` forces the stated limit.  In the survival
case the unique positive zero is `x*=S_in-S*`; in the washout and critical
cases zero is the only nonnegative limiting zero.  The invariant biomass-free
face is handled separately.  Direct differentiation gives the two triangular
spectra.  Partial fractions on `Q=S_in` give the logarithmic formula; its
`x*=0` specialization gives the critical identity and asymptotic coefficient.

## Boundary policy

- `X(0)=0`: `X(t)=0` and `S(t)=S_in+(S(0)-S_in)e^{-Dt}`.
- `D=0`, `X(0)>0`: `Q` is conserved, substrate decreases to zero and biomass
  increases to `YQ(0)`.
- `mu_max=0`: biomass decays exponentially and substrate relaxes linearly.
- `S_in=0`: `Q=Q(0)e^{-Dt}`, so both coordinates converge to zero.
- `K=0` and `Y=0` change or destroy the frozen model and are not obtained by
  dividing the positive-parameter formulas.

## Evidence and Route-A boundary

The proof is continuous-parameter mathematics.  Eighteen rational rows only
reconstruct signs, equilibria, spectra and separated coefficients.  There is
no rational-prime carrier, primitive periodic ledger, dynamical zeta, target
divisor or operator.  Hence

```text
(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)
ROUTE_A_REJECTED; Route B false.
```
