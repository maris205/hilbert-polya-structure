# HCS-C348: one-dimensional iid RWRE Solomon phase theorem

This package gives one complete theorem for a nearest-neighbour random walk in
an iid static environment: quenched finite-interval hitting probabilities,
direction from \(\mathbf E\log\rho\), annealed almost-sure velocity including
transient zero-speed phases, and full Beta and constant-environment faces.

The release contains analytic proofs, exact finite regression evidence, an
independent checker, a SymPy lane, isolated replay, hostile mutations, strict
Route-A evaluation, three substantive paper revisions, and deterministic PDF
gates.

Run from this directory:

```text
python -B code/c348_rwre_producer.py
python -B code/c348_rwre_checker.py
python -B code/c348_rwre_sympy_crosscheck.py
python -B code/c348_rwre_replay.py
python -B code/c348_rwre_mutation.py
python -B code/c348_release_manifest.py
```

Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.  The strict Route-A tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; overall verdict is
`ROUTE_A_REJECTED`, and Route B is false.
