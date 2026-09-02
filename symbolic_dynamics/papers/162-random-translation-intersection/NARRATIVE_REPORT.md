# P162 narrative report

## Outcome

The paper turns the RTI scout into one compact theorem package without
inflating the classical ingredients.  Its central organizing fact is that a
long random history has a lossless sufficient statistic: the subspace spanned
by its translations.  This gives the temporal law, but it is not yet the
paper's distinguishing axis.  The second half asks the inverse question for
an arbitrary target and resolves it by the target's translation stabilizer.

## Mathematical progression

The literal update is an erosion by the two-point subspace `{0,v}`.  Erosions
compose by adding their structuring subspaces, so after `t` steps every source
has been intersected over all translations in `H_t=span(v_1,...,v_t)`.  A
fixed rank-`r` subspace has exactly

```text
S(t,r)=product_{i=0}^{r-1}(2^t-2^i)
```

ordered generating histories.  Gaussian subspace counting then supplies the
whole rank law.  Full span empties every non-full source, and `V\{0}` shows
that this bound cannot be improved: its erosion by `H` is exactly `V\H`.

For a prescribed target `B`, forward rank information alone is insufficient.
The history span must lie in `Stab(B)`.  Once it does, `B` consists of full
`H`-cosets.  Every outside coset may be populated by any proper subset, and
these choices are independent.  Weighting by source size and summing over
all admissible subspaces and their histories produces the arbitrary-target
polynomial in the main theorem.  This axis survives removal of the classical
erosion and random-rank components because it is an inverse enumeration
conditioned on target shape.

## Required gate repair

The hostile gate found one minor presentation defect in the scout's one-step
specialization: odd target size forces trivial stabilizer, making the
nontrivial-stabilizer exponent formally half-integral.  The manuscript now
uses two branches:

```text
1                                           if s=0,
1+(2^s-1)3^(2^(d-1)-|B|/2)                  if s>=1.
```

The second exponent is integral because a target with nontrivial translation
stabilizer is a union of two-point orbits.  No zero-times-undefined convention
is used.

## Contribution and ownership boundary

The paper assigns zero contribution credit to erosion algebra, generic
morphological iteration, stochastic morphology, and finite-field rank laws.
The assessed residual is the exact conjunction of a sharp worst-source
witness, a target-stabilizer weighted inverse atlas, and recovery of the
stabilizer dimension from a boundary fibre statistic.  The existing bounded
search found no direct owner of that conjunction, but this remains a scoped
non-hit rather than a novelty claim.

## Release posture

The artifact is anonymous and remains `HOLD_EXTERNAL`.  It is not approved
for posting, submission, circulation, or author contact.  At the Round-0
author-draft stage, hostile review rounds were deliberately outside the
drafting task; both are now complete and closed.
