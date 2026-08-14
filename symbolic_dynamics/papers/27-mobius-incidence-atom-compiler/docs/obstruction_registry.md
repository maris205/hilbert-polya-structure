# Obstruction Registry — SD-C29

## O1 — finite radical conjugacy

Any complete primitive-idempotent lift with fixed diagonal labels is conjugate
to the coordinate family by a unit in \(1+J\). The canonical conjugator is
the incidence zeta matrix itself.

**Decision:** STOP_INCIDENCE_SIMILARITY_COLLAPSE.

## O2 — countable bounded similarity

On \(H_\eta\), \(\eta>1\), the zeta and Möbius transforms converge absolutely
in operator norm and are inverse. Hence \(q_p=Z_\eta E_pZ_\eta^{-1}\).

**Decision:** no new ordinary cyclic determinant.

## O3 — trace-class boundary

At \(u=1\), atom eigenvalues are \(p^{-s}\), so trace class requires
\(\operatorname{Re}s>1\). The marker can shift an absolute-convergence domain
when \(|u|<1\), but it does not continue the \(u=1\) object.

**Decision:** A3_FAIL.

## O4 — source mutation proves too much

If the source relation is altered so that \(6\) covers \(1\), the compiler
selects \(6\). This confirms source equivariance but shows that the compiler
has no independent primality oracle.

**Decision:** retain the mutated-source control in Paper28.

## O5 — scalar and one-sided ablations

Scalar Möbius accepts squarefree composites and is not an idempotent
coefficient at primes. Zeta without its Möbius inverse loses
cross-orthogonality. The unfiltered compiler selects composites.

**Decision:** the cover predicate and two-sided conjugation are both required.

## Remaining loophole

Although \(q_pq_q=0\) for \(p\ne q\), generally \(q_p^*q_q\ne0\). Paper28 may
test this mixed Gram geometry through one chiral/adjoint completion, with
diagonal and mutated-source controls and no target-zero data.
