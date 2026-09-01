# Build and freeze record — P151

**Status:** **ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL**

## Round 0

- Engine: pdfTeX 1.40.22 / LaTeX2e 2021-11-15.
- Sequence: `pdflatex -> bibtex -> pdflatex -> pdflatex`.
- Result: success, 6 A4 pages, 351,991 bytes.
- Frozen file: `main_round0_original.pdf`.
- SHA-256:
  `64ea74c13f5fedcd4d4280426224723a2b290f16ff6d53ceb860163b456215af`.
- Purpose: preserve the first successful draft before self-QA.  It retains
  the visible plain-text `qquad` typo in the endpoint/mean display and the
  single 23 pt overfull killed-path line documented by the QA pass.

## Pre-hostile proof/self-QA build

- Result: success, 6 A4 pages, 351,762 bytes.
- SHA-256:
  `456480f4472e8b33f9ce4525b71d33af5a78cacd407cd4ca976a3dcbe5b17af7`.
- Repair: restored the missing backslash in `\qquad`, split the long
  killed-path solution into displays, and made the ownership-table columns
  ragged-right for readable source names.
- Bibliography: 5/5 verified primary records printed; every entry is cited.
- Cross-references/citations: resolved; no undefined or rerun warnings.
- Bad boxes: none in the settled log.
- PDF: version 1.5, unencrypted; title, author, subject, and keyword metadata
  blank; all reported font rows embedded, subsetted, and Unicode mapped.
- Reproducibility: volatile PDF date/trailer information is suppressed.  A
  consecutive clean pdfTeX pass preserved the current PDF byte for byte at
  the hash above.
- Visual QA: all 6 pages rasterized and inspected.  The repaired equation (6),
  ownership table, theorem, exact-audit table, declarations, and bibliography
  are legible and within page bounds.
- Exact control: cold replay matched `verification_output.txt` byte for byte;
  1,446,432 exact integer/rational assertions passed.
- External status: `HOLD_EXTERNAL`.

## Hostile-review-A repair build

- Files: `main.pdf` and `main_round1.pdf` are byte-identical.
- Result: success, 6 A4 pages, 356,664 bytes.
- SHA-256:
  `24fddbfb896510cf2712a8ade2a3ac37d04712676f635e39f1170c4cc334e8d9`.
- The original Round-0 PDF remains unchanged at the hash above.
- Repair: added the Sericola generic time/place owner and Chen general-tree
  PGF neighbour, narrowed the residual to the explicit unequal-spider
  continuant factorization and scalar variance, upgraded the
  de la Iglesia--Juarez citation to its 2023 version of record, replaced the
  overstated independent-moment wording, and added the `z=1` regularity
  bridge.
- Bibliography: 7/7 verified primary records printed; every entry is cited.
- Settled log: no unresolved citation/reference, rerun request, or bad box.
- External status stays `HOLD_EXTERNAL`.

## Independent Review-B build and visual gate

- Cold replay matched `verification_output.txt` byte for byte; all 1,446,432
  exact integer/rational assertions passed.
- Two isolated clean
  `pdflatex -> bibtex -> pdflatex -> pdflatex` builds were mutually
  byte-identical and byte-identical to the current package PDF at
  `24fddbfb896510cf2712a8ade2a3ac37d04712676f635e39f1170c4cc334e8d9`.
- All six current pages were rasterized and inspected at original detail.  The
  ownership table, theorem, continuant/renewal displays, repaired
  `Q(0)/Q(1)/D(1)` bridge, audit table, declarations, and seven references are
  legible and within bounds.  No overlap, clipping, blank page, corrupt glyph,
  unresolved marker, or identifying metadata was found.
- Hostile Review A (0 Critical / 1 Major / 3 Minor) is fully closed; Hostile
  Review B returned ACCEPT (0 / 0 / 0).

## Final archival freeze

Root froze `main_round2.pdf` as a read-only, byte-identical copy of the
accepted current `main.pdf`: 6 A4 pages, 356,664 bytes, SHA-256
`24fddbfb896510cf2712a8ade2a3ac37d04712676f635e39f1170c4cc334e8d9`.
The final paper-local `SHA256SUMS` manifest was regenerated after closure and
passes in full.  This archival step does not change the accepted review
status.
