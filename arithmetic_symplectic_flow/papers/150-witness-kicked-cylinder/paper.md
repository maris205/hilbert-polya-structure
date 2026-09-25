# Witness kicks select prime support but leave continuous cylinder packets

**Paper ID:** 150-witness-kicked-cylinder  
**Candidate ID:** ASFS-20260915-WKC01  
**Date:** 2026-09-15  
**Status:** STOP — PRIME-ONLY PERIODIC SUPPORT; CONTINUUM PACKETS AND ORDINARY PRODUCT FAILURE.  
**Evidence:** exact elementary proof on the complete state space.  
**Route:** owner-level geometry, arithmetic support and complete periodic
ledger; formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

A single symplectic map on all integer-labelled cotangent cylinders feeds
local proper-divisor witnesses into its continuous momentum. A momentum
cycle sum excludes every composite fibre from the full periodic set. In
each prime fibre the surviving map is an integrable shear: precisely the
rational momenta are periodic, with least full-state period
lcm(K_n, denominator(p)). Quotienting by cyclic phase retains a continuum
of distinct packets at each rational momentum. The same unit-roof
suspension therefore has prime-only periodic support but not one finite
packet per prime. Its ordinary unweighted product fails already on the
length-one family at n=2, p=0. The candidate stops without changing its
roof or restricting its phase space. No billiard-table realization,
operator trace, formal Route coordinate, or universal no-go theorem for
scattering dynamics is asserted.

## 1. Frozen object and same-object ledger

The [version-1 card](candidate-card.md) was frozen before these claims.
For every n>=2 put

\[
K_n=\max(1,\lfloor\log_2(n-1)\rfloor),\qquad
B(n,k)=\{d:2^k\le d<2^{k+1},\ d<n\},
\]
\[
b(n,k)=\sum_{d\in B(n,k)}1_{\{d\mid n\}},\qquad 1\le k\le K_n.
\tag{1}
\]

The integer K_n can equivalently be read from binary length; no prime
logarithm is an input. The blocks partition 2,...,n-1. For n=2 the sole
block is empty. With k^+ cyclic successor, the complete base is

\[
M=\coprod_{\substack{n\ge2\\1\le k\le K_n}}T^*S^1,\qquad
(q,p)\in(\mathbb R/\mathbb Z)\times\mathbb R,\qquad
\omega=dq\wedge dp,
\]
\[
F(n,k,q,p)=\bigl(n,k^+,q+p\pmod1,\ p+b(n,k)\bigr).
\tag{2}
\]

| Field | Owner and exact scope | Result / boundary |
| --- | --- | --- |
| Base and form | Every full cylinder in M with its canonical area | Smooth symplectic geometry established below |
| Arithmetic | All n, divisibility and the fixed blocks (1), executed in (2) | Prime-only periodic support, not a prefiltered prime domain |
| Clock and flow | tau=1 and the mapping torus of this exact F | Complete three-dimensional suspension |
| Primitive convention | Least full-state period, all q and real p, quotient only by cyclic time | Complete rational-momentum classification |
| Repetition and stability | Same map and unit roof | Repeated length r m; unipotent monodromy |
| Analytic proposal | Ordinary unweighted product over every primitive flow orbit | Scoped failure from continuous short-period multiplicity |
| Measure | Componentwise canonical area | No finite normalization of canonical area or trace normalization is supplied |
| Coding | Intrinsic integer, phase and witness observations | Full symbolic conjugacy OPEN; not used for time |
| Operator / later owner | No operator, function space, Hamiltonian, contact or quantum owner supplied | OPEN / NOT SUPPLIED |

The base is a countably disconnected noncompact smooth surface. Its
odd-dimensional mapping torus is not thereby a symplectic manifold or
Hamiltonian flow. Equation (2) defines a scattering/twist map mathematically;
it is not a claim that a billiard table with specified reflecting walls has
been constructed.

## 2. Question, lineage and scope

The precise [prior-work](../../docs/prior_work/README.md) arrow is

~~~text
prime/composite divisor-exclusion symbols
  -> autonomous phase-local witness batches
  -> direct momentum kicks in conservative cylinder geometry.
~~~

The retained predicate is exclusion of every proper divisor between 2
and n-1. This is a constraint deformation of the symbolic sieve, not a
conjugacy to its full chronological trajectory and not a claim to complete
the original Logistic or Hénon systems.

The question is whether actual geometric execution of the witness rule
suffices for finite prime packets. The answer for (2) is negative despite
an exact positive support result. The distinction from
[103](../103-arithmetic-billiard-static-input-boundary/paper.md) is that
the arithmetic test acts during evolution, not only through preselected
rectangle dimensions. Unlike
[052](../052-hyperbolic-wheel-packet-lift/paper.md), the carrier is not
assembled from a prime-indexed wheel list. Unlike
[137](../137-sieve-mask-translation/paper.md), its periodic support excludes
composite labels. These are scoped comparisons, not transferred claims.

No prime table, Riemann zeros, von Mangoldt weights, fitted parameter,
prime-specific component selection or logarithmic roof enters (1)--(2).
The binary batching is a fixed macrotime convention; a full scan still
processes n-2 elementary divisor tests. Stronger physical timing and target
naturalness are not established.

## 3. Global geometry and flow

### Proposition 1 — Exact inverse and symplecticity

M is Hausdorff and second countable, and F is a global smooth
symplectomorphism.

**Proof.** A countable disjoint union of cotangent cylinders is a smooth
Hausdorff surface with a countable atlas. Given (n,k',Q,P), let k be the
preceding phase and write b=b(n,k). The unique inverse is

\[
F^{-1}(n,k',Q,P)
=\bigl(n,k,Q-P+b\pmod1,\ P-b\bigr).
\tag{3}
\]

This formula respects q modulo one and is smooth on each component.
Because b is constant on that component, the pullback is

\[
d(q+p)\wedge d(p+b)
=(dq+dp)\wedge dp=dq\wedge dp.
\tag{4}
\]

Thus both the inverse and symplectic identity hold on the full M, with no
excluded impacts, corners or boundary singularities. QED.

The frozen suspension is

\[
M_1=(M\times[0,1])/((z,1)\sim(Fz,0)).
\tag{5}
\]

For 0<=u<1 and arbitrary real t, write j=floor(u+t). Flow time t is
represented by (F^j z,u+t-j). The globally invertible map and unit roof
make this well-defined for every real t. Only finitely many section
crossings occur in finite time, so there is no Zeno obstruction.

## 4. Complete periodic classification

### Proposition 2 — Composite exclusion and prime support

No composite fibre contains a periodic point. Every prime fibre contains
periodic points.

**Proof.** Suppose a full state has positive period m. The phase must
return, so K_n divides m. Summing its momentum increments gives

\[
0=p_m-p_0
=\sum_{t=0}^{m-1}b(n,k_t)
=\frac{m}{K_n}\sum_{k=1}^{K_n}b(n,k).
\tag{6}
\]

The final sum counts all proper divisors d with 2<=d<n. It vanishes
exactly for prime n, including the empty-block case n=2. Hence composite
fibres are impossible. If n is prime, all kicks vanish; p=0 and any q
then return after the phase completes its K_n steps. QED.

This is an endogenous support selector in one all-integer map. It does
not yet assert a finite number of packets over each selected label.

### Proposition 3 — All least periods and packet multiplicities

For a prime n, a full state is periodic if and only if p is rational.
Write p=a/d in lowest terms with d>=1, including p=0 with d=1.
Every q at that momentum has least full-state period

\[
m(n,p)=\operatorname{lcm}(K_n,d)
=K_n\frac{d}{\gcd(K_n,d)}.
\tag{7}
\]

For each such pair (n,p), the number of primitive base orbits is
continuum, not one and not a finite number.

**Proof.** For prime n the exact iterate is

\[
F^j(n,k,q,p)=(n,k+j\pmod{K_n},q+jp\pmod1,p).
\tag{8}
\]

A return requires K_n|j and jp an integer. If any positive j satisfies
the latter condition then p is rational. For p=a/d in lowest terms it
is equivalent to d|j. The least simultaneous positive solution is (7),
independently of q.

Every orbit meets the phase-k=1 circle at that fixed p. Its successive
intersections are q, q+K_np, q+2K_np, and so on modulo one. This rotation
has order h=d/gcd(K_n,d), so each primitive orbit contains exactly h
such section points. The full packet space is consequently

\[
(\mathbb R/\mathbb Z)/\langle K_np\pmod1\rangle,
\tag{9}
\]

the quotient of a circle by a finite rotation group. It is again a
circle and has continuum cardinality. Equation (9) counts all orbits;
it does not select one representative packet and discard the others.
Together with Proposition 2 this classifies every real state and every
period, including negative rational p and irrational nonperiodic p. QED.

### Proposition 4 — Owned flow lengths and stability

Each primitive base orbit of (7) yields exactly one oriented primitive
closed orbit of (5), of length m(n,p). Its r-fold traversal has length
r m(n,p). Every such orbit is parabolic.

**Proof.** A return to the same suspension height takes an integer
number of unit crossings. Its least positive return therefore agrees
with the least full-state base period, while cyclic phase changes
identify section points of the same flow orbit. The r-fold traversal
adds the same unit roof a total of r m times. No orientation-reversal
quotient is imposed.

On the full tangent space of each cylinder,

\[
DF=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
P_\gamma=DF^{m}=\begin{pmatrix}1&m\\0&1\end{pmatrix}.
\tag{10}
\]

All eigenvalues are one, and det(I-P_gamma^r)=0 for every positive r.
This degeneracy is retained, not normalized away. QED.

## 5. Ordinary-product stop

### Proposition 5 — No ordinary unweighted product in a right half-plane

The frozen proposal

\[
\prod_{\gamma\ {\rm primitive}}(1-e^{-sT_\gamma})^{-1}
\tag{11}
\]

does not define a finite ordinary product for any positive real s.
In particular it supplies no ordinary analytic Euler product in a right
half-plane.

**Proof.** At n=2 one has K_n=1 and b=0. For each q modulo one,
(2,1,q,0) is a distinct fixed point. Each gives a distinct primitive
flow orbit of length one. Selecting any L distinct such orbits solely
as a lower-bound subcollection of the complete product gives

\[
\prod_{\gamma\ {\rm in\ that\ subcollection}}
(1-e^{-sT_\gamma})^{-1}=(1-e^{-s})^{-L}.
\tag{12}
\]

For real s>0 this tends to infinity with L. All other real factors
are greater than one. Thus even the directed net of finite
subproducts cannot converge to a finite value. Equivalently the
first-repetition sum already contains arbitrarily many identical
positive terms e^{-s}. This is a multiplicity obstruction, independent
of orbit cutoffs or numerical precision. QED.

No claim excludes an independently frozen measured, weighted or
regularized construction. None is the ordinary counting product (11),
and none is supplied here. No operator trace is inferred from a failed
scalar product.

## 6. Controls and adverse findings

| Frozen comparator / check | Exact outcome | Interpretation |
| --- | --- | --- |
| Zero witness force | Every integer fibre has all rational-momentum periodic families | Actual kicks, not just the component label, select prime support |
| Block cardinality force b(n,k)=|B(n,k)| | Total momentum increment per scan is n-2; all n>=3 lose periodic points, while n=2 retains its empty-block family | Positivity alone does not select primes; the arithmetic relation matters |
| Shifted test d|(n+1) in the same blocks | Periodic support is n with n+1 prime; n=4 gains support and n=3 loses it | Same geometry is sensitive to the specific integer divisibility relation |
| Full real momentum | Rational p of every sign are retained; irrational p never returns in prime fibres | Fixing p=0 would change the carrier and still leave a continuum |
| Full circular position | Packet quotient is the finite quotient (9), never a chosen centre | Prime-only support does not imply finite multiplicity |
| Ordinary counting | n=2, p=0 alone gives the lower bound (12) | No global enumeration is needed to certify this stop |
| PROVES_TOO_MUCH | Any nonnegative phase-local force has no cycles in fibres with positive total kick | Prime identification comes from divisor exclusion, not a uniquely arithmetic geometric rigidity principle |

For the shifted comparator, if n+1 is composite it has a proper divisor
between 2 and n-1 when n>=3: take a factor no larger than (n+1)/2.
If n+1 is prime none exists. The edge n=2 also has no shifted witness
because its block is empty and n+1=3 is prime. This proves the table's
support statement without replacing the candidate's test.

All controls are comparisons, not changed versions of ASFS-20260915-WKC01
with transferred credit. In particular no impact section, momentum
restriction, transverse hyperbolic owner or roof is borrowed from another
candidate. No finite computation, statistical fit, external arithmetic
table or literature theorem is used in the proofs.

## 7. Gate assessment and decision

| Gate | Evidence for this frozen object | Status / limitation |
| --- | --- | --- |
| P0 | Full smooth symplectic base, inverse, unit roof, complete flow and ledger convention | ESTABLISHED |
| A0 | Geometric witness execution yields periodic support exactly at prime labels; three arithmetic controls distinguish the rule | Bounded endogenous support ESTABLISHED; finite prime packets and target clock not established |
| A1 | Entire periodic set, least periods, cyclic quotient, repetitions and monodromy | Complete owner ledger ESTABLISHED; required finite packet multiplicity scoped FAIL |
| A2 | Frozen ordinary unweighted counting product | Scoped FAIL from continuous length-one multiplicity |
| Formal Route coordinates | No target/divisor evaluation | UNASSIGNED |
| Route B | No invocation or later owner | NOT INVOKED |

**Portfolio decision: stop this candidate; fork the search.** The decisive
reason is continuum short-period multiplicity. The exact positive
prime-support result remains a reusable control. No local adjustment of
walls, slopes, roofs or selected states is performed. This scoped result
does not prohibit other scattering geometries; any such proposal requires
a new frozen object and its own complete periodic ledger.

## Evidence index

- [Frozen candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence methods, limits and verification](evidence/README.md)
- [Local research plan](../../plan.md)
