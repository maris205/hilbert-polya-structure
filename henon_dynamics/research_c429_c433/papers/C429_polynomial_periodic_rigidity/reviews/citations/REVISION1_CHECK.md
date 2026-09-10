# C429 citation revision-1 check

## Result

**No open citation findings.** The revised Cattani–Dickenstein–Sturmfels locator correctly identifies the accessible preprint actually inspected in the original audit. All six citation keys, alphabetical reference numbers, bibliography entries, and eleven distinct external PDF link targets are preserved. This is a bounded revision check, not a fresh mathematical review, admission decision, peer-review verdict, or comprehensive source-status clearance.

The immutable 195-line `REPORT.md` remains the original baseline citation audit. Its unchanged primary-source checks are reused with all qualifications. The ARS citation workflow guides the locator/output comparison; the explicit revision-only scope overrides a new search, preflight, build, or automatic source correction. Only this new report was written.

## Input binding and actual read extent

The actual revised `main.pdf` has 16 pages and 423936 bytes, independently confirmed by `pdfinfo`. Its SHA-256 is:

```text
635f6868081c83ac0d76adde5ffe6a80e8eb7077a5c72dd44f7e7f19d75a36c6
```

The original audit binds the earlier PDF `118733318d139821d5cb29ab8deccc9d46fe577230563fbd38858df7ea431a02`; these versions are not conflated. Actual checked files for this revision include:

```text
1a607bc23fc307c86f15d4a489d260c0c9bd31ad77475bec9340ee4738e8a7b0  main.tex
17d4ee29e93504bb8f618f2221eb94feab237d368aac894b45dcdd125eb54c0e  sections/01_introduction.tex
2572ac5a6b6be971085d89df647042ea43f62df451b8c65962f31466db22f04b  references.bib
7922a4deb30d1ab568b3cf819d4be641de580f250c58f696660091feab81ce0c  main.bbl
1fa2ab8663dbe60e94bead4c6b4f3165f0454e1666f182ae6adfc6a0ea827c48  main.aux
2ecb0559cee12b7a75ce3acdc65f5b5a97a59191476bd8290aa6694ad834d7ee  reviews/citations/REPORT.md
bb0a9d613ae966a43a4eb25616c58a7bf1e436b24c2f7ee43b035527eb9fe60c  revisions/round1_author_revision_01/SOURCE_DIFF.patch
f5f5aa7a472e4461ca7f9dbda208c6a2355c64715b1ae91eb101f3c0bb848401  revisions/round1_author_revision_01/PDF_TEXT_DIFF.patch
```

I read the complete source and extracted-text diffs, independently diffed the actual current `main.tex` and introduction against `snapshots/author_baseline/`, read the current entry point and changed introduction context, and read the complete current `main.bbl`. The current hashes of `math_commands.tex` and Sections 2–7 still match the original audit. A scan of all active source files finds the same six citation occurrences and no `nocite`; the generated auxiliary citation/number mappings were checked directly. This is not a new full read or mathematical review of the unchanged proof sections.

I extracted the actual revised PDF's pages 2–3 and 15–16, inspected its external-link annotations, and visually viewed the existing revision images `revisions/round1_author_revision_01/visual/page-03.png`, `page-15.png`, and `page-16.png`. No new rendering, compilation, broad source search, retraction search, or structural preflight was run. Log/state review is not claimed as a new check here.

## Changes and citation disposition

| Actual source change | Citation assessment |
|---|---|
| Abstract now states an integer degree cap `M >= 1` | No citation added or altered. Mathematical validity is outside this check. |
| Introduction now says a nonzero scalar multiple of the powered leading coefficient | No external attribution or theorem dependency added. This report does not adjudicate that mathematical repair. |
| Introduction line 138 changes the locator to `Section 4 of the accessible preprint` for `cattani1996residues` | Supported. Original audit Section [1] directly inspected [the accessible author preprint's Section 4](https://arxiv.org/html/alg-geom/9404011v1), including its normal-form/residue/trace material. The added qualifier accurately distinguishes that read from unavailable full published-chapter access. |

The 1996 published chapter remains the bibliographic item, with the same explicitly labeled accessible preprint URL. The locator change neither introduces a new source nor claims that the full published chapter was inspected. The Levin–Sodin–Yuditskii abstract-only disclaimer and attribution through the inspected 1998 paper remain intact. Other source-applicability and bounded-priority statements are unchanged.

## Preserved generated output

| Number / key | Occurrences | Revised displayed locator | Revised citation page |
|---|---|---|---|
| [1] `cattani1996residues` | 1 | Section 4 of the accessible preprint | 3 |
| [2] `cvitanovic1998beyond` | 1 | Section 4 | 3 |
| [3] `kalinin2011livsic` | 1 | Theorem 1.1 | 2 |
| [4] `levin1994ruelle` | 1 | Historical attribution, no theorem locator | 3 |
| [5] `li2025ground` | 1 | Theorem 1.1 | 3 |
| [6] `zou2025finite` | 1 | Theorem 1.1 | 3 |

The Li–Zhang citation moved from original p. 2 to revised p. 3 through reflow; its surrounding sentence begins on p. 2. The original report's old PDF page map is not silently reused for this new PDF.

Both `references.bib` and generated `main.bbl` are byte-identical to those in the original audit. There are six references, no missing key, no unused entry, and no changed numbering. The bibliography remains on pages 15–16, with [1]–[2] on p. 15 and [3]–[6] on p. 16. The inspected revised images show readable entries, accents, page ranges, and links without clipping. The mildly stretched Li–Zhang line remains an optional cosmetic item, not a new citation defect.

`pdfinfo -url main.pdf` returns the same sixteen annotation rows representing eleven distinct URLs: six DOI targets and five accessible-text alternatives. Every target matches the original audit, including the chapter DOI underscore, the Cvitanović author-hosted path, both explicit arXiv v2 links, and the JAAC PDF path. Link preservation is not a fresh assertion that every external endpoint resolves.

## Qualifications carried forward

All original source-access limitations remain in force: the 1994 Levin–Sodin–Yuditskii full text is unavailable and no unread theorem from it is invoked; the Cattani published chapter and Li–Zhang publisher landing pages were not treated as complete published-text reads; four original DOI opens failed despite primary metadata corroboration; IOP's current publisher-status page was blocked; the Retraction Watch interface was unusable and no database query was completed; no machine-verifiable Crossmark clearance was obtained. The Li–Zhang arXiv administrative text-overlap note remains neutrally recorded, without a misconduct or retraction inference. The original bounded public search found no matching correction/retraction notice, not a universal guarantee.

The original PDF preflight was `UNAVAILABLE` because its parser was missing. It has not been rerun for the revised PDF and no new structural PASS is claimed. Page locations here rest on the documented extraction and existing visual inspection, with source line 138 the primary changed-citation anchor. The original audit's remaining integrity, similarity-screening, and non-peer-review limitations also remain unchanged.

**Handoff:** zero open citation must-fixes and zero source/PDF corrections requested for this exact revised hash. Preserve both citation reports separately. Any further source or PDF change needs its own appropriately scoped check; this result does not replace the separately assigned full manuscript review.
