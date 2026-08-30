# C241 exact-atlas and validation plan

## Claim-driven objective

Establish an auditable theorem package for the classical Lüroth map: branch
partition and image, affine inverse-word fixed points, multiplier products,
primitive-necklace counts, countable-period conclusion, finite weighted identity,
and the sharp distinction between absolute product convergence and meromorphic
continuation.

## Frozen configuration

* Baseline `489506cf92bfed721f94f22dd0444a60427f90a5`; evaluator authority SHA
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
* Date `2026-08-30`; `SOURCE_DATE_EPOCH=1788048000`.
* Branch rows \(m=2,\ldots,12\); word receipt alphabet \(2,\ldots,6\), lengths
  1–4; necklace cutoffs \(M=3,\ldots,8\), lengths 1–5; weighted cutoffs
  \(M=2,\ldots,12\), \(s\in\{1,3/2,3/4,1/2\}\), \(z\in\{1/3,1/2\}\).
* Scope firewall `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Independent gates

1. Producer writes a canonical JSON receipt with exact Fraction fields and
   90-digit weighted values.
2. The recursive checker recomputes branch maps, itineraries, fixed points,
   multipliers, necklaces, finite series, convergence labels, and provenance
   locks without importing producer helpers.
3. SymPy verifies affine inverses, every word's fixed equation and multiplier,
   the telescoping sum, and finite primitive-factor coefficients in exact
   rational arithmetic.
4. Replay runs a fresh producer in a temporary directory and compares bytes.
5. At least 20 hostile mutations—including repaired payload hashes—must fail
   the checker.
6. LuaLaTeX runs two settled passes for each of rounds 0, 1, and 2 in two
   fresh directories under the fixed epoch; PDFs are byte-identical across the
   paired builds, fonts embedded, text and logs inspected, and no sidecars kept.
7. The release script reruns all checks and closes a 27-payload/28-physical-file
   ledger, excluding only the manifest itself.

## Expected boundaries

The full \(A(s)\) converges absolutely for \(\Re(s)>1/2\); at \(s=1/2\) rows
mark divergence.  Absolute primitive product convergence additionally requires
\(|z|A(\Re(s))<1\).  The identity \(1/(1-zA(s))\) is meromorphic away from
denominator zeros in that half-plane, which is a continuation claim rather than
an enlarged absolute-convergence claim.  Route-A is therefore
`A0_FAIL/A1_PASS_ANALYTIC/A2_FAIL/A3_FAIL/A4_FORMAL_HINT`.
