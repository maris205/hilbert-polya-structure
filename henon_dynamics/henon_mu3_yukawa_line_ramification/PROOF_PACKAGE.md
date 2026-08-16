# HCS-C58 proof package

Status: **CONDITIONAL_PROOF_COMPLETE; PREMISES_MACHINE_REBOUND;
MACHINE_CODE_RESULTS: PREFREEZE_CODE_RESULTS_PASS;
POSTREFRESH_MACHINE_HOSTILE_AUDIT: POSTREFRESH_PASS;
FORMAL_DOCS_PASS; PAPER_PENDING; NOT_RELEASED.**

## 1. Claim

For the frozen HCS-C55/HCS-C56 cubic surface and its \(W(E_6)\) line field,
prove:

1. the distinction between the nine-prime surface divided-discriminant
   bad-prime envelope and exact eight-prime ramified support of \(E,K\);
2. complete filtered inertia at every finite ramified prime;
3. every local Swan and Artin conductor of \(V_6,V_{20}\);
4. exact conductors \(\mathfrak N(V_6),\mathfrak N(V_{20})\);
5. exact discriminants of \(E\) and \(K\);
6. archimedean classification using subgroup ToM 5 and character-table
   element-class index 17 under CTblLib `1.3.1`;
7. the explicit nondependency \(|D_3|\in\{18,36\}\);
8. the exact scope leaf `NO_BAD_EULER_OR_ROOT_NUMBER`.

## 2. Premise discipline and machine rebinding

The written argument below is an implication from H0--H7. Those exact instance
premises are rebound by the official producer and independent checker at the
`PREFREEZE_CODE_RESULTS_PASS` tier. All eight gates pass, the payload has
1149 scalar leaves, and 1199 rebound mutations are independently rejected. The
45-test suite and independent post-refresh machine audit also pass. The
independent formal-document review passes as well. This does not authorize a
paper or release: paper/release/promotion remain blocked.

Universal source theorems and frozen-instance computations remain separate.
Polynomial discriminants are used only in explicit Krasner bounds; they never
substitute for field differents or field discriminants.

## 3. Premises

- **H0 (frozen source and carrier lock).** The C55 surface, C56 degree-27
  field, C57 theta and delta polynomial identities, both permutation actions,
  and \(W(E_6)\) generators are byte-bound without drift;
  \(\operatorname{Gal}(K/\mathbf Q)=W(E_6)\). Theta alone is
  `KRASNER_CERTIFIED_AUTHORITY`; delta is
  `BOUNDED_NON_RESULT_NONDEPENDENCY` and supplies neither dependency nor
  corroboration.
- **H1 (surface envelope and field support).** The surface
  divided-discriminant envelope is
  \(\{2,3,5,181,283,997,1801,2346241,q\}\). The global maximal order gives
  exponent vector \((0,46,36,18,6,18,6,18,6)\) for
  \(\operatorname{Disc}(E)\), so the exact ramified support of both fields is
  the corresponding eight-prime set with \(2\) removed.
- **H2 (local arithmetic and theta authority).** The normalized local
  \((e,f,d)\) rows are those displayed below. Theta alone certifies the
  36-carrier partitions at tame precisions \([20,30,40]\) and wild precisions
  \([900,950,1000]\), with all stated bounds, stability, simplicity, and
  multiply-back identities.
- **H3 (complete decomposition/inertia inventory).** The 350-class
  `U4(2).2` Table-of-Marks scan gives exactly the three \(p=3\) and three
  \(p=5\) raw hits and every valid \((D,I,|D/I|)\) triple stated below.
- **H4 (filtered groups).** Exact `Fraction` arithmetic exhausts the ToM
  \(6\times2,7,8\) deep-\(C_3\) profiles. The unique nonnegative integral
  profile is ToM 7, and Serre IV §2 Proposition 9 selects ToM 140 as inertia.
- **H5 (characters).** Exact fixed-space calculations reconstruct all Swan
  and Artin dimensions and every conductor--different checksum.
- **H6 (reflection geometry and infinity).** Four-chart singular-locus
  elimination, Hessian and Hensel witnesses, transversality, and
  Picard--Lefschetz certify reflection subgroup ToM 2. Exact real-root counts
  and group/character tables certify subgroup ToM 5 and element-class index 17
  at infinity under CTblLib `1.3.1`.
- **H7 (independence and scope).** The independent checker reconstructs
  H0--H6 without importing producer theorem leaves, rejects every critical
  mutation, preserves the \(D_3\) nondependency, and enforces
  `NO_BAD_EULER_OR_ROOT_NUMBER`.

## 4. Surface envelope and exact field ramification

The surface divided-discriminant bad-prime envelope is

\[
\mathcal B_Y=\{2,3,5,181,283,997,1801,2346241,q\},
\]

where

\[
q=14932047182473291995860108491583652133938007263719.
\]

H1 gives

\[
\left(v_p(\operatorname{Disc}E)\right)_{p\in\mathcal B_Y}
=(0,46,36,18,6,18,6,18,6).
\]

At \(2\), the degree-27 permutation conductor is zero, so inertia fixes every
coset of the line stabilizer. That stabilizer is core-free because the 27-line
action is faithful. Hence the inertia image in \(W(E_6)\) lies in the trivial
core and is itself trivial. Away from \(\mathcal B_Y\), the good-reduction
source lock gives no line-field ramification. Therefore the exact finite
ramified support of \(E\) and \(K\) is

\[
\{3,5,181,283,997,1801,2346241,q\}.
\]

Thus the surface envelope and field support are not the same set.

## 5. Degree-36 local authority

At each tame \(C_3\) prime \(p=181,997,2346241\), theta is stable at
precisions \([20,30,40]\). Its global polynomial-discriminant exponent is
\(24\), twice the largest factor-polynomial discriminant exponent is \(24\),
and its factor degrees are \((3,6,9,18)\). Thus precision \(40\) exceeds both
Krasner bounds and certifies double-six inertia type \(3^{12}\).

At the wild primes theta is monic, simple, stable, and multiplies back at each
precision in \([900,950,1000]\). At \(3\), it has degrees
\((3,3,3,9,18)\), global polynomial-discriminant exponent \(886\), and
twice-largest-factor bound \(538\). At \(5\), the corresponding values are
\((1,5,10,10,10)\), \(746\), and \(246\). Each certified precision exceeds
both applicable bounds.

Delta has global polynomial-discriminant exponent \(840\) and
twice-largest-factor bound \(408\), so tame precision \(40\) meets neither
bound. It remains `BOUNDED_NON_RESULT_NONDEPENDENCY` at tame and wild
primes. No later proof step depends on delta or cites it as corroboration.

## 6. Wild filtration at \(p=5\)

H2 gives

\[
(e,f,d)=(1,1,0)^2,(5,1,7)^3,(10,1,15).
\]

The simultaneous 27/36 orbit-pattern hits are ToM 147 of order \(20\)
(`IdGroup(20,3)`), ToM 247 of order \(60\) (`IdGroup(60,5)`), and ToM
295 of order \(120\) (`IdGroup(120,34)`). The Sylow-\(5\) subgroup is
nonnormal in ToM 247 and ToM 295, which is incompatible with wild inertia.
Hence the unique valid pair is

\[
(D,I,|D/I|)=(147,147,1),\qquad I_0\cong C_5:C_4.
\]

Let \(P=C_5\). Comparing the \(P\)-refinement with the three degree-5 and one
degree-10 different exponents gives the unique layer count three:

\[
I_1=I_2=I_3=C_5,\qquad I_4=1.
\]

No other subgroup or filtration survives H2--H4.

## 7. Wild filtration at \(p=3\)

H2 gives

\[
(e,f,d)=(3,1,3),(6,1,7),(9,1,18)^2.
\]

The exhaustive simultaneous orbit-pattern hits are ToM 140 of order \(18\)
(`IdGroup(18,4)`), ToM 142 of order \(18\) (`IdGroup(18,3)`), and ToM
206 of order \(36\) (`IdGroup(36,10)`). ToM 206 has putative tame quotient
\(V_4\), so it cannot be \(I_0\). It can be a decomposition overgroup.
Normality and cyclic residue quotient give exactly

\[
(D,I,|D/I|)=(140,140,1),(142,142,1),(206,140,2),(206,142,2).
\]

The deep order-three subgroups in these pairs have profile inventory ToM 6
twice, ToM 7 once, and ToM 8 once. With base different vector
\((2,5,8,8)\) and one \(C_3^2\)-layer contribution \((1,2,4,4)\), exact
`Fraction` arithmetic gives

\[
\begin{array}{c|c|c}
\text{deep profile} & \text{deep-layer contribution} & (r,s)\\
\hline
\text{ToM 6} & (1/3,2/3,1,1) & (7,-18)\\
\text{ToM 7} & (0,0,1,1) & (1,6)\\
\text{ToM 8} & (1/3,2/3,1,1) & (7,-18).
\end{array}
\]

The ToM 6 and ToM 8 solutions are inadmissible because \(s<0\). ToM 7 is the
unique nonnegative integral solution and yields

\[
I_1=C_3^2,\qquad I_2=\cdots=I_7=C_3,\qquad I_8=1.
\]

For \(s\in I_0\) and \(\tau\in G_7/G_8\), Serre IV §2 Proposition 9 gives

\[
\theta_7(s\tau s^{-1})=\theta_0(s)^7\theta_7(\tau).
\]

The tame quotient is \(C_2\), and odd exponent \(7\) forces inversion on the
final \(C_3\). ToM 140 has this action; ToM 142 centralizes the deep subgroup
and is excluded. Therefore

\[
I_0=\operatorname{ToM}140\cong(C_3^2):C_2
\]

and the two surviving decomposition/inertia pairs are

\[
(D,I)=(140,140),\qquad(206,140).
\]

Thus \(|D_3|\in\{18,36\}\), with the same complete filtered inertia. ToM 206
is a possible decomposition overgroup only; it is not an inertia candidate.

## 8. Tame rows and the reflection bridge

At each of \(181,997,2346241\), the maximal-order rows are

\[
(3,1,2),(3,2,2),(3,6,2).
\]

Together with theta's certified \(3^{12}\) double-six type, the exhaustive
order-three profile scan selects tame \(C_3\) subgroup ToM 6.

At each of \(283,1801,q\), exact singular-locus elimination on all four affine
charts gives one reduced point in chart 0 and unit ideals in the other three.
At the point, the gradient vanishes and the affine Hessian determinant is a
unit. The first Hensel correction gives a unique critical point modulo \(p^2\),
and its critical value agrees with the integer witness modulo \(p^2\). Hence
the smoothing parameter has valuation one and the total space is regular and
transverse. Since every residue characteristic is odd, Picard--Lefschetz gives
tame root-reflection inertia.

The exhaustive order-two scan uniquely selects subgroup ToM 2. Its line and
double-six types are \(1^{15}2^6\) and \(1^{16}2^{10}\), its fixed dimensions
are \((5,15)\), and its Swan/Artin pairs are \((0,0)\) and \((1,5)\). This
argument makes no \(e/f\) decomposition-row claim at a reflection prime.

## 9. Local conductors

By H5 and the Artin formula,

\[
\begin{array}{c|cc}
p & \operatorname{Sw}(V_6,V_{20}) & a(V_6,V_{20})\\
\hline
3 & (5,18) & (11,35)\\
5 & (3,12) & (7,29)\\
181,997,2346241 & (0,0) & (6,12)\\
283,1801,q & (0,0) & (1,5).
\end{array}
\]

At every finite prime, the sum of the two Artin exponents equals the
permutation conductor and hence the local exponent of
\(\operatorname{Disc}(E)\). This is a closure check, not a replacement for the
branchwise different proof.

## 10. Global conductors and field discriminants

Put

\[
A=181\cdot997\cdot2346241,\qquad B=283\cdot1801\cdot q.
\]

Multiplying local conductor powers gives

\[
\mathfrak N(V_6)=3^{11}5^7A^6B,\qquad
\mathfrak N(V_{20})=3^{35}5^{29}A^{12}B^5.
\]

Their product equals the positive field discriminant:

\[
\mathfrak N(V_6)\mathfrak N(V_{20})
=\operatorname{Disc}(E)=3^{46}5^{36}A^{18}B^6.
\]

For the Galois closure, the local different formula is

\[
v_p(\operatorname{Disc}K)
=\frac{|W(E_6)|}{|I_0|}\sum_{i\ge0}(|I_i|-1).
\]

Substituting the proved filtrations gives exponents \(106560,80352,34560,
25920\) for \(p=3\), \(p=5\), tame \(C_3\), and reflection primes,
respectively. Therefore

\[
\operatorname{Disc}(K)
=3^{106560}5^{80352}A^{34560}B^{25920}.
\]

This proof uses no choice between the two surviving values of \(D_3\).

## 11. Archimedean classification

The exact signature \((3,12)\) gives line type \(1^3 2^{12}\), while
`polsturm(theta36)=4` gives double-six type \(1^4 2^{16}\). The exhaustive
order-two subgroup profiles ToM 2, 3, 4, and 5 have a unique simultaneous
match: **subgroup ToM 5**. In `CharacterTable("U4(2).2")`, the unique
order-two element class with size \(540\) and centralizer size \(96\) is
**element-class index 17**. These are different indexing systems. GAP and
CTblLib `1.3.1` then give

\[
V_6:(d^+,d^-)=(3,3),\qquad
V_{20}:(d^+,d^-)=(11,9).
\]

## 12. Scope locks

`NO_BAD_EULER_OR_ROOT_NUMBER`: C58 proves no decomposition Frobenius, bad
Euler polynomial or factor, local epsilon factor, local or global root number,
Artin holomorphy, automorphy, analytic continuation, or functional equation.
Even determining which of \((D,I)=(140,140),(206,140)\) occurs would not by
itself establish any such statement.

The proof also establishes no rational-point, Hasse-principle,
weak-approximation, or Brauer--Manin conclusion. These exclusions are part of
H7 and must survive every paper revision.

## 13. Machine evidence boundary

The official evidence tuple has certificate SHA-256
`456a481368d593f0d015436bf8a3a518d15b4567880fa7726c77d29a259d79ee`,
payload SHA-256
`fba2dfdf71977d8de6c85635eca6572e0b8a0680570f394af9e3e9e8698f732f`,
schema SHA-256
`ccbc20eb6e04d00f14cdc0ccf970caebf4d66b4103176515799ddca89639009a`,
check-report SHA-256
`64454700ddaa0bb9ff56c85afa213f038ec6b430bc38ef07e3f22924081d22e9`,
and scoped-manifest SHA-256
`a18742298722e2bff022b95be8a09806dd774a52ab8e095ebde78924c45ae730`.
The formal-document hostile audit independently passes. Paper proof review,
compilation, and release are not implied by either the machine or formal pass.
