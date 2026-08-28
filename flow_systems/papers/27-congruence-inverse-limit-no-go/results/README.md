# P27 results

The current result is analytic: `[PROVED]` the total inverse-limit flow has no
periodic points.  This carries the local progress tag
`PROVED_A1_OBSTRUCTION`, not a formal A1 verdict.  A finite-level diagnostic may
still be useful but receives no limit-flow orbit credit.

The Round-2 diagnostic is landed as
`round2/congruence_reduction_order_ledger.csv` with 24 rows.  Its main columns
are:

```text
element_id,positive_word,matrix_a,matrix_b,matrix_c,matrix_d,
positive_word_primitive,gamma3_class_primitivity,base_geodesic_length,
level_n,modulus_q,quotient_convention,psl_order_sequential,
psl_order_group_bound,order_crosscheck,terminal_scalar_sign,
previous_order_divides,bonding_compatibility,cumulative_common_multiplier,
finite_level_period_scale,finite_level_closed_lift_period,statistic_owner,
inverse_limit_flow_credit,evidence_status
```

The internally prespecified first eight levels use the actual modulus
`q_n=3 n!`:

| `n` | `q_n` |
|---:|---:|
| 1 | 3 |
| 2 | 6 |
| 3 | 18 |
| 4 | 72 |
| 5 | 360 |
| 6 | 2160 |
| 7 | 15120 |
| 8 | 120960 |

All eight levels were executed for three matrices.  Direct and independent
orders agree `24/24`; the largest observed projective order is `2880`.
All `21/21` nontrivial adjacent-level bonding/divisibility transitions pass;
the other three ledger rows are the level-1 initializations.
Canonical hashes are recorded in `round2/manifest.json`.  A byte-identical
second generation is retained under `reproduction_run2/`.

These `[NUMERICALLY_CERTIFIED]` rows describe finite-level lift behavior, not
periodic points of the inverse limit.  Normality is tied to the kernel
description of `Gamma(q)`, the PSL sign convention is explicit, and common-time
compatibility is separate from each finite-quotient order.  A2--A4 remain
`NOT_EVALUATED`; the formal Route-A tuple and overall status remain
`UNASSIGNED`.

## Round-4 period-escape audit

- `round4_period_escape_ledger.csv` rewrites the same 24 finite owners in the
  theorem's quotient-order/whole-`g`-loop closing-time schema; and
- `round4_period_escape_validation.json` records nested-modulus checks, all
  frozen sequences, growth/plateau counts, theorem-versus-finite-evidence
  separation, and unchanged Route firewalls.

Every period-to-base ratio equals the finite quotient order.  The last observed
orders are `288`, `2880`, and `576`; finite-prefix growth is
`NUMERICALLY_CERTIFIED`.  Asymptotic divergence is owned by the separate
`[PROVED]` group-theoretic theorem, not extrapolated from these rows.
The recorded time is minimal among whole traversals of the chosen `g`-loop; it
is not asserted to be an underlying primitive orbit's minimal period unless
conjugacy primitivity is separately proved.

## Round-5 cocompact control

- `round5_cocompact_homology_escape_ledger.csv` contains 24 rows for three
  primitive-homology owners across the eight factorial levels; and
- `round5_cocompact_homology_escape_validation.json` records the exact modular
  homology orders, nesting, primitivity certificates, computation boundary,
  owner firewall, and unchanged Route states.

Each owner has the certified quotient-order lower-bound sequence
`1,2,6,24,120,720,5040,40320`.  The corresponding minimal lifted-geodesic
period is at least that factor times its symbolic base length.  These are exact
homology quotient bounds; the canonical residual cores and full finite
quotients are intentionally not enumerated.  The general cocompact theorem is
`[PROVED]` in the accompanying note, while the serialized finite ledger is
`[NUMERICALLY_CERTIFIED]`.
