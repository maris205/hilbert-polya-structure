# HCS-C58: filtered inertia and Artin conductors of the 27 lines

Status: **MACHINE_CODE_RESULTS: PREFREEZE_CODE_RESULTS_PASS;
POSTREFRESH_MACHINE_HOSTILE_AUDIT: POSTREFRESH_PASS;
FORMAL_DOCS_PASS; PAPER_PENDING; NOT_RELEASED.**

HCS-C58 proves the complete filtered-inertia, conductor, and discriminant
package for the frozen degree-27 line field of the HCS-C55 cubic surface.
HCS-C56 proved that its normal closure has Galois group \(W(E_6)\), and HCS-C57
supplied both exact degree-36 polynomial identities and the double-six action
used by the local subgroup classifier.

The polynomial roles are deliberately asymmetric. The theta resolver alone is
`KRASNER_CERTIFIED_AUTHORITY` for degree-36 local factor partitions. The
delta resolver is `BOUNDED_NON_RESULT_NONDEPENDENCY`: it is neither a theorem
dependency nor corroborating evidence.

The official C58 code/results tuple has passed all gates G0--G7 and an
independent post-refresh machine audit. The independent formal-document audit
also passes. Paper construction, compilation, release, and promotion remain
pending.

## 1. Frozen objects

Let \(Y/\mathbf Q\) be the frozen smooth cubic surface, \(E/\mathbf Q\) its
degree-27 line field, and \(K/\mathbf Q\) its normal closure. The upstream
contract is

\[
[E:\mathbf Q]=27,\qquad
\operatorname{Gal}(K/\mathbf Q)=W(E_6),\qquad |W(E_6)|=51840.
\]

The line permutation representation decomposes as

\[
\mathbf Q[27\text{ lines}]=\mathbf1\oplus V_6\oplus V_{20}.
\]

Write

\[
q=14932047182473291995860108491583652133938007263719,
\]

\[
A=181\cdot997\cdot2346241=423395612137,\qquad
B=283\cdot1801\cdot q.
\]

## 2. Surface envelope versus exact field ramification

The surface divided-discriminant bad-prime envelope is

\[
\{2,3,5,181,283,997,1801,2346241,q\}.
\]

The exact finite ramified support of both \(E\) and \(K\) is instead

\[
\{3,5,181,283,997,1801,2346241,q\}.
\]

In the displayed nine-prime order, the exponent vector of
\(\operatorname{Disc}(E)\) is

\[
(0,46,36,18,6,18,6,18,6).
\]

Thus \(2\) belongs to the surface envelope but is unramified in both number
fields. The zero degree-27 permutation conductor makes inertia at \(2\) act
trivially on all line-stabilizer cosets. Because the 27-line action is
faithful, the stabilizer is core-free, so inertia is also trivial in \(K\).

## 3. Degree-36 local-factor authority

At the wild primes theta is stable, monic, simple, and multiplies back at each
certified precision in \([900,950,1000]\):

- at \(p=3\), its factor degrees are \((3,3,3,9,18)\), its global
  polynomial-discriminant exponent is \(886\), and twice the largest
  factor-polynomial discriminant exponent is \(538\);
- at \(p=5\), its factor degrees are \((1,5,10,10,10)\), its global exponent
  is \(746\), and its twice-largest-factor bound is \(246\).

Every certified precision exceeds both applicable bounds.

At each of \(p=181,997,2346241\), theta is stable at precisions
\([20,30,40]\). Precision \(40\) exceeds both its global
polynomial-discriminant exponent \(24\) and its twice-largest-factor bound
\(24\), certifying degrees \((3,6,9,18)\), equivalently type \(3^{12}\) on
double-sixes.

Delta has global polynomial-discriminant exponent \(840\) and
twice-largest-factor bound \(408\), so tame precision \(40\) proves neither
bound. Delta remains `BOUNDED_NON_RESULT_NONDEPENDENCY` at wild primes as
well, and no theorem leaf depends on it.

## 4. Filtered inertia at \(p=3\)

The exact maximal-order rows are

\[
(e,f,d)=(3,1,3),(6,1,7),(9,1,18),(9,1,18).
\]

An exhaustive scan of all 350 subgroup classes in GAP's `U4(2).2` Table of
Marks gives exactly these raw simultaneous 27/36 orbit-pattern hits:

- ToM 140, order \(18\), `IdGroup(18,4)`;
- ToM 142, order \(18\), `IdGroup(18,3)`;
- ToM 206, order \(36\), `IdGroup(36,10)`.

ToM 206 cannot be inertia because its putative tame quotient is noncyclic
\(V_4\); it can occur as a decomposition overgroup. The complete valid
decomposition/inertia inventory is

\[
(D,I,|D/I|)=(140,140,1),(142,142,1),(206,140,2),(206,142,2).
\]

Across all four pairs, the deep order-three profile inventory is ToM 6 with
multiplicity two, ToM 7 once, and ToM 8 once. With base different vector
\((2,5,8,8)\) and one-layer \(C_3^2\) contribution \((1,2,4,4)\), exact
`Fraction` arithmetic gives

\[
\begin{array}{c|c|c}
\text{profile} & \text{deep contribution} & (r,s)\\
\hline
\text{ToM 6} & (1/3,2/3,1,1) & (7,-18)\\
\text{ToM 7} & (0,0,1,1) & (1,6)\\
\text{ToM 8} & (1/3,2/3,1,1) & (7,-18).
\end{array}
\]

Only ToM 7 gives a nonnegative integral filtration. It forces

\[
I_1=C_3^2,\qquad I_2=\cdots=I_7=C_3,\qquad I_8=1.
\]

Serre, *Local Fields*, Chapter IV §2 Proposition 9, printed pages 69--70,
requires the tame involution to act by inversion on the odd final grade
\(G_7/G_8\). This selects ToM 140 and rejects central ToM 142. The final pairs
are

\[
(D,I)=(140,140),\qquad(206,140),
\]

so \(|D_3|\in\{18,36\}\), but the filtered inertia is uniquely

\[
I_0=\operatorname{ToM}140\cong(C_3^2):C_2,\quad I_1=C_3^2,\quad
I_2=\cdots=I_7=C_3,\quad I_8=1.
\]

The decomposition choice is a nondependency. The local conductor pairs are

\[
\operatorname{Sw}_3(V_6,V_{20})=(5,18),\qquad
a_3(V_6,V_{20})=(11,35).
\]

## 5. Filtered inertia at \(p=5\)

The exact rows are

\[
(1,1,0)^2,(5,1,7)^3,(10,1,15).
\]

All simultaneous orbit-pattern hits are ToM 147 of order \(20\)
(`IdGroup(20,3)`), ToM 247 of order \(60\) (`IdGroup(60,5)`), and ToM
295 of order \(120\) (`IdGroup(120,34)`). The latter two have nonnormal
Sylow-\(5\) subgroups. Thus

\[
(D,I,|D/I|)=(147,147,1),\quad
I_0\cong C_5:C_4,\quad I_1=I_2=I_3=C_5,\quad I_4=1.
\]

The local conductor pairs are

\[
\operatorname{Sw}_5(V_6,V_{20})=(3,12),\qquad
a_5(V_6,V_{20})=(7,29).
\]

## 6. Tame inertia

At each of \(181,997,2346241\), the maximal-order rows

\[
(3,1,2),(3,2,2),(3,6,2)
\]

combine with theta's certified \(3^{12}\) double-six type to select tame
\(C_3\) subgroup ToM 6. Its Swan pair is \((0,0)\) and its Artin pair is
\((6,12)\).

For each of \(283,1801,q\), exact singular-locus elimination on all four
affine charts gives one reduced point in chart 0 and unit ideals in the other
three. The gradient vanishes and the affine Hessian determinant is a unit. The
unique Hensel critical lift modulo \(p^2\) has critical value congruent to the
integer witness, so the smoothing parameter has valuation exactly one and the
total space is regular/transverse. Odd residue characteristic and
Picard--Lefschetz give tame root-reflection inertia.

The exhaustive order-two Table-of-Marks scan uniquely selects subgroup ToM 2,
with line type \(1^{15}2^6\), double-six type \(1^{16}2^{10}\), fixed
dimensions \((5,15)\), Swan pair \((0,0)\), and Artin pair \((1,5)\). No
local \(e/f\) decomposition row is asserted at a reflection prime.

## 7. Global conductor and discriminant formulas

The machine-checked formulas are

\[
\mathfrak N(V_6)=3^{11}5^7A^6B,\qquad
\mathfrak N(V_{20})=3^{35}5^{29}A^{12}B^5,
\]

\[
\operatorname{Disc}(E)=3^{46}5^{36}A^{18}B^6,
\]

\[
\operatorname{Disc}(K)
=3^{106560}5^{80352}A^{34560}B^{25920}.
\]

The permutation-representation identity gives the checksum

\[
\mathfrak N(V_6)\mathfrak N(V_{20})=\operatorname{Disc}(E).
\]

## 8. Archimedean classification

The exact signature \((3,12)\) gives line type \(1^3 2^{12}\), while
`polsturm(theta36)=4` gives double-six type \(1^4 2^{16}\). The unique
simultaneous order-two subgroup match is **subgroup ToM 5**. In
`CharacterTable("U4(2).2")`, the unique order-two element class of size
\(540\) and centralizer size \(96\) is **element-class index 17**. These are
different indices. GAP and CTblLib `1.3.1` give

\[
E:(r_1,r_2)=(3,12),\qquad
V_6:(d^+,d^-)=(3,3),\qquad
V_{20}:(d^+,d^-)=(11,9).
\]

## 9. G0--G7 machine contract

| gate | certified closure | status |
|---|---|---|
| G0 | 14 C58 sources plus frozen C55/C56/C57 inventories and both actions are byte-bound | `PREFREEZE_CODE_RESULTS_PASS` |
| G1 | surface envelope, eight-prime field support, exponent vector, maximal order, and reflection geometry | `PREFREEZE_CODE_RESULTS_PASS` |
| G2 | every local \((e,f,d)\) row and theta-only Krasner authority, with delta nondependency | `PREFREEZE_CODE_RESULTS_PASS` |
| G3 | all 350 subgroup classes, all \(p=3,p=5\) \(D/I\) candidates, and all orbit profiles | `PREFREEZE_CODE_RESULTS_PASS` |
| G4 | exact ToM \(6\times2,7,8\) `Fraction` exhaustion, both wild filtrations, and Serre inversion | `PREFREEZE_CODE_RESULTS_PASS` |
| G5 | fixed dimensions, Artin/Swan conductors, and conductor--different identities | `PREFREEZE_CODE_RESULTS_PASS` |
| G6 | global conductors/discriminants, reflection ToM 2, and ToM-5/element-17 infinity split under CTblLib `1.3.1` | `PREFREEZE_CODE_RESULTS_PASS` |
| G7 | independent replay, hostile mutations, manifest integrity, and `NO_BAD_EULER_OR_ROOT_NUMBER` | `PREFREEZE_CODE_RESULTS_PASS` |

## 10. Evidence inventory

The official prefreeze layer contains 14 source files and 8 result files. Its
live inventory has 22 entries; its self-excluding scoped manifest binds 21.
The payload has 1149 scalar leaves, the checker rejects 1199 rebound mutations,
all 45 tests pass, and CTblLib is exactly `1.3.1`.

| artifact | SHA-256 |
|---|---|
| `results/c58_certificate.json` | `456a481368d593f0d015436bf8a3a518d15b4567880fa7726c77d29a259d79ee` |
| canonical payload | `fba2dfdf71977d8de6c85635eca6572e0b8a0680570f394af9e3e9e8698f732f` |
| `results/c58_schema.json` | `ccbc20eb6e04d00f14cdc0ccf970caebf4d66b4103176515799ddca89639009a` |
| `results/c58_check_report.json` | `64454700ddaa0bb9ff56c85afa213f038ec6b430bc38ef07e3f22924081d22e9` |
| `results/c58_arithmetic_evidence.json.gz` | `e374d328a7937c48af93e0b46f54eead5a878f01acc161d8053fe4a10c5f6128` |
| `results/c58_group_evidence.json` | `0e0b3fd4927b3a8355037b57b86a1e3cc7efe15832be4f5ca76cb4989b71a1fd` |
| `results/scoped_hash_manifest.json` | `a18742298722e2bff022b95be8a09806dd774a52ab8e095ebde78924c45ae730` |

The clean default replay and independent post-refresh machine audit both
passed. These are prefreeze machine artifacts, not a release manifest.

## 11. Hard scope firewall

`NO_BAD_EULER_OR_ROOT_NUMBER`: C58 proves no decomposition Frobenius, bad
Euler polynomial or factor, local epsilon factor, local or global root number,
Artin holomorphy, automorphy, analytic continuation, or functional equation.
The order-\(18\)/order-\(36\) choice for \(D_3\) is irrelevant to filtered
inertia, conductors, and discriminants, and resolving it later would not by
itself authorize any prohibited claim.

C58 also makes no rational-point, weak-approximation, Hasse-principle,
Brauer--Manin, motive, Riemann-hypothesis, or Hilbert--Pólya conclusion.

## 12. Current handoff

The machine code/results layer is `PREFREEZE_CODE_RESULTS_PASS`, and its
post-refresh hostile audit is `POSTREFRESH_PASS`. The formal-document hostile
audit is `FORMAL_DOCS_PASS`. Paper, PDF, compilation, paper hostile review, full release
manifest, archive, and promotion are absent; status remains
`PAPER_PENDING / NOT_RELEASED`, with `promotion_authorized: false`.
