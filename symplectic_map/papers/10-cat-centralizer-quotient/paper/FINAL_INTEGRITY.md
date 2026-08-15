# Final Integrity Record

Record date: 2026-08-15 UTC  
Candidate: `cat_centralizer_cyclic_torsor_v1`  
Terminal status: **COMPLETE_LOCAL_FINAL_REVIEW_PASS**

This record closes the local manuscript pipeline after an independent
Round-2 decision of `PASS -- MAY FINALIZE`.  Finalization was strictly
mechanical: it created the release copy and updated external lifecycle
manifests.  It changed no manuscript source, mathematical statement, proof,
citation, bibliography, figure, source lock, code, experiment, or result.

## Independent authorization

| Object | SHA-256 | Decision |
|---|---|---|
| `paper/reviews/round2_review.md` | `ca8ee460f0956eb2f653e837402888b9d88d4888ae04ea1ad76231b6764a79ae` | `PASS -- MAY FINALIZE`; zero Critical, Major, or Minor findings |

Round 2 independently verified the approved source, PDF, Round-1 no-change
closure, claim and evidence boundaries, figure package, bibliography, and
revision integrity.  It authorized only a byte-preserving terminal
transition.

## Final manuscript binding

| Object | SHA-256 |
|---|---|
| immutable `paper/manuscript.tex` | `65bd460ac888ff5527f4401696788034973c3f97a532ee8a34184ce05fae72a6` |
| immutable `paper/math_commands.tex` | `1484c2da170d49053741bb6d843fbf561a99439f537f5e760dbc2c843658dd6f` |
| immutable `paper/references.bib` | `1ccce7ade3079ca995f00058f4811bdd02a9062d8038b27be2f967f480fe8699` |
| immutable `paper/build.sh` | `29bd4f55a6dd867f73a3afdad5f49d74ee0fdc0dff023473527e83ea22b0bb01` |
| historical `paper/paper_pre_review.pdf` | `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378` |
| independently approved `paper/paper_round1_revision.pdf` | `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378` |
| live `paper/manuscript.pdf` | `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378` |
| terminal `paper/paper_final.pdf` | `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378` |

All four PDFs above are byte-for-byte identical.  Historical pre-review
labels embedded in the frozen source or PDF remain immutable reviewed-
artifact history; this record and the terminal machine-readable manifests
are the authoritative current lifecycle state.

## Review and revision chain

| Object | SHA-256 |
|---|---|
| `PAPER_PLAN.md` | `972c13d2551e51bb2781bf7f177314812460c161af0ce1daa748eeff413cbe8a` |
| `notes/CITATION_VERIFICATION.md` | `b4596ed56aee5eb47314221bba681098e45011a3fdc9dafc201315e597a1bfc6` |
| `paper/reviews/round1_review.md` | `bb1bdfb379062d2fe11245568ca3f6a97845456004119d3954c17dd917828c24` |
| `paper/reviews/round1_response.md` | `b3c4d6ecea0d5bc165bcb50fbb240ffede2d44804cd32dd9b66d487b93d6d561` |
| `paper/INTEGRITY_ROUND1_REVISION.md` | `af4404f0606fdd2c8efc2c7d19eb1f89ed2b8298eaa26fc861faceb068c14364` |
| `paper/reviews/round2_review.md` | `ca8ee460f0956eb2f653e837402888b9d88d4888ae04ea1ad76231b6764a79ae` |

## Terminal release manifests

| Object | SHA-256 |
|---|---|
| `paper/PAPER_CONFIGURATION.md` | `4231373e4859f32d48a7e397116516df390b5d98d6ca5e0f15e25da71e0295f2` |
| `paper/CLAIM_MANIFEST.json` | `b8c1b46158d8dcad8edae9c610ac89bd2c46556a343d242b35cfe53538fa9c80` |
| `paper/EXPERIMENT_PASSPORT.json` | `476e9ad9ef290ac30d473079bdf677987abec8170996786536198c39d22f895f` |
| `paper/FIGURE_PACKAGE.json` | `23ce51a1c168081b278cffd88af7f76f38f37a56e0ea54c78793f0c339725b9b` |
| unchanged `paper/PLAGIARISM_MANIFEST.json` | `c7e0e2b02f2db393f5893c56ea5f8638067902dc48430728bd3763566781d75f` |
| `paper/PIPELINE_STATE.json` | `dc7550b39e42cdeeeacd4ae64f9fb4142b0f2e2e4b315d0e73f1932077e0b09c` |

All five JSON documents parse strictly with no duplicate key.  The terminal
pipeline hashes every terminal base manifest, the approved and final PDFs,
and the complete review chain.  It intentionally does not hash this record;
this record hashes the pipeline and does not hash itself.  The terminal
digest graph is therefore acyclic.

## Frozen scientific and figure evidence

| Frozen object | SHA-256 |
|---|---|
| source lock | `aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2` |
| proof package | `2eafe71f32c452ff8a20a6818ccb43082e02b866db7353e26c36ff432f1b2a4c` |
| claims--evidence matrix | `03424a71fc8716618545a6c7c8b0fd05f5ad744cff034255ab0337012da0303d` |
| independent source-lock review | `a551784d205d9ef52ce6a493ab66cb7295a4a9dadbeb8bb2353fc58e3011dff5` |
| code review history | `990b1762e2aea6c379288854cca918cc4bbe87b7ea7ccadef7458ecfcf6988f0` |
| raw registered result | `8dceb1b8a63db462c1fd55a242ea35de974f73b6c80da68517b91c9eebb214ff` |
| strict result manifest | `db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658` |
| independent result integrity | `29264a8fd97d3acf4435ed807294bffcda0844a48728d8572083d92a3bcf5b58` |
| Round-1 asset-repair history | `97f971328996efae866356bdc2c4715a68fcb470dcbe64029d7758d1ec73256a` |
| independent Round-2 asset pass | `9277132df8400c550f108c9a71d466a1c3752bbf3c1be2ae39d565e932bc3e87` |
| exact LaTeX figure includes | `dfd829b896edcfd02b8d7b02fd9d30bfe8ec49ce42adaba79e1d627cd930708b` |
| final figure manifest | `1a2c7de68772ddeb5c614d0ade89a48710e93a3e5a5ff4a393db5c6f3cd4c2ab` |
| explicit 25-path asset tree | `33b8e1d767221529ff2b97fddca0145b1f9724cae924c37afa2847ecfc2bc9d6` |
| figure determinism audit | `e3f51a1985f6d00a7655db882cbbccddcfa712f710e210af19b9d15c8485567e` |
| Figure 1 PDF | `ac8b29c810881e6383fb3f8b7cb55c602e052ef1677def5643d540b8ee12feb3` |
| Figure 2 PDF | `f86ff8e50c5a138996c8f379fa0309ddc6071cffca1d540b81e07304dae2dd73` |
| Figure 3 PDF | `0df9de8544c05e60749d456244c2920ac15c03a8bc5f5011a66f8d2c5e8cee33` |

All hashes reproduce their frozen bindings.  Terminal finalization did not
rerun or extend the registered candidate or tests, add a modulus or shell,
evaluate a numerical analytic parameter, access an external prime or zero
dataset, use the network, run a centralizer computation, or open a new
scientific route.

## Terminal build and PDF checks

- Two separate clean temporary paper trees independently produced SHA-256
  `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378`.
  Their PDF, LaTeX log, BibTeX log, bibliography, auxiliary, and outline
  files matched pairwise, and both PDFs compared byte-identically with the
  approved revision and final release.  Both build stderr streams were empty.
- Each build has 15 pages, 14 cited bibliography keys against exactly 14
  verified entries, zero LaTeX or package error or warning, zero BibTeX
  warning, zero box warning, and zero undefined citation or reference.
  Source closure is 56 unique labels and 40 references, with no missing
  target.
- All 29 font records are embedded, subset, and Unicode-mapped; there are no
  Type-3 fonts and zero raster-image object.  The three figure blocks retain
  their exact frozen vector-PDF includes.
- The approved digest passed inspection of all 15 pages.  Because the final
  PDF has exactly the same bytes, that inspection transfers without
  qualification to the release copy.
- The terminal paper inventory contains 50 regular files: the 49-item
  approved and review package plus this terminal integrity record.  It has
  exactly the three named lifecycle PDFs `paper_pre_review.pdf`,
  `paper_round1_revision.pdf`, and `paper_final.pdf`, alongside the live
  byte-identical `manuscript.pdf` and the three frozen figure PDFs; no
  alternative final PDF exists.
- Conservative reader-facing framing, the absence of a numeric novelty
  score, the C1--C10/X1--X2 claim firewall, all-modulus proof authority, and
  the finite nine-row control boundary remain unchanged.

## Terminal disposition

Independent Round 2 is complete and passed.  The final local release copy
and all external lifecycle manifests are closed.  Any later scientific,
citation, figure, source, code, result, or manuscript-byte change invalidates
this record and requires a new review gate.

Final status: `COMPLETE_LOCAL_FINAL_REVIEW_PASS`.
