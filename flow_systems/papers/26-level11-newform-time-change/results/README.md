# P26 Round-2 results

Canonical generated artifacts are:

- `newform_timechange_variation_ledger.csv`: 11 selected positive-necklace
  representatives, exact matrix/primitive metadata, lengths, numerical
  one-form proxies, explicit signed first-variation coefficients
  `dT_epsilon/d epsilon|_0`, and every residual/control value;
- `simpler_parent_length_control.csv`: all 125 primitive positive hyperbolic
  necklaces through cutoff 9, including the 11 selected rows;
- `round2_summary.json`: configuration, counts, finite-ledger metrics, maximum
  residuals, and claim boundary; and
- `artifact_manifest.json`: SHA-256 bindings for the generator, tests,
  reproduction script, and the three primary data artifacts.

The 11 selected rows split by length as 1 at length 7, 4 at length 8, and 6 at
length 9.  Their newform-proxy RMS is `0.8557007383823421`.  The matched generic
control has the same finite-ledger RMS by construction.  Correlation with
length is `0.38226372301679423` for the newform proxy,
`0.8180749583713894` for the matched generic control, and
`-0.11520138109343742` after the deterministic period permutation.

Maximum observed binary64 cross-check differences are:

```text
q cutoff (48 versus 192)               1.5021317523178368e-13
quadrature (512 versus 1024 panels)     6.661338147750939e-16
basepoint shift                         2.6645352591003757e-15
orientation reversal                    1.7763568394002505e-15
direct M^2 repetition                   3.9968028886505635e-15
repeat q cutoff (2048 versus 4096)      1.5418777365994174e-12
repeat quadrature (256 versus 512)      2.220446049250313e-15
```

These are observed double-truncation/double-quadrature differences, not exact
zeros or rigorous error bounds.  The ledger status is
`NUMERICALLY_CERTIFIED` for the finite exact owner enumeration and
`NUMERICAL_OBSERVATION` for periods and controls.

No prime labels or zero data occur.  The finite positive-word ledger is not a
complete `Gamma_0(11)` conjugacy-class certificate.  Hecke/Euler evidence is
`HEURISTIC`, testability is `NOT_TESTABLE`, the formal Route-A tuple remains
`UNASSIGNED`, and Route B was not run.
