# Divisor-driven torus covers: owned fibre time and excess primitive packets

Paper392; candidate `ANG-20260922-DTC01`; 2026-09-22.
Batch `NONUNIT-RETURN-20260922-I`, round3/5. Exact theorem / negative target test.
Outcome: `OWNED FIBRE CLOCK; EXCESS AND COMPOSITE PACKETS — STOP / FORK`
Classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; Route B NOT INVOKED.
T0 and the specified geometric T1 are established; T2's necessary target fails.
Strong naturalness OPEN; T3 NOT AUDITED. No smooth total-space volume is asserted.

## Abstract

The full coprime divisor-recurrence path source drives genuine finite coverings
of the complete two-dimensional torus. Its own Markov-times-Haar probability
has a positive every-Borel sheet IMAGE law, distinct from the all-point fibre
Jacobian clock. The retained-lag groupoid and full real extension keep every
unit step, null point and incoming history. In the frozen constant2 fibre there
are exactly three fixed-core packets of least time log2 and three least-source-
period-two packets of least time log4. None merge under the full actual owner.
The first multiplicity and the composite primitive independently fail the target.
Three controls are derived on their own sources. No wider cycle census follows.

## 1. Identity, question and provenance

The [97-line card](candidate-card.md) freezes the source, measure, fibre maps,
clock and controls. Its pre-proof SHA-256 is
`b55d995aea2d95e131a184d17a9d2a4790e44209a09347edd0bb371bb15efed0`.
The graph definition explicitly reuses [382](../382-divisor-prefix-recurrence/candidate-card.md);
the present probability and complete geometric owner are derived below, not
borrowed from that package. Divisibility changes both admissible edges and the
actual covering used. This is one-way coupling, not geometric feedback or a
new infinite-memory source. The symbolic process remains countable Markov.

| Field | This single frozen owner |
| --- | --- |
| Carrier/action | Full graph path space X times T²; shift with actual A_d fibre cover |
| Physical clock | Flat fibre-area inverse Jacobian, tau=log d; units stay zero |
| Probability | Own initial eta, nonuniform divisor P, normalized torus Haar |
| Arrows/packets | Actual retained-lag triples; full H, not a selected return |
| Classical geometry/operator | No symplectic base, positive roof or T3 owner supplied |

The necessary target requires every positive primitive to be log of an ordinary
prime, with at most one packet per prime. Theorems below concern this tuple,
not all covering constructions, admissibility rules or geometric clocks.
Definition-stage reading included old301/357/361/365/382/385/389 cards and
their appended outcomes. Shared author history is disclosed; no blindness,
literature priority or external-review claim. No peer/raw manuscript was read.

## 2. Full arithmetic source, probability and actual inverses

Put S={(a,b)>0:gcd(a,b)=1}, D_s={d:d divides a+b}, and
s=(a,b) --d--> t=(b,(a+b)/d). Closure follows because every divisor of a+b
is coprime to b. Each vertex has finite nonempty outdegree; choosing d=1
forever constructs an infinite path from every vertex. X contains all of them.
Each root component is the inverse limit of its finite nonempty prefix sets,
so is compact metrizable; the countable coproduct gives the frozen cylinder
topology and Borel structure. Edge cylinders identify with full target spaces.

For target t=(b,c), every predecessor is exactly
\[
 s=(dc-b,b),\qquad d\ge1,\quad dc>b,\quad\gcd(d,b)=1.                 \tag{1}
\]
Necessity uses a+b=dc and gcd(c,b)=1; conversely these conditions give a
positive coprime s and the stated legal edge. Thus (1) is exhaustive, including
units when legal. There are no terminals. Prepending this edge is a bijection
from X_t onto its complete edge cylinder, with shift as inverse.

Set C=sum_S 2^(-a-b), eta(s)=2^(-a-b)/C, Z_s=sum_(d in D_s)1/d and
P_s(d)=1/(d Z_s). Here 0<C<=1 and every eta,P is positive. The compatible
cylinder probabilities eta(s_0) product_(i<m)P_(s_i)(d_i) define a probability
nu on the full path space. Equivalently, independent uniform random variables
choose successive edges by their finite probability intervals. Every nonempty
cylinder has positive mass, hence nu has full support.

This nonuniform symbolic law is atomless, by its own argument: in any three
steps containing a d>=2, their probability product is <=1/2. If all three
divisors are1, the coprime Fibonacci update (a,b)->(b,a+b) has an even a+b
at one of these three steps (the three nonzero parity pairs cycle). There
Z_s>=3/2, so the product is <=2/3. Every length3n cylinder therefore has
mass <=(2/3)^n. This proves zero mass for every individual infinite path.
It is not stationary: incoming root mass at (1,1) is
\[
 {1\over C}\sum_{d\ge2}{2^{-d}\over d Z_{(d-1,1)}}
 \le {1\over6C} < \eta(1,1)={1\over4C},                         \tag{2}
\]
since d Z_(d-1,1)>=d+1>=3. No stationary source law is substituted.

Let Y=X times T², mu=nu times normalized flat Haar h_2, and
F(xi,v)=(shift xi,A_d v), A_d=[[0,-d],[1,0]]. For a target representative
(u,v) in [0,1)², all its fibre preimages are
\[
 (v,(k-u)/d\bmod1),\qquad 0\le k<d.                            \tag{3}
\]
They solve (-dy,x)=(u,v) modulo1; any solution determines a unique k modulo d.
Together with (1) this proves both inverse identities and all predecessor
domains. The formulas are Borel including every cut value; their images
partition each edge-cylinder fibre. Representatives do not create extra points.
The torus map itself is a smooth local diffeomorphism everywhere, also on cuts.
Thus F is a continuous local homeomorphism on Y using genuine local torus charts,
not a claim that the global Borel sheets are globally smooth charts.

## 3. Every-Borel IMAGE and the separately owned fibre clock

On each sheet (3), h_2(I E)=h_2(E)/d for every Borel E in T². To verify it,
use standard representative rectangles, subdivide across the finitely many
mod1 cuts and apply the ordinary linear determinant 1/d on each piece;
boundaries are Haar-null and are still mapped bijectively by (3). The same
factor follows in every local smooth chart, whose flat area forms agree.
On X_t, prepending edge e:s->t has IMAGE factor eta(s)P_s(d)/eta(t), first
on cylinders by their displayed probabilities and then on all Borel sets by
uniqueness of finite measures. Fubini therefore proves, for every Borel
E subset X_t times T², on every individual complete Borel sheet,
\[
 \mu(I_{e,k}E)=j_{e,k}\mu(E),\qquad
 j_{e,k}={\eta(s)P_s(d)\over d\eta(t)}>0.                       \tag{4}
\]
There is no restriction to conull histories. Full support passes to mu;
it is atomless, and (2) also proves that mu is not F-invariant.

The physical tau is instead -log of the inverse FIBRE-area Jacobian, namely
log d. The differential of the actual covering has determinant d at EVERY
torus point; each local inverse has determinant 1/d. Local lifts differ by
integer translations, so this value is unambiguous at all cuts and null points.
It is intrinsic to the fixed complete flat fibres, not an ambient smooth
structure or volume on Y. For the (1,1) self-edge d=2, (4) gives j=1/6,
whereas the geometric inverse Jacobian is1/2. These are different clocks.

For a legal prefix u=(e_0,...,e_(m-1)), define
D(u)=product_i d_i, B(u)=A_(d_(m-1))...A_(d_0), with empty values1,I.
Every inverse sheet of B(u) has fibre Jacobian 1/D(u); composition of (3)
lists all D(u) preimages. Its full probability IMAGE is
\[
 J_\mu(u)={\eta(s_0)\prod_{i<m}P_{s_i}(d_i)\over
                   \eta(s_m)D(u)}.                            \tag{5}
\]
This follows by iterating (4) and telescoping eta, for every Borel domain.
For two prefix sheets meeting a common tail, their history-pair IMAGE is
the ratio of (5); the geometric ratio uses only the factors 1/D. Different
sheet presentations do not add arrows to the actual groupoid.

## 4. All actual arrows, kernels, isotropy and phases

For z=(xi,v), write D_m(z)=product_(i<m)d_i and S_m(z)=log D_m(z).
The actual groupoid consists of (z,m-n,w) with F^m z=F^n w, source w.
It is Borel (a countable union of equality loci), with the usual countable
local inverse-pair atlas if topology is needed. Two witnesses for the same
triple differ by the same added integer in both exponents. After ordering
them, the extra common forward segment multiplies both D's by the same
factor. Thus c=log(D_m(z)/D_n(w)) is independent of witnesses. Padding
composable witnesses to a common middle iterate proves additivity; inversion
negates c. This also proves that c is the negative logarithm of the inverse
history-pair fibre Jacobian. No probability-clock substitution is used.

The following are the ENTIRE kernels, for any witnessing m,n:
\[
 \ker c=\{(z,m-n,w):D_m(z)=D_n(w)\},\quad
 \ker\ell=\{(z,0,w):F^m z=F^m w\text{ for some }m\};             \tag{6}
\]
their intersection imposes both same-depth meeting and equal D_m. These
finite integer-product criteria apply at every state, not only on loops.
On all Y times R use (w,h)->(z,h+c). Additivity gives a Borel groupoid
extension and all real height translations commute with it. Its orbit SET
has the resulting complete R-action; no Hausdorff or invariant-measure claim.

For ANY total deterministic map, a nonzero isotropy lag is equivalent to
eventual periodicity: F^m z=F^n z with m>n makes F^n z periodic. On its
eventual cycle the set of return integers is exactly qZ, where q is its
least period (division with remainder proves this). Hence source isotropy
is0 off eventual cycles and qZ on them. Here, on a least full q-cycle,
\[
 Q=D_q(z_*),\quad c(kq)=k\log Q,\quad H_z=(\log Q)\mathbb Z.     \tag{7}
\]
The initial transient cancels in each difference; the cyclic phase does not
change Q. Extension isotropy is the c-kernel of this qZ: zero if Q>1,
all qZ if Q=1. Off eventual cycles both isotropy and H are zero.
In MAIN a closed arithmetic path cannot have every d=1: a+b strictly
increases under (a,b)->(b,a+b). Thus every eventual full cycle has Q>1,
and extension isotropy is zero at every MAIN object and every height.

For completeness this classifies full periods without replacing them by
symbolic periods. For any least symbolic cycle of length ell, let B be its
ordered fibre product. Its full periodic states are exactly v with B^r v=v
for some r>=1; least such r gives full period q=ell r. All eventual states
are exactly all finite preimages of these, and every other state has trivial
isotropy. Equations (B^r-I)v=0 are equations on the WHOLE torus, not just
rational points or selected fixed fibres. This is a characterization, not
an enumeration of additional cycles; the frozen bounded probe follows next.

All incoming to a cycle z_j=F^j z_0 are the union, over every finite legal
prefix u ending at its root and every phase j, of states whose tail is that
of z_j and whose fibre v solves B(u)v=v_j. All D(u) solutions are retained.
This union need not be disjoint; equal states/triples are identified, never
counted as separate sheet-word histories. Conversely every source-orbit
member has such a forward meeting, so no incoming is missing. Distinct
periodic cores are in the same source orbit exactly when their cycles
coincide: a forward meeting of two periodic points makes the cycles equal.

For a general source orbit choose a base z_0 and an arrow g_y:y->z_0.
The full extension quotient over that orbit is R/H, with coordinate
h+c(g_y) modulo H. Different choices differ by an isotropy clock, proving
both sufficiency and necessity of this identification. Height time is
translation, with stabilizer exactly H. On a cycle incoming through
F^m y=z_j, the coordinate is h+S_j(z_0)-S_m(y) modulo log Q. Thus one
cycle gives one physical packet, with every real phase and repetitions
k log Q; finite incoming excursions cannot create or remove its primitive.

## 5. Entire fixed and least-two-period constant2 probe

Let xi_* be the (1,1) d=2 self-edge forever. Its whole fibre is invariant.
Fixed points satisfy y=x and 3x=0, and are exactly
p_r=(r/3,r/3), r=0,1,2. Their full source period is1 and (7) gives
H=(log2)Z, source isotropy Z, extension isotropy0. The three fixed cores
cannot meet forward, hence define three distinct primitive log2 packets.

Since A_2²=-2I, all points fixed by its square are exactly
{(r/3,s/3):r,s in {0,1,2}}. On this grid A_2 interchanges r and s,
because -2=1 modulo3. Removing the three diagonal fixed points leaves
exactly three cycles, indexed by unordered pairs {r,s}, r<s. Each has
least FULL source period2, source isotropy2Z, H=(log4)Z and extension
isotropy0. Its two phases are one packet, not two; the three cycles do
not merge. A primitive log4 is not a repetition of a different log2 packet.

For every one of these six cores, all incoming are exactly the prefixes
ending at root(1,1) with B(u)v equal to a specified core phase, as in §4.
Their physical coordinate is h+j log2-log D(u) modulo q log2, q=1 or2.
This includes unit prefixes, every inverse sheet and every real height.
The points and their finite preimages are Haar-null, but the actual geometry
already fixed their clock; neither (4) alone nor deletion sets their time.
Exactly three log2 and three log4 packets occur WITHIN THIS PROBE, not an
assertion that these exhaust MAIN. Both target violations are decisive;
no further main fibre period or arithmetic cycle census is performed.

## 6. Three separately owned controls

**U, INDEX-ONE.** On its own Y_U=X times T² and mu_U=nu times h_2,
F_U=(shift,Jv), J=A_1. Each arithmetic predecessor (1) has the unique
fibre inverse J^(-1)v=(v_2,-v_1). The probability sheet factor is
eta(s)P_s(d)/eta(t), not (4); local fibre Jacobian1 fixes tau_U=0.
For finite histories the probability factor is eta(s_0) product P/eta(s_m).
These follow from cylinders and the invertible Haar-preserving rotation,
giving every-Borel laws, full support and the same atomless, nonstationary
symbolic law. All actual arrows remain; ker c_U=G_U, and its intersection
with the lag kernel is exactly the full same-depth tail relation.

Here J^4=I. Its least fibre period r(v) is1 at (0,0),(1/2,1/2), 2 at
(0,1/2),(1/2,0), and4 everywhere else: solve Jv=v and J²v=-v=v.
For a symbolic eventual least period ell, the full eventual period is
lcm(ell,r(v)); for a non-eventually-periodic symbolic path isotropy is0.
Thus extension isotropy equals source qZ wherever present, while H={0}
EVERYWHERE. All incoming prefixes have their unique J^(-m) fibre lift to
each cyclic phase; general orbit meetings use the same unique inverse.
The phase coordinate is h in R, and there is no positive physical packet.
Zero geometric time does not erase its nonzero source/extension isotropy.

**A, ARITHMETIC-OFF.** Its own source is N_positive^N with iid p_d=2^(-d),
and its measure is this probability times h_2. It has full support and is
atomless since every n-prefix probability is <=2^(-n). All d>=1 precede
every tail, with every sheet (3); their every-Borel IMAGE is p_d/d, proved
by independence and the rectangle calculation. Finite-history IMAGE is
product_i p_(d_i)/D(u). Every A_d preserves full torus Haar because the
d inverse sheets have total factor1. Independence then proves this control's
product measure IS invariant, unlike MAIN; checking product cylinders suffices.
Its own geometric clock is log d. Deriving its actual triples by shift and
cover composition gives exactly (6) with its unrestricted prefixes; (7) and
the full-period product criterion follow from its own deterministic map.

The exceptional Q=1 cycles here must have digit tail1 forever, and J gives
least full periods1,2,4 exactly as listed for U. They have H=0 but source
and extension isotropy qZ; all other eventual cycles have Q>1 and extension
isotropy0. Non-eventual states have isotropy/H0. Solving its own constant2
equations gives the three diagonal fixed points and three off-diagonal
two-cycles above, hence three log2 and three log4 probe packets. ALL finite
digit prefixes are allowed incoming now: solve B(u)v=v_j on the whole torus.
The phase h+j log2-log D(u) modulo q log2 retains every sheet. Its different
source cannot identify different periodic cores, by the forward-meeting proof.

**C, CIRCLE-COVER.** Its own Y_C=X times T, mu_C=nu times normalized
length, and F_C=(shift,dv) use (1) and all inverse points (u+k)/d,
0<=k<d. Partitioning the circle gives every-Borel factor 1/d, so the own
probability IMAGE is eta(s)P_s(d)/(d eta(t)) and the finite version is (5).
This is a separate one-dimensional calculation, not transferred area geometry.
The complete circle derivative d fixes tau_C=log d at every cut/null point.
Full support, atomlessness and nonstationarity follow from its own product
law and §2's unchanged source argument. For its actual arrows the product
kernels (6) hold. The monodromy over a symbolic cycle is multiplication by
D_ell; least fibre return r gives full period ell r and H=r log D_ell Z.
Every eventual arithmetic cycle contains a nonunit, so extension isotropy0
everywhere; off eventual cycles source isotropy and H are zero as well.

In C's entire constant2 circle, fixed means v=2v, hence v=0 only; squared
fixed means 3v=0, giving0,1/3,2/3. The latter two form one least-period-two
cycle. Thus its probe has one log2 packet and one distinct primitive log4
packet, with source isotropy Z and2Z respectively. All incoming are legal
prefixes ending at(1,1), with v=(v_j+k)/D(u), 0<=k<D(u). Their phases are
h+j log2-log D(u) modulo q log2. No other core can merge these cycles.

## 7. Decision, limitations and reproducibility

The complete fibre geometry, own probability laws, actual inverses and full
lag/clock owners are established. The target stops on the required small
probe; controls neither repair it nor supply a borrowed clock. This does not
exclude every divisor-source extension, or every geometric/conditional clock.
Unit steps prevent a strictly positive roof; no classical mapping-torus,
symplectic lift, smooth total-Y volume, invariant MAIN law or T3 is claimed.
The generic period criterion is not an additional cycle enumeration.
Strong naturalness and nice coarse topology remain OPEN; formal UNASSIGNED,
Route B NOT INVOKED. Portfolio STOP / FORK; no next object is opened here.

Evidence: [card](candidate-card.md), [claim ledger](claim-ledger.md),
[overview](README.md). Exact proofs use cylinder measures, linear torus
charts and finite integer equations; no scientific numerics or cutoffs.
CP1 was root-released; CP2/CP3 and separate review remain root-owned.
AI-assisted derivation/writing has shared-history internal NOT_CALIBRATED
status, not external peer review. No outside references, searches or novelty claim.
Data availability: definitions and proofs are fully in this Markdown package.
Ethics: no human subjects or private data. Contributions: scoped AI-assisted
formal derivation/writing; root integration and review are separately owned.
Funding and conflicts: no declarations supplied; no unsupported declaration made.

EOF — DTC01 full-owner proof and three own controls; bounded target STOP / FORK.
