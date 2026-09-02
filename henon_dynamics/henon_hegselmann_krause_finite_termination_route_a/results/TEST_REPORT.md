# C312 test report

| lane | result |
|---|---|
| producer | 801 cases / 1,843 states / 28,895 leaves |
| independent checker | 28,870 checks, PASS |
| SymPy | 38 exact identities, PASS |
| isolated replay | byte-identical, PASS |
| hostile mutation | 26/26 rejected |
| release | exact ledger and deterministic PDF rounds |

The checker reconstructs every rational state, graph transition, threshold
contact, trajectory hash, mean, final cluster, permanent component, and time
bound without importing the producer.
