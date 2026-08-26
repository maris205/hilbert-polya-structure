# Paper improvement log

## Round 0

- Constructed the modular `amsart` manuscript and proof package.
- Proved the local SFT rule, rooted gauge count, cover topology, exact fixed
  spectra, moment inversion, and `D_8/Q_8` corollary.
- Added a source/ownership citation audit and exact finite controls.
- Frozen as `main_round0_original.pdf`.

## Round 1 internal hostile audit

- Re-derived every exponent and the left-coset convention.
- Clarified that the subgroup families are divisibility-directed rather than
  linearly nested in consecutive indices.
- Removed an unnecessary minimality phrase from the conclusion.
- Shortened a code filename to remove the only overfull box.
- Recompiled and repeated citation, font, metadata, text, and visual checks.

## Round 2 typesetting and source-role audit

- Removed six literal commas that had entered mathematical exponents in the
  abstract, theorem statements, and classical surface formulas.
- Added a source-level `rg '\^\{,'` gate because LaTeX compilation does not
  diagnose this class of semantic typo.
- Recast Klug consistently as the modern source/account used for normalization;
  classical ownership remains with Mednykh and Frobenius--Schur.
- Recompiled and regenerated extracted-text and visual QA artifacts.

## Official GPT-5.4/xhigh Round 1 — author resolution

- Preserved the pre-review manuscript as main_pre_gpt54_round1.pdf and the
  revised manuscript as main_gpt54_round1.pdf.
- Extended the known-base moment lemma to consecutive nonnegative indices,
  explicitly including \(m_0=0\). Theorem 5.2 now distinguishes recovery of
  \(b_d=(c_d^+-c_d^-)/d\) from the subsequent multiplication by known \(d\).
- Added an exact \(C_3\) zero-indicator control with signature \([1,0,0]\),
  direct/formula count comparisons, and reconstruction
  \((c_1^+,c_1^-,c_1^0)=(1,0,2)\).
- Replaced the former probe terminology with “families” or
  “divisibility-directed families” throughout author-facing manuscript and
  package material.
- Sharpened the source-role language: Klug is the chosen modern normalization
  source/account, while ownership of the classical formulas remains
  historical.
- Reran the exact controls, complete four-command build, source gates,
  font/metadata checks, extracted-text checks, and visual inspection.
- Recorded the full author response in
  rounds/GPT54_XHIGH_ROUND1_RESOLUTION.md. The supplied review contained no
  numerical score, and none has been inferred.

## Official GPT-5.4/xhigh Round 2 — proof audit and package sync

- Preserved the full official audit at
  `reviews/GPT54_XHIGH_ROUND2_PROOF_AUDIT.md`; it supplied no numerical score.
- Recorded the reviewer's core-mathematics verdict as **PASS**. The supplied
  audit found no critical or major mathematical defect and requested no
  manuscript theorem/proof change.
- Resolved its one package-synchronization finding by replacing the remaining
  Chinese false-nesting terminology in `BILINGUAL_ABSTRACT.md` with `子群族`
  and `非定向族`.
- Regenerated `qa/final_text.txt` and the legacy mirror
  `qa/final_text.new.txt` from the current PDF, eliminating stale terminology.
- Added `DECLARATIONS.md` so the package-level declaration claim is literal;
  it withholds authorship, specialist, priority, submission, and release
  authorization.
- Reran the exact controls and the complete deterministic four-command build.
  Because manuscript source did not change, the Round-2 PDF remains
  byte-identical to the Round-1 mathematical PDF.
- Frozen the current manuscript as `main_gpt54_round2.pdf`, regenerated
  current text/PDF/font/control/visual receipts, recorded comprehensive state
  in `PAPER_IMPROVEMENT_STATE.json`, and regenerated `SHA256SUMS`.
- Recorded the author response in
  `rounds/GPT54_XHIGH_ROUND2_RESOLUTION.md`.

## Final posture

- Official Round-2 core mathematics: **PASS**.
- Package-wide Round-2 compliance after synchronization and author replay:
  **PASS**.
- Stage 2.5 specialist/collision review: **PENDING**.
- External-release verdict: **HOLD -- specialist, priority, authorship, and
  release clearance have not been granted**.
- No priority claim is authorized.
