# Round 1 Refinement

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

## Anchor check

- The revised method still addresses whether the Hénon warp is active in the
  spectrum of the same fixed Q/W operator.
- The proposed divisor tower and adelic branches were rejected because they
  would change the source of the arithmetic structure.
- No new fitted parameter, boundary, or zero comparison was added.

## Simplicity check

- **Dominant contribution:** strict ground-state spectral activation under an
  equimeasurable Hénon warp.
- **Supporting contribution:** exact first relative heat carrier and its
  logarithmic coefficient.
- **Removed:** large FEM spectrum, RMT fitting, transfer-operator
  Hermitization, and a second arithmetic operator.

## Revised method

For a proper volume-preserving diffeomorphism \(\Psi\), compare

\[
H_{\Psi,h}=-\frac{h^2}{2}\Delta+2\pi e^{\pi|\Psi(q)|^2}
\]

with the radial rearrangement \(H_{0,h}\).  Symmetric rearrangement gives

\[
\lambda_1(H_{\Psi,h})\ge\lambda_1(H_{0,h}).
\]

Equality forces the positive ground state to be radial up to translation and
therefore forces the potential itself to be a translated radial potential.
For the centered Hénon warp, the degree-four homogeneous term is \(a^2x^4\),
so equality is impossible for \(a\ne0\).  Hence

\[
\lambda_1(H_{a,h})>\lambda_1(H_{0,h}).
\]

The supporting heat calculation retains the exact identity

\[
I_a-I_0=\frac{2a^2}{t^2}
\left[A_2(2\pi t)+4\pi r_a^2A_1(2\pi t)\right],
\]

while the full small-time heat asymptotic remains conditional on a uniform
remainder lemma.

## Refined verdict

`READY FOR PROOF PHASE`: the dominant theorem is complete and independently
reviewed.  The supporting asymptotic is intentionally labelled conditional.

