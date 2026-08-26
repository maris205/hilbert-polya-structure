# C181 executable contract

- `c181_rotor_router_producer.py`: exact graph, state, orbit, and frequency evidence.
- `c181_rotor_router_checker.py`: independent graph census, Leibniz cofactors, state enumeration, and orbit audit.
- `c181_sympy_crosscheck.py`: matrix-tree, kernel, Eulerian, trace, and selected full permutation-determinant checks.
- `c181_replay.py`: byte-identical evidence replay.
- `c181_mutation.py`: 25 repaired-hash semantic mutations and one stale-hash mutation.
- `c181_release_manifest.py`: Route-A v0.2 source-lock/artifact semantics and self-excluded release closure.

No producer code is imported by the checker. Every arc is represented by its own identifier, so parallel arcs remain distinguished. Finite enumeration is validation, not proof.
