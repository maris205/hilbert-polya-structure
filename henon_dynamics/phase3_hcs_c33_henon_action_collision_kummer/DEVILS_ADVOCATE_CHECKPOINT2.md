# HCS-C33 Phase-3 devil's-advocate checkpoint

## Verdict

`QUALIFIED_GO` for the exact node/Hill--Kummer theorem.

`STOP` for any claim of a full Kummer wreath group, Picard--Lefschetz
representation, dynamical zeta, or Hilbert--Pólya construction.

## Attacks that failed to kill the theorem

### The factor \(P_9^2\) might be only a discriminant artifact

The exponent is not used as the node proof.  Over
\(K_9=\mathbb Q[A]/(P_9)\), the repeated action value has a separable
quadratic normalization fiber, the remaining marker quotient is coprime,
the plane quadratic tangent cone is nondegenerate, and the two normalization
slopes differ exactly.

### The two points might be lower-period or parabolic

Period five is prime and the fixed factor is removed.  Coprimality with the
marker discriminant keeps the two points distinct.  The resultant with
\(h=\det(I-DH^5)\) excludes multiplier \(+1\); the separate resultant with
\(4-h=\det(I+DH^5)\) excludes multiplier \(-1\).

### The Hill product might depend on branch labels

Branch exchange fixes \(h_1h_2\).  The product is the quadratic norm of the
Hill polynomial, so it lies in the collision field without choosing a
branch.

### The square class might be a normalization artifact

A common Hill scaling multiplies the product by a square.  Independent
branch scalings would change it, but those are not induced by a common
normalization of one dynamical return determinant and are therefore outside
the allowed gauge group.

### Finite-prime evidence might be driving the claim

It is not.  The four frozen primes include square and nonsquare controls.
The theorem is proved by the exact rational field norm, whose odd valuations
force a nonsquare in \(K_9\).

### The action curve might just rename the old cover

It does: the producer derives a linear inverse subresultant and proves the
same function field.  The theorem does not claim otherwise.  The surviving
information is the singular action embedding together with the Hill square
class.

## Surviving vulnerabilities

1. The construction is fixed-period.  It has no trace-compatible
   all-period assembly.
2. One nonsquare does not prove independence of all \(S_9\)-conjugate
   classes or a \(C_2\wr S_9\) group.
3. An ordinary plane node does not automatically produce a
   Picard--Lefschetz representation for the full action family.
4. Generic Maxwell, Hill, Kummer, and symmetric-monodromy mechanisms are
   classical; novelty is restricted to the exact coupled Hénon
   specialization within the documented search bounds.

## Decision

The result is large enough to publish as a precise arithmetic-dynamical
theorem and strong enough to justify a new project directory.  It remains a
Route-A rejection because it provides no all-length dynamical determinant or
self-adjoint spectral structure.
