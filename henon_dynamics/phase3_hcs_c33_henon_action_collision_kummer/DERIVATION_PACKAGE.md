# HCS-C33 Phase-3 derivation package

## Target

Starting only from the chronological area-preserving Hénon family and its
cyclic generating action, prove that the generic degree-nine equal-action
collision has two distinct nonparabolic exact-period-five branches whose
symmetric Hill product defines a nontrivial Kummer class.

## Status

`PROVED_BY_EXACT_SYMBOLIC_CERTIFICATE`.

The producer derives the complete chain with exact rational arithmetic.  A
separate checker reconstructs the chronology, quotient-field node, Hill
identity, field norm, modular controls, and scope decision.  The released
certificate contains no floating-point theorem input.

## Invariant Object

The invariant object is not the known six-sheet normalization alone.  It is
the pair

\[
\left(
\text{singular action-image map }(A,q)\mapsto(A,c),
\ [h_1h_2]\in K_9^\times/K_9^{\times2}
\right),
\]

where \(h_i=\det(I-DH_A^5)\) are evaluated on the two normalization points
above the generic action node.  Branch exchange fixes the product, and a
common Hill normalization changes it by a square.

## Assumptions

1. The base field has characteristic zero.
2. The map is
   \(H_A(q,p)=(1-Aq^2-p,q)\) with derivative chronology later-on-left.
3. The reversor-line initial state is \((x_0,x_{-1})=(q,q)\).
4. The action is
   \(
   \Phi_{5,A}=\sum_{i\bmod5}
   (x_ix_{i+1}-x_i+A x_i^3/3).
   \)
5. Polynomial normalizations are the canonical primitive integral
   normalizations serialized by the certificate.
6. “Nonparabolic” means that the return matrix has neither eigenvalue
   \(+1\) nor eigenvalue \(-1\).

## Notation

- \(G_A(q)\): fixed-factor-removed period-five marker.
- \(R(A,q)\): remainder of \(3A^2\Phi_{5,A}\) modulo \(G_A\).
- \(W_5(A,c)\): primitive action-image resultant.
- \(P_2,P_5\): ramification factors already present in the normalization.
- \(P_9\): the coprime degree-nine equal-action collision factor.
- \(K_9=\mathbb Q[A]/(P_9)\).
- \(c_0\): the repeated action value over \(K_9\).
- \(g_2(q)=q^2+bq+d\): the two-point normalization fiber.
- \(M=D_4D_3D_2D_1D_0\): chronological period-five derivative.
- \(h(q)=\det(I-M)\): Hill value.
- \(N_H=N_{K_9[q]/(g_2)/K_9}(h)=h_1h_2\).

## Derivation Strategy

The derivation has four logically separate layers.

1. Reconstruct the old normalization and new action embedding from the map.
2. Work over the collision field and prove an actual two-branch node rather
   than infer one from a squared discriminant factor.
3. reconstruct the return stability and exclude both \(+1\) and \(-1\)
   multipliers.
4. descend the symmetric Hill product and disprove its being a square by an
   exact rational norm.

The modular prime rows and the \(S_9\) calculation are controls and
arithmetic context.  They do not replace the characteristic-zero node and
norm proof.

## Derivation Map

\[
\begin{array}{c}
H_A\text{ chronology}
\longrightarrow G_A(q)
\longrightarrow R(A,q),W_5(A,c)\\[2mm]
\longrightarrow
\operatorname{Disc}_cW_5
=2^{12}3^{30}A^{60}P_2^5P_5^3P_9^2\\[2mm]
\longrightarrow
K_9, c_0, g_2(q)
\longrightarrow
\text{two-point transverse node}\\[2mm]
\longrightarrow
h=\det(I-DH_A^5)=\det D^2\Phi_{5,A}\\[2mm]
\longrightarrow
N_H=N(h)=h_1h_2
\longrightarrow
N_{K_9/\mathbb Q}(N_H)\notin\mathbb Q^{\times2}.
\end{array}
\]

## Main Derivation

### 1. Chronological marker

Iterate

\[
x_{i+1}=1-Ax_i^2-x_{i-1},
\qquad x_{-1}=x_0=q.
\]

The gcd of \(x_5-q\) and \(x_4-q\) over \(\mathbb Q(A)[q]\) contains the
fixed-point factor

\[
F_A(q)=Aq^2+2q-1.
\]

After removing \(F_A\) and primitive-scaling, the remaining sextic is

\[
\begin{aligned}
G_A(q)={}&A^6q^6+2A^5q^5+(-3A^5+2A^4)q^4\\
&+(-4A^4+2A^3)q^3+(3A^4-4A^3+A^2)q^2\\
&+(2A^3-2A^2)q-A^3+2A^2-A-1.
\end{aligned}
\]

Exact reduction gives \(x_4-q\equiv x_5-q\equiv0\pmod{G_A}\), while

\[
\operatorname{Res}_q(G_A,F_A)=A^6P_2,
\qquad
\operatorname{Disc}_qG_A=2^6A^{30}P_2P_5.
\]

Since five is prime, any point fixed by \(H_A^5\) has period one or five.
Away from \(AP_2P_5=0\), removal of \(F_A\) therefore selects six distinct
exact-period-five marker points.

### 2. Action reduction and birationality

Differentiating the cyclic action with respect to \(x_i\) gives

\[
\partial_{x_i}\Phi_{5,A}
=x_{i-1}+x_{i+1}-1+Ax_i^2.
\]

Thus its critical equations are exactly the chronological recurrence.
Reducing \(3A^2\Phi_{5,A}\) modulo \(G_A\) gives

\[
\begin{aligned}
R={}&2A^5q^5+2A^5q^4+2A^4q^4-4A^4q^2
-2A^3q^3+6A^3q^2\\
&-2A^3q+2A^3-A^2q^2+4A^2q-8A^2+2A+2.
\end{aligned}
\]

Eliminating \(q\) yields

\[
W_5(A,c)=A^{-30}\operatorname{Res}_q(G_A,3A^2c-R).
\]

The full coefficient ledger is stored canonically in the certificate.
Specializing at \(A=6\) preserves degree six for both \(G_A(q)\) and
\(W_5(A,c)\).  Modulo \(37\), their coefficient rows from highest to
lowest degree are respectively

\[
(36,12,21,21,26,27,34),
\qquad
(26,34,7,16,19,8,4).
\]

Exact finite-field factorization gives the single factor-degree profile
\((6)\) in each case.  Equivalently, the Rabin tests for the prime
divisors \(2,3\mid6\) have trivial proper gcds and
\(x^{37^6}-x\) vanishes modulo each sextic.  Degree-preserving
irreducible specialization and Gauss's lemma therefore prove that both
generic sextics are irreducible over \(\mathbb Q(A)\).

A linear last nonzero subresultant

\[
U(A,c)q+V(A,c)
\]

has \(U\) coprime to \(W_5\) over \(\mathbb Q(A)\).  Hence
\(q=-V/U\) generically and

\[
\mathbb Q(A,q)=\mathbb Q(A,c).
\]

This proves that the action curve is a singular plane model of the known
normalization, not a new degree-six cover.

### 3. Collision factor and its parameter Galois group

Exact discriminant factorization gives

\[
\operatorname{Disc}_cW_5
=2^{12}3^{30}A^{60}P_2^5P_5^3P_9^2,
\]

with \(P_9\) as printed in `THEOREM_PACKAGE.md`.  Direct gcds prove
\(P_9\) squarefree and coprime to \(AP_2P_5\).

The modular factor degrees are

\[
\begin{array}{c|c}
p&\text{degrees}\ \\ \hline
7&(9)\\
17&(5,2,1,1)\\
23&(8,1).
\end{array}
\]

The first row makes \(P_9\) irreducible.  An 8-cycle with one fixed point
makes the point stabilizer transitive on the other eight letters.  Hence the
transitive group is 2-transitive and primitive.  Squaring an element of type
\((5,2,1,1)\) gives a pure 5-cycle.  Jordan's theorem gives \(A_9\), and an
8-cycle is odd, proving the group is \(S_9\).

### 4. Two-point fiber

In \(K_9[c]\), the exact gcd

\[
\gcd(W_5,(W_5)_c)=c-c_0
\]

has degree one.  Substitution into the normalization equations gives

\[
g_2(q)=\gcd(G_A,3A^2c_0-R)=q^2+bq+d.
\]

The certificate verifies

\[
b^2-4d\ne0,
\qquad
\gcd(g_2,G_A/g_2)=1.
\]

Therefore the repeated action value has exactly two distinct reduced points
in the normalization fiber.

### 5. Plane-node and normalization-tangent gates

Quotient-field evaluation gives

\[
W_5=(W_5)_A=(W_5)_c=0,
\]

\[
(W_5)_{cc}\ne0,
\qquad
(W_5)_{Ac}^2-(W_5)_{AA}(W_5)_{cc}\ne0.
\]

Thus the first nonzero homogeneous term is a nondegenerate quadratic with
two distinct tangent lines over \(\overline K_9\).

The normalization gives a second, branch-resolved proof.  Along \(G=0\),

\[
\frac{dq}{dA}=-\frac{\partial_A G}{\partial_q G},
\qquad c=\frac{R}{3A^2},
\]

so

\[
s(q)=\frac{(A\partial_AR-2R)\partial_qG
-A(\partial_qR)\partial_AG}
{3A^3\partial_qG}.
\]

The denominator is invertible modulo \(g_2\).  Writing
\(s(q)\equiv uq+v\pmod{g_2}\), exact quotient arithmetic gives

\[
u^2(b^2-4d)\ne0.
\]

The two normalization points therefore map to the two distinct tangents.

### 6. Hill determinant and the two multiplier tests

The derivative at the \(i\)-th chronological point is

\[
D_i=\begin{pmatrix}-2Ax_i&-1\\1&0\end{pmatrix},
\qquad \det D_i=1.
\]

The return derivative is later-on-left,

\[
M=D_4D_3D_2D_1D_0,
\]

and \(h=\det(I-M)=2-\operatorname{tr}M\).  Direct determinant expansion of
the cyclic action Hessian gives

\[
\det D^2\Phi_{5,A}=h
\quad\text{modulo }G_A.
\]

The \(+1\)-multiplier resultant is

\[
\operatorname{Res}_q(G_A,h)=-2^6A^{30}P_2^5P_5,
\]

which is coprime to \(P_9\).  This proves Morse nondegeneracy but does not by
itself exclude \(-1\).  Since \(\det M=1\),

\[
\det(I+M)=2+\operatorname{tr}M=4-h.
\]

The separate resultant is

\[
\operatorname{Res}_q(G_A,4-h)=-2^6A^{30}B_6B_9,
\]

and both \(B_6,B_9\) are coprime to \(P_9\).  Hence neither branch has
multiplier \(+1\) or \(-1\).

### 7. Symmetric Hill norm

In the quadratic étale algebra \(E=K_9[q]/(g_2)\), let \(\bar q\) denote
the class of \(q\) and let \(\sigma\) be the exchange involution.  Reduce
the Hill polynomial as

\[
h=h_A(\bar q)=\ell\bar q+m.
\]

Using \(q_1+q_2=-b\) and \(q_1q_2=d\),

\[
N_H=h\sigma(h)=h(q_1)h(q_2)=\ell^2d-\ell mb+m^2.
\]

This element lies in \(K_9\) and is fixed by branch exchange.  Moreover

\[
\frac{h/\sigma(h)}{h\sigma(h)}=\sigma(h)^{-2},
\]

so \([h/\sigma(h)]=[h\sigma(h)]\) in \(E^\times/E^{\times2}\).  After
passing to a splitting field this becomes
\([h_1/h_2]=[h_1h_2]\).

### 8. Nonsquare proof

The quotient calculation yields

\[
N_H=-\frac4{4827099043}Q_8(A)
\quad\text{in }K_9,
\]

for the degree-eight polynomial serialized in the certificate.  Because
\(P_9\) has leading coefficient \(110592\), the norm formula includes the
nonmonic correction

\[
N_{K_9/\mathbb Q}(N_H)
=\left(-\frac4{4827099043}\right)^9
\frac{\operatorname{Res}(P_9,Q_8)}{110592^8}.
\]

Exact simplification gives

\[
N_{K_9/\mathbb Q}(N_H)
=\frac{2^6\,13\,19^5\,41\,59^5\,5653^2}{3^5}.
\]

The rational number is not a square.  If \(N_H\) were a square in \(K_9\),
its field norm would be a square in \(\mathbb Q\).  Contradiction.

### 9. Gauge descent

For a closed orbit, a cyclic coboundary telescopes to zero.  Adding
\(\beta(A)\) to the action translates \(c\), while multiplying by a nonzero
\(\mu(A)\) rescales the target coordinate.  These are local automorphisms of
the action image away from zeros and poles and do not change the return
matrices.  A common Hill scaling \(h_i\mapsto\nu h_i\), with
\(\nu\in K_9^\times\), changes \(N_H\) by \(\nu^2\).  Thus the square class
is invariant under all declared gauges.

## Remarks

1. The squared appearance of \(P_9\) in the action discriminant is expected
   for a two-branch equal-critical-value collision.  The node proof uses
   the quotient fiber and tangent calculations, not this exponent alone.
2. The \(S_9\) theorem describes the parameter collision polynomial.  It
   does not prove independence of all conjugate Kummer classes.
3. The four finite primes dividing \(P_9(6)\) provide regression and
   adversarial controls.  The proof of nontriviality is the characteristic-
   zero field norm.

## Boundaries

- Period five only.
- Characteristic zero is primary; finite fields are controls.
- No real-minimum statement is made, so “Maxwell” is used only in the
  Lyashko--Looijenga equal-critical-value sense.
- No full wreath product, Picard--Lefschetz action, all-period zeta, global
  analytic continuation, or Hilbert--Pólya operator is constructed.
- The period-five normalization and generic mechanisms are prior art.

## Risks

1. A CAS producer and CAS checker can share implementation-level failure
   modes even when they share no code.  The hand derivation and exact
   mutation suite reduce but do not eliminate that risk.
2. Search-bounded novelty is not a proof of historical priority.  The paper
   claims an exact coupled result, not “the first” such object.
3. A single nonsquare class does not establish a rank-nine Kummer module or
   a full semidirect-product Galois group.
4. No compatibility across periods has been proved, which is the main
   obstruction to any dynamical-zeta promotion.
