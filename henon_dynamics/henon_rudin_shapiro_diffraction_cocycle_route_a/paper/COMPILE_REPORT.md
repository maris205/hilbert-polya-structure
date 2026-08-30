# C248 compilation and visual audit

Build engine: LuaLaTeX 1.14.0, two passes per revision, two independent fresh
temporary trees per revision.  Every invocation used
`SOURCE_DATE_EPOCH=1788048000`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.  The first
pass in each tree reports only the normal label/rerun notices from a fresh
auxiliary directory (no overfull or underfull boxes); the second pass is
settled with no undefined references, overfull boxes, or rerun warnings.

Fresh-tree SHA-256 results (tree A = tree B in every row):

| revision | tree A / tree B PDF SHA-256 | pages |
|---|---|---:|
| 0 original | `6b983a8ea3c5ebcefd4600e33bb56eeccb9e514e96052d87980958df46bf20cc` | 2 |
| 1 | `d7785363a463898dd0b6c3bba26f28463f6e258458a8d922dd6c52273266e84b` | 2 |
| 2 | `e67f4625fdf005ad943fc7aefab01e426b163e904901e59762f82d451b1bfcec` | 3 |

Retained artifact hashes are:

```text
paper/main_round0_original.pdf  6b983a8ea3c5ebcefd4600e33bb56eeccb9e514e96052d87980958df46bf20cc
paper/main_round1.pdf           d7785363a463898dd0b6c3bba26f28463f6e258458a8d922dd6c52273266e84b
paper/main_round2.pdf           e67f4625fdf005ad943fc7aefab01e426b163e904901e59762f82d451b1bfcec
paper/main.pdf                   e67f4625fdf005ad943fc7aefab01e426b163e904901e59762f82d451b1bfcec
```

The three revisions are content-distinct; `main.pdf` is byte-identical to
round 2.  `pdfinfo` reports three pages for the final, and `pdffonts` reports
26 embedded and subsetted Latin Modern/math font entries for the final (23 and
24 for rounds 0 and 1).  `pdftotext`
contains the substitution, Hadamard energy, infinite 4-adic recursion,
autocorrelation, diffraction, full-dynamical-spectrum boundary, and the
literal `NO_BAD_EULER_OR_ROOT_NUMBER` / Route-A verdict.  No build sidecars are
retained in the package.
