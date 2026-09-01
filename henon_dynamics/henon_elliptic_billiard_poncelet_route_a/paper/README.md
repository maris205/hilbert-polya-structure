# Manuscript build contract

- Round 0: frozen confocal owner, Jacobi covering, and rotation formula.
- Round 1: strict parameter monotonicity, endpoints, and minimal-period porism.
- Round 2: clean periodic family, A2 obstruction, executable receipt, ambient
  Dirichlet formal hint with failed same-clock/phase-weight gates, and
  Route-A/sector firewalls.

Each round is compiled twice in each of two fresh directories with LuaLaTeX,
`SOURCE_DATE_EPOCH=1788220800`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.  The final
`main.pdf` must be byte-identical to `main_round2.pdf`; all three revision PDFs
must have different hashes.
