# Experiment report — SD-C24

## Outcome

The exact audit confirms the cofactor construction and simultaneously closes
its scalar abelian selection route. The source-derived cocycle has genuine
integer holonomy and an honest Fredholm region, but `Q=2` contains one
primitive canonical cycle at every length, unitary characters preserve the
whole class, and the neutral regular determinant is one. The result is a sharp
Fredholm trilemma, not a Riemann Euler determinant.

## Exact census

- Source audit: 30,626 edges through `n=4096`, including 4,095 successor
  edges; zero quotient mismatches and zero loops.
- Simple cycles at `N=12/20/30`: `12/29/52`; holonomy-two cycles:
  `5/9/14`, with exactly the lengths `2..6`, `2..10`, and `2..15`.
- Atomic biconditional ledger: 120 enumerated/predicted witness rows for
  post-freeze atoms `2,3,5,7`, all exact.
- Rooted cycles through `r=8`: counts
  `0,2,3,10,10,29,28,82`, totaling 164 rooted words with rotations and
  temporal repetitions recorded explicitly.
- Group traces: 88 nonzero coefficient rows through `r=10`, `s=1,2`; all 80
  atomic coefficient checks agree exactly and no atomic repetition
  contamination occurs.
- Neutral trace/determinant: 42 trace/coefficient rows, all consistent with
  determinant one.

## Analytic and numerical audits

The theorem-side trace-class domain is exactly
`Re(s)>1/2` and `Re(s+u)>1/2`. Fifty-six diagnostic rows cover eight points
and seven cutoffs on both sides of both boundaries. They are labeled as
finite illustrations, not proofs. The pure cofactor controls retain unit
successor weights at every cutoff; boundedness is claimed only in the proved
range `Re(u)>1`, where noncompactness follows.

All 15 exact integer gauge cases pass. Twelve unitary finite-prefix cases have
entry and determinant errors below their registered thresholds. Alias-free
Fourier inversion reconstructs 12 nonzero group coefficients with maximum
absolute error below `2e-15`. Four exact rational finite determinants agree
with Newton trace expansions.

The obstruction controls are decisive: 124 induced-return rows distinguish
constant pure-cofactor weights from endpoint damping; 63 endpoint rows are
strictly factorially decreasing; 124 scalar phase rows retain every canonical
cycle; and 186 rows across six positive inventories preserve exactly the same
`Q=2` support, including composite lengths. The transported presentation adds
31 exact naturality checks. Selection margin is zero.

## Reproducibility and scope

The final suite contains 26 exact tests. Results, Route-A metadata, source
policy, cache cleanliness, and pending two-stage provenance are checked by an
independent integrity script. A full runner regenerates, tests, analyzes,
audits, freezes, verifies the SHA ledger, and repeats the entire sequence for
byte determinism.

No target zeros or target roots were evaluated. Corresponding metrics are
`not applicable; no_target_zero_evaluation`. No cross-family experiment was
run, and Route B remains locked.

## Route decision

`(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_WEAK,
A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)` with overall
`ROUTE_A_REJECTED`. The positive result is the exact same-object holonomy and
Fredholm structure. The blocking result is the all-length/product-holonomy
blindness theorem, reinforced by zero-margin controls.
