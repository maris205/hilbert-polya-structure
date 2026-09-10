# C433 citation revision 1: bounded change verification

Checked 2026-09-09 UTC; final local evidence collected at 21:24:14 UTC.

## Disposition and scope

**Zero open citation corrections; no new Critical, Major, or Minor finding.**
CIT-M01 is implemented and closed. Optional CIT-I01 is implemented.
CIT-I02 remains an unavailable/incomplete retraction-screening limitation,
not a negative database result or a correction silently marked complete.

This is the coordinator-authorized check of the actual revision, not a second
literature survey, mathematical review, manuscript pass, or release decision.
The ARS router, academic-paper workflow, citation role and format reference
were reread, along with the applicable repository guidance and batch plan.
The explicit plain alphabetical numbered mathematics style remains controlling.
The role's generic auto-correction instruction grants no edit authority here.
CP qualification, diagonal-operator typography and review disclosure remain
with the coordinator/E8; their diffs were identified, not independently cleared
as a mathematical/manuscript review by this report.

The original [236-line audit](REPORT.md) is immutable and still hashes to
`aa5fdfa7b9d2b635f25a6e9ac5d267529fa0ed879e3f1c54a0fab6c570551fbf`.

## Actual comparison and read extent

I read all ten baseline-to-current source diffs: main.tex, the eight sections,
and references.bib. Five files differ: main.tex, introduction, transfer,
conclusion, and bibliography. The other five section diffs are empty.
The bibliography has exactly the two approved changed fields:

| Original item | Actual source and generated result | Disposition |
| --- | --- | --- |
| CIT-M01, references.bib:5 | `Gonz{\'a}lez-Vega` and `Tom{\'a}s`; rendered González-Vega and Tomás | Closed |
| CIT-I01, references.bib:19 | `Jo{\"e}l`; rendered Joël | Optional normalization implemented |

The complete current 31-line bibliography and complete generated 23-line BBL
were read. The baseline/current BBL diff contains only these name changes and
their line wrapping. No title, date, venue, pagination, DOI, URL, citation key,
ordering, or source version changed. The text's four citation uses retain
their original attributed claims: CDS twice and Kiefer twice. The current
auxiliary mappings are CDS1996 = [1] and Kiefer2013 = [2], with plain style;
the source scan contains no nocite or new reference. Zero orphans remain.

All twelve current source/PDF files were separately compared with their exact
snapshots/v2_round1 counterparts: main.tex, eight sections, references.bib,
main.pdf and main_round1.pdf. Every cmp returned exit 0. The build-directory
PDF, current main.pdf and main_round1.pdf also have the same SHA-256.

I directly viewed the supplied `build/revision1_20260909/visuals/page-11.png`.
Both complete bibliography entries are visible, with the three revised accents,
the existing Björn accent, the mathematical Q, and all displayed identifiers
legible. I read the rendered bibliography text and freshly extracted the PDF
text to stdout: its SHA-256 exactly matches the existing main.txt. I inspected
pdfinfo and all external URL annotations. The PDF has 11 pages, 374,934 bytes.
This was one supplied bibliography bitmap, not an all-page visual review or
independent regeneration of the image. No structural preflight or certified
local-PDF page-anchor PASS is claimed or needed for this scoped check.

## Exact resulting-byte bindings

All paths below are relative to this manuscript directory.

| Artifact | SHA-256 |
| --- | --- |
| references.bib | 318f239a9934e4e9cd1e0467db8b989b0fd47911bda7ef58d3b85c74be93ef41 |
| main.pdf; main_round1.pdf; build/revision1_20260909/main.pdf | 489a1038a9e6f27f589e63b2be6dfe69485a6bd2ab6672360d4407b3ea49a7fa |
| build/revision1_20260909/main.bbl | 42982de30ea22b6f47adc9b9d4203004a4fde4d17c4fc75d495f632b7753f3bc |
| build/revision1_20260909/main.aux | 6ddca63076e95118f65bb54aa2283c664ef5f3d1b84dbe50352f5a644ee2a0d6 |
| build/revision1_20260909/main.txt and fresh stdout extraction | 00e38594979639420d016c7b1e722a6189d844e0faee395b4ba088ed7e4489a7 |
| build/revision1_20260909/visuals/page-11.png | 512dc767ac4bd98d598f45a37f70765d89910e899b038f3b106a81da81cc0010 |

The PDF's exact three external annotation targets remain:

1. https://doi.org/10.1007/978-3-0348-9104-2_8
2. https://arxiv.org/abs/alg-geom/9404011
3. https://doi.org/10.2168/LMCS-9(1:8)2013

They match the visible identifiers and the previously audited targets.
No external resolver or publication status was revalidated in this round.

## Preserved limitations and handoff

All source-access/status limits in the original audit remain in force. In
particular, the Springer full published PDF was not read and its direct DOI
retrieval had failed despite successful publisher metadata access; Kiefer's
primary text was obtained from arXiv after the publisher PDF timed out and
the older author host failed. The earlier public notice screening identified
no matching notice but did not obtain a successful Retraction Watch database
query. This check adds no new search, database, publisher-PDF, plagiarism,
worldwide-novelty, human-read, or current-status clearance. The previously
resolved hidden LMCS bibliography legend is not reopened as an article notice.

Only this new revision-check report was written. The original audit, source,
bibliography, PDFs, snapshots, build outputs, shared records, evaluator and
Git state were not edited by this auditor. No rebuild, mathematics program,
new agent, network/API call, credential action or manuscript upload was run.
The citation corrections are closed on the bound bytes; broader manuscript,
reproducibility, visual-release and mathematical decisions remain separate.
