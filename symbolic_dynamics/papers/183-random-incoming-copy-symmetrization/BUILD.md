# Build record — P183 immutable rounds

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
  `9ee13796fc2a69fd9d064c55d0adf1e9fad26d3811e29f767e38d548908e6678`;
- `references.bib` SHA-256:
  `5b5f0fe2b7e78176d097ab2e919d35954adffff824528b999847be791038912d`;
- live and preserved PDF SHA-256:
  `6834170a0ee554a9f4c75040aad762326e24fa5a532e7987c57025be02bd235b`;
- `main.pdf` and `main_round0_original.pdf` are byte-identical;
- 4 A4 pages, 377864 bytes, PDF 1.5;
- 27/27 fonts embedded, subsetted, and Unicode mapped;
- blank Title, Author, Subject, Keywords, Creator, and Producer fields; no
  metadata stream, JavaScript, encryption, forms, or embedded files;
- zero LaTeX warnings, bad boxes, undefined references/citations, or errors in
  the final log;
- four rasterized pages were inspected at full-page and enlarged detail: no
  clipping, overlap, corruption, or unintended blank page was found.

The exact author control was run twice freshly:

```bash
python3 code/verify_p183.py
python3 code/verify_p183.py
```

Both transcripts are byte-identical to `code/CANONICAL.txt`.  The verifier
reports 47,033 assertions and `RESULT=PASS`; its SHA-256 is
`a7c56aa48783eae09e44a7df39f34109a891d33ac6a11e9b86e4fd22cdfdd472`,
and the canonical transcript SHA-256 is
`f21652d061f409a0833be4900d6cbafee6a034b3121a03750984073893c2dea1`.
These computations are author-side regression controls, not independent
review or novelty evidence.

This section preserves the Round-0 build receipt.  Review A and Review B
closed with zero findings, so Round 1 and Round 2 are deliberate
byte-identical receipts.  Two source-only cold builds reproduce the final
PDF; `IMPROVEMENT_LOG.md` and `FINAL_QA.md` bind the terminal evidence.
