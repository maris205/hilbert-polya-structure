# Sequential divisor kicks on full tori retain composite cycles and continuous prime families

**Paper ID:** 172-compact-toral-divisor-kicks  
**Candidate ID:** ASFS-20260915-TDK01  
**Date:** 2026-09-15  
**Status:** STOP — OWNED COMPOSITE CYCLES AND CONTINUOUS PRIME FAMILIES.  
**Evidence:** exact construction and scoped counterexamples; no numerical claim.  
**Route:** formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

A fixed cyclic scan tests one potential proper divisor per iterate and
uses that witness immediately as the amplitude of a smooth area-preserving
toral kick. All integer labels, all scan phases and all toral points are
retained. We prove the full map is a two-dimensional symplectomorphism
and that its unit-roof suspension is complete. However, its common invariant
toral origin yields a primitive closed orbit above every integer, including
the explicit composite 4. On each prime component the entire zero-momentum
circle supplies distinct primitive flow orbits of time p-1. Thus this is a
genuine sequential arithmetic-to-conservative construction, but not a
prime-exclusive finite-multiplicity or prime-logarithmic orbit mechanism.
The counterexamples stop this contract without classifying unrelated
composite orbits, changing the roof, or excluding other compact lifts.

## 1. Frozen identity, source, and ownership

The [version-1 card](candidate-card.md) was written before this audit.
For n >= 2 take D_n={1,...,n-1} with cyclic successor d^+ and set

\[
M=\coprod_{n\geq2}\coprod_{d\in D_n}\mathbb T^2_{n,d},
\qquad \omega=dq\wedge dp,
\qquad w(n,d)=\mathbf1_{\{2\leq d<n,\ d\mid n\}}.
\]

Use \(\pi\) only for the usual circle constant. The fixed map is

\[
Q=q+p\pmod1,\qquad
F(n,d,q,p)=\left(n,d^+,Q,
 p+\frac{w(n,d)}{2\pi}\sin(2\pi Q)\pmod1\right).
\tag{1}
\]

| Same-object field | Exact owner / limitation |
| --- | --- |
| Geometry | Every displayed torus with its canonical area; each fixed-n finite union is compact, the full countable M is noncompact and disconnected. |
| Map and parameters | Exactly (1); amplitude and linear twist fixed before audit, no per-prime coefficients. |
| Arithmetic | The current single divisor test affects the current toral map. No completed prime mask, aggregate count, selected prime label, or prime table is an update input. |
| Symbolic/sequential source | Observable w(n,d), phase d, conserved n; no Markov conjugacy or all-prime chronological enumeration is asserted. |
| Roof and flow | tau=1 on all M; S=(M times [0,1])/((x,1)~(Fx,0)), with the same translation flow throughout. |
| Measure | Haar area one on each torus, counting over components; invariant sigma-finite measure of infinite total mass, with Lebesgue suspension time. |
| Primitive convention | Least full-state period, oriented cyclic identification, every toral coordinate retained; repetitions rT. |
| Analytic and later owner | No operator, trace, determinant or zeta constructed; Hamiltonian/contact/quantum lift DEFERRED. |

The precise arrow from the
[prior-work guide](../../docs/prior_work/README.md) is

\[
\text{prime/composite divisor-exclusion symbols}
\longrightarrow\text{one witness per sequential phase}
\longrightarrow\text{direct compact-fibre conservative shear coupling}.
\]

A complete phase cycle visits every potential proper divisor, together
with the guarded zero test d=1. Its derived witness sum is zero exactly
when n is prime: a prime has no d with 2 <= d < n dividing it, and a
composite has such a divisor. The action need not store that sum, and does
not use it as a precomputed input. This is an exact preservation of the
divisor-exclusion observable, not a conjugacy to an earlier Logistic or
Hénon trajectory, nor a derivation of arithmetic from an arithmetic-free law.

The compact geometry is a new design within that source lineage. Unlike
[140](../140-cyclic-divisor-counter/paper.md) and
[141](../141-divisor-counter-henon-lift/paper.md), there is no complete
finite counter, and unlike 141 there is no noncompact hyperbolic plane.
Unlike [152](../152-coupled-witness-henon-escape/paper.md), a step does not
aggregate the whole divisor list. The packet-thickening controls
[033](../033-wheel-packet-symplectic-thickening-screen/paper.md) and
[052](../052-hyperbolic-wheel-packet-lift/paper.md) motivate checking full
multiplicity, but no theorem or orbit count is transferred from them.

## 2. Question and strongest claim

Can this actual sequential divisor action on compact symplectic fibres
produce prime-exclusive primitive packets, without selecting geometric
centres or changing its unit clock?

**Scoped answer: no.** The whole construction exists, but an actual composite
has a primitive closed orbit and a prime has a continuum of distinct
primitive closed orbits. Their exhibited prime-family times are p-1, not
log p. This is a counterexample for (1), not a theorem that all compact
conservative or all sequential arithmetic systems must fail.

## 3. Full smooth symplectic map and complete suspension

### Proposition 1 — Positive-dimensional full owner

F is a globally defined smooth symplectomorphism of the full two-dimensional
manifold M. Its unit suspension is a complete three-dimensional flow.

**Proof.** Write the toral map at a given phase as K_w composed with D,

\[
D(q,p)=(q+p,p),\qquad
K_w(Q,p)=\left(Q,p+\frac{w}{2\pi}\sin(2\pi Q)\right),
\]

with coordinates taken modulo one. The integer linear shear D respects
the integer lattice; the sine shear is well-defined because its added
function is one-periodic. Both are smooth toral diffeomorphisms. Given an
output (n,e,Q,P), let d=e^- be the preceding phase, compute w=w(n,d), and
recover

\[
p=P-\frac{w}{2\pi}\sin(2\pi Q)\pmod1,
\qquad q=Q-p\pmod1.
\tag{2}
\]

This is a smooth inverse on every component, including the n=2 component.
For the area form,

\[
D^*(dq\wedge dp)=(dq+dp)\wedge dp=dq\wedge dp,
\]
\[
K_w^*(dQ\wedge dP)
 =dQ\wedge\bigl(dp+w\cos(2\pi Q)dQ\bigr)=dQ\wedge dp.
\]

The phase permutation therefore preserves the same area form globally.
The countable disjoint union of smooth tori is Hausdorff and second countable;
each torus is an open component. It is not a compact global carrier.

For a suspension representative (x,u), 0 <= u < 1, and any real t, set
k=floor(u+t). The time-t state is represented by
(F^k x,u+t-k). The inverse (2) makes this formula defined for every real
t, and a bounded time interval has finitely many roof crossings. Endpoint
gluing yields a smooth mapping torus and complete translation flow. Its
dimension is three; no Hamiltonian or symplectic structure on that odd
dimensional carrier is inferred. QED.

Returning to the same suspension point requires height modulo one to return,
hence an integer elapsed time, followed by return of the complete base
state. Primitive flow times consequently equal least full-state map periods.

## 4. Decisive full-state periodic tests

### Proposition 2 — A primitive cycle above every integer

For every n >= 2 the points (n,d,0,0), d in D_n, form one primitive
F-cycle of least period n-1. Their suspension is one closed orbit of
primitive time n-1 and repetitions r(n-1).

**Proof.** At q=p=0 the linear shear leaves Q=0 and the sine is zero
for either value of the actual divisor witness. Thus only the phase
advances. The phase permutation has least period n-1, so no smaller
positive iterate can return the full state. The suspension observation
following Proposition 1 gives the time and repetition law. QED.

This states the existence of one exhibited cycle above each n, not uniqueness
of that fibre's periodic orbit. It does not restrict M to these points.
For n=4 the actual witness sequence is (0,1,0) at d=(1,2,3), and the
three full states return even though the successful d=2 test is executed.
Thus an actual composite primitive orbit already disproves prime exclusivity.

The example is not a marginal toral fixed family masquerading as an isolated
point. At the origin the single-step derivative is

\[
J_w=\begin{pmatrix}1&1\\w&1+w\end{pmatrix}.
\]

For the n=4 orbit starting at d=1 its actual three-step monodromy is

\[
J_0J_1J_0=\begin{pmatrix}2&5\\1&3\end{pmatrix},
\qquad \det=1,\quad \operatorname{tr}=5.
\tag{3}
\]

Its eigenvalues are (5+sqrt(21))/2 and (5-sqrt(21))/2. In particular
this exhibited composite orbit is hyperbolic and nondegenerate. No
classification of other composite orbits is needed or asserted.

### Proposition 3 — Continuous prime families and the wrong clock

For each prime integer \(\ell\), the set of points
(ell,d,q,0), with all q in R/Z and all d in D_ell, yields a circle's worth
of distinct primitive flow orbits. Every one has primitive time ell-1.

**Proof.** Every witness is zero when n=ell is prime. On that entire
integer component F acts as (d,q,p) -> (d^+,q+p,p). At p=0 the coordinate
q is constant, and the full state returns first after ell-1 phase steps.
Different q values cannot be points on the same flow orbit: neither the
base action nor continuous suspension height changes their q. Therefore
cyclic identification removes the phase representatives but not the
continuum of q labels. QED.

The monodromy of these families is J_0^(ell-1), namely
\(\left(\begin{smallmatrix}1&\ell-1\\0&1\end{smallmatrix}\right)\),
so the eigenvalue one and degeneracy are retained explicitly. Already
ell=2 gives a continuum of distinct primitive time-one flow orbits.
The proposition does not claim this is the full prime periodic set;
other momentum values have not been needed for the stopping test.

Along primes ell tending to infinity,

\[
\frac{\ell-1}{\log\ell}\longrightarrow\infty.
\]

This follows from the elementary real-variable growth x/log x and
unboundedness of primes. No fixed positive conversion of clock units makes
even these obligatory prime-family lengths asymptotic to log ell. The
roof remains one, and the conserved prime label does not change under
repetition. There is no prime-power time interpretation supplied by the
integer phase alone.

## 5. Controls, adverse evidence, and scope limits

| Control | Exact test | Consequence |
| --- | --- | --- |
| Actual composite | n=4, witnesses (0,1,0), full toral origin | Primitive period three survives a nonzero divisor kick; prime exclusivity fails. |
| Suppress all witnesses | Set w=0 in a separate comparator | The same origin cycle survives for every integer; its existence is source-blind. |
| All-one forcing | Set w=1 at every phase in a separate comparator | The same origin cycle again survives, including on primes; periodic existence at this point is not a primality selector. |
| Real source coupling | At q=1/4, p=0 a w=1 step changes momentum by 1/(2 pi), whereas w=0 does not | The arithmetic does act on the geometry; failure is not justified by falsely calling the whole map source-independent. |
| Complete multiplicity | Retain all q at momentum zero in prime fibres | A continuum of different flow orbits remains after cyclic phase identification; selecting q=0 would change the ledger. |
| Clock ownership | Keep the declared unit roof | Obligatory prime-family times are ell-1; no post-audit log roof is substituted. |
| Geometry category | Compact tori and finite fixed-n union, all n present | The full carrier is noncompact; no connected compact all-integer realization or universal compact-surface no-go is claimed. |
| PROVES_TOO_MUCH | Replace w by any binary phase predicate in (1) | Every such action shares the origin cycle; that cycle cannot certify arithmetic specificity. |

There are no numerical cutoffs, orbit-enumeration estimates or precision
dependencies. All decisive tests are exact identities on the full specified
carrier. The composite periodic set away from the exhibited orbit and the
remaining prime periodic set are deliberately left unclassified after the
early failure. No ordinary finite-multiplicity orbit product, transfer
operator or trace is asserted in the presence of the retained families.

The ARS contribution here is limited to separating the proved construction,
its exact counterexamples and the bounded conclusion. This is not a full
publication workflow, venue certification or human peer review.

## 6. Gate assessment and decision

| Obligation | Result for ASFS-20260915-TDK01 | Scope |
| --- | --- | --- |
| P0 / geometric owner | ESTABLISHED by (1)--(2) and Proposition 1 | Full two-dimensional symplectic map; complete same-roof suspension. |
| A0 source ingredient | ESTABLISHED local witness execution and exact zero-scan observable | A genuine engineered source arrow; canonical arithmetic naturalness remains OPEN. |
| A0 target / early period test | Scoped FAIL: composite cycle and mandatory nonlogarithmic prime-family lengths | Stop this proposed prime-exclusive prime-log mechanism; not a formal Route score. |
| A1 full-ledger obligation | Scoped FAIL for the requested finite prime-packet organization | Exact counterexamples and their repetitions established; entire periodic set not classified. |
| A2 | NOT PURSUED after the decisive early failure | No zeta, analytic continuation, determinant or operator claim. |
| Formal Route | UNASSIGNED | No formal target/divisor evaluation. |
| Route B | NOT INVOKED | No later-route rescue. |

**Decision: STOP this candidate's target promotion; retain its exact sequential
source and compact-fibre symplectic construction as a negative control.**
No geometry or clock was changed during the audit. A future map, carrier,
source selector or roof would require a fresh card and a new candidate ID.
No such follow-on candidate is initiated here.

## Reproducibility / evidence index

- [Frozen card](candidate-card.md), [claim ledger](claim-ledger.md),
  [package status](README.md), and [evidence record](evidence/README.md).
- The finite source inputs n=4, d=1,2,3 and matrices in (3) are displayed
  completely; their products and all infinite-family claims have exact
  proofs above. No numerical experiment or external theorem is needed.
- The evidence record identifies the separate-invocation mathematical
  review and the local structural checks; neither replaces these proofs.
