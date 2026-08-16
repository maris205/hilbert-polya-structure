# HCS-C58 paper plan

Status: **MACHINE_CODE_RESULTS: PREFREEZE_CODE_RESULTS_PASS;
POSTREFRESH_MACHINE_HOSTILE_AUDIT: POSTREFRESH_PASS;
FORMAL_DOCS_PASS; PAPER_PENDING; NOT_RELEASED.**

Working title:

> Filtered inertia and Artin conductors of the 27 lines on an explicit cubic
> surface

The exact code/results tier and independent post-refresh machine audit have
passed. No paper source, PDF, compilation report, paper hostile-audit artifact,
release manifest, archive, or promotion is yet authorized.

## 1. Contribution contract

For the frozen Yukawa cubic surface, its degree-27 line field \(E\), and its
\(W(E_6)\)-normal closure \(K\), the paper must prove:

1. filtered inertia at all nine primes in the surface divided-discriminant
   envelope, with trivial inertia at \(2\), hence exact eight-prime field
   ramification support;
2. complete wild filtrations at \(3\) and \(5\), tame \(C_3\) inertia at
   \(181,997,2346241\), and tame root-reflection inertia at \(283,1801,q\);
3. all local Artin and Swan characters on \(V_6,V_{20}\);
4. exact conductors of \(V_6,V_{20}\) and exact discriminants of \(E,K\);
5. the signature and archimedean \(V_6,V_{20}\) multiplicities;
6. why the order-\(18\)/order-\(36\) choice for \(D_3\) changes none of these
   conclusions.

The surface divided-discriminant bad-prime envelope is

\[
\{2,3,5,181,283,997,1801,2346241,q\},
\]

whereas the exact finite ramified support of both fields is

\[
\{3,5,181,283,997,1801,2346241,q\}.
\]

In the displayed envelope order,

\[
\bigl(v_p(\operatorname{Disc}E)\bigr)_p
=(0,46,36,18,6,18,6,18,6).
\]

The scope sentence must appear under its machine-enforced name:

> `NO_BAD_EULER_OR_ROOT_NUMBER`: C58 proves no decomposition Frobenius, bad
> Euler polynomial or factor, local epsilon factor, local or global root
> number, Artin holomorphy, automorphy, analytic continuation, or functional
> equation. Resolving \(D_3\) later would not by itself prove any such claim.

## 2. Abstract contract

The future abstract should say that the surface and field are explicit rather
than generic; exact maximal-order data are combined with the 27-line and
36-double-six actions of \(W(E_6)\); an exhaustive decomposition/inertia scan,
an exact deep-\(C_3\) filtration calculation, and Serre's graded tame-action
formula determine the unique filtered inertia at \(3\); and the resulting
conductors and discriminants are exact.

The abstract must not describe the two degree-36 polynomials as dual local
authorities. The theta resolver alone is `KRASNER_CERTIFIED_AUTHORITY`;
delta is `BOUNDED_NON_RESULT_NONDEPENDENCY`, neither a theorem dependency
nor corroborating evidence. The 36-double-six *action* is a necessary
group-theoretic carrier, while only theta certifies its local partitions.

Novelty superlatives remain prohibited unless the paper-stage source audit
supports them.

## 3. Main theorem suite

### Theorem A: local orders, envelope, and local-factor authority

List the exact \((e,f,d)\) rows:

\[
\begin{array}{c|l}
p & (e,f,d)\text{ rows}\\
\hline
3 & (3,1,3),(6,1,7),(9,1,18)^2\\
5 & (1,1,0)^2,(5,1,7)^3,(10,1,15)\\
181,997,2346241 & (3,1,2),(3,2,2),(3,6,2).
\end{array}
\]

Prove the nine-prime surface envelope, the separate exact eight-prime
ramified support of \(E,K\), and the exponent vector
\((0,46,36,18,6,18,6,18,6)\).

For the degree-36 local partitions, record the exact theta-only bounds:

- at \(p=181,997,2346241\), theta is stable at precisions \([20,30,40]\),
  has global polynomial-discriminant exponent \(24\), twice-largest-factor
  bound \(24\), and degrees \((3,6,9,18)\);
- at \(p=3\), theta is stable, monic, simple, and multiplies back at
  \([900,950,1000]\), with degrees \((3,3,3,9,18)\), global exponent \(886\),
  and twice-largest-factor bound \(538\);
- at \(p=5\), the corresponding data are degrees \((1,5,10,10,10)\), global
  exponent \(746\), and twice-largest-factor bound \(246\).

Every certified precision exceeds both applicable bounds. Delta's global
polynomial-discriminant exponent is \(840\) and its twice-largest-factor bound
is \(408\) at tame precision \(40\); it satisfies neither inequality there and
supplies no theorem evidence at any prime.

### Theorem B: exhaustive filtered-inertia classification

At \(p=3\), the 350-class GAP `U4(2).2` Table-of-Marks scan must report all
raw hits:

\[
\operatorname{ToM}140\ (|H|=18,\operatorname{IdGroup}(18,4)),\quad
\operatorname{ToM}142\ (|H|=18,\operatorname{IdGroup}(18,3)),\quad
\operatorname{ToM}206\ (|H|=36,\operatorname{IdGroup}(36,10)).
\]

ToM 206 is possible only as a decomposition overgroup. The complete valid
triples are

\[
(D,I,|D/I|)=(140,140,1),(142,142,1),(206,140,2),(206,142,2).
\]

Across those pairs, prove the profile inventory ToM 6 with multiplicity two,
ToM 7 once, and ToM 8 once. The exact `Fraction` ledger is

\[
\begin{array}{c|c|c}
\text{profile} & \text{deep contribution} & (r,s)\\
\hline
6 & (1/3,2/3,1,1) & (7,-18)\\
7 & (0,0,1,1) & (1,6)\\
8 & (1/3,2/3,1,1) & (7,-18).
\end{array}
\]

Here the base different vector is \((2,5,8,8)\) and the one-layer
\(C_3^2\) contribution is \((1,2,4,4)\). Only deep subgroup ToM 7 yields a
nonnegative integral filtration. Serre IV §2 Proposition 9 at final grade
\(7\) requires inversion and rejects central ToM 142. Conclude

\[
I_0=\operatorname{ToM}140,\quad I_1=C_3^2,\quad
I_2=\cdots=I_7=C_3,\quad I_8=1,
\]

with final survivors

\[
(D,I)=(140,140),(206,140).
\]

At \(p=5\), list all raw hits ToM 147, 247, and 295, of orders \(20,60,120\)
and `IdGroup` labels \((20,3),(60,5),(120,34)\). Nonnormal Sylow-\(5\)
subgroups exclude ToM 247 and 295, leaving uniquely

\[
(D,I,|D/I|)=(147,147,1),\quad
I_1=I_2=I_3=C_5,\quad I_4=1.
\]

### Theorem C: tame reflection bridge and local characters

For each of \(283,1801,q\), prove every link in the geometric bridge: exact
singular-locus elimination on four affine charts, one reduced chart-0 point,
unit ideals on the other charts, vanishing gradient, unit affine Hessian,
unique Hensel critical lift modulo \(p^2\), critical-value congruence, smoothing
parameter of valuation one, and regular/transverse total space. Odd residue
characteristic and Picard--Lefschetz then give tame root-reflection inertia.

The exhaustive order-two scan must select subgroup ToM 2, with line type
\(1^{15}2^6\), double-six type \(1^{16}2^{10}\), fixed dimensions \((5,15)\),
Artin pair \((1,5)\), and Swan pair \((0,0)\). Make no local \(e/f\) row claim
at these primes.

Prove the complete local conductor table:

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

### Theorem D: global arithmetic and infinity type

With

\[
A=423395612137,\qquad
B=283\cdot1801\cdot
14932047182473291995860108491583652133938007263719,
\]

prove

\[
\begin{aligned}
\mathfrak N(V_6)&=3^{11}5^7A^6B,\\
\mathfrak N(V_{20})&=3^{35}5^{29}A^{12}B^5,\\
\operatorname{Disc}(E)&=3^{46}5^{36}A^{18}B^6,\\
\operatorname{Disc}(K)&=
3^{106560}5^{80352}A^{34560}B^{25920}.
\end{aligned}
\]

The signature \((3,12)\) gives line type \(1^3 2^{12}\), and
`polsturm(theta36)=4` gives double-six type \(1^4 2^{16}\). The unique
simultaneous subgroup match is **subgroup ToM 5**. In
`CharacterTable("U4(2).2")`, the unique order-two element class of size
\(540\) and centralizer size \(96\) is **element-class index 17**. With GAP
and CTblLib `1.3.1`, derive

\[
V_6:(d^+,d^-)=(3,3),\qquad V_{20}:(d^+,d^-)=(11,9).
\]

## 4. Proposed structure and size

| Section | Contents | Estimated pages |
|---|---|---:|
| 1 | Introduction, contribution, and exact firewall | 2--3 |
| 2 | Explicit surface, line field, and frozen upstream inputs | 2--3 |
| 3 | \(W(E_6)\), 27/36 actions, and representation characters | 3--4 |
| 4 | Exact local orders and theta Krasner certificates | 4--5 |
| 5 | \(p=3\): all \(D/I\) pairs, deep profiles, and Serre inversion | 5--6 |
| 6 | \(p=5\), tame \(C_3\), and reflection geometry | 4--5 |
| 7 | Artin/Swan conductors and discriminants | 3--4 |
| 8 | Infinity type and theorem scope | 2--3 |
| Appendices | Schemas, subgroup tables, hashes, checker summaries | 5--7 |

Expected length: approximately 30--40 pages including appendices.

## 5. Essential tables and figures

The paper should include:

- a table separating the nine-prime surface envelope from the eight-prime
  field support and displaying the nine-entry exponent vector;
- one table of all local \((e,f,d)\) rows;
- one theta precision/bound table that labels delta only as a bounded
  nonresult and nondependency;
- tables of all \(p=3,p=5\) raw subgroup hits and valid \(D/I\) pairs;
- the ToM \(6\times2,7,8\) exact-`Fraction` ledger;
- one filtration diagram each for \(p=3\) and \(p=5\);
- one reflection-bridge checklist and the exhaustive ToM 2 profile;
- one fixed-space/character table for every filtration layer;
- one global conductor/discriminant factor table;
- a separate infinity row for subgroup ToM 5 and element-class index 17;
- a scope table separating inertia invariants from prohibited analytic claims.

A decorative figure is unnecessary.

## 6. Proof-critical source locators

The bibliography and proof text must bind claims to:

- Jean-Pierre Serre, *Local Fields*, Chapter II §2, Exercises 1--2, printed
  page 30, for the Krasner/Hensel stability criterion; the source gives no
  C58 instance inequality;
- Serre, Chapter IV §2, Proposition 9, printed pages 69--70, for
  \(\theta_i(s\tau s^{-1})=\theta_0(s)^i\theta_i(\tau)\);
- Serre, Chapter VI §2, Corollary \(1'\), printed pages 100--101, and Chapter
  VI §3, Proposition 6 and Corollary 1, printed pages 103--104, for the
  conductor--discriminant identities;
- SGA 7 II, Exposé XV, for Picard--Lefschetz reflection;
- Takeshi Saito, “The discriminant and the determinant of a hypersurface of
  even dimension,” Proposition 2.3 and Theorem 3.5, printed pages 864--866,
  with the cubic-surface specialization on page 870;
- Elsenhans--Jahnel for explicit cubic-surface/discriminant precedent;
- Banwait--Fité--Loughran, Table 7.1, for the \(W(E_6)\) convention;
- stable PARI/GP manual sections used for local maximal-order routines.

GAP's `U4(2).2` naming and CTblLib `1.3.1` are reproducibility
conventions, not sources of the frozen-instance theorem. SOURCE_AUDIT.md
governs the full bibliographic records and permitted uses.

## 7. Reproducibility appendix contract

The appendix must record:

- all 14 source files, 8 result files, 22 live entries, and the 21-entry
  self-excluding scoped manifest;
- certificate, payload, schema, check-report, evidence, and manifest digests;
- the unique project-local default command and clean replay condition;
- PARI/GP, GAP, TomLib, SmallGrp, and CTblLib `1.3.1` versions;
- the local-output schema, 1149 payload leaves, and all eight passing gates;
- the complete subgroup enumeration and exact rational arithmetic;
- the independent checker and all 1199 rejected rebound mutations;
- all 45 passing tests and the independent `POSTREFRESH_PASS` audit;
- the asymmetric theta/delta authority policy and named firewall leaf.

Raw exploratory transcripts are not paper authorities.

## 8. Paper kill gates

Machine prerequisites and the independent formal-document audit have passed.
The paper itself must fail review if it:

- promotes delta to authority or calls it corroborating evidence;
- omits a raw subgroup hit, valid \(D/I\) pair, or deep profile;
- treats ToM 206 as inertia;
- selects deep ToM 6 or ToM 8;
- omits a Hensel/transversality link in the reflection bridge;
- conflates subgroup ToM 5 with character-table element-class index 17;
- drifts from CTblLib `1.3.1` without a fresh machine rebinding;
- inserts any claim prohibited by `NO_BAD_EULER_OR_ROOT_NUMBER`.

Compilation and release remain later gates:

- [x] formal-document hostile audit passes;
- [ ] LaTeX source exists and compiles deterministically;
- [ ] references and citations have no unresolved warnings;
- [x] mathematical notation agrees with all formal roots at the planning handoff;
- [ ] the PDF passes a hostile paper audit;
- [ ] formal, machine, and paper layers are separately frozen;
- [ ] release manifest and archive are verified;
- [ ] promotion is explicitly authorized.

## 9. Nonclaims to repeat in the paper

The two final possibilities \((D,I)=(140,140),(206,140)\) yield the same
filtered inertia, characters, conductors, and discriminants. They do not
license decomposition Frobenius or analytic local data. The paper must repeat
the complete `NO_BAD_EULER_OR_ROOT_NUMBER` sentence, not merely a shortened
root-number caveat. It must retain the rational-point, weak-approximation,
Hasse-principle, and Brauer--Manin exclusions.

## 10. Current handoff

The code/results tier is `PREFREEZE_CODE_RESULTS_PASS`, all G0--G7 gates
pass, and the independent post-refresh machine audit is `POSTREFRESH_PASS`.
The formal-document hostile audit is `FORMAL_DOCS_PASS` and its external
aggregate is frozen in Route. Paper and release states remain `PAPER_PENDING`
and `NOT_RELEASED`, and `promotion_authorized` remains false.
