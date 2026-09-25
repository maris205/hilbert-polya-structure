# ISR01 — independent card-only derivation

Candidate: `ANG-AUDIT-20260923-ISR01`; date 2026-09-23.
Reviewer: `/root/nonlocal_source_review`; shared-history internal AI, NOT_CALIBRATED.
Input: clarified candidate-card.md, 92 lines, SHA256 508624072f638f23fe35f1d03e50013f9219200f92b692653c02f529725695ed.
Original 85-line prefix SHA256 59264a3ec121fa302a507d64153e38702c9469d2f610a09943966ac2a4fef98a.
CP1: scope-review.md, 109 lines, SHA256 d659922fd9c66c5e55ec2bddfce40f100d0c3fcb7761d78ece99aeaed074b5df.
Root fully read CP1, resolved the terminal-edge clarification, then separately
released mathematics. The clarified card was reread completely before proof.
The graph here is exactly the actual transition graph; terminals have no edges.
No author paper, README, ledger, Outcome, helper/peer answer or sibling research
was read. Shared prior history and disclosed design expectations remain;
this is not blind, cross-model, human or external verification. AI performed
the derivation and checking. No external source, scientific code, numerical
experiment, parameter adjustment, Git action, PDF or publication is used.

## 1. All-point IMAGE owner and complete histories

For active v write f_v(x)=d_v x+beta_v. Its actual inverse
g_v(y)=(y-beta_v)/d_v has domain T(I_v) and range I_v, with derivative
1/d_v at every actual target, including its included endpoint. For every
Borel E in T(I_v), real affine change of variables gives

    mu(g_v E)=integral_E (1/d_v) dmu(y).

Both sides use restricted Lebesgue measure on the FULL X; the affine inverse
image lies in I_v. The frozen version is finite and positive at every point.
Thus the branch-owned clock is kappa(x)=log d_v for x in I_v, at endpoints
as well as interiors. Every legal step is positive, but a terminal has no
next-step clock. IMAGE alone would not select null-point values: the assigned
inverse-derivative prescription supplies that separate all-point ownership.

For each y in X, ALL predecessors are g_v(y), for every active v with
y in T(I_v). They lie in disjoint source intervals, even when branch images
overlap. Iterating this rule retains every legal inverse history and endpoint.
For Borel E in X, disjointness in the SOURCE gives the full preimage formula

    mu(T^(-1)E)=integral_E sum_(v active) 1_(T(I_v))(y)/d_v dmu(y).

The sum may be infinite. It is not a branch IMAGE version and cannot replace
one branch's 1/d_v in the clock. For an actual legal prefix set

    D_0(x)=1,   D_m(x)=product_(t=0)^(m-1) d_(v(T^t x)),
    S_m(x)=log D_m(x).

Every fixed inverse itinerary has actual inverse slope 1/D_m and its full
Borel IMAGE law on that itinerary's actual target domain. Products never
include a nonexistent terminal step. Countably many finite branch words
retain all actual predecessors; no symbolic path space replaces X.

## 2. Exact finite closed-word realization without IR

Let W=(v_0,...,v_(n-1),v_n=v_0) be a directed closed path, n>=1.
All its vertices are active by the clarified graph rule. Define

    F_W=f_(v_(n-1)) ... f_(v_0),
    F_W(x)=D_W x+B_W,
    D_W=product_(t=0)^(n-1) d_(v_t),
    B_W=sum_(t=0)^(n-1) beta_(v_t) product_(u=t+1)^(n-1) d_(v_u).

Composition order means the rightmost map acts first. Its inverse affine map
is Psi_W=g_(v_0) ... g_(v_(n-1)), with unique fixed point

    p_W=-B_W/(D_W-1),   D_W>=2^n>1.

Each edge gives g_(v_t)(I_(v_(t+1))) subset I_(v_t), including its half-open
endpoints. Hence Psi_W maps I_(v_0) into itself and extends continuously to
a contraction of its closed interval into itself. Specifically Psi_W(a)>=a
and Psi_W(b)<=b; Psi_W(x)-x is strictly decreasing, so p_W lies in [a,b].
The actual realization test is

    x_0=p_W, x_(t+1)=f_(v_t)(x_t),
    a_(v_t)<=x_t<b_(v_t) for EVERY t, and x_n=x_0.

Under the exact image hypothesis this test succeeds exactly when p_W<b_(v_0).
To prove sufficiency, start at p_W in I_(v_0) and apply the inverse branches
in reverse time. Each stays in its stated interval, and their composition
returns to p_W. This gives precisely the displayed legal forward itinerary.
Necessity is immediate from the actual starting interval. The unique point
thus realizes the word if it passes; adjacency alone does not certify passage.

The complete boundary cases have a useful stronger description. The candidate
intermediate points obtained by inverse continuation lie in the corresponding
CLOSED intervals. Along an edge v->w, interval containment implies

    f_v(a_v)<=a_w,   f_v(b_v)>=b_w.

If a candidate source phase is a_v, its next candidate phase is therefore
a_w; if it is b_v, its next phase is b_w. The candidate next phase must also
belong to [a_w,b_w], giving equality in each case. Around a closed word this
shows that either EVERY phase is interior, EVERY phase is its left endpoint,
or EVERY phase is its right endpoint. The first two cases are actual; the
last is excluded by the half-open convention at every phase. Equivalently,
the excluded case has f_(v_t)(b_(v_t))=b_(v_(t+1)) throughout the word.
An excluded right endpoint might belong to a DIFFERENT interval as its left
endpoint. That actual point is not deleted: its fixed partition then gives
a different itinerary and its own test. No alternative endpoint coding is used.

For a realized length-n word, its point's least period is the least repetition
length of its vertex word. Indeed an actual shorter period repeats its unique
interval itinerary. Conversely if W=U^k, the fixed point of Psi_U^k is the
unique fixed point of Psi_U, so the actual point returns after length(U).
The legal intermediate membership already holds. Thus primitive actual cycles
are in bijection with realized primitive closed vertex words modulo cyclic
rotation. Nonprimitive words are repetitions of those cycles, not new packets.
For W=U^k, D_W=D_U^k and S_W=k log D_U; this is a repetition law, not a new
composite primitive obstruction. Distinct primitive necklaces cannot code
the same actual orbit because the disjoint half-open partition fixes its code.

## 3. Complete G, kernels, isotropy and height phases

Use exactly the frozen actual triples (x,m-n,y) with legal T^m x=T^n y.
Their clock is c=log D_m(x)-log D_n(y). Witnesses for the same triple differ
by common padding; the longer one certifies legal continuation of the common
tail, whose identical added sum cancels. Aligning the middle witness lengths
proves closure and additivity under composition. Reversing a triple negates
lag and clock. Forward transport x->Tx has lag -1 and clock -kappa(x).
The FULL kernels, always with the actual common-tail condition retained, are

    K_clock: D_m(x)=D_n(y);
    K_lag:   m=n;
    K_both:  m=n and D_m(x)=D_m(y).

They may contain nonunit mergers. With varying digits, equal products need
not imply equal prefix lengths. No quotient erases these arrows or terminals.

Nonzero source isotropy is equivalent to eventual periodicity: a nonzero-lag
self equality exhibits an eventual cycle, and conversely its late prefixes
give all period lags. If that least cycle has length q and product D_gamma,
then every point in its FULL finite inverse saturation has

    Iso_G=qZ,  c(x,kq,x)=k log D_gamma,
    H=(log D_gamma)Z,  Iso_extension(x,h)={0},
    L=log D_gamma>0,  repetitions kL (k>=1).

Here D_gamma>=2^q, so there is no ineffective nonzero isotropy on a cycle in
this particular class. Every non-eventually-periodic point, including every
terminating point, has source/extension isotropy zero and H={0}. Its missing
terminal step is still undefined, not assigned the value zero.

For ALL incoming and phases, fix a reference x_* in any source orbit O and
an actual arrow g_x:x_*->x of lag k_x and clock b_x for each x in O.
Every arrow y->x is uniquely of the form g_x u g_y^(-1), where u is source
isotropy at x_*. Thus in an eventual orbit its possible lags/clocks are

    k_x-k_y+nq,   b_x-b_y+n log D_gamma,   n in Z.

These give all three kernels within the full saturation, not only the core.
In a non-eventual orbit there is only n=0 and exactly one arrow between each
pair. The complete height phase is [h-b_x] in R/H. Changing the connecting
arrow changes it by an element of H; changing reference changes coordinates,
not the physical orbit. Hence each full source orbit owns one physical R/H,
not one per incoming point. A nonzero H gives one closed positive packet;
H={0} gives a free physical line. No global Borel selector/manifold is asserted.

In particular, the source orbit of a terminal e is ALL finite predecessors
of e. For x whose terminal hitting time is a, choose g_x=(x,a,e), giving
phase h-S_a(x) in R. Different terminal endpoints cannot have a common tail.
Actual infinite escaping or other non-eventual trajectories remain with H=0.
An abstract infinite graph path is not automatically a point or a cycle:
its actual cylinder intersection must be used, and need not be singleton.
All period claims above use finite returns of actual points only.

## 4. IR and the exact grammar/prime-packet criterion

First, IR makes EVERY finite closed word interior-realized. If a closed word
had a boundary candidate, Section 2 makes all its phases the same type of
endpoint. Any finite closed walk contains a simple directed cycle: remove
loops between repeated vertices until a minimal closed segment remains.
That segment has an endpoint fixed by its inverse word, contradicting IR.
Thus under IR no closed word is lost at an excluded endpoint or realized only
on an included endpoint. No such conclusion was assumed without IR.

Call an SCC cyclic when it contains a finite directed cycle. Under IR,
prime-only primitive support holds IF AND ONLY IF both conditions hold:

    (G1) every cyclic SCC is a singleton vertex with a self-loop;
    (G2) the digit d_v at every self-loop vertex is an ordinary integer prime.

Necessity: any SCC with at least two vertices contains a simple directed cycle
of length q>=2. Take an edge between distinct vertices in it and a shortest
return path; together they form such a cycle. IR realizes it in the interior.
Its vertices are distinct, so its actual least period is q, not a repetition.
Its multiplier is a product of q integers at least 2, hence composite.
This violates prime-only support. A self-loop, also interior-realized by IR,
has one fixed point with primitive log d_v, requiring d_v prime.

Sufficiency: every finite closed walk lies within one SCC. Under (G1) it must
be v^n at one self-loop vertex. Its affine fixed point is the same unique
fixed point for every n; higher n are repetitions. There are NO other periodic
points by Section 2. Under (G2) these are exactly the prime-log primitives.
This argument applies equally to a countable graph; infinite escaping paths
do not create a finite cycle or a positive physical H.
Digits on noncyclic vertices need not be prime: their preperiod contributions
shift incoming phases but cancel from the eventual cycle's entire H.

In this regime there is exactly ONE packet per self-loop vertex, including
all its incoming. Distinct vertices give distinct fixed points/source orbits,
even if one loop has graph paths leading to another or their digits coincide.
Consequently the full three-part target holds under IR exactly when (G1),(G2)
hold, there is AT LEAST ONE self-loop vertex, and the digits on these vertices
are pairwise distinct. More generally IR makes positive nonemptiness equivalent
to existence of a directed cycle; no existence is silently presumed.
All-prime coverage would further require the set of loop digits to equal the
set of all ordinary primes. This is only a characterization of frozen data,
not a construction, prime selector, or proof of endogenous arithmetic origin.
It presupposes the exact interval realization; arbitrary abstract graphs are
not thereby claimed to admit the required affine/endpoint geometry.

IR is sufficient for this graph-level equivalence, not claimed necessary for
an individual actual prime packet. Without IR, use the exact endpoint test;
one may not infer actual composite cycles just from graph adjacency.

## 5. Control A — all points, terminal rays and one prime packet

A owns X=[-1,1), active I=[-1/2,1/2), and terminals
E_A=[-1,-1/2) union [1/2,1). Its actual map is 2x on I, a bijection I->X.
For EVERY y in X the unique inverse is y/2 in I, including y=-1.
Affine substitution gives its own all-point IMAGE density 1/2 and clock log2.
All m-step inverses are y/2^m; no endpoint or terminal predecessor is lost.
Its graph has I->I and I->each terminal, with no outgoing terminal edges.
The only simple cycle is I's self-loop, fixed at 0 in the interior: IR holds.

The point 0 is fixed and has no incoming point other than itself at every
depth. It is the ONLY nonterminating point: for any x nonzero, successive
doublings eventually leave I and, at the first such step, land in E_A.
Let a(x)>=0 be the first n with 2^n x in E_A, and e(x)=2^a(x) x.
This definition includes already-terminal points with a=0 and respects the
asymmetry: -1/2 is active and next reaches -1, whereas +1/2 is terminal.
No trajectory reaches the excluded point +1 from a legal source.

Every terminal e in E_A labels exactly the full source ray

    O_e={e/2^n:n>=0}.

Distinct e give disjoint rays. For x=e/2^a, y=e/2^b the unique arrow has
lag a-b and clock (a-b)log2, since both histories land at e. Every point of
each ray has source/extension isotropy zero, H={0} and full phase
Phi(x,h)=h-a log2 in R. All nonzero points belong to these rays; there is
no additional nonterminating, nonperiodic family.
At 0, source isotropy is Z, extension isotropy zero, H=(log2)Z and phase
h modulo log2. There is exactly ONE positive primitive log2 packet, with
repetitions k log2. Words I^n all represent that fixed orbit repeatedly,
not longer primitive cycles. Because T is injective and c=lag times log2,
the full lag kernel, clock kernel and their intersection are units, including
on terminal rays. A meets the necessary three-part target, not all-prime
coverage or arithmetic naturalness; it remains an external control.

## 6. Control B — all points and an actual primitive two-cycle

B owns components X_0=[-1,1), X_1=[2,4), with coordinates
x=3epsilon+u, epsilon in {0,1}, u in [-1,1). Active means
u in [-1/2,1/2); the four terminal intervals mean u in E_A in either component.
The given formulas become

    T(epsilon,u)=(1-epsilon,2u) on the full active domain.

The actual inverse is (epsilon,u)->(1-epsilon,u/2), unique at every target.
Equivalently y in X_0 has inverse (y+6)/2 in J, and y in X_1 has inverse
(y-3)/2 in I. Each branch separately owns IMAGE density 1/2 at every point;
their target components are disjoint. B's own clock is log2, not borrowed.
The graph has I->J and the two J-component terminals, and J->I and the two
I-component terminals. Its only simple cycle is I,J,I up to rotation.
The two-return affine maps fix 0 in I and 3 in J, both interior. IR holds.

The points 0 and 3 form ONE least-two cycle: T0=3 and T3=0, and neither is
fixed. Its product is 4 and source isotropy is 2Z; extension isotropy is zero,
full H=(log4)Z, and primitive time is log4, NOT a repetition of a fixed cycle.
There is ONE positive packet, all phases h+epsilon log2 modulo log4 and
repetitions k log4. The only incoming points of the core are those two points.
Words (IJ)^k repeat this least-two orbit; they do not create new packets.

Every u nonzero eventually reaches a unique terminal e=(epsilon_e,u_e).
If its hitting time is a, u_e=2^a u and epsilon_e=epsilon+a modulo2.
The ENTIRE source ray of e is

    O_e={(epsilon_e-n modulo2, u_e/2^n):n>=0},

interpreted as the actual real points 3epsilon+u. For levels a,b its unique
arrow has lag a-b, clock (a-b)log2 and phase h-a log2 in R. Its source and
extension isotropy and H are zero. These rays exhaust every noncore point;
included -1/2 and excluded +1/2 active endpoints are handled exactly as in A
in each component, without identifying the two different terminal endpoints.

The full G consists of these rays and the core groupoid. On the core, an arrow
from phase eta to epsilon has every lag l=eta-epsilon modulo2 and clock
l log2; only even l are loops. A lag-one interphase arrow is not a physical
return and cannot reduce H from log4 Z to log2 Z. Injectivity and the constant
clock make all three full kernels units. There are no omitted nonterminating
noncore points. B fails prime-only with the genuinely composite primitive 4,
as the IR graph criterion predicts; multiplicity one does not repair it.

## 7. Control C — full doubling owner and every period

C owns full X=D=[0,1), with its two disjoint half-open source intervals.
Its actual inverse branches are

    g_0(y)=y/2 in [0,1/2),
    g_1(y)=(y+1)/2 in [1/2,1),     0<=y<1.

Each has its OWN prescribed IMAGE density 1/2, including y=0, by real affine
substitution. The clock is log2 at EVERY source point. Summing both disjoint
preimages gives mu(T^(-1)E)=mu(E), but that total density 1 is NOT a branch
inverse version and supplies no zero clock. All m-step predecessors are

    (y+k)/2^m,   0<=k<2^m.

All are legal and distinct. There are no terminals or removed dyadic points.
T(x)={2x}, and induction gives T^m x={2^m x} for every x in [0,1).
The entire G and its clock therefore are

    G={(x,m-n,y): 2^m x-2^n y is an integer, m,n>=0},
    c=(m-n)log2.

Clock kernel, lag kernel and intersection coincide, but they are NOT units:

    K={(x,0,y): x-y in Z[1/2]},   x,y in [0,1).

Indeed equal-length tails agree exactly when 2^m(x-y) is integral for some m.
For example 0 and 1/2 have a nonunit zero-lag merger. Ineffective merger arrows
between distinct objects must not be confused with isotropy at one object.

### 7.1 Dyadic coding, exact periodic sets and IR

Let e_t=floor(2T^t x). These are the UNIQUE actual interval digits and
x=sum_(t>=0) e_t/2^(t+1). Dyadics use the terminating-zero expansion, including
1/2 as 1000..., not 0111.... Greedy sequences are precisely binary sequences
that are not eventually all ones. The all-ones infinite word represents 1,
outside X. Eventually-one alternatives at an interior dyadic boundary are
not its actual half-open itinerary and are not extra copies of that point.

For every n>=1 the complete exact fixed set is

    Fix(T^n)={k/(2^n-1):0<=k<=2^n-2},   cardinality 2^n-1.

This follows directly from (2^n-1)x being integral, with 0<=x<1; it is not
finite sampling. A binary length-n block of value k has inverse fixed point
k/(2^n-1). The all-ones block is excluded; every other block is realized.
Least source period is its least block repetition length, or equivalently
the smallest r>=1 for which (2^r-1)x is integral. Primitive necklaces modulo
rotation label ALL actual periodic cores; repeated blocks label repetitions.
Writing P_q for the number of exact least-q points gives the complete recursion

    P_1=1,
    P_q=(2^q-1)-sum_(r|q, r<q) P_r;
    number of primitive source cycles of length q = P_q/q.

Every q occurs: q=1 is 0; for q>=2 choose x=1/(2^q-1). For 1<=r<q,
0<(2^r-1)x<1, so no smaller period is possible. In particular {1/3,2/3}
is ONE genuine least-two cycle, not a repeated visit to the fixed point 0.
Its primitive is log4; all q>=2 primitives q log2=log(2^q) are composite-time.

The actual graph has both edges from each of the two vertices. Its simple
cycles are the two self-loops and the two-vertex cycle up to rotation.
The left self-loop fixes 0, an INCLUDED left endpoint, not an interior point.
The right self-loop fixes 1, an EXCLUDED right endpoint. The two-cycle phases
1/3 and 2/3 are interior. Thus IR FAILS, even though many graph cycles are
actually realized. C cannot be used as an IR instance or a justification
for omitting the endpoint test.

### 7.2 Complete rational incoming packets and all heights

A point is eventually periodic exactly when it is rational. One direction
follows from an equality (2^(a+q)-2^a)x in Z. Conversely write a reduced
rational denominator as 2^s b with b odd. After s shifts the denominator is
b, and multiplication by 2 permutes residues modulo b, giving a finite cycle.
This also shows that an actual periodic point has odd reduced denominator;
even-denominator rationals are strictly preperiodic, not non-eventual.
For b>1 its eventual least period is the multiplicative order of 2 modulo b;
for b=1 its eventual cycle is the fixed point 0. Its preperiod is exactly s.

For EVERY primitive periodic core Gamma={p_0,...,p_(q-1)}, T p_t=p_(t+1),
its full source orbit is

    B_Gamma=union_(m>=0) {(p+k)/2^m:p in Gamma, 0<=k<2^m}.

This retains ALL inverse histories and no point with a different eventual
core. The B_Gamma are disjoint and partition the rationals in [0,1).
Every point in B_Gamma has source isotropy qZ, extension isotropy zero,
ENTIRE H=q log2 Z, primitive q log2 and repetitions kq log2.
For any landing T^a x=p_t define eta(x)=t-a modulo q. It is independent of
landing time. All arrows y->x have exactly lags
l=eta(y)-eta(x) modulo q and clock l log2; sufficient padding proves every
such lag exists. The complete phase is

    Phi(x,h)=h+eta(x)log2 modulo q log2.

This includes every incoming and height. The three coincident kernels within
the basin consist of zero-lag arrows between equal eta; they agree with the
global dyadic-difference criterion. The basin of 0 is ALL dyadics in [0,1),
not just {0}, and gives exactly ONE log2 packet rather than one per preimage.

### 7.3 Complete irrational source orbits

For any irrational reference x, its full source orbit is exactly

    O_x={(T^n x+k)/2^m:m,n>=0, 0<=k<2^m}.

These sets are common-tail equivalence classes and exhaust the irrationals;
equal classes are taken once, not once per reference. Every member is
irrational and non-eventual, with trivial source/extension isotropy and H={0}.
If T^m y=T^n x, the reference arrow x->y has lag m-n, clock (m-n)log2, and

    Phi(y,h)=h-(m-n)log2 in R.

The lag is independent of witness: two distinct lags would give nonzero
isotropy and hence a rational eventual point. This is an orbitwise exact
phase on the full free physical R, not a chosen invariant subcarrier.
Its zero-lag mergers remain precisely the dyadic differences already recorded.
There are no terminating points in C and no further classes of actual points.

C therefore fails prime-only through genuine higher-period packets, not merely
through repetitions. Its period-one packet is unique, while all higher least
periods and their multiplicities are retained. No all-prime coverage or
arithmetic admission is inferred from this full doubling control.

## 8. Scope, decision and freeze boundary

The all-point IMAGE clock, exact endpoint realization test, primitive-word
identification and complete actual source/height ledger are established for
the frozen class. Under IR the cyclic-SCC, prime-digit, nonemptiness and
distinct-digit conditions above are necessary AND sufficient for the stated
three-part target. They classify an existing grammar; they do not create one.
All three controls retain their full carriers, actual endpoints, incoming,
kernels, isotropy, H and phases. A passes the necessary packet conditions;
B and C fail prime-only for the specified reasons. All remain EXTERNAL.

Portfolio: retain the conditional symbolic-to-interval filter; STOP any
claimed prime-only realization that violates its proven hypotheses/conclusion,
and FORK only with separately frozen data. No main prime-symbolic grammar is
admitted. Strong naturalness and PROVES_TOO_MUCH remain open. Classical
symplectic/suspension fields NOT APPLICABLE; T3 NOT AUDITED; formal Route
UNASSIGNED; Route B NOT INVOKED. No novelty or general non-IR no-go is claimed.

After complete self-read and hash freeze, HOLD for root's full raw read and
separate PAPER UNLOCK. This report grants neither manuscript access nor round420.
