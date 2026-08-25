# C148 test report

| Test | Result |
|---|---|
| exact producer | PASS |
| producer-independent standard-library checker | PASS, 748 assertions |
| independent SymPy reconstruction | PASS, 141 checks |
| direct `B_k^k=A^(tensor k)` source vectors | PASS, 363/363 |
| direct trace formula sentinels | PASS, 60/60 |
| exact characteristic coefficient cells | PASS, 67/67 |
| exact polynomial degrees `2^k`, `k=1,...,5` | PASS |
| complex primitive path replay | PASS, periods 1--8 at `k=2` |
| closed/unitary, order-isospectral, hole-sensitive controls | PASS |
| canonical byte replay | PASS |
| repaired-hash semantic mutations | PASS, 40/40 rejected |
| stale-payload-hash mutation | PASS, 1/1 rejected |
| isolated fixed-epoch double PDF build | PASS, both byte-identical to release PDF |
| embedded fonts and clean final logs | PASS |
| two-page visual inspection | PASS |
| release-manifest closure | PASS, 27/27 payload files after manifest generation |

The checker imports no producer module.  SymPy uses literal low-`k` matrices
and a separately reconstructed characteristic recurrence.  Finite trace and
path prefixes are implementation sentinels; the all-period statements are
proved in `THEOREM_PACKAGE.md`.
