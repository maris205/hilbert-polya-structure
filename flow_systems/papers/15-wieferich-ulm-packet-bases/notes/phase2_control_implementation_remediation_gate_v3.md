# Paper 15 control-implementation remediation governance gate v3

Status: PASS AS A NARROW IMPL-08 CORRIGENDUM ONLY
Current six-path source verdict: QUARANTINED / REVISE / NOT FROZEN
ATTEMPT_3 status: SOLE AUTHORIZED FUTURE SOURCE TRANSACTION / UNCONSUMED
Static implementation review verdict: NOT YET ADMITTED
Runtime-profile acceptance, preflight, execution, generated-artifact,
manuscript, release, archive, and Git authority: none

This record is the sole successor-governance write authorized by the current
owner/orchestrator after a fresh scope audit found one Major ambiguity in the
frozen v2 gate's IMPL-08 row.  It is a corrigendum to that gate, not a design
amendment, implementation source, implementation attempt, source repair,
review, runtime-profile acceptance, or execution gate.  The frozen v2 record
is immutable and remains operative except for the exact narrow supersession
and interpretation stated in Section 3 below.

Until an external coordinator has issued one complete stable receipt for this
v3 record, v2 alone does not admit the implementation author.  After that
receipt, v2 and v3 operate together over the same still-unconsumed ATTEMPT_3,
subject to every v2 pre-write predicate.

## 1. Material Passport and pre-write adjudication

- Artifact kind: implementation-remediation governance corrigendum.
- Sole gate-author target:
  `papers/15-wieferich-ulm-packet-bases/notes/phase2_control_implementation_remediation_gate_v3.md`.
- Gate-author writes outside that target: zero.
- Gate target before this authoring step: absent under ordinary and
  symlink-aware checks.
- Frozen predecessor v2: regular, mode 0644, nlink 1, 1084 lines, 59542
  bytes, SHA-256
  `69563f95d9407ffe98c3e0c78c664ea8105f0f8e5f8994c4337f85fafb2063b1`.
- Current design review: regular, mode 0644, nlink 1, 6431 lines, 346453
  bytes, SHA-256
  `2bb21b0e75ebf6a65bc51a1e42047931c34e9a86be8d641c977ef8c06a9d5e19`.
- Preserved pre-v14 review prefix: 5962 lines, 321362 bytes, SHA-256
  `3a17a681b880d4f99bc41aabe2dcde3a29ec6117dc896de14991a73547fdb40f`.
- Effective comparator-probe design authority: amendment v2, regular, mode
  0644, nlink 1, 1750 lines, 98006 bytes, SHA-256
  `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea`.
- Latest design authority: amendment v14, regular, mode 0644, nlink 1, 1414
  lines, 65752 bytes, SHA-256
  `b20be3afd58f4eb82ab77b071057effe9678389c7a9525a5c86f6301f158939c`.
- Governing v14 remediation gate: regular, mode 0644, nlink 1, 1665 lines,
  84029 bytes, SHA-256
  `cb9100863e241f3271781512b8ed83971241974bedd9db9741b5b9acc596c292`.
- Current effective amendment count and order: thirteen, v1 through v11,
  then v13, then v14; v5 remains blocked/no-op provenance and amendment v12
  remains absent/skipped.
- Current design verdict: `PASS_C0_M0_m0`.
- Historical implementation attempts consumed: two.
- ATTEMPT_3 source mutation observed before v3 issuance: false.
- Project source imported, sourced, compiled as project code, or executed
  while preparing this gate: false.
- Platform preflight, runtime probe, generator, verifier, test, wrapper, or
  reproduction run performed while preparing this gate: false.
- Generated artifact, result, cache, helper, temporary, lock, or manifest
  member created while preparing this gate: false.

The complete applicable ARS-Codex 0.1.25 academic-research-suite router;
pipeline, reviewer, and experiment workflows; code-runner and integrity
roles; and integrity/reproducibility protocols were reread and re-hashed.
Their receipts remain exactly those frozen in v2 Section 1.1.  They require
fixed observations, explicit authority, evidence-bound claims, independent
review, and no execution or reproduction claim without an authorized actual
run.  They do not supply source correctness or runtime authority.

This v3 record intentionally predicts neither its own final line/byte count
nor its own SHA-256.  Those values must be computed externally after this
sole write and confirmed by a second unchanged read.

## 2. Exact unchanged source and absence barrier

Immediately before this sole governance write, a read-only lstat, complete
byte/hash pass, count, and three-root inventory reproduced the exact v2 start
quarantine in the same order:

| Ordered path | Type | Mode | nlink | Lines | Bytes | SHA-256 |
|---|---|---:|---:|---:|---:|---|
| `code/generate_controls.py` | regular | 0644 | 1 | 1086 | 56136 | `d1f1db09edade24a2d6ac48ee943079ecfc51217cd9cd05cc2a8241eaa7be9fc` |
| `code/test_controls.py` | regular | 0644 | 1 | 1239 | 98421 | `d2b124daa27040c0df5d19f6a278092b5977b0a37f6c0379cff3ffa6745bc756` |
| `code/README.md` | regular | 0644 | 1 | 75 | 3722 | `6d270eb371c1a30f3466d5fa7639a590ca669bbbe2213789a89ec797c72f7beb` |
| `experiments/reproduce.sh` | regular | 0644 | 1 | 4452 | 316515 | `930c6f8fc16ab9d64b15c00bc27a526df9057b9b52033ed247d7b6281d3cdc66` |
| `experiments/README.md` | regular | 0644 | 1 | 94 | 5419 | `266b902f840e70aa3bc872cb9c8ea9ff651f53771e7705524ec56f2311e96959` |
| `results/README.md` | regular | 0644 | 1 | 55 | 2342 | `b49120d0f2a7aba089d4a04b7d83a2fb9b89d3514d2e70768ac1f03fa7517028` |

```text
START_QUARANTINE_PATH_COUNT=6
START_QUARANTINE_LINES=7001
START_QUARANTINE_BYTES=482555
START_QUARANTINE_ALL_REGULAR=true
START_QUARANTINE_ALL_MODE_0644=true
START_QUARANTINE_ALL_NLINK_1=true
ATTEMPT_3_FIRST_SOURCE_MUTATION_OCCURRED=false
ATTEMPT_3_SOURCE_OR_METADATA_WRITE_OCCURRED=false
ATTEMPT_3_LINK_OR_RENAME_MUTATION_OCCURRED=false
```

The complete `code/`, `experiments/`, and `results/` inventories still
contain exactly those six entries.  All nine generated result paths listed
in v2 Section 4.1 remain absent.  The implementation peer review, execution
gate, result review, amendment-v12 target, and former workspace-root v11
stray remain absent.  Package-local `__pycache__`, `.pytest_cache`,
`.mypy_cache`, `.ruff_cache`, pyc, pyo, temporary, editor-swap, and lock
residue remain absent.

These bytes remain quarantine evidence only.  Their unchanged status means
ATTEMPT_3 has not been consumed; it does not make them accepted or frozen.

## 3. Sole normative corrigendum

V2 Section 7 IMPL-08 currently ends with the sentence:

```text
A hand-authored tuple or in-memory field edit is forbidden.
```

That categorical sentence conflicts with amendment-v2 Section 4 A-M2 and
the current review's A-M2/B4 adjudication.  A live `chmod` or `utimens`
operation necessarily covaries `ctime_ns`; the effective design therefore
requires two pure comparator counterfactuals cloned from one actual receipt.

The following text is the complete and exact normative replacement.  It
supersedes only the quoted final sentence of v2 Section 7 IMPL-08:

```text
For IMPL-08 only, the sentence “A hand-authored tuple or in-memory field edit is forbidden.” is superseded by the following text: “Inside test_rep_010, after an actually captured valid whole-root before-receipt Q has compared equal to an actually captured valid whole-root after-receipt, the method shall find exactly one record whose relative path is papers/15-wieferich-ulm-packet-bases/results/valuation_normalization_controls.csv. That record shall be regular and shall have baseline mode 0444; absence, duplication, a non-regular type, or any other captured mode shall fail closed and shall not be replaced by fabricated data. The method shall create Q_mode and Q_mtime as two separate complete deep clones directly from the same immutable Q; neither clone may be derived from or reused as the other, and Q, Q_mode, and Q_mtime shall share no mutable record or container. Q shall remain unchanged. Q_mode shall change exactly the selected record’s mode from 0444 to 0644. Q_mtime shall change exactly the selected record’s mtime_ns from t to t+1000000000. Record order, inventory, and every other record and coordinate—including ctime_ns—shall remain identical. Before either subject-comparator call, a separate independent tuple-difference oracle shall enumerate the complete (relative_path, coordinate, before, after) difference set; it shall not call, reuse, or derive any result from the subject comparator, and it shall prove exactly {(selected_path, mode, 0444, 0644)} for Q versus Q_mode and exactly {(selected_path, mtime_ns, t, t+1000000000)} for Q versus Q_mtime. The subject comparator shall then compare Q with the corresponding clone and shall exact-typed reject each comparison with E_VERIFY_ONLY_METADATA. A whole receipt or selected record detached from, canned independently of, or hand-authored instead of Q; mutation of Q; shared mutable aliasing; clone reuse; an expected-detector lookup; a canned rejection; a live chmod/utimens or other filesystem side effect used for either pure probe; or reliance on ctime_ns or any other covariate to supply the rejection remains forbidden. These two exact in-memory clone transformations derived from Q are required, not forbidden.”
```

The following interpretation is also exact and mandatory:

```text
For IMPL-08 only, Section 7’s prohibition on same-process simulation does not prohibit these two effective-design-authorized pure-comparator counterfactuals. They establish comparator coordinate sensitivity only; they are not live-filesystem collection, process-boundary, runtime-profile, platform, or execution evidence, and they do not replace any separately required live-filesystem receipt variant or external receipt.
```

No other v2 sentence, matrix row, source responsibility, acceptance floor,
evidence class, or authority changes.  In particular:

1. the first sentence of v2 IMPL-08 remains operative;
2. all five live-filesystem receipt variants and every external receipt remain
   mandatory;
3. all other forty-two IMPL rows remain verbatim operative;
4. the source-to-effective-design rewrite plan, sole-author transaction,
   static-only check set, stable source freeze, fresh independent static
   review, and separate execution-gate requirements remain operative; and
5. these two model-level comparator probes prove only selected-coordinate
   sensitivity and cannot be counted as filesystem, process, platform,
   profile, or execution evidence.

## 4. Narrow successor integration

The owner decision authorizing this v3 issuance narrowly supersedes v2's
`future-governance-path absence` and `sole next permitted action` fences only
as needed to create this exact previously absent v3 path and bind its stable
external receipt.  This is a mechanical successor-admission carve-out, not a
second substantive correction.

After the v3 stable receipt exists:

1. v2 and v3 form one ordered governance pair, with v3 later and controlling
   only for the conflict identified in Section 3;
2. v2's pre-write admission sequence again becomes the sole next permitted
   source-side action;
3. the external rewrite plan, every implementation-author intake and
   before/after receipt, the final six-source freeze, the fresh independent
   static review, and any future execution-gate intake must bind both the
   exact v2 receipt and the exact external v3 receipt;
4. any v2 phrase requiring `this gate` or the v2 gate receipt in those
   downstream bindings means the ordered v2-plus-v3 governance pair; and
5. every other v2 absence or drift predicate remains unchanged.

A missing, partial, self-predicted, stale, copied, or unstable v3 receipt
admits no source author.  Any v3 byte, path, type, mode, nlink, or receipt
drift after the external stable receipt is a STOP requiring another owner
decision.  V3 cannot retrospectively reset or unconsume a source mutation.

This v3 note is not a seventh source, one of the nine generated members, an
authority binding, a manifest member or schema field, a DAG node or edge, a
design amendment, a source freeze, a static implementation review, a runtime
profile object, or a run receipt.  The manifest remains at fourteen bindings,
eight nodes, and twelve distinct edges.  The historical original
implementation gate remains the serialized `implementation_gate` provenance;
v2 and v3 are bound externally by later governance and never serialized as a
fifteenth or sixteenth binding.

## 5. Attempt accounting and authority matrix

```text
P15R_CONTROL_IMPLEMENTATION_REMEDIATION_GATE=P15R-P2-CONTROL-IMPLEMENTATION-REMEDIATION-GATE-v3.0
GATE_ROLE=V2_IMPL_08_CORRIGENDUM_ONLY
GATE_VERDICT=PASS_AFTER_EXTERNAL_STABLE_V3_RECEIPT
V3_SUPERSESSION_SCOPE=V2_SECTION_7_IMPL_08_CONFLICT_ONLY
V2_FROZEN_RECORD_MODIFICATION_AUTHORIZED=false
V2_OTHER_CLAUSES_VERBATIM_OPERATIVE=true
V2_OTHER_IMPL_ROWS_OPERATIVE=42

HISTORICAL_ATTEMPTS_CONSUMED=2
V2_NEW_SOURCE_ATTEMPTS_AUTHORIZED=1
V3_IS_SOURCE_ATTEMPT=false
V3_ADDITIONAL_SOURCE_ATTEMPTS_AUTHORIZED=0
ATTEMPT_3_CONSUMED_AT_V3_ISSUANCE=false
ATTEMPT_3_REMAINS_SOLE_AUTHORIZED_FUTURE_SOURCE_TRANSACTION=true
V3_RESETS_OR_REPLENISHES_ATTEMPT_3=false
ATTEMPT_4_AUTHORIZED=false
TOTAL_AFTER_FIRST_ATTEMPT_3_SOURCE_WRITE=3

V3_STABLE_RECEIPT_REQUIRED_BEFORE_AUTHOR_ADMISSION=true
V2_AND_V3_RECEIPTS_REQUIRED_FOR_REWRITE_PLAN=true
V2_AND_V3_RECEIPTS_REQUIRED_FOR_SOURCE_FREEZE=true
V2_AND_V3_RECEIPTS_REQUIRED_FOR_STATIC_REVIEW=true
V2_AND_V3_RECEIPTS_REQUIRED_FOR_EXECUTION_GATE=true

V3_IS_SEVENTH_SOURCE=false
V3_IS_GENERATED_MEMBER=false
V3_IS_MANIFEST_MEMBER=false
V3_IS_AUTHORITY_BINDING=false
V3_IS_DAG_NODE_OR_EDGE=false
MANIFEST_AUTHORITY_BINDINGS=14
MANIFEST_DAG_NODES=8
MANIFEST_DAG_DISTINCT_EDGES=12

CURRENT_PROVISIONAL_SOURCE_QUARANTINED=true
CURRENT_PROVISIONAL_SOURCE_ACCEPTED=false
CURRENT_PROVISIONAL_SOURCE_FROZEN=false
CURRENT_PROVISIONAL_SOURCE_REVIEW_ADMITTED=false

CURRENT_RUN_PROFILE_ACCEPTED=false
CURRENT_RUNTIME_ATTESTATION_PRESENT=false
CURRENT_PLATFORM_AVAILABILITY_CLAIM=false
CURRENT_EXECUTION_AUTHORITY=false
PLATFORM_PREFLIGHT_AUTHORIZED=false
PLATFORM_RUNTIME_PROBE_AUTHORIZED=false
GENERATED_ARTIFACT_MATERIALIZATION_AUTHORIZED=false
GENERATOR_EXECUTION_AUTHORIZED=false
VERIFY_ONLY_EXECUTION_AUTHORIZED=false
UNITTEST_EXECUTION_AUTHORIZED=false
TOP_LEVEL_WRAPPER_EXECUTION_AUTHORIZED=false
CONTROL_EXECUTION_AUTHORIZED=false
REPRODUCTION_RUN_AUTHORIZED=false
AUTHOR_TOP_LEVEL_RUN_ATTEMPTS_AUTHORIZED=0
INDEPENDENT_TOP_LEVEL_RUN_ATTEMPTS_AUTHORIZED=0

DESIGN_CHANGE_AUTHORIZED=false
SOURCE_WRITE_AUTHORIZED_BY_V3_ALONE=false
POST_FREEZE_PATCH_AUTHORIZED=false
AUTOMATIC_RETRY_AUTHORIZED=false
FALLBACK_AUTHORIZED=false
PROOF_MODIFICATION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
ARCHIVE_AUTHORIZED=false
GIT_OPERATION_AUTHORIZED=false
```

Final governance determination: the confirmed IMPL-08 Major is closed only
by reading frozen v2 together with this exact v3 corrigendum after an external
stable v3 receipt.  The correction does not change the effective design; it
restores the gate to amendment-v2 A-M2 and the current review's A-M2/B4
adjudication.  ATTEMPT_3 remains the one authorized future source transaction
and remains unconsumed until its first source content, metadata, link, rename,
or entry mutation.  All static-review and execution separations remain false
until their existing v2 prerequisites and separate authorities are satisfied.
