# Paper 17 — Genuine Fiber Symmetry and Artin Character Factors

Candidate **SD-C19** replaces the atom-relabeling symmetry rejected in Paper 16
by a genuine finite fiber.  For the signed tensor-subset shift and the intrinsic
cocycle

\[
\alpha(S)=|S|\pmod 2,
\]

deck translations act only on the \(C_2\) coordinate and commute with the
arithmetically weighted shift.  The two character determinants and the whole
regular determinant are

\[
D_+=\prod_p(1-x_p),\qquad
D_-=\prod_p(1+x_p),\qquad
D_{\rm reg}=D_+D_-=\prod_p(1-x_p^2).
\]

At \(x_p=p^{-s}\), \(\Re s>1\), these become

\[
D_+=\zeta(s)^{-1},\qquad
D_-=\frac{\zeta(s)}{\zeta(2s)},\qquad
D_{\rm reg}=\zeta(2s)^{-1}.
\]

Only \(D_{\rm reg}\) is the determinant of the whole extension.  The other two
are isotypic blocks of that same transfer.  The construction is lawful and has
genuine recurrent fiber motion, but it does not repair the primitive orbit
ledger: mixed lifted cycles remain, singleton clocks are multiplied by the
fiber order, and all matched inventories reproduce the identities exactly.

## Main theorem and decision

A relabeling-natural, inclusion-compatible one-letter cocycle satisfying the
operator-coherent atom-local identity must obey
\(\alpha(S)=a^{|S|}\).  Its image is cyclic; if the full fiber extension is
transitive, the fiber group is cyclic.  This theorem does not cover
transition-dependent cocycles.

```text
GO_GENUINE_COMMUTING_FIBER
GO_SAME_OBJECT_ARTIN_FACTORIZATION
GO_ATOM_LOCAL_CHARACTER_FACTORS_AT_Z_EQ_1

STOP_PRIMITIVE_LIFT
STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH
STOP_SCOPED

(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_WEAK,
 A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

## Reading map

- Paper: [`main.pdf`](main.pdf)
- Frozen object: [`SOURCE_LOCK.md`](SOURCE_LOCK.md)
- Preregistered claims: [`PREREGISTRATION.md`](PREREGISTRATION.md)
- Proofs and derivations: [`PROOF_PACKAGE.md`](PROOF_PACKAGE.md),
  [`DERIVATION_PACKAGE.md`](DERIVATION_PACKAGE.md)
- Literature boundary: [`LITERATURE_AUDIT.md`](LITERATURE_AUDIT.md)
- Research narrative and paper plan:
  [`NARRATIVE_REPORT.md`](NARRATIVE_REPORT.md), [`PAPER_PLAN.md`](PAPER_PLAN.md)
- Figure specification: [`FIGURE_SPEC.md`](FIGURE_SPEC.md)
- Cross-family clues only: [`ROUND2_CLUES.md`](ROUND2_CLUES.md)
- Build verification: [`COMPILATION_REPORT.md`](COMPILATION_REPORT.md)

No Riemann-zero data, root fitting, geometric carrier, or Route-B operator is
used.  The only primary system family is Symbolic Dynamics.
