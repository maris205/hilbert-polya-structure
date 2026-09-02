# Deterministic compile report

## Frozen build contract

- engine: LuaLaTeX
- invocation: `lualatex -interaction=nonstopmode -halt-on-error -jobname=main`
- passes per build: 2
- independent fresh builds per round: 2
- environment: `SOURCE_DATE_EPOCH=1788307200`, `FORCE_SOURCE_DATE=1`,
  `TZ=UTC`
- deterministic trailer: fixed by `\pdfvariable trailerid`
- optional volatile PDF metadata: suppressed by
  `\pdfvariable suppressoptionalinfo 767`

## Fresh-build results

| round | pages | embedded/subset font rows | archived SHA-256 | fresh pair |
|---:|---:|---:|---|---|
| 0 | 2 | 20 | `baa01816e5a604b684a9ae067ff2c1fbf4b3a8bbac2b18c736ab5f1b7d479300` | byte-identical |
| 1 | 3 | 23 | `5a248cb37dfb8eb26b3b698fd9ae0d2f23375dd0018c93bec9cf4d90ba4b7bab` | byte-identical |
| 2 | 4 | 24 | `3a3684fe15c61d0e6fa76b46a0719a80e3e63d1a6a2a6091028f11d95a92e518` | byte-identical |

The hashes are pairwise different and `paper/main.pdf` is byte-identical to
`paper/main_round2.pdf`.

## Log, font, text, and visual audit

The final-pass log from both fresh builds of every round was searched for
`LaTeX Warning`, package warnings, overfull or underfull boxes, undefined
references, rerun requests, and missing characters.  The audit was
warning-free: zero matches in all six final-pass logs.  First-pass bootstrap
cross-reference notices are resolved by the declared second pass and are not
represented as final build warnings.

`pdffonts` found 20, 23, and 24 rows respectively.  Every font was embedded
and subset; no unembedded font row was present.  `pdfinfo` reported exactly
2, 3, and 4 pages.  `pdftotext` recovered the title, parabolic theorem,
strict/wall/zero/disconnected/rank-one boundaries, `19,056`, `84/84`, the
all-depth duplicate-JSON and complete-grid contracts, all five FAIL tokens,
`ROUTE_A_REJECTED`, `Route B is false`, the scope literal, and all four DOI
strings used in the audit.  Normalized extracted word counts are
644/1404/1881 for rounds 0/1/2 and increase strictly.

All nine pages across the three rounds were rasterized at 120 dpi and visually inspected.
Margins, equations, theorem text, the boundary table, hyperlinks, references,
and page numbers were intact; there was no clipping, overlap, blank accidental
page, missing glyph, or illegible line.  The intentionally short final
reference pages are stable and visually balanced.  Thus PDF, font, text, log,
and visual gates pass.

Raw compiler sidecars remain excluded from the exact release ledger; this
report and `PAPER_IMPROVEMENT_LOG.md` retain the audited log conclusions.
