# Paper Plan

**Working title:** A Frozen Test of Symbolic-Shadow Transport from a Critical
Quadratic Map to a Symplectic Hénon Map

**Paper type:** theory plus controlled diagnostic experiment

**One-sentence contribution:** A smooth finite-dimensional symplectic lift cannot
retain the critical quadratic map as a regular factor, and a source-locked test of
the weakest inherited parity shadow finds generic dissipative persistence but carrier
collapse at the area-preserving endpoint.

## Claims--evidence matrix

| Claim | Evidence | Status | Location |
|---|---|---|---|
| \(H_{a,\rho}^*\omega=\rho\omega\), \(\det M=\rho^n\), and the \(\rho=1\) generating function is exact | Symbolic derivation and 30 tests | PROVED identities / numerically checked code | Theory, App. A |
| The critical parent cannot be a smooth submersion factor of a local diffeomorphism over its critical fiber | Rank lemma and embedded-copy corollary | PROVED, elementary and not novel alone | Theory |
| Orbit software is calibrated in a full binary-shift regime | Exact primitive-necklace counts \(2,1,2,3,6,9,18,30,56,99\); 80-digit residual audit | NUMERICALLY_CERTIFIED through period 10 at \(a=6\) | Methods, Fig. 2 |
| The frozen \(u_c\) ledger is complete | Binary seeds miss many expected codes | NOT_TESTABLE; explicitly rejected | Methods, Fig. 2 |
| Parent parity is retained at the symplectic endpoint | Locked exposure, parity, neighbor, and test gates | STOP_SCOPED: carrier unavailable in sealed test | Results, Fig. 1 |
| Small-\(\rho\) parity persistence is arithmetic-specific | All four neighbor controls plus Markov null | REFUTED in the tested neighbor panel | Results |
| Dissipative behavior follows a generic attractor skeleton | Exact \(\rho_{\mathrm{PD}}=\sqrt{4a/3}-1\); 120-cell diagnostic | PROVED threshold / numerical mechanism diagnostic | Analysis |
| A prime Euler product or Riemann determinant follows | No qualifying A0/A1 evidence | STOP_SCOPED | Limitations |

## Structure

1. **Introduction.** Lead with the carrier-unavailability result, not
   Hilbert--Pólya speculation. Separate an attributed mod-2 seed from a rational-prime
   mechanism.
2. **Closest prior and claim boundary.** Fogedby--Jensen and
   Demaeyer--Gaspard on singular canonical Logistic extensions; Hénon
   continuation/anti-integrability; Sattari--Mitchell and Gallas on orbit ledgers;
   arithmetic orbit frameworks only as out-of-class context.
3. **Geometry and obstruction.** Exact conformal identity, singular endpoint,
   generating function, rank lemma, embedded-copy corollary, and nonclaims.
4. **Source-locked protocol.** Parity partition/statistic, exposure censoring,
   split/access log, high-\(a\) positive control, 80-digit non-interval audit,
   neighbor and temporal controls.
5. **Results.** Confirmatory endpoint first; split consistency; neighbor
   nonspecificity; full-shift calibration; incomplete \(u_c\) ledger.
6. **Dynamical explanation.** Fixed-point Jury threshold and secondary basin-period
   diagnostic; distinguish sink-produced parity from conservative bounded dynamics.
7. **Discussion and conclusion.** Strongest negative result, limitations from
   noncompact escape and ensemble dependence, Route-A rejection, and closed
   zeta/quantization branches.

## Figure and table plan

| ID | Content | Source | Status |
|---|---|---|---|
| Fig. 1 | Parity polarity and finite exposure versus \(\rho\), all three splits plus four sealed-test neighbors | frozen JSON/CSV outputs | Final figure generated |
| Fig. 2 | High-\(a\) primitive-count calibration and incomplete \(u_c\) search | ledger JSON | Generated |
| Fig. 3 | Basin-class fractions around analytic flip threshold | attractor diagnostic CSV | Generated |
| Table 1 | Candidate, primary endpoint, gates, and access history | source lock/manifest | Manuscript |
| Table 2 | Confirmatory endpoint and neighbor Holm contrasts | analysis JSON | Complete |
| Table 3 | Closest-prior claim comparison | verified bibliography | Manuscript |

## Claim language to enforce

- Use “singular reference” rather than smooth continuation from \(\rho=0\).
- Use “attributed parity shadow” rather than prime-generating Logistic seed.
- Use “high-precision residual audit” rather than interval certification.
- Use “incomplete exploratory ledger” at \(u_c\).
- Report “carrier unavailable in the frozen ensemble,” not an arithmetic failure
  among every bounded orbit.
- Route A is rejected for this candidate; Route B is not invoked.

## Independent-review disposition

Round 2 scored the narrowed package 6.8/10 and green-lit manuscript production as a
nonlinear-dynamics negative/diagnostic paper. It explicitly rejected arithmetic-
positive, arithmetic-disproof, Riemann-determinant, and Hilbert--Pólya framings.
