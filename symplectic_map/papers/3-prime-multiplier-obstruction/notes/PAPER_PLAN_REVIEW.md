# PAPER_PLAN Review

Verdict: `MINOR`

Review date: 2026-08-13

Scope reviewed:

- `PAPER_PLAN.md`
- `experiments/source_lock.json`
- `experiments/EXPERIMENT_PLAN.md`
- `experiments/EXPERIMENT_TRACKER.md`
- all paper-local notes in `notes/`
- all frozen result artifacts in `results/` relevant to theorem scope, controls, conjugacy, bridge scope, provenance, and validation

## Executive summary

The plan is scientifically aligned with the frozen evidence package.

I found no mismatch on the core items the manuscript must get right:

- the all-period theorem, rather than the `n<=4` cutoff, carries the raw-prime result;
- the open boundary `|lambda|=p^n` with `p=2`, `n>=2` is preserved correctly as `OPEN`;
- the cotangent construction is kept branchwise/local and is not inflated into a global symplectic theorem;
- the controls genuinely show both positive detections and assumption failure;
- the no-external-prime/no-zero/no-floating-recognition boundary is supported by the frozen protocol artifacts.

The remaining issues are editorial-structural rather than mathematical blockers. They are fixable before drafting and do not require rerunning code or changing results.

## What is already solid

### 1. The theorem/result boundary is clean

`PAPER_PLAN.md` consistently places the all-period force on the divisibility theorem and uses the finite computations only as implementation audits. This matches:

- `notes/PROOF_PACKAGE.md`
- `results/proof_audit.json`
- `results/negative_result_ledger.json`
- `results/EXPERIMENT_RESULTS.md`

In particular, the plan never closes the rational `p=2` exponent-prime residue by cutoff evidence, which is exactly the correct frozen boundary.

### 2. The candidate-specific claims match the exact audits

The Section 4/5 storyline is consistent with:

- `results/candidate_multiplier_audit.json`
- `results/exact_polynomials.json`
- `results/conjugacy_audit.json`

The exact low-period ledger in the plan matches the executed certificates:

- period 1: `L^2-2L-4u`, no rational roots
- period 2: `L-4+4u`, no rational roots
- period 3: `L^2+(-16+8u)L-64+64u`, no rational roots
- period 4: `L^3+(-48+16u^2)L^2+(256+256u^2)L+4096`, no rational roots

### 3. The controls are genuinely diagnostic

The controls section is supported by `results/control_audit.json` and is not cosmetic:

- `z^2` recovers the theorem-compatible `2^n` clock;
- `z^2-2` recovers the Chebyshev boundary and fixed raw-prime residue;
- `z^2-3/4` detects the odd raw prime `3` exactly when the algebraic-integer hypothesis is removed.

This is enough to support the plan’s claim that the pipeline is not an always-negative detector.

### 4. The cotangent bridge scope is correctly narrow

Section 6 and the global nonclaim language match `results/symplectic_bridge_audit.json`:

- exact one-form pullback on `q!=0`;
- reciprocal return pair on the zero section;
- explicit failure of globality at `q=0`;
- overlapping branch images;
- noncompactness;
- no reciprocal lift for critical zero-multiplier cycles.

### 5. Novelty positioning is fundamentally on the right scale

The current positioning as a narrow certificate/no-go note is appropriate. Primary-source spot checks support the main collision boundaries:

- Huguin 2021: unicritical maps with only rational multipliers are power/Chebyshev (`arXiv:2009.02422`; AMS publication `10.1090/ecgd/359`)
- Huguin 2022: quadratic rational maps with integer multipliers (`10.1007/s00209-022-03076-7`)
- Huguin 2023: maps whose multipliers all lie in a number field are power/Chebyshev/Lattès (`10.5802/jep.227`)
- Murakami–Sano–Takehira 2024/2025: integrality theorems for multiplier polynomials in unicritical-type families (`arXiv:2403.17315`)
- Ji–Xie 2023: multiplier/length-spectrum rigidity (`10.1017/fmp.2023.12`)
- Ji–Xie–Zhang 2026: infinite-dimensional `Q`-span of characteristic exponents for nonexceptional rational maps (`10.1007/s00208-026-03361-4`)
- Fogedby–Jensen 2005 and Demaeyer–Gaspard 2009: classical 2D/weak-noise symplectic extensions of 1D maps (`10.1007/s10955-005-5457-z`, `10.1103/PhysRevE.80.031147`)

So the plan’s “not a new general multiplier theory / not a new symplectic construction” stance is the right one.

## Required revisions before drafting

### R1. Make “rational” impossible to miss in the title/hero language

Status: required wording fix

Why:

The body is careful, but the working title still says “Raw Prime Multipliers” rather than “Raw Rational-Prime Multipliers.” Given how central the modulus-only nonclaim is, the title and Figure 1 language should not allow a reader to misparse the result as a modulus theorem over complex multipliers.

Where:

- `PAPER_PLAN.md:3-10`
- `PAPER_PLAN.md:157`
- `PAPER_PLAN.md:185-187`

Action:

- Either change the title to include `rational`, or define “raw prime multiplier” in the title-adjacent subtitle/first sentence of the abstract.
- In Figure 1 panel (b), label the open boundary as the “rational `p=2` exponent-prime gate,” not just the “base-2 exponent gate.”

### R2. Promote the exact-period contamination control from implicit to explicit

Status: required evidence-packaging fix

Why:

The strongest exact-period control is not only that `z^2-3/4` finds the raw prime `3`, but also that its formal period-2 component is completely removed by saturation, leaving exact period degree `0`. This is the clearest audit that the manuscript truly distinguishes formal from exact period.

Where:

- `PAPER_PLAN.md:114-121`
- `PAPER_PLAN.md:158`

Evidence:

- `results/control_audit.json` shows formal period contamination at `c=-3/4`, period 2, with removed factor degrees `[1,1]`, exact period degree `0`, and resultant degree `0`.

Action:

- In Table 2, explicitly add one row or one note for the `c=-3/4`, period-2 saturation/removal event.
- In Figure 2, show the contamination-removal marker, not just the raw-prime `3` hit.

### R3. Add the conjugacy-audit artifact wherever “independent duplication” is claimed

Status: required provenance fix

Why:

The plan often says the result is duplicated independently in `f_u` and `g`, which is true, but the explicit frozen artifact for that claim is `results/conjugacy_audit.json`. Right now the claim matrix and figure/table sources undername that artifact.

Where:

- `PAPER_PLAN.md:25`
- `PAPER_PLAN.md:120`
- optionally `PAPER_PLAN.md:158-160`

Action:

- Cite `results/conjugacy_audit.json` directly in C4 and in any figure/table caption that mentions coordinate duplication.
- Keep `results/exact_polynomials.json` for the displayed polynomials, but do not make it carry the duplication claim by implication.

### R4. Repair the sign convention in the novelty-boundary source that feeds Table 3

Status: required citation-logic fix

Why:

The plan itself uses the correct fixed-point residue `u=0` or `u=2`, but the underlying novelty note currently says the map has parameter neither `0` nor `-2`. For `g(z)=z^2-u`, the exceptional quadratic-family boundary should be written consistently as either:

- `u != 0, 2` in the `z^2-u` parameterization, or
- `c=-u != 0, -2` in the `z^2+c` parameterization.

Where:

- `notes/NOVELTY_AUDIT.md:89-92`
- downstream impact on `PAPER_PLAN.md:162`

Action:

- Correct the parameter convention in the novelty note before using it as the source for Table 3.
- In the manuscript, say explicitly which parameterization is in force when invoking the nonexceptional boundary.

### R5. Do not carry `Wang (2026)` into the draft without a concrete verified record

Status: required bibliography hygiene fix

Why:

The citation plan says “Wang (2026) for genealogy,” but no exact bibliographic identity for that entry appears in the audited local materials I reviewed. Because the plan itself forbids memory-synthesized BibTeX, this item needs to be either concretely verified or dropped.

Where:

- `PAPER_PLAN.md:170-180`

Action:

- Either add the exact publisher/DOI/arXiv-verified bibliographic record for `Wang (2026)`, or replace the sentence with an uncited genealogy statement that does not require that reference.
- Treat Berry–Keating the same way: keep only if the motivation sentence remains narrowly historical and non-claiming.

### R6. Tighten the Section 6 reciprocal-spectrum sentence to the audited domain

Status: recommended precision fix

Why:

The bridge audit proves the reciprocal pair on the zero section for periodic orbits avoiding `q=0`. The plan is close, but the domain restriction should sit in the same sentence as the claim.

Where:

- `PAPER_PLAN.md:126-130`

Action:

- Phrase the claim as: “for zero-section periodic orbits contained in the regular locus `q!=0`, the return derivative has spectrum `(lambda, lambda^{-1})`.”

## Pass/fail on the requested review axes

| Axis | Decision | Notes |
|---|---|---|
| Main theorem range | PASS | All-period raw-rational-prime obstruction is consistently theorem-driven. |
| Open boundary, especially `|lambda|=p^n` with `p=2`, `n>=2` | PASS | Preserved correctly as `OPEN` throughout plan and frozen results. |
| Cotangent bridge scope | PASS with wording tweak | Scientifically correct; add the regular-locus condition inline. |
| Controls | PASS with packaging tweak | Strong evidence; promote the formal/exact-period contamination control visually. |
| Citations / novelty positioning | MINOR | Positioning is sound, but one parameter-sign bug in the source note and one unresolved genealogy citation must be fixed. |
| Figure/table plan | MINOR | Good overall; add the conjugacy artifact and the contamination-removal witness explicitly. |
| Consistency with frozen results | PASS | No material overclaim found. |

## Bottom line

Recommendation: proceed to drafting after the six revisions above.

This is not a case where the theorem/result boundary or the evidence chain needs redesign. The plan is already strong on mathematical scope and frozen-result discipline. The remaining work is to remove small but avoidable ambiguity at the title/figure/citation layer before those ambiguities propagate into the manuscript.
