# P24 results — Rounds 2–5

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

## Round-3 Schottky-control results

The following deterministic artifacts were generated on 2026-08-27:

- `schottky_ping_pong_domains_round3.csv` — 8 paired-domain rows carrying the
  exact circle centers/radii and ping-pong certificate fields;
- `schottky_conjugacy_ledger_round3.csv` — 4,148 oriented cyclic classes through
  marked word length 5;
- `schottky_holonomy_shuffle_round3.csv` — 4,092 primitive-class rows with
  length/repetition frozen under a target-free phase permutation;
- `round3_metrics.json` — theorem checks, ledger counts, numerical residuals,
  match/unmatched axes, and Route boundary fields.

The exact construction certifies 8 disjoint closed disks, all 28 separation
inequalities, 8 conjugacy identities, and 22,409 distinct exact projective
matrices for the 22,409 freely reduced words including identity.  The cyclic
ledger splits into 4,092 primitive classes and 56 repetitions, paired into
2,074 unoriented classes.  Complex length and stability fields are numerical;
their maximum trace-invariant reconstruction residual is `1.097e-14`.

This is exact for the **marked word cutoff**, not a metric length-spectrum
cutoff.  The quotient is convex-cocompact and infinite-volume with no cusps.
Finite volume, cusp structure, covolume, length distribution, and full-group
orbit count are not matched to the Bianchi candidate.  No arithmetic owner or
post-freeze arithmetic join appears in these files.

## Round-4 finite-volume-control results

The following artifacts were generated with pinned `snappy==3.3.2`:

- `five_two_control_invariants_round4.json` — exact executable object/topology
  contract, theorem-source receipts, group/peripheral data, and explicitly
  non-interval numerical shapes, cusp parameter, and volume;
- `five_two_primitive_length_groups_round4.csv` — 18 complex-length groups
  representing 31 primitive geodesic classes by multiplicity at real length
  `<3.05`;
- `five_two_alt_crosscheck_round4.csv` — 9 primitive classes in 6 groups from
  the independent alternative algorithm at real length `<2.10`;
- `round4_metrics.json` — match axes, unmatched axes, counts, residual,
  source/number status split, and Route boundary.

Every length-group row records representative word, multiplicity, real length,
holonomy angle, orientation/parity, PSL trace square, primitive semantics,
completeness boundary, no-owner status, and target-data prohibition.  The
maximum cross-algorithm complex-length residual is `2.2944e-31`, with identical
prefix multiplicities.

The 31-class prefix is a `[NUMERICAL_OBSERVATION]`, not a Sage interval
certificate or a full primitive spectrum.  The separate source theorem chain
proves that `5_2=m015` is a genuine finite-volume one-cusp non-arithmetic
control.  No Bianchi/control score or arithmetic join was generated.

## Round-5 matched marked-word results

The pre-result contract is frozen separately in
`experiments/round5_freeze_contract.json`.  The generated artifacts are:

- `bianchi_matched_marked_word_round5.csv` — 2,074 canonical unoriented
  marked owners from 19,624 raw cyclically reduced words;
- `five_two_matched_marked_word_round5.csv` — 51 owners from 372 raw words
  under the identical algorithm and cutoff;
- `round5_matched_phase_comparison.json` — the predeclared complex
  phase/length moment, two 64-permutation null summaries, and the descriptive
  absolute standardized contrast;
- `round5_metrics.json` — exact/numerical evidence boundaries, counts,
  presentation confound, paper consequence, next artifact, and Route firewall.

The candidate ledger splits into 2,046 symbolic primitive and 28 repetition
owners; exact evaluation gives 1,940 loxodromic, 132 parabolic, and two identity
rows.  The control splits into 41 primitive and 10 repetition owners, with 48
loxodromic and three parabolic rows.  The comparison filter retains 1,932 and
39 primitive loxodromic rows.

The frozen standardized values are `-1.74684253916` and `-0.811352306226`;
their absolute contrast is `0.935490232934`.  This is a marking-dependent
`[NUMERICAL_OBSERVATION]`.  Marked-generator count/alphabet and presentation are not matched, so
the result is not an arithmetic verdict and neither CSV is a complete metric
length spectrum.  All target-data flags are `false`.
