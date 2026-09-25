# Independent mathematical model audit — ASFS-20260915-CWH01

**Date:** 2026-09-15.  
**Reviewed materials:** the frozen [candidate card](../candidate-card.md),
its documented control clarification, the complete [paper](../paper.md),
[claim ledger](../claim-ledger.md), [summary](../README.md) and
[evidence index](README.md).

**Result:** The stated full-space geometry, prime-only periodic
classification, primitive convention, monodromy, ordinary product and
exact absolute-convergence abscissa pass this bounded mathematical check.
No mathematical correction to Propositions 1--4 was required.

This is a separate model-subagent audit, not independent human peer review,
formal proof-assistant certification or a formal Route evaluation.
It supplies no new operator, external source lock or theorem credit.

## 1. Geometry and ownership

The full surface is a countable disjoint union of planes and therefore has
a countable smooth atlas. Every phase transition is a global polynomial
diffeomorphism. Given output coordinates (Q,P) and the preceding phase k,
the inverse geometric coordinates are

\[
q=2Q+(Q-1)^2+b(n,k)-P,\qquad p=Q.
\]

The derivative of the forward geometric map is

\[
\begin{pmatrix}0&1\\-1&2p\end{pmatrix},
\]

and direct pullback gives dq' wedge dp'=dq wedge dp. Dependence on n and k
does not introduce omitted derivatives: these labels index disjoint open
components, not continuous coordinates.

The unit-roof mapping torus belongs to this same globally invertible map.
A finite flow time traverses finitely many sections, so polynomial escape
over infinitely many iterates is not a finite-time incompleteness. The base
is two-dimensional and symplectic; the suspension is three-dimensional,
with no automatic Hamiltonian or symplectic-manifold assertion.

## 2. Complete periodic classification

For a full period m, cyclic phase return requires K_n to divide m.
Writing the coordinate recurrence around that period and summing gives

\[
0=\sum_{t=0}^{m-1}(p_t-1)^2+\sum_{t=0}^{m-1}b(n,k_t).
\]

All summands are nonnegative real numbers. Therefore all geometric
coordinates equal one and every visited witness count vanishes. The phase
traverses every block, and the blocks cover exactly d=2,...,n-1.
Vanishing is consequently equivalent to n being prime.

Conversely, the phase points (n,k,1,1) do form a cycle when n is prime.
The full phase label gives least period K_n. There is exactly one such
cycle for that n, and none for composite n. This reasoning quantifies
over all real coordinates and all periods; it does not select centres
from a larger periodic family.

The small cases were checked explicitly: n=2 has an empty block and
K_2=1; n=3 also has K_3=1 and no witness. These are distinct fixed
points in distinct components, not a single packet. Primes 5 and 7
likewise give distinct two-packets. Equal time is not an orbit quotient.

Unit-roof flow closure corresponds exactly to base return. Hence the full
flow has one primitive orbit of length K_p per prime and r-fold
repetitions of length r K_p, with no additional closed trajectories.

## 3. Monodromy and trace limitation

On every surviving section point the derivative is

\[
A=\begin{pmatrix}0&1\\-1&2\end{pmatrix}=I+N,\qquad N^2=0.
\]

Thus the primitive monodromy is I+K_p N and the r-fold monodromy is
I+r K_p N. Its two eigenvalues equal one, with nontrivial nilpotent part;
det(I-P_p^r)=0. The manuscript correctly calls this parabolic degeneracy.

Isolation of the actual periodic point is compatible with degeneracy of
the linearization: the full nonlinear cycle-sum proof establishes isolation.
Nevertheless, a periodic-point trace expression that divides by the
displayed determinant is not available. This does not prove that every
possible degenerate trace framework is impossible. No transfer operator
or Fredholm determinant follows merely from the ordinary scalar product.

## 4. Ordinary product and exact convergence boundary

The product uses exactly the full geometric ledger and its fixed unit
clock. For sigma>log 2, counting all integers with K_n=j gives 2^j
possibilities for n>=3, with the separate n=2 term. Therefore

\[
\sum_p e^{-\sigma K_p}
\le e^{-\sigma}+\sum_{j\ge1}2^j e^{-\sigma j}<\infty.
\]

Since K_p>=1, the absolute repetition sum is bounded by this expression
divided by 1-e^{-sigma}. The estimate is locally uniform in the stated
half-plane, so exponentiating the logarithmic series gives a holomorphic,
nonzero ordinary product there.

The lower-bound proof does not need the prime number theorem. If the sum
of prime reciprocals converged, the finite products over p<=N would obey

\[
\prod_{p\le N}(1-1/p)^{-1}
\le \exp\left(2\sum_{p\le N}1/p\right)
\]

and remain uniformly bounded. Their positive geometric expansions contain
1/n for every n<=N by unique factorization, so they dominate the divergent
harmonic partial sums. This is a contradiction.

For p>2, 2^{K_p}<p. At sigma=log 2 the first repetition is therefore
larger than 1/p term by term and is not summable. For smaller sigma its
absolute values only increase. The exact absolute-convergence abscissa
of the logarithmic series is consequently log 2, as stated.

This result concerns the ordinary product and its logarithmic series.
It is not an analytic-continuation, target-divisor or trace theorem.

## 5. Adversarial controls

All three stated comparison rules obey the same exact nonnegative cycle
sum, but their zero-witness fibres differ:

| Comparison | Complete periodic result | Audit note |
| --- | --- | --- |
| b=0 | One K_n packet for every n>=2 | Confirms the square force alone does not select primes |
| b equals block cardinality | Only the fixed packet at n=2 | Empty blocks at n=2 must not be silently discarded |
| Local tests use d dividing n+1 | Exactly the fibres with n+1 prime | For composite n+1 and n>=3 a nontrivial proper divisor is smaller than n and belongs to a block |

At n=2 the shifted comparison also has the empty block, consistently with
n+1=3 being prime. The original and shifted tests are different actions,
not interchangeable owners.

The cycle-sum method would work for other nonnegative finite constraints.
That is a genuine general constraint-programming limitation. It does not
invalidate the derived prime-only ledger for this frozen force. It
limits claims of canonical arithmetic naturalness or uniqueness.

## 6. Clock, lineage and editorial scope

The paper retains the precise lineage deformation: divisor-exclusion
constraints enter phase-resolved geometric forcing. No conjugacy with the
original causal sieve is claimed. Arithmetic affects the full continuous
recurrence and its periodic obstruction; it is not confined to a labels-only
observable or a primes-only carrier.

The clock remains the designed binary macrostep clock. Its K_p values
have logarithmic order but are not log p; primes 5 and 7 already prevent
any constant rescaling from making both periods exact prime logarithms.
One scan evaluates n-2 tests, not O(log n) elementary sequential work.
These limitations are preserved in the card, paper and claim ledger.

Two minor wording clarifications were sent to the author, without any
mathematical change requested:

1. Distinguish absence of an additional arithmetic witness accumulator
   from absence of all discrete state: the cyclic phase k remains present.
2. Describe comparator timing according to the initial card and its
   documented pre-drafting clarification, rather than implying that the
   third comparator appeared in the first version before all other work.

The same-object arithmetic, surface, phase, roof, full periodic ledger,
monodromy and ordinary product remain intact. No formal Route-A coordinate
or Route-B readiness follows from this audit. Route B remains NOT INVOKED.

## 7. Decision supported by the review

Retain the completed, bounded prime-only symplectic packet and ordinary-zeta
result. Any new clock, force, weighting or trace owner needs its own
appropriately frozen contract; it cannot inherit an exact prime-log claim or
a nondegenerate trace formula from this object.

No numerical experiment or cutoff was needed for this review. Only this
review file was written by the reviewer.

## Author response and closure — 2026-09-15

The author addressed both wording suggestions. Paper Section 3 now says
there is no additional arithmetic witness accumulator beyond the cyclic
phase clock. Section 6 now attributes the comparators to the initial card
and its documented pre-drafting clarification before their audits.

The reviewer inspected those changed sentences and confirms that both
comments are resolved. No candidate formula, theorem, proof, roof or
ownership statement changed, so no full mathematical rerun was needed.
This closes the bounded review handoff.
