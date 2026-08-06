# Experiment and Proof Plan

**Problem:** prove a non-removable spectral effect of the fixed Hénon warp
while preserving the existing Q/W operator and claim boundaries  
**Method thesis:** radial rearrangement uniquely minimizes the ground-state
energy; the Hénon warp has an exact negative first relative heat carrier  
**Date:** 2026-08-06

## Claim map

| Claim | Minimum convincing evidence | Block |
|---|---|---|
| C1 strict spectral activation | complete rearrangement proof with equality-case citation and independent audit | B1 |
| C2 exact first heat carrier | two independent quadratures, constants, sign, hashes | B2 |
| C3 full small-time relative heat asymptotic | uniform moving-region remainder \(o(L^2)\) | B3 |
| anti-claim: signal is a discretization/zero fit | analytic proof, no arithmetic inputs, optional common-grid illustration only | B1/B2/B4 |

## Paper storyline

- **Main paper must prove:** C1.
- **Strong extension, completed:** C3 with remainder \(O_{a,h}(tL^4)\).
- **Appendix:** R300 exact quadrature and reproducibility.
- **Cut:** RMT statistics, global \(a=1.02\) cycle zeta, adelic products,
  and individual zeros.

## Blocks

### B1 — strict rearrangement theorem

- **Status:** complete, independently reviewed.
- **Must finish:** the primary Brothers--Ziemer citation is now recorded;
  add positivity/analytic-regularity citations and line-check the form-domain
  argument.
- **Success:** no hidden assumption remains.
- **Failure interpretation:** weaken to non-strict ground-state ordering.
- **Priority:** MUST-RUN.

### B2 — exact heat carrier R300

- **Status:** `PASS_AFTER_R300_P1`; exact portion replicated and the analytic
  remainder closed separately.
- **Data:** frozen seven-point time grid.
- **Metric:** cross-implementation relative error and sign.
- **Result:** \(5.03\times10^{-15}\) maximum production discrepancy;
  arbitrary-precision checker passed.
- **Priority:** MUST-RUN, completed.

### B3 — R300-P1 uniform remainder theorem

- **Status:** complete; two independent proof audits returned `ACCEPT` after
  one local dominated-differentiation repair.
- **Task:** prove the relative Feynman--Kac/resummed-parametrix remainder.
- **Decomposition:**
  1. split \(|z|^2\le\pi^{-1}(L+C\log L)\) and the tail;
  2. bound \(V_a^{-1}\partial^\alpha V_a\) on the main region;
  3. bound Brownian-bridge exits;
  4. retain the exact classical cancellation before absolute values;
  5. show the sum of omitted relative terms is \(O(tL^4)\).
- **Result:** appendix-ready proof of the stronger
  \(O_{a,h}(tL^4)\) bound.
- **Failure:** keep C1/C2 and remove the full heat asymptotic.
- **Cost:** proof work, negligible compute; estimated 1--3 weeks.
- **Priority:** MUST-RUN for the stronger paper, not for the base theorem.

### B4 — optional finite-volume illustration

- **Task:** common-domain radial/Hénon ground-state and heat-trace comparison
  with a simple control \(a=0\).
- **Launch condition:** only after B1 citation audit; do not use R108 P2 branch.
- **Success:** correct sign under two grids; descriptive only.
- **Failure:** numerical illustration omitted; theorem unaffected.
- **Priority:** NICE-TO-HAVE.

### B5 — local horseshoe module R301

- **Task:** adaptive transverse-homoclinic precheck at \(a=51/50\).
- **Paper placement:** separate future project, not this main story.
- **Priority:** DEFERRED.

## Run order

| Milestone | Run | Decision gate | Cost | Status |
|---|---|---|---|---|
| M0 | R300 exact carrier | A/B identity and sign | <1 min CPU | DONE |
| M1 | C1 proof and independent audit | theorem survives equality-case check | proof-only | DONE |
| M2 | R300-P1 derivative/tail lemmas | each bound uniform in moving region | proof-only | DONE |
| M3 | R300-P2 full relative remainder | \(O(tL^4)\) or stop | merged into P1 | DONE |
| M4 | optional common-grid illustration | stable sign on two grids | <2 CPU h | DEFERRED; theorem does not need it |
| M5 | R301 horseshoe | separate \(P^*\) decision | <2 CPU h | DEFERRED |

## Risks

- **Remainder grows too fast:** publish C1/C2 only.
- **Equality citation mismatch:** explicitly add the missing critical-set
  hypothesis or weaken strictness.
- **Contribution seen as standard rearrangement:** emphasize the exact
  same-clock/different-spectrum theorem and explicit Hénon heat carrier.
- **Arithmetic overinterpretation:** keep P/Z table in abstract and
  conclusion.
