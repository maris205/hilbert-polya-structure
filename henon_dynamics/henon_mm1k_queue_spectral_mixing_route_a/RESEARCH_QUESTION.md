# Research question — HCS-C225

Can a finite-capacity M/M/1/K queue be upgraded from a textbook stationary
calculation to a convention-complete, independently auditable spectral and
mixing theorem, including every singular face and the controlled transition to
an infinite-capacity chain?

## Frozen answer

Yes, for the source-local object only.  Detailed balance with
`pi_n ∝ rho^n` conjugates the generator to a symmetric Jacobi matrix.  The
reflecting endpoint equations quantize the nonzero angles to
`theta_j=j*pi/(K+1)`, yielding all `K+1` modes.  Reassembling the modes gives
the exact finite transient kernel and the standard reversible spectral TV
bound.  Taking capacity limits then gives geometric stationarity and a positive
gap for `rho<1`, a `K^-2` gap collapse and null recurrence at `rho=1`, and
coordinatewise loss of finite stationary mass for `rho>1`.

The answer is not an arithmetic bridge.  State labels and rates are intrinsic
queue variables, with no primitive-periodic owner or target analytic object;
therefore the strict Route-A verdict is rejected and Route B remains false.

## Falsification checks

The package would be rejected if any endpoint convention changed, if a mode
failed the independent tridiagonal residual, if the reconstructed kernel lost
stochasticity/reversibility, if the TV bound failed, or if a repaired-hash or
nested-unknown mutation passed.  These tests are all executed in the release
manifest gate.
