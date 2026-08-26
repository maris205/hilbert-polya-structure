# Paper 17 Phase-2 first-run controls failure audit

Date: 2026-08-16  
Review status: **FINAL — REVISE C0/M1/m0**  
Audit type: independent, read-only implementation/run failure audit  
First-run tuple downstream-valid: **false**

## 1. Decision

The first authorized controls run is **not a controls PASS** and its tuple is
not valid for downstream control-result interpretation. The disposition is
`REVISE`, with one Major finding:

```text
C=0
M=1
m=0
M1=ISOLATED_VERIFIER_INHERITS_OUTER_REPRODUCTION_SENTINEL
FIRST_RUN_TUPLE_DOWNSTREAM_VALID=false
```

The visible six failures are reproducible from the checked-in source without
rerunning the top-level reproduction: package mutations P025--P030 invoke the
generator directly in a new package root, but inherit
`P17_REPRO_ACTIVE=1` from the outer run. The generator consequently treats the
isolated root as if its `experiments/` directory must contain the outer run's
owned lock. That lock was correctly not copied. The resulting experiment
inventory failure is exit 8 and occurs before the intended authority or
implementation binding checks at exit 6.

This is not merely six incorrectly expected return codes. The same leaked
state silently supplies the expected numeric exit 8 for P020--P022 and
P041--P042 from the wrong validation phase, while P031 contains two
simultaneous inventory defects and is not isolated. The required claim that
all 42 package mutations are isolated and exercise their named failure is
therefore unestablished.

The nine CSVs, their aggregate arithmetic, the 180-method source inventory,
and the manifest's byte/hash bindings and acyclic proof firewall all
reconstruct exactly. Those facts make the defect locally remediable and do
not reopen the upstream symbolic proof; they do not convert the failed run or
the manifest's declarative `status: PASS` field into a terminal controls PASS.

## 2. Scope, independence, and evidence boundary

This audit applied the ARS experiment-integrity and reproducibility rules and
the methodology, domain, devil's-advocate, and independent-review lenses. It
separates checked evidence, causal inference, and remediation advice.

The audit:

- read and independently hashed the effective control gate, base design,
  amendment, final design review, and implementation gate;
- read all five implementation files, all nine CSVs, and the manifest;
- independently reconstructed CSV headers, order, family counts, row counts,
  negative multiplicities, method inventory, manifest bindings, and DAG;
- used static control-flow tracing and direct `--verify-only` subprocesses in
  disposable copies under `mktemp` to test the proposed cause;
- did not contact an implementation author and does not use an author's
  explanation as proof;
- did not execute `experiments/reproduce.sh`, did not retry the consumed run,
  and did not modify or regenerate implementation, CSV, or manifest bytes; and
- removed every audit-created temporary root.

The run outcome in Section 7 is the bound first-run receipt recorded in
`notes/pipeline_state.md:26` and `notes/pipeline_state.md:69-78`, not a second
observation obtained by rerunning the top-level entry. Static source tracing
and the isolated probes independently test whether that receipt's stated
failure mechanism follows from the frozen bytes.

## 3. Exact authority and implementation passport

All sizes are byte counts and all digests are SHA-256.

| Authority input | Lines | Bytes | SHA-256 | Result |
|---|---:|---:|---|---|
| `notes/phase2_control_design_gate.md` | 201 | 8,455 | `093ca31fa840b992a105cbfd4911353e3df49ba7e05ae8e43d541059999b6647` | exact |
| `notes/phase2_control_design_lock.md` | 2,103 | 98,350 | `abdc4239077b9c9a82d22ccd86e560bb6fd0850dfcfbb261cf500120555a03aa` | exact |
| `notes/phase2_control_design_amendment_v1.md` | 219 | 8,737 | `83c8effb2dc4e79f90ef4c72cf5b8f4b20974dc21af8a02e074e19a231b0970d` | exact |
| `notes/phase2_control_design_review.md` | 543 | 22,442 | `42d1389171a7c23ed40657ff979a2500a8b3daade2561af54755c0c1c4339326` | exact |
| `notes/phase2_control_implementation_gate.md` | 336 | 13,494 | `aa73b08716e6064f93c1f760a9b91f16239ec204d4ea19a84cebf8d93833cf3e` | exact |

The final design-review file also preserves its historical 382-line,
15,885-byte prefix at
`a3daae0ed8331cc33e8338e60eadb13a0f2833a092b41b844d95893f2e895342`.
The implementation gate is therefore the exact gate named for this audit,
not a look-alike or later variant.

| Manifest-ordered implementation path | Bytes | SHA-256 | Result |
|---|---:|---|---|
| `code/generate_controls.py` | 74,206 | `dcbdc0c2313a8e0a5e2faca96c8ddcb12b92a49b33feb043fdc1d0efdce6c207` | exact |
| `code/test_controls.py` | 60,726 | `d315f2ebecac4be3bc20f7d66012ffc5538e339305e86dfa4429159ed90734e6` | exact |
| `code/README.md` | 1,567 | `8e7b566b57a63e61710c70aea8b49110b05993d7dc6588f62dd606a58b9b700a` | exact |
| `experiments/reproduce.sh` | 9,876 | `37319ae5f87105bdb8317b2fc9a8f017012c7a12909aa98aa09ea0ab1b22575f` | exact |
| `experiments/README.md` | 1,104 | `0428aba1b78d430b338ac202985d5d85b260f84bf2e6327077cb026eb06e23f3` | exact |

The code, experiments, and results inventories contain exactly the frozen
`3 + 2 + 10` regular, single-link entries. No symlink, multi-link entry,
closed cache, or task-residue entry was found at audit freeze.

## 4. Independent CSV reconstruction

### 4.1 Canonical order, dimensions, signs, and hashes

The CSVs occur in the gate/manifest order below. Counts exclude the header.

| # | CSV | Columns | Rows | Negative | Nonnegative | Bytes | SHA-256 |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | `range_first_handedness_controls.csv` | 17 | 1,662 | 36 | 1,626 | 236,510 | `5afb4ff1b27d9fd06443e199eec149051415a088169658c05525d723aefc8fd0` |
| 2 | `action_blind_open_records.csv` | 16 | 1,520 | 0 | 1,520 | 203,475 | `e1f7c4902a6c6f2af609873b21a8d5c9660ceb5853941728b2474a0cbe4f9ccc` |
| 3 | `connected_disconnected_firewall.csv` | 16 | 19 | 4 | 15 | 4,561 | `5ab31e9b0b8eec75e104321c92fe0e1c77f936213f6d24debd83032eeeeba079` |
| 4 | `domain_guard_controls.csv` | 15 | 25 | 10 | 15 | 6,822 | `36ffce22fadd01205d9cc334e4054a7b8bbc099a925dfdf85ef464c5d012b5df` |
| 5 | `quantale_localic_firewall.csv` | 18 | 21 | 7 | 14 | 4,851 | `efc5ba1bf4a6568f679e1c64f4f2103430e71f472f6898e1f158417dfabf70f3` |
| 6 | `actual_standard_owner_controls.csv` | 17 | 18 | 11 | 7 | 5,744 | `00973eaf6eb2890ac452093704049f5e090ff134ccec268604df15d36a4bbd82` |
| 7 | `dilation_strict_marker_controls.csv` | 19 | 140 | 5 | 135 | 29,504 | `ae673db6b04f2c91af86688b957fc9fef629a5c307588c72278a2f4f5811b2eb` |
| 8 | `fixed_prime_provenance_controls.csv` | 17 | 21 | 11 | 10 | 8,924 | `168e5d57109745c0b4fd20270e7026dc1c7352e9367fef752310c740eac593f5` |
| 9 | `target_summary.csv` | 12 | 10 | 0 | 10 | 1,947 | `5a36b9e1790f6a2f0c7cf35d9e681c426fd83db120c0ac202ed78ede6e5eb390` |
| **Total** | **9 CSVs** | — | **3,436** | **84** | **3,352** | — | — |

Thus the independently observed ordered header-width vector is exactly
`17,16,16,15,18,17,19,17,12`, and
`3436 - 84 = 3352` independently agrees with the stored aggregate.

### 4.2 Exact schemas

The parsed header sequences are:

```text
range_first_handedness_controls.csv=
  schema_version,row_id,row_family,case_kind,group_token,object_x,h,object_y,k,
  sheet_a,subject_composable,subject_value,oracle_value,detected,
  negative_reason,oracle,status

action_blind_open_records.csv=
  schema_version,row_id,row_family,case_kind,action_case,comparison_case,
  subset_u,subset_v,arrow_open,subject_value,oracle_value,record_equal,
  detected,negative_reason,oracle,status

connected_disconnected_firewall.csv=
  schema_version,row_id,row_family,case_kind,owner_domain,input_n,input_sheet,
  claim_token,subject_value,oracle_value,scope_token,source_binding,detected,
  negative_reason,oracle,status

domain_guard_controls.csv=
  schema_version,row_id,row_family,case_kind,owner_domain,topology_token,
  claim_token,evidence_mode,subject_value,oracle_value,scope_token,detected,
  negative_reason,oracle,status

quantale_localic_firewall.csv=
  schema_version,row_id,row_family,case_kind,owner_domain,bare_quantale_receipt,
  q_h_receipt,local_compactness_receipt,promotion_attempt,licensed,
  subject_value,oracle_value,source_binding,scope_token,detected,
  negative_reason,oracle,status

actual_standard_owner_controls.csv=
  schema_version,row_id,row_family,case_kind,packet_id,owner_token,
  topology_token,topos_token,quantale_token,base_frame_token,comparison_field,
  subject_value,oracle_value,detected,negative_reason,oracle,status

dilation_strict_marker_controls.csv=
  schema_version,row_id,row_family,case_kind,L,L_prime,scale_c,r,t,u,
  claim_token,subject_value,oracle_value,inverse_value,scope_token,detected,
  negative_reason,oracle,status

fixed_prime_provenance_controls.csv=
  schema_version,row_id,row_family,case_kind,prime_token,generic_theorem_state,
  actual_topology_input,stabilizer_input,claim_token,subject_value,oracle_value,
  source_binding,scope_token,detected,negative_reason,oracle,status

target_summary.csv=
  schema_version,row_id,artifact,expected_rows,expected_columns,
  expected_negative_rows,oracle_class,canonical_order_key,scope_token,
  artifact_order_index,status,notes
```

### 4.3 Family and negative-reason arithmetic

First-occurrence family order and cardinalities independently parse as:

```text
C17-1: ARROW=36, UNIT=6, INVERSE=36, PAIR=1296,
       SHEET_ACTION=36, SHEET_ASSOC=216,
       WRONG_PRODUCT_ORDER=18, OPPOSITE_SHEET_ACTION=18
C17-2: OPEN_DESCRIPTOR=48, INVOLUTION=48, PRODUCT=768, BASE=48,
       CROSS_OPEN=32, CROSS_INVOLUTION=32, CROSS_PRODUCT=512, CROSS_BASE=32
C17-3: SYMBOLIC_RECEIPT=3, Z3_ACTION=9, Z3_PROPERTY=3, PROMOTION_ATTACK=4
C17-4: OWNER_RECEIPT=3, CLAIM_SCOPE=12, WRONG_DOMAIN_ATTACK=10
C17-5: SOURCE_RECEIPT=3, GATE_TRUTH_TABLE=8, PROMOTION_ATTACK=7, OWNER_SCOPE=3
C17-6: OWNER_RECORD=2, FIELD_COMPARISON=5, OWNER_SPLICE_ATTACK=11
C17-7: SYMBOLIC_RECEIPT=2, OBJECT_MAP=4, ARROW_MAP=16,
       SOURCE_COMPAT=16, RANGE_COMPAT=16, INVERSE_COMPAT=16,
       PRODUCT_COMPAT=64, STRICT_MARKER=4, PLAIN_SCALE_PROMOTION=2
C17-8: GENERIC_PRECONDITION=1, FIXED_PRIME_SUBSTITUTION=3,
       ALLOWED_P9_INPUT=6, PROVENANCE_PROMOTION_ATTACK=11
SUMMARY: 10 ordered rows
```

Row IDs are unique and dense within their frozen artifact prefixes; no family
interleaving or order drift was found. There are exactly 48 distinct nonempty
negative-reason tokens. `WRONG_GROUP_PRODUCT_ORDER` and
`OPPOSITE_SHEET_ACTION_HANDEDNESS` occur 18 times each,
`STRICT_MARKER_NONUNIT_SCALE` occurs three times, and each of the other 45
reason classes occurs once. Hence `18 + 18 + 3 + 45 = 84`.

## 5. Independent unittest and mutation inventory

The source was parsed as Python syntax and explicit `test_*` definitions were
counted by class, without importing or executing the suite.

| Class | Explicit methods |
|---|---:|
| `TestC17_1RangeFirst` | 10 |
| `TestC17_2ActionBlind` | 10 |
| `TestC17_3ConnectedFirewall` | 6 |
| `TestC17_4DomainGuards` | 6 |
| `TestC17_5QuantaleLocalic` | 6 |
| `TestC17_6OwnerPackets` | 6 |
| `TestC17_7Dilation` | 8 |
| `TestC17_8FixedPrime` | 6 |
| **C17 semantic/package checks subtotal** | **58** |
| `TestTargetSummary` | 8 |
| `TestManifest` | 10 |
| `TestReproduction` | 8 |
| `TestOracleIndependence` | 6 |
| **Nonmutation support subtotal** | **32** |
| `TestSemanticMutations` | **48** |
| `TestPackageMutations` | **42** |
| **Total** | **180** |

All 180 method names are distinct. The semantic registry is dense from S001
through S048, and the package registry is dense from P001 through P042. The
mutation subtotal is `48 + 42 = 90`; the complete arithmetic is
`58 + 32 + 48 + 42 = 180`. The bound run receipt independently reports that
180 runtime methods were discovered, but its six failures prevent that runtime
inventory from being accepted as a successful suite.

The source-level 48 semantic methods map one-for-one to the 48 nonempty reason
classes reconstructed in Section 4. The 42 package method names and their
declared expected exit classes are present, but M1 prevents the execution from
establishing isolation and target-specific failure for all 42.

## 6. Manifest reconstruction and DAG

`results/manifest.json` is 5,355 bytes with SHA-256
`697da2ca079313b0f4cc5eed266a29c2a1dd7f6821ba4674da4f7089738ee612`.
Parsing and canonical reserialization with sorted keys, two-space indentation,
UTF-8, and one final LF reproduces the checked-in bytes.

Its exact top-level key set is:

```text
acyclic_policy,aggregates,artifacts,bindings,implementation,
package_id,reproduction,schema_version,status
```

The manifest has exactly five ordered authority bindings. Every stored byte
count and digest matches the current target:

1. control-design gate, 8,455 bytes,
   `093ca31fa840b992a105cbfd4911353e3df49ba7e05ae8e43d541059999b6647`;
2. Paper-9 manuscript, 61,831 bytes,
   `24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb`;
3. base control design, 98,350 bytes,
   `abdc4239077b9c9a82d22ccd86e560bb6fd0850dfcfbb261cf500120555a03aa`;
4. final control-design review, 22,442 bytes,
   `42d1389171a7c23ed40657ff979a2500a8b3daade2561af54755c0c1c4339326`;
5. implementation gate, 13,494 bytes,
   `aa73b08716e6064f93c1f760a9b91f16239ec204d4ea19a84cebf8d93833cf3e`.

The five ordered implementation entries exactly match Section 3, and the nine
ordered artifact entries exactly match Section 4. The stored aggregate values
are `9/3436/3352/84/84/180/48/42/90/10`; the reproduction object records two
fresh generations and three byte-identical copies.

The independently reconstructed graph is acyclic:

```text
manifest
  -> 5 external authority/source bindings
  -> 5 implementation leaves
  -> 9 CSV artifact leaves
```

The manifest is not a member of any of those arrays and has neither a self
entry nor a self hash. No Paper-17 proof or proof-review path, basename, byte
count, or digest occurs. Both direct-proof flags are false, and authority is
indirect through the control-design gate. The upstream proof therefore cannot
depend on this downstream manifest.

The manifest's internal `status: PASS` is consistent with its generated
candidate shape, but it is not an execution receipt and cannot override the
failed external run or the required independent controls audit.

## 7. Bound first-run receipt

The sole authorized top-level run was consumed once. The frozen receipt is:

```text
TOP_LEVEL_ENTRY=experiments/reproduce.sh
TOP_LEVEL_EXIT=10
UNITTEST_METHODS=180
UNITTEST_FAILURES=6
UNITTEST_ERRORS=0
FAILED_METHODS=P025,P026,P027,P028,P029,P030
EXPECTED_CHILD_EXIT=6
ACTUAL_CHILD_EXIT=8
AUTOMATIC_RETRY=false
MANUAL_RETRY=false
LOCK_RESIDUE=0
CACHE_RESIDUE=0
TEMP_RESIDUE=0
OTHER_TASK_RESIDUE=0
```

The zero-residue receipt establishes clean failure-path cleanup; it does not
establish suite correctness. No audit action consumed another top-level run.

## 8. Static causal trace

The checked-in control flow is sufficient to explain the receipt:

1. `experiments/reproduce.sh:6-9` reserves exit 3 for entry when
   `P17_REPRO_ACTIVE` is already set. On a normal entry, lines 11--16 install
   deterministic variables and export `P17_REPRO_ACTIVE=1`.
2. The script acquires its own exact lock and eventually launches the unittest
   process at `experiments/reproduce.sh:263`; the process inherits the active
   variable and the outer root legitimately contains the owned lock.
3. `code/test_controls.py:133-137` builds `clean_environment()` by copying all
   of `os.environ` and updating five deterministic variables. It never removes
   `P17_REPRO_ACTIVE`.
4. `code/test_controls.py:140-145` uses that environment by default for direct
   generator verification. `isolated_copy()` at lines 818--835 copies the five
   implementation files and controlled inputs/results, but correctly does not
   copy the outer root's lock.
5. `_verify_case()` at lines 846--849 makes one named mutation and calls
   `run_verify()` without an environment override. P025--P030 at lines 888--893
   expect authority/implementation binding exit 6.
6. In the isolated generator, `code/generate_controls.py:1395-1400` interprets
   any nonempty `P17_REPRO_ACTIVE` as permission for an owned lock. Manifest
   validation at lines 1314--1320 consequently adds
   `.p17-control-reproduce.lock` to the required experiment inventory. The
   isolated directory contains only `README.md` and `reproduce.sh`, so it raises
   exit 8, `unlisted or unhashed implementation path`.
7. The intended binding loop does not begin until
   `code/generate_controls.py:1332-1345`; it is unreachable in those six child
   invocations. Each method therefore observes 8 rather than 6.
8. The unittest entry counts six failures, no errors, and returns 10 at
   `code/test_controls.py:941-954`. The outer script maps the failed suite to
   top-level exit 10 at `experiments/reproduce.sh:263`.

The child in P025--P030 does **not** execute `reproduce.sh`. Accordingly, the
child result is not recursive-entry exit 3, nor a 3-to-8 mapping. It is a direct
generator exit 8 caused by cross-root environment leakage. Exit 3 remains the
separate intended P035 behavior.

## 9. Independent isolated probes

Disposable copies were built outside the checkout. Each probe invoked only
`python3 -B code/generate_controls.py --verify-only --output-dir results` in
the copy. No top-level reproduction entry was invoked.

| Mutation | Clean child env, no lock | Inherited active env, no lock | Inherited active env, exact lock |
|---|---|---|---|
| P025 design-gate digest | 6, target binding | 8, experiment inventory | 6, target binding |
| P026 Paper-9 digest | 6, target binding | 8, experiment inventory | 6, target binding |
| P027 design-lock digest | 6, target binding | 8, experiment inventory | 6, target binding |
| P028 design-review digest | 6, target binding | 8, experiment inventory | 6, target binding |
| P029 implementation-gate digest | 6, target binding | 8, experiment inventory | 6, target binding |
| P030 implementation digest | 6, target binding | 8, experiment inventory | 6, target binding |

Removing only `P17_REPRO_ACTIVE` restores the intended exit 6 in every case.
Keeping the variable but supplying the inventory item that it implies also
restores exit 6. These two counterfactuals localize both the leaked state and
the exact masking branch. The lock column is causal diagnosis only; adding a
fake lock to isolated mutation packages would violate single-mutation
isolation and is not an acceptable repair.

Companion probes found broader same-code masking:

| Methods | Intended clean-env failure | Inherited active/no-lock observation | Audit result |
|---|---|---|---|
| P020--P021 | artifact hash/byte exit 8 | experiment inventory exit 8 | numeric false positive |
| P022 | artifact-order exit 8 | experiment inventory exit 8 | numeric false positive |
| P041 | manifest-aggregate exit 8 | experiment inventory exit 8 | numeric false positive |
| P042 | reproduction-aggregate exit 8 | experiment inventory exit 8 | numeric false positive |
| P031 | added code path exit 8 | added code path plus missing implied lock, exit 8 | causally ambiguous, not isolated |

The current `_verify_case()` asserts only the integer return code. It therefore
reports the five wrong-branch exit-8 cases as successes and cannot show that
P031 has exactly one filesystem mutation. P019 and P023--P024 reach earlier
manifest parse/shape/firewall checks, so this audit does not charge them with
the same masking defect. P037 reaches its earlier CSV/CRLF check. These bounds
keep the finding narrow while demonstrating that its effect exceeds the six
visible failures.

Every probe root and holder was removed. No probe wrote to the controlled
implementation, results, manifest, or authority inputs.

## 10. Finding

### M1 — Isolated verifier inherits outer reproduction ownership state

**Requirement.** The implementation gate requires all 48 semantic and all 42
package mutations to be isolated and to fail for the expected class. An outer
run's active/lock ownership is root-specific orchestration state; it is not a
property of a newly copied mutation root.

**Observed defect.** `clean_environment()` preserves the outer sentinel and
`_verify_case()` reuses it for another root. The corresponding lock is not and
must not be copied. The generator then validates the isolated root against an
environmental inventory rule belonging to the outer root.

**Impact.** P025--P030 visibly fail, P020--P022 and P041--P042 pass for the
wrong reason, and P031 is not a one-delta witness. Exact return-code equality
alone cannot distinguish these paths because several named manifest failures
share closed exit class 8. Therefore the run fails and the promised 42-class
package mutation coverage is not established.

**Severity.** Major. The defect invalidates a required reproducibility and
fail-closed control layer and blocks every downstream consumer, but the CSV
package and upstream proof bytes remain independently bound and the cause is
localized to test orchestration. No Critical or additional Minor finding is
warranted on the audited bytes.

## 11. Downstream validity and stop conditions

The exact first-run evidence tuple remains useful as a historical failed-run
record, but it is downstream-invalid as a controls result:

```text
CURRENT_CONTROLS_PASS=false
FIRST_RUN_TUPLE_DOWNSTREAM_VALID=false
CONTROL_RESULT_INTERPRETATION_AUTHORIZED=false
INDEPENDENT_CONTROLS_AUDIT_PASSED=false
UPSTREAM_SYMBOLIC_PROOF_REOPENED=false
STANDALONE_PASS=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_INVOCATION_ALLOWED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
GIT_AUTHORIZED=false
PUBLIC_SYNC_AUTHORIZED=false
```

In particular, internal agreement of the CSV and manifest bytes is not a
license to quote, interpret, promote, route, compose, or publish the controls.

## 12. Minimum versioned remediation contract

No remediation is authorized by this report. A later authority may adopt the
following minimum contract.

1. **Create a new versioned implementation-remediation gate.** It must bind
   the original implementation gate at
   `aa73b08716e6064f93c1f760a9b91f16239ec204d4ea19a84cebf8d93833cf3e`,
   the failed implementation/CSV/manifest tuple, the no-retry run receipt, and
   this review's externally computed digest. It must state that the original
   sole-run authorization was consumed and that any later run is one newly
   authorized replacement run, not a retry.
2. **Keep the repair root-specific and minimal.** An isolated child environment
   must be derived explicitly with `P17_REPRO_ACTIVE` absent. Every direct
   generator invocation against an isolated copy, including `_verify_case()`
   and the P037/P038 paths, must use that child environment. P035 alone must
   insert `P17_REPRO_ACTIVE=1`; P036 must explicitly keep it absent while
   presenting its pre-existing-lock witness. Actual outer-root checks must
   retain the outer active variable and its genuinely owned lock. Do not add a
   fake lock to ordinary isolated copies and do not globally scrub the variable
   from real outer-root verification.
3. **Prove single-delta isolation.** Before each ordinary isolated mutation,
   the pristine copied package must verify at exit 0 under the child
   environment. A before/after receipt must show only the named mutation, and
   the mutated package must reach its frozen numeric exit class. This applies
   at least to P020--P031 and P041--P042 and should be centralized for all
   ordinary `_verify_case()` users. It must not rely on console prose, which
   the design declares noncanonical, and it must not add or hide a 43rd package
   class. Counts stay exactly `180/48/42/90`.
4. **Preserve the data package.** All nine CSV bytes, headers, order, family
   counts, reason multiplicities, and aggregate values
   `3436/3352/84` must remain byte-identical. No proof, proof review, new source,
   schema, exit taxonomy, or semantic oracle change is part of this repair.
5. **Create a new canonical manifest.** Changing `code/test_controls.py`
   necessarily changes one of the five implementation bindings, so the current
   manifest cannot certify the repaired implementation. The replacement
   manifest must preserve the same five authority bindings, nine CSV artifact
   bindings, top-level schema, order, counts, DAG, and no-self/no-direct-proof
   policy; its implementation entry must bind the repaired test-suite bytes.
   The first manifest digest remains a historical failure-tuple digest and must
   never be relabeled as the repaired manifest.
6. **Authorize exactly one new serialized replacement run.** After the repaired
   implementation and new manifest are frozen, a new gate must authorize one
   and only one top-level `experiments/reproduce.sh` execution. Automatic or
   unversioned retry remains forbidden. Passing requires all 180 methods, zero
   failures, zero errors, all 84 negatives, two fresh generations, three-way
   identity, verify-only immutability, and zero lock/cache/temp/task residue.
7. **Require a fresh independent post-run controls audit.** The replacement
   run does not self-pass. A reviewer independent of the implementation must
   bind the new gate, implementation, manifest, all artifacts, and complete run
   receipt before any downstream state changes.

A new control-design gate or amendment is **not** required if the remediation
is confined to this root-specific environment/isolation repair and preserves
the frozen schema, counts, methods, exit taxonomy, five-binding manifest shape,
and semantic oracles. The remediation gate should remain an external authority
over the fixed five-binding manifest. If a future proposal instead adds the
remediation gate as a sixth manifest binding, changes the exit taxonomy, or
changes any frozen data/method count, that is design drift and requires a new
design amendment plus independent design review before implementation.

The required authorization answers are therefore:

| Question | Answer |
|---|---|
| New versioned implementation-remediation gate? | **Yes** |
| New control-design gate/amendment for the minimum repair? | **No** |
| New canonical manifest after the implementation hash changes? | **Yes** |
| New sole serialized replacement run, explicitly authorized? | **Yes** |
| Fresh independent post-run controls audit? | **Yes** |
| Route, manuscript, release, Git, or public sync now? | **No / false** |

## 13. Final audit receipt

```text
P17_PHASE2_CONTROLS_REVIEW=REVISE
FINDINGS=C0/M1/m0
BOUND_IMPLEMENTATION_GATE_SHA256=aa73b08716e6064f93c1f760a9b91f16239ec204d4ea19a84cebf8d93833cf3e
BOUND_FIRST_RUN_MANIFEST_SHA256=697da2ca079313b0f4cc5eed266a29c2a1dd7f6821ba4674da4f7089738ee612
FIRST_RUN_TOP_LEVEL_EXIT=10
FIRST_RUN_METHODS=180
FIRST_RUN_FAILURES=6
FIRST_RUN_ERRORS=0
FIRST_RUN_RETRIED=false
FIRST_RUN_CLEANUP_RESIDUE=0
CSV_ARTIFACTS=9
CSV_BODY_ROWS=3436
NONNEGATIVE_CSV_ROWS=3352
EXPLICIT_NEGATIVES=84
SEMANTIC_MUTATION_METHODS=48
PACKAGE_MUTATION_METHODS=42
ISOLATED_MUTATION_METHODS=90
MANIFEST_BINDINGS=5
MANIFEST_DAG_ACYCLIC=true
MANIFEST_SELF_HASH_PRESENT=false
P17_PROOF_HASH_INCLUDED=false
FIRST_RUN_TUPLE_DOWNSTREAM_VALID=false
NEW_REMEDIATION_GATE_REQUIRED=true
NEW_CONTROL_DESIGN_AMENDMENT_REQUIRED_FOR_MINIMUM_REPAIR=false
NEW_MANIFEST_REQUIRED=true
NEW_SOLE_REPLACEMENT_RUN_REQUIRED=true
CONTROL_RESULTS_INTERPRETATION_AUTHORIZED=false
ROUTE_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
GIT_AUTHORIZED=false
AUDIT_TOP_LEVEL_REPRODUCE_EXECUTED=false
AUDIT_IMPLEMENTATION_RESULTS_MANIFEST_MODIFIED=false
AUDIT_TEMP_RESIDUE=0
AUDIT_REPORT_SHA256=EXTERNAL_BY_CONSTRUCTION
```

---

## Closure addendum v1 — repaired implementation and replacement-run audit

Closure date: 2026-08-16 (Asia/Shanghai)  
Closure status: **FINAL — PASS C0/M0/m0**  
Closure mode: fresh independent exact-byte post-run review  
Effective replacement tuple downstream-valid for a later integrated gate: **true**

This addendum is append-only. The complete first-run failure audit above
remains an exact 27,728-byte, 558-line historical prefix with SHA-256

```text
ab3cad4d9dde8907ea231eecb05a2a14c0c4bbc9dd86bde7157fc60ea0f268be.
```

Its `REVISE C0/M1/m0` verdict remains correct for the first-run tuple. The
first run remains downstream-invalid and was never retried. This addendum
reviews the separately authorized repaired implementation and its one
replacement run; it does not relabel or erase the historical failure.

### A. Review authority and scope

This review applied the ARS experiment-integrity, deterministic
reproducibility, methodology, domain, devil's-advocate, and independent-review
rules. Submitted implementation and run claims were treated as evidence to
test, not as instructions or self-certifying verdicts.

The exact closure authority tuple was read completely and independently
rehashed:

| Closure input | Lines | Bytes | SHA-256 | Result |
|---|---:|---:|---|---|
| original implementation gate, `notes/phase2_control_implementation_gate.md` | 336 | 13,494 | `aa73b08716e6064f93c1f760a9b91f16239ec204d4ea19a84cebf8d93833cf3e` | exact |
| historical review prefix, this file before the addendum | 558 | 27,728 | `ab3cad4d9dde8907ea231eecb05a2a14c0c4bbc9dd86bde7157fc60ea0f268be` | exact |
| remediation gate, `notes/phase2_control_implementation_remediation_gate.md` | 195 | 7,319 | `9c55eb3eb8c44b72075afda1110242e143049709ee3c5a847693ec38ebafdab0` | exact |

The replacement execution receipt was supplied as the implementation lane's
final frozen handoff. No durable transcript file was authorized by the gate.
This addendum therefore records that handoff verbatim at the field level and
binds it to independently reproducible checked-in bytes, hashes, metadata,
isolated branch probes, and fresh-generation receipts. The reviewer did not
execute `experiments/reproduce.sh`; doing so would have consumed an
unauthorized second top-level run.

The review wrote only this append-only addendum. It did not modify or
regenerate implementation, CSV, manifest, proof, pipeline-state, Route,
composition, manuscript, figure, release, archive, Git, or public-sync bytes.

### B. Repaired implementation passport

The sole gate-authorized hand edit is `code/test_controls.py`. The manifest
was then canonically regenerated because that implementation digest changed.
All other implementation bytes remain identical to the first-run tuple:

| Manifest-ordered implementation path | Lines | Bytes | SHA-256 | Disposition |
|---|---:|---:|---|---|
| `code/generate_controls.py` | 1,443 | 74,206 | `dcbdc0c2313a8e0a5e2faca96c8ddcb12b92a49b33feb043fdc1d0efdce6c207` | unchanged |
| `code/test_controls.py` | 1,049 | 66,677 | `d61cfe8fb6bb6bb03e31558258a9de9a27e4e1d6fe7ec93144d51fb1783eebad` | repaired exact bytes |
| `code/README.md` | 35 | 1,567 | `8e7b566b57a63e61710c70aea8b49110b05993d7dc6588f62dd606a58b9b700a` | unchanged |
| `experiments/reproduce.sh` | 309 | 9,876 | `37319ae5f87105bdb8317b2fc9a8f017012c7a12909aa98aa09ea0ab1b22575f` | unchanged |
| `experiments/README.md` | 20 | 1,104 | `0428aba1b78d430b338ac202985d5d85b260f84bf2e6327077cb026eb06e23f3` | unchanged |

The source AST contains exactly 180 distinct explicit `test_*` methods. Their
independently parsed allocation remains:

```text
conformance/reproduction/oracle methods = 90
semantic mutation methods S001..S048    = 48
package mutation methods P001..P042     = 42
total explicit methods                  = 180
isolated mutation methods               = 90.
```

No method was added, removed, renamed, dynamically manufactured, or hidden by
the repair.

### C. Root-cause repair and special-state audit

The repaired source closes M1 with a root-specific state boundary:

1. `isolated_environment()` derives the deterministic child environment and
   explicitly removes `P17_REPRO_ACTIVE`.
2. Every ordinary `_verify_case()` creates a fresh isolated copy, proves that
   pristine copy at exit 0 under that scrubbed environment, takes a complete
   tree snapshot, applies one registered mutation, checks the snapshot delta,
   requires the frozen numeric exit, and proves verify-only did not change the
   mutated copy.
3. P037 uses the same scrubbed environment and proves CRLF rejection without
   rewrite. P038 uses it for the nonempty generation-root rejection.
4. P035 alone explicitly adds `P17_REPRO_ACTIVE=1`; its test freezes the
   environment-only delta, recursive exit 3, and unchanged tree.
5. P036 explicitly leaves the sentinel absent, creates only the exact lock
   witness, requires concurrency exit 3, compares the lock's type/size/
   mode/mtime/link metadata before and after, and requires the whole mutated
   tree to remain unchanged.

Independent static inspection of `experiments/reproduce.sh` confirms the
effective order

```text
recursive sentinel guard
  -> deterministic environment/root validation
  -> exact no-follow pre-existing-lock check
  -> all-other residue scan
  -> atomic lock mkdir
  -> owned-lock state.
```

Thus P035 cannot fall through into inventory validation, P036 cannot be
preempted by generic residue exit 5, and ordinary isolated roots cannot inherit
the outer run's root-specific ownership state. No fake lock is injected into
an ordinary isolated copy.

### D. Independent affected-case probes

The reviewer constructed a new disposable root for each affected ordinary
case. Each root independently copied the exact five implementation files,
the four manifest-bound local authority files, the Paper-9 source, and the
complete ten-file package. `P17_REPRO_ACTIVE` was absent. Before mutation,
every root passed verify-only at exit 0 and retained an identical recursive
lstat/hash snapshot. After the one registered mutation, the target entry
returned the following frozen numeric class and left the mutated snapshot
unchanged:

| Case | Registered payload delta | Pristine exit | Target exit | Post-call immutability |
|---|---|---:|---:|---|
| P020 | manifest artifact SHA | 0 | 8 | exact |
| P021 | manifest artifact byte count | 0 | 8 | exact |
| P022 | manifest artifact order | 0 | 8 | exact |
| P023 | manifest self-hash key | 0 | 8 | exact |
| P024 | direct P17-proof binding | 0 | 8 | exact |
| P025 | design-gate binding digest | 0 | 6 | exact |
| P026 | Paper-9 binding digest | 0 | 6 | exact |
| P027 | design-lock binding digest | 0 | 6 | exact |
| P028 | design-review binding digest | 0 | 6 | exact |
| P029 | implementation-gate binding digest | 0 | 6 | exact |
| P030 | implementation digest | 0 | 6 | exact |
| P031 | one unlisted implementation file | 0 | 8 | exact |
| P037 | target-summary LF-to-CRLF mutation | 0 | 7 | exact |
| P038 | one nonempty output-root fixture | 0 | 4 | exact |
| P041 | manifest unittest aggregate | 0 | 8 | exact |
| P042 | manifest copy-count aggregate | 0 | 8 | exact |

For P031, the full lstat receipt also observes the unavoidable parent `code/`
directory metadata change caused by creating the one payload file; no second
payload entry exists. P038's registered fixture consists exactly of the new
output directory and its one `sentinel` file. All disposable roots were
removed. These probes invoked only generator `--verify-only` or `--generate`
in temporary roots; none invoked the top-level reproduction entry.

The six historically visible cases P025--P030 now reach authority/
implementation exit 6, not the unrelated experiment-inventory exit 8.
P020--P022 and P041--P042 no longer receive a same-number false positive from
the missing implied lock. P031 contains only its registered unhashed-path
mutation.

### E. CSV reconstruction and exact data identity

All nine CSVs are byte-for-byte identical to the historical first-run frozen
hashes:

| # | CSV | Columns | Rows | Negative | SHA-256 |
|---:|---|---:|---:|---:|---|
| 1 | `range_first_handedness_controls.csv` | 17 | 1,662 | 36 | `5afb4ff1b27d9fd06443e199eec149051415a088169658c05525d723aefc8fd0` |
| 2 | `action_blind_open_records.csv` | 16 | 1,520 | 0 | `e1f7c4902a6c6f2af609873b21a8d5c9660ceb5853941728b2474a0cbe4f9ccc` |
| 3 | `connected_disconnected_firewall.csv` | 16 | 19 | 4 | `5ab31e9b0b8eec75e104321c92fe0e1c77f936213f6d24debd83032eeeeba079` |
| 4 | `domain_guard_controls.csv` | 15 | 25 | 10 | `36ffce22fadd01205d9cc334e4054a7b8bbc099a925dfdf85ef464c5d012b5df` |
| 5 | `quantale_localic_firewall.csv` | 18 | 21 | 7 | `efc5ba1bf4a6568f679e1c64f4f2103430e71f472f6898e1f158417dfabf70f3` |
| 6 | `actual_standard_owner_controls.csv` | 17 | 18 | 11 | `00973eaf6eb2890ac452093704049f5e090ff134ccec268604df15d36a4bbd82` |
| 7 | `dilation_strict_marker_controls.csv` | 19 | 140 | 5 | `ae673db6b04f2c91af86688b957fc9fef629a5c307588c72278a2f4f5811b2eb` |
| 8 | `fixed_prime_provenance_controls.csv` | 17 | 21 | 11 | `168e5d57109745c0b4fd20270e7026dc1c7352e9367fef752310c740eac593f5` |
| 9 | `target_summary.csv` | 12 | 10 | 0 | `5a36b9e1790f6a2f0c7cf35d9e681c426fd83db120c0ac202ed78ede6e5eb390` |

The independent parser reconstructed the ordered header-width vector
`17,16,16,15,18,17,19,17,12`, every family order/cardinality, dense row-ID
range, and all reason multiplicities. The totals are:

```text
CSV_BODY_ROWS=3436
EXPLICIT_NEGATIVE_ROWS=84
NONNEGATIVE_CSV_ROWS=3352
DISTINCT_NEGATIVE_REASON_CLASSES=48
EXPECTED_NEGATIVES_DETECTED=84.
```

The reason ledger retains 18 wrong-product witnesses, 18 opposite-sheet
witnesses, three strict-nonunit witnesses, and one row for each of the other
45 classes. No CSV, schema, family, reason, oracle, source binding, or result
value drift was found.

### F. Replacement manifest and acyclic authority

The repaired canonical manifest is 5,355 bytes with SHA-256

```text
a15cc81ca8e41b7fd76560304bf713701f416a028558b9d9c5653b58f7ebc254.
```

Parsing and canonical `sort_keys=True`, two-space-indented reserialization
reproduces its exact bytes. It has exactly five authority bindings, five
implementation entries, and nine CSV artifact entries. Every recorded byte
count and digest matches its current target. The repaired test entry is
`d61cfe8f...`; all other implementation and all nine artifact bindings are
unchanged.

The remediation gate remains external and is not a sixth binding. The
manifest contains no self entry/hash and no path, basename, byte count, or
digest for a Paper-17 proof or proof review. The four direct-proof/self flags
remain false, so the graph remains acyclic. Its internal `status: PASS` is a
package-shape receipt only; the effective controls PASS comes from the
external run receipt plus this independent review.

### G. Independent deterministic reproduction receipts

The reviewer first captured a full checked-in receipt covering the ten
generated artifacts, with type, mode, size, SHA-256, nanosecond mtime and
ctime, link count, device and inode. A scrubbed-environment checked-in
verify-only call returned exit 0 and left that complete receipt unchanged.

The reviewer then generated two distinct fresh temporary packages A and B in
separate generator processes, verified each at exit 0, and compared all ten
artifacts across checked-in/A/B. Every CSV and the manifest matched
byte-for-byte:

```text
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
THREE_WAY_BYTE_IDENTITY_10_OF_10=true
FRESH_MANIFEST_SHA256=a15cc81ca8e41b7fd76560304bf713701f416a028558b9d9c5653b58f7ebc254.
```

The compact checked-in metadata/byte receipt specified by
`experiments/reproduce.sh` was independently reconstructed from the current
ten files. Its SHA-256 exactly equals the frozen replacement handoff:

```text
CHECKED_IN_RECEIPT_SHA256=e00311fdefa4fecbd4fa9d8f281c078a5828f3430f59c2ae15195ac81f2fcd0c.
```

Under the ARS deterministic-experiment rule, the independently repeated
generation and exact 10-of-10 byte comparison support
`REPRODUCIBLE` for the generated package. This conclusion is limited to the
finite package; it is not a mathematical theorem or publication verdict.

### H. Bound original and replacement execution receipts

The historical original-run fields remain:

```text
ORIGINAL_SOLE_RUNS=1
ORIGINAL_RUN_EXIT=10
ORIGINAL_RUN_RETRIED=false
ORIGINAL_RUN_TUPLE_DOWNSTREAM_VALID=false.
```

The final frozen replacement handoff is:

```text
REPLACEMENT_TOP_LEVEL_RUNS=1
REPLACEMENT_TOP_LEVEL_EXIT=0
RETRY=0
AUTOMATIC_SECOND_ATTEMPTS=0
MANUAL_SECOND_ATTEMPTS=0

UNITTEST_METHODS=180
UNITTEST_FAILURES=0
UNITTEST_ERRORS=0
SEMANTIC_MUTATION_CLASSES=48
PACKAGE_MUTATION_CLASSES=42
ISOLATED_MUTATION_METHODS=90
EXPECTED_NEGATIVES_DETECTED=84
NEGATIVE_FAILURES=0

CSV_BODY_ROWS=3436
NONNEGATIVE_CSV_ROWS=3352
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
CHECKED_IN_RECEIPT_SHA256=e00311fdefa4fecbd4fa9d8f281c078a5828f3430f59c2ae15195ac81f2fcd0c

COMPETING_P17_PROCESSES=0
LOCK_RESIDUE=0
CACHE_RESIDUE=0
TEMP_RESIDUE=0
TASK_RESIDUE=0
INVENTORY_DRIFT=0
CSV_HASH_DRIFT=0.
```

The replacement is a newly authorized execution under the remediation gate,
not a retry under the consumed original gate. No automatic or manual second
attempt occurred.

At closure freeze, a fresh no-follow scan independently found exactly the
`3/2/10` code/experiments/results inventories, zero competing Paper-17
generator/test/reproduction process, zero exact lock, zero closed cache or
task residue in the Paper-17 subtree, and zero `p17-controls.*` or
closure-probe temporary roots. All reviewer-created roots had been removed.

### I. M1 closure and effective verdict

The historical M1 is closed on the repaired implementation:

```text
HISTORICAL_FIRST_RUN_VERDICT=REVISE_C0_M1_m0
HISTORICAL_M1=ISOLATED_VERIFIER_INHERITS_OUTER_REPRODUCTION_SENTINEL
HISTORICAL_FIRST_RUN_TUPLE_DOWNSTREAM_VALID=false

M1_REPAIR=ROOT_SPECIFIC_ISOLATED_ENVIRONMENT_PLUS_PRISTINE_SINGLE_DELTA_RECEIPTS
M1_EFFECTIVE_STATUS=CLOSED
NEW_CRITICAL_OPEN=0
NEW_MAJOR_OPEN=0
NEW_MINOR_OPEN=0

EFFECTIVE_CONTROLS_REVIEW_VERDICT=PASS_C0_M0_m0
REPLACEMENT_RUN_TUPLE_DOWNSTREAM_VALID_FOR_LATER_GATE=true
INDEPENDENT_CONTROLS_AUDIT_PASSED=true.
```

No new Critical, Major, or Minor finding arose from the repair, replacement
manifest, replacement receipt, affected-branch probes, fresh generation,
verify-only immutability, or cleanup audit.

The controls remain finite diagnostics and serialization receipts. They do
not prove connectedness of the real line, any topos/quantale equivalence,
local compactness, `q_H`, localic reconstruction, non-etaleness, numerical
scale, C-star/Haar/trace/determinant structure, novelty, priority, or Route-B
eligibility. This addendum closes the controls-audit gate only; it does not
itself issue a later integrated interpretation gate.

```text
CONTROL_RESULTS_INTERPRETATION_AUTHORIZED=false
UPSTREAM_SYMBOLIC_PROOF_REOPENED=false
STANDALONE_PASS=false
TECHNICAL_NOTE_CANDIDATE=true
ROUTE_A_AUTHORIZED=false
ROUTE_B_INVOCATION_ALLOWED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
FIGURE_WORK_AUTHORIZED=false
CITATION_PACKAGE_AUTHORIZED=false
RELEASE_AUTHORIZED=false
ARCHIVE_AUTHORIZED=false
GIT_AUTHORIZED=false
PUBLIC_SYNC_AUTHORIZED=false
AUDIT_TOP_LEVEL_REPRODUCE_EXECUTED=false
AUDIT_IMPLEMENTATION_RESULTS_MANIFEST_MODIFIED=false
AUDIT_TEMP_RESIDUE=0
CLOSURE_REPORT_SHA256=EXTERNAL_BY_CONSTRUCTION
```
