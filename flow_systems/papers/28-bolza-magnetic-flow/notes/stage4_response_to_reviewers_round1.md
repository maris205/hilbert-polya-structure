# Paper 28 Stage 4 response to reviewers — Round 1

Date: **2026-08-30**

Status: **4 RESOLVED; 0 DELIBERATE LIMITATION; 0 UNRESOLVABLE; 0 DISAGREED**

## REV-01

**Reviewer comment.** Correct the manuscript's replay sequence so that it matches the audited builder and retains the validation and explicit-refresh gates.

**Response.** The emitted revision has corrected the sequence: proof guards and finite traversal/reconstruction run first in fresh temporary directories; build_validation then checks the freeze, upstream source locks, source matrix, theorem fields, and output bindings. It has retained verify-only temporary-to-canonical comparison and has stated that canonical files can change only after validation passes and through the explicit refresh path.

**Location.** The emitted patch has replaced anchored block B0099 in the subsection “Independent replay obligations.”

**Anchored blocks.** `B0099`

**Status.** `RESOLVED`

## REV-02

**Reviewer comment.** Localize direct regression coverage for the canonicalization invariants and state the same-builder assurance boundary accurately.

**Response.** The emitted revision has reported the executed direct tests for two consecutive Delta-factor cancellations, global-negation normalization idempotence, all four generator/inverse products in both orders, and sampled canonical-state collisions. It has also disclosed that the tests import the audited certificate builder and do not independently reimplement the eight-transition closure checker, so no independent-closure claim has been made.

**Location.** The emitted patch has replaced anchored block B0048 in the subsection “Canonicalization invariants.”

**Anchored blocks.** `B0048`

**Status.** `RESOLVED`

## REV-03

**Reviewer comment.** Supply a compact non-ranking A0–A4 legend and consolidate the unexecuted downstream obligation chain without promoting the Route record.

**Response.** The emitted revision has defined the A0–A4 obligations, retained the formal full P28 tuple as unassigned, and retained the historical proxy (A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL) without update or promotion. It has classified the exact control systole and target-blind cutoff as A0–A1 infrastructure only, identified 144 solely as equality-achieving group elements, and recorded the matched census, owner quotienting, magnetic and signed-field work, A2, determinant and analytic-continuation work, A3/A4 and spectral work, and Route B as not run.

**Location.** The emitted patch has inserted the obligation legend immediately after anchored block B0106 in “Adversarial checks and Route-A interpretation.”

**Anchored blocks.** `B0106`, `B0126`

**Status.** `RESOLVED`

## REV-04

**Reviewer comment.** Provide a field-general typed map that separates the present geodesic outputs from every unconstructed magnetic, owner, determinant, analytic, and spectral object.

**Response.** The emitted revision has mapped the fixed control surface, exact PSU(1,1) group-element state, and target-blind cutoff to geodesic translation length and the retained cutoff. It has separately typed the magnetic Hamiltonian/flow, clock/action, owner quotient and multiplicities, determinant weights, analytic continuation, and spectral realization as unconstructed inputs, constructions, or proofs, and it has drawn no A2, A3, A4, or Route-B conclusion.

**Location.** The emitted patch has inserted the typed interface immediately after anchored block B0037 in “Related exact-computation setting and claim boundary.”

**Anchored blocks.** `B0037`, `B0125`

**Status.** `RESOLVED`

## Round summary

- Resolved: 4
- Deliberate limitations: 0
- Unresolvable: 0
- Reviewer disagreements: 0
- Canonical word-count delta: +386
- New bibliography entries: 0

The emitted revision has corrected the replay sequence, documented the executed same-builder direct invariant tests and their independence boundary, added a non-ranking A0–A4 obligation legend, and added a field-general typed interface. It has preserved the unassigned full P28 tuple, the unpromoted historical proxy, the element-level meaning of 144 equality states, the unchanged canonical results, and the Route-A/Route-B scope firewall.

New-content highlights:

- Canonicalization invariants: executed direct-test coverage and same-builder assurance boundary
- Adversarial checks and Route-A interpretation: non-ranking A0–A4 obligation legend
- Related exact-computation setting and claim boundary: field-general typed interface
