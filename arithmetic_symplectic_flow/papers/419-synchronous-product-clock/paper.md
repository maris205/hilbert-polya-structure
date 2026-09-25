# Synchronous products: full packet multiplicity and summed density clocks

Candidate: ANG-AUDIT-20260923-SPC01. Date2026-09-23.
Outcome: SYNCHRONOUS PRODUCT LAW ESTABLISHED; TWO INTEGER-EXPANDING CYCLES FORCE COMPOSITE PRIMITIVES — CONDITIONAL FILTER / FORK

## Abstract and owner

For the two total measured Borel maps fixed in the [card](candidate-card.md),
the full synchronous product owns the sum of their pointwise IMAGE clocks.
Its actual groupoid is the SAME-LAG fibre product, not the unrestricted product.
Parent cycles of lengths p,q yield gcd(p,q) different product packets, each
of least SOURCE cycle period lcm(p,q) and signed sum (lcm/p)C_1+(lcm/q)C_2. Zero sums retain
ineffective isotropy. Two integer-expanding parent cycle multipliers force a
composite primitive multiplier. Three full controls show the obstruction,
clock cancellation with packet multiplicity, and the mixed-sign boundary.
This is a conditional realization filter, not an admitted arithmetic carrier.

The source, product measure, branch partition, inverse versions, groupoid and
height action all belong to SPC01. Classical symplectic/suspension fields are
NOT APPLICABLE. T3 NOT AUDITED; formal Route UNASSIGNED; Route B NOT INVOKED.
No operator, target-zero comparison or RH assertion is made. The lineage link
is symbolic admissibility -> full higher-dimensional realization, conditional
on separately supplied parents; generic geometry supplies no arithmetic seed.

## 1. IMAGE, clock, and the exact arrow relation

Write a parent arrow g_a=(z_a,k,w_a), with T_a^m z_a=T_a^n w_a, k=m-n,
and c_a(g_a)=S_am(z_a)-S_an(w_a). Parent branch inverse densities q_ai are
prescribed at EVERY actual point, not merely as equivalence classes a.e.
The product branch inverse is I_1i times I_2j, and its pointwise density is
Q_ij(y_1,y_2)=q_1i(y_1)q_2j(y_2). On Borel rectangles the IMAGE identity follows
from the two parent identities. Sigma-finiteness, positive densities, product
integration and extension from rectangles to Borel sets give the identity on
every actual product inverse domain. This proves ownership for mu_1 times mu_2.
Consequently kappa(z_1,z_2)=kappa_1(z_1)+kappa_2(z_2), at all points.
No factor from dimension, number of branches or sheet count may be inserted.

**Theorem 1 (synchronization).**
G_T is bijective, as a groupoid, to
{(g_1,g_2): lag(g_1)=lag(g_2)}; its clock is c_1(g_1)+c_2(g_2).
One direction is projection of the same witnesses m,n. Conversely choose
parent witnesses (m_1,n_1),(m_2,n_2) of the same lag k. Their two differences
m_2-m_1 and n_2-n_1 agree. Increase the smaller pair to the larger pair by
applying the appropriate extra iterate to its common endpoint. TOTALITY makes
this legal. These synchronized witnesses give the product arrow. Equal actual
triples are identified, so witness choice creates no copies. Composition and
inverse are componentwise and preserve common lag.

The same witness extension adds the same tail sum on both sides, proving
cocycle descent; synchronizing intermediate witnesses proves additivity.
Alternatively it follows from the two parent cocycles once the bijection is
proved. A forward arrival (Tz,-1,z) has clock -kappa(z), not +kappa(z).
The proof does NOT apply to partial parents: a terminal endpoint may prevent
the extra iterate. No assertion about that larger class is made.

Write ell for common lag. The complete kernels are

    K_ell = {(g_1,g_2): ell_1=ell_2=0},
    K_c   = {(g_1,g_2): ell_1=ell_2, c_1+c_2=0},
    K_ell intersect K_c = {ell_1=ell_2=0, c_1+c_2=0}.

They are formulas for ALL actual arrows, not just isotropy. Cancellation can
occur between nonzero parent clocks. Lag-zero merging arrows need not be units
for noninjective parents; no such arrows are discarded.

## 2. Cycles, all incoming and the complete isotropy image

A deterministic total-map source is isotropic iff it is eventually periodic:
an equality T^m x=T^n x with m>n supplies an eventual cycle; conversely its
least cycle period generates every possible lag. Thus source isotropy is pZ
for eventual least period p, and zero otherwise. If either product coordinate
is not eventually periodic, product source isotropy and H are zero.

Now fix parent least cycles gamma_1,gamma_2 of lengths p,q, sums C_1,C_2.
Put g=gcd(p,q), l=lcm(p,q). On their p q core pairs the forward action adds
(1,1) to phase indices in Z/p times Z/q. It has exactly g orbits, distinguished
by the phase difference modulo g; each has l states. They are distinct source
packets: two periodic cores of a deterministic map cannot merge later unless
they lie on the same cycle. For EACH of the g packets,

    source isotropy = l Z,
    C_* = (l/p) C_1 + (l/q) C_2,
    c(l r) = r C_*,   H = C_* Z.                     (1)

Every coordinate traverses its full core l/p or l/q times, proving (1).
This is the ENTIRE H, not the image of an arbitrarily chosen loop. If C_*!=0,
extension isotropy is zero, positive primitive L=abs(C_*), repetitions rL
for positive integers r. If C_*=0, extension isotropy remains lZ and H=0;
there is no positive primitive and the phase fibre is a free real line.

For exact incoming classification index each parent cycle by x_ai=T_a^i x_a0.
If x_a first reaches x_aj_a after h_a steps, set eta_a(x_a)=j_a-h_a modulo
its parent period. This is independent of a later choice of entrance time and
eta_a(T_a x_a)=eta_a(x_a)+1. On the FULL Cartesian product of the two eventual
basins the g packets are exactly

    eta_2(x_2)-eta_1(x_1)=delta modulo g, delta in Z/g.    (2)

Indeed every such pair eventually reaches a core pair, and (2) identifies its
core orbit; all these core orbits occur. No incoming lies outside these two
basins. Equivalently each complete packet is union over n>=0 of T^{-n} of its
whole core. Immediate predecessors are ALL pairs of actual parent predecessors;
depth-n predecessors use the SAME n. This is not a choice of independent
parent entrance depths or a section of the basin.

For non-eventually-periodic pairs the equally complete source-orbit relation
is Theorem1: z~w iff there exist parent common-tail arrows from w_a to z_a
of the SAME lag. Merely requiring both independent parent orbit relations
would merge packets. The full predecessor product formula still applies,
and source isotropy/extension isotropy/H are all zero. No countability or
global regularity of the quotient is asserted.

## 3. Every height and phase

The owned extension acts on all X times R by (w,h)->(z,h+c).
Within a source packet choose one reference b and any actual arrow
g_z=(b,k_z,z), FROM z TO b. Its phase coordinate is

    h+c(g_z) modulo H_b.                              (3)

Two choices of g_z differ by reference isotropy, hence by H_b; (3) is exactly
the orbit-set phase invariant, not just necessary. For (1) it gives R/C_*Z
if C_*!=0, and R if zero. For a non-eventual packet it gives R because H=0.
This is an orbitwise construction; no global Borel selector, Hausdorff orbit
space, positive suspension roof or smooth flow is claimed. Height translation
adds its real parameter to (3). At (z,h) isotropy is precisely source isotropy
intersected with ker c, as already computed.

## 4. Scoped arithmetic obstruction

Assume for the displayed pair of parent cycles that A=exp(C_1) and B=exp(C_2)
are BOTH integers >=2. The signed C_* is positive and

    exp(L)=A^(q/g) B^(p/g).

Both factors are integers >=2, so this is composite. Existence of just this
cycle pair in the FULL product already refutes prime-only support there;
the g copies cannot be selected down to one. No parent-cycle existence is
inferred from the hypotheses of Theorem1. If every pair is absent, an empty
positive ledger is not success. The obstruction is not extended to arbitrary
rationals, opposite signs, a different clock or asynchronous products.
Nonempty, prime-only, unique-per-prime and all-prime coverage remain distinct.

## 5. Three full controls

All three controls are global bijections. Thus actual arrows are uniquely
(z,k,F^k z), k in Z; a periodic source retains different k arrows. There are
no strictly preperiodic incoming points to a core, and every predecessor is
the actual F^{-n}z. These statements concern the FULL carrier.

**A.** On R^2 with area, F=(2x,3y), inverse=(x/2,y/3), J=1/6 at every point,
kappa=log6. IMAGE follows by linear change of variables on every Borel set.
The origin is the ONLY periodic state: 2^n x=x and 3^n y=y with n>0 force
x=y=0. It is one fixed packet, source isotropy Z, H=(log6)Z, extension
isotropy zero, primitive log6 and all repetitions. Every nonzero state has
the full free source orbit {(2^n x,3^n y):n in Z}, source/extension isotropy
zero and H=0. For a chosen reference z*, at z=F^n z* phase is h+n log6.
At the origin it is h mod(log6)Z. On all arrows c=k log6, so both kernels
and their intersection consist exactly of units. Necessary prime support fails.

**B.** On (R times Z/2)^2 with its area/counting product, F=(2x,j+1,y/2,k+1),
inverse=(x/2,j-1,2y,k-1). J=1 everywhere: discrete permutations add no factor,
and real inverse determinant is one. Thus kappa=c=0 on the entire owner.
All periodic states have x=y=0, by the two real dilation equations. The four
origin-sheet states form TWO least-SOURCE-period-2 packets: k-j=0 or1 modulo2, each with
source/extension isotropy 2Z and H=0. There is no positive primitive. All
nonzero-real states have the full free orbit
{(2^n x,j+n,2^{-n}y,k+n):n in Z}, with both isotropies/H zero. In every
packet height h itself is the free phase. K_c=G, K_ell=units and intersection
units. The two parent origin cycles have p=q=2 and signed sums +/-2log2;
this checks BOTH gcd multiplicity and cancellation without deleting a sheet.

**C.** On full R^2 with area, F=(6x,y/2), inverse=(x/6,2y), J=1/3,
kappa=log3 at every point. The origin is the only periodic state, one fixed
packet with source Z, H=(log3)Z, extension isotropy zero and primitive log3.
Every nonzero state has the full free orbit {(6^n x,2^{-n}y):n in Z}, with
source/extension isotropy/H zero. Phase at F^n z* is h+n log3, or modulo
(log3)Z at the origin. Both kernels/intersection are units, since c=k log3.
This control satisfies nonempty/prime-only/unique for prime3 but NOT all-prime
coverage. Parent signed multipliers 6 and1/2 violate the two-integer-expanding
hypothesis; it is a boundary control, not a counterexample or arithmetic seed.

## 6. Method, status and handoff

Inputs are the frozen [card](candidate-card.md) and exact equations above.
All proofs are symbolic; no scientific code, finite orbit scan, precision
parameter, external literature campaign or unverified citation is used.
See the [claim ledger](claim-ledger.md) and [batch record](../415-divisor-word-sweep/batch-log.md).
The three controls address geometry, ownership, cancellation and multiplicity;
arithmetic-label randomization has no parent arithmetic source here.
Strong naturalness and PROVES_TOO_MUCH remain open for any future prime seed.

Conditional measured-ownership and synchronous-ledger theorems are established
under the exact class hypotheses. No endogenous arithmetic parent is supplied,
so this is NOT an arithmetic T1 pass or a formal Route coordinate. Portfolio
CONDITIONAL FILTER / FORK: two actual integer-expanding parent cycles already
produce an intrinsic composite primitive. Mixed signs and noninteger inputs
need their own audit. No partial-parent theorem, unconditional high-dimensional
no-go, new main candidate, operator or round420 is authorized.

AI-assisted design/drafting/proof by root; separate shared-history same-model
card-only derivation is frozen before manuscript comparison. Design expectations
were disclosed, not blind preregistration. Review is NOT_CALIBRATED, not human,
external peer or cross-model validation. Mathematical proof, internal review
and mechanical file completion remain different evidence categories.
