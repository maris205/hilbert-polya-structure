# Final QA — P128

Status: **PASS / GO_INTERNAL / HOLD_EXTERNAL**.

- Independent Review A found no major defect and required three minor
  repairs: fixed-cut trace uniqueness, literal transfer-matrix construction
  in the verifier, and formal-Euler-product terminology.  Round one closes
  all three.  Independent Review B returned **CRITICAL 0 / MAJOR 0 / MINOR
  0**; the consolidated verdict is `GO_INTERNAL / HOLD_EXTERNAL`.
- Fresh canonical verifier: **PASS, 180,453 assertions**.  Fresh stdout is
  byte-identical to `code/verification_output.txt`; each is 1,712 bytes with
  SHA-256
  `3b5e5bbbe94ec7ed7e689ff6a2cfeb2dc04a1ebc1ce9686c44194518ac1b1204`.
  The verifier SHA-256 is
  `1b58fb8f71ac74082fb0ed9131a555a2ed4b7716da035e731ee9e5da0ac4a2fe`.
- Fresh isolated build: **PASS** for
  `pdflatex -> bibtex -> pdflatex -> pdflatex`.  It copied only `main.tex`
  and `references.bib`, reproduced the frozen PDF byte for byte, and its
  settled log/BLG contain no error, warning, undefined citation/reference,
  bad box, or actionable rerun request.  Bibliography closure is **6/6**.
- `main.pdf`, `main_round1.pdf`, and `main_round2.pdf` are byte-identical:
  **4 A4 pages, 386,639 bytes**, SHA-256
  `f49d7c850e6c607130b96ff80f409ac642bae21ecae80203857262f831677439`.
  The immutable round-zero PDF is distinct and preserved at SHA-256
  `e2c063e17ce35249978a5729d27194c9223a893865b62ef11ce8f90c2435d667`.
- `pdfinfo` reports blank Title, Author, Subject, and Keywords; A4 page size,
  rotation 0, no metadata stream, form, JavaScript, or encryption.
  `pdfdetach` reports zero embedded files.  All **28/28** font rows are
  embedded, subsetted, and Unicode-mapped.
- Both independent reviews raster-inspected all four pages.  The final
  isolated build is byte-identical to that reviewed artifact, so the visual
  evidence transfers without qualification: no clipping, collision,
  malformed formula, bad break, missing glyph, or orphan reference page.
- Fresh extracted-text scans contain no `??`, `[VERIFY]`, internal-draft
  marker, or undefined-reference sentinel.  The all-depth formal orbit Euler
  product and target-refined unit-fibre claims remain inside the reviewed
  ceiling; the old window/clock/fixed/depth theory, Garefalakis--Reis input,
  and P110 order-dual mechanism remain zero credit.
- Novelty, priority, authorship, posting, submission, specialist contact,
  and every external-release action remain **HOLD**.

The accompanying `SHA256SUMS` covers the source, bibliography, verifier and
canonical output, all round PDFs, both independent reviews and their
consolidation, the support documents, and this final-QA record.  The
manifest excludes itself and transient LaTeX auxiliaries.
