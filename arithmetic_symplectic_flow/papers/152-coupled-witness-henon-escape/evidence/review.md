# Bounded mathematical review — ASFS-20260915-CHE01

**Date:** 2026-09-15  
**Candidate:** ASFS-20260915-CHE01  
**Review scope:** the frozen coupled Hénon map, complete periodic-state proof,
monodromy, ordinary-zeta convergence, and the declared arithmetic controls.  
**Finding:** no mathematical blocker identified for the stated scoped results.  
**Calibration:** NOT_CALIBRATED; criteria_binding_unavailable.

This is a separately assigned model review, not human peer review, a
cross-model result, a literature novelty assessment, or a Route evaluation.
The reviewer read the [frozen card](../candidate-card.md), the entire
[paper](../paper.md), the [claim ledger](../claim-ledger.md), the
[package overview](../README.md), and the [evidence index](README.md).
The reviewer recomputed the arguments rather than relying on a prior
candidate's verdict. The author and reviewer use the same model family;
separate task execution does not establish independent error processes.
No manuscript file was edited by this reviewer.

## Criterion-bound checks

The criteria are the local candidate contract and the same-object obligations
in the [controlling plan](../../../plan.md), not inferred journal standards.

| Check | Judgment | Paper anchor | Independent verification and limit |
| --- | --- | --- | --- |
| Full global symplectic owner | MEETS | Equations (2), (5), (6) | The displayed inverse is two-sided; the symmetric Hessian cancels the additional two-form. Countably many open four-dimensional components cause no smooth-manifold obstruction. |
| Composite exclusion | MEETS | Equations (7)--(9) | Every positive integer witness count produces a strictly positive second force component, contradicting the sum of any finite periodic recurrence. All real states and all periods are covered. |
| Complete prime periodic set | MEETS | Equations (10)--(11) | Both eigenvalues of C are positive. Every two-dimensional block has positive reciprocal multipliers off the unit circle, so every iterate has only the zero fixed coordinate. The intrinsic phase gives exactly one primitive K_p-cycle. |
| Repetition and monodromy | MEETS | Equations (12)--(13) | The two negative block determinants multiply to a strictly positive four-dimensional determinant for every repetition. The determinant concerns the return map, not the flow-direction multiplier. |
| Ordinary-zeta owner and abscissa | MEETS | Equations (14)--(16) | The full periodic classification supplies the unweighted product; elementary comparison gives normal convergence on Re(s) greater than log 2 and prime-harmonic divergence gives the exact absolute-convergence boundary. |
| Arithmetic controls and generality | MEETS | Section 6 | Zero forcing, positive-count replacement, and the shifted divisibility test change the surviving labels as stated. The generic witness-encoding limitation is retained. |
| Stronger natural clock and analytic owner | NOT_ASSESSED | Sections 3, 6--8 | The package explicitly leaves a privileged clock, operator, trace, continuation, and Riemann relevance unresolved; this review supplies none of them. |

## Recomputed mathematical details

### Geometry and complete composite exclusion

Writing the real-coordinate derivative as

\[
DF=\begin{pmatrix}0&I\\-I&S\end{pmatrix},
\qquad S=2I+\nabla^2V_a(P)=S^T,
\]

gives the symplectic identity directly. Solving the first image coordinate
for the old P and then the second for the old Q reproduces equation (5)
without any implicit inverse-function assumption. Every fixed integer
component is included, and the phase permutation preserves the component
counting measure. Unit roof prevents finite-time accumulation of returns.

For the composite sign argument, the identity

\[
g_a(t)=e^t+(a-1)(e^t-t)>0
\qquad(a\in\mathbb Z,\ a\geq1)
\]

is valid for all real t because e^t-t is at least one. The case a=1 needs
only strict positivity, not a positive uniform lower bound on the whole
line. A hypothetical m-cycle has a finite sum of strictly positive terms
in its second recurrence component, whereas the second difference sums to
zero. Thus the proof does not omit an a=1 escape regime or assume global
boundedness of arbitrary nonperiodic trajectories.

### Prime packets and stability

The prime Hessian is exactly

\[
C=\begin{pmatrix}1&1\\1&2\end{pmatrix},
\qquad \operatorname{spec}(C)=\{(3-\sqrt5)/2,(3+\sqrt5)/2\}.
\]

Applying the same orthogonal change to Q and P is symplectic. Each resulting
block has characteristic polynomial

\[
r^2-(2+\nu)r+1,
\]

whose roots are positive reciprocals with neither equal to one. All powers
therefore have no nonzero fixed vector. This excludes additional periodic
points on the full real fibre, rather than selecting the origin by fiat.
The label p is unchanged and the phase must make a whole K_p turn, so the
least period is exactly K_p. The two small primes 2 and 3 are distinct
period-one packets, not one merged packet.

For every positive integer m,

\[
\det(I-B_\nu^m)=2-\lambda_\nu^m-\lambda_\nu^{-m}<0
\quad(\lambda_\nu>1).
\]

Multiplication over the two blocks verifies both the sign and the absence
of degeneracy in equation (12). No passive factor or earlier candidate's
stability matrix is used.

### Scalar analytic object

For sigma greater than log 2, the term exp(-sigma K_p) is bounded by a
constant times (p-1) to the power -sigma/log 2. Comparison with all integers
gives summability, and the repetition tail has the uniform bound used in
equation (15). At sigma equal to log 2, the first-repetition term is at
least 1/p. The paper supplies its own finite-Euler-product proof that the
prime harmonic sum diverges. The argument does not need the prime number
theorem, an asymptotic count in every dyadic interval, or numerical prime
data. Absolute convergence depends only on Re(s), so the claimed abscissa
is correct also for the complex logarithmic series.

This establishes only the chosen ordinary scalar product. In particular,
nonzero return-map determinants do not by themselves establish a function
space, distributional trace, Fredholm determinant, or continuation.

## Scope issue raised and addressed

Before the paper was completed, the reviewer asked the author to distinguish
this candidate's timing from the earlier local-batch schedule. Here the
complete witness count is evaluated at every step. Consequently K_n is a
chosen all-integer binary label phase, not the number of elementary
operations performed by one complete scan.

**Adjudication: ADDRESSED.** Section 3 explicitly states that the K_n steps
do not partition one scan and records K_p(p-2) direct divisibility tests per
primitive prime period. Sections 6 and 7 preserve the rounded-clock and
naturalness boundaries. Ownership of the stipulated time and its
logarithmic-order formula are proved; a stronger natural timing explanation
is not supplied or silently inherited.

The shifted control is also correct in the completed manuscript: n=3 is
excluded because 2 divides 4. For every n at least 3, a composite n+1 has
a divisor between 2 and sqrt(n+1), strictly below n, so the stated interval
detects it. The n=2 interval is empty. No finite check is used to prove this
infinite control statement.

## Coverage receipt and handoff

No unresolved mathematical defect was found in the reviewed claims.
The coverage table above records the geometry, complete periodic
classification, all repetitions, scalar convergence, and controls checked.
Naturalness, external novelty, operator theory, and target identity were
not treated as silently satisfied criteria.

The same-object ledger remains intact for ASFS-20260915-CHE01. The bounded
portfolio decision may be **advance**: prime-exclusive full packets and
nondegenerate return monodromy coexist in this actual coupled map. Any
changed potential, clock, or carrier requires a **fork** and a fresh card.
Formal Route coordinates remain UNASSIGNED; Route B remains NOT INVOKED.
