# Reframed HCS-C23 large-gate plan

## Claim under test

For each chronological word \(w\), the sequence

\[
\Delta_{w,r}=\operatorname{Norm}_{A_w/R}\det(I-M_w^r)
\]

is already the cyclic-resultant sequence of its packet multiplier polynomial.
The fixed-word tower is therefore a classical baseline.

The revised question is whether **distinct** chronological Hénon words obey
an exact cross-word/cross-period algebraic or ideal-theoretic relation among
their packet multiplier polynomials \(P_w\) or cyclic resultants
\(\Delta_{w,r}\), and whether that relation fails for matched reciprocal
integer polynomials and frozen reversible-map controls.

Before an extended ledger is inspected, the proposed relation must be written
as a versioned, falsifiable formula specifying:

- the allowed pairs \((u,r),(v,s)\);
- the exact gcd, divisibility, valuation, resultant, or ideal relation;
- every multiplicity and repetition convention;
- the finite discovery range and a sealed validation range;
- the null statistic and rejection threshold.

Until such a formula is frozen, C23 is an infrastructure/negative-result
project, not a paper-level arithmetic-structure claim.  The first-gate result
that chronology survives packet norm for the two C22 controls remains a
finite separation certificate only.

## Frozen object

- words: primitive binary necklaces;
- period: \(1\le n\le10\), with exceptional cyclic equations handled at
  \(n=1,2\);
- return map: later letters act on the left;
- repetitions: \(1\le r\le12\);
- primes: every degree-good \(\ell\le251\);
- base ring: \(R=\mathbb Z[1/(2\cdot5\cdot59\cdot61)]\);
- axes retained: \((\ell,e,w,n,r)\);
- cyclic rotations: exact conjugacy quotient;
- reversal: equality metadata, not quotient multiplicity;
- no transition or parameter averaging.

Here **degree-good** means that reduction preserves the degree of the maps and
the generic rank/length of the chosen affine fixed-point scheme.  It does not
mean étale: nontransverse fibers are retained because they are the events
being measured.  The exact finite-flat locus and every excluded prime must be
derived independently of the observed event table.

## Work packages

### P0 -- mandatory classical baseline

This package precedes all novelty tests.

1. Over \(K=\operatorname{Frac}(R)\), construct
   \[
   P_w(T)=\operatorname{Norm}_{A_{w,K}/K}\det(TI-M_w).
   \]
2. Prove, with the implemented resultant convention,
   \[
   \Delta_{w,r}=\operatorname{Res}_T(P_w(T),T^r-1).
   \]
3. Verify reciprocity, integrality conditions, the automatic divisibility for
   \(r\mid s\), and the Hillar--Levine cyclic-resultant recurrence on exact
   small cases.
4. Record which information in the \(r\)-tower merely reconstructs \(P_w\),
   using Hillar's reciprocal-polynomial rigidity as the control.
5. Label every fixed-word divisibility, recurrence, reconstruction, and
   cyclotomic factor as `CLASSICAL_BASELINE`; none can trigger promotion.

P0 fails if the reported integral \(\Delta_{w,r}\) cannot be shown to agree
with the cyclic resultant on a canonical finite-flat model or a fixed
canonical presentation.

### P1 -- full packet ledger

Extend the square-free algebra engine to every primitive necklace through
period ten.  For each \((w,\ell)\), compute multiplication by \(t_w\) once,
then all \(L_{w,r}\).  Store singularity, kernel dimension, rational witnesses,
the fixed-scheme rank check, and exact artifact hashes.

The ledger is chronological data, not evidence of a new law until a
pre-registered cross-word formula is evaluated on it.

### P2 -- residue degrees

For every singular packet, compute the reduced support algebra of

\[
A_w/(L_{w,r})
\]

and recover closed-point degrees \(e\) from Frobenius fixed dimensions or an
independent elimination factorization.  Nilpotent length and residue degree
must be separate fields.  Good-reduction/cotangent-order phenomena predicted
by Hutz are tagged as controls rather than new arithmetic structure.

### P3 -- integral Fitting/valuation layer

Construct a canonical finite-flat \(R\)-model, or state and freeze a canonical
presentation and denominator-cleared integral lattice, before interpreting
norm valuations.  Compute local Smith/Fitting data at event primes and prove
which reported ideal is invariant under the allowed basis/presentation
changes.  Do not equate modular kernel dimension with norm valuation.

No ideal-theoretic result is promotable until this canonicity condition is
proved.

### P4 -- cross-word/cross-period test

Keep the following levels separate:

0. fixed-word cyclic-resultant identities, recurrences, and reconstruction;
1. fixed-word divisibility when \(r\mid s\);
2. empirical relations between repetitions of a single \(P_w\);
3. an exact relation involving distinct chronological words, possibly also
   distinct periods.

Levels 0--2 are classical baseline or exploratory metadata.  Only level 3 is
a viable novelty target, and only when the relation is stated before the
sealed range is opened and is not reproduced by the controls below.  Broad
post hoc correlations or clustering of prime supports do not count as a
candidate law.

### P5 -- primitive-divisor test

For a fixed word, call \(\ell\) primitive at repetition \(r\) only when

\[
\ell\mid\Delta_{w,r}
\quad\text{and}\quad
\ell\nmid\Delta_{w,m}\quad(1\le m<r).
\]

If only proper divisors \(m\mid r\) are tested, label the result
`DIVISOR-PRIMITIVE`, not Zsigmondy-primitive.  Do not define cross-word
primitivity by ordering a finite ledger: that property changes when the word
or period cutoff grows.  A cross-word primitive divisor may be introduced
only after a natural, cutoff-independent partial order on \((w,r)\) has been
specified.

The present finite ranges can falsify or motivate a conjecture; they cannot
establish an infinite primitive-divisor theorem.

## Mandatory controls

### Structural Hénon controls

- C22 period-seven same-bigram pair;
- C22 period-eight same-trigram pair;
- every cyclic rotation;
- common-reversor reversal equality;
- constant words and simpler autonomous parents;
- shuffled word labels after the complete ledger is frozen.

### Primary cyclic-resultant null

The primary null is not an isolated algebraic unit.  For every observed
packet polynomial \(P_w\), construct an ensemble of monic reciprocal integer
polynomials \(Q\) matched on:

- even degree;
- coefficient-height dyadic bin;
- square-free/non-cyclotomic status over \(\mathbb Q\);
- dyadic bin of \(|\operatorname{disc} Q|\);
- number of prime divisors of \(\operatorname{disc} Q\) in the frozen prime
  range.

For each accepted \(Q\), compute the identical observable

\[
C_Q(r)=\operatorname{Res}_T(Q(T),T^r-1),\qquad 1\le r\le12.
\]

Freeze before generation: the coefficient sampler, acceptance bins, number of
accepted controls per \(P_w\), rejection cap/failure behavior, and a
deterministic seed derived from the literal string `HCS-C23-RECIPROCAL-NULL-v1`
and the word label.  If an exact stratum cannot be populated under the frozen
cap, report it as unmatched; do not adapt bins after examining the target
statistic.

This matched \(Q\)-ensemble is the exact null for all claims depending only on
the packet polynomial and its cyclic resultants.  A signal reproduced by it
is not Hénon-specific.

### Secondary dynamical null

Use reversible polynomial automorphisms only after freezing the family,
degree and coefficient ranges, sample count, parameter exclusions, random
seed, and the same fixed-scheme/prime filters.  The phrase "generic reversible
map" without these data is not a reproducible control.  Apply the same packet
polynomial and cyclic-resultant pipeline to this null.

For both nulls, the exact comparison statistic, uncertainty interval, and
rejection threshold belong to the preregistration.  "Controls look similar"
or "within uncertainty" is not an evaluable criterion without these fields.

## Fast kill rules

Close HCS-C23 as a structure candidate if any of the following holds:

1. no explicit cross-word/cross-period formula can be frozen before the full
   or extended ledger is inspected;
2. every observed relation reduces to a fixed-word cyclic-resultant,
   cyclotomic, recurrence, or reconstruction identity;
3. the matched reciprocal-polynomial null reproduces the proposed relation
   under the pre-registered statistic and threshold;
4. the frozen reversible-map controls reproduce it;
5. residue-degree or valuation data depend on a noncanonical lattice,
   compactification, presentation, or selected root;
6. a primitive-prime claim depends on the finite ledger ordering or changes
   when the \(n\) or \(r\) cutoff grows;
7. the proposed relation disappears on the sealed prime/period extension.

On a kill, retain the packet ledger, cyclic-resultant implementation, and
finite chronology-separation certificates as infrastructure/negative
results, then change dynamical form rather than enlarging an unstructured
scan.

## Promotion rule

Do not form an Euler product or claim a Zsigmondy/strong-divisibility
phenomenon unless all of the following pass:

- an explicit canonical all-period statement involving distinct words or
  distinct chronological periods;
- a proof or a sharply delimited conjecture with sealed out-of-sample
  validation, not only a finite fitted pattern;
- separation from the matched reciprocal-polynomial and frozen reversible
  dynamical nulls;
- a canonical integral/Fitting interpretation;
- rigorous repetition, multiplicity, and primitive-divisor conventions;
- Route-A reevaluation at least at A1.

Two separating primes, or any finite table within
\(n\le10,r\le12,\ell\le251\), cannot by themselves satisfy these conditions.
Without an all-period cross-word law, report C23 as a finite arithmetic
chronology result and close the candidate.
