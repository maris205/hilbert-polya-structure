# Official Experiment Results

Date: 2026-08-14 UTC  
Candidate: `cat_torsion_primitive_divisor_capacity_v1`  
Frozen matrix:

\[
A=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
\]

## Executive result

The single registered exact audit passed.  For the frozen cat map, a point
of prime additive order and exact dynamical period \(n\) exists exactly when

\[
n\notin\{1,6,12\}.
\]

The exact computation covers only the source-locked range
\(n=1,\ldots,12\).  The conclusion for every \(n>12\) is proof-derived from
the imported primitive-divisor theorem plus the separately proved
finite-field kernel and negative-trace parity lemmas; no period above twelve
was computed.

The carrier theorem certifies intrinsic torsion capacity, but the proposed
order clock fails the first specificity gate: it realizes every positive
integer, prime and composite, is unbounded and discontinuous in every
torsion neighborhood, and is invisible to the native derivative monodromy
at fixed period.  The terminal classification is therefore
`INTRINSIC_TORSION_CAPACITY_CERTIFIED_A0_FAIL_PROVES_TOO_MUCH`.

## Frozen execution scope

| Item | Frozen/observed value |
|---|---|
| Registered exact audits | 1 |
| Registered run count | 1 |
| Registered periods | \(1,2,\ldots,12\) |
| Candidate numerical runs | 0 |
| Periods above twelve computed | none |
| External prime tables | not accessed |
| Generated prime target arrays | 0 |
| Riemann-zero data | not accessed |
| Floating or approximate matching | not used |
| Raw result pass | `true` |

This is a deterministic exact audit.  There are no stochastic seeds,
sampling errors, means, standard deviations, confidence intervals, or
continuous performance baselines.  The relevant delta against the frozen
baseline is exact equality: all twelve direct determinants equal their
recurrence values, and every enumerated finite-field count equals its locked
prediction, so every exact residual is zero.

## Raw determinant and factor ledger

Here \(\Delta_n=\det(A^n-I)\).  `Primitive carrier` identifies the selected
first-appearance prime when one exists.  Period ten is deliberately marked
separately: its carrier is real but does not arise from a primitive divisor
of \(\Delta_{10}\).

| \(n\) | \(\Delta_n\), direct = recurrence | Exact factorization | Prime support | Primitive carrier / boundary conclusion |
|---:|---:|---|---|---|
| 1 | \(-1\) | \(-1\) | none | no prime-order fixed point |
| 2 | \(-5\) | \(-5\) | \(\{5\}\) | \(p=5\) |
| 3 | \(-16\) | \(-2^4\) | \(\{2\}\) | \(p=2\) |
| 4 | \(-45\) | \(-3^2\cdot5\) | \(\{3,5\}\) | \(p=3\) |
| 5 | \(-121\) | \(-11^2\) | \(\{11\}\) | \(p=11\) |
| 6 | \(-320\) | \(-2^6\cdot5\) | \(\{2,5\}\) | no exact-period-six prime-order carrier |
| 7 | \(-841\) | \(-29^2\) | \(\{29\}\) | \(p=29\) |
| 8 | \(-2205\) | \(-3^2\cdot5\cdot7^2\) | \(\{3,5,7\}\) | \(p=7\) |
| 9 | \(-5776\) | \(-2^4\cdot19^2\) | \(\{2,19\}\) | \(p=19\) |
| 10 | \(-15125\) | \(-5^3\cdot11^2\) | \(\{5,11\}\) | nonprimitive \(p=5\) Jordan carrier |
| 11 | \(-39601\) | \(-199^2\) | \(\{199\}\) | \(p=199\) |
| 12 | \(-103680\) | \(-2^8\cdot3^4\cdot5\) | \(\{2,3,5\}\) | no exact-period-twelve prime-order carrier |

All twelve records satisfy:

- direct matrix-power and recurrence determinants agree exactly;
- the internally computed factorization matches the frozen ledger;
- the evidentiary role remains
  `DEVELOPMENT_SEEN_PRIMARY_LITERATURE_REPRODUCTION`, not blind discovery.

## Raw finite-field period profiles

Every nonzero vector of each frozen support space \(\mathbb F_p^2\) was
enumerated exactly.  In total, the profiles cover 41,003 nonzero vectors over
eight primes.  The count notation `period: points` is used below.

| Prime \(p\) | Nonzero vectors | Observed exact-period profile | Frozen prediction | Count residual |
|---:|---:|---|---|---:|
| 2 | 3 | \(3:3\) | \(3:3\) | 0 |
| 3 | 8 | \(4:8\) | \(4:8\) | 0 |
| 5 | 24 | \(2:4,\ 10:20\) | \(2:4,\ 10:20\) | 0 |
| 7 | 48 | \(8:48\) | \(8:48\) | 0 |
| 11 | 120 | \(5:120\) | \(5:120\) | 0 |
| 19 | 360 | \(9:360\) | \(9:360\) | 0 |
| 29 | 840 | \(7:840\) | \(7:840\) | 0 |
| 199 | 39,600 | \(11:39600\) | \(11:39600\) | 0 |

The decisive modulo-five boundary is exact: four nonzero vectors have
period two, twenty have period ten, and the twenty period-ten points form
exactly two cycles.  Thus the absence of a primitive divisor at \(n=10\)
does **not** imply absence of an exact-period carrier.  Conversely, the full
support checks at \(n=6\) and \(n=12\) leave zero carriers at those periods.

## Theorem-versus-computation boundary

| Range or claim | Evidence type | What was established | What was not done |
|---|---|---|---|
| Frozen \(n=1,\ldots,12\) | exact registered computation plus frozen proof | determinant/factor ledger, complete support-prime period profiles, exception set \(\{1,6,12\}\), Jordan repair at 10 | no post-hoc period extension |
| General positive trace, \(n>12\) | imported Flatters theorem plus exact symbolic contract | primitive determinant divisor produces a nonzero finite-field kernel vector of prime additive order and exact period \(n\) | imported theorem was not reproved computationally |
| General negative trace, \(n>12\) | separate parity proof for \(B=-M\) | odd \(n\) uses primitive index \(2n\); \(4\mid n\) uses \(n\); \(n\equiv2\pmod4\) uses \(n/2\), with 7, 9, 11 covered separately | no tail matrix or orbit was evaluated |
| Standard cat, all \(n>12\) | consequence of the general theorem | prime-order exact-period carrier exists | no finite cutoff is promoted to an all-period proof |

The proof-contract sample periods 13, 14, 15, 16, 18, 22, and 26 are branch
bookkeeping records only.  Every such record explicitly says
`matrix_or_orbit_computation_performed=false`; both
`tail_periods_computed` and `periods_above_twelve_computed` are empty.

The exclusion at \(n=12\) makes the uniform general threshold sharp: a
universal claim covering all hyperbolic \(\mathrm{SL}_2(\mathbb Z)\) maps
cannot replace “every \(n>12\)” by a lower threshold.

## Clock capacity and specificity

The exact group-theoretic contract establishes

\[
\operatorname{Per}(T_A)=\operatorname{Tor}(\mathbb T^2),\qquad
L(x)=\log\operatorname{ord}(x),\qquad L(Ax)=L(x).
\]

For every \(m\ge1\), \((1/m,0)\) is a periodic point of exact additive
order \(m\).  Hence the clock has full integer capacity,

\[
\exp L(\operatorname{Per}(T_A))=\mathbb N,
\]

not a prime-specific range.  Recorded checks at orders 1, 4, 6, and 9 all
pass, while the symbolic construction proves the full range rather than a
sampled subset.

At a base point of order 18, the recorded coprime perturbations have exact
orders 342, 990, and 2,286 for denominators 19, 55, and 127.  The general
construction \(N_k=km+1\) proves that the order tends to infinity along
points converging to every torsion point.  Therefore \(L\) is unbounded and
discontinuous in every relative torsion neighborhood.

For the explicit order-five, period-ten carrier,

| Quantity | Exact value | Dependence |
|---|---|---|
| Orbit average | \(\log 5\) | torsion order |
| Unnormalized orbit sum | \(10\log 5\) | period and torsion order |
| \(r\)-fold repeat sum | \(r\,10\log 5\) | repetition, period, torsion order |
| Native monodromy | \(A^{10}=\begin{pmatrix}10946&6765\\6765&4181\end{pmatrix}\) | period only |
| Monodromy characteristic polynomial | \(X^2-15127X+1\) | period only |

Thus native monodromy is torsion-order blind: at a common period it cannot
read which carrier prime is present.  The global point label \(\log p\), its
orbit average, the unnormalized sum \(n\log p\), and the native unstable
log-multiplier \(n\log\alpha\) are distinct quantities and are not
interchangeable.

## Key findings

1. **Observation:** the frozen cat has prime-order exact-period carriers for
   every positive period except 1, 6, and 12.  **Interpretation:** primitive
   determinant divisors explain the ordinary small cases and all periods
   above twelve, while a separate Jordan mechanism is essential at period
   ten.  **Implication:** determinant primitivity is sufficient but not
   necessary for a carrier.  **Next step:** use this exact classification as
   a theorem input; no larger-period scan is warranted.

2. **Observation:** the general hyperbolic carrier contract passes for both
   trace signs, with no tail computation.  **Interpretation:** the
   negative-trace result depends on a genuine parity conversion, especially
   the \(n/2\) branch when \(n\equiv2\pmod4\).  **Implication:** the broad
   \(|\operatorname{tr}M|>2\) statement is supported without silently
   attributing the new parity lemma to the imported theorem.  **Next step:**
   preserve this proof/computation separation in any later exposition.

3. **Observation:** the order clock realizes primes and composites by the
   same formula and is nowhere locally bounded on the torsion domain.
   **Interpretation:** it measures intrinsic torsion capacity but has no
   arithmetic specificity or regular local-observable structure.
   **Implication:** the candidate fails Route-A gate A0 by proving too much.
   **Next step:** any future prime-specific clock must be a genuinely new,
   separately source-locked observable; it cannot be inferred from this
   order label.

4. **Observation:** native monodromy depends only on period.  **Interpretation:**
   linear dynamics supplies no point-order channel at fixed period.
   **Implication:** transfer, zeta, quantization, and prime/zero matching do
   not open automatically from the carrier theorem.  **Next step:** none of
   those experiments is authorized within Paper 8.

## Classification and route decision

| Field | Frozen result |
|---|---|
| Classification | `INTRINSIC_TORSION_CAPACITY_CERTIFIED_A0_FAIL_PROVES_TOO_MUCH` |
| Route A | `A0_FAIL_PROVES_TOO_MUCH_NO_A1_TO_A4` |
| Route B | `NOT_OPENED` |
| Result status | certified exact carrier theorem; rejected prime-specific clock |

The Route-A failure does not weaken the carrier theorem.  It prevents that
theorem from being over-promoted into a prime clock, prime-orbit bijection,
or spectral/zero-matching claim.

## Provenance note

The raw result is SHA-256
`0d8054ad36ad8cdef1496948cf5dd98d6a1a55c186d68124f45a5e6e35bddaa0`
and is linked to the unique claim and completed terminal record.  The
post-run validation required two transparent repairs to provenance logic;
neither repair changed any determinant, factorization, finite-field count,
theorem contract, raw result, claim, or terminal artifact.  Full details are
recorded in `experiments/OFFICIAL_VALIDATION_REPORT.md`.

The source-lock-bound `experiments/EXPERIMENT_TRACKER.md` remains unchanged
at SHA-256
`b977106d20039a5de31db31969ead23829d4dab058d9c7f4c03b1b96e54748f9`.
Its source-lock-era TODO states are historical design records, not the live
post-run status.  No replacement tracker was added to the closed
`results/` inventory.
