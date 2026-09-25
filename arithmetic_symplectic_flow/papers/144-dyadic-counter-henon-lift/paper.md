# A dyadic divisor-executing symplectic map with exact packets and logarithmic macroperiods

**Paper ID:** 144-dyadic-counter-henon-lift.  
**Candidate ID:** ASFS-20260915-DBH01.  
**Date / status:** 2026-09-15; ADVANCE — EXACT MARKED RETURN, FULL SYMPLECTIC PACKETS, LOGARITHMIC MACROPERIOD.  
**Route state:** owner-level construction evidence; formal Route coordinates
UNASSIGNED; Route B NOT INVOKED.

## Abstract

One explicitly frozen two-dimensional symplectic map executes dyadic batches
of proper-divisor tests while advancing a cyclic phase and modular witness
counter. Its carrier is the full countable disjoint union of planes over
every integer, phase and counter, and its transverse rule is the fixed
Hénon-form map (q,p) to (p,3p-q). We prove the inverse, complete suspension,
arithmetic return criterion, and entire intrinsic periodic set. A marked
integer fibre contains a full-state return after one complete phase scan
exactly when its label is prime. If a_n counts proper divisors and
g_n=gcd(n,a_n), the complete n-fibre contributes g_n primitive orbits of
length K_n n/g_n, where K_n is its binary scan depth. In particular, prime p
contributes p orbits and K_p/log(p) tends to 1/log(2). This is the actual
unit-roof clock of this same geometric map, not a clock imported from a
symbolic comparator. The ordinary product of all packets is holomorphic
and nonzero for Re(s)>2 log(2). The result does not give exact logarithmic
prime lengths, one orbit per prime, a prime-power trace, or an operator.
The binary macroclock is a valid architectural choice; neither a unique
canonical choice nor physical constant-cost divisor batching is claimed.

## 1. Question, frozen identity and lineage

The [version-1 card](candidate-card.md) was frozen before this audit. The
question is whether its positive-dimensional symplectic owner retains the
complete arithmetic return, finite packet multiplicity and chosen macroclock,
without silently selecting centres from extra periodic families.

For every integer n>=2 define
\[
K_n=\max(1,\lfloor\log_2(n-1)\rfloor),\qquad
C_n=\mathbb Z/n\mathbb Z,
\]
\[
D(n,k)=\{d\in\mathbb Z:2^k\leq d<2^{k+1},\ d<n\},
\quad
b(n,k)=\sum_{d\in D(n,k)}\mathbf1_{\{d\mid n\}},
\quad 1\leq k\leq K_n.
\tag{1}
\]
Write k^+ and k^- for cyclic successor and predecessor. The full owner is
\[
M=\coprod_{\substack{n\geq2,\ 1\leq k\leq K_n\\c\in C_n}}
\mathbb R^2_{n,k,c},\qquad
\omega|_{\mathbb R^2_{n,k,c}}=dq\wedge dp,
\]
\[
\mathcal F(n,k,c,q,p)=
(n,k^+,c+b(n,k)\bmod n,p,3p-q).
\tag{2}
\]
No integer, counter value or transverse point has been removed.

The exact [prior-work](../../docs/prior_work/README.md) arrow is
prime/composite divisor exclusion, followed by reversible sequential witness
accumulation in binary batches, followed by a Hénon-form area-preserving
realization retaining phase and counter. The exclusion agrees with
[050](../050-causal-binary-sieve-fixed-point-screen/paper.md): every composite
has a proper divisor and one no greater than its square root. This is a
specified deformation of the source rule, not a claimed conjugacy with a
historical chronological prime word or a Logistic map.

[143](../143-dyadic-batched-divisor-counter/paper.md) supplies a separate
discrete comparator and [141](../141-divisor-counter-henon-lift/paper.md) a
serial geometric comparator. Neither supplies theorem or gate credit here.
The batch map, its derivative and every orbit statement are proved directly
from (1)--(2). In particular, (2) changes the base action and phase space
relative to 141; it is not a roof replacement on that old map.

| Owner field | Exact specification | Scope |
| --- | --- | --- |
| Geometry | Full countable disjoint union M of planes, componentwise dq wedge dp | Two-dimensional, disconnected and noncompact |
| Base map | Equation (2), coefficient 3 fixed | One global autonomous smooth symplectomorphism |
| Arithmetic inputs | All integers, divisibility and the displayed dyadic partition | No supplied prime table, selected prime fibres or zero data |
| Coding | Projection to (n,k,c) intertwines the geometric action and its discrete rule | Not a conjugacy of all M |
| Clock and flow | Roof identically 1 over (2); endpoint-glued suspension | One geometric macrostep per unit |
| Primitive convention | All least-period full base orbits, modulo cyclic phase | No reversal quotient or selected counter |
| Stability | Same transverse derivative at every step | Computed monodromy, not an assumed trace weight |
| Analytic owner | Ordinary unweighted product of the entire derived ledger | No transfer operator, domain or trace supplied |
| Later geometry | Contact, Hamiltonian and quantum owners | NOT SUPPLIED |

The closed-orbit calculation is required to test this geometric hypothesis.
The short product bound records its immediate analytic consequence; it is
not a formal target/divisor evaluation.

## 2. Geometry, inverse and complete owned flow

### Proposition 1 — Positive-dimensional symplectic realization

M is a Hausdorff second-countable smooth manifold of dimension two, and
mathcal F is a smooth symplectomorphism of all M.

**Proof.** The component index set is countable and each component is an
open Euclidean plane. The union of their countable Euclidean bases is a
countable basis for the disjoint-union topology. Distinct components are
separated, and the usual charts provide the stated smooth structure.

For an output (n,k',c',q',p'), recover
\[
k=(k')^-,\quad
c=c'-b(n,k)\bmod n,\quad
q=3q'-p',\quad p=q'.
\tag{3}
\]
This is a unique full preimage. The forward map and inverse are linear
smooth maps between their open plane components, with the displayed discrete
component permutation.

For the transverse map H(q,p)=(p,3p-q),
\[
H^*(dq\wedge dp)=dp\wedge(3dp-dq)=dq\wedge dp.
\]
The component permutation preserves the same componentwise form. Thus (2)
is globally symplectic. QED.

No connectedness, compactness or finite invariant volume is asserted. The
componentwise area measure has infinite total mass and is not an operator
trace prescription.

The frozen suspension is
\[
S=(M\times[0,1])/((z,1)\sim(\mathcal Fz,0)).
\tag{4}
\]
For a representative (z,u) with 0<=u<1 and any real t, put
m=floor(u+t). Translation is represented by
(\(\mathcal F^m z,u+t-m\)). This is defined for every t because the base
is globally invertible. On any bounded time interval there are only
finitely many unit-roof crossings. The flow is therefore complete and has
no Zeno accumulation.

Returning to the same suspension point requires returning the height modulo
one and hence integer elapsed time. The remaining condition is a full
base-state return. Thus least base periods equal primitive flow lengths.
This is a three-dimensional suspension, not itself a symplectic manifold
or an asserted Hamiltonian flow.

## 3. Exact arithmetic executed by the action

### Proposition 2 — Batch coverage and zero-witness return

Let
\[
a_n=\sum_{k=1}^{K_n}b(n,k).
\]
The blocks in (1) partition the proper-divisor candidates {2,...,n-1},
with one empty block at n=2. Consequently
\[
a_n=\#\{d:2\leq d<n,\ d\mid n\},\qquad
0\leq a_n\leq n-2<n,
\]
\[
a_n=0\quad\Longleftrightarrow\quad n\text{ is prime}.
\tag{5}
\]
After K_n steps, the discrete coordinates return to k and change c by a_n
modulo n, independently of the starting phase and counter.

**Proof.** For n>=3, put K=K_n. The inequalities
2^K<=n-1<2^{K+1} show that the disjoint dyadic intervals for k=1,...,K,
intersected with d<n, cover every integer from 2 through n-1 exactly once.
For n=2 the single interval has empty intersection. This proves the count
and bound.

A prime has no such divisor. Every composite n=uv, u,v>=2, has
2<=u<n, so has a witness. The strict bound a_n<n ensures that a nonzero
integer witness count cannot vanish modulo n. During one complete cyclic
phase traversal each block occurs once; its increments sum to a_n even
when the starting phase changes. QED.

The complete geometric iterate has the more precise form
\[
\mathcal F^{K_n}(n,k,c,v)=
(n,k,c+a_n\bmod n,B^{K_n}v),
\quad
B=\begin{pmatrix}0&1\\-1&3\end{pmatrix},
\tag{6}
\]
where v=(q,p). Therefore zero counter displacement is equivalent to primality
for every discrete state, but return of an arbitrary nonzero transverse
state is not asserted. The full-state existence statement follows below.

This source uses an explicitly permitted arithmetic algorithm; it does not
derive arithmetic from an arithmetic-free map. Divisibility is evaluated
inside each application of the fixed action, and the return mechanism is
affected by the resulting witnesses. A supplied completed prime word is not
an input.

## 4. The complete intrinsic periodic ledger

### Theorem 3 — Every packet, period and monodromy

Put
\[
g_n=\gcd(n,a_n),\qquad \gcd(n,0)=n,\qquad
\ell_n=K_n\,\frac{n}{g_n}.
\tag{7}
\]
For each n, the full geometric map has exactly g_n primitive orbits, all
of least period ell_n. Its entire periodic set consists of the points
with q=p=0. These statements count all transverse points before excluding
any and retain all counter multiplicity.

**Proof.** A full return first requires returning the phase, hence its
time is mK_n for an integer m>=1. The counter then returns exactly when
n divides ma_n. The least such m is n/g_n, including a_n=0. Thus every
discrete state over n has least period ell_n. There are nK_n states, so
their number of distinct cycles modulo cyclic phase is
nK_n/ell_n=g_n.

The eigenvalues of B are
\[
\lambda_\pm=(3\pm\sqrt5)/2,\qquad
\lambda_+>1,\quad 0<\lambda_-<1.
\]
For any positive integer j, neither eigenvalue of B^j is one, so
B^j-I is invertible. Therefore B^j v=v holds only for v=0. Since the
transverse evolution in (2) is exactly B at every step, every full periodic
point must have v=0, and every discrete cycle at v=0 is indeed periodic.
No other periodic family exists. QED.

For n=2 and n=3, K_n=1 and a_n=0, so the complete ledgers contain two
and three fixed-point orbits respectively. Their suspensions are five
different primitive circles of length 1, not interchangeable representatives.

Let M_n denote the union of all plane components at the marked integer n.
The exact arithmetic/full-state relation is
\[
n\text{ is prime}
\quad\Longleftrightarrow\quad
\operatorname{Fix}(\mathcal F^{K_n})\cap M_n\ne\varnothing.
\tag{8}
\]
For a composite, a_n>0 and n/g_n>1, so no such one-scan full-state return
exists. For a prime, every point with v=0 returns after one scan, while
nonzero transverse points still do not return.

By (4), each primitive base orbit owns a flow length ell_n, and r-fold
traversal has length r ell_n. The map preserves n under repetitions; a
repeated orbit over p does not thereby become an orbit labelled p^r.

The derivative monodromy on a least-period orbit is B raised to ell_n.
Its multipliers are lambda_+ raised to ell_n and lambda_- raised to ell_n;
in particular,
\[
\det(I-B^{\ell_n})
=2-\lambda_+^{\ell_n}-\lambda_-^{\ell_n}\ne0.
\tag{9}
\]
This is a hyperbolic, nondegenerate full periodic ledger. It does not imply
unit trace weights or a transfer-operator identity.

## 5. Actual logarithmic macroperiod and its limits

### Proposition 4 — Prime periods under the frozen roof

Every prime p has exactly p primitive orbits, each of length K_p. For p>2,
\[
0<\log_2 p-K_p<1,\qquad
\frac{K_p}{\log p}\longrightarrow\frac1{\log2}.
\tag{10}
\]
This is the actual geometric suspension length, measured in the frozen
unit macrostep, for every one of its prime-fibre orbits.

**Proof.** For primes, (5) gives a_p=0 and g_p=p; apply (7).
For p>2 the binary inequalities give
2^{K_p}<p<=2^{K_p+1}. Equality on the right would make p a power of
two larger than two, which is impossible for a prime. Taking base-two
logarithms gives the strict bounded difference, and division by log p
gives the ratio limit. At p=2, the separate value K_2=1 is retained. QED.

No prime-log roof has been inserted. The phase count is the binary length
of n-1 for all integers and comes from the chosen uniform partition.
The unit roof is a valid clock for the explicitly defined geometric
macro-action; an additional proof that this clock is uniquely canonical is
not required for (4) or (10) to be true.

The following stronger interpretations do not follow:

- Exact prime-log time: primes 5 and 7 both have K=2, so their lengths
  cannot both equal their distinct natural logarithms. No fixed positive
  rescaling makes every prime length exactly log p. Equation (10), an
  asymptotic statement with a constant conversion factor, remains positive.
- Unique prime packets: the five and seven primitive orbits over these
  labels are all present. Forgetting marked n loses even prime-sector
  length injectivity. Selecting one counter orbit is not allowed.
- Constant-work batching: a direct evaluation of all indicators in one
  full scan performs n-2 divisibility tests, since the blocks partition
  those candidates. A full primitive traversal performs
  (n-2)n/g_n such tests. This is an operation count for that direct
  implementation, not a lower bound for all algorithms and not an
  obstruction to defining the mathematical macro-action.
- A canonical Riemann clock or prime-power trace: a uniform binary design
  is not by itself evidence of either stronger claim. They remain OPEN /
  NOT SUPPLIED, rather than a new prerequisite retroactively invalidating
  the proved geometric construction.

Thus the linear prime-clock obstruction of the serial comparator 141 is
not an obstruction to this different batched map. The improved order of
growth has the explicitly declared architectural origin above.

## 6. Same-object ordinary product

### Proposition 5 — Sufficient half-plane of analytic convergence

The full ordinary unweighted primitive-orbit product is
\[
Z_{\rm DBH}(s)=
\prod_{n\geq2}(1-e^{-s\ell_n})^{-g_n}.
\tag{11}
\]
It is holomorphic and nonzero on Re(s)>2 log(2). There its repetition
logarithm converges absolutely and locally uniformly:
\[
\log Z_{\rm DBH}(s)=
\sum_{n\geq2}g_n\sum_{r\geq1}\frac{e^{-sr\ell_n}}r.
\tag{12}
\]

**Proof.** Formula (11) uses exactly Theorem 3's complete multiplicities
and the roof of (4), so no symbolic clock or separate analytic owner is
being substituted. Write sigma=Re(s). Since g_n<=n and ell_n>=K_n>=1,
it suffices first to bound the single traversal sum by
\(\sum_{n\geq2}n e^{-\sigma K_n}\).

Isolate n=2. For n>=3 with K_n=K, the range is
2^K<n<=2^{K+1}. It contains 2^K integers, each at most 2^{K+1}.
Therefore
\[
\sum_{n\geq2}g_n e^{-\sigma\ell_n}
\leq 2e^{-\sigma}
+2\sum_{K\geq1}(4e^{-\sigma})^K<\infty
\quad(\sigma>\log4).
\tag{13}
\]
For every ell>=1,
\[
\sum_{r\geq1}\frac{e^{-\sigma r\ell}}r
\leq\frac{e^{-\sigma\ell}}{1-e^{-\sigma}}.
\]
This bounds the absolute value sum in (12). The same bounds are uniform
on compact subsets of the half-plane by choosing their positive lower
real-part bound above log4. The holomorphic logarithmic sum can thus be
exponentiated to give a holomorphic nonvanishing product. QED.

The half-plane is sufficient, not claimed optimal. The exact abscissa,
boundary behaviour and analytic continuation are OPEN. Equations (11)--(12)
do not supply an operator, Banach/Hilbert space, domain, trace or Fredholm
determinant. Composite packets remain in the product and prime packets
have their full p-fold multiplicity.

## 7. Controls and argument boundaries

Every changed rule below is a separate comparator, not an unnoticed
modification of (2).

| Control | Exact effect | Inference and boundary |
| --- | --- | --- |
| Set b=0 | Every n has n cycles of length K_n | Phase depth alone does not distinguish primes; the actual witness action lengthens composite returns. |
| Replace b(n,k) by the cardinality of D(n,k) | Full scan displacement becomes n-2 | Only n=2 has zero displacement; every n>=3 prime loses the one-scan selector. |
| Replace modulus n by modulus 2 | At n=6, two proper divisors produce zero total modulo 2 | The frozen modulus n prevents a genuine arithmetic alias. |
| Include all noncentral transverse points | B^j-I is invertible at every positive period | No extra continuum can be hidden by selecting centres or a section. |
| Replace the discrete permutation by an arbitrary one | The same transverse hyperbolicity retains its packet ledger | Geometry alone does not generate arithmetic; (5)--(8) require actual divisor updates. |
| Compare serial action 141 | Its arithmetic count agrees, but its phase count and periods differ | The present clock belongs to a new base, not to a renamed old suspension. |
| Count elementary tests | n-2 direct tests per full scan | Macrostep time and direct computational cost must not be conflated. |
| Retain all prime and composite packets | Prime p has multiplicity p; composites have g_n>=1 | No prime-only Euler product or one-packet-per-prime selection follows. |

The marked arithmetic selector survives the appropriate nonarithmetic and
aliasing controls; the macroperiod asymptotic has an exact dyadic derivation.
The strongest naturalness limitation is that other uniform bounded witness
predicates can also be accumulated by counters and realized by the same
generic transverse geometry. This limits a claim of privileged Riemann
relevance, not the validity of the stated endogenous divisor execution or
its actual suspension clock.

The paper uses the ARS claim-evidence-counterargument discipline to keep
those levels separate. It does not report a full ARS publication pipeline,
calibrated panel, human review, novelty search or venue-fit certification.

## 8. Gate assessment and decision

| Obligation | Same-object evidence | Status / boundary |
| --- | --- | --- |
| P0 geometric owner | Equations (1)--(4), global inverse and symplectic pullback | ESTABLISHED for the full disconnected 2D carrier |
| A0 source component | Executed divisibility, no counter alias and marked one-scan return (8), adversarial controls | ESTABLISHED at the declared marked arithmetic-mechanism level |
| A0 clock evidence | Actual prime lengths K_p and asymptotic (10) under the frozen unit roof | Logarithmic macroperiod ESTABLISHED; exact/canonical prime-log interpretation not established |
| A1 owner component | Full intrinsic periodic set, all g_n multiplicities, monodromy and repetitions | ESTABLISHED; not a one-orbit-per-prime or prime-power identification |
| A2 scalar-product component | Full product (11) on Re(s)>2 log(2) | ESTABLISHED for that ordinary product; operator/trace and continuation OPEN |
| Formal Route coordinates | No separate formal target/divisor evaluation | UNASSIGNED |
| Route B | No invocation | NOT INVOKED |

**Decision: advance as an exact same-object construction result; stop
stronger target promotion at the stated evidence boundary.** This object
does supply positive-dimensional geometry, an executed arithmetic return
mechanism, complete finite packet multiplicities and a logarithmic-order
owned clock simultaneously. Those results are retained without imposing a
new requirement of unique canonical geometry.

The missing one-prime/one-packet structure, exact prime-log timing and
operator/trace owner are not concealed. Any future change in roof, quotient,
transverse action or packet convention requires a new frozen candidate;
none is implemented here. No formal A0+A1+A2 Route pass is inferred from
these owner-level components.

## Reproducibility and declarations

The [card](candidate-card.md), [claim ledger](claim-ledger.md), and
[evidence index](evidence/README.md) record exact inputs and claim scope.
All global claims follow from the displayed proofs. There is no numerical
run, cutoff, floating-point tolerance, prime table or external parameter
fit. The only finite illustrations, n=2,3 and primes 5,7, are direct
substitutions, not the basis for an infinite claim.

Data availability: all definitions and proofs are provided in local Markdown.
Ethics: no human/animal participants or personal data. Contributions:
AI-assisted formulation, mathematical derivation, drafting and checking under
the user's direction; no human verification is attested. Funding and
conflicts: no user declarations supplied, hence unknown. This is an internal
research package, not a submission-ready manuscript.
