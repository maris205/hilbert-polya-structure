# Independent Post-run Analyzer Review

Review date: 2026-08-15 UTC.

## Verdict

**ANALYZER_PASS**

The separate Paper-11 post-run analyzer correctly repairs the sole
list-versus-tuple defect that blocked the first manifest attempt, while
preserving the registered execution tree and every registered result artifact
as immutable evidence. Its execution-tree and analyzer-tree authorities are
separate, the repaired K005 boundary requires the exact JSON singleton-list
semantics, the result and analyzer inventories are closed, and the V2 manifest
path is exclusive, one-shot, and read-only after creation.

No blocker was found. No candidate command, registered audit, execution test,
live manifest command, network operation, or external-data operation was run.
The candidate and scientific packages were not imported. Execution-tree files
were treated only as immutable framed-hash inputs; substantive inspection was
limited to `postrun_analyzer/` and the immutable source/result/review artifacts.
This review file is the sole workspace write.

## Bound identities

All identities below were independently recomputed from regular, single-link
files and matched exactly.

| Object | SHA-256 | Status |
|---|---|---|
| source lock v2 | `331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b` | exact |
| immutable registered execution tree | `5ee1918a57fee56a2ca5a117c5749f614efbfd6baed96ae45480d6091a4741eb` | exact |
| separate post-run analyzer tree | `423082f4675a1d41622bcb3d090a2c4c67d4732ff6dc32d0298505d90d5a78c3` | exact and distinct from execution tree |
| analyzer JUnit | `be518a4c54c317d4e1ab95a0bcc90cbca0f1a30458c26c053d2a19376e14464a` | exact; 10/10 |
| deployment-review history | `3cfe1a34677ef5af06d1a8448de74f5d5dc202dc0136ccf51bfd88f3915110c5` | exact; final `DEPLOYMENT_PASS` |
| raw registered result | `bef8aa5d632ed11b1ca58a123bbfe967a5426e2049d862118a373e4c1dc005fe` | exact |
| independent result-integrity review | `c91737c8bf860bd559eebebe08420fc5d095800c47d132381f584e918e714a20` | exact; `RESULT_PASS` |
| pre-execution audit | `429c43d1002b5e51ad60ee7614f3156081f32651972500624d05185694996479` | exact |
| durable registered claim | `c58c9bc93d0e6af2440c163323d7dcc3c098a0c470f0f11bfb31fa98fb82c79f` | exact |
| certified terminal | `e6ec2c40094a933a3b6f18a46afb36df538e84fb8afee9b63ba6ab166acbe983` | exact |
| immutable execution post-run JUnit | `a4bd081c0ac9bd8ab9efca301d01c858e5e90a43e9c2796acc0431d79df0287f` | exact; not rerun |
| official result report | `06f547fdfbbfb3bd51a57041758a49f18acceca9dda8e19967c2364500d64918` | exact |
| official validation report | `754a36c0e2e6b5c5002ecb8b3473d0af0e077b4f5b88da2bc6851bdafad23221` | exact |

The immutable execution chain strict-parses with duplicate-key, floating
value, nonfinite constant, and trailing-data rejection. The preflight records
zero registered audits; the durable claim records the unique
`REGISTERED_RUN_0001`; the terminal binds that claim and the raw-result hash,
ends in `COMPLETED_CERTIFIED`, and records the exact ordered nine-modulus tuple
plus the separately completed structural control. The registered audit count
is one and the candidate numerical-run count is zero.

The deployment review contains exactly one canonical final Round-2 authority
for the bound execution tree, and the result review contains exactly one
canonical `RESULT_PASS` authority for the bound raw result. Duplicate,
noncanonical, stale, or value-altered authority records are rejected.

## Independent dual-tree reconstruction

I independently reproduced the documented unsigned-64-bit length-framed
tree digest rather than accepting the analyzer's printed hashes.

- The execution tree contains exactly 36 framed paths, including an exact
  closed 26-file code inventory in the three directories
  `equivariant_clock`, `scripts`, and `tests`. Its digest is
  `5ee1918a57fee56a2ca5a117c5749f614efbfd6baed96ae45480d6091a4741eb`.
- The analyzer tree contains exactly 12 framed files in the three directories
  `equivariant_clock_postrun`, `scripts`, and `tests`. Its digest is
  `423082f4675a1d41622bcb3d090a2c4c67d4732ff6dc32d0298505d90d5a78c3`.
- No file in either inventory is a symlink, hard link, nested unexpected
  object, or nonregular object. No bytecode cache is present.
- The two hashes differ, and their roles are explicit:
  `IMMUTABLE_REGISTERED_CANDIDATE_EXECUTION` versus
  `POSTRUN_VALIDATOR_ONLY_NO_CANDIDATE_AUTHORITY`.

Static AST inspection of every non-test analyzer executable found no import
of `equivariant_clock`, network/process/dynamic-loader/data-science modules,
no forbidden dynamic call, and no floating literal. Independent safe-audit
processes had no `equivariant_clock` or `equivariant_clock.*` entry in
`sys.modules` before or after hashing, semantic validation, attack checks, or
the isolated manifest lifecycle.

## Exact first-attempt and K005 reproduction

The historical first manifest attempt is recorded as:

| Field | Exact value |
|---|---|
| attempt | `1` |
| builder | `IMMUTABLE_EXECUTION_TREE_V1_BUILDER` |
| state | `FAILED_PREWRITE_NO_FILE` |
| failure code | `CONTROLS_NOT_EXACT_RECOMPUTED_TRUE` |
| manifest created | `false` |
| root cause | `K005_JSON_LIST_COMPARED_TO_PYTHON_TUPLE` |

I reproduced the defect independently with the strict-loaded raw result. JSON
decoding returns each `fixing_group_elements` value as a Python list. The old
predicate compared that value with the tuple
`(expected_a_inverse_power,)`; all 87 enumeration-engine comparisons are
therefore false. The first value is false, `any(...)` is false, and
`all(...)` is false. The raw-result digest remained
`bef8aa5d632ed11b1ca58a123bbfe967a5426e2049d862118a373e4c1dc005fe`
before and after reproduction, and no manifest file was created.

The repaired predicate was then reconstructed without invoking the candidate.
For both engines and every locked row it requires:

1. `fixing_group_elements` has exact type JSON/Python list;
2. the list has length one;
3. its sole element equals `expected_a_inverse_power`; and
4. that expected value is a two-by-two matrix of exact integers.

The per-engine record counts are the exact source orders
`3,4,10,8,5,3,12,12,30`, totaling 87 records per engine and 174 jointly. All
174 corrected checks pass. Tuple substitution, an empty list, an extra
element, a wrong matrix, or a malformed expected matrix is rejected. K005 is
therefore recomputed true using serialized list semantics, not coerced tuple
semantics. The complete stored K001--K012 control dictionary is also required
and recomputed; the immutable execution-chain semantic gate reports no error.

## Analyzer JUnit and independent rerun

The bound JUnit is a regular single-link XML file with exactly the required
ten unique test names and zero failures, errors, or skips. It includes tests
for executable isolation, immutable tree and artifacts, exact legacy failure,
corrected K005 semantics, strict JSON, canonical analyzer authority, analyzer
inventory, immutable chain authorities, prewrite inventory, final closure,
and tamper rejection.

I independently reran only these two analyzer test modules in a copied
temporary project, with plugin autoload and bytecode generation disabled. The
result was `10 passed`, zero failure/error/skip, with the same exact test-name
set. The independently generated JUnit has SHA-256
`a1234cb93e61d6ad814b481fdd46c578d098d03f381022119b12bd27a6568583`;
the byte difference from the frozen JUnit is expected because pytest records
run-specific timing, timestamp, and host metadata. No execution-tree test or
candidate command was run.

## Inventory, authority, and adversarial closure

Before this review file was written, `results/` contained exactly the eight
immutable base-result files plus `POSTRUN_ANALYZER_PYTEST.xml`. It contained no
review authority, no result manifest, no directory, no symlink, and no extra
object. Adding this file produces exactly the prescribed prewrite inventory;
`result_manifest.json` remains absent.

The analyzer's read and inventory boundaries reject all of the following:

| Attack class | Independent result |
|---|---|
| changed immutable raw result | rejected |
| missing analyzer review | rejected |
| extra result file | rejected |
| symlinked analyzer review | rejected |
| duplicate manifest JSON key | rejected |
| duplicate manifest file record | rejected |
| altered execution-tree digest stored in manifest | rejected |
| extra analyzer source file | rejected |
| symlinked analyzer source file | rejected |
| changed analyzer JUnit | rejected as stale authority |
| changed analyzer-review bytes | rejected as stale stored semantics |
| duplicate analyzer authority | rejected |
| changed immutable execution-tree byte | rejected |
| symlinked manifest | rejected |

The strict JSON parser separately rejects duplicate keys, floats, `NaN`,
`Infinity`, and trailing data. Analyzer authority parsing requires one and
only one prefix occurrence, one canonical compact sorted JSON line, the exact
nine-key schema, and exact current execution/result/review/analyzer/JUnit
bindings.

## Isolated one-shot manifest lifecycle

I copied the immutable project to a fresh temporary tree, retained the exact
frozen analyzer JUnit, and inserted a temporary canonical review authority
bound to the exact analyzer and JUnit hashes. The following sequence was
independently reproduced:

1. prewrite composition passed with an empty error list while
   `result_manifest.json` did not exist;
2. the exclusive writer created the manifest exactly once;
3. read-only final closure passed against the exact final inventory and live
   non-self hash records;
4. the manifest hash was unchanged before and after read-only validation;
5. prewrite composition correctly ceased to pass after the manifest entered
   the final inventory; and
6. a second writer invocation raised `FileExistsError`.

The isolated fixture manifest SHA-256 was
`7f0b295ea8cd50f72eaece94798ef7fe1227c260fa7f991f5a2b9d44d7810b08`.
That digest belongs only to the temporary review fixture and is not a live or
release authority. All fourteen attacks in the preceding table were then
applied to independent copies of the closed fixture; every final-closure
verdict was false.

## Scope and authorization boundary

This review certifies only the separate post-run analyzer and its ability to
close the already independently approved immutable result. It does not
re-execute or independently reclassify the scientific candidate, replace the
existing `DEPLOYMENT_PASS` or `RESULT_PASS`, authorize another registered
audit, alter the terminal classification, open Route B, or authorize
manuscript claims beyond the frozen source/result package.

The analyzer is authorized to perform the later single V2 manifest write only
after this exact review authority is present and its complete prewrite gate is
recomputed. This review itself does not create the live manifest.

EQUIVARIANT_CLOCK_POSTRUN_ANALYZER_REVIEW_V1 {"analyzer_junit_sha256":"be518a4c54c317d4e1ab95a0bcc90cbca0f1a30458c26c053d2a19376e14464a","analyzer_tree_sha256":"423082f4675a1d41622bcb3d090a2c4c67d4732ff6dc32d0298505d90d5a78c3","candidate_id":"cat_equivariant_retention_tradeoff_v1","execution_code_sha256":"5ee1918a57fee56a2ca5a117c5749f614efbfd6baed96ae45480d6091a4741eb","registered_result_sha256":"bef8aa5d632ed11b1ca58a123bbfe967a5426e2049d862118a373e4c1dc005fe","result_review_sha256":"c91737c8bf860bd559eebebe08420fc5d095800c47d132381f584e918e714a20","reviewer_independent":true,"source_lock_sha256":"331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b","verdict":"POSTRUN_ANALYZER_PASS"}
