# Proof package

## 1. Frozen recurrence

For `H6(q,p)=(1-6q^2-p,q)`, a periodic coordinate sequence satisfies

\[
q_{j+1}=1-6q_j^2-q_{j-1}.
\]

The derivative at coordinate `q` is

\[
D(q)=\begin{pmatrix}-12q&-1\\1&0\end{pmatrix},\qquad \det D(q)=1.
\]

## 2. Reflection chains

Put

\[
b=\frac{1-6a^2}{2},\qquad
c=1-6b^2-a,\qquad
d=1-6c^2-b.
\]

For `A6`, use `(a,b,c,d,c,b)` and impose `1-6d^2-2c=0`.  Its primitive
degree-six factor is

\[
2916a^6-1782a^4+108a^3+279a^2-33a-2.
\]

For the shared `A7/B7` chain, use `(a,b,c,d,d,c,b)` and impose
`1-6d^2-c-d=0`.  The non-fixed primitive factor has degree fourteen and is
printed in the manuscript appendix and certificate.

## 3. Trace elimination

Chronological multiplication and reduction modulo the `A6` coordinate
polynomial give

\[
T_6(a)=-2(1364688a^4-94608a^3-379080a^2+56808a+689).
\]

The resultant is the square of

\[
F_6(T)=T^3+48342T^2-334511988T+306994257352.
\]

The square records the two reflection-axis choices for each orbit.  `F6` is
irreducible modulo 5 and has one root in each of

```text
(-54575,-54574), (1094,1095), (5137,5138).
```

The period-seven resultant is irreducible modulo 37, has degree fourteen,
and has exactly one root in each of the fourteen locked intervals in the
certificate.  Hence it is totally real.  Rational coordinate boxes identify

```text
A7: a in (551935742/10^9, 551935743/10^9), trace in (-390512,-390511)
B7: a in (-600956965/10^9,-600956964/10^9), trace in (230985,230986).
```

## 4. Exact excess separation

For `u>2`, the expanding reciprocal root satisfies

\[
u-1<\frac{u+\sqrt{u^2-4}}2<u,
\]

and therefore

\[
\log(u-1)<\operatorname{arcosh}(u/2)<\log u.
\]

The five nonphysical `A5` trace intervals yield

\[
E(A_5)>\log(709\cdot588\cdot389\cdot769\cdot4444).
\]

The two nonphysical `A6` intervals and the P56 `B6` half-trace interval give

\[
E(A_6)+E(B_6)<\log(1095\cdot5138\cdot3902).
\]

Exact multiplication gives

```text
lower = 554208972546768
upper =     21953081220
margin = 554187019465548.
```

Thus `E(A5)>E(A6)+E(B6)`.  The degree-fourteen field has nonphysical
expanding embeddings, so `E(B7)>0`.  Consequently

\[
\Delta_5=E(A_5)+E(B_7)-E(A_6)-E(B_6)>0.
\]

## 5. Local-potential consequence

P56 proves

\[
N_5(A_5)+N_5(B_7)=N_5(A_6)+N_5(B_6).
\]

Pairing this relation with any width-five potential forces `Delta_5=0`, a
contradiction.  Every width-at-most-five potential can be lifted to width
five by ignoring extra coordinates, proving the theorem.

## 6. Finite sharpness

The four relation rows have rank three at width five.  At width six, columns

```text
000021, 000023, 000210, 000231
```

form a determinant `-1` minor.  For the cumulative rows

```text
C1,A3,A4,B4,A5,B5,B6,A6,B7
```

the nine locked columns in the certificate form a determinant `+1` minor.
Thus the finite data are freely interpolable at width six.

## 7. Claim boundary

This proves no width-at-most-five locally constant realization.  It does not
prove that a general Hölder function fails: a fixed finite set of disjoint
periodic orbits is Hölder-interpolable.  A one-sided Hölder no-go still needs
an asymptotic lower bound on infinitely many `Delta_m` that conflicts with
the P56 exponential necessary upper bound.
