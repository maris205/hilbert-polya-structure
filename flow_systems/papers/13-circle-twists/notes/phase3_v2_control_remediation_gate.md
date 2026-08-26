# Paper 13 Phase-3 v2 control-oracle remediation gate

Version: **P13-CONTROL-ORACLE-REMEDIATION-v1**  
Date: **2026-08-15 (Asia/Shanghai)**  
Decision: **PASS TO ONE BOUNDED ORACLE REMEDIATION AND AUTHOR REPRODUCE**  
Open controls finding: **C0 / M1 / m0**  
Controls audit status: **not passed**  
`route_b_invocation_allowed: false`

## 1. Exact decision and precedence

Every artifact named below was independently rehashed immediately before
this gate was written.  Every digest matched.  The retained Phase-2 source
ledger reran `12/12 OK`, and the controlled implementation/result roots were
free of prohibited cache entries and task-temporary residue.

The binding independent review is:

| Artifact | Verified SHA-256 | Effective decision |
|---|---|---|
| `notes/phase3_v2_controls_review.md` | `83465435fda898c213b5923e0f42e84833dae8bb08476f7a12453523dfe20d04` | `REVISE`, C0/M1/m0 |

That review found the current CSV values, schemas, counts, serialization, and
manifest DAG correct, but found that the implementation does not derive
several detector and positive-oracle receipts independently and does not run
the complete isolated mutation registry.  This gate authorizes only the
minimal repair of that M1.

The first-run manifest

```text
results/manifest.json
SHA-256=52a6ea213fc7ebadbe26cc13716caf91c69c7adb829cec72434bea761b103e3d
```

is now a historical nonconforming baseline.  It is superseded for downstream
evidence purposes by this remediation decision and must not be consumed as a
passed controls package.  A newly generated manifest will itself remain only
a candidate until a fresh independent controls audit passes.  This gate does
not close M1 and does not grant result interpretation.

Any input-hash drift, write outside Section 5, schema/count/truth drift,
unapproved CSV-byte change, retry, second author top-level run, proof binding,
or weakened mutation gate voids this authorization fail-closed.

## 2. Frozen design and authorization lineage

| Artifact | Verified SHA-256 | Role |
|---|---|---|
| `notes/phase3_v2_design_gate.md` | `0094462b1e06cde0cf1fcc3536c608dcd96ef1e9eb0d85a0714df1666b799706` | bounded v2 theorem/control-design authority |
| `notes/phase3_control_design_lock.md` | `900c541713b1711bdab7fa0d264355b6d8ee27014094e60eac6aabe38190604c` | immutable v1 base control design |
| `notes/phase3_control_design_amendment_v1.md` | `5c9caea983b0047c4b16d0437c23b117a6b8150bbeb67b79c60fb9b2ba6a737e` | amended-v1 exact-row closure |
| `notes/phase3_control_design_review.md` | `bf56b96e19b682600ed5de43f7df51ef381fe82d4e12363f66cd1e7d2a5a5184` | final amended-v1 PASS C0/M0/m0 |
| `notes/phase3_control_design_amendment_v2.md` | `0c0113cff7cf7853d2f4e90ab311ace347f0bebbd8bbf36ab38501fd279c54d9` | frozen v2 control design head |
| `notes/phase3_control_design_v2_review.md` | `4385b74e81454ab699975a1c0f8217837ae1a7f90a6a220d47eecfdaaeca71c6` | independent design PASS C0/M0/m0 |
| `notes/phase3_v2_control_implementation_gate.md` | `e3226570f6d9630d5a912cb6b189d194bd33df395e276ce56d48ad75f9601312` | original bounded implementation authority; superseded only on repair/run scope by this gate |

All design schemas, row registries, mathematical/evidence ceilings,
serialization rules, exact totals, verify-only requirements, and manifest
firewalls remain binding except for the narrowly stronger oracle and mutation
requirements in Sections 6--9 below.  This gate is a remediation
authorization, not a design amendment and not a controls PASS receipt.

## 3. Exact active 24-lock manifest authority

The repaired manifest retains the same path-sorted 24-entry `bindings` set.
All entries rehashed exactly.

### 3.1 Active Phase-1/2/source locks

| Binding path | Verified SHA-256 |
|---|---|
| `notes/research_protocol.md` | `519563a28c3f11e3b3853f6875a84191444a68cd2c032c4cfcf69ca4152d5064` |
| `notes/candidate_lock.md` | `8cc0d08971762aa784afe1c844215353f170a75a3c0ab892415458ab010d0266` |
| `notes/pipeline_state.md` | `d98bf49d2eb5c1905ea3625251d787b247f3cf19577ff40f8bc0136186280fd5` |
| `notes/phase1_amendment_v1.md` | `ea5242ba6a8a1f2f867e8b258abc802fdeaace54db76629f0a9f0629e3e90d27` |
| `notes/phase1_final_gate.md` | `8a97a0bedcb048f1c9aa7db18d43bde45b17f1d7e92d38d2eeace688c64aee19` |
| `notes/phase2_novelty_search.md` | `444507f623a998152fdc8e427ee8a3f917c11d5823278b110d431dbcacac6eea` |
| `notes/phase2_convention_owner_audit.md` | `498830945b10a9213da945710d21b7ea74d9e0747864e23ca6223efc9bb74f52` |
| `notes/phase2_framework_source_audit.md` | `b47b1d6319c8419d96ca8679e3ff13b531a58f06a8b14afd95ec11f773345592` |
| `notes/phase2_final_review.md` | `ffcfbac5768fc409b3fa9e5df4f3b46a2366f553373664c78f4364d456854cd9` |
| `notes/sources/framework_source_manifest.md` | `4712cabd696d6d00205eb1eddd3c0d2dbf6706bfa14c097690a278941128606e` |
| `notes/sources/framework_sources.sha256` | `7fe6067bfc8e16e8b0447df295a887d48c2c04fa5ba25c9cca8acc7afade733f` |
| `notes/sources/.gitignore` | `c36e58e6a0e338579a7be747879a2891b023bfb79a676da58afca5e1b94c86be` |

### 3.2 Active v2 owner and review locks

| Binding path | Verified SHA-256 |
|---|---|
| `notes/phase3_control_design_lock.md` | `900c541713b1711bdab7fa0d264355b6d8ee27014094e60eac6aabe38190604c` |
| `notes/phase3_control_design_amendment_v1.md` | `5c9caea983b0047c4b16d0437c23b117a6b8150bbeb67b79c60fb9b2ba6a737e` |
| `notes/phase3_control_design_review.md` | `bf56b96e19b682600ed5de43f7df51ef381fe82d4e12363f66cd1e7d2a5a5184` |
| `notes/phase3_standalone_review.md` | `0397e1555a1ff07d30f06c3182b6cf570228ccd3e8db9e3c96666d118079c224` |
| `notes/phase3_standalone_amendment_v2.md` | `99c796bffe24f262d8ac8458b21fd253451bca51bac4b283660dab319992ed82` |
| `notes/phase3_standalone_amendment_v2_ownership_addendum.md` | `d9523d1692d60fbdff7bbf5ab6c00d44bdcd26f02dc5cdeeba8c7ba43d78a39f` |
| `notes/phase3_v2_methodology_review.md` | `96a5067015847ff88155b91658ae94e9ef5a6355ae176c1945644b3e729f4f74` |
| `notes/phase3_v2_devils_advocate.md` | `1c6bbb0bc7d3fc366de4d8a4eb869d4d4708f19647f10d780be095ac9e81f110` |
| `notes/phase3_v2_source_feasibility.md` | `3ce4e8db7914c0053a31b7e0e08e8f0fe02e0b2db15620f194c1ccae5ffeb320` |
| `notes/phase3_v2_design_gate.md` | `0094462b1e06cde0cf1fcc3536c608dcd96ef1e9eb0d85a0714df1666b799706` |
| `papers/2-flow-zeta/paper/manuscript.tex` | `72c34a0a30279ed7c070917a2c9242b8e9cb0a37a56779c246fa2cae04097fdc` |
| `papers/2-flow-zeta/notes/proof_audit.md` | `aaab83c32eb9d6c172be192dbb14acc6ed927a972d61c24a90dbfe94ecd0dbae` |

The v2 control design remains the separate manifest `design_head`, not a
twenty-fifth `bindings` entry.  This remediation gate, the implementation
gate, the v2 control-design review, and the controls review remain external
audit authorities; none is inserted by silently changing the reviewed
24-entry manifest schema.

## 4. First-run implementation and result baseline

### 4.1 Six implementation/readme files

| Path | Bytes | First-run SHA-256 |
|---|---:|---|
| `code/README.md` | 693 | `680a4106b6d572c6104f437fda23da9eb4be1f5eb9165d250059645c08ce5044` |
| `code/generate_controls.py` | 68,218 | `2e01da8782e63081f2895f9f9b3ccba11b18a2494b7e631080f6cf5d7bdec31e` |
| `code/test_controls.py` | 35,336 | `d81fcfd9e6a379ae421087fce613b627f90217e6d99838261c8886c6f05cf2b1` |
| `experiments/README.md` | 512 | `bd0b6a34beec217b525df0fbedbc78a166baa93cb2ad0ec40e7c6fc02ebb6a0b` |
| `experiments/reproduce.sh` | 3,913 | `56e15fc0d625ba78f96197294fed9ac7aff593717af9e338a55722b86dc250ca` |
| `results/README.md` | 532 | `aa240a9776b276e3dd196514084d1c3f1d6a7e8dc4922be89ba02c6bb7e9ff3b` |

These hashes identify the rejected first-run implementation baseline.  The
repair must change at least the generator and test implementation hashes.
README or reproduce-script bytes may change only to document or enforce this
same remediation contract; no unrelated refactor is authorized.

### 4.2 Twelve designed CSV baselines

| Artifact | Rows | Columns | Negatives | First-run SHA-256 |
|---|---:|---:|---:|---|
| `nerve_factorization_controls.csv` | 280 | 17 | 0 | `a00d2d6439aee3022703940b36892136ef7083d49541d2d8ad3bfd994a7582ba` |
| `circle_multiplier_cocycle_controls.csv` | 500 | 20 | 0 | `21a5246dba9dbe573a56fa9a0c18399061ff3e09d0238f68213123f3fa77e0a7` |
| `lift_integer_defect_controls.csv` | 500 | 20 | 0 | `598d414e46a7d34d1ab6a70b0047967047d984f24a3443aa19224a14a12da5b8` |
| `gauge_coboundary_controls.csv` | 196 | 19 | 0 | `c8717d8748691e92e8a7ea7ec1a196a5f42d5e151ee6e51244e2875f59677f26` |
| `twisted_convolution_controls.csv` | 78 | 23 | 0 | `2874817f2af1d3da31a29f497eba770eeac9c7275e6cc8693a7fa468fb482add` |
| `twisted_involution_controls.csv` | 54 | 26 | 0 | `114228b425905d5e235576b34f57eb15a0fd987065d4d206726045cceee569b5` |
| `completion_gauge_controls.csv` | 756 | 28 | 0 | `e7b8253a7d501b0c7b1d81939b59bfdc2f441b20592c678f749e643c0b800b2a` |
| `action_period_nonretention_controls.csv` | 56 | 20 | 0 | `9361f555cec4f74cab12faf30595e74830a00b44d7890e43579eae81ddcc9ee1` |
| `negative_domain_controls.csv` | 20 | 12 | 20 | `82b9e5988b30a8212235558af98a787df823213a7b0ad82be7d080da7c84c123` |
| `actual_standard_support_transfer_controls.csv` | 96 | 21 | 27 | `7bfb8ca2ed176d1a7aca2e5aa3680fd2d3992ef1d8e86a79b22c971912051176` |
| `target_summary.csv` | 12 | 11 | 0 | `97c2052c6286dd2013f735a79e7331d7a29f2bba7b2575fdc226865a34528f60` |
| `completion_corona_controls_v2.csv` | 117 | 41 | 20 | `672a29d4ac1b220336527517e50ba855f6a0c93568effd9b97e792015e4b2c41` |

The independent review reconstructed all twelve current CSVs byte for byte
and found their stored mathematical values correct.  These hashes are the
presumptive repaired-output hashes under the exact byte policy in Section 10.

## 5. Sole authorized repair write set and execution budget

Edits are authorized only at the same six checked-in paths:

```text
papers/13-circle-twists/code/generate_controls.py
papers/13-circle-twists/code/test_controls.py
papers/13-circle-twists/code/README.md
papers/13-circle-twists/experiments/reproduce.sh
papers/13-circle-twists/experiments/README.md
papers/13-circle-twists/results/README.md
```

Regeneration may replace only the twelve CSVs in Section 4.2 and
`papers/13-circle-twists/results/manifest.json`.  No other implementation,
helper, lock, source, proof, note, report, transcript, cache, or persistent
scratch artifact may be created or changed by the author repair lane.

After the repair bytes and regenerated candidate package are stable, the
author is authorized exactly one new externally serialized top-level run:

```text
papers/13-circle-twists/experiments/reproduce.sh
```

Recursive or concurrent entry and automatic retry remain failures.  If this
single run exits nonzero, leaves residue, changes checked-in bytes during
verify-only, or fails any count/oracle/mutation check, the authorization is
consumed and the lane stops; another run requires a new exact gate.  Temporary
work is permitted only in the two newly created empty `mktemp -d` roots and
must be removed by exit trap on success or failure.

## 6. Semantic negative-detector remediation

Every v1 and v2 registered negative must be verified semantically.  The
implementation must:

1. parse the exact fixture grammar into a typed attempted promotion;
2. construct the attempted algebraic, owner, credit, topology, framework,
   evidence, or manifest state from those parsed values;
3. evaluate the corresponding frozen invariant on that constructed state;
4. derive `observed_detector` from the actual failed predicate; and only then
5. compare the derived result with `expected_detector`, the registered reason,
   and the exact `violated_lock` assertion.

`negative_reason`, `expected_detector`, or `violated_lock` may select an
assertion to check, but none may supply, index, or copy the observed detector.
A reason-to-detector table, direct expected-token copy, nonempty-field test,
or mismatch-blind fallback is forbidden.  A malformed fixture, altered
semantic value, wrong lock, reason/fixture mismatch, or lock/fixture mismatch
must fail generation rather than receive `PASS`.

The three manifest-negative rows must construct their manifest mutations
from the parsed fixture instructions, not from the reason label.  The
mutated object must then pass through the same recursive no-proof,
no-self-hash, and complete-authority validator used for a candidate manifest;
the failure class is derived from that validation result.

Each of the 67 registered negatives must retain its exact-fixture success
probe and gain at least one malformed or semantically changed fixture/lock
rejection probe inside the existing 176-method budget.

## 7. Independent positive-oracle remediation

Positive rows and `status` values must be produced from independently coded
formulas, not copied fields or self-comparisons.

### 7.1 V2 family validation before serialization

A dedicated v2 family validator must run before CSV serialization and must
independently recompute:

- scalar norms and norm classes from exact stored Gaussian pairs, never from
  a copied `(input_norm, coordinate_norm_class)` tuple;
- finite/infinite multiplier, algebra-membership, `c0` membership, quotient-
  distance, nonzero-image, and injectivity predicates from the closed owner
  and input tables;
- finite-tail quotient distance and injectivity from the explicit `(m,n)`
  coordinate-ideal model;
- gauge left and right exponents from separate expressions parsed from
  `k`, `t`, `tau`, and the frozen orientation, with no shared final helper
  result copied into both sides;
- owner/credit/topology and max/reduced evidence rows against their closed
  literal registries; and
- every family count, row-kind count, artifact summary, self-summary, and
  package aggregate from the actually emitted rows, actual headers, and
  actual `unittest` discovery.

The generic row validator remains necessary but is not sufficient.  Each
family-specific predicate must succeed before `status=PASS` is assigned.
`status` may not be an unconditional default in the row-construction helper.
Any failed recomputation aborts generation; it is not serialized as a passing
row.

### 7.2 Product, star, gauge, and norm independence

Where a row compares two sides, the two witnesses must be computed by
separate formulas and data paths before equality is tested:

- twisted products and associativity sides are reconstructed in their own
  parenthesizations rather than copied or compared with one stored side;
- the actual and time involution values use separately implemented actual-
  owner and time-owner star formulas; calling the same `star_value` function
  twice is forbidden;
- gauge-square left and right exponents use independently coded expressions;
  a shared erroneous phase helper may not make both sides pass merely by
  producing the same wrong value; and
- `xi_norm_sq` is computed from the original coefficients, while
  `character_times_xi_norm_sq` is separately recomputed from the explicitly
  character-weighted coefficients.  `norm_sq == norm_sq` and copying one
  norm into both fields are forbidden.

The same principle applies to stored booleans and final status: the truth
value must follow from the recomputed witnesses and frozen predicate, not
from the expected token or current CSV cell.

## 8. Complete isolated mutation registry within 176 methods

No test method may be added, deleted, merged, renamed, or parametrically
hidden.  Discovery must remain exactly 176.  Existing methods must be
strengthened internally to apply isolated mutations to a fresh valid scratch
package and verify that each fails for its intended reason.

At minimum, isolated cases must cover separately:

1. new-CSV content, header, body-row count, and row order;
2. each owner and cardinality-credit class, including actual/bare/standard/
   discrete separation and Paper-2 zero-credit allocation;
3. maximal/reduced evidence tokens and their nonconflation;
4. stored hash/digest edges, including artifact, implementation,
   design-head, and v2 design-gate bindings;
5. a changed row `status` and an unconditional-status implementation probe;
6. `observed_detector`, `expected_detector`, fixture semantics, and violated-
   lock mismatches as distinct cases;
7. every summary field class: artifact identity, row count, column count,
   negative count, test-method count, the 117/41 self-summary, and the
   2665/67/176 package aggregate;
8. manifest self-entry/self-digest, concurrent proof binding, missing
   authority, and extra/missing manifest inventory;
9. verify-only byte and metadata writes; and
10. one preserved-v1-body drift.

Each mutation must start from a valid package, be observed to fail the exact
intended validator class, and be cleaned before the next case.  A single
generic byte mismatch is not evidence that every semantic mutation class was
exercised.

The strengthened static/in-memory probes must also demonstrate rejection of:

- nonsense or semantically altered fixture/lock inputs for every registered
  negative family;
- a wrong gauge phase rule that makes copied left/right values agree;
- one-side product/star/gauge witness corruption;
- copied or tautological norm equality;
- a drifted per-artifact summary with a stale package total; and
- a manually forced `PASS` status after a failed family predicate.

## 9. Determinism, reproduction, and manifest DAG

The repaired package must preserve exactly:

```text
CSV_ARTIFACTS=12
GENERATED_ARTIFACTS_INCLUDING_MANIFEST=13
V1_CSV_BODY_ROWS=2548
V2_NEW_CSV_BODY_ROWS=117
CSV_BODY_ROWS=2665
V1_EXPLICIT_NEGATIVE_ROWS=47
V2_NEW_EXPLICIT_NEGATIVE_ROWS=20
EXPLICIT_NEGATIVE_ROWS=67
EXPECTED_NEGATIVES_DETECTED=67
NEGATIVE_FAILURES=0
UNITTEST_METHODS=176
UNITTEST_FAILURES=0
UNITTEST_ERRORS=0
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
TOLERANCE_POLICY=EXACT_ZERO
```

Strict checked-in verify-only, two distinct fresh empty roots, three-way
13-artifact byte identity, external serialization, no retry, recursive-entry
rejection, cache checks, and exit-trap cleanup remain mandatory.  The
environment remains `LC_ALL=C`, `TZ=UTC`, `PYTHONHASHSEED=0`,
`PYTHONDONTWRITEBYTECODE=1`, and `python3 -B`.

The replacement manifest remains schema
`paper13-circle-twists-controls-manifest/2`, with the same 24 path-sorted
authority bindings and the same separate v2 design head.  It must bind the
six repaired implementation files and twelve regenerated CSVs by path, byte
count, and SHA-256, but must not bind itself.  Neither summary CSV contains a
self-digest, and no implementation file contains the replacement manifest
digest.

The proof block remains exactly:

```text
proof_binding = {
  concurrent_phase3_proof_hash_included: false,
  policy: POST_PROOF_AUDIT_BINDS_SEPARATELY
}
```

No proof path, byte count, digest, proof-derived oracle, non-null proof
sentinel, or key matching `proof.*sha` is permitted.  This remediation gate
and the controls review remain external audit inputs; inserting them into the
frozen 24-binding array is not authorized.  The stable controls package may
meet a stable proof only later as two separate inputs to an independently
authorized integrated audit.

## 10. Exact CSV-byte policy

The independent controls review established that all current stored CSV
values are correct.  Therefore the presumptive and expected remediation
outcome is:

```text
V2_CSV_BODY_BYTE_IDENTITY_REQUIRED=true
V1_CSV_BODY_BYTE_IDENTITY_DEFAULT=true
EXPECTED_UNCHANGED_CSV_HASHES=12/12
```

The repaired implementation must derive those same bytes independently.  It
may not edit a CSV by hand or change a row merely to make a new validator
pass.

For the eleven v1 contract bodies, the only conditional exception is a
formula-compelled correction to an already existing witness/evidence value
cell.  Such a correction is authorized only if all of these conditions hold:

1. two independently coded owner-side formulas agree on the replacement and
   show the old cell inconsistent with the frozen formula;
2. the change is limited to the affected existing witness/evidence field;
3. schema, header, row ID, row count, order, negative registry, oracle label,
   tolerance, expected predicate, boolean truth, and `status=PASS` meaning do
   not change;
4. no theorem, owner, credit, or evidence ceiling changes;
5. the author handoff reports exact file, row ID, field, old value, new value,
   both derivations, and resulting old/new file hashes; and
6. the independent controls audit adjudicates the change before accepting the
   package.

The current review supplies no known instance requiring this exception.
Consequently any v1 byte difference without the complete formula-compelled
receipt above is a failure.  If an independent formula changes an expected
truth value, boolean, status meaning, schema, row count, or registry, this
gate is insufficient: stop without the author top-level run and obtain a new
reviewed design amendment.

The v2 CSV and all non-evidence v1 cells remain byte-locked to the hashes in
Section 4.2.  Implementation hashes must change; the replacement manifest
hash must change accordingly even when all twelve CSV hashes remain stable.

## 11. Author handoff and fresh independent controls audit

After the one authorized author run completes, the author handoff must freeze:

- all six repaired implementation hashes and byte counts;
- all twelve regenerated CSV hashes, counts, widths, and negatives;
- the replacement manifest hash and its canonical 24-binding/design-head
  receipt;
- exact `2665/67/176`, zero failures/errors, verify-only immutability, two-
  fresh/three-way identity, no-cache, cleanup, and single-run receipts; and
- any conditional v1 evidence-cell delta receipt required by Section 10.

The first-run implementation and manifest hashes remain historical only and
cannot be relabelled as the repaired handoff.

After handoff, a fresh independent controls auditor must first run read-only
static and in-memory/scratch mutation probes covering Sections 6--8.  Those
probes may not import expected detector output as their oracle and may not
change checked-in bytes.  Only after all static probes pass may the auditor
consume exactly one separately serialized top-level reproduce.  The auditor
must independently verify the replacement hashes, complete mutation
registry, CSV byte policy, strict verify-only, two fresh roots, three-way
identity, no-cache/cleanup, and no-proof/no-self-hash DAG.

The fresh audit must return `C0/M0/m0` before the replacement manifest can
become stable downstream controls evidence.  This gate neither performs nor
pre-passes that audit.  A failed static probe prevents the auditor run; a
failed auditor run receives no automatic retry and requires a new gate.

## 12. Downstream stop and machine-readable receipt

No controls result may be interpreted while M1 remains open.  `NOTE_OR_MERGE`
remains binding, and proof, proof binding, source, Route, composition,
standalone, manuscript, citation, release, Git, and public synchronization
remain unauthorized.

```text
PHASE3_V2_CONTROL_REMEDIATION_GATE=PASS_TO_BOUNDED_REMEDIATION
VERSION=P13-CONTROL-ORACLE-REMEDIATION-v1
CONTROLS_REVIEW_SHA256=83465435fda898c213b5923e0f42e84833dae8bb08476f7a12453523dfe20d04
CONTROLS_FINDINGS=C0/M1/m0
CRITICAL_OPEN=0
MAJOR_OPEN=1
MINOR_OPEN=0
M1_CLOSED=false
FIRST_RUN_IMPLEMENTATION_GATE_SHA256=e3226570f6d9630d5a912cb6b189d194bd33df395e276ce56d48ad75f9601312
FIRST_RUN_MANIFEST_SHA256=52a6ea213fc7ebadbe26cc13716caf91c69c7adb829cec72434bea761b103e3d
FIRST_RUN_MANIFEST_DOWNSTREAM_EVIDENCE_VALID=false
REPLACEMENT_MANIFEST_REQUIRED=true
REPLACEMENT_MANIFEST_FROZEN=false
REMEDIATION_AUTHORIZED=true
AUTHORIZED_IMPLEMENTATION_PATHS=6
AUTHORIZED_CSV_REGENERATION=12
AUTHORIZED_MANIFEST_REGENERATION=1
AUTHOR_TOP_LEVEL_REPRODUCE_RUNS_AUTHORIZED=1
AUTHOR_TOP_LEVEL_REPRODUCE_CONSUMED=false
NEGATIVE_DETECTOR_SEMANTIC_DERIVATION_REQUIRED=true
POSITIVE_ORACLE_INDEPENDENT_FORMULAS_REQUIRED=true
FAMILY_AND_PACKAGE_SUMMARY_RECOMPUTATION_REQUIRED=true
COMPLETE_ISOLATED_MUTATION_REGISTRY_REQUIRED=true
V1_TAUTOLOGICAL_STAR_NORM_REPAIR_REQUIRED=true
CSV_ARTIFACTS=12
GENERATED_ARTIFACTS=13
CSV_BODY_ROWS=2665
EXPLICIT_NEGATIVES=67
UNITTEST_METHODS=176
V1_CSV_BODY_BYTE_IDENTITY_DEFAULT=true
V1_EVIDENCE_CELL_CHANGE_ONLY_IF_FORMULA_COMPELLED=true
V2_CSV_BODY_BYTE_IDENTITY_REQUIRED=true
MANIFEST_BINDINGS_ARRAY_COUNT=24
MANIFEST_DESIGN_HEAD_SEPARATE=true
MANIFEST_SELF_HASH_PRESENT=false
CONCURRENT_PROOF_HASH_INCLUDED=false
INDEPENDENT_STATIC_MUTATION_PROBES_REQUIRED=true
INDEPENDENT_AUDITOR_TOP_LEVEL_REPRODUCE_RUNS_REQUIRED=1
INDEPENDENT_CONTROLS_AUDIT_PASSED=false
CONTROL_RESULTS_INTERPRETATION_AUTHORIZED=false
PROOF_AUTHORIZED=false
PROOF_BINDING_AUTHORIZED=false
STANDALONE_PASS=false
NOTE_OR_MERGE_BINDING=true
ROUTE_A_AUTHORIZED=false
ROUTE_B_INVOCATION_ALLOWED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
CITATION_PACKAGE_AUTHORIZED=false
RELEASE_AUTHORIZED=false
GIT_AUTHORIZED=false
PUBLIC_SYNC_AUTHORIZED=false
```

This file does not embed its own digest.  Its SHA-256 is computed only after
the bytes are frozen and must be bound externally by the author handoff and
fresh independent controls audit.

**Final verdict: PASS TO ONE BOUNDED ORACLE REMEDIATION — C0/M1/m0 remains
open.  Only a fresh independent `C0/M0/m0` controls audit may close M1 and
replace the first-run manifest as downstream evidence.**
