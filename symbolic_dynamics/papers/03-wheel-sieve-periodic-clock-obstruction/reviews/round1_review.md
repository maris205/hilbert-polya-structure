# Round 1 Review

Manuscript reviewed: `papers/03-wheel-sieve-periodic-clock-obstruction/`

Objects checked:

- current source (`main.tex`, `sections/`, `references.bib`, `SOURCE_LOCK.md`, `PROOF_PACKAGE.md`)
- visual baseline `main_round0_original.pdf`
- upstream dependencies in Paper 01 and Paper 02, especially the wheel prime-enumeration proof and the Paper-02 scope boundary

Review standard:

- theorem correctness first
- then assumption discipline, novelty language, project-scope consistency, figure/reference/shareability readiness

## Overall verdict

Verdict: **REVISE**

Score: **6/10**

Bottom line: I do **not** currently see a theorem-breaking flaw in the two main mathematical statements as they are now written:

- the direct-image obstruction is correct under the exact single-valued decoder and equivariance hypotheses;
- the closure obstruction is correct under the stated continuity and lag-pair/diagonal-separation hypothesis;
- the topological countercontrols do the right job of showing why continuity or exactness cannot be silently weakened.

However, I do see several substantial issues that block acceptance in its present form. They are not “the proof is false” issues; they are mostly issues of claim calibration, theorem hierarchy, and source-positioning discipline. For a theorem note whose contribution is mainly scoping and obstruction packaging, those issues are central rather than cosmetic.

## Summary assessment

The manuscript is strongest when it says the following, and only the following:

1. for the graded wheel source with exact level clock \(q_{k+1}\) (or \(\log q_{k+1}\)),
2. an exact single-valued autonomous decoder on a shift-compatible image forces fiber consistency,
3. hence the direct image inherits a strict grading and has no periodic point,
4. and a closure version remains true only after adding a continuous total decoder and a lag-pair separation hypothesis.

That package is mathematically sound and genuinely useful inside this project. It also fits the open branch left by Paper 02.

The manuscript is weaker whenever it drifts from that scoped statement toward “minimality,” “assumption-completeness,” or a novelty posture that is stronger than the actual theorem package supports. Because the central proofs are elementary, the paper lives or dies on exact positioning.

## Strengths

- The direct-image theorem is clean and correct.
- The newly explicit decoder/fiber criterion is the right lemma to surface.
- The factor direction is now mathematically correct and clearly opposite to the strict-extension direction of Paper 02.
- The closure theorem states the right extra hypothesis; continuity alone is correctly shown to be insufficient.
- The compactified-clock countercontrol is well chosen and directly addresses a likely objection.
- The roof vs absolute-clock distinction is basically correct and, importantly, does not try to prove a false “no roofs on periodic systems” statement.
- Route-A / Route-B discipline is mostly respected: no determinant, no spectral claim, no illicit transfer of arithmetic credit.

## Critical issues

I do **not** currently find a Critical issue that invalidates the principal theorem statements.

In particular:

- the Paper-01 wheel proof is sufficient for what is needed here: injectivity and unboundedness of the exact clock;
- the direct-image contradiction is valid;
- the closure proof is valid under the stated hypotheses;
- the compact-target proposition is valid as a compactness-of-image argument;
- the boundary examples really do show failure after deleting the relevant hypotheses.

That said, “no Critical theorem error” does **not** mean the draft is ready. The Major issues below are substantive and should be fixed before the note is treated as a stable shareable paper.

## Major issues

### Major 1 — The manuscript still overstates minimality/sharpness in several places

The current mathematics proves a clean **explicit sufficient criterion** for closure aperiodicity and gives several well-chosen assumption-deletion controls. What it does **not** prove is genuine minimality in the logical sense.

Problematic phrases include, or are close to:

- “minimal clock-topology condition”
- “assumption-complete”
- “sharp topological extension”
- in places, “sharpness” language that can be read as a necessity theorem rather than as a family of countercontrols

Why this matters:

- The closure theorem gives one robust condition:
  \[
  \overline{P_m}\cap \Delta_C=\varnothing.
  \]
  This is sufficient, and sharp against the specific compactification/discontinuity controls shown here.
- But the paper does not classify all topological codomains \(C\), all non-Hausdorff pathologies, all measurable/noncontinuous decoders, or all weaker hypotheses under which periodic boundary points can or cannot occur.
- So “minimal” is too strong unless you prove a converse/necessity theorem, which the manuscript does not.

Required revision:

- Replace “minimal” by “explicit,” “natural,” or “sufficient for the intended clock codomains.”
- Replace “assumption-complete” by something like “assumption-explicit” or “scope-complete for the frozen controls considered here.”
- In Section 5, use “sharp against these controls” rather than language that suggests an optimality theorem over all possible weakenings.

### Major 2 — The compact-target proposition is correct, but its logical status must be demoted and separated more clearly from the periodicity obstruction

The proposition on compact targets is mathematically fine:

- continuous image of compact into \(\mathbb N_{\mathrm{disc}}\) is finite;
- continuous image of compact into \(\mathbb R\) is bounded;
- the full wheel clock range is infinite/unbounded.

But this is **not** a periodic-point theorem. It is a prior feasibility obstruction to carrying the full exact clock continuously on a compact phase space.

At present the paper sometimes presents it too close to the main no-periodic-point theorem, so a fast reader may absorb it as if it were another periodicity obstruction of the same type. It is not.

Why this matters:

- The direct-image theorem is dynamical and uses equivariance plus exact decoding.
- The closure theorem is topological-dynamical and uses continuity plus lag-pair separation.
- The compact-target proposition is only a compactness-of-range argument; once the compact space and continuous decoder exist, no periodicity assumption enters at all.

Required revision:

- Explicitly say, in Section 4 and already in the introduction, that the compact-target proposition is **independent of periodicity** and even of the closure theorem’s diagonal-separation mechanism.
- Reword places where it sounds like “compact targets are ruled out because they would create periodic points.” That is not the logic.
- In the abstract/conclusion, present this proposition as a separate impossibility statement: compact phase spaces cannot continuously carry the full exact wheel clock, period.

### Major 3 — Novelty/prior-art language still needs further tightening

The manuscript has already improved by acknowledging classical coboundary/ordered-cohomology background and by mentioning Heeren 2026. But the novelty positioning still reads too aggressively in places relative to the actual result.

My recommendation is to defend only the following novelty claim:

- not a new universal periodic-coboundary theorem;
- not the first symbolic sieve;
- but a source-specific obstruction package for the frozen wheel clock, together with exact scope controls and project consequences.

What still needs attention:

- phrases such as “exact-clock trichotomy,” “sharp topological extension,” and “assumption-complete wheel-sieve stationarization audit” still sound larger than the proven content;
- Heeren 2026 is prior art close enough that title/version/date metadata should be treated carefully and rechecked before external circulation;
- the paper should avoid any sentence that could be paraphrased as “we are first to symbolically encode sieve nonstationarity” or “we are first to notice the periodic contradiction.”

Required revision:

- Narrow the novelty sentence in abstract/introduction/conclusion to “source-specific obstruction package” or equivalent.
- Keep the classical mechanism explicitly classical.
- Keep Heeren framed as direct symbolic-sieve prior art and this note as a stationarization obstruction for one frozen wheel object.

### Major 4 — The relation to Paper 02 is mathematically consistent, but still not highlighted early enough for readers following the project sequence

Paper 02 studied:

- strict extensions \(Y \to X\),
- strong-bisimulation quotients,
- finite-local decoders,
- and left open the infinite image/recoding branch.

Paper 03 studies the live branch by reversing direction:

- exact image/factor or closure recoding \(X \to Y\).

That is correct. But a reader moving quickly from Paper 02 to Paper 03 can still momentarily feel that the categorical direction has silently changed under the same “stationarization” label.

This is not a proof error; it is a project-consistency communication problem.

Required revision:

- In the first page of the introduction, say explicitly that Paper 03 addresses the **remaining live branch from Paper 02**, namely source-to-target images/closures with exact clock decoding.
- Add one sentence of the form: “Unlike the strict-extension direction treated in Paper 02, the present note studies exact source-to-target images/closures \(X\to Y\).”
- This will prevent readers from confusing “extension obstruction” and “factor/recoding obstruction.”

## Minor issues

### Minor 1 — State more plainly that Proposition 4.3 does not need the dynamics once the continuous exact decoder exists

The current proposition is correct, but one sentence would help:

- “This proposition uses only compactness of \(Y_0\) and continuity of \(d\), not equivariance, periodicity, or the closure theorem.”

That one line would remove a likely misreading.

### Minor 2 — The roof discussion is sound, but one sentence should more explicitly protect ordinary suspension roofs

Section 5.3 is much better than the earlier versions, but I still recommend adding one direct sentence in the manuscript body:

- “We are not proving any obstruction to ordinary positive suspension roofs on periodic base systems; the obstruction concerns inherited pointwise absolute labels \(q_{k+1}\) or \(\log q_{k+1}\) on revisited target states.”

This would make the scope impossible to misread.

### Minor 3 — In the real-clock closure proof, add the final topological conclusion explicitly

You already argue that \(P_m\) is locally finite and has no finite accumulation point. For readability, add the last step explicitly:

- therefore \(P_m\) is closed in \(\mathbb R^2\), or equivalently its closure adds no finite point and in particular misses the diagonal.

This is mathematically routine, but worth spelling out.

### Minor 4 — “compact symbolic target” is slightly too specific

The compact-target proposition does not actually use symbolic structure. “Compact recoded phase space” or simply “compact target space” would be more accurate than “compact symbolic target.”

### Minor 5 — Check the exact bibliographic metadata for Heeren 2026 before public release

The current bib entry is plausible, but SSRN metadata/versioning can shift. Before external sharing, verify:

- exact displayed title,
- exact version date,
- SSRN/DOI pairing,
- whether “SSRN preprint” or “working paper” is the preferred public label.

This is a shareability issue, not a mathematical issue.

### Minor 6 — The figure is conceptually useful, but the caption should keep repeating “same target object”

The figure itself is fine. The caption already helps. I would keep one recurring sentence in the paper text near the figure:

- the arrows classify clock semantics for the same target object;
- they are not a recipe for splicing arithmetic evidence from one branch into periodic data from another.

This is especially important because the note’s central governance claim is “no cross-object credit transfer.”

## Actionable revision checklist

Below is the concrete revision list I would require for the next round.

1. Replace all “minimal” / “assumption-complete” / over-strong sharpness wording by more precise scope language.
2. Reframe the compact-target proposition as a separate compactness-of-range impossibility, not as another periodicity theorem.
3. Tighten novelty language to “source-specific obstruction package,” not a first symbolic sieve / first periodic contradiction / universal theorem claim.
4. On page 1, explicitly contrast Paper-02 strict extensions with Paper-03 source-to-target exact images/closures.
5. Add one explicit sentence safeguarding ordinary suspension roofs from misreading.
6. In the real-clock closure proof, make the final closure/no-diagonal step explicit.
7. Before external sharing, recheck Heeren 2026 metadata and keep the citation phrasing conservative.

## Recommendation on acceptance/shareability

For internal project use:

- mathematically useful now;
- especially useful as a theorem stop for the exact-clock inherited-factor branch.

For external/shareable paper status:

- **not yet ready**;
- not because the main proofs fail, but because the paper’s value lies in exact claim calibration, and that calibration still needs one more pass.

## Final score card

Mathematical correctness: **8/10**

Assumption discipline: **7/10**

Novelty calibration: **5/10**

Project-scope consistency: **7/10**

Shareable-paper readiness: **5/10**

Overall: **6/10**

Final verdict: **REVISE**

## One-line decision

The core obstruction theorems appear correct and useful, but the draft should be revised to reduce overclaim, separate the compactness lemma from the periodicity theorem, and tighten the Paper-02/Paper-03 and Heeren/prior-art positioning before it is treated as a stable shareable note.
