# Paper 06 Source Lock

## Stage identity

- Date frozen: 2026-08-13.
- Base candidate: SD-C07.
- New candidate: **SD-C08**.
- Candidate name: minimal-binary Parry/Hellinger extension.
- Primary and only system family: Symbolic Dynamics.
- Stage status: **GO_A3_ARCHIMEDEAN_FACTOR / STOP_GLOBAL_COMPLETION**.
- Route B: locked.

## Frozen source

The arithmetic source is the symmetric monoidal skeleton of finite full
shifts

\[
F_m\boxtimes F_n\cong F_{mn},\qquad h(F_n)=\log n.
\]

Its tensor atoms are recovered internally as the nonunit indecomposables.
The unique atom of least positive entropy is \(F_2\). No prime table is part
of the candidate definition.

Let \(K_2=J_2/2\) be the maximal-entropy Parry transition of \(F_2\). Under
the intrinsic symbol-permutation action,

\[
\mathbb C^2=\mathbb C\Omega_2\oplus E_2,
\quad \Omega_2=2^{-1/2}(1,1),
\quad E_2=\mathbb C(1,-1).
\]

Both summands have multiplicity one. The orientation of \(E_2\) is a sign
gauge and disappears under absolute Mellin transform.

## Frozen candidate object

SD-C08 is the tuple consisting of:

1. the full-shift tensor source and its atom-loop suspension with roof
   \(h(F_p)=\log p\);
2. the distinguished internal object \(F_2\) and its Parry kernel \(K_2\);
3. the tilted Parry trace family
   \[
   H(z)=e^{zQ/2}K_2e^{zQ/2},
   \qquad Q=\operatorname{diag}(1,-1);
   \]
4. the matrix-weighted atom transfer
   \[
   \mathcal A_s=\bigoplus_{F_p}p^{-s}K_2;
   \]
5. the binary sign Birkhoff sum under the same \(K_2\) process;
6. the Hellinger chiral pairing of \(\mathcal A_s\) and
   \(\mathcal A_{1-s}\).

The matrix weight is a transfer cocycle on the symbolic atom loop. It is not
called a group cocycle, a unitary cocycle, or an actual skew-product shift.

## Frozen transforms and domains

- Fredholm determinant of \(\mathcal A_s\): initially \(\Re s>1\).
- Binary fluctuation Mellin limit: \(\Re s>0\).
- Their same-source product: initially \(\Re s>1\).
- Chiral self-adjoint family: \(s=1/2+it\).
- Paired \(\det_3\) diagnostic: \(1/3<\Re s<2/3\).

The Mellin and Fredholm transforms are two canonical functors of the two
irreducible sectors of one \(S_2\)-equivariant source. Their probability
generators are unified by
\(\operatorname{tr}H(z)^r=(\cosh z)^r\), but they are not declared to be a
single determinant.

## Allowed inputs

- full shifts, tensor product, tensor atoms, and topological entropy;
- the maximal-entropy Parry measure/kernel of a finite full shift;
- symbol-permutation representations and their isotypic decomposition;
- Birkhoff sums, local central limit estimates, Mellin transforms;
- Fredholm and Schatten determinants on their proved domains;
- finite atom cutoffs recovered from multiplication and preregistered
  \(q\)-symbol, biased, reversible, and inventory controls.

## Forbidden inputs and moves

- Riemann-zero tables or target-root fitting;
- copying the Gamma factor, zeta continuation, or the functional equation
  into the candidate;
- selecting \(1/2\) because it is the target critical line;
- treating the same-source product as a proved single dynamical determinant;
- analytic continuation of the finite-\(N\) Mellin moments by declaration;
- deleting divergent traces without naming the regularization and its loss;
- cross-atom mixing credited without an exact cancellation theorem for mixed
  primitive cycles;
- treating mass noncommutation as sufficient for spectral motion in the
  one-sided ansatz \(A_t=G^{1/2+it}K\), whose phase is universally removable;
- borrowing coordinates from a different candidate or system family;
- Route B.

## Precision and data lock

Finite algebraic identities are evaluated directly. Mellin experiments use
odd \(N\) to avoid a zero atom for negative moments. Binary64 errors, complete
grids, and slow-convergence corners are reported. No Riemann zero or
target-root cutoff exists.
