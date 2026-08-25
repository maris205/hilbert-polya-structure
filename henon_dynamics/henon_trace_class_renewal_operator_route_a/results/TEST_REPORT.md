# Test report

All commands were rerun from the package root on 25 August 2026.

| test | result |
|---|---|
| deterministic producer | PASS |
| independent checker | PASS, 110 assertions |
| separate SymPy reconstruction | PASS, 56 checks |
| canonical byte replay | PASS |
| semantic mutations | PASS, 24/24 repaired-hash rejections |
| stale-hash sentinel | PASS, 1/1 rejection |

Evidence file SHA-256:
`2206007b8c0008c8529ce5e421ad34c6c8a92498e95300b7a10f594c63fae5a2`.

The finite replay does not prove the infinite statements.  The trace-class,
determinant, entire-order, and primitive-product results have independent
all-order proofs in `THEOREM_PACKAGE.md` and the paper.

The final release additionally requires manifest closure and two isolated
fixed-epoch PDF rebuilds; their final hashes are recorded after those gates.
