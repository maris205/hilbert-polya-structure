# C190 paper artifacts

`main.tex` is the final source.  The release preserves the PDFs produced by
the baseline and two actual source-revision rounds:

- `main_round0_original.pdf` — recurrent coordinates, fixed/cycle ledger,
  zeta, and evidence boundary;
- `main_round1.pdf` — adds the full noninvertible Koopman algebraic spectrum;
- `main_round2.pdf` — adds recurrent reflection reversal, nonfaithful/global
  boundaries, audit totals, strict Route-A stop, and declarations;
- `main.pdf` — byte-identical release copy of round 2.

LuaLaTeX is used for the bilingual abstract.  Final and fresh builds use the
frozen epoch `SOURCE_DATE_EPOCH=1787702400`, `FORCE_SOURCE_DATE=1`, and UTC.
Exact hashes, log, font, determinism, and visual findings are in
`COMPILE_REPORT.md`.
