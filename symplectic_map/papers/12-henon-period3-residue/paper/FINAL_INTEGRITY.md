# Terminal Final Integrity Record

Date: 2026-08-16 UTC  
Canonical path base: `papers/12-henon-period3-residue`  
Candidate: `henon_period3_residue_proof_note_v1`  
Status: `COMPLETE_LOCAL_FINAL_REVIEW_PASS`

This record seals a purely mechanical proof-only terminal finalization after
a fresh independent Round-2 `PASS` / `MAY_FINALIZE`. It introduces no
manuscript, bibliography, figure, source, theorem-scope, citation-evidence,
registered-evidence, or scientific change. No candidate, registered audit,
test suite, code, analyzer, result, runtime, figure generator, or scientific
computation was run, and no network access was used.

The terminal graph is acyclic: four base terminal nodes feed the terminal
pipeline state, which feeds this integrity record. This record contains no
digest for itself.

## Independent release gate and exact final identity

| Node | Path | SHA-256 | Disposition |
|---|---|---|---|
| Round-2 review | `paper/reviews/round2_review.md` | `f56ff399b120e5fb9729e51b4d52dcde64df954fb064f32319998d678c3c0577` | `PASS`; `MAY_FINALIZE`; 0/0/0/0 findings |
| Approved source | `paper/manuscript.tex` | `5c3b09a835aa41f35899f3c720982f911acf7046559c8433f38ab38ce61a0447` | exact review-bound identity |
| Approved revision PDF | `paper/paper_round1_revision.pdf` | `9541a3ad0ffae34cc5c7a17cfd524de73a6685d1a3f7ba2b472061186b721375` | 19 pages |
| Live manuscript PDF | `paper/manuscript.pdf` | `9541a3ad0ffae34cc5c7a17cfd524de73a6685d1a3f7ba2b472061186b721375` | byte-identical |
| Terminal final PDF | `paper/paper_final.pdf` | `9541a3ad0ffae34cc5c7a17cfd524de73a6685d1a3f7ba2b472061186b721375` | byte-identical copy |

All three PDF files are byte-identical. The final PDF was created only after
the approved source, approved revision PDF, independent review, proof-only
authority, and asset identities passed their preflight gate.

## Acyclic terminal metadata chain

The base layer contains no reference to another new terminal metadata node
and no self-hash. The pipeline state binds all four base nodes and does not
hash itself or this integrity record. This record binds the pipeline and base
nodes and intentionally does not hash itself.

| Layer | Path | SHA-256 |
|---|---|---|
| base | `paper/PAPER_CONFIGURATION_FINAL.md` | `340b1a2397c118a3095a905098fc4bedc52bc9a58717412c9e396c85aafd00e2` |
| base | `paper/CLAIM_MANIFEST_FINAL.json` | `71ffb0a7009731d166b063184afaff4067f04a4360c7f4e54f619d0bc58ba310` |
| base | `paper/PROOF_ONLY_PASSPORT_FINAL.json` | `ba7eaf0cd305e1f39c57dfa990915e2238ba218167239e620c5ad7d8a60211ab` |
| base | `paper/FIGURE_PACKAGE_FINAL.json` | `5aedd6e2430f13a767001fdd26d4e54a6254b671ac4af42ddb2b6a4446ee4048` |
| state | `paper/PIPELINE_STATE_FINAL.json` | `13fa2e20c6177393386e53584841f8778f7864a7e513475fc45fa6cab809b425` |

The expected terminal mutation inventory is exactly the final PDF plus these
six versioned terminal metadata nodes, including this integrity record. No
unexpected terminal variant or symlink is present in `paper/`.

## Preserved R0 and R1 history

The following pre-existing files were rehashed after final PDF creation and
remain byte-exact:

| Historical node | SHA-256 |
|---|---|
| `paper/PAPER_CONFIGURATION.md` | `9e1d8439e3faa1db334d4eee9c19bf98a23e7fe5d01357123b85afbaa94aa987` |
| `paper/CLAIM_MANIFEST.json` | `d212ca5cde6580087e34c69fe19d3706d140f0cc45d5d662ba9065fe8b1fb8cb` |
| `paper/PROOF_ONLY_PASSPORT.json` | `cc5fbd4836f589a3f5316c69b085868b53f24fa1bf5c95488a4a8010bf3eea6b` |
| `paper/FIGURE_PACKAGE.json` | `46c3e73993342be77edbcb3eb4566ed60486ddf9d1a14ceecbacf1e1b7beb0c0` |
| `paper/PLAGIARISM_MANIFEST.json` | `ada038c79338466dd05b2a0cc57094539884acfe2fdf0dfac6d3e608cf81366b` |
| `paper/PIPELINE_STATE.json` | `a72bc3afba6284abcf318cd9831dec12ffb36415fbd1729033c19656b4aaf6a4` |
| `paper/AUTHOR_PRE_REVIEW_AUDIT.md` | `ed741017ac3820e02b8a990afab2cd973daac089c786ad5072fc71d17d4bbfd4` |
| `paper/INTEGRITY_PRE_REVIEW.md` | `b5ba58d5f0c55ada0be179a1a8eea5516abcf79465f71f5603ae013735c53945` |
| `paper/ROUND1_REVISION_MANIFEST.json` | `858dad0bec9a53b4365698bf7c671dffeccb9d27e865850763da151cdeb7badf` |
| `paper/PIPELINE_STATE_ROUND1.json` | `aac89881de74526db9c81f425a84004f2b036e987dccf06016554d4aeb1fb96e` |
| `paper/INTEGRITY_ROUND1.md` | `186b75544f8204e3416aea44b089f25563c899c9d1c819b7a9473e1ec0c1a9f9` |

The independent Round-1 review remains
`a7fcbb957ecb285dd9d5fb7d1adf5b5b1237a20108b2d01ac468191f72b80f9c`,
its response remains
`e1fbdbb2b9beafdbc956351c98935088d6b02966e772216fd5ec92a82bd48531`,
the exact patch remains
`9a7c526d9bba02b1ccb241f6c28a2412ee34b73b333cde97750fb38335b49a05`,
and the apply report remains
`5c133824a94a4e8e8d15e6260e458972e505fa143beacdac8ffba0320928a533`.
The Round-0 source snapshot and pre-review PDF remain
`de706b358a6b1fdec47da2ab88704ab8011ed22a1dd7de560b8912d0c845a617`
and
`bb3cd34efbff6ec3c2bc2803b0c68b30b701d79833d5a9b4eebeb68d101da949`.

## Frozen proof-only authority closure

| Authority | Path or role | SHA-256 | Boundary |
|---|---|---|---|
| source lock | `experiments/source_lock.json` | `2fa930f697f6040cb16916d2b4dba7ec591a712882c108848e9eecf53608e1c2` | frozen source package |
| source review R2 | `notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md` | `5e66edcd7f33769f748c8b6bd6582aa7e05b3325329839c46bf3627945803d11` | `SOURCE_LOCK_PASS` |
| proof package | `notes/PROOF_PACKAGE.md` | `36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9` | sole scientific theorem authority |
| claims/evidence matrix | `notes/CLAIMS_EVIDENCE_MATRIX.md` | `5630610bb637e155fa631eb2d9c4b36c6ea334ae976a6ef39a53dd733b8c62de` | C1--C18, PC1/PC2, nonclaims |
| novelty assessment | `notes/NOVELTY_ASSESSMENT.md` | `c497dc4e2c404fbbfc3c89450991964d1049f06288a051bc647a15005a66146a` | bounded positioning only |
| citation verification | `notes/CITATION_VERIFICATION.md` | `eb99e7ab59e5d2947b6d5dab0d23dd471c05d090280f7915f010210b021e39ee` | citation-role boundary |
| proof-only scope | `notes/PROOF_ONLY_MANUSCRIPT_SCOPE.md` | `d0dc07976e9631e5d30ffe6d20f1e4d7d76aea4c04d1d42598e3b594d0fc23b9` | manuscript claim boundary |
| registered-audit postmortem | `notes/REGISTERED_AUDIT_POSTMORTEM.md` | `6648a0c3642d24eac1e22f3cc7349a805209d3293b556d6d5d5cbd873d0f831b` | provenance only, not science |
| proof-only lock | `experiments/proof_only_manuscript_lock.json` | `2c7f056b7f9566f754a06c30417105c0b1cefb2d0081f4bca8bb3a00adbf8eeb` | closed eight-path allowlist |
| independent handoff | `notes/INDEPENDENT_PROOF_ONLY_HANDOFF_REVIEW.md` | `407cec5bf295c29330c24ae461dca86ad1bf54d77f44d477d83a821bf7e41711` | `PROOF_ONLY_HANDOFF_PASS` |

Claims C1--C18 and PC1/PC2 remain unchanged, as do nonclaims O1 and X1--X5.
Universal nonvanishing of `D_m` remains open. No D8, D9, E8, or E9 value is
present or used. No global quartic separation claim, global cutoff
`P(4)=3`, method-novelty claim, historical-priority proof, or registered
computational certification is introduced.

## Consumed registered-audit failure provenance

The predecessor disposition remains exactly:

`REGISTERED_AUDIT_TERMINAL_FAIL / NO_RERUN / NO_RAW_RESULT / NO_RESULT_PASS`

Its historical bindings are deployment review
`23000b3478e325271be5f06148037c053bd002befe17345d7f532dfb36183f0c`,
frozen code tree
`3c625fd5357bae97a4ee990443b0a59aa79e7f2d82d5986a5b5b2d8769acd521`,
durable claim
`3b7075f7d5b1b3199c213ae34327f2c80c9f03396b5a792c086416ce99d581c0`,
and terminal record
`1e0896af17907e41f7028a71c056e02d5f8fb4ddf63d3d033063979e0b1d802d`.
These are failure-provenance bindings only and were not read or used as
manuscript science during terminal finalization.

The deterministic Track-Q scalar-versus-pair endpoint attribution remains an
approximately 0.98-confidence forensic inference, not an observed traceback;
child stderr was lost. No scientific mismatch was recorded, and that absence
is not evidence of agreement. There is no Q/R comparison, raw result,
result-pass, certification, D8/D9/E8/E9 value, patch, or rerun. Registered
evidence used is `false`.

## Frozen bibliography and figure assets

The bibliography remains
`f1b6fe0807e33debf87c8be19e1b81b2a4a10f886fd9f4ae1d20bf264e978adc`.
Its 11-entry inventory closes all 10 cited keys; optional `BianchiHe2026` is
the sole unused entry.

| Asset authority | SHA-256 |
|---|---|
| independent asset review R2 (`ASSET_PASS`) | `7b633dd001f1ae086863826612a15d74325406f1eaf2b95fc49e49eddd7ae404` |
| preserved asset review R1 | `d6bc5c624d371752f06ff1d8a8ae27367a7b4c2370b4ab2f19b52cbe24d95ed6` |
| paper plan | `e4876a50d172ccfb857b3c6667a0be85d12105f4d7da63da393531a36cef9d31` |
| citation contract | `997ca84ee7d868f34cacc783993f10d1b82b86c71fbdc1c9b80f38bcf5199bfd` |
| asset tree | `a5006ef63be3bcc585567276f05f063fd6786c6170081e0eea8ec0ca128598ee` |
| figure manifest | `3adc970996ea7a6e1dc043a554c88b8007f4fe203aa30a522b0a4663dcb31096` |
| figure trace | `7ffb609fd2e7a1f4cd1598d750e754787d72b0efec03188b4789e3e95003185d` |
| figure contract | `d9624e640ea36bf4c26fe8c0d9dfffd97c0a34bc0cbc0cc66ab839e91e1d3ac9` |
| LaTeX includes | `c4f111618a2b52689c58d674f4eb89354ed050e29d233cea7b74c1a72d978676` |

The three exact frozen vector PDFs retain SHA-256 digests
`1fbed2c5d27025763b68f660a87f695d4c7fe3a96e7786ef98b0bdccf0a53b79`,
`744853231c1c2700bb29f0ca4d8cf0d4059691966d91a0316c7674c526054835`,
and
`e120cb0c8d05cf884862c3e0d23a8db7b45115e5691fda65620d9bcf203c5f6a`.
They remain on pages 3, 7, and 9. No caption, label, figure, plan, contract, or
asset was regenerated or changed.

## Deterministic terminal rebuild

Two new isolated clean builds were performed under the frozen environment
`SOURCE_DATE_EPOCH=1786838400`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`, and
`LC_ALL=C`, using explicit
`pdflatex -> bibtex -> pdflatex -> pdflatex`. Both builds reproduced every
approved deterministic artifact byte for byte:

| Artifact | Build A | Build B | Approved workspace |
|---|---|---|---|
| PDF | `9541a3ad0ffae34cc5c7a17cfd524de73a6685d1a3f7ba2b472061186b721375` | same | same |
| LOG | `cbbe4b13e6d38a7263956b163572741c7f3fc03621a18222ea5e57b412c7e68c` | same | same |
| BLG | `be7f60aae83be2fe4e5cc3d0d2898fcd73661df5e2333ae4173dc63bb971ad61` | same | same |
| BBL | `ac0ae8c4f0de3188e42f6f0b17775eb1cf90468431b048986ba23caa12dd522a` | same | same |
| AUX | `67a5988dcf5b5359a7933f077ca2a7f92b39f82f5ceb7b8dd23200a935da3824` | same | same |
| OUT | `7b918498371e32fa96c359d8d5fbdf195fa62091df38d36b9b6df9882a9593d1` | same | same |

## PDF, citation, reference, font, vector, and visual QA

- PDF: 19 pages, letter size, unencrypted, no JavaScript or form.
- Visual: the independent Round-2 review passed all 19 pages. Exact approved
  PDF digest identity transfers that 19/19 visual result to the terminal copy.
- Citations: 10 unique cited keys; 11 unique bibliography entries; missing
  keys 0; sole optional unused key `BianchiHe2026`.
- Cross-references: 91 labels, all unique; 43 reference uses over 34 unique
  targets; missing targets 0.
- Fonts: 38 records, all 38 embedded, subset, and Unicode-mapped; Type-3
  count 0.
- Figures: three frozen vector PDFs on pages 3, 7, and 9; raster image objects
  0.
- Diagnostics: LaTeX, package, pdfTeX, BibTeX, citation, reference,
  duplicate-label, undefined, overfull-box, underfull-box, and terminal error
  hits 0.
- Scope scans: bare `quad` source/PDF hits 0; literal D8/D9/E8/E9
  source/PDF hits 0.
- Metadata: visible author `Anonymous`; PDF title, subject, keywords, and
  author metadata blank.

All 19 JSON files under `paper/`, plus the two explicitly allowed experiment
JSON authorities, parse under duplicate-key rejection and non-finite-constant
rejection. All explicit terminal path/hash bindings close. The final
inventory contains exactly the authorized final PDF and six terminal metadata
nodes, with no unexpected terminal variant and no symlink in `paper/`.

## Terminal disposition

The only terminal mutations were creation of the byte-identical
`paper/paper_final.pdf` and the six explicitly versioned terminal metadata
nodes. Every R0/R1/review artifact remains immutable. The terminal status is
exactly:

`COMPLETE_LOCAL_FINAL_REVIEW_PASS`

No further local manuscript, science, source, code, preexecution, result,
runtime, bibliography, figure, scope, citation-evidence, or lifecycle
mutation is authorized under this completed run.
