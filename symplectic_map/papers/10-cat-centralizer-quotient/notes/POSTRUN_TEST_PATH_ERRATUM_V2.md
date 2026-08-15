# Paper 10 post-run JUnit path metadata erratum (V2)

Status: `READY_FOR_INDEPENDENT_ERRATUM_REVIEW`

This is a notes-only, immutable-chain-external metadata correction. It does
not edit or replace the historical result manifest, any result artifact, the
frozen implementation, the paper, or any Paper 11 artifact. It does not
assert an independent-review verdict.

## Canonical machine record

The following prefix occurs exactly once. The JSON object is canonical
(UTF-8, one line, keys in lexical order) and intentionally excludes this
document's own SHA-256 so that no circular self-hash is created.

CENTRALIZER_POSTRUN_TEST_PATH_ERRATUM_V2 {"affected_json_pointer":"/postrun_audit/gates/postrun_tests/path","candidate_id":"cat_centralizer_cyclic_torsor_v1","correct_path":"results/POSTRUN_TESTS.xml","correct_path_sha256":"c0124c04106ba81c12ad89814e1547d6e16d3f7eb1f9864d21ec0178ca7e8195","erratum_id":"P10_POSTRUN_TEST_PATH_ERRATUM_V2","erroneous_path":"results/PRE_EXECUTION_TESTS.xml","execution_code_sha256":"87b08f11fc67eae47bdf745f8286700376f3debc5ac3fd190075a5fa2632f436","historical_manifest_path":"results/result_manifest.json","historical_manifest_sha256":"db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658","historical_manifest_unchanged":true,"independent_erratum_review_verdict":null,"no_candidate_rerun":true,"no_registered_rerun":true,"no_test_rerun":true,"paper11_reopen_required":false,"pre_execution_test_path":"results/PRE_EXECUTION_TESTS.xml","pre_execution_test_sha256":"5a5b82c5aaed3dd5aca2c180bd4d1bf589e3b9a8ae4cc3dc9bf30cb04787227b","recorded_sibling_sha256":"c0124c04106ba81c12ad89814e1547d6e16d3f7eb1f9864d21ec0178ca7e8195","result_review_unchanged":true,"scientific_raw_unchanged":true,"source_lock_sha256":"aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2","status":"READY_FOR_INDEPENDENT_ERRATUM_REVIEW","supersession_scope":"METADATA_PATH_INTERPRETATION_ONLY","top_level_file_records_correct":true}

An independent reviewer should hash this complete Markdown file externally
and bind that digest in a separate review artifact. This document must not be
edited after that digest is issued.

## Exact correction

The affected historical artifact is
`results/result_manifest.json`, SHA-256
`db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658`.
At JSON pointer `/postrun_audit/gates/postrun_tests/path`, it records:

```text
results/PRE_EXECUTION_TESTS.xml
```

The correct value is:

```text
results/POSTRUN_TESTS.xml
```

The sibling field
`/postrun_audit/gates/postrun_tests/sha256` is already correct. Its recorded
value is
`c0124c04106ba81c12ad89814e1547d6e16d3f7eb1f9864d21ec0178ca7e8195`,
which is the SHA-256 of the actual post-run JUnit file. The two distinct test
artifacts are:

| Role | Path | SHA-256 |
|---|---|---|
| pre-execution JUnit | `results/PRE_EXECUTION_TESTS.xml` | `5a5b82c5aaed3dd5aca2c180bd4d1bf589e3b9a8ae4cc3dc9bf30cb04787227b` |
| post-run JUnit | `results/POSTRUN_TESTS.xml` | `c0124c04106ba81c12ad89814e1547d6e16d3f7eb1f9864d21ec0178ca7e8195` |

The affected post-run gate's other metadata remains unchanged, including its
12 tests, zero failures, zero errors, zero skips, empty error list, and true
gate status. No other JSON pointer is corrected by this erratum.

## Frozen generator root cause

The frozen execution code tree is SHA-256
`87b08f11fc67eae47bdf745f8286700376f3debc5ac3fd190075a5fa2632f436`.
The relevant frozen source files are:

| File | SHA-256 | Exact relevant lines |
|---|---|---|
| `code/centralizer_q/gates.py` | `e2fa657da47dded5b27c130c737b4894def43520e89869782c6c0fd5267c0fa1` | 134 defines `parse_junit(path)`; 164 always emits `PREEXECUTION_TEST_PATH`; 165 hashes the caller-supplied `path` |
| `code/centralizer_q/manifest.py` | `e225ecfed583c809d752e64f264bb87e88ea8047ae3105f3173bb1dbc5ae343f` | 494 passes `root / POSTRUN_TEST_PATH`; 495 overwrites only `stage` |
| `code/centralizer_q/constants.py` | `f818eda3966578755d95257671c3cb4ca6cb223f07d0c49d0bf28173f05077ef` | 135 defines the PRE path; 141 defines the POST path |

Thus `parse_junit` read and hashed the correct POST file, but serialized the
PRE constant into its `path` field. `collect_postrun_audit` changed only the
stage label, so that stale path label entered the historical manifest beside
the correct POST-file digest. This is a path-label metadata defect, not an
artifact-selection or test-execution defect.

## Correct top-level records and inventory

The historical manifest's top-level `/files` records already distinguish the
two files correctly:

- `/files/5` records `results/POSTRUN_TESTS.xml` with SHA-256
  `c0124c04106ba81c12ad89814e1547d6e16d3f7eb1f9864d21ec0178ca7e8195`.
- `/files/7` records `results/PRE_EXECUTION_TESTS.xml` with SHA-256
  `5a5b82c5aaed3dd5aca2c180bd4d1bf589e3b9a8ae4cc3dc9bf30cb04787227b`.

The top-level prewrite/final inventories also name both files correctly. The
historical `results/` exact inventory remains unchanged; this notes-only file
must not be inserted into it or into the historical manifest.

## Supersession and impact boundary

This V2 erratum supersedes only the interpretation of
`/postrun_audit/gates/postrun_tests/path`: consumers must read that one value
as `results/POSTRUN_TESTS.xml` while retaining its already-correct sibling
digest and all other historical manifest fields. It does not supersede the
manifest artifact or its whole-file SHA-256. The manifest remains the
immutable historical object identified by
`db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658`.

Scientific and publication artifacts are unaffected:

| Artifact | SHA-256 | Effect |
|---|---|---|
| `results/EXPERIMENT_RESULTS.json` | `8dceb1b8a63db462c1fd55a242ea35de974f73b6c80da68517b91c9eebb214ff` | unchanged scientific raw result |
| `results/INDEPENDENT_RESULT_INTEGRITY.md` | `29264a8fd97d3acf4435ed807294bffcda0844a48728d8572083d92a3bcf5b58` | unchanged result-integrity review |
| `paper/manuscript.tex` | `65bd460ac888ff5527f4401696788034973c3f97a532ee8a34184ce05fae72a6` | unchanged manuscript source |
| `paper/paper_final.pdf` | `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378` | unchanged final paper |
| `paper/FINAL_INTEGRITY.md` | `e0a4803ff8e2063ebf5766803212579b44cd80c15572b166c1389f0242f8e6ce` | unchanged final integrity record |

The scientific classification remains
`CENTRALIZER_CYCLIC_TORSOR_CERTIFIED / A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.

Paper 11 continues to bind the historical whole-manifest SHA-256 exactly:
`../11-cat-equivariant-clock/experiments/source_lock.json:79-80` and
`../11-cat-equivariant-clock/code/equivariant_clock/constants.py:115-117`
both bind
`db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658`.
Because that historical object and hash are preserved, and because the
scientific raw result is unchanged, Paper 11 does not require source-lock,
execution, result, manifest, or manuscript reopening. No Paper 11 file is
modified by this erratum.

## No-rerun declaration

Creating this notes-only correction performed no candidate execution, no
registered execution, and no test execution. It changed no modulus, row,
control, result, review, manifest, paper, or downstream binding. Its sole
pending action is a fresh independent metadata-erratum review.
