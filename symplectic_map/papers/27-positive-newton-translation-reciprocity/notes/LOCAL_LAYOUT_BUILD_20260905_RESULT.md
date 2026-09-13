# Preserved second local attempt and read-only diagnosis

Status: FAIL_PRESERVED_NO_RETRY

The reviewed layout script ran once in session 72428 and exited 1 after r0's four publication commands all completed with status 0. The exact stored failure is `BIB_LOG`; r1 was never touched or started. The evidence and source root at `build/layout-20260905-evidence` and `build/layout-20260905-r0` remain intact. No successful-build or release classification is assigned to them.

Actual main.pdf: 336871 bytes, SHA256 `ab195a2b49012e9b4b320ddbabffd9666c076b37b09a8b9dc20c400dd266a5b4`, 29 total pages; reference sentinel 28 gives 27 proof pages. All 13 prior overfull boxes are gone. Custom Metadata is now no; the Creator, Producer and epoch dates remain correct.

Read-only downstream diagnosis, without rerunning a publication command, found two validator representation errors:

1. `citation_check` incorrectly matches the substring `warning` in BibTeX's normal built-in function statistic `warning$ -- 0`. This line reports zero calls, not a diagnostic. The whole actual blg was read; it has the expected plain.bst and sole references.bib database, 20 entries and no real warnings/errors.
2. Layout-preserving PDF extraction interleaves the boundary table's columns and hyphenates narrow labels. Requiring every boundary label to appear contiguously in that extraction falsely fails at `Positive coordinates`. A separate `pdftotext -raw` diagnostic preserves cell order and displays all seven labels. Only three exact physical-wrap aliases are needed; neither the PDF nor source should be rewritten for this parser issue.

The unchanged PDF semantic/font/security/geometry/metadata validator passed diagnostically for these actual bytes. It found 22 embedded Type1 fonts, no parser repairs or unsafe objects, letter portrait pages and correct dates. Final TeX log acceptance passed with zero overfull and 18 retained underfull hboxes; independent warning/content review and main visual inspection are separate requirements.

The next bounded correction is a new standalone final-build script with unchanged source identity and fresh namespaces, not a replay or reclassification of this failed attempt. It must receive independent prebuild delta review, all pure tests and read-only downstream diagnostics before its one actual execution. This is correction 3/3; no further automatic compile-fix cycle is planned.
