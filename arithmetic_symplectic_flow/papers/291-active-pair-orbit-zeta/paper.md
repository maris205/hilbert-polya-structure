# The ordinary orbit zeta of the complete active-pair owner

Audit ID: `ASFS-AUDIT-20260920-APZ01`.
Candidate ID: `ANG-20260920-APR01` (unchanged 288/289).
Paper ID: `291-active-pair-orbit-zeta`. Date: 2026-09-20.
Status: `ORDINARY ORBIT ZETA ESTABLISHED; TRACE/FREDHOLM OWNER OPEN — SCOPED ADVANCE / FORK`.
Result type: exact scalar orbit-counting and analytic-identity audit.

## Abstract

The complete active-pair owner has exactly one primitive oriented
time-circle per prime, with least time log p and all repetitions
retained. Under the newly frozen ordinary unit-weight counting
normalization, its orbit-zeta logarithm converges normally and
absolutely precisely in the half-plane Re s>1. A finite-product
unique-factorization argument identifies its own zeta there with
the ordinary Dirichlet series sum n^(-s), hence with the Riemann
zeta function. Classical meromorphic continuation then continues this
same scalar function. Differentiation derives a locally finite
length-weighted periodic-counting measure with prime-power coefficients.
This is not a trace formula, Fredholm determinant, spectral model or
naturalness result. Three separate arithmetic controls produce distinct
counting functions. The full non-Hausdorff carrier and all null,
terminal and nonreturning states are unchanged.

## 1. Frozen identity and the same-object dependency

The [analytic card](candidate-card.md) was frozen before this audit,
SHA-256

    76830495c7e32a08de4dc270d620e6144ce307da3d8360b67954e5332464f413

It is a new scalar analytic contract for the SAME candidate, not a
new dynamical object or retroactive revision of 288/289. Those prior
papers explicitly left such a contract for later work.

Let K=Z_hat, with its full topology and normalized additive Haar h.
The complete source is Y=coproduct_(a,b>=2) {(a,b)} x K², with
joint Haar mass one per root. Its unchanged partial rule is

    w(b)=#{d:1<d<b,d divides b}, j=x mod b in [0,b-1],
    c_pair=2b-a+w(b)+j,
    T(a,b,x,y)=(b,c_pair,y,(x-j)/b+y), only if c_pair>=2.

All terminal states remain. The full retained-lag partial-tail
groupoid owns c_G=log D_alpha-log D_beta on actual beta-to-alpha
branches, where D_alpha is the product of consumed indices. The
real extension on all Y x R has complete real translation and
arrows (w,t)->(z,t+c_G(g)). No roof or clock is changed here.

| Ledger item | Same-candidate evidence | Boundary |
|---|---|---|
| Arithmetic lineage | Proper-divisor admissibility -> active integer feedback -> coupled residue source | Stated deformation, not a classical symplectic lift |
| Full map/groupoid/clock | [288](../288-active-pair-residue-flow/paper.md), Lemma 1 / Proposition 2 | Joint IMAGE law, including null states |
| Complete primitive/repetition list | 288 Theorems 5/6 | Exactly one gamma_p of least log p per prime; no other positive packets |
| Packet topology | [289](../289-active-pair-packet-topology/paper.md), Theorem 3 | Closed embedded circles in the FULL quotient |
| Full ambient topology | 289 Theorem 6 | Non-Hausdorff, unchanged |
| Analytic normalization | Present frozen card | Unit primitive weights and 1/r repetitions; scalar counting only |
| Operator/domain/trace/Fredholm determinant | NOT SUPPLIED | No borrowing from another object or a target function |

The all-period seed proof in 288 and the full-quotient proof in 289
are essential dependencies. This paper does not infer the prime ledger
from the desired Euler product. Source hashes and exact references
are recorded in [evidence](evidence/README.md).

## 2. Ordinary counting and local finiteness

Let P be ALL actual primitive oriented time-circles of this complete
owner. Count a circle once, not once per source state or transient
preimage. Freeze a_(gamma,r)=1 and define

    L_C(s)=sum_(gamma in P) sum_(r>=1) exp(-s*r*T_gamma)/r,
    Z_C(s)=exp L_C(s)

where absolute convergence is established. The normalization is the
ordinary unweighted orbit convention. It is not asserted to coincide
with stability determinants or the trace weights of any operator.

**Proposition 1.** The measure

    nu_C=sum_(gamma in P) sum_(r>=1) T_gamma delta_(r*T_gamma)

is a locally finite positive Borel measure on positive time. Its
support is bounded away from zero. No nonreturning state is removed
from the owner by this definition.

*Proof.* The complete prior ledger gives gamma=gamma_p and T=log p.
For r log p<=R, necessarily p<=exp R and r<=R/log 2. Thus only
finitely many pairs (p,r) occur on any bounded time interval, and
each contributes the finite weight log p. The least possible time
is log 2. Every existing circle and every positive repeat is counted;
all other states remain in the dynamical object but supply no closed
orbit to this ordinary sum. This is the usual distinction between a
periodic-orbit functional and restricting a dynamical carrier. QED.

The primitive-length weight in nu_C will be DERIVED by differentiation
of the frozen 1/r convention, not inserted as an arithmetic input.

## 3. Normal convergence and the exact scalar identity

**Theorem 2.** On Re s>1, L_C is normally absolutely convergent,
Z_C is holomorphic and nonzero, and

    Z_C(s)=product_p (1-p^(-s))^(-1)=sum_(n>=1) n^(-s).

The original double logarithmic series has sharp absolute-convergence
half-plane Re s>1; no assertion about every possible conditional
summation outside that region is made.

*Proof.* Substitute only the already proved COMPLETE packet ledger:
L_C(s)=sum_p sum_(r>=1) p^(-rs)/r. On a compact subset of Re s>1
choose sigma_0>1 below all its real parts. Then

    sum_p sum_r |p^(-rs)/r|
      <= [1/(1-2^(-sigma_0))] sum_(n>=2) n^(-sigma_0) < infinity.

The Weierstrass test proves normal absolute convergence and permits
the finite geometric-log identity followed by limits. Hence Z_C is
the displayed product and is nonzero as exp L_C.

For an integer cutoff N, the finite product over p<=N expands by
geometric series to the absolutely convergent sum of n^(-s) over
positive integers whose prime factors are all at most N.
Unique factorization gives coefficient one. It includes every n<=N.
The difference from sum_(n>=1)n^(-s) is bounded in modulus by
sum_(n>N)n^(-sigma_0), which tends to zero uniformly on the same
compact set. The product limit is therefore the stated Dirichlet
series. This cutoff is an exact proof device, not a finite numerical
experiment or an incomplete orbit census.

For sharpness, at real s=1 each finite product over p<=N is at
least sum_(n<=N)1/n, because its nonnegative expansion contains all
those integers. Taking real logarithms and letting N grow proves
sum_p sum_r p^(-r)/r diverges. For 0<sigma<=1 its terms are at
least the corresponding terms at sigma=1. For sigma<=0 even the
r-sum at p=2 diverges in absolute value. Absolute values depend
only on sigma=Re s, proving the stated boundary. QED.

The final Dirichlet series is the standard definition of zeta(s)
on Re s>1 in [NIST DLMF 25.2.1](https://dlmf.nist.gov/25.2#E1).
The candidate identity above was proved from its own ledger, not
obtained by assigning that name to an unrelated analytic object.

**Corollary 3 (scalar continuation only).** Z_C has the classical
meromorphic continuation to C, with a single simple pole at s=1
of residue one.

*Justification.* The standard zeta function has that continuation,
as stated in [DLMF section 25.2(i)](https://dlmf.nist.gov/25.2#i).
Theorem 2 proves equality on an open half-plane; hence this is a
continuation of the SAME scalar function, unique as a meromorphic
continuation on C. The historical continuation theorem is cited,
not reproved or claimed as a new research result here. No global
single-valued logarithm of Z_C follows, and the original double
series is not claimed to converge beyond its proved domain.

This does not locate any zero, compare numerical zeros, construct a
completed-Xi determinant, or identify an operator spectrum. A scalar
identity obtained from an engineered prime ledger does not close
the earlier arithmetic-naturalness question.

## 4. Differentiation derives the prime-power length count

**Proposition 4.** On Re s>1,

    R_C(s)=-Z_C'(s)/Z_C(s)
          =sum_p sum_(r>=1) (log p) p^(-rs)
          =integral_(0,infinity) exp(-st) dnu_C(t).

Equivalently nu_C has coefficient log p at t=log n if n=p^r
for some prime p and r>=1, and zero at other integer logarithms.

*Proof.* On the same compact half-plane as above the differentiated
absolute sum is bounded by

    [1/(1-2^(-sigma_0))] sum_(n>=2) (log n) n^(-sigma_0),

which converges. Thus differentiation term by term is justified.
The derivative of exp(-srT)/r is -T exp(-srT), so the frozen
repetition denominator cancels r and leaves PRIMITIVE length T,
not the repeated length rT. Since Z_C=exp L_C there, its logarithmic
derivative is -L_C', proving the first formula. Proposition 1 and
absolute convergence justify the Laplace integral. Unique factorization
gives at most one prime base for an integer prime power, yielding
the coefficient statement. QED.

These are the usual prime-power coefficients, obtained as an output
of actual least lengths and repetitions. No such weight was placed
in T, c_G, a_(gamma,r) or the source. nu_C is a periodic-counting
measure, NOT a trace distribution. There is no identified evolution
operator whose trace equals this integral, and no Weil/explicit-formula
or quantum statement is made.

The differentiated series also fails absolute convergence for
Re s<=1: at sigma=1 each term is at least log 2 times the
corresponding logarithmic-series term, and the same comparison
and single-prime r-test apply below that line.

## 5. Exact arithmetic controls keep extra primitives visible

The three controls have their own full actions and domains, frozen
and classified in 288 Section 6. Apply the SAME ordinary counting
convention to each of those separate complete ledgers; do not change
APR01 or promote a control to its operator owner.

| Control | Its own orbit-counting zeta on Re s>1 | Distinction from the main owner |
|---|---|---|
| OFF, witness v=0 | product_(n>=2)(1-n^(-s))^(-1) | Every integer index is a primitive |
| ON, witness v=1 | 1 | No periodic packets |
| SHIFTED, v(b)=w(b+1) | product_(n>=2,n+1 prime)(1-n^(-s))^(-1) | Different primitive index family |

The same absolute majorants over all n>=2 justify these products
and differentiated series for Re s>1 (ON is the empty sum/product).
No global continuation for OFF or SHIFTED is inferred here.

For OFF, the length-count coefficient at t=log 4 is log 2+log 4:
the repeat of primitive index 2 and the distinct primitive index 4
both remain. In the main owner that coefficient is only log 2.
At t=log 6, OFF has log 6 while the main owner has zero. For
SHIFTED the coefficient at log 3 is zero, whereas the main owner
has log 3; at log 4 it again retains log 2+log 4. ON has no
positive-time atom at all. These coefficients distinguish the measures.
For analytic distinction, let A(s)=sum_m a_m m^(-s) be the difference
of two logarithmic-derivative functions, absolutely convergent at some
sigma_0>1, and let m_0 be its first nonzero coefficient. For real
sigma>=sigma_0,

    |m_0^sigma A(sigma)-a_(m_0)|
      <= m_0^sigma_0 [m_0/(m_0+1)]^(sigma-sigma_0)
         sum_(m>m_0) |a_m| m^(-sigma_0) -> 0.

The first differences from the main owner are m_0=4 for OFF,
m_0=3 for SHIFTED and m_0=2 for ON. Thus their logarithmic
derivatives differ, so the corresponding nonzero Z functions cannot
be identical. This argument uses the proved absolute convergence,
not an inference from a finite numerical comparison.

Thus index arithmetic alone does not force the main scalar function.
The original witness selection matters, but the generic zero-set
encoding risk identified in 288/289 remains. Neither the Euler product
nor its continuation makes this engineered choice uniquely natural.

## 6. Counting measure is not joint Haar or an automatic trace

By 288 Proposition 7 the full returning source set B=union_p B_p
is countable and joint-Haar-null. Consequently 1_B=0 almost everywhere,
and multiplication by 1_B on ordinary square-integrable equivalence
classes is the zero map. A nonzero orbit-counting contribution cannot
be obtained merely by calling this indicator a nonzero projection
onto returning states in that Haar space.

This elementary measure check constructs no Hilbert/quantum model
and computes no trace. It does NOT say every integral-kernel trace
must ignore null diagonals, nor rule out continuous-function spaces,
distributional traces, transverse measures or other justified analytic
owners. None is supplied by this paper. A future choice must state
its actual space, action, domain and relationship to the entire owner.

Likewise the non-Hausdorff full coarse quotient remains as proved in
289. Summing its closed circles does not Hausdorffize it. Both facts
are scope controls, not reasons to erase the positive scalar result.

## 7. Assessment and next research decision

| Obligation | This audit's outcome | Remaining boundary |
|---|---|---|
| Same-source T0/scoped T1 | Retained from 288 | Stronger arithmetic naturalness OPEN |
| Complete T2 circles/repetitions | Retained from 288/289 | Full quotient remains non-Hausdorff |
| Ordinary scalar T3 zeta | ESTABLISHED, with declared unit weights and sharp absolute domain | Counting normalization, not stability/trace weights |
| Scalar meromorphic continuation | ESTABLISHED by proved identity and classical continuation | Not a new continuation theorem or zero-location result |
| Length-counting measure | ESTABLISHED; coefficients derived from repetitions | NOT an operator trace |
| Operator/domain/Fredholm/trace | NOT SUPPLIED / OPEN | Requires a separate actual analytic-owner contract |
| Classical A0/A1/A2 / formal Route / B | NOT APPLICABLE / UNASSIGNED / NOT INVOKED | No Route success or quantum owner |

Portfolio: **scoped advance / fork**. Retain the exact scalar analytic
layer for APR01; continue breadth for a stronger arithmetic mechanism.
The next genuinely different analytic step would require an explicitly
defined same-owner operator and a proved trace/determinant relationship,
not renaming the known scalar function as a determinant. No such step
is started here. The parallel [breadth note](evidence/breadth-note.md)
supplies no new rule; it records a fixed-source-block reachability
diagnostic as a possible search preference, not an extra retroactive gate.

## Evidence and disclosure

The [claim ledger](claim-ledger.md), [evidence index](evidence/README.md),
[primary-source scope record](evidence/source-record.md) and
[internal adverse review](evidence/independent-review.md) document the
dependency locks, all-state proofs, exact controls and review order.
There is no scientific numerical run, fitted parameter, target-zero
input or finite-check extrapolation. ARS structures the freeze and
three internal adverse checkpoints. Same-model/shared-context AI review
is not external peer review, formal verification or independent-error
evidence. Old packages and mirrors are unchanged; 241/242 paused;
the programme goal remains active.
