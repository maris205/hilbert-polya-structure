# Paper 13 Phase-3 v2 exact-byte controls review

Date: **2026-08-15 (Asia/Shanghai)**  
Decision: **REVISE CONTROL IMPLEMENTATION BEFORE ANY NEW EXECUTION**  
Verdict: **C0 / M1 / m0**  
Review mode: independent exact-byte, source-semantic, and integrity audit  
Independent top-level reproduction consumed by this lane: **no**  
Files written by this lane: **this review only**  
`route_b_invocation_allowed: false`

## 1. Decision and exact boundary

The checked-in package has the exact designed CSV bytes, schemas, row order,
row counts, negative counts, and current manifest edges.  An independent
reconstruction matched all twelve CSVs byte for byte, including all eleven
amended-v1 bodies.  The manifest is canonical, every declared digest matches,
strict verify-only preserved bytes and metadata, and the current tree is free
of prohibited cache and task-temporary residue.

The package nevertheless does **not** pass the required independent controls
audit.  One Major integrity finding remains: several registered negative and
positive oracles are emitted by lookup, copied values, or tautological
self-comparison rather than by the independent construction and recomputation
required by the frozen designs.  The isolated v2 tamper method also does not
exercise the complete required mutation-class registry.  Read-only in-memory
mutation probes demonstrate that incorrect fixtures, a wrong gauge phase
rule, and inconsistent package-summary arithmetic can still receive `PASS`.

This is an implementation-integrity defect, not a discrepancy in the current
CSV values.  It prevents acceptance of the current `67/67` detector receipt
and the current source package as fail-closed controls.  No independent
top-level reproduce was run after this defect was established; spending that
single run on a known nonconforming implementation would not close the gate.

This review authorizes no repair.  A separate versioned repair authorization,
new stable implementation/result/manifest hashes, one newly serialized author
run, and a fresh independent controls audit are required.

## 2. Exact authority and implementation tuple

Every artifact in this section was read and rehashed from its current bytes.
All supplied digests match.

### 2.1 Frozen design lineage and external implementation gate

| Artifact | Verified SHA-256 | Receipt |
|---|---|---|
| `notes/phase3_v2_design_gate.md` | `0094462b1e06cde0cf1fcc3536c608dcd96ef1e9eb0d85a0714df1666b799706` | MATCH |
| `notes/phase3_control_design_lock.md` | `900c541713b1711bdab7fa0d264355b6d8ee27014094e60eac6aabe38190604c` | MATCH |
| `notes/phase3_control_design_amendment_v1.md` | `5c9caea983b0047c4b16d0437c23b117a6b8150bbeb67b79c60fb9b2ba6a737e` | MATCH |
| `notes/phase3_control_design_review.md` | `bf56b96e19b682600ed5de43f7df51ef381fe82d4e12363f66cd1e7d2a5a5184` | MATCH; effective append-only verdict is `PASS C0/M0/m0` |
| `notes/phase3_control_design_amendment_v2.md` | `0c0113cff7cf7853d2f4e90ab311ace347f0bebbd8bbf36ab38501fd279c54d9` | MATCH; manifest design head |
| `notes/phase3_control_design_v2_review.md` | `4385b74e81454ab699975a1c0f8217837ae1a7f90a6a220d47eecfdaaeca71c6` | MATCH; design review `PASS C0/M0/m0` |
| `notes/phase3_v2_control_implementation_gate.md` | `e3226570f6d9630d5a912cb6b189d194bd33df395e276ce56d48ad75f9601312` | MATCH; bound externally by this review, not inserted into the manifest |

The review read the historical v1 review through its appended amended-v1
closure.  Its prefix `C0/M1/m0` applies only to the unamended base; the frozen
complete digest above has the effective v1 design verdict `PASS C0/M0/m0`.

### 2.2 Six implementation files

| Implementation path | Bytes | Verified SHA-256 |
|---|---:|---|
| `code/README.md` | 693 | `680a4106b6d572c6104f437fda23da9eb4be1f5eb9165d250059645c08ce5044` |
| `code/generate_controls.py` | 68,218 | `2e01da8782e63081f2895f9f9b3ccba11b18a2494b7e631080f6cf5d7bdec31e` |
| `code/test_controls.py` | 35,336 | `d81fcfd9e6a379ae421087fce613b627f90217e6d99838261c8886c6f05cf2b1` |
| `experiments/README.md` | 512 | `bd0b6a34beec217b525df0fbedbc78a166baa93cb2ad0ec40e7c6fc02ebb6a0b` |
| `experiments/reproduce.sh` | 3,913 | `56e15fc0d625ba78f96197294fed9ac7aff593717af9e338a55722b86dc250ca` |
| `results/README.md` | 532 | `aa240a9776b276e3dd196514084d1c3f1d6a7e8dc4922be89ba02c6bb7e9ff3b` |

The controlled `code/` and `experiments/` inventories contain exactly these
authorized implementation paths.  All are regular files; no symlink or extra
implementation path was found.

## 3. Exact generated-artifact receipt

The twelve CSV entries and the manifest rehash as follows.

| Artifact | Rows | Columns | Negatives | Bytes | Verified SHA-256 |
|---|---:|---:|---:|---:|---|
| `nerve_factorization_controls.csv` | 280 | 17 | 0 | 42,284 | `a00d2d6439aee3022703940b36892136ef7083d49541d2d8ad3bfd994a7582ba` |
| `circle_multiplier_cocycle_controls.csv` | 500 | 20 | 0 | 61,642 | `21a5246dba9dbe573a56fa9a0c18399061ff3e09d0238f68213123f3fa77e0a7` |
| `lift_integer_defect_controls.csv` | 500 | 20 | 0 | 58,121 | `598d414e46a7d34d1ab6a70b0047967047d984f24a3443aa19224a14a12da5b8` |
| `gauge_coboundary_controls.csv` | 196 | 19 | 0 | 28,580 | `c8717d8748691e92e8a7ea7ec1a196a5f42d5e151ee6e51244e2875f59677f26` |
| `twisted_convolution_controls.csv` | 78 | 23 | 0 | 11,271 | `2874817f2af1d3da31a29f497eba770eeac9c7275e6cc8693a7fa468fb482add` |
| `twisted_involution_controls.csv` | 54 | 26 | 0 | 7,829 | `114228b425905d5e235576b34f57eb15a0fd987065d4d206726045cceee569b5` |
| `completion_gauge_controls.csv` | 756 | 28 | 0 | 143,905 | `e7b8253a7d501b0c7b1d81939b59bfdc2f441b20592c678f749e643c0b800b2a` |
| `action_period_nonretention_controls.csv` | 56 | 20 | 0 | 22,249 | `9361f555cec4f74cab12faf30595e74830a00b44d7890e43579eae81ddcc9ee1` |
| `negative_domain_controls.csv` | 20 | 12 | 20 | 5,520 | `82b9e5988b30a8212235558af98a787df823213a7b0ad82be7d080da7c84c123` |
| `actual_standard_support_transfer_controls.csv` | 96 | 21 | 27 | 21,768 | `7bfb8ca2ed176d1a7aca2e5aa3680fd2d3992ef1d8e86a79b22c971912051176` |
| `target_summary.csv` | 12 | 11 | 0 | 2,416 | `97c2052c6286dd2013f735a79e7331d7a29f2bba7b2575fdc226865a34528f60` |
| `completion_corona_controls_v2.csv` | 117 | 41 | 20 | 45,092 | `672a29d4ac1b220336527517e50ba855f6a0c93568effd9b97e792015e4b2c41` |
| `manifest.json` | -- | -- | -- | 9,790 | `52a6ea213fc7ebadbe26cc13716caf91c69c7adb829cec72434bea761b103e3d` |

The current results inventory is exactly twelve CSVs, `manifest.json`, and
the authorized non-generated `README.md`.  There is no extra generated file
or directory.

## 4. Independent byte, schema, family, and arithmetic audit

The CSV audit did not import the implementation's generator tables.  It
independently reconstructed the headers, canonical enumeration, exact phase
and Gaussian-integer arithmetic, AP predicates, ND/ST literal tables,
amended-v1 summary, all eight v2 families, and canonical CSV serialization.

The result was:

```text
CSV_BYTE_RECONSTRUCTION=12/12_MATCH
V1_CSV_BYTE_RECONSTRUCTION=11/11_MATCH
V1_BODY_ROWS_EXACT=2548
CSV_BODY_ROWS=2665
EXPLICIT_NEGATIVES=67
V2_SUMMARY_RECOMPUTED=2665/67/176
```

The v2 41-column file has contiguous IDs `V2-0001`--`V2-0117` and the exact
family partition:

| Family | Rows | Row kind |
|---|---:|---|
| `FINITE_C0_MODEL` | 18 | `DIAGNOSTIC` |
| `INFINITE_ANALYTIC_BOUNDARY` | 18 | `DIAGNOSTIC` |
| `FINITE_TAIL_QUOTIENT_MODEL` | 12 | `DIAGNOSTIC` |
| `GAUGE_COMMUTATION_MODEL` | 24 | `DIAGNOSTIC` |
| `OWNER_CREDIT_LEDGER` | 8 | `DIAGNOSTIC` |
| `MAX_REDUCED_EVIDENCE_LEDGER` | 4 | `DIAGNOSTIC` |
| `FIREWALL_NEGATIVE` | 20 | `NEGATIVE` |
| `V2_PACKAGE_SUMMARY` | 13 | `SUMMARY` |
| **Total** | **117** | `84 DIAGNOSTIC / 20 NEGATIVE / 13 SUMMARY` |

Independent value recomputation found the current stored values correct:

- finite scalar rows have the exact zero/unit/`i` norm classes and finite
  zero-corona branch;
- infinite rows preserve the zero/nonzero `c0` split, quotient distance,
  injective analytic branch, and unconditional fixed-prime owner tokens;
- finite-tail rows have the exact positive-tail quotient distances and do
  not claim an actual multiplier corona;
- all 24 gauge rows have the correct independently recomputed exponents and
  frozen `SIGMA_OVERLINE_TAU_EQ_DELTA_ALPHA` orientation;
- all eight owner/credit rows preserve Paper-2 credit and the
  actual/bare/standard/discrete firewalls;
- all four max/reduced rows retain separate non-proof evidence tokens;
- the twenty v2 negative rows and the thirteen v2 summary rows match their
  frozen literal registries; and
- the immutable v1 `target_summary.csv` remains the `2548/47/128` snapshot,
  while the v2 summary alone records `2665/67/176`.

The test module currently exposes exactly 176 callable `test_*` methods, and
standard `unittest` discovery also counts exactly 176.  This method-count
receipt does not cure the oracle-independence defect in Section 7.

## 5. Manifest-v2 and dependency-DAG audit

`manifest.json` is byte-canonical under
`json.dumps(ensure_ascii=False, sort_keys=True, indent=2) + "\n"`.  It has
schema `paper13-circle-twists-controls-manifest/2`, package ID
`paper13-circle-twists-controls-v2`, the exact separately typed design head,
and a path-sorted 24-entry `bindings` array.

Every one of the 24 binding paths rehashes to its stored digest.  The twelve
base paths and twelve v2 paths are disjoint.  The design-head path is not
miscounted as a twenty-fifth binding.  The manifest binds six implementation
files path-sorted and twelve CSVs in canonical artifact order, each by byte
count and SHA-256.

The proof block is exactly:

```text
proof_binding = {
  concurrent_phase3_proof_hash_included: false,
  policy: POST_PROOF_AUDIT_BINDS_SEPARATELY
}
```

No proof path, proof digest, non-null proof sentinel, proof-derived oracle,
manifest self-entry, or manifest self-digest is present.  Neither summary CSV
contains a self-digest.  None of the six implementation files contains the
current manifest digest.  The implementation gate is correctly external to
the manifest and is bound by this review at its frozen digest.

Thus the current byte graph is acyclic:

```text
24 frozen authorities + separate v2 design head
                       -> six implementation files
                       -> twelve CSV artifacts
                       -> manifest.json

stable proof ------------------+
stable controls manifest ------+-> later independent integrated audit
```

This DAG receipt passes and is not the source of M1.

## 6. Verify-only, serialization, run handoff, and residue receipt

A separate read-only invocation of the implementation's verify path was
wrapped in independent before/after receipts over relative path, file type,
mode, size, nanosecond modification time, and SHA-256.  The receipts were
identical:

```text
VERIFY_ONLY_BYTES_METADATA_IMMUTABLE=true
```

The current controlled roots contain zero `__pycache__`, `*.pyc`, `*.pyo`,
`.pytest_cache`, or `.mypy_cache` entries.  No author fresh-A or fresh-B root
remains under the task temporary parent.  Current inventory, canonical LF,
UTF-8-without-BOM, and exact-zero tolerance checks pass.

The stable author handoff reported one serialized top-level run with exit
zero, `TOP_LEVEL_RUNS=1`, `176/176` tests, two fresh generations, three-way
identity of thirteen artifacts, `67/67` registered negative rows, no cache,
and cleanup.  This review records that handoff but does not elevate it over
the source-semantic counterexamples below.  The independent audit lane did
not start its reserved top-level reproduce.

## 7. M1 — registered oracles and tamper gates are not independently fail-closed

**Severity:** Major.  
**Locations:** `code/generate_controls.py` lines 398--403, 431--433,
640--705, 739--802, and 822--849; `code/test_controls.py` lines 330--403 and
577--591.  
**Violated authority:** amended-v1 Sections 3--4; v2 design Sections 4, 5,
7, 8, 10, and 12; implementation-gate Sections 4, 5, 7, and 8.

### 7.1 Negative detectors accept unrelated fixtures and locks

The v2 detector parses only enough to establish that a fixture and lock are
nonempty.  For the three manifest reasons, it constructs a mutation selected
by `reason`, not by the parsed fixture.  It then returns a second literal
`reason -> detector` table for all twenty rows.  The other seventeen reasons
perform no semantic fixture/lock check at all.  This is the prohibited
expected-token oracle in another table.

A read-only in-memory probe replaced every v2 fixture with `X=Y` and every
violated lock with `WRONG_LOCK`.  All twenty still returned their registered
expected detector:

```text
V2_NONSENSE_FIXTURE_LOCK_ACCEPTED=20/20
```

The analogous probe also passed 8/20 v1 policy rows, namely the dense-H,
heterogeneous, reverse-J, finite-as-infinite, fixed-prime-cardinality,
owner-framework, control-as-proof, and concurrent-proof-binding rows:

```text
V1_NONSENSE_FIXTURE_LOCK_ACCEPTED=8/20
```

Consequently the generator has not established that the frozen attempted
promotion was constructed and rejected.  It has established only that a
reason label indexes the expected output token.  The current claim
`EXPECTED_NEGATIVES_DETECTED=67` is therefore not an independently supported
control receipt even though the 67 rows themselves are byte-correct.

### 7.2 Positive v2 status and package arithmetic can pass invalid values

The local v2 `add` helper assigns `status=PASS` unconditionally.  The scalar
input table stores the norm and norm class without storing and independently
measuring the required `(re,im)` scalar.  The gauge block computes one
`exp` value and copies it into both left and right fields.  The package row is
the literal tuple `2665/MIXED/67/176`, not a recomputation from the preceding
twelve summary rows and actual test discovery.  The generic row validator
then checks only schema, count, stored `PASS`, IDs, tolerance, negative
presence, and field whitespace; it does not recompute family oracles.

Two read-only in-memory probes make the gap concrete:

1. Replacing the gauge phase helper with the incorrect constant rule
   `alpha_exp(k,t)=7` produced 24 gauge rows with `(lhs,rhs)=(7,7)`.  All
   24 retained `PASS`, and the generic row validator accepted the file.
2. Drifting the first artifact summary from 280 to 281 left the package row
   at `2665` with `status=PASS`; the generic row validator again accepted it.

The exact receipts were:

```text
WRONG_PHASE_RULE_GAUGE_ROWS_PASS=24/24
WRONG_PHASE_RULE_DISTINCT_PHASES=[('7', '7')]
DRIFTED_ARTIFACT_SUMMARY_FIRST_ROWS=281
UNRECOMPUTED_PACKAGE_TOTAL_STILL=2665
DRIFTED_SUMMARY_STATUS=PASS
```

Two inherited v1 surfaces show the same pattern.  The actual and time star
fields are computed by the same function call before comparison, and the
character-isometry predicate is the tautology `norm_sq == norm_sq`, with the
same value copied into both norm fields.  The current stored rows are correct,
but these code paths do not supply the two independently derived witnesses
required by the design.

### 7.3 The isolated v2 tamper method does not cover the frozen registry

The twelve inherited tamper methods mutate content/header/count/order in four
different v1 CSVs, package inventory, one artifact digest, one arbitrary
binding digest, one implementation byte count, and one proof block.  The
single new v2 tamper method performs only one replacement of the first
`UNCONDITIONAL_FIXED_PRIME` substring.

It does not separately construct and reject the frozen new-CSV header, row
count, row order, owner token, evidence token, negative detector, and package-
summary drifts.  It also does not exercise design-head and v2-gate drift as
package tamper cases.  Strict expected-byte comparison would reject those
mutations if presented, but the required isolated failure suite does not
present them.  The implementation gate requires execution of the complete
class registry, not only the existence of a validator that should reject an
untested byte mismatch.

### 7.4 Consequence

M1 does not allege a false current mathematical value, proof claim, digest,
row, or count.  It establishes that the implementation and its 176-method
suite do not meet the frozen independent-oracle and failure-injection
contract.  Because the authorization is explicitly voided by weakening a
frozen failure gate, the controls cannot be accepted as a stable evidence
package on the current implementation and manifest digests.

## 8. Minimal fail-closed repair contract

Any later repair must remain separately authorized and must satisfy all of
the following without changing the frozen mathematical/evidence ceiling:

1. Replace reason-to-detector lookup with a detector for each registered row
   that parses the exact fixture grammar and exact violated-lock token,
   constructs the attempted algebraic, owner, credit, framework, or manifest
   promotion, and derives the observed detector from the resulting failed
   predicate.  A malformed, semantically altered, or reason/fixture/lock-
   mismatched row must fail generation rather than receive a detector.
2. Make the three manifest-negative mutations arise from their parsed fixture
   instructions, not from the reason label.  Recursively validate the exact
   no-proof/no-self/no-unbound-authority policy after mutation.
3. Add a separate v2 family validator invoked before serialization.  It must
   recompute scalar norms from exact Gaussian pairs; finite/infinite
   membership and quotient predicates from the closed owner/input tables;
   finite-tail distance from the explicit `(m,n)` model; gauge left and right
   exponents by independent expressions parsed from `k`, `t`, `tau`, and the
   orientation; owner/evidence rows against closed literal registries; and
   the package row from the twelve preceding summaries plus actual unittest
   discovery.  `status=PASS` may be emitted only after those checks succeed.
4. Replace the inherited star and character-isometry self-comparisons with
   independently implemented actual/time formulas and an explicit
   character-weighted norm sum.  The eleven v1 CSVs must remain byte-identical
   to the exact current v1 bytes.
5. Strengthen the existing test methods, without adding, deleting, merging,
   renaming, or hiding a discoverable method, so discovery remains exactly
   176.  Each registered negative must receive both its exact-fixture success
   probe and at least one malformed or semantically changed fixture/lock
   rejection probe.
6. Expand the existing v2 tamper method internally to run isolated scratch-
   package mutations for new-CSV content, header, count, order, owner,
   evidence, detector, and package-summary drift; design-head and v2-gate
   drift; manifest self-entry; proof binding; verify-only byte/metadata write;
   and v1-body drift.  Every mutation must be observed to fail for the
   intended class, and scratch cleanup must be checked after each case.
7. Preserve strict verify-only, two fresh empty roots, three-copy equality,
   no retry, recursive/concurrent entry rejection, no-cache checks, and exit-
   trap cleanup.  The twelve CSV hashes should remain unchanged if only oracle
   implementation is repaired; the implementation hashes and therefore the
   manifest hash must change and be frozen anew.
8. After a separate repair authorization, perform exactly one newly
   serialized author top-level run, release its reservation, and hand off the
   new implementation/result/manifest hashes.  A fresh independent controls
   audit must then perform its own serialized reproduce before any downstream
   gate consumes the package.

No proof, proof binding, source, Route, composition, manuscript, citation,
standalone, release, Git, or public-synchronization work is part of this
repair contract.

## 9. Severity register and downstream consequence

| Severity | Count | Open item |
|---|---:|---|
| Critical (`C`) | 0 | none |
| Major (`M`) | 1 | M1: oracle/detector independence and complete isolated-tamper execution are not fail-closed |
| Minor (`m`) | 0 | none |

```text
P13_V2_CONTROLS_REVIEW=REVISE
FINDINGS=C0/M1/m0
V2_DESIGN_GATE_SHA256=0094462b1e06cde0cf1fcc3536c608dcd96ef1e9eb0d85a0714df1666b799706
BASE_V1_DESIGN_SHA256=900c541713b1711bdab7fa0d264355b6d8ee27014094e60eac6aabe38190604c
V1_DESIGN_AMENDMENT_SHA256=5c9caea983b0047c4b16d0437c23b117a6b8150bbeb67b79c60fb9b2ba6a737e
FINAL_V1_DESIGN_REVIEW_SHA256=bf56b96e19b682600ed5de43f7df51ef381fe82d4e12363f66cd1e7d2a5a5184
V2_DESIGN_SHA256=0c0113cff7cf7853d2f4e90ab311ace347f0bebbd8bbf36ab38501fd279c54d9
V2_DESIGN_REVIEW_SHA256=4385b74e81454ab699975a1c0f8217837ae1a7f90a6a220d47eecfdaaeca71c6
IMPLEMENTATION_GATE_SHA256=e3226570f6d9630d5a912cb6b189d194bd33df395e276ce56d48ad75f9601312
GENERATOR_SHA256=2e01da8782e63081f2895f9f9b3ccba11b18a2494b7e631080f6cf5d7bdec31e
TESTS_SHA256=d81fcfd9e6a379ae421087fce613b627f90217e6d99838261c8886c6f05cf2b1
REPRODUCE_SHA256=56e15fc0d625ba78f96197294fed9ac7aff593717af9e338a55722b86dc250ca
MANIFEST_SHA256=52a6ea213fc7ebadbe26cc13716caf91c69c7adb829cec72434bea761b103e3d
INPUT_HASHES_MATCH=true
CSV_ARTIFACTS_RECOMPUTED=12
GENERATED_ARTIFACTS_RECOMPUTED=13
V1_CSV_BODIES_BYTE_IDENTICAL=true
V1_CSV_BODY_ROWS_RECOMPUTED=2548
V2_NEW_CSV_BODY_ROWS_RECOMPUTED=117
CSV_BODY_ROWS_RECOMPUTED=2665
EXPLICIT_NEGATIVES_RECOMPUTED=67
UNITTEST_METHODS_DISCOVERED=176
CURRENT_CSV_BYTES_MATCH_DESIGN=true
MANIFEST_BINDINGS_ARRAY_COUNT=24
MANIFEST_DESIGN_HEAD_SEPARATE=true
MANIFEST_SELF_HASH_PRESENT=false
CONCURRENT_PROOF_DIGEST_PRESENT=false
VERIFY_ONLY_BYTES_METADATA_IMMUTABLE=true
PROHIBITED_CACHE_ENTRIES=0
TASK_TEMP_RESIDUE=0
INDEPENDENT_TOP_LEVEL_REPRODUCE_CONSUMED=false
NEGATIVE_DETECTOR_INDEPENDENCE_PASSED=false
POSITIVE_ORACLE_INDEPENDENCE_PASSED=false
COMPLETE_ISOLATED_TAMPER_REGISTRY_EXECUTED=false
INDEPENDENT_CONTROLS_AUDIT_PASSED=false
CONTROL_RESULTS_INTERPRETATION_AUTHORIZED=false
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
CRITICAL_OPEN=0
MAJOR_OPEN=1
MINOR_OPEN=0
```

**Final verdict: REVISE — C0/M1/m0.**  The current twelve CSVs and manifest
have exact designed bytes and a correct acyclic binding graph, but the source
does not independently establish the stored detector/oracle `PASS` values or
execute the complete frozen tamper registry.  Every downstream gate remains
closed pending a separately authorized repair, new frozen run tuple, and a
fresh zero-finding independent controls audit.

This review does not embed its own digest.  Its SHA-256 is computed only after
the bytes are frozen and is carried externally.

# Addendum A — oracle-remediation closure

Date: **2026-08-15 (Asia/Shanghai)**  
Addendum version: **P13-CONTROL-ORACLE-REMEDIATION-CLOSURE-v1**  
Effective decision for the replacement tuple: **PASS**  
Effective verdict: **C0 / M0 / m0**  
Independent top-level reproduction consumed by this lane: **yes, exactly one**  
Files written by this lane: **this append-only controls review only**  
`route_b_invocation_allowed: false`

## A1. Prefix preservation and scope

This addendum closes the one Major finding recorded above for a separately
authorized, separately hashed replacement implementation.  It does not
rewrite or reinterpret the historical finding.  Immediately before this
append, the complete original review prefix rehashed exactly as follows:

```text
ORIGINAL_REVIEW_PREFIX_SHA256=83465435fda898c213b5923e0f42e84833dae8bb08476f7a12453523dfe20d04
ORIGINAL_REVIEW_PREFIX_BYTES=22768
ORIGINAL_REVIEW_PREFIX_LINES=442
ORIGINAL_REVIEW_PREFIX_TERMINAL_LF=true
```

The prefix verdict `REVISE C0/M1/m0` remains the correct historical verdict
for generator `2e01da...`, tests `d81fcf...`, runner `56e15f...`, and manifest
`52a6ea...`.  The effective verdict of the complete review is now `PASS
C0/M0/m0` only for the replacement tuple frozen below.  The first-run
manifest is not revived or relabelled as acceptable downstream evidence.

The closure audit remained within the bounded controls authorization.  It
did not edit any implementation, generated artifact, authority, proof,
Route, composition, manuscript, citation, standalone, release, Git, or
public-synchronization file.

## A2. Exact replacement authority and implementation tuple

The replacement is externally governed by the same frozen design lineage,
the historical implementation gate, and the new remediation gate.  Every
entry below was read in full where applicable and rehashed from its stable
bytes.

| Authority | Bytes | Verified SHA-256 | Role |
|---|---:|---|---|
| `notes/phase3_v2_design_gate.md` | 13,957 | `0094462b1e06cde0cf1fcc3536c608dcd96ef1e9eb0d85a0714df1666b799706` | original v2 design gate |
| `notes/phase3_control_design_lock.md` | 34,870 | `900c541713b1711bdab7fa0d264355b6d8ee27014094e60eac6aabe38190604c` | base v1 design |
| `notes/phase3_control_design_amendment_v1.md` | 22,269 | `5c9caea983b0047c4b16d0437c23b117a6b8150bbeb67b79c60fb9b2ba6a737e` | v1 amendment |
| `notes/phase3_control_design_review.md` | 26,900 | `bf56b96e19b682600ed5de43f7df51ef381fe82d4e12363f66cd1e7d2a5a5184` | effective v1 design review |
| `notes/phase3_control_design_amendment_v2.md` | 43,727 | `0c0113cff7cf7853d2f4e90ab311ace347f0bebbd8bbf36ab38501fd279c54d9` | manifest design head |
| `notes/phase3_control_design_v2_review.md` | 29,126 | `4385b74e81454ab699975a1c0f8217837ae1a7f90a6a220d47eecfdaaeca71c6` | v2 design review |
| `notes/phase3_v2_control_implementation_gate.md` | 17,410 | `e3226570f6d9630d5a912cb6b189d194bd33df395e276ce56d48ad75f9601312` | historical implementation authorization |
| `notes/phase3_v2_control_remediation_gate.md` | 25,363 | `1ffba02ae468f7f847146a82a51c2e221aa25a64e65330cddd27504c2a971a42` | bounded remediation and fresh-audit authorization |

The repaired implementation receipt is:

| Implementation path | Bytes | Verified SHA-256 |
|---|---:|---|
| `code/README.md` | 1,082 | `fa18564c8aa001cc8e287a8d0520f8696499f2658083bef3c7ee029361df954b` |
| `code/generate_controls.py` | 126,247 | `8eabcc08426d16a2b12784fb060c7aa55214e544957098488b6deee138577829` |
| `code/test_controls.py` | 66,161 | `64d031244d112ff93c518c2e6d1df84d198b8051ab5ba462dfcdf057c1f61aaf` |
| `experiments/README.md` | 745 | `3e014b0c997d62c7cf9eea30a436033cd8a49982a7bb342e23b08ddb58042ade` |
| `experiments/reproduce.sh` | 4,108 | `a1013af1ad852d30ce0f67aba8c9421118181c5612cc95de228199fa3d3fbdcd` |
| `results/README.md` | 660 | `99d4a3bd2a71374157b63458fbe21df3f32745da1935b82ef55aceaf86f6074c` |
| `results/manifest.json` | 9,792 | `26a41e2920d9a3743cc1b681aa1e32d601dc12e5fded15b3c6349840bd9094c2` |

The six implementation records and twelve artifact records in the
replacement manifest match these files by path, byte count, and SHA-256.
The manifest is canonical sorted-key JSON and has schema
`paper13-circle-twists-controls-manifest/2`.

## A3. Static and in-memory fail-closed probes

All read-only preflight probes were performed before the independent runner
reservation was requested.  `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`
were active; the checked-in result receipt and implementation metadata were
identical before and after, with zero cache or task-temporary residue.

The implementation's write-free static entry point returned:

```text
STATIC_MUTATION_PRECHECK=PASS
LOCKED_CSV_HASHES=12/12
UNITTEST_METHODS=176
STATIC_PRECHECK_RECEIPT_IMMUTABLE=true
STATIC_PRECHECK_IMPLEMENTATION_IMMUTABLE=true
STATIC_PRECHECK_CACHE_DELTA=0
```

An additional audit harness used the checked-in artifact rows as the frozen
positive receipts and independently attacked the parser/validator surfaces.
Its exact receipt was:

```text
INDEPENDENT_EXACT_NEGATIVE_FIXTURES=40/40
INDEPENDENT_NEGATIVE_EXPLOIT_REJECTIONS=200/200
INDEPENDENT_SUPPORT_NEGATIVE_MUTATIONS=108/108
INDEPENDENT_POSITIVE_ORACLE_MUTATIONS=14/14
INDEPENDENT_MANIFEST_MUTATIONS=14/14
INDEPENDENT_TOTAL_EXPECTED_REJECTIONS=336
IN_MEMORY_PROBE_RECEIPT_IMMUTABLE=true
IN_MEMORY_EXPLOIT_PREFLIGHT=PASS
```

For each of the 20 v1 and 20 v2 detector rows, the exact fixture produced
the frozen detector.  Five attacks per row were then rejected separately:
the original `X=Y`/`WRONG_LOCK` exploit, a semantic value change, malformed
grammar, a wrong violated-lock token, and a rotated reason token.  The 27
support-transfer negatives each rejected four isolated owner/class/support/
status mutations.  Thus a reason label, expected detector, or current CSV
cell no longer selects a successful detector by itself.

The positive-oracle probes separately rejected left- and right-product
witness corruption, actual- and time-owner star corruption, one-sided and
copied norm witnesses, one-sided and copied gauge witnesses, a shared wrong
gauge phase rule, a stale per-artifact summary with unchanged package total,
and a manually forced `PASS` after a failed finite-family predicate.  Patching
the unrelated v1 `alpha_exp` path did not change any v2 gauge row.  Source
inspection also established distinct actual/time star functions, distinct
gauge-left/gauge-right functions, explicit character-weighted coefficients,
and blank v2 status during construction; the family validator alone finalizes
`PASS` after full recomputation.

The manifest probes separately rejected artifact, implementation,
design-head, design-gate, proof, self-digest, self-artifact, missing-authority,
extra/missing inventory, and proof-derived-oracle mutations.  The three v2
manifest-negative fixtures are parsed as mutation instructions and evaluated
against the recursive firewall rather than mapped from their reason labels.

## A4. Exact CSV, schema, family, and manifest receipt

All twelve CSV SHA-256 values remain byte-for-byte identical to the exact
values frozen in Section 3 of the preserved prefix.  No formula-compelled v1
evidence-cell exception was used.  The post-remediation recomputation is:

```text
CSV_HASHES_EXACT=12/12
V1_CSV_BODIES_BYTE_IDENTICAL=true
CSV_ARTIFACTS=12
GENERATED_ARTIFACTS_INCLUDING_MANIFEST=13
V1_CSV_BODY_ROWS=2548
V2_NEW_CSV_BODY_ROWS=117
CSV_BODY_ROWS=2665
V1_EXPLICIT_NEGATIVE_ROWS=47
V2_NEW_EXPLICIT_NEGATIVE_ROWS=20
EXPLICIT_NEGATIVE_ROWS=67
UNITTEST_METHODS_DISCOVERED=176
V2_SCHEMA_COLUMNS=41
V2_SUMMARY_RECOMPUTED=13/13
```

The v2 family, kind, and oracle partitions were independently parsed from
the 117 checked-in rows and then accepted by the repaired family validator:

| Family | Rows | Kind | Exact oracle |
|---|---:|---|---|
| `FINITE_C0_MODEL` | 18 | `DIAGNOSTIC` | `FINITE_C0_CONSTANT_COORDINATE_MODEL` |
| `INFINITE_ANALYTIC_BOUNDARY` | 18 | `DIAGNOSTIC` | `INFINITE_CONSTANT_NORM_C0_CORONA_BRANCH` |
| `FINITE_TAIL_QUOTIENT_MODEL` | 12 | `DIAGNOSTIC` | `FINITE_TAIL_SUP_QUOTIENT_DISTANCE` |
| `GAUGE_COMMUTATION_MODEL` | 24 | `DIAGNOSTIC` | `FROZEN_COMPONENT_DIAGONAL_GAUGE_TERM` |
| `OWNER_CREDIT_LEDGER` | 8 | `DIAGNOSTIC` | `OWNER_CREDIT_TOPOLOGY_EXACT_TOKEN` |
| `MAX_REDUCED_EVIDENCE_LEDGER` | 4 | `DIAGNOSTIC` | `MAX_REDUCED_EVIDENCE_SEPARATION` |
| `FIREWALL_NEGATIVE` | 20 | `NEGATIVE` | `EXPECTED_DETECTOR_TOKEN` |
| `V2_PACKAGE_SUMMARY` | 13 | `SUMMARY` | `V2_COUNT_SCHEMA_NEGATIVE_TOTAL` |

The kind totals are exactly `84 DIAGNOSTIC / 20 NEGATIVE / 13 SUMMARY`.
Each of the twelve artifact-summary rows independently matches its parsed
row count, 41-or-v1 column count, and negative count; the package row is
exactly `2665 / 67 / 176`.

The replacement manifest has exactly 24 unique path-sorted authority
bindings, six path-sorted implementation records, twelve canonical-order
artifact records, and one separate v2 design head.  All 43 external edge
hashes match.  The manifest binds neither itself, this review, nor the
remediation gate.  Its proof block remains exactly:

```text
proof_binding = {
  concurrent_phase3_proof_hash_included: false,
  policy: POST_PROOF_AUDIT_BINDS_SEPARATELY
}
```

No manifest-self digest appears in the manifest, summaries, or six
implementation files.  No concurrent Paper-13 proof path, proof byte count,
proof digest, proof-derived oracle, or non-null proof sentinel appears.  The
binding graph is acyclic, and the remediation gate plus this review remain
external audit inputs as required.

An independent direct strict `--verify-only` invocation passed before the
top-level run.  A receipt including bytes, modes, mtimes, inodes, and hashes
was identical before and after:

```text
VERIFY_ONLY_BYTES_METADATA_IMMUTABLE=true
PROHIBITED_CACHE_ENTRIES=0
TASK_TEMP_RESIDUE=0
```

## A5. Serialized author and independent reproduction receipts

The author handoff froze one successful no-retry top-level run, released its
reservation, and reported `176/176`, two fresh generations, three-copy
identity for all thirteen generated artifacts, strict verify-only, exact
`2665/67`, cleanup, and no cache or process residue.  The handoff hashes
matched the stable bytes rehashed in Section A2.

Only after every independent preflight probe above passed did this audit ask
for and receive an exclusive Paper-13 runner reservation.  No other lane was
authorized to run generator, tests, or reproduction during the reservation.
The audit then invoked `experiments/reproduce.sh` exactly once, with no retry.
It exited `0` and returned:

```text
P13_CONTROL_RUN_RESERVATION=ACQUIRED
TOP_LEVEL_RUNS=1
VERIFY_ONLY_IMMUTABLE=true
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
BYTE_IDENTICAL_ARTIFACTS=13
Ran 176 tests in 17.777s
UNITTEST_METHODS=176
UNITTEST_FAILURES=0
UNITTEST_ERRORS=0
CSV_ARTIFACTS=12
GENERATED_ARTIFACTS_INCLUDING_MANIFEST=13
CSV_BODY_ROWS=2665
EXPLICIT_NEGATIVE_ROWS=67
EXPECTED_NEGATIVES_DETECTED=67
NEGATIVE_FAILURES=0
TOLERANCE_POLICY=EXACT_ZERO
PROHIBITED_CACHE_ENTRIES=0
PROCESS_CHILDREN_REAPED=true
P13_CONTROL_REPRODUCTION=PASS
TEMP_ROOTS_REMOVED=2
TASK_TEMP_RESIDUE=0
```

The 176-method run executed the expanded isolated scratch mutation registry,
including v2 content/header/count/order, each owner/credit and evidence
class, status, all five negative fields, every summary-field class, artifact/
implementation/design/gate edges, self/proof/inventory cases, verify-only
byte and metadata writes, and preserved-v1-body drift.  All tests passed.

After exit, the replacement manifest and all six implementation files
rehash-matched `7/7`, the CSVs rehash-matched `12/12`, and the original review
prefix still matched its exact digest, byte count, and line count.  The
independent post-run scan found zero prohibited cache entries, zero A/B temp
roots, zero `.test-scratch` residue, and zero relevant runner/generator/test
processes.  The external reservation was then explicitly released.

## A6. M1 closure determination

The original M1 had three coupled surfaces.  Each is now closed for the
replacement tuple:

1. **Negative detector independence — closed.**  Exact fixture grammars are
   parsed and used to construct the attempted violation.  Reason, lock, and
   detector are derived outputs, and mismatched or malformed inputs fail
   closed.  The original nonsense-fixture exploit is rejected for every v1
   and v2 detector row.
2. **Positive oracle independence — closed.**  Product parenthesizations,
   actual/time stars, gauge sides, and unweighted/character-weighted norms
   use separate formula paths.  The v2 validator independently reconstructs
   scalar, membership, quotient, owner, evidence, family, kind, artifact,
   self-summary, and package-summary predicates before final status.
3. **Complete isolated tamper execution — closed.**  The discoverable method
   count remains exactly 176, while the strengthened methods execute every
   remediation-gate mutation class against isolated valid scratch packages.
   The serialized independent run observed all 176 methods pass and cleanup
   complete.

No current mathematical cell, owner token, evidence ceiling, schema, row ID,
row order, row count, negative registry, or CSV digest changed in order to
obtain closure.  The repair changes only the implementation integrity and its
replacement manifest edges.  Therefore original finding **M1 is closed**;
there is no remaining Critical, Major, or Minor controls finding.

## A7. Effective severity and downstream boundary

| Severity | Open | Closure result |
|---|---:|---|
| Critical (`C`) | 0 | none raised |
| Major (`M`) | 0 | original M1 closed for the replacement tuple |
| Minor (`m`) | 0 | none raised |

The replacement manifest is now stable exact-byte controls evidence within
the frozen finite-diagnostic and policy-ledger ceiling.  This audit does not
turn finite controls into proof evidence for continuum cardinality,
arbitrary-index multiplier identities, completion norm chains, or corona
faithfulness.  It authorizes no proof edit or proof binding, source work,
Route A or B, composition, standalone claim, manuscript, citation package,
release, Git operation, or public synchronization.  `NOTE_OR_MERGE` remains
binding, and any later integrated proof-controls audit must bind the stable
proof and stable controls package as separate inputs under a new explicit
authorization.

## A8. Machine-readable closure receipt

```text
P13_V2_CONTROLS_REVIEW_EFFECTIVE=PASS
REMEDIATION_CLOSURE_VERSION=P13-CONTROL-ORACLE-REMEDIATION-CLOSURE-v1
FINDINGS=C0/M0/m0
ORIGINAL_REVIEW_PREFIX_SHA256=83465435fda898c213b5923e0f42e84833dae8bb08476f7a12453523dfe20d04
ORIGINAL_REVIEW_PREFIX_BYTES=22768
ORIGINAL_REVIEW_PREFIX_LINES=442
ORIGINAL_M1_CLOSED=true
CRITICAL_OPEN=0
MAJOR_OPEN=0
MINOR_OPEN=0
V2_DESIGN_GATE_SHA256=0094462b1e06cde0cf1fcc3536c608dcd96ef1e9eb0d85a0714df1666b799706
BASE_V1_DESIGN_SHA256=900c541713b1711bdab7fa0d264355b6d8ee27014094e60eac6aabe38190604c
V1_DESIGN_AMENDMENT_SHA256=5c9caea983b0047c4b16d0437c23b117a6b8150bbeb67b79c60fb9b2ba6a737e
FINAL_V1_DESIGN_REVIEW_SHA256=bf56b96e19b682600ed5de43f7df51ef381fe82d4e12363f66cd1e7d2a5a5184
V2_DESIGN_SHA256=0c0113cff7cf7853d2f4e90ab311ace347f0bebbd8bbf36ab38501fd279c54d9
V2_DESIGN_REVIEW_SHA256=4385b74e81454ab699975a1c0f8217837ae1a7f90a6a220d47eecfdaaeca71c6
FIRST_RUN_IMPLEMENTATION_GATE_SHA256=e3226570f6d9630d5a912cb6b189d194bd33df395e276ce56d48ad75f9601312
REMEDIATION_GATE_SHA256=1ffba02ae468f7f847146a82a51c2e221aa25a64e65330cddd27504c2a971a42
GENERATOR_SHA256=8eabcc08426d16a2b12784fb060c7aa55214e544957098488b6deee138577829
TESTS_SHA256=64d031244d112ff93c518c2e6d1df84d198b8051ab5ba462dfcdf057c1f61aaf
REPRODUCE_SHA256=a1013af1ad852d30ce0f67aba8c9421118181c5612cc95de228199fa3d3fbdcd
CODE_README_SHA256=fa18564c8aa001cc8e287a8d0520f8696499f2658083bef3c7ee029361df954b
EXPERIMENTS_README_SHA256=3e014b0c997d62c7cf9eea30a436033cd8a49982a7bb342e23b08ddb58042ade
RESULTS_README_SHA256=99d4a3bd2a71374157b63458fbe21df3f32745da1935b82ef55aceaf86f6074c
FIRST_RUN_MANIFEST_SHA256=52a6ea213fc7ebadbe26cc13716caf91c69c7adb829cec72434bea761b103e3d
FIRST_RUN_MANIFEST_DOWNSTREAM_EVIDENCE_VALID=false
REPLACEMENT_MANIFEST_SHA256=26a41e2920d9a3743cc1b681aa1e32d601dc12e5fded15b3c6349840bd9094c2
REPLACEMENT_MANIFEST_STABLE=true
REPLACEMENT_MANIFEST_DOWNSTREAM_CONTROLS_EVIDENCE_VALID=true
CSV_HASHES_UNCHANGED_FROM_PRESERVED_SECTION_3=12/12
CSV_ARTIFACTS_RECOMPUTED=12
GENERATED_ARTIFACTS_RECOMPUTED=13
V1_CSV_BODIES_BYTE_IDENTICAL=true
V1_CSV_BODY_ROWS_RECOMPUTED=2548
V2_NEW_CSV_BODY_ROWS_RECOMPUTED=117
CSV_BODY_ROWS_RECOMPUTED=2665
EXPLICIT_NEGATIVES_RECOMPUTED=67
UNITTEST_METHODS_DISCOVERED=176
V2_SCHEMA_COLUMNS=41
V2_FAMILY_COUNTS_EXACT=true
V2_ORACLE_MAP_EXACT=true
MANIFEST_BINDINGS_ARRAY_COUNT=24
MANIFEST_DESIGN_HEAD_SEPARATE=true
MANIFEST_EDGE_HASHES_EXACT=43/43
MANIFEST_SELF_HASH_PRESENT=false
CONCURRENT_PROOF_DIGEST_PRESENT=false
NEGATIVE_DETECTOR_INDEPENDENCE_PASSED=true
POSITIVE_ORACLE_INDEPENDENCE_PASSED=true
COMPLETE_ISOLATED_TAMPER_REGISTRY_EXECUTED=true
VERIFY_ONLY_BYTES_METADATA_IMMUTABLE=true
AUTHOR_TOP_LEVEL_REPRODUCE_CONSUMED=true
INDEPENDENT_TOP_LEVEL_REPRODUCE_CONSUMED=true
INDEPENDENT_TOP_LEVEL_REPRODUCE_RUNS=1
INDEPENDENT_TOP_LEVEL_REPRODUCE_EXIT=0
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
BYTE_IDENTICAL_ARTIFACTS=13
UNITTEST_FAILURES=0
UNITTEST_ERRORS=0
NEGATIVE_FAILURES=0
PROHIBITED_CACHE_ENTRIES=0
TASK_TEMP_RESIDUE=0
TEST_SCRATCH_RESIDUE=0
RELEVANT_PROCESSES_AFTER_RUN=0
INDEPENDENT_CONTROLS_AUDIT_PASSED=true
CONTROL_RESULTS_INTERPRETATION_AUTHORIZED=true
CONTROL_RESULTS_INTERPRETATION_SCOPE=FINITE_DIAGNOSTICS_AND_POLICY_LEDGERS_ONLY
STANDALONE_PASS=false
NOTE_OR_MERGE_BINDING=true
PROOF_AUTHORIZED=false
PROOF_BINDING_AUTHORIZED=false
SOURCE_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_INVOCATION_ALLOWED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
CITATION_PACKAGE_AUTHORIZED=false
RELEASE_AUTHORIZED=false
GIT_AUTHORIZED=false
PUBLIC_SYNC_AUTHORIZED=false
```

**Effective final verdict for the replacement tuple: PASS — C0/M0/m0.**
The original M1 is closed.  The unchanged twelve CSVs and their exact
`2665/67/176` package totals are now supported by fail-closed semantic
detectors, independently recomputed positive oracles and summaries, the full
isolated mutation registry, and one successful serialized independent
reproduction.

This complete review does not embed its own digest.  Its final SHA-256 is
computed only after these bytes are frozen and is carried externally.
