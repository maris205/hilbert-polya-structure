# SD-C01 — Finite-State Arithmetic Skeleton

## Frozen construction

The baseline is the two-sided full \(q\)-shift with \(q\in\{2,3,5\}\),
constant symbol roof \(\log q\), unit potential, and trivial cocycle.  Its
inverse zeta determinant is

\[
D_q(s)=1-q^{1-s}.
\]

The comparison class is a finite directed multigraph with a positive
locally-constant edge roof, complex locally-constant weight, and an intrinsic
finite-dimensional unitary cocycle.  No rational prime, Riemann zero, or
target-fitted phase is an input.

## Findings

- **PROVED:** the full shift has the same degree-by-degree primitive count as
  monic irreducible polynomials over \(\mathbb F_q\), and its repetitions give
  the corresponding function-field Euler bookkeeping.
- **PROVED:** this is a counting identity/function-field analogue, not a
  canonical rational-prime identification.
- **PROVED:** every nondegenerate determinant in the finite-memory comparison
  class is a finite exponential polynomial and has \(O(R)\) zeros in
  \(|s|\le R\), counted with multiplicity.
- **PROVED:** the completed Riemann divisor has order \(R\log R\), so the
  comparison class cannot equal a zero-free entire factor times \(\xi(s)\).
- **PROVED:** a nontrivial finite-group character can cancel the positive
  sector locally, but the full skew product retains the trivial sector and the
  \(O(R)\) obstruction.

This is a successful exact arithmetic skeleton for the function-field
analogue and a negative baseline for the rational-prime Hilbert–Pólya target.
It stops at Route A.

## Artifacts

- [Derivation package](DERIVATION_PACKAGE.md)
- [Proof package](PROOF_PACKAGE.md)
- experiment code and machine-readable results under the session-level
  code/ and results/ directories
