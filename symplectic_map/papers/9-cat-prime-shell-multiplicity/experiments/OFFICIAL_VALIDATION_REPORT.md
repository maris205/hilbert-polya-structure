# Official Validation Report

Date: 2026-08-14 UTC  
Candidate: `cat_prime_shell_multiplicity_obstruction_v1`  
Validation mode: frozen-artifact analysis and post-run closure preparation

## Scientific validation decision

`REGISTERED_RESULT_SEMANTICS_PASS`

The one-shot exact audit completed with terminal state
`COMPLETED_CERTIFIED`.  Its raw payload satisfies the strict frozen semantic
contract: both finite-field engines agree on all five registered rows, all
twelve mechanism controls pass, every counter and evidence role has the
required exact type and value, and the proof-only/nonclaim firewall remains
intact.  No registered rerun, numerical run, new prime, composite scan,
external data access, or centralizer calculation occurred during post-run
analysis.

This report is intentionally finalized before the independent result
integrity authority and the one-shot result manifest.  Those later artifacts
must bind this immutable report and the raw result.  Their future self-hashes
are not embedded here, avoiding a circular manifest dependency.  Final live
closure is established by `results/INDEPENDENT_RESULT_INTEGRITY.md` and
`results/result_manifest.json`, not by editing this report afterward.

## Immutable execution chain

| Artifact or role | SHA-256 / value | Validation |
|---|---|---|
| Source lock | `662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49` | exact and live |
| Independent source review | `9509278ce55d908dba7d7cb4a809a335cc51d9364e8bfdfd1dc66be594775b8f` | `SOURCE_LOCK_PASS` |
| Execution code/design tree | `466fb64928ad5f8b5b4c2643d8875c98568bbbdaabd4abeb6f24cc7ba13ecddb` | independently authorized |
| Pre-execution JUnit | `096dfff6203d48b22340e8def19bacca27294d383c1807f6856985fe99ff0cd8` | 23/23 pass |
| Deployment review | `dffcd516d349ef864d078764b9e9ccaa2edccd70d52802e77b6965baa70b9b27` | canonical Round-4 `DEPLOYMENT_PASS` |
| Authorized pre-execution audit | `a54ad84f5e889b9e54a4f4407b1e8a9021a001358188419ffa961f11d8f2b75a` | claim-bound, all five safe gates pass |
| Registered claim | `863d9d3c4e77bd2407776244c8e925abd60fd265cff5163698e81d32f144e2d4` | unique durable `STARTED` claim |
| Raw experiment result | `448de06e92bd7ab4e5374e5d1f57413df45859cd3476ff14b2691b63ac364fab` | strict registered-result semantics pass |
| Registered terminal | `bc82784449e50ec85c3d268197ab8489c7e2a888bfb35aa4a49915488b66273c` | `COMPLETED_CERTIFIED` |
| Post-run JUnit | `43f03d9be620188422dbb01d8ff016d4811eb505475214845ae17dffb21c6304` | 23/23 pass |

The terminal links the exact claim and result hashes, records
`REGISTERED_RUN_0001`, and lists exactly \(2,3,5,7,11\) as both started and
completed.  It records one registered exact audit, one registered run, zero
candidate numerical runs, and no failure code.

## Deployment review history

The independent review record preserves all failed rounds byte-for-byte.

1. Round 1 rejected alias/container/dynamic capability escapes, a hollow
   registered-result schema, and missing parent-directory durability.
2. Round 2 confirmed those repairs but rejected dunder/builtins/path
   capability bypasses, a false float counter, and hollow official gate
   records.
3. Round 3 confirmed the prior fixes but reproduced unreviewed
   `os.spawnl` and arbitrary-path `os.open/os.read` calls.
4. Round 4 independently replayed every attack, validated exact
   file/function/AST call-site allowlists and canonical executable-body
   digests, reran 23 safe tests, and issued the only deployment authority.

The preserved history-prefix hashes are respectively
`77b9cc4b892e0395006d1e058ea065db8b5eae8c829be361ee013b8f469201c0`,
`0647a31103b55d55ce901c150cb9b72230ea35541e04af14e539ce9e2ef92db5`,
and
`775d05e002ce4cd1bc343cbca01f2b2db471c239442c9e0752500aafb6c55cff`.
No candidate was registered before Round 4.

## Registered scientific validation

| Gate | Exact observation | Status |
|---|---|---|
| Closed input scope | only matrix \(((2,1),(1,1))\), primes \((2,3,5,7,11)\), repeats \((1,2,3)\) | pass |
| Direct shell partitions | all 203 nonzero vectors occur exactly once in 37 canonical cycles | pass |
| Analytic classifications | binary/inert/ramified/split certificates reproduce every locked profile | pass |
| Dual-engine comparison | shell size, periods, cycles, \(m_p\), and split strata agree in every row | pass |
| Ramified boundary | \(p=5\) has two length-two and two length-ten cycles | pass |
| Raw/label separation | raw factors retain lengths; label factors have degree \(m_p\) | pass |
| Repeat ledger | label coefficient is exactly \(m_p/r\) for \(r=1,2,3\) | pass |
| Scalar degree obstruction | every odd registered row has degree greater than one | pass |
| Equal-weight control | \(m_p^{1-r}\) fails repeats two and three for odd rows | pass |
| Fractional identity | orbit point masses sum exactly to one in every shell | pass |
| Selector boundary | retaining one orbit exposes discard cost \(m_p-1\) | pass |
| Symbolic composite guard | \(q\) remains symbolic; no composite shell is enumerated | pass |
| Analytic/escape guard | global claims are proof-only; all listed escapes remain outside scope | pass |

The raw result has exact top-level counters
`registered_exact_audits=1`, `candidate_numerical_runs=0`,
`generated_prime_target_arrays=0`,
`numeric_s_or_log_evaluations=0`, `composite_shells_enumerated=0`,
`centralizer_computations_run=0`, `parameter_or_matrix_searches=0`, and
`normalization_or_selector_searches=0`.  Boolean values cannot substitute
for these integer counters under the validator.

## Product and mechanism firewall

The validation keeps four constructions distinct:

- the raw-return product, whose monomials contain primitive orbit lengths;
- the one-time orbit-label product, whose denominator degree is \(m_p\);
- scalar weights inside ordinary factors, whose nonzero degree cannot
  collapse to one and whose equal-weight power sums fail under repetition;
- outer fractional shell masses, which yield an exact unit exponent only as
  global normalized counting.

A one-orbit selector is also represented separately and reports every
discarded cycle.  It is not declared canonical.  Consequently the certified
A0 failure applies to direct all-orbit labeling and pure nonzero scalar
factor weights.  It is not a theorem against matrix-valued weights,
numerator or alternating cancellation, transfer/Fredholm determinants,
cohomological superdeterminants, centralizer quotients, or enriched
selectors.

## Theorem/computation firewall

- Exactly five inherited, development-seen prime shells were registered.
- No new prime was generated, loaded, or searched.
- The all-odd-prime multiplicity statement is sourced to
  `notes/PROOF_PACKAGE.md`; it is not extrapolated from five rows.
- The global contracts are proof-only:
  `DIVERGES_REAL_1_LT_SIGMA_LE_2`,
  `NOT_ABSOLUTE_1_LT_SIGMA_LE_2`, and
  `ABSOLUTE_SIGMA_GT_3`.
- The strip \(2<\Re s\le3\), exact abscissa, analytic continuation, and
  conditional convergence are unclaimed.
- The composite-order identity is symbolic only.  It uses the product over
  prime divisors of \(q\) and supplies no numerical \(q\).
- No numerical \(s\), logarithm, Euler product, or zero datum was evaluated.
- Centralizer, matrix, numerator, Fredholm, cohomological, enriched-selector,
  transfer, quantum, and Route-B work was neither executed nor closed.

## Post-run regression evidence

The post-run JUnit contains 23 tests with zero failures, errors, or skips.
It revalidates the exact dual engines, forbidden-modulus boundary,
raw/label semantics, mechanism controls, symbolic composite guard, strict
JSON and inventory rules, all scanner attack families, exact review parser,
durable file-then-directory `fsync`, hollow-gate rejection, result-schema
rejection, and one-shot lifecycle guard.  The lifecycle test observes the
existing claim and rejects a second registered invocation before candidate
execution.  No registered rerun occurred.

## Frozen tracker handling

The source lock and execution tree bind
`experiments/EXPERIMENT_TRACKER.md` at
`00fc66f266b7a1ddcccc0b355ff7dbb6ea787f1d60319862dbd7d5da6262d0b9`.
It was therefore not edited.  Its `TODO_NOT_AUTHORIZED` rows and zero-run
header document the source-design state, not current execution state.
Changing them after deployment would invalidate the source gate, reviewed
tree, deployment authority, claim, raw result, and terminal simultaneously.

The two official reports are the authorized human post-run record.  No
replacement tracker is added to `results/`, whose inventory is exact and
will be closed by the manifest.

## Result-integrity and manifest protocol

Before the strict manifest may be written, a fresh independent reviewer must
inspect the immutable execution chain, raw scientific payload, post-run
JUnit, and these reports, then issue exactly one canonical `RESULT_PASS`
authority bound to the execution tree and raw-result hash.  The manifest
builder subsequently requires the exact pre-manifest inventory, recomputes
every gate, records hashes for all non-self evidence and both reports, writes
once with durable exclusive semantics, and immediately validates the final
inventory.  Any missing, extra, changed, linked, malformed, or stale file
must fail closure.

Because this report is itself a manifest input, it does not embed the future
manifest hash.  The final manifest deliberately records no recursive
self-hash; its own SHA-256 is supplied by the read-only closure validator.

## Classification and limits

| Field | Certified value |
|---|---|
| Scientific classification | `PRIME_SHELL_MULTIPLICITY_OBSTRUCTION_CERTIFIED` |
| Route A | `A0_FAIL_GLOBAL_NORMALIZATION_ONLY` |
| Route B | `ROUTE_B_NOT_OPENED` |
| Finite evidence | exact development-seen reproduction at \(p=2,3,5,7,11\) |
| All-prime statement | proof-only, not finite-experiment inference |
| Admitted unit-factor repair | complete-shell `GLOBAL_NORMALIZED_COUNTING` |
| Main live escape | centralizer quotient reserved for Paper 10 |

This validation does not certify a prime-only local potential, prime-orbit
bijection, prime/zero match, exact analytic abscissa, transfer determinant,
quantization claim, or closure of any escape outside the pure fixed nonzero
scalar denominator theorem.  No manuscript was created or modified during
this post-run analysis.
