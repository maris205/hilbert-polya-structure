# Build record — P173

The anonymous manuscript uses deterministic PDF settings and the standard
four-command BibTeX build recorded in `README.md`.  Round-0 build logs are
stored as `build_pdflatex_1.log`, `build_bibtex.log`,
`build_pdflatex_2.log`, and `build_pdflatex_3.log`.

Final dual-review, cold-build, replay, font, metadata, and byte-comparison
evidence is recorded below.

## Hostile Review A repair build

The repaired author verifier now includes the `n=0` Jordan sentinel and
passes 13,307 exact assertions; a fresh process is byte-identical to
`verification_output.txt` (SHA-256
`b32f20b843b22d719633620971f12cdc67a1e3ca02003aff41ea3b15261421d0`).
The four-command Round-1 settling build has zero warning, bad box, unresolved
citation/reference, rerun request, or fatal error.  The result is four A4
pages, 304,997 bytes, SHA-256
`1a66075c7d64ae943cbbd42503b81964ea7fabe85e2ee7515001a052aa5cce22`;
`main.pdf` and `main_round1.pdf` are byte-identical, while the original
three-page Round-0 PDF remains preserved.

Review A's read-only delta audit closed both Major and both Minor findings;
author and reviewer transcripts replay byte-identically.  Review B's source,
reciprocal-collision, and null-event-proof repairs define the Round-2 source;
the four-command settling build has no warning, bad box, unresolved citation
or reference, rerun request, or fatal error.  `main.pdf` and
`main_round2.pdf` are byte-identical: 4 A4 pages, 333,340 bytes, SHA-256
`01235b8279d922b0d120f869f32ef8be1ee6aea105dafbc5ea25155be1ef039c`.
Reviewer B's subsequent read-only delta accepted both Major repairs and the
Minor repair, leaving zero open findings.  External status remains
`HOLD_EXTERNAL`.

## Final source-only cold builds

Two distinct `mktemp` directories were created.  Before compilation, each
contained exactly `main.tex` and `references.bib`.  Each ran the documented
sequence `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`; stdout is preserved in
the eight `final_cold_a_*` and `final_cold_b_*` logs.  The final logs contain
no warning, bad box, unresolved citation/reference, rerun request, or fatal
error.  The expected first-pass citation messages settle normally.

Both fresh PDFs, `main.pdf`, and `main_round2.pdf` are byte-identical:

```text
pages:   4 A4
bytes:   333340
sha256:  01235b8279d922b0d120f869f32ef8be1ee6aea105dafbc5ea25155be1ef039c
```

## Final exact-certificate replay

Fresh stdout was preserved in `final_replay_author.txt`,
`final_replay_review_a.txt`, and `final_replay_review_b.txt`.  The files match
the author, Review-A, and Review-B canonical transcripts byte for byte and
report 13,307, 36,390, and 9,995,101 assertions, respectively.

## Final PDF and integrity QA

`pdfinfo` reports four A4 pages, 333,340 bytes, no encryption, and blank
title, author, subject, keywords, creator, and producer fields.  All 24 fonts
reported by `pdffonts` are embedded, subsetted, and Unicode-mapped.  Raster
inspection of all four pages found no clipping or malformed display; the
anonymous author is visible, and `HOLD_EXTERNAL` is text-visible on pages 1
and 4.  Extracted text has no `??`, `[?]`, or `[VERIFY]` marker.
The four files in `qa_final/` are byte-identical to a fresh 110-dpi Poppler
render of the locked PDF.

The complete paper-local `SHA256SUMS` lists every regular file except itself,
53 entries in total, and verifies with `sha256sum -c SHA256SUMS`.

Final disposition:

```text
DUAL_REVIEW_CLOSED / SPIKE_2_COLLISION_RISK / HOLD_EXTERNAL
```
