# P67 Stage 2.5 integrity and priority audit

Audit date: **2026-08-26 UTC**  
Manuscript: *Arithmetic Prefixes and Cycle-Matroid Dependence in a Multiplicative Plaquette Shift*  
Audit posture: author-side integrity and search-bounded priority audit, not independent specialist certification  
External state: **HOLD**

## 1. Executive verdict

**Overall Stage 2.5 release-gate verdict: FAIL.**

This is a release-integrity failure, not a finding that the theorem is false. The
global root decomposition, explicit integration formula, product homeomorphism,
arbitrary-finite-shape graphic-matroid theorem, Haar rank law, prefix formula, and
exponent-rectangle formula form a coherent proof chain. The deterministic finite
proof-regression control replayed byte-for-byte and all displayed counts agree with
the script and frozen receipts. No ghost citation, dangling key, unresolved compiled
citation, table discrepancy, or theorem/control contradiction was found.

External release is nevertheless blocked by three objective source/declaration
defects:

1. `KenyonPeresSolomyak2012` has a literal title-field mismatch: the authoritative
   title is “Hausdorff dimension for fractals invariant under multiplicative
   integers,” without the word “the.”
2. The current ownership discussion omits material adjacent owners: Abbe--Spirkl for
   the representable-matroid entropy-rank mechanism, Ban--Hu--Lai--Liao for recent
   affine multiplicative shifts, and Király--Rosen--Theran for graph-symmetric
   matroids. These sources do not state the P67 combined theorem, but they materially
   change the owner subtraction.
3. Author identity/order, contributions, funding, competing interests, and a final
   author-approved AI-use disclosure are unavailable or unresolved.

The exact-combination search found no collision only within the recorded public-Web
queries through 2026-08-26. Collision risk is **MEDIUM**. This audit supplies neither
a worldwide novelty conclusion nor a priority certificate.

Axis decisions:

| Axis | Decision |
|---|---|
| Mathematical/proof consistency | PASS within this audit |
| Existing-reference authenticity | PASS_WITH_ONE_LITERAL_MISMATCH |
| Citation-context fidelity | PASS for 13/13 contexts |
| Numerical/control integrity | PASS as finite proof-regression controls |
| Paragraph-overlap screen | PASS_WITH_TOOL_LIMITATIONS |
| Priority framing | FAIL_PENDING_OWNER_SUBTRACTION |
| Declarations | UNRESOLVED |
| Overall Stage 2.5 release gate | **FAIL** |
| External release | **HOLD** |

## 2. Scope, immutability, and protocol coverage

No manuscript source, bibliography, control source, frozen output, or PDF was edited
during this audit. Work was confined to `stage2_5/`; the pre-existing generated
claim-registry artifacts were preserved. Baseline fingerprints were:

| File | SHA-256 |
|---|---|
| `main.tex` | `940ceda23385c37a2c3f362640c8cd362807685b848329bbf4897b8f2b4984ae` |
| `references.bib` | `2851302e6b59779e23cee662718950514f8220930a8508b42343552f129b58e2` |
| `sections/0_abstract.tex` | `6c85ebb06c2b65a9de7cefd1539e58bb39d267d9c92a4a2e120dc2e7e45bbe9d` |
| `sections/1_introduction.tex` | `fdc642229f41a624642b0bbc82b1cb993a321c6940342d7c404c94d6fbc99ef5` |
| `sections/2_coordinates.tex` | `753f854a67953cda01c212b7944ea0a7de7a38a4ee0c2ffb0bf921edc2efafa7` |
| `sections/3_finite_projections.tex` | `1be0f040f760612682de95b0e459e29f7d26f6894d45dd1fbfe3513af38d8764` |
| `sections/4_prefixes.tex` | `c51ca036caa18671dbd7e1de401dda1610ef55efe755801827d4e74bdf776314` |
| `sections/5_rectangles.tex` | `d319cd07c398100065988ad1d34e0b8139e5a9650f9d260e85f60edae8d137a0` |
| `sections/6_scope.tex` | `9831b3753d5e50931db3bafe9d4e2cc1bbb15c683d1cd66d8558e3c41d56590e` |
| `sections/7_conclusion.tex` | `98d5bb23e906f9ee4f4530e17a071a2452b42d613fa8902845a8feb3fbfef572` |

Protocol coverage:

| Phase | Required surface | Audited surface | Status |
|---|---|---|---|
| A | 100% bibliography entries and stored fields | 8/8 entries; author/title/venue/year/volume/issue/pages/DOI/arXiv as applicable | 7 VERIFIED, 1 MISMATCH, 0 NOT_FOUND |
| B | at least 30% citation contexts | 13/13 citation commands, 100%, against abstracts or original texts | PASS_WITH_BIB_CORRECTION |
| C | all tables, numbers, code/enumeration claims and receipts | all manuscript quantitative surfaces, script branches, stored output, build output | PASS; proof-regression only |
| D | at least 30% body paragraphs and at least one per major section | 21/68 = 30.88%; three from each of Sections 1--7 | PASS_WITH_TOOL_LIMITATIONS |
| E | all HIGH-IMPACT plus at least `min(10,total)` | all 18 semantically identified claim families | PASS_WITH_SOURCE_NOTES |

For Phase E, `semantic completeness=not_machine_detectable`. Semantic extraction can
miss implicit claims, so neither the generated registry nor the human-normalized
registry below can certify completeness. To reduce that risk, all 18 identified
claim families were audited rather than only the protocol minimum of ten.

## 3. Phases A and B — source authenticity and citation fidelity

The query-by-query record, authoritative direct URLs, field decisions, ghost/dangling
comparison, and all 13 context checks are in
[`SOURCE_SEARCH_LEDGER.md`](SOURCE_SEARCH_LEDGER.md).

### A. Bibliography result

- Seven records are **VERIFIED**.
- `KenyonPeresSolomyak2012` is **MISMATCH** only because the BibTeX title inserts
  “the”; the [publisher](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/abs/hausdorff-dimension-for-fractals-invariant-under-multiplicative-integers/3C3FCA7CF3E96B031469BA351CFA0868),
  [arXiv](https://arxiv.org/abs/1102.5136), and
  [DOI record](https://doi.org/10.1017/S0143385711000538) agree on the title without
  that word. The work, DOI, authors, venue, date, volume, issue, and pages are real
  and correct; this is not a ghost citation.
- No record reached `NOT_FOUND`; the three-query failure rule was therefore not
  invoked.

### B. Key and context result

- unique cited keys: 8;
- unique bibliography keys: 8;
- dangling in-text keys: 0;
- uncited bibliography entries: 0;
- ghost works: 0;
- citation commands content-checked: 13/13 (100%);
- substantively unsupported contexts: 0.

The context audit used source abstracts and original texts, not metadata alone. It
confirmed the manuscript's descriptions of multiplicative-integer dimension theory,
two-generator and multidimensional multiplicative shifts, pattern generation,
surface entropy, prime-valuation symbolic models, Whitney's matroid language, and
Watanabe's total correlation. The title mismatch remains a bibliography correction
even though the associated contextual claim is supported.

## 4. Phase C — proof, table, and proof-regression consistency

### C1. Classification and deterministic replay

P67 reports no empirical experiment, sampled dataset, numerical approximation,
statistical inference, fitted model, or randomized run. The Python program is a
deterministic exact finite-field/graph **proof-regression control**. It tests selected
finite consequences; it does not prove the infinite decomposition, product topology
statement, all-shape theorem, or literature status.

Replay command:

```bash
python3 code/verify_plaquette_matroid.py
```

Audit-time receipt:

| Artifact | SHA-256 | Comparison |
|---|---|---|
| `code/verify_plaquette_matroid.py` | `d0a2d3a1bd0c743b375eaf7e2dc98b100ff08f30cd741641cb1fcd81ab98a158` | source fingerprint |
| fresh stdout | `a44506264017a8e6250e123df4477898def6c23f560c67b4e829948967c0bb26` | reference replay |
| `code/verify_plaquette_matroid.out` | `a44506264017a8e6250e123df4477898def6c23f560c67b4e829948967c0bb26` | byte-identical |
| `build/verify_plaquette_matroid.current.out` | `a44506264017a8e6250e123df4477898def6c23f560c67b4e829948967c0bb26` | byte-identical |

The fresh terminal line was `ALL CHECKS PASS`.

This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

Here the required C4 sentence uses “experiment” only as a protocol boundary: this
manuscript contains no experiment.

### C2. Complete code/output/manuscript traceability

| Quantitative or enumerative assertion | Code locator | Frozen result | Manuscript/package locator | Verdict |
|---|---|---|---|---|
| unique `n=r a^i b^j`, root exclusions, and `ab\nmid n` iff on an axis | `code/verify_plaquette_matroid.py:49-60,158-169` | 10,000 coordinates = 5 multiplier pairs × 2,000 indices | `sections/2_coordinates.tex:10-29`; `CONTROL_RESULTS.md:23-29` | PASS |
| explicit axis reconstruction satisfies all in-cutoff plaquettes | code lines 171-198 | 15 instances = 5 multiplier pairs × 3 fields | `sections/2_coordinates.tex:78-119`; control lines 30-32 | PASS_WITH_FINITE_SCOPE |
| prefix constraint rank `floor(L/(ab))`, image dimension `L-floor(L/(ab))` | code lines 63-78,202-217 | 320 = 4 parameter triples × 80 cutoffs | `sections/4_prefixes.tex:6-75`; control lines 34-41 | PASS |
| arbitrary finite projection dimension equals root-wise graph rank | code lines 81-155,220-243 | 12,288 = 3 parameter triples × `2^12` subsets | `sections/3_finite_projections.tex:3-111`; control lines 38-41 | PASS_WITH_FINITE_SCOPE |
| rectangle constraint rank `(M-1)(N-1)` and dimension `M+N-1` | code lines 246-292 | 108 = 3 fields × 6 × 6 rectangles | `sections/5_rectangles.tex:11-48`; control lines 43-49 | PASS |
| one-edge deletion/addition rank-versus-cycle-rank dichotomy | code lines 295-332 | 11 = 4 cycle deletions + 3 tree deletions + 4 additions | `sections/5_rectangles.tex:70-98`; control lines 53-60 | PASS |
| finite image uniformity and fibre size `q^components` | code lines 335-375 | all 9 potential enumerations | `sections/3_finite_projections.tex:113-148`; control lines 47-49 | PASS |
| every distinct pair is independent; forest joint independence | code lines 377-398 | 3 shapes × 3 fields; PASS | `sections/3_finite_projections.tex:132-163` | PASS_WITH_FINITE_SCOPE |
| four-cycle alternating relation, including characteristic 2 | code lines 394-404 | 3 fields; PASS | `sections/3_finite_projections.tex:145-163`; control lines 49-51 | PASS |
| displayed prefix/rectangle comparison | formulas checked above | exact exponents | `sections/5_rectangles.tex:103-122`; `sections/6_scope.tex:60-76`; `sections/7_conclusion.tex:18-28` | PASS |

All output counts have exact arithmetic provenance:

- `10,000 = 5 × 2,000`;
- `15 = 5 × 3`;
- `320 = 4 × 80`;
- `12,288 = 3 × 2^12`;
- `108 = 3 × 6 × 6`;
- `11 = 4 + 3 + 4`;
- `9 = 3 × 3`.

No table cell or displayed numeric count lacks a code, proof, or direct-formula
locator. No manuscript assertion treats this finite replay as experimental evidence
or as a proof of the general theorem.

### C3. Main proof-chain audit

1. **Arithmetic components.** Coprimality gives unique exponent extraction and a
   root not divisible by either multiplier (`sections/2_coordinates.tex:10-29`).
2. **Mixed-difference integration.** The plaquette equation telescopes to
   `y_{i,j}=y_{i,0}+y_{0,j}-y_{0,0}`, and direct substitution gives the converse
   (`sections/2_coordinates.tex:42-68`).
3. **Global extension.** The free set `{n:ab\nmid n}` contains the two axes of every
   root component, the explicit inverse is coordinatewise finite, and both maps are
   product-topology continuous (`sections/2_coordinates.tex:78-119`).
4. **Finite projections.** Restriction to a finite shape becomes an edge-evaluation
   map from row/column potentials; unused potentials can be extended globally
   (`sections/3_finite_projections.tex:3-47`). Thus the result is genuinely about
   globally extendable finite patterns, not only a truncated system.
5. **Rank and cycles.** The incidence rank is vertices minus components and cycle
   sums are necessary and sufficient (`sections/3_finite_projections.tex:49-111`).
6. **Haar law.** The product homeomorphism pushes uniform product measure to Haar;
   the finite image is uniform, giving entropy `d(F) log q` and total correlation
   `beta(F) log q` (`sections/3_finite_projections.tex:113-163`).
7. **Geometric specializations.** Prefix and rectangle formulas follow from the same
   rank theorem but use distinct normalizations (`sections/4_prefixes.tex:3-103`;
   `sections/5_rectangles.tex:3-122`).

No missing implication or control-only dependency was found in this chain. This is
an audit conclusion, not a substitute for external mathematical refereeing.

## 5. Phase D — paragraph overlap and author-overlap screen

### D1. Sampling rule and coverage

A body paragraph was defined as a blank-line-delimited LaTeX narrative block after
removing comments and command-only lines, with at least 20 alphabetic tokens.
Counts were: Introduction 9, Coordinates 11, Finite projections 16, Prefixes 9,
Rectangles 10, Scope 9, Conclusion 4; total **68**. Three paragraphs per section were
selected, giving **21/68 = 30.88%**, and every major body section is represented.
Each query used an exact 8--12-word string.

`NO_EXACT_MATCH_IN_INDEXED_WEB` means that the quoted phrase did not appear in a
publicly indexed result inspected for that query. It is not an originality finding.

| # | Section and locator | Exact 8--12-word query | Search result |
|---:|---|---|---|
| 1 | `sections/1_introduction.tex:3-7` | “Multiplicative symbolic constraints come with more than one natural finite geometry” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 2 | introduction 9-19 | “we isolate one finite-field linear rule and ask for an exact answer” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 3 | introduction 125-132 | “The proof has three short layers First the multiplicative root decomposition” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 4 | `sections/2_coordinates.tex:24-29` | “Both exponents and then the root are unique” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 5 | coordinates 57-68 | “Direct substitution proves the converse The gauge formula follows immediately” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 6 | coordinates 115-119 | “The inverse is therefore continuous in the product topology” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 7 | `sections/3_finite_projections.tex:3-6` | “The product homeomorphism solves global extension but it does not” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 8 | finite projections 29-35 | “potentials on the used vertices extend to all row and column indices” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 9 | finite projections 68-72 | “It suffices to check the fundamental cycles relative to any spanning forest” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 10 | finite projections 140-148 | “Finally two distinct arithmetic coordinates produce two distinct edges” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 11 | `sections/4_prefixes.tex:3-4` | “The global free-axis coordinates immediately give the exact prefix law” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 12 | prefixes 36-44 | “the pivot computation below is not by itself an extension theorem” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 13 | prefixes 99-103 | “The sets are arithmetic intervals not a declared” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 14 | `sections/5_rectangles.tex:3-9` | “An exponent rectangle instead stays inside one component and retains” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 15 | rectangles 39-48 | “The pattern exponent has boundary rather than area order” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 16 | rectangles 91-98 | “An added edge is dependent exactly when its endpoints were already connected” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 17 | `sections/6_scope.tex:3-4` | “The finite-shape theorem sits at the intersection of several established frameworks” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 18 | scope 38-46 | “The paper-specific result is the explicit arithmetic assembly of these ingredients” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 19 | scope 81-89 | “These checks exercise composite coprime multipliers and the characteristic-two sign convention” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 20 | `sections/7_conclusion.tex:9-16` | “The arbitrary finite-shape theorem adds the missing local organization” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 21 | conclusion 18-28 | “A separate choice of action and averaging sequence is required” | NO_EXACT_MATCH_IN_INDEXED_WEB |

Representative retrieved hits were generic or unrelated rather than phrase matches,
including a [Springer linguistics article](https://link.springer.com/article/10.1007/s11049-022-09543-4),
a [graph-theory book mirror](https://dokumen.pub/topics-in-graph-theory-0367507870-9780367507879.html),
and an unrelated [mathematics study-material page](https://www.teachmint.com/tfile/studymaterial/class-9th/examplemaths/9thmaths/b6685728-5b8f-485b-880f-5dd631880d8e).
They are recorded only to show result classification, not as sources for P67.

### D2. Author-overlap status

`NOT_RUN_AUTHOR_IDENTITIES_UNAVAILABLE`

The manuscript says only “Anonymous,” so no responsible author set exists against
which to run author-publication overlap.

### D3. Tool limitation statement

This screen used general public-Web indexing, not Turnitin, iThenticate, Crossref
Similarity Check, subscription full-text databases, or a complete historical archive.
Exact-string search can miss paywalls, nonindexed works, TeX/math normalization, OCR
errors, paraphrases, translations, and vocabulary changes. Result rankings can drift.
The 30.88% sample is not exhaustive, and AI-text/plagiarism detectors have false
positive and false negative modes. Phase D therefore cannot certify originality.

## 6. Phase E — semantic claim registry and evidence decisions

The registry below normalizes semantically contiguous theorem claims instead of
treating every formula fragment as a separate claim. Every identified claim was
audited: 18/18, including all HIGH claims. The protocol floor is
`min(10,total)=10`. Again, `semantic completeness=not_machine_detectable`.

| ID | Impact | Claim and exact locator | Source/provenance checked | Verdict |
|---|---|---|---|---|
| P67-E01 | HIGH | unique arithmetic root/exponents, `sections/2_coordinates.tex:10-29` | coprimality/valuation proof; 10,000 finite regressions | VERIFIED_INTERNAL |
| P67-E02 | HIGH | mixed-difference integration and converse, coordinates 42-68 | telescoping and direct substitution | VERIFIED_INTERNAL |
| P67-E03 | HIGH | restriction `X -> F_q^{B}` is a product homeomorphism, coordinates 78-119 | explicit inverse plus coordinatewise continuity | VERIFIED_INTERNAL |
| P67-E04 | HIGH | every finite projection is exactly the potential image and has `q^{d(F)}` patterns, `sections/3_finite_projections.tex:3-47` | global extension argument and finite linear algebra | VERIFIED_INTERNAL |
| P67-E05 | HIGH | alternating cycle sums are complete compatibility conditions, finite projections 49-82 | spanning-forest integration | VERIFIED_INTERNAL |
| P67-E06 | HIGH | coordinate matroid is a direct sum of root-wise graphic matroids, finite projections 84-111 | oriented incidence representation; [Whitney](https://doi.org/10.2307/2371182) context | VERIFIED_WITH_OWNER_NOTE |
| P67-E07 | HIGH | Haar entropy and total correlation are rank and cycle-rank times `log q`, finite projections 113-148 | uniform finite quotient; [Watanabe](https://doi.org/10.1147/rd.41.0066); control | VERIFIED_WITH_MISSING_ABBE_SPIRKL_CONTEXT |
| P67-E08 | HIGH | distinct coordinates are pairwise independent but a four-cycle is dependent, finite projections 145-163 | graphic rank proof and exact enumeration | VERIFIED |
| P67-E09 | HIGH | prefix pattern count `q^{L-floor(L/(ab))}`, `sections/4_prefixes.tex:6-34` | global-axis restriction and arbitrary-shape theorem | VERIFIED_INTERNAL |
| P67-E10 | HIGH | independent pivot rows give the same prefix rank, prefixes 36-75 | explicit pivot columns | VERIFIED_INTERNAL |
| P67-E11 | NORMAL | prefix log-count rate is not automatically a dynamical entropy, prefixes 77-103 | scope/definition boundary | VERIFIED_SCOPE |
| P67-E12 | HIGH | exponent rectangle has count `q^{M+N-1}`, cycle rank `(M-1)(N-1)`, and stated Haar laws, `sections/5_rectangles.tex:11-37` | complete bipartite graph calculation | VERIFIED_INTERNAL |
| P67-E13 | NORMAL | rectangle area-normalized log rate is zero, rectangles 39-48 | exact asymptotic division | VERIFIED_INTERNAL |
| P67-E14 | HIGH | distinct roots give independent product factors, rectangles 50-68 | global product decomposition | VERIFIED_INTERNAL |
| P67-E15 | HIGH | exact edge-deletion/addition dichotomy, rectangles 70-98 | graph rank identities and 11 controls | VERIFIED |
| P67-E16 | HIGH | the theorem and counts hold over every finite field, including characteristic 2, `sections/6_scope.tex:81-95` | proofs use field-linear incidence algebra; controls in fields 2,3,5 | VERIFIED_WITH_CONTROL_BOUNDARY |
| P67-E17 | NORMAL | stated finite control counts and receipt, scope 81-89; `CONTROL_RESULTS.md:21-73` | byte-identical replay and arithmetic census | VERIFIED_CONTROL_DISCLOSURE |
| P67-E18 | HIGH | bounded search found no exact full-combination collision, scope 48-58 | alternate-term ledger through 2026-08-26 | SUPPORTED_WITHIN_SEARCH_ONLY |

No mathematical headline claim rests solely on the finite script. P67-E17 is a claim
about the control receipt itself. P67-E07, E08, E12, E15, and E16 have general proofs;
their controls are regression evidence only.

## 7. Search-bounded priority audit and owner subtraction

The full alternate-term query strings and direct results are in
[`SOURCE_SEARCH_LEDGER.md`](SOURCE_SEARCH_LEDGER.md). At least three materially
different formulations were searched for each core advance through 2026-08-26.

| Core progress | Nearest owners located | Precise owner subtraction | Collision risk |
|---|---|---|---|
| multiplicative index decomposition and shift setting | [Kenyon--Peres--Solomyak](https://arxiv.org/abs/1102.5136), [Peres--Schmeling--Seuret--Solomyak](https://arxiv.org/abs/1206.4742), [Ban--Hu--Lin](https://arxiv.org/abs/1207.7154) | multiplicative-semigroup symbolic framework, dimension and pattern-generation questions predate P67; P67's residual claim is the displayed finite-field mixed-difference integration and its exact free-axis product map | MEDIUM |
| recent affine/multidimensional multiplicative shifts | [Ban--Hu--Lai--Liao 2025](https://doi.org/10.1016/j.aim.2025.110266), [Ban--Hu--Lai--Liao axial products](https://arxiv.org/abs/2402.19324) | affine index constraints, multidimensional entropy, axial products, and surface entropy are prior territory; P67 does not own those frameworks | MEDIUM |
| graphic-matroid finite projection | [Whitney](https://doi.org/10.2307/2371182), [Király--Rosen--Theran](https://arxiv.org/abs/1312.3777) | graphic/linear matroids and graph-symmetric algebraic matroids are established; residual paper mass is the arithmetic assembly `F -> direct sum_r M(G_r(F))` plus global extendability for this rule | MEDIUM |
| entropy rank under uniform finite-field linear variables | [Watanabe](https://doi.org/10.1147/rd.41.0066), [Abbe--Spirkl](https://arxiv.org/abs/1909.12175) | total correlation and representable-matroid entropy-rank mechanisms are established; P67's specific contribution is identifying its evaluation matroid and translating its cycle rank into the stated Haar dependence law | MEDIUM |
| prefix and exponent-rectangle formulas | nearest multiplicative surface-entropy neighbors above | boundary-versus-density normalizations are related context; residual formulas are specializations of P67's finite-shape theorem, not standalone framework claims | MEDIUM |

The searches did **not** locate a public source stating the full conjunction of:

1. the exact multiplicative plaquette equation;
2. the free-axis global product homeomorphism;
3. arbitrary globally extendable finite projections represented by root-wise graphic
   matroids; and
4. the corresponding Haar forest/cycle total-correlation law.

The permissible search conclusion is exactly:

`BOUNDED_NO_EXACT_COLLISION_LOCATED_AS_OF_2026-08-26`

This is not a global novelty finding. The residual collision risk is **MEDIUM**
because the mixed-difference and incidence-rank steps are elementary and could be
implicit under algebraic-action, coding-theory, matrix-completion, matroidal entropy,
or non-English terminology. External specialist review remains necessary.

## 8. Seven-mode AI failure checklist

| Failure mode | Evidence checked | Verdict |
|---|---|---|
| 1. Implementation bug | line-level script audit, exact field arithmetic, count identities, fresh replay, two stored-output comparisons | CLEAR_WITHIN_FINITE_CONTROL_SCOPE; controls do not prove generality |
| 2. Hallucinated citation | 8/8 records searched, direct authoritative URLs, 13/13 contexts, key-set comparison | ONE_REAL_TITLE_MISMATCH; no ghost work |
| 3. Hallucinated experimental result | no empirical experiment exists; every number is a deterministic enumeration count or exact formula | NOT_APPLICABLE_NO_EMPIRICAL_EXPERIMENTS |
| 4. Shortcut reliance | product homeomorphism, finite extension, cycle completeness, rank, and Haar laws have manuscript proofs independent of code | CLEAR_WITH_DISCLOSED_CONTROL_BOUNDARY |
| 5. Bug reframed as insight | no code/formula discrepancy found; priority statement is already bounded | CLEAR_MATHEMATICALLY; source framing still incomplete |
| 6. Methodology fabrication | definitions, proof chain, exact script, frozen output, and source ledger are present; no statistical method is claimed | CLEAR_THEORETICAL_METHOD |
| 7. Frame-lock | searches used multiplicative shifts, mixed differences, graphic/algebraic matroids, matrix completion, entropy rank, coding and surface-entropy terms | PASS_WITH_NOTES; omitted owners found, medium residual risk |

## 9. Authorship, funding, COI, and AI disclosure

| Field | Current evidence | Audit status | Required action |
|---|---|---|---|
| Author identity/order/affiliations | `main.tex:39` says only “Anonymous” | UNRESOLVED | responsible researchers authorize the final list |
| Contributions / CRediT | no final statement in manuscript | UNRESOLVED | supply and approve contributor roles |
| Funding | no author-attested statement | UNRESOLVED | disclose sources/grants or explicitly approve “none” |
| Competing interests / COI | no author-attested statement | UNRESOLVED | disclose interests or explicitly approve “none” |
| AI/tool assistance | package provenance exists, but no final author-approved manuscript disclosure | UNRESOLVED | state tools, model/role/extent as required by venue and obtain human approval |
| Human/animal/personal data | none used by the mathematical manuscript | NO_PARTICIPANT_ETHICS_ISSUE_IDENTIFIED | retain accurate statement if venue requires |
| D2 author-overlap | identities unavailable | `NOT_RUN_AUTHOR_IDENTITIES_UNAVAILABLE` | rerun after author identification |
| External dissemination | internal HOLD | BLOCKED | no upload, contact, release, submission, or priority statement |

No missing declaration is inferred as “none.” Absence of supplied author information
is recorded as unresolved, not fabricated into a pass.

## 10. Objective correction list and disposition

### Required before external release

1. Correct the `KenyonPeresSolomyak2012` BibTeX title to “Hausdorff dimension for
   fractals invariant under multiplicative integers”; rebuild and verify the rendered
   reference.
2. Add and accurately engage Emmanuel Abbe and Sophie Spirkl, “Entropic Matroids and
   Their Representation,” [DOI](https://doi.org/10.3390/e21100948),
   [arXiv](https://arxiv.org/abs/1909.12175). State that the general finite-field
   representable-matroid entropy-rank mechanism is prior; retain only the arithmetic
   identification and consequences as P67-specific mass.
3. Add or explicitly justify the treatment of Ban--Hu--Lai--Liao, “Hausdorff
   dimensions of affine multiplicative shifts,”
   [DOI](https://doi.org/10.1016/j.aim.2025.110266), and
   Király--Rosen--Theran, “Algebraic matroids with graph symmetry,”
   [arXiv](https://arxiv.org/abs/1312.3777). Make the distinct index geometry and
   matroid object explicit.
4. Keep every novelty statement search-bounded; do not convert the negative search
   into worldwide novelty or priority language. Obtain specialist review spanning
   multiplicative symbolic dynamics, algebraic actions/coding, and matroidal entropy.
5. Resolve author identity/order, contributions, funding, COI, and AI/tool-use
   disclosure; then run D2 author-overlap screening.
6. After source/declaration edits, rerun citation compilation, ghost/dangling checks,
   control/output comparison, PDF QA, and this Stage 2.5 audit against the new hashes
   and search-freeze date.

### No correction identified by this audit

- No change to the core equation, global inverse, continuity argument, finite-shape
  extension, incidence-rank/cycle proof, Haar formula, prefix exponent, rectangle
  exponent, or edge-update lemma is required on the audited evidence.
- No stored control value or script branch requires correction.
- The remaining seven existing bibliography records require no field repair.

### Final disposition

P67 is mathematically coherent within this audit, but the source/ownership and
declaration record is not ready for external use. Overall status remains **FAIL** at
the Stage 2.5 release gate and **HOLD** externally until the objective corrections are
made and re-audited. No worldwide novelty or priority certificate is issued.
