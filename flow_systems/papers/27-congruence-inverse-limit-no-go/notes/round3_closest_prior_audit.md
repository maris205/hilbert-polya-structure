# P27 Round-3 search-bounded novelty and closest-prior audit

Date: **2026-08-27 (UTC)**

    ARS_STAGE=1_RESEARCH
    DOCUMENT_ROLE=SOURCE_AND_CLOSEST_PRIOR_AUDIT
    MANUSCRIPT_DRAFT=false
    ARS_STAGE_2_STARTED=false
    FORMAL_ROUTE_A_TUPLE=UNASSIGNED
    A2_A4=NOT_EVALUATED
    ROUTE_B_EVALUATION=NOT_RUN
    ROUTE_B_INVOCATION_ALLOWED=false

## Audit question

This audit asks three deliberately narrow questions:

1. Has a primary source already established the broad phenomenon that a
   hyperbolic laminated or solenoidal geodesic flow can have no periodic
   orbits?
2. Has a primary source already supplied the structural mechanism relevant to
   the P27 tower, namely an inverse limit of hyperbolic surface coverings with
   simply connected leaves?
3. Within the frozen search, was the exact factorial principal-congruence
   statement for “Gamma(3 n!),” or the explicit finite-owner firewall, located
   verbatim?

The audit does **not** attempt to prove absolute novelty. Its conclusion is
bounded by the frozen queries, source surfaces, inclusion rules, and date below.

## Search protocol

### Scope and source policy

- Search date and cutoff: 2026-08-27; sources available through that date.
- Discovery surface: current web search with exact-phrase and
  domain-restricted queries.
- Technical adjudication surface: original journal or publisher pages, DOI
  landing pages, author or institution-hosted manuscripts, and author arXiv
  records and PDFs.
- Language: English-language records and English full texts.
- Date range: no lower bound.
- Citation chasing: only references directly exposed by a verified primary
  source were followed.
- Secondary aggregators, ResearchGate mirrors, encyclopedias, Q&A pages, and
  search-result snippets were permitted for discovery only and were not used to
  settle a technical or novelty judgment.

### Inclusion criteria

A source was included in the closest-prior set if it met at least one of these
conditions:

1. it defines a hyperbolic or punctured solenoid as an inverse limit of finite
   surface coverings;
2. it defines or studies the leafwise geodesic flow on such a space;
3. it states an example with no periodic orbits for a laminated geodesic flow;
4. it identifies a leaf fundamental group with a group-chain intersection; or
5. it treats the exact noncompact finite-area regular-cover object class used by
   P27.

### Exclusion criteria

A source was excluded from the closest-prior set if it concerned only ordinary
finite-level geodesic flows or Selberg zeta functions, one-dimensional abelian
solenoid automorphisms, inverse limits of interval maps or symbolic systems,
mapping class groups without a relevant leaf or flow result, compactified
algebraic inverse limits without the leafwise continuous-time flow, or an
unverified secondary retelling.

## Frozen search strings

The following query set reproduces the search boundary used for the
closest-prior decision. Quotation marks and domain filters are part of the
queries.

### Inverse-limit and laminated geodesic flow

    "geodesic flow" "inverse limit" covering spaces periodic orbits
    "hyperbolic solenoid" "geodesic flow" periodic orbit
    "inverse limit" "geodesic flow" "periodic point"
    "residual tower" geodesic flow closed geodesics
    "no periodic points" "geodesic flow" lamination
    "without periodic orbits for the geodesic flow" lamination
    "geodesic flow" solenoid "closed geodesic"
    "Universal Hyperbolic Solenoid" "periodic" geodesic
    "universal hyperbolic solenoid" "geodesic flow" periodic
    "punctured solenoid" "geodesic flow"
    "solenoidal" "geodesic flow" hyperbolic surface periodic
    "hyperbolic solenoid" "periodic orbits" geodesic

### Primary-source and domain-restricted variants

    site:arxiv.org "Horocycle flows for laminations by hyperbolic Riemann surfaces"
    site:aimsciences.org "Horocycle flows for laminations by hyperbolic Riemann surfaces"
    site:arxiv.org hyperbolic solenoid geodesic flow periodic orbits
    site:projecteuclid.org solenoid geodesic flow periodic
    site:arxiv.org "universal hyperbolic solenoid" geodesic flow
    site:projecteuclid.org "universal hyperbolic solenoid" geodesic
    site:arxiv.org "punctured solenoid" inverse limit finite covers hyperbolic
    site:arxiv.org modular solenoid hyperbolic surface inverse limit
    site:arxiv.org "hyperbolic solenoidal surfaces of finite type"
    site:arxiv.org "Horocyclic trajectories in hyperbolic solenoidal surfaces of finite type"

### Congruence-tower variants

    site:arxiv.org congruence solenoid geodesic flow modular surface inverse limit
    site:ams.org congruence solenoid modular surface inverse limit
    "principal congruence" "inverse limit" "geodesic flow"
    "congruence solenoid" hyperbolic
    "congruence completion" "solenoid" PSL(2,Z) surface
    "congruence tower" "solenoid" Riemann surface
    "principal congruence subgroups" "solenoid"
    "inverse limit" "Gamma(N)" modular curves solenoid
    "Gamma(3 n!)" congruence subgroup inverse limit
    "Γ(3n!)" modular surface
    "3 n!" principal congruence subgroup tower
    "Gamma(3n!)" geodesic

### Group-chain and owner-boundary variants

    site:arxiv.org weak solenoid leaf fundamental group intersection group chain
    site:arxiv.org McCord solenoid leaf stabilizer intersection subgroups
    "leaf" "intersection" "group chain" weak solenoid
    "fundamental group of a leaf" weak solenoid
    site:arxiv.org inverse limit flow periodic points common period
    site:springer.com inverse limit flows periodic point common period
    "inverse limit flow" "periodic points"
    "inverse limit" flows "periodic orbit" common period
    site:arxiv.org closed geodesic lift regular cover order quotient group period
    site:projecteuclid.org closed geodesics finite covers order deck group lift
    site:springer.com closed geodesic lift finite cover order quotient group
    "closed geodesic" "order" "deck group" lift cover

## Included primary sources and verification

### S1. Martínez, Matsumoto, and Verjovsky (2016)

Matilde Martínez, Shigenori Matsumoto, and Alberto Verjovsky, “Horocycle
flows for laminations by hyperbolic Riemann surfaces and Hedlund's theorem,”
*Journal of Modern Dynamics* 10 (2016), 113--134.

- Publisher record:
  https://www.aimsciences.org/article/doi/10.3934/jmd.2016.10.113
- DOI: https://doi.org/10.3934/jmd.2016.10.113
- Author arXiv record: https://arxiv.org/abs/0711.2307
- Author arXiv PDF: https://arxiv.org/pdf/0711.2307
- Verification: publisher title, authors, venue, year, pages, DOI, and abstract
  matched the arXiv manuscript on 2026-08-27.
- Content locators in the arXiv PDF:
  - pp. 2--3, §2.2: the laminated geodesic flow is defined leafwise and
    restricts on each leaf to the ordinary hyperbolic-surface geodesic flow;
  - p. 12, Example 4: a compact hyperbolic lamination example is constructed
    without periodic geodesic-flow orbits;
  - pp. 15--16, Example 6: the universal hyperbolic solenoid is an inverse limit
    of finite regular covers and has dense simply connected hyperbolic leaves.
- Inclusion role: **direct prior for the broad aperiodicity phenomenon** and
  direct structural prior for the universal-solenoid comparison.
- Difference from P27: Example 4 is not the frozen “Gamma(3 n!)” covering
  tower, while Example 6 studies the universal compact object and horocycle
  minimality rather than stating P27's exact proposition.

### S2. Penner and Šarić (2008)

Robert C. Penner and Dragomir Šarić, “Teichmüller theory of the punctured
solenoid,” *Geometriae Dedicata* 132 (2008), 179--212.

- DOI: https://doi.org/10.1007/s10711-007-9226-9
- Author arXiv record: https://arxiv.org/abs/math/0508476
- Author arXiv PDF: https://arxiv.org/pdf/math/0508476
- Institution-hosted preprint:
  https://www.math.stonybrook.edu/preprints/ims05-06.pdf
- Verification: title, authors, and full text were checked on the author arXiv
  record and institution-hosted preprint; journal, volume, pages, and DOI were
  cross-checked against the publisher-linked bibliographic record.
- Content locators:
  - Introduction, pp. 1--2: the punctured solenoid is the inverse limit over
    all finite-index subgroups of PSL_2(Z) and is noncompact;
  - §2, Definition 2.1 and the following discussion: the inverse-limit
    construction is explicit and every leaf is homeomorphic to the unit disk
    and dense.
- Inclusion role: **closest direct structural prior in the noncompact modular
  setting**.
- Difference from P27: the paper uses the directed system of all finite covers,
  not the single frozen factorial principal-congruence chain, and studies
  Teichmüller theory rather than reduction-order ownership.

### S3. Alcalde Cuesta, Carballido Costas, Martínez, and Verjovsky (2026)

Fernando Alcalde Cuesta, Álvaro Carballido Costas, Matilde Martínez, and
Alberto Verjovsky, “Horocyclic trajectories in hyperbolic solenoidal surfaces
of finite type,” *Groups, Geometry, and Dynamics* (online first, 2026).

- Publisher record: https://ems.press/journals/ggd/articles/14299725
- DOI: https://doi.org/10.4171/GGD/967
- Author arXiv record: https://arxiv.org/abs/2411.18418
- Author arXiv PDF: https://arxiv.org/pdf/2411.18418
- Verification: publisher authors, title, accepted and publication dates, DOI,
  and abstract matched arXiv v2, dated 28 January 2026, on 2026-08-27.
- Content locators in arXiv v2:
  - pp. 2--3: inverse limits of finite covers of finite-area hyperbolic surfaces
    are the central object class;
  - pp. 7--8, Definitions 4--5: the leafwise geodesic flow and a hyperbolic
    solenoidal surface of finite type are defined;
  - pp. 12--14, §3.3 and the setup of §4: inverse limits of finite regular
    coverings are called McCord solenoids, and decreasing finite-index
    subgroups of a nonuniform lattice give the relevant noncompact tower.
- Inclusion role: **closest prior for the exact geometric object class and
  terminology**.
- Difference from P27: the paper's theorems concern horocycle dynamics and
  cuspidal minimal sets; the checked text does not state the “Gamma(3 n!)”
  no-geodesic-period theorem or the finite-owner firewall.

### S4. Hurder and Lukina (2019)

Steven Hurder and Olga Lukina, “Wild solenoids,” *Transactions of the American
Mathematical Society* 371 (2019), no. 7, 4493--4533.

- DOI: https://doi.org/10.1090/tran/7339
- Author arXiv record: https://arxiv.org/abs/1702.03032
- Author arXiv PDF: https://arxiv.org/pdf/1702.03032
- Author publication record:
  https://homepages.math.uic.edu/~hurder/publications.html
- Verification: author publication metadata and arXiv full text agreed on
  title, authors, and journal details; the DOI was cross-checked on 2026-08-27.
- Content locator: p. 17, Definition 5.5 and the following paragraph identify
  the kernel of a group chain, the intersection of its subgroups, with the
  fundamental group of the corresponding leaf.
- Inclusion role: **direct source for the group-chain and leaf-topology
  mechanism**.
- Domain caveat: its weak-solenoid setup assumes a closed compact base
  manifold. P27 therefore uses it as structural comparison, not as a
  substitute for the explicit noncompact proof.

### S5. McCord (1965), foundational background only

M. C. McCord, “Inverse limit sequences with covering maps,” *Transactions of
the American Mathematical Society* 114 (1965), no. 1, 197--209.

- DOI: https://doi.org/10.1090/S0002-9947-1965-0173237-0
- AMS PDF:
  https://www.ams.org/journals/tran/1965-114-01/S0002-9947-1965-0173237-0/S0002-9947-1965-0173237-0.pdf
- Verification: title, author, journal, volume, issue, pages, and DOI were
  verified in the AMS bibliographic record. The AMS PDF returned HTTP 403 to
  the present retrieval tool, so no decisive technical inference in this audit
  depends on uninspected McCord text.
- Inclusion role: foundational provenance for the term “McCord solenoid,” not
  a closest geodesic-flow result.

## Representative exclusions

| Source family | Decision | Reason |
|---|---|---|
| Chris Odden, *The baseleaf preserving mapping class group of the universal hyperbolic solenoid* (2005) | background only | Compact universal-solenoid topology and mapping class group; no checked geodesic-period result. |
| Bering and Studenmund, *Topological Models of Abstract Commensurators* (arXiv:2108.10586) | excluded from closest set | Full-solenoid topology and commensurators, not periodic-geodesic ownership. |
| Clark, Fokkink, and Lukina, *The Schreier continuum and ends* (arXiv:1007.0746) | excluded from closest set | Leaf-end topology does not sharpen the closest flow result beyond S2--S4. |
| Papers on periodic points of one-dimensional solenoidal automorphisms | excluded | Different phase space, map, and period notion. |
| Finite-level Selberg-zeta, length-spectrum, and modular-geodesic papers | excluded from same-owner evidence | They concern individual finite quotients and cannot establish a periodic point of the inverse-limit flow. |
| Algebraic or scheme inverse limits of compactified modular curves | excluded | Different owner and category; no leafwise unit-speed continuous-time flow. |
| ResearchGate, encyclopedia, Q&A, and search snippets | discovery only | Not used for technical adjudication or novelty. |

## Claim-by-claim closest-prior judgment

| P27 claim or framing | Search-bounded judgment | Consequence |
|---|---|---|
| A hyperbolic laminated geodesic flow can have no periodic orbit. | **Directly prior** via Martínez--Matsumoto--Verjovsky, Example 4. | Any broad “first aperiodic laminated geodesic flow” claim is rejected. |
| Inverse-limit hyperbolic solenoids can have simply connected leaves. | **Directly prior** for universal and punctured solenoids via S1 and S2. | The simply-connected-leaf mechanism is not new. |
| Noncompact finite-area regular-cover inverse limits form a named hyperbolic McCord-solenoidal object class with a leafwise geodesic flow. | **Directly prior** via S3. | P27 must adopt existing terminology and cite S3. |
| For the exact chain “Gamma(3 n!),” Per(M_infinity) is empty, with an explicit PSL-sign proof of the residual intersection. | **No verbatim primary-source match located in the frozen search.** | This may be presented only as a search-bounded explicit specialization; novelty remains [OPEN], never absolute. |
| The 3-by-8 reduction-order ledger with two independent algorithms. | Project-specific reproducible data. | It supports transparency and the case study, not general theorem novelty. |
| Finite closing periods cannot be credited as periods of the inverse-limit flow without one common time and one owner. | No named identical “owner firewall” located; the distinction follows from the inverse-limit flow definition. | Present as a methodological and claim-discipline contribution, not as a deep new theorem. |

## Closest-prior synthesis

The audit found a **direct prior at the level of the broad result and its
structural mechanism**. S1 already exhibits a hyperbolic lamination whose
geodesic flow lacks periodic orbits. S1 and S2 place simply connected
hyperbolic leaves inside compact and punctured inverse-limit solenoids. S3
places P27's noncompact finite-area regular-cover tower inside an already named
and actively studied object class. S4 makes the subgroup-intersection and leaf
fundamental-group relation explicit in the compact weak-solenoid setting.

The exact factorial-chain proof remains useful because it is elementary,
sign-sensitive in PSL_2(Z), and fully tied to the generated finite-level
ledger. It is not enough to support a claim that P27 discovered a new general
aperiodicity theorem.

## Search-bounded novelty decision

    DIRECT_STRUCTURAL_PRIOR_FOUND=true
    BROAD_APERIODICITY_NOVELTY_CLAIM=REJECTED
    EXACT_GAMMA_3_FACTORIAL_STATEMENT_FOUND_VERBATIM=false
    ABSOLUTE_NOVELTY_CLAIM_ALLOWED=false
    PROPOSED_PAPER_CLASS=EXPLICIT_CASE_STUDY_AND_OWNERSHIP_METHOD_NOTE
    STANDALONE_THEOREM_NOVELTY=NOT_SUPPORTED_BY_THIS_AUDIT

The defensible contribution is narrowed to the combination of:

1. an explicit “Gamma(3 n!)” case with a transparent PSL-sign residual proof;
2. a reproducible finite-quotient reduction-order ledger with independent
   algorithms and transition checks;
3. a formal distinction between level-dependent closing multiples and one
   common positive inverse-limit period; and
4. an evidence and owner policy preventing finite-level zeta or orbit data from
   being credited to a total-space flow with empty periodic set.

This is an incremental methodological and explicit-case contribution. A
stronger standalone paper would require a genuinely broader theorem, a new
invariant, or a nontrivial comparison result beyond the already known
simply-connected-leaf mechanism.

## Limitations and residual risks

1. The search did not include subscription-only MathSciNet or zbMATH citation
   graphs, and no claim of exhaustive coverage is made.
2. Exact-phrase searches can miss differently worded corollaries in books,
   theses, or non-English literature.
3. S4 has a compact-base hypothesis; the P27 noncompact statement must retain
   its own proof.
4. “No verbatim hit for Gamma(3 n!)” is a negative search observation, not
   evidence of absolute novelty.
5. The methodological term “owner firewall” appears project-local. Ordinary
   covering-space logic may already encode the same distinction without that
   terminology.
6. Before any Stage-2 manuscript, a human should confirm the source locators,
   inspect citation chains around S2 and S3, and decide whether a short methods
   note is a viable publication unit.
