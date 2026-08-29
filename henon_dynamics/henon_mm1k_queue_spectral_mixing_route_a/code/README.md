# C225 code map

| file | role |
|---|---|
| `c225_mm1k_producer.py` | canonical exact-rate/high-precision evidence generator |
| `c225_mm1k_checker.py` | independent schema, formula, kernel, boundary and matrix spot-check |
| `c225_mm1k_sympy_crosscheck.py` | exact symbolic generator/Jacobi/Chebyshev identities |
| `c225_mm1k_replay.py` | clean temporary-process byte replay |
| `c225_mm1k_mutation.py` | repaired-hash, nested-unknown and stale-hash hostile tests |
| `c225_release_manifest.py` | 27-payload closure, PDF, source and gate manifest |

All scripts use only source-defined rates and finite queue states.  The checker
intentionally does not import the producer.  Run from the package root with
`python -B`; the manifest invokes the five audits again in clean subprocesses.
