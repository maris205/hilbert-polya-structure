# P199 Review A — source-only build and page inspection

2026-09-05 UTC. Input: frozen Round0 main.tex and references.bib only.
Neither author auxiliary files nor a previously compiled bibliography was
copied to the new directory `/tmp/p199-review-a.4kMTHt`.

Commands in that directory:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All four commands exited zero. Final main.log contains no Warning,
Overfull, Underfull, undefined, or multiply-defined matches. Initial
undefined citations before the BibTeX/pass sequence are expected and
are not hidden; all pass logs and final bibliography are preserved in qa/.
This is a real physical reviewer cold build, not a replay of an author
build log. It does not substitute for the terminal two-build requirement.

Cold PDF and frozen Round0 PDF are byte-identical:
`b6ba18a10e83281c1dd491b47cf5d8513ab9914933c659411c8d5c24b72478a0`.
Poppler reports four A4 pages, 320,789 bytes, PDF 1.5, no encryption,
JavaScript, form, or metadata stream. All 24 displayed font entries are
embedded and subsetted, with Unicode maps. Author/title/subject/keywords,
creator and producer metadata fields are empty. Anonymous visible author
and running heads contain no identifying personal information.

The ARS pdf_read_preflight script was actually invoked on the frozen
PDF. It returned **UNAVAILABLE** because pypdf is not installed. Its
unmodified generated JSON is preserved in qa/pdf_preflight.json. This
is not recorded as structural preflight PASS. Independent Poppler
metadata, raster rendering, and byte identity are separate evidence.

`pdftoppm -r 125 -png` rendered the cold PDF; all four images were
individually opened by this reviewer and are preserved in qa/.

| Page | Actual inspection |
|---|---|
| 1 | Anonymous title/abstract, definitions, exact owner factor and start of clock theorem legible; long formulas inside margins; no clipping or citation placeholders |
| 2 | Clock proof, depth-CDF product, inverse theorem and boundary cases legible; displayed denominators/exponents unambiguous; no collision with footer |
| 3 | Inverse/image proofs, root-gap derivative and finite table fit; HOLD_EXTERNAL and missing P51–P56 caveat visible; no table truncation |
| 4 | All three references resolved, DOI/URL line breaks legible and no overflow; mostly white remainder is acceptable for this four-page short note |

Theorem/proof page breaks leave full statements readable; no missing
figure is implied by this text-and-table note. No visual repair required.
