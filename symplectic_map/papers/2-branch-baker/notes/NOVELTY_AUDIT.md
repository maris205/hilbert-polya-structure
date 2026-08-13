# Novelty Audit at Design Freeze

## Verdict

`NARROW / STRUCTURAL CASE STUDY`

The three-state PCF graph, its rational parent zeta, the boundary-period
correction, generalized baker realization, and generic baker quantization are
not new.  The defensible research contribution is therefore restricted to a
Route-A obstruction certificate: a finite-state, finite-memory,
locally-constant multiplicative cocycle has a finite-rank length group and
cannot intrinsically realize the full rational-prime logarithm family.

Estimated novelty is 4--5/10 for the worked case and at most about 6/10 if the
finite-memory theorem, its sharpness, and its excluded classes are stated and
proved cleanly.

## Direct collisions and resulting scope decisions

| Candidate element | Closest prior art | Frozen treatment |
|---|---|---|
| \(RLR^\infty\) determinant and parent zeta | Alsed\`a, Bobok, Misiurewicz, and Snoha, *The Real Teapot* (2025) | Reproduction baseline; no novelty claim |
| Period discrepancy at a monotonicity boundary | Hofbauer, *Periodic points for piecewise monotonic transformations* (1985) | One-orbit worked example only |
| Weighted boundary corrections | Milnor--Thurston (1988); Rugh--Tan, *Kneading with weights* (2015) | Convention audit, not a new formalism |
| Generalized Markov baker/natural-extension methods | Bose (1989); Bruin--Kalle (2014) | Classical construction platform |
| Baker quantization | Balazs--Voros (1989); Saraceno (1990) | Downstream precedent only; A4 remains closed |

## Remaining proposition worth testing

For a finite directed graph with a finite-memory locally constant
multiplicative unstable cocycle, every periodic-orbit instability length is an
integer combination of finitely many edge/block log-slopes.  Its rational
span therefore has finite rank.  In contrast, the set
\(\{\log p:p\text{ rational prime}\}\) is rationally linearly independent by
unique factorization.  Such a finite-clock carrier cannot contain every
prime logarithm exactly.
Equivalently, it can contain no more distinct exact prime logarithms than the
dimension of that rational span.  A finite-memory cocycle is included by
finite block recoding.

The claim is deliberately narrow.  It does not exclude variable-derivative
smooth maps, non-locally-constant roof functions, countably many states,
higher-dimensional constructions, or systems that explicitly encode
arithmetic data.

## Terminology controls

- `factor-orientation-weighted zeta` is not `Lefschetz zeta`.
- `branch-history carrier` is not the full topological inverse-limit
  continuum.
- `piecewise exact symplectic on branch interiors` is not `global smooth
  symplectomorphism`.
- The parent derivative cocycle is not the baker monodromy.

## Verified primary references

- Alsed\`a, Bobok, Misiurewicz, and Snoha, *The Real Teapot*, ETDS 45 (2025),
  <https://doi.org/10.1017/etds.2025.15>.
- Hofbauer, *Periodic points for piecewise monotonic transformations*, ETDS 5
  (1985), <https://doi.org/10.1017/S014338570000287X>.
- Rugh and Tan, *Kneading with weights*, Journal of Fractal Geometry 2 (2015),
  <https://doi.org/10.4171/JFG/24>.
- Bose, *Generalized baker's transformations*, ETDS 9 (1989),
  <https://doi.org/10.1017/S0143385700004788>.
- Bruin and Kalle, *Natural extensions for piecewise affine maps via Hofbauer
  towers* (2014), <https://arxiv.org/abs/1306.5451>.
- Balazs and Voros, *The quantized baker's transformation* (1989),
  <https://doi.org/10.1016/0003-4916(89)90259-5>.
- Berry and Keating, *The Riemann Zeros and Eigenvalue Asymptotics* (1999),
  <https://doi.org/10.1137/S0036144598347497>.

Search boundary: sources checked through 2026-08-13; this is a targeted
novelty audit, not a systematic review.
