# Exact-validation plan

The theorem is continuous and analytic; computation is designed only to make
coefficient mistakes and release drift hard to hide.

## Exact panels

- Enumerate 500 rational tuples from four positive `a` values, a five-by-five
  grid for the real and imaginary parts of `b`, and five signed values of `q`.
- Classify each tuple as smooth univalent, boundary cusp,
  interior-critical invalid, or circular.
- On every smooth tuple recompute exact rational coefficient velocities,
  both components of `(a^2 b)_dot`, `M0_dot-2q`, and the squared univalence
  ratio.
- Construct 180 noncircular suction families whose algebraic critical value
  `u_c` is rational.  Verify the exact first time, endpoint coefficient,
  critical preimage, cusp point, and `1/B` normal-form ratio.

## Independent lanes

1. The producer writes canonical JSON from exact fractions.
2. The checker reimplements every row and strict schema without importing the
   producer.
3. SymPy derives the Fourier equations, invariants, scalar minimum, area
   integral, factorized injectivity identity, and cusp series.
4. Replay runs the producer twice in isolated temporary directories and
   requires byte identity with checked evidence.
5. Hostile mutation repairs the outer payload hash after each semantic
   alteration and attacks JSON/YAML parsers, order, deletion, truncation,
   evaluator authority, route fields, and forbidden flags.

## Paper and release

Build three substantively distinct conditional manuscripts twice each under
the fixed epoch.  Reject warnings, layout defects, missing or unembedded
fonts, extraction garbage, raster failures, stale reports, extra payloads,
optimized Python, and manifest self-inclusion.
