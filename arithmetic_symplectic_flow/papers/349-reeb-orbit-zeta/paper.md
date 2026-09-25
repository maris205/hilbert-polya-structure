# Same-flow orbit zeta and the scalar transverse-weight obstruction

**Paper ID:** `349-reeb-orbit-zeta`  
**Audit ID:** `ANG-AUDIT-20260921-RCZ01`  
**Unchanged flow ID:** `ANG-20260921-RCF01`  
**Date/type:** 2026-09-21; exact analytic derivation and scoped negative result.  
**Status:** `ORBIT ZETA ESTABLISHED; SCALAR IDENTIFICATION STOP; NATURALNESS OPEN`.  
**Route:** owner-level T3 only; classical A0/A1/A2 NOT APPLICABLE;
formal Route A UNASSIGNED; Route B NOT INVOKED.

## Abstract

For the full RCF01 contact quotient and its unchanged Reeb flow, the ordinary
physical orbit zeta equals the classical Riemann zeta in its half-plane of
absolute convergence. This follows from the already proved complete physical
primitive ledger, not from an inserted trace coefficient. The actual scalar
pullback has a different positive-time flat trace: each repetition acquires
the inverse transverse fixed-point Jacobian. We construct that distribution
directly from the joint time-space kernel, including its noncompact owner,
and derive its distinct flat-determinant function and meromorphic continuation.
The full-volume L2 pullbacks are unitary but not trace class. Three complete
controls distinguish arithmetic selection, isolated multiplicity and geometric
holonomy. The ordinary zeta identity does not yield the proposed scalar
trace/Fredholm identification, strong arithmetic naturalness or a Route pass.

## 1. Candidate identity and same-object ledger

The new identity is an ANALYTIC AUDIT of RCF01, not a changed dynamical
candidate. The original192-line [card](candidate-card.md) froze all objects
before these derivations. The unchanged scientific input is
[348's full card](../348-reeb-contact-refinement/candidate-card.md) and
[348's proof](../348-reeb-contact-refinement/paper.md), specifically G1–G4,
P1, C1–C3 and the transverse-return supplement. The input locks and actual
access are recorded in [source provenance](evidence/source-record.md).

| Item | Exact owner used here | Standing |
| --- | --- | --- |
| Carrier | Full RCF01 retained-lag groupoid quotient Q | Same frozen source, not a selected core |
| Classical symplectic map/roof | No such base-map suspension supplied | NOT APPLICABLE |
| Arithmetic | All integer words, complete cover-atom factorization and gcd reduction | Unchanged; no prime table input |
| Geometry | Contact form beta and its full normalized Reeb action Phi | Unchanged |
| Measure | Descended contact volume nu, not counting-atlas pushforward | Infinite invariant volume |
| Primitive convention | All actual physical Phi-orbits; one least-log p circle per atom | Same-object input theorem |
| Repetition | k traversals of that same physical circle | No composite relabelling |
| Analytic objects | Ordinary Z_orb; separately scalar U_t, Theta_0 and D_0 | Frozen here, proved below |
| Controls | Each of348's three full modified owners | No borrowed MAIN return matrix |

The source is the coproduct over ALL finite ordered positive-integer words,
including empty, units and repetitions. The map replaces a singleton by its
complete sorted atom-factor word and coalesces the first pair of a longer
word by gcd; empty is terminal. On a nonempty word with first entry a its
geometric transport is(q,xi,z)->(q/a,a xi,z). The groupoid retains actual
common-future triples with lag, all inverse branches and their full domains.
In coordinates u=log q and v=q xi this transport is u->u-log a, fixing v,z.
These are precisely348's inputs, not a substitute symbolic model.

By its proved full quotient and packet theorem,

```text
Q = Q_terminal disjoint-union coproduct_(p atom) Q_p,
Q_terminal = R^3,  Q_p = (R/(log p)Z) x R^2,
beta = (1+vz)du+(v dz-z dv)/2,
nu = beta wedge d beta = du dv dz,
Phi^t(u,v,z) = (u+t,exp(t)v,exp(-t)z).
```

Cover atoms are precisely prime integers, as348 G1 proves from divisibility.
Every source word has its actual first-hit translation into one of these
components; none of its points or incoming histories is dropped. On Q_p,
the equality Phi^t x=x means t in(log p)Z and
(exp(t)-1)v=(exp(-t)-1)z=0. Thus the full primitive set consists of ONE
circle v=z=0 per p, of least period L_p=log p. Every other point, including
all terminal points, is nonperiodic. These equations also reconfirm the
same input ledger without using an analytic object to infer periodicity.

Lineage is proper-divisor admissibility -> factor-word/gcd dynamics -> full
contact geometric lift -> this SAME physical ledger's analytic layer.
This is not a proved conjugacy of previous Logistic/Henon systems, nor
canonical arithmetic geometry. All source/form/flow engineering remains
visible; the naturalness gap is not erased by an analytic identity.

## 2. Question and claim boundary

Does the ordinary physical orbit zeta have a rigorous analytic meaning, and
does the frozen classical scalar pullback own its counting distribution or
reciprocal determinant? The answer splits:

- YES for the ordinary zeta and its identity on Re s>1.
- YES for a positive-time scalar flat trace and a DIFFERENT determinant
  function, initially on Re s>0.
- NO for equality of those two traces/determinants, or ordinary trace class
  of this full-L2 pullback.

All statements are exact conditional on the explicitly checked unchanged
348 input theorem. No finite experiment is offered as proof. No nuclear or
anisotropic function space, differential-form bundle, compensating amplitude,
gamma completion, zero matching or quantum construction is supplied. No
universal impossibility claim about other operators follows from this one.

## 3. Definitions, inputs, and provenance

For the entire primitive set P, freeze the ordinary convention

```text
Z_orb(s) = exp(sum_(gamma in P) sum_(k>=1) exp(-s k ell_gamma)/k),
D_orb(s) = 1/Z_orb(s),
Theta_orb = sum_(gamma in P) sum_(k>=1) ell_gamma delta_(k ell_gamma).
```

Primitive weights are1 and the logarithmic repetition weight is1/k.
Theta_orb is a length-counting measure, not yet an operator trace.
Separately, with the full contact volume and H=L2(Q,nu), freeze

```text
U_t f = f composed with Phi^(-t), initially f in C_c^infinity(Q),
K_t(x,y) = delta_(Phi^(-t)(x))(y), relative to nu.
```

The proposed Theta_0 is the spatial diagonal restriction of this JOINT
(t,x,y) kernel followed by integration over x, tested on compact subsets
of t>0. It is not a fixed-time trace assigned at a singular return time.
Only after that construction is legitimate do we set

```text
D_0(s) = exp(- integral_(0,infinity) exp(-s t) Theta_0(dt)/t).
```

Time zero and any zero-time regularization are outside this definition.
All functions normalize to1 as Re s tends to positive infinity in their
initial domains. A reciprocal orbit zeta or a flat-determinant FUNCTION is
not by terminology an ordinary Fredholm determinant.

The only external mathematical input is the classical continuation of the
named zeta function, verified in [NIST DLMF25.2](https://dlmf.nist.gov/25.2):
the Dirichlet series on Re s>1 continues meromorphically to C, with its only
pole simple at1 and residue1. Our dynamical identity and scalar formulas
are proved below, not supplied by that reference. The unnecessary exposure
to a zeros-overview page is disclosed in the source record; it is not used.

## 4. Method and proofs

### J1a. Ordinary physical orbit zeta

The SAME complete ledger gives, with sigma=Re s>1,

```text
log Z_orb(s) = sum_p sum_(k>=1) p^(-ks)/k.
```

Absolute convergence, uniformly on sigma>=1+epsilon, follows from

```text
sum_p sum_k p^(-k sigma)/k
 <= sum_p p^(-sigma)/(1-p^(-sigma))
 <= (1-2^(-sigma))^(-1) sum_(n>=2) n^(-sigma) < infinity.
```

Consequently exponentiation and grouping by p give
Z_orb(s)=product_p(1-p^(-s))^(-1). Finite products expand into the sum of
n^(-s) over integers whose prime factors lie in that finite prime set,
with coefficient EXACTLY1 by unique factorization. Every positive integer
eventually belongs to such a set. Domination by sum n^(-sigma) passes to
the limit and proves

```text
Z_orb(s) = sum_(n>=1) n^(-s) = zeta(s),  Re s>1.
```

This is a derived counting identity, not an assigned Euler product. The
verified classical continuation then gives the unique meromorphic
continuation of Z_orb. Its reciprocal is D_orb=1/zeta, meromorphically;
this step proves no Fredholm representation or spectral interpretation.

The half-plane is sharp for ABSOLUTE convergence of the defining log sum.
For completeness, sum_p1/p diverges: otherwise
sum_p[-log(1-1/p)] would converge, since its k>=2 part is bounded by a
convergent integer-square sum. The finite Euler products at s=1 would be
uniformly bounded. But the product over primes<=N includes every integer
n<=N in its positive geometric expansion, so dominates sum_(n<=N)1/n,
a contradiction. For sigma<=1 the k=1 absolute terms are at least1/p.
This argument uses no prime asymptotic or zero information.

### J1b. Length distribution, differentiation and analytic truncations

On a compact time interval(0,T], only p^k<=exp(T) can contribute. There
are finitely many such pairs and no positive time below log2. Thus

```text
Theta_orb = sum_p sum_(k>=1) (log p) delta_(k log p)
```

is a locally finite positive measure on(0,infinity). For sigma>1 its
Laplace transform converges absolutely: it is bounded using
sum_(n>=2)(log n)n^(-sigma)<infinity and the same geometric denominator.
These estimates on any smaller closed half-plane also justify local
uniform termwise differentiation. Hence

```text
-Z_orb'(s)/Z_orb(s) = integral exp(-s t) Theta_orb(dt)
                   = sum_p sum_k (log p) p^(-ks),  Re s>1.
```

The prime-power coefficients arise from the ordinary derivative of the
derived orbit sum; they were not fed back into the dynamics or operator.
For an integer cutoff P>=2 the omitted primitive part of log Z_orb obeys

```text
absolute tail <= P^(1-sigma)/((sigma-1)(1-2^(-sigma))).
```

Indeed enlarge primes>P to all integers>P and use the integral bound for
their decreasing power sum. These are analytic approximants with an honest
domain and tail, not a finite completeness census. No numerical cutoff
was used to establish any theorem here.

### J2a. Actual joint kernel diagonal

On a circular component of length L=log p, the inverse flow is
([u-t],exp(-t)v,exp(t)z). In local product coordinates its kernel has
three Dirac factors, so the candidate diagonal expression is

```text
delta_(L Z)(t) delta((1-exp(-t))v) delta((1-exp(t))z).
```

This expression requires justification, not just formal multiplication.
Near a possible return t=kL>0, use a lift of the circular coordinate.
The defining constraint for the restriction is, up to immaterial signs,

```text
F(t,u,v,z) = (t-kL, (1-exp(-t))v, (1-exp(t))z).
```

At its zero set the derivative in(t,v,z) is diagonal with nonzero entries
1,1-exp(-kL),1-exp(kL). Thus F is a submersion there. Equivalently the
joint kernel's conormal distribution has a valid diagonal pullback.
The elementary Dirac change-of-variables rule then gives precisely

```text
delta(t-kL) delta(v) delta(z) / a(p,k),
a(p,k) = |(1-p^(-k))(1-p^k)| = p^k+p^(-k)-2 > 0.
```

Integration over the FULL circular phase contributes L, not kL: the
fixed circle is traversed in the trace integral once even for a repeated
return. There are no positive-time fixed points on the terminal component;
the restricted distribution there is zero. For h with compact support in
(0,T], only finitely many p,k occur. Its spatial support is the finite
union of their compact central circles. The projection of this support
to the test-time interval is proper. Therefore both the noncompact spatial
integration and the countable component sum are well-defined, without
an infinity-minus-infinity regularization or a selected state subspace.

We have constructed, from the actual full kernel,

```text
Theta_0 = sum_p sum_(k>=1) (log p)/a(p,k) delta_(k log p).
```

It is a positive locally finite measure on positive time. This is a flat
trace distribution, not an ordinary trace of U_t on H at each time.

### J2b. Full-volume L2 status and the decisive mismatch

Contact-volume invariance gives ||U_t f||_2=||f||_2, and U_(-t) is its
inverse. Density extends U_t uniquely to a unitary on the entire H.
H is infinite dimensional, for example by disjoint positive-volume boxes
in one component. Thus |U_t|=I has infinite trace: every U_t, including
t=0, is noncompact and not trace class. The ordinary trace-class determinant
det(I-z U_t) is consequently unavailable for nonzero z by that prescription.
This does not contradict the positive-time joint flat trace and does not
rule out a separately specified future operator construction.

At t=log2 the only contributing pair is p=2,k=1. Its denominator is
a(2,1)=1/2. Therefore

```text
Theta_orb({log2}) = log2,
Theta_0({log2})   = 2 log2.
```

Already this coefficient refutes the proposed identification. Other
denominators vary with p,k, so no common constant rescales all coefficients.
STOP that scalar identification here. The following construction describes
the actual frozen D_0; it is not a compensating modification to recover D_orb.

### J2c. The actual scalar flat-determinant function

Dividing the derived time measure by t=k log p gives

```text
log D_0(s) = - sum_p sum_(k>=1) p^(-ks)/(k a(p,k)).
```

Because a(p,k)=p^k(1-p^(-k))^2,

```text
p^(-k) < 1/a(p,k) <= 4 p^(-k).
```

Absolute/local uniform convergence follows for sigma>0 from the same
integer-series estimate now with exponent sigma+1. For sigma<=0 the
k=1 terms dominate1/p, so the defining integral is not absolutely
convergent. This is the exact absolute-convergence boundary; it is not
a barrier to meromorphic continuation. The Laplace transform of Theta_0
and termwise logarithmic differentiation are also valid for sigma>0,
using the convergent log-weighted integer majorant. With the sign of our
reciprocal convention, D_0'/D_0 is that Laplace transform.

The geometric-series derivative supplies the positive identity

```text
1/a(p,k) = p^(-k)/(1-p^(-k))^2
         = sum_(m>=1) m p^(-km).
```

For sigma>0 its entire absolute triple sum is bounded by the estimate
above. Fubini and the already proved Euler identity, now at s+m with
Re(s+m)>1, yield

```text
log D_0(s) = - sum_(m>=1) m log zeta(s+m),
D_0(s)     = product_(m>=1) zeta(s+m)^(-m),   Re s>0.
```

Here each logarithm is the single analytic Euler-series branch on Re>1.
The infinite product is NOT presumed a Fredholm factorization.

For any compact K in C let b=min_(s in K) Re s. Choose M so b+M>=2.
For Re z>=2 the Euler log has absolute bound
C 2^(-Re z): enlarge its prime sum to integers and bound
sum_(n>=2)n^(-sigma) by(1+2/(sigma-1))2^(-sigma).
Hence sum_(m>=M) m log zeta(s+m) converges uniformly on K and locally
on a neighborhood of K. Its exponential is holomorphic and nowhere zero.
The finitely many earlier factors zeta(s+m)^(-m) are meromorphic by the
verified classical continuation. Their product with this tail defines
a meromorphic continuation of D_0 to all C. Different choices of M agree
by the same overlap identity. No zero-location hypothesis is used.

Both D_0 and Z_orb normalize to1 as sigma tends to infinity, by their
absolute majorants. Their continued reciprocals are nonetheless different:
D_0 is holomorphic and nonzero at s=1 by its convergent defining exponential,
whereas D_orb=1/zeta has a zero there. The direct coefficient mismatch
already proved this without continuation.

## 5. Results

| Object | Established meaning | Initial absolute domain | Boundary |
| --- | --- | --- | --- |
| Z_orb | Full physical orbit zeta equals zeta | Re s>1 | Ordinary counting, not scalar trace |
| Theta_orb | Locally finite length-counting measure | Positive compact time; Laplace Re s>1 | Derived coefficients, no operator assignment |
| Theta_0 | Actual joint-kernel scalar flat trace | Positive compact time; Laplace Re s>0 | Inverse transverse Jacobians retained |
| D_0 | Product over m of zeta(s+m)^(-m) | Re s>0 | Meromorphic continuation, not ordinary Fredholm representation |
| U_t on H | Full-volume unitary group | All real t | Never trace class |

The source, clock, primitive and repetition conventions remain identical
throughout MAIN. The two analytic weight systems were distinguished before
calculation; their disagreement is retained, not normalized away.

## 6. Controls and adverse findings

### J3a. FACTOR-OFF retains composite primitives

Its OWN complete quotient, proved in348 C1, is two terminal R3 components
and one circular component of length log n for EVERY integer n>=2. The
same displayed hyperbolic physical flow and volume apply on those full
components. Its ledger has one primitive for every such n. Consequently

```text
Z_F(s) = product_(n>=2) (1-n^(-s))^(-1), Re s>1,
Theta_F = sum_(n>=2,k>=1) (log n) delta_(k log n),
Theta_0,F = sum_(n>=2,k>=1) (log n)/a(n,k) delta_(k log n),
log D_0,F(s) = -sum_(n>=2,k>=1) n^(-ks)/(k a(n,k)), Re s>0.
```

The preceding integer majorants prove these domains and local finiteness;
the same local kernel submersion proves the scalar formula for this OWN
flow. The domains are sharp for absolute convergence by the k=1 integer
harmonic comparison. At log4 the n=2,k=2 and n=4,k=1 contributions are
distinct and must add. Theta_F has coefficient log2+log4=3 log2;
MAIN Theta_orb has only log2 there. The scalar control likewise adds BOTH
terms with denominator a(2,2)=a(4,1)=9/4. No merging of commensurable
components is allowed. Its full-L2 unitary is again not trace class.
No global continuation of this control is needed or claimed here.

### J3b. DRIFT-ONLY is not an isolated-orbit trace problem

Its OWN flow on Q_p is([u+t],v,z). Each(v,z) in R2 supplies a distinct
primitive circle of the same length log p. At any real s, even a countably
infinite subset of this family gives an infinite positive k=1 sum. At
complex s the absolute terms have the same problem. Thus there is no
half-plane of absolute orbit-sum convergence and no locally finite
unweighted length-counting measure. Picking a center or a transverse
probability measure would change the frozen counting prescription.

For its actual scalar kernel the diagonal constraints are(t-kL,0,0),
not the three-rank constraint of MAIN. The transverse identity kernels
restrict formally to delta(0) twice; the prescribed distributional diagonal
pullback is not defined. Equivalently its conormal restriction has the
forbidden transverse covectors. This failure occurs locally, before the
additional issue of noncompact fixed R2 fibers. Theta_0 and D_0 are
UNDEFINED under this card, not zero and not MAIN's formula. Its volume
pullback remains unitary/non-trace-class. This is not a claim that every
other regularization or transverse weighting is impossible.

### J3c. UNIT-HOLONOMY has no positive-time contribution

Its OWN full quotient is one R3 per source basin, with u real and no
circular identification. All points require t=0 for a physical return,
despite the retained source lag isotropy. The primitive set is empty, so
Z_U=D_orb,U=1 and Theta_orb,U=0. The joint kernel diagonal has empty
positive-time support on every component; thus Theta_0,U=0 and D_0,U=1,
entirely. Its full-volume pullbacks are still unitary and not trace class.
An empty flat trace is not an ordinary zero trace for a non-trace-class
operator. Source lag cannot replace the missing geometric period.

### Strongest adverse inference and naturalness

FACTOR-OFF satisfies the same local Reeb/volume and scalar-kernel geometry
but has extra composite primitives. Thus that geometry by itself PROVES
TOO MUCH to explain prime selection. The factorization/gcd source selects
the packet set; hyperbolic transverse dynamics isolates its circles; source
geometric holonomy supplies the periods. The ordinary zeta is then forced
by the complete ledger. Its familiar name is not independent evidence that
the engineered source or contact structure is canonical or unique.

No new naturalness theorem is established. Nor can finite checks, a
meromorphic function or an internal review convert this owner-level result
into a formal Route certificate. The scalar failure is specific, not a
no-go against every future transfer or graded construction.

## 7. Gate assessment

| Gate | Evidence | Disposition | Remaining boundary |
| --- | --- | --- | --- |
| J1 / ordinary owner-level T3 | Same-input verification and J1a–b | ESTABLISHED | Strong naturalness OPEN |
| J2 / scalar positive-time trace | Joint kernel submersion and proper support | ESTABLISHED | Not an ordinary L2 trace |
| J2 / actual D_0 | Absolute triple sum and locally uniform meromorphic product | ESTABLISHED | No Fredholm representation supplied |
| J2 / scalar equals ordinary | log2 coefficient; distinct value behavior at1 | STOP: FALSE FOR FROZEN CHOICE | No retuning under this card |
| J3 / controls | All three full own ledgers and kernels | COMPLETE scoped audit | No universal no-go |
| T0–T2 | Same348 source/flow, not changed here | Retained same-object dependencies | No cross-candidate credit |
| Classical A0/A1/A2 | No classical base-map suspension | NOT APPLICABLE | Not rebranded by T3 |
| Formal Route A / B | Not evaluated | UNASSIGNED / NOT INVOKED | Separate entry/authority required |

## 8. Conclusion and decision

Portfolio **ADVANCE** the unchanged RCF01 ordinary orbit zeta and actual
scalar flat-determinant function; **STOP** their proposed scalar
identification. The decisive gate reason is the unavoidable transverse
Jacobian in the SAME flow's scalar kernel, not lack of an Euler product.
Strong arithmetic naturalness remains OPEN.

The bounded next-step audit ends with that split outcome. Any different
operator, function space, bundle or trace requires a fresh analytic owner
card and user-selected continuation; the present record does not silently
authorize it. The original flow, source, clock and controls remain fixed.
There is no new reserve candidate, formal Route evaluation or external release.

## Reproducibility and evidence index

The proofs above are exact symbolic/analytic arguments; no experimental
precision, cutoff, finite orbit enumeration or numerical zero data is used.
The only cutoff formula is a proved analytic tail bound. An independent
reader must check348's full quotient/packet theorem, the elementary kernel
restriction here and the cited classical continuation; file checks alone
cannot certify those arguments.

- [Frozen owner card](candidate-card.md).
- [Input identity and external-source provenance](evidence/source-record.md).
- [Pre-analysis scope review](evidence/scope-review.md).

AI disclosure: root and delegated internal agents perform the derivations,
adversarial checks and document work. Human proof verification, external
peer review, cross-family/model independence and calibrated confidence are
NOT attested. Independent derivations and checkpoints are recorded with
their actual input boundaries; a review label is not a mathematical proof.

EOF — author proof; independent analysis and final handoff checks pending.

## Final clarification — frozen478-line analysis input preserved

The preceding478 lines are the fixed checkpoint2 author input, SHA-256
`d6431109167315e5c3467c00739b00fe3f2696d255f7b15f1738a8074089d1fd`.
This supplement resolves a terminology point and makes the adverse local
trace test explicit. It changes no object, coefficient, domain or conclusion.

In J3a, the phrase "two terminal R3 components" must be read as TWO
NONCIRCULAR R3 components: the empty-terminal component and the singleton-1
basin. Only empty is terminal. Singleton(1) is fixed by the FACTOR-OFF
source, with retained Z source isotropy, as348 C1 and the frozen card
already require. On BOTH full components the physical coordinate u is
real and the physical flow translates it by t, so there is no positive
physical return or contribution to either trace. This clarification
preserves, rather than deletes, the unit source kernel.

For DRIFT-ONLY the undefined-diagonal statement can also be checked by
an explicit local regularization test, not only a wavefront criterion.
Near t=kL>0, write its full local kernel in the three difference
coordinates (u'-u+t-kL,v'-v,z'-z). Replace each Dirac factor by
rho_epsilon(a)=epsilon^(-1)rho(a/epsilon), with rho smooth, nonnegative,
compactly supported, integral1 and rho(0)>0. On the spatial diagonal
the two transverse factors multiply to epsilon^(-2)rho(0)^2. Pairing
the remaining time factor with a nonnegative test function supported near
kL and nonzero there tends to a strictly positive finite number; use
also a compact positive spatial test to avoid any infinite-volume issue.
The whole pairing therefore diverges as epsilon^(-2). There is no
unregularized distributional diagonal restriction under the prescribed
kernel construction. Subtractions, transverse measures or a selected center
would be new definitions, not values of the frozen Theta_0.

**Final mathematical status:**
`ORBIT ZETA ESTABLISHED; SCALAR IDENTIFICATION STOP; NATURALNESS OPEN`.
The ordinary zeta identity and actual scalar flat-determinant function are
positive owner-level T3 results; their proposed identification is false.
The same RCF01 source, form, clock, quotient and full physical ledger remain
intact. Classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.

EOF — final mathematical clarification; review records have separate standing.

### Completed-package evidence navigation

- [Independent MAIN scalar derivation](evidence/scalar-independent.md).
- [Independent full-control derivations](evidence/control-independent.md).
- [Analysis review and final delta review](evidence/analysis-review.md).
- [Claim ledger](claim-ledger.md).
- [Verification, exact versions and preservation](evidence/verification.md).

The control report also preserves a completed OPTIONAL NONCORE elementary
continuation calculation. It is not needed for this paper's control verdict
and is not promoted into a new MAIN result. Root checked the complete
control derivation, including that clearly separated supplement.

EOF — current scientific record; review verdicts remain bounded by their receipts.
