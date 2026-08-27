# P24 Round-2 results

The following deterministic artifacts were generated on 2026-08-27:

- `bianchi_complex_length_ledger_round2.csv` — 11,481 unique exact matrices;
- `bianchi_holonomy_shuffle_control_round2.csv` — 10,944 target-free control rows;
- `round2_metrics.json` — aggregate counts, residuals, scope markers, and Route state.

The main ledger records:

```text
representative_word,matrix,determinant,level3_membership,matrix_class,
trace_re,trace_im,complex_length_re,holonomy_angle,
symbolic_cyclic_class,symbolic_root,symbolic_repetition_exponent,
exact_power_root_id,exact_power_exponent,primitive_status,
orientation_pair_id,orientation,word_collision_multiplicity,
trace_collision_multiplicity,parabolic_cusp_risk,completeness_boundary
```

`[NUMERICALLY_CERTIFIED]` covers exact matrix arithmetic and the stated finite
word ball.  `primitive_status=PRIMITIVE_WITHIN_WORD_BALL_NOT_GROUP_CERTIFIED`
is deliberately not a full-group primitive claim.  Parabolic rows are retained
and marked as cusp elements; continuous-spectrum/scattering terms are not
computed.

Arithmetic validation must use a separate post-freeze join table with
`gaussian_prime_ideal`, `norm`, `rational_prime`, `split_type`,
`ramification_index`, `ideal_power`, and `owner_multiplicity`.  It may not alter
the orbit rows or cutoff.  The primary target is `zeta_{Q(i)}`; the rational-
prime join is secondary and receives no automatic Riemann-`zeta` A0 credit.
No such join table was generated in Round 2.
