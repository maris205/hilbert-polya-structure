# HCS-C58 derivation

Status: **THEOREM_TARGET_LOCKED; CONDITIONAL DERIVATION COMPLETE;
MACHINE PREMISES PREFREEZE_CODE_RESULTS_PASS; POSTREFRESH_PASS;
FORMAL_DOCS_PASS; PAPER_PENDING; NOT_RELEASED.**

This document derives the locked formulas from exact premises now certified by
the eight machine gates G0--G7 and the independent post-refresh hostile audit.
The code/results tuple is a prefreeze machine theorem and the independent
formal-document audit has passed; paper compilation and release remain
separate pending gates.

## 1. Representation setup

Let

\[
W=W(E_6),\qquad |W|=51840,
\]

and let \(E\) be the degree-27 line field with normal closure \(K\). The
permutation representation decomposes over \(\mathbf Q\) as

\[
\mathbf Q[27]=\mathbf1\oplus V_6\oplus V_{20}.
\tag{1.1}
\]

For a lower-numbered inertia filtration

\[
I_0\supseteq I_1\supseteq I_2\supseteq\cdots,
\]

the Artin conductor is

\[
a_p(V)=
\operatorname{codim}V^{I_0}
+\sum_{i\ge1}
\frac{|I_i|}{|I_0|}
\operatorname{codim}V^{I_i}.
\tag{1.2}
\]

The second term is the Swan conductor.

For the 27-point permutation representation, conductor--discriminant gives

\[
a_p(V_6)+a_p(V_{20})
=v_p(\operatorname{Disc}E).
\tag{1.3}
\]

Equation (1.3) is a closure check. It does not determine the separate
constituents without subgroup fixed-space calculations.

At \(p=2\), its left side is zero.  Thus inertia acts trivially on all 27
cosets of a line stabilizer.  The stabilizer is core-free because the
27-line \(W(E_6)\)-action is faithful, so the inertia image in the normal
closure \(K\) is trivial.  This core-free bridge is essential: merely knowing
that the non-Galois field \(E\) has discriminant exponent zero would not by
itself justify an unqualified statement about an arbitrary normal closure.

The surface divided-discriminant bad-prime envelope is
\(\{2,3,5,181,283,997,1801,2346241,q\}\), whereas the exact finite
ramified support of both \(E\) and \(K\) is
\(\{3,5,181,283,997,1801,2346241,q\}\). In that nine-prime order,

\[
v_p(\operatorname{Disc}E)=(0,46,36,18,6,18,6,18,6).
\tag{1.4}
\]

Thus 2 belongs to the surface envelope but is unramified in both number
fields.

## 2. Direct local differents

For a local factor of degree \(n=ef\) with different exponent \(d\), its
contribution to the field discriminant is \(fd\).

At \(p=3\), all \(f=1\), so

\[
v_3(\operatorname{Disc}E)
=3+7+18+18=46.
\tag{2.1}
\]

At \(p=5\),

\[
v_5(\operatorname{Disc}E)
=0+0+7+7+7+15=36.
\tag{2.2}
\]

At each tame order-three prime,

\[
v_p(\operatorname{Disc}E)
=1\cdot2+2\cdot2+6\cdot2=18.
\tag{2.3}
\]

At a reflection prime, the tame reflection has six transpositions on the
27 lines, so its permutation conductor is six:

\[
v_p(\operatorname{Disc}E)=6.
\tag{2.4}
\]

## 3. Prime \(5\)

The simultaneous orbit targets are

\[
27:\ (1,1,5,5,5,10),
\qquad
36:\ (1,5,10,10,10).
\tag{3.1}
\]

The complete simultaneous Table-of-Marks hits are ToM 147 of order 20
(`IdGroup(20,3)`), ToM 247 of order 60 (`IdGroup(60,5)`), and ToM 295 of
order 120 (`IdGroup(120,34)`). The latter two have nonnormal Sylow-5
subgroups. Hence the unique valid decomposition/inertia pair after the
exhaustive normality and cyclic-residue-quotient tests is
\((D,I,|D/I|)=(147,147,1)\), with

\[
I_0\cong C_5:C_4,\qquad |I_0|=20.
\tag{3.2}
\]

Let \(P=C_5\). Comparing branchwise tame differents with the \(P\)-orbit
refinement forces exactly three positive layers:

\[
I_1=I_2=I_3=P,\qquad I_4=1.
\tag{3.3}
\]

The fixed dimensions are

\[
\dim(V_6^{I_0},V_{20}^{I_0})=(2,3),
\qquad
\dim(V_6^P,V_{20}^P)=(2,4).
\tag{3.4}
\]

Hence the inertia codimensions are \((4,17)\), and the \(P\)-codimensions
are \((4,16)\). Therefore

\[
\operatorname{Sw}_5(V_6,V_{20})
=3\frac5{20}(4,16)=(3,12),
\tag{3.5}
\]

\[
a_5(V_6,V_{20})
=(4,17)+(3,12)=(7,29).
\tag{3.6}
\]

The sum \(7+29=36\) agrees with (2.2).

## 4. Prime \(3\): layer lengths

The simultaneous orbit targets are

\[
27:\ (3,6,9,9),
\qquad
36:\ (3,3,3,9,18).
\tag{4.1}
\]

Only the theta resolver certifies this degree-36 local partition. It is monic,
simple, stable, and multiplies back at each precision in
\([900,950,1000]\). At \(p=3\), its global polynomial-discriminant exponent
is 886 and twice its largest factor-polynomial discriminant exponent is 538;
every certified precision exceeds both bounds. Delta remains
`BOUNDED_NON_RESULT_NONDEPENDENCY`: it is neither a theorem dependency nor
corroborating evidence.

The wild subgroup is

\[
P=C_3^2,\qquad |P|=9.
\tag{4.2}
\]

Relative to the four \(I_0\)-orbits, the \(P\)-refinement codimensions in
the permutation carrier are

\[
(2,4,8,8).
\tag{4.3}
\]

Across all four valid \((D,I)\) pairs, the order-three profile inventory is
ToM 6 with multiplicity two, ToM 7 with multiplicity one, and ToM 8 with
multiplicity one. The exact `Fraction` calculation uses base different vector
\((2,5,8,8)\), one-layer \(C_3^2\) contribution \((1,2,4,4)\), and
deep-layer contributions

\[
\begin{array}{c|c|c}
\text{profile}&\text{deep contribution}&\text{formal }(r,s)\\ \hline
\text{ToM 6 (multiplicity 2)}&(1/3,2/3,1,1)&(7,-18)\\
\text{ToM 7 (multiplicity 1)}&(0,0,1,1)&(1,6)\\
\text{ToM 8 (multiplicity 1)}&(1/3,2/3,1,1)&(7,-18)
\end{array}.
\tag{4.4}
\]

The ToM 6 and ToM 8 solutions are not nonnegative; ToM 7 is the unique
admissible deep subgroup and has line cycle type \(1^9 3^6\). Therefore the
only filtered chain is

\[
|I_0|=18,\quad I_1=C_3^2,\quad
I_2=\cdots=I_7=C_3\ (\text{ToM 7}),\quad I_8=1.
\tag{4.5}
\]

## 5. Prime \(3\): embedding uniqueness

Using GAP's `U4(2).2` Table of Marks with all 350 subgroup classes, the
complete \(p=3\) orbit-pattern hits are ToM 140 of order 18
(`IdGroup(18,4)`), ToM 142 of order 18 (`IdGroup(18,3)`), and ToM 206 of
order 36 (`IdGroup(36,10)`). ToM 206 cannot be \(I_0\), because its putative
tame quotient is noncyclic \(V_4\), but it can be a decomposition overgroup.
After normality and cyclic-residue-quotient tests, the exhaustive valid triples
\((D,I,|D/I|)\) are

\[
(140,140,1),\quad(142,142,1),\quad(206,140,2),\quad(206,142,2).
\tag{5.1}
\]

After this exhaustive D/I scan and the Fraction profile test, the two possible
inertia embeddings are

\[
\text{ToM 140}\cong(C_3^2):C_2,
\qquad
\text{ToM 142}\cong C_3\times S_3.
\tag{5.2}
\]

The required deep \(Q\) is inverted in ToM 140 and central in ToM 142.

Serre IV.2 Proposition 9 states

\[
\theta_i(s\tau s^{-1})
=\theta_0(s)^i\theta_i(\tau).
\tag{5.3}
\]

At the last nonzero quotient \(G_7/G_8=Q\), the tame element has
\(\theta_0(s)=-1\). Hence

\[
\theta_7(s\tau s^{-1})
=(-1)^7\theta_7(\tau)
=-\theta_7(\tau).
\tag{5.4}
\]

The action is inversion, so ToM 142 is impossible. The filtered inertia is
uniquely ToM 140 up to \(W(E_6)\)-conjugacy, and the two surviving pairs are
\((D,I)=(140,140)\) and \((206,140)\). Thus

\[
|D_3|\in\{18,36\}.
\tag{5.5}
\]

This unresolved choice is a nondependency for all filtered-inertia,
conductor, and discriminant conclusions.

## 6. Prime \(3\): conductors

The fixed dimensions are

\[
\begin{array}{c|ccc}
&I_0&P&Q\\ \hline
\dim V_6^H&0&0&4\\
\dim V_{20}^H&3&4&10
\end{array}.
\tag{6.1}
\]

Therefore

\[
\operatorname{Sw}_3(V_6,V_{20})
=\frac9{18}(6,16)
+6\frac3{18}(2,10)
=(5,18),
\tag{6.2}
\]

\[
a_3(V_6,V_{20})
=(6,17)+(5,18)=(11,35).
\tag{6.3}
\]

Again \(11+35=46\), agreeing with (2.1).

## 7. Tame order-three and reflection rows

For the selected size-80 \(C_3\) class,

\[
\dim(V_6^{C_3},V_{20}^{C_3})=(0,8),
\tag{7.1}
\]

so

\[
a_p(V_6,V_{20})=(6,12).
\tag{7.2}
\]

The degree-36 type \(3^{12}\) separates this class from the size-480 class
with type \(1^3 3^{11}\).

Here theta alone has role `KRASNER_CERTIFIED_AUTHORITY`. At each of
\(p=181,997,2346241\), theta is stable at precisions \([20,30,40]\), and
precision 40 exceeds both \(v_p(\operatorname{Disc}(\theta))=24\) and twice
the largest factor-polynomial discriminant exponent, also 24. Delta has
global polynomial-discriminant exponent 840 and twice-largest-factor bound
408, so precision 40 proves neither Krasner bound; delta remains
`BOUNDED_NON_RESULT_NONDEPENDENCY` and is not used.

At each of \(283,1801,q\), exact singular-locus elimination over all four
affine charts gives one reduced point in chart 0 and unit ideals in the other
three. The gradient vanishes, the affine Hessian determinant is a unit, and
Hensel lifting gives a unique critical point modulo \(p^2\). The critical
value agrees with the integer witness modulo \(p^2\), so the smoothing
parameter has valuation exactly one and the total space is regular and
transverse. In odd residue characteristic, Picard--Lefschetz therefore gives
tame root-reflection inertia. The exhaustive order-two scan uniquely selects
subgroup ToM 2, with line type \(1^{15}2^6\), double-six type
\(1^{16}2^{10}\), and

\[
\dim(V_6^{C_2},V_{20}^{C_2})=(5,15),
\tag{7.3}
\]

and hence

\[
a_p(V_6,V_{20})=(1,5).
\tag{7.4}
\]

The reflection Artin pair is \((1,5)\) and its Swan pair is \((0,0)\). This
geometric bridge makes no local \(e/f\) decomposition-row claim. Both the
order-three and reflection rows are tame, so their Swan conductors vanish.

## 8. Global Artin conductors

Put

\[
A=181\cdot997\cdot2346241,\qquad
B=283\cdot1801\cdot q.
\tag{8.1}
\]

Collecting the local exponents gives

\[
N(V_6)=3^{11}5^7A^6B,
\tag{8.2}
\]

\[
N(V_{20})=3^{35}5^{29}A^{12}B^5.
\tag{8.3}
\]

Multiplication yields

\[
N(V_6)N(V_{20})
=3^{46}5^{36}A^{18}B^6
=\operatorname{Disc}E.
\tag{8.4}
\]

## 9. Normal-closure discriminant

For a Galois extension with group \(W\), a rational prime with inertia
filtration \(I_i\) contributes

\[
v_p(\operatorname{Disc}K)
=\frac{|W|}{|I_0|}
\sum_{i\ge0}(|I_i|-1).
\tag{9.1}
\]

At \(p=3\),

\[
\sum_{i\ge0}(|I_i|-1)
=(18-1)+(9-1)+6(3-1)=37,
\]

\[
v_3(\operatorname{Disc}K)
=\frac{51840}{18}\cdot37=106560.
\tag{9.2}
\]

At \(p=5\),

\[
\sum_{i\ge0}(|I_i|-1)
=(20-1)+3(5-1)=31,
\]

\[
v_5(\operatorname{Disc}K)
=\frac{51840}{20}\cdot31=80352.
\tag{9.3}
\]

For tame \(C_3\) and \(C_2\),

\[
\frac{51840}{3}(3-1)=34560,
\qquad
\frac{51840}{2}(2-1)=25920.
\tag{9.4}
\]

Therefore

\[
\operatorname{Disc}K
=3^{106560}5^{80352}A^{34560}B^{25920}.
\tag{9.5}
\]

Only inertia appears in (9.1), so (5.4) does not affect (9.5).

## 10. Archimedean type

The exact signature \((3,12)\) gives line type \(1^3 2^{12}\), and
`polsturm(theta36)=4` gives double-six type \(1^4 2^{16}\). The exhaustive
order-two subgroup profiles ToM 2, 3, 4, and 5 have a unique simultaneous
match: subgroup ToM 5. In `CharacterTable("U4(2).2")`, the unique order-two
element class with class size 540 and centralizer size 96 is element-class
index 17. These are different indices, fixed under GAP and CTblLib 1.3.1.

The fixed dimensions are

\[
\dim V_6^{c=1}=3,\qquad
\dim V_{20}^{c=1}=11.
\tag{10.1}
\]

Thus

\[
V_6:(d^+,d^-)=(3,3),\qquad
V_{20}:(d^+,d^-)=(11,9).
\tag{10.2}
\]

This determines the stated archimedean parity, but not any root number.

## 11. Derivation firewalls

- Direct local differents precede conductor identities.
- Both permutation carriers precede subgroup uniqueness.
- Serre's law, not aesthetic group choice, eliminates ToM 142.
- Reflection rows use geometry and do not assert uncomputed \(e/f\) data.
- \(\operatorname{Disc}K\) uses inertia, not a guessed decomposition group.
- `NO_BAD_EULER_OR_ROOT_NUMBER`: C58 proves no decomposition Frobenius, bad
  Euler polynomial or factor, local epsilon factor, local or global root
  number, Artin holomorphy, automorphy, analytic continuation, or functional
  equation. Even resolving \(D_3\) later would not authorize any of these;
  each needs an independent theorem.
- G0--G7 and the post-refresh hostile audit certify the machine premises;
  the formal-document audit also passes, while paper compilation and release
  remain pending.
