# HCS-C32 Phase 3 derivation package

This document records the algebra behind the exact certificate.  All finite
field equalities are interpreted modulo the prime under discussion.

## 1. Generating function and recurrence

Use the type-one generating function

\[
S_6(q,Q)=qQ-q+2q^3.
\]

The canonical equations are

\[
p_0=-\partial_qS_6(q,Q)=1-Q-6q^2,
\qquad
P=\partial_QS_6(q,Q)=q.
\]

Hence

\[
(Q,P)=(1-6q^2-p_0,q)=H_6(q,p_0).
\]

For a cyclic word, differentiation of

\[
\Phi_n=\sum_iS_6(x_i,x_{i+1})
\]

gives

\[
\partial_{x_i}\Phi_n
=x_{i-1}+x_{i+1}-1+6x_i^2.
\tag{1}
\]

Equation (1) is exactly the Hénon recurrence.  It also fixes the orientation
of every derivative product used below.

## 2. Hessian construction and the small-clock traps

Each summand contributes

\[
\partial_{x_i}^2(2x_i^3)=12x_i,
\qquad
\partial_{x_i}\partial_{x_{i+1}}(x_ix_{i+1})=1.
\]

The safe algorithm is to differentiate each formal cyclic summand and only
then identify repeated indices.  Therefore:

- for (n\ge3), the Hessian has diagonal (12x_i) and cyclic nearest-neighbor
  entries (1);
- for (n=2), the two oriented cyclic terms are both (x_0x_1), so the
  off-diagonal entry is (2);
- for (n=1), the term (x_0x_0) contributes (2) to the diagonal.

For example, over (mathbb F_{61}),

\[
D^2\Phi_1(3)=(38),
\qquad
D^2\Phi_2(3,4)=
\begin{pmatrix}36&2\\2&48\end{pmatrix}.
\]

These values are mutation sentinels in both producer and checker.

## 3. Chronological monodromy

At ((q,p_0)),

\[
DH_6(q,p_0)=A(q)=
\begin{pmatrix}-12q&-1\\1&0\end{pmatrix}.
\]

If (x_0,x_1,\ldots,x_{n-1}) occur in time order, then application order is

\[
M=A(x_{n-1})\cdots A(x_1)A(x_0).
\tag{2}
\]

Later factors are on the left.  Reversing (2) is explicitly covered by a
mutation test.

The linearized recurrence is

\[
\delta x_{i+1}=-12x_i\delta x_i-\delta x_{i-1}.
\tag{3}
\]

The cyclic second-variation equation (B_z\delta x=0) is the same recurrence
with periodic boundary conditions.  Comparing the continuant determinant for
(3) with the characteristic determinant of (2) gives

\[
\det B_z=(-1)^{n+1}\det(I-M).
\tag{4}
\]

Formula (4) is the frozen one-dimensional specialization of the discrete Hill
formula.

## 4. Exact finite-field scan

For each registered prime and clock length, the producer iterates all states
((q,p_0)\in\mathbb F_p^2).  A state is included at clock (n) only when its
least positive return time is exactly (n).  Its coordinate word is reduced
to the lexicographically least cyclic rotation only when orbit classes are
formed; the raw state count retains all marked rotations.

For every primitive marked state the producer records

\[
\left(
\Phi_n,
\det D^2\Phi_n,
\chi_p(\det D^2\Phi_n),
M,
\det(I-M)
\right).
\]

A collision group requires the same (Phi_n) and the same nonzero quadratic
character, but at least two distinct determinant values among distinct cyclic
classes.

The independent checker does not reuse this state-by-state period test.  It
decomposes the full permutation (H_6:\mathbb F_p^2\to\mathbb F_p^2) into
cycles, filters by exact cycle length, reconstructs every word, and computes
determinants by recursive cofactor expansion rather than modular elimination.

## 5. The (p=61,n=5) witness

The two canonical words are

\[
z_A=(12,12,40,27,40),
\qquad
z_B=(33,58,36,36,58).
\]

Substitution in (1) gives five zero residuals for each word.  Direct evaluation
gives

\[
\Phi_5(z_A)=\Phi_5(z_B)=45.
\]

Term-by-term differentiation gives the two Hessians printed in
`THEOREM_PACKAGE.md`, with

\[
\det B_A=44,
\qquad
\det B_B=7.
\]

Both are nonsquares in (mathbb F_{61}), but

\[
44\cdot7^{-1}=15=25^2.
\tag{5}
\]

The chronological products (2) are

\[
M_A=\begin{pmatrix}49&10\\42&31\end{pmatrix},
\qquad
M_B=\begin{pmatrix}10&11\\14&46\end{pmatrix}.
\]

Both have determinant one, and (4) gives Hill values (44) and (7).

## 6. Constructing the congruence certificate

The producer does not hardcode the change of basis.  It first diagonalizes
each symmetric form by congruence over (mathbb F_{61}).  It then recursively
represents the target diagonal entries by the source form, restricts to the
orthogonal complement, and conjugates back to the original bases.

The resulting matrix is

\[
C=
\begin{pmatrix}
9&45&15&55&29\\
46&30&6&10&27\\
16&29&0&20&15\\
0&0&0&11&12\\
0&0&0&0&7
\end{pmatrix}.
\]

The checker independently verifies

\[
\det C=22,
\qquad
C^{\mathsf T}B_A C=B_B.
\tag{6}
\]

Equation (6), rather than a Legendre-symbol comparison alone, is the exact
certificate that the quadratic models are isometric.

## 7. Quadratic Fourier factor

Let (Q_B(y)=\frac12y^{\mathsf T}By).  Diagonalize
(B=P^{\mathsf T}\operatorname{diag}(b_1,\ldots,b_n)P).  Since a linear
change of variables permutes (k_r^n),

\[
\sum_y\psi_r(t(c+Q_B(y)))
=\psi_r(tc)
\prod_{j=1}^n
\sum_{u\in k_r}\psi_r\!\left(\frac{tb_j}{2}u^2\right).
\]

For (a\ne0),

\[
\sum_u\psi_r(au^2)=\chi_r(a)G(\chi_r,\psi_r).
\]

Multiplication yields

\[
\psi_r(tc)\chi_r(t)^n
\chi_r(\det B)\chi_r(2)^{-n}
G(\chi_r,\psi_r)^n.
\tag{7}
\]

The exact congruence (6) is stronger than equality of (7): it identifies the
quadratic polynomials themselves after change of variables, over every finite
extension of the base field.

## 8. From quadratic models to local sheaves

At a nondegenerate critical point in odd characteristic, the henselian Morse
lemma removes all terms of order at least three by a henselian coordinate
change.  Thus the local function germ is represented by (c+Q_B).  The local
vanishing-cycle object has rank one in its Morse degree; its Kummer/Gauss
character is controlled by the quadratic form.  Local Fourier transform maps
this quadratic character to the corresponding Gauss representation.

Therefore (6) and equality of the critical values imply an isomorphism of the
two local objects.  This conclusion is invariant under the common
Fourier--Deligne shift convention.

## 9. Why the conclusion is local

The global exponential sum

\[
E_{p,n}(r;t)=
\sum_{x\in\mathbb F_{p^r}^n}\psi_r(t\Phi_n(x))
\]

is not, without further hypotheses, the direct sum of the isolated Morse
factors alone.  Its Fourier description can also contain contribution from
infinity, and a family may carry nontrivial monodromy connecting critical
values.  Degenerate fibers require higher-jet data.  Hence the exact collision
kills only the proposal that each good-prime Morse-local factor intrinsically
recovers the full Hill value.

## 10. The next nonlocal invariant

For the deformation

\[
H_a(q,p_0)=(1-aq^2-p_0,q),
\qquad
S_a(q,Q)=qQ-q+\frac a3q^3,
\]

consider the critical-value discriminant obtained by eliminating the cyclic
critical equations together with

\[
\det D^2\Phi_{n,a}=0.
\]

By the Hill identity, this is precisely the parabolic locus
(det(I-DH_a^n)=0).  Monodromy around this discriminant is not determined by
the separate Morse germs and is therefore the next large intrinsic door.

