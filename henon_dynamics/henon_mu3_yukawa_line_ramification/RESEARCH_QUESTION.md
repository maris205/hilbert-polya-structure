# HCS-C58 research question

Status: **THEOREM_TARGET_LOCKED; MACHINE_CODE_RESULTS:
PREFREEZE_CODE_RESULTS_PASS; POSTREFRESH_MACHINE_HOSTILE_AUDIT:
POSTREFRESH_PASS; FORMAL_DOCS_PASS;
PAPER_PENDING; NOT_RELEASED.**

## 1. Primary question and exact boundary

For the frozen cubic surface \(Y/\mathbf Q\), let \(E\) be its degree-27 line
field and \(K\) its \(W(E_6)\)-normal closure. Can one determine, for every
ramified rational prime, the lower-numbered inertia filtration inside
\(W(E_6)\), and from it compute the exact Swan and Artin conductors of
\(V_6,V_{20}\), together with \(\operatorname{Disc}(E)\) and
\(\operatorname{Disc}(K)\)?

At the machine code/results tier, the answer is yes. Its precise boundary is:

> `NO_BAD_EULER_OR_ROOT_NUMBER`: C58 proves no decomposition Frobenius, bad
> Euler polynomial or factor, local epsilon factor, local or global root
> number, Artin holomorphy, automorphy, analytic continuation, or functional
> equation. Even a later resolution of \(D_3\) would not by itself authorize
> any such claim; each requires an independent theorem.

## 2. Locked mathematical formulation

Write

\[
\mathbf Q[27]=\mathbf1\oplus V_6\oplus V_{20},\qquad |W(E_6)|=51840.
\]

For a rational representation \(V\), define

\[
a_p(V)=\operatorname{codim}V^{I_0}
+\sum_{i\ge1}\frac{|I_i|}{|I_0|}\operatorname{codim}V^{I_i}.
\]

The theorem package consists of eight exact tasks:

1. distinguish the surface divided-discriminant envelope
   \(\{2,3,5,181,283,997,1801,2346241,q\}\) from exact ramified support
   \(\{3,5,181,283,997,1801,2346241,q\}\) of both \(E,K\), and prove exponent
   vector \((0,46,36,18,6,18,6,18,6)\);
2. exhaust all \(p=3\) decomposition/inertia pairs and determine the unique
   filtered-inertia class;
3. exhaust all \(p=5\) candidates and determine its unique filtration;
4. determine tame \(C_3\) subgroup ToM 6 at \(181,997,2346241\) from the
   theta-only certified 36-carrier partition;
5. establish the complete four-chart/Hensel/Picard--Lefschetz bridge and
   exhaustive reflection subgroup ToM 2 at \(283,1801,q\);
6. compute every local \(a_p(V_6),a_p(V_{20})\) and Swan conductor;
7. derive the exact global conductors and both field discriminants;
8. distinguish archimedean subgroup ToM 5 from character-table element-class
   index 17 under CTblLib `1.3.1` and determine the plus/minus dimensions.

Here

\[
q=14932047182473291995860108491583652133938007263719.
\]

## 3. Surface envelope and locked local table

The surface divided-discriminant bad-prime envelope is

\[
\mathcal B_Y=\{2,3,5,181,283,997,1801,2346241,q\},
\]

but the exact finite ramified support of \(E\) and \(K\) is

\[
\mathcal R_{E,K}=\{3,5,181,283,997,1801,2346241,q\}.
\]

On \(\mathcal B_Y\), in the displayed order,

\[
\left(v_p(\operatorname{Disc}E)\right)_p
=(0,46,36,18,6,18,6,18,6).
\]

| prime | filtered-inertia conclusion | degree-27 local rows | \((a_p(V_6),a_p(V_{20}))\) |
|---:|---|---|---:|
| \(2\) | \(1\) | \(v_2(\operatorname{Disc}E)=0\) | \((0,0)\) |
| \(3\) | \(I_0=\operatorname{ToM}140,\ I_1=C_3^2,\ I_2=\cdots=I_7=C_3\) with deep subgroup ToM 7, \(I_8=1\) | \((3,1,3),(6,1,7),(9,1,18)^2\) | \((11,35)\) |
| \(5\) | \(I_0=\operatorname{ToM}147,\ I_1=I_2=I_3=C_5,\ I_4=1\) | \((1,1,0)^2,(5,1,7)^3,(10,1,15)\) | \((7,29)\) |
| \(181,997,2346241\) | tame \(C_3\), subgroup ToM 6 | \((3,1,2),(3,2,2),(3,6,2)\) | \((6,12)\) |
| \(283,1801,q\) | tame root reflection, subgroup ToM 2 | no \(e/f\) row claim | \((1,5)\) |

All three displayed tame \(C_3\) rows occur at each of
\(181,997,2346241\); they are not assigned one row per rational prime.

## 4. Locked degree-36 authority policy

The 27-line and 36-double-six *actions* are both necessary for exact subgroup
classification. The two degree-36 polynomials are not symmetric local
authorities: theta alone is `KRASNER_CERTIFIED_AUTHORITY`, while delta is
`BOUNDED_NON_RESULT_NONDEPENDENCY`, neither dependency nor corroborating
evidence.

At each of \(p=181,997,2346241\), theta is stable at precisions
\([20,30,40]\). Precision \(40\) exceeds both the global
polynomial-discriminant exponent \(24\) and twice-largest-factor bound \(24\),
and certifies degrees \((3,6,9,18)\), equivalently \(3^{12}\). Delta's global
polynomial-discriminant exponent is \(840\), and its twice-largest-factor bound
is \(408\), so precision \(40\) proves neither.

At \(p=3\), theta is stable, monic, simple, and multiplies back at every
precision in \([900,950,1000]\); its degrees are \((3,3,3,9,18)\), global
polynomial-discriminant exponent \(886\), and twice-largest-factor bound
\(538\). At \(p=5\), the corresponding values are degrees
\((1,5,10,10,10)\), exponent \(746\), and bound \(246\). All certified
precisions exceed both applicable bounds. Delta remains a bounded nonresult.

## 5. Complete decomposition/inertia targets

### \(p=3\)

The exhaustive 350-subgroup-class GAP `U4(2).2` scan gives raw hits ToM 140
of order \(18\) (`IdGroup(18,4)`), ToM 142 of order \(18\)
(`IdGroup(18,3)`), and ToM 206 of order \(36\) (`IdGroup(36,10)`).
ToM 206 cannot be inertia because its putative tame quotient is noncyclic
\(V_4\), but it may be a decomposition overgroup. The complete valid triples
are

\[
(D,I,|D/I|)=(140,140,1),(142,142,1),(206,140,2),(206,142,2).
\]

Across all valid pairs, the deep order-three profile inventory is ToM 6 twice,
ToM 7 once, and ToM 8 once. Exact `Fraction` arithmetic uses base different
vector \((2,5,8,8)\), one-layer \(C_3^2\) contribution \((1,2,4,4)\), and

\[
\begin{array}{c|c|c}
\text{profile} & \text{deep contribution} & (r,s)\\
\hline
6 & (1/3,2/3,1,1) & (7,-18)\\
7 & (0,0,1,1) & (1,6)\\
8 & (1/3,2/3,1,1) & (7,-18).
\end{array}
\]

Only ToM 7 yields a nonnegative integral filtration. Serre IV §2 Proposition 9
at final grade \(7\) forces the tame involution to invert the deep \(C_3\),
selecting ToM 140 and excluding central ToM 142. The final pairs are

\[
(D,I)=(140,140),(206,140),\qquad |D_3|\in\{18,36\}.
\]

This is uniqueness of filtered inertia, not uniqueness of the decomposition
group.

### \(p=5\)

The raw simultaneous hits are ToM 147, 247, and 295, of orders \(20,60,120\)
and `IdGroup` labels \((20,3),(60,5),(120,34)\). ToM 247 and 295 have
nonnormal Sylow-\(5\) subgroups. Hence the unique valid triple is

\[
(D,I,|D/I|)=(147,147,1).
\]

The different equations uniquely give three \(C_5\) layers.

## 6. Reflection and archimedean targets

For each of \(283,1801,q\), exact elimination on four affine charts yields one
reduced chart-0 singular point and unit ideals elsewhere. The gradient
vanishes, the affine Hessian is a unit, the Hensel critical point is unique
modulo \(p^2\), and its critical value agrees with the integer witness modulo
\(p^2\). The smoothing parameter therefore has valuation one and the total
space is regular/transverse. Odd residue characteristic and
Picard--Lefschetz give a root reflection. The exhaustive order-two scan
uniquely selects subgroup ToM 2, with line type \(1^{15}2^6\), double-six type
\(1^{16}2^{10}\), fixed dimensions \((5,15)\), Artin pair \((1,5)\), and Swan
pair \((0,0)\).

At infinity, signature \((3,12)\) gives line type \(1^3 2^{12}\), and
`polsturm(theta36)=4` gives double-six type \(1^4 2^{16}\). The unique
simultaneous subgroup match is **subgroup ToM 5**; in
`CharacterTable("U4(2).2")`, the unique order-two element class of size
\(540\) and centralizer size \(96\) is **element-class index 17**. With CTblLib
`1.3.1`,

\[
V_6:(d^+,d^-)=(3,3),\qquad V_{20}:(d^+,d^-)=(11,9).
\]

## 7. Locked global formulas

Put

\[
A=181\cdot997\cdot2346241,\qquad B=283\cdot1801\cdot q.
\]

Then

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

is an independent closure check, not a substitute for branchwise local
different calculations.

## 8. Success criteria and achieved machine tier

The code/results tier succeeds because:

- all 14 project sources and upstream inputs are byte-bound;
- both action carriers are reconstructed, with theta-only local authority and
  delta nondependency enforced;
- every local arithmetic row is independently parsed and normalized;
- all \(p=3,p=5\) raw hits, \(D/I\) pairs, and deep profiles are exhausted;
- the Serre graded-action constraint and exact reflection bridge are executable
  and mutation-tested;
- subgroup ToM 5 and element-class index 17 are separately checked under
  CTblLib `1.3.1`;
- both discriminants are independently reconstructed;
- all G0--G7 gates pass, with 1149 payload leaves and 1199 rejected rebound
  mutations;
- all 45 project tests and independent post-refresh machine audit pass;
- the named firewall is machine-enforced.

The official principal digests are certificate
`456a481368d593f0d015436bf8a3a518d15b4567880fa7726c77d29a259d79ee`,
payload
`fba2dfdf71977d8de6c85635eca6572e0b8a0680570f394af9e3e9e8698f732f`,
schema
`ccbc20eb6e04d00f14cdc0ccf970caebf4d66b4103176515799ddca89639009a`,
check report
`64454700ddaa0bb9ff56c85afa213f038ec6b430bc38ef07e3f22924081d22e9`,
and scoped manifest
`a18742298722e2bff022b95be8a09806dd774a52ab8e095ebde78924c45ae730`.

## 9. Kill criteria for later layers

Kill or rescope the paper/release lane if any later artifact:

- treats the nine-prime surface envelope as field ramification;
- promotes delta to authority, dependency, or corroboration;
- lowers theta precision below either applicable Krasner bound;
- omits a raw group hit, valid \(D/I\) pair, or deep profile;
- treats ToM 206 as inertia or selects ToM 6/8 as the deep subgroup;
- skips a singular-locus, Hessian, Hensel, transversality, or
  Picard--Lefschetz link;
- conflates subgroup ToM 5 with element-class index 17 or drifts from CTblLib
  `1.3.1`;
- infers a conductor only from the global sum;
- hides the order-\(18\)/order-\(36\) decomposition nondependency;
- inserts any claim prohibited by `NO_BAD_EULER_OR_ROOT_NUMBER`.

## 10. Current state

Machine code/results, its post-refresh audit, and the independent formal-doc
hostile review have passed. Paper construction, hostile paper review,
compilation, release, and promotion are pending. Status remains
`PAPER_PENDING / NOT_RELEASED`, and `promotion_authorized` is false.
