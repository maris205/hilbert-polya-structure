# P32 Stage-1 Phase-1 Research Question Brief

Date: **2026-09-01 UTC**  
Mode: **ARS Deep Research / FULL / Phase 1 only**  
Status: **REVISED PHASE-1 DESIGN — pending independent Checkpoint-1 replay**

## Topic area

Growing-panel limits for the separately registered pure homology-cover
calibrator of P27, with the inherited `1/N` clock and `1/N^3` logarithmic
multiplicity normalization held fixed.

## Primary research question

Does the paired frozen `1/N` clock and `1/N^3` logarithmic-normalization scheme recover the base primitive-owner factor for every owner under a certified target-blind exhaustion of the pure genus-two homology-cover calibrator?

“Recover” is an ownerwise universal endpoint, tested first in a defined formal
algebra. A single certified higher- or zero-content mismatch closes that
endpoint as `FULL_RECOVERY_OBSTRUCTED_OWNERWISE`. Analytic convergence of a
content-one subproduct is a separate secondary endpoint and cannot answer the
primary RQ after a full-owner obstruction. Neither endpoint can rescue P27's
residual inverse-limit flow.

## FINER assessment

| Criterion | Score | Phase-1 justification |
|---|---:|---|
| Feasible | 4/5 | The lift order and multiplicity are exact functions of the homology content; a complete growing owner enumeration and analytic tail bound are the hard components and have explicit kill gates. |
| Interesting | 5/5 | P27 proved exact recovery on every fixed content-one panel but explicitly left panel growth and the global product open. |
| Novel | **3/5 — PROVISIONAL** | No Phase-2 literature search has run. This is a project-defined gap, not a priority or novelty claim. |
| Ethical | 5/5 | The work is theoretical and computational mathematics with no human subjects or personal data. |
| Relevant | 5/5 | The question tests the exact boundary between finite A1 calibration and any A2-like global claim and supplies a mandatory proves-too-much control. |
| **Average** | **4.4/5 — PROVISIONAL** | The average includes an explicitly provisional novelty placeholder. |

## Frozen operational definitions

- **Candidate:** only `H_N=ker(Gamma -> H_1(Sigma;Z/NZ))` for a marked closed
  genus-two surface and its unit-speed geodesic flow; this tower is
  nonresidual and is not P27's residual inverse-limit owner.
- **Owner:** an oriented primitive conjugacy class of the marked surface group.
- **Homology content:** for vector `v(g) in Z^4`,
  `d(g)=gcd(|v_1|,...,|v_4|)`; `d=0` is a separate null-homology stress class.
- **Surface-group frame:**
  `Gamma=<a1,b1,a2,b2 | [a1,b1][a2,b2]=1>` with alphabet order
  `a1<a1^-1<b1<b1^-1<a2<a2^-1<b2<b2^-1`; inversion remains a separate
  orientation.
- **Canonicalization interface:** `SG2OwnerCanonical-v1` must supply a complete
  equality normal form, oriented conjugacy canonical representative,
  primitive-root certificate, deterministic serialization, and certified
  prefix enumerator. Its theorem/implementation binding is currently
  **UNBOUND**. Until all correctness, termination, completeness, and prefix
  certificates are bound, every requested panel is `PANEL_NOT_EVALUABLE`.
- **Panel:** after that interface closes, order owners by canonical word length
  and the frozen alphabet lexicographic tie-break; theorem families
  `P_m^all` and `P_m^(d)` are defined for every integer `m>=1`. The fixed
  finite diagnostics use `m in {8,16,32,64,128}` plus diagonal-prefix values
  `m_k=2^k` for `1<=k<=8`. Failure to certify `m` eligible owners gives
  `INSUFFICIENT_CERTIFIED_POPULATION(d,m)` with no padding or adaptive order.
- **Normalization:** physical lifted time multiplied by exactly `1/N`; raw
  lift-component log product multiplied by exactly `1/N^3`.
- **Primary formal topology:** for positive-content owner set `O_+`, use
  `R=lim_(F,D) Q[u_g:g in F]/(u_g:g in F)^(D+1)`, where `F` ranges over finite
  owner subsets, outside variables map to zero, and `D` is total-degree
  truncation. Equality means equality under every finite-support coefficient
  projection. For content `d(g)>=1`, scalar specialization is
  `u_g=exp(-s ell(g)/d(g))` on finite panels; an infinite specialization is
  undefined until absolute tail convergence is proved.
- **Analytic topology:** local uniform convergence on `Re(s)>1` means uniform
  convergence on every genuine compact rectangle
  `K(delta,T,R)={1+delta<=Re(s)<=R, |Im(s)|<=T}`, quantified over
  `delta>0`, finite `T>=0`, and finite `R>=1+delta`.
- **Two schedules:** the theorem-level cofinal sequence is `N_k=k!` and
  diagonal `m_k=2^k` for every integer `k>=1`; the future executable prefix is
  only `1<=k<=8` and is a finite consistency certificate, never limit evidence.

## Scope boundaries

### In scope

- The pure homology tower, deck degree `N^4`, exact owner orders, primitive
  lift counts, and the four inherited clock/multiplicity quadrants.
- Target-blind growing panels of exact primitive owners, separated by homology
  content `d=0`, `d=1`, `d=2`, `d=3`, and an all-owner prefix.
- The infinite theorem schedule `N_k=k!`, `m_k=2^k` for all `k>=1`, the
  separately labeled finite execution prefix `1<=k<=8`, the frozen
  simultaneous normalization, exact owner-factor coefficients, and
  predeclared iterated and diagonal limit orders.
- Higher-content owner controls and asymmetric marked-metric controls; the
  structural claim must remain valid or fail without arithmetic labels.
- First, a universal full-owner recovery theorem, a finite ownerwise
  obstruction, or a fail-closed not-evaluable status; second and separately,
  a possible content-one subproduct theorem on the compact-rectangle domain.

### Out of scope

- Any mutation of P27's residual tower, common physical clock, aperiodicity
  theorem, or Route tuple.
- Content-dependent clocks, content-dependent multiplicity normalization,
  owner weights, or outcome-fitted panels; these define different candidates.
- Declaring the content-one subproduct to be the full primitive spectrum.
- A rational-prime map, Riemann-zero comparison, target divisor, transfer
  operator, analytic continuation outside a proved domain, or Route B.
- Phase-2 bibliography, synthesis, manuscript drafting, scientific execution,
  or novelty claims in this file.

### Key assumptions to test rather than promote

- A theorem-backed implementation can satisfy every field of the
  `SG2OwnerCanonical-v1` fail-closed interface and certify each requested
  prefix. This is tested rather than assumed.
- A summable primitive-owner tail bound is available on the declared analytic
  domain; otherwise only the formal ownerwise result may be reported.
- Each required `d=0,1,2,3` stratum contains enough owners for every registered
  panel size. Failure yields the frozen insufficient-population status rather
  than substitution or a smaller post-outcome panel.
- Metric specialization does not erase an ownerwise mismatch; this requires a
  proof, not a favorable numerical grid.

## Sub-questions

1. What exact order, lift multiplicity, rescaled period, and renormalized owner factor follow from each homology content, including the separately typed `d=0` case, for every modulus `N`?
2. Does the full-owner formal endpoint recover every base factor, or which certified owner supplies the first frozen ownerwise obstruction or not-evaluable gate?
3. Independently of the full-owner verdict, does the certified content-one subproduct converge locally uniformly on every `K(delta,T,R)` under theorem-level infinite schedules rather than their finite execution prefix?

## Sub-question bindings (#547)

1. **Inherits:** group = marked genus-two surface group; tower = pure
   `H_N`; owner = oriented primitive class; clock = hyperbolic arclength;
   normalization = `1/N` and `1/N^3`; target data = forbidden.
   **Deviations:** none.
2. **Inherits:** all bindings of Sub-question 1; panels = certified canonical
   content strata and all-owner prefixes; owner variables = independent in the
   declared inverse-limit ring; controls = higher/zero content and marked
   metrics. **Deviations:** none.
3. **Inherits:** all bindings of Sub-questions 1--2; theorem schedule =
   `N_k=k!`, `m_k=2^k` for all `k>=1`; finite prefix = `k<=8` and never limit
   evidence; analytic domain = every finite `K(delta,T,R)`; analytic claim =
   content-one only and requires absolute tail control. **Deviations:** none.

## Candidate questions considered

| # | Candidate | FINER average | Disposition |
|---:|---|---:|---|
| 1 | Does the paired frozen `1/N` clock and `1/N^3` logarithmic-normalization scheme recover the base primitive-owner factor for every owner under a certified target-blind exhaustion of the pure genus-two homology-cover calibrator? | **4.4/5, Novel=PROVISIONAL** | **Selected:** tests universal ownerwise recovery first, without letting a restricted analytic subproduct replace that endpoint. |
| 2 | Does the content-one subproduct alone converge locally uniformly? | 4.0/5, Novel=PROVISIONAL | Secondary only: even a positive answer would omit higher-content primitive owners and could not be called a full product. |
| 3 | Can content-dependent clock and multiplicity factors recover every homology-content stratum? | 3.6/5, Novel=PROVISIONAL | Deferred: it changes the frozen normalization and creates a new candidate. |
| 4 | Can the positive homology-cover identity restore periodic points to the residual inverse limit? | 2.2/5, Novel=PROVISIONAL | Rejected: the owners, tower, clock, and quantified objects differ; P27's residual conclusion is immutable. |

## Route boundary

A0 remains absent because the construction and every planned theorem/control
are independent of rational-prime arithmetic and apply across marked metrics.
A successful formal or analytic calculation cannot rescue the residual owner,
cannot automatically receive A2, and cannot open Route B.

## Phase boundary

This file is an RQ Brief only. It contains no bibliography, synthesis, draft,
scientific result, claim registration, or Route evaluation.
