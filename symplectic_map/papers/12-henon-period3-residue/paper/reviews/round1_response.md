# Response to Independent Manuscript Review — Round 1

Date: 2026-08-16 UTC  
Manuscript: *Period-Three Trace Residues and a Minimal Separator on an
Exceptional Quartic Hénon Fiber*  
Round-1 review SHA-256:
`a7fcbb957ecb285dd9d5fb7d1adf5b5b1237a20108b2d01ac468191f72b80f9c`  
Round-1 recommendation: `MINOR REVISION — DO_NOT_FINALIZE`  
Revision state: `READY_FOR_INDEPENDENT_ROUND2`

We implemented the sole requested correction, M1, as exactly seven
source-token substitutions. Each bare text token `quad` in the displayed
transfer-flow formulas was changed to the LaTeX spacing command `\quad`.
No surrounding mathematics or prose was changed. No theorem, formula value,
claim, qualifier, equation tag, citation, bibliography entry, figure, caption,
label, scientific input, proof-only authority, or Round-0 record was changed.

## Response to M1: seven bare `quad` tokens

**Reviewer comment.** Page 12 rendered seven literal `quad` strings because
the corresponding source tokens lacked leading backslashes. The review
required the seven tokens at source lines 867, 869, and 882--884 to become
`\quad`, with no surrounding change.

**Response.** The requested edit was applied exactly:

| Round-0 source line | Token substitutions | Round-1 result |
|---:|---:|---|
| 867 | 1 | `s_d=j,\quad T_d=0,` |
| 869 | 1 | `s_i=0,\quad T_i=r\quad(i\ne d).` |
| 882 | 2 | `U_1=0,\quad V_2=0,\quad` |
| 883 | 2 | `V_1=r-u,\quad U_2=r-v,\quad` |
| 884 | 1 | `n_1=r-u,\quad n_2=r-v.` |

The revised source and extracted PDF text each contain zero bare `quad`
tokens. Page 12 was rendered and inspected at full-page resolution; the
transfer formulas now show normal mathematical spacing with no literal
artifact.

**Status:** `RESOLVED`.

## Exact and reversible change record

The Round-0 source is byte-preserved at
`paper/revisions/manuscript_round0.tex`, SHA-256
`de706b358a6b1fdec47da2ab88704ab8011ed22a1dd7de560b8912d0c845a617`.
The coordinate-guarded patch is
`paper/revisions/round1_patch.json`, SHA-256
`9a7c526d9bba02b1ccb241f6c28a2412ee34b73b333cde97750fb38335b49a05`.
Its application report is
`paper/revisions/round1_apply_report.json`, SHA-256
`5c133824a94a4e8e8d15e6260e458972e505fa143beacdac8ffba0320928a533`.

The unified diff has five removed and five added source lines and exactly
seven token substitutions. The source remains 1,419 lines; its byte count
increases by seven, precisely one backslash per corrected token. Mechanically
reversing the seven recorded operations reproduces the exact Round-0 source
digest above. The revised source SHA-256 is
`5c3b09a835aa41f35899f3c720982f911acf7046559c8433f38ab38ce61a0447`.

The unchanged Round-0 review PDF remains
`paper/paper_pre_review.pdf`, SHA-256
`bb3cd34efbff6ec3c2bc2803b0c68b30b701d79833d5a9b4eebeb68d101da949`.
All Round-0 configuration, manifest, passport, audit, pipeline, plagiarism,
figure-package, and integrity records remain byte-exact.

## Rebuild and QA

Two fresh isolated trees were built under the deterministic environment
`SOURCE_DATE_EPOCH=1786838400`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`, and
`LC_ALL=C`, using the explicit sequence
`pdflatex -> bibtex -> pdflatex -> pdflatex`. The PDF, LOG, BLG, BBL, AUX,
and OUT files are pairwise byte-identical across the two builds, and the live
workspace artifacts match them exactly.

| Artifact | SHA-256 |
|---|---|
| Revised `paper/manuscript.tex` | `5c3b09a835aa41f35899f3c720982f911acf7046559c8433f38ab38ce61a0447` |
| `paper/manuscript.pdf` | `9541a3ad0ffae34cc5c7a17cfd524de73a6685d1a3f7ba2b472061186b721375` |
| `paper/paper_round1_revision.pdf` | `9541a3ad0ffae34cc5c7a17cfd524de73a6685d1a3f7ba2b472061186b721375` |
| Terminal `paper/manuscript.log` | `cbbe4b13e6d38a7263956b163572741c7f3fc03621a18222ea5e57b412c7e68c` |
| `paper/manuscript.blg` | `be7f60aae83be2fe4e5cc3d0d2898fcd73661df5e2333ae4173dc63bb971ad61` |
| `paper/manuscript.bbl` | `ac0ae8c4f0de3188e42f6f0b17775eb1cf90468431b048986ba23caa12dd522a` |
| `paper/manuscript.aux` | `67a5988dcf5b5359a7933f077ca2a7f92b39f82f5ceb7b8dd23200a935da3824` |
| `paper/manuscript.out` | `7b918498371e32fa96c359d8d5fbdf195fa62091df38d36b9b6df9882a9593d1` |

The revised PDF remains 19 pages. Page 12 and all 19 pages passed visual
inspection, with no clipping, overlap, missing glyph, unreadable figure, or
float regression. LaTeX, package, pdfTeX, BibTeX, citation, cross-reference,
overfull-box, and underfull-box warning or error hits are zero.

The bibliography remains exactly 11 entries with closure for all 10 cited
keys; optional `BianchiHe2026` remains the sole unused entry. All 91 labels
are unique, and all 43 reference uses resolve. The three frozen figure blocks
remain unchanged and render on pages 3, 7, and 9. All 38 font records are
embedded, subset, and Unicode-mapped; Type-3 fonts and raster image objects
are zero. PDF title, subject, keywords, and author metadata remain blank, and
the visible author line remains `Anonymous`.

## Proof-only and scope regression

The exact seven-token diff leaves C1--C18 and PC1/PC2 unchanged under the
frozen claim manifest. The full Step-9 certificate, the separate fixed-moment
and local-multiplicity arguments, both source-level quartic-slope derivations,
quartic-fiber minimality, and every nonclaim are unchanged. Universal
nonvanishing of `D_m` remains open. The source and PDF contain no D8, D9, E8,
or E9 value or label. Registered evidence remains unused.

The revision continues to be governed by the proof-only lock SHA-256
`2c7f056b7f9566f754a06c30417105c0b1cefb2d0081f4bca8bb3a00adbf8eeb`,
the independent proof-only handoff SHA-256
`407cec5bf295c29330c24ae461dca86ad1bf54d77f44d477d83a821bf7e41711`,
and proof authority SHA-256
`36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9`.
No code, preexecution, result, or runtime input was read or used for this
revision.

## Commitment ledger

```yaml
- concern_id: R1-M1
  commitment_extracted:
    - commitment_text: "Replace exactly seven bare quad tokens by \\quad without any surrounding source change."
      commitment_type: correct_latex_rendering
      required_evidence_type: exact_reversible_source_edit_and_pdf_regression
      fulfillment_status: fulfilled
```

## Round boundary

Round 1 resolves M1 but does not authorize finalization. The revised package
is stopped at `READY_FOR_INDEPENDENT_ROUND2`. No `paper_final.pdf` exists. A
fresh, hash-bound Round-2 reviewer must verify the exact seven-token diff,
the corrected page-12 rendering, and the regenerated downstream integrity
chain.
