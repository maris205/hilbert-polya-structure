# Build and verification record — P139 Round-3 owner repair

**Artifact:** anonymous Stage-2 Round-3 owner-repaired short paper  
**External status:** `HOLD_EXTERNAL`  
**Build date:** 2026-09-01 (UTC)

## Owner citation closure

The controlling static owner is:

> Sabrina Mantaci, Antonio Restivo, Giovanna Rosone, and Marinella Sciortino,
> “Suffix Array and Lyndon Factorization of a Text,” *Journal of Discrete
> Algorithms* **28** (2014), 2--8, DOI
> `10.1016/j.jda.2014.06.001`.

The official ScienceDirect record confirms the title, journal, volume, date,
page range, author list, and DOI.  The institutional accepted manuscript states
in Theorem 2.2 that the left-to-right minima of the suffix permutation are
exactly the starting positions of the Lyndon factors.  The manuscript now
cites that theorem at the first ownership boundary and labels its equivalent
strict-suffix-record statement and reproduced proof as owned static input.
The ordered-tail comparison is also labelled classical static machinery.
Neither statement receives residual contribution credit.

## Toolchain

- Python 3.12.3
- pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)
- BibTeX 0.99d (TeX Live 2022/dev/Debian)

## Exact verifier

From this directory:

```bash
python code/verify.py | cmp - code/verification_output.txt
```

The comparison exits successfully.  Neither verifier file changed during the
owner repair:

```text
code/verify.py
01d10e3ffde5cfe675665e0cdfb1d2fc5e411c864ef83a82e93ca3d7d23e6b75

code/verification_output.txt
801b82a729adff63f35dc92306ad1044444d2cd0fc89b603306064fd7f6ec0fe
```

The canonical transcript still records complete functional graphs for
`n=1,...,18` (524,286 states), ordered-Lyndon/matrix target fibres through
`n=14`, the two special fibres through `n=18`, 2,654,300 exact assertions, and
final status `PASS`.  Its Duval-mask/suffix-record comparison is an integration
check for the imported theorem, not residual ownership evidence.

## Historical PDF preservation

The pre-repair PDFs were read but not overwritten.  All three retain the same
SHA-256:

```text
main_round0_original.pdf  3d41d36820b33b2b4f9215dd55d8b9d620d7c39ae0f65c5512426c8d7b79acf0
main_round1.pdf           3d41d36820b33b2b4f9215dd55d8b9d620d7c39ae0f65c5512426c8d7b79acf0
main_round2.pdf           3d41d36820b33b2b4f9215dd55d8b9d620d7c39ae0f65c5512426c8d7b79acf0
```

## Repaired manuscript build

Run from this directory:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The settled repaired build has 4 A4 pages and a file size of 326,430 bytes.  A
second build in an isolated temporary directory containing only `main.tex` and
`references.bib` was byte-for-byte identical to the working PDF.

SHA-256 of both `main.pdf` and the read-only `main_round3.pdf`:

```text
3c4b474a05290223a1ea70a050cab1b7b46043b0ca3c67f88327d9f71ceb76e3
```

## Bibliography verification

The settled bibliography contains only the five cited entries.  Mantaci et
al. appears in `main.bbl` with all four authors, *Journal of Discrete
Algorithms* 28, pages 2--8, year 2014, and DOI
`10.1016/j.jda.2014.06.001`.  The other four previously verified entries are
unchanged.  BibTeX reports zero warnings.

## Settled QA

- LaTeX warnings: 0
- BibTeX warnings: 0
- undefined or multiply defined references: 0
- overfull/underfull boxes: 0
- extracted-text sentinels (`??`, `[?]`, `qquad`, `TODO`, `FIXME`, `XXX`,
  `VERIFY`): 0
- unembedded fonts: 0; all 25 reported font rows are embedded and subset
- metadata author/title/subject/keywords: blank; no metadata stream
- citation closure in extracted text: Mantaci et al. cited as Theorem 2.2 in
  the ownership boundary and printed completely in the references
- visual inspection: all 4 repaired pages inspected; no clipping, overlap,
  malformed formula, stranded heading, or broken bibliography entry

`main_round3.pdf` is mode `0444` and is the frozen repaired rendering.
