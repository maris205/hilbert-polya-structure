# Code

The code is independent of the prior project's Python package. For \(a=6\)
catalogues through period 12 or beyond, it requires the hash-locked period-12
catalogue as a validation bridge; the two inherited proof documents are also
verified by the standalone checker.

## Entry points

| File | Purpose |
|---|---|
| henon_roof.py | symbolic enumeration, contraction lift, exact clock audit, cycle sections, roots, and controls |
| generate_catalog.py | complete orbit ledgers for one cutoff and parameter |
| analyze_roots.py | both orientation sectors, numerical winding audits, high-precision refinement, and staged matching |
| run_controls.py | frozen random, exact-parent, and neighboring-parameter controls |
| summarize_results.py | strict JSON/CSV/Markdown analysis |
| make_figure1.py | vector paper figure from persisted analysis JSON |
| make_paper_includes.py | result-dependent figure caption and primary-artifact hash rows |
| check_results.py | standalone read-only reconstruction that does not import the producer module |
| build_manifest.py | SHA-256 repository handoff manifest |
| run_all.sh | complete regeneration, tests, paper compilation, and manifest |

## Fast verification

    python henon_instability_roof_zeta/code/check_results.py
    pytest -q henon_instability_roof_zeta/code/tests

The recorded independent audit passes 38/38 checks; the unit suite passes 7/7.
The full run_all.sh pipeline is CPU-only, but the period-20 root and control
stages take several minutes.
