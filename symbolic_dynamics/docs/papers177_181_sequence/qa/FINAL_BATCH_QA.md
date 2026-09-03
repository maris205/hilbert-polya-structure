# Final batch QA — Route A, P177–P181

**Audit date:** 2026-09-03 UTC.  **Decision:**
`PASS_INTERNAL / ROUND2_DUAL_REVIEW_FREEZE / HOLD_EXTERNAL`.

The closed batch contains exactly five final papers, five paper-local author
controls, ten process-separated hostile-review controls, three immutable PDF
receipts per paper, and two source-only cold builds per paper.  No experiment
is claimed.  All exact programs are bounded proof-regression/falsification
controls; the infinite-family conclusions rest on the manuscripts' written
proofs.

## Paper-local replay gate

| paper | final author control | exact assertions | canonical transcript SHA-256 | result |
|---:|---|---:|---|---|
| P177 | `verify_p177.py` | 1,095,999 | `1ca091424ae0125bf443594b7bbf8c4b61a0fe61826635d7cd9d2e94c1eee501` | byte-identical replay / PASS |
| P178 | `verify_p178.py` | 44,689 | `cc5443ae10945425723343fb1fc0116915ed96f51116a3463b23c0d7ce8d974f` | byte-identical replay / PASS |
| P179 | `code/verify_p179.py` | 252,320 | `e0264ffec9f83da16e45d00ed1801963137c107368c75ef46204addec609f2cf` | byte-identical replay / PASS |
| P180 | `code/verify_p180.py` | 770,697 | `1cc3b6253f83521f6b0cf0fa11a160d90aaa91683341655b78de0381467c024b` | byte-identical replay / PASS |
| P181 | `verify_p181.py` | 6,273,070 | `31cfd5449454e6c682ebb105059329ddd53825df7ea047dfe1d61e7b91d1f24c` | byte-identical replay / PASS |
| **total** | **five paper-local controls** | **8,436,775** | — | **5/5 PASS** |

P179's final total includes 127,202 new comparisons between literal
singleton-isolation histories and the corrected blockwise support formula.
The sentinel `SUPPORT_RESIDUAL_SINGLETON=PASS` guards the late size-one
residual repair.

## Ten reviewer packages

| paper | review A package / assertions | review B package / assertions | package state |
|---:|---|---|---|
| P177 | `reviewer_A_algebra` / 36,510 | `reviewer_B_root` / 224,874 | 2/2 manifests and canonical replays PASS; 0 open |
| P178 | `reviewer_stochastic` / 53,524 | `reviewer_B_root` / 36,899 | 2/2 manifests and canonical replays PASS; 0 open |
| P179 | `reviewer_A_algebra` / 120,977 | `reviewer_stochastic` / 209,583 | 2/2 Round-2 re-entry accepts; manifests and canonical replays PASS; 0 open |
| P180 | `reviewer_A_algebra` / 243,393 | `reviewer_stochastic` / 1,143,286 | 2/2 manifests and canonical replays PASS; 0 open |
| P181 | `reviewer_A_algebra` / 17,364,060 | `reviewer_B_root` / 377,591 | 2/2 manifests and canonical replays PASS; 0 open |
| **total** | **17,818,464** | **1,992,233** | **10/10 packages; 19,810,697 assertions; 0 open** |

Each package contains one hostile-review report, one closed delta receipt,
one reviewer-owned verifier, one canonical transcript, and one
non-self-referential manifest covering the other four items.  The ten
reviewer manifests therefore pass 40/40 declared entries.  Author plus
reviewer controls total 28,247,472 assertions; Stage-1 scouting remains a
separate 11,670,420-assertion breadth record over 38 fresh literal systems.
None of these counts is a count of validated subclasses or evidence of
novelty.

## Two source-only builds per paper

Each cold directory was initialized from only `main.tex` and
`references.bib`, then built through a settled LaTeX/BibTeX cycle.  In every
row, both cold sources match the live sources and both cold PDFs match the
live/Round-2 PDF byte for byte.

| paper | cold directories | pages | bytes | font rows | final PDF SHA-256 | result |
|---:|---|---:|---:|---:|---|---|
| P177 | `qa_final/cold_build_1`, `qa_final/cold_build_2` | 4 | 342,318 | 29 | `ff93b3bf239536ad2256948c6c2877b27435d437f71f2df7f411771a0420516c` | 2/2 exact |
| P178 | `qa_final/cold_build_1`, `qa_final/cold_build_2` | 3 | 294,428 | 24 | `b637423674d7ec40f0e1e316a60f92b1dc5cc3d30061c8cbd444c8aaab5e76ce` | 2/2 exact |
| P179 | `qa_final/cold_build_1`, `qa_final/cold_build_2` | 3 | 256,926 | 20 | `6c93451aa6116c32164ee0d255315f88e0299b60c2ba17879d73c75309e1773c` | 2/2 exact |
| P180 | `qa_final/cold_build_1`, `qa_final/cold_build_2` | 3 | 268,029 | 24 | `d0b08ddc5de6a91a120282d6c31dcc56ca67c1bfdc5202d68b24a22335c80b59` | 2/2 exact |
| P181 | `qa_final/cold_build_1`, `qa_final/cold_build_2` | 3 | 345,290 | 28 | `57f62423e760c5a7f4f3add7bd94a559d99468acea3b05082afa5b28e1d24861` | 2/2 exact |
| **total** | **ten isolated directories** | **16** | **1,506,991** | **125** | — | **10/10 exact** |

All 125/125 font rows are embedded, subsetted, and Unicode mapped.  Settled
logs contain no unresolved citation/reference, rerun request, warning, bad
box, or error.

## Immutable PDF-round receipts

| paper | Round 0 SHA-256 | Round 1 SHA-256 | Round 2/live SHA-256 |
|---:|---|---|---|
| P177 | `28f719fc52d8a06d61b0425df82f718b4592e736028b3137dc7a0212fe053fec` | `ff93b3bf239536ad2256948c6c2877b27435d437f71f2df7f411771a0420516c` | `ff93b3bf239536ad2256948c6c2877b27435d437f71f2df7f411771a0420516c` |
| P178 | `b637423674d7ec40f0e1e316a60f92b1dc5cc3d30061c8cbd444c8aaab5e76ce` | `b637423674d7ec40f0e1e316a60f92b1dc5cc3d30061c8cbd444c8aaab5e76ce` | `b637423674d7ec40f0e1e316a60f92b1dc5cc3d30061c8cbd444c8aaab5e76ce` |
| P179 | `c0a97f79c22799e90b3c2bd95d0060b4b75b38b28536332e5d60fe38f2a5f923` | `9c6018baa87f9e772a46e70cafb59cc804f6711c3a1b82852327df4b00f8bd7d` | `6c93451aa6116c32164ee0d255315f88e0299b60c2ba17879d73c75309e1773c` |
| P180 | `3051dc087aa5c26bb2bcc69e363af75918fe51797dd509161979656fb8ecb248` | `d0b08ddc5de6a91a120282d6c31dcc56ca67c1bfdc5202d68b24a22335c80b59` | `d0b08ddc5de6a91a120282d6c31dcc56ca67c1bfdc5202d68b24a22335c80b59` |
| P181 | `1df6b41b097c29cc933123906fa1539a37c0944bd843d007204c07b2dc824ad0` | `57f62423e760c5a7f4f3add7bd94a559d99468acea3b05082afa5b28e1d24861` | `57f62423e760c5a7f4f3add7bd94a559d99468acea3b05082afa5b28e1d24861` |

All five live PDFs equal their Round-2 receipts.  Distinct earlier bytes are
preserved where theorem source changed; byte equality across adjacent rounds
records a review-only closeout and does not erase provenance.

## Source, manifest, mechanical, and visual gate

- Bibliography/citation key equality passes for **15/15 entries**: 4, 2, 3,
  3, and 3 across P177–P181.  Every source has a bounded background or
  negative-control role; no citation carries a selected theorem claim.
- The five paper manifests contain 18 non-self entries each and pass
  **90/90**.  The ten reviewer manifests contain four non-self entries each
  and pass **40/40**.
- All final PDFs use A4 media boxes, show an anonymous byline and a visible
  external-hold boundary, and have blank identifying metadata.  Encryption,
  forms, JavaScript, personal acknowledgements, affiliations, email
  addresses, and ORCID identifiers are absent.
- All 16 final pages were rasterized and inspected.  No clipping, overlap,
  blank page, missing glyph, malformed equation, illegible reference, or
  running-furniture defect was found.  P180's references-only final page is
  intentional and nonblank.
- P179's corrected Round-2 source is
  `94ff9a5e84d50473b9c48afeb79098bd83cec1e848612e18b71b0b24ac03bbb6`.
  Both original reviewers explicitly re-entered on that source and final PDF
  `6c93451aa6116c32164ee0d255315f88e0299b60c2ba17879d73c75309e1773c`;
  the residual-singleton finding is closed rather than masked by the earlier
  Round-1 acceptance.

## Release boundary

The final gate establishes internal theorem-package and artifact integrity
only.  It does not establish novelty, priority, ownership completeness,
freedom to operate, bibliographic exhaustiveness, or external readiness.  No
upload, posting, circulation, contact, or submission is authorized.  All
five papers remain `ROUND2_DUAL_REVIEW_FREEZE / HOLD_EXTERNAL`.
