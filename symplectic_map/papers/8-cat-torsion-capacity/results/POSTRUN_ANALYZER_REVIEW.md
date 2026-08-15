# Independent Post-Run Analyzer Review

Date: 2026-08-14 UTC  
Reviewer role: fresh independent, read-only analyzer reviewer  
Verdict: **POSTRUN_ANALYZER_FAIL**

## Bound scope

- Immutable registered-execution tree: `b4441fb68ac42ab1649ee62037fb7cdf741aa9c09a0b0d5cffc4003697caa059`.
- Post-run analyzer tree reviewed: `3434fc93bfcd1018c49f5df3adcb4728fb07173801f27ad06947e39121a2ce2f`.
- Source lock: `87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269dce`.
- I did not invoke the registered candidate, access external prime/zero data, or modify code, source-locked inputs, execution artifacts, either JUnit record, or the pre-execution/code-review authorities.

## Evidence that passed

The six immutable execution hashes exactly match the analyzer constants:

| Role | Observed SHA-256 |
|---|---|
| execution review | `0fe0a5ba625cbbb88bd6ed6a8ff61389a916fd300127a244981fa4643ffa25a6` |
| pre-execution audit | `850cb7cd8eb3ca63dd4e54757e569a66e01f190db0980c8d9682f4931d711883` |
| registered claim | `14b06403bd5a23b533138ccec4962d74910e6e0242abfcf7ac5fe6b3a947a0ee` |
| raw experiment result | `0d8054ad36ad8cdef1496948cf5dd98d6a1a55c186d68124f45a5e6e35bddaa0` |
| registered terminal | `b3a40e9db554ffdc9fe14b654d84f8e918f26fdb47025eb301337b3ecd5fa192` |
| execution-tree post-run JUnit | `2a0844152eea6d9184d374a6e33c3c4be72fce8deb60296c77650027104348cc` |

The result's embedded `pre_execution_gates` are canonically identical to the gates in the claim-bound pre-execution audit. The claim binds that audit's hash. The immutable execution review binds the execution tree and source lock. Live source-lock, upstream-binding, exact-inventory, and executable-isolation checks pass.

`results/pytest.xml` parses as 21/21 passed with all required execution security tests. `results/POSTRUN_ANALYZER_PYTEST.xml` parses as 25/25 passed with all ten required analyzer/security tests. Their distinct hashes are kept in distinct roles.

In isolated copies, the pre-write V2 builder passed, and the following attacks all failed closed: changed, missing, or malformed preflight, claim, terminal, and raw result; changed, missing, or malformed execution/analyzer JUnit evidence; stale/wrong-tree and duplicate analyzer authorities; extra files, extra symlinks, and required-file symlinks in `results/`; and attempted overwrite of the official preflight after the claim. A second registered-lifecycle entry attempt stopped at the existing-artifact guard while `cat_torsion.candidate` remained absent from `sys.modules` before and after, so the candidate was not rerun.

## Blocking finding

`POST_RESULT_FILES` describes only the pre-write `results/` inventory and omits `result_manifest.json`. `write_post_run_manifest` validates that pre-write inventory and then creates the manifest exclusively. There is no function or command that reads an existing V2 manifest and verifies its exact final inventory, recorded file hashes, schema, dual-tree roles, and semantic audit.

The defect reproduces deterministically in an isolated exact copy:

1. Install a canonical passing analyzer authority bound to the two hashes above.
2. `build_post_run_manifest(project_root)` returns `pass: true` before the manifest exists.
3. `write_post_run_manifest(project_root)` creates `results/result_manifest.json`.
4. A subsequent `build_post_run_manifest(project_root)` returns `pass: false` with `RESULT_FILE_INVENTORY_NOT_EXACT`, solely because the just-created manifest is now present.
5. No read-only final-manifest validator exists elsewhere in the code or CLI.

Consequently, the current V2 artifact is a one-shot builder output, not a verifiable final closure. It cannot demonstrate that the actual post-write tree is exactly the tree the manifest purports to certify. This is a release-blocking provenance defect even though the scientific result and immutable execution chain themselves passed review.

Required repair: add a read-only existing-manifest validator with an exact post-write inventory that includes `result_manifest.json`; validate the manifest's exact schema and fields, all recorded hashes and required semantics, both tree authorities/JUnit roles, and reject tampering, missing/extra entries, duplicate paths, unsafe links, and self-record inconsistencies. Keep the builder pre-write check and candidate-rerun prohibition unchanged, then obtain a fresh analyzer-tree review.

CAT_TORSION_POSTRUN_ANALYZER_REVIEW_V1 {"analyzer_code_sha256":"3434fc93bfcd1018c49f5df3adcb4728fb07173801f27ad06947e39121a2ce2f","candidate_id":"cat_torsion_primitive_divisor_capacity_v1","execution_code_sha256":"b4441fb68ac42ab1649ee62037fb7cdf741aa9c09a0b0d5cffc4003697caa059","reviewer_independent":true,"source_lock_sha256":"87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269dce","verdict":"POSTRUN_ANALYZER_FAIL"}
CAT_TORSION_POSTRUN_ANALYZER_REVIEW_V2 {"analyzer_code_sha256":"1aadef8597a641f2fd4e29ec63202942291a22d2552fa966bdb79d771f860f34","candidate_id":"cat_torsion_primitive_divisor_capacity_v1","execution_code_sha256":"b4441fb68ac42ab1649ee62037fb7cdf741aa9c09a0b0d5cffc4003697caa059","review_round":2,"reviewer_independent":true,"source_lock_sha256":"87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269dce","verdict":"POSTRUN_ANALYZER_PASS"}
