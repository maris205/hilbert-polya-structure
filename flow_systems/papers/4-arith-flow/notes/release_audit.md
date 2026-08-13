# Paper 4 release audit

Date: 2026-08-13  
Decision: **PASS / ACCEPTED AFTER MINOR REVISION**

## Independent review closure

The independent reviewer initially requested two minor corrections and issued
the final verdict `ACCEPT`.  Both required items are closed:

- the cycle-type invariance proposition now explicitly assumes that all
  points are periodic and notes that additional infinite nonperiodic orbits
  change the conclusion;
- the proof/source audit notation and a damaged `prime` TeX token were
  repaired.

The accompanying wording now also distinguishes the chosen discrete topology
from the separately frozen roof and zeta normalization.  The independent
review records zero critical, major, or residual required minor issues.  The
separate citation audit records `ACCEPT`: every bibliography item was located,
cited, and matched to the claim it supports.

## Reproduction and production checks

```text
unit tests: 13/13 PASS
result manifest: PASS
Riemann-zero inputs: 0
fitted parameters: 0
network inputs to reproduction: 0
Route-A YAML parse (three Stage-4 records): PASS
XeLaTeX undefined citations/references: 0
missing characters: 0
overfull boxes: 0
underfull boxes: 0
LaTeX warnings: 0
PDF pages: 16
representative-page visual inspection: PASS
```

## Frozen release

- PDF: `paper/paper.pdf`
- TeX SHA-256:
  `da04db49fc641c938f0ca2ecee7d9b4ad89b78a7fc6adebe871280b434ba8041`
- PDF SHA-256:
  `775c6016ae17fceb2f875b3cc5608563efae85b037553d8167597c4c45b5ae6a`
- native record:
  `../../evaluations/route_a/FF-FROB-SUSP-P1-F2/2026-08-13-stage4.yaml`
- rational-prime target record:
  `../../evaluations/route_a/FF-FROB-SUSP-P1-F2-RIEMANN/2026-08-13-stage4.yaml`
- target-encoded control record:
  `../../evaluations/route_a/SPECZ-TAUT-NORM-CIRCLES/2026-08-13-stage4.yaml`

The positive result is deliberately scoped to the native finite-field zeta.
It does not transfer the construction to the rational-prime Euler product and
does not establish any Route-B or Hilbert--P\'olya claim.
