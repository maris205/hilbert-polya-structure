# Pre-Review Integrity Record

Record date: 2026-08-15 UTC  
Candidate: `cat_centralizer_cyclic_torsor_v1`  
Disposition: **PASS TO FRESH INDEPENDENT MANUSCRIPT REVIEW**

This terminal author-side record freezes the Paper 10 pre-review package.  It
is not an independent mathematical or publication review and does not
authorize finalization.

## Bound manuscript package

| Object | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `65bd460ac888ff5527f4401696788034973c3f97a532ee8a34184ce05fae72a6` |
| `paper/math_commands.tex` | `1484c2da170d49053741bb6d843fbf561a99439f537f5e760dbc2c843658dd6f` |
| `paper/build.sh` | `29bd4f55a6dd867f73a3afdad5f49d74ee0fdc0dff023473527e83ea22b0bb01` |
| `paper/references.bib` | `1ccce7ade3079ca995f00058f4811bdd02a9062d8038b27be2f967f480fe8699` |
| `paper/manuscript.pdf` | `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378` |
| `paper/paper_pre_review.pdf` | `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378` |
| `paper/PAPER_CONFIGURATION.md` | `94961e117e6204e9a42bbce35fa7ba6c2810ce3393697a13214f68fe68f3f17e` |
| `paper/CLAIM_MANIFEST.json` | `3f035a405315dfcdff5e31f78ac27641732780b4bb22d5d2ccc8d8c3769d5237` |
| `paper/EXPERIMENT_PASSPORT.json` | `fec2691fd7b6e0a7f98f92c62aa57779004524e61987323ca05f6f4fbd837b07` |
| `paper/FIGURE_PACKAGE.json` | `90955f034974fc0e856648688f25996d9dd53224ed7222c01e6c0a5d95f0d6f2` |
| `paper/PLAGIARISM_MANIFEST.json` | `c7e0e2b02f2db393f5893c56ea5f8638067902dc48430728bd3763566781d75f` |
| `paper/PIPELINE_STATE.json` | `3b68ddf777724d36fecb84822acf37814926e181531cca26d3484fab566def3a` |
| `paper/AUTHOR_PRE_REVIEW_AUDIT.md` | `96372368227e392739688b51c9a1328408285084b3c052cbc09f6169de3bb355` |

The dependency graph is deliberately acyclic: the source/PDF and five base
manifests are hashed by `PIPELINE_STATE.json`; that pipeline file does not
hash the author audit or this record; the author audit hashes the pipeline;
this terminal record hashes both and does not hash itself.

## Frozen upstream evidence

| Object | SHA-256 / disposition |
|---|---|
| `PAPER_PLAN.md` | `972c13d2551e51bb2781bf7f177314812460c161af0ce1daa748eeff413cbe8a` |
| `notes/CITATION_VERIFICATION.md` | `b4596ed56aee5eb47314221bba681098e45011a3fdc9dafc201315e597a1bfc6` |
| `experiments/source_lock.json` | `aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2` |
| `notes/PROOF_PACKAGE.md` | `2eafe71f32c452ff8a20a6818ccb43082e02b866db7353e26c36ff432f1b2a4c` |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `03424a71fc8716618545a6c7c8b0fd05f5ad744cff034255ab0337012da0303d` |
| independent source review | `a551784d205d9ef52ce6a493ab66cb7295a4a9dadbeb8bb2353fc58e3011dff5` (`SOURCE_PASS`) |
| reviewed execution tree | `87b08f11fc67eae47bdf745f8286700376f3debc5ac3fd190075a5fa2632f436` |
| two-round deployment review history | `990b1762e2aea6c379288854cca918cc4bbe87b7ea7ccadef7458ecfcf6988f0` (final `DEPLOYMENT_PASS`) |
| raw registered result | `8dceb1b8a63db462c1fd55a242ea35de974f73b6c80da68517b91c9eebb214ff` |
| final result manifest | `db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658` (`PASS`) |
| independent result integrity | `29264a8fd97d3acf4435ed807294bffcda0844a48728d8572083d92a3bcf5b58` (`RESULT_PASS`) |
| frozen bibliography | `1ccce7ade3079ca995f00058f4811bdd02a9062d8038b27be2f967f480fe8699` |
| exact LaTeX figure includes | `dfd829b896edcfd02b8d7b02fd9d30bfe8ec49ce42adaba79e1d627cd930708b` |
| final figure manifest | `1a2c7de68772ddeb5c614d0ade89a48710e93a3e5a5ff4a393db5c6f3cd4c2ab` |
| explicit 25-path asset tree | `33b8e1d767221529ff2b97fddca0145b1f9724cae924c37afa2847ecfc2bc9d6` |
| Round-1 repair history | `97f971328996efae866356bdc2c4715a68fcb470dcbe64029d7758d1ec73256a` |
| fresh Round-2 asset review | `9277132df8400c550f108c9a71d466a1c3752bbf3c1be2ae39d565e932bc3e87` (`ASSET_PASS`) |

The asset-tree digest is tied to its explicit 25-path allowlist and is not
redefined by the expanded manuscript directory.  Manuscript production
changed none of the upstream files and changed no file under `code/`,
`experiments/`, `results/`, or `paper/figures/`.

## Release checks

- Two independently created clean build trees reproduced the exact PDF
  digest above and byte-identical terminal LaTeX log, BibTeX log,
  bibliography, auxiliary, and outline files.  `manuscript.pdf` and
  `paper_pre_review.pdf` are byte-identical 15-page anonymous PDFs.
- Terminal counts are: LaTeX/package warnings 0, errors 0, overfull boxes 0,
  underfull boxes 0, undefined references 0, undefined citations 0, and
  BibTeX warnings 0.  Citation closure is 14 cited keys against exactly 14
  verified entries, with no missing or unused key.  Source label/reference
  closure is 56 labels and 40 references, with no missing target.
- All 29 fonts are embedded, subset, and Unicode-mapped; there are no Type-3
  fonts.  The PDF has zero raster-image objects.  All 15 pages of the exact
  frozen digest were visually inspected, with no clipping, overlap, missing
  figure, corrupt glyph, or illegible table entry.
- The three frozen vector PDF figures are present with live references and
  exact independently approved caption blocks.  Their output hashes,
  determinism audit, trace, provenance, and asset QA remain unchanged.
- The C1--C10/X1--X2 manuscript firewall matches the paper plan.  The
  displayed finite ledger matches 9/9 registered rows and 12/12 fields per
  row.  All-modulus authority remains the proof; finite rows are never
  promoted to proof or novelty evidence.
- The normalized substantive body has zero common 12-word shingles with each
  of Papers 1--9 and the original proposal under the recorded project-local
  heuristic screen.
- The reader-facing manuscript uses conservative low-novelty language and no
  numeric novelty score.  It makes exact nonclaims for new centralizer,
  zeta, equivariant/stacky, Hecke, quantization, transfer/Fredholm,
  prime--zero, and RH results.
- No candidate or tests were rerun; no source/code/result/figure/reference
  artifact was edited; no modulus, matrix, analytic value, prime/zero data,
  enriched construction, or network lookup was introduced.

## Independence and finalization boundary

The manuscript has received author-side production, compilation,
transcription, and integrity checks only.  A fresh independent reviewer must
now inspect this exact source and PDF.  `paper_pre_review.pdf` is the sole
review copy; `paper_final.pdf` does not exist, and finalization is not
authorized.

Final status: `READY_FOR_FRESH_INDEPENDENT_MANUSCRIPT_REVIEW`.
