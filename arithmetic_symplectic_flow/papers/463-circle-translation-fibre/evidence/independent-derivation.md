# CTF01 — card-only independent derivation

Candidate: ANG-AUDIT-20260924-CTF01. Paper463.
Reviewer: `/root/rcr01_independent_review`, 2026-09-24 UTC.
Status: RAW; freeze before any author-manuscript access.

## 0. Input and staged access

The only scientific input read for this derivation is the amended frozen
card, FULL numbered read1–101/EOF, SHA-256
`57d55f1ae10db86df85edc051766496db6288e3fbfdef958051161cb8bc8e9f7`.
Its original92-line prefix and explicit pre-release control-version lock
are both retained. Root reported FULL reading the amended161-line CP1 PASS,
SHA `ca90b126851efe2e3e0f88395f5e5a3902f57b593e1442c75462de245e03e70a`,
before issuing DISTINCT RAW RELEASE.

No author manuscript, README, claim ledger, Outcome, helper/peer result,
old proof or other scientific file was opened. The staged ARS adaptation
and personally refreshed instructions are recorded in CP1. This reviewer
inherits the same model/shared-root history and prior tasks: NOT_CALIBRATED,
not blind, human, external, cross-model or independent-error validation.
No scientific program, numerical census, network, Git, PDF, old mutation,
operator/zero work or465 is used. Proofs below are exact deductions.

## 1. Complete Borel inverse branches and own product IMAGE

Write S=R/Z additively, with normalized Haar length lambda. Let E_i=T(D_i)
and nu=mu times lambda on Y=X times S. The product is standard Borel and
nu is sigma-finite. Each source piece D_i times S is Borel and F-injective:
equality of outputs forces equality of x by the parent branch, then equality
of the angle by cancellation in S. Its image is exactly E_i times S and
its actual inverse is

    Theta_i(y,t)=(theta_i y,t-alpha(theta_i y)).             (1)

The inverse is Borel, since theta_i and alpha are Borel and group addition
is continuous. The pieces form a complete countable disjoint partition of
the legal source D times S. All predecessor branches are retained, including
branches into terminal parent targets. Every target angle is allowed.

Let B be ANY Borel subset of E_i times S and set
B_y={t:(y,t) in B}. Its fibre-length function g(y)=lambda(B_y) is Borel;
this follows first for rectangle indicators and then by the usual
nonnegative measurable-function approximation for product integration.
The fibre of Theta_i B above x in D_i is B_(Tx)-alpha(x), hence its Haar
length is g(Tx). Therefore nonnegative product integration gives

    nu(Theta_i B)=integral_(D_i) g(Tx) dmu(x)
                =integral_(E_i) g(y) J_i(y) dmu(y)
                =integral_B J_i(y) dnu(y,t).               (2)

The middle equality is the weighted form of the parent IMAGE assumption:
prove it for indicators of Borel subsets of E_i, then simple functions,
then increasing nonnegative approximations. Sigma-finiteness supports the
product integration used here. This proves (2) for full Borel B, not only
rectangles, and uses no derivative or smoothness of alpha.

Prescribe the lift density to be J_i(y) at EVERY point of this branch
image, as frozen on the card. This version is positive and finite and
satisfies (2); null-point values do not follow uniquely from (2), but are
explicit input. The own clock is consequently

    kappa_F(x,s)=-log J_i(Tx)=kappa_T(x).                  (3)

It is finite Borel on the legal source and may be signed or zero. No clock
is assigned on the terminal complement. The entire original carrier and
product measure, including all null strata, remain unchanged.

## 2. Legal iterates, every inverse depth and two cocycles

Let D_n be the set of parent points admitting n actual legal steps, with
D_0=X. For x in D_n define

    A_n(x)=sum_(j=0)^(n-1) alpha(T^j x) in S,
    K_n(x)=sum_(j=0)^(n-1) kappa_T(T^j x) in R,
    A_0=0, K_0=0.

Then F admits n steps exactly on D_n times S and

    F^n(x,s)=(T^n x,s+A_n(x)), S_n^F(x,s)=K_n(x).         (4)

Both sums concatenate along legal histories. Every depth-n predecessor
of (y,t) is exactly

    {(x,t-A_n(x)): x in D_n, T^n x=y}.                    (5)

The parent preimages in (5) are all actual inverse words with their legal
intermediate guards. The disjoint source itineraries account for every
predecessor, with no choice of an angle or branch. Their composed inverse
densities are the products of the successive prescribed J_i values; repeated
weighted substitution proves their own IMAGE identities. Each factor is
evaluated on the actual target at that step, whether or not that target
admits another step. Formula (5) holds for all n, including n=0.

For a parent arrow g=(x,k,y) with legal witness (m,n), define

    a(g)=A_m(x)-A_n(y) in S,
    c(g)=K_m(x)-K_n(y) in R, k=m-n.                      (6)

Two witnesses of the SAME triple have the same depth difference. The later
witness advances both depths equally along an actually existing common
tail, whose angle and clock cancel. Thus both a and c descend to triples.
This does not assume that an arbitrary meeting can be padded past a terminal.

For composition, suppose the middle point has existing witness depths n
and p. Align them at max(n,p), not at an unproved longer depth. If p>=n,
advance the first meeting by p-n along that existing middle history; if
n>=p, advance the second by n-p. The other path has the same continuation
from its meeting. The middle sums cancel, proving additivity of a and c.
Inverses negate both cocycles; units have zero values. In particular

    (Tx,-1,x) has a=-alpha(x), c=-kappa_T(x).             (7)

The identical argument proves the lift clock's descent and additivity from
legal lift witnesses. No total-map padding is used on finite histories.

## 3. Exact lifted arrows, kernels and full height action

For z=(x,s), w=(y,t), the complete lift relation is

    (z,k,w) exists iff some legal (m,n) satisfies
    k=m-n, T^m x=T^n y, s+A_m(x)=t+A_n(y).               (8)

Equivalently there is a parent arrow g=(x,k,y) and s=t-a(g).
Its clock is exactly c(g). Every parent arrow has a unique lift for each
chosen SOURCE angle, but it need not lift between arbitrarily prescribed
endpoint angles. Thus projection is not an identification of full groupoids.

The complete lag, clock and joint kernels of either owner are its actual
arrows with k=0, c=0, or both. For F, (8) plus these equations includes
all branch merging, all terminal histories and every angle. A lag-zero
kernel need not contain only units when the parent is noninjective.

The extension arrow sends (w,h) to (z,h+c), and physical translation adds
any real number to heights. At a source object, the source isotropy consists
of its actual retained-lag self-arrows; the extension isotropy is its clock
kernel, and H is its ENTIRE clock image. A convenient complete phase rule
is as follows. In any source class choose a reference b and actual arrows
b->z with clocks B_z. The clocks of all arrows w->z form the coset

    B_z-B_w+H_b.

This follows by composing with the two reference arrows and all reference
isotropy. Hence extension orbits are exactly (h-B_z) modulo H_b. All real
heights remain. Choice changes B_z only by H_b. Physical translation is
transitive on R/H_b with stabilizer H_b. These are set-level coordinates,
not a regularity claim or a global measurable-selector construction.

If H=0, phases are real and there is no positive physical primitive. If
H=L Z with L>0, every phase lies in R/(L Z), primitive L is its least
positive return, and all positive integer repetitions remain. Zero-clock
source isotropy is not removed or confused with a positive physical period.

## 4. All terminal-ending parent and lift classes

Let a parent point x have finite remaining lifetime d_x and terminal endpoint
b=T^(d_x)x. Put B_x=K_(d_x)(x), beta_x=A_(d_x)(x). For a fixed b, EVERY
point ending there belongs to its complete parent source class. Between
any ordered pair x,y in that class there is exactly one parent arrow:

    k=d_x-d_y, a=beta_x-beta_y, c=B_x-B_y.                (9)

Existence uses their terminal meeting. Any other meeting has the same
remaining lifetime on both sides and hence the same lag. A nonzero-lag
self-arrow would create an eventual cycle and contradict finite lifetime.
The parent lag/clock/joint kernels are equal-depth, equal-B, and joint
relations. Source/extension isotropy and H are0; all phases are h-B_x in R.

By(8), the full lifted terminal endpoint of (x,s) is

    (b,u), u=s+beta_x.

For EACH u in S, the complete source class is

    {(x,u-beta_x): x ends at b}.                         (10)

It includes the terminal (b,u) and every actual incoming depth from (5).
Arrows have the same lag and clock as(9), restricted to(10); their full
kernels are the same equality tests inside that class. All isotropy/H
vanishes and all phases are h-B_x. No terminal angle is discarded and
no terminal is given a fictitious outgoing step or isotropy Z.

## 5. Infinite non-eventual parent and lift classes

In an infinite parent class with no eventual cycle, no nonzero-lag self-arrow
can occur: such an arrow would give two equal iterates and an eventual cycle.
Thus there is a unique parent arrow between any ordered pair in that class.
Choose a reference b and write the lag, angle and clock of b->x as
ell_x, beta_x, B_x. All pair arrows are their differences:

    k=ell_x-ell_y, a=beta_x-beta_y, c=B_x-B_y.            (11)

The parent kernels are equal-ell, equal-B and their intersection. Parent
source/extension isotropy and H are0, with real phase h-B_x.
The complete lift classes are, for EVERY u in S,

    {(x,u-beta_x): x in the parent class}.               (12)

Indeed(8) is precisely s+beta_x=t+beta_y. Every class occurs over b.
Its arrows, kernels and real phases are the restrictions of(11); source
and extension isotropy and H remain0. All infinite incoming merges and
inverse depths are included through(5), without selecting a single forward
ray. The fibre cannot create a cycle above a non-eventual parent class.

## 6. Every eventual parent core and the complete angular relation

Let v_j=T^j v_0, j mod q, be a parent core of least period q. Define

    C=K_q(v_0) in R, A=A_q(v_0) in S.

For any x in its full incoming basin, let n_x be first core-entry depth,
j_x the entry index, and rho_j=(-j mod q) in {0,...,q-1}. Set

    N_x=n_x+rho_(j_x), B_x=K_(N_x)(x), beta_x=A_(N_x)(x).

Then T^(N_x)x=v_0, with every actual incoming branch recorded in the sums.
The complete parent arrows in this basin are exactly

    k=N_x-N_y+q a,
    angle=beta_x-beta_y+a A,
    clock=B_x-B_y+a C, a in Z.                          (13)

Necessity follows by advancing any meeting to a sufficiently late visit to
v_0, which is legal on this infinite tail. Conversely any a is the difference
of two sufficiently large nonnegative numbers of complete core circuits.
The parent kernels are (13) with k=0, clock=0, or both. At every incoming
point, source isotropy is qZ, H=CZ, and extension isotropy is0 when C!=0
or qZ when C=0. All parent phases are h-B_x modulo CZ (real for C=0).

For z=(x,s), put u_z=s+beta_x. The exact lifted relation over this basin is

    u_z-u_w=-a A,
    k=N_x-N_y+q a, c=B_x-B_y+a C, a in Z.                (14)

Consequently complete lift source classes are indexed by ALL cosets
u+<A> in S/<A>, where <A>={a A:a in Z}. In one such class every incoming
parent point x is accompanied by exactly all angles s with s+beta_x in
that coset. This is the full basin/component assignment, not a core-only
description or a choice of one angle above each incoming point.

Fix u_0 in one coset and choose integers a_z with u_z=u_0-a_z A. Put

    L_z=N_x+q a_z, V_z=B_x+C a_z.                        (15)

These are phase coordinates, not changes to the owner or clock. Their
ambiguity and the full isotropy depend on the order of A, as follows.

## 7. Finite angular order: all cores and continuum multiplicity

Suppose A has additive order d<infinity, including d=1 when A=0. The
return F^q on the fibre above v_0 is the translation s->s+A. Every one
of its orbits contains exactly d points, and there is one such orbit per
coset of the finite subgroup <A>. Each gives one F-core of least period qd.
Any return time projects to a multiple of q and then must kill A, so qd
is least. Conversely every F-periodic point projects to an actually periodic
parent point; intersecting its core with the reference fibre gives exactly
one of these d-point orbits. No other F cores exist above this parent core.

For each coset, the complete incoming basin is exactly its class in(14):
every incoming parent point has d included angles, and every such point
eventually reaches that F core. Different cosets do not merge through an
incoming branch, since(14) is necessary for ANY legal meeting. The set
S/<A> has continuum cardinality: a rational rotation of order d generates
the subgroup {j/d:0<=j<d}, and all representatives in[0,1/d) label distinct
cosets. This argument counts every core, not one preferred representative
as a replacement owner.

The admissible a in(14) are a_z-a_w+d t, t in Z. Thus every arrow within
one full basin has

    k=L_z-L_w+qd t, c=V_z-V_w+dC t.                     (16)

The complete lag/clock/joint kernels are (16) with k=0, c=0, or both.
At EVERY point of the basin, source isotropy is qd Z and its entire
clock image is dC Z. Extension isotropy is0 for C!=0 and qd Z for C=0.
All extension phases are

    h-V_z modulo dC Z.                                 (17)

Changing a_z by a multiple of d changes V_z by dC Z, so(17) is well-defined
as an orbit coordinate. For C=0 it is real and the zero-clock source
isotropy remains. For C!=0 EACH of the continuum many distinct full packets
has primitive d abs C and all repetitions n d abs C, n>=1. These are
distinct packets even though their primitive lengths coincide.

## 8. Infinite angular order and phase changes

If A has infinite additive order, translation by A has no finite orbit.
There are no F cores above this parent core. Each full source component
is nevertheless retained as one coset class in(14). The a_z in(15) is now
unique relative to u_0, and all pair arrows are exactly

    k=L_z-L_w, c=V_z-V_w.                              (18)

Thus the three kernels are equal-L, equal-V, and joint relations. All
source/extension isotropy and H are0, even when C!=0. Every real phase
h-V_z remains; there is no positive primitive. Each coset is countable
but is not identified with its closure. There are continuum many cosets
(a countable partition-class size cannot reduce the cardinality of the
circle quotient below continuum, by countable cardinal multiplication).
No regular or measurable quotient of this orbit relation is presumed.

For clarity, an infinite-order element of S is an irrational rotation.
Its subgroup is dense, but this does not add source arrows. An elementary
density argument takes N+1 fractional parts of multiples of its irrational
representative in N equal intervals. Two yield a nonzero subgroup element
with real representative delta in(0,1/N), after changing sign if necessary.
Integer multiples of delta approximate every point of[0,1) to within delta.
This proves density, not equality of that countable subgroup with S, and
not a periodic return in the height extension.

Changing reference parent phase preserves ALL these data. If P_j is the
angle accumulated from v_0 to v_j, actual transport F^j restricts on the
reference fibre to the bijection s->s+P_j. Circle addition is commutative,
so the accumulated A and signed C are unchanged by cyclic reindexing.
That translation conjugates the two return translations and maps all finite
or infinite orbit cosets bijectively. Least periods, packet multiplicity
and entire H are preserved. Full basins are the intrinsic F classes from
(8); their reference labels change, not their objects. Height-phase
coordinates change by the clock of a reference arrow and the applicable
H ambiguity, leaving all phases. No global class selector is asserted.

Sections4–8 exhaust the partial parent cases: finite lifetime, infinite
non-eventual history, and eventual core. A periodic lift point projects
to an actually periodic parent point; an eventually periodic lift point
projects to an eventually periodic parent point. Incoming nonperiodic
points of a cyclic parent basin have not been incorrectly excluded.

## 9. Exact implication for the necessary prime benchmark

The positive lift ledger is nonempty if and only if at least one parent
core has C!=0 and finite-order return angle A. All other cases above have
H=0 and no positive primitive. This includes the possibility of no parent
cores at all, or only zero-clock/infinite-order ones.

Whenever such a core exists, §7 gives continuum many distinct full packets
of the SAME positive primitive L=d abs C. If L is not log of an ordinary
prime, prime purity fails. If L=log p, multiplicity at most one for that
prime fails. If no such core exists, positive nonemptiness fails. Therefore
NO owner in this full circle-translation class satisfies all three necessary
benchmark clauses simultaneously. All-prime coverage cannot repair this.

No rationality of exp(abs C) is used or assumed. The argument is the actual
full-circle packet multiplicity, not a transferred finite/countable-fibre
power lemma. C=0 and negative C are already accounted for. Removing a null
stratum, selecting one angular orbit, or replacing a dense orbit by its
closure would change the owner and does not evade this conclusion in scope.

## 10. Common full parent and formulas for controls A/B/C

For each separately owned control, the parent is T(x)=2x on ALL R with
Lebesgue measure. Its actual inverse is y/2, with the card-locked analytic
inverse density J=1/2 at EVERY y, including0. For every Borel E,
Leb(E/2)=(1/2)Leb(E); hence kappa_T=ell=log2 pointwise.
All iterates T^n x=2^n x and inverse sets {y/2^n} are legal. Complete
parent arrows are (2^(-k)y,k,y), k in Z, with clock k ell.

All parent kernels are units. The origin is the only parent core and
its full basin is {0}; there source isotropy is Z, H=ell Z, extension
isotropy0, and all phases are h modulo ell Z. Its primitive is log2 with
every positive integer repetition. Every nonzero parent class is
{epsilon 2^n v:n in Z}, epsilon in{+1,-1}, v in[1,2), with isotropy/H0
and all real phases h+log(abs x). Neither sign or any incoming iterate
is discarded, and no nonzero point enters the origin.

For a constant angular increment a, the lift F_a(x,s)=(2x,s+a) is a
global Borel bijection with actual inverse (y,t)->(y/2,t-a). Formula(2),
or direct product substitution, proves every-Borel IMAGE with the fixed
all-point density1/2. Thus its own clock is ell. For all integers n,

    F_a^n(x,s)=(2^n x,s+n a),
    F_a^(-n){(y,t)}={(y/2^n,t-n a)} for n>=0.           (19)

All arrows from(y,t) to(x,s) are exactly

    x=2^(-k)y, s=t-k a, k in Z, c=k ell.                (20)

All three lift kernels are units, since c=0 iff k=0. On EVERY nonzero
base class the complete lift classes are, for all u in S,

    {(epsilon 2^n v,u+n a):n in Z}.                     (21)

They have source/extension isotropy and H equal0. All real phases are
h+n ell, equivalently h+log(abs x) up to the constant log v. This explicitly
includes all bilateral histories, both signs and every angle; (19) supplies
every incoming depth. Only the origin classification differs among A/B/C.

## 11. Control A: zero angular increment

Here a=0. At the origin EACH (0,s), s in S, is a separate fixed core and
its complete basin consists of that point. Source isotropy is Z, whole
H=ell Z, extension isotropy0, with all phases h modulo ell Z. There are
continuum many distinct positive packets of primitive log2, each with all
positive integer repetitions. Their equal lengths do not make one packet.
This fails prime multiplicity one. Nonzero classes, inverse depths and
all kernels are exactly (19)–(21) with a=0, not an origin-only owner.

## 12. Control B: half-turn increment

Here a=1/2 mod1, of order2. Origin cores are the pairs

    {(0,u),(0,u+1/2)}, u in[0,1/2).

Every such pair is retained, giving continuum many distinct least-period2
cores. There are no nonzero incoming points. Each whole source packet has
source isotropy2Z, H=2ell Z=(log4)Z and extension isotropy0. Writing the
origin angle as u+j/2 with j=0,1 gives all extension phases

    h+j ell modulo 2ell Z.

Indeed the forward arrow from u to u+j/2 has clock -j ell. Every packet
has primitive log4 and all repetitions n log4. Thus prime purity fails,
in addition to retaining the equal-length multiplicity. The nonzero
classes and phases, complete inverse histories and unit kernels are still
(19)–(21); the lift clock is not divided by its two-step source period.

## 13. Control C: irrational angular increment

Here a=gamma=sqrt(2) mod1 has infinite order. If a nonzero integer multiple
were0, sqrt(2) would be rational; the usual reduced-fraction squaring parity
argument excludes that possibility. Origin source classes are exactly

    {(0,u+n gamma):n in Z}, indexed by S/<gamma>.

Each is countable and dense in the origin circle by the argument in §8,
but is NOT the circle itself. All of these continuum many classes remain.
Each has source/extension isotropy and H equal0. Relative to a reference
u, the integer n in u+n gamma is unique, and every real phase is h+n ell.
There is no positive primitive or positive repetition on the origin or
on any nonzero class. The full positive ledger is empty, not obtained by
discarding the origin stratum. Equations(19)–(21) supply all other histories,
angles, phases and unit kernels, without taking an orbit closure.

## 14. Control D: own partial translation and every endpoint

The parent T(x)=x+1 has legal source(-2,0), actual image(-1,1) and inverse
theta(y)=y-1 on that image. The frozen analytic inverse version is J=1 at
EVERY such y; translation substitution proves every-Borel IMAGE. Thus its
own clock is0 on the legal source, with no clock assigned to terminals.

Legal n-step source domains are R for n=0, (-2,0) for n=1, (-2,-1) for
n=2, and empty for n>=3. The exact parent depth-n inverse sets are

    n=0: {y};
    n=1: {y-1} if -1<y<1, otherwise empty;
    n=2: {y-2} if 0<y<1, otherwise empty;
    n>=3: empty.                                       (22)

All parent source classes are the three-point chains

    t-2 -> t-1 -> t, for each t in(0,1),

the two-point chain -1->0, and singleton terminals at every x outside
(-2,1). In particular -2 and1 are singleton terminals;0 is terminal with
the legal predecessor -1; -1 itself is a source without a predecessor,
not a terminal. These chains exhaust all real objects and every incoming
history, including both source-domain endpoints without extending the map.

In a chain ending at t, denote its point of remaining depth j by t-j.
Every ordered pair has one arrow of lag j_z-j_w and clock0. Since depths
are distinct in each chain, the lag and joint kernels are units; the clock
kernel is the entire parent groupoid. All source/extension isotropy and
H are0; every extension phase is h in R and the positive ledger is empty.

For the lift alpha(x)=[x], the actual inverse is

    (y,t)->(y-1,t-[y-1])=(y-1,t-[y]),
    on (-1,1) times S.                                 (23)

Formula(2) proves its every-Borel product IMAGE, with J_F=1 at every
actual target, including all legal special/null targets. Its own clock
is0. No terminal target is excluded just because it lacks another step.
For an allowed n, the accumulated angle is
sum_(j<n)[x+j]=[n x+n(n-1)/2]=[n x]. Hence

    F^n(x,s)=(x+n,s+[n x]),
    depth-n inverse of (y,t)=(y-n,t-[n y])
    whenever the corresponding case of (22) is legal.  (24)

There are no other inverse histories. Every full lift source class over
a terminal t in(0,1) and EACH terminal angle u in S is the three-point chain

    (t-2,u-[2t]) -> (t-1,u-[t]) -> (t,u).                (25)

Over terminal0, for EACH u in S, it is (-1,u)->(0,u). At any real x
outside(-2,1), every (x,u) is a singleton terminal class. Equations(25)
and these boundary cases exhaust R times S; no exceptional angle, endpoint
or isolated terminal is removed.

Within each chain, all ordered pairs have lag equal to their remaining-depth
difference and clock0. The lift lag/joint kernels are units, its clock kernel
is the entire groupoid, and source/extension isotropy and H are0 everywhere.
All real phases h remain. Both the parent and lift have no positive packet
or positive repetition, despite having all their finite histories and units.

## 15. Scope disposition and raw freeze

The own Borel product IMAGE, complete legal angle relation, full source
classification and full-circle multiplicity establish the scoped conditional
result without a rational multiplier hypothesis. All four controls retain
their original full measures, null-stratum versions, source histories and
terminal objects. They remain EXTERNAL CONTROLS, not prime discovery from
the chosen coefficient2 or freely selected angular increments.

Portfolio FORK / retain conditional filter. The symbolic-history to angular
memory arrow is audited, but no endogenous prime-symbolic source or strong
naturalness mechanism is supplied. Classical NOT APPLICABLE; arithmetic T1
NOT PASSED; T3 NOT AUDITED; formal UNASSIGNED; Route B NOT INVOKED. No
operator/trace, zero matching, publication or next candidate is implied.

Freeze this raw before manuscript access. RAW READY communicates only its
path, line count and SHA, with no mathematical outcomes. Root FULL raw
reading and DISTINCT PAPER UNLOCK are required before final comparison.
Any later correction requires a separate erratum, never a silent rewrite
of this exposed raw. No465 is authorized.
