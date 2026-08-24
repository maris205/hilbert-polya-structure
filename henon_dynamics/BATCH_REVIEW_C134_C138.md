# Batch review: HCS-C134--HCS-C138

Date: 2026-08-24

System family: five separate Route-A dynamical refinements under
`NO_BAD_EULER_OR_ROOT_NUMBER`.

Recommendation: **retain all five as explicit structural progress; continue
Route A; keep Route B unauthorized**.

## Completed paper outputs

1. **C134** replaces C129's single fifth-root phase with a faithful Laurent
   character torus on the same scaled graph-directed affine family.  The first
   three normalized logarithmic Fredholm jets recover every branch-labelled
   integer translation.  The exact `k=1/k=6` control separates finite-quotient
   aliasing from faithful recovery, while label orientation and
   finite-precision stability remain explicit boundaries.
2. **C135** refines C130's destination-symbol roof to four directed-edge
   coordinates.  Its exact determinant and all-period primitive product
   separate `000111` from `001011`.  The primitive pair
   `001011/001101` still collides, and the identity `N01=N10` proves that the
   antisymmetric off-diagonal roof direction is invisible to all periodic
   data.
3. **C136** extends C131's odd-level metaplectic family to every primitive
   additive character.  Fourier, chirp, Weyl, evolution, and the involutive
   antiunitary `Theta_[r,c]=F_[r,c]K_r` factor exactly under canonical CRT.
   Fixed ordered multifactor leaves are independent of split schedule and
   parenthesization.  The standard `c=1` local factors fail by more than a
   scalar; no factor-permutation coherence is inferred.
4. **C137** promotes C132's one Möbius digit pair to the full rectangle
   `[3,7/2] x [6,7]`.  Closed branch images have uniform gap `1/45`, the
   Bergman owner has trace norm at most `89/16` and an explicit trace-norm
   Lipschitz bound, and `aaabb/aabab` retain a uniform positive order gap.
   Tangency on `[3,4] x [6,7]` is the exact negative control.
5. **C138** equips C133's theta graph with magnetic holonomy.  The resulting
   unitary family has common-phase gauge invariance, parameter-changing
   antiunitary reversal, a complete Laurent determinant, and an oriented
   winding ledger.  Individual primitive orientations retain flux sign even
   though the fully aggregated determinant is inversion-even.  The real
   half-phase lift and its single-edge `2*pi` sign conjugacy are explicit.

## Uniform release audit

All five deterministic producers, independent checkers, separate symbolic
cross-checks, canonical byte replays, and hostile mutation suites pass.  The
independent receipts are:

- C134: 71 checker assertions and 64 symbolic checks;
- C135: 2,121 checker assertions and 37 symbolic checks;
- C136: 1,131,414 exact checker cases and 96,449 symbolic/congruence checks;
- C137: 18,414 exact word receipts and 18,379 symbolic checks;
- C138: reconstruction of 14,760 rooted and 1,905 primitive walk receipts,
  plus 197 symbolic checks.

Mutation rejection totals are respectively 48/48, 43/43, 84/84, 41/41,
and 45/45.  Their repaired/stale splits are `47+1`, `42+1`, `83+1`, `40+1`,
and `44+1`, for 261/261 rejections overall.

Every release manifest has an exact 27/27 disk ledger with no missing, extra,
size-mismatched, or hash-mismatched payload.  Each package contains 28
physical release files including its self-excluded manifest.  No
`__pycache__`, `.pyc`, LaTeX auxiliary, log, recorder, or output file remains.

Five fresh isolated fixed-epoch double builds reproduce the checked-in PDFs
byte for byte.  The 14 rendered pages use embedded/subset fonts and show no
clipping, collision, truncation, malformed formula, broken table, or blank
content.  Final build logs contain no warning, overfull/underfull box,
undefined reference or citation, or multiply-defined label.

## Content-addressed release ledger

| paper | evidence SHA-256 | PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|
| C134 | `45fa45b4668464564abb79db54b0e76b76c3acab5ae163acadb81a31d7bdc21d` | `404b2618ff7e51c6018a7b9c007b0d683dd3ade8ac6af0484f3f782692d651d5` | `7ebffe3e141628585077e340e3c3860a46fb555443b1dabdd7b9fcff701e7c18` |
| C135 | `9980adaab9eb511fca367b83620d557ee2227a5e9c979b6c7c8ae9a73aebee36` | `0a0ab1a405e2fdec843d26a6fa1de81d74ce12768721dd21dcee29502882c808` | `401529017d3aed50d291ff979ef22ad59664126d82bc13c47ccb4a540fe4e076` |
| C136 | `5b3f4a6494c8f4559a99b520247c1b83f1504884a31aaeb1fcdc3c153bbac47b` | `ab83e92b78e5857946d501c579bc3d53ca233ea5d32bf1c1865506ce776a460d` | `df52aaa1c947907903a2b8a3abcab1c0fcf628b002af691f25fd6a367aaa16ac` |
| C137 | `415863573ee584d72b4a47adf1e923ef04c94cef64c843c736a8e4e90802cfdd` | `71619e35d0395c53e946bf18c97e320a0f80f88ffcca1ef3fc207020b18b8a2a` | `709a3ccc2c717e69bfaf2e509a93d477717bcaeaa3dcfbd16d9b78e62a374a8b` |
| C138 | `733c703d9bb7b4a69dbe12ebc6d09e65dabff227b636b439c27f1d5e4a9c93c8` | `abc8fb4dff98646b07ff030a900467f1d5cfe5c0ce9db317d57205bb7689f0c6` | `664d07b1783b5f423133f19ea5b8dddc9b39f95b1434fb29428855bf95ad7905` |

## Cross-review repairs and failure-mode audit

The reviews were internal evidence-anchored theorem/scope audits; no external
reviewer independence, acceptance score, or novelty score is claimed.  They
produced four release-relevant repairs:

- C134 added exact source-lock and Newton-jet checker/mutation coverage and
  synchronized the final paper's validation totals.
- C135 removed two carriage-return control characters that had corrupted
  roman labels in the rendered primitive formulas.
- C136 moved its A1 evidence back to inherited classical torus primitive
  structure, added a complete antiunitary proof/check/mutation chain for A4,
  and narrowed multifactor coherence to fixed ordered leaves.
- C138 made the directed-bond diagonal order and the `2*pi` half-phase sign
  conjugacy explicit, avoiding an entrywise-periodicity overclaim.

The remaining failure modes are deliberately retained:

- **Character completeness:** C134 proves exact labelled algebraic recovery,
  not stable inversion from arbitrary finite-precision samples.
- **Orbit injectivity:** C135 resolves one population collision but proves a
  finer same-edge-count collision and an antisymmetric-roof kernel.
- **CRT scope:** C136 proves induced-character associativity, not standard
  character repair, factor permutation, even-level, or noncoprime coherence.
- **Uniform geometry:** C137's theorem is for its frozen smaller rectangle;
  the larger rectangle has an exact zero gap.
- **Flux aggregation:** C138 retains orientation at the primitive-ledger
  level, while full determinant aggregation is necessarily flux-even.
- **Forbidden promotion:** target divisor matching, arithmetic local factors,
  Euler factors, root numbers, automorphy, Hilbert--Pólya, and Route B appear
  only in explicit nonclaim or hostile-mutation contexts.

## Route-A assessment

The strict tuples are:

```text
C134 (A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
C135 (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
C136 (A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)
C137 (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
C138 (A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)
```

C136 and C138 reach different A4 subgates on distinct source systems; their
coordinates are not combined.  No candidate has a frozen external target
comparison, so A2/A3 remain failed.  Every overall verdict is
`ROUTE_A_EXPLORATORY` and `route_b_invocation_allowed=false`.

## Next gate

The smallest source-internal continuations are a certified normed
finite-precision observation model for C134, a genuinely order-sensitive roof
beyond C135 edge counts, a source-derived standard-character correction or
controlled cross-level limit for C136, and a flux-sensitive nonaggregated
operator statistic for C138.  A target-facing divisor or counting comparison
requires a separately frozen protocol and explicit authorization; it is not
part of this batch.
