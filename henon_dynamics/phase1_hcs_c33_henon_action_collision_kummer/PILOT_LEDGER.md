# Exact Phase-1 pilot ledger

## Status

The calculations below were run as disposable exact SymPy probes.  They are
not yet a release certificate and must be independently reimplemented in
Phase 3.  They are sufficient to decide that the research question is
feasible and nonvacuous.

## 1. Old marker cover

For the exact period-five marker \(G_A(q)\),

\[
\operatorname{Disc}_qG_A
=2^6A^{30}P_2(A)P_5(A),
\]

where

\[
P_2=16A^2-28A-19
\]

and

\[
P_5=16A^5-108A^4+105A^3+27A^2-97A-47.
\]

Both factors are irreducible over \(\mathbb Q\).

## 2. Action plane curve

The reduced action numerator is

\[
\begin{aligned}
R_A(q)={}&2A^5q^5+2A^5q^4+2A^4q^4-4A^4q^2
-2A^3q^3+6A^3q^2\\
&-2A^3q+2A^3-A^2q^2+4A^2q-8A^2+2A+2.
\end{aligned}
\]

It satisfies

\[
R_A(q)\equiv3A^2\Phi_{5,A}\pmod{G_A(q)}.
\]

The primitive resultant \(W_5(A,c)\) has degree six in \(c\).  At \(A=6\),
its coefficient vector is

\[
\begin{aligned}
(&1586874322944,\ 235092492288,\ -1847271909888,\\
&-670184419968,\ 319843221264,\ 149420336472,\ 14657284973).
\end{aligned}
\]

Modulo \(37\), this specializes to an irreducible sextic.  Hence the action
value is a primitive generator of the same generic degree-six function field
as the old marker coordinate.  This is a duplication firewall: ordinary
permutation/Galois monodromy of the normalization is not a new result.

## 3. New equal-action divisor

Exact elimination gives

\[
\operatorname{Disc}_cW_5
=2^{12}3^{30}A^{60}P_2^5P_5^3P_9^2,
\]

with

\[
\begin{aligned}
P_9(A)={}&110592A^9-294912A^8+159744A^7+225792A^6\\
&-162816A^5-51520A^4+50672A^3+736A^2\\
&-6032A+1037.
\end{aligned}
\]

The pilot verifies:

- \(P_9\) is irreducible and squarefree over \(\mathbb Q\);
- \(\gcd(P_9,P_2P_5)=1\);
- over \(K_9=\mathbb Q[A]/(P_9)\), the singular point satisfies
  \(W=W_A=W_c=0\);
- \(W_{cc}\ne0\) and the tangent-cone discriminant is nonzero in \(K_9\).

Thus the generic \(P_9\) point is an ordinary equal-action node of two
distinct sheets, not ramification of the normalized orbit cover.

### Arithmetic monodromy of the collision parameters

The discriminant of \(P_9\) is

\[
2^{96}3^{12}13^3 19^5 41^3 59^5 9056471^2,
\]

so \(7,17,23\) are unramified.  Exact modular factorization gives cycle
types

\[
\begin{array}{c|c}
p&\text{degrees of the irreducible factors of }P_9\bmod p\\ \hline
7&(9)\\
17&(5,2,1,1)\\
23&(8,1).
\end{array}
\]

The factor modulo \(7\) proves irreducibility and transitivity.  The
\((8,1)\) element, together with transitivity, proves two-transitivity and
hence primitivity.  Squaring the \((5,2,1,1)\) element yields a pure
five-cycle.  Jordan's theorem then gives \(A_9\), while the eight-cycle is
odd.  Consequently

\[
\boxed{\operatorname{Gal}(P_9/\mathbb Q)=S_9.}
\]

This is the monodromy of the collision-parameter divisor.  It is not a new
calculation of the degree-six marker-cover Galois group.

## 4. Nonparabolic control

Let \(h_A(q)=\det(I-DH_A^5)\), computed in the cyclic action convention.
The exact resultant is

\[
\operatorname{Res}_q(G_A,h_A)
=-2^6A^{30}P_2^5P_5.
\]

It is coprime to \(P_9\).  Therefore both branches of the generic
equal-action node are nondegenerate Morse points.

## 5. The Hill Kummer class

Let \(q_1,q_2\) be the two node branches.  Their Hill product reduces in
\(K_9\) to

\[
N_H=-\frac4{4827099043}Q_8(A),
\]

where

\[
\begin{aligned}
Q_8(A)={}&1099287308943360A^8-2052594837734400A^7\\
&-280866909871104A^6+2471392536562048A^5\\
&+359663285550912A^4-726673931525216A^3\\
&-99889575560184A^2+74824104729347A+6180584501363.
\end{aligned}
\]

Because \(P_9\) is not monic, the normalized degree-nine field norm is
computed as

\[
\operatorname{Norm}_{K_9/\mathbb Q}(N_H)
=\left(-\frac4{4827099043}\right)^9
\frac{\operatorname{Res}_A(P_9,Q_8)}{110592^8}.
\]

Exact cancellation gives

\[
\operatorname{Norm}_{K_9/\mathbb Q}(N_H)
=\frac{1929715196403899883576140608}{243}
=\frac{2^6\,13\,19^5\,41\,59^5\,5653^2}{3^5}.
\]

This rational number is not a square.  Consequently

\[
\boxed{N_H\notin K_9^{\times2}.}
\]

The Kummer cover \(u^2=N_H\) is therefore nontrivial.

## 6. Exact \(A=6\) specialization controls

The collision polynomial satisfies

\[
P_9(6)=673104399533
=61\cdot157\cdot3203\cdot21943.
\]

Every row below is an equal-action collision between two split branches.

| \(p\) | action \(c\) | diagonal representatives \(q_1,q_2\) | Hill values \(h_1,h_2\) | \(N_H\) | square? |
|---:|---:|---:|---:|---:|:---:|
| 61 | 45 | 12, 36 | 44, 7 | 3 | yes |
| 157 | 76 | 58, 129 | 26, 96 | 141 | yes |
| 3203 | 150 | 1805, 2375 | 1577, 2906 | 2472 | **no** |
| 21943 | 20277 | 7923, 20203 | 4539, 16878 | 6229 | yes |

At \(p=61\), cyclic rotation turns the two diagonal representatives into
the exact C32 words

\[
(12,12,40,27,40),
\qquad
(33,58,36,36,58).
\]

Since \(44/7=15=25^2\pmod{61}\), this row reproduces the C32 Morse-local
collapse.  At \(p=3203\), the matched equal-action collision has nonsquare
Hill ratio, so the quadratic local gate distinguishes the two branches.

## 7. Interpretation boundary

The pilot proves that the proposed Kummer object is nontrivial.  It does not
yet establish priority, an all-period tower, a global \(L\)-function, or a
Hilbert--Pólya spectrum.  Those are downstream questions and remain outside
the Phase-1 claim set.
