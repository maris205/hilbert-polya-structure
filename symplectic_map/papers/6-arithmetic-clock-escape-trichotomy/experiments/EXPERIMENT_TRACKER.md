# Experiment Tracker: Additive Finite Arithmetic Capacity

**Candidate:** `additive_finite_arithmetic_capacity_v2`  
**Current state:** `REGISTERED EXACT/STATIC AUDIT COMPLETE / CAPACITY_BOUND_CERTIFIED`  
**Historical source-lock v1 SHA-256:**
`f5465d92601cf8cd179bd514a08ca991992e718508ec54bf956d36d1280b80c9`  
**Independent proof/novelty review SHA-256:**
`4036f346b75e44ff1acc8402cc1b17f497f3510ee0f4aa6456288f9856fbb63b`  
**Source-lock v2 SHA-256:**
`2d27abceb65cd0ad39612b287e27e2bbdb0b097a67e3bff4d4d6e280e6e4e3fc`

**Historical reviewed pre-execution tree SHA-256 (Round 3):**
`464dacc999e940b483f568d0b5a5398a2a2a1ed9e58abe6cb9f7a4fe1ec1220e`

**Final reviewed and registered tree SHA-256:**
`10fd57b1f99616799f05c3b6a4ce11a9e8ea747d33bb50299aac618948482fb7`

The terminal-binding tree received a fresh independent final review bound to
the current source lock. The unique active authority is `DEPLOYMENT_PASS`, and
the single registered exact/static audit has now completed without changing
the scientific source lock or executing a numerical candidate.

## Provenance chronology

1. Version 1 was locked with zero Paper-5 candidate execution and zero target
   data.
2. An independent reviewer attacked only the version-1 research question,
   proof package, source lock, and experiment plan.  No Paper-5 implementation
   existed and no prime/zero dataset was accessed.
3. The reviewer returned `REPAIR` and independently derived the additive
   theorem.
4. Version 2 incorporates all ten mandatory repairs before formal candidate
   execution.
5. Implementation authoring and noncandidate development tests are permitted;
   the registered audit remains closed pending independent code review.
6. Independent Round 3 passed the preceding code tree while Paper 4 was still
   nonfinal, so the formal upstream gate correctly remained closed.
7. Paper 4 subsequently reached `COMPLETE_LOCAL` after an independent Round-2
   manuscript review.  A mechanical author-side binding froze the actual
   terminal hashes for Papers 3 and 4; both upstream records and the combined
   gate now pass.
8. Freezing Paper 4 changed executable constants and tests, which stales the
   Round-3 authority.  No registered audit is permitted until a fresh
   independent reviewer binds the current tree.
9. A fresh independent final tree-bound review reproduced the current tree,
   source lock, actual Paper-3/Paper-4 terminal bindings, and adversarial
   lifecycle tests, then issued the sole active `DEPLOYMENT_PASS` authority.
10. The registered wrapper ran exactly once. All nine proof, scope, control,
    isolation, authority, upstream, escape, and output gates passed and emitted
    `CAPACITY_BOUND_CERTIFIED`.
11. The official post-run suite reported 51 passing tests, and the exclusive
    result manifest closed the strict schemas, hashes, counters, timestamps,
    result-tree allowlist, and eight required artifacts.

## Execution counters at version-2 lock

| Counter | Value |
|---|---:|
| External prime tables accessed | 0 |
| Prime target arrays generated | 0 |
| Riemann-zero data accessed | 0 |
| Candidate numerical runs | 0 |
| Registered exact/static candidate runs | 0 |
| Target matches computed | 0 |
| Paper-5 figures generated | 0 |
| Paper-5 manuscript written | 0 |

## Mandatory repair registry

| Repair | Requirement | Status |
|---|---|---|
| B01 | Additive theorem promoted; selector union demoted | CLOSED_IN_V2 |
| B02 | Canonical form and exact allowed/excluded operations | CLOSED_IN_V2 |
| B03 | Uniform extension-invariant $S_{\mathbb Q}$-unit definition | CLOSED_IN_V2 |
| B04 | $q>0$ algebraic and $q^2$ certified | CLOSED_IN_V2 |
| B05 | Full Hermite--Lindemann, squaring, valuation proof | CLOSED_IN_V2 |
| B06 | Class-M dimension lemma, separate degrees, normal saturation | CLOSED_IN_V2 |
| B07 | Class-L higher-block recoding | CLOSED_IN_V2 |
| B08 | Class-A algebraicity/gauge distinction and $\mathbb A^2$ control | CLOSED_IN_V2 |
| B09 | Set semantics, representation choice, powers, $q=1$, real log | CLOSED_IN_V2 |
| B10 | Escape gates scoped as necessary certificate failures only | CLOSED_IN_V2 |

## Gate registry

| Gate | Purpose | Status |
|---|---|---|
| G000 | Version-2 JSON validity and immutable hash | PASS |
| G005 | Historical v1 and independent-review provenance binding | PASS |
| G010 | Additive canonical-form normalization | PASS_THEORY |
| G020 | Hermite--Lindemann/valuation independence proof | PASS_INDEPENDENT_THEORY_REVIEW |
| G030 | Class-L higher-block certificate | PASS_THEORY |
| G040 | Class-M fixed-support certificate with repaired field ledger | PASS_THEORY |
| G050 | Class-A algebraicity/gauge certificate | PASS_THEORY |
| G060 | Selector theorem only as corollary | PASS_THEORY |
| G070 | Novelty collision search and safe positioning | PASS_WITH_MODERATE_NOVELTY |
| G080 | Exact controls, proof/scope ledgers, implementation, and isolation | PASS: 6 CONTROLS; 20 PROOF IDS; 10/9 SCOPE IDS; 12-FILE SCANNER |
| G090 | Independent code review | FINAL_TREE_BOUND_DEPLOYMENT_PASS |
| G100 | Registered exact/static audit | PASS: CAPACITY_BOUND_CERTIFIED; SINGLE RUN |
| G110 | Upstream Paper-3/Paper-4 final theorem/hash consistency | PASS_BOTH_ACTUAL_TERMINAL_PACKAGES |
| G120 | Paper production | NOT_STARTED |

No gate was promoted by a finite target search. The final label was emitted
only by the independently authorized registered exact/static audit.

## Pre-execution development checks (historical)

| Check | Command | Result |
|---|---|---|
| Syntax compilation | `python -m compileall -q code` | PASS |
| Isolated unit tests | `pytest -q` | PASS; current count in author binding record |
| Executable isolation | invoked by the development suite | PASS: 12 files scanned, zero findings |
| Independent review authority | fail-closed diagnostic | Historical Round-3 tree correctly rejected after terminal binding |
| Upstream final bindings | strict actual-artifact replay | PASS: Paper 3 and Paper 4 terminal packages |

## Official registered run

| Item | Official result |
|---|---|
| Registered exact/static runs | 1 |
| Classification | `CAPACITY_BOUND_CERTIFIED` |
| Registered gates | 9/9 PASS |
| Official post-run tests | 51 PASS |
| Candidate numerical runs | 0 |
| Target matches computed | 0 |
| External prime tables accessed | false |
| Prime target arrays generated | false |
| Riemann-zero data accessed | false |
| Numerical logarithms evaluated | false |

## Official artifacts and immutable linkage

| Artifact | SHA-256 |
|---|---|
| `results/EXPERIMENT_RESULTS.json` | `9f9878247dc821d15b503abe5a3df713d5bde0f3c76690493dc1b4a98091ace4` |
| `results/registered_run.json` | `4ebec117a2254dc4502c7afd4094e833bc751b8a7e3bffcc16496dd0fd0ea5e3` |
| `results/result_manifest.json` | `21d6910ec1e8e2995d4141f264dce06902f7d1787dea6f28d82346ebd54e3d79` |
| `experiments/official_pytest.xml` | `34915053371701fafd147dd39986b7a5eb157ff09c44f425edfd88f0a8ac17da` |
| `experiments/OFFICIAL_EXPERIMENT_RESULTS.md` | `00d6003467877af3fff47db97b09906edbf1b6b22b56e8b6f9e2bc1672e4f21c` |
| `experiments/OFFICIAL_VALIDATION_REPORT.md` | `b8f746419946ba3be479e7c2fea85da7ba1e7858527f8aa91d863787efb08aa9` |

The machine result manifest was built before the human-readable reports and
records the exact three-file result tree required by the reviewed protocol;
JUnit and prose reports therefore live under `experiments/` and are linked
here by hash. The result manifest itself is exclusive and immutable.

## Classification boundary

`CAPACITY_BOUND_CERTIFIED` certifies only the locked additive
rank-plus-support implication and its declared L/M/A embeddings. It does not
claim a universal no-go theorem, a complete or sufficient escape trichotomy,
historical priority, Riemann-zero evidence, or Route-B progress. Losing a
certificate hypothesis is necessary to escape this bound, but is not itself
evidence of an arithmetic correspondence.
