# Proof package

## Definitions and gradients

\[
\nabla V=(2q_1q_2^2q_3^2+gq_1^{g-1},\;2q_1^2q_2q_3^2,\;2q_1^2q_2^2q_3),
\]
\[
\nabla W=(2p_1p_2^2p_3^2,\;2p_1^2p_2p_3^2,\;2p_1^2p_2^2p_3+gp_3^{g-1}).
\]
The maps (S(q,p)=(q,p+\nabla V(q))), (T(q,p)=(q+\nabla W(p),p))
are polynomial automorphisms with inverses obtained by subtraction.  Their
Jacobian blocks are triangular symplectic shears; the block-matrix
calculation (J^T\Omega J=\Omega) uses the Hessian symmetry.  The composition
is therefore an explicit canonical polynomial symplectic map (not every
affine-triangular map is canonical).

The complete support rows (column order ((q_1,q_2,q_3,p_1,p_2,p_3))) are
\[
\begin{array}{c|c}
\partial_{q_1}V&(1,2,2,0,0,0),\ (g-1,0,0,0,0,0)\\
\partial_{q_2}V&(2,1,2,0,0,0)\\
\partial_{q_3}V&(2,2,1,0,0,0)\\
\partial_{p_1}W&(0,0,0,1,2,2)\\
\partial_{p_2}W&(0,0,0,2,1,2)\\
\partial_{p_3}W&(0,0,0,2,2,1),\ (0,0,0,0,0,g-1).
\end{array}
\]

## Selector inequalities

Write (x=U_2/U_1), (y=U_3/U_1), with (x,y\ge1) and
\(x+y<(g-3)/2\).  Comparison on the two relevant pure-versus-mixed faces
gives the exact margins
\[
M_S=(g-2)-2x-2y,
\quad M_T=(2g-6)x+(g-6)y-6.
\]
Both are positive for (g\ge8) on the open cone; the cone itself uses the
stricter height margin (R=(g-3)/2).  The second gap is the corrected
selector expression.  At (g=7) the seed reaches the strict-cone boundary, so
the propagation proof is not claimed there; this is not a selector tie.

## Recurrence and cone invariance

The selected leading exponents are
\[
A_g=\begin{pmatrix}g-1&0&0\\2&1&2\\2&2&1\end{pmatrix},\quad
B_g=\begin{pmatrix}1&2&2\\2&1&2\\0&0&g-1\end{pmatrix},\quad
C_g=B_gA_g=\begin{pmatrix}g+7&6&6\\2g+4&5&4\\2(g-1)&2(g-1)&g-1\end{pmatrix}.
\]
For (U'=C_gU), direct substitution with (x=U_2/U_1,y=U_3/U_1) and
(D=g+7+6x+6y) gives the exact normalized tests
(X'-1=(g-3-x-2y)/D),
(Y'-1=[g-9+(2g-8)x+(g-7)y]/D), and (H=U_1Q/2) with
(Q=g^2+2gx+4gy-4g-24x-24y-25).  For (8\le g\le11),
(Q>2g^2-17g+11\ge3); for (g\ge12), (Q\ge g^2+2g-73>0).
Explicitly, for (U=(a,b,c)^T),
\[
U'_2-U'_1=(g-3)a-b-2c,\qquad
U'_3-U'_1=(g-9)a+(2g-8)b+(g-7)c,
\]
and
\[
H_2(U')=(g-3)U'_1-2U'_2-2U'_3=U_1Q,
\quad H(U')=R U'_1-U'_2-U'_3=H_2(U')/2=U_1Q/2.
\]
The displayed normalized bounds are the complete height proof; no second
coefficient argument is required.

## Support semiring and no cancellation

The support sets are finite subsets of \(\mathbb N^6\), ordered as
\((q_1,q_2,q_3,p_1,p_2,p_3)\), and composition uses Minkowski addition.  The
rigorous phase/carry induction below identifies the unique selected term; the
semiring lemma then proves its positive coefficient cannot cancel in
characteristic zero.  No claim that arbitrary old face hyperplanes are
preserved by nonnegative matrices is used.

## Visibility and exact degree

The explicit difference is
\[
C_g-A_g=\begin{pmatrix}8&6&6\\2g+2&4&2\\2g-4&2g-4&g-2\end{pmatrix}.
\]
Its positive entries show (q_j>p_j) for each (j).  Direct comparison gives
\[
U_3-U_2=[-6+(2g-7)x+(g-5)y]U_1>0,
\quad U_3-U_1=[g-9+(2g-8)x+(g-7)y]U_1>0.
\]
Thus (q_3) is the largest of all six coordinate degrees.  With
(u_{n+1}=C_gu_n) and (v_{n+1}=A_gu_n),
\[
\deg(F_g^n)=e_3^T C_g^n\mathbf 1\quad(n\ge0).
\]
for the fixed initial seed.  Perron–Frobenius applied to the positive power of
\(C_g\) gives the root limit \(\lambda_1=\rho(C_g)\).  The row sums are
\(g+19,2g+13,5(g-1)\), all strictly below \((g-1)^2\) for (g\ge8);
hence \(\rho(C_g)<(g-1)^2\).

## Algebraic checks

The characteristic polynomial of (C_g) is to be displayed and expanded in
the manuscript; in the variable (t) its exact form is
\[
\chi_{C_g}(t)=t^3-(2g+11)t^2+(g^2-16g+19)t-9(g-1)^2.
\]
Reduction modulo 5 is irreducible for
\(g\equiv2,3,4\pmod5\); Gauss's lemma therefore gives irreducibility in
\(\mathbb Q[t]\) and degree-exactly-three Perron roots for every such (g\ge8).
This is an algebraic corollary, not a dynamical genericity claim.  The value
\(g=7\) is a domain-boundary anti-example, not a selector tie.

At (g=7), the seed ((x,y)=(1,1)) lies on the boundary
\(x+y=(g-3)/2\), while its S face gap is
\(M_S=(g-2)-2x-2y=1).  This is why (g=7) is excluded from the strict
cone proof rather than treated by continuity.

## Coordinate-level substitution ledger

For (Q_i) denoting the three coordinates after the first shear, and (P_i)
the three coordinates after the second shear, the substitution is
\[
\begin{aligned}
Q_1&=q_1,&Q_2&=q_2,&Q_3&=q_3,\\
P_1&=p_1+2q_1q_2^2q_3^2+gq_1^{g-1},&
P_2&=p_2+2q_1^2q_2q_3^2,&
P_3&=p_3+2q_1^2q_2^2q_3.
\end{aligned}
\]
The output coordinates are
\[
\begin{aligned}
q'_1&=q_1+2P_1P_2^2P_3^2,\\
q'_2&=q_2+2P_1^2P_2P_3^2,\\
q'_3&=q_3+2P_1^2P_2^2P_3+gP_3^{g-1},\\
p'_i&=P_i.
\end{aligned}
\]
These six equations are the complete coordinate definition used in every
induction step.  The inverse is equally explicit: first subtract the three
(W)-gradient terms from (q'), then subtract the three (V)-gradient terms
from (p').  No birational inverse, denominator, or analytic continuation is
used.

## Six-by-six Jacobian and symplectic check

With (H_V=\nabla^2V(q)) and (H_W=\nabla^2W(P)), where
(P=p+\nabla V(q)) is the intermediate p-coordinate after S, the Jacobians are
\[
J_S=\begin{pmatrix}I_3&0\\H_V&I_3\end{pmatrix},\qquad
J_T=\begin{pmatrix}I_3&H_W\\0&I_3\end{pmatrix}.
\]
Writing Ω=\begin{pmatrix}0&I_3\\-I_3&0\end{pmatrix}, symmetry of the
Hessians gives (J_S^TΩJ_S=Ω) and (J_T^TΩJ_T=Ω).  Hence
\(J_F=J_TJ_S\) is symplectic at every point.  This is the precise meaning of
canonical in this paper; an affine-triangular polynomial automorphism need not
have symmetric Hessian blocks and is not silently included.

## Carry table and support semiring

Every displayed gradient row has coefficient (2) or (g), hence lies in the
positive subsemiring ℕ.  In the ordered basis
\((q_1,q_2,q_3,p_1,p_2,p_3)\), the gradient rows (V_i update p_i; W_i update q_i) are
\[
\begin{array}{c|c|c}
\text{source}&\text{target coordinate}&\text{row(s)}\\ \hline
V_1&p_1&(1,2,2,0,0,0), (g-1,0,0,0,0,0)\\
V_2&p_2&(2,1,2,0,0,0)\\
V_3&p_3&(2,2,1,0,0,0)\\
W_1&q_1&(0,0,0,1,2,2)\\
W_2&q_2&(0,0,0,2,1,2)\\
W_3&q_3&(0,0,0,2,2,1), (0,0,0,0,0,g-1).
\end{array}
\]
Products of monomials add rows, and sums take their union.  Consequently each
support is a finite subset of ℕ⁶ and composition is described by Minkowski
addition.  This table is also the audit trail for every entry of (A_g) and
(B_g); no omitted monomial is used in the proof.

## Selector derivation

For a positive weight vector (U), divide all candidate weights by (U_1),
put (x=U_2/U_1), (y=U_3/U_1), and compare the pure and mixed rows.  The
pure (q_1^g) versus mixed (q_1q_2^2q_3^2) face gives
\[
M_S=(g-2)-2x-2y.
\]
The pure (p_3^g) versus mixed (p_1^2p_2^2p_3) face gives
\[
M_T=(2g-6)x+(g-6)y-6.
\]
On (x,y\ge1) and (x+y<R=(g-3)/2), both are strict for (g\ge8).  The
constant (R) is deliberately one unit stricter than the natural first face;
this slack is consumed by the carry inequalities.  There is no third
independent face gap: the two displayed forms are the complete selector ledger.

## Cone algebra in full

For (U'=C_gU), let (x=U_2/U_1,y=U_3/U_1),
(D=g+7+6x+6y), and (R=(g-3)/2).  Then
\[
X'-1=\frac{g-3-x-2y}{D},\quad
Y'-1=\frac{g-9+(2g-8)x+(g-7)y}{D}.
\]
With (H_2=(g-3)U'_1-2U'_2-2U'_3=U_1Q) and
(H=H_2/2=RU'_1-U'_2-U'_3),
\[
Q=g^2+2gx+4gy-4g-24x-24y-25.
\]
For (8\le g\le11), (x<R-y,y\ge1) gives
(Q>2g^2-17g+11\ge3).  For (g\ge12), (x,y\ge1) gives
(Q\ge g^2+2g-73>0).  This is the complete two-case cone proof.

## Base case and old-term induction

At (n=0), set (u_0=p_0=\mathbf1).  The S face selects
(v_1=A_gu_0), and (A_g\mathbf1>\mathbf1), so selected gradient terms
strictly dominate carried p-terms.  For (n\ge1), assume
(p_n=A_gu_{n-1}).  Since ((C_g-I)u_{n-1}>0),
(A_gu_n>A_gu_{n-1}=p_n), and the S selector remains strict.  The T face
then selects (u_{n+1}=C_gu_n); ((C_g-I)u_n>0) makes this strictly larger
than carried q-terms.  The two face gaps (M_S,M_T) separately rule out old
pure/mixed ties.  This phase-labelled induction proves
(v_{n+1}=A_gu_n, u_{n+1}=C_gu_n) and never invokes an automatic preservation
of arbitrary old face hyperplanes.

## No-cancellation lemma

Lemma (positive support).  Let (R=ℕ[z_1,…,z_6]).  If a polynomial is written
as a finite sum of distinct monomials with positive coefficients, then replacing
each variable by a polynomial in (R) preserves positivity of every selected
Minkowski-sum coefficient.  Proof: distributivity expands a coefficient as a
finite sum of products of positive integers.  In characteristic zero its image
in (K) is nonzero.  Applying this lemma at every induction step proves that
the selected support coefficient cannot cancel.  The lemma is intentionally
not asserted in positive characteristic.

## Degree and Perron limit

The visibility matrix (C_g-A_g) is entrywise positive for (g\ge8), while
the (e_3) row is visible in the (p_3^g) carry.  The cone inequalities give
(U_3>U_2) and (U_3>U_1).  Therefore the third coordinate realizes the
maximum at every full step and the exact identity is
\[
\deg(F_g^n)=e_3^TC_g^n\mathbf1\quad(n\ge0).
\]
Since (C_g) is primitive, Perron–Frobenius gives
\(\lim_{n\to\infty}\deg(F_g^n)^{1/n}=\rho(C_g)\).  Its row sums are

\[
r_1=g+19,\qquad r_2=2g+13,\qquad r_3=5(g-1).
\]
For (g\ge8), each is strictly less than ((g-1)^2), so
\(\rho(C_g)<(g-1)^2\).

## Characteristic polynomial and mod-five audit

Expanding \det(tI-C_g) along the first row and collecting powers of (g)
gives
\[
\chi_g(t)=t^3-(2g+11)t^2+(g^2-16g+19)t-9(g-1)^2.
\]
For (g\equiv2,3,4\pmod5), reduction has no root in \mathbb F_5: the five
evaluations at (t=0,1,2,3,4) are respectively nonzero (the residue classes
are checked separately in the manuscript's small table).  A cubic with no
linear factor is irreducible over \mathbb F_5.  This is a matrix-algebra
corollary only; it does not assert irreducibility over (K) or generic
dynamical behavior.

The promised no-root table is
\[
\begin{array}{c|ccccc}
g\bmod5\backslash t&0&1&2&3&4\\ \hline
2&1&3&1&1&4\\
3&4&3&4&3&1\\
4&4&2&3&3&3
\end{array}
\]
where entries are residues in \mathbb F_5.  The table is obtained by direct
substitution into the displayed \chi_g(t), so it is auditable without a CAS.

## Degree induction in coordinate language

For every (n\ge0), (u_n) denotes q-weights before S and
(v_{n+1}) denotes the intermediate p-weights after S.  The S phase gives
(v_{n+1}=A_gu_n).  T leaves these p-weights unchanged and updates q-weights
(u_{n+1}=B_gv_{n+1}=C_gu_n).  With (u_0=p_0=\mathbf1), the strict phase
induction proves these identities and the visibility argument gives

\[
\deg(F_g^n)=e_3^TC_g^n\mathbf1,\qquad n\ge0,
\]

where (n=0) is the harmless initial tie.  This is a single-row equality, not
a maximum over an unproved collection of coordinates.

## Strictness bookkeeping

There are three distinct strictness sources: the S face gap, the T face gap,
and the height cone inequality.  The first two select monomials; the third
propagates their strict ordering.  At no point may one infer a selector from a
row-sum estimate.  Conversely, the row-sum estimate is used only after exact
degree has been proved, to bound ρ.  This separation is recorded so that a
future referee can localize a failure to selection, propagation, or growth.

## Canonical terminology note

The word “Hamiltonian” refers only to the displayed polynomial potentials and
their exact gradients.  “Canonical” refers to preservation of the standard
symplectic form by the six-by-six Jacobian.  “Affine-triangular” refers to the
broader literature class and allows maps that are not gradient shears.  Paper
21 proves no inclusion or classification theorem relating the two classes.

## Referee-facing proof checklist

The manuscript proof is accepted only when the following implications appear in
this order.  First, the inverse formulas establish that the map is an
automorphism before any degree is discussed.  Second, the Jacobian calculation
establishes canonicity independently of the support calculation.  Third, the
carry table is converted to (A_g) and (B_g) by writing the row additions,
not by pattern recognition.  Fourth, the two selector gaps are checked on the
strict cone.  Fifth, the cone image is checked by three linear forms.  Sixth,
the old-term induction and semiring lemma establish support uniqueness and
non-cancellation.  Only then may the visibility identity be called an exact
degree formula.  Finally PF and row sums give the limit and strict upper bound.

This order prevents circular reasoning: row sums cannot prove selectors;
selectors cannot replace the semiring lemma; and a PF limit cannot upgrade an
unproved degree upper bound to equality.

## Carry-to-matrix derivation

The first shear sends a weight (U) to
\[
((g-1)U_1,\;2U_1+U_2+2U_3,\;2U_1+2U_2+U_3)^T=A_gU.
\]
The second shear sends a weight (V) to
\[
(V_1+2V_2+2V_3,\;2V_1+V_2+2V_3,\;(g-1)V_3)^T=B_gV.
\]
Substitution (V=A_gU) gives (C_gU) with rows
\[
((g+7)U_1+6U_2+6U_3,
(2g+4)U_1+5U_2+4U_3,
2(g-1)U_1+2(g-1)U_2+(g-1)U_3).
\]
This line-by-line calculation is the bridge between the six support rows and
the Perron matrix, and is included to make transcription errors detectable.

## Limits of the algebraic corollary

The mod-five table proves irreducibility of the characteristic polynomial after
reduction for the listed residue classes.  It does not prove that the Perron
root is a unit, a Salem number, or a degree invariant under conjugacy.  It also
does not imply a classification of all cubic Perron numbers.  The only use in
Paper 21 is to record an exact, checkable algebraic feature of this displayed
matrix family.

## Authoritative phase induction and exact cone ledger

The phase induction is fixed as follows.  Set (u_0=p_0=\mathbf1).  After
the S face, (p_n=A_gu_{n-1}) for (n\ge1); since
((C_g-I)u_{n-1}>0), one has (A_gu_n>A_gu_{n-1}=p_n).  Thus the S-selected
gradient terms strictly dominate carried (p)-terms.  After the T face,
(u_n) is sent to (u_{n+1}=C_gu_n); the strict inequality
((C_g-I)u_n>0) similarly dominates carried (q)-terms.  Therefore, for all
(n\ge0),
\[
v_{n+1}=A_gu_n,\qquad u_{n+1}=C_gu_n.
\]
This is a phase-labelled induction; no assertion that a nonnegative matrix
automatically preserves every old face hyperplane is used.

For (x=U_2/U_1,y=U_3/U_1), put
(D=g+7+6x+6y).  The exact ratio margins are
\[
X'-1=\frac{g-3-x-2y}{D}>0,qquad
Y'-1=\frac{g-9+(2g-8)x+(g-7)y}{D}>0.
\]
The height form is (H=U_1Q/2), where
\[
Q=g^2+2gx+4gy-4g-24x-24y-25.
\]
For (8\le g\le11), (x<R-y), (y\ge1) gives
(Q>2g^2-17g+11\ge3).  For (g\ge12), (x,y\ge1) gives
(Q\ge g^2+2g-73>0).  These are the complete two-case bounds.

Visibility is explicit:
\[
U_3-U_2=[-6+(2g-7)x+(g-5)y]U_1>0,
\quad U_3-U_1=[g-9+(2g-8)x+(g-7)y]U_1>0.
\]
The matrix (C_g-A_g>0) proves each (q_j) degree exceeds its corresponding
(p_j) degree; together with (q_3) being the largest q-coordinate, all six
coordinates are bounded by (q_3).  Hence, for every (n\ge0) (with the
harmless (n=0) tie),
\[
\deg(F_g^n)=e_3^TC_g^n\mathbf1\quad(n\ge0).
\]

The eight gradient monomial coefficients, in order
(V_1)-mixed, (V_1)-pure, (V_2,V_3,W_1,W_2,W_3)-mixed,
(W_3)-pure, are

\[
(2,g,2,2,2,2,2,g),
\]

and they occupy six derivative rows.  (V_i) gradients update (p_i), while
(W_i) gradients update (q_i); these are gradient rows, not carry rows.

Finally, for (g\equiv2,3,4\pmod5), the explicit no-root table and Gauss's
lemma imply \(\chi_g(t)\) is irreducible in \(\mathbb Q[t]\) for every such
\(g\ge8\).  Therefore \(\rho(C_g)\) is a degree-exactly-three algebraic
integer and Perron number in these infinite subfamilies.  This is the sole
meaning of “cubic Perron” in the title and does not assert irreducibility over
the ambient field (K).

## Boundary audit

At (g=7), (R=2) and the seed (x,y)=(1,1) lies on the boundary of the strict
cone x+y<(g-3)/2.  Its actual S face gap is
(M_S=(g-2)-2x-2y=1); no selector tie is asserted.  The proof domain starts
at (g>=8) because the strict cone is then available at the required seed and
the carry inequalities close.  We record (g=7) only as a domain-boundary
anti-example, not as an omitted special case.
