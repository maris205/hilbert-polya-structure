# Evidence record — ASFS-20260918-ETC01

## Scope

This is an exact Markdown proof audit of a freshly frozen candidate.  The card
was written before the proof.  No numerical search, GPU computation, prime
table, Riemann-zero data, fitted parameter, or finite-cutoff extrapolation was
used.

## Candidate-specific checks

1. **Carrier and inverse.** For every output phase, the predecessor phase and
   equation (6) give a two-sided inverse on the entire real plane.  The
   component Jacobian preserves $dq\wedge dp$.
2. **Suspension completeness.** The integer label is conserved.  At fixed $n$,
   the finite phase set has minimum roof $\log(n/(n-1))$ (and the $n=2$
   roof is $\log2$), so neither forward nor backward crossings accumulate in
   finite time.
3. **Full periodic ledger.** Summing the exact recurrence over an arbitrary
   period forces every square and every visited witness to vanish.  Phase return
   visits all $d=1,\ldots,n-1$, leaving exactly the prime labels and the
   disclosed $n=2$ neutral singleton.
4. **Multiplicity and clock.** The $p-1$ phase points over each prime form one
   primitive oriented flow orbit; the universal phase roof sums to $\log p$,
   and repetitions multiply that time by $r$.
5. **Analytic boundary.** The scalar product is recorded only on $\Re s>1$.
   The central derivative is unipotent, so $\det(I-P_p^r)=0$ for every
   repetition; a standard nondegenerate flat-trace denominator cannot simply be
   imported.

## Controls and provenance

The paper compares the new all-phase carrier with 222's divisor-test-only
phase set, the unit-roof comparator, zero-witness/altered-force controls,
all-state and sentinel checks, and the adjacent-ratio engineered timing in
control 160.  Those controls preserve the negative naturalness finding: exact
telescoping is owned by the declared phase geometry but is not thereby shown
to be canonical or source-natural.

## Verification method

The five package files were read back after writing.  Candidate IDs, statuses,
and local links were checked for consistency.  The mathematical claims are
infinite-family statements proved symbolically; no finite computation is being
used as evidence for them.  No root registry or root README was changed in
this exclusive package path.
