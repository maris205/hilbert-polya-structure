# Independent evaluation-boundary consistency review

Date: 2026-09-06. Reviewer: current-team `scout_nonaffine_charp`, not the
author of the batch plan, evaluations, or global registry updates.

Verdict: **PASS_AFTER_TWO_MINOR_CONTROL_CLARIFICATIONS**. Both findings were
corrected by the coordinator and their affected lines rechecked. There is
no remaining source/target consistency blocker in the reviewed artifacts.
This is an internal consistency review, not a new grade, human peer review,
or certification that every future manuscript/release gate has passed.

## Scope and authority actually read

The following four artifacts were read completely:

- `BATCH_PLAN.md` (95 lines at review);
- `EVALUATION_SCOPE.md`;
- `evaluations/route_a/HCS-C407/2026-09-06.yaml` (103 lines);
- `evaluations/route_a/HCS-C408/2026-09-06.yaml` (103 lines).

The full 686-line authority `flow_systems/skills/route-a-evaluator.md`
v0.2.0 was read, together with the complete repository batch skill,
its workflow, and the prior-work guide. The complete flow candidate and
obstruction registries were also read. The authority's pinned hash is
recorded consistently; a repeated hash/schema test is not presented as
this substantive review.

The batch workflow explicitly permits narrow failure-condition reviews
without generating a fresh evaluation or updating registries. Accordingly,
this reviewer did not independently repeat the six background-PDF routing
performed by the coordinator. `EVALUATION_SCOPE.md` describes that as a
bounded read of PDF pages 1–3, not a full-proof audit, and this review does
not upgrade it. In particular, the prior-work guide's paper-6 claim is not
used here as an established external theorem.

Relevant theorem evidence was compared as follows: C407's full proof and
primary-source boundaries were independently reviewed earlier in
`wild_ordinary/CROSS_REVIEW_ARITHMETIC_TOPOLOGY.md`; for C408 this narrow
review read its exact object and theorem sections, generating-function
section, and the complete coordinator's `ROOT_CLUSTER_REVIEW.md`, rather
than claiming a second full audit of every local-algebra calculation.
The new top sections of both Hénon registries were additionally inspected.
No evaluator, evaluation, registry, theorem file, or old payload was edited
by this reviewer. Only this new review file was written.

## 1. The route tuples remain exact and conservative

| Candidate | Tuple in YAML, scope record, and new registry | Overall |
|---|---|---|
| C407 | `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` | `ROUTE_A_EXPLORATORY`, source-local |
| C408 | `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` | `ROUTE_A_REJECTED` as a target candidate |

The prose agrees with these labels. C407's exact primitive counting input
does not become a target A1 pass: no prime-to-primitive correspondence,
uniform stability convention, or target phase/amplitude transport is
provided. C408's all-period thickness formula is not treated as a primitive
orbit ledger at all. Its A1 failure survives mathematical admission.

`PROVED` in an A0/A1 evidence-status field refers to the stated source
evidence or proved mismatch, not to a passed target gate. The neighboring
strongest-failure fields, explicit scope fields, tuples and overall verdicts
make this distinction clear. Both candidates have A2/A3/A4 failure labels;
no implied upgrade is hidden in a source rationality or topology statement.

## 2. Exact objects, clocks, and generating-function conventions

C407 keeps the same object throughout: a genuinely realized positive-entropy
hyperbolic FAD system, with a fixed finite distortion-prime set, positive
periodic coefficient, nonnegative real finite exponent types, and exponent
periods coprime to their own prime. Abstract admissible detector data are
not silently asserted to be realized dynamical systems. Time is the native
integer iterate, and `pi_f(N)` counts primitive orbits of length at most N.
The normalization is exactly `N*pi_f(N)/Lambda^N`.

Its new observable is the complete real accumulation set, not a determinant
or a source zero divisor. The explicitly named classical Artin–Mazur zeta
is an input convention only. Neither the polylogarithmic covering estimate
nor the Cantor conclusion introduces rational-prime periods or a target
analytic continuation. Classical detector asymptotics, one-prime topology,
negative-integer slicing, and fixed-count realizations are deducted.

C408 consistently retains the unsaturated finite cyclic relation algebra
over C, for all odd `k>=3` and native relation lengths `n=2m`. Local Artin
length is distinguished from ordinary cardinality and from a rotation/orbit
quotient. The two alternating phases are both counted. Dividing-period
support is not renamed exact-period support.

The native-clock conversion can be checked directly, independently of the
geometric proof. In the logarithm of

`Z_k(u^2)^((k+1)/2) * Z_k(-u^2)^((k-1)/2)`,

the coefficient of `u^(2m)` is

`ell_m/m * [(k+1)/2 + (k-1)(-1)^m/2]`.

This equals `b_(2m)/(2m)` for the frozen values `b_(2m)=2ell_m` when m is
odd and `b_(2m)=2k ell_m` when m is even. Thus the two series conventions
are compatible and do not silently replace relation time by orbit time.
Both are explicitly refused an Artin–Mazur interpretation.

The embedding-dimension obstruction is used with the correct restricted
claim: for `m>=3`, this local algebra cannot be a fixed subscheme of a
smooth surface. It is not a theorem that every different saturation,
boundary model or dynamical extension is impossible. A torus-map lift is
not imported into the frozen nonreduced observable.

## 3. Controls, missing tests, and scope flags

Both A0 panels explicitly remain `INCOMPLETE`. The neighboring-family
theorems and simpler-parent comparisons are not relabeled as a completed
three-category random/arithmetic panel. No target data split is fabricated:
the absence of training, validation, and sealed-test regions is stated.
All nine required A2 metrics per candidate, eighteen total, are
`NOT_TESTABLE`, not numerical zero or passed measurements.

All nine target/Route-B scope flags per candidate, eighteen total, are
false. The explicit `route_b_invocation_allowed` fields are also false.
No claimed target Euler factor, root number, automorphy, functional
equation, divisor/counting law, zero match, or Hilbert–Pólya operator was
found elsewhere in the four reviewed artifacts.

The C407 own-prime-period counterexample is correctly classified as an
outside-hypothesis control. It does not refute the admitted theorem. Its
broad family conclusion cannot select a unique arithmetic target. The
C408 six original-equation checks are bounded controls, while the stopped
`k=3,m=4` computation is explicitly not PASS. Neither finite set is used
as a proof of the all-parameter theorem.

`STOP_SCOPED` is attached to an invalid inference from source evidence to
the target. The record explicitly says that no Davenport–Heilbronn or
other target adversarial-function panel ran. Thus it does not manufacture
an experimental failure or a universal impossibility result.

### Closed findings

1. **Control category mismatch, MINOR.** Original C407 YAML line 30 explained
   unrun `shuffled_primes` using replacement of primes by composites. These
   are different controls; prime shuffling does not turn primes into
   composites. The coordinator replaced this with the literal statement
   that no prime-label shuffle comparison was run or claimed. Affected
   line reread: **CLOSED**. Evidence anchor: `text`, C407 A0 controls.
   Confidence: 5/5, direct category comparison with evaluator A0.
2. **A1 control inventory omission, MINOR.** The initial combined field in
   each YAML named random weights/phases/periods but did not explicitly
   name same-density random lengths. Both now use the field
   `shuffled_periods_random_weights_random_phases_same_density_lengths`
   and explicitly say all four were unrun and not credited as passes.
   Affected fields reread: **CLOSED**. Evidence anchor: `text`, both A1
   metrics and evaluator's mandatory A1 controls. Confidence: 5/5,
   direct inventory comparison. No grade changed during the correction.

## 4. Publication, future-work, and batch-completion boundaries

The mathematical admission is expressly independent of the target route
verdict. The BATCH_PLAN freezes five contracts but says that the two new
manuscripts and their review/build/release gates are unfinished. It does
not claim five completed PDFs at this stage, count the unnumbered wild
note as an extra paper, or start C409. The old three-paper package is
reused without reopening its frozen payload or repeating accepted checks.

C407's novelty wording is source-local to the checked BCH 2024 v2. The
unobtained final EMS book version and absence of worldwide priority
certification remain visible. No nonhyperbolic classification, detector
injectivity, or atomless Haar pushforward is inferred. C408 keeps all
other zero supports, even k, and total torus counts outside its contract;
known deep-point support is not counted as its new theorem.

The YAML `next_smallest_test` fields are future obligations, not successful
tests or authorization to execute them now. C407 requires an intrinsic
prime-to-primitive correspondence for a fixed realization before a target
fit. C408 requires a new scheme comparison before any dynamical boundary
interpretation; that cannot mean asserting an isomorphism already ruled
out by the stated embedding-dimension obstruction. Neither instruction
authorizes Route B, external uploading, or another paper in this batch.

The new top Hénon registry entries match the reviewed tuples and
manuscript-in-progress status. The old vacant-slot sections are explicitly
marked as earlier superseded checkpoint statements, so their preserved
wording does not contradict the current admission. The cited new proof,
evaluation, scope, plan, and review targets were present among the artifacts
read in this check; no global link-census claim is made.

## Final disposition

All two requested control clarifications are closed. No remaining
inconsistent target promotion, missing-clock splice, unreported passed
control, or premature five-paper completion claim was found. Continue the
already authorized manuscript/review/release work with the current tuples
unchanged. This review is not a substitute for the pending full manuscript
comparison, final build verification, visual inspection, or sealed release
integrity checks.
