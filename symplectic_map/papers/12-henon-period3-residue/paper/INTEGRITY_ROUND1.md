# Round-1 Revision Integrity Record

Date: 2026-08-16 UTC  
Candidate: `henon_period3_residue_proof_note_v1`  
State: `READY_FOR_INDEPENDENT_ROUND2`

This is the terminal author-side integrity record for the bounded Round-1
revision. It is not a Round-2 review, an acceptance decision, or authorization
to finalize. No `paper_final.pdf` exists.

## Acyclic Round-1 chain

| Node | SHA-256 |
|---|---|
| Round-0 `paper/INTEGRITY_PRE_REVIEW.md` | `b5ba58d5f0c55ada0be179a1a8eea5516abcf79465f71f5603ae013735c53945` |
| Independent `paper/reviews/round1_review.md` | `a7fcbb957ecb285dd9d5fb7d1adf5b5b1237a20108b2d01ac468191f72b80f9c` |
| Round-0 source snapshot `paper/revisions/manuscript_round0.tex` | `de706b358a6b1fdec47da2ab88704ab8011ed22a1dd7de560b8912d0c845a617` |
| Exact patch `paper/revisions/round1_patch.json` | `9a7c526d9bba02b1ccb241f6c28a2412ee34b73b333cde97750fb38335b49a05` |
| Apply report `paper/revisions/round1_apply_report.json` | `5c133824a94a4e8e8d15e6260e458972e505fa143beacdac8ffba0320928a533` |
| Author response `paper/reviews/round1_response.md` | `e1fbdbb2b9beafdbc956351c98935088d6b02966e772216fd5ec92a82bd48531` |
| `paper/ROUND1_REVISION_MANIFEST.json` | `858dad0bec9a53b4365698bf7c671dffeccb9d27e865850763da151cdeb7badf` |
| `paper/PIPELINE_STATE_ROUND1.json` | `aac89881de74526db9c81f425a84004f2b036e987dccf06016554d4aeb1fb96e` |

The patch, apply report, revision manifest, and pipeline state parse as strict
JSON with no duplicate keys. The graph is acyclic: this terminal record binds
the pipeline state and intentionally contains no digest for itself.

## Revised package

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `5c3b09a835aa41f35899f3c720982f911acf7046559c8433f38ab38ce61a0447` |
| `paper/manuscript.pdf` | `9541a3ad0ffae34cc5c7a17cfd524de73a6685d1a3f7ba2b472061186b721375` |
| `paper/paper_round1_revision.pdf` | `9541a3ad0ffae34cc5c7a17cfd524de73a6685d1a3f7ba2b472061186b721375` |
| `paper/math_commands.tex` | `40a7fe009279e803be822ad2a3fcae56793b2b5c098e0876800e51d1b4f24510` |
| `paper/references.bib` | `f1b6fe0807e33debf87c8be19e1b81b2a4a10f886fd9f4ae1d20bf264e978adc` |
| `paper/manuscript.log` | `cbbe4b13e6d38a7263956b163572741c7f3fc03621a18222ea5e57b412c7e68c` |
| `paper/manuscript.blg` | `be7f60aae83be2fe4e5cc3d0d2898fcd73661df5e2333ae4173dc63bb971ad61` |
| `paper/manuscript.bbl` | `ac0ae8c4f0de3188e42f6f0b17775eb1cf90468431b048986ba23caa12dd522a` |
| `paper/manuscript.aux` | `67a5988dcf5b5359a7933f077ca2a7f92b39f82f5ceb7b8dd23200a935da3824` |
| `paper/manuscript.out` | `7b918498371e32fa96c359d8d5fbdf195fa62091df38d36b9b6df9882a9593d1` |

The Round-0 review PDF remains byte-preserved at
`paper/paper_pre_review.pdf`, SHA-256
`bb3cd34efbff6ec3c2bc2803b0c68b30b701d79833d5a9b4eebeb68d101da949`.
The Round-0 source snapshot has the exact original manuscript SHA-256
`de706b358a6b1fdec47da2ab88704ab8011ed22a1dd7de560b8912d0c845a617`.

## M1 closure and exact reversibility

The only revision item was `R1-M1`. Exactly seven bare `quad` tokens on
Round-0 lines 867, 869, and 882--884 were replaced by `\quad`. The exact diff
contains five removed and five added lines, leaves the 1,419-line count
unchanged, and increases the source by exactly seven bytes. It contains no
other source difference.

The revised manuscript source and extracted PDF text each contain zero bare
`quad` tokens. Mechanically reversing the seven coordinate-guarded operations
restores the exact Round-0 source SHA-256
`de706b358a6b1fdec47da2ab88704ab8011ed22a1dd7de560b8912d0c845a617`.

No Round-0 metadata, integrity, history, bibliography, figure, caption,
citation contract, proof, scientific input, proof-only lock, proof-only
handoff, registered-audit artifact, code, preexecution, result, or runtime
artifact changed.

## Proof-only authority and asset bindings

| Authority or asset | SHA-256 / status |
|---|---|
| `experiments/proof_only_manuscript_lock.json` | `2c7f056b7f9566f754a06c30417105c0b1cefb2d0081f4bca8bb3a00adbf8eeb` |
| `notes/INDEPENDENT_PROOF_ONLY_HANDOFF_REVIEW.md` | `407cec5bf295c29330c24ae461dca86ad1bf54d77f44d477d83a821bf7e41711` / `PROOF_ONLY_HANDOFF_PASS` |
| `notes/PROOF_PACKAGE.md` | `36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9` |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `5630610bb637e155fa631eb2d9c4b36c6ea334ae976a6ef39a53dd733b8c62de` |
| `notes/INDEPENDENT_PLAN_FIGURE_REVIEW_R2.md` | `7b633dd001f1ae086863826612a15d74325406f1eaf2b95fc49e49eddd7ae404` / `ASSET_PASS` |
| `paper/figures/ASSET_TREE.json` | `a5006ef63be3bcc585567276f05f063fd6786c6170081e0eea8ec0ca128598ee` |
| `paper/CITATION_KEY_CONTRACT.json` | `997ca84ee7d868f34cacc783993f10d1b82b86c71fbdc1c9b80f38bcf5199bfd` |
| `paper/figures/FIGURE_MANIFEST.json` | `3adc970996ea7a6e1dc043a554c88b8007f4fe203aa30a522b0a4663dcb31096` |

The three frozen vector figure PDFs retain SHA-256 digests
`1fbed2c5d27025763b68f660a87f695d4c7fe3a96e7786ef98b0bdccf0a53b79`,
`744853231c1c2700bb29f0ca4d8cf0d4059691966d91a0316c7674c526054835`,
and
`e120cb0c8d05cf884862c3e0d23a8db7b45115e5691fda65620d9bcf203c5f6a`.

## Scientific-drift and build closure

C1--C18, PC1/PC2, and all nonclaims remain unchanged under the preserved
claim manifest SHA-256
`d212ca5cde6580087e34c69fe19d3706d140f0cc45d5d662ba9065fe8b1fb8cb`.
Universal nonvanishing of `D_m` remains open. No D8, D9, E8, or E9 label or
value appears. Registered evidence remains unused.

- Two fresh isolated deterministic builds and the synchronized workspace are
  byte-identical for PDF, LOG, BLG, BBL, AUX, and OUT.
- The revised PDF is 19 pages. Page 12 and all 19 pages passed visual
  inspection; no clipping, overlap, missing glyph, or float regression was
  found.
- LaTeX, package, pdfTeX, BibTeX, citation, reference, overfull-box, and
  underfull-box warning or error hits are zero.
- The bibliography has 11 entries and all 10 cited keys close; optional
  `BianchiHe2026` is the sole unused entry.
- All 91 labels are unique, and all 43 reference uses resolve.
- Figures 1--3 remain exact frozen blocks on pages 3, 7, and 9.
- All 38 font records are embedded, subset, and Unicode-mapped; Type-3 fonts
  and raster image objects are zero.
- PDF title, subject, keywords, and author metadata are blank; the visible
  author line is `Anonymous`.

## Binding direction and stop condition

`Round-0 integrity -> independent Round-1 review -> exact patch/apply ->`
`revised source/PDF + response -> Round-1 revision manifest -> Round-1`
`pipeline state -> this integrity record`.

- `ready_for_independent_round2`: `true`
- `independent_round2_review_completed`: `false`
- `finalization_authorized`: `false`
- `final_pdf_created`: `false`

The package must stop for a fresh, hash-bound independent Round-2 review. Any
later change to a bound file invalidates this record and requires regeneration
of the downstream chain.
