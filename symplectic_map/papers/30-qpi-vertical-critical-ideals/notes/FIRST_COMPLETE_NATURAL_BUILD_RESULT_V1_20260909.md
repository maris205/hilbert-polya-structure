# Paper30 first successful complete natural build: actual result and stop

Date: 2026-09-09. Status: `BUILD_SUCCESS / PAGE_WINDOW_FAIL / USER_DECISION_REQUIRED`.
Batch07 local acceptance remains **3/5**; Paper30 is not accepted and Paper31 has not started.
This record reports actual production evidence, not a capacity forecast or a scientific re-vote.

## 1. Source and build succession

The [complete static disposition](COMPLETE_DRAFT_STATIC_DISPOSITION_V1_20260909.md)
accepts the complete V1 proof transcription plus the three V2 wording/citation clarifications.
The first production root r0 used all eleven frozen V2 files; its first pdfLaTeX
process failed at a TeX optional-row-spacing ambiguity. No PDF was generated.
Its source, raw stdout and auxiliary/log files remain untouched.

The [failure and V3 recovery record](FIRST_NATURAL_FAILURE_AND_RECOVERY_V1_20260909.md),
SHA-256 `729af58292b30c1cdee472d7cb749f3c9ae07892581273eab1539f4f3d054110`,
was written before the recovery run. V3 changes only the cases-row syntax and displays
one identical equation to remedy the observed 50.51622pt overflow.
The whole 59-line [non-author fix-delta report](BUILD_FIX_DELTA_RECHECK_V1_20260909.md)
was read and accepted by the root; its SHA-256 is
`ac60f1a3bb9f2909cb09deab6d4bc463e9cc049903e144f376a4e2b3050f890b`.
Its nine unchanged files were checked byte-for-byte; no scientific content or layout
parameter changed. This is ordinary compiler recovery, not a new candidate review.

The complete frozen source `paper/v3/` was copied into the absent
`build/natural-20260909-r2/work/`. All eleven source checksums passed before copying,
on the copy before compilation, and on the copy after the final pass.
The checksum file [SOURCE_V3_20260909.sha256](SOURCE_V3_20260909.sha256) has SHA-256
`ea4cbd50e6aa4539126b82e035880dc706696ac90319d0c1f73afe9275801ac4`.

## 2. Actual process results

The exact four commands, flags, fixed environment and local dependencies are those
recorded before execution in the first-build protocol and V3 recovery record.

| r2 process, in order | Exit code | Actual result |
|---|---:|---|
| pdfLaTeX pass 1 | 0 | Complete source processed; expected first-pass references not yet converged. |
| BibTeX | 0 | 17 entries used, no BibTeX warning or error. |
| pdfLaTeX pass 2 | 0 | Bibliography included; normal citation/label convergence warnings remained. |
| pdfLaTeX pass 3 | 0 | Final PDF; no undefined citation/reference or rerun request. |

No extra convergence pass was needed. The four complete stdout logs and the final
TeX/BibTeX auxiliary inputs remain in r2. No failed or successful root was cleaned.

## 3. Physical page result and independent confirmation

Actual [complete draft PDF](../build/natural-20260909-r2/work/main.pdf):
**41 total pages = 39 body pages + 2 reference pages**, 546638 bytes, PDF 1.5, letter
612 × 792 pt. SHA-256:
`06a4e848e177b6b69a6593b7894286f55babb1ba09d64b29a1263d926c075d91`.

The root checked pdfinfo, all extracted page boundaries, the `LastBodyPage=39`
aux label and the actual page-39/page-40 images. Page 39 contains the final
state-order corollary, its proof and the closing scope limits. References start on
a separate physical page 40 and continue through page 41; no cover or empty page is subtracted.

A fresh independent non-compiling agent confirmed the same PDF identity, all 41
physical/printed page numbers and actual images of pages 39–41 in the 62-line
[boundary check](FIRST_PDF_BOUNDARY_CHECK_V1_20260909.md), SHA-256
`6fa9fa7a6a76f981d9d415b8f97985cc9f8a37d70c17fcdc24eb9e7a6acbf8b7`.
The root read that entire terminal report and checked its identity.
This limited check is not an independent full-manuscript/PDF acceptance.

The locked body range is 22–30. **39 > 30 by 9 pages: PAGE_WINDOW_FAIL.**
This actual result supersedes forecasts only for production-page evidence; it does
not rewrite the original candidate votes, change the contract or revoke proven content.

## 4. Actual logs, fonts and limited visual checks

Final TeX log: no undefined references/citations, missing-character/font warnings,
fatal errors or underfull boxes. BibTeX used all 17 intended entries with zero warnings.
pdffonts reports 23 font resource rows, all embedded Type 1 fonts.
This is not a claim of a zero-warning build: two overfull paragraphs remain.

| Remaining issue | Actual location | Width | Disposition |
|---|---|---:|---|
| Cyclic matrix equation in the fixed-Picard paragraph | §3 source 313–321, PDF p.14 | 9.96825pt | Actual page viewed: right-margin protrusion, no visible clipping; not yet repaired. |
| Cohomology identities at the start of the obstruction proof | §6 source 46–51, PDF p.22 | 6.8397pt | Actual page viewed: right-margin protrusion, no visible clipping; not yet repaired. |

The root also viewed actual pages 19, 20 and 30. Page 20 confirms the formerly
50.51622pt insertion-equation overflow is resolved; page 30 renders the two correct
support intervals. Root images are retained in `r2/inspection/`.
Root visual reading in this stage covers only pages 14, 19, 20, 22, 30, 39, 40,
not all 41 pages. Full visual/PDF acceptance is explicitly not granted.

## 5. Bound final artifacts

Paths below are relative to `build/natural-20260909-r2/`.

| Actual artifact | Bytes | SHA-256 |
|---|---:|---|
| `work/main.pdf` | 546638 | `06a4e848e177b6b69a6593b7894286f55babb1ba09d64b29a1263d926c075d91` |
| `work/main.aux` | 19856 | `b2b43885bf4ef9c7083975586b1320c3fe6dd31a1c6b7a87b6a7ab91f931abd2` |
| `work/main.bbl` | 6040 | `41d28bd7f9d20856e5e70d22879183dd8c6458d0e5f490e053f7a61bed79f819` |
| `work/main.blg` | 914 | `1199addeddc0e44a5028f0cca03ef758bd702c07331ba70f7b4c78a74d1136f4` |
| `work/main.log` | 24432 | `1424a5b431c99cc0c303f06d7496320ca4fddb3a01c37f23c2b8352f132f2c8f` |
| `work/main.fls` | 51361 | `2b0bebdfa7805f36d551b99d62efe54c8e4f831b82a00ddb51f346a4addee7c6` |
| `pdflatex-1.stdout.log` | 26138 | `bb241a706601c7da96df7cd0074c1c0a0e10d6bfa3a63ab17ed4546517e6a8fe` |
| `bibtex.stdout.log` | 158 | `7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9` |
| `pdflatex-2.stdout.log` | 11063 | `e98f2506ed7eabaa556dd564b3e65006ccb85dd4b0ed949899be3fc3a18f8192` |
| `pdflatex-3.stdout.log` | 7759 | `cccc297fdeb55a85293bea6f25b275d21a6e3f1bdd08f7018949acc23fbebb1e` |
| `pdfinfo.txt` | 569 | `e2727a43d92cd392b2840e27bfe1e52d7e8c8f1cd608f94ca779ae882e72106e` |
| `pdffonts.txt` | 2350 | `296bf836eb76659a020c8145185a1bafb7e56ee5014fd8291acbe562023c503d` |
| `main.layout.txt` | 147542 | `93979c41e61cecdd1b43aabb6bc690529c5e668dc23e0e1e9e0ed33b4e8b276f` |

## 6. Current boundary and next decision

The unchanged [publication lock](PUBLICATION_LOCK_20260909.md) requires a page-window
pass before the independent second-root build. Therefore no r1/r3 second build was
started; both roots were checked absent. Byte determinism, complete actual-PDF review
and independent final integrity/acceptance remain unperformed, not failed tests.

The actual complete source/PDF, V1/V2, r0 failure and all immutable controls remain
preserved. No font/margin/line-spacing shrink, proof deletion, appendix transfer,
candidate splitting, page-threshold change or external operation has occurred.
The two residual local layout issues are accurately recorded; they cannot explain
or cure the nine-page window excess and are not used to justify repeated page probing.

Changing the page contract or locked scientific scope needs an explicit user decision.
No such change has been authorized. Local work now pauses at that decision boundary;
Paper30 does not count as the fourth accepted paper and Paper31 does not advance.
