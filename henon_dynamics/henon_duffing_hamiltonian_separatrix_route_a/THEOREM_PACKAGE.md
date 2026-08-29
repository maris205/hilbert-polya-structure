# C232 theorem package

Let `V(x)=delta*x^2/2+beta*x^4/4`, `beta>0`, and `H=v^2/2+V(x)`.

1. **Topology.** For `delta>=0`, every `E>0` is one compact center oval. For
   `delta<0`, with `Vmin=-delta^2/(4 beta)`, the levels `Vmin<E<0`, `E=0`,
   and `E>0` are respectively two well ovals, two homoclinic loops, and one
   outer oval.
2. **Turning roots.** With `y=x^2`,
   `y_+-=(-delta+sqrt(delta^2+4 beta E))/beta` and
   `y_-=(-delta-sqrt(delta^2+4 beta E))/beta`; the sign pattern selects each
   interval in the ledger.
3. **Action and period.** On a component `[ell,r]`,
   `T=sqrt(2) int_ell^r (E-V)^(-1/2) dx` and
   `I=pi^(-1) int_ell^r sqrt(2(E-V)) dx`, with `I'=T/(2 pi)`.
4. **Separatrix.** For `delta=-alpha^2`,
   `x_h=+-sqrt(2)*alpha/sqrt(beta)*sech(alpha*t)` solves the homoclinic
   equation exactly.
5. **Limits.** The center, pure-quartic scaling, and logarithmic saddle limits
   are stated and checked without claiming an unproved global period
   monotonicity theorem.
6. **Scope.** `beta=0` harmonic/inverted/free faces are separate models; no
   target divisor, arithmetic labels, or Hilbert--Polya operator is defined.

The executable ledger is a regression oracle. All-family statements are the
displayed elementary proofs, not extrapolations from the twenty numerical
rows.
