# Round 0 Initial Proposal

## Problem Anchor

- **Bottom-line problem:** Find a fixed, zero-input Hénon-based quantum
  construction that satisfies more than a numerical or fitted subset of the
  Hilbert--Pólya requirements; partial analytic progress is acceptable.
- **Must-solve bottleneck:** The current operator passes Q and W, but the
  Hénon warp needs a non-removable spectral theorem before any attempt at the
  prime-power P bridge.
- **Non-goals:** proving RH; predicting individual zeros; deriving rational
  primes from a Ruelle zeta; reselecting \(a=1.02\); retrying R108 under the
  unchanged protocol.
- **Constraints:** fixed \(a=51/50\); same Paper 7 Hilbert space and operator;
  no prime or zero arrays; 32 CPU cores and 60 GB RAM; at most three core
  validation blocks.
- **Success condition:** an analytic invariant distinguishes the Hénon-warped
  operator from its equimeasurable radial control while the two growing
  Riemann--von Mangoldt terms remain unchanged, with the next missing lemma
  stated exactly.

## Initial thesis

Use the first integrated Wigner--Kirkwood gradient term in the relative heat
trace to prove that the clock-preserving Hénon deformation is spectrally
active.  Area preservation cancels the complete classical heat term, while
the one-step centered Hénon metric leaves a positive angular gradient
invariant.

## Initial core claim

With \(L=\log(1/(2\pi t))\), aim to prove

\[
\operatorname{Tr}(e^{-tH_{a,h}})-\operatorname{Tr}(e^{-tH_{0,h}})
=-\frac{a^2}{24\pi}L^2+O(L).
\]

## Initial validation

1. derive the coefficient by two independent quadratures;
2. verify the sign and exact logarithmic moments;
3. prove a uniform noncompact heat-kernel remainder.

## Initial risk

The local Wigner--Kirkwood expansion may not be uniform on the effective
region that expands as \(t\downarrow0\).  If the remainder is not smaller than
\(L^2\), the formal coefficient cannot be promoted to a heat-trace theorem.

