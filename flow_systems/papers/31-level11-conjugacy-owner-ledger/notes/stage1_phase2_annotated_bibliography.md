# Paper 31 — Stage 1 Phase 2 Annotated Bibliography

## Bibliography-only status

- Workflow: ARS deep-research full mode, Stage 1 Phase 2 only.
- Search date: 2026-09-02 UTC.
- Checkpoint-1 input state: PASS after revision and recheck.
- Phase-1 inputs held fixed:
  - RQ brief SHA-256: b5927371ff7422b084dee6c8644ba14981b88b8f15cab9997f5df254cdd312b1
  - methodology blueprint SHA-256: 046e4b826ffd0cfbf2e697d13bbf8d925dc775ef262798af4c4f2ef8e9ca23d2
  - resolution SHA-256: 624780725fc006517bfc391c0945e8a2ae67a09c482f6b28d4d1278bc49b204e
  - Checkpoint-1 recheck SHA-256: 0c5613704e9ee3eaaa727086174c08c9aa88ed1ed8355de2e352abacddb17592
- Fence: this file records source discovery, bibliographic metadata, topical relevance, and conservative claim-support boundaries. It does not perform source-verification verdicts, evidence synthesis, novelty adjudication, computation, or manuscript drafting.
- Frozen scientific boundary: the global oriented primitive owner identity is distinct from the cell-local no-double-credit estimand. P31 may close an A1 ownership question only; no source listed here is treated as automatically establishing A2 or a global determinant/product identity.

## Search protocol

### Interfaces actually used

1. Crossref REST metadata records, queried by exact or near-exact title and author.
2. DOI resolver landing pages and first-party journal or publisher pages: AMS, Cambridge University Press, Oxford University Press, London Mathematical Society, World Scientific, Springer, Elsevier, Project Euclid, Johns Hopkins University Press, and Centre Mersenne.
3. Author or institutional repositories only when they exposed a stable manuscript or bibliographic record: Oxford ORA and author-hosted manuscripts.
4. AMS institutional publications for the Pell-equation survey.

Search-engine result totals were not recorded because they are volatile and are not reproducible database hit counts. The counts below are counts of records manually captured into the screening ledger.

### Verbatim queries

- "Gamma_0(11) subgroup modular group conjugacy hyperbolic elements"
- "finite index subgroup PSL2Z conjugacy algorithm"
- "subgroups of the classical modular group Millington DOI"
- "arithmetic geometric method subgroups modular group Kulkarni DOI"
- "special polygons subgroups modular group applications DOI"
- "algorithm determining subgroup modular group congruence Lang Lim Tan"
- "identifying congruence subgroups modular group Hsu DOI"
- "computing fundamental domains for Fuchsian groups Voight DOI"
- "continued fractions conjugacy problem SL_2(Z) Appelgate Onishi"
- "conjugacy classes hyperbolic matrices SL(n,Z) ideal classes order"
- "solution conjugacy problem certain arithmetic groups Grunewald"
- "conjugacy problem GL(n,Z) Eick Hofmann O'Brien"
- "class numbers indefinite binary quadratic forms Sarnak DOI"
- "explicit formula number classes primitive hyperbolic elements Gamma_0(N) Golovchanskii Smotrov"
- "conjugacy problem modular group class number real quadratic number fields Traina"
- "modular surface continued fractions Series DOI"
- "linearity conjugacy problem word-hyperbolic groups DOI"
- "conjugacy problem hyperbolic groups finite lists DOI"
- "reversing symmetries toral automorphisms centralizer DOI"
- "solving the Pell equation Lenstra AMS"

### Prior inclusion criteria

A source was eligible when it was a primary research article, scholarly book/chapter, or authoritative institutional publication and addressed at least one frozen interface:

1. finite-index subgroups of PSL(2,Z), especially exact encodings, fundamental domains, or congruence recognition relevant to Gamma_0(11);
2. integral or subgroup conjugacy of hyperbolic matrices, including oriented versus inverse/reversing classes;
3. primitive-root or proper-power detection, centralizers, continued-fraction reduction, ideal classes, or Pell-type arithmetic;
4. a terminating positive/negative conjugacy decision theorem whose hypotheses and completeness argument could be inspected later;
5. exact algorithms capable of informing the Phase-1 certificate contract or its fail-closed feasibility gate.

Older foundational papers were eligible under a currency exemption when they supply the theorem or construction being considered. They were paired, where possible, with modern algorithmic treatments.

### Prior exclusion criteria

- tertiary explanations, encyclopedia pages, informal notes, and software manuals;
- duplicate preprint/publisher/DOI manifestations of the same work;
- sources confined to A2 zeta/determinant claims rather than P31's A1 owner question;
- sources about unrelated groups or local/p-adic conjugacy without a credible bridge to the frozen integral subgroup problem;
- bounded-search heuristics that do not expose a completeness theorem for negative certificates;
- sources whose only relevance was generic background already covered by a more direct included source.

### Screening and deduplication accounting

| Ledger stage | Count |
|---|---:|
| Manually captured records | 44 |
| Duplicate manifestations removed | 9 |
| Unique records screened | 35 |
| Excluded after title/abstract/metadata screening | 13 |
| Included in this bibliography | 22 |

Deduplication key order was DOI, then normalized title + year + first author. Publisher versions were retained over duplicate aggregators or preprints. The 22 included records are unique under that rule.

The 13 exclusions comprised: two A2/global-zeta sources; three tertiary or software-documentation sources; two noncanonical duplicate hosts; one newer special-polygon paper overlapping the included foundational polygon/fundamental-domain sources without supplying element-conjugacy certificates; one PID matrix-conjugacy extension lacking the Gamma_0(11) subgroup condition; one free-by-cyclic group paper; one general root-decision pathology paper without a constructive interface here; one p-adic conjugacy paper; and one overlapping preprint on double cosets/fundamental domains.

## Included sources and annotations

### Theme A — modular-subgroup and fundamental-domain interfaces

#### P31-S01 — Millington (1969)

M. H. Millington, “Subgroups of the Classical Modular Group,” Journal of the London Mathematical Society, s2-1(1), 351–357. DOI: https://doi.org/10.1112/jlms/s2-1.1.351

- Relevance: foundational classification data for finite-index modular subgroups.
- Candidate support boundary: may support a later specification of subgroup signatures and finite-index structure. It does not by itself decide conjugacy of a fixed pair inside Gamma_0(11), distinguish the project's oriented owner serialization, or certify all negative pairs.
- Currency: foundational exemption; retained for the original modular-subgroup classification role.

#### P31-S02 — Kulkarni (1991)

Ravi S. Kulkarni, “An Arithmetic-Geometric Method in the Study of the Subgroups of the Modular Group,” American Journal of Mathematics 113(6), 1053–1133. DOI: https://doi.org/10.2307/2374900

- Relevance: arithmetic-geometric and special-polygon machinery for finite-index subgroups.
- Candidate support boundary: can inform an exact subgroup domain/side-pairing representation. A separate theorem and implementation contract are still required to turn that representation into complete positive and negative Gamma_0(11)-conjugacy certificates.
- Currency: foundational exemption.

#### P31-S03 — Chan, Lang, Lim, and Tan (1993)

Shih-Ping Chan, Mong-Lung Lang, Chong-Hai Lim, and Ser-Peow Tan, “Special Polygons for Subgroups of the Modular Group and Applications,” International Journal of Mathematics 4(1), 11–34. DOI: https://doi.org/10.1142/S0129167X93000030

- Relevance: special polygons and associated exact finite subgroup data.
- Candidate support boundary: potentially supports a deterministic fundamental-domain fixture. It does not alone establish the project's element-level canonical owner relation, primitive-root policy, or all-pairs negative-certificate completeness.
- Currency: foundational exemption.

#### P31-S04 — Lang, Lim, and Tan (1995)

Mong-Lung Lang, Chong-Hai Lim, and Ser-Peow Tan, “An Algorithm for Determining if a Subgroup of the Modular Group is Congruence,” Journal of the London Mathematical Society 51(3), 491–502. DOI: https://doi.org/10.1112/jlms/51.3.491

- Relevance: an exact algorithmic interface for congruence recognition.
- Candidate support boundary: supports checking subgroup presentation/recognition assumptions, not the distinct problem of deciding whether two hyperbolic elements are conjugate inside a fixed congruence subgroup.
- Currency: foundational exemption.

#### P31-S05 — Hsu (1996)

Tim Hsu, “Identifying Congruence Subgroups of the Modular Group,” Proceedings of the American Mathematical Society 124(5), 1351–1359. DOI: https://doi.org/10.1090/S0002-9939-96-03496-X

- Relevance: finite permutation/presentation tests for identifying congruence subgroups.
- Candidate support boundary: can constrain a replayable Gamma_0(11) subgroup model. It is not a substitute for the frozen conjugacy certificate interface or for orientation/inversion conventions.
- Currency: foundational exemption.

#### P31-S06 — Voight (2009)

John Voight, “Computing Fundamental Domains for Fuchsian Groups,” Journal de Théorie des Nombres de Bordeaux 21(2), 467–489. DOI: https://doi.org/10.5802/jtnb.683

- Relevance: modern exact computational construction of fundamental domains for Fuchsian groups.
- Candidate support boundary: may supply feasibility evidence for a finite exact domain and reduction routine. Later verification must check whether its hypotheses and outputs yield a terminating, complete Gamma_0(11) pair-conjugacy decision, rather than merely a bounded enumeration.

### Theme B — integral conjugacy, reduction, centralizers, and arithmetic certificates

#### P31-S07 — Latimer and MacDuffee (1933)

C. G. Latimer and C. C. MacDuffee, “A Correspondence Between Classes of Ideals and Classes of Matrices,” Annals of Mathematics 34(2), 313–316. DOI: https://doi.org/10.2307/1968204

- Relevance: foundational ideal-class correspondence for integral matrix conjugacy.
- Candidate support boundary: addresses ambient integral similarity under its hypotheses. The Gamma_0(11) congruence restriction, determinant-one lift, orientation, inversion, and project serialization all require separate treatment.
- Currency: foundational exemption.

#### P31-S08 — Taussky (1949)

Olga Taussky, “On a Theorem of Latimer and MacDuffee,” Canadian Journal of Mathematics 1(3), 300–302. DOI: https://doi.org/10.4153/CJM-1949-026-1

- Relevance: clarifies the matrix/ideal correspondence used in arithmetic conjugacy reductions.
- Candidate support boundary: supports only the ambient correspondence it states; it does not close subgroup-constrained conjugacy or certificate completeness.
- Currency: foundational exemption.

#### P31-S09 — Wallace (1984)

D. I. Wallace, “Conjugacy Classes of Hyperbolic Matrices in SL(n,Z) and Ideal Classes in an Order,” Transactions of the American Mathematical Society 283(1), 177–184. DOI: https://doi.org/10.1090/S0002-9947-1984-0735415-0

- Relevance: directly links hyperbolic SL(n,Z) conjugacy classes with ideal classes.
- Candidate support boundary: is relevant to an ambient-class layer, but no Gamma_0(11)-specific coset/congruence refinement or global owner byte rule follows automatically.
- Currency: foundational exemption.

#### P31-S10 — Appelgate and Onishi (1981)

Harry Appelgate and Hironori Onishi, “Continued Fractions and the Conjugacy Problem in SL_2(Z),” Communications in Algebra 9(11), 1121–1130. DOI: https://doi.org/10.1080/00927878108822637

- Relevance: continued-fraction reduction for the ambient SL_2(Z) conjugacy problem.
- Candidate support boundary: a promising exact positive/negative ambient decision component. Later verification must isolate its completeness theorem and then prove the additional Gamma_0(11) subgroup constraint; bounded continued-fraction searches are not enough.
- Currency: foundational exemption.

#### P31-S11 — Grunewald (1980)

Fritz J. Grunewald, “Solution of the Conjugacy Problem in Certain Arithmetic Groups,” in Word Problems II, Studies in Logic and the Foundations of Mathematics 95, 101–139. DOI: https://doi.org/10.1016/S0049-237X(08)71335-1

- Relevance: an arithmetic-group conjugacy decision framework.
- Candidate support boundary: may provide a terminating existence theorem at the arithmetic-group level. It does not provide the project's concrete canonical witness/obstruction payload without an explicit specialization and replay construction.
- Currency: foundational exemption; document type conservatively counted as non-peer-reviewed for the percentage audit.

#### P31-S12 — Grunewald and Segal (1980)

Fritz Grunewald and Daniel Segal, “Some General Algorithms. I: Arithmetic Groups,” Annals of Mathematics 112(3), 531–583. DOI: https://doi.org/10.2307/1971091

- Relevance: general exact algorithms for arithmetic groups.
- Candidate support boundary: supports an algorithm-existence layer only. P31 still needs a finite, deterministic specialization with explicit termination, subgroup membership, oriented equivalence, and negative-certificate replay fields.
- Currency: foundational exemption.

#### P31-S13 — Eick, Hofmann, and O’Brien (2019)

Bettina Eick, Tommy Hofmann, and E. A. O’Brien, “The Conjugacy Problem in GL(n,Z),” Journal of the London Mathematical Society 100(3), 731–756. DOI: https://doi.org/10.1112/jlms.12246

- Relevance: modern algorithmic treatment of integral matrix conjugacy.
- Candidate support boundary: can anchor current feasibility for ambient GL(n,Z). It does not automatically preserve SL orientation, impose Gamma_0(11), decide inversion policy, or expose the project's complete negative-certificate serialization.

#### P31-S14 — Sarnak (1982)

Peter Sarnak, “Class Numbers of Indefinite Binary Quadratic Forms,” Journal of Number Theory 15(2), 229–247. DOI: https://doi.org/10.1016/0022-314X(82)90028-2

- Relevance: arithmetic of indefinite forms and hyperbolic conjugacy/class-number structure.
- Candidate support boundary: may inform expected class decomposition and test fixtures, but class-number formulas do not certify any particular pair or establish the frozen global-owner/cell-estimand separation.
- Currency: foundational exemption.

#### P31-S15 — Series (1985)

Caroline Series, “The Modular Surface and Continued Fractions,” Journal of the London Mathematical Society s2-31(1), 69–80. DOI: https://doi.org/10.1112/jlms/s2-31.1.69

- Relevance: symbolic/continued-fraction coding of modular geodesics and reduction.
- Candidate support boundary: can inform canonical reduction conventions. It is not an exact Gamma_0(11) subgroup-conjugacy solver and does not define the project owner ledger.
- Currency: foundational exemption.

### Theme C — hyperbolic-group decision interfaces and inversion

#### P31-S16 — Epstein and Holt (2006)

David B. A. Epstein and Derek F. Holt, “The Linearity of the Conjugacy Problem in Word-Hyperbolic Groups,” International Journal of Algebra and Computation 16(2), 287–305. DOI: https://doi.org/10.1142/S0218196706002986

- Relevance: terminating conjugacy algorithms and computable bounds in word-hyperbolic groups.
- Candidate support boundary: potentially supplies a completeness route after an exact Gamma_0(11) automatic/hyperbolic presentation is fixed. It does not determine the project's primitive-root canonicalization, witness bytes, or subgroup-specific replay schema.

#### P31-S17 — Buckley and Holt (2013)

David J. Buckley and Derek F. Holt, “The Conjugacy Problem in Hyperbolic Groups for Finite Lists of Group Elements,” International Journal of Algebra and Computation 23(5), 1127–1150. DOI: https://doi.org/10.1142/S0218196713500203

- Relevance: simultaneous/list conjugacy algorithms, useful to an all-pairs or centralizer-coset interface.
- Candidate support boundary: establishes no project-specific result until the frozen group presentation, list encoding, orientation, and completeness-to-certificate translation are verified.

#### P31-S18 — Baake and Roberts (2001)

Michael Baake and John A. G. Roberts, “Symmetries and Reversing Symmetries of Toral Automorphisms,” Nonlinearity 14(4), R1–R24. DOI: https://doi.org/10.1088/0951-7715/14/4/201

- Relevance: centralizers and reversing symmetries distinguish ordinary conjugacy from equivalence under inversion.
- Candidate support boundary: helps formulate the conflict matrix for oriented versus inverse-linked classes. It does not choose P31's frozen convention or prove any Gamma_0(11) owner equivalence.

### Theme D — Pell and computational-number-theory support

#### P31-S19 — Lenstra (2002)

H. W. Lenstra Jr., “Solving the Pell Equation,” Notices of the American Mathematical Society 49(2), 182–192. Stable institutional PDF: https://www.ams.org/notices/200202/fea-lenstra.pdf

- Relevance: authoritative exposition of Pell equations and fundamental units, which can enter centralizer parameterizations for hyperbolic matrices.
- Candidate support boundary: background for a candidate arithmetic subroutine only; it is neither a peer-reviewed conjugacy theorem nor a complete subgroup negative certificate.

#### P31-S20 — Cohen (1993)

Henri Cohen, A Course in Computational Algebraic Number Theory, Graduate Texts in Mathematics 138, Springer. DOI: https://doi.org/10.1007/978-3-662-02945-9

- Relevance: exact computational algebraic-number-theory algorithms supporting ideal arithmetic, units, and Pell-type tasks.
- Candidate support boundary: implementation background. It does not establish the exact P31 scientific equivalence relation, the 9,453-pair completeness claim, or the global/cell weighting interpretation.
- Currency: foundational exemption; scholarly book conservatively counted as non-peer-reviewed for the percentage audit.

### Theme E — direct modular/Gamma_0(N) near-neighbor precedents

#### P31-S21 — Golovchanskii and Smotrov (2008)

V. V. Golovchanskii and M. N. Smotrov, “An Explicit Formula for the Number of Classes of Primitive Hyperbolic Elements in the Group Gamma_0(N),” Sbornik: Mathematics 199(7), 1009–1031. DOI: https://doi.org/10.1070/SM2008v199n07ABEH003951; authoritative full-text record: https://www.mathnet.ru/eng/sm3853

- Relevance: the closest included primary precedent for primitive hyperbolic class structure directly in Gamma_0(N), rather than only in the ambient modular group.
- Candidate support boundary: supports class-counting and can inform independent census totals or completeness fixtures after theorem verification. A counting formula does not decide whether a specified pair is conjugate, return a canonical oriented owner, resolve inversion, or serialize positive/negative pairwise certificates.

#### P31-S22 — Traina (1985)

Charles Traina, “The Conjugacy Problem of the Modular Group and the Class Number of Real Quadratic Number Fields,” Journal of Number Theory 21(2), 176–184. DOI: https://doi.org/10.1016/0022-314X(85)90049-6

- Relevance: a direct modular-group conjugacy/class-number precedent connecting the decision problem with real quadratic arithmetic.
- Candidate support boundary: can inform the ambient modular conjugacy and class-number layer. It does not impose the Gamma_0(11) subgroup constraint, freeze oriented-versus-inverse equivalence, or provide the project's canonical pairwise witness/obstruction and all-pairs replay contract.
- Currency: foundational exemption.

## Coverage map against the frozen Phase-1 interfaces

| Frozen interface | Candidate sources | Bibliography-stage coverage boundary |
|---|---|---|
| Exact Gamma_0(11) finite-index representation and class structure | P31-S01–S06, S21 | Strong candidate coverage for subgroup/domain encodings and a direct Gamma_0(N) primitive-class counting precedent; no included source alone supplies the complete pair-conjugacy certificate contract. |
| Ambient integral/modular hyperbolic conjugacy | P31-S07–S13, S22 | Multiple arithmetic and algorithmic routes exist at GL/SL, modular, or ideal-class level; subgroup, lift, orientation, and serialization remain separate proof obligations. |
| Reduction, centralizers, Pell, primitive-power ingredients | P31-S10, S14–S20 | Candidate ingredients are covered; a complete maximal-root and subgroup-centralizer interface has not been established at Phase 2. |
| Oriented versus inverse-linked class conflict | P31-S15, S18 | The distinction is represented, but the frozen P31 choice is a project definition and cannot be imported implicitly. |
| Complete positive and negative certificates | P31-S10–S13, S16–S17 | Algorithm-existence literature is present; exact witness/obstruction serialization and replay completeness remain a verification target. |
| Global owner identity versus cell-local no-double-credit estimand | none directly | This is a project-specific estimand discipline. No source is being cited as merging or proving these two layers. |
| A2/global determinant implication | deliberately excluded | Out of scope. Closing A1 never automatically closes A2. |

## Distributional-skew advisory

- Peer-reviewed research articles: 19/22 = 86.4%.
- Conservatively non-peer-reviewed in this audit: one scholarly chapter, one AMS expository article, and one scholarly book.
- Fifteen of 22 sources (68.2%) were published before 2000. This is just below the 70% hard advisory threshold and remains a material historical skew. The skew is expected because modular-subgroup classification, integral conjugacy, continued fractions, and arithmetic-group algorithms are foundational topics. The currency exemption prevents automatic exclusion, but it does not establish that old algorithms are implementation-ready or that later corrections do not exist.
- Modern anchors (2001–2019) were retained for fundamental-domain computation, hyperbolic-group decision algorithms, reversibility, GL(n,Z) conjugacy, and direct Gamma_0(N) primitive-class counting.
- Theme balance: modular subgroup/domain/direct Gamma_0(N) structure 7; integral or modular conjugacy/reduction/arithmetic 10; general hyperbolic decision algorithms 2; reversibility 1; computational Pell/number-theory support 2. No single theme exceeds 70%.

## Limitations and handoff to later phases

1. This is not a source-verification report. Metadata and abstracts/available landing-page text were inspected; theorem statements, proof hypotheses, errata, and exact algorithm outputs still require a separate verification pass.
2. No included source directly validates the project-defined canonical owner bytes, the all-9,453-pair completeness fixture, or the proposed negative-certificate payload.
3. The direct Gamma_0(N) counting formula in P31-S21 supplies a near-neighbor census precedent, not a pairwise decision/certificate interface; it cannot be used to infer certificate completeness.
4. Ambient GL_2(Z), SL_2(Z), or full modular-group conjugacy is not silently promoted to Gamma_0(11)-conjugacy. The congruence-subgroup refinement remains a central gap.
5. Primitive-root/proper-power detection is covered only through candidate ingredients; the complete subgroup-specific maximal-root interface remains to be located or derived.
6. The literature does not erase the frozen distinction between a global oriented primitive owner appearing across cells/degrees and a cell-local no-double-credit weighting rule.
7. Absence of a directly matching serialized certificate in this included set is not a novelty claim and must not be described as one.
8. If later verification cannot identify a complete theorem-to-certificate contract, the Phase-1 kill gate remains NOT_EVALUABLE_CONJUGACY_INCOMPLETE rather than a negative scientific result.

The machine-readable companion inventory is stage1_phase2_source_inventory.tsv.
