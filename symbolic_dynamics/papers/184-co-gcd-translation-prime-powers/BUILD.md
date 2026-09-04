# Build record — P184 immutable rounds

Status: `ROUND2_DUAL_REVIEW_FREEZE / HOLD_EXTERNAL`.

Build date: 2026-09-03 UTC.  The deterministic build was:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The last two LaTeX passes produced byte-identical PDFs.  Mechanical receipts:

- `main.tex` SHA-256:
  `6f11630dfbb68ff3ac30e652130497b3c473a45869c968fb0679136ba2b8b44a`;
- `references.bib` SHA-256:
  `3c1b98b55d0e6a6215f88e3182173254974b158ba34a0f744be3bf0c12769b66`;
- live and preserved PDF SHA-256:
  `991e9eae521268083d5eabb02d5ff536a40eefe000aa970ce23d6c97ea8888ab`;
- `main.pdf` and `main_round0_original.pdf` are byte-identical;
- 4 A4 pages, 353576 bytes, PDF 1.5;
- 25/25 fonts embedded, subsetted, and Unicode mapped;
- blank Title, Author, Subject, Keywords, Creator, and Producer fields; no
  metadata stream, JavaScript, encryption, forms, or embedded files;
- zero LaTeX warnings, bad boxes, undefined references/citations, or errors in
  the final log;
- four rasterized pages were inspected at full-page and enlarged detail: no
  clipping, overlap, corruption, or unintended blank page was found.

The exact author control was run twice freshly:

```bash
python3 code/verify_p184.py
python3 code/verify_p184.py
```

Both transcripts are byte-identical to `code/CANONICAL.txt`.  The verifier
reports 109,478 assertions and `RESULT=PASS`; its SHA-256 is
`7636127ed7eb4693aa5adb1dd7d68406b21d776299da7b7a64b71b866dbbe653`,
and the canonical transcript SHA-256 is
`616f48c16bc1d335c658bcfded8b0b004b5dafdec79b77cb17a333ce3067acda`.
These computations are author-side regression controls, not independent
review or novelty evidence.

This section preserves the Round-0 build receipt.  Review A and Review B
closed with zero findings, so Round 1 and Round 2 are deliberate
byte-identical receipts.  Two source-only cold builds reproduce the final
PDF; `IMPROVEMENT_LOG.md` and `FINAL_QA.md` bind the terminal evidence.
