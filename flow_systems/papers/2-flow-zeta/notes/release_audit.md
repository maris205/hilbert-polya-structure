# Paper 2 release audit

Date: 2026-08-13  
Decision: **PASS / ACCEPTED AFTER MINOR REVISION**

## Independent review closure

The reviewer recommendation in `peer_review_round1.md` was minor revision.
All required items were closed:

- the real `sigma <= 0` branch was added to the abscissa proof;
- the component theorem now names componentwise `*`-algebras, positive
  traces, and an invariant `*`-automorphism action;
- nonintegral formal masses use the power-series logarithm on the stated
  absolute-convergence half-plane;
- N2 now distinguishes normalized Haar probability on each individual
  homogeneous circle from a source-canonical packet assembly and trace
  coefficient;
- abstract, claim ledger, and YAML retain the proved ordinary-product failure
  / enriched-alternative `NOT_TESTABLE` split;
- Deninger manifestations and the 2022 arXiv erratum are named explicitly;
- the trace-gate figure and all overfull lines were repaired.

The citation audit's mandatory bibliography changes were also closed:

- Bourgeois is recorded as the Fields Institute Communications chapter;
- Renault's AMS volume title is corrected;
- Kordyukov's St. Petersburg Mathematical Journal publication is recorded;
- GLP erratum author ordering follows the audited PDF title page;
- the Fried benchmark is narrowed to the cited compact/Fuchsian setting.

## Reproduction and production checks

```text
unit tests: 5/5 PASS
Riemann-zero inputs: 0
fitted packet masses: 0
fitted scales: 0
YAML parse/schema-critical assertions: PASS
XeLaTeX undefined citations/references: 0
missing characters: 0
overfull boxes: 0
PDF pages: 20
PDF visual checks: pp. 1, 7, 13, 14, 15, 16, and bibliography PASS
```

`qpdf --check` was not available in the environment and is therefore not
reported as passed.  `pdfinfo` and `pdftotext` both read the final release PDF
successfully.

## Frozen release

- PDF: `paper/paper.pdf`
- PDF SHA-256:
  `86a60810f1f2a975bc5e694cb854a7de4bb796168f9a273888c013f84323a183`
- Route-A record:
  `../../evaluations/route_a/DEN-WITT-Z-FIN/2026-08-13-stage2.yaml`
- Overall verdict: `ROUTE_A_EXPLORATORY`
- Route-B invocation: `false`

The paper proves failure only for the conventional individual-orbit product.
It does not assert universal nonexistence of a measured, groupoid, or
cohomological enrichment.

