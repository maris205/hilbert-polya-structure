# Experiment Plan: Additive Finite Arithmetic-Capacity Certificate

**Candidate:** `additive_finite_arithmetic_capacity_v2`  
**Plan version:** 2  
**Date:** 2026-08-14  
**Execution mode:** exact symbolic/static audit only; formal candidate run
requires a passing independent code review

## Decision target

Certify or reject the implication

$$
\forall p\in\mathcal P_{\rm hit},\quad
\log p=v_p+\log q_p+\alpha_p
\quad\Longrightarrow\quad
\#\mathcal P_{\rm hit}
\le \dim_{\mathbb Q}V+|S_{\mathbb Q}|,
$$

under the source-locked hypotheses that $V$ has finite rational dimension,
$S_{\mathbb Q}$ is fixed and finite, $q_p>0$ is algebraic with
$q_p^2$ an $S_{\mathbb Q}$-unit, and $\alpha_p$ is real algebraic.

This is a proof-dependency, exact-control, and provenance audit.  It must not
enumerate prime targets, read a prime table, read Riemann-zero data, solve for
candidate matches, or use floating tolerance.

## Claims and falsifiers

| ID | Claim | Required exact evidence | Falsifier |
|---|---|---|---|
| C001 | The additive canonical form is closed under finite rational sums, differences, repetitions, and rational scales of in-scope L/M terms, and algebraic sums of A terms. | Structured closure ledger; positive-root finite-extension argument for M. | An allowed operation not reducible to $(v,\log q,\alpha)$, or an excluded irrational multiplier-log coefficient silently admitted. |
| C002 | $S_{\mathbb Q}$-unit status is invariant under finite field extension and inversion. | Valuation identity at places above the base field. | A finite extension creating a nonzero valuation above a previously good rational prime. |
| C003 | Outside $S_{\mathbb Q}$, chosen $v_p$ terms for distinct hits are rationally independent. | Denominator clearing, $\log R=\beta$, Hermite--Lindemann, squaring, and one-place-per-prime valuation isolation. | A nonzero relation satisfying every declared hypothesis. |
| C004 | The total distinct-prime capacity is at most `dim_Q(V)+cardinality(S_Q)`. | Linear-independence count plus the finite inside-support count. | More outside hits than `dim_Q(V)` or more distinct inside primes than the fixed support contains. |
| C005 | The selector/union theorem is only a corollary. | Explicit embeddings $(\ell_L,1,0)$, $(0,|\lambda|,0)$, and $(0,1,\mathcal A)$. | Treating selector union logic as the proof of C003. |
| L001 | Fixed finite memory contributes to one finite-rank $V$. | Higher-block recoding certificate. | A purported finite-memory observable requiring infinitely many block edges. |
| M001 | Good-reduction Hénon modulus squares have fixed support. | Separate-degree homogenization, projective-affine dimension lemma, maximum argument, unit monodromy, normal saturated extension. | A certified outside-place nonzero valuation satisfying every hypothesis. |
| A001 | Allowed A-readouts and algebraic endpoint shifts are real algebraic; compatibility is separately required for canonical gauge invariance. | Safe evaluation and gauge ledger. | Conflating algebraicity with endpoint cancellation, or admitting log-after-action. |
| E001 | Escape gates are necessary failures of this certificate only. | Explicit nonclaim classifier. | Language asserting completeness, mutual exclusivity, sufficiency, or a universal no-go. |

## Run order and gates

### M0: source-lock and pre-execution provenance

1. Validate JSON and SHA-256 for version 2.
2. Verify the historical version-1 hash and independent-review hash.
3. Verify that the independent report predates all Paper-5 implementation and
   that every data/execution counter at both locks is zero.

### M1: implementation authoring and noncandidate tests

Implement a small standard-library package that:

- encodes proof dependencies as structured identifiers rather than accepting
  mathematical prose as machine proof;
- audits canonical-form closure and all declared exclusions;
- performs exact rational arithmetic for boundary controls;
- scans every executable Python module for networking, process execution,
  numeric logarithms, floating literals/tolerance, dynamic import, target-data
  arrays, and unreviewed data-file reads; and
- emits no theorem classification unless the deployment gate passes.

Syntax compilation and isolated unit tests are permitted before review because
they are development checks, not the registered formal audit.  They may use
formal labels and the frozen exact boundary constant `2`; they may not compute
candidate target sets or write official result artifacts.

### M2: independent code review (mandatory before formal audit)

The reviewer receives the source lock, proof package, code, and tests.  The
review must independently check:

1. fail-closed source-lock/hash validation;
2. structured proof-dependency IDs and no phrase-based proof acceptance;
3. correct treatment of rational coefficients, negative powers, $q=1$,
   repeated hits, and one representation per distinct prime;
4. complete repair closure for the ten independent-review items;
5. scanner self-coverage and absence of network/prime/zero/tolerance paths;
6. controls that demonstrate scope without being promoted to candidate data;
7. a fail-closed formal-run authority marker; and
8. no universal-no-go, trichotomy, historical-first, or Route-B output label.

Any critical or major issue returns the implementation to M1.  A passing
review must write the exact machine authority specified by the protocol.

### M3: controls-first registered exact audit

Only after M2 passes:

1. run the fixed exact controls;
2. run the static isolation scan;
3. audit the structured proof and scope ledgers;
4. validate upstream theorem hashes when Papers 3 and 4 are final; and
5. write a single registered JSON report and immutable result manifest.

No orbit search, prime enumeration, or numerical candidate run exists in M3.

### M4: classification

- `CAPACITY_BOUND_CERTIFIED` only if every proof, scope, provenance, control,
  isolation, and upstream-consistency gate passes;
- `NARROW_OR_MERGE` if the theorem is correct but manuscript novelty is judged
  insufficient; and
- `REJECTED_OR_REQUIRES_AMENDMENT` on an in-scope counterexample, source-lock
  mismatch, unsupported dependency, or forbidden-data finding.

## Exact controls

| Control | Exact object | Expected role |
|---|---|---|
| K001 | Formal rank-$r$ L architecture with $r$ distinct inserted labels | Capacity sharpness without enumerating targets; explicitly target injection. |
| K002 | $a=-15/16$, fixed point $(5/4,5/4)$ | Exact trace $5/2$, determinant $1$, eigenvalues $2,1/2$; the displayed support is already bad. |
| K003 | Identity exact map on $\mathbb A^2$ with symbolic constant `LOG_2` | Positive-dimensional forbidden transcendental injection; no numeric logarithm call. |
| K004 | Formal repeated certificates and arbitrary selection | Set semantics: repeated hits do not increase capacity and one certificate per prime suffices. |
| K005 | $q=1$ and negative/rational formal exponents | Real-log and unit-closure edge cases. |

## Metrics

All metrics are categorical and exact:

- source-lock/provenance: PASS/FAIL;
- ten-item mandatory repair closure: 10/10 required;
- proof-dependency ledger: every required ID present exactly once;
- canonical-form closure/exclusion ledger: PASS/FAIL;
- controls: PASS/FAIL by integer or rational identities;
- executable isolation findings: exactly zero required;
- external prime tables accessed: false;
- Riemann-zero data accessed: false;
- candidate target matches computed: zero;
- novelty: ordinal and noninflated, never an execution metric.

Confidence intervals, $p$-values, and approximate error bars are inapplicable.

## Stop rules

Stop and fail closed if:

- any coefficient, support, representation rule, or architecture is selected
  after inspecting a target;
- any external or enumerated prime/zero dataset is read or generated;
- a floating tolerance, nearest-prime routine, numeric logarithm, fitting, or
  approximation is used as exact evidence;
- an algebraic irrational multiplier-log coefficient or arbitrary nonlinear
  mixer is admitted without a new theorem;
- the class-M proof omits field-extension/saturation or silently asserts
  $\overline\lambda=\lambda^{-1}$;
- algebraicity is confused with canonical gauge invariance;
- a fourth class is included without a new source lock;
- a formal report is attempted before passing independent code review; or
- output language claims a universal no-go, complete trichotomy, sufficiency,
  historical priority, Riemann-zero result, or Route-B progress.

## Required artifacts

- repaired research question, complete proof package, compact dependency
  ledger, independent proof/novelty report, and novelty summary;
- version-2 source lock and this plan/tracker;
- exact symbolic/static audit implementation, controls, and tests;
- independent code review before the registered audit;
- registered result/validation reports and manifest;
- upstream Paper-3/Paper-4 proof-hash binding;
- paper plan, reproducible vector figures, LaTeX manuscript, clean PDF, two
  independent manuscript-review rounds, and final integrity record.
