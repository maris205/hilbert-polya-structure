# P32 Devil's Advocate Report — Checkpoint 1

Date: **2026-09-01 UTC**  
Review mode: **independent cross-review of Phase-1 scoping only**  
Reviewed artifacts: `stage1_phase1_rq_brief.md` and
`stage1_phase1_methodology_blueprint.md`

## Verdict: REVISE

The pure-homology tower is carefully separated from P27's residual tower, the
general-content factor exposes a credible falsification path, and the design
does not allow a content-one subproduct to masquerade as the full product.
No Critical issue was found. The declared analytic topology, limit schedule,
and growing-panel order nevertheless contain Major specification errors, so
Checkpoint 1 cannot pass as written.

## Critical issues

No Critical issues identified.

## Major issues

### P32-DA-1 — The declared “compact” analytic sets are not compact

- **Severity:** Major
- **Type:** Method / mathematical definition
- **Location:** Design-freeze registry, “Analytic domain”; P4; interval-grid
  diagnostics.
- **Problem:** `K(delta,T)={Re(s)>=1+delta, |Im(s)|<=T}` is unbounded in the
  positive real direction and therefore is not compact. The blueprint alternates
  between “locally uniform on compact sets” and uniform statements on this
  unbounded half-strip without specifying which norm or theorem is intended.
- **Impact:** The primary analytic endpoint and the required tail bound are not
  well-defined. A proof on each bounded rectangle would not, as currently
  written, establish the stronger unbounded-strip statement.
- **Required revision:** Either define compact rectangles
  `K(delta,T,R)={1+delta <= Re(s) <= R, |Im(s)|<=T}` and quantify over finite
  `R`, or explicitly request uniform convergence on the closed half-strip and
  state the stronger norm and tail estimate. Align the RQ, P4, validity table,
  diagnostic grids, and result fields to one choice.

### P32-DA-2 — A finite schedule is incorrectly called cofinal and cannot carry a limit

- **Severity:** Major
- **Type:** Logic / order of limits
- **Location:** Design-freeze registry, “Tower schedule” and “Limit orders.”
- **Problem:** `N_k=k!`, `k=1,...,8` is a finite diagnostic prefix, not a
  cofinal sequence, and it cannot support `N_k -> infinity`. The same ambiguity
  affects the diagonal statement `m_k=2^k`: the theorem-level infinite index and
  the finite execution index are not separated.
- **Impact:** Numerical completion at `k=8` could be presented as evidence about
  an iterated or diagonal limit that the executed schedule never approaches in
  the mathematical sense.
- **Required revision:** Freeze two distinct objects: theorem schedule
  `N_k=k!` for every `k in N` with `m_k=2^k`, and computational prefix
  `1<=k<=8`. State that computation is a finite consistency certificate only;
  every limit and interchange requires a proof quantified over all sufficiently
  large `k`.

### P32-DA-3 — The canonical growing-panel order is not actually defined

- **Severity:** Major
- **Type:** Sampling / reproducibility
- **Location:** Design-freeze registry, “Equivalence,” “Owner order,” and P1.
- **Problem:** “Canonical surface-group normal-form length, then
  lexicographic order” does not identify a normal-form or conjugacy-reduction
  algorithm for the genus-two one-relator group. Different complete normal
  forms can give different representative lengths and therefore different
  first-`m` panels while satisfying this prose.
- **Impact:** The construction, validation, and stress panels can drift with the
  implementation. Target blindness does not cure an undefined sampling frame,
  and the growing-panel diagnostics cease to be reproducible.
- **Required revision:** Name and specify the exact normal form and conjugacy
  canonicalization, including rewrite rules or a deterministic algorithm,
  orientation/inversion convention, tie-breaking, termination/completeness
  certificate, and serialization. Freeze its test vectors before any panel is
  generated.

### P32-DA-4 — “Coefficientwise in independent owner variables” lacks an ambient formal topology

- **Severity:** Major
- **Type:** Construct validity / mathematical definition
- **Location:** RQ Brief, “Primary topology”; Methodology P3–P4.
- **Problem:** The design invokes a countable collection of independent owner
  variables and says first-coefficient mismatch cannot cancel, but it does not
  define the completed ring, allowed monomials, coefficient projections, or
  directed system of finite panels. The formal result is the primary endpoint,
  not a cosmetic notation choice.
- **Impact:** “Coefficientwise convergence,” “full formal product,” and
  equality across different panel orders have no single frozen meaning.
- **Required revision:** Define the formal algebra explicitly—for example, a
  product topology indexed by finite-support owner monomials—and state the
  embeddings of each finite product, the directed set, and the coefficient
  projections used for equality. Then prove that the first mismatch survives
  in that algebra before scalar specialization.

## Minor issues

### P32-DA-5 — The primary RQ bundles a nearly immediate obstruction with a separate analytic problem

- **Severity:** Minor
- **Type:** Scope / framing
- **Location:** Primary RQ and P3–P4.
- **Problem:** Once a certified `d>1` primitive owner enters the all-owner
  panel, P3 gives a first-coefficient mismatch and the full-product recovery
  claim stops. A locally uniform tail theorem is then relevant only to a
  restricted content-one subproduct, not to rescuing the full product.
- **Recommendation:** State two ordered endpoints explicitly: first, the full-
  owner recovery theorem or finite ownerwise obstruction; second, only if
  scientifically useful after that result, the separately labeled analytic
  convergence of the maximal surviving subproduct. Do not let success in the
  second answer the failed first question.

### P32-DA-6 — Panel-order reversal is not a substantive finite control

- **Severity:** Minor
- **Type:** Control design
- **Location:** Frozen controls.
- **Problem:** Row permutation of a finite commutative product is tautologically
  invariant and does not test rearrangement of an infinite conditionally
  convergent product.
- **Recommendation:** Retain row permutation as a serialization test, but do not
  count it as analytic evidence. Test exhaustion through distinct certified
  cofinal panel families only after absolute convergence is proved.

## Observations and strengths

- The factor calculation is staged before scalar evaluation, which sharply
  limits cancellation-based rationalization.
- The design correctly separates `d=0` and prohibits applying the `d>=1`
  formula by convention.
- Higher-content strata, unnormalized quadrants, neighboring schedules, and
  metric changes are treated as adversarial controls rather than positive
  evidence.
- The A0-absent and Route-B-closed boundaries are explicit.

## Strongest counter-argument

> The proposed “extension” is already defeated as soon as one certified
> higher-content primitive owner appears: its independent-variable factor has
> a different first coefficient, so no growing-panel or local-uniform argument
> can turn the all-owner product into the base product. The analytic program
> therefore risks becoming a sophisticated study of a content-one subproduct
> after the primary full-product question has already failed.

The current kill gate partly acknowledges this argument but the RQ and analytic
work plan still combine the full-product and restricted-subproduct endpoints.

## What's missing

1. A genuinely compact domain definition, or an explicitly stronger
   unbounded-half-strip convergence norm.
2. A clean separation between infinite theorem schedules and finite executed
   diagnostic prefixes.
3. A fully specified surface-group normal form and conjugacy canonicalization
   defining every “first `m`” panel.
4. The ambient completed formal ring/topology and coefficient projections for
   independent owner variables.
5. A proof-level statement that each required `d=0,1,2,3` panel exists to the
   registered size, or a frozen insufficient-population disposition.
6. The exact `d=0` factor and its limit disposition before it is used as a
   global-product stress class.
7. Separate claim names and stopping rules for the all-owner obstruction and
   the content-one analytic subproduct.

## Stress-test results

| Test | Result | Reason |
|---|---|---|
| Remove the three inherited content-one examples—does the algebraic RQ remain answerable? | PASS | The general order/multiplicity theorem is not logically dependent on those examples, although panel feasibility becomes less evidenced. |
| Flip the expected answer—could full base-product recovery fail? | **YES, strongly credible** | One certified `d>1` owner produces the predeclared first-coefficient obstruction. |
| Include a `d=0` owner—does the frozen method already determine its limiting factor? | **FAIL until revised** | The design promises a separate derivation but does not freeze the formula or resulting limit classification. |
| Replace the canonical normal form by another complete normal form—are the finite first-`m` panels unchanged? | **NOT ESTABLISHED** | The owner set is intrinsic, but the registered prefixes depend on the undefined representative order. |
| Run only `k=1,...,8`—does this test `N_k -> infinity`? | **NO** | A finite prefix is not cofinal and cannot validate a limit. |
| Apply the factor theorem to a different marked metric—does the formal mismatch survive? | LIKELY YES, NOT YET PROVED HERE | Homology content is metric-independent, but the claimed scalar/local-uniform specialization still needs the stated proof. |
| “So what?”—is the significance justified? | PASS WITH REFRAMING | A rigorous universal-normalization obstruction is valuable, provided it is not presented as a positive full-product extension. |

## Issue dispositions required for Checkpoint-1 replay

| Issue | Required disposition | Checkpoint effect |
|---|---|---|
| P32-DA-1 | **Must revise:** correct and synchronize the analytic domain and convergence norm. | Blocks PASS while unresolved. |
| P32-DA-2 | **Must revise:** separate infinite theorem schedules from finite execution prefixes. | Blocks PASS while unresolved. |
| P32-DA-3 | **Must revise:** freeze an exact owner canonicalization and panel-order algorithm. | Blocks PASS while unresolved. |
| P32-DA-4 | **Must revise:** define the independent-owner formal algebra/topology and coefficient maps. | Blocks PASS while unresolved. |
| P32-DA-5 | **Should revise:** separate full-product obstruction from content-one analytic convergence. | Minor; does not alone block progression. |
| P32-DA-6 | **Should revise:** relabel row permutation as reproducibility, not analytic evidence. | Minor; does not alone block progression. |

## Checkpoint conclusion

Checkpoint 1 should be replayed after the four Major definitions are repaired.
No Phase-2 source work, computation, bibliography, synthesis, drafting, claim
registration, or Route promotion is authorized by this review.
