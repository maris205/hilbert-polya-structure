# Final QA — P129

Status: **PASS / GO_INTERNAL / HOLD_EXTERNAL**.

- Independent Review A required the stopped-walk cancellation, three direct
  owner subtractions, finite-clock/strong-Markov detail, the indirect-merger
  label invariant, the predictable compensator, and exact support-range
  wording to be made explicit.  Round one closes every item.  Independent
  Review B returned **CRITICAL 0 / MAJOR 0 / BLOCKING MINOR 0**, and passed
  10,972 additional exact reviewer assertions; the consolidated verdict is
  `GO_INTERNAL / HOLD_EXTERNAL`.
- Fresh canonical verifier: **PASS, 506,663 assertions**.  Fresh stdout is
  byte-identical to `code/verification_output.txt`; each is 477 bytes with
  SHA-256
  `3e40359274ae4bb033db5efe16d463b28af3fcd7464f9589bc5b136626acd080`.
  The verifier SHA-256 is
  `fe79e8e3dfa1d15b16d04138d39ef653ac45bbd6addea50d3b53adf34f5aa272`.
- Fresh isolated build: **PASS** for
  `pdflatex -> bibtex -> pdflatex -> pdflatex`.  It copied only the modular
  source, command file, and bibliography, reproduced the frozen PDF byte for
  byte, and its settled log/BLG contain no error, warning, undefined
  citation/reference, bad box, or actionable rerun request.  Bibliography
  closure is **8/8**.
- `main.pdf`, `main_round1.pdf`, and `main_round2.pdf` are byte-identical:
  **6 A4 pages, 342,879 bytes**, SHA-256
  `5c64a88c1d003fd2729dd032eb229f9073975753040082919d0fc056d1c439f2`.
  The immutable round-zero PDF is distinct and preserved at SHA-256
  `404b21a8beb9f9691326262544fc797cd1b62bf69b36ad2b5b65f693495dc05d`.
- `pdfinfo` reports blank Title, Author, Subject, and Keywords; A4 page size,
  rotation 0, no metadata stream, form, JavaScript, or encryption.
  `pdfdetach` reports zero embedded files.  All **25/25** font rows are
  embedded, subsetted, and Unicode-mapped.
- Both independent reviews raster-inspected all six pages.  The final
  isolated build is byte-identical to that reviewed artifact, so the visual
  evidence transfers without qualification: no clipping, collision,
  malformed formula, missing glyph, blank page, or orphan heading.
- Fresh extracted-text scans contain no `??`, `[VERIFY]`, internal-draft
  marker, or undefined-reference sentinel.  The PDF's sole `PILOT_ONLY`
  occurrence is the explicit scope exclusion; the unproved maximum-endpoint
  formula remains only in the verifier under `MANUSCRIPT_CLAIM=NO` and does
  not leak into the theorem contract.
- The reported 16,383 and 2,047 control counts remain explicitly cumulative
  `(ambient n, mask)` instances.  Assiotis, Hitczenko--Wesołowski, and
  Sniady--Urban mechanisms, generic coalescing/ballot machinery, and the
  P114/P117/P121/P126 silhouettes remain zero credit.
- Novelty, priority, authorship, posting, submission, specialist contact,
  and every external-release action remain **HOLD**.

The accompanying `SHA256SUMS` covers the modular source, bibliography,
verifier and canonical output, all round PDFs, both independent reviews and
their consolidation, the support documents, and this final-QA record.  The
manifest excludes itself and transient LaTeX auxiliaries.
