# Residual owner gate for P121

**Role:** independent nonauthor residual-owner audit  
**Audit date:** 2026-08-30  
**Disposition:** **EXTERNAL HOLD**

This audit is deliberately narrower than a manuscript review.  It asks only
whether a direct owner was found for the three residuals isolated in the
current `main.tex`.  I read the current source and the primary paper of
Disanto--Fuchs--Paningbatan--Rosenberg, then searched its citation
neighborhood and the neighboring random-tree, antichain, and phylogenetic
literatures.  I did **not** read `HOSTILE_REVIEW_A.md`, and I made no change to
the manuscript or any other package file.

## Executive gate

| residual | closest direct owner | residual after subtraction | gate |
|---|---|---|---|
| (i) Expected antichains marked by cardinality | Disanto et al. own the same random statistic at `s=1`; Andriantiana--Wagner--Wang explicitly own antichains of each cardinality on a fixed rooted tree | the Yule/uniform-history average, its bivariate ODE, and the displayed Euler closed form | **PROCEED WITH CAUTION** (bounded no-direct-owner finding) |
| (ii) All-order Riccati hierarchy and strict radius ladder | Disanto et al. own the exact distributional recursion, the first two moment equations, the Riccati linearization, and the order-two pole analysis | only the strict continuation `rho_r<rho_{r-1}` for every `r>=3`, with the positive unit-residue pole and resulting exact exponential limsup | **PROCEED WITH CAUTION** (bounded no-direct-owner finding); give the hierarchy itself very low credit |
| (iii) `P(X_n=n)=2^(n-2)/(n-1)!` | Chang--Fuchs 2010, Table 1, literally gives the Yule--Harding probability of a `k`-caterpillar as `2^(k-2)/(k-1)!`; Rosenberg 2006 is the earlier `r`-caterpillar owner | none; “ordered-history” is only an equivalent presentation of the same Yule probability | **ABANDON AS A RESIDUAL / ZERO CREDIT** |

The hard collision in (iii) is not a mere nearby result.  It is the same
event, the same measure after the standard ranked-plane-history/Yule
identification, and the same closed formula.

## Claim reconstruction from the current source

The owner comparison used the literal claims below.

1. For the internal-node ancestor poset of the random evaluation tree,
   `P_T(s)=sum_B s^|B|` satisfies
   `P_T(s)=s+P_TL(s)P_TR(s)`.  With
   `a_n(s)=E P_Tn(s)` and
   `A(z,s)=sum_(n>=1) a_n(s)z^(n-1)`, the paper claims

       dA/dz = A^2 + s/(1-z)^2,  A(0,s)=1,

   and an explicit logarithmic-derivative solution in terms of the two
   Euler exponents `(1+-sqrt(1-4s))/2`.  Its coefficients are expected
   numbers of internal-node antichains of each cardinality.

2. For `m_(r,n)=E X_n^r` and
   `F_r(z)=sum_(n>=1)m_(r,n)z^(n-1)`, the paper claims

       F_r' = sum_(k=0)^r binom(r,k) F_k^2.

   Writing `F_r'=F_r^2+G_r` and `F_r=-U_r'/U_r` produces a triangular
   Riccati/linear-ODE hierarchy.  The claimed residual begins at `r=3`:
   the radii satisfy

       1=rho_0 > rho_1 > rho_2 > ... > 0,

   each positive boundary point is a simple pole with local form
   `F_r(z)=1/(rho_r-z)+O(1)`, and
   `limsup_n (E X_n^r)^(1/n)=rho_r^(-1)`.  No full coefficient asymptotic
   is claimed for `r>=3`.

3. The minimum is attained exactly by the planar comb/caterpillar histories,
   and the paper records

       P(X_n=n)=2^(n-2)/(n-1)!  (n>=2).

## Search protocol and exact formulations

The search was bounded, not universal.  I used DOI/Crossref metadata,
OpenAlex, Semantic Scholar's citation endpoint, arXiv, publisher/author
full texts, and literal web searches.  Searches were run through the audit
date and included explicit 2025--2026 formulations.

### Direct citation neighborhood

The DOI `10.1214/22-AAP1791` resolves to OpenAlex work `W3035146328`.
OpenAlex returned seven citing works; Semantic Scholar returned ten records,
including preprint/published duplicates.  The materially closest items were:

- Disanto et al., *The distributions under two species-tree models of the
  total number of ancestral configurations...*, which analyzes the related
  total statistic, again at the level of the first two moments and lognormal
  behavior ([primary author PDF](https://web.math.nccu.edu.tw/mfuchs/TotConfig_revisionFV.pdf),
  [DOI](https://doi.org/10.1016/j.aam.2023.102594));
- Lappo--Rosenberg, which gives the lattice and Cartesian-product structure
  of ancestral configurations and tabulates fixed examples by lineage
  cardinality, but does not form the cardinality-marked internal-antichain
  expectation or the higher-moment radius ladder
  ([primary open text](https://pmc.ncbi.nlm.nih.gov/articles/PMC10704929/),
  [DOI](https://doi.org/10.1016/j.dam.2023.09.033));
- Fuchs's 2025 survey of the Yule/BST correspondence and moment-transfer
  methods, which is methodological rather than a statement of any of the
  three residual formulas
  ([primary open text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11867161/),
  [DOI](https://doi.org/10.1098/rstb.2023.0304)).

The other citation records concern external branch lengths, clade sizes,
tree-valued Markov-chain lumpability, sports-tournament histories, or the
Colijn--Plazzotta rank.  None states one of the first two residuals.  No
2026 direct citation in these two citation graphs supplied such a result.

### Literal queries for residual (i)

The formulations included:

- `"antichain polynomial" "random binary search tree"`
- `"antichain polynomial" "random binary tree"`
- `"Sperner polynomial" rooted tree random`
- `"expected number" "k-element antichains" random binary search tree`
- `cardinality marked antichains random rooted tree generating function`
- `"subtrees containing the root" "random binary search tree" number of leaves`
- `"root-containing subtrees" random binary tree leaves`
- `"sqrt(1-4s)" antichain tree`
- `"A_z=A^2" antichain tree`
- `2025 "antichain polynomial" random tree`
- `2026 "antichain polynomial" binary tree`

These queries did locate the fixed-tree cardinality owner discussed below,
but not the Yule-averaged bivariate OGF or its displayed closed form.

### Literal queries for residual (ii)

The formulations included:

- `"higher moments" "root configurations" phylogenetic trees`
- `"arbitrary moments" Riccati "ancestral configurations"`
- `"root configurations" "third moment"`
- `"number of antichains" "random binary search tree" moments`
- `"root containing subtrees" random binary search tree moments`
- `"1+X_L X_R" random tree`
- `"product-plus-one" random binary tree`
- `"strictly decreasing" radii of convergence moments random tree`
- `"simple pole" "higher moments" random binary search tree Riccati`
- `"Sturm comparison" "higher moments" generating functions random trees`
- `2025 2026 "root ancestral configurations" moments`

The searches recovered Disanto et al.'s order-one and order-two analysis and
generic random-tree moment machinery, but no paper stating the all-`r`
strict radius cascade for this statistic.

### Literal queries for residual (iii)

The formulations included:

- `"2^{n-2}" "(n-1)!" caterpillar tree Yule`
- `"2^(n-2)" "(n-1)!" caterpillar`
- `probability Yule Harding tree is caterpillar exact`
- `ordered unlabeled histories caterpillar probability`
- `"2^{k-2}" "(k-1)!" caterpillars`
- `Rosenberg 2006 r-caterpillars`
- `2025 2026 caterpillar 2^(n-2) Yule`

This search produced a literal exact match in Chang--Fuchs 2010.

## Residual (i): cardinality-marked expected antichains

### What is directly owned

Disanto--Fuchs--Paningbatan--Rosenberg directly own the random variable in
shifted notation.  Their Proposition 3.5 gives the uniform-split recurrence,
Section 3.2 gives the nonempty-antichain correspondence, and Sections 5.2--5.3
analyze the unmarked first and second moments
([journal primary PDF](https://rosenberglab.stanford.edu/papers/DisantoEtAl2022-AAP.pdf),
[DOI](https://doi.org/10.1214/22-AAP1791)).  Thus `A(z,1)` and every unmarked
claim are fully owned.

More importantly for the marker, Andriantiana--Wagner--Wang explicitly study
antichains of **given cardinality** in a rooted-tree poset.  They identify an
antichain with the leaves of a subtree containing the root and introduce
counts `eta_l` for root-containing subtrees having `l` leaves.  This is the
same fixed-tree cardinality refinement represented by the coefficients of
`P_T(s)` ([primary EJC PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i3p28/pdf),
[DOI](https://doi.org/10.37236/3101)).  Consequently:

- the cardinality marker as an object is owned;
- the fixed-tree antichain/root-subtree bijection is owned;
- the elementary product recursion for the fixed-tree polynomial deserves
  no novelty credit.

Lappo--Rosenberg is also close but not identical.  It stratifies ancestral
configurations by the number of lineages in a configuration.  P121 instead
marks the number of selected **internal vertices after deleting leaf
lineages**.  These two exponents are not equal in general: a configuration's
lineage count also includes all uncovered leaves.  Hence the lattice paper is
an important firewall citation, not a direct owner of `A(z,s)`.

### Residual delta

I found no primary source that takes the fixed-tree cardinality polynomial,
averages it under the uniform ranked-plane-history/Yule split law, and obtains

`A_z=A^2+s/(1-z)^2`

together with the displayed Euler/logarithmic-derivative closed form.  That
specific conjunction survives the bounded search.

### Verdict

**PROCEED WITH CAUTION.**  The defensible residual is the exact
**Yule-averaged bivariate transform and its closed solution**, not “introducing
a cardinality marker” and not the fixed-tree recursion.  The strongest owner
objection is that the transform is a short parametric lift of the already
owned split recurrence; the source should therefore describe it as a precise
closed refinement and explicitly give zero credit to the fixed-tree marker
of Andriantiana--Wagner--Wang.

This is a bounded no-direct-owner finding, not a priority certification.

## Residual (ii): arbitrary moments and the strict pole ladder

### What is directly owned or mechanically implied

The exact finite distributional recurrence in Disanto et al. already
determines every raw moment.  Expanding `(1+ab)^r` therefore makes the
all-order triangular identity an immediate algebraic consequence of the
direct owner's recurrence.  I did not find the identity printed for arbitrary
`r` in that paper, but absence of the displayed formula does not make this
one-line expansion a high-credit theorem.

Disanto et al. also directly own:

- the complete `r=1` Riccati equation and dominant pole;
- the `r=2` recurrence;
- Riccati-to-second-order-linear-ODE conversion at order two;
- location of a positive simple pole and the stronger order-two coefficient
  asymptotic.

The total-configuration sequel remains at mean/variance level.  Fuchs's 2025
survey explains general Yule/BST and moment-transfer machinery but does not
state an arbitrary-order pole ladder for this multiplicative statistic.
Generic Riccati linearization, Sturm comparison, Pringsheim, and
Cauchy--Hadamard are of course established tools and carry no contribution
credit by themselves.

### Residual delta

No searched primary source states, for this root-configuration/product-plus-one
statistic, that for **every** `r>=3`:

- the first positive zero of the order-`r` linearized solution occurs before
  `rho_(r-1)`;
- hence `rho_r<rho_(r-1)` strictly;
- the positive boundary singularity is a simple pole with normalized residue
  one; and
- the coefficient growth has the exact Cauchy--Hadamard limsup
  `rho_r^(-1)`.

The nontrivial residual is the infinite strict continuation.  The unit
residue is a local consequence of a simple zero, and the limsup follows from
the radius, so those two phrases should not be sold as independent advances.

### Verdict

**PROCEED WITH CAUTION.**  Give very low or zero novelty weight to the
all-order moment identity itself and center any residual claim on the
all-`r>=3` strict radius theorem.  The owner statement should say explicitly
that the hierarchy starts from an exact law and two base cases already owned
by Disanto et al.  Within the bounded direct-source and citation-neighborhood
search, I found no direct temporal owner of the strict ladder.

Again, this is not a universal novelty guarantee.  It is a bounded finding
through 2026.

## Residual (iii): exact caterpillar minimum mass

### Literal direct owner

Chang--Fuchs, *Limit theorems for patterns in phylogenetic trees*, lists in
Table 1 the Yule--Harding probability of a `k`-caterpillar as

`2^(k-2)/(k-1)!`.

This appears literally in their primary text
([author PDF](https://web.math.nccu.edu.tw/mfuchs/parameters_pt_rev.pdf),
[DOI](https://doi.org/10.1007/s00285-009-0275-6)).  Their paper cites
Rosenberg's earlier study of `r`-caterpillars under the Yule model
([DOI](https://doi.org/10.1007/s00026-006-0278-6)).

The “ordered-history” presentation does not create a residual difference.
Uniform ranked plane trees have `(n-1)!` histories, and forgetting ranks and
plane order gives the Yule--Harding law.  This is the same equivalence used in
Disanto et al.'s Lemmas 3.3--3.4 and Proposition 3.5.  Setting `k=n` in the
Chang--Fuchs table gives exactly

`P(X_n=n)=2^(n-2)/(n-1)!`.

Disanto et al. additionally own the fact that the caterpillar is the
root-configuration minimizer.  Thus both the extremal shape and its exact
probability were in the literature before P121.

### Verdict and required subtraction

**ABANDON AS A RESIDUAL; ZERO CREDIT.**  This formula may remain only as an
owned normalization/corollary, with Chang--Fuchs (and preferably Rosenberg
2006) cited.  It should not appear in an abstract or contribution list as a
residual result, even with a “no priority” disclaimer: a no-priority claim is
not the same as an accurate direct-owner attribution.

## Required owner-facing ceiling

P121 retains a potentially defensible two-part residual only after the
following subtraction:

1. Credit Andriantiana--Wagner--Wang for fixed-tree antichains of specified
   cardinality and restrict (i) to the Yule-averaged bivariate OGF/closed
   form.
2. Treat the arbitrary-order moment recurrence as a mechanical consequence
   of Disanto et al.'s exact law; restrict (ii) to the strict `r>=3` radius
   continuation.
3. Remove the caterpillar probability from the residual/contribution set and
   attribute the exact formula directly to Chang--Fuchs 2010, with the older
   Rosenberg 2006 pattern owner noted.
4. Preserve the current hard ceiling: no full `r>=3` coefficient asymptotic,
   no uniqueness of the complex dominant singularity, and no priority claim.

Until that direct-owner repair is made and independently checked, the paper
remains **EXTERNAL HOLD**.

## Primary-source register

- F. Disanto, M. Fuchs, A. R. Paningbatan, and N. A. Rosenberg (2022),
  [journal PDF](https://rosenberglab.stanford.edu/papers/DisantoEtAl2022-AAP.pdf),
  [DOI 10.1214/22-AAP1791](https://doi.org/10.1214/22-AAP1791).
- E. O. D. Andriantiana, S. Wagner, and H. Wang (2013),
  [primary EJC PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i3p28/pdf),
  [DOI 10.37236/3101](https://doi.org/10.37236/3101).
- H. Chang and M. Fuchs (2010),
  [author PDF](https://web.math.nccu.edu.tw/mfuchs/parameters_pt_rev.pdf),
  [DOI 10.1007/s00285-009-0275-6](https://doi.org/10.1007/s00285-009-0275-6).
- N. A. Rosenberg (2006),
  [DOI 10.1007/s00026-006-0278-6](https://doi.org/10.1007/s00026-006-0278-6).
- E. Lappo and N. A. Rosenberg (2024),
  [primary open text](https://pmc.ncbi.nlm.nih.gov/articles/PMC10704929/),
  [DOI 10.1016/j.dam.2023.09.033](https://doi.org/10.1016/j.dam.2023.09.033).
- F. Disanto, M. Fuchs, C.-Y. Huang, A. R. Paningbatan, and N. A. Rosenberg
  (2024),
  [author PDF](https://web.math.nccu.edu.tw/mfuchs/TotConfig_revisionFV.pdf),
  [DOI 10.1016/j.aam.2023.102594](https://doi.org/10.1016/j.aam.2023.102594).
- M. Fuchs (2025),
  [primary open text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11867161/),
  [DOI 10.1098/rstb.2023.0304](https://doi.org/10.1098/rstb.2023.0304).

Database coverage, indexing lag, variant terminology, and inaccessible
non-indexed sources prevent any no-hit statement from proving novelty.  The
two `PROCEED WITH CAUTION` decisions above mean only that this bounded audit
found no literal direct owner after the stated subtraction.

## Post-repair verification

### Scope and method

This is a source-only follow-up against the owner-facing ceiling above.  I
read the current `main.tex`, `README.md`, `PAPER_PLAN.md`,
`NARRATIVE_REPORT.md`, `CLAIMS_EVIDENCE.md`, and `BUILD.md`, and searched
those six files for every occurrence of the fixed-tree marker, the
all-order moment identity, caterpillars/minimum mass, contribution/residual
language, and the `r>=3` ladder.  I did not edit any source/support file and
did not consult `HOSTILE_REVIEW_A.md`.

### Claim-by-claim check

1. **Andriantiana--Wagner--Wang fixed-tree marker: RESOLVED.**  The
   manuscript attributes the fixed-tree cardinality refinement at
   `main.tex:98--101` and, more explicitly, the cardinality marker and
   equivalent root-subtree leaf statistic at `main.tex:231--237`.
   `README.md:18--20`, `PAPER_PLAN.md:24--28,38--42`,
   `NARRATIVE_REPORT.md:40--43`, `CLAIMS_EVIDENCE.md:10`, and
   `BUILD.md:37--40` preserve that subtraction.  The bibliography entry is
   present with DOI `10.37236/3101`.

2. **All-order identity at zero credit: RESOLVED IN THE MANUSCRIPT, WITH
   ONE SUPPORT-DOCUMENT WORDING MISS.**  The abstract calls it a mechanical
   expansion (`main.tex:58--60`); the residual list makes it only an
   interface (`main.tex:124--127`); and the proposition aftermath explicitly
   assigns zero contribution credit (`main.tex:326--330`).  The same explicit
   zero-credit fence appears in `README.md:32--34`,
   `PAPER_PLAN.md:43--46`, and `CLAIMS_EVIDENCE.md:11`.  By contrast,
   `NARRATIVE_REPORT.md:61--68` displays the all-order identity and says only
   that orders one and two are owned.  That wording can still suggest that
   the arbitrary-order identity is part of the residual.  It should say
   explicitly that the identity itself is the mechanical binomial expansion
   of the owned exact law and receives zero credit.  `BUILD.md:39--41`
   correctly locks the residual to two items, so it creates no contrary
   claim, although it does not independently restate this zero-credit
   sentence.

3. **Chang--Fuchs/Rosenberg and caterpillar subtraction: RESOLVED.**  The
   direct formula and owners are stated at `main.tex:102--105` and again at
   `main.tex:502--508`; the proposition is labelled fully owned and receives
   zero contribution credit.  The abstract contains no caterpillar/minimum
   result, and the manuscript's residual/contribution list at
   `main.tex:118--128` contains only the marked average and the `r>=3`
   continuation.  `README.md:19--20,32--34`,
   `PAPER_PLAN.md:24--28,51--52`, `NARRATIVE_REPORT.md:84--91`,
   `CLAIMS_EVIDENCE.md:15`, and `BUILD.md:37--41` likewise retain the mass
   only as owned background/control.  Bibliography entries include
   Chang--Fuchs DOI `10.1007/s00285-009-0275-6` and Rosenberg DOI
   `10.1007/s00026-006-0278-6`.

4. **Two-part residual ceiling: SUBSTANTIVELY RESOLVED, BUT THREE STALE
   SHORTHANDS SHOULD BE NARROWED.**  The abstract (`main.tex:57--64`), exact
   residual list (`main.tex:118--128`), and conclusion
   (`main.tex:574--579`) leave only (i) the Yule-averaged marked transform and
   (ii) the strict radius/pole continuation beginning at `r=3`.  README's
   two-item list, the plan's one-sentence contribution, the claims map, and
   the build summary agree.  Nevertheless, three bounded-search sentences
   still say **“all-r/all-order pole ladder”**: `main.tex:141--144`,
   `README.md:36--39`, and `PAPER_PLAN.md:79--83`.  Because the low-order
   base is owned, the exact owner-safe object searched for is “the strict
   `r>=3` continuation of the owned low-order ladder.”  These are scope
   shorthands rather than theorem overclaims, but they should be conformed.

   A second minor structural ambiguity occurs at `PAPER_PLAN.md:33`: the
   heading “Frozen residual claims” governs a list that also contains an
   identification-only lemma, the zero-credit all-order interface, and the
   fully owned caterpillar normalization.  The item-level caveats are
   correct, but a heading such as “Frozen claim ledger: residuals and owned
   controls,” or separating the two true residuals, would make the owner
   fence literal.

### Post-repair verdict

**SUBSTANTIVE OWNER REPAIR PASSES; PHRASE-LEVEL CLEANUP REMAINS.**  No
caterpillar claim leaks into the abstract or contribution package, and no
mathematical theorem is presently counted beyond the two permitted
residuals.  The unresolved text is limited to the missing explicit
zero-credit sentence in `NARRATIVE_REPORT.md`, the three “all-r/all-order
pole ladder” search shorthands, and the overbroad plan heading.  External
status remains **HOLD**; this source check is not a novelty or priority
clearance.

**FINAL POST-CLEANUP SOURCE VERDICT: PASS.**  All previously listed phrase-level misses are resolved; the residual is now stated consistently as only the Yule-averaged marked transform and the strict `r>=3` continuation of the owned low-order ladder, with the all-order identity and caterpillar normalization at zero credit.  External status remains **HOLD**.
