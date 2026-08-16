# HCS-C58 experiment tracker

Status: **THEOREM_TARGET_LOCKED; PREFREEZE_CODE_RESULTS_PASS;
POSTREFRESH_PASS; FORMAL_DOCS_PASS; PAPER_PENDING;
NOT_RELEASED.**

Date locked: 2026-08-16.

This ledger records the transition from Phase-1 selection to the official
prefreeze machine tuple. The independent formal-document audit has also
passed. Rows still marked pending belong to paper, commit, archive, or release
work and may not be cited as completed.

## 1. Milestone ledger

| Milestone | State | Evidence or next artifact |
|---|---|---|
| A/B/C hostile comparison | PASS | Alternative A and C kill records in RESEARCH_QUESTION.md |
| Research target selection | LOCKED | Filtered inertia, Artin characters, conductors, and discriminants |
| Primary-source localization | PHASE1 PASS | SOURCE_AUDIT.md, including Serre IV §2, Proposition 9 |
| Exact theorem statement | LOCKED TARGET | THEOREM_PACKAGE.md |
| Conditional derivation | MACHINE PREMISES CERTIFIED | DERIVATION.md and G0–G7 tuple |
| Project-local exact implementation | PREFREEZE_CODE_RESULTS_PASS | Eight gates G0–G7 |
| Independent checker | PASS_PREFREEZE_CODE_RESULTS | `c58_check_report.json`, `64454700...` |
| Machine hostile audit | POSTREFRESH_PASS | Strict read-only audit after mandatory live replay |
| Paper source and PDF | PENDING | No paper directory is authorized at this phase |
| Release | NOT RELEASED | Scoped machine manifest exists; no release commit/archive/promotion authorization |

## 2. Gate tracker

| Gate | Exact purpose | State | Required completion record |
|---|---|---|---|
| G0 | Bind frozen C55/C56/C57 and independent action carriers | PREFREEZE_CODE_RESULTS_PASS | Full self-excluded inventories 47/46/64 |
| G1 | Prove the nine-prime surface envelope, exact eight-prime field support, and global maximal order | PREFREEZE_CODE_RESULTS_PASS | Exact factorization and discriminant certificate |
| G2 | Recompute every local maximal order and branch row | PREFREEZE_CODE_RESULTS_PASS | Exact `e,f,d` rows and differents |
| G3 | Exhaust all 350 `U4(2).2` subgroup classes and theta-only local authority | PREFREEZE_CODE_RESULTS_PASS | Complete D/I and dual-action tables |
| G4 | Recover filtrations by exact `Fraction`, Serre inversion, and the reflection bridge | PREFREEZE_CODE_RESULTS_PASS | Selected/rejected profile witnesses |
| G5 | Compute fixed spaces, Swan terms, and Artin characters | PREFREEZE_CODE_RESULTS_PASS | Character-by-layer equalities |
| G6 | Close conductors, discriminants, and ToM-5/element-17 infinity types under CTblLib 1.3.1 | PREFREEZE_CODE_RESULTS_PASS | Symbolic products and signature authority |
| G7 | Independent checker, 1199 mutation rebounds, manifest, and scope firewall | PREFREEZE_CODE_RESULTS_PASS | `64454700...`; no unresolved blocker |

All eight gates are bound by payload `fba2df...` in certificate `456a4813...`.

## 3. Exact target ledger

Write

\[
q=14932047182473291995860108491583652133938007263719,
\]
\[
A=181\cdot 997\cdot 2346241=423395612137,\qquad
B=283\cdot 1801\cdot q.
\]

The implementation is required to reproduce all of the following simultaneously.

| Place | Filtered inertia target | Local line-field target | Artin target on \((V_6,V_{20})\) |
|---|---|---|---|
| \(2\) | trivial | unramified | \((0,0)\) |
| \(3\) | \(I_0\simeq (C_3^2):C_2\), \(I_1=C_3^2\), \(I_2=\cdots=I_7=C_3\), \(I_8=1\) | \((3,1,3),(6,1,7),(9,1,18)^2\) | \((11,35)\), Swan \((5,18)\) |
| \(5\) | \(I_0\simeq C_5:C_4\), \(I_1=I_2=I_3=C_5\), \(I_4=1\) | \((1,1,0)^2,(5,1,7)^3,(10,1,15)\) | \((7,29)\), Swan \((3,12)\) |
| \(181,997,2346241\) | tame \(C_3\) | all three rows \((3,1,2),(3,2,2),(3,6,2)\) at each prime | \((6,12)\) at each prime |
| \(283,1801,q\) | tame root reflection \(C_2\) | no decomposition-row claim | \((1,5)\) at each prime |

The surface divided-discriminant bad-prime envelope is
`{2,3,5,181,283,997,1801,2346241,q}`; the exact ramified support of both
number fields is the eight-prime set obtained by deleting 2. On the displayed
nine-prime envelope the exponent vector of `Disc(E)` is
`(0,46,36,18,6,18,6,18,6)`. Hence 2 is in the surface envelope but
unramified in both \(E\) and \(K\).

The two degree-36 polynomials are not symmetric authorities. Theta alone is
`KRASNER_CERTIFIED_AUTHORITY`. At tame primes it is stable at `[20,30,40]`,
with global and twice-largest-factor bounds 24/24; at p=3 it is stable and
multiplies back at `[900,950,1000]`, with bounds 886/538; at p=5 the same
precisions clear 746/246. Delta is
`BOUNDED_NON_RESULT_NONDEPENDENCY`, with tame bounds 840/408, and supplies
neither a dependency nor corroboration.

At each reflection prime, exact four-chart uniqueness, unit Hessian, unique
critical Hensel lift modulo \(p^2\), critical-value congruence, valuation-one
smoothing, regular total space, and odd-characteristic Picard--Lefschetz
select tame root-reflection subgroup ToM 2. Its line/double-six types are
\(1^{15}2^6\)/\(1^{16}2^{10}\); the Artin/Swan pairs are
\((1,5)\)/\((0,0)\). This makes no local \(e/f\) row claim.

The required global identities are

\[
\operatorname{Disc}(E)=3^{46}5^{36}A^{18}B^6,
\]
\[
\mathfrak N(V_6)=3^{11}5^7A^6B,\qquad
\mathfrak N(V_{20})=3^{35}5^{29}A^{12}B^5,
\]
\[
\operatorname{Disc}(K)=
3^{106560}5^{80352}A^{34560}B^{25920}.
\]

The identity

\[
\mathfrak N(V_6)\mathfrak N(V_{20})=\operatorname{Disc}(E)
\]

is a mandatory cross-check, not an independent premise. The exact signature
\((3,12)\) gives line type \(1^3 2^{12}\), while
`polsturm(theta36)=4` gives double-six type \(1^4 2^{16}\). The unique
simultaneous subgroup match is ToM 5; separately, the unique matching element
in `CharacterTable("U4(2).2")` is element-class index 17, of size 540 and
centralizer size 96. Under CTblLib 1.3.1 the \((+,-)\)-multiplicities are
\((3,3)\) on \(V_6\) and \((11,9)\) on \(V_{20}\).

## 4. The \(p=3\) decision ledger

The raw orbit-pattern hits are ToM 140/order 18/`IdGroup(18,4)`, ToM
142/order 18/`IdGroup(18,3)`, and ToM 206/order 36/`IdGroup(36,10)`.
ToM 206 has a noncyclic putative tame quotient \(V_4\), so it is never
inertia, but it may be the decomposition group. The complete valid ledger is

| \(D\) ToM | \(I\) ToM | \(|D/I|\) | status before deep/Serre tests |
|---:|---:|---:|---|
| 140 | 140 | 1 | valid |
| 142 | 142 | 1 | valid |
| 206 | 140 | 2 | valid; ToM 206 is D-only |
| 206 | 142 | 2 | valid; ToM 206 is D-only |

Across every row the deep-order-three inventory is ToM 6 twice, ToM 7 once,
and ToM 8 once. With base different `(2,5,8,8)` and the one-layer
\(C_3^2\) contribution `(1,2,4,4)`, the exact `Fraction` ledger is

| Deep profile | contribution | formal `(r,s)` | decision |
|---|---|---|---|
| ToM 6 (multiplicity 2) | `(1/3,2/3,1,1)` | `(7,-18)` | no nonnegative filtration |
| ToM 7 | `(0,0,1,1)` | `(1,6)` | unique admissible profile |
| ToM 8 | `(1/3,2/3,1,1)` | `(7,-18)` | no nonnegative filtration |

Thus \(I_1=C_3^2\), \(I_2=\cdots=I_7=C_3\) with deep subgroup ToM 7,
and \(I_8=1\). Serre, *Local Fields*, Chapter IV §2 Proposition 9 gives
\(\theta_i(s\tau s^{-1})=\theta_0(s)^i\theta_i(\tau)\). At final grade 7
the tame involution must invert, selecting inertia ToM 140 and killing central
ToM 142. The two final pairs are `(D,I)=(140,140)` and `(206,140)`, so
\(|D_3|\in\{18,36\}\) is unresolved but irrelevant to all certified
inertia, conductor, and discriminant claims.

`NO_BAD_EULER_OR_ROOT_NUMBER`: C58 proves no decomposition Frobenius, bad
Euler polynomial/factor, local epsilon factor, local or global root number,
Artin holomorphy, automorphy, analytic continuation, or functional equation.
Even resolving \(D_3\) later would not authorize those independent claims.

## 5. Alternative ledger

| Alternative | Phase-1 evidence | Decision |
|---|---|---|
| Order-three Brauer jump on the ordered Steiner-triplet degree-240 field | Natural first nonzero \(H^1\simeq \mathbf Z/3\), after degree 40/80/120 false doors | DEFERRED: no new arithmetic consequence yet |
| Quaternion evaluation on the C57 degree-36 field | No executable common-field model and no nonconstant Hilbert evaluation | KILLED FOR C58 |
| Tame-only ramification note | Correct but too narrow and risks salami slicing | KILLED |
| Wild theorem using only the 27-line carrier | Does not resolve all inertia-class ambiguity | KILLED; dual 27/36 carrier required |

The \(p=1373\) observation that a target quartic assumes both square and
nonsquare values at smooth points is explicitly not a certificate of a
nonconstant Hilbert evaluation.

## 6. Hash and release ledger

| Artifact | Current value |
|---|---|
| Code commit | null |
| Provenance commit | null |
| Default live replay | PASS (nonmutating; no canonical run hash emitted) |
| Certificate / payload | `456a4813...` / `fba2df...` |
| Schema / independent check | `ccbc20eb...` / `64454700...` |
| Evidence tuple | `e374d3...` / `0e0b3f...` |
| Scoped result aggregate | manifest `a1874229...` (21 entries, self excluded) |
| Machine hostile report | `POSTREFRESH_PASS` (external read-only verdict; no self-hash) |
| Formal package hash | external 13-root aggregate recorded in Route; Route excluded |
| Paper source hash | null |
| PDF hash | null |
| Compilation report hash | null |
| Full-project manifest | null |
| Release archive | null |

The remaining nulls are required and truthful. No C58 commit, paper artifact,
full-project release manifest, or archive yet exists.

## 7. Next actions

1. Begin paper work from the post-refresh machine tuple and audited documents.
2. Compile and hostile-audit the paper.
3. Only then create a release commit, full-project manifest, and archive.

C59–C61 remain contingent and unselected throughout this tracker.
