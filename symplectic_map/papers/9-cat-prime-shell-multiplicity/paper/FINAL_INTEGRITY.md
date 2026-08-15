# Final Integrity Record

Record date: 2026-08-15 UTC  
Candidate: `cat_prime_shell_multiplicity_obstruction_v1`  
Terminal status: **COMPLETE_LOCAL_FINAL_REVIEW_PASS**

This record closes the local manuscript pipeline after an independent
Round-2 decision of `PASS -- MAY FINALIZE`.  Finalization was strictly
mechanical: it created the release copy and updated external lifecycle
manifests.  It changed no manuscript source, mathematical statement, proof,
citation, bibliography, figure, source lock, code, experiment, or result.

## Independent authorization

| Object | SHA-256 | Decision |
|---|---|---|
| `paper/reviews/round2_review.md` | `32cc795c358d979988673658398dd4dbf2768cd9f1b38464b9b438703c2ebd23` | `PASS -- MAY FINALIZE`, 8.5/10, zero Critical/Major/Minor findings |

Round 2 independently verified the approved source, PDF, Round-1 closure,
claim map, figure package, and revision asset tree.  It authorized only a
byte-preserving terminal transition.

## Final manuscript binding

| Object | SHA-256 |
|---|---|
| immutable `paper/manuscript.tex` | `fb54cb9273c89ad5f76a9485d67a815555050b3c71e630e47d367b043ae6e26c` |
| immutable `paper/math_commands.tex` | `13548ef611eaeb0184fd951e8f3689274b137747467e9857c25e39d249f486e2` |
| immutable `paper/references.bib` | `37ee7c23398806b9e59e86ec9fbf6fd0dfc0483043cff9459d0837b2bd2457ae` |
| immutable `paper/build.sh` | `7e58c5a0a2ae849b7202aebb68a1f4f3323f68dc14a11ec3df7891c78f8d3446` |
| historical `paper/paper_pre_review.pdf` | `9b63f190e7c751c27682d1a9cc9246f0153edddfec61d4539c573ab70070d51c` |
| independently approved `paper/paper_round1_revision.pdf` | `96a560712ae7fb34e1d0ecfcd59e9b2c210ad61fe8ee0537c3a5ff5c860b4cd6` |
| live `paper/manuscript.pdf` | `96a560712ae7fb34e1d0ecfcd59e9b2c210ad61fe8ee0537c3a5ff5c860b4cd6` |
| terminal `paper/paper_final.pdf` | `96a560712ae7fb34e1d0ecfcd59e9b2c210ad61fe8ee0537c3a5ff5c860b4cd6` |

The final PDF is byte-for-byte identical to the independently approved
Round-1 revision PDF.  Historical pre-review labels embedded in the frozen
source or PDF remain immutable reviewed-artifact history; this record and
the terminal machine-readable manifests override them as the authoritative
current lifecycle state.

## Review and revision chain

| Object | SHA-256 |
|---|---|
| `PAPER_PLAN.md` | `41a1e6e9356c3820c3890fca232b60302673c1a28a83d8ba26f932eec5f73e3e` |
| `notes/CITATION_VERIFICATION.md` | `ae25c56d17703ee00b8168eba33bbec77c688e72c8fb6ac520214e523241b808` |
| `paper/reviews/round1_review.md` | `dc34ea65a091680e3a2e0f89b15f804f45b3a7be7ae11502d82c668ec6d58ed8` |
| `paper/reviews/round1_response.md` | `2cb3da5c9af34b12cb8a4e6f6c7c5b7c8299a95628f5d1126742dcc7be110934` |
| `paper/INTEGRITY_ROUND1_REVISION.md` | `40df4fe0e893f3ae308fa609c34b39cc74be044a1ca03866d28c7f12f4e337dd` |
| `paper/reviews/round2_review.md` | `32cc795c358d979988673658398dd4dbf2768cd9f1b38464b9b438703c2ebd23` |

## Terminal release manifests

| Object | SHA-256 |
|---|---|
| `paper/PAPER_CONFIGURATION.md` | `8c5b0ae01be1c467296c3a18638f3a993170b807eb8a87e9965a6a15dff35a0b` |
| `paper/CLAIM_MANIFEST.json` | `09348a2db96f04b85b0a9bd66dead97f64d0724551f9cba65bbb258b5f6caded` |
| `paper/EXPERIMENT_PASSPORT.json` | `cc4f48930ff35cdef207bb16cb5db4d13f86888f813d08e5cc47830333145e17` |
| `paper/FIGURE_PACKAGE.json` | `c09224620375c5bda053448d4726d4123f1bff6b1519de7a1a89988a348bddf0` |
| unchanged `paper/PLAGIARISM_MANIFEST.json` | `479415a2c9bd1985ee14925ba31c193cae479f38ca6a3676b5154a8230497316` |
| `paper/PIPELINE_STATE.json` | `f4876e8dccbd9502af593fa77318dbf0b3c1f60ccef39c6d483d8e0df4a1e922` |

All five JSON indexes parse strictly with no duplicate key.  The pipeline
hashes every terminal base manifest, the approved PDF, and the complete
review chain.  It intentionally does not hash this terminal record; this
record hashes the pipeline, so the digest dependency graph is acyclic.

## Frozen scientific and figure evidence

| Frozen object | SHA-256 |
|---|---|
| source lock | `662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49` |
| proof package | `47216ad4021d3476bfd0850ebec24c9ceafb5af8c0573214182fd2d0da7b2daa` |
| raw registered result | `448de06e92bd7ab4e5374e5d1f57413df45859cd3476ff14b2691b63ac364fab` |
| strict result manifest | `8ca12744638a47b6e4fa3239a60a19d79229d2b9596ae4fe4b2f66a399618f92` |
| independent result integrity | `aa0c7db555f11920c7305be508f6cfff62375970e112e9f720111831da20b3bd` |
| independent plan/figure/citation review | `f8c22bfba9299230a8e2051c089863bf6603ebcb84e5e42955ecbf36a874ec06` |
| current figure manifest | `23468908fb020e80677e7a5b8e8686c2d14edbec2dc1e74f06973940c12adb8e` |
| current figure determinism audit | `a6aab23da51635f07e68104507a5ab55f49d64abdf33f70205e5317478b71129` |
| Figure 1 PDF | `16045d45187cb3e8fb81192203e1255f2ddc749e3a4faf6ffd45b256b67c6531` |
| Figure 2 PDF | `39ddd9baaaa2fc5ce7026f1d5cb844ec3147cbd707959e5ada1f61ea12f2b0da` |
| Figure 3 PDF | `2b0a72db9d8cea6d901a8f2e03d6f2a17c49a4d2a2cd217e36ccbf148d4806b4` |
| Round-1 explicit 24-path figure-asset tree | `0526235c1b3581aba830e054d1f883fd677cb7a752180bb8a0eeb0dbab7a862e` |

All hashes reproduce their frozen bindings.  Terminal finalization did not
rerun or extend the registered candidate or tests, add a prime or composite
shell, evaluate a numerical analytic parameter, access an external prime or
zero dataset, use the network, run a centralizer computation, or open a new
scientific route.

## Terminal build and PDF checks

- Two separate clean temporary paper trees independently produced SHA-256
  `96a560712ae7fb34e1d0ecfcd59e9b2c210ad61fe8ee0537c3a5ff5c860b4cd6`.
  Their PDF, log, and BibTeX-log hashes matched pairwise, and both PDFs
  compared byte-identically with the approved revision and final release.
- Each build has 15 pages, 11 bibliography items, zero BibTeX warning, zero
  LaTeX/package/citation/reference/overfull/underfull warning, 37/37 embedded
  and subset fonts, and zero raster image object.
- The approved PDF passed independent visual inspection of all 15 pages.
  Because the final PDF has exactly the same bytes, that inspection transfers
  without qualification to the release copy.
- The terminal paper inventory contains 47 regular files: the 46-item
  approved/review package plus this one terminal integrity record.  It has
  exactly the three named lifecycle PDFs `paper_pre_review.pdf`,
  `paper_round1_revision.pdf`, and `paper_final.pdf`, alongside the live
  byte-identical `manuscript.pdf`; no alternative final PDF exists.

## Terminal disposition

Independent Round 2 is complete and passed.  The final local release copy
and all external lifecycle manifests are closed.  Any later scientific,
citation, figure, source, code, result, or manuscript-byte change invalidates
this record and requires a new review gate.

Final status: `COMPLETE_LOCAL_FINAL_REVIEW_PASS`.
