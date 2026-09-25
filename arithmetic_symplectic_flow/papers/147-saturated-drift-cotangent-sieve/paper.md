# Saturated drift and a full prime-only hyperbolic cotangent ledger

**Paper ID:** 147-saturated-drift-cotangent-sieve  
**Candidate ID:** ASFS-20260915-SDC01  
**Date:** 2026-09-15  
**Status:** PRIME-ONLY HYPERBOLIC PACKETS AND ORDINARY ZETA ESTABLISHED; TARGET CLOCK AND OPERATOR OPEN.

Formal Route coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

We construct a single symplectic map on the countable disjoint union of
all integer/phase planes. A cyclic binary scan injects local proper-divisor
witnesses into a one-dimensional saturated drift; its canonical cotangent
lift supplies the full two-dimensional geometry. A hypothetical composite
cycle would accumulate a strictly positive configuration displacement, so
no composite fibre contains any periodic state. In prime fibres monotone
sign drift and the full momentum equation leave exactly one primitive
orbit per prime. Its period is the binary phase count K_p, and its
monodromy is diag((3/2)^K_p,(2/3)^K_p); every repetition is nondegenerate.
The same unit-roof suspension has the complete prime-only orbit ledger and
an ordinary zeta whose logarithmic series has exact absolute-convergence
abscissa log 2. All statements concern the full real carrier, not selected
centres or finite samples. The force gain and binary batching are explicit
engineering choices. The present periods are not exact log p. Canonical
arithmetic geometry, transfer operators and target spectral conclusions
remain open; an exact target-clock construction would require a new candidate.

## 1. Frozen identity and source relation

The [version-1 card](candidate-card.md) was frozen before this result.
For every integer n>=2 put

\[
K_n=\max(1,\lfloor\log_2(n-1)\rfloor),\quad
B(n,k)=\{d:2^k\le d<2^{k+1},\ d<n\},
\]
\[
b(n,k)=\sum_{d\in B(n,k)}1_{\{d\mid n\}},
\qquad 1\le k\le K_n.
\tag{1}
\]

Binary integer length defines K_n without numerical logarithm evaluation.
The single block for n=2 is empty. For n>=3, the blocks partition precisely
2,...,n-1; hence

\[
a(n):=\sum_{k=1}^{K_n}b(n,k)
=\#\{d:2\le d<n,\ d\mid n\},
\quad a(n)=0\ \Longleftrightarrow\ n\text{ is prime}.
\tag{2}
\]

The carrier and its fixed action are

\[
M=\coprod_{n\ge2,\ 1\le k\le K_n}\mathbb R^2_{n,k},
\qquad \omega|_{\mathbb R^2_{n,k}}=dq\wedge dp,
\]
\[
f_{n,k}(q)=q+\tfrac12\tanh q+K_n b(n,k),
\]
\[
F(n,k,q,p)=
\left(n,k^+,f_{n,k}(q),\frac{p}{f'_{n,k}(q)}\right),
\qquad \tau=1.
\tag{3}
\]

Here k^+ is the cyclic phase successor. No component is removed according
to primality. The integer label is conserved, but its local divisibility
tests act on configuration trajectories in (3), rather than decorating an
unrelated geometric orbit.

The precise [prior-work lineage](../../docs/prior_work/README.md) is
prime/composite divisor exclusion -> local symbolic admissibility witnesses
-> autonomous cyclic phase deformation -> a one-dimensional source-dependent
map and its positive-dimensional conservative cotangent lift. This is a
replacement of the one-way deletion realization of the constraint, not a
conjugacy to the original causal sieve or a claim that (3) has Hénon form.
The retained arithmetic predicate and the geometric lifting operation are
explicit. The different Hénon-form map in
[145](../145-convex-witness-henon-sieve/paper.md) is a source/clock comparator
only; its periodic or analytic conclusions are not imported.

## 2. Same-object ledger and claim boundary

| Item | Owner in ASFS-20260915-SDC01 | Scope |
| --- | --- | --- |
| Geometry | Full M, omega and (3) | Smooth disconnected noncompact surface |
| Arithmetic | Every witness in (1) enters the configuration update | All n permitted; no prime table or external prime selector |
| Parameters | Exactly tanh, coefficient 1/2, gain K_n and binary blocks | Fixed all-integer rule, no zero fitting or parameter scan |
| Coding | Intrinsic integer, phase and witness observations | No full-state Markov coding claimed |
| Measure | Componentwise symplectic area | No finite invariant probability or trace normalization supplied |
| Clock | Unit macrostep roof on (3) | One unbounded-size block is one map step |
| Flow | Mapping torus of exactly this F and roof | Complete oriented three-dimensional suspension |
| Periodic data | All full-state periodic points modulo cyclic phase | Composite and noncentral momentum states included before proof |
| Stability | Derivative of this same F | Hyperbolic monodromy, all repetitions nondegenerate |
| Analytic object | Ordinary unweighted Z; all repetition weights equal 1 | Absolute logarithmic convergence on Re(s)>log 2 |
| Operator, space and trace | OPEN / NOT SUPPLIED | No trace or Fredholm identity inferred |
| Later owner | Hamiltonian, contact and quantum constructions DEFERRED | No Route-B invocation |

The strongest claim is a complete mathematical construction of prime-only
hyperbolic packets and their ordinary product. It is not a proof that
prime distribution singles out this geometry. Countable disconnectedness
and noncompactness are part of the actual object, not suppressed caveats.
The odd-dimensional suspension is not automatically symplectic or
Hamiltonian.

## 3. Exact geometry and complete flow

### Proposition 1 — Global symplectic diffeomorphism

The full map (3) is a smooth symplectomorphism of M.

**Proof.** M is Hausdorff and second-countable because its plane components
form a countable family, each with a countable atlas. On every component,

\[
f'_{n,k}(q)=1+\tfrac12\operatorname{sech}^2q\in(1,3/2].
\tag{4}
\]

The bounded tanh term and fixed componentwise constant K_n b(n,k) imply
f(q)->+infinity as q->+infinity and f(q)->-infinity as q->-infinity.
Thus f is a strictly increasing onto smooth diffeomorphism of the line.
Given (n,k',Q,P), take k to be the preceding phase and define
q=f_{n,k}^{-1}(Q), p=P f'_{n,k}(q). This is the global smooth inverse
of F. There is no assumed explicit elementary formula for f^{-1}.

With Q=f(q), P=p/f'(q), the canonical one-form satisfies
P dQ=p dq. Consequently dQ wedge dP=dq wedge dp. This proves preservation
of the stated symplectic form on every component, and hence globally. QED.

### Proposition 2 — Complete owned suspension

The mapping torus

\[
M_1=(M\times[0,1])/((z,1)\sim(Fz,0))
\tag{5}
\]

is a smooth three-dimensional manifold and carries the suspension flow
for all real times.

**Proof.** The gluing uses the global diffeomorphism from Proposition 1.
Translation in the interval coordinate, with F or F^{-1} at crossings,
defines the flow. Every finite positive or negative time crosses only
finitely many unit roofs, so only finitely many globally defined iterates
are used. There is no finite-time accumulation of returns. Unbounded
coordinates after arbitrarily many iterates do not negate completeness
at finite suspension time. QED.

## 4. Full periodic classification

### Proposition 3 — Composite escape excludes every period

No composite integer fibre contains any periodic point of F.

**Proof.** Let a full state have period m>0. Since the phase is part of
the state, m=rK_n for some positive integer r. Write q_t for the actual
configuration coordinates, retaining all phase updates. Summing (3),

\[
0=q_m-q_0
=\frac12\sum_{t=0}^{m-1}\tanh q_t
+K_n\sum_{t=0}^{m-1}b(n,k_t)
=\frac12\sum_{t=0}^{m-1}\tanh q_t+K_n r a(n).
\tag{6}
\]

The strict bound tanh q_t>-1 gives the right side strictly greater than
-m/2+K_n r a(n). For composite n, a(n)>=1, so this is at least m/2>0.
This contradicts (6). The proof assumes neither bounded coordinates nor
a chosen section of the momentum fibre, and applies to every proposed
period, every phase origin and every real initial position and momentum.
QED.

### Proposition 4 — Exactly one primitive orbit in each prime fibre

The complete periodic set is

\[
\operatorname{Per}(F)=
\{(p,k,0,0):p\text{ prime},\ 1\le k\le K_p\}.
\tag{7}
\]

Each prime p contributes exactly one primitive orbit of least period K_p.

**Proof.** For prime p, every b(p,k)=0 and the position update is the
same map f_0(q)=q+(1/2)tanh q at every phase. If q>0, all subsequent
positions are positive and strictly increasing. If q<0, they remain
negative and strictly decrease. Neither trajectory returns. Thus a
periodic state must have q=0 at every step.

At q=0, (4) is 3/2, so the complete momentum equation is
p_t=(2/3)^t p_0. A positive return time therefore forces p_0=0.
Conversely, the states (p,k,0,0) follow the cyclic phase exactly, so they
form one K_p-cycle. The phase rules out every shorter full-state period.
Proposition 3 excludes all composite fibres. This proves (7) on the full
carrier without selecting centres from a larger periodic family. QED.

For example, primes 2 and 3 give separate fixed points in different
integer fibres; primes 5 and 7 give separate primitive two-cycles.
Equal length never identifies distinct orbits.

### Proposition 5 — Hyperbolicity, flow packets and repetitions

The flow (5) has exactly one oriented primitive closed orbit gamma_p for
each prime p, with T_p=K_p. Its r-fold repetition has length rK_p.
Its primitive section monodromy is

\[
P_p=\operatorname{diag}((3/2)^{K_p},(2/3)^{K_p}),
\]
\[
\det(I-P_p^r)=2-(3/2)^{rK_p}-(2/3)^{rK_p}<0.
\tag{8}
\]

**Proof.** At a surviving state, the derivative of (3) is diagonal:
the momentum-position derivative -p f''(q)/(f'(q))^2 vanishes because
p=0. Its diagonal is (3/2,2/3). Multiplying along the actual K_p-cycle
and then along its repetitions proves (8); the strict inequality follows
from x+x^{-1}>2 for x>1.

A closed unit-roof flow orbit crosses the section a positive integer
number of times and yields a periodic point of F. Conversely a primitive
base orbit yields exactly one oriented closed flow orbit, after quotienting
its K_p section points by cyclic phase. Reversal is not a second orbit of
the fixed oriented flow. Proposition 4 is complete, so this correspondence
adds no hidden packets. The roof sum gives K_p and then rK_p. QED.

For a fixed iterate m, any contributing fibre satisfies K_n|m, hence
K_n<=m and n<=2^{m+1}, including n=2. Thus the complete fixed-point set
of F^m is finite. This is a useful local finiteness fact, not by itself
the existence of an operator trace.

## 5. Ordinary zeta and its exact absolute-convergence boundary

### Proposition 6 — Same-object ordinary product

With the frozen ordinary repetition weights all equal to 1,

\[
Z(s)=\prod_{p\ \mathrm{prime}}(1-e^{-sK_p})^{-1},
\qquad
\log Z(s)=\sum_p\sum_{r\ge1}\frac{e^{-srK_p}}r.
\tag{9}
\]

The logarithmic series converges absolutely and normally on Re(s)>log 2,
defines a holomorphic logarithm there, and has exact absolute-convergence
abscissa log 2. In particular Z is holomorphic and nonzero on that half-plane.

**Proof.** Proposition 5 supplies precisely the primitives, multiplicities
and repetitions in (9), with the same roof. For sigma>log 2 and n>=3,
K_n>log_2(n-1)-1, giving

\[
e^{-\sigma K_n}<e^\sigma(n-1)^{-\sigma/\log 2}.
\tag{10}
\]

The right side is summable over all integers n>=3. Also K_n>=1, so

\[
\sum_p\sum_{r\ge1}\frac{e^{-\sigma rK_p}}r
\le \frac{1}{1-e^{-\sigma}}\sum_p e^{-\sigma K_p}<\infty.
\tag{11}
\]

On a compact subset of the stated half-plane, use its minimum real part
in (10)--(11) to obtain normal convergence. Exponentiation then defines
the nonzero holomorphic product (9).

For the lower bound, K_p<=log_2 p, so 2^{-K_p}>=1/p.
The elementary divergence of sum_p 1/p can be seen directly: if it were
finite, the finite products product_{p<=N}(1-1/p)^{-1} would remain bounded,
since -log(1-1/p)<=2/p. But expanding each finite geometric product,
unique prime factorization shows it includes every 1/n for 1<=n<=N.
It therefore dominates the unbounded harmonic partial sums, a contradiction.
Thus the r=1 terms in (9) already diverge absolutely when sigma=log 2.
They dominate these same terms for every sigma<log 2, proving the exact
abscissa. No prime number theorem, orbit-count fit or numerical zero data
is needed. QED.

An absolute-convergence boundary is not a natural-boundary or analytic-
continuation theorem. Hyperbolicity and (8) do not turn (9) into a flat
trace or Fredholm determinant. No transfer operator or function space has
been frozen in this package.

## 6. Controls and adverse findings

| Control or objection | Exact outcome | Scope |
| --- | --- | --- |
| Set every b(n,k)=0 | Every integer fibre has one primitive K_n-cycle with the same hyperbolic matrix | Geometry alone does not select primes; the arithmetic force is active |
| Replace b(n,k) by block cardinality | For n>=3 the scan sum is n-2>=1, so all such fibres have no periodic point; n=2 survives its empty block | Retains the small-integer edge case instead of silently declaring complete emptiness |
| Replace each test d|n by d|(n+1) | The survivors are n=2 and the n>=3 with n+1 prime | Arithmetic relabelling changes the actual orbit ledger at fixed carrier and geometry |
| Retain every noncentral momentum | Even when q=0, p!=(0) cannot return because it is multiplied by (2/3)^m | The finite ledger is intrinsic, not zero-section post-selection |
| Passive hyperbolic-factor objection | Witnesses move q itself; cotangent momentum is the canonical companion of that same q-map | No stability factor is borrowed from another candidate |
| Macrostep versus elementary work | K_n map steps execute n-2 individual divisor tests over a complete scan | No O(log n) sequential primality algorithm is claimed |
| Changed roof or gain | Would define a different candidate and need a new card | The present ordinary product cannot be transferred silently |

For the shifted-test control, the blocks still cover 2,...,n-1.
If n>=3 and n+1 is composite, it has a divisor between 2 and
sqrt(n+1)<=n-1; thus some shifted witness is positive. If n+1 is prime,
all shifted witnesses vanish. The exceptional n=2 retains its empty block.
For example n=3 is rejected and n=4 is accepted, unlike the original rule.

The gain K_n is an engineered domination bound. Over rK_n steps, the
largest possible negative drift magnitude is strictly less than rK_n/2,
whereas one proper-divisor witness in each scan contributes rK_n.
This all-integer formula was frozen before testing. It is neither a
per-prime choice nor a prime-length roof, but it is also not a derivation
of a uniquely distinguished physical force from arithmetic.

The mechanism has an explicit PROVES_TOO_MUCH limitation: replacing the
divisor tests by any nonnegative integer local constraints on finite cyclic
phase lists gives the same rejection proof whenever at least one constraint
is nonzero. Hence the geometry is a general constraint realization.
Its prime specificity resides in the actually executed divisor-exclusion
rule (1), not in an unsupported uniqueness assertion about tanh or cotangent
geometry. This limitation does not make the proved full-state rule an
external prime selector; it prevents a stronger claim of canonical
Riemann arithmetic naturalness.

The clock is likewise limited:
K_p=log_2 p+O(1), not log p. For example K_5=K_7=2, so no single constant
rescaling can turn both lengths into log 5 and log 7. The binary partition
is a fixed all-integer processing rule, not a forbidden hand-inserted
T_p=log p; it still leaves the target's exact clock unsupplied.

## 7. Gate assessment

| Gate | Evidence for ASFS-20260915-SDC01 | Status | Limitation |
| --- | --- | --- | --- |
| P0 | Equations (1)--(5), full inverse, measure/coding/clock ledger | ESTABLISHED | Noncompact disconnected carrier is retained |
| Owner A0 arithmetic | Local witnesses cause composite escape and exact prime selection, with three explicit arithmetic controls | ESTABLISHED bounded endogenous mechanism | Generic-constraint realization and gain engineering qualify naturalness |
| Owner A0 clock | The owned phase count derives K_p=log_2 p+O(1) | LOGARITHMIC-ORDER MACROCLOCK ESTABLISHED | Exact prime-log clock and canonical target relevance OPEN |
| Owner A1 | Complete periodic set, primitive quotient, multiplicity, repetitions and (8) | ESTABLISHED | No compactness, mixing or global hyperbolic-set claim |
| Owner A2 scalar object | The same ordinary product (9), exact absolute abscissa log 2 | ESTABLISHED ORDINARY ZETA ONLY | Operator, function space, trace, Fredholm identity and continuation OPEN |
| Formal Route A | No target/divisor evaluation performed | UNASSIGNED | Owner labels are not a formal Route pass |
| Route B | No invocation or coordinate | NOT INVOKED | No Hilbert/quantum conclusion |

## 8. Decision and evidence

Portfolio decision: **advance** to a separately specified analytic-owner
audit if authorized, because this object retains prime-only packets while
removing the parabolic repetition denominators of its source comparator.
This paper completes the bounded source, full-ledger and ordinary-zeta
obligations; it does not silently extend its analytic proposal.

Any change of the map, roof, gain, carrier or central analytic object
requires a new versioned owner card under the repository's freeze rule.
In particular, an operator claim must name its domain, action, weights,
normalization and relation to this complete ledger before it is tested.
No formal Route coordinate was evaluated.

All mathematical results here are direct analytic proofs. No finite
numerical orbit sample is used to support the infinite claims.
The [evidence index](evidence/README.md), [claim ledger](claim-ledger.md)
and [frozen card](candidate-card.md) distinguish proof, review and validation.
This Markdown research record makes no submission, venue-fit or human
peer-review claim.
