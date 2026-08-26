# Test report

All executable tests passed on 2026-08-26 from repository commit `bbb809ee198bc9ad5f196383baab1e3d9de38e43`.

```text
C181_PRODUCER_PASS graphs=1629 order_audits=1697 census=1/18/1606
C181_CHECKER_PASS assertions=93786
C181_SYMPY_PASS checks=24890 determinant_graphs=23 sympy_version=1.14.0
C181_REPLAY_PASS bytes=2860684 sha256=48f5f825d26909aa6998dc45f4192e86a2e36bd3c95906c7d66dbb00b0079754
C181_MUTATION_PASS repaired_hash_rejections=25 stale_hash_rejections=1
```

The independent checker uses a Leibniz determinant rather than the producer’s rational elimination and reconstructs the graph and state ledgers without importing producer code. SymPy recomputes every matrix-tree cofactor and kernel identity and forms 23 full permutation determinants. Mutation tests recompute the embedded hash before semantic validation.

Paper and manifest audits are recorded separately.
