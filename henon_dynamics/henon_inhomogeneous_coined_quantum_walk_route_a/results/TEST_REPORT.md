# Test report

All exact tests passed on 25 August 2026.

| test | result |
|---|---|
| producer | PASS |
| independent checker | PASS, 62 assertions |
| separate SymPy reconstruction | PASS, 39 checks |
| canonical byte replay | PASS |
| repaired-hash semantic mutations | PASS, 29/29 |
| stale-hash sentinel | PASS, 1/1 |

Evidence SHA-256:
`07873e5ad9a1939177833946d5c6d611b494bb3258d8e67857afa3948d84d65b`.

No test takes an absolute value in place of a signed amplitude.  Absolute
matrix entries are used only for the raw-product convergence bound.

The final uniform batch gate repeats isolated PDF builds, manifest closure,
and visual inspection.
