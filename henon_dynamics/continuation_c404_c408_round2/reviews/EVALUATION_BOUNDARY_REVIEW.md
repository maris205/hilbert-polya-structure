# Independent evaluation-boundary consistency review

Date: 2026-09-06. Reviewer: the current Hénon-arithmetic team agent.
This report preserves the completed read-only consistency check of the
three Route-A YAML records and their shared scope statement. It is
separate from the C405 manuscript review and is not a new formal
evaluation, a mathematical review of all three papers, or external
human peer review.

## Verdict and unchanged inputs

**No internal tuple, scope-flag, metric, or source/target-boundary
inconsistency was found in the inspected records.** All five input
hashes below were rechecked before preserving this report and are
unchanged from the completed consistency check.

Paths in the first four rows are relative to
henon_dynamics/continuation_c404_c408_round2/. The authority path is
relative to the repository root.

| Inspected input | SHA-256 |
|---|---|
| EVALUATION_SCOPE.md | 3f57c80303721af3652ade4574af275aa0c19054dde9f1159e53ea81e42016d8 |
| evaluations/route_a/HCS-C404/2026-09-06.yaml | d82f8c63d5b35b88f9d59ae09cb6c1af4a2dbfb18d37430151f9c3e86bd22a40 |
| evaluations/route_a/HCS-C405/2026-09-06.yaml | d904350cf40ffe54e333ae5ee26fef012c242d9400b6c14ae4fb230e564e1941 |
| evaluations/route_a/HCS-C406/2026-09-06.yaml | 0e69a4cb7bc9a8a3995edb88fdaef7a89d799f86228f83747e0b18c6f8f78258 |
| flow_systems/skills/route-a-evaluator.md | 6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c |

The evaluator authority is version 0.2.0. Its 686 lines were read
completely, as were all three YAML records and EVALUATION_SCOPE.md.
The reviewer also read the C406 proof package's opening contract and
source definitions, not its complete proof, for this limited comparison.
The C404 and C405 mathematical contracts had already been read in the
separate proof/manuscript tasks.

## Exact tuples and their declared meanings

| Candidate | Exact tuple (A0, A1, A2, A3, A4) | Overall status |
|---|---|---|
| HCS-C404 | (A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL) | ROUTE_A_EXPLORATORY |
| HCS-C405 | (A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FORMAL_HINT) | ROUTE_A_EXPLORATORY |
| HCS-C406 | (A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION) | ROUTE_A_REJECTED |

Each tuple is identical to the five verdicts in that record's a0–a4
sections. No record treats mathematical source success as target
determinant or target analytic success.

- **C404:** A1_PASS_ANALYTIC is explicitly limited to native S-cycle
  counts. It does not assert an owner correspondence for all rational
  primes, logarithmic prime clocks, or von Mangoldt amplitudes.
  Its natural-boundary theorem is not continuation through that boundary.
- **C405:** A4_FORMAL_HINT refers only to the positive source operator,
  including the nonzero maximal-convolution operator in the finite-F
  branch. The divergent branch's zero strong-resolvent limit and absence
  of an orbit-to-Hamiltonian transport remain explicit.
- **C406:** A4_NATURAL_QUANTIZATION is expressly source-Schrödinger-only:
  the same closed form defines the source spectral count and unitary
  group, with real-form complex-conjugation symmetry. It is not a
  supplied arithmetic classical-orbit transport or target zero divisor.
  The overall record remains ROUTE_A_REJECTED.

These source-only qualifications must accompany any later excerpt of
the A1 or A4 labels. A bare label would omit a material restriction.

## Flags, missing metrics and controls

Each record has nine scope flags, giving **27 explicitly false flags**:

~~~text
claims_target_arithmetic_local_data
claims_target_euler_factors
claims_root_number
claims_automorphy
claims_target_divisor_or_counting_law
claims_target_functional_equation
claims_target_zero_match
claims_hilbert_polya_operator
invokes_route_b
~~~

Each record also has nine A2 metrics, giving **27 NOT_TESTABLE metrics**:

~~~text
zero_error_train
zero_error_validation
zero_error_test
extra_zero_count
missing_zero_count
root_count_discrepancy
cutoff_drift
precision_drift
control_margin
~~~

No unavailable error or missing/extra-zero count is encoded as zero.
All three records have route_b_invocation_allowed set to false.
All retain A2_FAIL and A3_FAIL, and the common
NO_BAD_EULER_OR_ROOT_NUMBER boundary.

The mandatory three-type A0 control panel is explicitly INCOMPLETE
in every record and in the shared scope statement. Proven neighboring
parameter comparisons and simpler-parent comparisons are distinguished
from unrun randomization/control categories. Inapplicable prime-list
controls are marked NOT_TESTABLE where appropriate. Neither a proof
nor source self-adjointness is presented as completing those controls.

## Actual read-only checks performed

The completed pass used normal file reads and SHA-256 checks, then
parsed each YAML independently with Python/PyYAML from shell standard
input. This was a record-format check, not a numerical or mathematical
experiment. The parsed checks were:

~~~text
tuple == [a0.verdict, a1.verdict, a2.verdict, a3.verdict, a4.verdict]
every scope_flags value is the boolean false
route_b_invocation_allowed is the boolean false
every a2.metrics value equals the literal NOT_TESTABLE
~~~

All four conditions returned true for all three candidates. The
candidate identifiers, exact tuples and overall statuses were also
printed and compared with the text. Manual inspection supplied the
nine-key counts in each category and the source-only/control-scope
checks above.

All three YAML files contain the same reference-routing string,
../../../EVALUATION_SCOPE.md. A read-only realpath existence check
from the C404 YAML directory resolved it to the actual batch-level
scope file. The identical relative directory depth of C405 and C406
gives the same target. This does not claim a separate audit of every
artifact link in the package.

For the present report-preservation task, only the five input hashes
were rechecked; no parser, proof, experiment, or formal evaluation was
rerun. This newly authorized report is the only file written.

## Limits of this review

The reviewer did not independently repeat the coordinator's full
prior-work routing, validate every proof in the six background PDFs,
or regrade the candidates. In particular, the shared scope's refusal
to adopt a background guide's zeta-zero characterization as a newly
verified theorem is preserved. The reviewer did not perform a new
complete C406 mathematical review, final PDF construction or all-page
visual QA in this task.

No YAML, authority, scope statement, manuscript, experiment, registry,
evaluation state, or Git state was edited. The conclusion is bounded
to the consistency of the exact records above and must not be cited
as target-arithmetic certification or permission to invoke Route B.
