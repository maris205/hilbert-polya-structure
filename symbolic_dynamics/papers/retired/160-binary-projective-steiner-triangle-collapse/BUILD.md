# Build record — P160 Round 0

## Commands

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p160.py > verification_output.txt
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Frozen Round-0 artifacts

- `main.pdf` and `main_round0_original.pdf`: byte-identical, 4 A4 pages,
  355,500 bytes, SHA-256
  `a988139ec5b9cd600ced9f7eeffdeb42e5b8f8268c1161670661cdc3d0cc84b5`.
- `verification_output.txt`: 4,836,144 assertions, PASS, SHA-256
  `38b12108ba9440d2acfc2c0f0abde61f7d1daaf18f7c705f9eefd0ca6071efec`.
- `verify_p160.py`: SHA-256
  `e7066b7d3fb96d7905835675793d664a53ec2ce3aec2ffaaaf5d527f3e60cb46`.

Two directories containing only `main.tex` and `references.bib` were built
independently with the same four commands.  Both PDFs were byte-identical to
the frozen Round-0 PDF.  The final LaTeX and BibTeX logs contain no unresolved
citation/reference, box, rerun, or bibliography warning.

Round 0 is historical input to later hostile review.  It must not be silently
overwritten after formal Review A opens.
