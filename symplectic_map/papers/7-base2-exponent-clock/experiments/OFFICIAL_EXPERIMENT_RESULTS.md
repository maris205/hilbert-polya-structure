# Official Experiment Results

Status: `P5_ANALYSIS_COMPLETE_REGISTERED_RUN_0001_COMPLETED_NO_HIT`

Candidate: `pcf_quadratic_exact_2adic_boundary_v1`

This report analyzes only the frozen exact artifacts of
`REGISTERED_RUN_0001`. It does not rerun the candidate, extend the frozen
period range, or introduce numerical, prime, zero, or network data.

## Outcome

The one-shot registered run completed all frozen periods `n=2,...,7` and
stopped normally with `COMPLETED_NO_HIT`. For every period and both targets
`B_n=+1` and `B_n=-1`, the exact gcd is the constant polynomial one and the
independently computed resultant has nonzero exact rational field norm. The
two engines agree in all twelve target checks.

This is a development-seen reproduction and implementation-falsification
ledger. Periods 2--7 had already been inspected before source lock, there
were no blind periods, and the output is not a validation or test split.

## Raw registered table

Here `D_n=deg(Psi_n^set)`, the cycle count is `D_n/n`,
`G_+=deg gcd(Psi_n^set,B_n-1)`, and
`G_-=deg gcd(Psi_n^set,B_n+1)`. Each exact field norm is written as `2^v2`
times its exact odd part. Runtimes are the serialized exact nanosecond counts;
decimal seconds are displayed only as an exact unit conversion.

| Run | `n` | `D_n` | Exact cycles | `G_+` | `N_+`, `v2(N_+)` | `G_-` | `N_-`, `v2(N_-)` | Wall time |
|---|---:|---:|---:|---:|---|---:|---|---:|
| R042 | 2 | 2 | 1 | 0 | `2^2 * 1`, 2 | 0 | `2^2 * 1`, 2 | 63,931,487 ns (0.063931487 s) |
| R043 | 3 | 6 | 2 | 0 | `2^9 * 1`, 9 | 0 | `2^9 * 1`, 9 | 174,504,404 ns (0.174504404 s) |
| R044 | 4 | 12 | 3 | 0 | `2^20 * 1`, 20 | 0 | `2^24 * 1`, 24 | 411,053,181 ns (0.411053181 s) |
| R045 | 5 | 30 | 6 | 0 | `2^50 * 16807`, 50 | 0 | `2^60 * 161051`, 60 | 1,637,080,691 ns (1.637080691 s) |
| R046 | 6 | 54 | 9 | 0 | `2^102 * 117649`, 102 | 0 | `2^120 * 387420489`, 120 | 4,033,271,287 ns (4.033271287 s) |
| R047 | 7 | 126 | 18 | 0 | `2^294 * 1`, 294 | 0 | `2^266 * 868028736113769706358509`, 266 | 16,919,324,815 ns (16.919324815 s) |

Total serialized candidate wall time: 23,239,165,865 ns (23.239165865 s).

For every row, the exact-period component is monic and squarefree, its degree
is divisible by `n`, the normalized product is invariant under `g` modulo
that component, formal-dynatomic and set-theoretic degrees agree, and both
gcd/resultant engines agree. The optional `q=3` diagnostic was
`NOT_REQUESTED` for every candidate period.

## Evidence and inference

### Direct frozen evidence

1. **Observation.** All six records have status `PASS`, both target gcd
   degrees are zero, and both exact field norms are nonzero.
   **Interpretation.** No exact-period root represented in the frozen
   set-theoretic component satisfies `B_n=+1` or `B_n=-1` for `2<=n<=7`.
   **Implication.** The correct finite label is
   `BASE2_EQUALITY_ABSENT_N2_TO_N7_DEVELOPMENT_SEEN`.
   **Next step.** Do not extend the cutoff after seeing this null result;
   preserve it as a frozen reproduction ledger.

2. **Observation.** The power-map positive/negative-target control, Chebyshev
   signed-equality control, formal-period-pollution control, and upstream
   Paper-2 regression all passed using the shared exact engines.
   **Interpretation.** The pipeline detects both equality signs, rejects a
   known negative target, and does not confuse formal-period pollution with
   an exact cycle. **Implication.** The candidate absences are not explained
   by a target-sign, exact-period, or always-negative classifier defect.
   **Next step.** Retain these controls unchanged for artifact review; no
   additional candidate execution is warranted in this source lock.

3. **Observation.** Runtime rises from 63,931,487 ns at `n=2` to
   16,919,324,815 ns at `n=7`, while exact-set degree rises from 2 to 126.
   **Interpretation.** Exact symbolic elimination cost grows sharply over the
   frozen range. **Implication.** A larger brute-force cutoff would add cost
   without converting a finite ledger into an all-period argument.
   **Next step.** Direct follow-up effort toward proof-level constraints on
   the unramified norm or cycle polynomial, under a new source lock if it is
   made a separate project.

### Proof-backed conclusions, not finite-run extrapolations

- `EXACT_2ADIC_VALUATION_ALL_PERIODS_CERTIFIED_BY_PROOF`: Theorems A--B prove
  `w(Lambda_C)=n*w(2)` for every finite exact period `n>=2` cycle of the frozen
  map. The proof-contract checks only audit consistency with that proof; the
  six computed periods are not its logical basis.
- `BASE2_EQUALITY_ABSENT_N2_N3_BY_LOCAL_THEOREM`: Lemma D's local
  two-coefficient obstruction excludes `B_C=+/-1` at exact periods 2 and 3.
  R042--R043 reproduce that conclusion but do not establish it.

### Open or deliberately unadvanced conclusions

- `BASE2_EQUALITY_ALL_PERIODS_OPEN_N_GE_4`: the degree-four residue witness
  shows that the two-coefficient filter is not sufficient from period 4
  onward, and finite absence through period 7 cannot close the gap.
- `ROUTE_A_NOT_ADVANCED / ROUTE_B_NOT_OPENED`.
- Modulus-only equality and characteristic-exponent equality are not inferred
  from the rational equality audit.

## Data-use declaration

- New blind periods: none.
- Candidate numerical runs: zero; every candidate calculation was exact
  symbolic arithmetic.
- Numerical or approximate matching: none.
- External prime tables: not accessed.
- Riemann-zero data: not accessed.
- Network data during the registered run or this analysis: not accessed.
- Post-null period extension: none.

## Frozen artifact bindings

- Source lock SHA-256:
  `205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1`.
- Proof package SHA-256:
  `9c4cff04ac7434822c5e0d091509947da554ac612a6f7b4332c5675fc6a355c9`.
- Reviewed code-tree SHA-256:
  `7a5ea42ea52d35bf4d6608b1175a43ab81ceaa9ed8fbfd0e35e183920dbdd27a`.
- Registered result SHA-256:
  `847564ffb9e69aee2018dfa179490fafa81b733ad58231dab9202b82623f3ce6`.
- Terminal ledger SHA-256:
  `06215794b323552bc953c3ea8935d76c15b205bc7df13c170e448c0562b0b7b9`.

