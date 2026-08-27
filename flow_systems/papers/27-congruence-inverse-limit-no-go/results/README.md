# P27 results

The current result is analytic: `[PROVED]` the total inverse-limit flow has no
periodic points.  This carries the local progress tag
`PROVED_A1_OBSTRUCTION`, not a formal A1 verdict.  A finite-level diagnostic may
still be useful but receives no limit-flow orbit credit.

The planned diagnostic is now landed as
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
