# Compilation report

- Engine: LuaLaTeX 1.14, two passes per revision.
- Fixed environment: `SOURCE_DATE_EPOCH=1788048000`, `FORCE_SOURCE_DATE=1`,
  `TZ=UTC`.
- A fixed LuaTeX trailer ID is declared in `main.tex`; independent fresh
  temporary trees therefore produce byte-identical PDFs.  The final proof
  block uses the environment's single QED marker (the duplicate explicit
  marker from the draft was removed).
- PDFs are two pages each; round 0, round 1, and round 2 hashes are pairwise
  distinct; `main.pdf` is byte-identical to round 2.

| artifact | SHA-256 | pages |
|---|---|---:|
| `main_round0_original.pdf` | `1cf00668f36e7d1b6d48f990a3ffe0867f2f54a294875230a3a30ebda396f464` | 2 |
| `main_round1.pdf` | `bd1442ee27a526003cab4198db9ea3ac81038b42c92b81be5247b6f3526575e5` | 2 |
| `main_round2.pdf` | `8e79456a5dd340cd6755d2db9c3809656f25e9d181d9c74b87a80bbd2dff99fc` | 2 |
| `main.pdf` (copy of round 2) | `8e79456a5dd340cd6755d2db9c3809656f25e9d181d9c74b87a80bbd2dff99fc` | 2 |

- References/citations: none undefined; text extraction and embedded-font
  checks pass.
- The final pass has no unresolved references or layout boxes exceeding the
  margin.  The long evaluator tuple is kept in a compact monospace line and
  remains within the declared page geometry.
