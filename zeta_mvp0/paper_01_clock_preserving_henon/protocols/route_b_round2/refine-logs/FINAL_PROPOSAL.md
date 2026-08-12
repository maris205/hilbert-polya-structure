# Research Proposal: Same Riemann--von Mangoldt Clock, Different Quantum Spectrum

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

## Method thesis

An area-preserving Hénon warp leaves the complete classical
Riemann--von Mangoldt clock unchanged but cannot remain spectrally inert: the
radial equimeasurable operator uniquely minimizes the ground-state energy, and
the Hénon member has an explicit nonzero first relative heat carrier.

## Dominant contribution

For every \(a>-1\), \(a\ne0\), and fixed \(h>0\), prove

\[
\boxed{\lambda_1(H_{a,h})>\lambda_1(H_{0,h}).}
\]

The proof combines:

1. exact equimeasurability from \(\det D\Psi_a=1\);
2. Pólya--Szegő and increasing/decreasing Hardy--Littlewood inequalities;
3. the Brothers--Ziemer equality classification;
4. the degree-four obstruction \((|\Psi_a|^2)_4=a^2x^4\), which excludes
   radiality about any translated center.

This is a fixed-operator theorem and contains no prime or zero data.

## Supporting contribution

For

\[
I_a(t)=\int e^{-tV_a}|\nabla V_a|^2dq,
\]

derive exactly

\[
I_a-I_0
=\frac{2a^2}{t^2}
\left[A_2(2\pi t)+4\pi r_a^2A_1(2\pi t)\right]>0.
\]

The R300-P1 Brownian-bridge theorem upgrades the carrier to

\[
-\frac{a^2}{24\pi}
\left[L^2+\bigl(2(1-\gamma)+4\pi r_a^2\bigr)L+\kappa_a\right]
+O_{a,h}(tL^4).
\]

R300 independently confirms the identity to \(5.03\times10^{-15}\) in
double precision and \(1.17\times10^{-61}\) internally at arbitrary
precision.  R300-P1 proves the formerly missing uniform noncompact remainder
by expanding the exact Brownian functional in its amplitude and controlling
the integrated fourth derivative on a moving main/tail decomposition.

## Complexity budget

- **Reused:** Paper 7 self-adjoint domain, compact resolvent, and two-term W
  theorem.
- **New:** one rearrangement theorem and one explicit heat invariant.
- **Rejected:** new trainable/fitted components, a second operator, arithmetic
  direct sums, zero comparisons, and large spectral sweeps.

## Claim map

| Claim | Status | Boundary |
|---|---|---|
| Q/W remain valid under the same warp | proved previously | not re-claimed as new |
| Hénon warp is spectrally non-inert | proved and independently reviewed | does not prove positive-measure chaos |
| first relative heat carrier and coefficient | exact and replicated | independent of fixed \(h\) at leading order |
| uniform \(-a^2L^2/(24\pi)\) heat asymptotic | proved; independently audited | fixed \(a,h\), one Hénon warp; remainder \(O(tL^4)\) |
| rational-prime trace P | open | no \(r\log p\) times or von Mangoldt amplitudes |
| explicit-formula Z/RH | not tested | forbidden before P |

## Minimal validation

1. **Completed proof audit:** the strict ground-state and Brownian-remainder
   proofs both passed independent review; add final publication citations.
2. **Completed uniform remainder:**
   \(R_{a,h}(t)=O_{a,h}(tL^4)\).
3. **Optional illustration:** compare radial/Hénon heat
   traces or ground states in a common finite-volume discretization; no fitted
   arithmetic interpretation.

## Failure modes

- If a later referee finds an unrepairable issue in the uniform bridge
  domination, fall back to the strict ground-state theorem and exact carrier.
- If a cited equality theorem requires an unmet critical-set condition,
  weaken to the non-strict rearrangement inequality until repaired.
- If a future orbit module is introduced, label it \(P^*\) unless rational
  prime powers are derived structurally.

## Positioning

The contribution is not a Hilbert--Pólya solution.  It is an analytic
separation result: a broad family can share the two Riemann--von Mangoldt mean
terms while having provably different quantum spectra.  This both strengthens
the Hénon candidate and demonstrates why W alone cannot select an arithmetic
operator.
