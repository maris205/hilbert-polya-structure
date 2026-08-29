# Build record — P107

Status: **final mechanical QA passed for internal use / external HOLD**.

Final replay date: 2026-08-29 UTC.  Run from this directory:

```bash
python3 code/verify_annihilator_power.py > /tmp/p107-finalqa-verifier.txt
cmp -s /tmp/p107-finalqa-verifier.txt code/verification_output.txt
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The canonical verifier stdout was byte-identical to the stored output and
reported `212843` assertions.  Its SHA-256 is
`0ad8903f24d032b94daaf4d2cb77295ee9e14cd2c50a0ed9705dd17b4fce2fd3`.

The required four-stage build exited zero.  Repeating the complete four-stage
sequence produced the same PDF SHA-256 both times:
`76ea9249f290657d83d7ceeed2ba2ddad12d95b7c6b2f4f2142ff417f46b6c39`.

Final artifact metrics:

- 4 A4 pages, 271,211 bytes, PDF 1.5;
- empty author metadata, no encryption, forms, JavaScript, or rotation;
- zero actual warnings, undefined citations/references, multiply defined
  labels, overfull/underfull boxes, fatal errors, or rerun requests;
- all 23 font entries embedded, subsetted, and Unicode mapped;
- searchable text: 10,208 bytes in plain extraction and 13,646 bytes in
  layout-preserving extraction;
- 5/5 bibliography keys cited, with no uncited or unresolved key;
- all four pages rendered at 150 dpi and visually passed.

See `FINAL_QA.md` for the complete gate and `SHA256SUMS` for the frozen
artifact manifest.  No external posting, submission, contact, novelty, or
priority action is authorized.
