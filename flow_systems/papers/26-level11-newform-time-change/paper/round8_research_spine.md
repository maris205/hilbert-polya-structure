# Paper 26 Round-8 research spine

Working title: *Exact Homological Obstructions to Hecke Recurrences for a
Level-11 Newform Time Change*

## Paper-level advance

Round 8 upgrades the manuscript spine from “four exact exceptions inside a
numerical rejection” to a complete theorem for the entire frozen finite
population.  All 138 Hecke cycle-owner instances and all 55 word/prime groups
now have exact, mutually exclusive homology and quadratic-moment verdicts.

## Central theorem chain

1. The positive time change has primitive period derivative
   `integral_gamma Re(2*pi*i*f(z)dz)` for the level-11 newform.
2. The prime-to-11 Hecke correspondence produces a finite cycle pushforward,
   not a single primitive orbit, and its unweighted periods satisfy the
   newform eigenrelation.
3. Canonical inverse orientation cancels first variation and adds second
   variation, forcing quadratic degree moments for any scalar all-`s` law.
4. Exact Schreier homology gives the real involution
   `tau(x,y,z)=(-x,y+z,-z)` and one real-period coordinate `k=2y+z`.
5. Every normalized real period is the rational ratio
   `k(output)/k(source)`, so the degree moments are rational sums of squares.
6. The 138 instances split as 2 full kernels, 2 projection-only kernels, and
   134 true nonkernels.  No instance is unresolved.
7. Both primary scalar laws have exactly 4/55 survivors and 51/55 failures;
   the secondary control has 0/55 survivors.  The four positives are
   topological/parity kernels, not primitive Euler evidence.

## Suggested manuscript structure

1. **Frozen flow and period law.** Define the reciprocal-speed time change and
   its exact primitive period variation.
2. **Hecke cycle ownership.** Prove the double-coset cycle pushforward and
   distinguish cycle degree from zeta repetition.
3. **First- and second-variation obstructions.** Derive inverse-pair parity and
   the degree-moment criteria.
4. **Exact homology model.** Present the 12-coset Schreier complex, cusp
   quotient, real involution, and coordinate `k`.
5. **Complete finite taxonomy.** State the 138-instance and 55-group tables,
   including prime/law counts and failure mechanisms.
6. **Why the four survivors do not rescue an Euler mechanism.** Separate full
   kernels from projection-only kernels and run the secondary law control.
7. **Limitations and next theorem obligation.** Emphasize the missing global
   conjugacy census, determinant, continuation, A2 campaign, and quantum lift.

## Claim discipline

The paper may claim an exact theorem for the frozen finite output multiset and
a proved non-implication from the linear Hecke relation to the proposed scalar
second-variation recurrences.  It may not claim a complete primitive-orbit
census, a prime/orbit bijection, primitive Euler factorization, a global
dynamical determinant, a Riemann-zero match, Route-A promotion, or Route-B
readiness.

ARS remains at **Stage 1 RESEARCH**.  Formal Route-A status remains
`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` and
`ROUTE_A_EXPLORATORY`.
