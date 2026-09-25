# PPA01 — card-only independent raw proof

Candidate `ANG-AUDIT-20260922-PPA01`; Paper398, round4/5 of
`GEOMETRIC-FEEDBACK-20260922-J`. Reviewer `/root/nonlocal_source_review`.
2026-09-22. Root read CP1 and explicitly released this derivation.
candidate-card.md SHA256 91999304e936a18fcaac26324828d0635014dabb78fc553ea9c54ed5fd24cbb6
scope-review.md SHA256 63fbefbe787f62715280e62a10fca89317d4a99b28e56b4141ef5cd0f221d7b6
Input is the complete frozen72-line card, reread before deriving below.
No398 manuscript, peer proof or other new scientific output was read.
Prior shared history and the recovery-summary exposure disclosed in CP1
remain: internal same-family NOT_CALIBRATED, not blind or external review.
All mathematics needed below is derived here, not transferred from393/394.

## 1. Full round-density IMAGE and the actual branch clock

For any real invertible3-by-3 matrix A write delta=abs(det A)>0.
Let f_A(u)=Au/||Au|| on the unit sphere S2. If E is a Borel sphere set,
the preimage under A of the unit-radius cone over f_A(E) consists of
ru with u in E and 0<r<1/||Au||. Polar volume and linear change of variables
give sigma(f_A(E))/3=(delta/3) integral_E ||Au||^(-3) d sigma(u).
Thus its sphere-area IMAGE density is delta/||Au||^3 everywhere: the
smooth pointwise Jacobian agrees with this density, first a.e., then
everywhere by continuity and the full support of sphere area.
Antipodal equivariance descends the identity to the round density m on RP2:

    J_A([v]) = delta ||v||^3 / ||Av||^3,
    m(F_A E) = integral_E J_A dm                         (1)

for EVERY Borel E. The double-cover factor cancels. This is a density,
not an oriented global volume form. The expression is invariant under
nonzero representative scaling; scalar matrix scaling also cancels.
Direct norm cancellation proves J_(AB)(x)=J_A(F_B x) J_B(x).
Consequently all positive and negative integer powers have their own (1).

For each frozen P_i, T(P_i) is Borel since F_(A_i) is a diffeomorphism.
Every Borel E subset T(P_i) satisfies m(I_i E)=integral_E J_(A_i) dm.
Restriction does not alter its frozen all-point smooth-extension version.
Hence kappa(x)=-log J_(A_i)(Tx) is defined at every x in P_i, including
its assigned boundary. Overlap of different inverse domains permits
different actual inverse branches, not ambiguity in the forward owner.
No kappa is supplied at a terminal. Empty sums and the empty matrix are0,I.

If x has a valid k-step word i0,...,i(k-1), put
P_k(x)=A_i0 ... A_i(k-1), in that order. Then

    T^k x = F_(P_k(x))^(-1) x,
    S_k(x) = -log J_(P_k(x))(T^k x).                    (2)

This follows by the product law, with no content reduction or new clock.
Signed step clocks need not be positive return times.

## 2. Full actual groupoid, kernels, histories and return group

Write g=(z,n,w), witnessed by valid k,l>=0 with n=k-l and
T^k z=T^l w. Another witness for the same triple has k'=k+d,l'=l+d.
For d>=0 the two added sums start at the same actual common point and
cancel. Reverse the comparison for d<0. Therefore
c(g)=S_k(z)-S_l(w) is witness independent, including terminal histories.
Inversion swaps k,l and endpoints and negates c. To compose two arrows,
align their two forward times at the shared endpoint at their maximum;
that iterate is valid because both given iterates are valid. This yields
the endpoint triple with summed lag, and cancellation proves additivity.
Thus the card's equal-triple identification and all integer lags are valid.

All incoming histories at w are precisely these legal witnesses: choose
a valid l at w, and any legal finite inverse word of length k landing at
T^l w. Nothing licenses an inverse word outside its actual domain.
Let u=T^k z=T^l w, P=P_k(z), Q=P_l(w), and take v representing u. Then

    c(g)=log(J_Q(u)/J_P(u))
        =3 log(||Pv||/||Qv||)-log(abs(det P)/abs(det Q)). (3)

This describes the full clock kernel by J_P(u)=J_Q(u).
The full lag kernel consists of all (z,0,w) with T^k z=T^k w for some
valid k. Its intersection with the clock kernel additionally requires
S_k(z)=S_k(w). These are necessary and sufficient conditions, with every
legal word and boundary included. For a noninjective owner, the lag kernel
need NOT be units; no invertible-control property is transferred to it.

Let I_x denote source isotropy expressed as a subgroup of integer lags.
A nonzero isotropy arrow implies that some forward tail is periodic.
If x is not eventually periodic, I_x={0}; this includes terminal tails.
If T^m x reaches a cycle of least period q, every isotropy lag is a
multiple of q, and witnesses (m+q,m) and their powers give all qZ.
Writing C for the sum around that least cycle, cyclic shifts preserve C,
and (2) gives c(x,nq,x)=nC. Therefore the ENTIRE ledger is

    eventual least period q: I_x=qZ, H_x=CZ,
      extension isotropy={nq:nC=0};
    not eventually periodic: I_x={0}, H_x={0},
      extension isotropy={0}.                          (4)

In particular C!=0 gives trivial extension isotropy and least physical
period L=abs(C). C=0 gives H={0}, not H=R and not a positive period,
while the full source isotropy survives upstairs.

The R-translation action on extension orbit classes is well-defined since
it commutes with every arrow. Its stabilizer at [(x,h)] is exactly H_x:
a translation identifies (x,h) with (x,h+t) exactly when an isotropy arrow
has clock t. Fix a source orbit and anchor x. For g:x->z its full phase
coordinate is h-c(g) modulo H_x; different choices of g differ by H_x.
Thus there is ONE transitive physical R/H_x orbit per entire source orbit,
including all incoming trees and all real heights. Distinct source orbits
with equal L are different packets. No quotient-manifold regularity follows.
Distinct periodic cycles cannot be joined by incoming histories: a common
forward tail would force those deterministic cycles to be the same cycle.

## 3. Interior-cycle arithmetic and the rational eigenspace alternative

Take the tested point p with least source period q and its frozen legal
q-step open neighborhood. Put M=A_i0 ... A_i(q-1) in the exact order (2).
For a representative v of p, Mv=lambda v, with lambda real and nonzero.
The full two-dimensional round-volume cycle clock is

    C=log(abs(lambda)^3 / abs(det M)).                  (5)

Assume C!=0 and r=exp(abs(C)) is rational. Then exp(C) is r or1/r,
so abs(lambda)^3, and hence lambda^3, is rational.
If lambda were irrational, t^3-lambda^3 would be irreducible over Q:
a reducible rational cubic has a rational root, and its unique real root
is lambda. The minimal polynomial would therefore have degree3 and equal
the characteristic polynomial of M. It follows that det M=lambda^3,
contradicting C!=0 in (5). Therefore lambda is rational.

Now E=ker(M-lambda I) is a rational linear subspace. If dim E=1 it has
a nonzero rational generator, making p rational, contrary to hypothesis.
Thus dim E>=2. Dimension3 would make M scalar and C=0, so dim E=2.
For completeness the characteristic polynomial is
(t-lambda)^2(t-mu), with mu rational and nonzero. Equation(5) becomes
C=log(abs(lambda)/abs(mu)), and its nonzero value excludes abs(mu)=abs(lambda).
This also excludes a size2 Jordan block with all eigenvalues lambda.
The relevant continuum is therefore the rational eigenspace's PROJECTIVE
LINE, not a family of irrational eigenvalues and not the whole RP2.
Every point of P(E) has the same full ambient cycle Jacobian and C.
No induced one-dimensional density on P(E) has been substituted for m.

## 4. From the eigenline continuum to distinct least-period packets

On the frozen q-step neighborhood, each partial iterate T^j, 0<=j<=q,
agrees with one smooth projective composition. Since T^j p!=p for
1<=j<q, continuity permits a smaller open neighborhood W of p such that
T^j(W) is disjoint from W for every such j. One can choose disjoint
neighborhoods of p and each T^j p and intersect their finite inverse images.
Keep W inside the given legal-itinerary neighborhood.

For every y in P(E) intersect W, T^q y=y, its q-step itinerary is legal,
and those disjointness conditions exclude every shorter period. Repeating
the itinerary remains legal because it returns to y. Every such y has
least period q and cycle clock C. Equations(4) give its complete source
isotropy qZ, trivial extension isotropy, H=CZ and L=abs(C)>0.

If two different such y were on the same source q-cycle, one would be
T^j of the other for 1<=j<q, contradicting disjointness. They also cannot
merge via incoming histories by the last paragraph of Section2. Every
open neighborhood V of p contained in W meets P(E) in a real arc and
hence in continuum many points; after removing its countably many rational
points, continuum many irrational ones remain. These provide continuum
many DISTINCT primitive packets with the SAME full H and the same L.
All phases of each packet and all repetitions nC are retained.

This answers the card's conditional question positively. It does not
promote a selected irrational point to a unique arithmetic orbit.
No such neighborhood proof is available merely from a boundary-only
itinerary. Boundary points remain in (1)–(4); the conclusion is not asserted
for them without the full stated neighborhood. Other dimensions, densities
and nonprojective maps are not covered by this theorem.

## 5. Global invertible control convention

For each control, T=F_A^(-1) on its OWN full RP2. All arrows are
(F_A^n w,n,w), n in Z; different integer lags are never collapsed.
Their complete clock, with v representing w, is

    c_n(w)=3 log(||A^n v||/||v||)-n log(abs(det A)),
    J_(A^n)(w)=exp(-c_n(w)).                            (6)

Each satisfies (1) on EVERY Borel set for every n. All incoming points are
exactly F_A^Z w, with every indicated arrow; no extra predecessor branch
exists. Lag kernel and its intersection with the clock kernel are units.
Equations(4) and the phase formula in Section2 give every height, including
when multiple lags have identical endpoint maps. The following lists also
give the complete clock kernels and all source orbit classes explicitly.

## 6. S: scalar control

A=2I3, abs(det A)=8, and A^n=2^n I3 for all integer n. Thus J_(A^n)=1
and c_n=0 everywhere. Every projective point is fixed; there is no
nonperiodic complement. Each has source isotropy Z, extension isotropy Z
and H={0}. The clock kernel is the whole groupoid, while the lag kernel
and the intersection are units. Every source point is a separate source
orbit and owns one physical phase line R. There are continuum many such
lines and NO positive primitive packet. Irrational fixed points exist,
but the theorem's nonzero-clock hypothesis fails.

## 7. D: the continuum positive-packet control

A=diag(2,1,1), abs(det A)=2. Put v=(s,u,t), a=s^2, b=u^2+t^2.
Then ||A^n v||^2=4^n a+b and, for every integer n,

    J_(A^n)=2^n ((a+b)/(4^n a+b))^(3/2),
    c_n=(3/2)log((4^n a+b)/(a+b))-n log2.               (7)

The fixed set is exactly e=[1:0:0] plus the full line Q={s=0}.
For a,b both positive, projective periodicity would force 2^n=1 for
some n!=0, which is impossible. Thus all and only those mixed points are
nonperiodic; no other periods or eventually periodic points occur.

At e the clock c_n=n log4, source isotropy is Z, extension isotropy is0,
H=(log4)Z and there is ONE primitive physical packet of least time log4.
At EACH point of Q the clock is -n log2, source isotropy is Z, extension
isotropy is0 and H=(log2)Z. The entire Q therefore contributes continuum
many DISTINCT primitive log2 packets. The log4 packet is not identified
with a repetition of a different log2 source orbit.
Each mixed orbit is exactly {[2^n s:u:t]:n in Z}; its two isotropies are0,
H={0}, and its physical orbit is a full phase line R. There are continuum
many mixed source orbits, for example distinguished by the direction [u:t].

For n!=0 set r_n=2^(2n/3)>0. Equation c_n=0 is equivalent to
4^n a+b=r_n(a+b). Since 4^n=r_n^3 and r_n!=1, the EXACT locus is

    b=r_n(r_n+1)a.                                    (8)

Both a,b must be positive at any projective point on (8). These are all
nonunit zero-clock arrows and all lie on mixed source orbits; n=0 gives
all units. The formula includes both signs of n and every coordinate
boundary. All incoming points, full heights and circle/line phases are as
in Section5. The irrational points of Q have rational eigenvalue1 in a
two-dimensional rational eigenspace and realize the continuum conclusion.

## 8. C: irrational eigenvalue with zero cycle clock

A sends (s,t,u) to (2u,s,t), abs(det A)=2, and A^3=2I3.
Let alpha be the positive real cube root of2; it is irrational because
t^3-2 has no rational root. The only real eigenline is
e=[alpha^2:alpha:1], with eigenvalue alpha. These assertions follow directly
from (2u,s,t)=lambda(s,t,u), which forces lambda^3=2 and u!=0.
Thus e is the unique fixed projective point. Since F_A^3 is identity,
EVERY other point has least period3; there is no nonperiodic complement.

Put a=s^2,b=t^2,d=u^2, Q0=a+b+d, Q1=a+b+4d, Q2=a+4b+4d.
For every n=3m+r with m in Z and r in {0,1,2}, equation(6) becomes

    J_(A^(3m))=1,                  c_(3m)=0;
    J_(A^(3m+1))=2(Q0/Q1)^(3/2), c_(3m+1)=(3/2)log(Q1/Q0)-log2;
    J_(A^(3m+2))=4(Q0/Q2)^(3/2), c_(3m+2)=(3/2)log(Q2/Q0)-log4. (9)

Euclidean division covers negative as well as positive n. Hence the
COMPLETE clock kernel consists of all lags divisible by3, together with

    n=1 mod3: Q1=alpha^2 Q0,
    n=2 mod3: Q2=alpha^4 Q0.                           (10)

Equivalently (4-alpha^2)d=(alpha^2-1)(a+b), and
(4-alpha^4)(b+d)=(alpha^4-1)a, respectively. Their coefficients are
positive on both sides; these full projective quadrics contain many
nonfixed points, not just e. For example setting b=0 in the first relation
allows a,d>0 and gives a zero-clock nonisotropy arrow. No coordinate locus
or nonfixed three-cycle is removed. Lag kernel/intersection remain units.

At e all clocks c_n vanish, so source and extension isotropy are Z and
H={0}. Elsewhere source and extension isotropy are3Z and H={0}, because
the three-step sum vanishes. Each complete three-cycle is one source orbit,
not three packets, and owns one phase line R; e owns another phase line.
There are continuum many three-cycle source orbits, each of size3. There
are NO positive primitive physical packets anywhere on this control.
The single-step clock is not identically zero: (9) at [1:0:0] gives
c_1=-log2. Individual signed steps must not be mistaken for a cycle time.
All actual histories are the full finite source cycles with all integer
lags retained; (9) and Section2 preserve all phases and repetitions.
This control shows why the nonzero-cycle premise is essential even at an
irrational point with a full smooth legal neighborhood.

## 9. Scope and frozen handoff

The conditional interior theorem and all three full-owner ledgers above
use the exact frozen round-density clock. They supply no endogenous prime
source, main-candidate admission, uniqueness of an arithmetic packet,
minimum-dimension theorem, boundary-only theorem or novelty assertion.
S/D/C are external coefficient controls; no selected invariant subspace
has replaced any of their full carriers or volume owners. No countability
or discreteness of the full physical primitive ledger was imposed.
Classical NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.
This raw proof precedes manuscript access; CP2/CP3 are not yet performed.
No scientific numerical run, external search, Git write or publication.

EOF — independent raw complete; freeze bytes and await PAPER UNLOCK.
