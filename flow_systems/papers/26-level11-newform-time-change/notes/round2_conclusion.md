# P26 Round-2 conclusion

## Outcome

Round 2 produced a deterministic, auditable finite ledger for the frozen
level-11 newform time-change candidate.  Among 125 primitive positive
hyperbolic `LR` necklaces through word length 9, exactly 11 left-to-right word
matrices satisfy `c mod 11=0`.  The generated artifacts bind each row to its
exact word, matrix, primitive root/exponent, orientation, and geodesic length.

This statement is deliberately finite: positive necklaces through cutoff 9
are not a complete set of hyperbolic conjugacy classes of `Gamma_0(11)`.

## Numerical period evidence

For each selected axis, the generator numerically integrates
`Re(2 pi i eta(z)^2 eta(11z)^2 dz)`.  The primary calculation uses q cutoff
192 and 1024 Simpson panels.  Independent calculations test cutoff 48,
512 panels, an axis-coordinate basepoint shift, reversed orientation, and a
direct symmetric `M^2` axis integral.  The repeated-orbit calculation uses q
cutoff 4096 and 512 panels, with independent 2048-cutoff and 256-panel checks.
Under the frozen exact law
`T_epsilon=ell+epsilon integral_gamma alpha_f`, each signed period proxy is
also written explicitly as `first_variation_coefficient_dT_depsilon_at_0`,
with a separate `first_variation_sign` column.

The maximum observed residuals are `1.5021317523178368e-13` for the primitive
q-cutoff comparison, `1.5418777365994174e-12` for the repeated-orbit q-cutoff
comparison, and at most `3.9968028886505635e-15` for the remaining period,
orientation, basepoint, and quadrature identities.  These are observed
binary64 differences; they are neither exact-zero claims nor certified error
bounds.  Periods therefore carry `NUMERICAL_OBSERVATION` status.

## Controls and interpretation

The selected newform-proxy RMS is `0.8557007383823421`.  A deterministic
bounded PSL2Z-invariant observable built from `j/1728` is matched to this RMS
on these 11 rows only.  The ledger also contains a fixed cyclic permutation of
newform periods, while a separate 125-row artifact supplies the simpler-parent
length control.  Period-versus-length correlations are approximately `0.3823`
(newform), `0.8181` (matched generic), and `-0.1152` (permuted).  These finite
descriptive values do not establish arithmetic specificity.

No exact orbit-owned Hecke recurrence was derived, and no prime table or
Riemann-zero data entered selection, computation, or evaluation.  Consequently:

```text
hecke_euler_evidence_status=HEURISTIC
hecke_euler_testability=NOT_TESTABLE
formal_route_a_tuple=UNASSIGNED
route_b_evaluation=NOT_RUN
route_b_invocation_allowed=false
```

Round 2 closes the requested finite computation and reproducibility checks. It
does not pass the next arithmetic gate.  Advancement requires an exact
source-derived recurrence that does not import prime labels.
