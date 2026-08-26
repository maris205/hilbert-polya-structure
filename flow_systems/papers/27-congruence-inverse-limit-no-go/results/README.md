# P27 planned results

The current result is analytic: `[PROVED]` the total inverse-limit flow has no
periodic points.  This carries the local progress tag
`PROVED_A1_OBSTRUCTION`, not a formal A1 verdict.  A finite-level diagnostic may
still be useful but receives no limit-flow orbit credit.

Planned `congruence_lift_ledger.csv` columns:

```text
base_matrix,base_primitive,length,level_n,modulus_q,finite_quotient_order,
lift_representative_eta_n,conjugate_eta_gamma_power_eta_inverse,
gamma_power_in_Gamma_q,closed_lift_period,lift_multiplicity,normalized_mass,
same_time_compatibility,normality_check,trivial_product_control
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

These `[OPEN]` rows describe finite-level lift behavior, not periodic points of
the inverse limit.  The ledger must retain the compatible-lift representative
`eta_n`, verify normality before replacing conjugate membership by
`gamma^m in Gamma(q_n)`, and keep the common-time condition separate from the
finite-quotient reduction order.  A2--A4 remain `NOT_EVALUATED`; the formal
Route-A tuple and overall status remain `UNASSIGNED`.
