# Build protocol — P132

From this directory:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Final QA must repeat the four stages in an isolated temporary directory
containing only `main.tex` and `references.bib`; rerun the exact-control byte
comparison; inspect settled LaTeX/BibTeX logs, bibliography closure, every PDF
page, embedded fonts, extractable text, page size, and anonymous metadata.

External status remains `HOLD_EXTERNAL` regardless of mechanical build status.

## Round-1 result

Completed on 2026-08-31 UTC after implementing every Review-A item.

- The fresh paper-local verifier replay matched
  `code/verification_output.txt` byte for byte (`cmp=0`).
- The required four-stage build, repeated in the isolated directory
  `/tmp/p132r1iso.qzm8OP`, produced a byte-identical PDF and a settled log with
  no error, undefined citation/reference, box warning, or rerun request.
- `main.tex` has SHA-256
  `a26bee914dd2909c825a7c1d3e2a012c09b2def816b14db85ab27c40b60bddaf`.
- `main.pdf` and `main_round1.pdf` are byte-identical three-page A4 files of
  326,101 bytes with SHA-256
  `dcfd7eddb0cb85a197f0ae875af97fd353f50070317ca4ec6f8de0ad5a74527e`.
- All 25 reported font rows are embedded, subsetted, and Unicode-capable;
  identifying metadata is blank.  The repaired abstract, fixed-language
  display, and constant-fibre display are visually clean.
- The immutable round-zero artifact remains unchanged with SHA-256
  `f6329905059f20811380dcfe1163d9cd908a592e428a358ec1f9461d55140679`.

The round-one artifact remains anonymous and `HOLD_EXTERNAL`.
