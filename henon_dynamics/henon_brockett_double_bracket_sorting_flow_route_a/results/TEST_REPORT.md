# C185 test report

## Exact executable checks

- Producer: PASS — 5,912 permutation rows, 118,004 pair modes, six exact
  rational matrix rows.
- Independent checker: PASS — 183,158 assertions; no producer import.
- SymPy reconstruction: PASS — 253,765 checks through a separate symbolic
  path.
- Canonical replay: PASS — 12,391,893 evidence bytes reproduced byte for byte.
- Mutation suite: PASS — 67 repaired-hash semantic attacks and one stale-hash
  attack rejected.

## Coverage

The independent checker reconstructs the schema, candidate/date/commit,
evaluator authority, every source-lock field, full theorem string registry,
finite cutoff, all permutations and pair modes, inversion/Morse dimensions,
energy extrema, rational Lax/Lyapunov rows, the source-stabilizer versus
target-tangent repeated-spectrum boundary, source metadata and year,
attribution boundary, all Route-A qualifications, eleven
scope flags, nonclaims, and integrity metadata.

SymPy independently proves the symbolic `3x3` squared-norm identity, skew and
symmetric matrix types, five isospectral trace derivatives, the full tangent
linearization, and each pair-rate formula.  It then traverses the complete
finite ledger.

Finite tests do not prove the all-size theorem.  The proof is carried in
`THEOREM_PACKAGE.md` and `paper/main.tex`.
