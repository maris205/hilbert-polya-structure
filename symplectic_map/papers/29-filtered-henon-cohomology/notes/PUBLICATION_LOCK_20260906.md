# Local publication and measurement lock

Date: 2026-09-06. Status: locked protocol, not accepted artifact.

1. English, anonymous, article class, 11pt, letterpaper, one column, all margins
   1 inch. Use standard article baselines, paragraph indentation, theorem and
   display spacing. No line-spread changes, enlarged spacing, forced chapter
   page breaks, resized text or text-width manipulation for page counts.
2. Main body: physical pages from the title through the conclusion in Section 8,
   inclusive; 22<=body_pages<=30. References begin on a fresh page and are excluded.
   No appendix or acknowledgments. A physical page must contain substantive body
   content to count; a trailing blank/body-label-only page does not count.
3. Preserve exact mathematical scope and full proofs. Do not duplicate scalar and
   multiphase arguments, present check reports as paper content, or add new results.
   Verified background is only as long as necessary for a self-contained proof.
4. No decorative raster figure or numerical experiment is needed. An inline
   mathematical comparison may be used only if it clarifies a real distinction,
   not to supply missing physical pages. No figure-generation phase is pending.
5. Only verified, actually cited bibliography entries. Use formal journal metadata
   where available and state author-manuscript numbering explicitly if needed.
   Bousch remains a 1992 unpublished manuscript, not a fabricated journal article.
6. Finish one natural source version before its first PDF measurement. Record and
   seal all source files, then build into a fresh explicit directory under build/.
   If that complete, correctly compiled body is shorter than22 pages, stop this
   bounded validation and preserve it; do not lengthen the paper to recover a PASS.
   If it exceeds30, record the failure rather than silently change the locked scope.
7. Ordinary compile defects may receive minimal repairs in a preserved successor
   source/root. Do not erase failure logs or reuse an already failed build root.
   No fix may change the physical page criterion or introduce padding.
8. Use available pdflatex, bibtex, pdflatex, pdflatex with SOURCE_DATE_EPOCH=0,
   FORCE_SOURCE_DATE=1, TZ=UTC and a fixed locale. latexmk is not required.
   Capture each pass log and input recorder. A second fresh root reproduces
   the same source after the first build passes the page gate; compare final PDFs.
   No need for the former Paper28 dependency-capsule infrastructure.
9. Successful compilation is not acceptance. Check body/reference boundary, all
   fonts embedded, undefined references/citations, all equations and the complete
   actual rendered document. An independent reader reviews the real source/PDF
   for proof fidelity, attribution, substantive pages, no padding and scope.
   A final independent integrity review binds the accepted source and actual PDF.
10. Review/fix rounds address real translation, content or rendering defects,
    preserve versions and recheck changed dependencies only. No automatic demand
    for new science, experiments or repeated prior-art searches.
11. Publication effect: local anonymous deliverable only. No submission, upload,
    hosting, push, external message or paid resource. The old candidate FAIL
    remains unchanged even if a new artifact is eventually accepted.

The source and build may be inspected locally using installed tools. No credentials
or new access scope are required. Paper27/28 accepted artifacts remain untouched.
