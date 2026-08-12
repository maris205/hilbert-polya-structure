# HCS-C33 Phase-3 results

## Primary theorem

For the area-preserving Hénon family

\[
H_A(q,p)=(1-Aq^2-p,q),
\]

the exact period-five action image has a degree-nine collision component
\(P_9(A)=0\).  At its generic point:

- the normalization fiber contains exactly two distinct reduced points;
- the two plane branches meet as an ordinary transverse node;
- both points have exact period five;
- neither return matrix has multiplier \(+1\) or \(-1\);
- the symmetric Hill product \(N_H=h_1h_2\) descends to
  \(K_9=\mathbb Q[A]/(P_9)\);
- \([N_H]\) is nontrivial in \(K_9^\times/K_9^{\times2}\).

The decisive nonsquare certificate is

\[
N_{K_9/\mathbb Q}(N_H)
=\frac{1929715196403899883576140608}{243}
=\frac{2^6\,13\,19^5\,41\,59^5\,5653^2}{3^5}.
\]

## Exact action discriminant

\[
\operatorname{Disc}_cW_5
=2^{12}3^{30}A^{60}P_2^5P_5^3P_9^2,
\]

where \(P_9\) is coprime to the marker-ramification factors \(P_2,P_5\).
The squared exponent is not used as a node proof; the certificate separately
checks the two-point fiber, plane tangent cone, and normalization slopes.

## Nonparabolic correction

The Morse/Hill resultant

\[
\operatorname{Res}_q(G_A,h_A)=-2^6A^{30}P_2^5P_5
\]

excludes multiplier \(+1\), but it does not exclude multiplier \(-1\).  The
released theorem includes the additional gate

\[
\operatorname{Res}_q(G_A,4-h_A)=-2^6A^{30}B_6B_9,
\]

with \(P_9\) coprime to \(B_6B_9\).  This is why the final wording “no
multiplier \(+1\) or \(-1\)” is justified.

## Parameter Galois control

Exact modular factor degrees

\[
(9)\pmod7,\qquad(5,2,1,1)\pmod{17},
\qquad(8,1)\pmod{23}
\]

prove

\[
\operatorname{Gal}(P_9/\mathbb Q)=S_9.
\]

This is a theorem about the collision-parameter polynomial.  It does not
promote the quadratic extension to a full \(C_2\wr S_9\) group.

## Frozen finite-prime controls at \(A=6\)

\[
P_9(6)=61\cdot157\cdot3203\cdot21943.
\]

| prime | common action | branch markers | Hill values | \(\chi(h_1h_2)\) | role |
|---:|---:|---:|---:|---:|---|
| 61 | 45 | 12, 36 | 44, 7 | +1 | post-hoc C32 regression |
| 157 | 76 | 58, 129 | 26, 96 | +1 | square control |
| 3203 | 150 | 1805, 2375 | 1577, 2906 | -1 | adversarial nonsquare control |
| 21943 | 20277 | 7923, 20203 | 4539, 16878 | +1 | square control |

These reductions are controls, not the proof of the characteristic-zero
nonsquare theorem.

## Reproducibility status

- producer payload digest:
  `21ba04e8518e1218550a1e70d8f73898b3fbf3afaf11931875e03ece4225c5da`;
- independent semantic gates: `12/12 PASS`;
- adversarial/regression tests: `33/33 PASS`;
- arithmetic mode: exact integer/rational and finite-field computation.

## Route-A decision

\[
(A1\_\mathrm{WEAK},A2\_\mathrm{FAIL},A3\_\mathrm{FAIL},
A4\_\mathrm{FORMAL\_HINT}),
\]

with overall `ROUTE_A_REJECTED` and Route B unauthorized.  No zeta or
Hilbert--Pólya claim is made.
