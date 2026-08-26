# Paper 13 Phase-3 v2 exact control-implementation gate

Date: **2026-08-15 (Asia/Shanghai)**  
Decision: **PASS TO BOUNDED CONTROL IMPLEMENTATION AND EXECUTION**  
Gate findings: **C0 / M0 / m0**  
Control-design review: **PASS C0/M0/m0**  
Proof and publication disposition: **unchanged and not authorized**  
`route_b_invocation_allowed: false`

## 1. Decision and narrow authority

Every artifact named in Sections 2 and 3 was independently rehashed
immediately before this gate was written.  Every digest matched, and the
retained Phase-2 source ledger reran `12/12 OK`.  The independent v2 design
review returns `PASS C0/M0/m0` on the exact final control-design amendment.
The prerequisite recorded by `notes/phase3_v2_design_gate.md` is therefore
satisfied.

This gate authorizes only:

1. implementation of the exact frozen control package in the six checked-in
   implementation paths listed in Section 4;
2. deterministic generation and verification of the exact twelve CSVs and
   one manifest listed in Section 5; and
3. one externally serialized top-level execution through
   `papers/13-circle-twists/experiments/reproduce.sh`, including its required
   verify-only, fresh-generation, comparison, test, tamper, cache, and cleanup
   phases.

No theorem proof, proof binding, proof interpretation, source work,
standalone decision, Route action, composition, manuscript, citation,
release, Git operation, or public synchronization is authorized.  Any input
hash mismatch, count drift, extra checked-in path, or weakening of a frozen
failure gate voids this authorization fail-closed.

## 2. Exact control-design authorization tuple

| Artifact | Verified SHA-256 | Gate receipt |
|---|---|---|
| `notes/phase3_v2_design_gate.md` | `0094462b1e06cde0cf1fcc3536c608dcd96ef1e9eb0d85a0714df1666b799706` | bounded v2 design authority: MATCH |
| `notes/phase3_control_design_lock.md` | `900c541713b1711bdab7fa0d264355b6d8ee27014094e60eac6aabe38190604c` | immutable v1 base design: MATCH |
| `notes/phase3_control_design_amendment_v1.md` | `5c9caea983b0047c4b16d0437c23b117a6b8150bbeb67b79c60fb9b2ba6a737e` | exact-row v1 closure: MATCH |
| `notes/phase3_control_design_review.md` | `bf56b96e19b682600ed5de43f7df51ef381fe82d4e12363f66cd1e7d2a5a5184` | final amended-v1 PASS C0/M0/m0: MATCH |
| `notes/phase3_control_design_amendment_v2.md` | `0c0113cff7cf7853d2f4e90ab311ace347f0bebbd8bbf36ab38501fd279c54d9` | final frozen v2 design head: MATCH |
| `notes/phase3_control_design_v2_review.md` | `4385b74e81454ab699975a1c0f8217837ae1a7f90a6a220d47eecfdaaeca71c6` | independent v2 design review, PASS C0/M0/m0: MATCH |

The final v1 review is read through its append-only zero-finding closure; its
historical prefix verdict concerns the unamended base alone.  The v2 design
review independently recomputed the schema, all row partitions, package
arithmetic, test allocation, manifest DAG, serialization, and failure gates.
It authorizes no theorem claim, and neither does this gate.

## 3. Unchanged active Phase-1/2 and source tuple

These are the twelve exact upstream paths that the frozen manifest design
inherits from the v1 base.  They were rehashed again for this authorization.

| Binding path | Verified SHA-256 | Receipt |
|---|---|---|
| `notes/research_protocol.md` | `519563a28c3f11e3b3853f6875a84191444a68cd2c032c4cfcf69ca4152d5064` | MATCH |
| `notes/candidate_lock.md` | `8cc0d08971762aa784afe1c844215353f170a75a3c0ab892415458ab010d0266` | MATCH |
| `notes/pipeline_state.md` | `d98bf49d2eb5c1905ea3625251d787b247f3cf19577ff40f8bc0136186280fd5` | MATCH |
| `notes/phase1_amendment_v1.md` | `ea5242ba6a8a1f2f867e8b258abc802fdeaace54db76629f0a9f0629e3e90d27` | MATCH |
| `notes/phase1_final_gate.md` | `8a97a0bedcb048f1c9aa7db18d43bde45b17f1d7e92d38d2eeace688c64aee19` | MATCH |
| `notes/phase2_novelty_search.md` | `444507f623a998152fdc8e427ee8a3f917c11d5823278b110d431dbcacac6eea` | MATCH |
| `notes/phase2_convention_owner_audit.md` | `498830945b10a9213da945710d21b7ea74d9e0747864e23ca6223efc9bb74f52` | MATCH |
| `notes/phase2_framework_source_audit.md` | `b47b1d6319c8419d96ca8679e3ff13b531a58f06a8b14afd95ec11f773345592` | MATCH |
| `notes/phase2_final_review.md` | `ffcfbac5768fc409b3fa9e5df4f3b46a2366f553373664c78f4364d456854cd9` | MATCH |
| `notes/sources/framework_source_manifest.md` | `4712cabd696d6d00205eb1eddd3c0d2dbf6706bfa14c097690a278941128606e` | MATCH |
| `notes/sources/framework_sources.sha256` | `7fe6067bfc8e16e8b0447df295a887d48c2c04fa5ba25c9cca8acc7afade733f` | MATCH; ledger rerun 12/12 OK |
| `notes/sources/.gitignore` | `c36e58e6a0e338579a7be747879a2891b023bfb79a676da58afca5e1b94c86be` | MATCH |

This gate authorizes no acquisition, replacement, retention, or editing of a
source.  The Phase-2 novelty ceiling remains `SUPPORTED_WITHIN_SEARCH` and
has no control or proof meaning.

## 4. Exact checked-in implementation write set

Checked-in implementation writes are authorized only at these six paths:

```text
papers/13-circle-twists/code/generate_controls.py
papers/13-circle-twists/code/test_controls.py
papers/13-circle-twists/code/README.md
papers/13-circle-twists/experiments/reproduce.sh
papers/13-circle-twists/experiments/README.md
papers/13-circle-twists/results/README.md
```

No other checked-in path under `code/`, `experiments/`, or `results/` may be
created or changed except the thirteen exact generated artifacts in Section
5.  No file under `notes/`, `paper/`, another paper, or any other project path
may be changed by the implementation or run.

The implementation must preserve every inherited v1 header, schema, row ID,
literal, oracle, negative reason, tolerance, enumeration order, quoting rule,
and body byte as closed by the v1 base plus amendment.  The v2 delta is only
the reviewed 41-column, 117-body-row
`completion_corona_controls_v2.csv` and the manifest-v2 augmentation.  Any
additional implementation file, helper, generated report, transcript, cache,
or persistent scratch file is outside this authorization.

Runtime scratch is permitted only in the two distinct newly created empty
`mktemp -d` roots required by Section 7.  Both roots must be removed by an
exit trap on success or failure; they are not checked-in artifacts.

## 5. Exact generated artifact set and totals

The twelve authorized CSV artifacts, in canonical artifact order, are:

```text
papers/13-circle-twists/results/nerve_factorization_controls.csv
papers/13-circle-twists/results/circle_multiplier_cocycle_controls.csv
papers/13-circle-twists/results/lift_integer_defect_controls.csv
papers/13-circle-twists/results/gauge_coboundary_controls.csv
papers/13-circle-twists/results/twisted_convolution_controls.csv
papers/13-circle-twists/results/twisted_involution_controls.csv
papers/13-circle-twists/results/completion_gauge_controls.csv
papers/13-circle-twists/results/action_period_nonretention_controls.csv
papers/13-circle-twists/results/negative_domain_controls.csv
papers/13-circle-twists/results/actual_standard_support_transfer_controls.csv
papers/13-circle-twists/results/target_summary.csv
papers/13-circle-twists/results/completion_corona_controls_v2.csv
```

The thirteenth and only other generated artifact is:

```text
papers/13-circle-twists/results/manifest.json
```

The implementation and run must close exactly these reviewed targets:

```text
CSV_ARTIFACTS=12
GENERATED_ARTIFACTS_INCLUDING_MANIFEST=13
V1_CSV_BODY_ROWS_BYTE_IDENTICAL=2548
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

The old `target_summary.csv` remains the immutable v1 snapshot with 2,548
body rows.  It must not be rewritten as the v2 package summary.  The thirteen
summary rows inside `completion_corona_controls_v2.csv` alone describe the
augmented `2665/67/176` package.  Adding, deleting, merging, renaming, or
parametrically hiding a discoverable test method is forbidden.

## 6. Manifest-v2 DAG and proof firewall

`results/manifest.json` must implement exactly the frozen schema
`paper13-circle-twists-controls-manifest/2` and package ID
`paper13-circle-twists-controls-v2`.  Its `design_head` is the externally
computed digest of
`notes/phase3_control_design_amendment_v2.md`, namely
`0c0113cff7cf7853d2f4e90ab311ace347f0bebbd8bbf36ab38501fd279c54d9`.

The canonical `bindings` array remains the exact path-sorted 24-entry union
specified by Sections 2 and 11.1 of the frozen design: the twelve unchanged
Phase-1/2/source paths above and the twelve disjoint v2 authority paths frozen
there.  This implementation gate does not amend that reviewed count or insert
itself into the manifest.  A later independent controls audit must bind this
gate externally alongside the stable manifest.

The manifest must bind:

- the six implementation paths, path-sorted, by relative path, byte count,
  and SHA-256; and
- the twelve CSV artifacts, in canonical artifact order, by relative path,
  schema, column count, body-row count, negative-row count, byte count, and
  SHA-256.

The manifest must not list or hash itself.  Neither summary CSV may contain
its own digest.  The v2 design contains no self-digest, and no implementation
file may contain the manifest digest.  The exact proof block remains:

```text
proof_binding = {
  concurrent_phase3_proof_hash_included: false,
  policy: POST_PROOF_AUDIT_BINDS_SEPARATELY
}
```

No proof path, proof byte count, proof digest, proof-derived oracle value,
non-null concurrent-proof sentinel, or key matching `proof.*sha` is
permitted.  The concurrently developing P13-8A--C proof is not a manifest
input and must not be read to generate an oracle.  Stable proof and stable
controls manifest may meet only as separate immutable inputs to a later
independent integrated audit; the controls manifest is never mutated to add
the proof.

The only allowed dependency direction is:

```text
frozen authorities + frozen v2 design
                  -> six implementation files
                  -> twelve CSV artifacts
                  -> manifest.json

stable proof ------------------+
stable controls manifest ------+-> later independent integrated audit
```

## 7. Sole serialized reproduction contract

The sole top-level entry point is:

```text
papers/13-circle-twists/experiments/reproduce.sh
```

Only one top-level run may execute at a time.  External serialization is
mandatory; recursive entry, nested invocation, concurrent top-level runs,
and automatic retry are failures.  The script must orchestrate the complete
contract in this order:

1. reject prohibited caches or residue in every controlled checked-in root;
2. verify all twelve checked-in CSVs and the checked-in manifest in strict
   read-only `--verify-only` mode before any fresh generation;
3. preserve and compare the checked-in artifacts' bytes and metadata before
   and after verify-only;
4. create two distinct, newly created, empty `mktemp -d` roots;
5. generate fresh A and fresh B independently and verify each independently;
6. compare all thirteen artifacts byte-for-byte across checked-in, fresh A,
   and fresh B;
7. discover and run exactly 176 `unittest` methods, with zero failures and
   zero errors;
8. execute the complete isolated tamper/failure suite, detecting all 67
   registered negative rows with zero negative failures; and
9. recheck cache/residue gates and remove both temporary roots by exit trap
   on either success or failure.

Every phase must run with:

```text
LC_ALL=C
TZ=UTC
PYTHONHASHSEED=0
PYTHONDONTWRITEBYTECODE=1
python3 -B
```

Generated bytes may use no randomness, network state, timestamp, absolute
path, process/host identifier, temporary-root name, unordered map/set order,
binary floating-point oracle, or host-dependent locale/time value.

## 8. Verify-only, tamper, and no-cache requirements

`--verify-only` may open controlled artifacts only for reading.  It may not
repair, rewrite, normalize, touch, chmod, rename, regenerate, or update any
artifact or manifest.  Its before/after receipt must compare relative path,
file type, mode, size, nanosecond modification time, and bytes.  Access time
is excluded because reading may update it.  Any content or metadata change is
a failure.

The isolated tamper suite must reject every failure class frozen by the v1
and v2 designs, including:

- new-CSV content, header, row count, row order, owner token, evidence token,
  negative detector, or package-summary drift;
- any byte drift in the eleven preserved v1 CSV bodies;
- missing or extra CSVs, manifest entries, checked-in files, or directories;
- any authority, design-head, implementation, or artifact digest drift or
  omission;
- a manifest self-entry or self-digest;
- any proof path, proof digest, non-null concurrent-proof sentinel, or
  proof-derived oracle value;
- substitution of historical v1 conditional fixed-prime rows for the v2
  unconditional analytic branch; and
- any verify-only byte or metadata write.

Before and after checked-in verification, each fresh generation, the unit
test run, every isolated failure path, and cleanup, all controlled roots must
be free of:

```text
__pycache__
*.pyc
*.pyo
.pytest_cache
.mypy_cache
```

A pre-existing prohibited cache is rejected, not deleted or ignored.  A
newly created cache or task-temporary residue is a failure.  Cleanup may
remove only the two exact temporary roots created by the run; it may not
silently repair the checked-in tree.  No failure is retried automatically.

## 9. Evidence ceiling and independent post-run audit

A row, test, negative, reproduction, or manifest `PASS` means only that the
finite diagnostic or ledger agrees with the frozen deterministic design.  It
does not prove or support as proof evidence:

- continuum cardinality;
- an arbitrary-index `c0` multiplier identity;
- the component maximal/reduced norm chain;
- the infinite intersection or faithful corona theorem;
- extension of a dense gauge identity through a completion, multiplier, or
  corona quotient; or
- the unconditional fixed-prime theorem.

No control output may be interpreted as novelty, theorem confirmation,
standalone weight, or Route evidence.  Paper 2's lower-bound credit and the
actual/bare/standard/discrete owner firewalls remain unchanged.

After the single complete run, an independent controls audit is mandatory.
It must bind this gate externally, all six stable implementation digests, all
thirteen stable generated artifacts including the manifest, and the exact
run receipts needed to verify `12/13/2665/67/176`, zero test/negative
failures, strict verify-only immutability, two fresh generations, three-way
byte identity, tamper rejection, cleanup, no-cache, and the no-proof/no-self-
hash DAG.  The audit must return zero open Critical, Major, and Minor findings
before any later gate may consume the controls as a stable evidence package.

This gate neither performs nor pre-passes that audit.  Result interpretation
and every downstream action remain fail-closed while the independent audit
is absent or non-PASS.

## 10. Downstream stop and machine receipt

`NOTE_OR_MERGE` remains binding.  The following machine-readable values are
the complete authorization boundary:

```text
PHASE3_V2_CONTROL_IMPLEMENTATION_GATE=PASS
FINDINGS=C0/M0/m0
V2_DESIGN_GATE_SHA256=0094462b1e06cde0cf1fcc3536c608dcd96ef1e9eb0d85a0714df1666b799706
BASE_V1_DESIGN_SHA256=900c541713b1711bdab7fa0d264355b6d8ee27014094e60eac6aabe38190604c
V1_DESIGN_AMENDMENT_SHA256=5c9caea983b0047c4b16d0437c23b117a6b8150bbeb67b79c60fb9b2ba6a737e
FINAL_V1_DESIGN_REVIEW_SHA256=bf56b96e19b682600ed5de43f7df51ef381fe82d4e12363f66cd1e7d2a5a5184
V2_DESIGN_AMENDMENT_SHA256=0c0113cff7cf7853d2f4e90ab311ace347f0bebbd8bbf36ab38501fd279c54d9
V2_DESIGN_REVIEW_SHA256=4385b74e81454ab699975a1c0f8217837ae1a7f90a6a220d47eecfdaaeca71c6
INPUT_HASHES_MATCH=true
RETAINED_SOURCE_LEDGER=12/12_OK
CONTROL_IMPLEMENTATION_AUTHORIZED=true
CONTROL_EXECUTION_AUTHORIZED=true
AUTHORIZED_CHECKED_IN_IMPLEMENTATION_PATHS=6
CSV_ARTIFACTS=12
GENERATED_ARTIFACTS=13
CSV_BODY_ROWS=2665
EXPLICIT_NEGATIVES=67
UNITTEST_METHODS=176
VERIFY_ONLY_READ_ONLY_REQUIRED=true
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
TAMPER_GATES_REQUIRED=true
NO_CACHE_REQUIRED=true
SOLE_TOP_LEVEL_REPRODUCE=experiments/reproduce.sh
TOP_LEVEL_RUN_SERIALIZATION_REQUIRED=true
MANIFEST_BINDINGS_ARRAY_COUNT=24
MANIFEST_SELF_HASH_PRESENT=false
CONCURRENT_PROOF_HASH_INCLUDED=false
PROOF_INTERPRETATION_AUTHORIZED=false
CONTROL_RESULTS_INTERPRETATION_AUTHORIZED=false
INDEPENDENT_CONTROLS_AUDIT_REQUIRED=true
INDEPENDENT_CONTROLS_AUDIT_PASSED=false
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
the bytes are frozen and is an external input to the required post-run
controls audit.

**Final verdict: PASS — C0/M0/m0, authorizing only the exact bounded control
implementation and execution defined above.  Every proof, interpretation,
standalone, Route, composition, manuscript, and release gate remains closed.**
