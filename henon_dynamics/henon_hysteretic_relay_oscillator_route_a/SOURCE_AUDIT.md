# Source and scope audit

- Candidate: HCS-C252, two-threshold hysteretic relay phase oscillator.
- Baseline: 3ff451e904f8f063e88c40ef87f4697a6586b1a5.
- Evaluator: flow_systems/skills/route-a-evaluator.md v0.2.0, SHA-256
  6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c.
- Arithmetic origin: none; h, gamma, and y0 are source-defined parameters.
- Clock: continuous hybrid time. Normalization: h>0 and return section
  Sigma_-=(theta=-h,sigma=+1).
- Determinant convention: none; no primitive-orbit/Fredholm determinant.
- Forbidden data: target primes/zeros, arithmetic local data, Euler factors,
  root numbers, automorphy, target divisors/function equations, and
  Hilbert--Polya operators. All scope flags are false.

The relay convention is guard priority with instantaneous equality switching;
it deliberately excludes an unspecified sliding continuation. The finite
receipt is exact in h and gamma and uses high-precision exponentials only for
serialization. Citations provide terminology, not priority certification.
