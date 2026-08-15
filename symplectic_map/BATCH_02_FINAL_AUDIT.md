# Batch 02 final independent audit

Audit date: 2026-08-15 UTC  
Batch scope: Papers 7--11  
Audit mode: fresh, fail-closed, local read-only verification  
Verdict: **`BATCH02_FINAL_AUDIT_PASS`**

No batch-integrity blocker remains. All five papers have a hash-closed local
terminal publication state, the Paper-10 post-run JUnit path defect is closed
by a canonical external erratum and a fresh independent `ERRATUM_PASS`, and
Paper 11 plus the three top-level indexes preserve the required scientific
boundaries. No Paper 12 or sixth Batch-02 paper has been opened.

## Canonical machine authority

The following prefix occurs exactly once. The JSON object is canonical UTF-8
on one line with lexical key order and compact separators. It intentionally
does not contain this Markdown file's own SHA-256, avoiding a self-hash cycle.

BATCH02_FINAL_AUDIT_V1 {"advisories":["P7_V1_STATUS_SCHEMA_VARIANT","P8_DUAL_ROLE_JUNIT_HISTORY","P10_EXTERNAL_ERRATUM_MUST_CO_DISTRIBUTE","P11_TERMINAL_FINAL_SUFFIX_AND_HISTORICAL_BASE_NODES","NO_LIVE_EXTERNAL_CITATION_LOOKUP_BY_CONSTRAINT","GIT_METADATA_UNAVAILABLE"],"audit_constraints":{"candidate_rerun_performed":false,"external_data_accessed":false,"git_mutation_performed":false,"network_accessed":false,"registered_rerun_performed":false,"test_rerun_performed":false},"audit_date_utc":"2026-08-15","batch_id":"BATCH_02","batch_input_status":"COMPLETE_LOCAL_PENDING_BATCH_AUDIT","blocker_count":0,"git_sync":{"performed":false,"readiness":"ARTIFACT_READY_GIT_METADATA_UNAVAILABLE"},"indexes":{"batch_status_sha256":"8323e8896f89fcfd8848be0a2c5e20b9ef4214f2815f81a2368a38b56b3dba67","candidate_registry_sha256":"f340196908f5904ae026e1a695cc8f548d885c563e0cfdcc15600ec724cb81a7","obstruction_registry_sha256":"3871ddbfc4bb92ed6983f3337976fe31fb514974cf2ace446812ce96059a32ce","readme_sha256":"070c330dad01005d8a039fad5874ab8e1003dbd91b418dc40ba4b8f3302bb567"},"no_paper12_opened":true,"p10_erratum":{"affected_json_pointer":"/postrun_audit/gates/postrun_tests/path","correct_path":"results/POSTRUN_TESTS.xml","erratum_review_sha256":"62838ef837a17b91414f1e8327d76a7dc114b7b52d6493e5fb88468901bf77ee","erratum_sha256":"c433451ef942f0e88af8441ed2117e2e9933dac097f48a4516e3bbf5f216833b","remaining_blocker":"NONE","verdict":"ERRATUM_PASS"},"p11_dual_tree":{"analyzer_path_count":12,"analyzer_tree_sha256":"423082f4675a1d41622bcb3d090a2c4c67d4732ff6dc32d0298505d90d5a78c3","execution_path_count":36,"execution_tree_sha256":"5ee1918a57fee56a2ca5a117c5749f614efbfd6baed96ae45480d6091a4741eb"},"paper_count":5,"papers":[{"candidate_id":"pcf_quadratic_exact_2adic_boundary_v1","final_integrity_sha256":"78de855be97e81f826d10749d243d08e3d0498136585d5c4a7ccf2a4c89adfab","final_pdf_sha256":"fac4b7a3a5f19f515ebd982a3eef0e3c63e1c025616fbaeb62a94621d19632bf","number":7,"pipeline_path":"paper/PIPELINE_STATE.json","pipeline_sha256":"9dc8b2eb3a97e292bb999b59f812380f7f325673db005b06afd9b82737e91c6b","project":"papers/7-base2-exponent-clock","result_manifest_sha256":"6d9407408437954f52b4a1cb7f0caa50ca00bd22be9cf9a348a1bbb60c9a87e8","result_review_sha256":"f1a39f31ceaa6b4eee1a469c2f8fcb5028a33f6c7ccfcc1cb311b95fc5778c4f","round2_review_sha256":"f9a9937fd439bd5a91df1b45709775615fc1fe7920777488d72e8d1e6cfb62d6","source_lock_sha256":"205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1","status":"COMPLETE_LOCAL_FINAL_REVIEW_PASS"},{"candidate_id":"cat_torsion_primitive_divisor_capacity_v1","final_integrity_sha256":"c7a2dae286ea955b695adb4087488340a45ce5b06cfb911fea6c22121e2c008d","final_pdf_sha256":"5ff37aca10905bd7fd84f25a81e47601ed9883259519b02e2809f77485770d98","number":8,"pipeline_path":"paper/PIPELINE_STATE.json","pipeline_sha256":"00dbea0183cd525f580d845c3b886470692e40a8bc69097b3c4354b6f346492b","project":"papers/8-cat-torsion-capacity","result_manifest_sha256":"045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f","result_review_sha256":"5f544f637ccbe9e9f584cfdd41a3188ab76153670bd5d3cdbc881ea5cbf2229d","round2_review_sha256":"4f0da5c2174b6185a743e8834fa2a3c73b72fc4afa09b811cd730f3ad95f5d95","source_lock_sha256":"87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269dce","status":"COMPLETE_LOCAL_FINAL_REVIEW_PASS"},{"candidate_id":"cat_prime_shell_multiplicity_obstruction_v1","final_integrity_sha256":"7abbf1d25a3d57ccf3f195aa633237d2e641073ba647dcaacd6a177d7c66a712","final_pdf_sha256":"96a560712ae7fb34e1d0ecfcd59e9b2c210ad61fe8ee0537c3a5ff5c860b4cd6","number":9,"pipeline_path":"paper/PIPELINE_STATE.json","pipeline_sha256":"f4876e8dccbd9502af593fa77318dbf0b3c1f60ccef39c6d483d8e0df4a1e922","project":"papers/9-cat-prime-shell-multiplicity","result_manifest_sha256":"8ca12744638a47b6e4fa3239a60a19d79229d2b9596ae4fe4b2f66a399618f92","result_review_sha256":"aa0c7db555f11920c7305be508f6cfff62375970e112e9f720111831da20b3bd","round2_review_sha256":"32cc795c358d979988673658398dd4dbf2768cd9f1b38464b9b438703c2ebd23","source_lock_sha256":"662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49","status":"COMPLETE_LOCAL_FINAL_REVIEW_PASS"},{"candidate_id":"cat_centralizer_cyclic_torsor_v1","final_integrity_sha256":"e0a4803ff8e2063ebf5766803212579b44cd80c15572b166c1389f0242f8e6ce","final_pdf_sha256":"f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378","number":10,"pipeline_path":"paper/PIPELINE_STATE.json","pipeline_sha256":"dc7550b39e42cdeeeacd4ae64f9fb4142b0f2e2e4b315d0e73f1932077e0b09c","project":"papers/10-cat-centralizer-quotient","result_manifest_sha256":"db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658","result_review_sha256":"29264a8fd97d3acf4435ed807294bffcda0844a48728d8572083d92a3bcf5b58","round2_review_sha256":"ca8ee460f0956eb2f653e837402888b9d88d4888ae04ea1ad76231b6764a79ae","source_lock_sha256":"aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2","status":"COMPLETE_LOCAL_FINAL_REVIEW_PASS"},{"candidate_id":"cat_equivariant_retention_tradeoff_v1","final_integrity_sha256":"4433959f41b280d2555958de70201d27770e7cac649339b0474aa564647ef7b1","final_pdf_sha256":"9f9a0a25ba82a56d10980ecafad3be8cc893523fc494e5dd66a9307dd831888b","number":11,"pipeline_path":"paper/PIPELINE_STATE_FINAL.json","pipeline_sha256":"14f396b3c668b8b0fada7d3fdfa305656609bf859f80801d965c9e8b60eadf8c","project":"papers/11-cat-equivariant-clock","result_manifest_sha256":"a0b409061c34eff0d68fdc326fe4ec6ff9295895444b857ee161fd77e417292c","result_review_sha256":"c91737c8bf860bd559eebebe08420fc5d095800c47d132381f584e918e714a20","round2_review_sha256":"093f79564578370992c5e74e7925cd46a07ed00c7abc3561d907d0f12f69a0e0","source_lock_sha256":"331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b","status":"COMPLETE_LOCAL_FINAL_REVIEW_PASS"}],"verdict":"BATCH02_FINAL_AUDIT_PASS"}

## Audit boundary and method

This audit followed the local academic-pipeline integrity and state-machine
rules and the paper-compile post-build verification rules. It independently
read and hashed the current bytes rather than accepting terminal prose as
proof. Checks included strict JSON parsing with duplicate-key rejection,
recursive path/hash resolution, closed inventories, XML parsing of existing
JUnit receipts, static LaTeX/BibTeX closure, PDF metadata/font/text inspection,
byte comparison, and local Markdown-link resolution.

No candidate, registered audit, test suite, post-run analyzer, figure
generator, or LaTeX compiler was executed. No file other than this audit was
created or modified. No network, external prime table, zero data, external
bibliographic API, Git write, or Git synchronization operation was used.

## Five terminal publication identities

Every terminal PDF exists, is nonempty and unencrypted, and is byte-identical
to both `paper_round1_revision.pdf` and live `manuscript.pdf`. Every Round-2
authority binds the observed PDF and returns `PASS / MAY_FINALIZE` (equivalent
punctuation variants included). Each final-integrity record and authoritative
pipeline state carries `COMPLETE_LOCAL_FINAL_REVIEW_PASS`.

| Paper | Final PDF SHA-256 | Round-2 review SHA-256 | FINAL_INTEGRITY SHA-256 | Authoritative pipeline SHA-256 |
|---:|---|---|---|---|
| 7 | `fac4b7a3a5f19f515ebd982a3eef0e3c63e1c025616fbaeb62a94621d19632bf` | `f9a9937fd439bd5a91df1b45709775615fc1fe7920777488d72e8d1e6cfb62d6` | `78de855be97e81f826d10749d243d08e3d0498136585d5c4a7ccf2a4c89adfab` | `9dc8b2eb3a97e292bb999b59f812380f7f325673db005b06afd9b82737e91c6b` |
| 8 | `5ff37aca10905bd7fd84f25a81e47601ed9883259519b02e2809f77485770d98` | `4f0da5c2174b6185a743e8834fa2a3c73b72fc4afa09b811cd730f3ad95f5d95` | `c7a2dae286ea955b695adb4087488340a45ce5b06cfb911fea6c22121e2c008d` | `00dbea0183cd525f580d845c3b886470692e40a8bc69097b3c4354b6f346492b` |
| 9 | `96a560712ae7fb34e1d0ecfcd59e9b2c210ad61fe8ee0537c3a5ff5c860b4cd6` | `32cc795c358d979988673658398dd4dbf2768cd9f1b38464b9b438703c2ebd23` | `7abbf1d25a3d57ccf3f195aa633237d2e641073ba647dcaacd6a177d7c66a712` | `f4876e8dccbd9502af593fa77318dbf0b3c1f60ccef39c6d483d8e0df4a1e922` |
| 10 | `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378` | `ca8ee460f0956eb2f653e837402888b9d88d4888ae04ea1ad76231b6764a79ae` | `e0a4803ff8e2063ebf5766803212579b44cd80c15572b166c1389f0242f8e6ce` | `dc7550b39e42cdeeeacd4ae64f9fb4142b0f2e2e4b315d0e73f1932077e0b09c` |
| 11 | `9f9a0a25ba82a56d10980ecafad3be8cc893523fc494e5dd66a9307dd831888b` | `093f79564578370992c5e74e7925cd46a07ed00c7abc3561d907d0f12f69a0e0` | `4433959f41b280d2555958de70201d27770e7cac649339b0474aa564647ef7b1` | `14f396b3c668b8b0fada7d3fdfa305656609bf859f80801d965c9e8b60eadf8c` |

Paper 11's terminal state is `paper/PIPELINE_STATE_FINAL.json`; its `state`,
`status`, and `final_status` are all exactly
`COMPLETE_LOCAL_FINAL_REVIEW_PASS`. Papers 7--10 use
`paper/PIPELINE_STATE.json`; Paper 7's older V1 schema is discussed under
advisories.

PDF QA reproduced 11, 12, 15, 15, and 19 pages respectively. All PDFs use
letter pages, have zero Type-3 fonts, and have 33, 33, 37, 29, and 39 font
records respectively, all embedded. Extracted text contains no `[VERIFY]`,
`[?]`, or `??` marker. The final Paper-11 PDF contains no reader-facing
`Paper 10` or `Paper 11` internal sequence label.

## Source, result, and base-manifest chain

| Paper | Source lock SHA-256 | Result manifest SHA-256 | Independent result review SHA-256 | Result-review verdict |
|---:|---|---|---|---|
| 7 | `205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1` | `6d9407408437954f52b4a1cb7f0caa50ca00bd22be9cf9a348a1bbb60c9a87e8` | `f1a39f31ceaa6b4eee1a469c2f8fcb5028a33f6c7ccfcc1cb311b95fc5778c4f` | `PASS` |
| 8 | `87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269dce` | `045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f` | `5f544f637ccbe9e9f584cfdd41a3188ab76153670bd5d3cdbc881ea5cbf2229d` | `PAPER8_RESULT_INTEGRITY_PASS` |
| 9 | `662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49` | `8ca12744638a47b6e4fa3239a60a19d79229d2b9596ae4fe4b2f66a399618f92` | `aa0c7db555f11920c7305be508f6cfff62375970e112e9f720111831da20b3bd` | `RESULT_PASS` |
| 10 | `aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2` | `db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658` | `29264a8fd97d3acf4435ed807294bffcda0844a48728d8572083d92a3bcf5b58` | `RESULT_PASS` |
| 11 | `331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b` | `a0b409061c34eff0d68fdc326fe4ec6ff9295895444b857ee161fd77e417292c` | `c91737c8bf860bd559eebebe08420fc5d095800c47d132381f584e918e714a20` | `RESULT_PASS` |

The terminal base nodes also reproduce exactly:

| Paper | Configuration | Claim manifest | Experiment passport | Figure package |
|---:|---|---|---|---|
| 7 | `63f8fb6b034db7de6d26e760d0243c63c079cf59d4452881aea39a3198eb8232` | `1fb3727833dbe9c9aa7fd8cb24cec9d9beb787f5a3cb99ed7ba2dabc768889e5` | `bd525b773182b605ee7bf5bc643223e4822fcc0294d2347b35a5da4db8d0dc39` | `a1f41aa96293807d8d98ddcb50e17b706b741883a99e4570886f8d70fb3683f2` |
| 8 | `38d64ee140b09520f34a73310aabb7634973435d727c06788c0f4eb925a63db9` | `9581ddf7ef1a069960f429e43f38515725c6033c8c18f6c8f25526bda1e97b0a` | `54fd313cc29c620f127c5f205bb95b77344a1f1308ad88b69d3edcf22edb2555` | `cdda5fe5385f4f8005f123dade3047a95df32fd63aebb5484d4e656214c7aa05` |
| 9 | `8c5b0ae01be1c467296c3a18638f3a993170b807eb8a87e9965a6a15dff35a0b` | `09348a2db96f04b85b0a9bd66dead97f64d0724551f9cba65bbb258b5f6caded` | `cc4f48930ff35cdef207bb16cb5db4d13f86888f813d08e5cc47830333145e17` | `c09224620375c5bda053448d4726d4123f1bff6b1519de7a1a89988a348bddf0` |
| 10 | `4231373e4859f32d48a7e397116516df390b5d98d6ca5e0f15e25da71e0295f2` | `b8c1b46158d8dcad8edae9c610ac89bd2c46556a343d242b35cfe53538fa9c80` | `476e9ad9ef290ac30d473079bdf677987abec8170996786536198c39d22f895f` | `23ce51a1c168081b278cffd88af7f76f38f37a56e0ea54c78793f0c339725b9b` |
| 11 (`*_FINAL`) | `569075fed19c49106fc9b59b30274683b58ae9ee53bc5452ef1aed3b6c78e9c5` | `b4d714997f468f69933ce1c16aaa8193e54746388fed0080e062b832e10ae72a` | `79f19bd78304f891ccb54a219ca91e79e31d30b5082977a7a3877ab0b7df7220` | `3e5c2ea6f465c4fafe95bbfae08de323565a394376b2d39f8b93b10e27769297` |

The five `FINAL_INTEGRITY.md` tables supplied 18, 19, 21, 21, and 28
resolvable path/hash rows; every row matched its current byte object. Pipeline
states bind their base nodes without a reverse final-integrity edge, so the
terminal metadata graph is acyclic.

Strict parsing accepted all project JSON files with no duplicate key,
non-finite constant, malformed JSON, or trailing content: 12/12, 11/11,
13/13, 15/15, and 23/23 for Papers 7--11. No project tree contains a symlink
or a multiply-linked regular file.

## Closed result inventories and existing test receipts

| Paper | Exact `results/` inventory | Top-level manifest file records | Existing JUnit receipts parsed, not executed |
|---:|---:|---:|---|
| 7 | 10/10 | 12/12 hashes | 38 tests; 0 failure/error/skip |
| 8 | 11/11 | 14/14 hashes | 21 tests plus analyzer 27; all 0 failure/error/skip |
| 9 | 9/9 | 10/10 hashes | pre 23 and post 23; all 0 failure/error/skip |
| 10 | 9/9 | 10/10 hashes | pre 12 and post 12; all 0 failure/error/skip |
| 11 | 11/11 | 13/13 hashes | pre 16, post 16, analyzer 10; all 0 failure/error/skip |

Every inventory entry is a regular file. There is no missing, extra,
nonregular, symlinked, or hash-mismatched result object. Existing result data
record zero candidate numerical runs and zero candidate reruns. Papers 10 and
11 also record zero network/external-data/prime-data/zero-data accesses; the
earlier papers' corresponding frozen controls likewise remain false/zero.

## Paper 10 metadata erratum closure

The immutable historical manifest remains at SHA-256
`db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658`.
At `/postrun_audit/gates/postrun_tests/path` it carries the stale value
`results/PRE_EXECUTION_TESTS.xml`, while its sibling digest is
`c0124c04106ba81c12ad89814e1547d6e16d3f7eb1f9864d21ec0178ca7e8195`,
the actual SHA-256 of `results/POSTRUN_TESTS.xml`. The real pre-execution file
instead hashes to
`5a5b82c5aaed3dd5aca2c180bd4d1bf589e3b9a8ae4cc3dc9bf30cb04787227b`.

The notes-only erratum
`notes/POSTRUN_TEST_PATH_ERRATUM_V2.md` hashes to
`c433451ef942f0e88af8441ed2117e2e9933dac097f48a4516e3bbf5f216833b`.
Its unique canonical record parses with duplicate-key rejection and supplies
exactly the effective correction `results/POSTRUN_TESTS.xml`. The fresh
independent review
`notes/INDEPENDENT_POSTRUN_TEST_PATH_ERRATUM_REVIEW.md` hashes to
`62838ef837a17b91414f1e8327d76a7dc114b7b52d6493e5fb88468901bf77ee`
and returns `ERRATUM_PASS / BATCH_METADATA_BLOCKER_CLOSED`, with
`remaining_blocker: NONE`.

Static source inspection independently confirms the frozen root cause:
`parse_junit(path)` hashes its caller-supplied path but serializes the PRE
constant; the post-run collector passes the POST path and replaces only the
stage. The manifest's top-level PRE and POST records are already correct, both
JUnit files parse as 12/12 passing receipts, and the nine-file result inventory
is unchanged. The erratum and review live under `notes/` and therefore do not
mutate the historical result inventory, final PDF, result review, pipeline, or
Paper-11 whole-file upstream bindings.

This closes the former batch blocker as an external pointer supersession. A
consumer interpreting that nested historical field must co-distribute and
apply the erratum and its independent review; silently consuming the old
manifest alone would still expose the stale label.

## Paper 11 special closure

### Scope and classification

The raw exact ledger contains the ordered tuples

`(q,n_q,r_q,m_q) = (2,3,3,1), (3,8,4,2), (5,20,10,2), (7,48,8,6),`
`(11,100,5,20), (4,12,3,4), (6,24,12,2), (9,72,12,6),`
`(10,60,30,2)`.

Thus the `q=2` point-cardinality factor is exactly `(1-t^3)^(-1)` and is
the unique locked row/type pair with source support and unit exponent. The
collision `r_2=r_4=3` prevents that local exception from identifying the
modulus. Source audit, terminal claim manifest, final manuscript, figures,
Round 2, and final integrity all use the family-uniform conclusion: no single
audited reduction supplies a common intrinsic modulus/prime clock across all
nine rows. They do not restore the rejected exception-free per-row claim or
promote the finite ledger to an all-`q` theorem. The terminal classification
is
`EQUIVARIANT_RETENTION_COMPRESSION_TRADEOFF_CERTIFIED /
A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.

### Walton publication layer

The terminal bibliography and final manuscript consistently give Laura
Walton's record as *Journal of Number Theory* **192** (2018), 386--405,
DOI `10.1016/j.jnt.2018.03.023`. The frozen design-side 189/202--223
transcription is explicitly disclosed as immutable historical provenance and
is not used for a scientific inference. Walton remains a finite-field
quotient/twist scope boundary; the manuscript claims neither an extension to
composite residue rings nor an implementation of Walton's theorem.

### Dual-tree evidence

Independent static reconstruction of the documented length-framed hash gave:

- immutable registered execution tree: 36 closed paths,
  `5ee1918a57fee56a2ca5a117c5749f614efbfd6baed96ae45480d6091a4741eb`;
- separate post-run analyzer tree: 12 closed paths,
  `423082f4675a1d41622bcb3d090a2c4c67d4732ff6dc32d0298505d90d5a78c3`.

Both inventories are exact and role-distinct. The execution tree is the
registered candidate authority; the analyzer is validator-only and carries no
candidate authority. The V2 result manifest, analyzer review, independent
result review, terminal base nodes, and final-integrity record bind these same
digests.

## Figures, citations, and static manuscript closure

Each manuscript resolves all three referenced final figures. Paper 7's figure
manifest has `pass=true`, twenty tracked artifacts, and a byte-identical
determinism record. Papers 8--11 each have a `PASS` figure manifest with three
figure stems in PDF/PNG/SVG (nine live output hashes); all output, source,
planning, provenance, asset-tree, and determinism hashes inspected in their
terminal packages match.

Static citation closure is exact:

| Paper | Cited keys / BibTeX keys | Missing or unused keys | Labels | Referenced targets | Missing targets |
|---:|---:|---:|---:|---:|---:|
| 7 | 12/12 | 0/0 | 40 | 30 | 0 |
| 8 | 14/14 | 0/0 | 34 | 17 | 0 |
| 9 | 11/11 | 0/0 | 44 | 20 | 0 |
| 10 | 14/14 | 0/0 | 56 | 31 | 0 |
| 11 | 14/14 | 0/0 | 65 | 40 | 0 |

Current LaTeX and BibTeX logs contain no fatal error, undefined citation,
undefined reference, or malformed-BibTeX diagnostic. Fresh online reference
lookup was intentionally not performed because this audit was prohibited from
using the network; the frozen citation-verification packages and terminal
publication-layer consistency were checked locally.

## Top-level indexes and batch boundary

| Index | SHA-256 | Audit result |
|---|---|---|
| `README.md` | `070c330dad01005d8a039fad5874ab8e1003dbd91b418dc40ba4b8f3302bb567` | Papers 7--11 present; scientific boundaries accurate |
| `docs/candidate_registry.md` | `f340196908f5904ae026e1a695cc8f548d885c563e0cfdcc15600ec724cb81a7` | five candidate IDs and Route outcomes accurate; all local links resolve |
| `docs/obstruction_registry.md` | `3871ddbfc4bb92ed6983f3337976fe31fb514974cf2ace446812ce96059a32ce` | O9--O13 preserve theorem scope; all local links resolve |
| `BATCH_02_STATUS.md` | `8323e8896f89fcfd8848be0a2c5e20b9ef4214f2815f81a2368a38b56b3dba67` | five queue rows final/complete; P10 erratum and P11 terminal log exact |

The indexes preserve the decisive boundaries: Paper 7's arbitrary-`n>=4`
equality tail remains open; Paper 8 is a proves-too-much/nonlocal capacity
result; Paper 9 is scalar-scope multiplicity with only a global tautological
normalization; Paper 10's full-centralizer compression kills native period and
still requires an external `q` label; Paper 11's conclusion is family-uniform
and explicitly retains the `q=2` exception.

The Batch status `COMPLETE_LOCAL_PENDING_BATCH_AUDIT` was correct at audit
entry. Under the sole-write constraint it was not edited; this file's
canonical `BATCH02_FINAL_AUDIT_PASS` authority now records completion of that
pending audit. The `papers/` tree has no `12-*` directory, the indexes have no
Paper-12/O14/candidate-12 entry, and the batch log explicitly says no sixth
paper is opened.

## Nonblocking advisories

1. **Paper 7 V1 state naming.** Its pipeline has top-level
   `stage=COMPLETE_LOCAL` and `status=FINAL_REVIEW_PASS`, while the same object,
   Claim Manifest, Passport, and FINAL_INTEGRITY carry exact
   `final_status=COMPLETE_LOCAL_FINAL_REVIEW_PASS`. This is a documented older
   schema variant, not an incomplete current state.
2. **Paper 8 dual-role JUnit history.** Historical pre-execution records retain
   the authorization-time `pytest.xml` digest
   `81ffc571c773cfa9a69f157559fdaa3611f55c748908c20183e4eae3f3420aa1`;
   the live post-run file is
   `2a0844152eea6d9184d374a6e33c3c4be72fce8deb60296c77650027104348cc`.
   The final manifest explicitly declares `content_changed_after_execution`
   and gives the two records distinct roles.
3. **Paper 10 external erratum distribution.** The historical manifest remains
   internally stale at one path field by design. The canonical erratum and its
   `ERRATUM_PASS` review must accompany it whenever that nested field is
   interpreted.
4. **Paper 11 historical nodes.** Unsuffixed pre-review metadata and Round-1
   state files remain immutable history. Terminal consumers must use the
   explicit `*_FINAL` base nodes and `PIPELINE_STATE_FINAL.json`, as bound by
   `FINAL_INTEGRITY.md`.
5. **Local-only citation audit.** No fresh external bibliographic lookup was
   permitted. This audit confirms the frozen citation packages, local metadata,
   key closure, and final publication layer, not a new live-database search.
6. **Git metadata unavailable.** The workspace root has no `.git` directory and
   is not discoverable as a Git worktree. Branch, index, worktree cleanliness,
   remote, and push readiness therefore cannot be independently certified.

None of these advisories changes a scientific result, terminal PDF identity,
result inventory, final-integrity chain, or the batch verdict.

## Git synchronization readiness

Artifact-level disposition: **`ARTIFACT_READY_GIT_METADATA_UNAVAILABLE`**.
The five project packages, erratum pair, four top-level index/status files, and
this final audit are locally coherent and ready to be handed to an authorized
Git synchronization step. Git synchronization was not performed. Because the
workspace is not a Git worktree, this report does not claim a clean index,
specific branch, configured remote, successful commit, or successful push.

## No-rerun and no-external-data declaration

This final audit performed:

- zero candidate runs or reruns;
- zero registered runs or reruns;
- zero test/analyzer executions;
- zero figure or manuscript builds;
- zero network or external-data accesses;
- zero Git mutations or synchronization operations.

Only existing bytes were read, parsed, hashed, and compared. The sole output
is this `BATCH_02_FINAL_AUDIT.md` authority.

## Final decision

Blockers: **0**  
Advisories: **6, all nonblocking and explicitly bounded**  
Final verdict: **`BATCH02_FINAL_AUDIT_PASS`**

