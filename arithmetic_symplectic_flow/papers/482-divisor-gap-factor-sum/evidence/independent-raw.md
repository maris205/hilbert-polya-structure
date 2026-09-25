# DGF01 — independent frozen-card derivation

Date: 2026-09-25. Candidate: `ANG-20260925-DGF01`.
Package: `482-divisor-gap-factor-sum`, batch `PRE-P0-STRUCTURE-20260925-AA`.
Reviewer: `pcr01_independent_review`, separate from the author/helper.

## 0. Release, input and limits

This proof began after DISTINCT RAW RELEASE and root's reported FULL read
of the 188-line CP1 report. Sole scientific input: clarified candidate
card, 97 lines, personally reread 1–97 EOF (request 1–125), SHA-256
`74d6ee846d89f2f19d69f360a2aa36568385d2f46674c183f65271ad62098402`.
Its original 87-line prefix remains
`fb8a360abd0abd5489676b70b990a55dd258ca69019fefc9cf5cb11369ad0f89`.
Scope report SHA-256:
`7f63d339d01da2156099329e890082271785ed7e5900b65a5b30efd4a370d71e`.

No author file, current peer/helper proof or old proof was opened. The
method is exact partition, affine-measure, integer-equation and history
algebra, with no scientific program, numerics, network, Git, PDF or 485.
ARS instruction reads/adaptation and inherited exposures are recorded in
the immutable CP1 report. Same-model/shared-history `NOT_CALIBRATED`;
not blind, outcome-sealed, human, external or cross-model verification.
There is no higher-period search. Conditional cycle structure below is
not a census. The pre-proof target uses ACTUAL primitive L=log p, without
rescaling/merging, and separates nonemptiness, purity, uniqueness and coverage.

## 1. Whole carrier, full partitions and four actual maps

Let X = N_{>=1} times [0,1] with the product Borel structure and original
mu = counting times Lebesgue. It is sigma-finite: each integer level has
measure one. Every endpoint and cut remains a point of the full carrier,
even though each singleton is null. The discrete counting factor is one
at both the source and target levels of a single branch.

For fixed N, list divisors as 1=d_1<...<d_t=N, put d_0=0, and write
e_N(d_i)=d_{i-1}. Their positive gaps sum to N. Consequently the intervals

    [d_{i-1}/N,d_i/N), i<t;       [d_{t-1}/N,1], i=t

are disjoint and cover [0,1], with every internal cut assigned to its
right branch. These are the M/F intervals with l=e/N and w=(d-e)/N.
A has N consecutive equal intervals with l=(d-1)/N,w=1/N, d=1,...,N.
U has t consecutive equal intervals with l=(r-1)/t,w=1/t, label d_r.
In each case only the last interval is closed at 1. All widths are positive.

Write b for an actual own branch label, I_{U,N,b} for its source interval,
and (l,w,f) for its left endpoint, width and new integer:

| Owner | Label and own l,w | f_U(N,b) |
| --- | --- | --- |
| M | d divides N; e/N, (d-e)/N | d+N/d |
| A | 1<=d<=N; (d-1)/N, 1/N | d+floor(N/d) |
| F | d divides N; e/N, (d-e)/N | N+1 |
| U | divisor d of rank r; (r-1)/tau(N), 1/tau(N) | d+N/d |

Each full map is

    T_U(N,x) = (f_U(N,b), (x-l)/w), x in I_{U,N,b}.

Nonlast branches map onto the WHOLE [0,1) at their target level; last
branches map onto the WHOLE [0,1]. Thus every map is total and Borel, and
all D_{U,r}=X. At N=1 there is exactly one branch, l=0,w=1, and all four
maps send (1,x) to (2,x); there are not two endpoint/unit branches.
Future parsing uses the new integer and the actual new coordinate.

For all owners, w<=1, with equality exactly at N=1. Indeed for N>1
the divisor partitions have at least two positive parts, as do the equal
partitions used by A and U. All target integers f_U are at least 2.
These facts will keep zero-clock steps without mislabeling them as cycles.

## 2. Exact entire inverse atlas and all-point original IMAGE

For every actual branch (U,N,b), put m=f_U(N,b) and let V_b be [0,1]
for its last branch and [0,1) otherwise. Its inverse is

    theta_{U,N,b}(m,v) = (N,l+w v),        v in V_b.

The two inverse identities hold pointwise on their entire displayed
domains, since x=l+w v reverses the affine update. Inclusion of v=1
only for a last branch is essential: it is not replaced by an a.e. rule.
Each branch is a Borel bijection and there are countably many branches.

For any target y=(m,v), all actual predecessors are enumerated as follows:

| Owner | Enumerate candidate integers/labels, then use own x=l+w v |
| --- | --- |
| M/U | Every ordered d,q>=1 with d+q=m; N=dq; branch labelled d |
| A | Every ordered d,q>=1 with d+q=m; every integer dq<=N<d(q+1), d<=N |
| F | N=m-1>=1 and every divisor d of N |

In each row impose the own last/nonlast v-domain and recheck the source
branch and integer law. This gives an exact set Pre_U(y), not a multiset.
Soundness is the inverse identity. Conversely a predecessor's actual d
and q=N/d, or q=floor(N/d) for A, supply exactly one of the enumerated
choices; F's source integer is forced. This proves completeness, including
empty fibres and all overlaps. In A, the half-open integer inequality is
equivalent to the floor condition. Actual source branch uniqueness prevents
duplicate label copies of one source; distinct predecessors are all kept.
Each fibre is finite, although arbitrary depth is retained below.
The target level m=1 has no predecessors, not a deleted unit.

For every Borel E in a displayed target branch, the actual affine inverse
has original-measure image

    mu(theta E) = w mu(E) = integral_E w dmu.

This is the real affine scaling identity on that level, with counting
factor one; it holds for arbitrary Borel sets, including endpoint/null
sets, not just intervals. The frozen every-point version is J_theta=w
from that affine germ, including every legal boundary point. No a.e.
uniqueness argument or incoming-branch multiplicity supplies its values.

The owned legal clocks therefore are

    kappa_M(N,x) = kappa_F(N,x) = log[N/(d-e_N(d))] on their own d branch,
    kappa_A(N,x) = log N,
    kappa_U(N,x) = log tau(N).

They are nonnegative, zero exactly at N=1. These are separate original
IMAGE computations for the four maps. They are not a common clock copied
from M, nor a predeclared strictly positive roof on the full X.

## 3. Exact lineage interface

Take integer 1<D<N and x=(D-1/2)/N. If D divides N, its previous divisor
e is an integer <=D-1, so e/N < x < D/N; hence its actual branch is D.
If D does not divide N, let d_+ be the least divisor strictly above D,
which exists because N is a divisor. Its previous divisor e is <=D-1,
and e/N < x < d_+/N, so the selected branch is d_+, not D. This proves
the declared iff and the next-divisor alternative on the whole stated
interface. The feedback law then changes the next integer partition.
It is an exact symbolic-admissibility/geometric-gap connection, not proof
of strong naturalness, a prime-only clock or a symplectic realization.

## 4. Full retained histories, cocycle and history-pair IMAGE

Fix one owner U. Every iterate is legal. Define

    W_r(z) = product_{i=0}^{r-1} w_U(T_U^i z),   W_0=1,
    S_r(z) = -log W_r(z),                       S_0=0,
    G_U = {(z,r-s,y): T_U^r z=T_U^s y, r,s>=0}.

All W_r are positive. Arrows are equal triples only, with source y and
range z; lag is retained, not replaced by the choice of branch labels.
The units, inverse and multiplication are

    (z,0,z),  (z,k,y)^-1=(y,-k,z),
    (z,k,y)(y,l,u)=(z,k+l,u).

Composition exists: for witnesses (r,s) and (a,b), advance the intermediate
y histories to n=max(s,a). This gives witnesses (r+n-s,n) and
(n,b+n-a), whose composite has the required lag. All advances are legal.
Define

    c(z,r-s,y)=S_r(z)-S_s(y)=log[W_s(y)/W_r(z)].

If two witnesses have the same lag, their two indices differ by the same
integer; compare the smaller pair to the larger one. Their common future
adds the same clock to both sums, so the difference is unchanged.
The same intermediate advancement makes the two intermediate S_n(y)
terms cancel in composition, proving additivity. All objects are Borel
on their countable actual-history atlas. In particular,

    c(T_U z,-1,z)=-kappa_U(z), with witnesses (0,1).

A finite branch itinerary restricts one integer level to a Borel interval
(possibly empty or an endpoint), with positive affine slope 1/W_r and
injective forward map. Its inverse IMAGE version is W_r at every point,
by successive affine identities. Finite itineraries are countable and
cover all histories, without any integer/depth cutoff.
Zero-step charts are identities on integer levels and together cover X.

For two itinerary charts F_r:B->V and F_s:C->Y, match their images at
K=V intersect Y. The history-pair chart F_r^-1 o F_s has source
F_s^-1(K), and on every Borel E in that domain its image measure is

    mu((F_r^-1 o F_s)E)
      = integral_E [W_r(F_r^-1 F_s y)/W_s(y)] dmu(y)
      = integral_E exp[-c(F_r^-1 F_s y,r-s,y)] dmu(y).

Each ratio is constant on a fixed itinerary pair and is its actual affine
germ derivative; thus the prescribed all-point version is retained even
on a singleton chart. These charts cover every arrow with all overlaps
identified by triples, not counted as new copies.

## 5. All-depth incoming and exact source/phase tests

For each of the four exact Pre_U sets in Section 2 define

    Pre_U^0(y)={y},
    Pre_U^{n+1}(y)=union_{v in Pre_U^n(y)} Pre_U(v).

Induction gives Pre_U^n(y)={z:T_U^n z=y}: the next inverse is an actual
one-step predecessor, and any actual (n+1)-step path factors that way.
This proves soundness and completeness at every depth, without a bound.
All finite histories are their compatible chains; all infinite incoming
histories are exactly the infinite compatible chains z_0=y with
T_U z_{i+1}=z_i. No arbitrary choice of one predecessor replaces them.

The entire incoming arrow set and source orbit of z are, with equal
triples deduplicated,

    G_U^z={(z,r-s,y):r,s>=0, y in Pre_U^s(T_U^r z)},
    O_U(z)=union_{r,s>=0} Pre_U^s(T_U^r z).

These are necessary and sufficient tests: membership supplies actual
meeting witnesses and every arrow supplies one membership. For all real
heights h,k the extension-orbit test is exactly

    (z,h) ~ (y,k)
    iff some r,s>=0 satisfy T_U^r z=T_U^s y
                         and h-S_r(z)=k-S_s(y).

Thus full incoming, non-eventual points and all heights are included,
not only returns, centres or equal-time representatives. Endpoint inverse
restrictions from Section 2 remain imposed at every depth.

The three exact kernel tests are

    ker lag={(z,0,y): some r has T_U^r z=T_U^r y},
    ker c={(z,r-s,y): T_U^r z=T_U^s y and W_r(z)=W_s(y)},
    ker(lag,c)={(z,0,y): some r has T_U^r z=T_U^r y and W_r(z)=W_r(y)}.

The clock and joint tests are independent of witness by descent. They
include all actual equal-depth mergers, not only units. At N=1 the genuine
forward arrow ((2,x),-1,(1,x)) has c=0 for every owner and every x;
nonzero-lag zero-clock arrows cannot be discarded.

## 6. Conditional source isotropy, ENTIRE H and every real phase

For a point whose forward path is not eventually periodic, equality of
two different forward times is impossible, so source isotropy is trivial.
If its eventual cycle has least source period ell, source isotropy is
ell Z: differences of equal times on the cycle are exactly multiples of
ell, and any multiple can be witnessed after cycle entry. This applies
also to every transient point feeding the cycle.

Let L be the sum of the actual ell clocks on that cycle. No cycle contains
N=1, since no target integer is 1. All its widths are therefore strictly
less than one, so L>0. A positive-lag isotropy generator ell has clock L;
every isotropy arrow of lag n ell has clock nL. Thus the extension
isotropy (clock-zero source isotropy) is trivial everywhere, both on
non-eventual and eventual-periodic components, while source isotropy need
not be trivial. The whole period group of height translation is exactly

    H_z=c(Iso_G(z)) = {0} on non-eventual components,
    H_z=L Z on an eventual least-ell cycle component.

There are no additional real periods: a height translation returning an
orbit class must be witnessed by an arrow from its chosen source object
to itself, hence by source isotropy. Conversely each such clock is an
actual stabilizing translation. Consequently an actual cycle has physical
primitive L, not a proper divisor of L, with repetitions nL for n>=1.

For every source component choose an object only as a coordinate anchor,
not as a selected subowner. Its full real phase space is R/H_z. An arrow
from the anchor to another object changes h by its actual c; different
choices of arrow differ by H_z. On a cycle component an equivalent
coordinate is h-S_a(z) modulo L, where a is any actual arrival at the
chosen cycle anchor. Later arrivals differ by whole cycle sums. On a
non-eventual component H=0 and all real phases remain distinct. The
exact orbit test in Section 5 defines these statements on the full object
without requiring a smooth quotient or a global measurable section.

Distinct source components are not merged when their L values or phases
coincide. A cycle component has one closed translation orbit with all its
phase classes; those phases are not extra primitive packets. This entire
conditional ledger asserts no location of a higher-period cycle.

## 7. Complete global fixed-state solution for M and U

For either M or U, integer return at a fixed state forces, with N=dq,

    dq=d+q,  equivalently (d-1)(q-1)=1.

Positive integers force d=q=2 and N=4. This is exhaustive for every N,
including N=1, with no cutoff. At N=4 the divisors are 1,2,4.

For M the d=2 interval is [1/4,1/2), l=1/4,w=1/4. Real fixedness is
x=(x-1/4)/(1/4), hence the unique solution x=1/3 lies strictly inside.
For U the same divisor has rank 2 among 3, interval [1/3,2/3),
l=1/3,w=1/3; fixedness gives the unique interior solution x=1/2.
Thus the COMPLETE fixed sets are

    Fix_M={p_M}, p_M=(4,1/3), with L_M=log 4,
    Fix_U={p_U}, p_U=(4,1/2), with L_U=log 3.

No endpoint, cut, other branch or fixed continuum is omitted: all other
integer/branch choices have already failed the integer equation, and
each remaining real equation is linear with nonzero coefficient.

For Q in {M,U}, at p_Q source isotropy is Z and extension isotropy is trivial;
the ENTIRE H is L_Q Z, phases are R/(L_Q Z), and repetitions are nL_Q.
Each contributes exactly ONE primitive packet, not one for every phase.
MAIN's actual primitive log 4 is not log p for an ordinary prime; 4=2^2
does not permit replacing the least positive period by log 2. U's log 3
is prime-valued, but belongs to the different geometry and different point.

The complete first incoming levels, directly from the entire atlas, are

    Pre_M(p_M)={(3,1/9), (4,1/3), (3,5/9)},
    Pre_U(p_U)={(3,1/4), (4,1/2), (3,3/4)}.

Every further incoming level is the exact recursion of Section 5, not a
restriction to these displayed integers. For Q in {M,U} and p=p_Q the full
source packet is B_Q(p)=union_{a>=0} Pre_Q^a(p); it equals O_Q(p), since p is fixed.
All incoming chains, including the compatible infinite chains, are kept.
The constant inverse chain at p is one such chain, not a replacement for
the others. At every z in B_Q(p), if T_Q^a z=p, the full phase test is

    h-S_{Q,a}(z) modulo L_Q.

It is independent of the arrival time modulo L_Q, and two such extension
points belong to the same orbit exactly when these residues agree.
Their source/extension isotropy and entire H are the core's ones. This
gives all actual incoming and all real phases, not just the core itself.

## 8. Complete global fixed-state solution for A

At a fixed state N=d+floor(N/d). The endpoint labels d=1 and d=N each
give N+1 instead, so 1<d<N. Writing q=N-d, the floor equation is

    d(N-d)<=N<d(N-d+1).

The left inequality implies N<=d^2/(d-1)=d+1+1/(d-1), while N>=d+1.
For d>=3 this forces N=d+1; for d=2 it permits only N=3 or 4. Each
listed case satisfies the right inequality as well. Hence the complete
integer-return branches are d=N-1 for every N>=3, plus N=4,d=2.

Because w=1/N and l=(d-1)/N, real fixedness is

    x=(d-1)/(N-1).

For d=N-1 this gives p_N=(N,(N-2)/(N-1)). It belongs strictly to its
nonlast interval: it is greater than (N-2)/N, and less than (N-1)/N
since N(N-2)<(N-1)^2. The extra N=4,d=2 gives q_4=(4,1/3), also interior.
There are no other fixed coordinates or exceptional N=1 solutions.
Therefore

    Fix_A={p_N:N>=3} union {q_4},
    L(p_N)=log N,              L(q_4)=log 4.

These are distinct fixed points, including p_4=(4,2/3) and q_4=(4,1/3).
Two distinct fixed points cannot have an equal-future arrow, since all
their forward iterates remain those different points. Their full basins
are therefore disjoint source packets. Equal log 4 does not merge the two.
Every fixed packet has source isotropy Z, trivial extension isotropy,
ENTIRE H=(log N)Z at its core and basin, primitive log N, and all positive
repetitions. All phases R/((log N)Z) remain in each packet.

The entire fixed-packet multiplicity ledger is: no fixed packet for
N=1,2; one log N packet for each N>=3 except N=4, which has two.
Thus this fixed ledger contains one log p packet for every prime p>=3
and composite-log packets as well. This does not prove global uniqueness
of prime packets or rule out a log 2 packet at a higher source period.

For EVERY fixed p=(m,v) just listed, v is interior. Its exact first
incoming set has the uniform closed formula

    Pre_A(p) = {(K,(d-1+v)/K):
                 1<=d<=m-1,
                 d(m-d)<=K<d(m-d+1), K integer}.

Here q=m-d>=1 ensures K>=d, and v<1 makes every proposed target legal.
Actual branch reconstruction verifies every entry; the inverse atlas
proves there are no others. All deeper levels and compatible infinite
chains are obtained by the unrestricted Pre_A recursion, including points
at integers outside the fixed-core family. The full incoming packet is
exactly B_A(p)=union_a Pre_A^a(p). For any such point z, choose an actual
arrival time a; its complete phase is h-S_{A,a}(z) modulo log m. This
is the same necessary-and-sufficient phase test as in Section 7, with all
transients and real heights retained separately for every fixed packet.

## 9. Complete F control, without a periodic census

Fixedness would require N+1=N, which has no solution. Thus Fix_F is empty
on the whole X, not just a bounded window. More strongly, the exact
identity integer(T_F^r(N,x))=N+r rules out any equality of two distinct
forward times. This is a global monotonicity proof, not a higher-period
search. Therefore F has trivial source and extension isotropy everywhere,
ENTIRE H={0}, all real phases R on each source component, and no positive
primitive translation packets or repetitions anywhere.

Its complete inverse at target (m,v) is the Section 2 list at N=m-1.
Every backwards step lowers the integer by one, so Pre_F^a(m,v) is empty
for a>=m. All shorter levels are determined by the exact own partition
recursion, retaining endpoints; there is no compatible infinite backward
history ending at any finite m. Source orbits still include all points
meeting a future of the target, as in Section 5, so finite predecessor
depth is not a claim that a source orbit is finite or an isolated unit.
The global nonemptiness failure belongs to F only and is not evidence
that MAIN has no positive packets.

## 10. Gate decision, ownership and separate target clauses

The original-measure partition/inverse/IMAGE ownership chain is established
for each full owner, with every endpoint, cut and N=1 unit retained.
The decisive MAIN witness is its unique global fixed core p_M=(4,1/3):
its actual least positive primitive is log 4, ENTIRE H=(log 4)Z, and no
incoming arrow supplies a half-period. Hence MAIN positive nonemptiness
is established, while prime-only purity fails. The frozen rule gives
STOP / FORK without any higher-period census or measure/gap/law repair.

The four target clauses must not be conflated:

| MAIN clause | What this bounded proof establishes |
| --- | --- |
| Positive nonemptiness | YES, the actual log 4 packet |
| Prime-only purity | NO, log 4 is not log of an ordinary prime |
| At-most-one packet per prime | OPEN globally; not decided by this fixed ledger |
| All-prime coverage | OPEN globally; not decided by this fixed ledger |

The A comparison is an arithmetic-discrimination warning: it retains an
own log 4 fixed packet at the same coordinates as p_M and many further
fixed packets, including a second distinct log 4 packet. U changes both
the real fixed coordinate and its actual clock to log 3; transferring
that value to M would change the owner. F retains branch geometry but
its monotonically increasing integer has no return packet. None repairs
MAIN. Empty fixed sets in general are not claimed to imply globally empty
positive ledgers; the stronger F conclusion used its separate proof.

Strong naturalness/PROVES_TOO_MUCH beyond these controls, higher-period
locations/census, and global prime coverage/uniqueness remain OPEN or
NOT AUDITED. Source periodic points are not globally declared absent.
No rescaling, packet merging, chosen-centre restriction, clock insertion,
external prime/zero data or different measure is introduced.

Outcome: OWNED DIVISOR-GAP IMAGE; NONPRIME FIXED PRIMITIVE — STOP / FORK.
Classical fields NOT APPLICABLE; T1 NOT PASSED; T3 NOT AUDITED; formal
coordinates UNASSIGNED; Route B NOT INVOKED. No trace, operator, zeta,
determinant, spectral or RH claim is made.

Freeze after complete self-read and hash receipt. HOLD for root's full raw
read and a distinct PAPER UNLOCK before any author-surface comparison.
