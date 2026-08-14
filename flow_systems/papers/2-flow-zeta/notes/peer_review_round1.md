# Paper 2 independent peer review — Round 1

**Manuscript:** *Arithmetic Period Packets and the Missing Trace: A Source-Locked Zeta Audit of Deninger's Rational-Witt Flow*  
**Review date:** 2026-08-13  
**Review mode:** independent mathematical/domain/methodology stress test  
**Recommendation:** **MINOR REVISION**  
**Confidence:** **4/5** — the full manuscript, compiled PDF, Deninger source audit, trace-framework audit, no-go audit, proof audit, Route-A record, code, tests, and principal local source passages were inspected; this was not a line-by-line rederivation of every cited trace theorem.

## 1. Editorial verdict

The central result is sound and appropriately narrow. The manuscript proves a genuine theorem-level obstruction to the **ordinary one-factor-per-individual-orbit product**: each prime packet contains uncountably many primitive orbits at one length, so the finite-subset product net diverges. It also correctly refuses to promote this result into a universal impossibility theorem for measured, groupoid, clean-family, or cohomological enrichments. The conditional component-mass theorem is elementary but useful, and its hypotheses are mostly disclosed with unusual care.

No critical or major defect was found in the main mathematical argument. The paper should be accepted into the project series after a small revision. The required changes are local: complete one omitted convergence case, make the conditional trace theorem's algebraic hypotheses explicit, remove two small evidence-status drifts, sharpen the N2 discussion, correct one bibliography entry, and repair visible LaTeX overfull/diagram problems. No new experiment and no Riemann-zero calculation is needed.

## 2. Strongest counter-argument and adjudication

The strongest objection is that the paper could be read as turning an **absence in the audited source** into a theorem of **nonexistence or non-canonicity for every construction derived from the frozen object**. In particular, the abstract's sentence “It does not,” the Route-A metric `canonical_determinant: false`, and the claim-ledger phrase “refuted conditionally” can sound stronger than the paper's actual proof. The direct-sum theorem shows non-uniqueness only under its stipulated componentwise homogeneous axioms; it does not exhaust every arithmetic functor, relation between prime components, or future packet-specific trace theorem.

This objection does **not** defeat the manuscript, because the body repeatedly states the correct split: ordinary orbitwise A2 is proved to fail, while a source-intrinsic measured alternative is open or not testable. The remedy is to make the abstract, ledger, and YAML use that same split without isolated stronger tokens. After that alignment, the main conclusion is defensible.

## 3. Strengths

### S1. The source lock is unusually disciplined

The manuscript distinguishes Deninger's source-defined packet facts from topology and measure assertions not established by the source. It correctly treats equations (37)--(39) as a noncanonical equivariant set description and equation (40) as the separately canonical projection.

- **Evidence anchor:** text: `paper/manuscript.tex:323-349`, especially “used as a noncanonical R-equivariant bijection of sets”
- **Source cross-check:** local `deninger-dynamical-systems-arithmetic-schemes-v4.pdf`, equations (38)--(40), Theorems 5.2 and 6.1

### S2. The uncountability proof is complete and covers \(p=2\)

The sign-subgroup argument avoids the weaker finite-generation shortcut from the early source note. It explicitly fixes the \(2\)-adic coordinate, uses infinitely many odd primes, and needs only that \(p^{\widehat{\mathbb Z}}\) is a closed procyclic image. The involution argument in a finite cyclic quotient is valid.

- **Evidence anchor:** equation: Proposition 1 and proof, `paper/manuscript.tex:374-430`
- **Independent support:** `notes/proof_audit.md:24-136`

### S3. The ordinary-versus-measured boundary is preserved

The finite-subset-net theorem proves exactly the ordinary product obstruction and the following remark explicitly withholds any universal claim about measured, clean-family, groupoid, or cohomological constructions.

- **Evidence anchor:** equation: Theorem 4 and Remark 5, `paper/manuscript.tex:454-501`

### S4. The normalization audit separates genuinely different interfaces

N1, N2, N3, and O are not conflated. In particular, the manuscript acknowledges the real Section-11 Haar convolution algebra while showing that no packet-return bridge is supplied. This avoids the two opposite errors of overlooking Section 11 or treating any Haar normalization as the desired dynamical trace.

- **Evidence anchor:** table: Figure 1 and Section-11 bridge table, manuscript PDF pp. 7 and 15
- **Source cross-check:** `notes/phase2_deninger_source_audit.md:347-394`

### S5. Route-A and computation are leakage-aware

The ordinary A2 failure, the untested enriched alternative, and downstream A3 non-applicability are distinguished in prose. The code uses only deterministic closed-point prime data, discloses every mass model, and is not used to infer existence of a trace.

- **Evidence anchor:** table: Route-A split table, `paper/manuscript.tex:1032-1078`
- **Evidence anchor:** dataset: `results/packet_trace_controls_manifest.json`

## 4. Critical issues

None.

The review explicitly checked for a false universal no-go, an invalid uncountability quotient argument, an illicit packet-to-one-orbit collapse, an undisclosed Euler-product insertion, and a Route-B jump. None survives as a critical defect in the current body text.

## 5. Major issues

None.

The core claims survive without new mathematics or re-analysis. The items below are important for precision and publication quality but can be repaired locally.

## 6. Minor issues and required revisions

### W1. The abscissa proof omits the σ ≤ 0 branch

Theorem 7 states convergence “exactly when” σ > α + 1, but its proof starts with σ > 0 and only observes that the claimed convergence domain lies there. Exactness also requires explicitly disposing of σ ≤ 0. The result remains correct: for σ = 0 the inner harmonic series diverges, while for σ < 0 its terms do not tend to zero.

- **Severity:** Minor
- **Evidence anchor:** equation: Theorem 7 proof, `paper/manuscript.tex:660-695`
- **Confidence:** 5/5 — direct elementary series check
- **Required revision:** State that σ is real and add the one-sentence σ ≤ 0 argument before treating σ > 0.

### W2. The component-mass theorem should name the involutive algebraic structure

“Positive trace” is only defined after a ∗-structure and a positive cone have been fixed. The theorem currently says merely “algebraic direct sum” and “algebras,” although its proof uses positivity. Standard readers will infer the intended componentwise ∗-algebra, but it should not remain implicit in a theorem whose purpose is hypothesis discipline.

- **Severity:** Minor
- **Evidence anchor:** equation: Theorem 6, `paper/manuscript.tex:563-593`
- **Confidence:** 5/5 — definitional algebra point
- **Required revision:** Replace the hypotheses by an algebraic direct sum of ∗-algebras with componentwise product and involution, each carrying a nonzero positive trace. Retain the already stated finite-support and completion caveats.

### W3. The formal nonintegral packet product needs an explicit logarithm convention

For real noninteger \(m_p\), the expression \((1-p^{-s})^{-m_p}\) needs a branch convention before it is called a holomorphic product. On \(\Re s>0\) this is easy: \(|p^{-s}|<1\), so the holomorphic logarithm determined by the power series for \(-\log(1-p^{-s})\) is available. The positive-series theorem itself is unaffected.

- **Severity:** Minor
- **Evidence anchor:** equation: formal product and logarithm, `paper/manuscript.tex:642-658`
- **Confidence:** 5/5 — standard infinite-product convention
- **Required revision:** Define \(Z_m\) through the displayed logarithmic series on its absolute-convergence half-plane, or explicitly select the power-series branch of `Log` on \(\Re s>0\).

### W4. N2 should acknowledge the canonical probability on each individual orbit

The flow parameter and isotropy \((\log p)\mathbb Z\) already make every individual orbit an \(\mathbb R\)-homogeneous circle with a unique normalized invariant Haar probability. What is missing is not that local probability in isolation, but a source-canonical measurable assembly/disintegration over the orbit base, proof of independence from packet coordinates, and a theorem identifying any chosen fibre normalization with a trace coefficient. The present text gestures toward this distinction but can be read as denying even the orbitwise probability.

- **Severity:** Minor
- **Evidence anchor:** text: N2 discussion, `paper/manuscript.tex:536-553`
- **Confidence:** 4/5 — standard homogeneous-space measure fact; packet measurability remains source-dependent
- **Required revision:** Add one sentence acknowledging normalized invariant probability on each abstract circle, then state precisely why this does not supply the global packet measure or return trace. Keep fibre total mass \(1\), \(\log p\), and a trace-derived mass explicitly separated.

### W5. Evidence-status tokens drift at two output surfaces

The manuscript's controlled vocabulary contains `proved`, `conditional`, `open`, and `not testable`, but the claim ledger uses “refuted conditionally.” The YAML metric `canonical_determinant: false` can likewise be read as a nonexistence result, although the same YAML correctly calls measured alternatives `NOT_TESTABLE`. These are small tokens with disproportionate downstream risk because registries may treat them as machine-readable verdicts.

- **Severity:** Minor
- **Evidence anchor:** table: claim ledger, `paper/manuscript.tex:1215-1237`; dataset: `evaluations/route_a/DEN-WITT-Z-FIN/2026-08-13-stage2.yaml:67-88`
- **Confidence:** 5/5 — direct consistency comparison
- **Required revision:** Use `CONDITIONAL` for the homogeneous-axiom non-uniqueness theorem and change `canonical_determinant: false` to `NOT_TESTABLE` or `not_defined_for_frozen_object`. Preserve `conventional_orbit_product: divergent` as the proved negative.

### W6. Keep the abstract's first answer synchronized with the split verdict

The standalone “It does not” is immediately qualified and is defensible if “already defines” means “is supplied by the theorem-level packet data.” Nevertheless, it is the easiest sentence to quote without the qualification and therefore the most likely source of an exaggerated universal-no-go reading.

- **Severity:** Minor
- **Evidence anchor:** text: abstract, `paper/manuscript.tex:82-89`, “It does not.”
- **Confidence:** 4/5 — editorial scope-risk assessment
- **Required revision:** Prefer a split sentence such as: “Not at the presently auditable level: the ordinary orbitwise product fails, while a source-intrinsic measured replacement is not yet testable.” No change to the paper's actual theorem is needed.

### W7. One reference has the erratum authors in the wrong order

The local erratum first page gives “Paolo Giulietti, Carlangelo Liverani, and Mark Pollicott.” The BibTeX entry currently orders them as Giulietti, Pollicott, Liverani. The substance and arXiv identifier are correct.

- **Severity:** Minor
- **Evidence anchor:** text: `paper/references.bib:145-153`; local source first page, “PAOLO GIULIETTI, CARLANGELO LIVERANI, AND MARK POLLICOTT”
- **Confidence:** 5/5 — direct source metadata
- **Required revision:** Correct the author order. It would also improve source locking to add `arXiv:1807.06400v4` to the Deninger journal entry or its note, because v4 is the audited manifestation.

### W8. The PDF has several visible but nonfatal layout defects

The final XeLaTeX build resolves citations and references and contains no missing-character warning. However, the log reports overfull boxes of about 16.0 pt at lines 230--239, 15.3 pt at lines 916--926, and 12.9 pt at the Route-A display. Figure 1's arrow labels are crowded across box boundaries, and the framework longtable is readable but excessively ragged. XeCJK also reports an undefined CJK monospaced family.

- **Severity:** Minor
- **Evidence anchor:** figure: manuscript PDF pp. 7, 13--15; `paper/manuscript.log:1104-1419`
- **Confidence:** 5/5 — compiled-log and rendered-page inspection
- **Required revision:** Reflow the obligations and Anosov paragraphs; replace the long Route-A `align*` block with a compact table/description; redesign Figure 1 with two rows or shorter arrow labels; set a CJK mono font or avoid CJK in monospaced contexts. The 1 pt table overflows are cosmetic but can be removed while rebalancing column widths.

## 7. Source-faithfulness assessment

### Deninger packet theorem

**Pass.** Direct inspection of the local v4 text confirms:

- equations (38)--(39) give the choice-dependent equivariant packet coordinates;
- the paragraph following (39) says the packet fibres over the compact group \(B_p\);
- the source explicitly states that maps (37), (38), and the fibration depend on (x) and ι;
- equation (40), rather than the \(B_p\) projection, is declared canonical;
- Theorem 5.2 gives the pre-suspension isotropy decomposition;
- Theorem 6.1 gives the suspended packet decomposition, common period, and uniqueness of the packet containing a periodic orbit.

The manuscript does not silently upgrade these facts to a canonical homeomorphism or locally trivial bundle.

### Section 11

**Pass.** The manuscript accurately reports a Haar-normalized convolution algebra on a different inverse-limit multiplicative group and does not mislabel the algebra homomorphism as a trace. The negative statement is properly phrased as absence of a source theorem connecting it to packet returns.

### Trace frameworks

**Pass with ordinary citation caution.** The manuscript uses Duistermaat--Guillemin, Bourgeois, Kordyukov, ALKL, Connes/Renault, and Anosov/Ruelle results as applicability benchmarks, not as universal nonexistence theorems. This is the correct inference level. The bibliography audit already discloses that page-level PDF preflight was unavailable; the manuscript preserves that limitation.

## 8. Route-A / Route-B assessment

The substantive status is coherent with `skills/route-a-evaluator.md`:

| Layer | Review verdict | Comment |
|---|---|---|
| A0 | `A0_ANALYTIC_ARITHMETIC_ORIGIN` | closed points and the clock are intrinsic under the disclosed `E_f` lock |
| A1 | `A1_WEAK` | genuine periods/repetitions, but uncountable multiplicity and no derived weight/phase/monodromy |
| A2 | `A2_FAIL` for the conventional product | proved by the finite-subset net |
| A2 alternative | `NOT_TESTABLE` | measured/groupoid/cohomological candidate not defined, not refuted |
| A3 | serialized `A3_FAIL`, substantively not reached | acceptable because the route evaluator's enum has no `A3_BLOCKED_BY_A2`; prose must continue to say not reached |
| A4 | `A4_FAIL` / no natural lift supplied | no same-object quantum/cohomological lift |
| Overall | `ROUTE_A_EXPLORATORY` | calibrated; arithmetic survivor without determinant |
| Route B | not authorized | correct under the current route rules |

No Route-B work should be triggered by this manuscript alone.

## 9. Revision checklist

Required before acceptance:

- [ ] Add the σ ≤ 0 divergence sentence to Theorem 7's proof.
- [ ] State the ∗-algebra/componentwise hypotheses in Theorem 6.
- [ ] Define the logarithm convention for nonintegral formal packet masses.
- [ ] Clarify individual-orbit Haar probability versus packet disintegration/trace.
- [ ] Align abstract, claim ledger, and YAML with the ordinary-fail / enriched-not-testable split.
- [ ] Correct the GLP erratum author order and identify the audited Deninger v4 manifestation.
- [ ] Remove significant overfull boxes and uncrowd Figure 1.
- [ ] Recompile, confirm no undefined citations/references or missing characters, and visually inspect pp. 1, 7, 13--16, and the bibliography.

## 10. Final recommendation

**MINOR REVISION, then ACCEPT.** The paper's strongest contribution is not a new zeta function but a clean theorem-and-interface boundary: intrinsic arithmetic periods do not by themselves supply an orbit-counting determinant, while the broader packet-trace problem remains open rather than disproved. That conclusion is mathematically useful, source-faithful, and suitable as the second project in the research sequence once the local precision and typesetting issues above are repaired.
