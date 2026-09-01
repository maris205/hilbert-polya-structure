# Exact validation plan

1. Evaluate `E_beta(-x)` from its defining series for six beta values and 24
   stable-range scalar cells.
2. Audit 32 Dirichlet modes for every beta at a common `t^beta=1/1024`, giving
   192 positive, strictly mode-decreasing multipliers.
3. Test the composition law at `t=s=1/4`: five memory clocks must fail and the
   classical `beta=1` face must pass.
4. Use the independent identity
   `E_(1/2)(-x)=exp(x^2)erfc(x)` to test the scaled resolvent limit over 96
   large-argument mode cells.
5. Enumerate exact rational smoothing exponents in the declared `theta>=0`
   domain around `theta=1` and Schatten exponents around `p=1/2`, retaining
   both equality boundaries; separately record why `theta<0` is bounded but
   outside the smoothing claim.
6. Require a producer-independent checker, SymPy coefficient/eigenbasis audit,
   byte replay, repaired-hash mutations, deterministic PDFs, and exact manifest
   closure.

No GPU experiment is appropriate.  These are deterministic checks of an
analytic infinite-dimensional theorem.
