# Paper 16 — Character-Resolved Cycle-Index Determinants

Candidate **SD-C18** retains the atom-permutation information erased by the
scalar tensor-subset determinant.  At squarefree content \(pqr\), the formal
Burnside residual is

\[
[S_3/S_3]+[S_3/C_3]-[S_3/C_2],
\]

with subgroup marks \((0,0,3,1)\), and its representation image is

\[
\mathbf1+\mathbf{sgn}-\mathbf{Std},
\qquad \chi=(0,0,3).
\]

This is a genuine formal equivariant signal.  It does not become an
arithmetic character-Fredholm factor in the canonical realizations:

- distinct weights \(p^{-s}\) break fixed-fiber \(S_n\) commutation;
- equal weights leave only the trivial rank-one image;
- the diagonal subset lift has ghosts \(b(x^r)\), not \(b(x)^r\), and adds
  mixed determinant factors;
- any readout detecting the isolated \(pqr\) residual introduces a mixed
  primitive trace-log term absent from the pure Euler ledger;
- the diagonal prime-subset operator satisfies
  \(D_s\in\mathcal S_q\iff q\operatorname{Re}s>1\), but its valid Fredholm
  determinant is still the wrong mixed product.

## Main decision

```text
GO_FORMAL_EQUIVARIANT_LEDGER
STOP_CHARACTER_FREDHOLM_FIBERS
STOP_STANDARD_SUPERTRACE_INTERPRETATION
STOP_ARITHMETIC_SELECTIVITY
PROVES_TOO_MUCH

(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_WEAK,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

The scalar rank-one shadow retains the exact Euler determinant proved in the
preceding paper.  That scalar A2 result is not a character-resolved SD-C18
result and is not combined with this candidate's route tuple.

## Reading map

- Paper: [`main.pdf`](main.pdf)
- Frozen object: [`SOURCE_LOCK.md`](SOURCE_LOCK.md)
- Preregistered claims: [`PREREGISTRATION.md`](PREREGISTRATION.md)
- Proofs: [`PROOF_PACKAGE.md`](PROOF_PACKAGE.md)
- Derivations: [`DERIVATION_PACKAGE.md`](DERIVATION_PACKAGE.md)
- Primary-source boundary: [`LITERATURE_AUDIT.md`](LITERATURE_AUDIT.md)
- Research story: [`NARRATIVE_REPORT.md`](NARRATIVE_REPORT.md)
- Manuscript plan: [`PAPER_PLAN.md`](PAPER_PLAN.md)
- Figure specification: [`FIGURE_SPEC.md`](FIGURE_SPEC.md)
- Cross-family clues only: [`ROUND2_CLUES.md`](ROUND2_CLUES.md)
- Build verification: [`COMPILATION_REPORT.md`](COMPILATION_REPORT.md)

## Source boundary

Burnside-valued zeta functions, the Burnside/species correspondence,
cycle-index and necklace/Witt formalisms, and \(\lambda\)/Adams operations are
classical.  The paper claims only the SD-C18 application and its scoped
incompatibility theorem for the canonical rank-one and diagonal lifts.

No Riemann-zero data, root fitting, geometric carrier, or Route-B operator is
used.
