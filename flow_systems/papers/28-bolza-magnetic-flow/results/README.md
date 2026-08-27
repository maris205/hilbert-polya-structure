# P28 results and planned orbit ledger

## Round-3 source-bound trace contract

`round3_trace_regime_contract.csv` contains 12 rows for
`b=0,+1/2,-1/2` at common even powers `N=2,4,8,16`.  It freezes the operator,
semiclassical scale, transformed spectral center/window, unit-speed classical
shell, source parameter map, primitive period/action factors, and every owner
firewall.  `round3_trace_regime_validation.json` records a PASS: eight signed
field rows are source-bound, four zero-field control rows remain open, no row
assigns a formal Route-A tuple, and no fixed-operator credit is allowed.

The signed-field result depends on the explicit modeling choice that the
degree-one connection is a square root of the source's `B=1` quantization
connection.  The ledger contains no eigenvalues or orbit samples.

## Round-2 owner ledger

`bolza_tensor_family_owner_ledger.csv` contains 12 exact owner rows for
`b=0,+1/2,-1/2` at common tensor powers `N=1,2,4,8`. It records bundle degrees,
named Hilbert/operator owners, antiunitary and classical field-reversal
partners, holonomy repetition, and the prohibition on fixed-operator credit
transfer. Its validation is in `round2_owner_ledger_validation.json`.

This file contains no primitive magnetic orbit, eigenvalue, or trace data.
The `h=1/N` column is a `MODELING_CHOICE`; the rescaled operator and trace
regime remain `UNASSIGNED`, the energy window remains `OPEN`, and all orbit
ownership fields remain `NOT_ESTABLISHED`.

## Planned magnetic-orbit ledger

No magnetic-orbit data is claimed.  Planned
`bolza_semiclassical_tensor_trace_ledger.csv` columns:

```text
field_b,bundle_degree,tensor_power_N,energy_window,trace_regime,
primitive_id,repetition,period,stability,
connection_holonomy,maslov_phase,symmetry_sector,
time_reversal_partner,metric_control_id,cutoff_risk,evidence_token
```

Schema semantics:

- `bundle_degree` is the base-bundle degree: `0,+1,-1` for
  `b=0,+1/2,-1/2`.  At `tensor_power_N=N`, the actual operator-bundle degree is
  `N*bundle_degree`.
- `b=-1/2` uses the dual bundle `L^*`; its tensor family is
  `Δ^{(L^*)^N}`.
- `energy_window` records the exact `N`-dependent or rescaled spectral window.
  Round 3 now binds it for the source-compatible even-subsequence subtype; it
  remains open outside that scope.
- `trace_regime` must be either `SEMICLASSICAL_TENSOR_POWER` or the explicitly
  separate `FIXED_OPERATOR_HIGH_ENERGY_CONTROL`; rows from the two regimes may
  not be pooled.
- `evidence_token` must be one of
  `PROVED|HEURISTIC|MODELING_CHOICE|OPEN`.

The `b=0,+1/2,-1/2` runs must share the same `tensor_power_N`, energy-window
convention, trace regime, normalization, and orbit-selection rule.  Future
numerical orbit rows may cite `PROVED` trace ownership only for the frozen
source-compatible signed-field even subsequence and only with its clock and
orientation conventions.  Zero-field, odd-`N`, arbitrary-twist, full all-`N`,
and fixed-operator rows remain `OPEN` / `NOT_ESTABLISHED`.

```text
FIXED_OPERATOR_HIGH_ENERGY_TRACE=OPEN
FIXED_OPERATOR_MAGNETIC_ORBIT_OWNERSHIP=NOT_ESTABLISHED
```
