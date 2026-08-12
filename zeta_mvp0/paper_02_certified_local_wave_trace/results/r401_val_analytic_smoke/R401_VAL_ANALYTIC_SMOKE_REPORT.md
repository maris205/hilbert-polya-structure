# R401-VAL Analytic Implementation Smoke

Overall status: **PASS_IMPLEMENTATION_SMOKE**.

This run checks Arb-backed exact constants, zero-safe `exprel` and
`log1prel`, normal-coordinate reconstruction, analytic radial/warped period
bounds, and 60 parameterized shell-identity points at both 128-bit and
256-bit precision.

It is not a validated flow integration, does not close the global cover or
the local Krawczyk tree, and does not certify
`delta_tr > 0.01`.

- protocol hash gate: `True`
- radial proof hash gate: `True`
- warped proof hash gate: `True`
- 128-bit status: `PASS_IMPLEMENTATION_SMOKE`
- 256-bit status: `PASS_IMPLEMENTATION_SMOKE`

The 256-bit outward enclosures include

\[
 \|\nabla^2V_a\|_{\rm op}
 \le 102.444797022348<103,
 \qquad
 T_{\rm warped}\ge0.620775995736>0.60,
\]

and

\[
 T_{\rm radial}\ge0.997570934052>0.99.
\]

The normalized full-shell outer bound is
\(|Q_2|\le0.419934928155<0.421\).  All 60 shell-identity points at each
precision enclose \(K_\epsilon=1\), including \(\epsilon=0\) and
\(\epsilon=0.101\).

The independent checker does not import the production module.  It
reconstructed the exact constants and analytic bounds with 256-bit Arb
arithmetic, verified all three frozen hashes, and passed **15/15** checks.

These are analytic/special-function implementation checks only.  The result
does not contain a validated Taylor/Lohner flow, global exclusion tree,
local phase-cover tree, or Krawczyk continuation and therefore cannot be
reported as `PASS_ENDPOINT` or `PASS_FULL` under R401-VAL.
