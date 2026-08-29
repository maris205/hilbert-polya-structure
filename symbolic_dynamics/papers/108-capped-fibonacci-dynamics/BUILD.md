# Build record — P108

Status: **final mechanical QA passed for internal use / external HOLD**.

Final replay date: 2026-08-29 UTC.  Run from this directory:

```bash
python3 code/verify_capped_fibonacci.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Final frozen replay

The canonical verifier passed **67,475,970 exact assertions**, and its
fresh stdout was byte-identical to `code/verification_output.txt`.  Both
files have SHA-256
`ca2e3c6f0bb312544ec08921416fb39eb2293e2d547e67bca2ae383e802aa48c`.
The four-stage LaTeX/BibTeX sequence exited zero.  Repeating the complete
sequence reproduced the same final PDF hash:

    pages=3
    page_size=A4 (595.276 x 841.89 pt)
    pdf_version=1.5
    bytes=269786
    sha256=610f893fc1bfb6d393777e90f048eefcfa7780789ee9d5b6ddd7d0cd38446c23

The final `main.log`/`main.blg` scan has zero actual warnings, undefined
citations/references, overfull or underfull boxes, multiply defined labels,
fatal errors, or rerun requests.  `pdfinfo` reports an empty author field and
no encryption, forms, JavaScript, or rotation.  Plain `pdftotext` recovered
8,291 bytes in 212 lines; layout-preserving extraction recovered 10,420
bytes in 152 lines, with no unresolved sentinel.  All 4/4 bibliography keys
are cited.  `pdffonts` reports 21 entries, all embedded, subsetted, and
Unicode-mapped.  All three pages were rendered at 150 dpi and visually
inspected without clipping, overlap, broken references, malformed displays,
or illegible bibliography text.

See `HOSTILE_REVIEW.md` for the consolidated A/B decision, `FINAL_QA.md` for
the complete mechanical gate, and `SHA256SUMS` for the frozen evidence
manifest.  External release remains **HOLD**.
