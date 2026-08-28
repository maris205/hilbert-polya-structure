# P25 Round-8 validation report

## Material Passport

- Origin skill: `ars-codex:academic-research-suite`
- Origin stage: ARS Stage 1 research
- Candidate: `P25-Q-SYMBOL-NO-REPEAT-PHASE-CALIBRATOR`
- Freeze SHA-256: `43393de457d985009883ab31a023c7dcf6444f9640e86d9aa969cc3993cf49a4`
- Core SHA-256: `9a29d8894b1ac81f9588fe221375bddc671898b9b08b409b0fa5a1d5a42a9014`

## Exact theorem

For disk radius `a>0` and equilateral center separation `d`, the symmetric
period-two bounce has mean flight length `d-2a`, while the symmetric
period-three triangle has mean flight length `d-sqrt(3)a`.  Their exact gap is
`(2-sqrt(3))a>0`.  A roof coboundary `tau=c+u-u o sigma` would give mean `c`
on every periodic orbit, so the physical roof is not cohomologous to a
constant.  For every scalar `c`, at least one witness has mean-length error at
least `(2-sqrt(3))a/2`.

## Locked replay

- Exact witness-family rows: `6`.
- Frozen physical owner rows: `2241`.
- At each of `d/a=29/5,6,31/5`, exactly three period-two owners agree with
  the period-two scalar clock and the other 744 frozen owners disagree at the
  prespecified tolerance.
- The replay checks the exact symmetric formulas but does not prove the
  theorem from floating-point rows.

## Route boundary

The theorem refutes only an owner- and repetition-preserving global scalar
substitution from the unit-roof determinant to the physical clock.  It does
not refute a transfer operator with the genuine nonconstant roof, compute the
Gutzwiller--Voros zeta, or compute the exact multiple-scattering determinant.
The formal A1--A2 tuple remains owned by the unit-roof symbolic calibrator;
the physical three-disk tuple remains `UNASSIGNED`, the overall calibrator
verdict remains `ROUTE_A_REJECTED`, and Route B remains closed.
