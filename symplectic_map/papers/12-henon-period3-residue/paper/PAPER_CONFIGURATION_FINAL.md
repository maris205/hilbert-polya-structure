# Terminal Paper Configuration

- Canonical path base: `papers/12-henon-period3-residue`.
- Candidate/lifecycle: `henon_period3_residue_proof_note_v1`.
- Title: *Period-Three Trace Residues and a Minimal Separator on an
  Exceptional Quartic H\'enon Fiber*.
- Terminal date: 2026-08-16 UTC.
- Final status: `COMPLETE_LOCAL_FINAL_REVIEW_PASS`.
- Format: anonymous 11 pt, single-column specialist mathematics note.
- Evidence mode: theorem proof only; registered evidence is not used.
- Length: 19 pages including references and three frozen vector figures.
- Final source: `paper/manuscript.tex`, SHA-256
  `5c3b09a835aa41f35899f3c720982f911acf7046559c8433f38ab38ce61a0447`.
- Shared commands: `paper/math_commands.tex`, SHA-256
  `40a7fe009279e803be822ad2a3fcae56793b2b5c098e0876800e51d1b4f24510`.
- Bibliography: `paper/references.bib`, SHA-256
  `f1b6fe0807e33debf87c8be19e1b81b2a4a10f886fd9f4ae1d20bf264e978adc`.
- Approved revision PDF: `paper/paper_round1_revision.pdf`, SHA-256
  `9541a3ad0ffae34cc5c7a17cfd524de73a6685d1a3f7ba2b472061186b721375`.
- Live manuscript PDF: `paper/manuscript.pdf`, SHA-256
  `9541a3ad0ffae34cc5c7a17cfd524de73a6685d1a3f7ba2b472061186b721375`.
- Terminal final PDF: `paper/paper_final.pdf`, SHA-256
  `9541a3ad0ffae34cc5c7a17cfd524de73a6685d1a3f7ba2b472061186b721375`.
- The approved revision, live manuscript, and terminal final PDFs are
  byte-identical.

## Independent release authority

The fresh Round-2 verification review is
`paper/reviews/round2_review.md`, SHA-256
`f56ff399b120e5fb9729e51b4d52dcde64df954fb064f32319998d678c3c0577`.
It records verdict `PASS`, disposition `MAY_FINALIZE`, and zero Critical,
Major, Minor, and residual findings. It binds the exact source and approved
revision PDF above and authorizes only hash-preserving terminalization.

The preserved Round-1 chain remains immutable:

- review `a7fcbb957ecb285dd9d5fb7d1adf5b5b1237a20108b2d01ac468191f72b80f9c`;
- response `e1fbdbb2b9beafdbc956351c98935088d6b02966e772216fd5ec92a82bd48531`;
- exact patch `9a7c526d9bba02b1ccb241f6c28a2412ee34b73b333cde97750fb38335b49a05`;
- apply report `5c133824a94a4e8e8d15e6260e458972e505fa143beacdac8ffba0320928a533`;
- revision manifest
  `858dad0bec9a53b4365698bf7c671dffeccb9d27e865850763da151cdeb7badf`;
- pipeline state
  `aac89881de74526db9c81f425a84004f2b036e987dccf06016554d4aeb1fb96e`;
- integrity record
  `186b75544f8204e3416aea44b089f25563c899c9d1c819b7a9473e1ec0c1a9f9`.

The Round-0 source snapshot and pre-review PDF remain byte-preserved at
SHA-256
`de706b358a6b1fdec47da2ab88704ab8011ed22a1dd7de560b8912d0c845a617`
and
`bb3cd34efbff6ec3c2bc2803b0c68b30b701d79833d5a9b4eebeb68d101da949`.

## Deterministic terminal build and QA

Two new disposable isolated clean trees, each containing only the approved
source, shared commands, bibliography, and three referenced figure PDFs,
were built by the explicit sequence
`pdflatex -> bibtex -> pdflatex -> pdflatex` under
`SOURCE_DATE_EPOCH=1786838400`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`, and
`LC_ALL=C`. The builds are byte-identical to each other and to the approved
workspace artifacts:

| Artifact | SHA-256 |
|---|---|
| PDF | `9541a3ad0ffae34cc5c7a17cfd524de73a6685d1a3f7ba2b472061186b721375` |
| LOG | `cbbe4b13e6d38a7263956b163572741c7f3fc03621a18222ea5e57b412c7e68c` |
| BLG | `be7f60aae83be2fe4e5cc3d0d2898fcd73661df5e2333ae4173dc63bb971ad61` |
| BBL | `ac0ae8c4f0de3188e42f6f0b17775eb1cf90468431b048986ba23caa12dd522a` |
| AUX | `67a5988dcf5b5359a7933f077ca2a7f92b39f82f5ceb7b8dd23200a935da3824` |
| OUT | `7b918498371e32fa96c359d8d5fbdf195fa62091df38d36b9b6df9882a9593d1` |

Terminal QA closes at 19 pages, 10 cited keys against 11 bibliography
entries, 91 unique labels, 43 reference uses across 34 targets, and zero
missing or duplicate targets. Optional `BianchiHe2026` is the sole unused
bibliography entry. All 38 font records are embedded, subset, and
Unicode-mapped; Type-3 fonts and raster image objects are zero. Build,
package, BibTeX, citation, reference, undefined, overfull-box, underfull-box,
and terminal error hits are zero. The visible author is `Anonymous`; PDF
title, subject, keywords, and author metadata are blank. Because the terminal
PDF is byte-identical to the independently approved revision, its 19/19
visual QA transfers exactly without a new content judgment.

## Proof-only authority and registered-failure boundary

The sole scientific theorem authority is `notes/PROOF_PACKAGE.md`, SHA-256
`36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9`.
The closed proof-only lock is
`experiments/proof_only_manuscript_lock.json`, SHA-256
`2c7f056b7f9566f754a06c30417105c0b1cefb2d0081f4bca8bb3a00adbf8eeb`,
and the independent handoff is
`notes/INDEPENDENT_PROOF_ONLY_HANDOFF_REVIEW.md`, SHA-256
`407cec5bf295c29330c24ae461dca86ad1bf54d77f44d477d83a821bf7e41711`
(`PROOF_ONLY_HANDOFF_PASS`). Claims C1--C18 and PC1/PC2, together with all
nonclaims, remain exactly within the pre-review claim manifest SHA-256
`d212ca5cde6580087e34c69fe19d3706d140f0cc45d5d662ba9065fe8b1fb8cb`.
Universal nonvanishing of `D_m` remains an open nonclaim.

The consumed predecessor remains exactly
`REGISTERED_AUDIT_TERMINAL_FAIL / NO_RERUN / NO_RAW_RESULT / NO_RESULT_PASS`.
The postmortem at `notes/REGISTERED_AUDIT_POSTMORTEM.md`, SHA-256
`6648a0c3642d24eac1e22f3cc7349a805209d3293b556d6d5d5cbd873d0f831b`,
records only a forensic inference: approximately 0.98 confidence in a
deterministic Track-Q scalar-versus-pair endpoint defect; child stderr was
lost. No scientific mismatch was recorded, which is not evidence of
agreement. No Q/R result, certification, value of D8/D9/E8/E9, patch, rerun,
candidate import, test, or scientific computation supports the note.
Registered evidence remains unused.

## Frozen asset closure

- independent Round-2 asset review (`ASSET_PASS`):
  `7b633dd001f1ae086863826612a15d74325406f1eaf2b95fc49e49eddd7ae404`;
- preserved Round-1 asset review:
  `d6bc5c624d371752f06ff1d8a8ae27367a7b4c2370b4ab2f19b52cbe24d95ed6`;
- asset tree:
  `a5006ef63be3bcc585567276f05f063fd6786c6170081e0eea8ec0ca128598ee`;
- figure manifest:
  `3adc970996ea7a6e1dc043a554c88b8007f4fe203aa30a522b0a4663dcb31096`;
- figure trace:
  `7ffb609fd2e7a1f4cd1598d750e754787d72b0efec03188b4789e3e95003185d`;
- LaTeX includes:
  `c4f111618a2b52689c58d674f4eb89354ed050e29d233cea7b74c1a72d978676`;
- paper plan:
  `e4876a50d172ccfb857b3c6667a0be85d12105f4d7da63da393531a36cef9d31`;
- citation contract:
  `997ca84ee7d868f34cacc783993f10d1b82b86c71fbdc1c9b80f38bcf5199bfd`.

Figures 1--3 retain their exact frozen vector PDF digests
`1fbed2c5d27025763b68f660a87f695d4c7fe3a96e7786ef98b0bdccf0a53b79`,
`744853231c1c2700bb29f0ca4d8cf0d4059691966d91a0316c7674c526054835`,
and
`e120cb0c8d05cf884862c3e0d23a8db7b45115e5691fda65620d9bcf203c5f6a`,
on pages 3, 7, and 9.

This terminal configuration is a base metadata node. It hashes no other new
terminal metadata node and does not hash itself.
