# C188 compile report

Status: PASS.

## Frozen build

- Engine: LuaHBTeX 1.14.0 (TeX Live 2022/dev/Debian).
- Source epoch: `1787702400`; `FORCE_SOURCE_DATE=1`; `TZ=UTC`.
- Build: two successful LuaLaTeX passes per revision artifact.
- Page geometry: A4, 595.276 by 841.89 points.

## Content-distinct revision ledger

| artifact | pages | bytes | SHA-256 | distinguishing paragraph |
|---|---:|---:|---|---|
| `main_round0_original.pdf` | 3 | 165,171 | `89303b9d4960695ac775c624d98c6c99bd6278e54a53b8b26a2441183f651b52` | convention, cyclicity, exact transient and sharp family |
| `main_round1.pdf` | 3 | 165,181 | `d1e96880081a58f60fa92c3a99d239a0d7643f19981c9d9acd971e7dbec6696c` | CSR, orbit strata, eigencone and ultimate spans |
| `main_round2.pdf` | 3 | 165,199 | `f84601e5cf3b35d2ba2c2774f07fcd1cb8b380b3e5775a846acd91733e8a99f6` | ownership, reducible boundary, hostile audit and Route-A stop |
| `main.pdf` | 3 | 165,199 | `f84601e5cf3b35d2ba2c2774f07fcd1cb8b380b3e5775a846acd91733e8a99f6` | byte-identical release copy of round two |

Extracted text confirms that the revision-focus paragraphs differ.  The three
revision hashes are pairwise distinct, and final equals round two.

## Independent deterministic rebuilds

Two fresh temporary directories, each seeded only with `main.tex`, were built
twice at the frozen epoch.  Both outputs had SHA-256
`f84601e5cf3b35d2ba2c2774f07fcd1cb8b380b3e5775a846acd91733e8a99f6`
and were byte-identical to the release PDF.

## Release checks

- Release, revision and fresh-build logs contain no warning, undefined
  reference, missing character, overfull or underfull box, fatal message, or
  error.
- `pdffonts` reports every listed font embedded and subsetted.
- Text extraction preserves both abstracts, equations, source ledger, exact
  verdict and both references.
- All three rendered pages were inspected at 130 dpi.  No clipping, collision,
  blank page, broken glyph, or illegible formula was found.  Page three is the
  deliberately separated declarations-and-references page.
