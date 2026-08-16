# HCS-C58 exact experiment plan

Status: **THEOREM_TARGET_LOCKED; PREFREEZE_CODE_RESULTS_PASS;
POSTREFRESH_PASS; FORMAL_DOCS_PASS; PAPER_PENDING;
NOT_RELEASED.**

## 1. Objective

Build a project-local, independently replayable certificate for the complete
filtered-inertia and conductor theorem of the frozen degree-27 line field.
The implementation must certify local arithmetic, finite-group classification,
representation characters, and global discriminants without conflating any of
those layers.

## 2. Experiment matrix

| ID | gate | exact task | required output | kill condition |
|---|---|---|---|---|
| X0 | G0 | frozen source import | full hashes, paths, statuses, fresh upstream replay | any byte or semantic drift |
| X1 | G1 | divided discriminant replay | nine-prime surface envelope; exact eight-prime support of E and K; exponent vector `(0,46,36,18,6,18,6,18,6)`; two engines | disagreement or unexplained factor |
| X2 | G1 | global maximal order | 27-element order basis, basis discriminant, \(v_2=0\) | wrong degree, index, or discriminant |
| X3 | G2 | local \(p=3\) order | four normalized \((e,f,d)\) rows, exponent 46 | any missing row or wrong sum |
| X4 | G2 | local \(p=5\) order | six normalized rows, exponent 36 | any missing row or wrong sum |
| X5 | G2 | tame \(C_3\) local orders | three rows at each of \(181,997,2346241\), exponent 18, local index zero | any nonmaximal order |
| X6 | G3 | degree-36 local factors | theta-only authority at tame `[20,30,40]` and wild `[900,950,1000]`; delta bounded nonresult/nondependency | authority or bound drift |
| X7 | G3 | 350-class `U4(2).2` inventory | all p=3,p=5 D/I triples, normalizers, actions, fixed spaces | hidden or deleted survivor |
| X8 | G4 | p=5 filtration | unique `(D,I)=(147,147)`, chain `20,5,5,5,1`, exact different equation | any competing chain |
| X9 | G4 | p=3 filtration | all ToM `6x2,7,8` Fraction profiles; chain `18,9,3^6,1`; ToM 140 by inversion | central or negative-layer survivor |
| X10 | G5 | character/conductor table | fixed dimensions, Swan/Artin pairs, every orbit conductor | fractional or mismatched row |
| X11 | G6 | global and infinity closure | conductors/discriminants; subgroup ToM 5 versus element-class index 17 under CTblLib 1.3.1 | any primewise or index mismatch |
| X12 | G7 | independent hostile prefreeze gate | strict schema/checker/mutations/manifest and `NO_BAD_EULER_OR_ROOT_NUMBER` | any fail-open mutation |

The X numbering is an execution breakdown. G0--G7 remain the only theorem
gate numbering.

## 3. Locked direct local targets

### 3.1 Prime \(3\)

\[
(e,f,d)=(3,1,3),(6,1,7),(9,1,18),(9,1,18),
\]

\[
\sum f d=3+7+18+18=46.
\]

The local factor degrees are

\[
(3,6,9,9),
\]

while the theta resolver alone certifies the degree-36 factor degrees

\[
(3,3,3,9,18).
\]

Theta is stable, monic, simple, and multiplies back at each certified
precision in `[900,950,1000]`. Its global polynomial-discriminant exponent is
886 and its twice-largest-factor bound is 538. Delta is
`BOUNDED_NON_RESULT_NONDEPENDENCY`, not a theorem dependency or corroborating
carrier.

### 3.2 Prime \(5\)

\[
(e,f,d)=(1,1,0)^2,(5,1,7)^3,(10,1,15),
\]

\[
\sum f d=0+0+7+7+7+15=36.
\]

The 27/36 degree patterns are

\[
(1,1,5,5,5,10)
\quad\text{and}\quad
(1,5,10,10,10).
\]

For theta these factors are stable, monic, simple, and multiply back at
precisions `[900,950,1000]`; its global polynomial-discriminant exponent is
746 and its twice-largest-factor bound is 246. Every precision clears both
bounds. Delta remains a bounded nonresult/nondependency.

### 3.3 Tame order-three primes

At each \(p=181,997,2346241\),

\[
(e,f,d)=(3,1,2),(3,2,2),(3,6,2),
\]

\[
\sum f d=2+4+12=18.
\]

At each tame prime, theta is stable at `[20,30,40]`; precision 40 exceeds
both its global and twice-largest-factor polynomial-discriminant bounds, each
24, and certifies degrees `(3,6,9,18)`, or inertia type `3^12`. Delta has
corresponding bounds 840 and 408, so precision 40 certifies neither and delta
is not used.

### 3.4 Reflection primes

At \(p=283,1801,q\), exact four-chart elimination gives one reduced point in
chart 0 and unit ideals elsewhere. Gradient vanishing, a unit affine Hessian,
the unique Hensel critical lift modulo \(p^2\), critical-value congruence,
valuation-one smoothing, and regular transverse total space feed
Picard--Lefschetz in odd residue characteristic. The resulting tame root
reflection is subgroup ToM 2, with line type \(1^{15}2^6\), double-six type
\(1^{16}2^{10}\), Artin pair \((1,5)\), and Swan pair \((0,0)\). No local
\(e/f\) decomposition row is asserted.

## 4. Exact representation targets

At \(p=3\), the fixed dimensions must be

| subgroup | \(\dim V_6^H\) | \(\dim V_{20}^H\) |
|---|---:|---:|
| \(I_0\) | 0 | 3 |
| \(C_3^2\) | 0 | 4 |
| deep \(C_3\) | 4 | 10 |

At \(p=5\),

| subgroup | \(\dim V_6^H\) | \(\dim V_{20}^H\) |
|---|---:|---:|
| \(I_0=C_5:C_4\) | 2 | 3 |
| \(C_5\) | 2 | 4 |

The checker must derive these spaces from exact matrices; table comparison
alone is insufficient.

The exhaustive p=3 Table-of-Marks hits are ToM 140 of order 18, ToM 142 of
order 18, and ToM 206 of order 36. ToM 206 is a possible decomposition
overgroup only, never inertia. The four valid `(D,I,|D/I|)` triples are

\[
(140,140,1),(142,142,1),(206,140,2),(206,142,2).
\]

Across these pairs, exact `Fraction` arithmetic exhausts ToM 6 with
multiplicity two, ToM 7 once, and ToM 8 once. Base vector `(2,5,8,8)`,
one-layer \(C_3^2\) contribution `(1,2,4,4)`, and deep contributions
`(1/3,2/3,1,1)`, `(0,0,1,1)`, `(1/3,2/3,1,1)` give formal solutions
`(7,-18)`, `(1,6)`, `(7,-18)`. Thus only deep ToM 7 survives. Serre IV §2
Proposition 9 requires inversion at final grade 7, leaving
`(D,I)=(140,140),(206,140)` and \(|D_3|\in\{18,36\}\).

At p=5, the raw hits 147/247/295 have orders 20/60/120; nonnormal Sylow-5
subgroups eliminate 247 and 295, leaving only `(147,147,1)`.

## 5. Global arithmetic targets

Let

\[
A=181\cdot997\cdot2346241,\qquad
B=283\cdot1801\cdot
14932047182473291995860108491583652133938007263719.
\]

The exact outputs are

\[
N(V_6)=3^{11}5^7A^6B,
\qquad
N(V_{20})=3^{35}5^{29}A^{12}B^5,
\]

\[
\operatorname{Disc}E=3^{46}5^{36}A^{18}B^6,
\]

\[
\operatorname{Disc}K
=3^{106560}5^{80352}A^{34560}B^{25920}.
\]

Canonical decimal encodings may be shipped as secondary guards. The
prime-power expressions and their derivations are the mathematical objects.

## 6. Adversarial mutations

| mutation | expected gate |
|---|---|
| \(p=3\) deep \(C_3\) multiplicity \(6\to5\) | G4/G5 fail |
| \(p=3\) deep \(C_3\) multiplicity \(6\to7\) | G4/G5 fail |
| inversion action \(\to\) central action | G4 fail by Serre Prop. 9 |
| ToM 140 \(\to\) ToM 142 | G4 fail |
| tame \(C_3\) size-80 \(\to\) size-480 | G3/G5 fail on degree-36 action/characters |
| change one \(e,f,d\) value | G2/G5 fail |
| delete one reflection witness | G1/G5 fail |
| change one global exponent | G6 fail |
| \(|D_3|=18\leftrightarrow36\) | inertia/conductor unchanged; Euler firewall still active |
| producer boolean changed without primitive data | checker must ignore/recompute |
| promote delta to authority or corroboration | G3/G7 fail |
| lower theta precision below either stated bound | G3 fail |
| treat ToM 206 as inertia or delete a valid D/I pair | G3/G4 fail |
| select deep ToM 6 or 8 | exact `Fraction` G4 fail |
| omit any reflection Hensel/Picard--Lefschetz link | G1/G4 fail |
| conflate subgroup ToM 5 with element-class index 17 or drift from CTblLib 1.3.1 | G6/G7 fail |
| insert a forbidden Frobenius/Euler/epsilon/root-number/analytic claim | `NO_BAD_EULER_OR_ROOT_NUMBER` G7 fail |

## 7. Default and slow replay

The default runner should:

1. bind all frozen inputs and normalized raw evidence;
2. reconstruct compact exact consequences;
3. run G0--G7 and mutations;
4. write into a staged directory;
5. promote atomically only after the independent checker passes;
6. clean stages, locks, and caches on success or failure.

Slow PARI order regeneration is an explicit opt-in target. It must have
resource limits, exact commands, and output hashes. The default replay may not
silently spend minutes regenerating data.

## 8. Acceptance sequence

1. Approve source and schema design.
2. Implement producer without promotion.
3. Implement an independent checker from primitive inputs.
4. Add unit and negative tests.
5. Run full G0--G7 in a fresh external work directory.
6. Run a hostile read-only machine audit.
7. Freeze the machine-prefreeze tuple.
8. Re-audit the 13 formal documents against the tuple and freeze their
   external aggregate. **Completed: `FORMAL_DOCS_PASS`.**
9. Authorize paper construction. **Current gate.**

## 9. Current state

All X-rows and all eight G0--G7 gates passed the official refresh and the
independent `POSTREFRESH_PASS` audit. The frozen prepaper machine tuple binds
certificate `456a4813...`, payload `fba2df...`, schema `ccbc20eb...`, check
report `64454700...`, evidence `e374d3...`/`0e0b3f...`, and self-excluding
manifest `a1874229...`. It has 14 code files, 8 results, 22 live files, 21
scoped entries, 1149 payload leaves, 1199 rejected rebound mutations, and 45
passing tests. The independent formal-document hostile review also passes;
paper construction, release, and promotion remain pending.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains active.
