# Paper20 — Initial Proposal (superseded design log)

This log records the starting A4 idea and the corrections that were required
before a candidate gate could pass. It is not an independent review.

## Initial idea

Start with a composition of Hamiltonian shears
\[
S_V(q,p)=(q,p+\nabla V(q)),\qquad
T_W(q,p)=(q+\nabla W(p),p),
\]
and seek a sparse, asymmetric pair of potentials whose Newton-face degree
recurrence is a positive matrix with a Perron root not equal to the product of
the two one-shear degrees. The first exploratory notation used generic
gradient matrices \(A,B\), a finite Newton fan, and a cone of competing face
inequalities.

The candidate was then narrowed to the literal family
\[
 V_g=q_1^2q_2^2+q_1^g,\qquad W_g=p_1^2p_2^2+p_2^g,\qquad g\ge5,
\]
on \(\mathbb A^4\). This is the only family retained in the final proposal.

## Corrections required by the proof audit

### 1. Generic matrices were not admissible

An arbitrary pair of nonnegative matrices can be made to have almost any
spectral radius, but those matrices need not arise from polynomial gradient
monomials. The final design binds each row to an actual monomial exponent:
\[
 A_g=\begin{pmatrix}g-1&0\\2&1\end{pmatrix},\qquad
 B_g=\begin{pmatrix}1&2\\0&g-1\end{pmatrix}.
\]
Any extension must repeat the selector calculation from the supports.

### 2. The symmetric two-monomial template was rejected

If both gradient rows have the same row sum, then the Perron root of the
complete product can collapse to the product of the two shear degrees. That
would not support a non-product headline. The retained pair has opposite
triangular orientation: the high pure power selects the first \(S\)-row and the
second \(T\)-row, while the mixed monomial supplies the other rows.

### 3. Half-step and full-step matrices were separated

The off-diagonal matrix
\[
 \begin{pmatrix}0&B\\A&0\end{pmatrix}
\]
records two half-steps. The complete map \(F=T\circ S\) returns to the \(q\)
phase and has
\[
 C=BA,
 \qquad
 \widehat M=\begin{pmatrix}C&0\\A&0\end{pmatrix}.
\]
Using the half-step matrix without a period or square-root correction was
removed from the proposal.

### 4. A single strict two-shear cone was rejected

The tempting condition \(Au>v\) and \(Bv>u\) cannot be a strict invariant for
the completed step, because the returned intermediate vector is exactly
\(v_{n+1}=Au_n\). The final proof uses a \(q\)-phase cone for \(u_n\), a
separate \(S\)-phase selector check for \(v_{n+1}\), and a \(T\)-phase check
before returning to the \(q\) phase.

### 5. Visibility was made explicit

The spectral radius of a formal matrix is not automatically the dynamical
degree. The final proof identifies \(q_2\) as the maximal coordinate degree and
uses \(e_2\) to observe the positive Perron class. Without this step, the
claim is only a recurrence for an auxiliary vector.

### 6. Scope was narrowed

The initial notes considered arbitrary sparse supports, coefficient families,
and possible finite fans. Those extensions were removed. The final package is
uniform only in integer \(g\ge5\), with the displayed positive coefficients,
over characteristic zero. Any broader statement is a STOP condition.

## Initial-gate outcome

The corrected explicit family received a conditional design pass. The pass is
void if a future draft restores generic matrices, strict one-phase cones,
half-step spectral claims, or an unqualified “all sparse shears” theorem.
