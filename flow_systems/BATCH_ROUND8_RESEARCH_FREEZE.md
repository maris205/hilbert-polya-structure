# Round 8 research freeze — Papers 24--28

Date: **2026-08-28**

## Workflow and route boundary

- ARS position: **Stage 1 / RESEARCH**, full-mode theorem and exact-computation
  continuation.  This file is the Phase-1 design freeze for Round 8; it is not
  authorization to enter Stage 2.
- Roadmap: `skills/route-a-evaluator.md` controls A0--A4.  Route B is not
  invoked, because no positive rational-prime candidate has reached
  `ROUTE_A_SUCCESS_ROUTE_B_READY`.
- Outcome-neutrality: a proved obstruction, a full exact classification, a
  valid negative control, and a positive certificate are all acceptable.  A
  larger finite sample without a new theorem or certificate is not.
- Forbidden inputs: rational-prime tables, Riemann-zero tables, target-zero
  fitting, post-test clock changes, and transfer of Route credit between
  differently owned objects.
- Common acceptance contract: every paper must add a theorem or precisely
  bounded certificate, a frozen machine-readable contract, deterministic
  outputs, tests, a two-build reproducibility check, a paper-facing research
  spine, and a new append-only Route-A record.

## Research-question brief

| Paper | Primary Round-8 question | Route-A interface | FINER (F/I/N/E/R) |
|---|---|---|---|
| P24 | Is the normalized trace discriminant `D_m` specific to the Gaussian level-3 owner, or is it a generic principal-congruence identity that survives three source-independent controls? | A0 specificity and proves-too-much gate; A1 owner separation | `5/5/4/5/5` |
| P25 | Can the unit-roof `q`-symbol determinant be transferred to the physical three-disk clock by one scalar time substitution preserving primitive words and repetitions? | Typed A1--A2 ownership firewall; physical A2 remains separate | `5/5/4/5/5` |
| P26 | What is the exact, mutually exclusive kernel type of every one of the 138 frozen cycle-owner instances and all 55 grouped quadratic-moment cases? | A1 exact owner/weight classification; A2 is not inferred | `5/5/5/5/5` |
| P27 | After registering a new clock and normalization, which of the four time/multiplicity-renormalization choices preserves a fixed primitive-owner panel along the genus-2 homology tower? | New-owner A0 proves-too-much control and A1 finite-panel theorem | `5/5/5/5/5` |
| P28 | Does the source-verified nonarithmetic genus-2 control admit a rigorous systole/lower-bound or finite word-to-length completeness certificate strong enough to authorize a predeclared common cutoff? | A1 completeness gate before any matched census; A0 controls remain mandatory | `3/5/5/5/5` |

All averages exceed `3.0`, and no FINER component is below `2`.  P28 has the
lowest feasibility score because a finite word enumeration is not a
completeness proof without a geometric stopping certificate.

## Scope bindings and hypotheses

### P24 — congruence specificity

- In scope: matrices `gamma=I+mA` with determinant one, the Round-7 marked
  Gaussian ledger, a simpler parent, a neighboring level/parameter, and a
  non-Gaussian arithmetic ring.
- Bold hypothesis: integrality of `(tr(gamma)^2-4)/m^2` follows from the
  determinant equation over a broad class of rings and therefore proves too
  much by itself.
- Required significant result: a general algebraic theorem plus three executed
  controls; the first congruence jet may be added only with its exact
  conjugacy/inversion law and residual-collision count.
- Out of scope: promoting a finite marked-word invariant to the full Bianchi
  flow or claiming a rational-prime owner.

### P25 — roof nontransfer

- In scope: the frozen equilateral three-disk billiard at `d/a=5.8,6.0,6.2`,
  its exact period-2 and period-3 symmetric orbits, and the separately typed
  unit-roof no-repeat shift.
- Bold hypothesis: two exact periodic averages already obstruct a constant
  roof coboundary and every global substitution `z=exp(-c s)`.
- Required significant result: a theorem-level ownership firewall, supported
  by a full frozen-ledger replay but not inferred from floating-point data.
- Out of scope: an exact physical multiple-scattering determinant computation,
  a Gutzwiller--Voros equality, or transfer of the symbolic A2 verdict.

### P26 — complete exact taxonomy

- In scope: every frozen Round-4/Round-6 cycle-owner instance, exact homology
  and modular-symbol coefficient maps, and all declared Hecke laws.
- Bold hypothesis: all numerical survivors and failures admit an exact kernel
  explanation, with no floating artifact or unresolved row.
- Required significant result: a complete mutually exclusive taxonomy and an
  equivalence theorem between the classifier and the quadratic-moment residual.
- Out of scope: a global Euler product, determinant, or target-zero comparison.

### P27 — registered collective renormalization

- In scope: the closed genus-2 homology cover
  `H_N=ker(Gamma -> H_1(Sigma;Z/NZ))`, primitive-content-one homology owners,
  the inherited hyperbolic clock, the explicitly new `1/N` clock, and the
  explicitly new geometric-mean multiplicity normalization.
- Bold hypothesis: time rescaling alone and multiplicity normalization alone
  each fail in a different way, whereas applying both returns the base
  finite-panel Euler factor exactly at every level.
- Required significant result: the four-case theorem with exact order,
  lift-multiplicity, support, and coefficient-prefix ledgers.
- Out of scope: relabeling this generic finite-panel calibrator as the original
  residual inverse-limit owner, or claiming a full-flow determinant.

### P28 — common-cutoff authorization

- In scope: the Round-7 source-locked `SU(1,1)` generators and presentation,
  rigorous hyperbolic geometry, interval/exact arithmetic, and source-verified
  completeness facts.
- Bold hypothesis: an axis/fundamental-domain displacement bound can turn a
  finite word search into a rigorous short-geodesic certificate.
- Required significant result: either a valid cutoff-authorizing certificate,
  or a new quantitative theorem proving exactly which missing bound prevents
  authorization.  Merely reporting a larger word search is insufficient.
- Out of scope: freezing a common cutoff first and justifying it afterward.

## Methodology blueprint

- Paradigm: mathematical/positivist; claims are separated into `PROVED`,
  `NUMERICALLY_CERTIFIED`, `NUMERICAL_OBSERVATION`, `OPEN`, and
  `NOT_TESTABLE` exactly as required by Route A.
- Method: theorem derivation, exact integer/algebraic computation, locked-input
  replay, and adversarial controls.  External literature is used only for
  named source facts and is independently verified.
- Data strategy: repository-frozen ledgers and source packages only.  New
  outputs are append-only and hash-bound.  No human subjects are involved.
- Analysis order: freeze object/owner/clock/normalization; prove the governing
  identity; build the deterministic replay; run controls; then assign the
  Route tuple.  The tuple is never selected from an attractive output.
- Validity: exact formulas dominate finite replays; every finite completeness
  claim needs a stopping theorem; primitive and repeated owners remain
  separate; signed/complex cancellations are preserved; independent review
  attacks owner transfer, proves-too-much behavior, hashes, and test counts.
- Reporting: mathematical research note plus reproducibility receipt; no
  preregistration platform is required for this theoretical/exact-computation
  round.  This freeze serves as the repository-local prespecification.

## Devil's-advocate checkpoint 1

Verdict: **PASS WITH NONBLOCKING WARNINGS**.

- Critical issues: none.
- Major issue prevented by design: P28 may not promote bounded word enumeration
  to completeness without a stopping certificate.
- Minor issue: P24/P25/P27 are likely to strengthen negative or generic-control
  conclusions rather than produce a positive arithmetic candidate.  This is a
  legitimate result, but the paper title and Route tuple must say so directly.
- Strongest counter-argument: five internally related negative-control papers
  could be mistaken for one result split into fragments.  Round 8 answers this
  by requiring five different theorem types: congruence universality, roof
  cohomology obstruction, full kernel taxonomy, renormalization quadrant, and
  geometric completeness.
- Frame-lock check: the round does not assume that progress means Route
  promotion; exact closure of a tempting but invalid bridge counts as progress.
