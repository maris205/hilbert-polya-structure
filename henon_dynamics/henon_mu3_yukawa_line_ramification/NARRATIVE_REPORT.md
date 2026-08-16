# HCS-C58 narrative report

Status: **MACHINE_CODE_RESULTS: PREFREEZE_CODE_RESULTS_PASS;
POSTREFRESH_MACHINE_HOSTILE_AUDIT: POSTREFRESH_PASS;
FORMAL_DOCS_PASS; PAPER_PENDING; NOT_RELEASED.**

## 1. Why C58 follows C57

C55 produced the explicit cubic-surface geometry, C56 produced the exact
degree-27 field of the lines and its \(W(E_6)\) structure, and C57 isolated the
degree-36 double-six carrier. C58 determines how that same
\(W(E_6)\)-extension ramifies, including its wild higher groups, and computes
the resulting Artin and Swan conductors of the two nontrivial constituents of
the 27-line permutation representation.

This is stronger than a list of bad fibers. The theorem reconstructs the
lower-numbered inertia filtration from exact local arithmetic, identifies its
embedding in \(W(E_6)\), and closes the calculation with both field
discriminants. The machine layer has passed all eight gates G0--G7 at the
prefreeze code-results tier, and the independent formal-document audit also
passes. Paper and release remain later gates.

## 2. Surface envelope, field support, and the two actions

The surface divided-discriminant bad-prime envelope is

\[
\{2,3,5,181,283,997,1801,2346241,q\},
\]

where

\[
q=14932047182473291995860108491583652133938007263719.
\]

The exact finite ramified support of both \(E\) and its normal closure \(K\) is

\[
\{3,5,181,283,997,1801,2346241,q\}.
\]

In the displayed nine-prime envelope order, the exponent vector of
\(\operatorname{Disc}(E)\) is

\[
(0,46,36,18,6,18,6,18,6).
\]

Thus \(2\) belongs to the surface envelope but is unramified in both fields.

The line action decomposes as

\[
\mathbf Q[27]\simeq \mathbf 1\oplus V_6\oplus V_{20}.
\]

The 27-line and 36-double-six actions are complementary group-theoretic
carriers. Their wild local partitions are

\[
\begin{array}{c|cc}
 & 27\text{-carrier} & 36\text{-carrier}\\
\hline
p=3 & (3,6,9,9) & (3,3,3,9,18)\\
p=5 & (1,1,5,5,5,10) & (1,5,10,10,10).
\end{array}
\]

The two frozen degree-36 polynomials do not have symmetric evidentiary roles.
The theta resolver alone is `KRASNER_CERTIFIED_AUTHORITY`; the delta resolver
is `BOUNDED_NON_RESULT_NONDEPENDENCY`, neither a theorem dependency nor
corroborating evidence. At \(p=3\), theta is stable, monic, simple, and
multiplies back at each precision in \([900,950,1000]\). Its factor degrees are
\((3,3,3,9,18)\), its global polynomial-discriminant exponent is \(886\), and
twice its largest factor-polynomial discriminant exponent is \(538\). At
\(p=5\), the corresponding data are degrees \((1,5,10,10,10)\), global exponent
\(746\), and twice-largest-factor bound \(246\). Every certified precision
exceeds both applicable bounds. Delta supplies no premise or cross-check.

## 3. Wild inertia at \(3\)

The maximal-order branches are

\[
(e,f,d)=(3,1,3),(6,1,7),(9,1,18),(9,1,18),
\]

so \(v_3(\operatorname{Disc}(E))=46\).

The exhaustive scan of all 350 subgroup classes in GAP's `U4(2).2` Table of
Marks finds exactly three raw simultaneous orbit-pattern hits:

- ToM 140, order \(18\), `IdGroup(18,4)`;
- ToM 142, order \(18\), `IdGroup(18,3)`;
- ToM 206, order \(36\), `IdGroup(36,10)`.

ToM 206 cannot be inertia because its putative tame quotient is the noncyclic
group \(V_4\), but it can be a decomposition overgroup. Normality and cyclic
residue-quotient tests give the complete valid list

\[
(D,I,|D/I|)=(140,140,1),(142,142,1),(206,140,2),(206,142,2).
\]

The deep \(C_3\) choice is not assumed. Across these valid pairs, the
order-three profile inventory is ToM 6 with multiplicity two, ToM 7 with
multiplicity one, and ToM 8 with multiplicity one. Exact `Fraction`
arithmetic starts from base different vector \((2,5,8,8)\), one-layer
\(C_3^2\) contribution \((1,2,4,4)\), and deep-layer contributions

\[
\begin{array}{c|c|c}
\text{profile} & \text{deep contribution} & (r,s)\\
\hline
\text{ToM 6} & (1/3,2/3,1,1) & (7,-18)\\
\text{ToM 7} & (0,0,1,1) & (1,6)\\
\text{ToM 8} & (1/3,2/3,1,1) & (7,-18).
\end{array}
\]

The negative value \(s=-18\) rules out ToM 6 and ToM 8. ToM 7 is the unique
nonnegative integral solution and forces

\[
I_1=C_3^2,\qquad I_2=\cdots=I_7=C_3,\qquad I_8=1.
\]

Serre's formula in *Local Fields*, Chapter IV, §2, Proposition 9, printed
pages 69--70,

\[
\theta_i(s\tau s^{-1})=\theta_0(s)^i\theta_i(\tau),
\]

then finishes the embedding classification. The final nonzero grade is odd,
so the tame involution must invert the deep \(C_3\). ToM 140 has this action,
whereas ToM 142 centralizes it. The final surviving pairs are

\[
(D,I)=(140,140),\qquad (206,140).
\]

Thus the filtered inertia is unique,

\[
I_0=\text{ToM 140}\cong(C_3^2):C_2,\quad I_1=C_3^2,\quad
I_2=\cdots=I_7=C_3,\quad I_8=1,
\]

while \(|D_3|\in\{18,36\}\). The decomposition-group choice is an explicit
nondependency for every inertia, conductor, and discriminant conclusion. The
resulting local invariants are

\[
\operatorname{Sw}_3(V_6,V_{20})=(5,18),\qquad
a_3(V_6,V_{20})=(11,35).
\]

## 4. Wild inertia at \(5\)

The exact local rows are

\[
(1,1,0)^2,\qquad(5,1,7)^3,\qquad(10,1,15),
\]

with total different exponent \(36\). The raw simultaneous orbit-pattern hits
are ToM 147 of order \(20\), ToM 247 of order \(60\), and ToM 295 of order
\(120\). The latter two have nonnormal Sylow-\(5\) subgroups, so the unique
valid decomposition/inertia pair is

\[
(D,I,|D/I|)=(147,147,1),\qquad I_0\cong C_5:C_4.
\]

The branchwise different equations give three wild \(C_5\) layers:

\[
I_1=I_2=I_3=C_5,\qquad I_4=1.
\]

Theta independently certifies the displayed degree-36 partition at all three
wild precisions; delta remains a bounded nonresult. Consequently

\[
\operatorname{Sw}_5(V_6,V_{20})=(3,12),\qquad
a_5(V_6,V_{20})=(7,29).
\]

## 5. Tame places

At each of \(181,997,2346241\), the maximal-order rows are

\[
(3,1,2),\qquad(3,2,2),\qquad(3,6,2).
\]

All three rows occur at each place. Theta alone certifies factor degrees
\((3,6,9,18)\), equivalently double-six inertia type \(3^{12}\), stably at
precisions \([20,30,40]\). Precision \(40\) exceeds both
\(v_p(\operatorname{Disc}(\theta))=24\) and twice the largest
factor-polynomial discriminant exponent, also \(24\). This selects the tame
\(C_3\) subgroup ToM 6 and yields Artin pair \((6,12)\). Delta has global
polynomial-discriminant exponent \(840\) and twice-largest-factor bound \(408\),
so precision \(40\) proves neither bound; it remains
`BOUNDED_NON_RESULT_NONDEPENDENCY`.

For each of \(283,1801,q\), exact singular-locus elimination over all four
affine charts gives one reduced point in chart 0 and unit ideals in the other
three. At the point, the gradient vanishes and the affine Hessian determinant
is a unit. Hensel lifting gives a unique critical point modulo \(p^2\); its
critical value agrees with the integer witness modulo \(p^2\), so the smoothing
parameter has valuation exactly one and the total space is regular and
transverse. Since the residue characteristic is odd, Picard--Lefschetz gives
tame root-reflection inertia.

The exhaustive order-two Table-of-Marks scan uniquely selects subgroup ToM 2,
with line type \(1^{15}2^6\), double-six type \(1^{16}2^{10}\), fixed
dimensions \((5,15)\), Artin pair \((1,5)\), and Swan pair \((0,0)\). This
geometric bridge makes no local \(e/f\) decomposition-row claim.

At \(2\), the zero degree-27 permutation conductor forces inertia to fix all
27 cosets. The line stabilizer is core-free because the 27-line action is
faithful, so inertia in \(K\) is trivial.

## 6. Global closure

Put

\[
A=181\cdot997\cdot2346241=423395612137,\qquad
B=283\cdot1801\cdot q.
\]

The machine-checked formulas are

\[
\mathfrak N(V_6)=3^{11}5^7A^6B,\qquad
\mathfrak N(V_{20})=3^{35}5^{29}A^{12}B^5,
\]

\[
\operatorname{Disc}(E)=3^{46}5^{36}A^{18}B^6,
\]

\[
\operatorname{Disc}(K)=
3^{106560}5^{80352}A^{34560}B^{25920}.
\]

The identity

\[
\mathfrak N(V_6)\mathfrak N(V_{20})=\operatorname{Disc}(E)
\]

is the global checksum supplied by
\(\mathbf Q[27]=\mathbf1\oplus V_6\oplus V_{20}\). Exact
\(\operatorname{Disc}(E)\), together with the faithful 27-line action, also
exhausts the finite ramification support of \(K\).

## 7. Archimedean classification

The exact signature \((3,12)\) gives line type \(1^3 2^{12}\), and
`polsturm(theta36)=4` gives double-six type \(1^4 2^{16}\). The exhaustive
order-two subgroup profiles ToM 2, 3, 4, and 5 have a unique simultaneous
match: **subgroup ToM 5**. In `CharacterTable("U4(2).2")`, the unique
order-two element class with class size \(540\) and centralizer size \(96\) is
**element-class index 17**. The subgroup and character-table indices are
different objects. Under GAP and CTblLib `1.3.1`, complex conjugation has

\[
V_6:(d^+,d^-)=(3,3),\qquad
V_{20}:(d^+,d^-)=(11,9).
\]

## 8. The deliberate firewall

`NO_BAD_EULER_OR_ROOT_NUMBER`: C58 proves no decomposition Frobenius, bad
Euler polynomial or factor, local epsilon factor, local or global root number,
Artin holomorphy, automorphy, analytic continuation, or functional equation.
Even a later resolution of \(D_3\) would not authorize any of those claims;
each requires an independent later theorem.

The project also makes no rational-point, weak-approximation,
Hasse-principle, or Brauer--Manin claim. These exclusions are theorem scope,
not informal caveats.

## 9. Machine evidence and current state

The official prefreeze tuple binds 14 source files and 8 result files, with a
22-entry live inventory and a 21-entry self-excluding scoped manifest. All
eight semantic gates pass; the payload contains 1149 scalar leaves, the
independent checker rejects 1199 rebound mutations, and the project-local test
suite passes all 45 tests. CTblLib is locked to `1.3.1`.

The principal digests are certificate
`456a481368d593f0d015436bf8a3a518d15b4567880fa7726c77d29a259d79ee`,
payload
`fba2dfdf71977d8de6c85635eca6572e0b8a0680570f394af9e3e9e8698f732f`,
schema
`ccbc20eb6e04d00f14cdc0ccf970caebf4d66b4103176515799ddca89639009a`,
check report
`64454700ddaa0bb9ff56c85afa213f038ec6b430bc38ef07e3f22924081d22e9`,
arithmetic evidence
`e374d328a7937c48af93e0b46f54eead5a878f01acc161d8053fe4a10c5f6128`,
group evidence
`0e0b3fd4927b3a8355037b57b86a1e3cc7efe15832be4f5ca76cb4989b71a1fd`,
and scoped manifest
`a18742298722e2bff022b95be8a09806dd774a52ab8e095ebde78924c45ae730`.
The independent post-refresh machine audit is `POSTREFRESH_PASS`.

The formal-document hostile audit is `FORMAL_DOCS_PASS`. No paper source, PDF,
paper hostile-audit artifact, release manifest, archive, or promotion is yet
authorized; `promotion_authorized` remains false. C59--C61 remain separate
later projects.
