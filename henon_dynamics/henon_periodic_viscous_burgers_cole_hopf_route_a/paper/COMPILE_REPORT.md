# C195 paper compile and visual-audit report

## Canonical build

Engine: LuaHBTeX/LuaLaTeX. Fixed environment:

```text
SOURCE_DATE_EPOCH=1787788800
FORCE_SOURCE_DATE=1
TZ=UTC
lualatex -interaction=nonstopmode -halt-on-error main.tex
lualatex -interaction=nonstopmode -halt-on-error main.tex
```

The source defaults to revision 2. Revisions 0 and 1 were built by defining
`\CRevisionRound` before `\input{main.tex}`, twice per revision. Their content
increments are documented in `PAPER_IMPROVEMENT_LOG.md`.

## Artifact ledger

| artifact | pages | SHA-256 |
|---|---:|---|
| `main_round0_original.pdf` | 1 | `eecc3f8158db238c700d794f08fba0fa0281f7228aa855e2596b1d2530090f32` |
| `main_round1.pdf` | 1 | `02c24806bd8caf6f0b602d66f2144ff94bb87015f26c6ca7619eac1ee2e8fb7d` |
| `main_round2.pdf` | 2 | `db9c96e3613114c03e7a91eb0abaa70c8873a53aa99918acc45711638aa15feb` |
| `main.pdf` | 2 | `db9c96e3613114c03e7a91eb0abaa70c8873a53aa99918acc45711638aa15feb` |

The three revision hashes are pairwise distinct. The final PDF is byte-identical to
round 2.

## Fresh-directory reproducibility

The final source was copied into two independently created empty temporary
directories. Each directory received two fixed-epoch LuaLaTeX passes. The package
PDF and both fresh PDFs had the same SHA-256:

`db9c96e3613114c03e7a91eb0abaa70c8873a53aa99918acc45711638aa15feb`.

Byte comparisons package-to-A and A-to-B both passed. Neither final second-pass log
contained a warning, overfull/underfull box, badness diagnostic, missing glyph,
undefined reference, fatal message, or error.

## Font, text, and page audit

- `pdfinfo`: 2 A4 pages, PDF 1.5, 172,786 bytes.
- `pdffonts`: 24 font rows; every font is embedded and subsetted.
- `pdftotext`: extraction succeeded and yielded 1,032 words; title, equations,
  route verdict, and both references were present.
- `pdftoppm -png -r 150`: rendered exactly two pages.
- Both rendered pages were inspected at original raster detail. Page 1 has the full
  theorem/proof without clipping or collisions. Page 2 has the exact-certificate
  table, ownership/scope boundary, and references with aligned rules and no truncation.

The first visual pass found the two references orphaned on an otherwise empty second
page. Round 2 was materially repaginated: the certificate/boundary material now forms
a coherent second page with a six-row audit table. The rebuilt result passed the
fresh-directory and clean-log checks above.

Build auxiliaries are excluded from the release and removed after audit.
