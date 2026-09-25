# Divisibility parity toggles are bijective but discontinuous, and their arithmetic seed escapes

**Paper ID:** `135-divisibility-parity-toggles`  
**Candidate ID:** `ASFS-SCOUT-20260914-98`  
**Date:** 2026-09-14  
**Status:** `PRE-P0 STOP — PRODUCT-TOPOLOGY DISCONTINUITY; EMPTY-SEED RANK ESCAPE`  
**Evidence:** exact elementary proofs over the full frozen infinite carrier.  
**Route state:** classical A0/A1/A2 `UNASSIGNED`; formal Route coordinates
`NOT EVALUATED`; Route B `NOT INVOKED`.

## Abstract

On all downsets of integer divisibility, toggle the odd intrinsic ranks and
then the even ranks, testing eligibility against each half-step's input.
Both simultaneous updates are well-defined involutions, so their composition
is a bijection. Nevertheless the composition and its inverse are discontinuous
in the frozen product topology. The empty downset produces the exact prime
support after the first half-step and reaches rank at most two after the full
step. Every subsequent full step increases the maximal occupied rank by two.
The construction stops at its topology and arithmetic-source-return
obstructions. The full ideal is a fixed point, so seed escape is explicitly
not a nonexistence claim about all periodic states. No roof, geometric lift,
trace, or determinant is constructed.

## 1. Frozen identity and same-object ledger

The [version-1 card](candidate-card.md) fixes P={2,3,...}, ordered by
divisibility, and J(P), its set of all downsets. The topology is inherited
from {0,1}^P. The rank of n is the maximum number of elements in a strict
divisibility chain ending at n; minimal elements therefore have rank one.
The chain-length convention was clarified before this audit.

| Item | Owner and specification | Evidence state |
| --- | --- | --- |
| Complete symbolic carrier | All I in J(P), including infinite ideals and P | frozen |
| Half-step updates | T_odd and T_even toggle every vertex of the designated rank parity simultaneously | well-defined involutions |
| Full action | F=T_even composed with T_odd | bijective; discontinuous |
| Allowed arithmetic data | Integer divisibility and its intrinsic rank only | no prime list, cutoff, fitted parameter, or prescribed word |
| Source state | Empty ideal | F^t(empty) has rank at most 2t, for integer t>=0 |
| Observable | Coordinate membership of this same downset | prime word at first half-step; full first step also contains semiprimes |
| Periodic convention | Least positive full F-period, modulo cyclic phase | source has no period; general classification not undertaken |
| Symplectic base, roof, suspension, operator, zeta | None supplied | NOT APPLICABLE or NOT SUPPLIED at this symbolic screen |

Neither the topology nor the toggle schedule changes in the proof. The map is
distinct from the rowmotion operation in [132](../132-divisibility-rowmotion/paper.md).
Its bijectivity is established directly, without transferring the finite
rowmotion theorem or any earlier Route result.

## 2. Question and lineage

The bounded question is whether a local parity decomposition can retain the
intrinsic prime/composite divisibility constraint while providing a reversible
continuous action and a returning arithmetic source state.

The [prior-work lineage](../../docs/prior_work/README.md) is realized at its
prime/composite-observable to symbolic-admissibility arrow: the state rule
requires the indicator of n to be no greater than the indicator of each divisor
d>=2. The minimal vertices of this particular integer poset are precisely
primes. Rank parity supplies a fixed, autonomous two-stage deformation of the
boundary update; it is not a time-dependent fitting schedule. No conjugacy
with a sequential sieve or a Logistic/Henon map is asserted. Conservative and
symplectic realization remain absent.

The strongest supported result is an exact combination of algebraic
reversibility, topological discontinuity, and source escape. There is no
prime-to-primitive-orbit correspondence, prime-dependent clock, or analytic
owner to evaluate.

## 3. Definitions and elementary order facts

Write d<.n when n covers d: d properly divides n and no integer of P lies
strictly between them under divisibility. This holds exactly when n/d is
prime. The rank r(n) equals Omega(n), the number of prime factors counted with
multiplicity. Indeed every strict chain step increases Omega by at least one,
and successively multiplying the factors of n constructs a chain attaining
Omega(n) elements. This is a proof of the rank interpretation, not prime data
supplied to define the action. In particular, cover neighbors have opposite
rank parity.

For I in J(P), the vertex n can be toggled exactly when

\[
B_n(I):\quad
\text{all lower covers of }n\text{ belong to }I,
\qquad
\text{all upper covers of }n\text{ are absent from }I.
\]

If n is absent, all its upper neighbors are already absent; addition requires
its lower covers to be present. If n is present, its lower covers are already
present; removal requires its upper covers to be absent. Checking covers is
sufficient: every interval of integer divisibility is finite and every strict
comparison is linked by a finite chain of covers. Empty lower-cover tests
are true. Upper covers are infinite in number and remain part of the test.

## 4. Exact audit

### Proposition 1 — The two simultaneous updates are involutions

For either parity c, define T_c(I) by toggling precisely those vertices of
parity c satisfying B_n(I). Then T_c maps J(P) to J(P) and T_c squared is the
identity. Consequently F is a bijection with inverse T_odd composed with
T_even.

**Proof.** Across any cover edge exactly one endpoint has parity c. If the
lower endpoint changes from one to zero, its upper endpoint was absent by
the eligibility test and remains absent. If the upper endpoint changes from
zero to one, its lower endpoint was present and remains present. The other
two changes cannot violate the downset inequality. Thus every cover
inequality is preserved, which implies all divisibility inequalities.

Every B_n test for a toggled vertex depends only on its cover neighbors;
none has parity c. Those neighbors remain unchanged throughout the
simultaneous update, so B_n(T_c(I))=B_n(I). A second update toggles exactly
the same vertices back. This argument defines the infinite update directly
coordinate by coordinate; it uses no convergence of an infinite composition
of individual toggles. QED.

### Proposition 2 — F and its inverse are discontinuous

Let q_j be distinct odd primes tending to infinity and put

\[
I=\{2\},\qquad I_j=\mathord\downarrow(2q_j)
=\{2,q_j,2q_j\}.
\]

Then I_j converges to I in J(P), but the coordinate at 2 of F(I_j) is one
for every j whereas the coordinate at 2 of F(I) is zero.

**Proof.** For any fixed integer coordinate other than 2, membership in I_j
eventually vanishes. This is precisely product convergence to I. At I the
prime 2 has no present upper cover and is removed in the odd half-step. At
I_j its upper cover 2q_j is present, so 2 is not removed. The following even
half-step never changes the odd-rank coordinate 2. Hence F fails continuity
at I. This also proves discontinuity of T_odd there.

For the inverse use K=downarrow(4)={2,4} and
K_j=downarrow(4q_j). These converge to K. At K, the even half-step removes
4; at K_j its upper cover 4q_j blocks removal. The following odd half-step
leaves coordinate 4 unchanged. Thus F inverse, and also T_even, are
discontinuous. QED.

The primes q_j here constitute an exact counterexample sequence in a proof;
they are not parameters or input data for F. No finite numerical cutoff can
establish or eliminate this failure of continuity.

### Proposition 3 — The complete empty-source orbit does not return

For k>=0 define I_k={n>=2:r(n)<=k}; in particular I_0 is empty. Then

\[
T_{\mathrm{odd}}(I_0)=I_1=\{\text{all primes}\},
\qquad F^t(I_0)=I_{2t}\quad(t=0,1,2,\ldots).
\]

More generally,

\[
F(I_k)=
\begin{cases}
I_{k+2},&k\text{ even},\\
I_0,&k=1,\\
I_{k-2},&k\geq3\text{ odd}.
\end{cases}
\]

Every I_k lies on the same nonperiodic full F-orbit.

**Proof.** For k>=1, the removable elements of I_k are exactly those of
rank k, and the addable elements are exactly those of rank k+1. Every lower
rank member has a present upper cover, obtained by multiplying by 2. Every
excluded element of rank above k+1 has an excluded lower cover. At I_0,
only rank one is addable and nothing is removable.

The odd half-step therefore raises even k by one and lowers odd k by one.
The even half-step raises odd k by one, lowers positive even k by one, and
fixes I_0. Composition gives the displayed formula. The full orbit through
the empty state, listed in its direction of motion, is

\[
\ldots,I_5,I_3,I_1,I_0,I_2,I_4,I_6,\ldots.
\]

These states are pairwise distinct because 2^{k+1} belongs to I_{k+1} and
not to I_k. No state on this orbit can have a finite positive period. QED.

The prime-indicator state is the intermediate half-step output and also a
full-orbit predecessor of the empty state. The complete first output F(I_0)
is I_2, which additionally contains products of two primes with multiplicity.
Reporting F(I_0) itself as the prime indicator would conflate a half-step
with the frozen unit of time.

## 5. Controls, negative results, and limits

| Control | Exact scope and finding |
| --- | --- |
| Algebraic inverse | Both half-steps are involutions on all downsets, including infinite ones; this repairs the set-bijection obstruction of 132 for this new map only. |
| Product topology | Arbitrarily large upper covers can change removal at the fixed coordinate 2 or 4. Both directions of the full action fail continuity. |
| Full-ideal control | P is fixed: every vertex has a present upper cover and none can be removed. Its indicator is identically one, so it supplies no prime-selective returning source. |
| Other periodic states | Not classified. Source escape and discontinuity do not imply an empty full periodic ledger. |
| Finite-poset comparison | A finite graded-poset version is a permutation of finitely many ideals and is continuous in the discrete product topology. The upper boundary and finite neighbor tests are changed inputs, so its finite periods give no periods for J(P). |
| Simpler-parent control | The same parity rule on one infinite chain has the same rank-initial source escape. That escape is a graded-order effect and is not a prime-distribution theorem. |
| Arithmetic labels | Minimality identifies ordinary primes only for the frozen divisibility relation. Arbitrary relabelling does not preserve this integer prime/composite observable. |
| Clock/geometry ownership | No bounded quotient, selected recurrent core, topology replacement, thickening, or geometric centre selection is introduced. |

The calculations are exact statements on the infinite carrier. There are no
finite orbit tables, numerical precision limits, spectral experiments, or
external analytic formulas. This package makes no literature-wide novelty
claim. Its elementary proofs do not invoke a finite-toggle theorem.

## 6. Gate decision

| Obligation | Evidence | Status |
| --- | --- | --- |
| Symbolic arithmetic source | Prime support at first half-step, with full-time rank propagation explicit | exact source-level positive control |
| Algebraic reversible action | Explicit two-sided inverse on J(P) | established |
| Continuous action on frozen topology | Coordinate counterexample at {2}; analogous inverse failure | scoped FAIL; decisive pre-P0 stop |
| Returning arithmetic-source packet | All rank-initial states form one infinite orbit | scoped FAIL on this source orbit |
| Geometric, clock, analytic ownership | No such objects supplied | NOT SUPPLIED |
| Classical A0/A1/A2 | No classical symplectic suspension admitted | UNASSIGNED; formal Route coordinates NOT EVALUATED |
| Route B | No evaluation | NOT INVOKED |

**Decision: stop; portfolio position: fork.** The discontinuity is sufficient
to end the audit of the frozen topological action, and the independently
planned source check also excludes its intended return. A different topology,
bounded carrier, toggle schedule, or selected recurrent subsystem requires a
new card. No classification of the remaining periodic states is pursued after
this stop. The same-object ledger remains intact.

## Evidence index

The [candidate card](candidate-card.md), [claim ledger](claim-ledger.md),
[evidence record](evidence/README.md), and [package overview](README.md) carry
the identical candidate ID and stop status. Propositions 1--3 are the primary
evidence for all infinite statements.
