# Round-1 Revision Integrity Record

Record date: 2026-08-15 UTC  
Candidate: `cat_prime_shell_multiplicity_obstruction_v1`  
Disposition: **READY FOR FRESH INDEPENDENT ROUND 2**

This terminal author-side record freezes the bounded Round-1 revision.  It
is not an independent Round-2 review, does not authorize finalization, and
does not authorize creation of `paper_final.pdf`.

## Bound revision package

| Object | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `fb54cb9273c89ad5f76a9485d67a815555050b3c71e630e47d367b043ae6e26c` |
| `paper/math_commands.tex` | `13548ef611eaeb0184fd951e8f3689274b137747467e9857c25e39d249f486e2` |
| `paper/references.bib` | `37ee7c23398806b9e59e86ec9fbf6fd0dfc0483043cff9459d0837b2bd2457ae` |
| `paper/build.sh` | `7e58c5a0a2ae849b7202aebb68a1f4f3323f68dc14a11ec3df7891c78f8d3446` |
| `paper/manuscript.pdf` | `96a560712ae7fb34e1d0ecfcd59e9b2c210ad61fe8ee0537c3a5ff5c860b4cd6` |
| `paper/paper_round1_revision.pdf` | `96a560712ae7fb34e1d0ecfcd59e9b2c210ad61fe8ee0537c3a5ff5c860b4cd6` |
| immutable `paper/paper_pre_review.pdf` | `9b63f190e7c751c27682d1a9cc9246f0153edddfec61d4539c573ab70070d51c` |
| `PAPER_PLAN.md` | `41a1e6e9356c3820c3890fca232b60302673c1a28a83d8ba26f932eec5f73e3e` |
| `notes/CITATION_VERIFICATION.md` | `ae25c56d17703ee00b8168eba33bbec77c688e72c8fb6ac520214e523241b808` |
| `paper/reviews/round1_review.md` | `dc34ea65a091680e3a2e0f89b15f804f45b3a7be7ae11502d82c668ec6d58ed8` |
| `paper/reviews/round1_response.md` | `2cb3da5c9af34b12cb8a4e6f6c7c5b7c8299a95628f5d1126742dcc7be110934` |
| `paper/PAPER_CONFIGURATION.md` | `fde14dcf6020fb183a6d69b0790bccc482dec6dc55961f8f0fd7f8650bd75932` |
| `paper/CLAIM_MANIFEST.json` | `8dd511a2775460bcd9d33a925df60c780fd946f46ca015c3bf6f41b6fa80ccc8` |
| `paper/EXPERIMENT_PASSPORT.json` | `847c3655ff9ff2e27f1d0755a8f5913ad81d4b8c07c4a48849bf3ac2acfcbac0` |
| `paper/FIGURE_PACKAGE.json` | `477e63151c7b203d3199b5e98122f1b2df315910ec05f1c262cadb3044a4032c` |
| `paper/PLAGIARISM_MANIFEST.json` | `479415a2c9bd1985ee14925ba31c193cae479f38ca6a3676b5154a8230497316` |
| `paper/PIPELINE_STATE.json` | `32253ea26d7fb485b4e61f2e2df0c2f661a811319716b77ca4ae963f85087d5a` |

The pipeline state intentionally does not hash this record or the response.
The response hashes the pipeline, and this terminal record hashes both, so
the dependency graph is acyclic.

## Figure revision binding

| Object | SHA-256 |
|---|---|
| current figure manifest | `23468908fb020e80677e7a5b8e8686c2d14edbec2dc1e74f06973940c12adb8e` |
| current determinism audit | `a6aab23da51635f07e68104507a5ab55f49d64abdf33f70205e5317478b71129` |
| current figure QA | `3b1ca743e64d758bc3a24db2ef8bbae46b40e9ef08a93f37620c57c046ba70bc` |
| current figure provenance | `2c5fbe6787fe6232d4c24da046a3c5bf7a77c09acbc630ac86ce5fbb1edda5fa` |
| Figure 1 PDF | `16045d45187cb3e8fb81192203e1255f2ddc749e3a4faf6ffd45b256b67c6531` |
| Figure 2 PDF | `39ddd9baaaa2fc5ce7026f1d5cb844ec3147cbd707959e5ada1f61ea12f2b0da` |
| Figure 3 PDF | `2b0a72db9d8cea6d901a8f2e03d6f2a17c49a4d2a2cd217e36ccbf148d4806b4` |
| Round-1 explicit 24-path framed tree | `0526235c1b3581aba830e054d1f883fd677cb7a752180bb8a0eeb0dbab7a862e` |
| historical pre-review predecessor tree | `312c4b095b58acb9e8047d7113308d28870e3db7633f37d17bd904ca2c7ebfaa` |

The 24 paths and unsigned-64-bit big-endian path/content framing are listed
exactly in `FIGURE_PACKAGE.json`.  The Round-1 tree was computed only after
the plan, generators, nine outputs, manifest, determinism audit, QA, and
provenance were frozen.  It is distinct from, and does not overwrite, the
independently reviewed historical predecessor.

## Historical and upstream evidence

| Frozen object | SHA-256 |
|---|---|
| historical `paper/AUTHOR_PRE_REVIEW_AUDIT.md` | `676cd1bced62b7a8cd776400cf0f79868fddc00e435b4e5689a2052ec03e1d6d` |
| historical `paper/INTEGRITY_PRE_REVIEW.md` | `9f95c32b4d1e9f620603e8f22440789aebd232679e01357f23dea76f382983dd` |
| source lock | `662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49` |
| proof package | `47216ad4021d3476bfd0850ebec24c9ceafb5af8c0573214182fd2d0da7b2daa` |
| raw exact result | `448de06e92bd7ab4e5374e5d1f57413df45859cd3476ff14b2691b63ac364fab` |
| strict result manifest | `8ca12744638a47b6e4fa3239a60a19d79229d2b9596ae4fe4b2f66a399618f92` |
| independent result integrity | `aa0c7db555f11920c7305be508f6cfff62375970e112e9f720111831da20b3bd` |
| independent plan/figure/citation gate | `f8c22bfba9299230a8e2051c089863bf6603ebcb84e5e42955ecbf36a874ec06` |

## Findings and checks

- **M1 closed.** Appendix B and the claim manifest now map C1--C9
  one-to-one; all nine source locators were checked and X1/X2 are absent.
- **M2 closed.** The public manuscript uses qualitative low-novelty
  synthesis/audit language and contains no numerical novelty score.
- **M3 closed.** The manuscript and Figure 3 use standalone present-audit
  and follow-up-centralizer wording.  All nine formats passed the supplied
  two-render byte comparison; Figure 1 and Figure 2 changed only in
  standalone metadata, while Figure 3 also changed the requested wording.
- **M4 closed.** The plan describes Figure 1's existing axis as linear; its
  data and axis implementation did not change.
- Two clean builds produced the same 15-page PDF.  The terminal log has zero
  warning, undefined citation/reference, or box warning.  Citation closure
  is 11/11; 37/37 fonts are embedded and subset; there is no raster image
  object; visual inspection passed 15/15 pages.
- The project-local originality rerun found zero common normalized
  contiguous 12-word shingle against each of Papers 1--8 and the proposal.
- Frozen source, proof, code, results, and official reports were not edited.
  The candidate and tests were not rerun.  No new prime, numerical
  `s`/logarithm, composite scan, or centralizer computation was performed.

## Independence and finalization boundary

These are author-side closure statements only.  The next permitted stage is
a fresh independent Round-2 review of the bound source, PDF, response,
figure revision, and integrity package.  Finalization remains unauthorized;
`paper_final.pdf` does not exist.

Final status: `READY_FOR_INDEPENDENT_ROUND2`.
