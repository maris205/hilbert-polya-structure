# HCS-C58 primary-source and novelty audit

Status: **THEOREM_TARGET_LOCKED; PRIMARY_LOCATORS_RECORDED;
MACHINE_CODE_RESULTS: PREFREEZE_CODE_RESULTS_PASS;
POSTREFRESH_MACHINE_HOSTILE_AUDIT: POSTREFRESH_PASS;
FORMAL_DOCS_PASS; PAPER_PENDING; NOT_RELEASED.**

Search boundary: **2026-08-16 UTC, bounded instance and topic search.**

This audit separates universal ramification theory, cubic-surface precedent,
finite-group/software conventions, and frozen-instance claims that C58
certifies itself. The code/results tier, post-refresh machine audit, and
independent formal-document hostile review have passed; paper-specific
bibliographic rechecking remains a paper prerequisite.

## 1. Primary-source matrix

| key | source and locator | authorized use | not supplied |
|---|---|---|---|
| Serre-Krasner | J.-P. Serre, *Local Fields*, Ch. II §2, Exercises 1--2, printed p. 30 | Krasner/Hensel factor-stability criterion | no C58 precision, polynomial-discriminant exponent, factorization, or instance inequality |
| Serre-LF | Serre, *Local Fields*, Ch. IV §2, Prop. 9, printed pp. 69--70 | tame conjugation on \(G_i/G_{i+1}\): \(\theta_i(s\tau s^{-1})=\theta_0(s)^i\theta_i(\tau)\) | no \(W(E_6)\) subgroup selection, frozen local rows, or deep-profile computation |
| Serre-Artin | Serre, *Local Fields*, Ch. VI §2, Cor. \(1'\), pp. 100--101; Ch. VI §3, Prop. 6 and Cor. 1, pp. 103--104 | Artin conductor and conductor--discriminant identities | no instance conductor or discriminant |
| Saito12 | T. Saito, “The discriminant and the determinant of a hypersurface of even dimension,” *Math. Res. Lett.* 19 (2012), 855--871, DOI 10.4310/MRL.2012.v19.n4.a10; Prop. 2.3, Thm. 3.5, pp. 864--866, cubic-surface specialization p. 870 | divided discriminant, determinant character, and Picard--Lefschetz bridge | no frozen singular point, higher filtration, Swan conductor, or line-field discriminant |
| SGA7 | SGA 7 II, Exp. XV, Picard--Lefschetz formula | reflection monodromy at a transverse ordinary quadratic singularity | no identification or transversality proof for these three fibers |
| EJ-Exp | A.-S. Elsenhans and J. Jahnel, “Experiments with general cubic surfaces,” in *Algebra, Arithmetic, and Geometry I*; Props. 21--22, pp. 651--652 | closest explicit full-\(W(E_6)\) precedent for ramification envelopes and \(p\)-adic factor patterns | no higher groups, maximal-order field discriminant, Swan/Artin conductors, or normal-closure discriminant for this surface |
| EJ-Disc | A.-S. Elsenhans and J. Jahnel, “The discriminant of a cubic surface,” *Geom. Dedicata* 159 (2012), 29--40, DOI 10.1007/s10711-011-9643-7; Thm. 2.12 | cubic discriminant and index-two determinant character | no complete local representation of this instance |
| BFL19 | B. Banwait, F. Fité, and D. Loughran, “Del Pezzo surfaces over finite fields and their Frobenius traces,” *Math. Proc. Camb. Phil. Soc.* 167 (2019), 35--60, DOI 10.1017/S0305004118000166; Table 7.1 | corrected finite-field \(W(E_6)\) class/trace convention | no number-field inertia theorem for the frozen surface |
| PARI | PARI/GP stable number-field manual sections for `nfbasis`, `nfinit`, `idealprimedec`, `nfcertify`, and `polsturm` | semantics of local orders, prime ideals, differents, and real-root counting | no proof that a particular C58 output was produced correctly |
| GAP-CTblLib | GAP `U4(2).2` Table-of-Marks/character-table convention; CTblLib version `1.3.1` | reproducible subgroup, character-table, class-size, and centralizer identifiers | no frozen-instance classification theorem and no license to conflate subgroup and element-class indices |

## 2. Krasner authority and its exact boundary

The 27-line and 36-double-six actions are both group-theoretically necessary,
but the two frozen degree-36 polynomials have asymmetric evidentiary roles.
Theta alone is `KRASNER_CERTIFIED_AUTHORITY`; delta is
`BOUNDED_NON_RESULT_NONDEPENDENCY`, neither theorem dependency nor
corroborating evidence.

At \(p=181,997,2346241\), theta is stable at precisions \([20,30,40]\). Its
global polynomial-discriminant exponent and twice-largest-factor bound are
both \(24\); precision \(40\) exceeds both and certifies degrees
\((3,6,9,18)\). Delta has global exponent \(840\) and twice-largest-factor
bound \(408\), so precision \(40\) certifies neither.

At \(p=3\), theta is stable, monic, simple, and multiplies back at every
precision in \([900,950,1000]\); its factor degrees are \((3,3,3,9,18)\),
global exponent \(886\), and twice-largest-factor bound \(538\). At \(p=5\),
the corresponding values are degrees \((1,5,10,10,10)\), global exponent
\(746\), and bound \(246\). Every certified precision exceeds both applicable
bounds. Serre-Krasner authorizes the stability implication; the producer and
checker prove each C58 inequality and factorization.

Polynomial discriminants occur only in these Krasner bounds. They do not
replace branch differents or either field discriminant.

## 3. Exact Serre use and complete group scan

If \(s\in G_0\) and \(\tau\in G_i/G_{i+1}\), Serre IV §2 Proposition 9 gives

\[
\theta_i(s\tau s^{-1})=\theta_0(s)^i\theta_i(\tau).
\]

For C58, \(G_7/G_8=C_3\), the nontrivial element of \(I_0/I_1=C_2\) has
\(\theta_0(s)=-1\), and odd exponent \(7\) forces inversion. This excludes the
embedding that centralizes the required deep \(C_3\).

Serre supplies this law, not the exhaustive instance classification. The C58
machine bundle separately certifies:

- all raw \(p=3\) hits ToM 140, 142, and 206;
- all valid triples
  \((140,140,1),(142,142,1),(206,140,2),(206,142,2)\);
- the fact that ToM 206 is a possible decomposition overgroup only;
- the deep-profile inventory ToM 6 with multiplicity two, ToM 7 once, and ToM
  8 once;
- exact `Fraction` solutions \((7,-18),(1,6),(7,-18)\), respectively;
- deep ToM 7 and final survivors \((D,I)=(140,140),(206,140)\).

At \(p=5\), the same bundle certifies raw hits ToM 147, 247, and 295 and
excludes the latter two by Sylow-\(5\) nonnormality, leaving uniquely
\((D,I,|D/I|)=(147,147,1)\). Neither the Table of Marks nor a source citation
supplies these frozen-instance conclusions without reconstruction.

## 4. Picard--Lefschetz and reflection primes

For each of \(283,1801,q\), the instance proof contains every required link:

1. exact singular-locus elimination over four affine charts;
2. one reduced singular point in chart 0 and unit ideals in the other charts;
3. vanishing gradient and unit affine Hessian determinant;
4. first Hensel correction and a unique critical point modulo \(p^2\);
5. congruence of the critical value with the integer witness modulo \(p^2\);
6. smoothing-parameter valuation one and regular/transverse total space;
7. odd residue characteristic and the Picard--Lefschetz implication;
8. exhaustive order-two Table-of-Marks selection of subgroup ToM 2.

The selected reflection has line type \(1^{15}2^6\), double-six type
\(1^{16}2^{10}\), fixed dimensions \((5,15)\), Swan pair \((0,0)\), and Artin
pair \((1,5)\). This bridge makes no local \(e/f\) decomposition-row claim.
Saito and SGA 7 authorize the universal geometric implication; the producer
and checker certify all exact inputs and the group identification.

## 5. General ingredients that are not novel

C58 must not claim novelty for:

- lower and upper ramification filtrations;
- Krasner/Hensel factor stability;
- the tame-character action on graded quotients;
- the Artin conductor formula;
- conductor--discriminant formulas for permutation representations;
- Picard--Lefschetz reflection monodromy;
- Saito's divided-discriminant/determinant theorem;
- \(\mathbf Q[27]=\mathbf1\oplus V_6\oplus V_{20}\);
- published \(W(E_6)\) class, orbit, or trace tables;
- GAP, TomLib, or CTblLib identifiers.

## 6. Frozen-instance claims certified by C58 evidence

The following claims cannot be imported from a source and are certified by the
official C58 machine tuple:

- the nine-prime surface divided-discriminant envelope;
- separate exact eight-prime ramified support of \(E,K\), including exponent
  vector \((0,46,36,18,6,18,6,18,6)\);
- the maximal order, exact \(\operatorname{Disc}(E)\), and all local
  \((e,f,d)\) rows;
- theta-only certified 36-carrier partitions at all tame and wild precisions,
  with delta contributing no evidence;
- complete \(p=3,p=5\) decomposition/inertia inventories;
- the ToM \(6\times2,7,8\) exact-`Fraction` profile exhaustion;
- both wild lower filtrations and all fixed dimensions;
- every local Swan and Artin conductor;
- the full reflection bridge and reflection subgroup ToM 2;
- global conductor and both field-discriminant formulas;
- the infinity identification of **subgroup ToM 5** versus
  **character-table element-class index 17**, with element size \(540\),
  centralizer \(96\), and CTblLib `1.3.1`.

The surface-envelope/field-support distinction is exact:

\[
\begin{aligned}
\mathcal B_Y&=\{2,3,5,181,283,997,1801,2346241,q\},\\
\mathcal R_{E,K}&=\{3,5,181,283,997,1801,2346241,q\}.
\end{aligned}
\]

The signature \((3,12)\) gives line type \(1^3 2^{12}\), while
`polsturm(theta36)=4` gives double-six type \(1^4 2^{16}\). These profiles
select subgroup ToM 5. `CharacterTable("U4(2).2")` then identifies the
matching order-two element as element-class index 17; the indices are not
interchangeable.

## 7. Closest precedent and bounded novelty

Elsenhans--Jahnel compute ramification information for a different
full-\(W(E_6)\) example using \(p\)-adic factor behavior. That is genuine
precedent and forbids presenting “ramified primes of an explicit cubic
surface” as the C58 novelty.

C58's bounded theorem bundle is different: exact local maximal orders,
theta-certified 36-carrier partitions, complete decomposition/inertia and
deep-profile scans, both wild filtered inertia groups, reflection geometry,
Swan/Artin conductors for both nontrivial line constituents, and exact
degree-27 and normal-closure discriminants for this frozen surface.

The bounded search combined “cubic surface,” “27 lines,” “\(W(E_6)\),”
“higher ramification,” “Swan conductor,” and “Artin conductor,” together with
exact searches for the 50-digit prime and claimed large exponents. No prior
treatment of this fixed instance or comparably complete local package was
found within the stated boundary.

Authorized wording:

> For this explicit full-\(W(E_6)\) cubic surface, determine the complete
> filtered-inertia and Artin-conductor data of the two nontrivial constituents
> of the 27-line permutation representation, including both wild primes, and
> derive the exact line-field and normal-closure discriminants.

This is search-bounded. “The first for any cubic surface” is not authorized.

## 8. Alternatives audited and rejected

The degree-240 ordered Steiner-triplet field has nonzero
\(H^1\cong\mathbf Z/3\), but its general classification and explicit
order-three construction are already central in Elsenhans--Jahnel. Without a
new arithmetic consequence, it is too close to C57 for C58.

The frozen C57 quaternion class is explicit, but no executable common-field
identity or local point producing a nonconstant Hilbert evaluation was
certified. Square/nonsquare quartic values at a smooth \(p=1373\) point do not
alone establish nonconstant evaluation.

A tame-only note would be too close to an appendix. C58 is theorem-sized
because it contains both wild filtrations, their exact group embeddings, and
the global closure.

## 9. Evidence and source gates

The official tuple binds 14 source files and 8 result files, a 22-entry live
inventory, and a 21-entry self-excluding scoped manifest. It has 1149 payload
leaves, 1199 rejected rebound mutations, 45 passing tests, and exact CTblLib
version `1.3.1`. Principal SHA-256 values are:

- certificate:
  `456a481368d593f0d015436bf8a3a518d15b4567880fa7726c77d29a259d79ee`;
- payload:
  `fba2dfdf71977d8de6c85635eca6572e0b8a0680570f394af9e3e9e8698f732f`;
- schema:
  `ccbc20eb6e04d00f14cdc0ccf970caebf4d66b4103176515799ddca89639009a`;
- check report:
  `64454700ddaa0bb9ff56c85afa213f038ec6b430bc38ef07e3f22924081d22e9`;
- arithmetic/group evidence:
  `e374d328a7937c48af93e0b46f54eead5a878f01acc161d8053fe4a10c5f6128`
  and
  `0e0b3fd4927b3a8355037b57b86a1e3cc7efe15832be4f5ca76cb4989b71a1fd`;
- scoped manifest:
  `a18742298722e2bff022b95be8a09806dd774a52ab8e095ebde78924c45ae730`.

The paper-stage audit must enforce these gates:

- no source theorem may be upgraded into an instance calculation;
- no Table-of-Marks label may be accepted without reconstructing its action;
- delta may not be promoted to authority, dependency, or corroboration;
- every \(D/I\) pair and deep profile must remain explicit;
- ToM 206 must remain decomposition-only;
- subgroup ToM 5 and element-class index 17 must remain distinct;
- CTblLib version drift requires a fresh machine rebinding;
- no local arithmetic output may come from an undocumented temporary process;
- every source cited in the paper needs an exact locator and precise “does not
  supply” boundary;
- `NO_BAD_EULER_OR_ROOT_NUMBER` must reject any decomposition Frobenius, bad
  Euler polynomial/factor, epsilon factor, root number, Artin holomorphy,
  automorphy, analytic continuation, or functional equation.

The exact \(D_3\) choice is irrelevant to all claimed inertia, conductor, and
discriminant results, but resolving it would not itself prove any prohibited
analytic statement. Formal-document hostile review passes; paper-specific
bibliographic rechecking remains pending before paper authorization.
