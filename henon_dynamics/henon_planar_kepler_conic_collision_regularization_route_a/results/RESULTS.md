# Results

The current canonical receipt is `c216_kepler_evidence.json`.

| Ledger | Count | Meaning |
|---|---:|---|
| exact orbit rows | 10 | elliptic, parabolic, and hyperbolic probes |
| radial collision rows | 4 | two bound, one parabolic, one positive-energy inward branch |
| Levi–Civita rows | 12 | nine regular lifts plus three collision configurations |
| fixed-set rows | 5 | three negative-energy shells and two nonperiodic boundaries |
| exact identity cells | 58 | zero residuals and exact reconstructed quantities |

The checker passes 260 assertions, the SymPy cross-check passes 17 checks, replay is byte exact, and the mutation harness rejects 24 repaired-hash semantic mutations plus one stale-hash mutation (25 total; an unknown-key mutation is included).  All numbers are finite regression evidence; the theorem package carries the continuum statements.

The Route-A tuple is `(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`, overall rejected, Route B false.
