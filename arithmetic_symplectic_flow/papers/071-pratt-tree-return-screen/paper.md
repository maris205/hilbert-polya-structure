# Pratt certificates retain a prime-recursive symbolic relation but have no directed recurrent carrier

**Paper ID:** 071-pratt-tree-return-screen  
**Record ID:** ASFS-SCOUT-20260914-48  
**Date / status:** 2026-09-14; PRE-P0 STOP  
**Route state:** No ASFS Route-A coordinate; Route B NOT INVOKED.

## Research question

Can the prime-factor recursion native to a Pratt primality certificate provide a
new, lineage-respecting recurrent symbolic seed for a later Hénon/symplectic
realization, rather than another advancing sieve window or externally labelled
geometry?

The answer for the direct certificate relation is negative. It retains a real
prime-recursive admissibility relation, but it is well-founded and has no directed
nontrivial return. This is a scoped structural result only; it neither excludes a
different reversible deformation nor claims a general no-go theorem for
prime-symbolic dynamics.

## Frozen object and same-object audit

For a prime p, a Pratt certificate records the complete prime factorization

\[
p-1=\prod_i q_i^{e_i},
\]

together with a suitable witness and recursively valid certificates for the prime
factors q_i. The screened directed relation has one arrow p -> q for each such
prime divisor. The base certificate is at 2.

| Required owner | Object in this screen | Status |
| --- | --- | --- |
| arithmetic source | factor relation among primes in certificates | owned by the source relation |
| symbolic/admissibility content | permitted child labels are prime factors of p - 1 | owned, but tree-valued |
| action and state space | directed rooted certificate relation | not a single-valued self-map |
| closed orbit / repetition | none under the directed relation | scoped FAIL |
| symplectic base, roof, suspension | none | NOT SUPPLIED |
| transfer operator / zeta / determinant | none | NOT APPLICABLE |

Thus no clock, physical flow, or analytic object is borrowed from another
candidate. The prior-work connection reaches the first arrow—prime/composite
observables to symbolic admissibility—but no established sequential Logistic-to-Hénon
or conservative lift follows from the certificate tree.

## Descent lemma

**Lemma (directed Pratt descent).** If p > 2 is a prime node and q is a
prime-factor child of p - 1, then 2 <= q < p. Consequently the directed
certificate relation has no directed cycle of positive length.

**Proof.** Since q divides p - 1, it is a positive divisor of p - 1 and hence
q <= p - 1 < p. A directed cycle would give a strict chain
p_0 > p_1 > ... > p_(r-1) > p_0, a contradiction. The terminal node 2 has
no nontrivial descendant. ∎

This rank is not an externally supplied enumeration clock: it is the node label
already required by the certificate definition. It nonetheless prevents the
certificate's own oriented recursion from furnishing the A1 primitive-orbit and
repetition convention.

## Controls and scope limits

- The relation is richer than a static prime table: primality is recursively
  certified through factor data and witnesses. This is why it was screened
  separately from 041's prime-gap language and 066's finite geometry.
- Treating a certificate edge as reversible would not repair the same object.
  A parent has several possible prime children and reverse traversal requires
  choosing or generating new parent and witness data. A deterministic extension
  would be a new candidate needing its own P0 card and lineage audit.
- A tree can be encoded by a shift or embedded in a geometric system, but selecting
  its paths or importing a Hénon map would not make that geometry an owner of the
  original certificate recursion.

| Gate | Result | Reason |
| --- | --- | --- |
| lineage pre-screen | retained as a bounded prime-symbolic seed | explicit p -> prime factors of p - 1 rule |
| A0 | NOT EVALUATED | no proposed symplectic candidate exists |
| A1 pre-screen | scoped FAIL | direct oriented relation is strictly descending |
| A2 | NOT EVALUATED | no same-object orbit/determinant owner |
| Route B | NOT INVOKED | no Route-A-ready candidate |

## Decision

**Portfolio position: stop/fork.** Do not tune witnesses, reverse isolated edges,
or append an external symplectic carrier to rescue this record. A future
Pratt-derived branch is admissible only if it specifies one autonomous,
non-well-founded prime-symbolic action that generates its own inverse/return data,
then separately passes the full one-object P0 and A0 checks.

## Evidence index

- Vaughan Pratt, [*Every Prime Has a Succinct Certificate*](https://epubs.siam.org/doi/pdf/10.1137/0204018)
- Carl Pomerance, [*Very Short Primality Proofs*](https://math.dartmouth.edu/~carlp/PDF/paper62.pdf)
- [063 monotone-elimination periodic-rigidity rule](../063-monotone-elimination-periodic-rigidity/paper.md) — related stop-rule contrast; this record uses a descending rank, not monotone deletion.
- [069 breadth trilemma frontier](../069-breadth-frontier-cycle-07/paper.md)
