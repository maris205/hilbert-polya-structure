# Final QA — P127

Status: **PASS / GO_INTERNAL / HOLD_EXTERNAL**.

- Independent Review A's two major proof/owner conditions and visible
  typesetting defect were repaired in round one.  Independent Review B
  returned **CRITICAL 0 / MAJOR 0 / MINOR 0**; the consolidated verdict is
  `GO_INTERNAL / HOLD_EXTERNAL`.
- Fresh canonical verifier: **PASS, 1,271,047 assertions**.  Fresh stdout is
  byte-identical to `code/verification_output.txt`; each is 738 bytes with
  SHA-256
  `53ec418b88941cad406b24cca6837818a36e69ed3ebb0194219b4c09fbea67b1`.
  The verifier SHA-256 is
  `58ea6c04eb35a43d1805128584a2c4c61f34e237dbccf6ab32bfd793a17692f8`.
- Fresh isolated build: **PASS** for
  `pdflatex -> bibtex -> pdflatex -> pdflatex`.  It copied only `main.tex`
  and `references.bib`, reproduced the frozen PDF byte for byte, and its
  settled log/BLG contain no error, warning, undefined citation/reference,
  bad box, or actionable rerun request.  Bibliography closure is **7/7**.
- `main.pdf`, `main_round1.pdf`, and `main_round2.pdf` are byte-identical:
  **3 A4 pages, 328,070 bytes**, SHA-256
  `107d6baa4063d747799f26710bc1de0bc0eb8a7460509e9d8beafe570f760f0d`.
  The immutable round-zero PDF is distinct and preserved at SHA-256
  `9ba5ea88ead104331d4bfbde46479e1ad17fb23553c593595b116406d40cb8bf`.
- `pdfinfo` reports blank Title, Author, Subject, and Keywords; A4 page size,
  rotation 0, no metadata stream, form, JavaScript, or encryption.  All
  **26/26** font rows are embedded, subsetted, and Unicode-mapped.
- Both independent reviews raster-inspected all three pages.  The final
  isolated build is byte-identical to that reviewed artifact, so the visual
  evidence transfers without qualification: no clipping, collision, blank
  page, malformed display, missing glyph, or orphan heading.
- Fresh extracted-text scans contain no `??`, `[VERIFY]`, internal-draft
  marker, or undefined-reference sentinel.  The factor-product route,
  codomain-wide fibre trichotomy, `n=1` guard, owner subtraction, and
  P102/P103/P125 firewall remain within the reviewed claim ceiling.
- Novelty, priority, authorship, posting, submission, specialist contact,
  and every external-release action remain **HOLD**.

The accompanying `SHA256SUMS` covers the source, bibliography, verifier and
canonical output, all round PDFs, both independent reviews and their
consolidation, the support documents, and this final-QA record.  The
manifest excludes itself and transient LaTeX auxiliaries.
