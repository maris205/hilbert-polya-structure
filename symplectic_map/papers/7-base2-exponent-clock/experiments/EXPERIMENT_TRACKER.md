# Experiment Tracker

## Frozen run registry

| Run | Purpose | Status |
|---|---|---|
| R000 | source-lock schema/hash and upstream binding | PASS |
| R001 | forbidden-data and runnable-code scan | PASS |
| R010 | parameter, Eisenstein, PCF, valuation identities | PASS |
| R011 | local theorem proof-contract audit | PASS |
| R012 | Frobenius--Hensel and norm identities | PASS |
| R013 | mod-2 two-coefficient filter, n=2/3 obstruction, n=4 insufficiency witness | PASS |
| R020 | power-map equality control | PASS |
| R021 | Chebyshev signed-equality control | PASS |
| R022 | negative target control | PASS |
| R023 | formal-period pollution control | PASS |
| R024 | upstream Paper-2 regression | PASS |
| R030 | independent pre-execution code review | DEPLOYMENT_PASS_ROUND_4 |
| R042 | frozen exact reproduction, n=2 | PASS_DEVELOPMENT_SEEN_NO_HIT |
| R043 | frozen exact reproduction, n=3 | PASS_DEVELOPMENT_SEEN_NO_HIT |
| R044 | frozen exact reproduction, n=4 | PASS_DEVELOPMENT_SEEN_NO_HIT |
| R045 | frozen exact reproduction, n=5 | PASS_DEVELOPMENT_SEEN_NO_HIT |
| R046 | frozen exact reproduction, n=6 | PASS_DEVELOPMENT_SEEN_NO_HIT |
| R047 | frozen exact reproduction, n=7 | PASS_DEVELOPMENT_SEEN_NO_HIT |
| R090 | full tests, P5 analysis, and strict result-manifest closure | PASS |
| R100 | independent manuscript review and final integrity | PENDING |

## Disclosure ledger

- Before source lock v1, exact exploratory gcd checks inspected periods 1--8
  and found no \(B_n=\pm1\) factor.
- Before source lock v1, a second exploratory timing and target-resultant
  benchmark re-inspected periods 4--7; gcds were trivial and resultants
  nonzero.  Both sign gcds had degree zero at every period, and each period
  completed in under two seconds in that benchmark.
- These accesses used no external prime table, Riemann-zero data, parameter
  fitting, approximate matching, or post-hoc sign choice.
- Therefore R042--R047 are reproducibility runs only.  There is no hidden
  validation/test split and no claim of preregistration.

Independent source/proof audit required an exact-period semantic repair before
deployment.  Source lock v2 incorporates the monic radical/set-difference
definition, freezes the Chebyshev period-two control, and fixes the exact norm
certificate.

## Registered execution and P5 closure

- Current state: `REGISTERED_RUN_0001_COMPLETED_NO_HIT_P5_ANALYZED`.
- Exactly one registered claim was created.  The terminal ledger records
  `COMPLETED_NO_HIT` after completing periods 2--7.
- Every one of the twelve `B_n=+/-1` target checks has gcd degree zero,
  nonzero exact rational field norm, and agreement between the gcd and
  resultant/norm engines.
- Serialized candidate wall time totaled 23,239,165,865 ns.
- The strict manifest is passing; JUnit records 38 tests with zero failures,
  errors, or skips.
- Human P5 reports:
  `experiments/OFFICIAL_EXPERIMENT_RESULTS.md` and
  `experiments/OFFICIAL_VALIDATION_REPORT.md`.

## Final scope labels

- `EXACT_2ADIC_VALUATION_ALL_PERIODS_CERTIFIED_BY_PROOF`.
- `BASE2_EQUALITY_ABSENT_N2_N3_BY_LOCAL_THEOREM`.
- `BASE2_EQUALITY_ABSENT_N2_TO_N7_DEVELOPMENT_SEEN`.
- `BASE2_EQUALITY_ALL_PERIODS_OPEN_N_GE_4`.
- `ROUTE_A_NOT_ADVANCED / ROUTE_B_NOT_OPENED`.

There were no blind periods, no candidate numerical runs, no post-null
extension, and no access to external prime tables, Riemann-zero data, or
network resources.
