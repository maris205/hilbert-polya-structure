# Geometric division/addition carry: an owned clock with an all-integer primitive ledger

Candidate ID: `ANG-20260920-GAC01`.
Status: `OWNED CARRY CLOCK; ALL-INTEGER PRIMITIVE LEDGER — STOP / FORK`.
Date: 2026-09-20. Markdown research record, not a publication.

## Abstract

On the entire nonnegative real plane we audit the autonomous map
T(x,y)=(y,(x-j)/(floor(y)+1)+y), where j is
the remainder of floor(x) modulo floor(y)+1. Complete
inverse branches, including all axes and cuts, supply an actual
Lebesgue IMAGE clock. The full retained-lag groupoid has positive
primitive packets, but exactly one for EACH integer N>=2,
of least time log N. Every periodic source point is an
integer diagonal; every eventually periodic source point is an integer
lattice point, entering its fixed core within two steps. We
classify all finite predecessor basins, source isotropy, time stabilizers
and extension kernels. A primitive log 4 packet cannot be
relabelled a repetition of the log 2 packet. Thus this
owner fails the prime-only ledger despite retaining positive closed times.
Three separately owned controls distinguish the effects of the divisor,
shear and carry. No formal Route coordinate is evaluated.

## 1. Frozen object, lineage and claim boundary

The [original card](candidate-card.md), first 180 lines, SHA-256
`c9184fc0e8062f01800716d82b76ee012c13bf7d0bad2aba0a2d68f88612bbba`,
precedes these claims. It freezes X=[0,infinity)^2, its
ordinary Borel structure and Lebesgue area, without added atoms,
root labels, selected centres or a scale fibre. Write

    x=A+r, y=B+s, 0<=r,s<1,
    m=B+1, A=m*q+j, 0<=j<m.
    T(x,y)=(y,q+r/m+y).                           (1)

The actual next floors/fractions are

    (B, B+q+epsilon; s, s+r/m-epsilon),
    epsilon=floor(s+r/m) in {0,1}.                (2)

This follows directly from (1), including equality at a carry
cut. Every finite point is retained; the same rule applies
to m=1 and all axes. No terminal or infinity completion.

The preserved observable is m|A iff j=0, with
proper-divisor symbols visible at 1<m<A. Quotient and real
carry affect the next actual integer coordinates. This is a
specific divisor-symbolic -> real-feedback deformation, not proof of a
prime selector or Logistic/Henon conjugacy. The choices m=B+1,
addition of y and Lebesgue density remain declared designs; stronger
naturalness is OPEN. The complete input/access record is in
the [source note](evidence/scout-record.md). No older source clock,
return theorem or Route result is transferred.

## 2. Exact inverse owner and full-point IMAGE

For B,q>=0, m=B+1 and j=0,...,m-1, let

    D_(B,q,j)=[m*q+j,m*q+j+1) x [B,B+1),
    E_(B,q)={B<=u<B+1, q<=v-u<q+1/m},
    h_(B,q,j)(u,v)=(m*(v-u)+j,u).             (3)

On D, equation (1) gives v-u=q+r/m; hence
T maps D bijectively to E and (3) is its
inverse. Conversely every preimage must have B=floor(u), q=floor(v-u)
and one of these j. Therefore the exact image is

    u>=0, v-u>=0,
    fractional_part(v-u)<1/(floor(u)+1).           (4)

Every target in (4) has EXACTLY m=floor(u)+1
distinct predecessors; outside it there are none. Half-open boundaries
decide equality without duplication. In particular all targets below v=u
and all upper gaps in (4) stay in X but
are not images. T is total, finite-to-one and nononto.
It is Borel, not continuous: along (x,1), x approaches
1 from below, the second output tends to 3/2,
whereas T(1,1)=(1,1). No etale or Hausdorff claim follows.

On EACH inverse branch

    Dh=[[-m,m],[1,0]], |det Dh|=m,
    mu(h E')=integral_(E') m dmu                (5)

for every Borel E' in its actual domain. This is
affine change of variables, not a count of predecessors. The
original all-point version J_h=m extends that formula to every
retained null axis/cut; no atom ratios are introduced. A.e.
IMAGE alone would not fix those values. The actual one-step
clock in the frozen direction is

    kappa(x,y)=-log(1+floor(y)).                  (6)

Thus the clock comes from the same geometric map and measure;
it is not an inserted positive roof or prime-time table.

For k>=0 define P_k(z) as the product of 1+floor(second
coordinate of T^i z), 0<=i<k, with P_0=1.
The finite forward branch has absolute Jacobian 1/P_k(z).
For an actual common-future arrow

    g=(z,k-l,w), T^k z=T^l w,
    source w, range z,

the local branch pair from w to z has

    J_g=P_k(z)/P_l(w),
    c(g)=-log J_g=-log P_k(z)+log P_l(w).        (7)

Every all-point product is finite and positive. Increasing both
k,l by the same amount appends the SAME factors and
leaves (7) unchanged. Two nonnegative presentations of a fixed
triple have just this common extension relation; thus c is
pointwise well-defined, including all null states. Synchronizing finite
common futures proves the cocycle law. Actual piecewise-affine branch
substitution proves IMAGE on each such branch-pair domain. No
arbitrary affine arrow or free branch word is added.

The countable Borel groupoid is the full set of these triples
in X x Z x X. The extension has ALL objects
(z,h), arrows (w,h)->(z,h+c(g)), and full real
translation h->h+t. The actual forward-step arrow z->Tz
has lag -1 and clock -kappa(z), not kappa(z).
The construction claims only a Borel/set quotient, not a
smooth mapping torus or positive-roof suspension.

## 3. Complete periodic and eventually periodic source ledger

### 3.1 All periods collapse to integer fixed cores

By (1), the second coordinate never decreases:

    y_next=y+q+r/m >= y.                         (8)

In ANY finite cycle the sum of these nonnegative increments
is zero. Thus every q and r on that cycle
vanishes; its y is constant and x_next=y. The cycle
must be a fixed point (t,t). Write t=n+r.
Then m=n+1, q=0, j=n and its second output
is t+r/(n+1); equality requires r=0. Conversely
every f_n=(n,n), n>=0, is fixed. These are
ALL periodic points and all have least source period one.
This is a whole-plane order proof, not a sampled period bound.

### 3.2 Integer reflection and all full predecessor basins

T maps integer lattice points to integer points. Conversely, if
T(x,y) is an integer pair, its first coordinate forces
y=B integer. Its second coordinate is B+q+r/m;
because 0<=r/m<1, integrality forces r=0. Hence

    T^(-1)(Z_nonnegative^2)=Z_nonnegative^2.       (9)

Every eventually periodic point is therefore an integer pair, with
no hidden off-lattice finite tail. At an integer pair (A,B),
put n=B+floor(A/(B+1)). Then n>=B and

    (A,B) -> (B,n) -> (n,n),                   (10)

since floor(B/(n+1))=0. Thus every integer point is
eventually periodic within TWO steps. This does not assert that
noninteger histories converge or arrive; all their returns are excluded
by (8)–(9), and all their states remain in X.

The entire basin of f_n is the finite set

    B_n={(A,B): 0<=B<=n,
         A=(B+1)*(n-B)+j, j=0,...,B},
    |B_n|=(n+1)*(n+2)/2.                       (11)

Indeed (10) reaches f_n precisely under this equation, and (9)
excludes all real noninteger predecessors. The formula includes f_n
and every depth-one or depth-two predecessor, not just selected
axes/centres. B_0 contains only the origin. Distinct basins
have no common future and hence no actual groupoid arrow.

### 3.3 Full isotropy, time phases and packet identity

For a total map, a nonzero retained lag at z means
two different iterates of z agree; equivalently z is eventually
periodic. In the present map the complete source isotropy is
Z at every integer pair and trivial at every noninteger pair.

Let d(z)<=2 be the least entry depth into f_n for
z in B_n, and K(z)=sum_(i<d(z)) kappa(T^i z).
For z,w in B_n every integer lag ell occurs: choose
common-future depths beyond both entry times. Formula (7) gives

    c(z,ell,w)=K(z)-K(w)
                 -(ell-d(z)+d(w))*log(n+1).   (12)

Therefore the ENTIRE time image and extension kernel are

    z in B_n, n>=1:  H_z=log(n+1) Z, kernel={0};
    z=origin:         H_z={0}, kernel=Z;
    z noninteger:     H_z={0}, source/kernel={0}. (13)

No subset of loops or preferred inverse branch is used. At
the origin a zero-time source loop persists in the extension;
zero H is not absence of source isotropy. At other integer
points source loops have nonzero time and no extension isotropy.

On B_n x R for n>=1, equation (12) gives
the complete extension-object invariant

    h-K(z) modulo log(n+1).                      (14)

Changing depths only changes this by integer multiples of that
same logarithm. Conversely (14) equal means an actual arrow
exists, since all integer lags occur. Real translation acts
transitively on this circle with least positive time log(n+1).
The many finite source predecessors are phases of ONE packet,
not extra primitive packets. Distinct n cannot merge by arrows.
The origin quotient is a real line with residual isotropy Z;
all noninteger classes have trivial time stabilizer. These sectors
cannot hide additional positive primitives.

Consequently the GLOBAL positive primitive ledger is exactly

    one packet for each N>=2, least time log N,
    repetitions r*log N, r=1,2,..., of that SAME packet. (15)

For example f_3=(3,3) has H=log4 Z, which does
not contain log2. Its basin is disjoint from that of
f_1=(1,1), whose least time is log2. Numerical equality
log4=2 log2 cannot turn the first primitive into the
second packet's repeat. This already violates the prime-only primitive
ledger. Prime-time packets do occur once each, but so do
all composite-time primitive packets. STOP / FORK; no spectral rescue.

## 4. UNIT-DIVISOR control — its own zero clock

On the same full plane, T_U(x,y)=(y,x+y) has exact
image u>=0,v>=u and unique inverse (v-u,u). Its
own inverse absolute Jacobian is 1 at every point, so
kappa_U=c_U=0. Every source cycle has nondecreasing y;
equality at all steps forces x=0 and then y=0.
The origin is the ONLY periodic point and its unique
preimage is itself; there are no other eventual periods.
At origin source/extension isotropy is Z and H=0; elsewhere
all three groups are trivial. There is no positive primitive
anywhere. These are this control's inverse and return theorems.

## 5. SHEAR-OFF control — complete tested square and axes

Its map is T_S(x,y)=(y,(x-j)/m). Its complete
inverse branches on the original D have domains

    B<=u<B+1, q<=v<q+1/m,
    h_S(u,v)=(m*v+j,u), j=0,...,m-1.           (16)

The exact image is u,v>=0 with fractional_part(v)<1/m,
m=1+floor(u), and every image point has m distinct
predecessors. Each inverse has absolute determinant m, so its
OWN kappa_S=-log m, with the same affine boundary convention.
That algebraic equality does not identify its source with the main.

At a fixed point x=y=n+r, if n=0 the
map is the swap and every (r,r), 0<=r<1,
is fixed. If n>=1 its second output r/(n+1)
is smaller than n+r, so no further fixed points exist.

The entire unit square Q=[0,1)^2 is invariant and
T_S|Q is the swap. Formula (16) shows every target
in Q has its sole predecessor in Q: no outside
tail joins it. Diagonal points have least source period one;
all others have least source period two. Its clock is
zero throughout Q; H=0 and extension isotropy equals source
isotropy, Z or 2Z respectively. There are no positive
primitives in this square.

On the ENTIRE axes, for every real t>0,

    (t,0) <-> (0,t),                           (17)

with least source period two. Put n=floor(t). The
two step kappa sum is -log(n+1). When n>=1,
the FULL H is log(n+1)Z and the extension kernel
is trivial; for 0<t<1 it is zero with kernel
2Z, as already counted in Q. Origin has source/kernel
Z and H=0. Every finite predecessor of an axis cycle
is retained as the union of all its actual inverse iterates.
For a minimal-entry tail the isotropy is conjugate to 2Z,
and its time image and phases are those of that cycle;
no preceding path can shorten the least loop time. Different
t give disjoint cycle sets, hence no common future and
no tail merger. For each n>=1 this CONTROL thus has
continuum many distinct primitive axis packets of least log(n+1).
This is a lower-bound family, not a census of other
periodic points outside Q and the axes; those remain UNCLASSIFIED.

## 6. CARRY-OFF control — unit-square rational recurrence

This owner has T_C=(y,B+q+fractional_part(s+r/m)). On
the split by epsilon=floor(s+r/m), its complete inverses are

    h_C(u,v)=(m*(v-u+epsilon)+j,u),
    B<=u<B+1, B+q<=v<B+q+1,
    0<=m*(v-u+epsilon-q)<1,                    (18)

with q>=0, j=0,...,m-1 and epsilon=0,1. For an
equivalent exact image description write u=B+s,v=C+t with
0<=s,t<1. A preimage exists precisely when

    C>=B, fractional_part(t-s)<1/(B+1).         (19)

Then q=C-B, epsilon=0 if t>=s and 1 otherwise,
r=m*fractional_part(t-s), and all m distinct j supply
the predecessors. These follow by solving t=s+r/m-epsilon;
the half-open interval for r ensures uniqueness of epsilon.
No wrap boundary is deleted. On EVERY inverse piece the
absolute determinant is m, giving its own kappa_C=-log m
and all-point affine clock, not a borrowed main groupoid.

At a fixed point x=y=n+r, q=0 and j=n;
fixedness requires fractional_part(r+r/(n+1))=r. Thus r/(n+1)
is an integer epsilon in [0,1), forcing r=0.
All fixed points are exactly (n,n), n>=0. At n>=1
their full loop group is Z with H=log(n+1)Z and
trivial extension kernel; origin has H=0 and source/kernel Z.
Its fixed-core basins can also be computed within this owner:
if T_C(x,y) is an integer pair then s=0 and
fractional_part(r/m)=r/m must be zero, so r=0. Thus
its integer lattice is invariant and inverse-reflecting. On that
lattice its OWN update is (A,B)->(B,B+floor(A/(B+1))),
which reaches the same triangular sets (11) within two steps.
These are its complete fixed-core basins, by this separate proof;
this does not rule out other periodic cores off the lattice.

The ENTIRE Q=[0,1)^2 is invariant with

    (r,s) -> (s,fractional_part(r+s)),
    M=[[0,1],[1,1]] modulo Z^2.                 (20)

By (18)–(19) it is bijective and has no outside
predecessors: B=C=q=j=0, m=1. The inverse is
(fractional_part(t-s),s) in target fractional coordinates (s,t).
Thus this is the actual entire source component, not a
chosen section or a torus substituted for the half-open square.

ALL periodic points of (20) are exactly the rational pairs.
Indeed on denominator D the integer matrix with determinant -1
permutes the finite set (Z/DZ)^2, so every such pair
is periodic. Conversely if M^k z=z modulo Z^2,
then (M^k-I)z is an integer vector. The eigenvalues
of M are (1+sqrt5)/2 and (1-sqrt5)/2,
neither having any positive power equal to 1; therefore
M^k-I is invertible over Q and z is rational.
The bijection has no additional eventually periodic points in Q.
For a rational point of least source period a, its
source and extension isotropy are aZ, but H=0 because
m=1 throughout Q. Irrational pairs have all groups trivial.
For example (1/2,0)->(0,1/2)->(1/2,1/2)->(1/2,0)
is a genuine source 3-cycle with ZERO closed time,
including its wrap at r+s=1. Higher cycles outside Q
are UNCLASSIFIED; the fixed and full-square gates suffice here.

## 7. Synthesis, adverse checks and portfolio decision

The full main owner, not just a chosen grid, has been
audited. The lattice appears as a PROVED complete eventual-return
locus, not as a restriction of the carrier. All real
noninteger points, every finite predecessor, all axes and null-version
choices remain. Positive closed packets really exist, but (15)
is an all-integer ledger: divisibility as an observable has
not supplied prime-selective recurrence. Equal clocks across different controls
do not transfer their orbit classifications or repair this defect.

T0 carrier/same-object ownership and the owned part of T1
are established by elementary proofs. Stronger arithmetic naturalness remains
OPEN. T2's full return/primitive classification is established but
its prime-only target FAILS. T3 NOT SUPPLIED / NOT
PURSUED after the decisive gate. Classical symplectic base, mapping
torus, positive roof and A0/A1/A2 NOT APPLICABLE;
formal Route coordinates UNASSIGNED; Route B NOT INVOKED.

ARS raw-card, synthesis and final-adverse checkpoints are reported in
the [review](evidence/independent-review.md) and [evidence](evidence/README.md).
They are shared-history internal AI checks, NOT_CALIBRATED, not
external peer review or independent-error evidence. No scientific numerics,
precision cutoff, external literature expansion or operator computation supports
these theorems; all proofs and exact input formulas are above.

Portfolio: STOP positive-prime-ledger promotion; retain this complete negative
and its positive/zero-time controls; FORK only to a separately
defined and frozen owner. No selective deletion of composite cores,
new measure, prime table, roof or changed packet equivalence is
authorized inside GAC01. Positive 304 and all older packages
stay unchanged; 241/242 paused; programme goal active.
