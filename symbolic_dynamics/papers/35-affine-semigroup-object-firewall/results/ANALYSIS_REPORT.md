# Paper 35 exact affine benchmark report

## Exact evidence table

| Block | Evidence class | Population | Metric | Value | Failures |
|---|---|---:|---|---:|---:|
| positive_height_windows | EXACT_FINITE_LEDGER_PLUS_INDEPENDENT_DAG_CHECK | 520 | strict_height_edges | 520 | 0 |
| symmetric_two_step_backtracks | EXACT_EDGEWISE_CONSTRUCTION | 520 | hashimoto_rejected_backtracks | 520 | 0 |
| hashimoto_word_census | EXHAUSTIVE_FOR_FROZEN_LENGTH_AND_BASES | 699040 | primitive_cyclic_nb_closed_words | 88 | 0 |
| affine_relation_witnesses | EXACT_SYMBOLIC_WITNESSES | 8 | closed_primitive_length_r_plus_3 | 8 | 0 |
| commutation_and_monoid_controls | EXACT_GENERIC_CONTROLS | 8 | generic_relation_cycles_survive | 1 | 0 |
| operator_certificates | FINITE_WITNESS_SEQUENCES_NOT_NUMERICAL_PROOF | 4 | exact_disjoint_support_certificates | 1 | 0 |
| finite_quotients | EXHAUSTIVE_FOR_Q_1_THROUGH_12 | 48 | relation_and_Uq_cycles_retained | 48 | 0 |
| bc_diagonal_firewall | EXACT_FINITE_RATIONAL_COEFFICIENT_IDENTITY | 2 | Tr_Dm_over_m_log_coefficients | 2 | 0 |
| prime_fock_marker_firewall | EVALUATOR_ONLY_EXACT_CONTROL | 8 | occupation_series_methods_equal | 1 | 0 |
| signed_matrix_groupoid_boundary | EXACT_BOUNDARY_FIXTURES | 3 | boundary_gate_pass | 1 | 0 |

The exhaustive claims are restricted to the frozen r/base/length and quotient ranges. Infinite operator conclusions remain theorem-owned by the mathematical lock.

## Findings

1. Observation: Every frozen positive P_r edge increased the authority height h_r(b,k)=b+r^k with the preregistered exact increment, and each induced finite window passed an independent Kahn DAG audit.
   Interpretation: The precise right-Cayley source is acyclic in the positive orientation; the result is not asserted for arbitrary ax+b action graphs.
   Implication: A nonzero positive primitive-cycle determinant cannot be extracted from this frozen graph without changing the source object.

2. Observation: Symmetrization produced one primitive length-two immediate backtrack per frozen edge; Hashimoto exclusion removed all of these witnesses.
   Interpretation: The nonbacktracking repair solves the universal reverse-edge artifact only.
   Implication: It does not solve presentation-relation cycles.

3. Observation: For r=2,3,4,5 at both bases, V U V^{-1} U^{-r} was admissible, primitive, cyclically nonbacktracking, and had length r+3; generic commutation and mutated monoid controls behaved the same way.
   Interpretation: Affine and commutation relations create generic reduced cycles independent of arithmetic acceptance labels.
   Implication: A Hashimoto ledger counts presentation geometry unless a further source-natural rule is proved.

4. Observation: All 48 quotient rows preserved the labelled affine relation and also acquired U_q^q; small moduli retained polygon collapse, including r=2,q=2.
   Interpretation: Finite quotients reproduce relation words while adding quotient-clock cycles and geometric degeneracies.
   Implication: A quotient determinant cannot silently be identified with the infinite graph-step determinant.

5. Observation: For both exact diagonal fixtures, [z^m](-log det(I-zD_beta))=Tr(D_beta^m)/m; the partition trace is only the linear coefficient, and det(I-D_beta)=0 at z=1 because n=1 contributes eigenvalue one.
   Interpretation: The diagonal trace, determinant germ, reciprocal determinant, and bosonic specialization are related but distinct objects.
   Implication: A same-source symbolic primitive interpretation requires a separate marker and whole-operator theorem.

6. Observation: The evaluator-only prime-Fock product matched independent occupation enumeration through degree six; z counted particle number and z=1 gave a finite Euler specialization.
   Interpretation: The control deliberately preloads a prime-indexed one-particle basis after the neutral source was hashed.
   Implication: It is a marker firewall, not an advance of the affine source.

7. Observation: Signed weights cancelled odd but not even power sums; a nonzero nilpotent matrix had determinant factor one; diag(1,-1) cancelled the first trace but not the second.
   Interpretation: Signed or matrix trace cancellation is weaker than literal deletion of primitive edge words.
   Implication: Groupoid, signed, and matrix successors remain open only with a source-natural all-orders and same-operator proof.

## Route verdict

The exact benchmark passes as a negative/correction benchmark. Route A is not advanced. The frozen route tuple is:

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL,
 A3_FAIL, A4_FAIL)
```

Paper 36 must exhibit source-natural cancellation or a quotient/induction with an explicit marker map and a same-whole-operator trace-log proof; otherwise this negative benchmark remains the conclusion.
