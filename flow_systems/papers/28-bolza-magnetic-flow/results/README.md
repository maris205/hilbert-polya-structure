# P28 results and owner ledgers

## Round-5 bounded matched marked-cyclic census

`round5_bolza_marked_cyclic_census.csv` contains 390 canonical records for all
freely and cyclically reduced marked words of length at most four, modulo
cyclic rotation and inversion.  The length counts are `4,16,60,310`; 366 rows
are marked-primitive candidates and 24 are explicit powers.  The artifact is
complete for that declared finite equivalence only.  It is not called a full
`Gamma`-conjugacy census.

Every row carries its marked root/repetition, exact matrix and inverse-paired
matrix hashes, exact trace and trace squared, 120-decimal length, exact
primitivity margin, homology vector/axis, owner-credit state, completeness
boundary, and route firewalls.  Exact arithmetic in
`Q(s,t,i)`, `s^2=2`, `t^2=1+s`, `i^2=-1`, finds no literal PSL matrix or
inverse collisions.  Equal trace squared is recorded only as an isospectral
group and never as a conjugacy certificate.

The exact `ell<2ell_B` test proves `Gamma` primitivity for 44 rows.  These
occupy 36 homology axes modulo sign.  `primitive_axis_owner_id` is assigned to
exactly one proved row per such axis; eight other proved primitives sharing an
axis are withheld, and 322 marked-primitive rows retain
`NOT_ESTABLISHED_MARKED_PRIMITIVE_ONLY`.  Thus no unresolved record creates a
second owner credit.

`round5_bolza_magnetic_branch_ledger.csv` contains only the 36 credited owners
per field at `k=+-1,+-2,+-3,+-4`: 288 rows per field and 576 total, split into
144 `|k|=1` branch rows and 432 repetition rows.  It retains the Round-4
inverse-paired owner convention, both partner involutions, the signed trace
time/action/stability laws, all regime firewalls, and 48/48 historical seed
compatibility checks.

Supporting artifacts are:

- `round5_bolza_marked_cyclic_certificate.json` — exact field, relator,
  normal-form, count, equality/inverse, trace-isospectral, primitivity, and
  distinctness certificates;
- `round5_bolza_marked_cyclic_validation.json` — `PASS` with row/law/partner,
  target-data, route, and Round-4 compatibility totals; and
- `round5_nonarithmetic_control_contract.json` — a design-only source and
  parameter contract.  It selects no geometry and reports no control result.

## Round-4 explicit Bolza magnetic-owner seed

`round4_bolza_magnetic_owner_ledger.csv` is the first genuine conjugacy/orbit
artifact.  It contains 48 target-free rows:

```text
4 inverse-paired primitive side-pairing axis owners per field
x 6 signed source branches (k=+-1,+-2,+-3)
x 2 signed fields
= 48 rows.
```

For each field there are four owner IDs, eight `|k|=1` primitive branches, and
24 signed trace branches.  The 16 `|k|=1` rows across both fields are branch
rows, not owner rows.  Every row records the inverse-pair definition, canonical
and branch words, signed `k`, primitive versus repetition branch status,
signed-`k` and field partners, the exact Bolza trace/norm/length, signed trace
time, absolute physical period, project even-`N` action coefficient, phase,
Maslov index, ordered `N_B^k,N_B^-k` Poincare multipliers, absolute stability
root, equation-(19) signed denominator, and all regime firewalls.  Field
reversal is `(b,axis,k)->(-b,same axis,-k)`.

`f_j` and `f_j^-1` are recorded as nonconjugate in `Gamma`, but they share one
inverse-paired axis-owner ID in this no-double-counting schema.  The negative
branch is not a second owner credit.  `round4_bolza_group_certificate.json`
records the published matrix source lock and 120-decimal transcription replay;
`round4_bolza_owner_validation.json` records `PASS`.

The exact scope is four primitive side-pairing owners only.  This is not a
complete Bolza primitive or systolic spectrum.  It assigns no rational-prime
or prime-ideal labels, and it does not contain eigenvalues or numerically
integrated trajectories.

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

## Extension schema beyond the Round-5 finite artifact

The Round-5 artifact now instantiates the central owner columns for the safely
credited finite subset.  The non-arithmetic control and later common-cutoff
comparison must preserve:

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
orbit rows may cite `PROVED` trace ownership only for the frozen
source-compatible signed-field even subsequence and only with its clock and
signed-`k`/inverse-pair conventions.  A new owner row also needs a certified
group normal form or another explicit primitivity and conjugacy/distinctness
certificate.  Marked-cyclic completeness alone is insufficient for full
`Gamma`-conjugacy credit.  Zero-field, odd-`N`,
arbitrary-twist, full all-`N`, and fixed-operator rows remain `OPEN` /
`NOT_ESTABLISHED`.

```text
FIXED_OPERATOR_HIGH_ENERGY_TRACE=OPEN
FIXED_OPERATOR_MAGNETIC_ORBIT_OWNERSHIP=NOT_ESTABLISHED
```
