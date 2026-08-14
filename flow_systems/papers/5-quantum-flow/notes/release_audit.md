# Paper 5 release audit

Date: 2026-08-13  
Decision: **PASS / ACCEPTED AFTER MINOR REVISION**

## Independent review closure

The final independent verdict is `ACCEPT`, with zero critical, major, or
residual required minor issues.  The two requested consistency corrections
are closed:

- the probability condition is explicitly
  $\sum_x w_xL_x=1$, and component weights are each finite and strictly
  positive;
- every local-rank claim is quantified over intervals of positive width,
  with irrational singletons separately recorded as zero-rank projections.

The release also freezes the square-map Frobenius convention, keeps B4/B5 as
scope annotations rather than verdicts, and distinguishes atomic vector
spectral measures from the continuous-spectrum points of the set-theoretic
operator spectrum.

The separate citation audit and the manuscript-integrity audit both report
`ACCEPT/PASS`.

After the first review lock, the Paper-6 cross-audit caught one metadata-only
corrigendum: Koopman's 1931 title uses plural “Transformations.”  The BibTeX
record and source matrix were corrected and the unchanged TeX body was
rebuilt.  This changes the PDF hash but no theorem, route verdict, locator, or
layout conclusion.

## Reproduction and production checks

```text
unit tests: 8/8 PASS
generated artifact hashes: stable
Riemann-zero inputs: 0
fitted parameters: 0
network inputs to reproduction: 0
B4/B5 invoked: false
Route-A Stage-5 YAML parse: PASS
XeLaTeX undefined citations/references: 0
missing characters: 0
overfull boxes: 0
underfull boxes: 5, confined to narrow table cells
PDF pages: 14
all-page rasterization and representative visual inspection: PASS
```

## Frozen release

- PDF: `paper/paper.pdf`
- TeX SHA-256:
  `3616a52872510f9b8ddb355b8f35b437ba0956dc592342757f5c64f5214c8f4a`
- PDF SHA-256:
  `802ad1a1169be166d5a82da2e0247a92e6c848113303c7d70818bbdfd90acef5`
- manifest SHA-256:
  `af9746cd5a5684ecbd7c92fdbbbf661ad6ad6acd00577c8ce5aa938421bf0344`
- Route-A record:
  `../../evaluations/route_a/FF-FROB-SUSP-P1-F2-KOOPMAN-P1/2026-08-13-stage5.yaml`

Formal limited Route-B result:

```text
B1_COMPLETE_OPERATOR_DEFINITION — PROVED
B2_SELF_ADJOINT — PROVED
B3_FAIL — PROVED
overall: ROUTE_B_REJECTED at Gate C
hilbert_polya_claim_allowed: false
```

B4 and B5 were not invoked and have no Paper-5 verdict.
