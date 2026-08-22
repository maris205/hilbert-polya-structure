# Theorem package (finite and conditional boundaries)

## Proposition 1 — Floquet block determinant

For branch labels `s0,s1` and phase matrices
\[
B_{t,s}=\begin{pmatrix}2\xi_s+\alpha_t&-1\\1&0\end{pmatrix},
\qquad \xi_0=-1,\;\xi_1=1,
\]
the chronological block matrix
\[
M_{(s_0,s_1)}=B_{1,s_1}B_{0,s_0}
\]
has determinant one.  This is an exact two-step algebraic statement.

## Proposition 2 — Primitive decomposition of the finite transfer

Let `Q` be the frozen four-state adjacency and let `A_ij=Q_ij M_j` be the
8-by-8 block transfer.  For every `n<=6`,
\[
\operatorname{Tr}(A^n)=\sum_{d\mid n}d\sum_{[w]\in\mathcal P_d}
 \operatorname{Tr}(M_w^{\,n/d}),
\]
where `P_d` is the set of lexicographically least rotations of admissible
non-periodic block words of length `d`.  The producer and independent checker
verify this identity for each of the chronological, reversed, and same-phase
controls.

## Proposition 3 — Newton consistency

For each finite transfer matrix, the coefficients of `det(I-zA)` satisfy the
Newton recurrence
\[
k c_k=-\sum_{j=1}^k c_{k-j}\operatorname{Tr}(A^j),\quad c_0=1,
\]
through the recorded prefix.  A separate SymPy implementation verifies the
integer coefficients.

## Explicit boundary

These propositions concern only the frozen finite symbolic model.  They do
not imply a geometric Hénon coding, completeness of real periodic orbits, a
nuclear/Fredholm operator, a global determinant, a zero-count theorem, or any
arithmetic identification.  Those upgrades are open and are not claimed.
