# Derivation package

## Target

Determine the full normal-closure Galois group of the quadratic extension
obtained by adjoining the square root of the intrinsic two-branch Hill
product over the period-five Hénon Maxwell collision field. The target is

\[
\operatorname{Gal}\!\left(
L(\sqrt{\beta_1},\ldots,\sqrt{\beta_9})/\mathbb Q
\right)=C_2\wr S_9.
\]

## Status

**PROVED.** The proof uses exact characteristic-zero algebra, one exact
\(19\)-adic Newton polygon, and an independently replayed finite
relation-module argument.

The arithmetic monodromy statement is proved. No all-period zeta or
Hilbert--Pólya interpretation is proved.

## Invariant Object

The invariant object is the square-class-decorated normalization of the C33
Maxwell divisor:

\[
(K,\beta),
\qquad K=\mathbb Q[A]/(P_9),
\qquad \beta=N_H.
\]

Here \(N_H=h\sigma(h)\) is the exchange-invariant product of the two Hill
determinants at the generic equal-action node. A common Hill normalization
\(h_i\mapsto\mu(A)h_i\) multiplies \(\beta\) by \(\mu(A)^2\), so its square
class is intrinsic.

## Assumptions

1. The hash-locked C33 certificate is the source of \(P_9\), \(\beta\),
   and the cyclic Hénon chronology.
2. The C33 theorem \(\operatorname{Gal}(P_9/\mathbb Q)=S_9\) is retained.
3. All fields have characteristic zero.
4. Valuations on ramified local fields are normalized to have value group
   \(\mathbb Z\).
5. No finite prime is selected by fitting a desired group. The prime \(19\)
   is forced by the exact norm/discriminant ledger and is used only as a
   proof certificate.

## Notation

- \(\alpha_1,\ldots,\alpha_9\): the roots of \(P_9\) in its splitting
  field.
- \(K=\mathbb Q(\alpha_1)\).
- \(L\): the splitting field of \(P_9\).
- \(\beta_i=\beta(\alpha_i)\).
- \(M=L(\sqrt{\beta_1},\ldots,\sqrt{\beta_9})\).
- \(R\subset\mathbb F_2^9\): the square-relation kernel among the
  \(\beta_i\).
- \(D=\operatorname{Disc}(P_9)\).
- \(N=N_{K/\mathbb Q}(\beta)\).
- \(v_{19}\): the rational \(19\)-adic valuation.

## Derivation Strategy

The proof deliberately separates three layers.

1. A local layer constructs one valuation parity row of weight two.
2. A permutation layer uses the already-proved \(S_9\) action to shrink
   the possible global relation kernel to one dimension.
3. A rational square-class layer kills the last possible relation and then
   upgrades the standard wreath embedding to equality by an order count.

This avoids computing the splitting field, class group, or a \(512\)-case
Kummer table.

## Derivation Map

\[
\begin{array}{c}
P_9(1802+T)\text{ has Newton edge of slope }-5/2,\\
\beta(1802+T)\text{ has a unique linear leading term}
\end{array}
\Longrightarrow
e_1+e_2\text{ is a valuation-parity row}.
\]

\[
e_1+e_2\text{ and its }S_9\text{-orbit}
\Longrightarrow
R\subset\langle(1,\ldots,1)\rangle.
\]

\[
[N]\ne1,[D]
\Longrightarrow
(1,\ldots,1)\notin R
\Longrightarrow
R=0.
\]

\[
R=0
\Longrightarrow
[M:L]=2^9
\Longrightarrow
\operatorname{Gal}(M/\mathbb Q)=C_2\wr S_9.
\]

## Main Derivation

### 1. Frozen polynomials and rational norms

C33 supplies

\[
\begin{aligned}
P_9(A)={}&110592A^9-294912A^8+159744A^7+225792A^6\\
&-162816A^5-51520A^4+50672A^3+736A^2-6032A+1037.
\end{aligned}
\]

It also supplies

\[
\beta=\frac{B_8(A)}{4827099043},
\]

where the coefficients of \(B_8\), from low to high degree, are

\[
\begin{split}
(&-24722338005452,-299296418917388,399558302240736,\\
&2906695726100864,-1438653142203648,-9885570146248192,\\
&1123467639484416,8210379350937600,-4397149235773440).
\end{split}
\]

The exact resultant normalization gives

\[
N=\frac{\operatorname{Res}(P_9,B_8)}
{110592^8\,4827099043^9}
=\frac{2^6\,13\,19^5\,41\,59^5\,5653^2}{3^5}.
\]

The discriminant factorization is

\[
D=2^{96}3^{12}13^3 19^5 41^3 59^5 9056471^2.
\]

Therefore

\[
[N]_{\mathbb Q^\times/\mathbb Q^{\times2}}
=3\cdot13\cdot19\cdot41\cdot59
\]

and

\[
[D]_{\mathbb Q^\times/\mathbb Q^{\times2}}
=13\cdot19\cdot41\cdot59.
\]

Their quotient has square-free class \(3\).

### 2. Exact Newton polygon at \(19\)

Put

\[
c=-3+5\cdot19^2=1802,
\qquad A=c+T.
\]

Writing

\[
P_9(c+T)=\sum_{i=0}^9 a_iT^i,
\]

the exact valuation vector is

\[
(v_{19}(a_0),\ldots,v_{19}(a_9))
=(5,3,0,0,0,0,0,0,0,0).
\]

After dividing each coefficient by its certified power of \(19\), the unit
residues are

\[
(18,6,5,6,13,7,15,12,5,12).
\]

The lower Newton polygon has the negative-slope edge

\[
(0,5)\longrightarrow(2,0),
\qquad \text{slope}=-\frac52.
\]

The point \((1,3)\) lies strictly above this edge. Since \(5\) and \(2\)
are coprime, the edge has ramification denominator \(2\), residual degree
\(1\), and accounts for exactly two roots with

\[
v_{19}(T)=\frac52.
\]

The residual polynomial in the edge variable is

\[
18+5Y\in\mathbb F_{19}[Y],
\]

which is separable. The horizontal edge accounts for the other seven roots,
which have \(v_{19}(T)=0\).

### 3. Hill valuation on the two-root cluster

Write

\[
B_8(c+T)=\sum_{i=0}^8 b_iT^i.
\]

The exact coefficient valuation vector and unit-residue vector are

\[
(v_{19}(b_0),\ldots,v_{19}(b_8))
=(3,0,0,0,0,0,0,0,0)
\]

and

\[
(18,6,10,13,14,11,9,8,9),
\]

respectively. For a cluster root, the valuations of the first terms are

\[
v_{19}(b_0)=3,
\qquad
v_{19}(b_1T)=\frac52,
\qquad
v_{19}(b_iT^i)\ge5\quad(i\ge2).
\]

The minimum \(5/2\) is unique, so there is no cancellation. The denominator
\(4827099043\equiv7\pmod{19}\) is a unit. Thus both cluster values of
\(\beta\) have rationally normalized valuation \(5/2\), or
integer-normalized valuation \(5\).

Furthermore,

\[
\gcd(P_9,B_8)\bmod19=A+3.
\]

Only the two roots in the repeated \(A+3\) cluster can have positive Hill
valuation. The remaining seven Hill values are units. Hence a valuation of
\(L\) above this cluster gives the parity vector

\[
\epsilon=e_1+e_2.
\]

This argument works directly with roots and the Newton polygon. Since
\(19\) divides the polynomial discriminant, a naive Dedekind factorization
of the power-basis order would be invalid. The leading coefficient
\(110592\) and the denominator of \(\beta\) are both \(19\)-adic units, so
nonmonicity introduces no local obstruction.

### 4. The relation kernel

Define

\[
R=\left\{r=(r_i)\in\mathbb F_2^9:
\prod_i\beta_i^{r_i}\in L^{\times2}\right\}.
\]

If \(r\in R\), every discrete valuation of the product is even. Applying
the certified valuation gives

\[
r_1+r_2=0.
\]

The Galois group is the full \(S_9\), so conjugating this valuation supplies
the same equality for every unordered pair:

\[
r_i+r_j=0\qquad(i\ne j).
\]

Therefore all coordinates of \(r\) agree, and

\[
R\subset\{0,\mathbf1\},
\qquad \mathbf1=(1,\ldots,1).
\]

Equivalently, the \(36\) pair vectors span the eight-dimensional
augmentation module and have the all-ones line as their orthogonal
complement. The certificate also reconstructs the orbit-span rank census
over all \(512\) binary vectors:

\[
\{0:1,\ 1:1,\ 8:255,\ 9:255\}.
\]

### 5. Exclusion of the all-ones relation

The all-ones relation is precisely

\[
\prod_{i=1}^9\beta_i=N\in L^{\times2}.
\]

If a rational number becomes a square in \(L\), then either it was already
a rational square or its square root generates a quadratic subfield of
\(L\). Since

\[
\operatorname{Gal}(L/\mathbb Q)=S_9,
\]

the unique quadratic subfield is the sign field

\[
\mathbb Q(\sqrt D).
\]

This remains true for the nonmonic defining polynomial: the rational
leading-coefficient factor does not change the alternating Vandermonde
square class. But \([N]\ne1\), and \([N/D]=3\ne1\). Hence
\(N\notin L^{\times2}\), so \(\mathbf1\notin R\). It follows that

\[
R=0.
\]

Thus the nine conjugate Hill square classes are independent.

### 6. Wreath group

Kummer theory gives

\[
\operatorname{Gal}(M/L)\cong C_2^9.
\]

The field \(M\) is the splitting field over \(\mathbb Q\) of

\[
F_{18}(U)=\prod_{i=1}^9(U^2-\beta_i).
\]

Restriction to \(L\) gives an exact sequence with quotient \(S_9\), while
the standard quadratic normal-closure construction embeds the group into
\(C_2\wr S_9\). Therefore

\[
|\operatorname{Gal}(M/\mathbb Q)|=2^9\,9!
=|C_2\wr S_9|.
\]

The embedding is onto:

\[
\operatorname{Gal}(M/\mathbb Q)=C_2\wr S_9.
\]

## Remarks and Interpretation

1. C33 proved that \(\beta\) is not a square in one degree-nine collision
   field. C34 proves that all nine Galois conjugates remain independent
   after passing to the common splitting field. This upgrades one quadratic
   extension to the full \(2^9\)-sheeted Kummer base.
2. The proof needs only one local prime because full \(S_9\) symmetry
   propagates one weight-two parity row to every pair.
3. The degree-eighteen norm polynomial is irreducible modulo \(7\), but that
   fact is retained only as an independent control. It is not substituted
   for the Kummer-rank argument.
4. The wreath group acts on signed square roots of nine collision
   parameters, not on eighteen independent branchwise Hill invariants. Each
   \(\beta_i\) is already the product of two branch Hill determinants.

## Boundaries and Non-Claims

- No statement is made beyond exact period five.
- No Euler product or transfer-operator determinant is constructed.
- The finite primes \(7\) and \(19\) certify exact algebraic claims; they
  are not interpreted as arithmetic primes attached to Hénon primitive
  orbits.
- The full wreath group is not a Hilbert--Pólya operator or a critical-line
  theorem.
- Standard Kummer and wreath-embedding machinery is prior art. Novelty is
  claimed only for this explicit Hénon Maxwell--Hill full-rank realization.

## Open Risks

1. An all-period theory would need compatible collision divisors and Hill
   Kummer modules for infinitely many periods; C34 supplies no such tower.
2. It is unknown whether the finite groups obtained at different periods
   organize into a natural profinite or motivic object.
3. It is unknown whether any representation of these groups enters a
   chronological dynamical determinant without external choices.
4. A future arithmetic bridge must preserve the distinction between each
   two-branch product \(\beta_i\) and the individual Hill determinants.
