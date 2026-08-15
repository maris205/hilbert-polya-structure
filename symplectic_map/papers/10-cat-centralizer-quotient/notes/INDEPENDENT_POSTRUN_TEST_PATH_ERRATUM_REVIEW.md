# Independent review of the Paper 10 post-run test-path erratum

Review date: 2026-08-15 UTC  
Candidate: `cat_centralizer_cyclic_torsor_v1`  
Review scope: notes-only, immutable-chain-external correction of one manifest
metadata path  
Verdict: **ERRATUM_PASS**  
Batch disposition: **BATCH_METADATA_BLOCKER_CLOSED**

## Canonical review authority

The following prefix occurs exactly once. The JSON object is canonical UTF-8
on one line with keys in lexical order. It binds the reviewed erratum and the
preserved historical manifest, not this review file's own SHA-256.

CENTRALIZER_POSTRUN_TEST_PATH_ERRATUM_REVIEW_V1 {"affected_json_pointer":"/postrun_audit/gates/postrun_tests/path","batch_integrity_disposition":"BATCH_METADATA_BLOCKER_CLOSED","candidate_id":"cat_centralizer_cyclic_torsor_v1","erratum_path":"notes/POSTRUN_TEST_PATH_ERRATUM_V2.md","erratum_sha256":"c433451ef942f0e88af8441ed2117e2e9933dac097f48a4516e3bbf5f216833b","historical_manifest_path":"results/result_manifest.json","historical_manifest_sha256":"db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658","immutable_chain_mutated":false,"independent_reviewer":true,"paper11_reopen_required":false,"remaining_blocker":"NONE","review_scope":"NOTES_ONLY_IMMUTABLE_CHAIN_EXTERNAL","scientific_impact":"NONE","verdict":"ERRATUM_PASS"}

## Review constraints and method

I treated every original Paper 10 code, result, experiment, paper, and review
artifact, and every Paper 11 binding, as read-only. I did not import or execute
the candidate, run the registered audit, run any test, invoke a result or
manifest builder, or use the network. I used only independent byte hashing,
strict data parsing, XML parsing, source inspection, and inventory comparison.
This review note is the sole write.

The review was fail-closed: a wrong erratum hash, non-canonical or duplicate
machine record, ambiguous correction scope, unmatched file digest, unexplained
generator behavior, changed immutable artifact, changed inventory, or broken
Paper 11 binding would have produced `ERRATUM_FAIL`.

## Erratum identity and machine-record checks

| Check | Independently observed | Result |
|---|---|---|
| Complete erratum SHA-256 | `c433451ef942f0e88af8441ed2117e2e9933dac097f48a4516e3bbf5f216833b` | exact |
| Authority prefix occurrences | 1 | PASS |
| UTF-8 decoding | strict | PASS |
| JSON parsing | strict; no duplicate keys, float, or non-finite value | PASS |
| Canonical serialization | byte-exact one-line JSON with lexical key order and compact separators | PASS |
| Self-hash design | erratum excludes its own digest; this review binds it externally | PASS |
| Pending-review field in erratum | `independent_erratum_review_verdict: null` | correct pre-review state |

The canonical erratum record identifies exactly one affected pointer, preserves
the historical object and digest, and declares a metadata-only supersession.
It does not claim its own independent verdict.

## Exact manifest defect and correction

The historical manifest remains byte-exact at SHA-256
`db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658`.
Strict parsing with duplicate-key rejection confirms the affected object is:

| JSON pointer | Historical value | Correct interpretation |
|---|---|---|
| `/postrun_audit/gates/postrun_tests/path` | `results/PRE_EXECUTION_TESTS.xml` | `results/POSTRUN_TESTS.xml` |

The sibling pointer
`/postrun_audit/gates/postrun_tests/sha256` already contains
`c0124c04106ba81c12ad89814e1547d6e16d3f7eb1f9864d21ec0178ca7e8195`,
which independently reproduces from the actual post-run JUnit file. The two
JUnit artifacts are distinct and correctly hash as follows:

| Role | Path | SHA-256 | Parsed totals |
|---|---|---|---|
| pre-execution | `results/PRE_EXECUTION_TESTS.xml` | `5a5b82c5aaed3dd5aca2c180bd4d1bf589e3b9a8ae4cc3dc9bf30cb04787227b` | 12 tests; 0 failures, 0 errors, 0 skips |
| post-run | `results/POSTRUN_TESTS.xml` | `c0124c04106ba81c12ad89814e1547d6e16d3f7eb1f9864d21ec0178ca7e8195` | 12 tests; 0 failures, 0 errors, 0 skips |

Both files contain the exact same required set of 12 test names, but their
bytes and digests differ. The affected gate therefore read and hashed the
post-run artifact; only its serialized path label is stale. Its stage, totals,
required-test receipt, empty error list, and `pass: true` remain supported.
No second JSON pointer requires correction.

## Frozen generator root cause

I independently reproduced the length-framed 30-file reviewed-tree digest as
`87b08f11fc67eae47bdf745f8286700376f3debc5ac3fd190075a5fa2632f436`;
the code inventory is exact. The three relevant source-file hashes also match
the erratum:

| Source | SHA-256 | Verified behavior |
|---|---|---|
| `code/centralizer_q/gates.py` | `e2fa657da47dded5b27c130c737b4894def43520e89869782c6c0fd5267c0fa1` | line 134 defines `parse_junit(path)`; line 164 serializes `PREEXECUTION_TEST_PATH`; line 165 hashes the supplied `path` |
| `code/centralizer_q/manifest.py` | `e225ecfed583c809d752e64f264bb87e88ea8047ae3105f3173bb1dbc5ae343f` | line 494 passes `root / POSTRUN_TEST_PATH`; line 495 changes only the stage label |
| `code/centralizer_q/constants.py` | `f818eda3966578755d95257671c3cb4ca6cb223f07d0c49d0bf28173f05077ef` | line 135 defines the PRE path and line 141 defines the POST path |

This establishes the stated root cause without executing frozen code:
`parse_junit` consumed and hashed the correct caller-supplied POST file, while
its output path field used the hard-coded PRE constant; the manifest collector
did not replace that field.

## Top-level file records and closed result inventory

The historical top-level file records are already correct:

- `/files/5` is `results/POSTRUN_TESTS.xml` with SHA-256
  `c0124c04106ba81c12ad89814e1547d6e16d3f7eb1f9864d21ec0178ca7e8195`.
- `/files/7` is `results/PRE_EXECUTION_TESTS.xml` with SHA-256
  `5a5b82c5aaed3dd5aca2c180bd4d1bf589e3b9a8ae4cc3dc9bf30cb04787227b`.

All ten top-level `/files` records reproduce against their live artifacts. The
live `results/` directory contains exactly the nine regular files in
`/result_inventory/final_files`, and its eight-file manifest-excluded set is
exactly `/result_inventory/prewrite_files`. There is no nonregular entry. The
erratum and this review live under `notes/`, so neither belongs in the closed
historical result inventory or manifest.

## Immutable scientific, review, and publication chain

The objects relevant to scientific meaning and publication remain byte-exact:

| Artifact | SHA-256 | Status |
|---|---|---|
| `experiments/source_lock.json` | `aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2` | unchanged |
| `results/EXPERIMENT_RESULTS.json` | `8dceb1b8a63db462c1fd55a242ea35de974f73b6c80da68517b91c9eebb214ff` | unchanged raw scientific result |
| `results/INDEPENDENT_RESULT_INTEGRITY.md` | `29264a8fd97d3acf4435ed807294bffcda0844a48728d8572083d92a3bcf5b58` | unchanged `RESULT_PASS` authority |
| `paper/manuscript.tex` | `65bd460ac888ff5527f4401696788034973c3f97a532ee8a34184ce05fae72a6` | unchanged manuscript source |
| `paper/reviews/round2_review.md` | `ca8ee460f0956eb2f653e837402888b9d88d4888ae04ea1ad76231b6764a79ae` | unchanged `PASS -- MAY FINALIZE` review |
| `paper/paper_final.pdf` | `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378` | unchanged final paper |
| `paper/FINAL_INTEGRITY.md` | `e0a4803ff8e2063ebf5766803212579b44cd80c15572b166c1389f0242f8e6ce` | unchanged terminal integrity record |
| `paper/PIPELINE_STATE.json` | `dc7550b39e42cdeeeacd4ae64f9fb4142b0f2e2e4b315d0e73f1932077e0b09c` | unchanged terminal state |

The raw result still reports one registered exact audit, zero candidate
numerical runs, and `pass: true`. The historical manifest still reports one
registered exact audit, zero candidate numerical runs,
`candidate_rerun_performed: false`, and `pass: true`. The terminal scientific
classification remains exactly:

`CENTRALIZER_CYCLIC_TORSOR_CERTIFIED / A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.

No scientific rerun or immutable-chain mutation is required or authorized.

## Paper 11 downstream bindings

Paper 11's source lock and frozen constants each contain 11 Paper 10 bindings.
I recomputed every bound artifact; all 11 of 11 match in both binding maps. In
particular:

- `papers/11-cat-equivariant-clock/experiments/source_lock.json:79-80` binds
  the historical manifest path and whole-file SHA-256
  `db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658`;
- `papers/11-cat-equivariant-clock/code/equivariant_clock/constants.py:115-117`
  binds the same path and digest; and
- the same maps separately bind the unchanged raw result, independent result
  review, official reports, final PDF, Round-2 review, final integrity record,
  and terminal pipeline state.

Paper 11 validates those upstream objects by their preserved whole-file hashes
and inherits the scientific theorem and raw ledger separately. It does not
depend on replacing the historical manifest or on treating the stale nested
path label as scientific data. Therefore the external pointer supersession
does not invalidate a Paper 11 source lock, code tree, execution, result,
manifest, review, or manuscript artifact. `paper11_reopen_required` is false.

## Impact classification and residual condition

- **Metadata impact:** one path label at one JSON pointer is wrong in the
  immutable historical manifest. The sibling digest, parsed test contents,
  gate totals, top-level file records, and inventories identify the correct
  POST artifact.
- **Scientific impact:** **NONE**. No datum, modulus, row, count, orbit,
  quotient, classification, or test outcome changes.
- **Review impact:** **NONE**. The independent result review and manuscript
  review bytes and their scientific conclusions remain unchanged.
- **Publication impact:** **NONE**. The manuscript source, final PDF, final
  integrity record, and pipeline state remain unchanged.
- **Downstream Paper 11 impact:** **NONE**. Its hash bindings remain exact and
  need no reopening.
- **Immutable-chain impact:** **NONE**. The historical manifest is preserved;
  the erratum supersedes only interpretation of the named pointer.

The residual condition is explicit: a consumer that reads the historical
manifest without its co-distributed erratum will still see the stale PRE path
label. That discoverability requirement is not an unresolved integrity blocker
in the reviewed package because the V2 erratum gives a unique canonical
machine record and this independent authority binds its exact digest. The
erratum and this review must accompany the historical manifest wherever that
nested field is interpreted.

## Final decision

The V2 notes-only supersession is precise, machine-readable, hash-bound, and
sufficient to correct the sole metadata interpretation defect while preserving
the immutable evidence chain. No scientific, result-review, publication, or
Paper 11 artifact needs mutation or reopening.

**Final verdict: `ERRATUM_PASS / BATCH_METADATA_BLOCKER_CLOSED`.**  
**Remaining blocker: `NONE`.**
