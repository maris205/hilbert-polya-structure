# Reflection restores prime returns but makes prime powers primitive too

**Paper ID:** 217-divisor-scattering-return  
**Candidate ID:** ANG-20260918-DPR01  
**Date:** 2026-09-18  
**Status:** STOP — EVERY INTEGER COMPONENT HAS PRIMITIVE RETURNS; PRIME POWERS ARE NEW ORBITS, NOT REPEATS.  
**Evidence:** exact proof; no numerical experiment.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

An ordered-port permutation on the full family of divisor-cover graphs
restores prime-component closed orbits without choosing prime components
in advance. A single multiplicative edge metric supplies a complete
positive-roof suspension. However, finiteness and invertibility force
every integer component, including every composite, to have primitive
closed orbits. More precisely, the component p^k has one primitive orbit
of time 2k log p. For k>1 it is not the k-fold traversal of the orbit in
component p, despite equality of time lengths. A two-distinct-prime
component pq has two oriented primitive orbits of time 2 log(pq).
These exact controls stop the proposed prime-only dictionary. No
geometric lift or analytic repair is pursued.

## 1. Frozen identity and lineage

The [version-1 card](candidate-card.md) precedes this proof. Let D_n be
all positive divisors of n>=2, including 1 and n. Its undirected cover
graph G_n joins u and v when they are comparable by divisibility and no
element of D_n lies strictly between them in that order. At each vertex
v order its neighbors by their ordinary integer labels and cyclically
permute that list, denoting the permutation by s_(n,v). A one-element
list has the identity successor. All components are retained in

\[
 X=\{(n,u,v):n\ge2,\ \{u,v\}\in E(G_n)\},\qquad
 F(n,u,v)=(n,v,s_{n,v}(u)),\qquad
 \tau(n,u,v)=|\log(v/u)|.
 \tag{1}
\]

X is discrete. The transformation groupoid of this map and its roofed
suspension are the declared broadened object. No operator is assigned.

| Owner field | Definition and boundary |
| --- | --- |
| Arithmetic input | All integers n>=2, integer order and divisibility; no prime-selected list |
| Symbolic state | All oriented cover edges in all G_n, including the component label |
| Evolution | The single permutation F in (1); no inter-component transitions |
| Clock | One declared all-edge logarithmic metric, not a fitted per-prime roof |
| Flow | Endpoint quotient (x,tau(x))~(F(x),0), ordinary time translation |
| Primitive convention | Least F cycle, then one suspended orbit; only cyclic phase is identified |
| Repetitions | Multiple traversals of that same flow orbit; component n unchanged |
| Analytic owner | NOT CONSTRUCTED; no zeta, determinant, trace or Hilbert space imported |
| Classical geometry | No positive-dimensional symplectic or Hénon realization supplied |

The exact [prior-work](../../docs/prior_work/README.md) arrow is
prime/composite divisor observables -> symbolic cover admissibility ->
deterministic port evolution. The preserved test is absence or presence
of a nontrivial factor between 1 and n. This is a replacement of a
sieve-inspired symbolic source, not a proved intertwining with a previous
chronological sieve. The later sequential/Hénon/symplectic arrows remain
unrealized. Naturalness is not inferred from a logarithm appearing in (1).

The nearest local control [136](../136-factorization-nonbacktracking-flow/paper.md)
uses ordered factor words and excludes immediate edge reversal. Its prime
components have no paths. Here the vertices, unit convention and return
rule are different: prime components may be traversed back and forth.
The new ID makes that change explicit. No theorem or Route credit is
transferred from 136, 194, 201 or 213.

## 2. Complete elementary owner checks

### Proposition 1 — Bijection, topology and completeness

F is a homeomorphism of the countable discrete state X. Every component
X_n is nonempty and finite, and every state in X is periodic. The roof
is continuous and bounded below by log 2, so the suspension is complete
in both directions.

**Proof.** D_n is a finite subset of {1,...,n}. Descending chains of
divisors connect each vertex to 1 via cover edges, so G_n is connected.
It contains at least two vertices, hence no isolated vertex. Each
neighbor list is nonempty finite and its successor is a permutation.
If t_(n,v) is its inverse, then

\[
 F^{-1}(n,v,w)=(n,t_{n,v}(w),v).
 \tag{2}
\]

This is a valid edge and composing (1) and (2) in either order gives
the identity. Continuity in both directions is automatic on the discrete
space. The arrows X times Z with the discrete topology give the declared
transformation groupoid; this is not the non-locally-compact 194 carrier.

Each X_n is a nonempty finite set invariant under a bijection. It is a
disjoint union of finite permutation cycles; there are no transients.
For comparable distinct integers u,v the larger divided by the smaller
is an integer at least 2. Hence tau>=log 2. At most finitely many roof
crossings occur in a bounded time interval, forwards or backwards using
(2). This defines the flow for every real time. QED.

The map is invertible. No general time-reversal symmetry of an arbitrary
ordered neighbor list is assumed or needed.

### Proposition 2 — Exact primitive and repetition convention

For each least F cycle x,Fx,...,F^(l-1)x there is one primitive suspended
orbit, of time

\[
 T(x)=\sum_{j=0}^{l-1}\tau(F^jx).
 \tag{3}
\]

Its r-fold traversal has time rT(x) and remains in the same n component.
There is at least one such primitive orbit for every integer n>=2.

**Proof.** The suspension over a finite permutation cycle is the cyclic
gluing of l oriented intervals with strictly positive lengths. A return
to a given interior point must complete an integer number of edge
crossings ending in the same edge state and the same height. The first
such return traverses exactly the l-cycle, with total time (3).
Endpoint representatives give the same circle, not extra orbits.
Repeating the traversal adds this same length r times. The component
observable N(x)=n is constant under F and under suspension gluing, hence
under the entire flow. The last assertion follows from Proposition 1.
QED.

This proposition already defeats prime-exclusive primitives: every
composite component has a full intrinsic periodic orbit. The following
short calculations identify the precise prime-power and orientation
errors. They do not reopen the failed dictionary.

## 3. Decisive arithmetic controls

### Proposition 3 — All prime-power components give new primitives

For every prime p and every integer k>=1, X_(p^k) is a single F cycle of
least map period 2k. The corresponding flow has exactly one primitive
orbit in that component, with time 2k log p.

**Proof.** The divisors are 1,p,...,p^k, and the cover graph is the path

\[
 1-p-p^2-\cdots-p^k.
 \tag{4}
\]

At an interior vertex there are exactly two neighbors, so cyclic
successor exchanges them; at each endpoint it fixes the sole neighbor.
Starting with (1,p), the directed edge states traverse the whole path
upward and then downward:

\[
 (1,p),(p,p^2),\ldots,(p^{k-1},p^k),
 (p^k,p^{k-1}),\ldots,(p,1).
 \tag{5}
\]

For k=1 this list is simply (1,p),(p,1). Every one of the 2k oriented
edges appears exactly once; the next state is the first state. Thus
2k is the least map period and no other cycle is omitted. Every roof
value on (5) is log p, giving the asserted primitive time. QED.

For k=1 the candidate has the proposed prime return, up to the uniform
round-trip factor 2. For k>1 its orbit is a **different primitive**,
not a repeat of that prime orbit:

\[
 T(\gamma_{p^k})=kT(\gamma_p),\qquad
 \gamma_{p^k}\ne\gamma_p^{\,k}.
 \tag{6}
\]

Here the right-hand notation means repeated traversal, not a second
geometric orbit. Equality is excluded by the invariant N: the two
traversals lie in the disjoint N=p^k and N=p components. In particular,
n=4 already supplies a four-state primitive circle of time 4 log 2,
as well as the twice-traversed circle in n=2 with that same time.
Matching lengths does not permit merging them.

### Proposition 4 — A squarefree component has two oriented primitives

For distinct primes p<q, G_(pq) is the four-cycle

\[
 1-p-pq-q-1.
 \tag{7}
\]

The eight edge states split into two F cycles of least map period 4,
one in each orientation, both with primitive flow time 2 log(pq).

**Proof.** The four listed divisors are exhaustive. The pair 1,pq is
not a cover, and p,q are incomparable, giving exactly (7). All vertices
have degree two, so an incoming edge continues to the other neighbor.
The two orientations are disjoint and exhaust the eight edge states.
The four roof values in either cycle are log p, log q, log p, log q.
They sum to 2 log(pq). Reversal is not a cyclic phase of the other
oriented edge cycle, and the frozen rule does not quotient by reversal.
QED.

Thus even the simplest two-factor composite supplies multiplicity two.
This is not a statement that every general G_n has the same cycle count;
that finer count is unnecessary after the stop.

## 4. Controls and what is not repaired

1. **Prime versus prime power.** Reflection restores the prime path absent
   in 136, but also gives a new primitive for every p^k. Removing these
   components would select the answer after the test and change X.
2. **Order control.** On (4) and (7), neighbor degrees are at most two.
   Every cyclic successor on the same neighbor set is the same permutation.
   Reordering ports cannot remove either counterexample. No claim of
   order independence for higher-degree graphs is made.
3. **Clock control.** Changing all roofs to 1 is a different clock. It leaves
   these primitive orbit distinctions intact and changes their lengths to
   2k and 4. The failure is therefore not a missing constant normalization.
   No altered roof is installed in the frozen candidate.
4. **PROVES_TOO_MUCH.** Any finite connected graph with at least one edge,
   cyclically ordered neighbor lists and positive edge roofs has the same
   finite-permutation recurrence argument. Such recurrence does not select
   primality. Arithmetic determines this graph family, but closedness alone
   does not distinguish its primes from composites.
5. **Geometric ownership.** A later hyperbolic transverse lift might avoid
   a continuum of periodic points, as illustrated by the separately owned
   [052 control](../052-hyperbolic-wheel-packet-lift/paper.md). If it faithfully
   retains the full source packet ledger, however, these extra composite
   primitives remain. Deleting their centres would not be a faithful lift.
   No lift is built here after the arithmetic stop.

No local fixed-point selection, trace subtraction, equal-length quotient,
prime-table restriction, determinant cancellation or self-adjoint operator
is used to rescue (1). Infinite orbit-product convergence is not evaluated.
The elementary all-n argument, not a finite enumeration, supports the
global claim in Proposition 2.

## 5. Gate and portfolio decision

| Gate | Exact evidence | Disposition |
| --- | --- | --- |
| T0 | Full discrete carrier, bijection, groupoid and complete suspension | Established for this broadened owner only |
| T1 | Divisibility is internal to graph admissibility; logarithmic edge metric declared uniformly | Scoped source/clock ownership; natural A0 remains OPEN, no prime-only mechanism established |
| T2 | Full finite-cycle characterization and repetitions; every n has primitives; exact p^k and pq controls | General convention established; target prime-only/prime-power dictionary FAILS |
| T3 | No operator or global product developed after stop | NOT ADVANCED |
| Classical A0/A1/A2 | No positive-dimensional symplectic realization | NOT EVALUATED; no classical passage inferred |
| Formal Route / B | No evaluation invoked | UNASSIGNED / NOT INVOKED |

**Decision: STOP this candidate; FORK the search.** The decisive reason is
not a delicate analytic estimate: a nonempty finite permutation component
at every integer forces composite primitive returns. This does not prove
that every arithmetic graph, infinite noncompact dynamics or conservative
construction has that defect. A next candidate must let its arithmetic
mechanism distinguish recurrent from escaping states before applying a
packet-preserving geometric lift; simply replacing the walk's clock or
thickening its finite states cannot settle that question.

## Evidence, scope and disclosure

The [claim ledger](claim-ledger.md) and [evidence index](evidence/README.md)
record the frozen inputs, low-memory method and actual verification.
All new results above are elementary proofs, with no numerical run,
external theorem import or novelty claim. The prior-work guide is used
for lineage, not to certify its linked external Paper-6 assertions.
ARS contributes bounded claim/evidence/reasoning and adverse controls,
not a full publication workflow, venue review or human peer review.
Model assistance is disclosed; there are no human-subject data or
new funding, authorship, conflict-of-interest or ethics attestations.
