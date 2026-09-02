# Paper improvement log — HCS-C285

The three archived PDFs come from one conditional source. Reviews below are
source-local hostile mathematical/presentation reviews; no external-review
identity or literature novelty assessment is fabricated.

## Score progression

| Round | Pages | Internal readiness | Substantive state |
|---|---:|---:|---|
| 0 | 2 | 6/10 | exact finite product form, derivatives, flows, and reversal |
| 1 | 3 | 8/10 | adds full unique/tied thermodynamic theorem and proof |
| 2 | 4 | 9/10 | adds boundary, evidence, collision, limitation, and Route-A closure |

## Round 0 hostile review

**Summary.** The finite theorem is self-contained and correctly distinguishes
nonreversible global balance from detailed balance. The title and abstract,
however, promise bottleneck condensation that the baseline manuscript does
not yet state or prove.

**Major findings.**

1. The unique/tied distinction must be a theorem, not a sentence inferred
   from a few coefficients. It needs the exact normalizer constant and a joint
   statement for all nonbottleneck coordinates and bottleneck shares.
2. A tied bottleneck cannot be resolved by perturbation or replaced by equal
   deterministic fractions. The conditional finite law and its Dirichlet
   limit must be explicit.
3. The proof must distinguish total-variation convergence of the countable
   nonbottleneck vector from weak convergence on the simplex.

**Fixes implemented in round 1.**

- Added Theorem 3 with
  `Z_N~w_*^N N^(r-1)/(r-1)! product(1-q_j)^(-1)`.
- Added the exact fixed-vector marginal and upgraded pointwise convergence to
  total variation because the limiting masses sum to one.
- Added the exact conditional uniform-composition factorial moments and used
  compact simplex moment determinacy to obtain
  `Dirichlet(1,...,1)`.
- Proved joint independence and separated unique, tied, all-equal, and
  one-station regimes.

Round-1 PDF SHA-256:
`ab2bf74aa9be4ab4a1a33b1b584755ab505e807134514b40e9bdb781ea13052d`.

## Round 1 hostile review

**Summary.** The main finite and thermodynamic theorems are now complete, but
release semantics are still under-specified. A hostile reader could confuse
self-route event counts with generator transitions, infer routing detailed
balance from the empty chain, or substitute zero service into an interior
formula.

**Major findings.**

1. State explicitly that `N=0` is a trivially reversible singleton and does
   not imply the positive-population routing criterion.
2. Separate zero routing entries (admissible under irreducibility) from zero
   service rates/weights (singular and excluded). Include `N=1`, `m=1`, equal
   weights, and traffic gauge.
3. State exactly what finite evidence verifies and what the analytic proof
   owns. Give independent-checker, symbolic, replay, and mutation counts.
4. Name the nearest repository collisions and give strict Route-A nonclaims;
   do not turn a finite Markov generator into a formal quantization.

**Fixes implemented in round 2.**

- Added the nine-row admissible/singular boundary table and accompanying
  periodic-routing and population semantics.
- Added the 9-case/177-state evidence ledger, 11,628-checker-assertion,
  28-SymPy-identity, 158,346-byte replay, and 64/64 hostile-rejection report,
  followed immediately by the finite-evidence/all-parameter-proof boundary.
- Added collision distinctions from C225, C263, C220, C246, C282 and C181.
- Added scope limitations and the literal all-fail tuple, overall rejection,
  Route-B false, and the no-formal-quantization statement.

Round-2/final PDF SHA-256:
`088d2ca85d86d1e1fc797071bef5aa8c4a4364178f0ab61f454d77df14e6000e`.

## Final hostile-hardening pass

The independent checker now validates exact JSON-decoded types at every
object and nested cell, rejects Boolean values wherever integers are required,
and accepts rational cells only as canonical reduced strings. The mutation
suite adds the four reproduced type-confusion escapes, further raw/nested type
attacks, noncanonical rational text, and top-level plus nested duplicate keys.
The paper source also repairs the state-space glyph to `\mathcal S_N` and
forces the intended abstract spacing before the zero-population sentence.

## Build and presentation review

Every round was built twice from each of two fresh directories using two
LuaLaTeX passes per build at `SOURCE_DATE_EPOCH=1788307200`. The pairs were
byte-identical to their archived PDFs. Page counts are `2,3,4`, so each
substantive revision is visible at the artifact level. Logs have zero LaTeX,
package, layout, missing-character, reference, or citation warnings. Font
rows are embedded and subset (`22/22`, `23/23`, `24/24`). All nine rendered
pages were visually inspected: equations, proof boxes, table rules, URLs,
page breaks, and margins are intact.

Round-0 PDF SHA-256:
`281d88d391a2ca9fdf79ba30ac840959150bf9081954571e7c9543c0ea798fe5`.
