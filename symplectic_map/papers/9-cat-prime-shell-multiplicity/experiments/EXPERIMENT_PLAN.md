# Experiment Plan

## Frozen experiment identity

- Candidate: `cat_prime_shell_multiplicity_obstruction_v1`.
- Safe title: **A Multiplicity Audit for Prime-Torsion Euler Products of
  the Cat Map**.
- Date: 2026-08-14 UTC.
- Current execution state: **design only; no code and no registered run**.
- Intended paper decision:
  `GO_SCOPED_NEGATIVE_NOTE_LOW_NOVELTY`.
- Intended route decision:
  `A0_FAIL_GLOBAL_NORMALIZATION_ONLY / ROUTE_B_NOT_OPENED`.

## Method thesis and evidence boundary

For the fixed cat map

$$
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},
$$

one prime-order torsion shell contains many primitive dynamical orbits.  An
unweighted orbit-label product therefore repeats the nominal Riemann local
factor $m_p$ times.  Pure nonzero scalar weights cannot collapse its
denominator degree; the exact fractional repair is complete-shell normalized
counting and is not prime-specific.

All general statements are proofs.  A later registered experiment, only if
separately authorized, is a deterministic reproduction of five inherited
finite controls.  It cannot establish an all-prime theorem, a convergence
statement, novelty, a canonical selector, or the absence of centralizer,
matrix-valued, numerator, Fredholm, or cohomological escapes.

## Claim map

| Claim | Why it matters | Minimum convincing evidence | Blocks |
|---|---|---|---|
| C1: $p=2$ is the unique shell with $m_p=1$; every odd prime has $m_p\ge p-1$, with the frozen split/inert/ramified formulas | establishes that the direct all-orbit shell construction has unavoidable multiplicity at every odd prime | complete finite-field proof; exact reproduction of only the inherited $p=2,3,5,7,11$ ledger as a falsification control | B1, B2 |
| C2: the raw-return and orbit-label products are different; the label product has exponent $m_p$ and coefficient $m_p/r$, pure fixed nonzero scalar weights cannot reduce it to one factor, and the exact fractional repair is shell-global and composite-compatible | determines the A0 route decision without overclaiming general dynamical-zeta impossibility | primitive/repetition derivation; formal polynomial-degree proof; exact symbolic control of repeats and fractional exponents; proof-only safe global bounds | B3, B4, B5 |

Anti-claims that the design must detect or forbid:

- all nonzero shell points form one orbit for every prime;
- the raw point-potential product is the orbit-label product;
- a weight $1/m_p$ repairs every repetition;
- no normalization can produce one Euler factor;
- the fractional repair detects primality;
- a five-prime audit proves an all-prime theorem or global convergence;
- the scalar denominator argument rules out matrices, numerators,
  alternating determinants, centralizer quotients, or enriched selectors.

## Frozen development-seen ledger

The only permitted prime inputs are

$$
\{2,3,5,7,11\}.
$$

They are inherited from Paper 8 and are not blind test data.

| $p$ | type | expected point-period profile | expected primitive cycles | $m_p$ | expected raw-return factor | expected fractional exponents |
|---:|---|---|---|---:|---|---|
| 2 | binary/inert | $3:3$ | one length-$3$ cycle | 1 | $(1-2^{-3s})^{-1}$ | $1$ |
| 3 | inert | $4:8$ | two length-$4$ cycles | 2 | $(1-3^{-4s})^{-2}$ | $1/2$ each |
| 5 | ramified | $2:4,\ 10:20$ | two length-$2$ and two length-$10$ cycles | 4 | $(1-5^{-2s})^{-2}(1-5^{-10s})^{-2}$ | $1/12$ per short cycle; $5/12$ per long cycle |
| 7 | inert | $8:48$ | six length-$8$ cycles | 6 | $(1-7^{-8s})^{-6}$ | $1/6$ each |
| 11 | split | $5:120$ | twenty-four length-$5$ cycles: four eigenline, twenty off-line | 24 | $(1-11^{-5s})^{-24}$ | $1/24$ each |

For every row, the separate expected orbit-label factor is
$(1-p^{-s})^{-m_p}$ and its formal repeat coefficient is $m_p/r$.  No
numerical value of $s$, $\log p$, a product, or a logarithm may be evaluated.

## Experiment blocks

### B1: exact shell-orbit ledger

- **Claim tested:** C1.
- **Why this block exists:** catches an incorrect finite-field case split,
  least-period calculation, or ramified Jordan boundary.
- **Task:** for each of the five fixed primes only, enumerate the nonzero
  vectors in $\mathbb F_p^2$, apply the fixed matrix modulo $p$, and record
  least periods and primitive cycles.  Independently check the split/inert
  classification from $X^2-3X+1$ and the direct $p=2,5$ identities.
- **Compared engines:** (i) exact vector permutation and (ii) analytic case
  certificate.  These are cross-checks, not competing methods.
- **Metrics:** exact equality of point counts, period histograms, cycle
  lengths, total $m_p$, and for $p=11$ the eigenline/off-line split.
- **Success criterion:** every field has exactly $p^2-1$ registered points;
  every point appears in exactly one primitive cycle; all five rows match the
  frozen ledger byte-for-byte after canonical sorting.
- **Failure interpretation:** theorem/control mismatch; halt.  Do not add
  primes, change the matrix, alter a cycle definition, or repair the expected
  row.
- **Paper target:** one exact control table, explicitly labeled
  “development-seen finite reproduction.”
- **Priority:** MUST-RUN only after a later deployment authorization.

### B2: theorem-contract classification checks

- **Claim tested:** C1.
- **Why this block exists:** keeps the finite audit tied to the actual proof
  rather than promoting five examples into a theorem.
- **Task:** verify exact Boolean contracts:
  $\tau_p\mid p-1$ in fixed split rows,
  $\tau_p\mid p+1$ in fixed inert rows,
  $m_p=(p^2-1)/\tau_p$ in unramified rows, and
  $A=-I+N$, $N^2=0$, $\operatorname{rank}N=1$ at five.  Check the asserted
  lower bound in every fixed row.
- **Metrics:** exact divisibility and equality gates only.
- **Success criterion:** all contracts pass and the result schema identifies
  their provenance as `FINITE_FALSIFICATION_CONTROL`, not
  `ALL_PRIME_EVIDENCE`.
- **Failure interpretation:** halt and return to proof review; computation
  cannot weaken the theorem post hoc.
- **Paper target:** appendix contract ledger, if a manuscript is later
  authorized.
- **Priority:** MUST-RUN only after a later deployment authorization.

### B3: two-product semantic audit

- **Claim tested:** C2.
- **Why this block exists:** point-potential return time and one-time orbit
  labeling are the most likely semantic source of a false Riemann factor.
- **Task:** from the canonical primitive cycles, construct formal exponent
  ledgers, never floating values:

  1. raw return: one factor at formal monomial $p^{-s|\gamma|}$ per orbit;
  2. orbit label: one factor at formal monomial $p^{-s}$ per orbit;
  3. repeats $r=1,2,3$: record raw exponent
     $p^{-sr|\gamma|}/r$ and label coefficient $m_p/r$.

- **Metrics:** exact symbolic monomial keys, rational coefficients, and
  equality with the frozen table.
- **Success criterion:** $p=5$ remains mixed in the raw product but has label
  exponent four; every label repeat has coefficient $m_p/r$.
- **Failure interpretation:** semantic implementation failure; halt.  In
  particular, division by a primitive period may not be used to erase the
  number of primitive cycles.
- **Paper target:** a two-column raw-versus-label table.
- **Priority:** MUST-RUN only after a later deployment authorization.

### B4: scalar obstruction, fractional repair, and selector controls

- **Claim tested:** C2.
- **Why this block exists:** separates three mathematically different ways
  of changing multiplicity.
- **Task:** use exact polynomial/rational arithmetic to check:

  - unweighted denominator degree $m_p$;
  - the equal-weight power sums
    $\sum_\gamma(1/m_p)^r=m_p^{1-r}$ for $r=1,2,3$;
  - shell-mass exponents
    $\sum_\gamma|\gamma|/(p^2-1)=1$;
  - a one-orbit selector has retained-cycle count one and discarded-cycle
    count $m_p-1$.

  The general fixed-nonzero-weight degree theorem and the composite-shell
  Jordan-totient identity remain proof-only; no parameter search and no
  composite-order enumeration is permitted.
- **Baselines:** unweighted all-orbit label product; naive equal scalar
  weights; fractional shell normalization; explicit one-orbit discard.
- **Metrics:** polynomial degrees, exact rational power sums, exponent sums,
  retained/discarded counts.
- **Success criterion:** only the fractional exponents sum to one without
  discarding cycles, and the output labels this result
  `GLOBAL_NORMALIZED_COUNTING`, never `LOCAL_POTENTIAL`.
- **Failure interpretation:** halt.  No post-output redefinition of “weight,”
  “local,” or “ordinary product” is allowed.
- **Paper target:** mechanism-boundary table.
- **Priority:** MUST-RUN only after a later deployment authorization.

### B5: proof-only global and escape-boundary contract

- **Claim tested:** C2.
- **Why this block exists:** prevents a local exact audit from silently
  expanding into analytic or quotient claims.
- **Task:** schema validation only.  Confirm that the result manuscript, if
  later produced, contains the safe bounds
  `DIVERGES_REAL_1_LT_SIGMA_LE_2`,
  `NOT_ABSOLUTE_1_LT_SIGMA_LE_2`, and
  `ABSOLUTE_SIGMA_GT_3`; contains no verdict for
  $2<\operatorname{Re}s\le3$; and lists centralizer quotients,
  numerator/Fredholm cancellations, matrix-valued weights, and enriched
  selectors as outside scope.
- **Metrics:** exact required/forbidden schema fields; no numeric analysis.
- **Success criterion:** no exact-abscissa, analytic-continuation,
  zero-matching, transfer, quantization, or centralizer-closure field exists.
- **Failure interpretation:** reject the result package as an overclaim even
  if B1--B4 pass.
- **Paper target:** limitations and route-decision statement.
- **Priority:** MUST-RUN only after a later deployment authorization.

## Controls and ablations

| ID | Exact prediction | Error caught |
|---|---|---|
| K001 shell partition | sum of cycle lengths is $p^2-1$ | missing or duplicated vectors |
| K002 binary exception | $m_2=1$ and orbit length is three | false “never one” statement |
| K003 ramified mixture | exactly two cycles at length two and two at length ten | treating $p=5$ as uniform-period |
| K004 inert minimum | $m_3=2$, $m_7=6$ | assuming maximal order without proof or using the wrong divisor |
| K005 split strata | $p=11$ has four eigenline and twenty off-line cycles | losing the split-case geometry |
| K006 raw/label separation | raw $p=5$ is mixed; label $p=5$ has exponent four | conflating return time with orbit label |
| K007 repetition | label coefficient is $m_p/r$ | fixing only the primitive term |
| K008 equal-weight failure | $m_p^{1-r}\ne1$ for odd $p$ and $r=2,3$ | hand-inserted $1/m_p$ repair |
| K009 fractional identity | weighted exponent sum is exactly one | confusing scalar factor weights with outer fractional exponents |
| K010 selector cost | discard count is $m_p-1$ | hiding symmetry breaking |
| K011 analytic boundary | no numerical $s$ or log fields | promoting finite arithmetic to analytic evidence |
| K012 escape boundary | centralizer/matrix/numerator routes remain `OUTSIDE_SCOPE` | overextending the scalar theorem |

The “ablations” here are formal mechanism comparisons, not fitted models.
Removing orbit length yields the label product; inserting $1/m_p$ inside
each scalar factor tests repeat failure; moving normalized shell mass outside
the factors yields the admitted exact identity; retaining one cycle records
the selector's discard cost.

## Milestones and run order

| Milestone | Planned runs | Gate | Expected cost | Current status |
|---|---|---|---|---|
| M0 source integrity | R000--R004 | final source-lock hash, independent source review, and later code hash/review agree | seconds, CPU | source design in progress; no run |
| M1 orbit ledger | R010--R014 | B1 and B2 pass for the five fixed primes only | seconds, CPU | not authorized |
| M2 product semantics | R020--R024 | B3 exact ledgers pass | seconds, CPU | not authorized |
| M3 mechanisms | R030--R034 | B4 degrees, power sums, and shell masses pass | seconds, CPU | not authorized |
| M4 closure | R090--R100 | B5, strict result manifest, and independent result review pass | minutes, CPU | not authorized |

Run order is immutable: source/hash preflight; closed-world input scan;
independent deployment authorization; B1/B2; B3; B4; B5; strict manifest;
independent result review.  No later run may begin after an earlier failure.

## Stop/go policy

- At source lock, code authoring, unit execution, and registered execution are
  all forbidden.  A new explicit task and a fresh independent code review
  bound to the final lock and code-tree hashes are required before a
  registered audit.
- Any source hash, matrix, field cardinality, point period, cycle count,
  factor exponent, rational coefficient, or dual-engine disagreement stops
  the audit.
- No new prime, composite order, matrix, potential, normalization, selector,
  repetition range, or analytic point may be added after lock.
- No external prime table, generated prime target array, Riemann-zero data,
  numerical $s$ grid, numerical logarithm, optimizer, tolerance match, or
  network access is permitted during a registered run.
- A passing five-prime audit does not increase the theorem's novelty or
  evidence level and cannot be described as blind validation.
- Centralizer quotient analysis is Paper 10.  It is a live escape and cannot
  be declared closed by a Paper-9 result.
- Route B is not opened under any Paper-9 outcome.

## Data, compute, and reproducibility budget

- External datasets: none.
- Fixed internal inputs: the matrix $A$ and the literal prime tuple
  `(2, 3, 5, 7, 11)`.
- Upstream control source: Paper-8 frozen exact result; its hash is bound in
  `source_lock.json`.
- Floating arithmetic: forbidden.
- Randomness and seeds: none; all ordering must be canonical.
- GPU: zero hours, not used.
- CPU: deterministic, single process, expected below one minute if later
  authorized.
- Memory: below 1 GiB.
- Network during a run: disabled.
- Reproducibility: exact JSON, canonical key ordering, source/code/result
  hashes, strict no-extra-file manifest, and independent result review.

## Planned reporting

If the fixed audit later passes, the result may report:

1. the five exact period/cycle rows;
2. formal raw-return and orbit-label ledgers;
3. exact repeat, degree, fractional-mass, and selector controls;
4. a proof-provenance statement for all-prime and analytic claims;
5. the terminal label
   `PRIME_SHELL_MULTIPLICITY_OBSTRUCTION_CERTIFIED /
   A0_FAIL_GLOBAL_NORMALIZATION_ONLY / ROUTE_B_NOT_OPENED`.

It may not report new primes, a measured abscissa, a fitted Euler product,
prime/zero data, a transfer determinant, a centralizer quotient, a
quantization, or a canonical selector.

## Final design checklist

- [x] At most two paper-level claims are frozen.
- [x] Every claim has a minimum evidence route and a failure interpretation.
- [x] The five audit primes and every expected row are predeclared.
- [x] Raw-return and orbit-label products are separate objects.
- [x] Repetitions, scalar degree, fractional normalization, and selector cost
  are separate controls.
- [x] General theorems and convergence bounds remain proof-only.
- [x] The development-seen and nonblind status is explicit.
- [x] No numerical $s$, logarithm, prime/zero dataset, or new prime scan is
  allowed.
- [x] Centralizer and non-scalar cancellation routes remain open boundaries.
- [ ] Fresh independent source-lock review is bound to the final hashes.
- [ ] Code authoring or execution has been separately authorized.
- [ ] Registered audit has been independently authorized.
