# Pre-Review Integrity Record

Record date: 2026-08-14 UTC  
Candidate: `cat_prime_shell_multiplicity_obstruction_v1`  
Disposition: **PASS TO FRESH INDEPENDENT MANUSCRIPT REVIEW**

This terminal author-side record freezes the Paper 9 pre-review package.  It
is not an independent mathematical review and does not authorize finalization.

## Bound manuscript package

| Object | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `67afe346285a1a1f322a437c19f14316164fbd0c9066d30e4012ce7ee0b90965` |
| `paper/math_commands.tex` | `13548ef611eaeb0184fd951e8f3689274b137747467e9857c25e39d249f486e2` |
| `paper/build.sh` | `7e58c5a0a2ae849b7202aebb68a1f4f3323f68dc14a11ec3df7891c78f8d3446` |
| `paper/references.bib` | `37ee7c23398806b9e59e86ec9fbf6fd0dfc0483043cff9459d0837b2bd2457ae` |
| `paper/manuscript.pdf` | `9b63f190e7c751c27682d1a9cc9246f0153edddfec61d4539c573ab70070d51c` |
| `paper/paper_pre_review.pdf` | `9b63f190e7c751c27682d1a9cc9246f0153edddfec61d4539c573ab70070d51c` |
| `paper/PAPER_CONFIGURATION.md` | `9f2db73918638cc1147ed62e04e916ece6897510d2b477a219b09db6311867d4` |
| `paper/CLAIM_MANIFEST.json` | `9d3c9ccf630f22cfd8dc7e3f9d6956cec45d816b14175d55553d833eeefc0c57` |
| `paper/EXPERIMENT_PASSPORT.json` | `3a9755107c93bf6426fd218a7e179225b61011401a0bc5638c3253d4781bf3a9` |
| `paper/FIGURE_PACKAGE.json` | `6385e0287c08e09a9acc37b932ab88c512640f15fbc96870573366123556d953` |
| `paper/PLAGIARISM_MANIFEST.json` | `db13bb00c5b6d5c2ed3fdd66ce1768c41fde4676719090da1b3dc728c1df1471` |
| `paper/PIPELINE_STATE.json` | `2dfa850b7f06af5630330a2a4964a598650cd4b509a031ddeb03afd0752cd5eb` |
| `paper/AUTHOR_PRE_REVIEW_AUDIT.md` | `676cd1bced62b7a8cd776400cf0f79868fddc00e435b4e5689a2052ec03e1d6d` |

The dependency graph is deliberately acyclic: the source/PDF and base
manifests are hashed by `PIPELINE_STATE.json`; that pipeline file does not
hash the author audit or this record; the author audit hashes the pipeline;
this terminal record hashes both and does not hash itself.

## Frozen upstream evidence

| Object | SHA-256 |
|---|---|
| `PAPER_PLAN.md` | `406e443e96e4822acb3530990cfe45b64921821738d013f0d328d551de5ed088` |
| `notes/CITATION_VERIFICATION.md` | `ae25c56d17703ee00b8168eba33bbec77c688e72c8fb6ac520214e523241b808` |
| `experiments/source_lock.json` | `662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49` |
| `notes/PROOF_PACKAGE.md` | `47216ad4021d3476bfd0850ebec24c9ceafb5af8c0573214182fd2d0da7b2daa` |
| independent source review | `9509278ce55d908dba7d7cb4a809a335cc51d9364e8bfdfd1dc66be594775b8f` |
| raw exact result | `448de06e92bd7ab4e5374e5d1f57413df45859cd3476ff14b2691b63ac364fab` |
| final result manifest | `8ca12744638a47b6e4fa3239a60a19d79229d2b9596ae4fe4b2f66a399618f92` |
| independent result integrity | `aa0c7db555f11920c7305be508f6cfff62375970e112e9f720111831da20b3bd` |
| independent plan/figure/citation review | `f8c22bfba9299230a8e2051c089863bf6603ebcb84e5e42955ecbf36a874ec06` |
| explicit frozen 24-path asset tree | `312c4b095b58acb9e8047d7113308d28870e3db7633f37d17bd904ca2c7ebfaa` |

The old asset-tree digest is tied to its explicit 24-path allowlist and is
not redefined by later manuscript files.  Its framing and inventory are
recorded in `FIGURE_PACKAGE.json`.  Manuscript production changed none of
the upstream files and changed no file under `source/`, `code/`, `results/`,
or `paper/figures/`.

## Release checks

- Two consecutive clean builds reproduced the exact PDF digest above and
  byte-identical terminal log and BibTeX log.  `manuscript.pdf` and
  `paper_pre_review.pdf` are byte-identical, 15-page anonymous PDFs.
- Terminal counts are: LaTeX/package warnings 0, errors 0, overfull boxes 0,
  underfull boxes 0, undefined references 0, undefined citations 0, BibTeX
  warnings 0.  Citation closure is 11 cited keys against exactly 11 verified
  entries, with no missing or unused key.
- All 34 fonts are embedded and subset.  The PDF has zero raster image
  objects.  All 15 pages of the exact frozen digest were visually inspected;
  no clipping, overlap, missing figure, corrupt glyph, or illegible entry
  was found.
- The three frozen PDF figures are present with semantic captions.  Their
  figure manifest, two-run determinism audit, provenance, and visual QA are
  unchanged and independently approved.
- The normalized substantive body has zero common 12-word shingles with
  each of Papers 1--8 and the original proposal under the recorded local
  heuristic screen.
- Claim/evidence inflation, proof logic, semantic conflation, provenance and
  forbidden-data use, citation/originality/anonymity, figure transcription,
  and build/release-state failure modes all pass the author-side audit.
- The finite audit remains development-seen and cannot prove the all-prime
  theorem or convergence.  Raw-return and orbit-label factors remain
  separate.  The scalar theorem remains limited to fixed nonzero pure
  denominators.  Fractional normalization succeeds but is global;
  selector, centralizer, matrix, numerator, alternating, Fredholm, transfer,
  and cohomological escapes are not ruled out.  No claim is made in
  `2 < Re(s) <= 3`, about zeros, or about priority.

## Independence and finalization boundary

The manuscript has received author-side production, compilation, and
integrity checks only.  A fresh independent reviewer must now inspect this
bound source and PDF.  `paper_pre_review.pdf` is the sole review copy;
`paper_final.pdf` does not exist, and finalization is not authorized.

Final status: `READY_FOR_FRESH_INDEPENDENT_MANUSCRIPT_REVIEW`.
