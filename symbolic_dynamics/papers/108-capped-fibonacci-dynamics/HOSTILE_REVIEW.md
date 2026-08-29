# Consolidated hostile-review decision — P108

Decision: **GO_INTERNAL / HOLD_EXTERNAL**.  This consolidation records the
two independent nonauthor reviews of the post-author manuscript.  It is not
an external referee report, novelty certificate, or release authorization.

## Aggregate severity and repairs

- **CRITICAL: 0.**
- **MATHEMATICAL MAJOR: 0.**
- **OWNER/SCOPE MAJOR: 0.**
- **MINOR: 3 across Reviews A and B, all repaired.**

Review A found that the paper-local historical collision boundary was
missing.  The manuscript, README, and claims ledger now distinguish P108's
deterministic capped second-order rule on a finite integer square from P83's
countable Catalan renewal shift, P89's iid reset/golden-mean matrix product,
and P101's random cap--floor interval composition.

Review B found two further minor scope defects.  First, the forward proof
lane had called capped addition and capped multiplication on a real interval
a semiring, although the latter operation need not be associative there.
That unnecessary assertion was removed: the proof now uses only the valid
clipping identity

```text
min(a,min(a,u)+min(a,v))=min(a,u+v)
```

for nonnegative inputs, and the conclusion says “finite saturated dynamics.”
No theorem formula or verifier output changed.  Second, Review B completed
the paper-local within-batch firewall: P107 is an annihilator--power ideal
map, P109 a nilpotent image map on finite-field subspaces, P110 a cyclic
shift--join map on partitions, and P111 an iid positive Heisenberg product.
None shares P108's phase, update, or Fibonacci half-plane depth statistic.

## Independently reconstructed theorem package

Both reviews rederived the exact iterate from the clipping identity and the
two Fibonacci recurrences.  They independently confirmed that `(0,0)` and
`(a,a)` are the only recurrent states; every other nonzero state reaches
`(a,a)`; and the positive-time depth is the first crossing

```text
F_(t-1)x+F_t y >= a.
```

The leading `1` in the lattice-point CDF counts `(0,0)` while `(a,a)` is
already in the half-plane.  The state `(1,0)` is slowest and gives the sharp
maximum

```text
1 + min{k>=0:F_k>=a},
```

including `D_1=2`.  Solving the inverse equations gives image `u<=v`, fibre
sizes `0`, `1`, and `u+1` in the three stated cases, exactly
`a(a+1)/2` Garden-of-Eden states, and the global fibre checksum `(a+1)^2`.
The two fixed points give zeta `(1-z)^(-2)` with no hidden cycle.

## Evidence and owner boundary

Both reviews freshly reproduced the frozen canonical stdout:

```text
capped Fibonacci dynamics exact control: PASS
assertions=67475970
states_checked=3622410
trajectory_formula_checks=60226906
fibre_formula_checks=3622410
caps=a=1..220
```

The literal orbit and reverse-fibre lanes are finite falsification controls,
not proofs for every cap.  Classical Fibonacci identities and matrices,
Binet estimates, saturated-system background, and Artin--Mazur zeta receive
zero novelty credit.  Bounded searches found no direct owner of the complete
finite-map conjunction, but search absence is not an owner certificate.
Contribution density and an undiscovered saturated-recurrence owner remain
the principal external risks.

No mathematical defect remains after the three documented repairs.  Public
posting, submission, specialist contact, novelty, and priority remain
**HOLD_EXTERNAL** pending specialist owner clearance and final artifact QA.
