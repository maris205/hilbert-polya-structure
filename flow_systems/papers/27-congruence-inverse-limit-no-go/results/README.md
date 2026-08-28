# P27 results

The current result is analytic: `[PROVED]` the total inverse-limit flow has no
periodic points.  This carries the local progress tag
`PROVED_A1_OBSTRUCTION` and the formal same-owner verdict `A1_FAIL`.  A
finite-level diagnostic may still be useful but receives no limit-flow orbit
credit.

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
compatibility is separate from each finite-quotient order.  The current formal
tuple is `(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
overall `ROUTE_A_REJECTED`; A2--A4 are `FAIL/NOT_TESTABLE` for the frozen
inverse-limit owner.

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

## Round-6 claim/source and positioning contract

- `round6_claim_source_matrix.csv` contains 13 claim rows.  Nine external
  rows bind five authoritative primary sources to exact URLs, locators,
  access date, domain caveats, and positioning effects.
- `round6_positioning_summary.json` freezes the common mechanism, direct-prior
  result, formal Route verdict, human-source gate, and three-way decision.
- `round6_artifact_manifest.json` binds the two generated result files.  The
  separate Round-6 reproducibility receipt binds the builder, tests, and
  reproducer source code by SHA-256.

All nine external rows are `PRIMARY_SOURCE_WEB_VERIFIED` and
`HUMAN_CONFIRMATION_PENDING`; zero rows are `USER_ATTESTED_READ`.  The frozen
decision is: short comparative owner-audit `GO`, standalone new aperiodicity
theorem `NO_GO`, same-owner Route-A A2 `NO_GO`.  The result is a positioning
and technical synthesis contract, not a manuscript or an absolute novelty
claim.

## Round-7 owner-factor support escape

- `round7_owner_factor_escape_ledger.csv` unifies 24 cusped exact-order rows
  and 24 cocompact exact lower-bound rows without mixing their evidence types;
- `round7_fixed_prefix_escape.csv` records 54 fixed owner/degree diagnostics;
  and
- `round7_owner_factor_escape_summary.json` records the theorem boundary,
  route firewall, and replay counts.

For each row, all formal coefficients below the certified order bound are
zero.  The cusped rows retain `NOT_ESTABLISHED` base conjugacy primitivity and
are not labeled primitive zeta factors.  The cocompact rows retain proved
primitive homology but do not fabricate full quotient orders.  Core SHA-256 is
`551e92315c46dcbb4d01bd84688bb77eca8fcd4a6c2eaec202fe04f621275845`.

## Round-8 homology-renormalization quadrants

- `round8_renormalization_quadrants.csv` contains 96 exact rows for three
  primitive owners, eight factorial moduli, and four clock/multiplicity
  choices;
- `round8_renormalization_prefix_coefficients.csv` contains 1,248 exact
  coefficients through degree 12; and
- `round8_homology_renormalization_summary.json` records the cover theorem,
  quadrant outcomes, new-owner firewall, and Route boundary.

Core SHA-256 is
`a1b588724dacb2ab2986326a7a5e1c6aec654c61538c1465e26564357b568b33`.
The fully renormalized finite-panel factor is exactly `(1-x_g)^(-1)` at every
level.  No full primitive census or full-flow determinant is claimed.
