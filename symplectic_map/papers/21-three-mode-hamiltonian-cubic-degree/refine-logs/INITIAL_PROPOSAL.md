# Initial proposal — Paper 21

**Candidate title:** *Three-Mode Hamiltonian Shears in A6: Exact Degree Growth and Cubic Perron Subfamilies*

## Candidate

Study a three-mode polynomial Hamiltonian shear map over an algebraically closed
field (K) of characteristic zero.  For an integer (g\ge8), set

\[
 V=q_1^2q_2^2q_3^2+q_1^g,\qquad W=p_1^2p_2^2p_3^2+p_3^g,
\]
and (F=T\circ S), where (S(q,p)=(q,p+\nabla V(q))) and
(T(q,p)=(q+\nabla W(p),p)).  The proposed result is an exact algebraic-degree
formula obtained from a positive invariant cone and a finite-dimensional
exponent recurrence.

## Working claim

On the cone (U_1>0, U_2/U_1\ge1, U_3/U_1\ge1,
U_2/U_1+U_3/U_1<(g-3)/2), the leading exponent vectors evolve by
\[
 v_{n+1}=A_gu_n,\quad u_{n+1}=C_gu_n,
\]
with
\[
A_g=\begin{pmatrix}g-1&0&0\\2&1&2\\2&2&1\end{pmatrix},\quad
B_g=\begin{pmatrix}1&2&2\\2&1&2\\0&0&g-1\end{pmatrix},
\]
\[
C_g=B_gA_g=\begin{pmatrix}g+7&6&6\\2g+4&5&4\\2(g-1)&2(g-1)&g-1\end{pmatrix}.
\]
The exact degree is (e_3^T C_g^n\mathbf 1); the normalized degree converges
to (\rho(C_g)).  The row sums are (g+19,2g+13,5(g-1)), all strictly
below ((g-1)^2) for (g\ge8).

## Risks to resolve

Selector margins, cone invariance, old-term induction, and no-cancellation must
be written explicitly.  At (g=7), the seed ((x,y)=(1,1)) lies on the
strict-cone boundary while its S face gap is 1; it is a domain anti-example,
not a selector tie.  Any statement about generic
maps, entropy, periodic points, torus automorphisms, or positive characteristic
is outside scope.
