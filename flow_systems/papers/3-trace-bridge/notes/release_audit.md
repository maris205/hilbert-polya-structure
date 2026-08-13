# Paper 3 release audit

Date: 2026-08-13  
Decision: **PASS / ACCEPTED AFTER MINOR REVISION**

## Independent review closure

The independent reviewer issued `MINOR REVISION`; the final re-review records
`ACCEPT` in `peer_review_round1.md`.  All eight requested precision changes
were closed:

- both abstracts now state the prior containing every possible nonzero
  singular location;
- the unacquired local Selberg convention is `NOT_TESTABLE`, distinct from the
  proved exact framework, and the protocol deviation is explicit;
- the Duistermaat--Guillemin wave operator is normalized to positive
  self-adjoint elliptic order one with real scalar principal symbol;
- the Ruelle display defines (P_V=(1/i)\mathcal L_V) and names the scalar
  (k=0) specialization;
- the T0 result is visibly a formal certificate/schema lemma and lists the
  transport evidence required for a new provenance;
- Deninger and modular Route-B non-entry reasons are serialized separately;
- protocol, blueprint, source matrix, and manuscript use the same
  punctured-line ambiguity and convention-status language;
- status-macro spacing and narrow table layout were repaired.

The independent citation audit found all ten bibliography entries real,
cited, and claim-aligned.  The registered Selberg DOI returned HTTP 404 on the
audit date; the stable CERN metadata URL is retained, and metadata is not
reported as full-text acquisition.

## Reproduction and production checks

```text
unit tests: 11/11 PASS
result-manifest entries: 8/8 PASS
Riemann-zero inputs: 0
fitted parameters: 0
network inputs to reproduction: 0
YAML parse for Stage-3 DEN/MOD records: PASS
XeLaTeX undefined citations/references: 0
missing characters: 0
overfull boxes: 0
underfull boxes: 0
LaTeX warnings: 0
PDF pages: 14
PDF visual checks: pp. 1, 4, 6, 10, 13, and 14 PASS
```

`pypdf` was unavailable for ARS preflight and is not reported as passed.
`pdfinfo`, `pdftotext`, and rendered-page inspection all succeeded.

## Frozen release

- PDF: `paper/paper.pdf`
- PDF SHA-256:
  `7ba58d4c389f476950125975c0c041e76d7691b8d0f769ab69ce319f8ed4fde7`
- Deninger Route-A record:
  `../../evaluations/route_a/DEN-WITT-Z-FIN/2026-08-13-stage3.yaml`
- Modular Route-A record:
  `../../evaluations/route_a/MOD-GEO/2026-08-13-stage3.yaml`
- Deninger overall: `ROUTE_A_EXPLORATORY`
- Modular rational-prime overall: `ROUTE_A_REJECTED`
- Route-B invocation: `false`

The frozen theorem rules out only the direct atomwise standard-clock DEN/MOD
splice.  It does not rule out a future source-derived morphism, time change,
non-atomic transform, or new arithmetic object.
