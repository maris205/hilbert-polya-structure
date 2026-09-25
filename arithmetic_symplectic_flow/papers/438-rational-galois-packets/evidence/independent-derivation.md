# Card-only derivation — Rational-itinerary Galois packets

Candidate: `ANG-AUDIT-20260923-RGP01`; paper 438; date: 2026-09-23.
Batch: `NONHOMOGENEOUS-FEEDBACK-20260923-R`, round 4/5 (435–439).
Reviewer: `/root/nonlocal_source_review`.
Root reported full reading of the 120-line CP1 and separately released raw.
Scientific input: the complete frozen 97-line card, read through EOF.
candidate-card.md SHA256 6ec186a6e4cbb26fb743633b11904de36145b4a22e0b0531098ff0ef79dd1c8b
scope-review.md — 120 lines — SHA256 74164dd06c4f00d64d0f546f699b2bbd410e9785297dc107c9e487ba5bafe9bb
No manuscript, README, ledger, author/helper answer, sibling/peer output,
batch summary or scout-history card was opened. Older shared history remains.
Inherited-model internal AI derivation/review: **NOT_CALIBRATED**, not blind,
human, external or cross-model verification. Served identity not attested.
Exact mathematical reasoning only; no scientific code, numerics, network,
external literature, Git, PDF, operator, model change or publication.

## 1. Full local-inverse ownership for the rational partial map

Each frozen f_i is real analytic on U_i: its rational-coordinate denominators
do not vanish there. Its derivative is nonsingular at every point of U_i.
The inverse-function theorem gives an injective open neighborhood of each
point. A rational ball containing that point can be chosen inside it and U_i.
Hence the countable rational-ball injectivity atlas covers U_i. Let B_(i,r)
be its frozen enumeration and assign the actual disjoint Borel pieces

    P_(i,r)=E_i intersect (B_(i,r) minus union_(s<r) B_(i,s)).

On B_(i,r), f_i is an open injective analytic local diffeomorphism, hence an
analytic diffeomorphism onto its open image. Let theta_(i,r) be its inverse.
The actual inverse domain W_(i,r)=f_i(P_(i,r)) is Borel under this homeomorphism.
For EVERY target y in X the complete actual predecessor set is

    I(y)={theta_(i,r)(y): y in W_(i,r)}.                    (1)

Every legal predecessor belongs to its unique E_i and first eligible ball,
so is included. Conversely every listed point is a legal predecessor. The
list retains distinct roots in overlapping images and does not add roots
outside the assigned source pieces. Labels are not additional point arrows.
For x=theta_(i,r)(y), the inverse-function derivative gives the prescribed
EVERY-point version

    J_(i,r)(y)=abs(det Dtheta_(i,r)(y))
              =1/abs(det Df_i(x)),
    kappa(x)=log abs(det Df_i(x)), x in E_i.                (2)

It is finite and strictly positive as a Jacobian at every actual point.
Every Borel A subset W_(i,r) satisfies
dx(theta_(i,r) A)=integral_A J_(i,r)(y)dy by change of variables on the full
ball inverse and restriction. This includes thin/cut/null pieces; the frozen
germ fixes their pointwise version, not a.e. uniqueness of a density.
Different atlas balls through one source have the same derivative (2).
Finite inverse words restrict EVERY intermediate point to its actual P_(i,r).
Successive change of variables proves their product IMAGE; iterating (1)
retains all legal roots at every depth. No target outgoing step is required.
X minus union E_i retains identities and incoming, but its next map value
and one-step clock are NOT DEFINED. No absorbing step or artificial zero roof.

## 2. Entire partial groupoid, incoming, kernels and height phases

Use actual legal triples (z,m-n,w), source w and range z, with
T^m z=T^n w, m,n>=0, equal triples identified. Set

    c(z,m-n,w)=S_m(z)-S_n(w), S_0=0.                       (3)

Equal-lag witnesses differ by a simultaneous index shift. The additional
legal common tail begins at one point, so its sums cancel. Composition aligns
the two middle prefixes at their greater legal depth, using the continuation
already given by that longer prefix. This proves descent, closure and
additivity without extending a terminal illegally. Inverse clocks negate;
the forward arrow (Tx,-1,x) has -kappa(x). Countable branch/witness conditions
give Borel data. Choosing a first witness does not alter the descended clock.

Write I^0(y)={y}, I^(m+1)(y)=union_(v in I^m(y)) I(v). The entire source
component of w is union_(n:T^n w exists) union_(m>=0) I^m(T^n w).
This is a complete mathematical recursion, not an effective finite census.
The three full kernels are exactly

    K_lag={(z,0,w): T^m z=T^m w for some legal m};
    K_c={(z,m-n,w): T^m z=T^n w, S_m(z)=S_n(w)};
    K_joint=K_lag intersect K_c.                           (4)

Nonzero source isotropy is equivalent to eventual periodicity: two unequal
legal iterates agree. An eventual least-q cycle has source isotropy qZ.
Let C be its actual forward clock sum. Prefixes cancel on loops, so its
entire isotropy clock group at EVERY incoming point is H=CZ, with c(kq)=kC.
If no eventual cycle exists, source isotropy and H are zero, including at
terminating components. Extension isotropy at every height is qZ when C=0,
trivial when C!=0, and trivial on every non-eventual component.

Fix a reference p in a component and actual arrows g_z=(z,l_z,p), b_z=c(g_z).
Every arrow w->z has lag l_z-l_w+kq and clock b_z-b_w+kC in an eventual
component; k ranges over ALL integers. A non-eventual component has exactly
the k=0 arrow. This lists all kernel elements by imposing lag, clock or both
equal to zero, without deleting nonunit coalescences. Complete extension
phases are [h-b_z] in R/H. No Borel global choice of references is asserted.
For a q-cycle p=x_0,...,x_(q-1), an incoming z with T^n z=x_j can use

    l_z=n-j, b_z=S_n(z)-S_j(x_0).                          (5)

Other legal choices change these by q and C multiples. All incoming depths
are retained. A terminal reference t instead uses its legal hitting depth
and prefix sum, without kappa(t). C!=0 gives one physical circle per source
component, primitive abs(C), repetitions k abs(C), k>=1. H=0 gives a free
real line, even if ineffective qZ source isotropy survives in the extension.
Equal periods never identify different source components.

## 3. Conditional admitted conjugates and their ACTUAL clocks

Let x_j=T^j x, 0<=j<q, be the proposed actual least-q cycle. Put L=K_x.
Each x_j is a rational expression in x with rational coefficients, so its
coordinate field is contained in L. Conversely going forward around the
remaining cycle expresses x rationally in x_j. Thus

    Q(coordinates of x_j)=L for EVERY j.                  (6)

No rational inverse formula was assumed; the forward return suffices here.
The EXTRA admission hypothesis is essential: sigma x_j belongs E_(i_j)
for every sigma in Gamma and each j. Rational coefficients then give the
actual equalities T(sigma x_j)=sigma x_(j+1), with indices modulo q.
Nonvanishing denominators remain valid at these admitted points. Injectivity
of each field automorphism preserves distinctness of the algebraic points,
NOT real-order inequalities; hence the conjugate cycle has
the same least period q. No real-order or piece-invariance inference was used.

The rational derivatives evaluated at x_j lie in L. Define the SIGNED
nonzero algebraic determinant product of the frozen itinerary germs by

    Delta=product_(j=0)^(q-1) det Df_(i_j)(x_j) in L^*.
    C=log abs(Delta).                                    (7)

The finite germ composition is legitimate locally along this itinerary even
if cuts prevent the actual T from having that formula on a whole neighborhood.
Equation (2) proves (7) as the OWN Lebesgue forward sum. At an admitted
conjugate core O_sigma={sigma x_j}, its signed product and clock are

    Delta_sigma=sigma(Delta), C_sigma=log abs(sigma Delta),
    entire H_sigma=C_sigma Z.                            (8)

Source isotropy is qZ; extension isotropy is qZ if abs(sigma Delta)=1 and
trivial otherwise. These statements hold separately on each core's entire
actual incoming component by (1)–(5). Its positive primitive, when present,
is abs(log abs(sigma Delta)), NOT log of a norm or a chosen multiple.
In particular primitive log p, p an ordinary prime, is equivalent to

    sigma Delta in {p,-p,1/p,-1/p}.                       (9)

The reciprocal cases cannot be dropped; a contracting return has a negative
forward sum but the same positive physical generator convention.
Only algebraic determinant values are conjugated. No sigma(log real value),
real-field action, measure transport through sigma or height action is used.
For comparison log abs(N_(K/Q) Delta)=sum_(sigma in Gamma) C_sigma; this
aggregate, including extension multiplicities, is not an individual clock.
The norm for a nonnormal L is likewise a product over embeddings, not a
substitute for the actual return. Taking a norm before abs/log changes owner.

## 4. Orbit stabilizer, nonnormal L and exact rotation consequences

Gamma acts on the finite set of admitted conjugate algebraic cores by
coordinate conjugation. Define

    S=Gamma_O={sigma:sigma O=O},
    H_x=Gamma_x={sigma:sigma x=x}=Gal(K/L).

S is the set stabilizer and a subgroup. For sigma in S write sigma x=x_r.
Actual conjugate equivariance gives sigma x_j=x_(j+r), so this is a rotation.
Its offset rho(sigma)=r mod q is a homomorphism S->Z/qZ. Its kernel is
EXACTLY H_x: fixing x fixes every rational forward iterate, and a zero
rotation fixes x. If m=|rho(S)|, then

    H_x normal in S, S/H_x is cyclic of order m dividing q;
    t=[Gamma:S] is the number of DISTINCT conjugate source cycles;
    [L:Q]=[Gamma:H_x]=t m.                               (10)

Each one of those cycles contains exactly m distinct conjugates of x; it can
contain other positions not conjugate to x. Distinct source cycles cannot
have intersecting actual eventual incoming components: a deterministic
forward orbit cannot reach two different cycles. Thus t counts different
complete source packets, not different names or phases on one packet.

The field-theoretic conclusion before assuming t=1 is only the following.
Set F=K^S, an intermediate field contained in L=K^(H_x). The normality above
gives L/F Galois cyclic of degree m, with [F:Q]=t. This does NOT assert that
L/Q is normal, cyclic, or of degree dividing q. The point stabilizer H_x
need not be normal in Gamma, so Gamma/H_x must NOT be treated as a group
at this stage. Each sigma in S sends L to itself by (6); a general sigma
can send it to a different conjugate subfield. Also S fixes Delta, since
rotating a cycle leaves its scalar determinant product unchanged; Delta lies F.

Under the ADDITIONAL condition that all conjugate cores are this one core,
t=1 and S=Gamma. Then H_x is normal in Gamma and

    L/Q is Galois cyclic, [L:Q]=m divides q.               (11)

The action is faithful only after quotienting by H_x, not on all of Gamma.
Neither cyclicity of Gamma nor [K:Q] dividing q follows: the auxiliary K may
have a large kernel Gal(K/L). Conversely (11) alone has not proved actual
admission or that all conjugate points occur on this particular cycle.

Suppose THIS cycle has a positive prime primitive log p. By (9) its Delta
itself is one of four rational values. Every admitted conjugate then has
the SAME signed Delta and SAME positive primitive log p. Therefore the
necessary at-most-one-packet-per-prime benchmark forces t=1, and hence (11).
If t>1, that positive prime is duplicated; if the positive primitive is not
a prime logarithm, prime-only already fails. When Delta=+1 or -1 there is
no positive packet here, so this argument forces no t=1 conclusion. Other
cycles might supply nonemptiness; no unconditional whole-owner failure or
existence claim follows from the conditional test.

If sigma in S rotates by r, the ACTUAL arrow x->x_r is (x_r,-r,x), with
clock -S_r(x), so height h moves to h-S_r(x). This is the phase relation
between those positions, not a Galois operation on real height. Different
conjugate cycles have no arrow between their cores and no phase merger.
No isomorphism of their real incoming sets, derivatives or measures follows
from algebraic core conjugation. Each is kept by its own recursion (1),(5).

## 5. Controls A and C — own inverses and complete source dynamics

Let f(x)=(x^3+2x)/4 and a(x)=f'(x)=(3x^2+2)/4>0. On R it is strictly
increasing, with limits -infinity and +infinity at the respective ends.
Thus A is a global analytic bijection, and its inverse theta(t) is the UNIQUE
real solution of s^3+2s-4t=0. Oddness and monotonicity imply theta(t)>0 iff
t>0. On C's SEPARATE carrier (0,infinity), f is likewise onto that carrier,
with limits 0 and infinity at its ends and the unique positive inverse.
No zero or negative point or inverse is added to C. Direct inverse
differentiation and change of variables on each owner's own full domain give

    J_A(t)=4/(3 theta(t)^2+2), t in R;
    J_C(t)=4/(3 theta(t)^2+2), t>0;
    kappa(x)=log a(x).                                   (12)

These finite positive analytic EVERY-point versions satisfy EVERY-Borel
IMAGE for their respective measures. There are no missing roots, terminals,
additional sheets or extra inverse weights. All inverse histories are the
unique theta^m(x), with the carrier restriction maintained at every depth.

An increasing line map has no nonfixed finite cycle: an initial strict
increase/decrease persists under iteration and cannot return. Fixed points
solve x(x^2-2)=0. Put s=sqrt2. A has exactly -s,0,s, each a singleton cycle.
C has exactly s. Their complete incoming sets are just themselves, because
both maps are bijective. Their source isotropy is Z, and the signed products,
forward sums and entire clock groups are

| Owner/core | Signed Delta | C | Entire H |
| --- | --- | --- | --- |
| A at 0 | 1/2 | -log2 | log2 Z |
| A at -s or s | 2 | log2 | log2 Z |
| C at s | 2 | log2 | log2 Z |

Extension isotropy is trivial in every row. Each core gives one circle, phase
h mod log2, primitive log2, and repetitions n log2. At 0 the positive primitive
is NOT discarded because its oriented clock is negative: this tests 1/p in (9).

All other points are non-eventual. The complete invariant interval strata and
one half-open fundamental set for every nonperiodic source orbit are

| Interval I | Forward direction and limit | Backward limit | Fundamental set D_I |
| --- | --- | --- | --- |
| (-infinity,-s) | decreasing to -infinity | -s from below | [-3,-2) |
| (-s,0) | increasing to 0 | -s from above | [-1,-3/4) |
| (0,s) | decreasing to 0 | s from below | [3/4,1) |
| (s,infinity) | increasing to infinity | s from above | [2,3) |

For A all four rows occur; for C exactly the two positive rows occur. These
claims follow from f(x)-x=x(x^2-2)/4, monotonicity and the fixed endpoints.
A finite limiting point of a monotone iterate would be a fixed point, proving
the displayed limits. The endpoint computations f(-2)=-3, f(-1)=-3/4,
f(1)=3/4 and f(2)=3 show that the iterates of each D_I tile its interval
disjointly. Consequently every nonperiodic orbit has a UNIQUE representative
b in D_I, and its full states are z_n=f^n(b), n in Z. All such orbits are
bi-infinite, with the actual incoming at depth m equal to z_(n-m). No point
is removed by the half-open choice; the limit endpoints are already separate
cores or excluded carrier boundaries, not extra finite-time ancestors.

## 6. A/C all-arrow ledger, kernels, phases and Galois boundary

For either own bijection and any integer n define D_n(w)=(f^n)'(w)>0.
For n>=0 this is the exact product of a along the n forward iterates;
D_0=1 and D_(-n)(w)=1/D_n(f^(-n)w). All these are actual derivatives of
the globally defined forward/inverse iterates, not illegal negative times
for a partial map. The full groupoid and signed clock are

    G={(f^(-k)w,k,w):w in the OWN carrier, k in Z},
    c(k;w)=-log D_(-k)(w).                               (13)

For a forward arrow k=-1 this is -log a(w), as required. All histories and
all three kernels are exactly specified by

    K_lag=units, K_joint=units,
    K_c={(f^(-k)w,k,w):D_(-k)(w)=1}.                      (14)

Equation (14) is an exact derivative-product equation for EVERY signed
integer k and EVERY actual w, permitted by the card; it is not a finite
census of its solutions. Nonunit solutions exist: a(w)=1 at
w=+sqrt(2/3), also at w=-sqrt(2/3) in A, and the corresponding forward
arrows have zero clock but different endpoints. Those are not source loops.
At every fixed core only the k=0 clock-kernel element occurs.

On a nonperiodic orbit z_n=f^n(b), write A_n=log D_n(b). Every arrow
z_m->z_n has lag m-n and clock A_m-A_n. Thus the complete clock kernel
is A_m=A_n, while lag/joint kernels are units, and the complete physical
phase is h+A_n in R. Source/extension isotropy and entire H are zero.
Each orbit supplies a free physical line and no positive repetitions.
Together (12)–(14), the four interval families and the fixed cores classify
the WHOLE A ledger and, with its own positive carrier, the WHOLE C ledger.

At A's probe s, K=L=Q(sqrt2), q=1; both conjugates s and -s are actually
admitted on the one full real source piece. They are distinct fixed cycles
with distinct full singleton incoming components, not phases of one cycle.
Here S=H_x={1}, m=1, t=2, [L:Q]=2; the duplicated primitive is log2.
A's third fixed packet at 0 adds another log2. The entire positive ledger
is exactly THREE log2 packets: prime-only and nonemptiness hold, uniqueness
fails. Nothing else in its full nonperiodic source contributes a period.
At the rational fixed 0, L=Q even if the auxiliary K is Q(sqrt2); this also
exhibits why [K:Q] need not divide a source period q=1.

At C's probe s the algebraic conjugate -s is outside its frozen carrier.
The extra admission hypothesis FAILS; the conditional duplicate conclusion
cannot be invoked. C has exactly ONE positive packet, of primitive log2,
so it passes the stated necessary nonempty/prime-only/at-most-one benchmark.
It does not have all-prime coverage or an endogenous arithmetic source, and
it is not a counterexample to the conditional theorem. No negative or zero
state is added to improve a comparison. A/C are separate complete owners.

## 7. Control B — own full inverse, histories and all kernels

Write g(x)=x^2+x+3=(x+1/2)^2+11/4>1 and

    F(x,y)=(-x,g(x)y),
    M(x)=g(x)g(-x)=x^4+5x^2+9>=9.

The given inverse theta(X,Y)=(-X,Y/g(-X)) is a two-sided analytic inverse
on the ENTIRE real plane. Its denominator is positive everywhere. Direct
differentiation gives signed det DF(x,y)=-g(x), and hence

    J_B(X,Y)=1/g(-X), kappa_B(x,y)=log g(x)>0.             (15)

The positive finite all-point inverse derivative proves EVERY-Borel IMAGE
for its own dxdy by global change of variables. There is exactly one actual
predecessor at each depth; no source piece, root or y=0 stratum is omitted.
For EVERY integer r, the exact iterates are

    F^(2r)(x,y)=(x,M(x)^r y),
    F^(2r+1)(x,y)=(-x,g(x)M(x)^r y).                     (16)

These include all inverse histories. The absolute iterate Jacobians are
M(x)^r and g(x)M(x)^r respectively; differentiating the second coordinate
adds an off-diagonal term but does not change that determinant.
All groupoid arrows are (F^(-k)w,k,w). Write L_x=log M(x), gamma_x=log g(x).
For source w=(x,y) their complete range/clock formulas are

    k=2r:   z=(x,M(x)^(-r)y), c=r L_x;
    k=2r+1: z=(-x,M(x)^(-r)y/g(-x)), c=r L_x+gamma_(-x).  (17)

In particular k=-1 gives c=-gamma_x. Since both gamma_x and gamma_(-x)
are positive, c has the sign of k for every nonzero k. Therefore

    K_lag=K_c=K_joint=units on ALL of B.                  (18)

This is a full kernel conclusion, unlike A/C's nonunit zero-clock loci.

## 8. B's complete periodic/nonperiodic packets and every physical phase

F^2 fixes x and multiplies y by M(x)>1. A periodic source must have y=0.
On that line the only fixed source is (0,0); all pairs {(a,0),(-a,0)}, a>0,
have least source period two. These are all periodic points; bijectivity
implies that their full incoming sets contain only their own core points.
At (0,0), signed Delta=-3, C=log3, source isotropy Z, entire H=log3 Z,
extension isotropy trivial. Its complete phase is h mod log3; primitive log3
and repetitions n log3. The orientation sign in Delta does not alter H.

For a two-cycle set gamma_+=log g(a), gamma_-=log g(-a), L=log M(a).
The signed cycle product is M(a)>0, C=gamma_++gamma_-=L. Source isotropy
is 2Z, entire H=LZ, extension isotropy trivial. Its full phase can be written

    at (a,0): h mod L;
    at (-a,0): h+gamma_+ mod L.                           (19)

The actual forward arrow has clock -gamma_+, so (19) matches between the
positions. Each pair is ONE circle of primitive L, repetitions nL; no
individual step or half-cycle is a smaller source-loop clock. Their full
arrows/kernels are the restrictions of (17),(18), not selected representatives.

For y!=0 there is no eventual cycle. If x=0, the complete source components
have unique parameters eta in {+1,-1}, b in [1,3) and states

    (0,eta 3^n b), n in Z.                              (20)

If x!=0, set a=abs(x)>0, G_+=g(a), M=M(a). The complete source components
have unique parameters a>0, eta in {+1,-1}, b in [1,M), and states

    z_(2n)=(a,eta M^n b),
    z_(2n+1)=(-a,eta G_+ M^n b), n in Z.                 (21)

For a point on the negative-x side, first divide its y by G_+ to obtain
the positive-x section; normalize its absolute value by an integer power
of M. Uniqueness of the half-open normalized value proves both coverage
and nonduplication in (21). For (20) the same argument uses factor 3.
Both signs of y and the full x=0 line are retained. The half-open sections
do not delete a point, merge packets or claim a global smooth quotient.
All these components are bi-infinite; their incoming histories are precisely
(16). Source and extension isotropy and entire H are zero, even though every
local clock is positive. Each gives a free physical line whose full phase is

    h+log abs(y) in R, y!=0.                             (22)

Indeed (17) gives log abs(y_range)=log abs(y_source)-c, so (22) is invariant.
On (20) it is h+n log3+log b; on (21) it is
h+n log M+epsilon gamma_++log b at index 2n+epsilon. Equal values on the
same source component are sufficient for an extension arrow, by (17).
No positive primitive occurs on these nonperiodic lines. Equations (16)–(22)
exhaust EVERY source, history, arrow, kernel, isotropy and physical phase.

## 9. B's Galois probe versus its FULL target ledger

At x=(sqrt2,0), the actual least source period is q=2. The two factors
of the signed product are -(5+sqrt2) and -(5-sqrt2), so

    Delta=(5+sqrt2)(5-sqrt2)=23, entire H=log23 Z.         (23)

Both conjugates are admitted on the full plane and are the two positions
of this SAME cycle. S=Gamma, H_x={1}, L=Q(sqrt2) is cyclic degree2 and
2 divides q=2. There is one primitive log23 packet, not two conjugate
packets. The individual step clocks log(5+sqrt2), log(5-sqrt2) determine
the nontrivial phase offset in (19); neither is a source return clock.
No Galois action on their real logarithms or heights has been introduced.
The norm of the signed CYCLE product over K is 23^2, not that primitive.
The norm of a single signed step happens to equal this actual two-step
product because these particular factors are conjugate positions; this is
not a general permission to replace an actual orbit by a field norm.

The full B positive ledger is nevertheless much larger: one fixed log3
packet and, for EACH a>0, one two-cycle packet of primitive
log(a^4+5a^2+9). The multiplier M(a) is strictly increasing for a>0,
tends to 9 as a decreases to 0, and tends to infinity. Thus these two-cycle
primitives range over the entire interval (log9,infinity), with one packet
per such length. The limiting value log9 at a=0 is not a new two-cycle
primitive: there the source period is one and log9 is a repetition of log3.
At a=1 the actual two-cycle primitive is log15, with ENTIRE H=log15 Z,
so B FAILS prime-only. Its prime-valued packets are not duplicate packets
for one prime, but uniqueness does not repair the nonprime continuum.
The source ledger, not just its successful log23 probe, controls that verdict.

## 10. Bounded theorem, controls and freeze disposition

Established conditionally: complete own rational-germ inverse/IMAGE atlas;
full partial groupoid, incoming, kernels and height phases; actual signed
cycle products and admitted conjugate clocks; exact orbit/point stabilizers;
the cyclic L/F consequence without assuming L/Q normal; and the additional
cyclic L/Q, degree-divides-q necessity for a positive prime packet under
the stated global prime-uniqueness benchmark and ALL-conjugate admission.
The necessary implication includes Delta=+/-p OR +/-1/p, not just expansion.
The auxiliary K receives no unwarranted cyclicity or degree-divisibility claim.
No real Galois measure action or complete-basin isomorphism was constructed.

All three controls are complete own owners. A fails uniqueness with three
log2 packets, including its contracting fixed zero. B's admitted probe is
one phase-connected log23 packet but its full ledger fails prime-only.
C has one log2 packet and passes the stated necessary partial benchmark;
its excluded conjugate makes the theorem's admission hypothesis unavailable.
None has the required full arithmetic source/all-prime conclusion. Equal
times never merged packets, and nonperiodic/axis states were retained.

Portfolio: retain this CONDITIONAL FILTER / FORK; no arithmetic candidate
admission or unconditional rational-map no-go. Naturalness/PROVES_TOO_MUCH
remain future source obligations, not solved by these external controls.
Arithmetic T1 NOT PASSED; T3 NOT AUDITED; classical NOT APPLICABLE;
formal UNASSIGNED; B NOT INVOKED. No 439 result, operator, new round or
publication follows. Only this raw file is written; original card and CP1
remain unchanged. CP2/CP3 have NOT been performed and no author access occurred.
Root must FULLY read this frozen raw before a DISTINCT PAPER UNLOCK.

EOF — 438 independent card-only derivation complete; HOLD for manuscript unlock.
