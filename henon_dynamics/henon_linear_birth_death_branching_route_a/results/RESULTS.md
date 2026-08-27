# Results

## Exact finite-time ledger

The canonical evidence contains thirteen parameter cases spanning
supercritical, subcritical, critical, pure-birth, pure-death, zero-time and
zero-rate regimes. For `z=0..4` and `n=0..12`, it records:

- 65 initial-population rows;
- 845 exact transition probabilities;
- 195 exact survivor-binomial weights;
- 130 exact mean/variance values;
- 26 exact one-ancestor `(p0,beta)` values; and
- 36 exact coefficients across nine M\"obius semigroup compositions.

The resulting ledger has **1,232 exact scalar identities**. The independent
checker made **2,194 assertions** and reconstructed transitions by convolution
without importing the producer.

## Symbolic and adversarial results

The separate SymPy route passed **1,009 checks**: 34 generic symbolic checks,
845 evidence coefficient checks and 130 evidence moment checks. The generic
set covers both Riccati equations, multiplicative/additive semigroup clocks,
critical continuity, pure birth, pure death, the subcritical conditional PGF
limit and exact quasi-stationary conditional-semigroup invariance, critical
scaled Laplace transform, and the supercritical atom/exponential and
binomial/gamma transforms.

Canonical replay reproduced all **76,842 evidence bytes**. The hostile audit
rejected 22 repaired-hash semantic/schema mutations and one stale-hash
mutation, for **23/23 rejections**.

## Asymptotic conditions retained

- Subcritical quasi-stationarity and critical Yaglom scaling state `z>=1`,
  because survival conditioning is undefined for `z=0`.
- Yaglom scaling states `lambda=mu=c>0`; the `c=0` chain is the identity.
- In the supercritical regime, the initial population enters through
  `K~Binomial(z,(lambda-mu)/lambda)` and atom
  `(mu/lambda)^z`; given `K=k>=1`, the component is gamma with shape `k` and
  rate `(lambda-mu)/lambda`.
- Pure birth has `K=z`; pure death and every finite-time degeneracy are
  retained explicitly.

## Content addresses

- Evidence payload SHA-256:
  `2be1666222c3cb7dbc407d571f0bc9c3d695b19b54067b105f15a9c02c5b3cf5`
- Evidence file SHA-256:
  `d94b84c4d64799ea2dc9728fc96b8d8eb0f4976fd7d006af7441dd4b00565818`
- Final PDF SHA-256:
  `b69dddd4ca490c5df40f294705807486c21a47257695348a9dc4b3a7d1815325`

Route-A tuple: `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; overall
`ROUTE_A_REJECTED`; Route B false.
