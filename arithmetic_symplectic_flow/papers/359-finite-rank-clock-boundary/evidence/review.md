# FRC01 — internal ARS analysis review

## Checkpoint 2

Verdict: **PASS**, for the conditional all-return bound, finite-block bridge and three full controls.
Calibration: **NOT_CALIBRATED**; internal shared-history model analysis, not blind or external peer review.

### Actual inputs, method, and limits

- Audit `ANG-AUDIT-20260921-FRC01`; authorized batch round 5/5, not a new arithmetic candidate.
- Read the complete original 116-line `candidate-card.md`; measured SHA-256
  `1054a232c9d6c7e27f60a9f9bbfc4dd3a3822f1ca9da5ceaeb3b0444c1a9c374`.
- Read the complete 210-line `paper.md`; measured SHA-256
  `3f444a0c4152951cecdb13b242c3d59bfd474fded28e537e98965155765fbff6`.
- No peer, scout, independent-proof, outcome, final surface or other scientific file was read.
  Prior shared history is disclosed; no earlier symbolic/geometry result supplies a missing proof here.
- Retained fully read stream and ARS instructions apply; no forced defect quota, score or research expansion.
- Methods: exact cancellation, factorization, signed sums, measure partitions and series; no numerical search, network, auxiliary agent, Git, PDF or author edit.
- Served model/effective reasoning remain independently unobserved (`UNKNOWN`); no cross-model, human-review or independent-error guarantee.

### 1. Whole return groups and the common-scale prime bound

- A chain identifying `(x,h+t)` with `(x,h)` composes to one actual loop at x. Conversely every
  such loop supplies its height difference. Thus the full return group is exactly `c(G_x^x)`;
  incoming histories and retained ineffective isotropy create no additional return outside it.
- On a loop the single-valued coboundary cancels. Every return therefore lies in the SAME
  integer span of the fixed omega_j, and hence in one rational space V of dimension d.
  This remains true for zero or nondiscrete stabilizers, to which no primitive is falsely assigned.
- A finite rational relation among distinct prime logarithms clears to integer exponents; moving
  negative powers across the equality and unique factorization force every exponent to vanish.
  Multiplication by any ONE nonzero lambda preserves rational independence.
- Consequently returns from different base objects still jointly occupy V: more than d distinct
  primes with exact return `lambda log p` would contradict its dimension. The argument bounds all
  returns, not only primitive ones, and does not assume the witnessing loops share one base orbit.
- The infinite-prime corollary follows by choosing d+1 primes. It also covers d=0 and any fixed
  global time unit, but neither prime-dependent scaling nor approximate returns.
- Disposition: PASS. A finite-rank subgroup can be dense; that fact does not defeat this exact bound.

### 2. Finite-block bridge on all signed histories

- A finite-block roof on a finite-edge shift has finitely many actual values on its legal full carrier.
  Counting each value along positive histories and reversing counts along negative histories gives
  Borel integer cocycles: concatenation works for mixed signs as well as positive histories.
- Their negatives produce the specified `c_tau=-R_n tau` on every retained-lag arrow.
  Periodic endpoints do not collapse distinct n, so no isotropy/history mismatch enters the counts.
- If `tau=f+u(sigma x)-u(x)`, telescoping for every signed n yields
  `c_tau=c_f-u(range)+u(source)`. Thus `b=-u` has exactly the frozen sign and is an actual
  all-arrow equality, not a fit on periodic data or a replacement of the original clock.
- The general Borel-cohomology step is an identity for the specified full extension. The later
  continuous/proper/finite-measure suspension construction is separately proved under bounded
  continuous roofs for the controls; it is not asserted for every arbitrary Borel transfer function.
- All controlling memory and phase must belong to the finite autonomous state before this bridge
  applies. Neither an unbounded schedule nor an arbitrary continuous roof is silently finite-block.
- Disposition: PASS, with the hypotheses kept explicit and owner-specific.

### 3. Common construction applied to each complete control

- Each control retains all binary two-sided sequences with the unique full inverse sigma^-1.
  Cylinder invariance extends to all Borel sets for the declared Bernoulli measure; periodic/null
  sequences are not removed. The actual retained-lag groupoid and signed roof cocycle are complete.
- For each verified roof with `1<=tau<=C`, the integer action is
  `(x,h)->(sigma^n x,h-R_n tau(x))`. Nonzero signed sums have nonzero sign, so it is free.
  If endpoint heights stay bounded, `|n|` stays bounded; compactness of X then gives properness.
- All signed sums are strictly increasing and tend to both infinities. Exactly one n places a
  representative in `0<=h<tau(x)`, giving the full fundamental domain, not a selected periodic section.
- Product measure on `X times R` is invariant under the integer action by shift invariance and
  fiberwise Lebesgue translation. The fundamental-domain mass is the finite integral of the OWN roof.
- For fixed time, the number of roof crossings is bounded. The crossing-count sets are Borel;
  translated/reduced pieces have disjoint images covering the domain. Summing the restricted
  product-measure identities proves invariance for every Borel subset of the suspension.
- Nonperiodic x has source isotropy zero and no positive return. If x has least shift period k,
  the entire isotropy is kZ and the full time group is LZ with L the sum of its k roof values.
  Positivity makes L least positive and the extension isotropy zero; all repetitions are retained.
- Actual arrows relate precisely one shift-orbit. All heights over a periodic shift-orbit form one
  physical packet, but equal periods in distinct shift-orbits cannot merge. Disposition: PASS.

### 4. U and V: separate clocks, measures, and exact ranks

- U's roof is one, so its full cocycle is `-n`, suspension mass one and least physical period k
  for each least-period-k sequence. Its two constant sequences are distinct primitive packets of time one.
  A nonzero return forces rank at least one; its displayed full representation supplies rank at most one.
- V's full signed counts give `-N_0-N_1 sqrt(2)`. Its own measure mass is `(1+sqrt(2))/2` and
  a least-period word has least time `m_0+m_1 sqrt(2)`, by its entire source isotropy, not a guessed roof sum.
  The constant sequences supply returns one and sqrt(2), rationally independent by the parity proof.
  Hence its minimal rational rank is exactly two, under any competing full-clock representation.
- Nonperiodic points and all phases follow the owner lemma for EACH roof, with no borrowed periods or roof/IMAGE-clock identification.
- Disposition: PASS.

### 5. W: full-point cohomology despite infinite memory

- The geometric tail bound gives uniform convergence, continuity and `1<=tau_W<=2`.
  Flipping one digit beyond an arbitrary fixed window changes the roof value, proving it is not
  finite-block; the infinitely many values are not used as evidence for an infinite clock rank.
- Its OWN suspension therefore satisfies the preceding full-owner hypotheses. Integrating the
  uniformly convergent series gives mass `1+(1/2)sum_(k>=1)2^-k=3/2`.
- The proposed u is uniformly convergent and continuous. Direct reindexing gives, at EVERY point,
  `u(sigma x)-u(x)=-x_0+sum_(j>=1)2^-j x_j`, hence the claimed roof identity exactly.
- Signed telescoping gives `c_W=-R_n(1+x_0)-u(sigma^n x)+u(x)` for all n, including negative
  histories. The first term is an integer cocycle, so generator one and `b=-u` satisfy the full hypothesis.
- On a least-period-k sequence, cancellation gives L=k+m_1; the entire isotropy calculation shows
  this is its least time. Nonperiodic points still have no return, and the constant zero sequence
  supplies return one. Thus minimal rational rank is exactly one, not merely an upper bound.
- Disposition: PASS. No roof/phase/source replacement or universal reduction of infinite-memory roofs is claimed.

### 6. Applicability and fifth-round stop

- This is a conditional filter, not a prime candidate or universal rejection; another commuting physical action cannot inherit its IMAGE rank bound.
- In particular no finite-rank representation for 358 is proved or refuted here; its T2 remains OPEN.
  Unbounded content alone is not an applicability proof. Naturalness is not supplied by the filter.
- No new formal T/Route coordinate is claimed; classical A0/A1/A2 not applicable, formal Route
  unassigned and B not invoked. No mathematical correction is required on the frozen inputs.
- This fifth round ends research under the current batch: summarize and await user confirmation,
  without a sixth search or an expanded 358 census. Final-surface CP3 remains a separate release.

Checkpoint 2 frozen at EOF.

## Checkpoint 3: released final surfaces

Verdict: **PASS**, no correction required; internal shared-history `NOT_CALIBRATED` remains in force.
This ARS final-surface check compares retained proof claims, not a new proof or external peer review.

- Confirmed the 115-line CP2 prefix SHA-256 before appending:
  `2f8563bad5bb6fef940450182ab0fb9fe25beeddb2f19f93b0cba56e05302188`.
- Read only new card lines 117–131; measured full 131-line SHA-256
  `f2323693ea25dba9779d937d539cee4573c604102fbfe144de113516baea3131`.
- Read the full 24-line README; measured SHA-256
  `0da3b9bcb91860f913583bde81d2bac7bf9a7b91c1bfb44a6374cbe3e0519539`.
- Read the full 23-line ledger; measured SHA-256
  `b89537ca803192a0893b7ff86b7b42a84e43f3f10306b4e06809a28a971a9675`.
- Original card 116-line prefix and unchanged 210-line paper hashes still match CP2.
  No independent report, peer, scout, batch summary, batch-log content or later package was read.
  Linked targets were checked for existence only; no external, numerical or new scientific work.
- Audit/status agree; the appended outcome supersedes historical contract openness without rewriting it.
- The bound remains conditional on an actual all-arrow representation and applies to exact returns
  for ONE common positive lambda, not per-prime scales or approximate/asymptotic matching.
  It is not an unconditional symbolic-dynamics prohibition or a new prime candidate. Disposition: PASS.
- Signed finite-block/cohomology bridges, the three own measures, full stabilizers and exact ranks
  remain consistent. W is a verified counterexample to infinite-range-as-escape, not a universal roof theorem.
- 358's representation remains NOT ESTABLISHED and T2 OPEN. No zero-IMAGE result transfers to
  357's distinct geometric physical time. These owner boundaries are explicit. Disposition: PASS.
- Naturalness remains OPEN; no new formal T/Route coordinate, formal Route UNASSIGNED and B NOT INVOKED.
  The fifth-round stop calls for summary and user confirmation, not a sixth search. Disposition: PASS.

Final checkpoint frozen at EOF; research stops here pending the authorized batch handoff and confirmation.
