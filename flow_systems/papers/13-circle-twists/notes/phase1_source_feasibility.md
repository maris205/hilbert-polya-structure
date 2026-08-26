# Paper 13 Phase-1 source and terminology feasibility review

Status: **MAJOR AMENDMENT**  
Review lane: independent source/terminology feasibility  
Review date: 2026-08-15  
Phase authorized: Phase 1 review only

## 1. Exact review receipt and scope

The reviewed bytes independently match the active tuple:

| Active lock | SHA-256 | Receipt |
|---|---|---|
| `research_protocol.md` | `99a6552621ebc38f0288255d34fc3bdca6dd4e8fe2fd8c5db4ec4d7594d7769e` | MATCH |
| `candidate_lock.md` | `3dd4f8ece7469edc0f5e55447b94e632281b66cb95792a7a10cbe370bc74c6f0` | MATCH |
| `pipeline_state.md` | `f4ed05d837414549d8cfecb4d2d05668fcea4cc2b148dbff5d5fe1dce73c2ad8` | MATCH |

Only those three Paper-13 locks were substantively reviewed. No sibling Paper-13 Phase-1 review was read. No prior-paper manuscript was reopened, no proof was attempted, and no source PDF was downloaded or retained.

## 2. Verdict

**Verdict: M — major amendment (`C=0`, `M=4`, `m=1`).**

Bounded primary-source discovery is feasible for all requested standard ingredients: normalized continuous circle multipliers on the time group, the real-line gauge collapse, twisted convolution and involution, the projective left regular representation, full/reduced twisted group completions, and amenability. I found no primary-source contradiction to the candidate mathematical direction.

The present bytes nevertheless do not pass the Phase-1 exact-byte gate. They include the Hausdorff singleton in an owner repeatedly described as non-Hausdorff, leave several sign/direction choices unstated, claim framework nonapplicability more broadly than the audited hypotheses permit, and do not yet contain a credible standalone novelty discriminator in light of an exact 1978 real-line precedent. Phase 2 is source-feasible only after the amendments in section 6 are locked.

## 3. Primary-source feasibility and ownership ceiling

| Topic | Primary/official source found | Feasibility assessment | Exact ownership ceiling |
|---|---|---|---|
| Normalized continuous group 2-cocycle and projective multiplier | Are Austad, “Spectral Invariance of \(*\)-Representations of Twisted Convolution Algebras with Applications in Gabor Analysis,” *J. Fourier Anal. Appl.* 27 (2021), article 56, [doi:10.1007/s00041-021-09860-z](https://doi.org/10.1007/s00041-021-09860-z), Definition 2.2 and (2.1)–(2.2) | **YES** | Locally compact group \(G\), hence the time group \(\mathbb R\); not the actual action groupoid. |
| Exact continuous collapse on the real line | Rafael Sorkin, “The triviality of continuous multipliers for the real line,” *Int. J. Theor. Phys.* 17 (1978), 369–376, [doi:10.1007/BF00674107](https://doi.org/10.1007/BF00674107) | **YES, with Phase-2 full-text check required** | The official abstract says every continuous group multiplier on \(\mathbb R\) is reduced to the identity by a continuous remultiplication. Phase 1 did not have full-text access, so normalization, quotient orientation, and the exact remultiplication formula remain to be translated against the frozen convention. It cannot own P13-1, P13-2, or the fixed-prime application. |
| Twisted convolution, involution, and projective left regular representation | Austad (2021), Definition 2.1, (2.3), and the formulas following Lemma 2.3 | **YES; exact formula match available** | Applies to \(L^1(\mathbb R,\sigma)\) (and therefore its \(C_c(\mathbb R)\) subalgebra) with a fixed left Haar measure and modular function. It does not define a groupoid algebra on the actual owner. |
| Full/reduced twisted norm equality for an amenable group | Austad (2021), Proposition 2.4; its original-source pointer is Horst Leptin, “Darstellungen verallgemeinerter \(L^1\)-Algebren,” *Invent. Math.* 5 (1968), 192–215, [EuDML record](https://eudml.org/doc/141915) | **YES** | The theorem is about a locally compact group and its twisted group algebra. It supports the time-group record only. Phase 2 should inspect Leptin’s cited Satz 6 rather than stop at the modern restatement. |
| Amenability/Følner criterion for \(\mathbb R\) | Andrzej Hulanicki, “Means and Følner condition on locally compact groups,” *Studia Math.* 27 (1966), 87–104, [doi:10.4064/sm-27-2-87-104](https://doi.org/10.4064/sm-27-2-87-104) | **YES** | Locally compact groups. A direct interval Følner check may specialize it to \(\mathbb R\); it supplies no amenability statement for the actual groupoid. |
| Standard Hausdorff étale groupoid cocycle/\(C^*\)-package | Are Austad and Eduard Ortega, “\(C^*\)-uniqueness Results for Groupoids,” *IMRN* 2022(4), 3057–3073, [doi:10.1093/imrn/rnaa225](https://doi.org/10.1093/imrn/rnaa225), Section 2 | **YES as a hypothesis boundary; NO on the actual owner** | Its twisted convolution and completion require a second-countable locally compact **Hausdorff étale** groupoid. The registered actual groupoid is not étale, and for a genuinely indiscrete carrier it is not Hausdorff. |
| A major non-Hausdorff groupoid \(C^*\)-framework | Jean-Louis Tu, “Non-Hausdorff groupoids, proper actions and K-theory,” *Doc. Math.* 9 (2004), 565–597, [doi:10.4171/DM/178](https://doi.org/10.4171/DM/178), Definitions 1.1, 2.1, and 4.6 | **NO on a genuinely indiscrete actual owner; useful exclusion source** | Tu’s “locally compact” spaces have compact Hausdorff neighborhoods and hence are locally Hausdorff; the main \(C^*\)-constructions additionally impose a Hausdorff unit space. For \(|X|>1\), neither \(X_{\mathrm{indisc}}\) nor \(X_{\mathrm{indisc}}\times\mathbb R\) is locally Hausdorff, and the unit space is not Hausdorff. Tu therefore does not license the proposed actual-owner completion. |

Historical primary sources are also available for Phase 2: Busby–Smith, “Representations of twisted group algebras,” *Trans. AMS* 149 (1970), 503–537, [doi:10.1090/S0002-9947-1970-0264418-8](https://doi.org/10.1090/S0002-9947-1970-0264418-8), and Packer–Raeburn, “Twisted crossed products of \(C^*\)-algebras,” *Math. Proc. Camb. Phil. Soc.* 106 (1989), 293–311, [doi:10.1017/S0305004100078129](https://doi.org/10.1017/S0305004100078129). They are corroborating candidates, not permission to move a group theorem onto the actual groupoid.

Adam Kleppner’s “Multipliers on Abelian Groups,” *Math. Ann.* 158 (1965), 11–34, [official repository record](https://eudml.org/doc/161251), is a particularly important **domain warning**: its Section 7 defines multipliers and similarity using Borel functions. It is valuable background for commutator bicharacters, but it cannot by itself support the candidate’s required *continuous* normalized trivializer.

No correction or retraction flag was visible in the official metadata pages checked on 2026-08-15. That metadata observation is not a substitute for the Phase-2 full-text/Crossmark integrity check.

## 4. Findings

### M1 — The generic owner does not yet make its non-Hausdorff case exact

**Locator:** research protocol sections 2.1 and 5; candidate lock “Hard domain locks” 1–2 and 6.  
**Finding:** the generic owner allows every nonempty \(X\). If \(X\) is a singleton, its indiscrete topology is Hausdorff and \(X\times\mathbb R\) is just the ordinary one-object time groupoid. Blanket statements that “the actual owner” is non-Hausdorff or outside standard frameworks are therefore false on an admitted case. For \(|X|>1\), the relevant failure is stronger and more informative than “non-Hausdorff”: the unit and arrow spaces have no nonempty Hausdorff neighborhood, and the range map is not a local homeomorphism.  
**Why major:** the framework ceiling, terminology, and claimed distinction between actual and standard owners all depend on this quantifier.  
**Required correction:** separate the genuinely non-Hausdorff generic owner \(|X|\ge 2\) from the singleton Hausdorff control, and bind a premise/locator establishing at least two units before calling the fixed-prime owner non-Hausdorff.

### M2 — Gauge direction and the regular/completion package are not fully typed

**Locator:** research protocol sections 3–5; candidate lock “Mandatory Phase-1 review questions.”  
**Finding:** “their quotient is \(\delta a\)” does not identify which quotient. The protocol specifies only the \(\sigma\)-to-trivial gauge map, not the general \(\sigma\)-to-\(\tau\) direction. It also requires an “exact unit-regular representation” without giving a formula; “unit-regular” is not the standard term for the group construction. Left Haar measure, modular convention, integrated representation, and the separation between standard group twisted \(C^*\)-algebras and author time-transported actual-owner records are not frozen.  
**Why major:** these choices control every product, star, representation, and transported norm identity. Nearby sources use several conjugate/right-versus-left conventions.  
**Required correction:** freeze the exact formulas in A2–A4 below and use “\(\sigma\)-projective left regular representation of \(\mathbb R\).”

### M3 — The retention target is broader than a provable named record

**Locator:** research protocol section 6 and P13-6.  
**Finding:** “its gauge-class or completed isomorphism invariant” quantifies over an undefined universe of invariants, while restrictions to different stabilizer subgroups land in different cohomology sets and are not automatically comparable. The dense-stabilizer control may use a nonclosed dense subgroup such as \(\mathbb Q\subset\mathbb R\), which is not locally compact in its subspace topology; locally compact group \(C^*\)-theorems cannot be applied to that restriction.  
**Why major:** P13-6 is a central generic claim, and its present retention predicate has no fixed codomain or finite proof obligation.  
**Required correction:** restrict retention to the three named records in A6 and state that dense nonclosed stabilizers are cohomological controls only, with no Haar, regular-representation, or \(C^*\)-completion claim.

### M4 — The standalone novelty case is presently high risk

**Locator:** research protocol sections 7, 10, and 12; candidate center.  
**Finding:** Sorkin (1978) is an exact-title primary precedent for continuous multiplier triviality on the real line. Austad (2021), with the older Busby–Smith/Leptin/Packer–Raeburn line, supplies the standard twisted convolution, star, regular-representation, and amenability package. P13-1/P13-2 are an elementary factorization caused by the indiscrete-to-\(T_0\) target boundary, and P13-6/P13-7 are currently framed as negative consequences of those ingredients.  
**Why major:** the protocol’s own standalone gate says a formal composition with a standard \(H^2(\mathbb R;\mathbb T)=0\) fact is `NOTE_OR_MERGE`; the source landscape makes that risk actual rather than hypothetical.  
**Required correction:** add the precommitted novelty discriminator in A8. A new proof of Sorkin’s conclusion, the standard gauge-star identities, a larger control table, or a fixed-prime substitution alone cannot satisfy it.

### m1 — “Multiplier” and source tiers need an explicit terminology warning

**Locator:** throughout sections 3, 7, and 10.  
**Finding:** “multiplier” is also standard terminology for Fourier multipliers, while classic projective-multiplier sources often use Borel rather than continuous cochains.  
**Required correction:** at first use write “normalized continuous \(\mathbb T\)-valued group 2-cocycle (projective multiplier)” and tag every Phase-2 source row `CONTINUOUS/CONTINUOUS`, `BOREL/BOREL`, or `MIXED`; only the first tier may own P13-3’s continuous gauge conclusion.

## 5. Bounded novelty sentinel

This was a feasibility sentinel, not execution of P13-9. On 2026-08-15 I searched publisher/Crossref/arXiv-indexed web results for the exact conjunctions and close variants:

- `"globally indiscrete" groupoid "circle" multiplier`
- `"indiscrete" "twisted groupoid" C*-algebra`
- `"marked period" groupoid continuous multiplier`
- `"rational Witt" groupoid twist multiplier`
- `"indiscrete topology" action groupoid cocycle cohomology`
- `"gauge collapse" multiplier groupoid`

No same-owner, same-topology, same-twist, same-marked-period primary package was returned. The nearest decisive precedent is nevertheless Sorkin’s exact continuous real-line collapse, followed by the standard twisted-group-algebra literature above. Therefore:

- no absolute “first,” “no prior work,” or “novel classification” wording is supportable;
- an exact-package statement may later be classified only as `SUPPORTED_WITHIN_SEARCH`, after Phase 2 records databases, coverage dates, complete query strings, deduplication, nearest works, and `last_searched_at`;
- the absence of an exact package does not make the composition of classical ingredients a standalone contribution.

## 6. Precise amendment list

### A1 — Split the generic owner by cardinality

Add to research protocol section 2.1 and the candidate hard locks:

> The generic theorems may quantify over nonempty \(X\), but every assertion that the actual owner is non-Hausdorff or outside an audited groupoid \(C^*\)-framework is conditional on \(|X|\ge 2\). The singleton \(X=\{*\}\) is a mandatory Hausdorff control and is identified with the one-object group \(\mathbb R\). Before the fixed-prime owner is called non-Hausdorff, bind a source/companion locator proving that its unit set contains at least two distinct points.

### A2 — Freeze gauge quotient orientation

Replace “their quotient is \(\delta a\)” by:

> For normalized multipliers \(\sigma,\tau\), write \(\sigma\sim\tau\) when \(\sigma\overline{\tau}=\delta a\) for a normalized continuous one-cochain \(a\). The proposed gauge map is \(U_a:A_\sigma\to A_\tau\), \((U_af)(t)=a(t)f(t)\). Thus \(\sigma=\delta a\) means \(\sigma\sim1\) and \(U_a:A_\sigma\to A_1\). Every later product, star, representation, and norm identity uses this direction.

### A3 — Freeze the time-group analytic conventions

Add before the twisted algebra obligations:

> Lebesgue measure \(dt\) is the fixed left Haar measure on \((\mathbb R,+)\), and \(\Delta_{\mathbb R}=1\). For the frozen cocycle convention,
>
> \[
> (\lambda_\sigma(s)\xi)(t)=\sigma(s,t-s)\xi(t-s),\qquad
> \lambda_\sigma(s)\lambda_\sigma(u)=\sigma(s,u)\lambda_\sigma(s+u),
> \]
>
> and the integrated representation is \(\pi_\sigma(f)=\int_{\mathbb R}f(s)\lambda_\sigma(s)\,ds\). The product and involution are
>
> \[
> (f*_\sigma g)(t)=\int_{\mathbb R}f(u)g(t-u)\sigma(u,t-u)\,du,
> \qquad
> f^{*_\sigma}(t)=\overline{\sigma(t,-t)}\,\overline{f(-t)}.
> \]

These are the additive specializations of Austad’s left conventions.

### A4 — Separate standard time-group and author actual-owner completions

Add an explicit two-row type table:

| Record | Domain | Status/source ceiling |
|---|---|---|
| \(C^*(\mathbb R,\sigma)\), \(C_r^*(\mathbb R,\sigma)\) | standard locally compact group twisted algebra | Defined independently of triviality by the standard group theory; full \(=\) reduced from amenability. |
| `TW-FULL-TRANSPORT(σ)`, `TW-RED-TRANSPORT(σ)` | Paper-11 author global-QC record after exact time reduction | Author-defined transported norms only; never called a standard actual-groupoid \(C^*\)-algebra. |

Also state whether the paper proves equality of the author records with the restrictions of the standard time-group norms, rather than leaving that identification implicit.

### A5 — Replace the universal framework exclusion by a named hypothesis matrix

The Phase-2 audit must record at least:

| Framework | Required hypotheses relevant here | Actual owner with \(|X|>1\) |
|---|---|---|
| Standard Hausdorff Haar-groupoid framework | locally compact Hausdorff arrow/unit spaces plus Haar system | fails Hausdorffness |
| Austad–Ortega étale twisted framework | second-countable locally compact Hausdorff étale groupoid | fails Hausdorffness and étaleness |
| Tu non-Hausdorff framework | locally compact in Tu’s locally-Hausdorff sense; core constructions use Hausdorff unit space | fails local Hausdorffness and Hausdorff unit space |

The resulting claim must be “the named audited frameworks do not apply,” not “no standard framework exists.” Do not infer that the actual owner lacks a fibre measure or author convolution merely from these failures.

### A6 — Make retention a finite typed predicate

Replace the open-ended invariant language by:

> The construction tests only (i) the normalized continuous gauge class, (ii) the isomorphism classes of the named author-transported full and reduced records, and (iii) for each unit \(x\), the class of the restricted cocycle on the literal subgroup \(H_x\subset\mathbb R\), with the permitted restriction-gauge relation stated explicitly. “Action/period blind” means these named records are constant in the registered comparison family. It does not quantify over every possible invariant of an action. A dense nonclosed \(H_x\) is a continuous-cochain control only; no locally compact group, Haar, regular-representation, or \(C^*\)-completion theorem is invoked on it.

### A7 — Freeze source tiers before proof dispatch

The Phase-2 source manifest must include theorem/definition locators, exact domain, cocycle convention, cochain regularity, gauge regularity, access status, and ownership ceiling. At minimum:

- Sorkin (1978): candidate exact `CONTINUOUS/CONTINUOUS` owner for P13-3, pending full-text sign/normalization check;
- Austad (2021): exact owner for the group formulas and projective left regular representation;
- Leptin (1968) plus Hulanicki (1966): original amenability/full-reduced chain;
- Tu (2004) and Austad–Ortega (2022): hypothesis-exclusion sources only;
- Kleppner (1965): `BOREL/BOREL`, background only, never sole support for a continuous trivializer.

The direct proof obligations in protocol section 8 remain mandatory even if Sorkin translates exactly.

### A8 — Add a standalone novelty go/no-go discriminator

Append to section 12:

> Sorkin (1978) is the nearest exact precedent for the time-group collapse. Standard twisted convolution, involution, projective regular representation, and amenable full/reduced equality are prior art. `STANDALONE_PASS` therefore requires a theorem on the registered actual owner whose content is not a formal consequence of P13-1/P13-2, Sorkin’s real-line collapse, and the standard gauge-star package. If an independent post-proof reviewer cannot identify that theorem and state the nonformal dependency break in one paragraph, disposition is `NOTE_OR_MERGE`. An exact-package search with no hit may support only a search-bounded package statement; it cannot override this discriminator.

## 7. Gate disposition

- Phase-2 source acquisition: **FEASIBLE AFTER AMENDMENT**.
- Exact definitions and theorem-hypothesis alignment: **NOT YET LOCKED**.
- Standard actual-groupoid \(C^*\)-framework: **NOT APPLICABLE under the named audited frameworks for \(|X|>1\); singleton exception mandatory**.
- Standalone novelty: **HIGH RISK / NOT YET FEASIBLE**.
- Phase-1 exact-byte gate: **BLOCKED on the current tuple**.
- Proof, controls, Route, manuscript, and release: remain **BLOCKED**.

---

## 8. Amended-v1 exact-byte re-lock

Re-review date: 2026-08-15  
Scope: source/terminology feasibility re-lock only  
Prior report digest before this append: `6552209281bfeea5ed68b61e0347554dca0c776e521de681f3121ff625f2dd6a`

### 8.1 Exact receipt and independence

The amended bytes independently match the tuple supplied for re-lock:

| Artifact | SHA-256 | Receipt |
|---|---|---|
| `research_protocol.md` | `519563a28c3f11e3b3853f6875a84191444a68cd2c032c4cfcf69ca4152d5064` | MATCH |
| `candidate_lock.md` | `8cc0d08971762aa784afe1c844215353f170a75a3c0ab892415458ab010d0266` | MATCH |
| `pipeline_state.md` | `d98bf49d2eb5c1905ea3625251d787b247f3cf19577ff40f8bc0136186280fd5` | MATCH |
| `phase1_amendment_v1.md` | `ea5242ba6a8a1f2f867e8b258abc802fdeaace54db76629f0a9f0629e3e90d27` | MATCH |

I read only those four amended-lock artifacts and my own preceding report. I did not read a sibling Phase-1 review, reopen a companion manuscript, start Phase-2 browsing, or acquire a source PDF.

### 8.2 Re-lock verdict

**PASS for this review lane: `C=0`, `M=0`, `m=0`.**

The initial `M` verdict in section 2 remains the historical verdict on the initial tuple only. The active amended tuple closes every source/terminology finding from that review and is fit to enter the bounded Phase-2 source, framework, and precedent audits once the pipeline has all three independent zero-finding receipts. This receipt does not approve a proof, controls implementation, Route evaluation, manuscript, standalone disposition, release, or Git/public synchronization.

### 8.3 Closure of the initial findings

| Initial finding | Amended-v1 closure | Re-lock |
|---|---|---|
| M1 — singleton/non-Hausdorff quantifier | Amendment 3.1 separates the singleton time-group control, makes every non-Hausdorff and framework-exclusion statement conditional on `|X|>=2`, and binds the fixed-prime at-least-two-points premise to the locked Paper-9 `cor:packet` locator. | CLOSED |
| M2 — gauge direction and analytic typing | Amendment 4 freezes `sigma overline(tau)=delta a` and `U_a:A_sigma->A_tau`; Amendment 5 separately freezes the actual fibre formula, time-group product/star, sigma-projective left regular representation, integrated form, gauge intertwiner, Haar/modular convention, and norm directions. | CLOSED |
| M3 — unbounded retention predicate | Amendment 6 replaces the open-ended invariant claim by the finite typed records `TIME-GAUGE`, `ACTUAL-TW-TEST`, `ACTUAL-TW-FULL`, `ACTUAL-TW-RED`, and `ISOTROPY-TWIST(x)`, with an explicit literal-subgroup firewall. Dense nonclosed stabilizers are restricted to continuous-cochain controls and receive no Haar, regular-representation, or completion theorem. | CLOSED |
| M4 — classical prior art and novelty discriminator | Amendments 2 and 11 identify Sorkin’s real-line collapse and the standard gauge-star/amenability package as prior art, default `STANDALONE_PASS` to false, and require an independent post-proof dependency-break judgment. P13-8 is the sole registered candidate; failure, direct-restatement status, or exact precedent triggers `NOTE_OR_MERGE`. | CLOSED |
| m1 — multiplier terminology and regularity tiers | Amendment 4 freezes the first-use phrase “normalized continuous T-valued group 2-cocycle (projective multiplier).” Amendment 10 requires `CONTINUOUS/CONTINUOUS`, `BOREL/BOREL`, or `MIXED` per source row and permits only the first tier to own P13-3. | CLOSED |

### 8.4 Requested source and framework checks

**Source-tier wording.** The amended manifest requirements are sufficiently typed for Phase 2: exact manifestation and locator, cocycle sign, cochain and gauge regularity, access status, and ownership ceiling are mandatory. Sorkin remains a candidate exact owner only after full-text convention translation; Kleppner remains Borel background only. The amendment does not promote an abstract, a nearby theorem, or a mismatched regularity class into proof ownership.

**Named-framework ceiling.** Amendment 10 requires a hypothesis matrix for the standard Hausdorff Haar-groupoid framework, the Austad–Ortega Hausdorff étale framework, and Tu’s locally Hausdorff framework. Its permitted conclusion is only that those named audited frameworks fail on the actual owner when `|X|>=2`. It expressly forbids both the universal claim that no standard framework exists and the inference that the author fibre construction is unavailable.

**Group-versus-author records.** Amendments 5.2–5.3 keep the standard time-group objects `C*(R,sigma)` and `C*_r(R,sigma)` separate from `TW-FULL-TRANSPORT(sigma)` and `TW-RED-TRANSPORT(sigma)`. The latter remain author-defined records on the Paper-11 time-reduced global-QC domain, with equality to restricted standard time-group norms left as an explicit proof obligation and no actual-groupoid `C*` renaming.

**Sorkin and standard-prior novelty ceiling.** The amended claim ledger assigns the real-line collapse and ordinary twisted group analytic package low or prior-covered weight. No exact-package search result may turn those ingredients into novelty, and no absence-of-hit wording may exceed `SUPPORTED_WITHIN_SEARCH`.

### 8.5 P13-8 source feasibility and nonformality checkpoint

P13-8 is **source-feasible and sufficiently distinct to justify Phase-2 searching**, but it is **not standalone-approved**.

The theorem has a finite, auditable dependency chain already typed in the amendment: the locked Paper-11 actual support identity, the locked Paper-12 same-carrier standardization and direction of `J`, and the elementary compactness behavior of a topological coproduct of nonempty compact Hausdorff orbit summands. It asserts only an ordinary `C_c` support condition on the Hausdorff arrow space, so it requires no transfer of a groupoid completion theorem to the actual owner. The fixed-prime form is correctly conditional on the bare set `Q_p` and makes no unproved orbit-count, measure, enumeration, or quotient-topology claim.

The target is not a formal consequence of Sorkin’s multiplier collapse or of the standard gauge-star/amenability package: its decisive input is the asymmetric same-carrier topology map and the change from actual quasi-compact support to standard compact support. Circle-valued gauges are nowhere zero, so support preservation is a separately checkable bridge rather than borrowed analytic novelty. This difference is enough to warrant an exact-package Phase-2 precedent search.

At the same time, the stated proof route may turn out to be a short corollary of the locked Paper-11 and Paper-12 results plus elementary topology. Amendment 8 correctly makes that possibility fail closed to `NOTE_OR_MERGE`, and Amendment 11 reserves the nonformal dependency-break and substantive-weight decision for an independent post-proof reviewer. This re-lock therefore certifies feasibility only.

### 8.6 Zero-finding coverage receipt and gate

| Surface checked | Basis for no residual finding |
|---|---|
| M1–M4 and m1 amendments | Each initial defect has a specific superseding declaration, locator, and fail-closed consequence. |
| Definitions and terminology | Owner, cochain, gauge, representation, support, completion, and restriction types are separated without an unqualified standard-theory label. |
| Source ownership | Primary-source candidates own only their exact group/regularity/framework domain; companion-owned premises retain explicit locators and ceilings. |
| Novelty posture | Classical ingredients are credited as prior art; search-bounded absence and substantive standalone judgment remain distinct. |
| P13-8 feasibility | The target is well typed and source-auditable, logically distinct from the Sorkin/standard group package, and explicitly denied automatic standalone force. |

- Source/terminology Phase-1 re-lock on the amended tuple: **PASS (`C0/M0/m0`)**.
- Bounded Phase-2 source/framework/precedent work: **FEASIBLE, subject to the pipeline’s other independent receipts**.
- Proof, controls implementation, Route, manuscript, standalone approval, and release: remain **BLOCKED**.
