# HCS-C133 — exact unitary quantum-graph scattering

C133 is a source-locked metric quantum graph on two vertices joined by three
edges of lengths `1,2,3`.  Degree-three Kirchhoff conditions give a rational
directed-bond scattering matrix.  Symmetric half-edge propagation produces a
unitary family on `C^6`, an exact antiunitary reversal, a closed secular
determinant, and an all-period primitive bond-orbit product.

This is the first package in the working series to reach the strict coordinate
`A4_UNITARY_OR_SCATTERING_CANDIDATE`.  It does not compare the secular divisor
with any external target, so A2/A3 remain failed and Route B is unauthorized.

## Reproduce

Run from this directory:

```bash
python3 code/c133_quantum_graph_producer.py
python3 code/c133_quantum_graph_checker.py
python3 code/c133_sympy_crosscheck.py
python3 code/c133_replay.py
python3 code/c133_mutation.py
python3 code/c133_release_manifest.py
```

The release ledger excludes only itself and transient build/cache files.  The
active firewall is `NO_BAD_EULER_OR_ROOT_NUMBER` and
`route_b_invocation_allowed: false`.
