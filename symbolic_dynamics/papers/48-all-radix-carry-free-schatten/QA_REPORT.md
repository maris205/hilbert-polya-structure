# Paper 48 Writer-Candidate QA Report

Date: 2026-08-18 UTC.

This is a writer-side mechanical, protected-state, and scientific-consistency
report.  It is not an independent writer audit and does not claim CLEAN.

## Manuscript artifact

- PDF: paper/CarryFreeRadixOperators.pdf
- SHA-256: 5bb755f9b2b0eaf56c79b8de5e94253bc9e7ed4b8d6ef9fd4c815f832cf54573
- Format: A4, 16 pages, anonymous metadata
- Build epoch: 1787011200
- Build sequence: pdflatex, bibtex, pdflatex, pdflatex
- The predecessor with SHA-256
  `daaf6435625c6f1206f3e1faaec090619f2bc2750be5e1b4ca2cf748c0063867`
  is withdrawn and is not the candidate for recheck.
- Fresh lanes A and B each regenerated every data-driven asset and rebuilt
  the paper from source.  Their PDFs, the named PDF, and the in-place PDF
  are byte-identical at the SHA-256 above.

## Compilation and rendering checks

- Final build completed with no LaTeX warning, undefined reference,
  unresolved citation, overfull box, or underfull box.
- All 33 font rows reported by pdffonts are embedded, subset, and have
  ToUnicode maps.
- Poppler default, layout, and raw extraction with `-nopgbrk` each contain
  zero illegal XML C0 controls, DEL characters, C1 controls, or U+FFFD.
  PyMuPDF text extraction has the same all-zero result.  No post-extraction
  sanitization was used.
- The raw Poppler bbox XHTML contains no illegal XML byte and parses
  directly as XML.  Both Poppler and PyMuPDF extractions also contain zero
  Private Use Area characters.
- Every page has extractable text.  Counting Unicode code points for which
  Python `str.isspace()` is false in the PyMuPDF page text gives the exact
  minimum on page 7: 1,180 characters.  The earlier statement “greater than
  1,200 characters” was based on a byte count and is withdrawn.  All 16
  per-page Unicode counts are recorded in
  `evidence/PDF_QA.json`.
- The PDF has no encryption, JavaScript, rotation, or unexpected page size.
- Sixteen rendered page previews were visually checked, including the
  data-driven phase plot, both TikZ diagrams, tables, appendices, and
  bibliography.
- Fresh fixed-epoch lanes A and B reproduce the same PDF and generated-asset
  bytes.  The retained lane workspaces are candidate-only replay material and
  are deliberately excluded from the minimal writer overlay.

## Pre-closure source corrections

- Explicit glyph-to-Unicode maps are loaded, and explicit stretchy sizing
  was removed at every delimiter site that produced extension-font control
  characters.  The mathematical expressions are unchanged.
- Lucas's DOI `10.24033/bsmf.127` is recorded with the official volume 6 in
  both `references.bib` and `evidence/SOURCE_VERIFICATION.md`; page 16 of
  the PDF displays `6:49--54`.
- Section 6 now defines the frozen one-sided edge shift on
  \(\mathbb N_0\), not a bilateral shift on \(\mathbb Z\).  Its periodic-word
  interpretation and proof wording are explicitly one-sided, with no scope
  expansion.

## Data and figure checks

- Canonical extraction: PASS, 1,965 rows per lane, 8,010 digit interval
  comparisons, and 420 shell envelopes.
- Canonical summary SHA-256:
  f3105dfe1733bcd8aa240d9ebcf9125acc44704a96d7c5682fbf991381548b3d.
- Results-ledger SHA-256:
  dd1fbc2ee0fb16bf4df7ff74cbc2dc59fa00e02e18d545f3b782c1ee4f55fc62.
- Re-running the extractor and asset generator left the canonical summary,
  ledger, plot PDF/PNG, and both LaTeX tables byte-identical.
- The asset generator rechecks the finite-proof firewall before emitting
  files.

## Independent finite replay

The frozen independent auditor passed in all four final invocations:

- State A, normal environment: PASS.
- State A, adversarial import path: PASS.
- State B, normal environment: PASS.
- State B, adversarial import path: PASS.

Each replay checked 3,930 science rows, 3,930 exact GF(2) ranks, 1,152 mask
rows per lane, and 12 trace-prefix instances.

## Frozen-input checks

- Integration inventory-file SHA-256:
  730219e484db08ca78284ad3dd4d95e611ce2c6562e40f0311697ef27f7d37c7.
- Full re-audit inventory-file SHA-256:
  834dc909438488e2bb3059fa90a6e66e1ada142681eb8a5fe10ed33d4005ff0c.
- Frozen-copy inventory-file SHA-256:
  cb4a5603e72baed2b1e1a3e9ec992bb391d09fd005d86cbe41a01b262f76e089.
- Dry-run checksum-and-metadata comparisons against the original integration
  candidate, State-A outputs, State-B outputs, and independent auditor were
  empty: the frozen copies remain exact.

## Live protected State-A replay

- Two canonical captures of the live protected root are byte-identical.
- `PROTECTED_STATEA_TREE.tsv` covers exactly 75 nodes: 57 regular files and
  18 directories, including the root.
- The protected manifest SHA-256 is
  `2c45b1c5cf683855b1a7b798edb719e9ab117d3223aa1d5cf4678efb12f16191`.
- The sealed Stage-0 part is exactly 59 nodes (44 files, 15 directories), and
  the declared `outputs/` part is exactly 16 nodes (13 files, 3 directories).
- The live State-A tree reconstructs to
  `c23b59034303af74f2a9433b92f9f5c1e1cce4510bd8032ef1214372390bda58`.
- The externally supplied post-output verdict is bound by its exact raw hash
  `6f69cddfd069d267e5a71f8ec342df71c31d456152a8ba910d93829daadcb5f9`.
- The independent writer-side replay record is
  `evidence/PROTECTED_STATEA_REPLAY.json`, SHA-256
  `d3db2a0579a96606da778c86f217849f2931b456f9e1e3556c307bd946c4d36c`.

These are byte, metadata, provenance, and finite-output checks.  They do not
prove any infinite theorem and do not turn the external verdict into a
writer-side CLEAN claim.

## Independent reviews

- Formal plan review: initial HOLD 7/10, followed by PLAN_READY 9/10 after
  all three major plan issues were repaired.
- Paper review round 1: Revise, 8.8/10, no mathematical correctness defect;
  one submission-readiness issue and three prose issues were repaired.
- Paper review round 2: ACCEPT, 9.4/10, with no critical, major, minor, or
  required action.
- That accepted review predates the pre-closure corrections above.  A
  writer-side nonregression audit and exact PDF/source anchors are recorded
  in `reviews/MANUSCRIPT_PRECLOSURE_NONREGRESSION.md`.  No independent-review
  disposition is silently transferred to the repaired PDF.

## Evidence-boundary check

The repaired candidate paper:

- proves infinite ideal statements analytically;
- labels finite lanes, mutations, and audit records as validation only;
- keeps the active/hidden wall distinction;
- treats phase removal as two-sided unitary equivalence;
- restricts ordinary trace and determinant to the trace-class domain;
- restricts the determinant logarithm to a neighborhood of zero;
- deletes the zero word before trace and period interpretation; and
- makes no priority, exhaustive-search, completed-function, or target-divisor
  claim.

## Gate

The earlier `WAIT_PROTECTED_AUTHORITY` state is retired: the exact live
protected manifest has now been injected and independently replayed.  The
controlling status is `HOLD_FOR_INDEPENDENT_WRITER_AUDIT`.  Mechanical QA and
writer-side closure are complete, but this report does not claim CLEAN,
installation, publication, or authority-write permission.
