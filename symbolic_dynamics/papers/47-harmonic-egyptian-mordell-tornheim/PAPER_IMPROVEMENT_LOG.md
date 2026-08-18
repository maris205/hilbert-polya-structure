# P47 paper improvement log

## Review progression

| Manuscript state | Independent review | Findings | Disposition |
|---|---|---:|---|
| Round 0 original | GPT-5.4 xhigh Round 1 | C0 / M2 / m3 | `ROUND1_FIX` |
| After Round 1 fixes | GPT-5.4 xhigh Round 2, same thread | C0 / M0 / m0 | `ROUND2_READY` |
| Round 2 review-ready state | post-review build and writer QA | zero automated QA defect | superseded after independent visual HOLD |
| Visual-HOLD repair | writer-side deterministic rebuild and full QA | repaired; fresh independent recheck required | `HOLD_FOR_INDEPENDENT_WRITER_AUDIT` |

No numerical score is invented: the independent reviewer reported severity
counts and dispositions rather than a score.

## Round 1 raw review

<details>
<summary>GPT-5.4 xhigh Round 1 review (verbatim)</summary>

1. Verdict

The core analytic package looks sound on this pass: I did not find a proof-breaking gap in the bounded/compact wall, the sharp `S_2` and `S_1` thresholds, the ordered-edge evaluation of `\Tr(E_s^2)`, the complex-factorization firewall, or the mixed-cycle/sign witnesses. The manuscript is also unusually disciplined about separating analytic proof from finite replay and provenance.

However, I found two statement-level determinant inaccuracies that must be fixed before acceptance: one in the abstract’s coefficient claim, and one in the main corollary’s overlap formula as rendered in the PDF. So my round-1 verdict is fix-required, not accept.

2. Strengths

- The two-coordinate architecture is coherent and well used: the divisor-row coordinate drives boundedness/compactness, while the coprime-scale coordinate drives ideal sums and traces.
- The endpoint obstructions are sharp and appropriately distinct: squarefree row degree at `\Re s=0`, loop-square divergence at `\Re s=1/2`, and diagonal obstruction at `\Re s=1`.
- The complex-parameter firewall is handled carefully and correctly: the text explicitly denies unitary conjugacy and refuses to transfer spectra/traces/determinants through the left-right factorization.
- The second-trace calculation is presented in the correct ordered-edge convention, with the no-factor-two point made explicitly.
- The provenance layer is well fenced off from theorem ownership. `CLAIMS_EVIDENCE.md`, `SOURCE_VERIFICATION.md`, and `CANONICAL_RESULTS_LEDGER.md` are aligned with the manuscript’s no-finite-inference / no-priority posture.
- The figure/table semantics are mostly clean and match the theorem statements rather than overreaching beyond them.

3. Numbered CRITICAL issues

None on this round. I did not find a core theorem/proof failure that would force rejection of the analytic claims themselves.

4. Numbered MAJOR issues

1. Abstract misstates the determinant coefficient.

   In `abstract.tex:20-22`, the sentence says that the displayed second trace “is the quadratic coefficient of the local logarithm of the regularized determinant.” That is mathematically false as written. The coefficient is
   `-[\Tr(E_s^2)]/2`, not `\Tr(E_s^2)` itself.

   This conflicts with the correct formula in `sections/06_traces_determinants.tex:103-107` and with the appendix permission table in `appendices/C_determinants_walks.tex:22-25`.

2. Main corollary prints the trace-class overlap formula incorrectly.

   In `sections/06_traces_determinants.tex:114-115`, the overlap identity is typeset as
   `\exp\!\bigl(z,2^{-s}\zeta(s)\bigr)`,
   which is not the claimed formula and renders incorrectly in the built PDF as `exp z, 2^{-s}\zeta(s)`.

   The correct statement is
   `\exp\!\bigl(z\,2^{-s}\zeta(s)\bigr)` or, better, `\exp\!\bigl(z\Tr(E_s)\bigr)`.
   This is a statement-level mathematical error in a key corollary, even though the surrounding domain bookkeeping is otherwise right. It also conflicts with the correct generic formula in `appendices/C_determinants_walks.tex:12-15`.

5. Numbered MINOR issues

1. Supporting-plan drift on determinant normalization.

   `PAPER_PLAN.md:97-103` repeats the same coefficient drift: it says the quadratic coefficient is “exactly the displayed Mordell--Tornheim trace,” whereas the coefficient is `-\Tr(E_s^2)/2`. Since this plan is part of the reviewed candidate bundle, it should be synchronized with the actual corollary.

2. Abstract row-coordinate sentence is under-specified.

   In `abstract.tex:8-10`, the row coordinate is stated as `n=m^2/d-m` without explicitly saying `d\mid m^2` and `d<m`. The body supplies this later, but the abstract version is currently too compressed and can be misread as an unrestricted substitution formula.

3. Introduction’s sign/positivity sentence should pin the real domain more explicitly.

   In `sections/01_introduction.tex:62-66`, the negative determinant witness is invoked without explicitly saying “for real `s>1`,” whereas Section 7 states the restriction correctly in `sections/07_cycles_sign.tex:35-53`. The intro should match that precision when drawing the positivity conclusion.

6. Exact actionable fixes with file/line anchors

1. Fix the abstract coefficient claim at `abstract.tex:20-22`.

   Recommended replacement idea:
   “Consequently, on `\Re s>1/2`,
   ` [z^2]\log\det_2(I-zE_s) = -\frac12 \Tr(E_s^2) `,
   so the displayed Mordell--Tornheim series gives the quadratic trace term.”

2. Fix the overlap formula at `sections/06_traces_determinants.tex:114-115`.

   Replace
   `\exp\!\bigl(z,2^{-s}\zeta(s)\bigr)`
   by either
   `\exp\!\bigl(z\,2^{-s}\zeta(s)\bigr)`
   or
   `\exp\!\bigl(z\Tr(E_s)\bigr)`.
   Then confirm that the rendered PDF no longer shows the malformed comma expression.

3. Sync the plan doc with the corrected determinant normalization at `PAPER_PLAN.md:97-103`.

   In particular, change the “quadratic coefficient” sentence to the exact `-\Tr(E_s^2)/2` normalization, and keep the overlap formula in the same corrected form as the manuscript corollary.

4. Tighten the abstract row-coordinate statement at `abstract.tex:8-10`.

   Add the missing conditions `d\mid m^2` and `d<m`, e.g.:
   “for fixed `m`, neighbors are parametrized by divisors `d\mid m^2`, `d<m`, via `n=m^2/d-m`.”

5. Tighten the introduction’s positivity witness at `sections/01_introduction.tex:62-66`.

   Make the real-domain restriction explicit, e.g.:
   “for real `s>1`, the `{3,6}` principal block has determinant `-18^{-s}`; hence in the real trace-class regime the operator need not be positive semidefinite.”

7. Explicit checks for forbidden errors

- Unitary-conjugacy claim: PASS.
  Correctly denied at `sections/03_graph_coordinates.tex:153-159` and `appendices/B_operator_details.tex:41-44`.

- Factor-two error in the ordered-edge second trace: PASS.
  Correctly handled at `sections/06_traces_determinants.tex:51-61`; no extra factor is inserted because `(a,b)` is already ordered.

- Ordinary determinant used in the Hilbert--Schmidt-only strip: PASS.
  Domain bookkeeping is correct at `sections/06_traces_determinants.tex:91-117,130-133` and `appendices/C_determinants_walks.tex:16-29`.
  The issue I flagged is a formula typo in the overlap identity, not a domain overreach.

- Finite-to-infinite inference: PASS.
  The firewall is explicit and repeated at `sections/08_replay_limitations.tex:17-22`, `appendices/D_canonical_replay.tex:28-33`, and `CLAIMS_EVIDENCE.md:18-25,46-60`.

- Priority/novelty overclaim: PASS.
  Ownership boundaries are handled carefully at `sections/02_related_work.tex:22-46` and `evidence/SOURCE_VERIFICATION.md:62-80`.

- PSD / nonreal-Hermitian overclaim: PASS.
  Correctly limited at `sections/07_cycles_sign.tex:49-53`; the text does not claim nonreal Hermiticity or import positivity through the left-right factorization.

- All-`S_p` / functional-equation / Hilbert--Pólya overclaim: PASS.
  Explicitly avoided at `sections/08_replay_limitations.tex:32-38`, `CLAIMS_EVIDENCE.md:46-60`, and `PAPER_PLAN.md:27-31`.

Counts: C0 / M2 / m3
ROUND1_FIX

</details>

### Fixes implemented after Round 1

1. Corrected the abstract normalization to
   `[z^2] log det_2(I-zE_s) = -Tr(E_s^2)/2`.
2. Replaced the malformed overlap exponent with
   `det_2(I-zE_s)=det(I-zE_s) exp(z Tr(E_s))`.
3. Added the exact divisor conditions `d|m^2`, `d<m` to the abstract.
4. Restricted the introductory negative-minor conclusion to real `s>1` and
   the real trace-class regime.
5. Synchronized the reviewed paper plan with the `-1/2` determinant
   normalization.

The warning-free Round-1 PDF has SHA-256
`5837f352495e0688bc1b0785a031c8cc04f01f5a811adb5332e04cfeb4abc087`.

## Round 2 raw review

<details>
<summary>GPT-5.4 xhigh Round 2 review (verbatim; same reviewer thread)</summary>

1. Verdict

All five Round-1 items are fixed in the live source, and the rendered `main.pdf` reflects the substantive corrections. On a fresh full pass over the current manuscript, plan, evidence docs, figures/tables, bibliography, and rendered PDF, I do not find any remaining critical or major issue. The analytic theorem package, the determinant-domain bookkeeping, the complex-factorization firewall, the ordered-edge conventions, and the finite-replay provenance separation are internally consistent on this pass.

2. Verified fixes

1. Abstract row-coordinate restriction fixed.

   Source check:
   - `abstract.tex:8-11` now states the fixed-row parametrization with the missing conditions `d\mid m^2`, `d<m`.

   Rendered-PDF check:
   - `main.pdf` text extraction, abstract lines 9-11, now reads that the neighbors in each fixed row are parametrized by `d | m^2`, `d < m`, through `n = m^2/d - m`.

2. Abstract determinant normalization fixed.

   Source check:
   - `abstract.tex:21-23` now states
     `[z^2]\log\det_2(I-zE_s)=-\Tr(E_s^2)/2` locally.

   Rendered-PDF check:
   - `main.pdf` text extraction, abstract lines 20-21, shows the corrected `-[Tr(E_s^2)]/2` normalization.

3. Overlap formula fixed in the main determinant corollary.

   Source check:
   - `sections/06_traces_determinants.tex:109-117` now gives
     `D_2(z;s)=D_1(z;s)\exp\!\bigl(z\Tr(E_s)\bigr)`.

   Rendered-PDF check:
   - `main.pdf` text extraction around the corollary, lines 704-715, no longer shows the old malformed comma expression; it now reflects the corrected overlap formula with `exp ... Tr(E_s)`.

4. Paper plan synchronized with the `-1/2` quadratic normalization.

   Source check:
   - `PAPER_PLAN.md:101-104` now states that the quadratic coefficient is `-Tr(E_s^2)/2`, i.e. minus one half of the displayed Mordell--Tornheim trace, and the overlap formula is synchronized.

5. Introduction positivity/sign restriction tightened.

   Source check:
   - `sections/01_introduction.tex:62-67` now pins the negative-minor argument to real `s>1` and explicitly says “in the real trace-class regime”.

   Rendered-PDF check:
   - `main.pdf` text extraction, introduction lines 107-108, reflects the corrected real-domain wording and the positive-semidefinite conclusion in the proper regime.

Additional build-status check:
- `main_round1.pdf` SHA-256 matches the supplied hash:
  `5837f352495e0688bc1b0785a031c8cc04f01f5a811adb5332e04cfeb4abc087`.
- `main.pdf` has the same SHA-256.
- Final `main.log` is clean: no unresolved-reference, citation, or LaTeX-warning hits on my grep pass.

3. Strengths

- The paper remains mathematically disciplined about legal domains:
  bounded/compact only for `\Re s>0`, `S_2` only for `\Re s>1/2`, and ordinary Fredholm determinants only for `\Re s>1`.
- The proof architecture is strong and still reads coherently:
  divisor-row coordinates handle boundedness/compactness, while coprime-scale coordinates handle ideal sums and traces.
- The complex-phase discussion is now both correct and consistently fenced:
  left-right unitary multiplication is used only for singular-value data, never for spectral or trace transfer.
- The trace/determinant normalization is now consistent across abstract, body, appendix, and plan.
- The finite replay layer is kept cleanly subordinate to analytic proof and does not leak into endpoint or novelty claims.
- The bibliography and ownership boundaries remain appropriately narrow and cautious.

4. Numbered CRITICAL issues

None.

5. Numbered MAJOR issues

None.

6. Numbered MINOR issues

None on this pass.

7. Actionable fixes

No required fixes remain from my review pass.

If you want optional polish only, the remaining work would be purely editorial/copyediting rather than mathematical or domain-correctness repair.

8. Explicit forbidden-error checks

- Unitary-conjugacy claim: PASS.
  `sections/03_graph_coordinates.tex:153-159` and `appendices/B_operator_details.tex:41-44` still correctly state that the factorization is not unitary conjugacy and does not transfer spectrum, powers, traces, positivity, or determinants.

- Factor-two error in the ordered-edge second trace: PASS.
  `sections/06_traces_determinants.tex:51-61` still explicitly uses ordered edges and correctly states that no extra factor two appears.

- Determinant domains and normalizations: PASS.
  `sections/06_traces_determinants.tex:91-117` and `appendices/C_determinants_walks.tex:5-29` now align correctly on:
  - `\det_2` legal on `\Re s>1/2`,
  - ordinary `\det` legal on `\Re s>1`,
  - local log series starting at `r=2` for `\det_2`,
  - overlap identity `\det_2(I-zE_s)=\det(I-zE_s)e^{z\Tr(E_s)}`,
  - quadratic coefficient `-[\Tr(E_s^2)]/2`.

- Finite-to-infinite inference: PASS.
  The firewall remains explicit in `sections/08_replay_limitations.tex:17-30`, `appendices/D_canonical_replay.tex:28-33`, and `CLAIMS_EVIDENCE.md:18-25,46-60`.

- Priority / novelty overclaim: PASS.
  The ownership boundary remains appropriately narrow in `sections/02_related_work.tex:22-46` and `evidence/SOURCE_VERIFICATION.md:62-80`; I do not see a priority overclaim.

- PSD / nonreal-Hermitian overclaim: PASS.
  `sections/07_cycles_sign.tex:35-53` correctly restricts the negative-minor positivity conclusion to real `s>1` and does not claim nonreal Hermiticity or imported self-adjointness.

- All-`S_p` / functional-equation / Hilbert--Pólya overclaim: PASS.
  The manuscript still explicitly disclaims those extensions in `sections/08_replay_limitations.tex:32-38`, `CLAIMS_EVIDENCE.md:46-60`, and `PAPER_PLAN.md:27-31`.

Counts: C0 / M0 / m0

ROUND2_READY

</details>

### Post-Round-2 build repair

Text-extraction QA found 13 illegal C0 characters in the Round-1 PDF, all
emitted by extensible mathematical delimiter glyphs.  Replacing the affected
delimiters with fixed parentheses changed no formula, theorem, domain, or
evidence claim.  Default, layout, and raw extraction now each contain zero
illegal C0/DEL/C1 and zero replacement characters.

Two clean fixed-epoch builds reproduced the final PDF, bibliography, and
compile log byte for byte.  All 14 A4 pages passed individual visual
inspection; 29/29 fonts are embedded, subsetted, and Unicode mapped; both
bbox modes contain zero out-of-page word boxes.  Full details are in
`evidence/PDF_QA.md`.

### Independent visual-HOLD repair

The independent writer audit rejected the earlier Round-2 rendering because
the three thick domain bands in Figure 2 crossed their labels, while the
strict-endpoint note collided with the ticks and the negative-domain label.
That rendering and its seal are permanently withdrawn:

- withdrawn PDF SHA-256:
  `bb30f866ecac88b8b5467dadecef968daa60dc9383af46eea0e7e5602a794eb0`;
- withdrawn writer-seal SHA-256:
  `cfb71220d7838d92345d9df70d47e6f2d669607a794cf1f2ee78b7a07f81f5b0`.

The repaired vector figure places each label above its corresponding band
and moves the strict-endpoint explanation into an independent white callout
to the right of the axis.  The open endpoints, thresholds
`0, 1/2, 1`, band extents, color encoding, and negative-domain statement are
unchanged.  The repaired Figure-2 source has SHA-256 `1da86f01205cb0ea57af2a7dc47bcb5993e1e3374229237cf7464fe320904c52`.
The resulting paper has again undergone fixed-epoch A/B reproduction plus
full writer-side text, font, bounding-box, and per-page visual QA.  These are
writer checks, not a substitute for the required fresh independent audit.

## Artifact hashes

- Round 0 original PDF: `3cab9e5f273b584d8759c5b7a88ed8f145046c6402bb651d94d01c21331eeb53`;
- Round 1 PDF: `5837f352495e0688bc1b0785a031c8cc04f01f5a811adb5332e04cfeb4abc087`;
- final `main.pdf` / Round 2 PDF: `b6c4d6aa27fe23f74b4c9e63628cd9b34b83d1d4d0908b040cc923af4c0ae12d`;
- final bibliography: `dd828b408bbe3bb486a8d8ea7fc8794d9c6759ac564176befae50dadf5a235dc`;
- final compile log: `23cf89d34d194a01ff9a4c3bcd3611670099f7286bccc121c336dbf89e7973d2`;
- PDF QA record: `e761980bddd67519af3bc6da2e120c088c435a32871b00abe50f11f38b4b8cc1`;
- repaired Figure-2 source: `1da86f01205cb0ea57af2a7dc47bcb5993e1e3374229237cf7464fe320904c52`.
