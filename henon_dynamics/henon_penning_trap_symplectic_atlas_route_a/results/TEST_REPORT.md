# Test report

## Commands

All commands run from the repository root with bytecode disabled:

```bash
python -B henon_dynamics/henon_penning_trap_symplectic_atlas_route_a/code/c274_penning_producer.py
python -B henon_dynamics/henon_penning_trap_symplectic_atlas_route_a/code/c274_penning_checker.py
python -B henon_dynamics/henon_penning_trap_symplectic_atlas_route_a/code/c274_penning_sympy_crosscheck.py
python -B henon_dynamics/henon_penning_trap_symplectic_atlas_route_a/code/c274_penning_replay.py
python -B henon_dynamics/henon_penning_trap_symplectic_atlas_route_a/code/c274_penning_mutation.py
```

## Outcomes

- Producer: PASS — 48 flow rows, 24 mode rows, 13 strobe rows, 7 period
  rows, 9 boundary rows, 2,743 numeric cells.
- Independent checker: PASS — 3,664 assertions.  It imports no producer code.
- SymPy cross-check: PASS — 96 independently derived symbolic identities.
- Fresh replay: PASS — 180,061 bytes and exact SHA-256 equality.
- Hostile mutation audit: PASS — 26/26 repaired-hash corruptions rejected.

The tests cover generator and gauge conventions, canonical symplecticity,
energy and semigroup laws, stable frequencies and signed actions, every regime
and boundary, field-sign conjugacy, active-mode periods, strobe fixed spaces,
metadata, Route-A literals, and forbidden claim flags.

The release gate additionally checks both formal citation keys, their distinct
model-lineage/terminology roles, the explicit no-proof-outsourcing sentence,
and both APS DOI literals in the final PDF.  These are source-traceability
checks, not mathematical dependencies.

## Evidence boundary

The continuum theorem is proved analytically.  These finite tests guard
implementation, transcription, and release integrity; they are not used as a
numerical proof of global boundedness or periodicity.
