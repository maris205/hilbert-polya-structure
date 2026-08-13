# Validation Report

## Material Passport

- Candidate: `pcf_markov_baker_v1`
- Report date: 2026-08-13
- Verification status: `VERIFIED`
- Verification scope: source-lock integrity, exact identities, independent
  parent audit, matched controls, split discipline, deterministic floating
  implementation, and Route-A stopping rule
- Statistical scope: no hypothesis-test (p)-values, confidence intervals,
  or fitted effect sizes are applicable; the primary result is exact and
  conjunctive

## Verification decision

The result is verified.  The complete pre-validation and pre-test hash chain
is intact, all 89 tests pass, all exact gates pass, the independent 100-digit
audit matches the frozen periodic quotient through period 20, and all three
floating splits complete every scheduled check with zero edge mismatch and
zero boundary failure.

The verified scientific conclusion is negative and scoped:

```text
The carrier passes its structural checks.
The finite locally constant scalar multiplier clock fails Route-A A0.
Formal A1 is WEAK: the intrinsic ledger is verified but carries no A0 arithmetic labels.
A2, A3, A4, and Route B remain closed.
```

## Reproducibility and provenance

| Item | Verification |
|---|---|
| Source lock | SHA-256 `20473ff34b1f9258281483f47b9db915eb2680d2a71e9e1e6e9f3cf3d6fc07c8` |
| Frozen code tree | SHA-256 `ad7f6637a90e6f5cfc4933b89adc70c543c0d0f259f295ea84da10c6fa5f0b11` |
| Validation unlock | Present and verified before validation sampling |
| Verification manifest | Present and verified before test sampling |
| Test unlock | Present and verified before sealed-test sampling |
| Split access log | Validation and test sampling plus analysis recorded |
| Development rerun | Byte-identical temporary reproduction |
| External prime/zero data | Explicitly false in every formal artifact |
| Forbidden legacy result access | Static isolation scan found no violation |

Environment recorded at verification:

```text
Python 3.12.3
Linux 5.4.0-155-generic x86_64, glibc 2.35
NumPy 2.4.4; SymPy 1.14.0; mpmath 1.3.0
SciPy 1.16.1; pytest 9.0.3
CPU-only; no GPU required
```

The source-lock amendment is not hidden: version 1 transcribed the
development seed inconsistently with its own SHA-256 derivation rule.  Version
2 corrected only that development value before any candidate execution or
split access.  Validation and test seeds and all scientific choices were
unchanged.

## Cross-split consistency

| Metric | Development | Validation | Test | Assessment |
|---|---:|---:|---:|---|
| Points | 65,536 | 65,536 | 65,536 | Frozen scale |
| Steps | 256 | 256 | 256 | Frozen scale |
| Completed checks | 16,777,216 | 16,777,216 | 16,777,216 | Complete |
| Maximum per-step roundtrip error | \(1.388\times10^{-16}\) | \(1.388\times10^{-16}\) | \(1.388\times10^{-16}\) | Stable |
| Edge mismatches | 0 | 0 | 0 | Pass |
| Boundary failures | 0 | 0 | 0 | Pass |
| Formal classification | `A0_FAIL / STRUCTURAL_ONLY` | same | same | Stable |

The checks are deliberately deterministic implementation stress tests.  The
16,777,216 rows per split are not treated as independent samples, and no
binomial confidence claim is made from them.

## Independent checks

- Direct canonical-cycle enumeration and trace/Möbius inversion reproduce the
  same period-1--20 primitive-count vector and total 226.
- A separately implemented high-precision inverse-branch audit, which does
  not import the cycle-ledger generator, reproduces every parent count and the
  one declared boundary duplicate through period 20.
- The maximum high-precision periodic residual is
  \(9.706\times10^{-98}\), below the frozen \(10^{-75}\) target.
- The dyadic control gives exactly 747 primitive binary necklaces through
  period 12.
- The dissipative, label-erasure, anti-symplectic, and all-positive-sign
  controls fail or change exactly the structural property they were designed
  to isolate.
- An independent code-review round ended with zero critical, major, or minor
  findings after fixes; the reviewed suite had 89 passing tests.

## Statistical-interpretation audit

| Risk | Assessment | Reason |
|---|---|---|
| Simpson's paradox | Not applicable | No grouped trend is aggregated into a population claim. |
| Ecological fallacy | Not applicable | No group-level statistic is assigned to individual trajectories or orbits. |
| Berkson's paradox / selection bias | Scope warning | The PCF parameter was selected precisely for a finite Markov partition.  Results are restricted to this candidate and class; they are not generalized to arbitrary quadratic or symplectic maps. |
| Collider bias | Not applicable | No conditioning variable is used to infer association between independent causes. |
| Base-rate neglect | Not applicable | No rare-event classifier, prime-hit rate, or enrichment statistic is reported. |
| Regression to the mean | Not applicable | There is no noisy extreme selected for follow-up and no effect-size claim. |
| Survivorship bias | Addressed | Every scheduled floating check completed; no escaping or failed trajectory was silently discarded.  Boundary points were handled by separate exact-relation tests. |
| Look-elsewhere effect | Pass | One source-locked candidate and one frozen scale were used; there was no parameter, seed, threshold, roof, or determinant sweep. |
| Garden of forking paths | Low risk, disclosed amendment | Decision rules and whitelisted artifacts were frozen before validation.  The sole development-seed correction preceded all execution and is recorded. |
| Correlation versus causation | Pass | No causal claim is drawn from numerical association.  Matched controls isolate symbolic coding, invertibility, sign convention, and symplecticity. |
| Reverse causality | Not applicable | No observational cause-effect relation is inferred. |

## Validity boundaries

### Internal validity

Internal validity is strong for the declared exact model.  Algebraic formulas,
two enumeration routes, an independent high-precision parent audit, six
controls, split-specific seeds, and a verified hash chain all agree.

### Construct validity

The experiment measures a branch-baker multiplier clock, not the raw
quadratic parent derivative cocycle.  The signed \(W\) weights encode factor
branch orientation, not symplectic orientation or a quantum/Maslov phase.  The
per-step roundtrip check measures implementation consistency, not long-time
shadowing.

### External validity

External validity is intentionally narrow.  The theorem covers fixed finite
graphs with finite-memory locally constant scalar multiplicative clocks.  It
does not cover point-dependent roofs, countable states, growing model
families, matrix spectral radii, approximate matching, or arbitrary smooth
symplectic dynamics.

### Novelty validity

The parent zeta, boundary-period mechanism, and generalized baker platform
are prior-art baselines.  The defensible contribution is the explicit
finite-clock obstruction certificate, its sharp finite-rank statement, and a
fully audited worked example.  It should be presented as a narrow structural
negative result, not as a new arithmetic or Hilbert--Pólya construction.

## Final verification statement

The evidence is sufficient to close this frozen candidate.  Further sampling
cannot remove the proved A0 obstruction.  Continuing to zero comparisons or
quantization would violate the stopping rule.  The appropriate next artifact
is a short structural/no-go manuscript; any attempt to escape the theorem's
assumptions must begin as a separately source-locked candidate.
