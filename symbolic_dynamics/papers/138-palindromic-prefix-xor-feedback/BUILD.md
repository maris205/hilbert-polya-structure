# Build and verification record — P138

**Artifact:** anonymous Stage-2 Round-0 short paper  
**External status:** `HOLD_EXTERNAL`  
**Build date:** 2026-09-01 (UTC)

## Toolchain

- Python 3.12.3
- pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)
- BibTeX 0.99d (TeX Live 2022/dev/Debian)

## Exact verifier

From this directory:

```bash
python code/verify.py | cmp - code/verification_output.txt
```

The comparison exits successfully.  The canonical transcript records:

- complete functional graphs for `n=1,...,18` (524,286 states);
- every-target decoder comparison through `n=15`;
- closed sharp-family checks through `n=64`;
- 3,870,590 exact assertions;
- final status `PASS`.

SHA-256 of `code/verification_output.txt`:

```text
551a61f69ba5bb09355bc99c95401bb89ee58ab5c732b81eaa24c6a016330675
```

## Manuscript build

Run from this directory:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The settled build has 3 A4 pages and a file size of 279,050 bytes.  A second
build in an isolated temporary directory containing only `main.tex` and
`references.bib` was byte-for-byte identical to `main.pdf`.

SHA-256 of both `main.pdf` and `main_round0_original.pdf`:

```text
6c2114456c77df71516e4d9b2573907a1633cedeb9e77890c3cdcca318828942
```

## Bibliography verification

The four entries were checked against primary publisher/proceedings records:

- Galil (1978), DOI `10.1016/0022-0000(78)90042-9`;
- Rubinchik--Shur (2018), DOI `10.1016/j.ejc.2017.07.021`;
- Harju--Huova--Zamboni (2015), DOI `10.1016/j.jcta.2014.10.003`;
- Bathie--Ellert--Starikovskaya (ISAAC 2025), DOI
  `10.4230/LIPIcs.ISAAC.2025.9`.

The BibTeX run reports zero warnings.

## Settled QA

- LaTeX warnings: 0
- BibTeX warnings: 0
- undefined or multiply defined references: 0
- overfull/underfull boxes: 0
- extracted-text sentinels (`??`, `[?]`, `qquad`, `TODO`, `FIXME`): 0
- unembedded fonts: 0; every reported font is embedded and subset
- metadata author/title/subject/keywords: blank; no metadata stream
- visual inspection: all 3 rendered pages inspected; no clipping, overlap,
  malformed formula, stranded heading, or broken bibliography entry found

`main_round0_original.pdf` is the frozen Round-0 rendering.  Later review
rounds must not overwrite it.
