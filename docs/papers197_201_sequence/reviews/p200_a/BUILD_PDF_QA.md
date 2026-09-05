# P200 Review A: cold source reproduction and actual visual QA

The fresh temporary build directory received only round0_snapshot/main.tex
and references.bib. The batch review_cold_build.sh then ran pdflatex with
recorder, BibTeX and two further pdflatex passes under epoch1704067200,
FORCE_SOURCE_DATE1, TZUTC and LC_ALLC. All returned zero. cmp matched the
frozen PDF7226b56257356fe3869a957983e0c92a7dbc79470f3e504f0f031c4b6248b3ea.
Generated inputs, outputs and logs remain in cold_build/.

Final main.log/main.blg have no Warning, Overfull, Underfull, undefined or
Error matches. Poppler reports4unencrypted A4pages,290689bytes, blank
identifying metadata, no forms or JavaScript. All21font rows show embedded,
subset and Unicode flags yes. The frozen PDF was rendered at120dpi and
ALL FOUR images were individually viewed by root in this Review A:

| Page | Observed content and result |
|---|---|
|1|Title/abstract, literal map, three-source boundary and row notation; readable, no clipping|
|2|Invariant-pivot lemma, full recurrence proof, row-clock theorem and two-visits argument; no overflow|
|3|Complete sharp itinerary, width qualification, inverse iff and proof; formulas fit and correct order|
|4|Maximizer theorem/proof, finite table, HOLD_EXTERNAL and all three references; legible, no overlap|

No visual repair requested. This is one manuscript-review cold build,
not the later terminal two-cold-build requirement and not venue compliance.
