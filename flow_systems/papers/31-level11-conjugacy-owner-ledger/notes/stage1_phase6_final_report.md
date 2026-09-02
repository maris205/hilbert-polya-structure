# Canonicalization Before Quadratic Audit: A Certificate-Methods Architecture for an Oriented Level-11 Owner Ledger

**Article type:** Closed-corpus certificate-methods research report; no theorem, implementation, or census result is claimed  
**Author:** Liang Wang  
**Affiliation:** School of Artificial Intelligence and Automation, Huazhong University of Science and Technology, Luoyu Road 1037, 430070, Hubei, P.R. China  
**Email:** wangliang.f@gmail.com  
**Report date:** 2026-09-02 UTC  
**Research stage:** ARS Stage 1 Phase 6, Revision 1  
**Report disposition:** `PHASE6_REVISION1_COMPLETE_WITH_ACKNOWLEDGED_LIMITATIONS`

## Declarations

**Funding:** None.  
**Competing interests:** None declared.  
**Human-subjects and animal-research status:** Not applicable. This report concerns theoretical mathematics, a frozen literature corpus, and project-local artifact definitions. It involves no participants, identifiable data, animals, recruitment, intervention, or institutional authorization claim.  
**Author contribution:** Liang Wang is the responsible human author. He specified the project object and restrictions, approved the stage gates and the Phase-6 design adjudication, and retains responsibility for the report's claims and any future use. The stage-gate confirmations do not attest that he performed full-text or source-passage verification.  
**Data and materials availability:** The report relies only on the frozen 22-row P31 source inventory and the hash-bound Stage 1 artifacts named in the Phase-6 input freeze. No new dataset, owner ledger, or scientific result was produced.  
**Execution status:** Literature synthesis and review adjudication were executed. New literature retrieval, source finalization, theorem proving, canonicalization, pair decisions, certificate generation, computation, experiment, and canonical-results refresh were not executed.

## Abstract

This report revises the research architecture for a finite ownership problem associated with a positive time change of the `Gamma_0(11)` geodesic flow. The frozen population contains 138 Hecke-output instances in 55 source-word/prime groups, with oriented primitive `Gamma_0(11)` conjugacy classes as the proposed owners. The earlier report made 9,453 terminal pair dispositions appear to be the foundational certificate. Phase-5 review identified that requirement as an unjustified architectural lock. Revision 1 instead makes a deterministic canonicalization map and its biconditional the primary target: two rooted, oriented inputs must receive the same canonical owner bytes exactly when they represent the same oriented primitive owner. The 9,453-row table is retained, but only as a derived adversarial audit of the canonical partition. Aggregate class counts remain weaker post-closure controls. The report also defines the distinct roles of a global owner table `G`, the 138-row incidence relation `I`, and the cell-local no-double-credit quotient `C`. The executed work is limited to closed-corpus evidence synthesis and review-informed method design. No canonicalization theorem, owner partition, all-pairs audit, or `G/I/C` table has been produced. All 22 inherited citations retain `anchor:none`; source identities and metadata close, but claim-to-passage faithfulness remains `INCONCLUSIVE`. The contribution is therefore a reproducible, fail-closed certificate architecture rather than a scientific ownership result. P31 remains A1-only, with no formal Route-A tuple, positive arithmetic A2 credit, Route-B invocation, or canonical manuscript change.

**Keywords:** canonical forms; modular geodesic flow; `Gamma_0(11)`; oriented conjugacy; certificate architecture; adversarial audit

## 1. Introduction, Research Question, and Contribution

Finite orbit ledgers require an equivalence rule before they can support a dynamical interpretation. A repeated row may represent the same primitive owner, a traversal power, an inverse-oriented owner, or a recurrence of one owner in another correspondence cell. P31 freezes those possibilities rather than allowing an outcome-dependent merge. Its inherited dynamical object is the positive time-changed flow `X_geo/rho_epsilon` on `T^1Y_0(11)`. The real level-11 newform differential, positivity interval, Hecke normalization, reciprocal log-zeta convention, and period coordinate `k=2y+z` remain unchanged.

The finite input is also unchanged: 138 instances are distributed over 55 source-word/prime groups. The inherited `2/2/134` split and the three 55-group diagnostic summaries are instance- or group-level controls, not owner counts. The proposed owner is an oriented primitive conjugacy class in `Gamma_0(11)` represented by a positive-trace determinant-one lift. Inversion is kept as a separate oriented owner and connected by an inverse-link field. A primitive traversal exponent is not a Hecke branch-cycle degree. Equality of trace, length, homology, or any other filter cannot by itself certify subgroup conjugacy.

The revised research question is:

**Can a deterministic, independently replayable canonicalization contract certify the complete oriented primitive-owner partition of the frozen 138-instance population, and, conditional on that closure, induce the distinct global, incidence, and cell-local estimands `G`, `I`, and `C`?**

This formulation changes the method priority without changing the object or scientific state. The primary target is a canonicalization biconditional, not 9,453 independently foundational negative certificates. The all-pairs expansion remains valuable because it can expose inconsistencies, nontransitive implementation defects, inverse-policy mistakes, and compensating merges or splits. It is nevertheless derived from the partition certificate unless a later theorem proves that bespoke pairwise evidence is necessary for a particular disposition.

The report's contribution is a certificate-methods architecture with three separated surfaces: a canonical proof object, a full-population adversarial audit, and downstream estimands. It is not positioned as a new conjugacy theorem, an implemented solver, or a novelty claim. No novelty search was authorized in Phase 6. The article type is therefore deliberately narrower than a mathematical-results paper.

## 2. Frozen Literature and Theoretical Boundary

### 2.1 Exact subgroup representations

The frozen literature first establishes that modular-subgroup structure can be represented through several exact mathematical interfaces. Millington's subgroup-classification work supplies foundational finite-index context (Millington, 1969)<!--ref:P31-S01--><!--anchor:none:-->. Kulkarni develops an arithmetic-geometric approach to modular subgroups (Kulkarni, 1991)<!--ref:P31-S02--><!--anchor:none:-->, while special-polygon constructions provide another finite-data surface (Chan et al., 1993)<!--ref:P31-S03--><!--anchor:none:-->. Congruence-recognition machinery is represented by an algorithmic treatment (Lang et al., 1995)<!--ref:P31-S04--><!--anchor:none:--> and a separate subgroup-identification route (Hsu, 1996)<!--ref:P31-S05--><!--anchor:none:-->. A later computational fundamental-domain framework supplies a potential exact Fuchsian-domain interface (Voight, 2009)<!--ref:P31-S06--><!--anchor:none:-->.

These sources support only a bounded synthesis finding: finite, replayable subgroup data are plausible ingredients. They do not bind the exact P31 representation, prove the required canonicalization biconditional, decide any frozen pair, or define owner bytes. Representation, decision, and certification remain distinct obligations.

### 2.2 Ambient and arithmetic conjugacy components

The second source group gives candidate components for matrix and arithmetic conjugacy. The ideal-class/matrix correspondence supplies ambient integral structure (Latimer & MacDuffee, 1933)<!--ref:P31-S07--><!--anchor:none:-->, and a later refinement develops that correspondence further (Taussky, 1949)<!--ref:P31-S08--><!--anchor:none:-->. Hyperbolic integral matrices and ideal classes provide another ambient relation (Wallace, 1984)<!--ref:P31-S09--><!--anchor:none:-->. Continued fractions supply a route for the ambient `SL_2(Z)` conjugacy problem (Appelgate & Onishi, 1981)<!--ref:P31-S10--><!--anchor:none:-->. Arithmetic-group conjugacy and general arithmetic-group algorithms enlarge the possible decision toolkit (Grunewald, 1980)<!--ref:P31-S11--><!--anchor:none:--> (Grunewald & Segal, 1980)<!--ref:P31-S12--><!--anchor:none:-->. Modern `GL(n,Z)` work supplies a further ambient algorithmic surface (Eick et al., 2019)<!--ref:P31-S13--><!--anchor:none:-->.

No source in this group may be promoted into the required oriented `Gamma_0(11)` solver. A valid specialization would still have to preserve determinant one, positive-trace lifting, the congruence condition, orientation, primitive roots, inverse linkage, termination, and independently replayable evidence. Failure of a bounded ambient search would not constitute a negative subgroup-conjugacy certificate.

### 2.3 Canonical reduction, roots, inversion, and replay

Canonicalization requires more than an ambient yes/no decision. Modular-geodesic reduction provides relevant coding context (Series, 1985)<!--ref:P31-S15--><!--anchor:none:-->. Word-hyperbolic conjugacy algorithms supply individual and batch decision precedents (Epstein & Holt, 2006)<!--ref:P31-S16--><!--anchor:none:--> (Buckley & Holt, 2013)<!--ref:P31-S17--><!--anchor:none:-->. Centralizers and reversing symmetries clarify why ordinary symmetry and inversion must be typed separately (Baake & Roberts, 2001)<!--ref:P31-S18--><!--anchor:none:-->. Pell equations and unit methods provide potential arithmetic subroutines (Lenstra, 2002)<!--ref:P31-S19--><!--anchor:none:-->, while computational algebraic number theory supplies broader implementation background (Cohen, 1993)<!--ref:P31-S20--><!--anchor:none:-->.

The synthesis does not choose among polygon, arithmetic, or hyperbolic-group implementations. It instead specifies the acceptance condition that any route must meet. A route is admissible only if its hypotheses are proved for the frozen marked object, its output is canonical under the orientation policy, its primitive-root and inverse fields are exact, and an independent verifier can replay success and failure evidence. The literature does not supply the project serialization or prove that this combined contract terminates.

### 2.4 Aggregate counts as post-closure controls

Class-number structure supplies useful aggregate context (Sarnak, 1982)<!--ref:P31-S14--><!--anchor:none:-->. A direct formula for primitive hyperbolic class counts in `Gamma_0(N)` is the closest frozen census precedent (Golovchanskii & Smotrov, 2008)<!--ref:P31-S21--><!--anchor:none:-->, and modular conjugacy has also been related to real-quadratic class numbers (Traina, 1985)<!--ref:P31-S22--><!--anchor:none:-->.

The information content of an aggregate count is lower than that of a labeled partition. Compensating false merges and false splits can preserve a total. Class counts can therefore test a closed owner table for consistency, but they cannot choose canonical representatives, certify an individual owner identity, or establish that every input has been resolved.

## 3. Executed Methodology

### 3.1 Closed-corpus literature synthesis

The only executed research method in this phase is literature synthesis over frozen artifacts. The upstream corpus process captured 44 records, removed nine duplicate manifestations, screened 35 unique records, excluded 13, and retained 22 sources. The inclusion frame covered modular-subgroup descriptions, integral and subgroup conjugacy, reduction and centralizers, primitive roots, and direct class-count precedents. Nineteen inventory rows are classified as peer-reviewed. The authorized metadata correction fixed the P31-S16 page range to 287–305.

The source-verification layer closed identity and metadata for 22 of 22 rows within its recorded scope. That layer mainly used DOI, publisher, journal, institutional, metadata, abstract, and limited authoritative-record surfaces. It did not inspect every theorem passage, produce claim-level page or section locators, or perform a general current retraction or source-conflict screen. The evidence matrix then assigned each source an admitted contribution, an excluded stronger claim, and an applicability warning. Phase 3 grouped the sources into representation, conjugacy, canonicalization, and census themes without converting proximity into theorem transfer.

### 3.2 Review-adjudicated revision procedure

Phase 5 supplied four procedurally separated, single-model-family review records: editorial, ethics, citation-integrity, and Devil's Advocate. Their integrated decision was `MAJOR_REVISION`, with no Critical finding and no ethics `BLOCKED` result. Revision 1 applies the author-adjudicated branch recorded in the Phase-6 contract. It changes report design only: canonicalization becomes primary, the all-pairs ledger becomes a derived audit, `G/I/C` receive self-contained conditional definitions, and the AI disclosure is narrowed to the actual verification surface.

No new retrieval occurred during Revision 1. No source field, reference, passage locator, direct quotation, experiment, code result, proof result, or canonical manuscript byte was introduced. The Phase-6 ClaimIntent manifest was frozen before this prose and supplies the complete set of eight substantive report claims. Every finding below is either a closed-corpus evidence-synthesis statement, a project definition, or a prospective method obligation.

## 4. Review-Adjudicated Certificate Architecture

### 4.1 Primary target: a canonicalization biconditional

Let `X` denote the frozen set of 138 instances after exact input validation. The future method should define a partial operation `root(x)` that either returns an oriented primitive `Gamma_0(11)` representative together with a traversal exponent and proof payload, or returns a typed not-evaluable state. It should then define a deterministic byte map

```text
kappa: X -> OwnerBytes
```

on every successfully resolved input. The primary theorem target is the biconditional

```text
kappa(x)=kappa(y)
if and only if
root(x) and root(y) represent the same oriented primitive Gamma_0(11) owner.
```

This is a target, not a proved statement. Its forward direction must prevent accidental byte collisions. Its reverse direction must show that all representatives of one oriented owner reduce to identical bytes. Both directions must be established in the exact subgroup and presentation used by P31. The map must not identify an owner with its inverse; instead, an `inverse_owner_bytes` field should connect the two oriented objects when that relation is defined.

The biconditional identifies the mathematical certificate invariant: a total, sound, complete, deterministic owner map. If such a theorem and its per-instance witnesses are independently replayable, the partition follows from byte equality. A separate bespoke negative proof for every unequal pair is then not logically foundational merely because the population is finite.

### 4.2 Prospective certificate and verifier contract

Each future per-instance certificate should bind at least: the immutable input identifier and hash; the subgroup representation and theorem version; exact membership evidence; the normalized matrix or word; the maximal primitive root and traversal exponent; the orientation convention; canonical owner bytes; inverse linkage; and the complete proof or reduction trace needed by a read-only verifier. A failure certificate should identify the exact failed precondition or unresolved theorem obligation rather than silently convert a timeout into nonconjugacy.

The verifier acceptance predicates are also prospective. It should recheck input binding, determinant and subgroup membership, root powering, primitiveness under the chosen theorem, orientation preservation, deterministic serialization, and any inverse relation. It should reject unknown fields, stale theorem versions, noncanonical encodings, missing proof data, or an unresolved subroutine. Independent replay means an implementation separate from the producer can evaluate the frozen mathematical predicates; it does not mean that two AI reviews have statistically independent errors.

No such schema, theorem binding, fixture set, producer, or verifier was implemented in Phase 6. The specification above partially addresses reproducibility at the report level while leaving scientific and implementation closure explicitly open.

### 4.3 The 9,453-row table as a derived adversarial audit

For `|X|=138`, the unordered-pair expansion has `binom(138,2)=9,453` rows. Once `kappa` is total, each row can carry the two input IDs, their owner bytes, the derived equality disposition, inverse relationship, and any optional direct-solver cross-check. The expected same-owner relation is equality of canonical bytes; inequality supplies the derived different-owner relation under the proved biconditional.

This table remains useful. It can test symmetry, transitivity consequences, deterministic sorting, collision handling, inverse-policy consistency, and agreement between canonical and direct routes. Adversarial fixtures can target pairs that share trace, length, homology, or other coarse invariants while differing in exact ownership. Aggregate-count controls can then operate on the completed partition without replacing any row-level audit.

The table is not described as a uniquely necessary proof architecture. If a future scientific requirement needs a separately replayable negative obstruction for particular cross-class pairs, that need must be justified and bound. Until then, the full table is a regression expansion of the canonical certificate rather than 9,453 independent foundations.

### 4.4 Distinct `G`, `I`, and `C` estimands

The downstream objects can be defined conditionally once `kappa` is total and the biconditional is proved. Define the global owner table

```text
G = {kappa(x): x in X},
```

with exactly one row per distinct oriented owner byte string. Define the incidence relation `I` with one row for every input instance, carrying its input fields, cell coordinates, owner bytes, traversal exponent, inverse link, and all frozen Hecke coordinates. Thus `|I|=138` even when `|G|<138`.

Let a cell key be the frozen tuple `(source_word, prime, hecke_degree)`. Define `C` as the set of distinct `(cell_key, owner_bytes)` pairs induced by `I`. Raw multiplicity remains visible in `I`, while `C` awards one unit to an owner within a cell. The same owner may appear once in each of several cells without being duplicated in `G`.

Conditional well-definedness is straightforward but important. If `kappa` is total and satisfies the biconditional, changing an input representative within the same oriented owner cannot change its `G` row or its cell-level owner key. Deduplication inside a cell is therefore invariant under representative choice. Conversely, two different canonical owner bytes cannot be merged in `C` without violating the definition. This set-theoretic argument does not prove that `kappa` exists or that the frozen inputs are resolved; it states what follows if the primary certificate closes.

## 5. Evidence-Synthesis Findings

Eight precommitted positions control this report. First, the frozen corpus supplies complementary subgroup, ambient-conjugacy, arithmetic, reduction, and hyperbolic-group components, but no executed complete oriented `Gamma_0(11)` owner solver. Second, the primary certificate target is the deterministic canonicalization biconditional. Third, the 9,453-row table is a derived adversarial audit, and aggregate counts remain post-closure controls. Fourth, `G`, `I`, and `C` are distinct estimands populated only after owner closure.

Fifth, a complete prospective certificate preserves subgroup membership, orientation, primitive-root status, inverse linkage, traversal exponent, deterministic serialization, and replayable failure evidence while keeping Hecke degree separate. Sixth, the report's methodological contribution is the separation of canonical proof object, audit expansion, and estimands. Seventh, metadata and source-identity closure do not clear theorem passages, retraction status, source conflicts, or the theorem-to-certificate bridge. Eighth, Revision 1 remains A1-only and changes no scientific result or Route state.

These are evidence-synthesis and design findings. They do not imply feasibility, novelty, theorem correctness, or implementation readiness. The central scientific state remains `NOT_EXECUTED`.

## 6. Reproducibility and Prospective Interface

Reproducibility in the present report means that another reader can recover the frozen corpus, Phase-4 report, Phase-5 reviews, Phase-6 manifest, and revision log from named hash-bound artifacts. The literature selection and source ledger are inspectable, and the citation/reference/source-ID sets close. Generative prose is not promised to be byte-reproducible, and source-passage judgments cannot be replayed because the locators were never finalized.

A later scientific package should freeze four layers before reading owner outcomes. Layer one binds the exact `Gamma_0(11)` representation and proves every input conversion. Layer two binds the canonicalization and root theorem, including both directions of the biconditional. Layer three freezes producer and verifier schemas, adversarial fixtures, and typed failure states. Layer four defines the derived all-pairs audit and the conditional `G/I/C` materialization. Hashes, theorem versions, serialization versions, and fixture manifests should be immutable across execution.

The smallest valid next test is not the census. It is a theorem-to-certificate dossier evaluated against deliberately small, target-blind fixtures. Scientific population execution requires separate authorization after the primary biconditional, root policy, inverse policy, and independent verifier have closed. A missing theorem or unresolved fixture should terminate as `NOT_EVALUABLE_CONJUGACY_INCOMPLETE`, not as a negative owner result.

## 7. Discussion and Implications

The revised architecture improves the match between the mathematical object and its evidence. A partition is naturally represented by a total equivalence invariant. Expanding that invariant to every pair can be an excellent audit, but expansion size should not be confused with proof content. This distinction reduces a false quadratic necessity while preserving the most demanding adversarial check available for the fixed population.

The change does not make P31 easy. The canonicalization theorem must simultaneously handle exact subgroup membership, oriented conjugacy, primitive roots, inverse linkage, and deterministic bytes. A compact certificate that lacks either direction of the biconditional would be weaker than the all-pairs design it replaces. The revision therefore narrows the foundational object without lowering the exactness standard.

The `G/I/C` separation also clarifies what a future result would mean. `G` answers how many global oriented primitive owners occur. `I` records how the 138 frozen instances map to those owners. `C` answers how owner identity contributes within each frozen correspondence cell. None of the inherited instance summaries can substitute for these estimands, and no cell-local recurrence can multiply the number of global owners.

For Route A, this remains primitive-owner infrastructure at A1. No primitive Euler product, dynamical determinant, zero comparison, analytic continuation, or arithmetic specificity test is produced. Editorial improvement cannot promote a Route coordinate. Route B remains closed because there is no Route-A readiness, Hilbert space, operator, domain, self-adjointness result, trace formula, or divisor identity.

## 8. Acknowledged Limitations

The dominant limitation is citation resolution. All 22 prose citation pairs retain `anchor:none`. The source ledger supports identity, metadata, and bounded claim-fitness accounting, but the exact passages and theorem hypotheses were not frozen. Claim-to-passage faithfulness is therefore `INCONCLUSIVE`. Revision 1 narrows language rather than inventing locators.

The corpus has no general current retraction or source-conflict clearance. Those fields remain `NOT_CHECKED` and `UNKNOWN_NOT_CHECKED`. The P31-S16 page correction is preserved, but one corrected field does not constitute a clean integrity screen. The corpus is historically weighted and no new contribution or novelty comparison was authorized.

The method architecture is uninstantiated. There is no bound canonicalization theorem, no producer or independent verifier, no completed fixture suite, no owner decision, and no `G/I/C` output. The conditional definitions show how outputs would relate after closure; they do not close the primary mathematical obligation.

Finally, AI-assisted review and drafting used one Codex model family with procedural role separation. This supplies multiple documented perspectives, not statistically independent validation. Liang Wang's gate confirmations establish author decisions and workflow authority only; they are not evidence of personal full-text checking.

## 9. Future Work

Future work should proceed in this order:

1. perform a separately authorized source-finalization pass that freezes exact theorem passages, hypotheses, correction status, and any required source-conflict or retraction checks;
2. bind one exact subgroup representation and prove the conversion from every frozen input;
3. state and prove the canonicalization biconditional, maximal-root contract, orientation convention, and inverse-link rule;
4. freeze certificate schemas, producer/verifier roles, typed failures, and target-blind adversarial fixtures;
5. execute the 138 per-instance certifications only after the interface recheck passes;
6. derive the 9,453-row audit and compare it with optional direct pair checks without treating aggregate counts as pair evidence; and
7. materialize and independently validate `G`, `I`, and `C` only after zero unresolved owner inputs.

Each step requires a new gate when it extends beyond literature-only report revision. Nothing in this report authorizes retrieval or scientific execution.

## 10. Conclusion

P31 now has a more defensible certificate architecture. The foundational target is a total deterministic canonical owner map with a proved biconditional for oriented primitive `Gamma_0(11)` ownership. The 9,453-row table remains a full-population adversarial audit derived from that certificate, not a presumed uniquely necessary collection of bespoke proofs. Aggregate class counts remain weaker controls, and the global owner table `G`, incidence relation `I`, and cell-local quotient `C` remain distinct conditional outputs.

This is concrete report-level progress, but it is not a scientific result. No canonical form, owner partition, pair audit, theorem, computation, or estimand table has been executed. The source corpus remains passage-unresolved, originality remains unassessed, the formal Route-A tuple remains `UNASSIGNED`, positive arithmetic A2 remains absent, and Route B remains closed.

## AI Disclosure and Verification Limitation

OpenAI Codex, using the GPT-5 model family, assisted during the session dated 2026-09-02 UTC; the exact backend snapshot/build was not exposed. AI-assisted work in the recorded pipeline included literature-search support, source-identity and metadata checking, evidence-matrix construction, evidence synthesis, report drafting, four role-based Phase-5 reviews, review synthesis, ClaimIntent-constrained Revision-1 drafting, citation-ID/reference closure checks, and revision-log accounting. No AI system executed a P31 solver, proof, pair decision, owner census, experiment, or canonical-results refresh.

Liang Wang is the responsible human author. He approved the project restrictions, stage gates, and the Phase-6 author-adjudicated design choice. Those approvals must not be interpreted as a statement that he personally read every source in full or verified any claim at the exact source-passage level. The recorded verification was bounded mainly to source identity, metadata, abstracts, authoritative landing pages, and project-local claim-fitness records. All 22 citations lack passage locators, so claim-to-passage faithfulness remains `INCONCLUSIVE`; the report does not claim theorem-level source verification, novelty clearance, or a clean retraction/conflict screen.

## References

- [P31-S10] Appelgate, H., & Onishi, H. (1981). Continued fractions and the conjugacy problem in `SL_2(Z)`. *Communications in Algebra, 9*(11), 1121–1130. https://doi.org/10.1080/00927878108822637
- [P31-S18] Baake, M., & Roberts, J. A. G. (2001). Symmetries and reversing symmetries of toral automorphisms. *Nonlinearity, 14*(4), R1–R24. https://doi.org/10.1088/0951-7715/14/4/201
- [P31-S17] Buckley, D. J., & Holt, D. F. (2013). The conjugacy problem in hyperbolic groups for finite lists of group elements. *International Journal of Algebra and Computation, 23*(5), 1127–1150. https://doi.org/10.1142/S0218196713500203
- [P31-S03] Chan, S.-P., Lang, M.-L., Lim, C.-H., & Tan, S.-P. (1993). Special polygons for subgroups of the modular group and applications. *International Journal of Mathematics, 4*(1), 11–34. https://doi.org/10.1142/S0129167X93000030
- [P31-S20] Cohen, H. (1993). *A course in computational algebraic number theory*. Springer. https://doi.org/10.1007/978-3-662-02945-9
- [P31-S13] Eick, B., Hofmann, T., & O'Brien, E. A. (2019). The conjugacy problem in `GL(n,Z)`. *Journal of the London Mathematical Society, 100*(3), 731–756. https://doi.org/10.1112/jlms.12246
- [P31-S16] Epstein, D. B. A., & Holt, D. F. (2006). The linearity of the conjugacy problem in word-hyperbolic groups. *International Journal of Algebra and Computation, 16*(2), 287–305. https://doi.org/10.1142/S0218196706002986
- [P31-S21] Golovchanskii, V. V., & Smotrov, M. N. (2008). An explicit formula for the number of classes of primitive hyperbolic elements in the group `Gamma_0(N)`. *Sbornik: Mathematics, 199*(7), 1009–1031. https://www.mathnet.ru/eng/sm3853
- [P31-S11] Grunewald, F. J. (1980). Solution of the conjugacy problem in certain arithmetic groups. In *Word Problems II* (pp. 101–139). Elsevier. https://doi.org/10.1016/S0049-237X(08)71335-1
- [P31-S12] Grunewald, F., & Segal, D. (1980). Some general algorithms. I: Arithmetic groups. *Annals of Mathematics, 112*(3), 531–583. https://doi.org/10.2307/1971091
- [P31-S05] Hsu, T. (1996). Identifying congruence subgroups of the modular group. *Proceedings of the American Mathematical Society, 124*(5), 1351–1359. https://doi.org/10.1090/S0002-9939-96-03496-X
- [P31-S02] Kulkarni, R. S. (1991). An arithmetic-geometric method in the study of the subgroups of the modular group. *American Journal of Mathematics, 113*(6), 1053–1133. https://doi.org/10.2307/2374900
- [P31-S04] Lang, M.-L., Lim, C.-H., & Tan, S.-P. (1995). An algorithm for determining if a subgroup of the modular group is congruence. *Journal of the London Mathematical Society, 51*(3), 491–502. https://doi.org/10.1112/jlms/51.3.491
- [P31-S07] Latimer, C. G., & MacDuffee, C. C. (1933). A correspondence between classes of ideals and classes of matrices. *Annals of Mathematics, 34*(2), 313–316. https://doi.org/10.2307/1968204
- [P31-S19] Lenstra, H. W., Jr. (2002). Solving the Pell equation. *Notices of the American Mathematical Society, 49*(2), 182–192. https://www.ams.org/notices/200202/fea-lenstra.pdf
- [P31-S01] Millington, M. H. (1969). Subgroups of the classical modular group. *Journal of the London Mathematical Society, s2-1*(1), 351–357. https://doi.org/10.1112/jlms/s2-1.1.351
- [P31-S14] Sarnak, P. (1982). Class numbers of indefinite binary quadratic forms. *Journal of Number Theory, 15*(2), 229–247. https://doi.org/10.1016/0022-314X(82)90028-2
- [P31-S15] Series, C. (1985). The modular surface and continued fractions. *Journal of the London Mathematical Society, s2-31*(1), 69–80. https://doi.org/10.1112/jlms/s2-31.1.69
- [P31-S08] Taussky, O. (1949). On a theorem of Latimer and MacDuffee. *Canadian Journal of Mathematics, 1*(3), 300–302. https://doi.org/10.4153/CJM-1949-026-1
- [P31-S22] Traina, C. (1985). The conjugacy problem of the modular group and the class number of real quadratic number fields. *Journal of Number Theory, 21*(2), 176–184. https://doi.org/10.1016/0022-314X(85)90049-6
- [P31-S06] Voight, J. (2009). Computing fundamental domains for Fuchsian groups. *Journal de Théorie des Nombres de Bordeaux, 21*(2), 467–489. https://doi.org/10.5802/jtnb.683
- [P31-S09] Wallace, D. I. (1984). Conjugacy classes of hyperbolic matrices in `SL(n,Z)` and ideal classes in an order. *Transactions of the American Mathematical Society, 283*(1), 177–184. https://doi.org/10.1090/S0002-9947-1984-0735415-0

## Report Metadata and Route Boundary

```text
REPORT_ID=P31-STAGE1-PHASE6-REVISION1-20260902
ARTICLE_TYPE=CLOSED_CORPUS_CERTIFICATE_METHODS_RESEARCH_REPORT
PHASE6_MANIFEST_ID=M-2026-09-02T11:37:06Z-31p6
PHASE6_MANIFEST_SHA256=b9a61badd7e6d05c31ae0ce4f81adfa6ea1c40269afe37de9a620c763597aa38
PHASE4_REPORT_SHA256=9465546ed487c96db45301de68c3640b673f7d604fc6262f39fa6029f5ae0213
SOURCE_CORPUS=FROZEN_22_ROWS
SOURCE_IDS_CITED=22/22
CITATION_PAIRS=22
CITATION_ANCHORS=22_NONE_0_NON_NONE
CLAIM_TO_PASSAGE=INCONCLUSIVE
FINDINGS_TYPE=EVIDENCE_SYNTHESIS_AND_PROSPECTIVE_METHOD_ARCHITECTURE_ONLY
CANONICALIZATION_BICONDITIONAL=PRIMARY_TARGET_NOT_PROVED
OWNER_POPULATION=138_INSTANCES_55_GROUPS_9453_DERIVED_AUDIT_ROWS
OWNER_LEDGER=NOT_EXECUTED
G_I_C_TABLES=NOT_CONSTRUCTED
NEW_RETRIEVAL=NOT_RUN
SCIENTIFIC_COMPUTATION=NOT_RUN
NOVELTY_ASSESSMENT=NOT_RUN
FORMAL_PROJECT_CLAIM_REGISTRATION=0/1
P31_ROUTE_SCOPE=A1_ONLY
FORMAL_ROUTE_A_TUPLE=UNASSIGNED
POSITIVE_ARITHMETIC_A2=0/1
ROUTE_B_INVOCATION=false
CANONICAL_MANUSCRIPT_MODIFIED=false
CANONICAL_BIBLIOGRAPHY_MODIFIED=false
```
