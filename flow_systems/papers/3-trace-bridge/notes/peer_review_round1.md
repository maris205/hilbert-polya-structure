# Paper 3 independent peer review — Round 1

**Manuscript:** *One Orbit Is Not a Trace: A Same-Object Certificate for Classical--Spectral Bridges*  
**Review date:** 2026-08-13  
**Review mode:** independent adversarial mathematical/domain/methodology review  
**Recommendation:** **MINOR REVISION**  
**Confidence:** **4/5** — the full LaTeX source, 14-page release PDF, protocol, source matrix, proof audit, composition blueprint, implementation, tests, generated results, and local primary-source hashes were inspected. The five trace frameworks were checked at the theorem-type level; the complete cofinite Selberg convention was not independently reconstructed because the project itself has not acquired the cited Selberg/Hejhal full text.

**Frozen submission reviewed:** `paper/manuscript.tex` SHA-256 `7c67b8929d111d19c44a40728c5d678f3153ab7b35bf3d15f5e8dfafe331e634`; `paper/paper.pdf` SHA-256 `19fc7e2c29cabc59a16915a91fce0eb907caa5e004af0f6fb2cd0733979bfec3`. Round-1 findings below refer to that submission snapshot; edits made concurrently after the snapshot should be adjudicated in re-review rather than silently erased from this report.

## 1. Editorial verdict

The three central claims survive adversarial checking.

1. The local-germ results are correct at their stated hypotheses. A full restriction near one period does not determine a global distribution, and—provided a set \(P\) is known to contain all possible nonzero singular support—equality of the singular germs at every point of \(P\) determines the difference only up to a distribution smooth on \(\mathbb R\setminus\{0\}\); fixing the zero germ leaves exactly a globally smooth difference.
2. The modular norm argument is complete. For \(m=|\operatorname{tr}A|>2\), the discriminant \(m^2-4\) is nonsquare, the nontrivial quadratic conjugation sends \(N_\gamma=\lambda^2\) to \(N_\gamma^{-1}\), and hence no positive power of \(N_\gamma\) is rational. The disjointness from every \(k\log p\) follows immediately by exponentiation.
3. The no-splicing lemma is valid as a type/provenance lemma. Its mathematical force is deliberately limited: it rejects an unproved coordinatewise union by definition, while a genuine transport theorem would create a new object to audit. The modular clock theorem, not T0 alone, supplies the substantive candidate-specific obstruction.

No critical or major defect was found. The paper should be accepted into the project series after a local precision revision. The main revisions are to expose the singular-support prior in the abstract, reconcile the Selberg source-acquisition limitation with the paper's own source-lock protocol, state two framework hypotheses/operators more exactly, and split the two Route-B non-entry reasons instead of assigning one undifferentiated `REFUTED` label. No new numerical experiment, zero lookup, or fitted computation is needed.

## 2. Strongest counter-argument and adjudication

The strongest objection is that the paper's most prominently named contribution—the “same-object certificate”—could be read as giving a mathematical no-composition theorem when its T0 lemma is actually a consequence of the chosen provenance schema. If field data are defined to retain immutable source labels, a record containing labels \(D\) and \(M\) necessarily fails a gate requiring one label. This is useful audit discipline, but it is not by itself a theorem that no functor, correspondence, time change, induced representation, or trace-preserving morphism can connect two objects. A critic could therefore dismiss Lemma 2 as tautological and accuse the surrounding “cannot be pasted together” language of deriving ontology from metadata.

This objection does not defeat the manuscript. The text already calls Lemma 2 a type statement, explicitly permits a new bridge morphism with transport proofs, and proves an independent algebraic obstruction for the most direct standard-clock atomwise bridge. The remedy is presentational: keep T0 identified as a formal certification rule, specify what evidence would convert transported data into one new source lock, and reserve the word “obstruction” for the quadratic support theorem. With that calibration, the certificate is a reproducible anti-equivocation device rather than an inflated no-go theorem.

## 3. Strengths

### S1. The local-germ theorem has the right exact boundary

The manuscript distinguishes full germs from singular germs, includes the necessary singular-support prior, describes the ambiguity on the punctured line rather than prematurely calling it globally smooth, and explicitly states that arbitrary prescribed local germs need not glue. It also correctly notes that an operator-defined trace is not made ambiguous by this inference theorem.

- **Evidence anchor:** equation: `paper/manuscript.tex:462-522`, especially Theorem 4 and its post-theorem boundary paragraph
- **Independent proof check:** `notes/proof_audit.md:33-156`
- **Assessment:** mathematically sound

### S2. The quadratic norm proof is universal and does not rely on finite separation

The factorization argument proves \(m^2-4\) nonsquare for every integral \(m>2\), and Galois conjugation proves irrationality for every positive repetition. The 108-row computation is correctly presented only as a regression control.

- **Evidence anchor:** equation: `paper/manuscript.tex:527-570`
- **Independent proof check:** `notes/proof_audit.md:158-224`
- **Assessment:** mathematically sound; no hidden primality, approximation, or decimal argument

### S3. The five trace frameworks are not collapsed into one ladder

The paper keeps fixed self-adjoint wave traces, exact cofinite Selberg identities, cohomological/b-trace Lefschetz distributions, flat traces and non-self-adjoint resonances, and \(\hbar\)-families separate. In particular, it does not infer a self-adjoint Hilbert--Pólya Hamiltonian from an exact flat trace or from cohomological exactness, and it does not turn a semiclassical expansion into a fixed-operator equality.

- **Evidence anchor:** table: `paper/manuscript.tex:327-457`
- **Primary-source cross-check:** the scalar \(k=0\) specialization of Dyatlov--Zworski's flat-trace formula and CRR Theorem 2.3 agree with the manuscript's intended distinctions
- **Assessment:** correct taxonomy, subject to the local wording revisions below

### S4. Candidate separation and Route discipline are substantive

`DEN-WITT-Z-FIN` is credited only with intrinsic prime-log packet support, while `MOD-GEO` is credited with its natural Laplacian and exact same-geometry trace architecture but rejected for the rational-prime atomic target. No favorable-coordinate average is taken, and no Route-B rescue is attempted.

- **Evidence anchor:** table: `paper/manuscript.tex:579-628`
- **Route-rule cross-check:** `skills/route-a-evaluator.md` Sections A0--A4 and overall decision; `skills/route-b-evaluator.md` Sections 2--3
- **Assessment:** substantively calibrated; one evidence-token split is required below

### S5. The computational artifacts reproduce exactly what they claim

`bash experiments/reproduce.sh` completed successfully: 11/11 tests passed, 108 quadratic rows were regenerated, the sampled local difference was exactly zero, the global bump difference was \(0.75\), the hybrid T0 result was false, and all eight manifest entries verified. The code records zero Riemann-zero inputs, zero fitted parameters, zero network inputs, and no random seed. It does not present finite controls as proofs of the universal theorems.

- **Evidence anchor:** dataset: `results/run_summary.json`, `results/certificate_t0_audit.json`, and `results/manifest.sha256`
- **Assessment:** reproducibility pass

## 4. Critical issues

None.

The review explicitly tested for a false local-to-global uniqueness claim, a missing support hypothesis in the theorem itself, a square-discriminant exception, a primitive/repetition mismatch, a clock-rescaling loophole hidden inside the frozen candidate, a transfer of Selberg coefficients without equal atomic support, and an unauthorized Route-B promotion. None survives as a critical defect in the body of the manuscript.

## 5. Major issues

None.

The core claims do not require new mathematics, re-analysis, or new data. The issues below are important source-lock and statement-precision repairs, but all can be resolved locally.

## 6. Minor issues and required revisions

### W1. The abstract omits the singular-support prior required by its strongest local-germ sentence

The abstract says that “all nonzero singular germs” leave an ambiguity smooth off zero without stating that \(P\) must contain every possible nonzero singular location. The theorem and limitations section correctly include this hypothesis, and the following paragraph even supplies the counterexample \(\delta_q\) when it is absent. Because the abstract's version is literally false without the prior, this condition must travel with the headline claim in both languages.

- **Severity:** Minor
- **Evidence anchor:** text: `paper/manuscript.tex:90-93`, “Even all nonzero singular germs leave an exactly characterized ambiguity that is smooth off zero”
- **Counter-anchor showing the correct statement:** equation: `paper/manuscript.tex:487-520`
- **Confidence:** 5/5 — direct distribution-theoretic check
- **Required revision:** Insert wording equivalent to “given a prior containing all possible nonzero singular support” in the English and Chinese abstracts. Preserve the separate zero-germ conclusion.

### W2. The Selberg limitation is honest, but it does not support a fully passed source-lock/convention gate

The manuscript responsibly prints only a typed schematic cofinite identity and discloses that no complete Selberg/Hejhal copy was locally read. That is enough to protect the quadratic support theorem, which uses no cofinite constants. It is not enough, under this paper's own protocol, to call the local cofinite convention “tested,” to treat T2/T6 as fully certified, or to say the pending convention was frozen. The protocol required acquisition before a coefficient table/manuscript citation, while the source matrix still says acquisition is pending.

- **Severity:** Minor
- **Evidence anchor:** text: `paper/manuscript.tex:214-221`, `347-373`, and `685-691`
- **Protocol anchor:** text: `notes/research_protocol.md:139-147` and `355-363`
- **Source-ledger anchor:** table: `notes/source_matrix.md:99-100` and `167-180`
- **Confidence:** 5/5 — direct internal-protocol comparison
- **Required revision:** Choose one of two clean resolutions:
  1. acquire and hash one full cofinite source, freeze its test class/Fourier/scattering convention, and then retain `PROVED`/passed T2 and T6 wording; or
  2. keep the schematic formula but replace “exact complete tested identity” by “established exact framework; local convention not formula-verified in this stage,” mark the convention-dependent parts of T2/T6 `OPEN` or `NOT_TESTABLE`, and record an explicit protocol deviation/amendment.

The second option is sufficient for this paper because the main no-splicing theorem is convention-independent.

### W3. The Duistermaat--Guillemin summary should state the normalized first-order operator used in the displayed wave group

The original framework starts with a positive elliptic operator and normalizes to the first-order wave generator governing the homogeneous bicharacteristic flow. The manuscript writes \(\Theta_P(t)=\operatorname{Tr}e^{-itP}\) for an unqualified positive elliptic pseudodifferential operator. To make that formula unambiguous, specify that the displayed \(P\) is the positive self-adjoint elliptic operator of order one (or explicitly replace an order-\(m\) operator by its positive \(m\)-th root), with real scalar principal symbol on a closed manifold.

- **Severity:** Minor
- **Evidence anchor:** equation: `paper/manuscript.tex:330-345`
- **Confidence:** 4/5 — standard wave-trace normalization; exact notation varies by source
- **Required revision:** Add the order-one/root normalization and scalar-principal-symbol qualification in the subsection and taxonomy row. This does not change the non-applicability finding for Deninger's frozen object.

### W4. The Ruelle flat-trace display reuses an undefined \(P\) and silently selects the scalar specialization

Equation (3) is correct for the scalar-function specialization, but the subsection does not define its dynamical generator and reuses \(P\), which previously denoted the elliptic wave operator. The cited Dyatlov--Zworski formula is stated for \(P=(1/i)\mathcal L_V\) on invariant form bundles; the general numerator includes the bundle trace \(\operatorname{tr}(\wedge^k\mathcal P_\gamma)\), while \(k=0\) reduces to the displayed coefficient.

- **Severity:** Minor
- **Evidence anchor:** equation: `paper/manuscript.tex:398-421`
- **Confidence:** 5/5 — direct check against the cited primary formula
- **Required revision:** Define the vector field and generator before the display, say explicitly that the equation is the scalar \(k=0\) case, and retain the wavefront/normal-return qualification. No coefficient change is required for that specialization.

### W5. Lemma 2 should remain visibly a formal schema lemma rather than a standalone mathematical obstruction

The proof is valid because T0 is defined to require one provenance pair, but the result is tautological relative to that definition. The sentence permitting a genuine bridge morphism is essential and should be made operational: a transport datum must identify source, target, clock, repetitions, trace/test class, coefficient, non-orbit terms, and normalization, and must rederive the transported fields in a new record. Otherwise a source-lock string remains audit metadata rather than a mathematical invariant.

- **Severity:** Minor
- **Evidence anchor:** equation: `paper/manuscript.tex:264-325`
- **Confidence:** 5/5 — direct logical-form analysis
- **Required revision:** Label Lemma 2 explicitly as a “formal certificate lemma” or “schema lemma,” and add one sentence defining the evidence required to assign a new provenance after a bridge. Keep Corollary 6 as the independent mathematical obstruction for the frozen DEN/MOD atomwise case.

### W6. The combined Route-B `REFUTED` token conflates two different failure states

The body correctly says Route B was not invoked. In the claim ledger, however, “either candidate is Route-B ready” is marked `REFUTED`. Under the Route-B skill, missing Hilbert space/operator/domain inputs make the Deninger audit `NOT_TESTABLE` and its entry unauthorized; for the modular candidate, the rational-prime Route-A entry fails, so Route B cannot be used as a rescue. These are not the same evidence state.

- **Severity:** Minor
- **Evidence anchor:** table: `paper/manuscript.tex:785-796`, especially the final row
- **Route anchor:** text: `skills/route-b-evaluator.md`, Sections 2--3
- **Confidence:** 5/5 — exact enum and entry-rule comparison
- **Required revision:** Split the final row into candidate-specific statements. Recommended wording: DEN—“Route-B entry unauthorized; required inputs `NOT_TESTABLE`”; MOD—“Route-B entry unauthorized for the rational-prime target because Route A is rejected.” Reserve `REFUTED` for the proved modular clock-support claim.

### W7. The frozen notes retain two pre-revision statements that no longer match the manuscript

The protocol's preliminary Theorem A says all nonzero period germs leave ambiguity “modulo a smooth term,” whereas the final theorem correctly says smooth only on the punctured line until the zero germ is fixed. The composition blueprint repeats the shorter form. The protocol also says its Selberg convention freeze is a Phase-A completion obligation even though the source matrix records it as pending. These drifts weaken the claim that the pre-manuscript record is source-locked.

- **Severity:** Minor
- **Evidence anchor:** text: `notes/research_protocol.md:236-256`; table: `notes/composition_blueprint.md:29-39`; text: `notes/research_protocol.md:355-363`
- **Confidence:** 5/5 — direct artifact comparison
- **Required revision:** Mark the germ language as superseded by Theorem A2's exact punctured-line statement, and explicitly document the Selberg acquisition deviation rather than silently treating Phase A as complete.

### W8. The PDF is readable, but one macro-space bug and heavily underfull tables should be cleaned

The release PDF has no unresolved citations/references, missing-character warnings, or overfull boxes, and visual inspection found no clipped mathematics. However, `\refuted refer` renders as `REFUTEDrefer`, and the log contains many bad underfull boxes in Tables 2--4 and the artifact map. The narrow columns create conspicuously stretched prose even though it remains legible.

- **Severity:** Minor
- **Evidence anchor:** text: `paper/manuscript.tex:185-191`; dataset: `paper/manuscript.log:1157-1440`
- **Confidence:** 5/5 — extracted-text and rendered-page inspection
- **Required revision:** Define status macros with `\xspace` or add braces at prose uses; rebalance the narrow longtable columns or use ragged-right paragraph columns. Recompile and visually inspect the certificate, taxonomy, candidate, and artifact tables.

## 7. Focused mathematical adjudication

### 7.1 Local-germ ambiguity

**Pass, after abstract synchronization.** The sheaf argument is sufficient for arbitrary \(P\subset\mathbb R\setminus\{0\}\); discreteness or local finiteness of \(P\) is not required because smoothness is checked pointwise. Conversely, adding any member of

\[
\mathcal A_0=\{S\in\mathcal D'(\mathbb R):S|_{\mathbb R\setminus\{0\}}\in C^\infty\}
\]

preserves the nonzero singular germs and the support prior on the punctured line. Strictly, the admissible distributions form an affine coset \(\Theta+\mathcal A_0\), while \(\mathcal A_0\) is the difference space; the current wording “ambiguity class” is acceptable, though “difference space” would be maximally precise. Proposition 3 would also read more cleanly as “same restriction on \(U\), hence the same full germ at \(T\)” rather than “same full germ on \(U\).” These latter points are optional copyedits.

### 7.2 Modular norm and clock support

**Pass without revision.** The lift sign disappears under \(|\operatorname{tr}A|\); \(D=m^2-4\) cannot be a square for integral \(m>2\); \(\lambda\lambda'=1\); and the field conjugate of \(N_\gamma^r\) is its inverse. If it were rational it would be fixed by conjugation, forcing \(N_\gamma^{2r}=1\), impossible for \(N_\gamma>1\). The standard translation-length identity \(\ell_\gamma=2\log\lambda\) then gives the claimed disjointness. The theorem is stronger than needed because it excludes equality with the logarithm of every rational number greater than one, not only prime powers.

### 7.3 T0 type lemma

**Pass as a formal audit lemma, not as a universal no-go theorem.** Its proof is definitionally complete. The manuscript's existing bridge-morphism caveat prevents the main overclaim. The requested wording revision is to keep that logical status visible at every summary surface.

### 7.4 Five trace-framework non-implications

**Pass with W2--W4.** None of the five rows licenses the inference printed in its “Does not imply” column. The most important distinction—exactness of a trace framework versus arithmetic support—is independently witnessed by the modular control. The Selberg row is framework-level rather than locally convention-certified; the DG and Ruelle rows need the small operator specifications above. The ALKL/Kordyukov and CRR descriptions match the locally acquired/source-checked materials at the level used by the paper.

### 7.5 Route decisions

**Substantive pass; token-level revision required.** The defensible state is:

| Candidate | Route-A state supported here | Route-B consequence |
|---|---|---|
| `DEN-WITT-Z-FIN` | retain intrinsic A0 arithmetic origin and weak packet-level A1; conventional A2 fails from Stage 2; A3/A4 evidence remains `NOT_TESTABLE` because no same-object analytic trace/operator exists | entry not authorized; full Route-B audit `NOT_TESTABLE` on required inputs |
| `MOD-GEO` | retain exact non-Riemann trace/Laplacian benchmark, A3 partial analytic structure, and A4 natural quantization; rational-prime A0/T7 is refuted under the frozen clock | entry not authorized for the rational-prime target; Route B may not rescue failed Route A |

No Hilbert--Pólya claim is allowed, and no hybrid route vector is valid.

## 8. Reproducibility and release audit

- Release PDF SHA-256 at review: `19fc7e2c29cabc59a16915a91fce0eb907caa5e004af0f6fb2cd0733979bfec3`.
- `paper/manuscript.pdf` and `paper/paper.pdf` were byte-identical at review.
- XeLaTeX rebuild succeeded at 14 pages. The new PDF differed only at the binary metadata/build level expected from a fresh PDF generation; citations and references resolved.
- `bash experiments/reproduce.sh`: **PASS**, 11/11 tests.
- Result manifest: **PASS**, 8/8 files verified.
- Local source hashes listed for Deninger, Duistermaat--Guillemin, Kordyukov, ALKL, Dyatlov--Zworski, and Fried match the source matrix.
- ARS PDF read preflight: **UNAVAILABLE** because `pypdf` is not installed. This was not promoted to `PASS`; source-line anchors, `pdftotext`, `pdfinfo`, and rendered-page inspection were used instead.
- Visual inspection: all 14 pages were rendered; representative pages 1, 4, 7, 10, 13, and 14 were inspected at readable scale. No clipping or missing glyph was found.

## 9. Revision checklist

Required before acceptance:

- [ ] Add the all-possible-singular-support prior to both abstracts.
- [ ] Either freeze one complete cofinite Selberg convention or downgrade convention-dependent T2/T6 wording and record the protocol amendment.
- [ ] State the normalized first-order Duistermaat--Guillemin wave operator.
- [ ] Define the Ruelle generator and identify Equation (3) as the scalar \(k=0\) flat-trace specialization.
- [ ] Keep Lemma 2 visibly classified as a formal/schema lemma and make new-provenance transport evidence explicit.
- [ ] Split the DEN and MOD Route-B non-entry statuses; do not label missing DEN operator inputs `REFUTED`.
- [ ] Synchronize the protocol/blueprint with the final punctured-line ambiguity theorem and the documented Selberg acquisition state.
- [ ] Fix `REFUTEDrefer`, improve the most stretched tables, rebuild, rerun the 11 tests, and verify the manifest.

## 10. Final recommendation

**MINOR REVISION, then ACCEPT.** The paper's strongest contribution is the conjunction of two different kinds of discipline: an exact algebraic theorem rules out the standard-clock atomwise DEN/MOD fusion, while a typed certificate prevents local, semiclassical, resonant, cohomological, and self-adjoint trace data from being silently interchanged. The elementary distribution and quadratic-field proofs are correct. Once the abstract, source-lock status, framework hypotheses, and Route evidence tokens are synchronized, the manuscript will be a sound third step in the project sequence.

## 11. Post-revision verification and final gate

**Re-review date:** 2026-08-13  
**Revised manuscript:** `paper/manuscript.tex` SHA-256 `b51a7527de679778603b3530dfb9c5f6c5336681ca3a285219baaa8eeb5cb7fb`  
**Revised release PDF:** `paper/paper.pdf` SHA-256 `7ba58d4c389f476950125975c0c041e76d7691b8d0f769ab69ce319f8ed4fde7`  
**Final recommendation:** **ACCEPT**  
**Confidence:** **5/5** for closure of the eight Round-1 requirements; the mathematical verdict remains scoped to the source manifestations and theorem families identified above.

### 11.1 Item-by-item verification

| Round-1 item | Verification | Result |
|---|---|---|
| W1 singular-support prior | Both English and Chinese abstracts now state the prior containing every possible nonzero singular location. | **FULLY ADDRESSED** |
| W2 Selberg source lock | The manuscript now distinguishes the established exact cofinite framework from a locally unverified convention; convention-dependent T2/T6 fields are `NOT TESTABLE`, and the protocol records a dated Phase-A execution amendment. | **FULLY ADDRESSED** |
| W3 DG operator normalization | The wave-trace subsection now specifies a positive self-adjoint first-order elliptic operator with real scalar principal symbol and explains the positive-root normalization from order \(m\). | **FULLY ADDRESSED** |
| W4 Ruelle generator/specialization | The manuscript defines \(P_V=(1/i)\mathcal L_V\), labels the display as the scalar \(k=0\) case, and records the bundle trace in the differential-form version. | **FULLY ADDRESSED** |
| W5 formal status of T0 lemma | The theorem heading and surrounding prose now call it a formal certificate/schema lemma and enumerate the rederivation evidence required for a new provenance. | **FULLY ADDRESSED** |
| W6 Route-B evidence split | The claim ledger now separates DEN's missing required inputs/unauthorized entry from MOD's failed rational-prime Route-A entry. No combined `REFUTED` token remains. | **FULLY ADDRESSED** |
| W7 note synchronization | The protocol and composition blueprint now state punctured-line ambiguity, zero-germ refinement, and the uncompleted Selberg convention acquisition explicitly. | **FULLY ADDRESSED** |
| W8 typesetting | Status macros now preserve following spaces, tables use ragged-right paragraph columns, and the rebuilt log has no warning class identified in Round 1. | **FULLY ADDRESSED** |

### 11.2 Regression checks

- `paper/manuscript.pdf` and `paper/paper.pdf` are byte-identical at SHA-256 `7ba58d4c389f476950125975c0c041e76d7691b8d0f769ab69ce319f8ed4fde7`.
- The release PDF has 14 pages and is readable by `pdfinfo` and `pdftotext`.
- The XeLaTeX/BibTeX log has no unresolved citation/reference, missing-character, overfull, underfull, or LaTeX warning found by the release audit.
- `bash experiments/reproduce.sh` again passed **11/11** tests and verified **8/8** manifest entries.
- All 14 release pages were rendered after revision; pages 1, 4, 6, 8, 10, and 12--14 were visually reinspected. The revised certificate, taxonomy, candidate-status, claim-ledger, artifact, and bibliography tables show no clipping or missing glyphs.
- The revisions do not alter the proofs of Theorem 4 or Theorem 5, do not add Riemann-zero data or fitted parameters, and do not widen the no-splicing claim beyond the frozen standard-clock atomwise case.

### 11.3 Final adjudication

No residual critical, major, or required minor issue remains. The Selberg acquisition obligation is now a disclosed limitation rather than an implicitly passed convention gate; it does not block the convention-independent support theorem or the paper's certification conclusion. The revised manuscript therefore passes the independent mathematical, source-lock, Route-discipline, reproducibility, and presentation gates.

**FINAL GATE: ACCEPT.**
