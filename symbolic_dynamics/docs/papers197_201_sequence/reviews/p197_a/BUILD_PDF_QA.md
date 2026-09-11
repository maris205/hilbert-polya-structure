# P197 Review A — source-only build and four-page inspection

Frozen PDF SHA-256:
`42cb9e1e7cd10858a7ecf98faf2d8ced79faeb31211f608fd20f4b75a01b792a`.

The clean temporary directory `/tmp/p197-review-a.QFjTqI` received only
the frozen `main.tex` and `references.bib`. `latexmk` was unavailable
(exit 127); no package was installed and no source was edited. The safe
fallback was pdflatex, bibtex, pdflatex, pdflatex, each with noninteractive
error-stop options where applicable. All four processes exited zero.
The resulting PDF has exactly the frozen hash above. Final main.log and
main.blg contain no Warning, Overfull, Underfull, undefined or Error matches.
Early first-pass missing citations are ordinary before-BibTeX diagnostics
and are retained in pass1.stdout, not concealed as final warnings.

Poppler reports four unencrypted A4 pages, 371,181 bytes, no JavaScript or
forms, and empty identifying metadata. All 28 font rows show embedded,
subset and Unicode mappings. No unresolved citations or equation numbers
were seen in the rendered pages.

## Actual page-level inspection

The frozen PDF, not a different draft, was rendered at 125 dpi using
pdftoppm. All four resulting images were individually viewed.

| Render | Inspected content | Result |
|---|---|---|
| page-1.png | title/abstract, map, source boundary, local-lemma statement and first proof paragraph | readable; no clipped text or missing glyphs |
| page-2.png | complete eight-row certificate, sharp-core theorem, witness phases, small-size qualification | readable table and formulas; lower-bound qualification present |
| page-3.png | full depth/cycle theorem, characteristic polynomial and Newton certificate, inverse theorem | equation numbering and matrix entries legible; no truncation |
| page-4.png | fibre proof, all maximum equality cases, exact-evidence table, limitations and all three references | all entries present; no overlap or overflow; hold notice visible |

No visual repair is requested. The document is an anonymous internal
short note; no unconfirmed venue/page-limit compliance is claimed.

## Structural-preflight limitation

The ARS structural preflight was run against the frozen PDF. It returned
`UNAVAILABLE`, because pypdf is not installed. Its exact JSON is preserved
in `qa/PDF_PREFLIGHT.json`. This is not relabelled PASS. The successful
Poppler parse, four observed render images and byte-identical source build
are separate evidence, not a substitute result for that tool. Findings use
source section/equation anchors; image filenames identify the visual audit.

Generated logs and images are in `qa/`, with a separate non-self manifest.
These review checks do not replace the root's terminal two-cold-build QA.
