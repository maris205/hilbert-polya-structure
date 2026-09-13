# Paper 19 Publication-Stage Scope

Date: 2026-08-19 UTC  
Role: separately invoked publication-governance author  
Project root: `papers/19-shiftlike-translate-gcd-obstruction`  
Status: scope complete; canonical publication lock still required; no manuscript authority

## 1. Authority and purpose

This document freezes the publication-stage contract for an anonymous, proof-first, pure-mathematics article. It does not draft, compile, revise, finalize, release, submit, upload, push, or externally communicate anything. The publication-governance author may create exactly this scope and, after exact readback, exactly `experiments/publication_lock.json`. No existing Paper 19 object or batch dashboard may change.

After the lock is written and validated, this author stops. The sole then-current Paper 19 write authority is one fresh independent publication-stage reviewer, who may create `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` only if every frozen check passes. Its final nonempty line must be exactly `PUBLICATION_STAGE_PASS`. A blocker requires the reviewer to write nothing and emit no pass token.

A publication-stage pass records only this governance gate. It does not authorize `paper/main.tex`, `paper/references.bib`, compilation, PDF persistence, revision, finalization, release, submission, upload, repository push, or any external effect.

## 2. Locked identity, story, and hypotheses

The title is exactly:

**Maximum-Dimensional Torus Translates in Sparse Shift-Like Recurrences: Coefficientwise Moduli and a Support-One GCD Obstruction**

The article is anonymous and public-safe. Author, affiliation, email, ORCID, acknowledgment, funding, reviewer, local-system, dashboard, path, hash, lifecycle-token, and private-artifact disclosures are absent from the public manuscript.

The locked story is: character relations first isolate an extremal shadow, and the paper then decides whether translating scalars lift it; the anchored multi-support shadow lifts along the explicit normalized scheme `E_m`, whereas the unique support-one penultimate shadow has no lift for `q>=3` and lifts for `q=2` exactly on the resonant coefficient locus.

The abstract and first two pages distinguish exact character extinction from the non-optimal scalar conclusion for `q>=3`. “Maximum-dimensional” in Part A means exactly `dim H=k-m`. Geometric dimension belongs to a contained translate `xi H`, never to `T_m`.

The common assumptions are an algebraically closed field `Omega` of characteristic zero, `k>=2`, `1<=nu<k`, and `a!=0`. The map, inverse, recurrence orientation, `V_m`, `T_m`, projection bijection, translate characters, ambient generation, independence, saturation, and arithmetic bridge precede the two parts.

Part A assumes actual collected support `P(X)=c+sum_(ell=1)^s b_ell X^(e_ell)` with `0<e_1<...<e_s`, `s>=2`, and all displayed coefficients nonzero, for `1<=m<k`.

Part B assumes `P(X)=c+bX^d` with `a,b,c!=0` and `d>=2`, and uses `g=gcd(k,nu)`, `q=k/g>=2`, `L=(k-nu)/g`, `1<=L<q`, and `gcd(q,L)=1`.

## 3. Exact article shape and page contract

The source has exactly eleven numbered sections, no appendix or supplement, zero figures, images, and diagrams, and zero numerical-result tables. At most one non-numerical theorem/provenance table is allowed if it materially clarifies theorem and predecessor ownership. There is no padding, display inflation, hidden text, forced blank page, or proof deferred outside the main text.

Substantive content is exactly 29 pages, including the abstract and Sections 1--11. References begin only after substantive page 29 and count separately. Total PDF pages equal 29 plus the nonempty reference pages, with no blank or appendix pages.

| Content block | Exact substantive pages |
|---|---:|
| Abstract | 0.35 |
| 1. Introduction | 1.65 |
| 2. Recurrences, character lattices, Laurent bridge, and predecessor boundary | 2.50 |
| 3. Saturated equality rigidity | 2.50 |
| 4. Normalized translates and nonemptiness | 4.00 |
| 5. Fixed-fiber and universal geometry | 3.00 |
| 6. Coefficientwise arithmetic sharpness | 1.50 |
| 7. Exclusive labels and gcd cores | 2.50 |
| 8. Component-height extinction and structural uniqueness | 4.00 |
| 9. Laurent shadow, original windows, and seven labels | 3.50 |
| 10. Scalar obstruction, `q=2` fill, and arithmetic consequences | 2.50 |
| 11. Related work, ownership limits, and conclusion | 1.00 |
| **Total** | **29.00** |

The abstract target is 180--220 words. Page one answers what, why, and so what. All headline conclusions, the `q=2` exception, `q>=3` limitation, and predecessor deductions appear within the first two substantive pages.

Scientific execution is identically zero: no scientific or computational experiment, CAS run, symbolic enumeration, finite-case search used as evidence, numerical run, benchmark, dataset, code, data product, result file, randomness, model, external service, or empirical claim is authorized or required.

## 4. Complete theorem contract

Every item is visibly stated and completely proved in the main text.

### Part A

- `TA1`: if `xi H subset V_m` and `dim H=k-m`, then `H=H_m`.
- `TA2`: geometric points of the explicit locally closed normalized scheme `E_m` classify all normalized maximum-dimensional translates, with the exact active interval, root equations, both open nonvanishing families, and coordinatewise inverse reconstruction.
- `TA3`: `E_m` is nonempty for every allowed coefficient tuple; squarefree `P` gives `delta^alpha_m` smooth geometric components; arbitrary `P` gives `r^alpha_m` reduced geometric components and the stated active nilpotent directions.
- `TA4`: over fixed actual support and its coefficient torus, the universal family is an explicit open product of root schemes and a free torus, flat relative lci, smooth over the discriminant complement, with the stated completed fiber local equations.
- `CA1`: for every coefficient tuple, a compatible finite extension and compatible finitely generated group make `T_(k-1)` infinite, while the delimited Paper 17 terminal result plus `EXT-L` gives finite `T_k` for every finite-rank group.

### Part B

- `TB1`: every support-one local character identity has exactly one exclusive `A`, `B`, `C`, or `Z` label and the locked scalar sign rule.
- `TB2`: original indices split into exactly `g` independent gcd residue cores.
- `TB3`: every arbitrary-rank nonzero scaling component has integer heights and satisfies `F_(j+q)=F_j+T F_(j+L)` with independent component colors.
- `TB4`: `q^2` consecutive core equations extinguish every involved character.
- `TB5`: `q^2-1` consecutive core equations admit one unique nonzero colored Laurent shadow up to its generator, with the central delta block, complete Laurent formulas, semigroup guard, and first collision `1+T^q`.
- `TB6`: at `m=kq-1` only residue `g-1` may carry the shadow; at `m=kq` all residues vanish, with original-window coverage through `u_(kq+k-1)`.
- `TB7`: for `q>=3` the unique shadow has the seven locked labels, with all zero and index guards.
- `TB8`: for `q>=3` those labels have no scalar lift, so `V_(kq-1)` has no positive-dimensional torus translate.
- `TB9`: for `q=2` such a translate exists at `m=kq-1` iff `a=-1` and `b c^(d-1)=-1`, including the general-`g` inactive-residue fill.
- `CB1`: `T_(kq)` is finite for every finite-rank group; `T_(kq-1)` is finite for `q>=3` and nonresonant `q=2`, while resonant `q=2` admits compatible infinitude. No effective count is claimed.

## 5. Non-negotiable proof details

Part A first proves middle collapse, then that the predecessor quotient is free and its lattice saturated, then uses equal-rank kernels for `H=H_m`. The normalized scheme uses `A_m=[max(0,m-nu),min(m,k-nu))` and `alpha_m=min(m,k-m,nu,k-nu)`. All reconstruction coordinates and both open families precede `TA2`. Proper-closed avoidance covers every active root tuple, including `alpha_m=m`. Actual support is fixed and all displayed universal coefficients remain invertible. Fiber counts, squarefreeness, reducedness, relative lci, discriminant-complement smoothness, and completed local equations retain their qualifiers.

Part B uses exclusive labels, never a rank-one ansatz. Each equation connects exactly its two nonzero coordinates. Each connected component has its own color `e_C`; torsion-freeness turns `d`-exponent edge weights into integer heights because a nonzero signed cycle would force `v=d^s v`. The recurrence lives in the direct sum of colored Laurent modules. Minimum-height backward tracing, `B` persistence, and the triangular zero set prove `q^2` extinction. For `q^2-1` equations, central-block coverage forces every nonzero component through `N_*=(L+1)q-1`, so disjointness leaves one component.

The explicit formulas are
`G(z)=(1+Tz^L)/(1+Tz^L+z^q)`
and
`H(z)=z^(q-1)/(1+Tz^(q-L)+z^q)`.
Full backward and forward degrees remain below `Lq` and `(q-L)q`, so coprime semigroup uniqueness makes every relevant coefficient zero or one monomial. The next coefficient `1+T^q` proves extinction without enumeration.

The abstract core only puts involved nonzero characters in one cyclic subgroup; unused direct summands are not excluded there. Only after `TB6` kills other original residues, covers every ambient coordinate, and invokes surjectivity of coordinate restrictions onto the actual character lattice may the source conclude `X*(H)=Z w` with primitive `w`. This actual-lattice step is mandatory.

For `q>=3` the seven labels are exactly `L-1:C`, `q-1:B`, `z_*-q:C`, `z_*+L-q:C`, `z_*:Z`, `z_*+L:A`, and `z_*+q:A`, with `z_*=(q-2)L+q-1`. The proof handles both cases of `F_(z_*)=0`, excludes `2L=q`, proves every index lies in `[0,q^2-2]`, and allows compatible coincidences. The scalar chain is `b c^(d-1)=-1`, then `a=-1`, then `2c=0`.

For `q=2` the five active scalars and primitive exponent vector are verified. For each inactive residue when `g>1`, use `Phi(x,y)=(y,c+b y^d-x)` with inverse `Phi^(-1)(x,y)=(c+b x^d-y,x)`; generic initial data avoid finitely many proper coordinate-zero hypersurfaces over the infinite field.

## 6. Thirty-one-item proof DAG

The numbering and dependencies are frozen, main-text, and acyclic.

1. `N01 / Lemma 2.1`, Character independence and ambient generation; common setup.
2. `N02 / Lemma 2.2`, Saturated equal-rank kernels; preliminary lattice algebra.
3. `N03 / Proposition 2.3`, Finite-rank arithmetic bridge; `EXT-L` and the internal torsion/field bridge.
4. `N04 / Theorem 2.4`, Anchored dimension theorem; delimited Paper 17 background.
5. `N05 / Proposition 3.1`, Anchored middle collapse; `N01`.
6. `N06 / Lemma 3.2`, Free quotient and saturation; `N05`.
7. `N07 / Theorem 3.3`, `TA1`; `N02`, `N04`, `N06`.
8. `N08 / Lemma 4.1`, Active interval and activity number; Part A definitions.
9. `N09 / Proposition 4.2`, Scalar reconstruction; `N07`, `N08`.
10. `N10 / Theorem 4.3`, `TA2`; `N09`.
11. `N11 / Lemma 4.4`, Root-tuple avoidance; `N08`, `N10`.
12. `N12 / Theorem 4.5`, `TA3`; `N11`.
13. `N13 / Lemma 5.1`, Universal root scheme; fixed-support root algebra.
14. `N14 / Theorem 5.2`, `TA4`; `N10`, `N13`.
15. `N15 / Proposition 5.3`, Completed fiber local structure; `N14`.
16. `N16 / Corollary 6.1`, `CA1`; `N03`, `N04`, `N12`.
17. `N17 / Lemma 7.1`, `TB1`; `N01`.
18. `N18 / Lemma 7.2`, `TB2`; Part B definitions.
19. `N19 / Proposition 7.3`, `TB3`; `N17`, `N18`.
20. `N20 / Lemma 8.1`, Minimum-height persistence and zero triangle; `N19`.
21. `N21 / Theorem 8.2`, `TB4`; `N20`.
22. `N22 / Lemma 8.3`, Central-block coverage; `N20`.
23. `N23 / Theorem 8.4`, structural `TB5`; `N20`, `N22`.
24. `N24 / Proposition 9.1`, backward/forward Laurent formulas; `N19`, `N23`.
25. `N25 / Lemma 9.2`, Coprime semigroup uniqueness; stated coprime lemma.
26. `N26 / Corollary 9.3`, explicit `TB5` and first collision; `N24`, `N25`.
27. `N27 / Proposition 9.4`, `TB6` and actual `X*(H)=Z w`; `N01`, `N21`, `N26`.
28. `N28 / Lemma 9.5`, `TB7`; `N24`, `N25`, `N26`.
29. `N29 / Theorem 10.1`, `TB8`; `N17`, `N27`, `N28`.
30. `N30 / Theorem 10.2`, `TB9`; `N17`, `N18`, `N23`, `N27`.
31. `N31 / Corollary 10.3`, `CB1`; `N03`, `N21`, `N29`, `N30`.

`EXT-L` is the sole indispensable external theorem. The only nonlocal recurrence input is the delimited Paper 17 dimension/terminal background. Source-design notes are not mathematical evidence.

## 7. Citation and predecessor contract

`EXT-L` is Michel Laurent, “Équations diophantiennes exponentielles,” Inventiones mathematicae 78 (1984), 299--327, DOI `10.1007/BF01388597`. It is qualitative only and used after geometry. It supplies no effective count, algorithm, exceptional locus, or positive-characteristic theorem. The manuscript proves the arbitrary-torsion division-hull and finitely generated field bridge; it does not embed an arbitrary large field into `C`.

The verified citation groups are frozen:

- `EXT-L / Laurent84`.
- Bedford--Pambuccian, Bera, Bera--Verma, and Kaur.
- Habegger; Suciu--Yang--Zhao; Corvaja--Levin--Zannier; Dill--Gallinaro; Amoroso--Sombra--Zannier; Martínez; Leroux.
- Ilten--Zotine and Ilten--Kelly.
- Bell--Chen--Hossain; Bell--Ghioca; Ji--Xie--Zhang; Mello--Yasufuku; Zhang's 2026 recurrence paper.
- Portfolio provenance keys `PV16`, `PV17`, and `PV18`.

BibTeX metadata comes only from the locked citation ledger or verified predecessor artifact, never memory. Every cited key occurs in `paper/references.bib`, every entry is cited, and source/build reviews compare TeX, BibTeX, and `bbl` key sets exactly. No new theorem dependency or citation enters without separately authorized governance.

`PV16` owns planar `q=2` support-one `CBA`, exact `T_4/T_3`, and the stronger effective result. Terminal-review SHA-256: `e355172b4533011d549453d02ee9939fb2dabc16fef035206ad4911fdf18eb76`. Final-PDF SHA-256: `b4ffdaf30e2d0684b875863393e6937c26f51ce89c6f47567a24ed9a123e5e4f`.

`PV17` owns `dim H<=k-m`, the relation lattice, special equality family, terminal `T_k`, and special-coefficient sharpness. Paper 19 begins with equality rigidity, complete `E_m` classification, coefficient-family geometry, and coefficientwise compatible-group sharpness. Terminal-review SHA-256: `941e8b47e4436fdd9bff6f48ebf6e8c1174d07f545a220ead9ad02d73b23ed9d`. Final-PDF SHA-256: `080282e18b085cc87bb590db239c4c8f8f80fd86147ded1aa775e67504b17f2e`.

`PV18` owns marked trace coordinates and scheme-theoretic ramification; there is no theorem overlap. Terminal-review SHA-256: `251d78d2989c0c76b6f1a3090c9aeccf9c66a7171829ca6b795c9ca97d359713`. Final-PDF SHA-256: `e9044c2a9e6452b58b9e345a17c33a211feed909414798fa4696e169b24be06b`.

All predecessor prose is neutral third person. The public text may say only that no direct collision was found in bounded checked primary sources through 2026-08-19, leaving unindexed, non-English, unpublished, and private work unresolved. It makes no absolute-priority claim and contains no local paths, hashes, reviewer identities, dashboards, or lifecycle tokens.

## 8. `STOP-S1` and `AC01--AC18`

`STOP-S1` permanently rejects: `unique q^2-1 character shadow => universal scalar lift and an exact kq scalar clock`. The first counterexample `(k,nu,d)=(3,1,2)` is negative history only, not evidence. The repair is universal no-lift for `q>=3` and exact coefficient-locus lift for `q=2`. For `q>=3` use “universal penultimate obstruction” or “one-step improvement over character extinction,” never exact, optimal, shortest, minimal, or sharp scalar threshold.

1. `AC01`: never assign geometric dimension to `T_m`.
2. `AC02`: no lower-dimensional or inclusion-maximal translate classification.
3. `AC03`: maximum-dimensional means exactly `dim H=k-m` in Part A.
4. `AC04`: `E_m` is not a Hilbert scheme, Fano scheme, or fine moduli functor.
5. `AC05`: component counts are geometric-fiber statements over an algebraically closed field.
6. `AC06`: the smooth `delta^alpha_m` component statement requires squarefree `P`.
7. `AC07`: the universal family fixes actual support and all displayed coefficients are invertible.
8. `AC08`: no irreducibility, reducedness, or complete total-singular-locus theorem on the discriminant boundary.
9. `AC09`: coefficientwise sharpness means compatible extension/group existence, not every fixed group.
10. `AC10`: Laurent supplies no effective cardinality, algorithm, or effective exceptional locus.
11. `AC11`: `kq-1` for `q>=3` is not exact, optimal, shortest, minimal, or sharp.
12. `AC12`: no novelty claim for the planar `q=2` `CBA` endpoint.
13. `AC13`: do not re-market Paper 17's dimension law, special equality family, or terminal `T_k`.
14. `AC14`: character independence, root schemes, discriminants, and lci facts are not headline novelty.
15. `AC15`: no positive-characteristic, `a=0`, `b=0`, `c=0`, or `d=1` extension.
16. `AC16`: no rational/Laurent-support or arbitrary-polynomial-automorphism extension.
17. `AC17`: bounded negative search is not absolute priority.
18. `AC18`: no effective enumeration, height theorem, periodic-point classification, submission, upload, or external lifecycle effect.

## 9. `SW01--SW24` source checklist

- `SW01` Exact title; no author, affiliation, or acknowledgment.
- `SW02` Exactly 29 substantive pages, references separate, no appendix or padding.
- `SW03` Zero figures/numerical-result tables; at most one justified nonnumeric provenance table.
- `SW04` Zero science/computation, code, data, CAS output, enumeration, or empirical evidence.
- `SW05` State the character-shadow/scalar-lift story in the abstract or first paragraph.
- `SW06` Front-load results, `q=2` exception, `q>=3` limit, and predecessor deductions.
- `SW07` Preserve inverse, orientation, `0<=n<m` equations, `0<=j<=m` states, and projection.
- `SW08` Introduce common, Part A, Part B hypotheses in that order.
- `SW09` Complete main-text proofs for `TA1--TA4`, `CA1`, `TB1--TB9`, `CB1`.
- `SW10` Prove saturation before rigidity; reconstruction and both open families before `TA2`.
- `SW11` Proper-closed avoidance for every active root tuple, including `alpha_m=m`.
- `SW12` Retain all squarefree, reduced-fiber, fixed-support, lci, discriminant, and completed-fiber qualifiers.
- `SW13` Include exclusive signs, colors, heights, and arbitrary-rank quantifiers.
- `SW14` Prove central coverage with `t,h,j` and both inequalities.
- `SW15` Derive `G/H`, full semigroup ranges, and `1+T^q` without enumeration.
- `SW16` Audit residue counts, coverage, and `u_(kq+k-1)` before actual `X*(H)=Z w`.
- `SW17` Derive seven triples, two-case `z_*` zero, index bounds, and compatible coincidences.
- `SW18` Scalar order: `b c^(d-1)=-1`, `a=-1`, `2c=0`.
- `SW19` `q=2` iff, five scalars, primitivity, actual `Phi`, and generic fill.
- `SW20` `EXT-L` only after geometry; arbitrary-torsion/field bridge included.
- `SW21` Neutral third-person Papers 16--18 ownership.
- `SW22` Preserve `STOP-S1` and `AC01--AC18`; no absolute priority.
- `SW23` All proofs main-text, citations verified, no new dependency.
- `SW24` End with assumptions, limits, unified answer, and no public downstream statement.

## 10. Frozen U15 ledger

Before this scope, the project contained exactly these fifteen regular, non-symlink, valid-UTF-8, BOM/CR/NUL-free, terminal-LF files:

| Path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `experiments/EXPERIMENT_PLAN.md` | `85a38df6f2fbf056aa2ca38de02566e3ddf3d165704c17446e6c05c74779ef2f` | 8034 | 197 |
| `experiments/EXPERIMENT_TRACKER.md` | `cbf456ab962ba39e9a9f5b1abbc8c68f078e73caf5928661cb1a2304359ff480` | 3237 | 103 |
| `experiments/source_lock.json` | `bba41a3df39f41f367e8fbfaec3703c09c56f1f63af8904e908d262f41179aba` | 30695 | 1 |
| `notes/CITATION_VERIFICATION.md` | `6bc87aaac7caaf47b448d0f1e8a9da886999c8990cdec0f7d8bf47119be84a06` | 10897 | 200 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `dd26db0e9446e9258734ec5f10d2cc05aef5e921a9a487bfd0051c849cbf0aae` | 10474 | 88 |
| `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | `12664657e0c6c0e667ace509e1e174f0ab80ed9be9ea0fd435e8284ed09324b7` | 25247 | 466 |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | `4b2f309d6a84bf53bd6b28319fba2a47386e4d3c1ac96c86375a1a43a155c724` | 24917 | 469 |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | `31a009eb64383eda501d37fd146a9a8456cdc427e951ec321c1b11108fc40b8b` | 25379 | 548 |
| `notes/NOVELTY_ASSESSMENT.md` | `612fb2a1e0168e314e5f00872e23a88bfd44a577e56153695e0664305fda7e9b` | 10172 | 195 |
| `notes/PROOF_PACKAGE.md` | `619d9fde3bbf206ae404b8c5f6bbf8f20ab08904f14026dd7ccd31d2951e600b` | 32247 | 892 |
| `notes/RESEARCH_QUESTION.md` | `9a7c5039f19f1b86a09b1eb25b32bfd8e05a39903c8899bb02169818129df715` | 21278 | 580 |
| `paper/PAPER_PLAN.md` | `8aac5856b1e480182cefe5796275fb9e8335efc161fd87e3782446716a74ff07` | 40343 | 428 |
| `refine-logs/FINAL_PROPOSAL.md` | `d863f893f41d74f5ed46ff0448d3424c44057a448cbd06f407be0e50f5ec08b7` | 10765 | 328 |
| `refine-logs/INITIAL_PROPOSAL.md` | `21a72723d938fe860ee68e8f522e8ab50a0f0b86537598303bd39354ee2e7980` | 8338 | 246 |
| `refine-logs/REVIEW_SUMMARY.md` | `aae1fcc983ec32b52d006e93f2e99253e260571b114c769f0742d11dae6e619b` | 12404 | 332 |

U15 totals are fifteen files, four project subdirectories (`experiments`, `notes`, `paper`, `refine-logs`), 274427 bytes, and 5073 LF. Its sorted aggregate-record SHA-256 is `6378b56846ca60e6a76f178ea6b335a95fbbbf01dffa5b4ea434724696152c35`. Record grammar: `project-relative-path<TAB>sha256<TAB>bytes<TAB>LF-count<TAB>regular_file<TAB>true<TAB>true<LF>`.

The plan identity is `paper/PAPER_PLAN.md` SHA-256 `8aac5856b1e480182cefe5796275fb9e8335efc161fd87e3782446716a74ff07` with terminal `PAPER_PLAN_AUTHOR_STOP`. The plan-review identity is `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` SHA-256 `12664657e0c6c0e667ace509e1e174f0ab80ed9be9ea0fd435e8284ed09324b7` with terminal `PAPER_PLAN_PASS`.

Gate provenance: candidate novelty 7.9, standalone 8.2, proof readiness 9.1; independent source-design novelty 8.2, standalone 8.4, proof readiness 9.2, unity/page feasibility 8.8; character adversary `PROVABLE AS STATED`, confidence 0.97. Scores are not evidence.

## 11. Exact universes and source gate

All sets are project-relative and exact:

- `U15`: Section 10's fifteen paths.
- `U16`: `U15` plus `notes/PUBLICATION_STAGE_SCOPE.md`.
- `U17`: `U16` plus `experiments/publication_lock.json`.
- `U18`: `U17` plus `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md`.
- `U20`: `U18` plus, in write order, `paper/main.tex` then `paper/references.bib`.
- `U21`: `U20` plus `notes/INDEPENDENT_MANUSCRIPT_SOURCE_REVIEW.md`.
- `U23`: `U21` plus `paper/main_round0.pdf` and `paper/BUILD_RECEIPT_R0.json`.
- `U24`: `U23` plus `notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md`.
- `U25`: `U24` plus `paper/SOURCE_REVISION_RECEIPT_R1.json`.
- `U27`: `U25` plus `paper/main_round1.pdf` and `paper/BUILD_RECEIPT_R1.json`.
- `U28`: `U27` plus `notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md`.

No role may list, stat, hash, read, precreate, or write a future path before its fence. Set-valued path lists are sorted; source and author write orders are separate sequences.

Only after `PUBLICATION_STAGE_PASS` and a separate invocation may an anonymous source author create `paper/main.tex` by one `apply_patch Add File`, read it back, then create `paper/references.bib` by a separate `apply_patch Add File`. Nothing else is created and no build occurs.

A fresh reviewer who authored none of `U20` reads all `U20` files and may add only `notes/INDEPENDENT_MANUSCRIPT_SOURCE_REVIEW.md` on full pass, terminal `MANUSCRIPT_SOURCE_PASS`. It checks source structure, full theorem/DAG proofs, citation sets, public safety, pages, anti-claims, and zero science. A blocker means write nothing; any repair needs a separate invocation and fresh full review at the still-absent path.

## 12. Deterministic R0/R1/R2 lifecycle

No build is authorized now. After `MANUSCRIPT_SOURCE_PASS` and separate build GO, R0 copies only the two sources into two clean temporary roots. It records resolved executable paths, executable hashes, versions, arguments, fixed environment, source hashes, and exit status, then identically runs:

1. `pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -recorder main.tex`
2. `bibtex main`
3. repeat the exact Step 1 `pdflatex` argv, including `-recorder`, twice.

Environment: `TZ=UTC`, `LC_ALL=C`, `LANG=C`, `SOURCE_DATE_EPOCH=1787097600`, `FORCE_SOURCE_DATE=1`. Network, shell escape, package install, home input, mutable cache input, and nondeterministic metadata are forbidden. Each root's recorder-generated `main.fls` is captured after every `pdflatex` pass and parsed into a complete resolved TeX input ledger; the final receipt binds the union of every recorded input path, SHA-256 digest, byte count, and role, and any unrecorded or forbidden input blocks persistence. The two PDFs, `bbl` files, normalized logs, font tables, and validation transcripts agree byte-for-byte where applicable. Temporary roots are deleted by explicit validated paths after receipt capture. Persistent writes occur in exact order: first `paper/main_round0.pdf`, then strict-canonical `paper/BUILD_RECEIPT_R0.json`; no other path persists.

R0 validates: successful four-command build; no errors, undefined/multiple references, missing citations, overfull/underfull boxes, or unexpected inputs; exact 29 substantive pages then nonempty references; eleven sections; thirty-one results; full `TA/CA/TB/CB` proofs; `STOP-S1`, `AC01--AC18`, `SW01--SW24`; actual `X*(H)` and arbitrary-rank proof; zero appendix/figures/images/numerical tables/code/data/science; no actions, attachments, annotations, embedded files, forms, scripts, multimedia, signatures, encryption, or private metadata; embedded fonts and no Type 3; TeX/BibTeX/`bbl` key equality; extractable unclipped text; no local path/hash/reviewer/dashboard/lifecycle language; deterministic two-root equality.

A fresh R1 reviewer reads exact `U23` and may write only `notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md`, whose last nonempty line is exactly `MANUSCRIPT_R1_PASS` or `MANUSCRIPT_R1_REPAIR_REQUIRED`. Findings have stable IDs, severity, source/PDF locations, bounded repair, and scope impact. An out-of-class blocker ends the lifecycle.

Exactly one separately invoked R1 source window follows, including a mandatory canonical no-op. On pass, sources remain byte-identical. On repair-required, only `paper/main.tex` and/or `paper/references.bib` may receive one bounded repair set mapped to findings, without new theorem, dependency, citation, science, appendix, figure, or scope. In either case strict-canonical `paper/SOURCE_REVISION_RECEIPT_R1.json` records disposition, before/after identities, exact changes or no-op proof, and no other mutation. No second repair window exists.

After separate R1 build GO, the two-clean-root protocol permits persistent writes in exact order: first `paper/main_round1.pdf`, then strict-canonical `paper/BUILD_RECEIPT_R1.json`; no other path persists. No-op requires R1 PDF byte identity with R0; repair repeats every validation and binds the authorized delta.

A fresh R2 reviewer reads exact `U27` and may write only `notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md` on all-pass, terminal `MANUSCRIPT_R2_PASS`. Any blocker gives no second repair, rebuild, substitution, or finalization. Even pass does not create `paper/main.pdf` or authorize release.

## 13. Finalization, external effects, and publication review

Reserved but unauthorized future paths are `notes/FINALIZATION_STAGE_SCOPE.md`, `experiments/finalization_lock.json`, `notes/INDEPENDENT_FINALIZATION_STAGE_REVIEW.md`, `paper/main.pdf`, and `paper/FINAL_RELEASE_MANIFEST.json`. They remain absent unless a new finalization-governance author is separately invoked after `MANUSCRIPT_R2_PASS` and creates a new exact lock/review chain.

Forbidden actions include dashboard mutation; predecessor mutation; identity disclosure; author/acknowledgment creation; email, chat, calendar, cloud, issue tracker, repository host, journal, arXiv, DOI, or social-platform access; commit, push, pull request, submission, upload, release, publication, announcement, or messaging; software installation; external compilation/science; and creation of code, data, results, assets, figures, `paper/reviews`, supplement, cover letter, response letter, license, archive, or release bundle. Every authorized effect is local-only.

After this governance author stops, a fresh reviewer who authored none of `U17` reads all seventeen files, rehashes exact `U17`, proves old inputs unchanged, validates this scope and strict-canonical lock, exact `U15 -> U16 -> U17 -> U18` equations, all contracts, and future absence. It must reject duplicate JSON keys and `NaN`, `Infinity`, and `-Infinity`; require recursive key sort, compact separators, UTF-8, `ensure_ascii=False`, `allow_nan=False`, no BOM/CR/NUL, one terminal LF, self-hash/byte exclusion, and no unbound source claim.

Any blocker means no write and no token. Full pass permits exactly `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` by `apply_patch Add File`, terminal `PUBLICATION_STAGE_PASS`, then reviewer stop. That pass still needs a separate source-author invocation.

## 14. Governance-author stop condition

After exact readback, the author may create the strict-canonical lock as the second and final write. It binds exact `U16`, declares exact `U17` and prospective `U18`, excludes its own SHA-256 and byte count, and freezes all theorem, proof, citation, public-safety, page, source-review, build, validation, revision, finalization, and permission contracts. It modifies nothing else and grants nothing downstream.

The lock's future SHA-256 and byte count are intentionally not claimed here. Final identities may be reported externally only after validation.

PUBLICATION_STAGE_SCOPE_READY
