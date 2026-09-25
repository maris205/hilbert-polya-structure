# DIS01 — independent card-bound raw derivation

Candidate: ANG-20260925-DIS01. Paper468.
Reviewer: `/root/rcr01_independent_review`, 2026-09-25 UTC.
Stage: DISTINCT RAW RELEASE, before any current manuscript access.

## 0. Input, exposure and scope

Scientific input is the unchanged candidate-card.md, FULL read again at
1–121/EOF in this RAW stage. Frozen SHA-256:
`fc36a5a9d68b245feb00f6da52a9d568122bfb9352cbe0f27e6ca0e7fb6bd10e`.
Root reported FULL reading the166-line CP1 report and issued the separate
RAW release. CP1 SHA was
`f3560c9b47bd6b846ca53b025c4372b132dba234d66c39a911bdea035c56a2c6`.
ARS/local instructions were personally refreshed during this same468
checkpoint sequence; the bounded original-mathematics adaptation continues.

The CP1 read of root readme.md1–36 exposed prior W/V outcome summaries;
that deviation was disclosed and root explicitly accepted its preservation,
not a retrospective blind/card-only provenance claim. Shared model/root
history and the card's disclosed scout/author design exposures remain.
NOT_CALIBRATED: no human, external, blind, cross-model or independent-error
verification claim. No further old outcomes/proofs, current author surfaces,
peer/helper proof or sibling scientific material was read at RAW stage.

All work below is exact symbolic reasoning, with no scientific program,
numerical census, literature/network call, Git mutation or PDF. Only this
raw file is written. No period-two/higher census or Paper470 is undertaken.
The generic history formulas cover the whole frozen owner; they do not
constitute an enumeration of its as-yet unclassified higher-period cores.

## 1. Four actual partial owners and their analytic germs

Write o=M,C,R,I for the four owners. For z=(x,y), set
A=1+floor(abs x), B=1+floor(abs y), g=gcd(A,B),
r=A-B floor(A/B). A,B are positive integers and 0<=r<B.
For each owner use exactly its card coefficient triple:

| Owner | G | R | H |
|---|---|---|---|
| M | g | r | g |
| C | 1 | r | 1 |
| R | g | 0 | g |
| I | g | r | 0 |

The capital R in formulas is the denominator coefficient, not a borrowed
remainder from another trajectory. Each owner rereads its own state.
On one assigned cell put
D=x^2+xy+y^2-R, N=xy(x+y)+G,
f=N/D+H(x-y), F(x,y)=(y,f).
The Borel cell partition can be made literally disjoint by specifying A,B
and sign(x),sign(y) in {-1,0,1}; zero signs are permitted only for the
corresponding readout1. This covers every axis and endpoint with the stated
floor convention. G,R,H are constant on each such piece.

Differentiation always means this cell's ambient analytic extension, not
a derivative of the discontinuous readout function across a boundary.
Since N_x=y(2x+y) and D_x=2x+y, direct subtraction gives

    (N/D)_x = (2x+y)(y^3-Ry-G)/D^2.

Similarly (N/D)_y=(x+2y)(x^3-Rx-G)/D^2. Define

    L_o(z) = H+(2x+y)(y^3-Ry-G)/D^2,
    K_o(z) = H D^2+(2x+y)(y^3-Ry-G).

The assigned Jacobian is

    DF = [[0,1],
          [L_o,(x+2y)(x^3-Rx-G)/D^2-H]],
    det DF = -L_o = -K_o/D^2.                         (1)

Thus the exact legal source is

    E_o = {z: D_o(z)!=0 and K_o(z)!=0}.              (2)

All coefficients in (2) are read at z. Its complement Z_o consists of
terminal objects, with no assigned outgoing step. It is not removed from
X=R2, and it is not replaced by an identity-map continuation. Both E_o and
Z_o are Borel, and F_o:E_o->X is Borel by the countable cell partition.
All four measured spaces remain original two-dimensional Lebesgue area.

## 2. Exhaustive one-step inverses, including degenerate polynomials

For any target t=(u,v), enumerate every source cell with its own owner's
G,R,H and retain ALL real roots of

    Q(x)=(v-H(x-u))(x^2+xu+u^2-R)-xu(x+u)-G.        (3)

For each proposed z=(x,u), test its actual A,B, signed-cell membership,
D!=0, K_o!=0 and F_o(z)=t. Deduplicate equal z only. Denote the resulting
set by P_o(t). There is no test requiring t itself to be in E_o.

If z is a genuine legal predecessor then its actual cell occurs in the
enumeration, its first image coordinate forces y=u, and multiplication
of the second-coordinate equality by its nonzero D yields (3). Thus it
is retained. Conversely every retained root is explicitly legal and has
forward image t. Therefore

    P_o(t)={z in E_o:F_o(z)=t}                      (4)

at EVERY t, including terminal targets and null faces.

For M,C,R, H is a positive integer, so (3) has degree exactly3, with leading
coefficient -H. For I it becomes

    Q(x)=(v-u)(x^2+ux)+v(u^2-R)-G.                 (5)

If v!=u this is quadratic. If v=u it is the constant u^3-Ru-G.
A nonzero constant has no roots. If this constant vanishes, Q is identically
zero, but every denominator-legal proposed source then has L_I=0 by (1),
and is removed by the actual regularity guard. No arbitrary representative
of that continuum is retained. This treats the full degree collapse rather
than dividing by v-u or assuming a quadratic at every target.

More generally differentiation of (3) at a root with D!=0 gives

    Q'(x)=-D L_o(x,u).                              (6)

Indeed at a root v-H(x-u)=N/D; substituting this into Q' yields (6).
Thus every retained root is simple; repeated roots fail the regularity
test. This is an independent check, not a replacement for that test.
There are at most3 retained roots per cell for M,C,R and at most2 for I.
Consequently (4) is countable, although no uniform bound on the full set
of predecessors across all source cells is asserted or needed.

## 3. Prescribed countable atlas and every-Borel IMAGE

For each signed cell C, let Omega_C be the ambient open set on which its
fixed-coefficient analytic map has D!=0 and K!=0. At each point of
C intersect Omega_C the analytic inverse-function theorem provides an
open neighbourhood on which that analytic map is a diffeomorphism.

Fix an enumeration of all rational-centred, positive-rational-radius balls
U whose closure lies inside Omega_C and on which this analytic map is
injective. The image of such a ball is open and its inverse is analytic.
These balls cover Omega_C: a sufficiently small ball of this kind contains
any prescribed point within an inverse-function neighbourhood. The exact
injectivity predicate defines the enumeration; no finite algorithm for
certifying every such ball is being claimed. All cells and balls together
form the card's countable rational-ball atlas.

Enumerate the pairs as (C_j,U_j), and first-eligible disjointize:

    V_j=C_j intersect U_j,
    P_j=V_j minus union_{i<j} V_i,
    B_j=F_o(P_j).

The P_j are disjoint Borel sets covering E_o. The assigned analytic
diffeomorphism on U_j maps P_j bijectively onto B_j. The latter is Borel
because a homeomorphism maps Borel subsets of U_j to Borel subsets of its
open image. Let theta_j:B_j->P_j be the restricted analytic inverse.
It is Borel and F_o|P_j is its Borel inverse. The SOURCE pieces P_j
partition the legal source; the inverse target domains B_j may overlap.
Different predecessors of the same target must not be collapsed because
their inverse target domains overlap.

At every t in B_j, the actual analytic inverse determinant is

    J_j(t)=abs(det Dtheta_j(t))
          =1/abs L_o(theta_j(t))>0, finite.         (7)

The derivative is that of the ambient analytic inverse, even if t lies
on a null image of a cell face. If two atlas germs represent the same
actual source, its unique assigned cell law has the same derivative, so
(7) agrees. Distinct-source branches are not subject to a spurious
cross-branch equality requirement. The first-eligible choice therefore
does not change the value at the actual source.

For EVERY Borel set A contained in B_j, ordinary change of variables for
the analytic diffeomorphism on U_j gives

    area(theta_j(A))=integral_A J_j(t) dt.          (8)

This is valid for null sets and infinite integrals, not just open sets or
rectangles. For a nonnegative Borel weight a, approximation by simple
functions yields the corresponding weighted identity. No density is
replaced, no null-set value is chosen only a.e., and no control's IMAGE
identity is inherited from M; the construction applies to each of the
four coefficient laws with its own E_o, atlas and determinant.

Only after (7)–(8), the card's pointwise clock is

    kappa_o(z)=-log J_actual(F_o(z))
              =log abs L_o(z)
              =log abs K_o(z)-2 log abs D_o(z).    (9)

It is finite Borel on E_o, with arbitrary sign or zero allowed. It is not
defined as an outgoing clock on Z_o. In particular, the null-point clock
is owned by the fixed analytic version (7), not by an inference of unique
pointwise values from an a.e. measure theorem.

## 4. Global fixed-set classification for every owner

A legal fixed point must have x=y=t because the first coordinate is y.
Then A=B=a=1+floor(abs t), g=a and r=0. All four denominator coefficients
are therefore R=0, and D=3t^2. Legality forces t!=0. The inertial term
H(x-y) vanishes at the point, but its derivative must NOT be discarded.
The fixed equation is

    t=(2t^3+G)/(3t^2), equivalently t^3=G.         (10)

All G are positive, so t>0; no negative or zero fixed state is missed.

For M,R,I, G=a, so t=a^(1/3) must satisfy

    a-1 <= a^(1/3) < a.                            (11)

For a=1 the root1 violates the strict upper endpoint. For a=2 the root
alpha=2^(1/3) satisfies 1<alpha<2 and is in the correct cell. For every
a>=3, (a-1)^3 >=4(a-1)>a, so the root is below a-1. Thus alpha is the ONLY
cell-consistent algebraic possibility for these three owners, globally.
No readout cutoff has entered the argument.

For C, G=1 everywhere, so (10) has just t=1. Its actual readouts are
A=B=2 and r=0; this is permitted because C's G,H are1, not g. In particular
one must not assign the endpoint t=1 to readout1.

At ANY such cell-consistent solution, t^3=G and R=0 imply

    L_o(t,t)=H,
    DF_o(t,t)=[[0,1],[H,-H]], det DF_o=-H.          (12)

For M and R, H=2 at (alpha,alpha); it is legal, with determinant -2.
For C, H=1 at (1,1); it is legal, with determinant -1.
For I, H=0 at (alpha,alpha); the determinant is0 and the point is ILLEGAL.
It remains a terminal object of I, with units and all actual incoming,
not a fixed source cycle. Hence the complete ACTUAL fixed sets are:

| Owner | Entire legal fixed set | Own J at the fixed point | Own kappa |
|---|---|---|---|
| M | {(alpha,alpha)} | 1/2 | log2 |
| C | {(1,1)} | 1 | 0 |
| R | {(alpha,alpha)} | 1/2 | log2 |
| I | empty | not applicable | not applicable |

The C fixed point lies on integer/null faces, so its zero clock is an
explicit use of the all-point lock. Equality of M/R fixed coordinates and
clock does not identify their full owners, predecessors, basins or ledgers.

## 5. All legal depths, all incoming and compatible histories

Everything in this and the next sections is repeated with a fixed owner o;
there is never a mixture of different coefficient-law trajectories.
Write T=F_o, E=E_o, kappa=kappa_o. Set D_0=X, T^0=id, S_0=0, and

    D_n={z:T^j z in E for every 0<=j<n},
    S_n(z)=sum_{j=0}^{n-1} kappa(T^j z), z in D_n.

These are Borel. For nonnegative integers n,m,
z in D_{n+m} iff z in D_n and T^n z in D_m, and then
S_{n+m}(z)=S_n(z)+S_m(T^n z). Terminal arrival is allowed at the last step;
the next step is not presumed legal.

For every t in X define the unrestricted exact recursion

    P^0(t)={t},
    P^{n+1}(t)=union_{w in P^n(t)} P_o(w).         (13)

Induction using (4) proves

    P^n(t)={z in D_n:T^n z=t}                     (14)

for EVERY n, with all source cells and all roots at each recursion stage.
Duplicates may be removed inside a set P^n, but equality of points reached
at different depths does not erase those depths or groupoid lags. A
compatible infinite backward history over t is exactly a sequence
t=z_0,z_1,... with z_{j+1} in P_o(z_j) for all j. These are all such
histories by (4); their existence is not inferred from a finite tree.
They are retained as histories, not made into a new inverse-limit owner.

Equations(13)–(14) apply in particular to every terminal target, to each
fixed core, and to every point whose later orbit has not been classified.
They specify exact incoming coverage, not a finite scientific computation.

## 6. History-pair IMAGE, descent and cocycle signs

Refine each D_n by all length-n itineraries through the disjoint P_j of
Section3. Each resulting Borel piece U_a has T^n injective, with Borel
image V_a and Borel inverse theta_a. There are countably many pieces.
Composition of the analytic inverse germs, restricted to the actual
itinerary, gives the full-point product density

    J_a(t)=exp(-S_n(theta_a(t))).                  (15)

Repeated weighted application of (8) proves every-Borel IMAGE with (15)
on these pieces. The proof includes n=0, for which the branch is identity,
J=1 and the carrier is all X. No endpoint differentiability of the global
piecewise map is substituted for the assigned analytic composition.

Take an r-step inverse branch theta_a and an s-step inverse branch theta_b,
restrict their common image to V_a intersect V_b, and put
z=theta_a(t), w=theta_b(t). The history-pair bisection w->z has lag r-s
and is the Borel bijection theta_a composed with T^s on its actual source.
Its assigned determinant density is the ratio

    J_a(t)/J_b(t)=exp[-S_r(z)+S_s(w)].             (16)

Using weighted IMAGE first through theta_b and then theta_a proves, for
EVERY Borel subset A of this history-pair source,

    area({z(w):w in A})
       = integral_A exp[-S_r(z(w))+S_s(w)] dw.     (17)

Thus IMAGE belongs to actual history maps, not a formal word or a quotient.

Define G exactly as in the card: triples (z,k,w) with a legal witness
T^r z=T^s w, k=r-s. Equal actual triples are identified, but distinct k
are never erased. Let c=S_r(z)-S_s(w). If a second witness (r',s') has
the same lag, then r'-r=s'-s. Order the two witnesses so this common
difference d is nonnegative. The longer witness supplies d legal steps
from the common image of the shorter one. The sum identity cancels the
same S_d from both sides, proving descent. No illegal terminal padding
is used. The density in (16) consequently descends on overlapping actual
history-pair bisections as well.

For multiplication (z,r-s,w)(w,p-q,v), align the middle iterate to
N=max(s,p). If s<=p, advance the first equality by p-s, which is legal
because the second witness supplies those middle steps. If p<=s, instead
advance the second equality by s-p using the first witness. In either
case the remaining legal equality witnesses the composed lag
(r-s)+(p-q); the common middle clock sums cancel. Hence c is additive.
Units have lag/clock0 and inverse changes both signs.

In particular the forward arrow is (Tz,-1,z), represented by r=0,s=1,
with c=-kappa(z). It is NOT assigned +kappa. The full extension has all
objects (z,h) in X times R and arrows

    (w,h) -> (z,h+c(z,k,w)).                       (18)

Every real translation h->h+t commutes with these arrows and acts on the
orbit SET. No measurable/smooth regular quotient or chosen section is needed.

## 7. Exact full-owner arrow, kernel, isotropy and phase tests

An exact test for (z,k,w) is: some r,s>=0 with r-s=k satisfy z in D_r,
w in D_s and T^r z=T^s w. Its c is the witness-independent difference
above. Using (13) gives all finite inverse witnesses with no depth bound.
The three full kernels are therefore

    K_lag={(z,k,w) in G:k=0},
    K_clock={(z,k,w) in G:c(z,k,w)=0},
    K_joint=K_lag intersect K_clock.               (19)

These are actual arrow conditions, not just isotropy tests. For example
different incoming branches can give nonunit zero-lag arrows. From (18),
two extension objects (w,h_w),(z,h_z) are equivalent exactly when some
such legal triple has h_z-h_w=c(z,k,w).

For completeness the following classification describes every possible
source component without locating or enumerating additional periodic cores.
Determinism makes terminal, infinite non-eventual, and eventual-periodic
types invariant under these common-future arrows.

### 7.1 Finite-ending components

Let b be an actual terminal object. Its full source component is the union
of all P^n(b). For each z in it, the unique remaining depth d(z) to b
and W(z)=S_{d(z)}(z) are well defined. Every arrow w->z has

    k=d(z)-d(w), c=W(z)-W(w),                     (20)

and there is exactly one such arrow. Any common image has equal remaining
depth to b, proving necessity; arrival at b proves sufficiency. Thus
K_lag on this component means equal d; K_clock means equal W; K_joint
means both. Source and extension isotropy are zero, H={0}, and the exact
extension phase is h-W(z) in R. All incoming and terminal endpoints remain.

### 7.2 Infinite non-eventual components

Choose an anchor a in one such component. There is exactly one retained-lag
arrow a->z for each z: two different lags would produce an equality of
unequal iterates and hence eventual periodicity. Write its lag ell(z) and
clock b(z). Every arrow w->z has

    k=ell(z)-ell(w), c=b(z)-b(w).                  (21)

This gives all three kernels by the corresponding equalities, source and
extension isotropy zero, H={0}, and exact real phase h-b(z). This anchor is
a set-theoretic coordinate, not a global Borel selector or a change of owner.

### 7.3 Eventual-periodic components, generic and not a new census

If a component reaches an actual least-q core, let C be the sum of its
own kappa around that core. At every point its source isotropy is qZ:
an unequal-iterate equality implies an eventual cycle whose least period
divides that difference; conversely, after actual core entry every integer
multiple of q is witnessed. Transient sums cancel, giving character

    lq -> lC, H=C Z.                              (22)

Choose one actual anchor arrow a->z with lag k_z and clock b_z for each z.
Every arrow w->z then has, for exactly one integer l,

    k=k_z-k_w+lq, c=b_z-b_w+lC.                   (23)

The kernels are precisely (23) with k=0, c=0, or both; this includes every
incoming phase and merger. Source isotropy qZ survives in the extension
exactly when C=0; otherwise extension isotropy is zero. The exact extension
phase is h-b_z modulo ENTIRE C Z. The equality test is literal membership
of (h_z-b_z)-(h_w-b_w) in C Z, not in a closure or a selected subgroup.
If C!=0 the least positive translation stabilizer is abs C, with all
integer repetitions. If C=0 there is no positive primitive and phases are
all real, even though source and extension isotropy remain qZ.

These statements supply the full generic tests for unclassified parts of
X. They do not assert existence, absence, number or clock of a new q>=2
core. Higher-period scientific conclusions remain OPEN.

## 8. Complete fixed-core basins and their entire kernels/phases

For each actual fixed point f from Section4, set lambda=kappa(f) and define

    B_f=union_{n>=0} P^n(f),
    d(z)=min{n:T^n z=f}, W(z)=S_{d(z)}(z),
    b(z)=W(z)-d(z)lambda, z in B_f.                (24)

Equations(13)–(14) make B_f an exact full-source definition, including all
readouts, signs, finite depths and compatible infinite incoming histories.
It is the ENTIRE source component of f: a common future with f means
eventual arrival at f, and arrival at f gives an arrow. No other component
can merge into it without itself being included in B_f.

For z,w in this basin EVERY integer k occurs, with exactly the arrow

    (z,k,w), c=b(z)-b(w)+k lambda.                 (25)

To see sufficiency, use witnesses r=d(z)+p,s=d(w)+q, p,q>=0, and choose
p-q=k-d(z)+d(w). Then their common image is f. Conversely any early
common image can be advanced legally until f and its added common clock
cancels, yielding (25). This proves there are no omitted extra clock
values from transient or incoming histories.

The complete basin kernels, including nonisotropy arrows, are

    K_lag={(z,0,w):z,w in B_f},
    K_clock={(z,k,w):b(z)-b(w)+k lambda=0},
    K_joint={(z,0,w):b(z)=b(w)}.                  (26)

At every basin point source isotropy is Z and its ENTIRE clock image is
lambda Z. Extension isotropy is Z if lambda=0 and zero otherwise. All
extension phases are h-b(z) modulo lambda Z, equivalently h-W(z) modulo
lambda Z. When lambda=0 this is the full real coordinate h-W(z), not a
collapsed zero-clock phase. Exact clock-kernel tests are:

- lambda!=0: (b(w)-b(z))/lambda must be the integer k;
- lambda=0: b(z)=b(w), with EVERY k allowed if equality holds.

In particular, a zero-clock fixed point does not imply the clock is zero
on its entire incoming basin. Off-core W values remain those of (9).

For M, f=(alpha,alpha), lambda=log2: one full fixed-core source component
owns H=log2 Z, zero extension isotropy and all phases modulo log2. Its
least positive primitive is log2, and repetitions have every positive
integer multiple n log2 (with both integer signs at isotropy level).
The phase circle is ONE translation packet, not a distinct packet per
height representative. The complete incoming set is M's own (24).

For R, the coordinate and lambda are the same, so its separately owned
fixed-core basin has the same abstract kernel/phase description. It is
still R's own (13), (24) and (9), not M's incoming basin or extra M credit.

For C, f=(1,1), lambda=0: its complete fixed-core basin has source and
extension isotropy Z, ENTIRE H={0}, all real phases h-W(z), and NO positive
primitive. Equation(26) gives its full clock and joint kernels; they are
not automatically all arrows just because the core clock is zero.

For I there is no actual fixed-core basin. The algebraic candidate
(alpha,alpha) is a terminal object, whose entire incoming component and
real phases are covered by Section7.1 with b=(alpha,alpha) and the same
unrestricted I recursion. No assertion of an empty incoming set is made.
Every other terminal/non-eventual/unclassified eventual component of all
four owners is likewise retained by Sections5–7.

## 9. Bounded scientific disposition

The arithmetic readouts are endogenous current-state integer operations:
at the card's seed (N-1,d-1), A=N,B=d and r=0 iff d divides N. For MAIN
these values enter the actual denominator, nonlinear numerator and inertia,
not a passive label register. This identity does not establish seed legality,
endogenous prime admission, strong naturalness or a prime-only ledger.

MAIN's global fixed-only gate owns exactly one positive fixed-core packet,
with primitive log2 and the complete full-source history described above.
No MAIN nonprime or duplicate witness is established by this gate. R
reproduces that fixed-coordinate/clock datum in a distinct control owner;
C owns only a zero-clock fixed core; I has no legal fixed core. These are
whole fixed-set conclusions, not full positive-ledger classifications.

The card's joint target concerns EVERY positive packet. Unclassified higher
periods may still supply a nonprime, a duplicate log2 packet, other primes,
or additional obstructions. Nothing here decides those possibilities.
Accordingly the frozen short gate ends BOUNDED OPEN / FORK, not STOP from
an unproved violation, and certainly not a prime-target pass. No extra
census, parameter change or owner repair is used to strengthen the result.

Same-object ownership is maintained separately for all four maps, original
area clocks and full histories. Strong naturalness and PROVES_TOO_MUCH
remain OPEN; arithmetic T1 NOT PASSED; classical NOT APPLICABLE; T3
NOT AUDITED; formal coordinates UNASSIGNED; Route B NOT INVOKED.
This raw is to be FULL self-read and frozen before any manuscript access.
Comparison requires root's FULL raw read and DISTINCT PAPER UNLOCK.
