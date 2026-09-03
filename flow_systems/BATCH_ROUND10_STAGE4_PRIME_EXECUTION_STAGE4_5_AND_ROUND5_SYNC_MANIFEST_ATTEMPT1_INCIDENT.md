# Round 10 publication-manifest attempt 1 incident

Date: **2026-09-04 UTC**

Status: **OUTER ALLOWLIST BUILDER CORRECTED BEFORE OUTPUT**

The first sync-manifest builder invocation stopped before emitting a manifest
because its recursive `stage4_prime_*` selection saw Python bytecode beneath a
`__pycache__` directory and the safety assertion correctly rejected the cache
path. No file was copied, staged, committed, or pushed. The builder was changed
to filter private/cache paths before validating the final explicit allowlist;
the prohibition on private payloads, bytecode, nested Git metadata, unrelated
legacy files, canonical papers, science/results, initial systems, and Route
files remains unchanged.
