# Build Record

Status: final post-cross-hostile four-stage build passed, 29 August 2026.

Build command, run from this directory:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Toolchain

```text
Python 3.12.3
pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)
BibTeX 0.99d (TeX Live 2022/dev/Debian)
```

All four build stages exited zero. The final `main.log`/`main.blg` scan has
no `Warning`, `Overfull`, `Underfull`, `undefined`, `multiply defined`, or
`Error` match.

## Artifact

```text
pages=5
page_size=A4 (595.276 x 841.89 pt)
pdf_version=1.5
bytes=305010
sha256=1b2d99cd2b40733faa5565ed7114fd9e405cfb0811f4152828c0e7e6600c4316
```

All fonts reported by `pdffonts main.pdf` are embedded and subsetted, with
Unicode maps. `pdftotext -layout` recovered the title, abstract, every
displayed theorem/proof, all three references, and the HOLD statement.
The extracted layout text is 19,439 bytes, and `pdffonts` reports 22 font
entries, all embedded and subsetted.
Deterministic PDF settings suppress volatile creation metadata and trailer
identifiers.
