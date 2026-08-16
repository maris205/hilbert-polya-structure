# Paper 38 exact experiment report — SD-C40

## Outcome

The exact integration confirms `STOP_BASS_SERRE_TREE_BRANCH` /
`CLOSE_ENTIRE_AFFINE_BRANCH` and strict `ROUTE_A_REJECTED`. The full
presentation-canonical Bass--Serre tree has an empty reduced closed-
path ledger; its full-tree Hashimoto operator is noncompact and not
trace class; and the standard discrete tree-lattice determinant
hypotheses fail. At `r=1` the automorphism-group image is discrete but
the action has infinite kernel and is nonproper; for `r>=2` the
faithful image is nondiscrete. The separately typed conjugacy ledger
is generic for `r>=2`, divergent at `r=1`, and marker-incompatible.

## Canonical exact counts

| Evidence | Exact result |
|---|---:|
| evaluator assertions | 277/277 |
| parameter rows | 11 |
| generic necklace rows among `r>=2` | 10/10 |
| deliberate GBS empty ledgers | 18/18 |
| deliberate GBS owned full-tree Fredholm | 0/18 |
| random one-relator controls | 64 |
| random controls eligible for the frozen split | 0/64 |
| compatible marker rows | 0/5 |

The random controls are eligibility controls: ineligible rows are not
counted as failures of a mechanism they do not possess.

## Reproducibility and separation

- Fresh/cold runs: 3/3 byte-identical.
- Run C executed from an isolated temporary code copy that was removed.
- Source and evaluator occupy disjoint directories and communicate
  only by canonical JSON through subprocess standard streams.
- Absent/null/empty/populated transport metadata and simulated future
  root-manifest absence/presence leave scientific and Route bytes
  unchanged.
- Integration checks: 44/44.
- Scientific aggregate SHA-256: `a9ffa66d826bcaf8eef0b00991aafa46cdbeaca7014430c68aacf070446adf24`.

## Analysis boundary

All reported counts are deterministic exact enumerations, so p-values,
confidence intervals, and error bars are not applicable. Finite tree,
orbit, and orthogonal-column rows audit formulas and implementation;
they do not replace the independent infinite-object proofs in
`PROOF_PACKAGE.md` and `DERIVATION_PACKAGE.md`. No quotient, arbitrary
representation, damping, Route-B repair, or post-result mechanism search
was performed.

## Material passport

Verification status: `VERIFIED` by exact fresh A/B and isolated cold-C
byte identity plus independent full integrity audit.
