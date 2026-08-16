# HCS-C58 implementation checklist

Status: **PREFREEZE_CODE_RESULTS_PASS; POSTREFRESH_PASS;
FORMAL_DOCS_PASS; PAPER_PENDING; NOT_RELEASED.**

Checked machine items are bound by the official prefreeze tuple and its
read-only post-refresh hostile audit. The independent formal-document audit
also passes. Paper, commit, archive, promotion, and release items remain
separate and are not inferred from either pass.

## A. Research and scope lock

- [x] Compare candidates A, B, and C under a hostile kill-first review.
- [x] Lock candidate B: exact filtered inertia, Artin characters, conductors,
  and discriminants for the 27-line field and its Galois closure.
- [x] Lock the dual 27/36 action-carrier method.
- [x] Enforce exact leaf `NO_BAD_EULER_OR_ROOT_NUMBER`: no decomposition
  Frobenius, bad Euler polynomial/factor, local epsilon factor, local/global
  root number, Artin holomorphy, automorphy, analytic continuation, or
  functional equation; resolving \(D_3\) later would not authorize them.
- [x] Keep C59–C61 contingent and unselected.

## B. G0: frozen-input binding

- [x] Inventory every C55, C56, and C57 input consumed by C58 (self-excluded
  full inventories 47/46/64).
- [x] Record the exact frozen path and SHA-256 digest of each input.
- [x] Verify the degree-27 line polynomial and the two degree-36 resolvents
  against their upstream contracts.
- [x] Bind theta alone as `KRASNER_CERTIFIED_AUTHORITY`, delta as
  `BOUNDED_NON_RESULT_NONDEPENDENCY`, and prove no derived leaf depends on or
  cites delta as corroboration.
- [x] Verify the faithful 27-line \(W(E_6)\) action and the degree-36
  double-six action independently.
- [x] Reject staged, temporary, cache, or untracked substitute inputs.
- [x] Produce a machine-readable source-binding report.

## C. G1: global discriminant support

- [x] Reconstruct the divided discriminant and its nine-prime surface
  bad-prime envelope `{2,3,5,181,283,997,1801,2346241,q}`.
- [x] Distinguish the exact ramified support of both \(E\) and \(K\) as the
  eight-prime set obtained by deleting 2.
- [x] Bind the `Disc(E)` exponent vector on the surface envelope as
  `(0,46,36,18,6,18,6,18,6)`.
- [x] Prove the global order is maximal, or supply equivalent local maximality
  certificates at every discriminant prime.
- [x] Verify \(p=2\) is absent from the field discriminant.
- [x] Use the zero permutation conductor and the core-free line stabilizer
  (faithful 27-line action) to prove \(p=2\) is also unramified in \(K\).
- [x] Define
  \(A=181\cdot997\cdot2346241=423395612137\) and
  \(B=283\cdot1801\cdot q\) with the locked value of \(q\).
- [x] Check \(\operatorname{Disc}(E)=3^{46}5^{36}A^{18}B^6\).

## D. G2: exact local arithmetic

- [x] At \(p=3\), recompute the four rows
  \((3,1,3),(6,1,7),(9,1,18),(9,1,18)\).
- [x] At \(p=5\), recompute
  \((1,1,0)^2,(5,1,7)^3,(10,1,15)\).
- [x] At each of \(181,997,2346241\), recompute all three rows
  \((3,1,2),(3,2,2),(3,6,2)\).
- [x] Verify tame theta stability at `[20,30,40]`, with authority precision 40
  clearing the exact bounds 24/24 and factor degrees `(3,6,9,18)`.
- [x] Verify wild theta stability and multiplyback at `[900,950,1000]`,
  clearing p=3 bounds 886/538 and p=5 bounds 746/246.
- [x] Negatively verify that delta's tame bounds 840/408 are not cleared at
  precision 40 and that delta supplies no tame or wild conclusion.
- [x] Check \(\sum f_i d_i=46\) at \(3\), \(36\) at \(5\), and \(18\)
  at each tame \(C_3\) prime.
- [x] Store raw exact output and a normalized schema-validated report.

## E. G3: complete subgroup discrimination

- [x] Enumerate all 350 subgroup conjugacy classes in GAP's `U4(2).2`
  Table of Marks.
- [x] Compute orbit partitions on both the 27-line and degree-36 carriers.
- [x] Filter by all local \(e,f,d\) rows, not merely total discriminant
  exponents.
- [x] Prove p=3 raw hits 140/142/206 and the exact valid triples
  `(140,140,1)`, `(142,142,1)`, `(206,140,2)`, `(206,142,2)`.
- [x] Prove ToM 206 is a decomposition overgroup only, never inertia.
- [x] Prove p=5 raw hits 147/247/295 and reject 247/295 by nonnormal
  Sylow-5 subgroups, leaving `(147,147,1)`.

## F. G4: ramification filtrations

- [x] Exhaust deep profiles ToM 6 with multiplicity two, ToM 7 once, and ToM
  8 once by exact `Fraction` arithmetic.
- [x] Verify base vector `(2,5,8,8)`, one-layer \(C_3^2\) contribution
  `(1,2,4,4)`, and deep contributions `(1/3,2/3,1,1)`, `(0,0,1,1)`,
  `(1/3,2/3,1,1)`.
- [x] Reject formal solutions `(7,-18)` for ToM 6/8 and uniquely select
  `(r,s)=(1,6)` for deep ToM 7.
- [x] Recover
  \(I_0=(C_3^2):C_2\), \(I_1=C_3^2\),
  \(I_2=\cdots=I_7=C_3\), \(I_8=1\) at \(3\).
- [x] Cite Serre, *Local Fields*, IV §2, Proposition 9, printed pages 69–70.
- [x] Apply
  \(\theta_i(s\tau s^{-1})=\theta_0(s)^i\theta_i(\tau)\)
  to \(G_7/G_8\).
- [x] Positively verify inversion for ToM 140.
- [x] Negatively verify that central ToM 142 is impossible.
- [x] Require the final p=3 pairs `(D,I)=(140,140)` and `(206,140)`, with
  \(|D_3|\in\{18,36\}\) an explicit nondependency.
- [x] Recover
  \(I_0=C_5:C_4\), \(I_1=I_2=I_3=C_5\), \(I_4=1\)
  at \(5\).
- [x] Verify tame \(C_3\) inertia at \(181,997,2346241\).
- [x] Verify at \(283,1801,q\): exact four-chart singular-locus uniqueness,
  unit Hessian, unique Hensel critical lift modulo \(p^2\), critical-value
  congruence, valuation-one smoothing, regular total space, and the
  odd-characteristic Picard--Lefschetz bridge.
- [x] Exhaust all order-two profiles and uniquely select root-reflection
  subgroup ToM 2; make no local \(e/f\) row claim.

## G. G5: local characters and conductors

- [x] Compute fixed-space dimensions on \(V_6\) and \(V_{20}\) for every
  ramification layer.
- [x] Derive the Swan tuple \((5,18)\) and Artin tuple \((11,35)\) at \(3\).
- [x] Derive the Swan tuple \((3,12)\) and Artin tuple \((7,29)\) at \(5\).
- [x] Derive \((6,12)\) at each tame \(C_3\) prime.
- [x] Derive \((1,5)\), Swan \((0,0)\), at each reflection prime.
- [x] Verify the branchwise conductor–different identity locally.
- [x] Reject any character table that matches only the total exponent.

## H. G6: global closure

- [x] Verify
  \(\mathfrak N(V_6)=3^{11}5^7A^6B\).
- [x] Verify
  \(\mathfrak N(V_{20})=3^{35}5^{29}A^{12}B^5\).
- [x] Verify
  \(\mathfrak N(V_6)\mathfrak N(V_{20})=\operatorname{Disc}(E)\).
- [x] Verify
  \(\operatorname{Disc}(K)=
  3^{106560}5^{80352}A^{34560}B^{25920}\).
- [x] Verify \(\operatorname{sig}(E)=(3,12)\) and
  `polsturm(theta36)=4`.
- [x] Identify complex conjugation's subgroup class as ToM 5 and its separate
  `CharacterTable("U4(2).2")` element-class index as 17.
- [x] Bind element-class size 540, centralizer size 96, and CTblLib 1.3.1.
- [x] Verify infinity multiplicities \((3,3)\) on \(V_6\) and \((11,9)\)
  on \(V_{20}\).

## I. G7: independent and hostile verification

- [x] Build an independent checker that does not import derived answers.
- [x] Compare the two action carriers and all local/global invariants.
- [x] Mutate each filtration break and require failure.
- [x] Replace ToM 140 by ToM 142 and require the Serre test to fail.
- [x] Mutate one local different exponent and require the global identity to
  fail.
- [x] Reject delta promotion/corroboration, lowered theta authority precision,
  a deleted D/I pair, ToM 206 as inertia, and deep ToM 6/8 selection.
- [x] Reject an incomplete reflection lift, subgroup-ToM/element-class index
  conflation, or CTblLib version drift.
- [x] Inject every `NO_BAD_EULER_OR_ROOT_NUMBER` forbidden claim and require
  the scope firewall to fail.
- [x] Verify deterministic output under a clean unique default run and its
  mandatory nonmutating live replay.
- [x] Verify no stage files, locks, caches, or temporary authorities remain.
- [x] Produce the 21-entry self-excluding scoped manifest `a1874229...` and
  obtain the independent `POSTREFRESH_PASS` verdict.

## J. Documentation, paper, and release

- [x] Create the 13 Phase-1 root Markdown documents.
- [x] Create the Phase-1 Route-A evaluation.
- [x] Populate machine identifiers after G0–G7 pass: certificate
  `456a4813...`, payload `fba2df...`, schema `ccbc20eb...`, check
  `64454700...`, and evidence `e374d3...`/`0e0b3f...`.
- [x] Record code/results counts 14/8/22/21, gates 8, leaves 1149/1199, and
  tests 45.
- [x] Obtain an independent hostile audit of all updated formal theorem
  statements and freeze their external aggregate/Route hashes.
- [ ] Draft the paper only after the machine layer is frozen.
- [ ] Compile and hostile-audit the PDF.
- [ ] Freeze code/results, formal documentation, and paper in separate layers.
- [ ] Create a self-excluding full-project manifest.
- [ ] Create and verify the release archive.
- [ ] Authorize promotion.

## Completion rule

The machine prefreeze and formal-document layers are complete and independently
audited. HCS-C58 is not released until the remaining unchecked paper, commit,
full-manifest, archive, promotion, and release items have exact evidence.
