# C309 test report

Required lanes:

| lane | expected result |
|---|---|
| canonical producer | `C309_PRODUCER_PASS` |
| independent checker | at least 1,300 checks, PASS |
| SymPy | 74 identities, PASS |
| isolated replay | archived SHA-256, PASS |
| hostile mutation | 34/34 rejected |
| release verifier | exact ledger, deterministic PDFs, PASS |

The checker does not import the producer.  It refuses optimized Python,
duplicate keys, nonfinite JSON, stale payload hashes, wrong types, altered
spectra/poles/flows/Loewner factors, damaged Morse--Bott dimensions, scope
escalation, and Route-B activation.
