# Paper20 independent deterministic-build review (R2)

**Review ID:** BUILD_R2_2026_08_22

This is a read-only readback of the author-stopped build receipt and PDF. No
rebuild, source edit, auxiliary-file edit, transport action, or publication
action was performed. The generated auxiliary files were inspected as declared
outputs; no new output was created by this review.

## Receipt and output identity

paper/BUILD_RECEIPT_R0.json is canonical JSON, 4,259 bytes/LF1, SHA
3e7da7d9b66c02f68864d04c177ff12317e52d87b3c38c7fc8748f95ca9e4d62. Its
self identity is null/self-excluded and its own hash/byte count do not occur
in its content.

The declared source bindings all match the current files, including the final
R2 source review identity:

* main.tex: 37,423 B, SHA
  2a27dc745bffa7c9efb2016edb416045216d9fcd8bad7beadf9143716eee2014;
* math_commands.tex: 702 B, SHA
  37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582;
* references.bib: 2,335 B, SHA
  529612c446e0a56919efb79dae7f80358f4f3fa1fc3424e6e15f7da2886c5eaf;
* BUILD_METADATA_R0.json: 3,588 B, SHA
  75e94cc9da7dd738fd287db32994fb98863d65c00350201ac6c77e48d017cc9c;
* PAPER_PLAN.md: 22,064 B, SHA
  4dfcf82f8dae85502fced2f7b1d73d80e35ee242eee609dd74b5f59ca793adf3;
* experiments/source_lock.json: 11,847 B, SHA
  57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581.

The PDF is a regular 0644 file, 380,574 bytes, SHA
ed58824860f77186210fee298b1631e7877868dc828b4b3a9cd048fcaa1545e9.
All six declared output files (main.pdf, .aux, .bbl, .blg, .log, .out) match
the receipt's byte, LF, mode, regular-file, and SHA fields.

## Deterministic build and diagnostics

The receipt records the authorized four-command sequence
pdflatex -> bibtex -> pdflatex -> pdflatex, with interaction nonstopmode and
halt-on-error; fixed SOURCE_DATE_EPOCH=1787356800, FORCE_SOURCE_DATE=1,
LANG=C, LC_ALL=C, and TZ=UTC; no network access; complete sequence; and no
source edits during build. The PDF metadata creation time is consistent with
the fixed epoch.

Independent readback confirms:

* 14 PDF pages, no encryption or corruption;
* zero fatal errors, undefined references, undefined citations, marker hits,
  and overfull boxes;
* BibTeX warning count zero;
* all 24 reported fonts embedded and subset;
* PDF text has no ??, [?], TBD, TODO, VERIFY, Missing $, or undefined tokens;
* displayed equation references resolve to the intended numbered labels
  (6.1)--(6.6), and conclusion/reference ordering matches the receipt.

Residual diagnostics are nonfatal but recorded: three underfull boxes in the
collision table, four hyperref PDF-string warnings from math in headings, and
one final label-changed warning. Since the PDF has no undefined references and
the extracted cross-references are correct, these are advisory cleanup items,
not independent fatal/build-integrity failures.

## Page-budget gate (blocking)

The build result is **not consistent with the locked page contract**. Both
PAPER_PLAN.md and BUILD_METADATA_R0.json define a substantive-page target of
24.0 pages with an authorized minimum of 22 and maximum of 26, measured
through the conclusion and excluding references. The receipt explicitly reports
body_through_conclusion_page=14, and independent PDF text readback places the
Conclusion on page 14. References begin later on that same page, so excluding
references cannot raise the substantive body count above 14.

Thus the built body is eight pages below the locked minimum and ten pages below
the planned target. The receipt does not contain a page-budget pass/fail field
or an amended plan/metadata scope. This is a contract-level mismatch, not a
mere underfull-box warning. To clear it, the author must either (a) expand and
rebuild the manuscript to the locked 22--26-page substantive range, or (b)
obtain an explicit authorized revision of the plan/metadata page contract and
regenerate the receipt. The reviewer cannot choose between those paths.

## Verdict

BUILD_R2_BLOCK

The deterministic build, PDF identity, source bindings, diagnostics, and fonts
pass mechanically. The build is blocked solely because its 14-page substantive
body violates the explicit 22--26-page/24-page plan contract. No publication,
upload, transport, or further build is authorized by this receipt review.
