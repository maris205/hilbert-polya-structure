# HCS-C33 Phase-3 theorem package

All statements use exact arithmetic.  The generic point of \(P_9=0\) means
its generic scheme point, whose residue number field is
\(K_9=\mathbb Q[A]/(P_9)\).

## Theorem 1: chronological action image

For

\[
H_A(q,p)=(1-Aq^2-p,q)
\]

with diagonal initial state, the fixed-factor-removed period-five marker is
a primitive sextic \(G_A(q)\).  The cyclic action

\[
\Phi_{5,A}=\sum_{i\bmod5}
\left(x_ix_{i+1}-x_i+\frac A3x_i^3\right)
\]

has Euler--Lagrange equations equal to the chronological Hénon recurrence.
Eliminating \(q\) produces a primitive degree-six plane curve
\(W_5(A,c)=0\), birational to \(G_A=0\).  Its discriminant satisfies

\[
\operatorname{Disc}_cW_5
=2^{12}3^{30}A^{60}P_2^5P_5^3P_9^2,
\]

where

\[
P_2=16A^2-28A-19,
\]

\[
P_5=16A^5-108A^4+105A^3+27A^2-97A-47,
\]

and

\[
\begin{aligned}
P_9={}&110592A^9-294912A^8+159744A^7+225792A^6\\
&-162816A^5-51520A^4+50672A^3+736A^2-6032A+1037.
\end{aligned}
\]

Moreover \(P_9\) is squarefree and coprime to \(AP_2P_5\).

The birational statement includes an exact irreducibility gate.  At
\(A=6\), both degree-six specializations remain degree six and are
irreducible modulo \(37\).  Gauss specialization therefore makes
\(G_A(q)\) and \(W_5(A,c)\) irreducible over \(\mathbb Q(A)\).  A linear
last nonzero subresultant \(U(A,c)q+V(A,c)\), with \(U\) coprime to
\(W_5\), then gives \(q=-V/U\) generically and proves

\[
\mathbb Q(A,q)=\mathbb Q(A,c).
\]

## Theorem 2: the generic \(P_9\) point is a two-branch ordinary node

Over \(K_9\), the repeated action value is unique and the normalization
fiber is cut out by a separable quadratic

\[
g_2(q)=q^2+bq+d.
\]

It is coprime to the remaining degree-four quotient of \(G_A\).  At the
corresponding point \((A,c_0)\),

\[
W_5=(W_5)_A=(W_5)_c=0,
\qquad (W_5)_{cc}\ne0,
\]

and

\[
(W_5)_{Ac}^2-(W_5)_{AA}(W_5)_{cc}\ne0.
\]

The two normalization slopes are also distinct: if
\(s(q)\equiv uq+v\pmod{g_2}\), then

\[
(s(q_1)-s(q_2))^2=u^2(b^2-4d)\ne0.
\]

Thus the action image has an ordinary transverse plane-curve node formed by
two distinct normalization points.

## Theorem 3: exact period and both multiplier gates

The two generic points above have least period five.  Their chronological
return matrices have neither multiplier \(+1\) nor multiplier \(-1\).

More precisely, with \(h_A(q)=\det(I-DH_A^5)\),

\[
\operatorname{Res}_q(G_A,h_A)
=-2^6A^{30}P_2^5P_5.
\]

The cyclic action Hessian satisfies

\[
\det D^2\Phi_{5,A}=h_A
\quad\text{on }G_A=0,
\]

so the action critical points are Morse.  Since \(\det DH_A^5=1\),

\[
\det(I+DH_A^5)=4-h_A.
\]

The second exact resultant is

\[
\operatorname{Res}_q(G_A,4-h_A)
=-2^6A^{30}B_6B_9,
\]

where

\[
\begin{aligned}
B_6={}&4096A^6-13312A^5+512A^4+17344A^3\\
&-7520A^2-16276A-3251,
\end{aligned}
\]

\[
\begin{aligned}
B_9={}&4096A^9-50176A^8+206336A^7-299584A^6\\
&-75552A^5+396684A^4+126657A^3\\
&-257337A^2-204849A-48843.
\end{aligned}
\]

Both \(B_6\) and \(B_9\) are coprime to \(P_9\).

## Theorem 4: nontrivial descended Hill--Kummer class

Let \(E=K_9[q]/(g_2)\), let \(\bar q\) be the class of \(q\), and let
\(\sigma\) be the exchange involution of this quadratic étale algebra.  Put
\(h=h_A(\bar q)\in E^\times\).  Its norm descends:

\[
N_H=h\sigma(h)=N_{E/K_9}(h)\in K_9^\times.
\]

It is fixed by branch exchange, and the square-class identity

\[
[h/\sigma(h)]=[h\sigma(h)]
\quad\text{in }E^\times/E^{\times2}
\]

holds.  Over a splitting field these are the classes
\([h_1/h_2]=[h_1h_2]\).  The descended representative \(N_H\) lies in
\(K_9\), and a common normalization \(h_i\mapsto\nu h_i\), with
\(\nu\in K_9^\times\),
leaves \([N_H]\) unchanged.

The exact rational norm is

\[
N_{K_9/\mathbb Q}(N_H)
=\frac{2^6\,13\,19^5\,41\,59^5\,5653^2}{3^5}.
\]

Its valuations at \(13,19,41,59\), and \(3\) include odd exponents, so it
is not a rational square.  Therefore \(N_H\notin K_9^{\times2}\), and

\[
u^2=N_H
\]

is a nontrivial quadratic Kummer extension of \(K_9\).

## Theorem 5: arithmetic parameter monodromy

The polynomial \(P_9\) is irreducible and

\[
\operatorname{Gal}(P_9/\mathbb Q)\cong S_9.
\]

Indeed, the frozen unramified modular factorizations give cycle types
\((9)\) modulo \(7\), \((5,2,1,1)\) modulo \(17\), and \((8,1)\) modulo
\(23\).  The 9-cycle gives transitivity; the 8-cycle makes a point
stabilizer transitive on the other eight letters, hence the group is
2-transitive and primitive.  Squaring the \((5,2,1,1)\) element gives a
5-cycle.  Jordan's theorem supplies \(A_9\), and the 8-cycle is odd.

## Corollary: gauge stability

Adding a parameter-dependent constant to the action shears the
\((A,c)\)-plane and preserves equal-action fibers.  A cyclic coboundary
telescopes on a closed orbit.  Multiplying the action by a nonzero
parameter-dependent scalar is a local target-coordinate automorphism away
from its zeros and poles.  None of these transformations changes the
intrinsic return matrices or the square class \([h_1h_2]\).

Independent branch-dependent rescalings are not admissible gauges.

## Route-A corollary

The result has strict ceiling

\[
(A1\_\mathrm{WEAK},A2\_\mathrm{FAIL},A3\_\mathrm{FAIL},
A4\_\mathrm{FORMAL\_HINT})
\]

and overall decision `ROUTE_A_REJECTED`.  The theorem produces an arithmetic
cover at period five, not an all-period clock, trace formula, analytic
determinant, functional equation, or self-adjoint spectral realization.

## Explicit claim boundary

The package does not claim:

- novelty of the period-five normalization or of generic Maxwell/Kummer
  mechanisms;
- a full \(C_2\wr S_9\) Galois group;
- Picard--Lefschetz monodromy;
- an extension to periods other than five;
- a dynamical zeta function or Hilbert--Pólya operator.
