# P25 Round-3 direct return-map validation

## Material Passport

- Origin Skill: experiment-agent
- Origin Mode: run + validate
- Origin Date: 2026-08-27
- Verification Status: VERIFIED
- Version Label: p25_round3_direct_return_map_v1

## Execution result

- Round-2 finite-difference certified/open: 9 / 2232.
- Round-3 direct return-map certified/open: 2241 / 0.
- Newly certified rows: 2232.
- Deterministic replay verdict: `REPRODUCIBLE`.
- Core-output combined SHA-256: `78bb657056717711c49f67fe89fe13616421ea9e145ff12c3b0e63fba25f1534`.
- Round-2 input-ledger SHA-256: `25584d28155ac80f63260830816a9cdf3ec54b8587c07edac600765783ed2736`.

## Independent numerical path

Each row is reconstructed from its collision points and then refined as a
periodic point of the 100-decimal-digit physical ray-intersection/reflection
map.  The Jacobian is formed by central differences at `1e-28`, `1e-32`, and
`1e-36`.  Neither the direct map nor its Jacobian accepts a paraxial matrix as
input.  The Round-2 paraxial trace is read only as the final comparison target.
When rounded collision points lie outside the direct Newton cylinder, a
high-precision specular-stationarity solve refines the collision geometry; the
reported stability still comes exclusively from the direct return map.

The physical Birkhoff map and the positive-reflection paraxial convention differ
by one orientation sign per collision:

```text
trace(direct physical map) = (-1)^word_length * trace(paraxial product).
```

This convention accounts for 804
odd-length rows that the old signed comparison left open.  The remaining
1428 old open
even-length rows lie beyond the binary64 finite-difference conditioning window.

## Certified residual envelope

- Maximum post-refinement return residual: `9.836e-71`.
- Refinement methods: `{"DIRECT_RETURN_MAP_MDNEWTON": 2202, "SPECULAR_STATIONARITY_FALLBACK": 39}`.
- Maximum multiscale trace relative span: `5.791e-32`.
- Maximum finest-step determinant residual: `3.686e-23`.
- Maximum parity-corrected trace relative residual: `5.424e-15`.
- Maximum half-density relative residual: `3.955e-15`.
- Failure tiers: `{"NONE": 2241}`.

## Claim boundary

The direct validation closes the numerical return-map cross-check at the frozen
word and geometry cutoffs.  It does not turn finite numerical work into a
theorem, an exact determinant identity, an arithmetic owner, a formal A0--A4
tuple, or an A2/Route-B evaluation.  The aggregate half-density remains
`NUMERICAL_OBSERVATION`, and its use as arithmetic evidence remains
`STOP_SCOPED / PROVES_TOO_MUCH`.  No prime or zero table was used.

## Core file hashes

- `results/round3_stability_metrics.json`: `c835fba3ac66476075415fe9266b111f584d9dd049a8e612ccbe50534af0e477`
- `results/three_disk_return_map_validation_round3.csv`: `1b932a5ca3cf7123e9428b3eb2f26078d8e289eabb11dd828379ecf39eeb414e`
