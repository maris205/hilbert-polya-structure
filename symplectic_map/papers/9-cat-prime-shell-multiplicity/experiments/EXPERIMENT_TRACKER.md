# Experiment Tracker

## Execution status at source design

- Candidate: `cat_prime_shell_multiplicity_obstruction_v1`.
- Code files authored for Paper 9: **0**.
- Unit or preflight executions: **0**.
- Candidate numerical runs: **0**.
- Registered exact audits: **0**.
- External prime tables or generated prime target arrays accessed: **0**.
- Riemann-zero data accessed: **0**.
- Numerical evaluations of $s$ or logarithms: **0**.
- Parameter, matrix, potential, normalization, or selector searches: **0**.
- Current authority: proof/literature/source-lock authoring only.

Every run below is a future placeholder.  `TODO_NOT_AUTHORIZED` is not a
queued job and does not grant permission to write or execute code.

## Frozen future run registry

| Run ID | Milestone | Purpose | Exact input/object | Priority | Status | Gate or expected record |
|---|---|---|---|---|---|---|
| R000 | M0 | source-lock schema/hash preflight | final seven-file source package | MUST | TODO_NOT_AUTHORIZED | final lock and six bound hashes parse and agree |
| R001 | M0 | upstream provenance | Paper-8 source, proof, raw-result, result-manifest, and review hashes | MUST | TODO_NOT_AUTHORIZED | every frozen hash agrees |
| R002 | M0 | closed-world input scan | future Paper-9 runnable tree | MUST | TODO_NOT_AUTHORIZED | only matrix and tuple `(2,3,5,7,11)`; no network/data loaders |
| R003 | M0 | independent code review | final source lock plus future code-tree hash | MUST | TODO_NOT_AUTHORIZED | explicit `DEPLOYMENT_PASS` required |
| R004 | M0 | single-claim/run guard | future registration state | MUST | TODO_NOT_AUTHORIZED | no prior or duplicate registered claim |
| R010 | M1 | exact vector-permutation audit | $p=2$ | MUST | TODO_NOT_AUTHORIZED | profile $3:3$, one $3$-cycle |
| R011 | M1 | exact vector-permutation audit | $p=3$ | MUST | TODO_NOT_AUTHORIZED | profile $4:8$, two $4$-cycles |
| R012 | M1 | exact vector-permutation audit | $p=5$ | MUST | TODO_NOT_AUTHORIZED | profile $2:4,10:20$, two cycles of each length |
| R013 | M1 | exact vector-permutation audit | $p=7$ | MUST | TODO_NOT_AUTHORIZED | profile $8:48$, six $8$-cycles |
| R014 | M1 | exact vector-permutation audit | $p=11$ | MUST | TODO_NOT_AUTHORIZED | profile $5:120$, twenty-four cycles; four eigenline, twenty off-line |
| R015 | M1 | analytic/enumerative cross-check | all five fixed rows | MUST | TODO_NOT_AUTHORIZED | split/inert/Jordan certificates and enumerations agree |
| R020 | M2 | raw-return factor ledger | $p=2$ | MUST | TODO_NOT_AUTHORIZED | one length-three factor |
| R021 | M2 | raw-return factor ledger | $p=3,7,11$ | MUST | TODO_NOT_AUTHORIZED | uniform-period factors with exponents $2,6,24$ |
| R022 | M2 | ramified raw-return ledger | $p=5$ | MUST | TODO_NOT_AUTHORIZED | separate length-two and length-ten factors, exponent two each |
| R023 | M2 | orbit-label factor ledger | all five fixed rows | MUST | TODO_NOT_AUTHORIZED | common label per orbit and exponent $m_p$ |
| R024 | M2 | repetition ledger | formal $r=1,2,3$ | MUST | TODO_NOT_AUTHORIZED | label coefficient exactly $m_p/r$ |
| R030 | M3 | pure scalar denominator degree | all five fixed rows | MUST | TODO_NOT_AUTHORIZED | degree $m_p$; only $p=2$ has degree one |
| R031 | M3 | equal-weight control | odd fixed rows, $r=1,2,3$ | MUST | TODO_NOT_AUTHORIZED | power sum $m_p^{1-r}$; failure for $r=2,3$ |
| R032 | M3 | fractional shell normalization | all five fixed rows | MUST | TODO_NOT_AUTHORIZED | exact exponent sum one with frozen rational weights |
| R033 | M3 | selector cost | all five fixed rows | MUST | TODO_NOT_AUTHORIZED | retained one, discarded $m_p-1$ |
| R034 | M3 | proof-only composite guard | symbolic $J_2(q)$ identity | MUST | TODO_NOT_AUTHORIZED | schema citation only; no composite enumeration |
| R090 | M4 | analytic/nonclaim schema guard | future result package | MUST | TODO_NOT_AUTHORIZED | safe strips only; $2<\Re s\le3$ and exact abscissa unclaimed |
| R091 | M4 | escape-boundary schema guard | future result package | MUST | TODO_NOT_AUTHORIZED | centralizer, matrix, numerator, Fredholm, cohomological routes remain outside scope |
| R099 | M4 | strict result manifest | all authorized future outputs | MUST | TODO_NOT_AUTHORIZED | fail closed on missing, extra, or stale artifacts |
| R100 | M4 | independent result review | final future result package | MUST | TODO_NOT_AUTHORIZED | reviewer-independent `RESULT_PASS` bound to exact hashes |

## Development-seen disclosure ledger

- The fixed matrix and the five prime controls are inherited from Paper 8.
- The exact period profiles at $p=2,3,5,7,11$ were visible before Paper-9
  source lock.
- The formulas for $m_p$, the mixed $p=5$ raw factor, the scalar degree
  obstruction, the failure of $1/m_p$ under repetition, and the fractional
  shell identity were derived before source lock.
- Gaspari (1994) and Baake--Neumärker--Roberts (2013) strongly cover the
  finite prime-lattice classification; Baake--Roberts--Weiss (2008) and
  Chandra (2026) strongly collide with the finite-orbit product packaging.
- Therefore every future finite output is an exact reproduction and
  falsification control, not blind evidence or novelty support.

## Immutable run policy

1. No run may move out of `TODO_NOT_AUTHORIZED` until a new task explicitly
   authorizes implementation and an independent code review issues a
   hash-bound deployment pass.
2. Runs execute in numeric order.  Any failure stops all later runs.
3. No row, prime, repeat range, expected coefficient, matrix, product,
   normalization, or scope field may change after output is inspected.
4. No numerical $s$ or logarithm, external prime list, Riemann-zero list,
   target fitting, tolerance matching, or network data access is permitted.
5. No run may investigate the centralizer quotient; that is reserved for
   Paper 10.
6. A passing audit cannot change
   `GO_SCOPED_NEGATIVE_NOTE_LOW_NOVELTY`, open Route B, or support a new
   classification, zeta, transfer, or quantization claim.

## Intended terminal labels

- `PRIME_SHELL_MULTIPLICITY_OBSTRUCTION_CERTIFIED`.
- `P2_UNIQUE_SINGLE_ORBIT_SHELL`.
- `ODD_PRIME_MULTIPLICITY_AT_LEAST_P_MINUS_1`.
- `RAW_RETURN_AND_ORBIT_LABEL_PRODUCTS_DISTINCT`.
- `PURE_NONZERO_SCALAR_DENOMINATOR_COLLAPSE_REJECTED`.
- `A0_FAIL_GLOBAL_NORMALIZATION_ONLY`.
- `CENTRALIZER_QUOTIENT_RESERVED_FOR_PAPER10`.
- `ROUTE_B_NOT_OPENED`.

None of these labels is currently issued.  At source design the only valid
state is `NOT_EXECUTED`.
