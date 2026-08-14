# Experiment Tracker: Exact Prime-Multiplier Obstruction Audit

**Candidate:** `pcf_quadratic_prime_multiplier_obstruction_v1`  
**Source-lock SHA-256:** `aab59e6d97e919bd9f11f74cf45d8163fc320560dfa74bee85401bd184d37842`  
**Execution date:** 2026-08-13  
**Required-run status:** complete

## Milestones

| Milestone | Runs | Status | Evidence |
|---|---|---|---|
| M0: freeze integrity | R000--R001 | PASS | Valid JSON/hash; 19 Python files and `pyproject.toml` scanned; zero forbidden-access finding. |
| M1: proof and controls | R010--R013 | PASS | Twelve proof-boundary checks and all three frozen controls passed. |
| M2: candidate preflight | R020--R022 | PASS | Exact isolating interval, unique-real-root certificate, conjugacy, and `g'=2z` passed. |
| M3: candidate algebra | R031--R034 | PASS | Exact dynatomic/resultant audits at `n=1,2,3,4` passed every chain, cycle-power, quotient, and divisibility gate. |
| M4: symplectic bridge | R040--R042 | PASS | Pullback/determinant/return identities and critical/global negative checks passed. |
| M5: optional real ledger | R050--R051 | NOT RUN / DISABLED | The ledger has no evidentiary role and remained disabled exactly as frozen. |

## Exact run registry

| Run ID | Purpose | Final status | Result artifact |
|---|---|---|---|
| R000 | Validate and hash source lock | PASS | `results/source_lock_validation.json` |
| R001 | Static forbidden-access audit | PASS | `results/source_lock_validation.json` |
| R010 | Proof-dependency audit | PASS | `results/proof_audit.json` |
| R011 | `c=0` power-map control | PASS | `results/control_audit.json` |
| R012 | `c=-2` Chebyshev control | PASS | `results/control_audit.json` |
| R013 | `c=-3/4` assumption-violation control | PASS | `results/control_audit.json` |
| R020 | Algebraic-parameter/root preflight | PASS | `results/parameter_preflight.json` |
| R021 | Exact `f_u`--`g` conjugacy | PASS | `results/parameter_preflight.json`, `results/conjugacy_audit.json` |
| R022 | Derivative-content identity | PASS | `results/parameter_preflight.json` |
| R031 | Candidate period 1 | PASS | `results/candidate_multiplier_audit.json` |
| R032 | Candidate period 2 | PASS | `results/candidate_multiplier_audit.json` |
| R033 | Candidate period 3 | PASS | `results/candidate_multiplier_audit.json` |
| R034 | Candidate period 4 | PASS | `results/candidate_multiplier_audit.json` |
| R040 | Canonical one-form pullback | PASS | `results/symplectic_bridge_audit.json` |
| R041 | Reciprocal return spectrum | PASS | `results/symplectic_bridge_audit.json` |
| R042 | Critical/global negative checks | PASS | `results/symplectic_bridge_audit.json` |
| R050 | Controls-only real-ledger feasibility | NOT RUN | Optional, unbudgeted, and unnecessary. |
| R051 | Candidate real ledger | DISABLED | No source-lock amendment; no candidate high-period ledger executed. |

## Final boundary

- Raw rational-prime multiplier: `ABSENT_BY_THEOREM` at all periods.
- Odd rational exponent-prime multiplier: `ABSENT_BY_THEOREM` at all periods.
- Rational `p=2` exponent-prime multiplier at period one: `ABSENT`.
- Rational `p=2` exponent-prime multiplier for periods `n>=2`: `OPEN`.
- Complex modulus-only target: outside the theorem.
