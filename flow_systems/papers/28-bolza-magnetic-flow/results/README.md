# P28 planned results

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
- `energy_window` records the exact `N`-dependent or rescaled spectral window;
  it remains `OPEN` until source-bound.
- `trace_regime` must be either `SEMICLASSICAL_TENSOR_POWER` or the explicitly
  separate `FIXED_OPERATOR_HIGH_ENERGY_CONTROL`; rows from the two regimes may
  not be pooled.
- `evidence_token` must be one of
  `PROVED|HEURISTIC|MODELING_CHOICE|OPEN`.

The `b=0,+1/2,-1/2` runs must share the same `tensor_power_N`, energy-window
convention, trace regime, normalization, and orbit-selection rule.  No row may
assign same-owner trace correspondence an evidence status stronger than
`OPEN`; the exact pipeline ownership state remains `NOT_ESTABLISHED`.

```text
FIXED_OPERATOR_HIGH_ENERGY_TRACE=OPEN
FIXED_OPERATOR_MAGNETIC_ORBIT_OWNERSHIP=NOT_ESTABLISHED
```
