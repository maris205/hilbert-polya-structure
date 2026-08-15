# Paper 34 exact analysis report

## Raw data table

| Block | Evidence class | Population | Metric | Value | Failures |
|---|---:|---:|---|---:|---:|
| complete_graph_enumeration | COMPLETE_FOR_FROZEN_N_LE_4 | 66066 | mixed_primitive_roots | 775471 | 0 |
| complete_shared_state_pairs | COMPLETE_FOR_FROZEN_N_LE_4 | 613996 | mixed_primitive_roots | 613996 | 0 |
| complete_repaired_connectors | COMPLETE_FOR_FROZEN_N_LE_4 | 161475 | mixed_primitive_roots | 161475 | 0 |
| preregistered_connector_normal_form | COUNTEREXAMPLE_CENSUS | 164336 | strict_external_witness_failures | 18272 | 18272 |
| hash_seeded_graph_controls | FINITE_DETERMINISTIC_CONTROL_NOT_EXHAUSTIVE | 64 | mixed_primitive_roots | 69073 | 0 |
| terminal_recognizer | EXACT_FINITE_IDENTITY | 160 | determinant_equal | 1 | 0 |
| arbitrary_inventory_pruning | EXACT_FINITE_CONTROLS | 8 | proper_supports_change_determinant | 6 | 0 |
| kraft_clock_proxy | FINITE_WITNESS_NOT_INFINITE_PROOF | 12 | exact_configuration_passes | 12 | 0 |
| first_return_marker | EXACT_FORMAL_POLYNOMIAL | 17 | raw_differs_but_z1_equal | 17 | 0 |
| independent_evaluator | INDEPENDENT_RECONSTRUCTION | 5 | aggregate_rows_equal | 5 | 0 |

Complete enumeration is restricted to all graph masks on at most four vertices. Hash-seeded graphs, Kraft cutoffs, inventories, and marker checks are finite deterministic evidence and are not part of that exhaustive claim.

## Key findings

1. Observation: The preregistered strict connector normal form failed on 18272 cycle pairs (including controls).
   Interpretation: One pair of attachment points need not admit two paths whose interiors simultaneously avoid both cycles.
   Implication: C2 is false as written, but this does not refute same-SCC positive concatenation closure.
   Next step: Use arbitrary SCC paths P:u->v and Q:v->u; permit cycle traversal or distinct attachment points.

2. Observation: The repaired audit exhaustively checked 66066 graphs, 613996 shared-state pairs and 161475 connector pairs, producing 775471 mixed roots with zero failures.
   Interpretation: Within the frozen positive finite class, cyclically distinct recurrent branches in one SCC close under concatenation to an additional primitive root.
   Implication: A literal one-orbit-per-label ledger must separate its recurrent cycles; this is finite evidence aligned with the independent theorem proof.
   Next step: Promote only the repaired hypothesis, not the rejected strict normal form.

3. Observation: The 64 deterministic 5..8 vertex controls added 69073 mixed roots with zero repaired-C2 failures.
   Interpretation: The mechanism is graph recurrence, not arithmetic inventory.
   Implication: These are finite controls and must not be merged with the complete n<=4 census.
   Next step: Keep the complete/control evidence classes separate in any paper table.

4. Observation: A 160-state exact adjacency with 34 acyclic decision states had the same Newton determinant as its 126-state recurrent product for all eight post-freeze inventories; every proper nonempty pruning changed it.
   Interpretation: Terminal recognition is determinant-neutral until rejected recurrent blocks are deleted.
   Implication: The selected determinant belongs to a label-dependent pruned operator, not to the unclassified recurrent object.
   Next step: Reject terminal orbitification/pruning as same-object arithmetic emergence.

5. Observation: All 12 q-ary/cutoff configurations passed prefix, Kraft, roof-share, and powered clock inequalities exactly.
   Interpretation: The finite artifacts instantiate the premises of the Kraft-clock argument without floating-point approximation.
   Implication: They are regression witnesses only; noncompactness remains an infinite weak-null theorem.
   Next step: Cite the analytic proof for noncompactness and label the cutoff table as a proxy.

6. Observation: All 17 raw cycle factors differed formally from first-return factors and agreed after z=1.
   Interpretation: Induction replaces graph-step length by return count.
   Implication: First return is valid only as a changed-marker object.
   Next step: Enforce the z^ell-to-z firewall in subsequent candidates.

7. Observation: The signed three-state control had determinant one, and orthogonal matrix branches killed mixed products while pure products survived.
   Interpretation: Positivity is the coefficientwise no-cancellation hypothesis.
   Implication: The prototype does not close signed, matrix, supertrace, or nonlocal-weight programs.
   Next step: Any such successor must prove source-natural cancellation and same-marker operator ownership independently.

## Suggested next experiments

1. Prove the repaired arbitrary-path connector lemma with formal edge variables.
2. Treat any signed or matrix successor as a new source-locked cancellation problem.
3. Do not reopen residue/Manin or terminal-decider families.
