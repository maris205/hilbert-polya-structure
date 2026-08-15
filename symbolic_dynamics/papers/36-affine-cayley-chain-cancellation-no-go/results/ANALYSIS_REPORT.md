# SD-C38 exact analysis report

## Raw comparison table

| Evidence | Case | Metric | Value | Role |
|---|---|---|---:|---|
| identity_words | r=2 | first_excess_length | 5 | exponent_control |
| identity_words | r=2 | first_excess_count | 10 | exponent_control |
| identity_words | r=3 | first_excess_length | 6 | exponent_control |
| identity_words | r=3 | first_excess_count | 12 | exponent_control |
| identity_words | r=4 | first_excess_length | 7 | baseline |
| identity_words | r=4 | first_excess_count | 14 | baseline |
| identity_words | r=5 | first_excess_length | 8 | exponent_control |
| identity_words | r=5 | first_excess_count | 32 | exponent_control |
| marker | r=1 | unit_step_marker_descends | true | balanced_control |
| marker | r=2 | unit_step_marker_descends | false | exponent_control |
| marker | r=3 | unit_step_marker_descends | false | exponent_control |
| marker | r=4 | unit_step_marker_descends | false | baseline |
| marker | r=5 | unit_step_marker_descends | false | exponent_control |
| finite_chain | r=1,q=4,t=3 | h1_affine_to_complete | 2->0 | finite_control |
| finite_chain | r=2,q=3,t=2 | h1_affine_to_complete | 1->0 | finite_control |
| finite_chain | r=3,q=4,t=2 | h1_affine_to_complete | 1->0 | finite_control |
| finite_chain | r=4,q=5,t=2 | h1_affine_to_complete | 1->0 | finite_control |
| finite_chain | r=4,q=7,t=3 | h1_affine_to_complete | 1->0 | finite_control |
| finite_chain | r=5,q=6,t=2 | h1_affine_to_complete | 1->0 | finite_control |
| generic_chain_lift | two_generator_one_relator | euler_multiplier | 0 | matched_generic |

## Key findings

### F1

- Observation: The first affine excess appears at lengths 5, 6, 7, and 8 for r=2,3,4,5, with exact excess counts 10,12,14,32.
- Interpretation: The unquotiented finite-trace control detects the defining relation at its shortest polygon length.
- Implication: Relation imposition does not itself cancel path multiplicity.
- Next step: Use the analytic contractibility proof, not finite counts, to classify the filled ledger.

### F2

- Observation: The unit marker descends only for balanced r=1; it fails for every r=2,3,4,5 mutation.
- Interpretation: Unequal relation-side lengths obstruct a free graph-step grading before determinants are considered.
- Implication: No quotient determinant can inherit the original marker for the affine family.
- Next step: Do not specialize z or alter deg(u) to repair the candidate.

### F3

- Observation: Affine-only finite cells leave H1 dimensions 2,1,1,1,1,1, while complete finite-presentation cells give zero in all six controls.
- Interpretation: The affine-only residue consists of omitted quotient relations, not infinite-source descent evidence.
- Implication: Complete relation cancellation is topologically total rather than selective.
- Next step: Retain finite quotients only as artifacts controls.

### F4

- Observation: The scalar chain lift has zero supertrace for all 48 sampled powers and all matched two-generator/one-relator controls.
- Interpretation: The multiplier 1-2+1 cancels the complete ledger independently of the affine arithmetic relation.
- Implication: The repair realizes the proves-too-much failure and earns no recognition credit.
- Next step: Paper 37 may test only a source-derived non-flat matrix coefficient system on the unquotiented same-marker shift.

## Decision

Prototype semantic checks: `33/33`.
Independent integration checks: `35/35`.
Authority tests: `53/53`.

The finite exact audit supports the frozen negative theorem boundary.
It does not replace the independent infinite proofs.
