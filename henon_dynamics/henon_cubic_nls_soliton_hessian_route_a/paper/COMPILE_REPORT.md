# Compile and PDF audit

LuaHBTeX/LuaLaTeX was run with `SOURCE_DATE_EPOCH=1787875200` and
`FORCE_SOURCE_DATE=1`.  For each revision, two independent output directories
were built with two passes each; the final PDFs compare byte-for-byte.

```text
lualatex -interaction=nonstopmode -halt-on-error -jobname=main_r0 \
  '\\def\\CRevisionRound{0}\\input{main.tex}'
lualatex -interaction=nonstopmode -halt-on-error -jobname=main_r1 \
  '\\def\\CRevisionRound{1}\\input{main.tex}'
lualatex -interaction=nonstopmode -halt-on-error -jobname=main_r2 \
  '\\def\\CRevisionRound{2}\\input{main.tex}'
```

| Artifact | Pages | Bytes | SHA-256 |
|---|---:|---:|---|
| `main_round0_original.pdf` | 1 | 118592 | `a570aa76357fc22cc7c0450413dcf64d1506d82fde9f96ae273aa2ca3b504e9a` |
| `main_round1.pdf` | 2 | 120102 | `ac62e4a1e983501385a408bc9f8c8c191e8f5ac81f969b0553f2a1b757e5c5f6` |
| `main_round2.pdf` | 2 | 128946 | `a03e7851eb02c4937c72289768edbb0591311176bc54705913d8beaac81624b4` |
| `main.pdf` (release = round 2) | 2 | 128946 | `a03e7851eb02c4937c72289768edbb0591311176bc54705913d8beaac81624b4` |

The three revision hashes are pairwise distinct and the release is byte equal
to round 2.  `pdffonts` reports 20 font instances, all embedded and subsetted.
`pdftotext` contains `Hessian`, `Pöschl`, `Morse`, `VK`,
`A4_NATURAL_QUANTIZATION`, `ROUTE_A_REJECTED`,
`NO_BAD_EULER_OR_ROOT_NUMBER`, `Weinstein`, `Zakharov`, `Teller`, and
`10.1007/BF01331132`.  Each revision was built in two independent output
directories; the paired PDFs compare byte-for-byte.  The first pass emits only
the normal `Label(s) may have changed` rerun notice; the second pass has no
overfull/underfull boxes, duplicate destinations, undefined references, rerun
warnings, or fatal errors.
