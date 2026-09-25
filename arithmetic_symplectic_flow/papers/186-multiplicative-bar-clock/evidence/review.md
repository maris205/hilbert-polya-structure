# Separate-call bounded algebra and clock review

**Paper ID:** 186-multiplicative-bar-clock  
**Candidate ID:** AFC-20260916-MBC01  
**Research date:** 2026-09-16, following the supplied workspace date.  
**Candidate status:** STOP — PRIME H1 CLASSES, BUT COMPOSITE HIGHER HOMOLOGY AND WRONG POINT-ORBIT CLOCK.  
**Review disposition:** SUPPORTED WITHIN THE DECLARED BOUNDED SCOPE; no required mathematical correction.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Review provenance and exact scope

This is the actual review invocation `multiplicative_bar_reviewer`, separate
from root's author invocation. I first read the frozen version-1 card and
derived the differential, first-homology, weight-4/6 and pure-weight clock
tests before reading the paper. I then read all five completed core files:
[README](../README.md), [card](../candidate-card.md), [paper](../paper.md),
[ledger](../claim-ledger.md) and [evidence index](README.md). Only this
review file was written by this invocation; no author core was edited.

The review is nonblind. It inherits the current model and shared context;
the dispatch disclosed the proposed interpretation and expected ownership
risk. Preliminary mathematical feedback was sent to the author before
final core freezing. Thus distinct invocation and separately worked
derivations do not establish independent model errors, a blinded design,
cross-model agreement or human peer review. No helper or external model
was used. No venue-fit or publication-readiness assessment was requested.

ARS was applied only as bounded claim/evidence/reasoning and counterargument
discipline, not as a full editorial or publication pipeline. The reviewed
question is the exact algebra and clock test below. I did not independently
verify the Positselski citation, its wording or the author's source-access
record; that bibliographic material remains outside this receipt's scope.
Nor did I repeat the historical collision search or audit the proofs of
the earlier packages cited only as comparisons.

## Bound author bytes

The hashes were obtained with `sha256sum` on the four named author files
after the author reported them ready. The evidence index remains unbound
for later administrative closure. A change to a bound file requires a
targeted re-review; this receipt does not cover later bytes automatically.

| Core file | SHA-256 |
| --- | --- |
| [README.md](../README.md) | `02fbe0780966b3123e7d17ae8c6b86f075f5b994e29cbfb26dfd1ccc6ab7d3d6` |
| [candidate-card.md](../candidate-card.md) | `bad1ff1435d988ad900a07ff2193c7092abda0ec749624a8ba36f460cbae2cb8` |
| [paper.md](../paper.md) | `c15e4666e1caf47f0eb860dd4fd2e63ce20d114686d0b7ddcc2d55ecca9610f4` |
| [claim-ledger.md](../claim-ledger.md) | `2d1f694c5b75e0047310d6e9d2f80e177c8083cadfb444087aa3b10e633446d2` |

The clock tool returned `2026-09-15 16:16:19 UTC` at this binding step.
That raw tool timestamp is retained separately from the supplied research
date; it has not been silently normalized to the latter.

## Re-derived mathematical checks

### 1. Differential and full first homology

For two original merge positions i<j, first merging at j and then at i
has sign (-1)^(i+j-2). First merging at i and then at j-1 has sign
(-1)^(i+j-3). The resulting words coincide; for adjacent positions this
uses associativity. These terms cancel in pairs, proving d^2=0, including
the zero maps at the bottom of the positive-degree complex.

Merging preserves product N. Since vectors have finite support, neither a
cycle nor a boundary at one weight obtains contributions from a different
weight. The direct-sum homology statement in Lemma 1 is therefore valid
without a completion or infinite-sum argument.

For all N, C_(1,N) has the single basis vector [N]. Every two-factor word
maps to its composite product, and every composite product has such a
two-factor word. Consequently im d_2 is exactly the span of composite
basis vectors, and H_1 has exactly the prime basis classes. This proves
Proposition 2 for all first homology, not merely a sampled range.

### 2. Complete weight-4 and weight-6 complexes

At weight 4 the only positive-degree basis vectors are [4] and [2|2].
The latter maps to the former with coefficient +1, so the complete
positive-degree complex is acyclic.

At weight 6 the basis is [6] in degree one and [2|3], [3|2] in degree
two. The differential is the row matrix (1 1). Three factors at least
two would have product at least 8, so there are no higher chain groups
at either weight 4 or weight 6. Thus

    H_(1,6) = 0,
    H_(2,6) = C ([2|3] - [3|2]),
    H_(k,6) = 0 for k >= 3.

The displayed degree-two class is a genuine nonzero class in the full
homology, not just in a truncation: weight preservation excludes every
possible boundary from another weight. This is a sufficient exact
counterexample to prime-only full homology. It does not classify all
higher homology or all composite weights.

### 3. Action, actual time and full amplitude multiplicity

On each weight sector U_t is scalar multiplication by exp(i t log N).
Exponential addition gives the group law, and preservation of N by d
gives chain compatibility. The induced action on the algebraic homology
is consequently well-defined. Its complete smooth action on each finite-
dimensional sector needs no claim about a topology on the full direct sum.

For every nonzero pure-weight class v,

    U_t v = v  iff  t log N is an integer multiple of 2 pi.

As N>=2, the least positive time is exactly 2 pi/log N and positive
repetitions have time r times that value. The frequency log N is not the
period. The zero class is fixed for every time and has no least positive
period; the paper correctly keeps it separate.

For any chosen nonzero v in a complex line, the orbits of rho v with
rho>0 are pairwise distinct, since U_t preserves complex modulus. Each
is the full circle of that radius, with orientation supplied by the
positive-time action. This coordinate choice proves continuous orbit
multiplicity without deleting any amplitudes or replacing the carrier by
a preferred normalized vector. It applies both to a prime H_1 line and
to the surviving composite H_(2,6) line. Proposition 4 is supported.

## Counterarguments, ownership and disposition

The most tempting contrary argument is that the positive H_1 result has
already isolated primes. It has isolated prime basis classes in one
homological degree, not the full frozen graded object. Projecting away
H_2 changes that object and still leaves the reciprocal-logarithmic
periods and continuous amplitude circles. A permutation quotient,
projectivization or new clock is not an in-place repair and is not proved
to work here. The paper makes these distinctions explicitly.

The same-object ledger remains intact: all words, positive degrees,
weights, differential and character action match the frozen card.
The source-level result is retained while its proposed full prime-orbit
interpretation receives a scoped STOP. The arbitrary-generator control
properly limits a claim of arithmetic naturalness; it does not invalidate
the integer calculation. Naturalness remains OPEN.

No blocking defect was found in the reviewed claims. The exact weight-6
counterexample is decisive for the frozen target, independently reinforced
by the clock and multiplicity tests. No full higher-homology theorem,
mixed-weight periodic classification, trace, determinant or quantum
construction was reviewed or is implied. No formal Route coordinate was
evaluated; classical A0--A2 fields remain NOT APPLICABLE and Route B
remains NOT INVOKED. Any later changed complex, quotient or action must
be frozen as a new candidate, rather than silently extending this receipt.

All mathematical checks above are exact symbolic derivations, not finite
numerical evidence. Root retains ownership of the single integrated
Round18 link, identity, status, review-hash and protected-file check.
