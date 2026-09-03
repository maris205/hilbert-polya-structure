# P175 build record

**Artifact:** anonymous AMS short note, author Round 0  
**Settled date:** 2026-09-03 UTC  
**External state:** `HOLD_EXTERNAL`

## Toolchain

- pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)
- BibTeX 0.99d (TeX Live 2022/dev/Debian)
- Python 3.12.3
- Poppler `pdfinfo` / `pdffonts` 22.02.0

## Reproduce the verifier

```sh
python3 verify_p175.py
```

Two fresh executions were compared byte for byte before the canonical
transcript was frozen.  Both returned `RESULT=PASS` with:

- assertions: `2111465`;
- literal-edge digest:
  `c0747bd57b5c2399e853de789e2d6f49b55b9b0663dc294486ea03f1855e9be5`;
- canonical transcript SHA256:
  `f9169bb2d6ccfb304dee28409c3ed07e86ba597cc1862524bcc7f29d5a34eb25`.

The program uses only the Python standard library and imports no scouting or
historical verification code.

## Reproduce the PDF

From this directory, run:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The settled command transcripts are `build_pdflatex_1.log`,
`build_bibtex.log`, `build_pdflatex_2.log`, and `build_pdflatex_3.log`.

## Frozen author Round-0 artifact checks

- Round-0 source-built PDF, preserved as `main_round0_original.pdf`: 3 pages,
  A4, 323477 bytes.
- Round-0 PDF SHA256:
  `32f296a1519fd598f0ef4c88bdbd0d655ff930b94e97eec42bd6f2b9ba1d1eba`.
- Round-0 `main.tex` SHA256:
  `ba1436720a49b0667e168afd5f5e352efc657b82907af3a402ca36fd1cfa5eff`.
- Round-0 `references.bib` SHA256:
  `d134944049dac7f06c2f757292dd550df7fd03b529dc87862b14f6b2728f8bcf`.
- `verify_p175.py` SHA256:
  `9a9ff255e36262034d1012a1cb38f5ef7018a4579a80a8ee1153c10f00741b2a`.

An author-round isolated cold build containing only `main.tex` and
`references.bib` produced the same Round-0 PDF SHA256 and compared byte for
byte with the now-preserved `main_round0_original.pdf`.

## Log and PDF inspection

- No `Warning`, `undefined`, `multiply defined`, `Overfull`, `Underfull`, or
  `Error` marker occurs in the settled LaTeX/BibTeX logs.
- All fonts reported by `pdffonts` are embedded; all are subset fonts.
- `pdfinfo` reports empty Title, Author, Creator, Producer, Subject, and
  Keywords fields.
- `pdftotext -layout` returned all sections, equations, the control table,
  and all seven references.
- All three pages were rendered to PNG at 150 dpi and inspected individually;
  no clipping, collision, missing glyph, blank page, or stranded heading was
  found.

No hostile-review artifact was generated in Round 0.

## Review rounds

Review A returned no finding; `main_round1.pdf` is byte-identical to the
Round-0 PDF.  Review B's exact-owner reframe produced the four-page Round-2
candidate, 328,780 bytes, SHA-256
`321d59b8b66cc2aef22296f214ee0d0072652c86d53293714599b0e07ee4b703`.
Its settled logs contain no warning, bad box, unresolved citation/reference,
rerun request, or fatal error.  Reviewer B delta-accepted the repair.  Two
final temporary directories initialized with only `main.tex` and
`references.bib` reproduced `main.pdf` byte for byte; their retained
`build_final_cold{1,2}_*.log` files have no warning or error.
