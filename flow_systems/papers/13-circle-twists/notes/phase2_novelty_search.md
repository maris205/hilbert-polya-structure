# Paper 13 Phase-2 bounded exact-package precedent search

## Search preregistration (frozen before retrieval)

- **Status at preregistration:** `SEARCH_PREREGISTERED_RESULTS_PENDING`.
- **Phase-1 authorization gate:** SHA-256 `8a97a0bedcb048f1c9aa7db18d43bde45b17f1d7e92d38d2eeace688c64aee19` (value supplied by the coordinating lane; this search does not reinterpret or edit the gate).
- **Preregistered at:** 2026-08-15T10:07:10+08:00.
- **Search cutoff:** records publicly discoverable by 2026-08-15.
- **Hard wall-clock stop:** 2026-08-15T11:07:10+08:00.
- **Role and scope:** Phase-2 bibliography/source-verification only. This report is a bounded precedent screen, not a proof review, novelty certificate, priority claim, or standalone decision.
- **Artifact rule:** inspect search records, HTML abstracts, DOI records, and publisher landing pages only. Do not download or retain PDFs. Do not read sibling Paper-13 Phase-2 reports.

### Preregistered search arms

**Arm A — continuous-real-line multiplier and standard twisted-algebra package.** Search for a single source or a tightly related prior-art family covering all or part of this conjunction:

1. continuous normalized circle-valued multipliers (continuous (2)-cocycles) on the additive group \(\mathbb R\);
2. triviality/cohomology collapse by a continuous circle-valued (1)-cochain (gauge/coboundary), with Sorkin's 1978 result treated as an exact prior-art sentinel rather than as new Paper-13 content;
3. the corresponding twisted convolution and involution formulas and gauge intertwiner;
4. passage to regular and full/reduced (C^*)-completions (including the amenable-group identification where invoked).

**Arm B — topology/support-transfer obstruction and conditional arithmetic instance.** Search for a single source or a tightly related prior-art family covering all or part of this conjunction:

1. one underlying carrier equipped first with its actual indiscrete topology and then with a same-carrier orbitwise-standard/disjoint-union topology;
2. the identity-induced comparison of the corresponding transformation/action groupoids;
3. a time-only kernel (\Phi(f)(x,t)=f(t)), whose actual support is (X\times\operatorname{supp}f), and whose pulled-back standard support is (\operatorname{Std}(X)\times\operatorname{supp}f);
4. the exact compact-support obstruction (J^*\Phi_{\mathrm{actual}}(f)\in C_c(G_{\mathrm{std}}(X))\) iff (f=0) or the orbit set (Q=X/\mathbb R) is finite;
5. preservation of support by a nowhere-zero circle-valued gauge;
6. only the conditional fixed-prime rational-Witt substitution (H=(\log p)\mathbb Z\), (Q=Q_p): nonzero transfer iff (Q_p) is finite, with no assertion that (Q_p) is finite or infinite and no unproved cardinality, measure, or topology assertion.

The arms are searched and adjudicated separately. A work that covers Arm A does not count as a hit for Arm B. Generic facts may be nearest precedents but are not promoted to an exact-package match.

### Exact-package flags (fixed decision rule)

- **`A_DIRECT_EXACT_PACKAGE=YES`** only if one externally published work states or proves all four Arm-A elements on the continuous \(\mathbb R\)/circle-multiplier domain, including the algebraic gauge and completion consequences. Otherwise the value is `NO_WITHIN_SEARCH`; component matches are listed separately.
- **`B_DIRECT_EXACT_PACKAGE=YES`** only if one externally published work contains all six Arm-B elements on the same owner/carrier/domain, including the exact iff and the rational-Witt conditional application. Otherwise the value is `NO_WITHIN_SEARCH`; elementary or partial component matches are listed separately.
- **`COMBINED_DIRECT_EXACT_PACKAGE=YES`** only if one external work contains both complete arms in their above conjunction. Any direct exact-package `YES` triggers the pipeline consequence `NOTE_OR_MERGE`; absence within this bounded screen cannot establish priority.

### Endpoints, literal queries, and fixed caps

Discovery records are screened from the displayed result set only; “returned” below never means an endpoint's unobserved total-hit estimate.

| ID | Endpoint | Literal query | Display cap |
|---|---|---|---:|
| A-C1 | Crossref works metadata | `Sorkin 1978 continuous multipliers real line` | 10 |
| A-C2 | Crossref works metadata | `continuous multiplier real line twisted convolution gauge C star algebra` | 10 |
| B-C1 | Crossref works metadata | `indiscrete topology transformation groupoid compact support finitely many orbits` | 10 |
| B-C2 | Crossref works metadata | `rational Witt groupoid cocycle compact support` | 10 |
| A-O1 | OpenAlex works metadata | `continuous multiplier R circle cocycle coboundary projective representation` | 10 |
| A-O2 | OpenAlex works metadata | `twisted group C star algebra real line cohomologous cocycle` | 10 |
| B-O1 | OpenAlex works metadata | `orbitwise topology groupoid compact support finite orbits` | 10 |
| B-O2 | OpenAlex works metadata | `rational Witt dynamics transformation groupoid` | 10 |
| A-R1 | arXiv search/abstract index | `"continuous multiplier" "real line"` | 10 |
| A-R2 | arXiv search/abstract index | `"twisted convolution" gauge cocycle` | 10 |
| B-R1 | arXiv search/abstract index | `"indiscrete topology" groupoid "compact support"` | 10 |
| B-R2 | arXiv search/abstract index | `"rational Witt" groupoid` | 10 |
| A-W1 | General scholarly web index | `"Sorkin" multiplier "real line" 1978` | 10 |
| A-W2 | General scholarly web index | `"continuous multipliers" "real line" cocycle` | 10 |
| A-W3 | General scholarly web index | `"projective representations" R multiplier coboundary` | 10 |
| A-W4 | General scholarly web index | `"twisted convolution" "real line" gauge` | 10 |
| A-W5 | General scholarly web index | `"twisted group C*-algebra" R cocycle cohomologous` | 10 |
| A-W6 | General scholarly web index | `"continuous multiplier" R "full" "reduced" C*-algebra` | 10 |
| B-W1 | General scholarly web index | `"indiscrete topology" "compact support" groupoid` | 10 |
| B-W2 | General scholarly web index | `"indiscrete" "transformation groupoid" "compact support"` | 10 |
| B-W3 | General scholarly web index | `"orbitwise" groupoid "compact support"` | 10 |
| B-W4 | General scholarly web index | `"compact support" "finitely many orbits" groupoid` | 10 |
| B-W5 | General scholarly web index | `"nowhere zero" gauge support "twisted groupoid"` | 10 |
| B-W6 | General scholarly web index | `"rational Witt" groupoid cocycle "compact support"` | 10 |

The primary budget is therefore exactly 24 queries and at most 240 displayed records. If and only if an arm yields zero retainable candidates after all twelve of its primary queries, activate its one fixed fallback query:

| ID | Endpoint | Literal query | Display cap |
|---|---|---|---:|
| A-F1 | General scholarly web index | `"multiplier representations" R cocycle Sorkin` | 10 |
| B-F1 | General scholarly web index | `"disjoint union" "compact support" "finite components" groupoid` | 10 |

Thus the absolute discovery ceiling is 26 queries/260 displayed records. Verify at most 20 distinct candidate identities on official DOI, publisher, journal, institutional-repository, or arXiv HTML landing pages. Citation chaining is limited to two bibliographic links per retained candidate and twelve links total; it is used only to verify a named nearest precedent, not to expand the query vocabulary. Duplicate versions are merged by DOI and normalized title.

### Inclusion and exclusion rules

**Include for full assessment:**

- primary mathematical research articles, books/chapters, proceedings, or preprints whose title/abstract/official metadata bears directly on at least one registered conjunction element;
- foundational sources outside a recent-date window, because the question is historical precedent rather than state-of-the-art performance;
- continuous topological-group results on \(\mathbb R\), and standard twisted convolution/group-(C^*) references, when their owner, regularity, or completion statement can be verified;
- transformation/action-groupoid or topology results that genuinely bear on same-carrier topology change, compact support across components/orbits, or support under a nowhere-zero gauge;
- rational-Witt sources only where official metadata or accessible HTML states a relevant dynamical/groupoid/topological construction.

**Exclude from exact-package status (but record as near misses when useful):**

- measurable/Borel multipliers without the required continuous statement; higher-dimensional vector groups or unrelated groups unless used solely as a comparator;
- generic cocycle, projective-representation, or (C^*)-algebra sources lacking the registered domain/regularity or gauge/completion link;
- generic compact-support facts for coproducts/disjoint unions that do not use the same carrier and the actual-to-standard groupoid comparison;
- proxy or quotient topology results that do not match the actual indiscrete and orbitwise-standard owners;
- rational-Witt papers lacking the registered conditional support-transfer statement;
- Papers 11–13, internal notes, secondary summaries, snippets without recoverable source identity, duplicates, retracted/fabricated items, and any record whose existence cannot be independently verified.

Languages are English for query execution; records in other languages may be included if indexed with enough translated metadata to apply the criteria. No lower publication-date bound is imposed. Source claims are graded relative to pure mathematics: a peer-reviewed primary proof or authoritative monograph is the field-standard source; preprints are retained with an explicit status caveat.

### Screening and stopping procedure

1. Run the 24 literal primary queries without changing wording.
2. Record endpoint success/failure, displayed records screened, deduplicated candidate identities retained, and exclusion reason classes in the query ledger.
3. Apply title/abstract screening, then verify retained identities and claim scope on official HTML/metadata pages. Abstract-only access can establish identity and advertised scope, but not an unstated theorem.
4. Record the nearest precedents arm by arm, including what each covers and every missing conjunction element.
5. Apply the fixed exact-package flags. Stop after the registered query and verification caps or the wall-clock deadline, whichever occurs first. Do not infer an absence beyond this search frame.

### Preregistered outcome vocabulary

- Maximum positive novelty-search wording: **`SUPPORTED_WITHIN_SEARCH`**.
- If a direct exact package is found: **`NOTE_OR_MERGE`**.
- If none is found: **`NO_DIRECT_EXACT_PACKAGE_FOUND_WITHIN_BOUNDED_SEARCH`**, never “novel,” “first,” “unprecedented,” or an equivalent priority claim.
- Standalone implication is conditional only: this search can leave the central package eligible for later proof/domain/owner adjudication; it cannot itself pass the standalone gate.

## Search execution ledger

### Execution receipt

- **Final status:** `SUPPORTED_WITHIN_SEARCH` — `NO_DIRECT_EXACT_PACKAGE_FOUND_WITHIN_BOUNDED_SEARCH`.
- **Search ran:** 2026-08-15T10:07:10+08:00 through 2026-08-15T10:19:36+08:00.
- **Primary queries attempted:** 24/24, with the literal strings above.
- **Conditional fallbacks:** Arm A fallback not activated because Sorkin and standard twisted-algebra candidates were retained. Arm B fallback `B-F1` was activated because no Arm-B candidate survived the complete-conjunction screen. Total discovery queries executed: 25.
- **Displayed result cards screened:** 119 after enforcing the registered ten-card/query ceiling. This is a card count, not a count of unique publications: the browsing interface coalesced some multi-query responses and repeated versions across endpoints.
- **Candidate identities advanced to official-metadata/scope verification:** 10; no identity exceeded the registered two-link chain and the total stayed below the 20-identity ceiling.
- **PDF handling:** no PDF was downloaded, copied, or retained. Some search indexes exposed text snippets from PDF-backed records; those snippets were treated as discovery data only. Verification used HTML metadata, abstract/landing pages, DOI records where reachable, and institutional bibliographic pages.
- **Endpoint degradations:** Crossref REST returned HTTP 429 at its base and its query URLs were blocked by the browser's safe-URL layer. The same four literal strings were therefore checked through a Crossref-domain index, which returned 18 coalesced, irrelevant cards. Direct OpenAlex API opening was blocked by the same safe-URL layer; the same four literal strings were checked through an OpenAlex-domain index, which returned 15 coalesced cards and no relevant work records. These degradations are limitations, not negative database results.

### Per-query ledger

For coalesced four-query web responses, the interface did not expose a defensible per-query card attribution. The ledger therefore reports the registered per-query ceiling (`<=10`) and the exact batch total rather than inventing per-query counts.

| ID | Endpoint outcome and screened count | Retained signal | Inclusion/exclusion disposition |
|---|---|---|---|
| A-C1 | Crossref REST degraded; Crossref-domain batch A-C1–B-C2: 18 cards total | none | No relevant Crossref work record exposed; endpoint degradation recorded |
| A-C2 | same batch, `<=10` attributable cards | none | Generic multiplier/electronics records excluded |
| B-C1 | same batch, `<=10` attributable cards | none | Unrelated compact-manifold/orbit records excluded |
| B-C2 | same batch, `<=10` attributable cards | none | No rational-Witt/groupoid conjunction record |
| A-O1 | OpenAlex-domain batch A-O1–B-O2: 15 cards total | none | OpenAlex help/topic pages and unrelated works excluded |
| A-O2 | same batch, `<=10` attributable cards | none | No usable work-level metadata exposed |
| B-O1 | same batch, `<=10` attributable cards | none | Unrelated topology/topic pages excluded |
| B-O2 | same batch, `<=10` attributable cards | none | No rational-Witt transformation-groupoid record |
| A-R1 | arXiv domain, 0 cards | none | zero displayed |
| A-R2 | arXiv domain, 4 cards | Austad 2021 | Included as continuous-cocycle/twisted-convolution precedent; three unrelated Hopf/gerbe records excluded |
| B-R1 | arXiv domain, 0 cards | none | zero displayed |
| B-R2 | arXiv domain, 0 cards | none | zero displayed |
| A-W1 | web batch A-W1–A-W4: 30 cards total, `<=10` attributable | Sorkin 1978 | Included; exact Arm-A cohomological sentinel |
| A-W2 | same batch, `<=10` attributable | Sorkin/Cattaneo lead | Included for identity follow-up; Fourier-multiplier homonyms excluded |
| A-W3 | same batch, `<=10` attributable | standard projective-representation background | Background only; finite/discrete/Borel-only records excluded from exact status |
| A-W4 | same batch, `<=10` attributable | Austad lead | Included as standard algebraic precedent, not an \(\mathbb R\)-triviality source |
| A-W5 | web batch A-W5–B-W2: 23 cards total, `<=10` attributable | Packer–Raeburn/Gillaspy leads | Included after identity verification; unrelated \(\mathbb Z^2\), quantum-group, and finite-group records excluded |
| A-W6 | same batch, `<=10` attributable | Omland; Sims–Williams | Included only for the standard amenable full/reduced completion component |
| B-W1 | same batch, `<=10` attributable | generic indiscrete compactness | Excluded from exact corpus: textbook-level topology only, no same-carrier groupoid map |
| B-W2 | same batch, `<=10` attributable | generic twisted groupoid records | Excluded from Arm-B exact status: no topology/support-transfer iff |
| B-W3 | web batch B-W3–B-W6: 19 cards total, `<=10` attributable | none | “orbitwise” homonyms and unrelated action/groupoid records excluded |
| B-W4 | same batch, `<=10` attributable | Ronchetti notes; Venkatesh context | Retained as the nearest finite-orbit-support/pullback comparator only |
| B-W5 | same batch, `<=10` attributable | Gillaspy gauge comparator | Retained for the cohomologous-cocycle multiplier map only; no support theorem advertised |
| B-W6 | same batch, `<=10` attributable | none | Rational-Witt algebra records lacking dynamics/groupoids/support were excluded |
| A-F1 | not run | n/a | Activation condition false |
| B-F1 | 12 cards displayed; first 10 screened per cap | none | All ten were unrelated automorphic, geometry, or generic compact-support records |

### Screening flow and exclusion ledger

The 119 screened cards collapsed by DOI/normalized title into ten identities worth verifying. The remaining cards were duplicates or failed at title/abstract screening. Because the interface coalesced result sets, a publication-level duplicate count cannot be reconstructed honestly; no pseudo-PRISMA precision is asserted.

| Stage | Count | Notes |
|---|---:|---|
| Primary queries attempted | 24 | 12 per arm |
| Conditional fallback queries attempted | 1 | B-F1 only |
| Displayed cards screened | 119 | after the fixed per-query cap |
| Distinct candidate identities scope-checked | 10 | 9 peer-reviewed articles (preprint/published versions deduplicated) and 1 unpublished-note comparator |
| Arm-A sources retained as direct or standard component precedents | 7 | Sorkin; Cattaneo (identity/title lead); Packer–Raeburn; Austad; Gillaspy; Omland; Sims–Williams |
| Arm-B direct-package sources retained | 0 | no source met the six-element conjunction |
| Arm-B partial comparators retained | 3 | Ronchetti, Venkatesh, and Gillaspy; none matches the owner/domain/topology package |
| Rational-Witt conditional-package records retained | 0 | algebraic Witt-ring or Witt-vector records without the registered dynamical support statement were excluded |

Primary exclusion classes were: multiplier homonyms from Fourier/operator/electronic engineering; Borel-only or discrete/finite-group projective representation results; higher-dimensional noncommutative-torus examples; generic twisted group/groupoid \(C^*\)-algebra papers without the \(\mathbb R\) collapse; generic indiscrete/discrete topology facts; “finite orbit” results in unrelated representation theory or dynamical systems; and rational-Witt algebra references without a transformation groupoid, topology comparison, compact-support iff, or conditional \(Q_p\) application.

## Arm A findings: exact prior art and standard package components

### A1. Exact cohomological sentinel

Rafael D. Sorkin's article, **“The triviality of continuous multipliers for the real line,”** *International Journal of Theoretical Physics* 17(5), 369–376 (1978), DOI [10.1007/BF00674107](https://doi.org/10.1007/BF00674107), is an exact prior-art match for the central continuous-\(\mathbb R\) multiplier-collapse claim. The indexed abstract says that every continuous group multiplier for \(\mathbb R\) can be reduced to the identity by a continuous “remultiplication” ([bibliographic/abstract record](https://eurekamag.com/research/088/939/088939666.php)). The official Springer article URL timed out and Crossref was rate-limited during this run, so the identity was triangulated from the DOI-bearing abstract record and an independent author bibliography; theorem details beyond the advertised abstract were not silently inferred.

**Consequence:** Paper 13 must cite and accurately delimit Sorkin wherever it states continuous \(\mathbb R\)-multiplier triviality or constructs the continuous gauge. This result is prior art, not a Paper-13 originality contribution.

U. Cattaneo's **“Locally Continuous Multipliers for Topological Vector Groups,”** *Mathematische Annalen* 239, 1–6 (1979), DOI [10.1007/BF01420489](https://doi.org/10.1007/BF01420489), is a nearby generalization lead verified through [EuDML metadata](https://eudml.org/doc/163201). The accessible record supplied no abstract and its full HTML timed out, so this screen does not claim which exact triviality theorem it proves. It should be checked in full before using it for a theorem-level sentence.

Cattaneo's **“Borel multipliers for the Bondi–Metzner–Sachs group,”** *Journal of Mathematical Physics* 20, 2257–2263 (1979), DOI [10.1063/1.524006](https://doi.org/10.1063/1.524006), is verified on the [AIP article page](https://pubs.aip.org/aip/jmp/article/20/11/2257/449558/Borel-multipliers-for-the-Bondi-Metzner-Sachs). It is useful historical context for Sorkin's stated BMS motivation, but it is Borel and on a different group; it is excluded from the continuous-\(\mathbb R\) exact flag.

### A2. Standard twisted convolution, gauge, and completion precedents

No single retrieved source combined Sorkin's exact \(\mathbb R\) collapse with every algebraic and completion consequence. The remaining elements are nevertheless standard prior art distributed across established sources:

1. Judith A. Packer and Iain Raeburn, **“Twisted crossed products of \(C^*\)-algebras,”** *Mathematical Proceedings of the Cambridge Philosophical Society* 106(2), 293–311 (1989), DOI [10.1017/S0305004100078129](https://doi.org/10.1017/S0305004100078129). The [publisher record](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/twisted-crossed-products-of-calgebras/79B8947245C46351F7F003D7F3BFBC39) explicitly describes locally compact groups, two-cocycle-twisted multiplication, and the corresponding twisted crossed-product \(C^*\)-algebras. It is a foundational algebra/completion reference, not an \(\mathbb R\)-triviality result.

2. Are Austad, **“Spectral invariance of \(^*\)-representations of twisted convolution algebras with applications in Gabor analysis,”** *Journal of Fourier Analysis and Applications* 27, article 56 (2021), DOI [10.1007/s00041-021-09860-z](https://doi.org/10.1007/s00041-021-09860-z). The [institutional published-version record](https://ntnuopen.ntnu.no/ntnu-xmlui/handle/11250/3134507) and [arXiv abstract](https://arxiv.org/abs/2002.02235) state the locally compact group, continuous \(2\)-cocycle, and twisted convolution algebra \(L^1(G,c)\). It is a direct standard-formula/representation precedent but does not advertise Sorkin's real-line collapse.

3. Elizabeth Gillaspy, **“K-theory and homotopies of 2-cocycles on higher-rank graphs,”** *Pacific Journal of Mathematics* 278(2), 407–426 (2015), DOI [10.2140/pjm.2015.278.407](https://doi.org/10.2140/pjm.2015.278.407), [arXiv:1403.3799](https://arxiv.org/abs/1403.3799). Its published treatment recalls twisted groupoid convolution/completion and states that multiplication by the continuous cochain implements an isomorphism for cohomologous cocycles. This is a close general gauge-intertwiner precedent, but on locally compact Hausdorff groupoids/higher-rank graphs rather than the Paper-13 real-line-plus-topology owner.

4. Tron Ånen Omland, **“Primeness and primitivity conditions for twisted group \(C^*\)-algebras,”** *Mathematica Scandinavica* 114(2), 299–319 (2014), DOI [10.7146/math.scand.a-17113](https://doi.org/10.7146/math.scand.a-17113). The [journal page](https://www.mscand.dk/article/view/17113) verifies the identity; the indexed paper text records that for an amenable group the full and reduced twisted group \(C^*\)-algebras are isomorphic. Its paper domain is discrete groups, so it is corroborating standard context, not the best owner match for \(\mathbb R\).

5. Aidan Sims and Dana P. Williams, **“Amenability for Fell bundles over groupoids,”** *Illinois Journal of Mathematics* 57(2), 429–444 (2013), DOI [10.1215/ijm/1408453589](https://doi.org/10.1215/ijm/1408453589), [arXiv:1201.0792](https://arxiv.org/abs/1201.0792). The abstract proves equality of full and reduced \(C^*\)-algebras for Fell bundles over measurewise amenable groupoids. This supplies a broader completion theorem; it does not supply the \(\mathbb R\) cocycle trivialization or Paper-13 support-transfer statement.

### Arm-A exact-package decision

- `A_DIRECT_EXACT_PACKAGE=NO_WITHIN_SEARCH` under the preregistered **single-work/all-four-elements** rule.
- `A_COMPONENT_PRIOR_ART=CONFIRMED`: Sorkin is exact for continuous real-line multiplier triviality; twisted convolution, gauge-induced algebra isomorphism, and completion consequences are standard and well represented by the cited prior-art family.
- **Manuscript treatment required:** present Arm A as credited background/derived consequence, with sign/convention checks done in the manuscript's own notation. It cannot carry the standalone contribution.

## Arm B findings: same-carrier support-transfer package

### B1. Nearest finite-orbit support/pullback comparator

Niccolò Ronchetti's technical notes **“Satake map for the mod \(p\) derived Hecke algebra”** were surfaced on a Stanford-hosted URL; a [UC San Diego seminar page](https://math.ucsd.edu/seminar/satake-homomorphism-mod-p-derived-hecke-algebra) independently verifies the author, title/topic, and institutional context. The indexed note text formulates derived Hecke objects as groupoid-cohomological data with support on finitely many orbits and checks that pullback/pushforward preserves compact support by finite-fiber conditions on connected components.

This is the closest structural comparator found, but it is **not** a direct Paper-13 precedent: it concerns \(p\)-adic Hecke groupoids, finite covering/fiber hypotheses, and compactly supported cohomology. It has no actual indiscrete topology, no same-carrier orbitwise-standard retopologization, no time-only kernel \(\Phi(f)\), no exact `f=0 or Q finite` theorem, no circle-gauge support statement, and no rational-Witt substitution. It is also an unpublished-note comparator, so it cannot support an absence or priority claim.

Akshay Venkatesh's peer-reviewed **“Derived Hecke algebra and cohomology of arithmetic groups,”** *Forum of Mathematics, Pi* 7, e7 (2019), DOI [10.1017/fmp.2019.6](https://doi.org/10.1017/fmp.2019.6), [arXiv:1608.07234](https://arxiv.org/abs/1608.07234), verifies the surrounding compactly supported/double-coset Hecke context. It is farther from the registered topology-transfer owner and likewise misses every distinctive same-carrier/rational-Witt element.

### B2. Gauge/support comparator

Gillaspy's published groupoid treatment above is the nearest verified source for the **gauge multiplication** part: cohomologous continuous circle cocycles are intertwined by multiplication by a continuous circle-valued cochain. Because a circle-valued cochain is nowhere zero, equality of zero sets/supports is an elementary consequence of the multiplier map. The searched source does not advertise the Paper-13 compact-support iff and does not combine the gauge with the actual-indiscrete/orbitwise-standard comparison. Accordingly, it is a component precedent only, not a B-package hit.

### B3. Topology comparison, exact iff, and rational-Witt application

The indiscrete-topology queries returned only generic textbook-level observations (for example, that indiscrete spaces have extremely broad compactness behavior), while the orbitwise/disjoint-union queries returned unrelated finite-orbit statements. No eligible source used the **same underlying carrier** with the registered actual and standard topologies and then proved the registered transformation-groupoid compact-support iff.

The two rational-Witt queries and the fallback returned no eligible dynamical/groupoid source. Results defining rational Witt rings or using Witt-vector affine flags were excluded because they did not contain the registered support-transfer statement. Therefore this search supplies no external evidence about whether a particular \(Q_p\) is finite or infinite; the Paper-13 arithmetic sentence must remain exactly conditional.

### Arm-B exact-package decision

- `B_DIRECT_EXACT_PACKAGE=NO_WITHIN_SEARCH`.
- No single source, and no source family retrieved in this bounded search, contained the actual-indiscrete to same-carrier orbitwise-standard transformation-groupoid comparison together with the time-only support computation, exact finite-orbit iff, gauge-support preservation, and rational-Witt conditional application.
- This is a **dated bounded-search result**, not proof of novelty or priority. The distinctive phrasing may be manuscript-specific and therefore resistant to bibliographic retrieval.

## Direct-package matrix

| Source | Continuous \(\mathbb R\) multiplier collapse | Twisted convolution/gauge/completion | Same-carrier topology change | Exact \(C_c\) finite-orbit iff | Gauge support preservation | Rational-Witt conditional | Direct exact package? |
|---|---:|---:|---:|---:|---:|---:|---:|
| Sorkin 1978 | **yes** (advertised theorem) | no advertised completion package | no | no | no | no | no |
| Cattaneo 1979, Math. Ann. | title-level general multiplier lead; theorem not fully verified here | not verified | no | no | no | no | no |
| Packer–Raeburn 1989 | no | **yes**, standard twisted crossed-product framework | no | no | no | no | no |
| Austad 2021 | no | **yes**, continuous-cocycle twisted convolution/representations | no | no | no | no | no |
| Gillaspy 2015 | no | **yes**, groupoid cocycle/gauge/full completion component | no | no | elementary support consequence only | no | no |
| Omland 2014 / Sims–Williams 2013 | no | full/reduced amenability component | no | no | no | no | no |
| Ronchetti notes | no | no | no | analogous finite-fiber/finitely-many-orbits support condition only | no | no | no |
| Venkatesh 2019 | no | no | no | contextual compactly supported Hecke setting only | no | no | no |

Final flags:

```text
A_DIRECT_EXACT_PACKAGE=NO_WITHIN_SEARCH
B_DIRECT_EXACT_PACKAGE=NO_WITHIN_SEARCH
COMBINED_DIRECT_EXACT_PACKAGE=NO_WITHIN_SEARCH
PIPELINE_FORCED_NOTE_OR_MERGE_FROM_DIRECT_PRECEDENT=NO
```

The last line means only that this bounded search did not trigger the **direct-precedent** rule. It does not override the separate methodological rule that routine restatements or failed proof/domain/owner gates require `NOTE_OR_MERGE`.

## Source verification and quality notes

Pure mathematics does not fit the clinical I–VII evidence pyramid literally. The applicable field standard here is a peer-reviewed primary proof or authoritative research monograph. Grades below are fitness-for-this-claim grades, not empirical-study grades.

| Identity | Existence/metadata status | Claim-scope status | Field-fit quality | Venue/COI/red-flag note |
|---|---|---|---|---|
| Sorkin 1978 | strong convergent metadata; DOI and journal coordinates agree; publisher fetch timed out | abstract verifies real-line continuous remultiplication only | A for the advertised theorem | established Springer journal; no predatory signal; ordinary intellectual authorship only |
| Cattaneo 1979, Math. Ann. | EuDML + DOI metadata verified | title only; theorem content not verified | A source / C claim-use until full text checked | established journal; no predatory signal |
| Cattaneo 1979, J. Math. Phys. | AIP publisher page + DOI verified | abstract verifies Borel BMS scope; excluded from continuous-\(\mathbb R\) exact status | A for its own domain | established AIP journal; no predatory signal |
| Packer–Raeburn 1989 | Cambridge publisher record + DOI verified | publisher extract verifies twisted locally compact-group \(C^*\) framework | A | established society journal; no predatory signal |
| Austad 2021 | DOI, arXiv, and NTNU published-version metadata agree | abstract verifies continuous cocycle and twisted convolution scope | A | peer-reviewed Springer journal; no predatory signal |
| Gillaspy 2015 | DOI, arXiv, and Pacific Journal metadata agree | published indexed text verifies cohomologous-cocycle gauge isomorphism context | A | established peer-reviewed journal; no predatory signal |
| Omland 2014 | journal HTML + DOI + arXiv agree | indexed paper text verifies amenable full/reduced statement, on discrete groups | A for its domain; comparator only here | established peer-reviewed journal; no predatory signal |
| Sims–Williams 2013 | DOI, arXiv, author/institution pages agree | abstract verifies full/reduced Fell-bundle theorem | A | established peer-reviewed journal; no predatory signal |
| Venkatesh 2019 | Cambridge DOI + arXiv agree | peer-reviewed contextual scope verified | A | established peer-reviewed journal; no predatory signal |
| Ronchetti notes | Stanford-hosted notes + UCSD seminar identity agree | snippet verifies the finite-fiber/finitely-many-orbits comparator | C comparator | unpublished notes; no venue-grade inflation; not used as theorem authority for Paper 13 |

No retraction, fabricated-identity, impossible-volume, or predatory-venue signal was found for the retained peer-reviewed sources. Funding and author declarations were not systematically available on every historical landing page; no substantive financial conflict was identified, and ordinary authorship-related intellectual interest is not treated as disqualifying.

## Distributional coverage advisory

`DISTRIBUTIONAL_SKEW_ADVISORY`:

- **Dimension:** methodology.
- **Concentration:** theoretical/operator-algebraic or representation-theoretic mathematics = 10/10 verified candidates (100%).
- **Advisory:** this is expected from the registered mathematical question, not a defect and not a novelty signal.
- **Search response:** no expansion; the user-authorized scope is an exact mathematical package, not an empirical literature.

Historical works are intentionally retained because precedent search makes foundational age relevant; the default five-year currency rule is inapplicable to Sorkin, Cattaneo, and Packer–Raeburn. The candidate set spans 1978–2021 and several independent journal/publisher families, so no single-venue concentration controls the conclusion.

## Limitations

1. Crossref and OpenAlex APIs degraded, and MathSciNet/zbMATH full review records and Google Scholar citation graphs were not directly available. Domain-index fallbacks are weaker than native APIs.
2. The no-PDF-retention rule limited assessment to metadata, abstracts, indexed snippets, and HTML. Except where an HTML source stated the result, theorem-level details must be checked by an authorized human/full-text lane before final citation wording.
3. Query language was English and exact-package vocabulary is partly project-specific. A differently named same construction could evade phrase retrieval.
4. The bounded 25-query, 119-card screen is not exhaustive. No negative search result licenses “first,” “novel,” “unprecedented,” or a priority claim.
5. Cattaneo's 1979 topological-vector-group paper is an important unresolved full-text check because its title suggests broader scope than Sorkin. It does not presently change the flag, since even a broad multiplier theorem would still lack the registered Arm-B conjunction.
6. Rational-Witt non-hits do not imply any fact about \(Q_p\). They only show that the registered conjunction was not retrieved under the bounded queries.

## Verdict and conditional standalone implication

**Verdict:** `SUPPORTED_WITHIN_SEARCH` — `NO_DIRECT_EXACT_PACKAGE_FOUND_WITHIN_BOUNDED_SEARCH` as of 2026-08-15. Arm A is demonstrably prior art as a component family and must be credited accordingly. Arm B's full same-owner/same-domain topology-support-gauge-rational-Witt conjunction was not found in this bounded screen.

**Standalone implication (conditional only):** this search does **not** pass Paper 13's standalone gate. If the exact Arm-B theorem later survives proof, source, topology/owner/domain, and nonredundancy review, the absence of a direct package in this dated screen leaves it eligible for a separate standalone adjudication. If a later search finds a direct exact package, or if the theorem is judged a routine/direct restatement of the elementary coproduct-compactness fact plus standard gauge invariance, the required disposition is `NOTE_OR_MERGE`. Arm A alone cannot support standalone status.

## AI-assistance disclosure

This bounded search and screening report was produced with AI-assisted web retrieval and classification. Retrieved content was treated as data rather than instruction. All final manuscript citations and theorem-scope statements require author verification against the original publication under the project's release controls.
