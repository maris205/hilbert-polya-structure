# Paper 30 — Stage 1 Phase 5 independent Devil's Advocate, Checkpoint 3

Date: **2026-09-02 UTC**  
Seat: **`R10-P5-DA`**  
Checkpoint: **3 — complete Phase-4 report**  
Verdict: **`REVISE`**

## Review lock and independence

This review is bound to the exact report
`stage1_phase4_research_report.md` at SHA-256
`44c76c5f8ac9c4f61d662295920a1e76aaedf21aa8fba6ba4e7616448061485a`
and its claim-intent manifest at SHA-256
`53a684425d8a15d90838fbbb331a73ea619e4efa764d71bf4811a7d0c68f620f`.
The governing Phase-5 review contract is SHA-256
`9e848c5f07a357bc4d4691687813379ac0db15875b40337f9a4df9d61193ece7`.

The seat reviewed frozen inputs only and remained blind to all other Phase-5
findings. It performed no retrieval, roof construction, determinant
evaluation, numerical run, report edit, manuscript edit, or roadmap
evaluation. The review uses the current Codex model family. Separation is
procedural, not proof of statistically independent errors; this is a
single-family, **`NOT_CALIBRATED`** review with no numerical reviewer score.

## Strength retained under attack

The report's strongest reasoning survives: internal Euler/trace/determinant
agreement is typed to one roof and cannot establish physical fidelity. The
quantum, semiclassical, and classical determinant firewall is also explicit
and appropriately conservative.

## Critical findings

No Critical finding was identified.

## Major findings

### `P30-DA-001` — the proposed “total” error contract is not shown to be exhaustive or additively composable

- **Severity:** Major.
- **Type:** Method; warrant gap; McNamara-style risk from an incomplete error
  ledger.
- **Exact report evidence:** Section 2.1 requires a geometry-based pointwise
  roof rather than fitted periodic totals. Section 2.4 states
  `E_total = E_orbit_tail(N) + E_rank(R) + E_quadrature + E_roundoff` after
  emphasizing that orbit and projected-operator representations are
  differently typed and lack an automatic coefficient map. Section 4.3 calls
  this a complete four-part error obligation, and Sections 6–8 treat its
  closure as one of six ordered gates.
- **Finding:** A coefficient correspondence does not by itself prove that four
  heterogeneous bounds live in the same norm, propagate through the same
  determinant map, or add without conditioning factors. More importantly, a
  numerically constructed geometry-derived pointwise roof can carry an input
  or model-enclosure error whose effect on the transfer operator and
  determinant is not one of the four displayed terms unless it is explicitly
  absorbed and stability-controlled. The report calls the equation “total”
  while leaving both exhaustiveness and propagation as unstated premises.
- **Impact:** A future calculation could satisfy all four named budgets and
  still fail to bound the determinant of the intended physical roof. Because
  the paper's contribution is the architecture itself, an under-specified
  central error gate is a Major report-level weakness even though no numerical
  claim has yet been made.

## Minor findings

No separate Minor finding was identified.

## Observations

### `P30-DA-002` — fixed Route failure does not erase nonarithmetic dynamics value

- **Severity:** Observation.
- **Exact report evidence:** Sections 4.4 and 8 keep
  `A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION` fixed while allowing a
  future typed physical determinant infrastructure result.
- **Finding:** This boundary is correct. It also means the paper's “so what?”
  must be judged as a classical-dynamics and validated-computation program,
  not by Hilbert–Pólya progress.

## Strongest steel-manned counterargument

> A determinant computed from an approximate pointwise flight roof can have
> small orbit-tail, projection, quadrature, and roundoff errors and still be
> far from the determinant of the exact physical roof if the operator is
> sensitive to roof perturbations. Until the report names a common norm and a
> stability mechanism that propagates geometry/roof uncertainty, the four
> terms are an inventory, not a complete certificate.

This counterargument accepts the report's type firewall and roof-agnostic
calibration result. It attacks the sufficiency of the proposed numerical
warrant, not the existence of the general research program.

## Missing evidence and perspectives

- a common norm or metric in which every displayed error term is bounded;
- a stability or conditioning statement connecting pointwise roof error to
  transfer-operator and determinant error;
- a demonstration that geometry/input, coding-boundary, and model-selection
  uncertainty are either absent or covered by named terms;
- a lawful propagation rule showing when the four bounds are additive rather
  than coupled; and
- an adversarial ill-conditioned example showing that the contract fails
  closed instead of certifying a misleading small total.

## Four stress tests

| Stress test | Qualified categorical outcome | Reason |
|---|---|---|
| Remove the strongest source | **CORE DESIGN SURVIVES; CERTIFICATE WEAKENS** | The roof-agnostic identity is distributed across the corpus, but removing the closest open-billiard or determinant theorem further weakens applicability and does not solve error composability. |
| Flip the research question | **UNIT-ROOF ALTERNATIVE PARTLY CREDIBLE** | A unit roof removes physical geometry error, yet rank, trace, quadrature, and conditioning still require one normed propagation argument; the objection narrows but remains. |
| Apply to a different context | **GENERALIZATION RISK HIGH** | Different billiards and function spaces can change regularity, conditioning, and approximation modes, so the four-term ledger cannot migrate by label. |
| Ask “so what?” | **SIGNIFICANCE JUSTIFIED BUT CONDITIONAL** | Separating calibration from physical specificity matters, but a future validated determinant depends on closing the error-warrant gap rather than merely populating four fields. |

## Frame-lock check

**`FRAME_LOCK_FOUND`**: the architecture assumes that the four named numerical
terms are exhaustive and can be summed after a coefficient map is supplied.
That is a substantive mathematical premise, not bookkeeping. The report
correctly says the terms are unproved, but it does not yet expose the possible
missing roof/input perturbation or nonlinear conditioning layer.

## Report-versus-science boundary

The finding concerns completeness of a proposed validation architecture. It
does not construct a roof, select a function space, evaluate a determinant,
assert an omitted error is nonzero, or change any scientific endpoint. All
P30 execution fields remain `NOT_RUN` or `NOT_EVALUATED`.

## Route boundary

Route A remains frozen at the report's nonpromotional boundary; no formal
tuple is assigned, positive arithmetic A2 remains zero, and Route B remains
closed. The roadmap hashes remain
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
and `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.
`REVISE` is solely a report-readiness verdict.

