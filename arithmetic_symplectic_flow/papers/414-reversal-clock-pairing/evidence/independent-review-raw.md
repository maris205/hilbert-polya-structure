# RCP01 — card-only independent raw derivation

Candidate `ANG-AUDIT-20260923-RCP01`; Paper414; batch410–414, round5/5.
Result: exact reversal pairing is established for the frozen full density-clock
class. That class cannot satisfy the stated nonempty prime/unique-packet target.
This is a conditional obstruction, not a universal arithmetic or Route theorem.

## 0. Release, access and method

Root released card-only mathematics after reading the complete78-line CP1.
Sole scientific input: the unchanged card, reread all82 lines through EOF.
candidate-card.md SHA256 99c06614e002221c8046483a2a2f5f48f8c67fd088f0fbe79abf5dc6c102d2ae — 82 lines.
scope-review.md SHA256 271d75545f79591d8d3e9b5438c12987aeea29f931604ceff12c46dbb10acc04 — 78 lines.
The previously fully read ARS/local instructions remain applicable. No author
manuscript, README, ledger, sibling,408, peer report or external source was read.
No scientific code, numerical search, auxiliary agent or Git operation was used.
Shell commands served only reading, existence checks and file receipts.
Method: exact density change of variables and chain rule; retained-lag groupoid
algebra; explicit all-point formulas and exhaustive orbit classification.
AI supplied derivation and drafting. Shared history and root's stated informal
design exposure are retained, not blind preregistration or independent evidence.
No model-family separation or human verification is certified; served model
identity/settings are not independently attested. Internal NOT_CALIBRATED.

## 1. Full owner, every-Borel IMAGE and signed iterates

For any C1 diffeomorphism A of M, its density Jacobian j_A is positive,
finite and continuous at EVERY point. In a local density a(x)|dx| it is
a(Ax)|det DA_x|/a(x), with the corresponding chart expression on the target.
The density formulation does not require an orientation. The chain rule is

    j_{AB}(z)=j_A(Bz)j_B(z),    j_{A^{-1}}(Az)=1/j_A(z).          (1)

Local change of variables, countable chart subdivision and disjointification
give mu(AE)=integral_E j_A dmu for every Borel E, including infinite measure.
Second countability supplies the countable covers; no exceptional points are
discarded. In particular the actual global inverse F^{-1} satisfies

    mu(F^{-1}E)=integral_E J(w)dmu(w),
    J(w)=j_{F^{-1}}(w)=1/j_F(F^{-1}w).                           (2)

This is an inverse IMAGE identity, not a pushforward density substituted for
the prescribed clock. Its null-point values are supplied by the differential
and density, not uniquely inferred from the measure identity alone.
The same argument gives the reversor's own IMAGE: since R^{-1}=R,
mu(RE)=integral_E j_R dmu and j_R(Rz)j_R(z)=1.

Write D_k(z)=log j_{F^k}(z) for ALL k in Z, D_0=0. Then

    D_{k+l}(z)=D_k(z)+D_l(F^k z),
    D_{-k}(F^k z)=-D_k(z).                                     (3)

For k>=0, D_k is the frozen forward sum S_k; for negative k it gives the
actual inverse-iterate clock. All iterates exist: there are no terminals.
Every inverse history is the unique word F^{-n}; no branch is selected away.

## 2. Entire source and extension groupoids

Invertibility reduces the frozen actual relation, without losing any lag, to

    G={(z,k,F^k z):z in M,k in Z},    c(z,k,F^k z)=D_k(z).        (4)

Indeed F^m z=F^n w iff w=F^{m-n}z. Every integer k has a nonnegative-depth
presentation. Formula (3) gives S_m(z)-S_n(w)=D_{m-n}(z), so the clock is
presentation-independent. For arrows (z,k,w),(w,l,u), their composite is
(z,k+l,u); (3) proves additivity. Inverse is (w,-k,z), with negative clock.
Arrows with different k remain distinct even when F has finite order.

The exact complete kernels are

    M_lag={all units (z,0,z)},
    K_clock={(z,k,F^k z):j_{F^k}(z)=1},
    K_clock intersect M_lag=M_lag.                              (5)

The extension retains every (z,h), h in R, with an arrow from (w,h) to
(z,h+D_k(z)). Its source transport w->F^{-k}w has the every-Borel IMAGE
density exp(-D_k(F^{-k}w)), by (1)–(2). No smooth quotient is asserted.

An aperiodic point has source isotropy0. A point on a least-q cycle O has
source isotropy qZ, c(nq)=nC_O, where C_O=sum_{z in O}kappa(z).
This sum is independent of the chosen cycle starting point. Invertibility
also proves there are no strictly preperiodic incoming points: F^m x in O
implies x=F^{-m}(F^m x) in O. All incoming states and negative histories are
still retained; a periodic component is exactly its q-point orbit.

Consequently the ENTIRE physical return group and extension isotropy are

    H_z=C_O Z on O,       extension isotropy={nq:nC_O=0};
    H_z={0} off cycles,  extension isotropy0 off cycles.          (6)

If C_O!=0 the positive primitive is |C_O| and all positive repetitions are
n|C_O|. If C_O=0, source and extension isotropy remain qZ, but no positive
height period exists. Aperiodic orbits likewise give free real-height lines.

For an explicit full phase coordinate choose b on a source orbit and write
z=F^n b. The arrow (b,n,z) goes FROM z TO b and has clock D_n(b). Hence

    phase(z,h)=[h+D_n(b)] in R/H_b.                             (7)

For an aperiodic orbit n is unique. On a q-cycle another choice differs by
q times an integer, changing (7) by C_O times that integer. This realizes
each entire extended component as R/H_b, with all height translations.
It neither picks a single phase nor claims a global measurable transversal.

## 3. The reversor: actual arrow sign and height involution

From RFR=F^{-1}, one obtains F^{-k}R=RF^k for every integer k. Thus the
object map R induces the groupoid automorphism

    Theta(z,k,w)=(Rz,-k,Rw).                                   (8)

It preserves the source/range convention: the new arrow goes FROM Rw TO Rz.
It does not interchange source and range and is not groupoid inversion.
Composition is preserved because -(k+l)=(-k)+(-l); Theta squared is identity.

Put rho=log j_R. Equation (1) and R squared=id give rho(Rz)=-rho(z).
Differentiating F^{-k}R=RF^k in the density sense gives

    j_{F^{-k}}(Rz) j_R(z)=j_R(F^k z) j_{F^k}(z),
    c(Theta g)=c(g)+rho(w)-rho(z).                              (9)

This is NOT an unconditional formula -c(g). Even when rho=0, it reads
c(Theta g)=c(g), despite the integer lag changing sign.
The density supplies a specific compatible lift, which we now construct:

    R_hat(z,h)=(Rz,h-rho(z)).                                  (10)

An original arrow (w,h)->(z,h+c) maps to endpoints (Rw,h-rho(w)) and
(Rz,h+c-rho(z)). Their height difference is exactly the right side of (9).
Hence (10) acts on the full extension and descends to its orbit SET.
Moreover R_hat squared(z,h)=(z,h-rho(z)-rho(Rz))=(z,h). It is an actual
involution, and it COMMUTES with all height translations h->h+t. Base
time reversal is therefore not physical-height time reversal for this clock.
No h->-h rule is imposed. This is a constructed density lift; no uniqueness
among arbitrary orbit-dependent height gauges is claimed.

Theta preserves M_lag and the unit intersection in (5). Its exact clock-kernel
image is {g=(z,k,w):c(g)=rho(z)-rho(w)}, by applying (9) to Theta inverse.
For g in K_clock its new clock is rho(w)-rho(z), so preservation of K_clock
requires that endpoint difference to vanish on all its arrows; it is not an
assumption here. The compatible height shift compensates this term. On an isotropy
arrow w=z the term cancels, so Theta preserves the loop's clock value while
negating its lag. This observation is what controls entire H, not a presumed
arrowwise clock sign. All three controls below have rho=0, so their K is preserved.

## 4. Signed cycle pairing, multiplicity and the conditional obstruction

If O is a least-q cycle, R(O) is another least-q cycle, with its cyclic order
reversed. The equality of least periods follows in both directions from (8).
At z in O apply (9) to (z,q,z). It has clock C_O; its image is
(Rz,-q,Rz), whose clock by (3) is -C_{R(O)}. Therefore

    C_{R(O)}=-C_O,    H_{Rz}=H_z=C_O Z.                         (11)

The extension-isotropy groups obey the same zero/nonzero test; the underlying
source lag map is k->-k, not deletion of ineffective isotropy.

There are exactly two possibilities for the reversal permutation of cycles:
(i) R(O)=O, which forces C_O=0; or (ii) two distinct cycles O,R(O).
In case(ii) either both clocks are zero, or their clocks are nonzero opposites.
The latter pair gives TWO distinct physical packets with the SAME primitive
|C_O|, each with all its repetitions. Distinct F orbits have no G arrow
between them. R_hat exchanging the packets does not identify them: R is
not an additional generator of the frozen source equivalence relation.

Self-reversal is not pointwise fixation. If Rb=F^s b on a self-reversed
q-cycle, then R(F^j b)=F^{s-j}b. Fixed vertices solve 2j=s modulo q:
there is one when q is odd, two when q is even and s even, and none when
q is even and s odd. In every such case the whole cycle clock is still0.

With reference b on O and Rb on R(O), (7), (9) and (10) show that the
paired phase map is [u]->[u-rho(b)]. Its square is identity because
rho(Rb)=-rho(b). In particular it preserves the direction of height time.
On a self-reversed source component H=0 (for periodic components by (11),
for aperiodic ones by (6)). Its quotient is R; a height-commuting involution
there is a translation whose square is identity, hence the identity. Source
isotropy may still be inverted by Theta; this does not create a positive period.

It follows that the FULL positive-packet set carries a fixed-point-free
involution preserving primitive time. Every finite nonempty fibre of a given
primitive time has even multiplicity; infinite fibres remain paired, without
an inappropriate finite count assertion. Nonempty prime-only support plus
at-most-one actual packet per prime is impossible: any such positive packet
has its distinct partner at the same log p. If there is no positive packet,
the nonempty requirement fails instead. Thus EVERY owner in the frozen
reversible full-density-clock class fails the combined necessary benchmark.
This does not require or establish all-prime coverage. It is not a theorem
about other clocks, partial/noninvertible/nonreversible maps or a quotient
that additionally identifies R partners; those change the hypotheses/owner.

## 5. Control A — full plane, zero density clock

F(x,y)=(2x,y/2), F^{-1}(x,y)=(x/2,2y), R(x,y)=(y,x).
Both maps are global smooth diffeomorphisms, R squared=id, and direct
composition gives RFR=F^{-1}. With its own Lebesgue AREA density, j_F=1
and j_R=1 at every point, including the origin. Thus J=1, kappa=rho=0.
Linear change of variables proves every-Borel inverse IMAGE, without a
distinguished-axis restriction. An expanding eigenvalue is not this clock.

The complete relation and kernels are

    G_A={((x,y),k,(2^k x,2^{-k}y)): (x,y) in R^2,k in Z},
    c_A=0,   K_A=G_A,   M_A=K_A intersect M_A=units.              (12)

The only periodic point is (0,0), fixed: for q>0 either nonzero coordinate
would require 2^q=1. At the origin source and extension isotropy are Z;
elsewhere both are0. ENTIRE H is0 at EVERY point. There are no positive
physical packets. The full origin component is retained as a zero-clock
source cycle with all real heights, not an omitted exception.

Every nonzero source component is the whole bi-infinite orbit in (12),
with its unique inverse histories and no strict preperiodic additions.
For completeness, if x!=0 let n=floor(log_2|x|), a=2^{-n}x and b=2^n y;
then z=F^n(a,b), with 1<=|a|<2. If x=0,y!=0, put m=floor(log_2|y|)
and b=2^{-m}y; then z=F^{-m}(0,b), with 1<=|b|<2. These disjoint cases
parametrize all nonzero orbits. All their real phases are simply h, since c=0.
The full extended orbit SET is (R^2/F^Z) times R, with free height translation.

Here R_hat(x,y,h)=(y,x,h). The origin cycle is self-reversed. An aperiodic
orbit is self-reversed precisely when y=2^k x for some integer k with x,y
nonzero; otherwise R exchanges distinct orbits. Nonzero coordinate axes are
exchanged, not dropped. This criterion follows by solving Rz=F^k z in (12).
Every quotient phase h is retained. The prime benchmark fails nonemptiness.

## 6. Control B — full projective line and opposite signed fixed clocks

Use both charts t=tan(theta) and s=1/t at infinity. The fixed round density
is |dt|/(1+t^2) on the t chart and |ds|/(1+s^2) on the s chart.
F is t->2t, equivalently s->s/2 near infinity; F^{-1} is t->t/2,
equivalently s->2s. R is t->1/t, globally theta->pi/2-theta modulo pi.
It is a round isometry, exchanging0 and infinity, with R squared=id and
RFR=F^{-1}. These are smooth global projective maps, not affine restrictions.

Direct density change of variables gives the EVERY-point formulas

    j_F(t)=2(1+t^2)/(1+4t^2),       j_F(infinity)=1/2,
    J(w)=2(1+w^2)/(4+w^2),         J(infinity)=2,
    kappa(t)=log j_F(t),           rho=0 everywhere.             (13)

For example in the s chart j_F(s)=(1/2)(1+s^2)/(1+s^2/4), including s=0.
The inverse s map has derivative2 at0. For R the coordinate/density factors
cancel exactly, so j_R=1 also at0 and infinity by the complementary charts.
The local formulas and global one-to-one changes of variable prove inverse
IMAGE for EVERY Borel subset of RP1. Null fixed-point values are prescribed
by these derivatives, not by deleting points from the measure law.

For every integer k and finite t, write

    D_k(t)=k log2+log(1+t^2)-log(1+2^{2k}t^2),
    D_k(infinity)=-k log2.                                      (14)

These are the logs of the actual iterate density Jacobians. The FULL
groupoid consists of (t,k,2^k t) for finite t, and (infinity,k,infinity),
all k in Z, with clock (14). Its lag kernel is units. Solving D_k=0 gives
the entire clock kernel: all units, together with

    (epsilon 2^{-k/2}, k, epsilon 2^{k/2}),
    epsilon=+1 or -1, k in Z excluding0.                         (15)

Indeed putting a=2^k in j_{F^k}(t)=1 yields (a-1)(1-a t^2)=0.
There are no further nonunit zero-clock arrows at0 or infinity. Thus
K_B intersect M_B=units, even though K_B itself is not only units.

The COMPLETE periodic set is {0,infinity}, each fixed; no nonzero finite t
can solve 2^q t=t for q>0. Their source isotropies are Z, their clocks are
C_0=log2 and C_infinity=-log2, and their extension isotropies are0. Each
whole incoming component is its singleton core. ENTIRE H at BOTH points is
log2 Z: there are exactly TWO distinct positive packets, primitive log2,
with all phases h modulo log2 and repetitions n log2. They are paired by
R_hat(t,h)=(1/t,h), with the0/infinity convention, and not merged by G_B.

Every other point has source/extension isotropy0 and H0. Its entire component
is {2^n v:n in Z}, for finite v!=0. Choose v=epsilon u, 1<=u<2, and
t=2^n v. The arrow (v,n,t) goes FROM t TO v, so the full real phase is

    h+D_n(v)=h+n log2+log(1+u^2)-log(1+t^2).                     (16)

This includes both signs and every height; asymptotic approach to a fixed
point is not finite incoming membership. R acts on all these components by
t->1/t. With paired references v and Rv, (9) shows the same real phase is
carried to the paired component because rho=0. The self-reversed aperiodic
components are exactly those satisfying t^2 in 2^Z; equivalently normalized
u is1 or sqrt2, for either sign. Their quotient phase action is identity;
the remaining components are exchanged in distinct pairs. Formula (10)
on actual points gives the full action, regardless of phase normalization.

This control satisfies prime-only positive support but FAILS uniqueness at2,
and gives no all-prime coverage. Removing infinity would remove one packet
and break the global reversor; replacing the round density by affine length
would also change the owner. Neither is an admissible repair here.

## 7. Control C — every source point periodic, no positive height period

On the ENTIRE circle theta modulo2pi, F(theta)=theta+pi and
R(theta)=-theta. Both preserve the length density; j_F=j_R=J=1 and
kappa=rho=0 at every point, including chart wraps. Rotational/reflection
change of variables proves their every-Borel IMAGE laws. R squared=id and
RFR(theta)=theta-pi=F^{-1}(theta). F is its own inverse, but the retained
lag groupoid is still indexed by Z, not a quotient finite two-element group.

    G_C={(theta,k,theta+k pi mod2pi):theta in circle,k in Z},
    c_C=0,   K_C=G_C,   M_C=K_C intersect M_C=units.              (17)

EVERY point has least source period2: theta+pi is never theta modulo2pi.
Its entire source component is {theta,theta+pi}, with all unique alternating
inverse histories. Source and extension isotropy are2Z at every point;
ENTIRE H is0 everywhere. There are no positive physical packets, although
there is a continuum of zero-clock source cycles. The full extended orbit
SET is (R/(pi Z)) times R, with phase h and free real-height translation.

R_hat(theta,h)=(-theta,h). The source cycle labelled by theta modulo pi
is sent to the one labelled by -theta modulo pi. Self-reversal occurs
exactly when 2theta=0 modulo pi, giving precisely TWO self-reversed cycles:
{0,pi} and {pi/2,3pi/2}. In the first R fixes the vertices; in the second
it exchanges them. All other cycles are paired distinctly. All have signed
cycle clock0, so this continuum does not produce even one positive period.
The necessary benchmark fails nonemptiness, with no point or phase removed.

## 8. Bounded conclusion and hold

The full density-Jacobian reversal theorem and all three own control ledgers
are closed: every-Borel inverse IMAGE, all-point clocks, actual arrows,
height involution, kernels/intersection, all source/extension isotropy, H,
incoming histories and phases are supplied without a cutoff or numerical scan.
The nonempty/unique-prime necessary target is obstructed for THIS reversible
global full-density-clock class by paired nonzero cycle clocks, not by an
unsupported claim that reversal always negates the clock of an arrow.

The source lineage remains conditional on a separately admitted reversible
geometric realization. No generic control supplies endogenous arithmetic,
strong naturalness, all-prime coverage, a trace/operator or Route credit.
Nonreversible, partial/noninvertible and other-clock owners are not ruled out;
identifying R partners would be a new owner, not a change of this ledger.
Classical NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.
Portfolio: STOP this class against the frozen necessary target; any later
fork requires separate authority. No round415 or new research is authorized.
Freeze raw, preserve CP1, and HOLD for root's full read and a separate
PAPER UNLOCK. No author or sibling surface may be read beforehand.

EOF — card-only independent raw; AI-assisted, shared-history NOT_CALIBRATED.
