# SD-C02 — Squarefree Admissible Shift

## Frozen construction

\[
X_{\rm sf}=
\left\{x\in\{0,1\}^{\mathbb Z}:
\operatorname{supp}(x)\bmod p^2
\ne\mathbb Z/p^2\mathbb Z\ \text{for every rational prime }p\right\}
\]

with the left shift, unit roof, zero potential, and trivial cocycle.

## Finding

**PROVED:** the only periodic point of \(X_{\rm sf}\) is \(0^\mathbb Z\).
Therefore

\[
\#\operatorname{Fix}(\sigma^n)=1,\qquad
\zeta_{X_{\rm sf}}(z)=\frac1{1-z}.
\]

The construction can have rich aperiodic language while its periodic-orbit
ledger is completely trivial.  Directly placing all \(p^2\) exclusions in the
grammar also fails the strict arithmetic-emergence version of A0.  The
candidate stops at A1 and is not sent to Route B.

## Why the finite controls differ

If only finitely many prime-square moduli are enforced, a periodic support can
avoid a residue in each of those moduli.  The collapse to the zero orbit uses
the unbounded supply of primes not dividing a proposed period.  Finite-modulus
experiments are therefore convergence diagnostics, not proofs of the
infinite-system statement.

## Artifacts

- [Proof package](PROOF_PACKAGE.md)
- code and finite-modulus controls under the session-level code/, experiments/,
  and results/ directories
