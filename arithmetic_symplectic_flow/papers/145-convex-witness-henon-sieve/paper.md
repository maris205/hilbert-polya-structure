# Convex witness forcing: a full prime-only periodic ledger in a Hénon-form map

**Paper ID:** 145-convex-witness-henon-sieve  
**Candidate ID:** ASFS-20260915-CWH01  
**Date:** 2026-09-15  
**Status:** PRIME-ONLY SYMPLECTIC PACKETS AND ORDINARY ZETA ESTABLISHED; CLOCK AND TRACE LIMITS.  
**Route:** Owner-level arithmetic, complete orbit and scalar-zeta results;
formal Route coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

We freeze a single symplectic map on a countably disconnected smooth surface
containing every integer fibre and every point of every component plane.
Each dyadic phase computes its proper-divisor witnesses and adds their
nonnegative count directly to a nonlinear Hénon-form recurrence. Summing
that recurrence around an arbitrary putative cycle proves a complete
classification: the integer fibre has a periodic orbit if and only if its
label is prime, and then has exactly one primitive orbit, of length
K_p=max(1,floor(log_2(p-1))). No counter-state quotient, centre selection
or primes-only domain is used. The unit-roof flow has the same prime-only
ledger and the ordinary product with exactly one Euler factor per prime.
Its logarithm has exact absolute-convergence abscissa log 2, by elementary
estimates. This is not the Riemann Euler product: periods are rounded binary
macrostep lengths, several primes have the same length, and all surviving
orbits are parabolic. The usual nondegenerate periodic-point trace
denominator vanishes. The paper establishes a bounded same-object positive
chain, not a natural exact prime-log clock, a transfer determinant, or a
formal Route pass.

## 1. Candidate identity and same-object ledger

The [version-1 card](candidate-card.md) fixes the object before this proof.
Write

\[
K_n=\max(1,\lfloor\log_2(n-1)\rfloor),\quad
B(n,k)=\{d:2^k\le d<2^{k+1},\ d<n\},
\]
\[
b(n,k)=\sum_{d\in B(n,k)}1_{\{d\mid n\}}.
\tag{1}
\]

Here K_n is equally definable from integer binary length. No list of primes
or logarithmic prime roof is an input. For n=2, K_n=1 and its sole block
is empty. If n>=3 and K_n=K, then 2^K<n<=2^{K+1}. Thus all the blocks
partition exactly the integers 2,...,n-1.

With k^+ cyclic successor, the full map is

\[
M=\coprod_{n\ge2,\ 1\le k\le K_n}\mathbb R^2_{n,k},\qquad
\omega|_{M_{n,k}}=dq\wedge dp,
\]
\[
\mathcal F(n,k,q,p)
=\bigl(n,k^+,p,2p-q+(p-1)^2+b(n,k)\bigr).
\tag{2}
\]

| Item | This candidate's owner | Evidence / boundary |
| --- | --- | --- |
| Base | Full M and (2), with exactly the displayed coefficients | Smooth global symplectic map proved below |
| Arithmetic | The witness tests (1), actually executed in (2) | No precomputed prime flag, selected prime domain or per-prime parameter |
| Symbolic relation | Integer/phase observations and local divisor-exclusion witnesses | A precise constraint-to-Hénon deformation, not a conjugacy to the original infinite sieve |
| Clock | tau=1 for (2) | Macrostep clock; elementary work is not constant |
| Flow | The mapping torus of this same map and roof | Complete three-dimensional suspension |
| Primitive ledger | All full-state cycles modulo cyclic phase | Complete classification, including composite fibres |
| Stability | Derivative of (2) on those same cycles | Unipotent monodromy; degeneracy retained |
| Zeta convention | Z, with a_gamma,r=1 for all repetitions | Ordinary orbit product only |
| Analytic domain | Re(s)>log 2 for the absolute logarithmic series | No continuation or target divisor claimed |
| Operator / function space | NOT SUPPLIED | No Fredholm determinant or flat trace inferred |
| Measure | Componentwise symplectic area | No finite probability or trace normalization |
| Later owner | Contact, Hamiltonian and quantum constructions DEFERRED | No Route-B statement |

There is no compactness or connectedness claim. There is no full-state Markov
coding claim: the observable phase is not substituted for the continuous
map. The base is symplectic; its odd-dimensional suspension is not thereby
a symplectic manifold or a Hamiltonian flow.

## 2. Question and claim boundary

Can the same nonlinear conservative recurrence both execute a prime-symbolic
constraint and eliminate every extraneous periodic packet without externally
selecting a centre? The answer is yes for this particular witness rule and
the full M in (2). The decisive device is a nonnegative cycle sum.

The strongest claim is an exact mathematical construction: one intrinsic
primitive closed orbit for each prime and no others, with the clock,
monodromy and ordinary product explicitly owned by the same flow. The
construction is a constraint realization, not evidence that prime
distribution uniquely selects this geometry.

Explicit nonclaims include exact periods log p, Riemann prime-power trace
weights, nondegenerate cycles, compact/connected dynamics, a canonical
arithmetic physical clock, analytic continuation, a transfer operator,
a spectral realization of zeros, and a formal Route pass.

## 3. Inputs, source lineage and provenance

The direct lineage is the prior-work prime/composite admissibility
constraint: n is admitted precisely when none of d=2,...,n-1 is a divisor.
We replace a one-way symbolic deletion record by an autonomous phase-resolved
geometric force. The phase advances by one fixed rule; every witness in its
current block acts in the continuous recurrence. This is not the claim that
the original causal sieve trajectory is symplectically conjugate to (2).

Unlike the counter lifts 141/144, (2) has no additional arithmetic witness
accumulator beyond its cyclic phase clock, and its arithmetic is not
confined to a permutation of components. Unlike a
primes-only disjoint union, M contains every n before any return test. A
conserved integer label is allowed by the all-integer scope distinction
in [140's audit](../140-cyclic-divisor-counter/evidence/carrier-scope-audit.md);
that distinction is permission to test an object, not borrowed arithmetic
or geometric credit.

The binary partition and the square force were fixed before the proof.
They are design choices. No prime data, orbit fit, Riemann-zero data or
parameter sweep was used. A full phase scan processes n-2 elementary
divisibility tests, not O(log n) sequential work.

## 4. Exact proofs

### Proposition 1 — Global geometry and complete flow

M is a Hausdorff second-countable smooth two-dimensional manifold with the
nondegenerate closed form omega. The map (2) is a global smooth
symplectomorphism.

**Proof.** A countable disjoint union of Euclidean planes has a countable
atlas and is Hausdorff. Each component has the usual symplectic form. Given
(n,k',Q,P), let k be the preceding phase. The unique inverse is

\[
(n,k',Q,P)\longmapsto
\bigl(n,k,\,2Q+(Q-1)^2+b(n,k)-P,\,Q\bigr).
\tag{3}
\]

Both maps are polynomial on each open component. Since q'=p and
p'=2p-q+(p-1)^2+b(n,k), with the discrete witness constant on a component,

\[
dq'\wedge dp'
=dp\wedge\bigl((2+2(p-1))dp-dq\bigr)
=dq\wedge dp.
\tag{4}
\]

The unit-roof quotient

\[
M_1=(M\times[0,1])/((z,1)\sim(\mathcal Fz,0))
\tag{5}
\]

defines the smooth mapping torus. Real translation in the second coordinate,
using the globally invertible map at each integer crossing, gives the
suspension flow for every real time. Unit crossings exclude finite-time
accumulation. Escape of coordinates under infinitely many iterates is not
a finite-time failure, since any finite flow time uses finitely many
polynomial iterates. QED.

### Proposition 2 — Complete prime-only periodic classification

The full periodic set of (2) is exactly

\[
\{(p,k,1,1):p\text{ prime},\ 1\le k\le K_p\}.
\tag{6}
\]

For each prime p these K_p points form exactly one orbit of least period K_p.
No composite fibre has any periodic point.

**Proof.** Consider any full-state period m. The integer n is conserved, and
the phase returns only if K_n divides m. Along the cycle put q_t=x_t and
p_t=x_{t+1}. The exact recurrence is

\[
x_{t+2}-2x_{t+1}+x_t
=(x_{t+1}-1)^2+b(n,k_t).
\tag{7}
\]

Summing over one period cancels the left side. Consequently

\[
0=\sum_{t=0}^{m-1}(x_{t+1}-1)^2+
\sum_{t=0}^{m-1}b(n,k_t).
\tag{8}
\]

Every term is nonnegative. Thus all x_t=1, and every visited b(n,k_t)=0.
Since the phase traverses every block an equal positive number of times,
this is equivalent to

\[
\sum_{k=1}^{K_n}b(n,k)
=\#\{d:2\le d<n,\ d\mid n\}=0.
\tag{9}
\]

Equation (9) is equivalent to n being prime, including n=2. Conversely,
when n is prime all forces vanish, so (n,k,1,1) advances through every phase
and closes. The phase itself rules out a smaller positive period than K_n.
This covers all real geometric states, all periods and all integer fibres;
no bounded enumeration or external selection is used. QED.

The point (1,1) is therefore derived from the full periodic equation, not
chosen as a section of a larger periodic family. For n=2 and n=3 there are
two distinct fixed points in two distinct integer components. For n=5 and
n=7 there are two distinct primitive two-cycles. Equal length never means
the same orbit.

### Proposition 3 — Flow packets, repetitions and monodromy

Each prime p gives exactly one oriented primitive closed orbit gamma_p of
(5). Its length is T_p=K_p, and its r-fold repetition has length r K_p.
There are no other closed orbits. All these orbits are parabolic.

**Proof.** A unit-roof closed flow orbit crosses its section an integer
number of times and yields a periodic point of the base. Conversely a
least-period base orbit gives one primitive flow orbit after quotienting
by its cyclic section points. Proposition 2 is complete, so neither extra
packets nor missing fibres can enter this correspondence. Reversing
orientation is not a second orbit of the fixed oriented flow.

Along (6), the derivative on the full two-dimensional transverse section is

\[
A=\begin{pmatrix}0&1\\-1&2\end{pmatrix}
=I+N,\qquad
N=\begin{pmatrix}-1&1\\-1&1\end{pmatrix},\qquad N^2=0.
\]

The primitive Poincare monodromy and its repetitions are therefore

\[
P_p=A^{K_p}=I+K_pN,\qquad
P_p^r=I+rK_pN,\qquad
\det(I-P_p^r)=0.
\tag{10}
\]

These are isolated periodic points in each relevant component despite their
degenerate linearization; Proposition 2, not the linearization, establishes
isolation and uniqueness. QED.

### Proposition 4 — Exact ordinary zeta and convergence boundary

The frozen ordinary unweighted product of the full suspension ledger is

\[
Z(s)=\prod_{p\ \mathrm{prime}}(1-e^{-sK_p})^{-1},
\quad
\log Z(s)=\sum_p\sum_{r\ge1}\frac{e^{-srK_p}}r.
\tag{11}
\]

The logarithmic series converges absolutely and locally uniformly on
Re(s)>log 2, and Z is holomorphic and nonzero there. The abscissa of
absolute convergence of this series is exactly log 2. No continuation
claim is made.

**Proof.** The product is derived only after Proposition 2, with weight one
and the repetition convention of Proposition 3. Write sigma=Re(s)>log 2.
For n>=3 the number of integers with K_n=j is 2^j. Counting all of them
rather than only primes gives

\[
\sum_p e^{-\sigma K_p}
\le e^{-\sigma}+\sum_{j\ge1}2^j e^{-\sigma j}<\infty.
\tag{12}
\]

The separate first term accounts for n=2. Since K_p>=1, the absolute
repetition sum is at most (12) divided by 1-e^{-sigma}. This is locally
uniform on the stated half-plane. Its exponential proves the claim for Z.

For the lower bound, first prove the elementary divergence of the sum of
prime reciprocals. If that sum were finite, then

\[
\prod_{p\le N}(1-1/p)^{-1}
\le\exp\left(2\sum_{p\le N}1/p\right)
\]

would be uniformly bounded, since -log(1-x)<=2x for 0<=x<=1/2.
Expanding this finite product as nonnegative geometric series includes
1/n for every n<=N by unique factorization, so it is at least
H_N=sum_{n=1}^N 1/n, which is unbounded. This contradiction proves
sum_p 1/p=infinity without a prime-number theorem.

For p>2, 2^{K_p}<p, so at sigma=log 2,

\[
e^{-\sigma K_p}=2^{-K_p}>1/p.
\tag{13}
\]

The first repetition already fails absolute summability. For smaller
sigma these nonnegative absolute values only grow. Together with (12)
this proves the exact absolute-convergence abscissa. At positive real
s<=log 2 the logarithm and positive finite subproducts diverge; this
does not prohibit an independently proved analytic continuation. QED.

## 5. Results and the exact remaining timing issue

For p>2 the prime period satisfies

\[
0<\log_2p-K_p<1,\qquad
K_p=\frac{\log p}{\log2}+O(1),\qquad
\frac{K_p}{\log p}\longrightarrow\frac1{\log2}.
\tag{14}
\]

The two small fixed packets have already been retained. The expression
(log 2)K_p=log p+O(1) is a numerical comparison, not a change of roof.
Even a single constant rescaling could not make the 5 and 7 packets have
their two different exact logarithmic lengths, because both have K=2.
There is no hidden equality between (11) and the Riemann Euler product.

The clock is genuinely the time of (2) and (5). Its binary scale was
chosen by batching witness tests. Smooth geometric realization makes those
macrosteps part of a valid flow; it does not prove that their duration is
independently forced by arithmetic or that unbounded batches are equal-cost
elementary computations. This is a scope limitation, not an assertion
that every chosen time convention is forbidden.

## 6. Controls and adverse findings

The comparators were specified in the initial card and its documented
pre-drafting clarification before their audits. They are different actions
used to test claims about (2), never substitute owners.

| Control | Exact result by the same cycle-sum argument | What it tests |
| --- | --- | --- |
| Delete the witness force: b=0 | Exactly one K_n packet for every integer n | The original prime-only ledger depends on arithmetic, not the square residual alone |
| Replace b by the block cardinality | Only n=2 remains periodic; every n>=3 has a nonempty block | The n=2 empty-block boundary is retained; generic positive force kills the other packets |
| Replace d dividing n by d dividing n+1 on the same blocks | Exactly the fibres with n+1 prime are periodic | Relabelling the tested integer changes which fibres return; 3 is rejected and 4 accepted |
| Full geometric state space | Equation (8) excludes every noncentral periodic state and all composite fibres | No post hoc centre restriction or deleted continuum |
| Elementary-work clock | Exactly n-2 tests over K_n macrosteps | No claimed logarithmic sequential primality algorithm |
| Generic nonnegative witnesses | For any such force, a cycle forces all its values and all square residuals to vanish | A reusable constraint construction; prime-specific uniqueness or naturalness is not proved |

For the third control, every proper divisor of n+1, when one exists and
n>=3, lies between 2 and n-1 and therefore appears in a block. At n=2 the
empty block agrees with primality of n+1=3. The stated profile follows
without an externally supplied prime list.

The PROVES_TOO_MUCH finding is important but scoped: this mechanism can
realize other finite nonnegative constraint systems. It does not make the
particular derived prime-only ledger false. It limits the claim that the
construction explains why Riemann's target should single out this geometry.

Equation (10) is an immediate analytic warning. Any proposed trace formula
that requires division by det(I-P_p^r) is undefined here. We neither apply
that expression nor claim that every possible degenerate-orbit trace
framework is impossible. A scalar unweighted product does not provide
an operator or resolve this obstruction.

## 7. Gate assessment

| Gate | Evidence for this exact candidate | Scoped result | Outstanding boundary |
| --- | --- | --- | --- |
| P0 | Explicit global symplectomorphism, full M, unit roof and complete flow | ESTABLISHED | Disconnected, noncompact; no later Hamiltonian owner |
| A0 arithmetic mechanism | Local divisor witnesses in the geometric update; complete prime-only returns; three arithmetic adversarial controls | ESTABLISHED for operational endogenous prime selection | Canonical Riemann relevance and natural exact prime-log timing OPEN; no unconditional full target-A0 PASS |
| A0 clock component | Exact K_p and (14) for the same flow | Logarithmic-order macroclock ESTABLISHED | Exact log p FAILS; binary batching origin disclosed |
| Owner A1 | All integer fibres and geometric points classified; one prime packet each; full repetitions and monodromy | ESTABLISHED | Parabolic degeneracy is part of the result, not omitted |
| Owner A2 scalar result | Full ordinary Z with exact absolute-convergence abscissa log 2 | ESTABLISHED in the stated half-plane | Operator, trace, continuation and target divisor NOT SUPPLIED / OPEN |
| Formal Route A | No target/divisor protocol evaluated | UNASSIGNED | Owner results are not a formal tuple |
| Route B | No formal readiness or separate evaluation | NOT INVOKED | No B coordinate |

This is now an actual same-object arithmetic / orbit / ordinary-zeta
construction. The table deliberately separates that positive operational
chain from the stronger natural-target and operator obligations.

## 8. Conclusion and portfolio decision

**Advance** through the bounded complete A1 and scalar A2 work recorded here;
those tasks are now complete. **Retain** this candidate as a prime-only
symplectic positive control. **Fork** any attempt to obtain a different
clock or nondegenerate geometric trace: changing the roof or force would be
a new object and require a fresh card. Do not repeatedly tune (2) to pretend
it already has exact prime lengths or a trace formula.

The decisive progress is the elimination of both composite packets and
extra prime multiplicity by an intrinsic periodic equation. The decisive
next obstruction is no longer “can this map have arithmetic closed
orbits?” but the rounded macroclock and parabolic trace boundary.

## Reproducibility and evidence index

All global claims above are exact proofs, not numerical extrapolations.
No computation, orbit cutoff, zero comparison, training fit or external
literature theorem is needed for these derivations. See the
[candidate card](candidate-card.md), [claim ledger](claim-ledger.md),
[evidence record](evidence/README.md), [summary](README.md), and
[independent model review](evidence/review.md).
