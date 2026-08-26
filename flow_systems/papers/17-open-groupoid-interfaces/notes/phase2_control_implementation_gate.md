# Paper 17 Phase-2 exact control-implementation gate

Date: **2026-08-16 (Asia/Shanghai)**  
Decision: **PASS TO ONE BOUNDED CONTROL IMPLEMENTATION AND SERIALIZED RUN**  
Gate findings: **C0 / M0 / m0**  
Effective control-design review: **PASS C0/M0/m0**  
Publication disposition: **Technical Note candidate; unchanged**  
`route_b_invocation_allowed: false`

## 1. Decision and narrow authority

Every stable input in Section 2 was rehashed immediately before this gate
was written. The base-design review's historical M1 is closed by the exact
versioned amendment and append-only closure review. The effective design
`base + amendment v1` is therefore independently reviewed at `C0/M0/m0`.

This gate authorizes only:

1. creation of the five exact implementation files in Section 3;
2. deterministic generation and verification of the nine CSVs and one
   manifest in Section 4; and
3. exactly one externally serialized top-level execution through
   `papers/17-open-groupoid-interfaces/experiments/reproduce.sh`, with the
   complete verify-only, mutation, cache, fresh-generation, byte-identity and
   cleanup contract frozen below.

No symbolic proof, proof edit, source acquisition, theorem interpretation,
standalone promotion, Route A/B, composition, manuscript, figure, citation,
release, archive, Git, or public synchronization is authorized. Any hash,
schema, path, count, ordering, mutation or exit-class drift voids this gate
fail-closed.

## 2. Exact implementation authority tuple

| Artifact | Verified SHA-256 | Receipt |
|---|---|---|
| Papers 14--18 batch amendment v3 | `09d7f23b8a20b2d1bfd45a32f7ef695772f7cec2b9c251b7dd217c6a0b37a4e8` | implementation-gate creation authorized |
| `notes/phase2_control_design_gate.md` | `093ca31fa840b992a105cbfd4911353e3df49ba7e05ae8e43d541059999b6647` | post-proof design authority |
| Paper-9 manuscript | `24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb` | fixed-prime provenance owner |
| `notes/phase2_control_design_lock.md` | `abdc4239077b9c9a82d22ccd86e560bb6fd0850dfcfbb261cf500120555a03aa` | immutable base design |
| `notes/phase2_control_design_amendment_v1.md` | `83c8effb2dc4e79f90ef4c72cf5b8f4b20974dc21af8a02e074e19a231b0970d` | exact concurrency-order repair |
| `notes/phase2_control_design_review.md` | `42d1389171a7c23ed40657ff979a2500a8b3daade2561af54755c0c1c4339326` | final append-only PASS C0/M0/m0 |

The first 15,885 bytes of the final review remain the historical base-only
review with SHA-256
`a3daae0ed8331cc33e8338e60eadb13a0f2833a092b41b844d95893f2e895342`.
Its M1 remains correct for the unamended base alone. The final review binds
amendment v1 and closes that M1 for the effective design; this gate consumes
only that complete final receipt.

The Paper-9 manifestation is exactly:

```text
papers/9-packet-separation/paper/manuscript.tex
```

No other Paper-9 artifact and no Paper-17 proof or proof-review digest may
enter the generated control manifest.

## 3. Exact checked-in implementation write set

Only these five checked-in implementation paths may be created:

```text
papers/17-open-groupoid-interfaces/code/generate_controls.py
papers/17-open-groupoid-interfaces/code/test_controls.py
papers/17-open-groupoid-interfaces/code/README.md
papers/17-open-groupoid-interfaces/experiments/reproduce.sh
papers/17-open-groupoid-interfaces/experiments/README.md
```

`code/` must contain exactly its three listed regular, single-link files and
`experiments/` exactly its two listed regular, single-link files, except for
the exact owned lock while a reproduction is active. No results README,
helper module, log, transcript, cache or persistent scratch file is
authorized. Runtime scratch may exist only in the two freshly created empty
temporary roots required by Section 7, and both must be removed on success or
failure.

No file under `notes/`, `paper/`, another paper, or an unlisted path may be
changed by implementation or execution.

## 4. Exact generated package and totals

The only generated package, in canonical order, is:

```text
01 papers/17-open-groupoid-interfaces/results/range_first_handedness_controls.csv
02 papers/17-open-groupoid-interfaces/results/action_blind_open_records.csv
03 papers/17-open-groupoid-interfaces/results/connected_disconnected_firewall.csv
04 papers/17-open-groupoid-interfaces/results/domain_guard_controls.csv
05 papers/17-open-groupoid-interfaces/results/quantale_localic_firewall.csv
06 papers/17-open-groupoid-interfaces/results/actual_standard_owner_controls.csv
07 papers/17-open-groupoid-interfaces/results/dilation_strict_marker_controls.csv
08 papers/17-open-groupoid-interfaces/results/fixed_prime_provenance_controls.csv
09 papers/17-open-groupoid-interfaces/results/target_summary.csv
10 papers/17-open-groupoid-interfaces/results/manifest.json
```

The exact reviewed targets are:

```text
DESIGN_SCHEMA=paper17-open-groupoid-controls/1
MANIFEST_SCHEMA=paper17-open-groupoid-controls-manifest/1
PACKAGE_ID=paper17-open-groupoid-controls
CSV_ARTIFACTS=9
GENERATED_ARTIFACTS_INCLUDING_MANIFEST=10
CSV_BODY_ROWS=3436
NONNEGATIVE_CSV_ROWS=3352
EXPLICIT_NEGATIVE_ROWS=84
EXPECTED_NEGATIVES_DETECTED=84
NEGATIVE_FAILURES=0
UNITTEST_METHODS=180
UNITTEST_FAILURES=0
UNITTEST_ERRORS=0
SEMANTIC_MUTATION_CLASSES=48
PACKAGE_MUTATION_CLASSES=42
ISOLATED_MUTATION_METHODS=90
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
```

The ordered CSV header widths remain exactly
`17,16,16,15,18,17,19,17,12`. Adding, removing, renaming, merging or
parametrically hiding a discoverable method or generated artifact is
forbidden.

## 5. Manifest DAG and proof firewall

`results/manifest.json` has exactly the frozen top-level keys, schema,
package ID and semantics from design Section 9.3. Its ordered `bindings`
array has exactly five elements:

```text
1 notes/phase2_control_design_gate.md
  sha256:093ca31fa840b992a105cbfd4911353e3df49ba7e05ae8e43d541059999b6647
2 ../9-packet-separation/paper/manuscript.tex
  sha256:24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb
3 notes/phase2_control_design_lock.md
  sha256:abdc4239077b9c9a82d22ccd86e560bb6fd0850dfcfbb261cf500120555a03aa
4 notes/phase2_control_design_review.md
  sha256:42d1389171a7c23ed40657ff979a2500a8b3daade2561af54755c0c1c4339326
5 notes/phase2_control_implementation_gate.md
  sha256:<externally computed final digest of this file>
```

The angle-bracket line is design notation only. The implementation receives
this gate's externally computed final digest after these bytes are frozen and
must serialize the real lowercase 64-hex value.

The manifest binds the five implementation paths in Section 3, in frozen
order, and the nine CSV artifacts in Section 4, in canonical order, each with
the required byte and SHA fields. The manifest is not an element of
`bindings`, `implementation`, or `artifacts`; it has no self digest or byte
count.

The exact acyclic policy remains:

```text
manifest_self_hash_included=false
manifest_self_entry_included=false
p17_proof_hash_included=false
p17_proof_review_hash_included=false
authority_policy=CONTROL_DESIGN_GATE_INDIRECT_PROOF_AUTHORITY
```

No path, basename, bytes or digest for a P17 proof/proof review is permitted.
The gate supplies indirect upstream authority; the controls remain finite
diagnostics and never become theorem evidence.

## 6. Semantic and mutation requirements

The implementation must preserve every frozen fixture, row family, exact
token, owner, source binding, header, column, row ID, order, scalar
serialization, negative-reason multiplicity and independent-oracle rule from
the effective design.

The verifier may not import generator helpers or accept persisted `PASS`,
detector, reason, summary or manifest tokens as semantic authority. It must
recompute raw CSV semantics before validating `target_summary.csv`, then
validate the manifest last. All 48 semantic and all 42 package mutations must
be isolated and fail for the expected class.

Finite diagnostics do not prove connectedness of the real line, any topos or
quantale equivalence, local compactness, `q_H`, source/localic
reconstruction, non-etaleness, C-star/Haar/trace/determinant structure,
numerical scale, novelty, priority or Route-B eligibility.

## 7. Sole serialized reproduction contract

The only top-level entry is:

```text
papers/17-open-groupoid-interfaces/experiments/reproduce.sh
```

Exactly one top-level run is authorized. It must be externally serialized;
recursive entry, concurrent entry, nested execution and automatic retry are
failures. The effective order at entry is:

```text
recursive guard
  -> deterministic environment and root validation
  -> no-follow exact pre-existing-lock check
  -> all-other cache/residue scan
  -> one atomic mkdir for the exact lock
  -> owned-lock state.
```

The exact lock path is
`experiments/.p17-control-reproduce.lock`. A pre-existing entry of any type
at that path is concurrent exit 3 and is not mutated. Any other
`.p17-control-*` or closed cache/residue entry is exit 5. An entry appearing
between the dedicated check and atomic `mkdir` is exit 3. Only a lock acquired
by the successful `mkdir` is exempt and cleanable.

Every phase must use the frozen deterministic environment including:

```text
LC_ALL=C
LANG=C
TZ=UTC
PYTHONHASHSEED=0
PYTHONDONTWRITEBYTECODE=1
python3 -B
```

The run must, in design order:

1. reject cache, task residue, symlink, multi-link and inventory drift;
2. capture the exact checked-in metadata/byte receipt;
3. run strict read-only verify-only on `results/` and prove the receipt is
   unchanged;
4. create two distinct fresh empty `mktemp -d` roots;
5. generate and independently verify A and B;
6. compare all ten artifacts across checked-in, A and B byte-for-byte;
7. discover and run exactly 180 explicit `unittest` methods;
8. detect all 84 expected negatives with zero negative failures; and
9. repeat all inventory/cache checks, remove A, B and only the owned lock,
   verify their absence and leave no cache or task residue.

No randomness, network, API, ambient clock, host/process identifier,
temporary-root name, absolute path, unordered iteration, locale-dependent
order or binary-floating oracle may affect generated bytes. Failure is never
retried automatically.

## 8. Verify-only and cleanup ceiling

Verify-only may open controlled artifacts only for reading. It may not repair,
rewrite, normalize, touch, chmod, rename, regenerate or update any artifact.
Before/after receipts compare relative path, type, mode, size, nanosecond
modification time, link count and bytes; access time is excluded.

The complete Paper-17 subtree must be free, before and after every phase, of:

```text
__pycache__
*.pyc
*.pyo
.pytest_cache
.mypy_cache
.ruff_cache
unowned .p17-control-* residue
```

Pre-existing residue is rejected, not deleted. Cleanup may remove only the
two exact temporary roots and the exact lock acquired by this invocation.

## 9. Required independent post-run audit

After the one authorized run, a separate independent controls reviewer must
bind this gate externally, the five implementation digests, all ten generated
artifacts including the stable manifest, and the complete run receipt. The
review must independently reconstruct all nine CSVs, all aggregate totals,
all 48/42 mutation classes, the manifest DAG, verify-only immutability,
two-fresh/three-copy byte identity, serialized entry, exit classification,
cleanup and zero-cache/residue state.

The independent review must return `C0/M0/m0` before any later gate consumes
the controls package. This file does not pre-pass that review and authorizes no
control-result interpretation.

## 10. Machine receipt and downstream stop

```text
P17_CONTROL_IMPLEMENTATION_GATE=PASS
FINDINGS=C0/M0/m0
BATCH_AMENDMENT_V3_SHA256=09d7f23b8a20b2d1bfd45a32f7ef695772f7cec2b9c251b7dd217c6a0b37a4e8
CONTROL_DESIGN_GATE_SHA256=093ca31fa840b992a105cbfd4911353e3df49ba7e05ae8e43d541059999b6647
BASE_CONTROL_DESIGN_SHA256=abdc4239077b9c9a82d22ccd86e560bb6fd0850dfcfbb261cf500120555a03aa
CONTROL_DESIGN_AMENDMENT_SHA256=83c8effb2dc4e79f90ef4c72cf5b8f4b20974dc21af8a02e074e19a231b0970d
FINAL_CONTROL_DESIGN_REVIEW_SHA256=42d1389171a7c23ed40657ff979a2500a8b3daade2561af54755c0c1c4339326
INPUT_HASHES_MATCH=true

CONTROL_IMPLEMENTATION_AUTHORIZED=true
CONTROL_EXECUTION_AUTHORIZED=true
AUTHORIZED_IMPLEMENTATION_PATHS=5
CSV_ARTIFACTS=9
GENERATED_ARTIFACTS=10
CSV_BODY_ROWS=3436
NONNEGATIVE_CSV_ROWS=3352
EXPLICIT_NEGATIVES=84
UNITTEST_METHODS=180
SEMANTIC_MUTATION_CLASSES=48
PACKAGE_MUTATION_CLASSES=42
ISOLATED_MUTATION_METHODS=90
VERIFY_ONLY_READ_ONLY_REQUIRED=true
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
SOLE_TOP_LEVEL_REPRODUCE=experiments/reproduce.sh
TOP_LEVEL_RUN_SERIALIZATION_REQUIRED=true
MANIFEST_BINDINGS=5
MANIFEST_SELF_HASH_PRESENT=false
P17_PROOF_HASH_INCLUDED=false
P17_PROOF_REVIEW_HASH_INCLUDED=false

INDEPENDENT_CONTROLS_AUDIT_REQUIRED=true
INDEPENDENT_CONTROLS_AUDIT_PASSED=false
CONTROL_RESULTS_INTERPRETATION_AUTHORIZED=false
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
```

This gate does not embed its own digest. Its final SHA-256 is computed only
after the bytes are frozen and is an external manifest binding and later
controls-audit input.
