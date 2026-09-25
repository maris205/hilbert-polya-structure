# Partial fixed-stride transport: legal arrow images and terminal splitting

Paper453; candidate `ANG-AUDIT-20260924-PST01`.
2026-09-24; conditional exact theorem and external controls.
outcome: EXACT PARTIAL-STRIDE IMAGE; TERMINAL SPLITTING; RATIONAL PACKET OBSTRUCTION

## Abstract

For one measured partial deterministic map with prescribed all-point inverse
IMAGE densities, uniform stride r defines a new partial owner on the SAME
full carrier. Its clock is the legal r-step sum. We prove the exact embedding
of its retained-lag groupoid into the parent's. Divisible lag is sufficient on
infinite histories but can fail at a terminal: the earliest common witness
must permit the extra steps needed to reach multiples of r. Terminal packets
split by actual sampled endpoints, not only depth residues. Infinite aperiodic
classes split into r classes; a least-q cyclic basin splits into gcd(q,r)
basins with primitive multiplier raised to r/gcd(q,r). Consequently uniform
stride cannot satisfy the nonempty, prime-pure, multiplicity-one benchmark
when every nonzero parent multiplier is rational. Four full-carrier controls
show composite clocks, duplicated prime packets, the irrational boundary, and
strict loss of zero-lag merging arrows at terminals. This is a transport audit,
not a prime-arithmetic candidate, a symplectic realization or a Route pass.

## 1. Owner, question and provenance

The [card](candidate-card.md) fixes a standard Borel X, sigma-finite mu,
partial Borel T:D->X and a countable disjoint Borel injective partition of D.
Each branch has its actual Borel inverse theta_i on Y_i and a positive finite
ALL-POINT Borel J_i such that, for every Borel E subset Y_i,

    mu(theta_i E) = integral_E J_i dmu.                       (1)

The prescribed versions at null points are part of the input. Equation(1)
alone does not uniquely determine them there. No later reweighting is allowed.
The own clock is kappa_T(z)=-log J_i(Tz) on its actual source piece. Terminal
points X\D remain objects with units and every incoming history, without an
outgoing clock or artificial identity evolution. Signed and zero clocks stay.

Fix integer r>=2. R=T^r has domain D_r of r actually legal steps and the SAME
X,mu, including intermediate points and terminals. It is not a selected
section, a roof division, an extra sheet or a completion of T. The audit's
lineage is finite symbolic batching -> actual partial evolution -> full
measured packet ledger. No arithmetic source is supplied. Classical symplectic
space/map/positive roof are NOT APPLICABLE; operator/trace/zeta are not built.

The question deliberately extends the TOTAL-only scope of the earlier423
card to its excluded partial-terminal boundary. Root's bounded collision
read of that card1–88 included its original83-line contract and the beginning
of its Outcome; no old proof was read or imported. Exact exposure hash and
pre-freeze informal feasibility thought are disclosed in the new card. The
total-cycle consequences below are rederived, not claimed as newly discovered
total-map facts. No global novelty or nonconjugacy certificate is asserted.

## 2. The sampled owner's inverse IMAGE is its own

For a source word (i_0,...,i_{r-1}), restrict to those z with all r steps
legal and T^jz in the indicated actual piece. These countably many Borel
pieces partition D_r and R is injective on each. Its inverse is the actual
composition theta_i0 ... theta_i(r-1), restricted by every intermediate
domain test. The target domain is Borel: test theta_i(r-1)(y) in the next
inverse domain, then continue backwards. Both inverse identities follow by
successive cancellation; every legal preimage supplies exactly such a word.
There is no target-next-step admission condition.

At y=Rz the frozen sampled inverse version is

    J_R(y) = product_{j=0}^{r-1} J_i(j)(T^{j+1}z).           (2)

It is finite positive at every actual point, including null states. Applying
(1) successively proves its own IMAGE identity. More explicitly, (1) first
extends from indicator functions to nonnegative Borel functions by simple
approximation; apply that identity at each composition. This gives
mu(theta_word E)=integral_E J_R dmu for EVERY Borel E in the actual domain,
not merely for rectangles or almost everywhere versions. It also proves

    kappa_R(z)=S^T_r(z),     S^R_n(z)=S^T_{rn}(z).           (3)

Here S is the sum along legal steps and S_0=0. Formula(3) is derived from
the sampled measure owner, not copied from a parent one-step clock.

## 3. Actual histories, all kernels and phase convention

For either U=T or R retain all triples

    G_U={(z,m-n,w): U^m z=U^n w legally; m,n>=0}.

Source is w, range z; equal triples, not just endpoint pairs, are identified.
Define lag ell(z,k,w)=k and c_U=S^U_m(z)-S^U_n(w). For two witnesses of the
same triple, their time pairs differ by a common integer. Starting from the
earlier pair, the added common tail is legal because the later pair exists;
its sums cancel. Thus c is well-defined even at terminal boundaries.
To compose two arrows, align the two witness times at their shared object
to their maximum. The longer of the ALREADY LEGAL middle histories supplies
exactly the needed continuation for the other witness. No continuation past
a terminal is presumed. This proves closure, additive lag and additive c;
inverse negates both, and units have zero. In particular (Uz,-1,z) has
clock -kappa_U(z), which fixes the sign convention throughout.

The full extension has objects X x R and arrows (w,h)->(z,h+c_U).
Physical time is unrestricted height translation on its orbit SET. We do
not assert a nice topological quotient or a global measurable selector.
For every owner the exact full kernels are

    K_lag={g:ell(g)=0}, K_clock={g:c(g)=0},
    K_joint=K_lag intersect K_clock.                       (4)

They include all merging arrows meeting these equalities, not just units.
The descriptions below turn(4) into complete classwise formulas, including
every incoming depth. Source isotropy is G_z^z; extension isotropy is its
subgroup c=0. Entire height-return group H_z=c(G_z^z) is the stabilizer of
height translation at the extension orbit of (z,h), independent of h.
A nonzero H=LZ has primitive L>0 and all positive integer repetitions nL.
H=0 yields no positive period, even when source isotropy is nontrivial.
One cyclic source component with H nonzero is one physical periodic packet:
its phases form R/H and height translation is transitive on that circle.
Different source components never become one packet because L agrees.

## 4. Exact arrow embedding: the terminal test

There is an injective groupoid homomorphism

    iota:G_R -> G_T,       (z,k,w) -> (z,rk,w),             (5)

preserving c by(3). It is identity on objects. Its image consists EXACTLY
of parent triples admitting a witness with BOTH witness times divisible by r.

For a more explicit test, fix a parent triple g=(z,k,w). Among its witness
pairs choose the earliest (a,b), equivalently the least b with a-b=k.
Every other witness is (a+j,b+j) for an integer j>=0 along the common
future of v=T^a z=T^b w. Conversely all such legal continuations are
witnesses. Let N(v) be the number of remaining legal steps, possibly infinity.
Then

    g in image(iota) iff k in rZ and N(v)>=(-a mod r),     (6)

where the right residue is in {0,...,r-1}. Indeed a+j and b+j can both be
divisible by r exactly under these two conditions. Earliest is important:
an arbitrary later witness could have used up legal padding even though an
earlier divisible witness existed. On infinite histories N(v)=infinity,
so divisibility is sufficient. Formula(6), not a total-map padding argument,
handles every terminal merging history. Clock compatibility does not restore
arrows that(6) excludes. The images of sampled kernels are the image in(5)
intersected with the corresponding parent kernels (lag zero included).

## 5. Complete components and incoming histories

Every deterministic forward history is terminal-ending, infinite without an
eventual cycle, or eventually on a unique finite least-period core. Related
points share the same case. We classify all three, not a bounded orbit list.

### 5.1 Terminal-ending

Put N(x)=maximal legal T length and p(x)=T^{N(x)}x. Two terminal-ending
points are T-related iff they have the same p. The unique arrow between z,w
in such a class has lag N(z)-N(w). Set B_T(x)=S^T_{N(x)}x; its clock is
B_T(z)-B_T(w). Thus(4) says respectively equal N, equal B_T, or both;
zero-lag merging need not be a unit. Isotropy and H are zero. The complete
phase coordinate is h-B_T(x) in R, with no phase selected or discarded.

For R the corresponding exact quantities are

    N_R(x)=floor(N(x)/r), p_R(x)=T^{r N_R(x)}x,
    B_R(x)=S^T_{r N_R(x)}x.                               (7)

Within one parent class, ALL sampled classes are indexed by the distinct
actual points v in that class with N(v)<r. The class for v is precisely
{x:p_R(x)=v}; it includes v and all actual R-incoming histories, at every
depth. Its arrows have lag N_R(z)-N_R(w), clock B_R(z)-B_R(w), kernels given
by their equality conditions, zero source/extension isotropy and H=0, and
all phases h-B_R(x). A residue N(x) mod r alone does not identify v when
incoming branches differ. No finite depth cutoff or artificial terminal
self-loop occurs in(7).

### 5.2 Infinite non-eventual classes

Fix one reference b in such a parent class purely to write coordinates.
Between any related endpoints there is exactly one lag: two different lags
would give a repeated forward value and hence eventual periodicity. Write
d(x)=ell(x,*,b), B(x)=c(x,*,b). All parent arrows then have lag d(z)-d(w)
and clock B(z)-B(w). Moreover d(Tx)=d(x)-1, so every residue mod r occurs.
By(6), precisely r R-classes occur, indexed by d mod r; inside each, the
R lag is (d(z)-d(w))/r and its clock is still B(z)-B(w). This includes
every incoming merge of divisible parent lag. For both owners the kernels
are equality of d, of B, or both, restricted to the relevant class. All
source/extension isotropy and H are zero. Every phase is h-B(x) in R.
These coordinates require no measurable choice across different classes.

### 5.3 Eventual least-q cores, including all incoming points

Let the parent core be v_j=T^jv_0, j=0,...,q-1; put
A_j=sum_{i<j}kappa_T(v_i), C=A_q. For any x in its FULL basin, let n(x)
be its first core entry and j(x) the entered index. Define

    t(x)=n(x)-j(x), B(x)=S^T_{n(x)}x-A_{j(x)}.

Complete parent arrows are exactly

    k=t(z)-t(w)+q a,   c=B(z)-B(w)+a C,   a in Z.          (8)

Necessity follows by comparing sufficiently advanced core positions;
sufficiency follows by advancing both histories far enough, which is legal
on this infinite tail. Thus all inverse branches and all incoming depths
are included, without selecting only core points. Formula(8) and k=0/c=0
give the FULL three kernels. Source isotropy is qZ, with c(aq)=aC;
extension isotropy is qZ if C=0 and {0} otherwise, and H=CZ. Phase is
h-B(x) modulo CZ (R itself when C=0). Any further incoming branch changes
B and the displayed representative, not H or the primitive abs(C).

For R set g=gcd(q,r). All g cyclic components, with their entire basins,
are indexed by t(x) mod g. On the core this is the usual stepping by r
modulo q. There are g distinct cycles of least R-period q/g. Explicitly
every sampled arrow is

    r k=t(z)-t(w)+q a,   c_R=B(z)-B(w)+a C.               (9)

For endpoints with equal t mod g the integer congruence is solvable, and
(6) gives all solutions; otherwise there is no arrow. This proves coverage
and all incoming assignments, including branches arriving at different
parent phases. Along each R-core one traverses r/g entire parent cycles:

    C_R=(r/g)C, source isotropy=(q/g)Z,
    H_R=(r/g)C Z.                                       (10)

Extension isotropy is (q/g)Z if C=0, else zero. Kernels are exactly(9)
with k=0, c_R=0, or both. For each component choose a core reference v;
let L(x) be any actual number of R steps from x to v. All phases are
h-S^R_{L(x)}x modulo C_R Z; different choices differ by that group.
If C_R=0 this is a real phase, and zero-clock source isotropy survives.
If C_R!=0 each of the g packets has primitive (r/g)abs(C) and all its
positive integer repetitions. No division by q, incoming depth or gcd is
performed on the whole return group beyond the explicitly proved(10).

## 6. Rational-parent obstruction and its exact scope

Assume for EVERY nonzero parent C that a=exp(abs(C)) is rational>1.
The sampled multiplier of each associated packet is a^h, h=r/g a positive
integer. If a=A/B is reduced and a^h is an ordinary prime p, unique integer
factorization gives B=1 and A^h=p, hence h=1 and A=p. Therefore a prime
sampled packet requires g=r>=2, in which case the SAME parent core produces
r distinct sampled packets of exactly that prime length. Multiplicity one
fails. If no nonzero parent C exists, all sampled H are zero and nonemptiness
fails. Thus no object in this rational subclass meets the full necessary
benchmark after a uniform stride r>=2. The proof needs neither all-prime
coverage nor a finite count of parent cores. Irrational parents are expressly
outside it; a rational theorem is not a universal acceleration theorem.

## 7. Four external controls on their WHOLE carriers

### A and C: all real dilations

For T_a(x)=a x on R with Lebesgue, a>1, the single inverse x/a has own
all-point IMAGE J=1/a and kappa=log a. For r=2, R_a=a^2 x has inverse
x/a^2, IMAGE1/a^2 and kappa_R=2log a, by direct substitution for every
Borel set, including the prescribed versions at x=0. Full arrows satisfy
z=a^{-k}w with c=k log a; sampled arrows satisfy z=a^{-2k}w with c=2k log a.
All three kernels are units. The origin is the ONLY eventual periodic core;
no nonzero point ever reaches it. Its source isotropy is Z for each map,
extension isotropy0, and H respectively log(a)Z and 2log(a)Z. Every nonzero
class is its full signed geometric orbit; no positive/negative half-carrier
is removed. Such classes have isotropy/H0, phases h+log|x| in R, and each
parent class splits into two sampled classes. Origin phases are h modulo
the indicated H; every positive integer repetition remains.

A has a=2: the parent sole primitive log2 becomes log4, which is composite.
C has a=sqrt5: the parent sole primitive log(sqrt5) is not prime-log, while
the sampled sole primitive is log5, with multiplicity one. There are no other
positive packets in either owner. C is a sharp boundary to a rational-parent
claim, not a counterexample to Section6 and not an endogenous arithmetic
construction: the geometric coefficient5 was supplied as external design data.

### B: two sheets and a genuine parent period two

T(x,j)=(sqrt2*x,j+1 mod2) on R x Z/2 owns Lebesgue x counting. Its unique
inverse is (y/sqrt2,l-1), J=1/sqrt2 at every point. R(x,j)=(2x,j) has own
inverse(y/2,j), J_R=1/2. Product substitution proves both every-Borel IMAGE
identities. Let a=sqrt2. Full parent arrows from(y,l) to(x,j) satisfy
x=a^{-k}y, j=l-k mod2, c=k log a; sampled arrows satisfy x=2^{-k}y,
j=l, c=k log2. All three kernels are units. Nonzero classes retain their
entire sheet-coupled geometric orbits, with all real phases h+log|x| and
H/isotropy0; each parent class splits into two sampled classes.

At zero, BOTH points form one parent least-two cycle and its complete basin
is exactly those two points. Parent source isotropy2Z, H=log2 Z, extension
isotropy0; all phases can be written h-j log a modulo log2. Under R the two
zero points are separate fixed cores, no nonzero incoming, each source
isotropyZ, H=log2 Z and all phases h modulo log2. Thus two full packets of
the same prime primitive survive, not one selected sheet. All repetitions
are positive integer multiples of log2. This realizes the multiplicity
alternative of Section6 without deleting the rest of either carrier.

### D: a partial square with terminal merging

X=R,Lebesgue; D=(-1,0) union(0,1), T(x)=x^2+2. Its two actual inverses
theta_±(y)=±sqrt(y-2) have domain(2,3), which consists of terminal objects.
There is no target-next-step test. Own all-point J_±=1/(2sqrt(y-2)) and the
one-dimensional substitution identity prove every-Borel IMAGE. Thus
kappa_T(x)=log(2|x|) on D, signed/zero included; no clock is assigned elsewhere.
The critical point0 and endpoints±1 remain terminal objects, not legal sources.

For every t in(2,3) put a=sqrt(t-2). Its complete parent class is
{t,+a,-a}, with depths delta(t)=0, delta(±a)=1 and potentials
B(t)=0, B(±a)=log(2a). Every ordered pair has the unique arrow of lag
delta(z)-delta(w) and clock B(z)-B(w). All other real objects are singleton
terminal classes. This exhausts all incoming depths: no source has a legal
second step, since T(D)=(2,3) is disjoint from D. Isotropy/H are zero, and
every extension phase is h-B(x), or h on singleton classes.

The parent lag and joint kernels include units and the two directed merging
arrows between+a and-a for each t. The clock kernel includes those arrows
as well. At t=9/4 (a=1/2), B=0 on all three points and ALL nine arrows of
that class are in the clock kernel; only equal-depth ones are in the joint
kernel. At every other t no additional nonunit clock-kernel arrows occur.

R=T^2 has EMPTY domain, not a zero outgoing clock: all real objects are
retained terminals, each a singleton class; only units exist. Its inverse
family is empty and its IMAGE requirements are vacuous, with no prescribed
legal step. All kernels equal that unit groupoid, isotropy/H0 and all phases
h in R. Its embedding image is only parent units, whereas parent lag-zero
contains (+a,0,-a). The earliest witness of this latter arrow is(1,1)
at terminal t; one more step would be required for stride2 and is illegal.
Thus(6) excludes it. The original two depth-one predecessors have the same
depth residue but different sampled endpoints, verifying the need for(7).
Both owners have empty positive ledgers; no positive period is manufactured.

## 8. Gate, adverse findings and decision

Conditional owner construction, exact image and whole packet classification
are proved under the frozen hypotheses. A uniform-stride repair is excluded
on the stated rational-parent subclass, while C exhibits the precise boundary.
Terminal retention of OBJECTS does not imply retention of all divisible-lag
ARROWS. The controls would prove too much if their externally supplied
dilation coefficients were promoted into arithmetic evidence; we do not do so.

Portfolio: FORK as a search filter, not advance as a prime candidate. Any
future sampled candidate needs its own source and exact IMAGE/terminal/packet
audit. No new candidate is started here. Classical fields NOT APPLICABLE;
arithmetic T1 NOT PASSED; T3 NOT AUDITED; formal Route coordinates UNASSIGNED;
Route B NOT INVOKED. Naturalness and all-prime coverage remain unestablished.

## Reproducibility and review boundary

Inputs are exactly the [frozen card](candidate-card.md), integer r and its
four specified controls. Methods are branchwise measure substitution, legal
history identities, finite cycle congruences and integer factorization; there
is no numerical cutoff, orbit census, scientific executable or external theorem
import used as a result lock. [Claim ledger](claim-ledger.md) records scopes;
[CP1](evidence/scope-review.md), [raw audit](evidence/independent-derivation.md)
and [final comparison](evidence/review.md) record the staged AI review.
Root authored this paper, README and ledger after FULLread CP1 and BEFORE its
first raw read. No author helper was used. The reviewer received card-only
science under separate raw release; final access requires frozen raw, root's
full read and a distinct unlock. Shared-history same-model work remains
NOT_CALIBRATED, not blind, human, external or cross-model peer validation.
No old file, source lock, Route credit or formal authorization is transferred.
