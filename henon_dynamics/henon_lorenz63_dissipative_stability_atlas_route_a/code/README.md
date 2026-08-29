# C227 code

The producer writes a canonical source-local Lorenz-63 theorem ledger.  The
checker independently reconstructs every frozen row and rejects unknown
schema material; the SymPy program reconstructs the generic identities; the
replay test compares clean-process bytes; and the mutation harness checks
semantic, schema, provenance, scope and stale-hash failures.

Run from the repository root:

```bash
python henon_dynamics/henon_lorenz63_dissipative_stability_atlas_route_a/code/c227_lorenz_producer.py
python henon_dynamics/henon_lorenz63_dissipative_stability_atlas_route_a/code/c227_lorenz_checker.py
python henon_dynamics/henon_lorenz63_dissipative_stability_atlas_route_a/code/c227_lorenz_sympy_crosscheck.py
python henon_dynamics/henon_lorenz63_dissipative_stability_atlas_route_a/code/c227_lorenz_replay.py
python henon_dynamics/henon_lorenz63_dissipative_stability_atlas_route_a/code/c227_lorenz_mutation.py
python henon_dynamics/henon_lorenz63_dissipative_stability_atlas_route_a/code/c227_release_manifest.py
```

The checker does not import the producer.  Exact rational strings are used
for theorem rows; numerical orbit classification is intentionally absent.
