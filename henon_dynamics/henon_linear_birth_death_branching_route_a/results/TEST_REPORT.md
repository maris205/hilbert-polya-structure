# Test report

All commands were run from repository root on 2026-08-27.

## Executable suite

```text
$ python henon_dynamics/henon_linear_birth_death_branching_route_a/code/c208_branching_producer.py
C208_PRODUCER_PASS; cases=13; semigroup_cases=9; exact_identities=1232;
payload_sha256=2be1666222c3cb7dbc407d571f0bc9c3d695b19b54067b105f15a9c02c5b3cf5

$ python henon_dynamics/henon_linear_birth_death_branching_route_a/code/c208_branching_checker.py
C208_CHECKER_PASS; assertions=2194; recursive_key_sets=96;
exact_scalar_identities=1232; producer_imported=false

$ python henon_dynamics/henon_linear_birth_death_branching_route_a/code/c208_branching_sympy_crosscheck.py
C208_SYMPY_PASS; checks=1009; generic_symbolic_checks=34;
evidence_coefficient_checks=845; evidence_moment_checks=130;
long_time_regimes=3

$ python henon_dynamics/henon_linear_birth_death_branching_route_a/code/c208_branching_replay.py
C208_REPLAY_PASS; bytes=76842

$ python henon_dynamics/henon_linear_birth_death_branching_route_a/code/c208_branching_mutation.py
C208_MUTATION_PASS; repaired_hash_rejections=22;
stale_hash_rejections=1; unknown_key_rejections=2; total_rejections=23
```

## PDF and release checks

Each revision was built twice with LuaLaTeX under
`SOURCE_DATE_EPOCH=1787788800`, using revision selectors 0, 1 and 2. The
three PDFs have distinct content and SHA-256 values. Two additional fresh
round-2 builds and released `main.pdf` were byte identical at
`b69dddd4ca490c5df40f294705807486c21a47257695348a9dc4b3a7d1815325`.

The final PDF has four A4 pages and 203,066 bytes. All 24 fonts are embedded
and subset. `pdftotext` extracted 2,136 words and 12,715 bytes, including the
exact scope literal `NO_BAD_EULER_OR_ROOT_NUMBER`. Final and
revision logs contain no warning, overfull, underfull, undefined-reference or
missing-character line. All four rendered pages were inspected at 120 dpi;
no clipping, collision, truncation or unreadable element was found.

The release-manifest command verifies the exact 27-payload path set, evidence
and PDF content addresses, three distinct revisions, final/round-2 equality,
scope flags, Route-A tuple, text extraction, font embedding/subsetting, absence
of sidecars, and 28 physical files including its self-excluded manifest.
