# Code Experiment Plan

## Material Passport

- Origin Skill: experiment-agent + experiment-bridge
- Origin Mode: plan-to-run
- Origin Date: 2026-08-13T11:09:45Z
- Verification Status: SOURCE_LOCKED
- Version Label: pcf_markov_baker_plan_v1
- Source Lock: source_lock.json
- Source Lock SHA-256:
  20473ff34b1f9258281483f47b9db915eb2680d2a71e9e1e6e9f3cf3d6fc07c8

## Experiment Overview

- **Title:** Finite-clock obstruction certificate for the PCF Markov--baker
- **Objective:** Verify the frozen compact piecewise-symplectic carrier,
  periodic quotient, determinant conventions, matched controls, and the
  finite-rank exact-prime-clock obstruction without accessing prime or
  Riemann-zero tables.
- **Hypothesis:** The carrier passes its structural checks, while its canonical
  locally constant instability clock is exactly lattice-valued and therefore
  fails Route-A A0 for an all-prime ledger.
- **Type:** exact computational mathematics plus deterministic simulation

## Setup

- **Language/Framework:** Python 3.12, NumPy 2.4, SymPy 1.14, mpmath 1.3,
  pytest 9
- **Working Directory:** papers/2-branch-baker
- **Compute:** CPU only; required suite below 0.5 CPU-hour and 1 GiB RAM
- **Timeout:** 30 minutes per command; expected complete suite below 10 minutes
- **External data:** none

## Milestones

| ID | Milestone | Split | Must run | Gate |
|---|---|---|---:|---|
| M0 | Exact PCF, graph, PF, tiling, symplectic and inverse sanity | none | yes | All exact identities pass |
| M1 | Candidate ledger through period 20 and dyadic ledger through 12 | none | yes | Frozen vectors and totals match two implementations |
| M2 | Boundary quotient, unsigned/orientation/Lefschetz convention audit | none | yes | All three objects remain distinct and match predictions |
| M3 | Six matched controls and static isolation audit | development | yes | Positive controls pass; negative controls are rejected or classified as frozen |
| M4 | Independent 100-digit parent-factor consistency audit | development | yes | Residual below 10^-75, exactly one declared boundary collapse |
| M5 | Floating implementation stress | development | yes | Zero transition failures; roundtrip error below 2e-13 |
| M6 | Frozen validation rerun | validation | yes | Code and analysis hashes frozen before access |
| M7 | Sealed reproducibility run | test | yes | Validation record and verification manifest frozen before access |

## Controls

| Control | Purpose | Frozen expected behavior |
|---|---|---|
| Dyadic baker | Ledger/inverse positive control | 747 primitive binary necklaces through period 12 |
| Folded-tent baker | Decreasing-branch sign positive control | Stable and unstable coordinates reverse together; determinant +1 |
| Matched dissipative, rho=1/2 | Code-only negative control | Same future graph, determinant 1/2, non-surjective image |
| Label erasure | Past-memory negative control | Unique inverse reconstruction fails |
| Anti-symplectic branch | Implementation negative control | Determinant -1, rejected |
| All-positive sign | Phase-null control | Unsigned ledger unchanged; inherited orientation cancellation removed |

## Expected Outputs

| Output | Path | Format | Success criterion |
|---|---|---|---|
| Exact preflight | results/exact_preflight.json | JSON | Every exact gate true |
| Candidate ledger | results/ledger.json | JSON | 226 primitive SFT cycles through period 20 |
| Independent audit | results/parent_audit.json | JSON | Frozen precision/residual/boundary gates pass |
| Development stress | results/float_stress_development.json | JSON | Frozen float gates pass |
| Validation stress | results/float_stress_validation.json | JSON | Created only after validation unlock |
| Sealed test stress | results/float_stress_test.json | JSON | Created only after sealed-test unlock |
| Analysis | results/analysis.json | JSON | Exact Route-A classification from frozen rules |
| Verification manifest | experiments/verification_manifest.json | JSON | Hashes all code, analysis, and pre-test artifacts |

## Analysis Plan

The primary result is conjunctive, not statistical:

1. structural carrier identities must pass exactly;
2. the matched controls must distinguish symbolic coding from symplecticity;
3. the canonical SFT multiplier ledger must equal the powers of two;
4. the finite-memory locally constant clock theorem then assigns
   A0_FAIL / STRUCTURAL_ONLY.

No effect size, p-value, prime enrichment, target-zero comparison,
quantization, or Route B analysis is permitted for this candidate.

## Access Discipline

Development may run immediately after implementation. Validation is unlocked
only after code, analysis, thresholds, and development artifacts are hashed.
The sealed test is unlocked only after the validation artifact and verification
manifest are frozen. Every access is appended to test_access_log.md.
