# Paper 8: Cat-Map Torsion Capacity

Status: `SOURCE_LOCKED_V1_NO_REGISTERED_EXECUTION`.

This project studies the standard hyperbolic toral automorphism

\[
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad
T_A(x)=Ax\pmod{\mathbb Z^2},
\]

and the torsion-order observable

\[
L(x)=\log\operatorname{ord}(x).
\]

The positive result is an exact prime-order carrier theorem.  Every
hyperbolic matrix in \(\mathrm{SL}_2(\mathbb Z)\) has a prime-order torsion
point of exact period \(n\) for every \(n>12\).  Positive trace is a direct
primitive-divisor corollary; negative trace requires a separate three-case
parity reduction through \(-A\).  For the frozen cat map, such a carrier exists exactly when
\(n\notin\{1,6,12\}\); the nonprimitive \(n=10\) case is supplied by the
Jordan block modulo five.

The negative result is a specificity certificate.  The periodic points are
exactly the torsion subgroup, and the same order observable realizes
\(\log m\) for every positive integer \(m\), is invariant, and is unbounded
and discontinuous in every torsion neighborhood.  The derivative
monodromy is constant across all period-\(n\) points and depends on \(n\), not
on the carrier prime.  Thus the project certifies intrinsic torsion capacity,
not a prime-specific clock, transfer determinant, quantization, or
Hilbert--Polya mechanism.  Its Route-A label is frozen as
`A0_FAIL_PROVES_TOO_MUCH`, subject to the registered proof audit and
independent final review.

## Frozen design artifacts

- `notes/RESEARCH_QUESTION.md`: object, questions, semantics, and nonclaims.
- `notes/PROOF_PACKAGE.md`: corrected theorem statements and full proof chain.
- `notes/NOVELTY_AUDIT.md`: scoped literature collision audit.
- `experiments/source_lock.json`: immutable candidate and evidence contract.
- `experiments/EXPERIMENT_PLAN.md`: exact post-lock audit design.
- `experiments/EXPERIMENT_TRACKER.md`: run registry and disclosure ledger.

No external prime table, Riemann-zero data, target fitting, numerical orbit
search, or registered candidate calculation belongs to the source-lock stage.
