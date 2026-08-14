# Experiment Tracker

## Material Passport

- Origin Skill: experiment-bridge
- Origin Date: 2026-08-13T11:09:45Z
- Verification Status: VERIFIED
- Version Label: pcf_markov_baker_tracker_v1

| ID | Experiment | Status | Output | Notes |
|---|---|---|---|---|
| M0 | Exact sanity | COMPLETE | `results/exact_preflight.json` | Every frozen algebra/geometry gate passed |
| M1 | Candidate/dyadic ledgers | COMPLETE | `results/ledger.json` | 226 candidate cycles through period 20; 747 dyadic-control cycles through period 12 |
| M2 | Determinant and boundary quotient | COMPLETE | `results/exact_preflight.json` | All conventions separated; sole boundary collapse verified |
| M3 | Controls and isolation | COMPLETE | `results/exact_preflight.json` | Six controls passed; zero forbidden-token violations |
| M4 | 100-digit independent audit | COMPLETE | `results/parent_audit.json` | Maximum residual 9.706e-98; exact count and boundary agreement |
| M5 | Development float stress | COMPLETE | `results/float_stress_development.json` | 16,777,216 checks; zero failures; 1.388e-16 maximum error |
| M6 | Validation | COMPLETE | `results/float_stress_validation.json`, `results/analysis_validation.json` | Hash unlock verified before sampling; frozen decision reproduced |
| M7 | Sealed test | COMPLETE | `results/float_stress_test.json`, `results/analysis_test.json` | First sealed run reproduced every gate; no refit |

## Budget

- Required formal suite consumed approximately 0.22 single-process
  wall-clock hours; one temporary development reproducibility rerun added
  approximately 0.06 hours.  This remained below the frozen 0.5-hour budget.
- GPU consumed: 0 GPU-hours.
- External prime/zero data accesses: 0.

## Protocol Deviations

1. Before any execution, the development seed numeric value was found not to
   match the frozen SHA-256 derivation rule. Source lock v2 mechanically
   corrects the value; validation/test seeds and every scientific design field
   are unchanged. See SOURCE_LOCK_AMENDMENT.md.

No other protocol deviation occurred.

## Completion Decision

```text
PRE_A0_STRUCTURAL_PASS
A0_FAIL / STRUCTURAL_ONLY
A1_WEAK (intrinsic structural ledger verified; no A0 arithmetic labels)
A2-A4 STOP_SCOPED
Route B FORBIDDEN
```

The compact branch-history carrier is verified.  Its canonical multipliers
are powers of two, and the general finite-memory locally constant scalar-clock
theorem excludes an exact all-prime logarithm ledger.  See
`results/EXPERIMENT_RESULTS.md` and `results/VALIDATION_REPORT.md`.
