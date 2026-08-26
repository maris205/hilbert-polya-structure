# P24 planned results

Stage 1 has frozen the schema but has not generated numerical orbit data.

Planned `bianchi_complex_length_ledger.csv` columns:

```text
word,matrix_trace,loxodromic,primitive_root,repetition,
length,holonomy_angle,orientation,holonomy_weight,
cutoff_complete_risk,shuffle_control_id
```

Any table produced later must be enumerated without a prime or Riemann-zero
lookup and must retain cusp/scattering limitations.

Arithmetic validation must use a separate post-freeze join table with
`gaussian_prime_ideal`, `norm`, `rational_prime`, `split_type`,
`ramification_index`, `ideal_power`, and `owner_multiplicity`.  It may not alter
the orbit rows or cutoff.  The primary target is `zeta_{Q(i)}`; the rational-
prime join is secondary and receives no automatic Riemann-`zeta` A0 credit.
