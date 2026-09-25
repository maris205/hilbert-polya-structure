# ADR01 — frozen-card independent raw derivation

Candidate: ANG-20260925-ADR01. Paper484, Batch AA round5/5.
Reviewer: `/root/rcr01_independent_review`, 2026-09-25 UTC.
Stage: DISTINCT RAW RELEASE; author manuscript remains LOCKED.
Same-model/shared-root history NOT_CALIBRATED; not blind/human/external review.

## 0. Exact inputs and scope

Sole scientific file: `candidate-card.md`, FULL1–91/EOF, SHA-256
`2dd3d58b9cc323bca77d8795893811f662e7a9967ce6266833bcbb2716155050`.
Its original81-line prefix has SHA-256
`f9303a37fdfa055c07626bc88c39a253cc63106fa852282ea2d3a0688005a3fb`.
Own CP1 is168 lines, SHA-256
`62451c005ba4cee929a01dbe956e08ba1db82910598d59eb9f8b26bc38a83041`.
The bound root clarification separates exact positive primitive log p,
packet uniqueness, positive nonemptiness and all-prime coverage; an empty
short window or zero H alone does not prove global positive-ledger failure.

No author/peer/helper artifact, old proof or other scientific file was read.
Shared historical exposure remains disclosed in CP1, not erased. Personally
completed ARS router/deep workflow/runtime/DA/fallacy/anti-leakage and local
instruction reads are retained, not falsely reported as fresh reads here.
The bounded original-proof adaptation uses categorical evidence, no numeric
score, forced issue quota or literature-citation exercise.

This file proves the four own inverse/history structures and the ENTIRE
one-consumption least-period family, without a digit cutoff. General
statements about an arbitrary actual eventual core are structural formulas,
not a search or classification of two-consumption or higher families.
No scientific code/numerics, network, Git, PDF, old edits or Paper485.

## 1. Digit and endpoint ownership

For x>0 let n(x)=1+floor(1/x), A_n=n(n-1), and

    I_n=(1/n,1/(n-1)],
    L_n(x)=A_n x-(n-1),
    v_n(y)=(y+n-1)/A_n.

The I_n are disjoint and partition(0,1]. Algebra gives the exact bijections

    L_n:I_n -> (0,1],  v_n:(0,1] -> I_n.                 (1.1)

The lower boundary is excluded and the upper included. In particular
v_n(0)=1/n is NOT an actual inverse on the n chart: its true digit is n+1.
Every x=1/j,j>=1 has digit j+1; if it is consumed, its actual image is1,
and its inverse-germ derivative is1/[j(j+1)]. For x=1 this is the n=2
chart. At target y=1, the actual preimage for digit n is1/(n-1).
There are no consumption preimages of0. No scan starts at0 either.

All four owners retain every(0,d),d>=2 as a terminal object with no
non-unit incoming history and no absorbing loop. Its unit still has
clock0. An affine extension to an excluded lower endpoint never gives
an extra actual inverse, even though its germ has a well-defined derivative.

The variable n is always reread from x; it is not a stored state label.
The proof below uses n only as a branch identifier. Consumption changes
the future digit source in the actual autonomous map.

## 2. Four complete inverse atlases and every-Borel IMAGE

Write Div(n)={d:2<=d<n, d divides n}. All targets below use(y,e) order.
For y=0 there are no preimages. For y>0, put m=n(y).

SCAN inverses, present only for e>=3, are the single candidate(y,e-1):

| Owner | Exact permission for that inverse |
| --- | --- |
| M | e<=m and e-1 does not divide m |
| P | e<=m |
| C | e<=m and e-1 does not divide m |
| E | Never |

These conditions are precisely2<=e-1<m plus the owner's original test.
The inverse is identity on the real coordinate and shifts the discrete
phase back by1. Its actual chart target is I_m times{e}, when permitted.
It need not be a legal outgoing target: arrival at a terminal is allowed.

CONSUMPTION inverses occur precisely at e=2 with y in(0,1]. For EVERY
digit n>=2 and each phase in the following row, output(v_n(y),d):

| Owner | All old consumption phases d |
| --- | --- |
| M | d=n |
| P | d=n |
| C | Every d in Div(n), not only its least element |
| E | Every integer d>=2 |

Formula(1.1) proves n(v_n(y))=n, actual permission and both inverse
identities. The source charts are I_n times{d}; each maps bijectively to
(0,1] times{2}. There is no target-outgoing test. This includes, for
example, consumption arriving at C's terminal(1,2).
An arbitrary preimage must be either a scan source, whose old phase is
forced, or a consumption source, whose digit/phase lies in the table and
whose real coordinate is forced by L_n(x)=y. Hence the lists are complete.
Distinct n source intervals and distinct old phases are distinct sources;
their multiplicity is not an inverse determinant.

All chart families are countable Borel source partitions of their own
legal domains. On each inverse the prescribed affine-germ value is

    J_scan=1,  J_consume=1/A_n                            (2.1)

EVERYWHERE on its actual target, including y=1. Both are positive finite.
Counting measure is on a fixed old/new phase in each chart. For EVERY
Borel B in the exact real target interval, affine substitution yields

    mu(theta_scan B)=mu(B),
    mu(theta_{n,d} B)=mu(B)/A_n.                         (2.2)

This proves each owner's own original-measure IMAGE, for null sets too.
Only now define kappa=-log J_actual(Fz). It is0 on every legal scan,
and log A_n on every legal consumption from digit n. No unit roof is
inserted and no factor counting consumption phases enters kappa.
The chosen germs, not an a.e. density argument, fix the null-point values.

## 3. Exact forward domains and complete finite/infinite incoming

Here is a finite-block test for every real x>0 and EVERY initial phase d.
It follows directly because scans leave x, hence n(x), unchanged.

- M: d>n is terminal. Otherwise let t be the first divisor of n in
  [d,n-1]. If present, scan until phase t and stop there without consuming
  (including immediate termination if t=d). If none, scan to n and consume.
- P: d>n is terminal; otherwise scan to n and consume.
- C: d>=n is terminal. For d<n, let t be the first divisor in[d,n-1].
  If present, scan to t and consume; if none, scan to n and terminate.
- E: consume immediately for EVERY d>=2.

A consumption from phase t after starting at d has t-d scans and one
consumption edge. Restart from(L_n(x),2), recomputing its digit. Formula
(1.1) keeps its real coordinate positive. Repeating this deterministic
procedure gives the maximal actual microstep history, finite or infinite.
Every infinite legal history has infinitely many consumptions, since a
single fixed-digit scan cannot last forever. This is a derived operational
test, not a different macro owner: original microstep lags and clocks remain.

Thus P and E have infinite forward histories at all x>0 with legal first
block; P's d>n states remain terminal. M and C may terminate at a later
block, and their precise outcome is determined by this untruncated actual
digit recursion, not by ignoring late initial phases. No periodic census
outside §6 is inferred from this description.

Let T_O be the actual terminal set for owner O. It consists of all(0,d),
and, at x>0 with n=n(x), the following additional states:

| Owner | Additional terminal phases |
| --- | --- |
| M | d>n or d in Div(n) |
| P | d>n |
| C | d>=n |
| E | None |

For incoming, let Pre_0(w)={w} and

    Pre_{r+1}(w)=union_{u in Pre_r(w)} Pre_1(u),          (3.1)

where Pre_1 is EXACTLY §2's own atlas. Induction proves this is the
entire legal r-step predecessor set, with no restrictions on the endpoint's
outgoing legality. Actual states are identified, not counted by words.
Each level is countable. Keep all compatible infinite sequences
(w_0=w,w_1,w_2,...) satisfying w_j in Pre_1(w_{j-1}); these are precisely
the complete infinite backward histories. No boundary limit adds an object.

For additional explicitness, if a backward word uses consumption digits
nu_1,...,nu_t in that order, its source real coordinate is

    v_{nu_t} composed ... composed v_{nu_1}(y),          (3.2)

with scans leaving that coordinate unchanged. Every intervening phase,
permission and true-digit test is still required by §2. The forward sum
from this predecessor back to w is log(product_i A_{nu_i}); an empty
product is1. Equations(3.1)–(3.2) describe every finite incoming, including
all late phases in C and infinitely many consumption phases in E.

One can also exactly decide existence of an infinite past without a
cycle search. Every positive(y,2) has one: repeatedly take the n=2,d=2
consumption inverse for M/P/E, or n=4,d=2 for C. Both choices stay legal
by(1.1). For e>=3, the only backward edges before reaching phase2 are
the forced scans. Therefore an infinite past exists exactly as follows:

- M/C: y>0, e<=n(y), and no integer in[2,e-1] divides n(y).
- P: y>0 and e<=n(y).
- E: y>0 and e=2 only.

For M/P/C the e=2 case is included by the empty-test convention. If
the forced scan chain is blocked it terminates after finitely many edges;
no consumption can enter a phase>2 to circumvent the block. This existence
test does not replace the full tree of compatible choices in(3.1).
At y=0 there is no infinite past. Having no point preimage is distinct
from having no groupoid arrows from other points in one's full packet.

## 4. Every legal history, pointwise cocycle and own IMAGE

Set D_0=X; D_r consists of points whose first r actual steps are legal.
Countable Borel charts make F and all D_r,F^r Borel on their domains.
For z in D_r define the integer product and sum

    Q_r(z)=product of A_{n(F^i z)} over consuming i<r,
    S_r(z)=log Q_r(z),   Q_0=1, S_0=0.                  (4.1)

This is the sum of actual microstep kappa from §2, not a new assigned roof.
Finite inverse words, restricted at every intermediate domain, cover all
histories countably. Affine substitution successively gives their own
EVERY-Borel IMAGE with prescribed pointwise inverse product

    J_word(y)=exp[-S_r(theta_word y)].                  (4.2)

All formulas use original Lebesgue times counting, including endpoints.

Let G={(z,r-s,w):F^r z=F^s w legally}. Source is w, range z, and only
equal triples are identified. For a witness put c=S_r(z)-S_s(w).
If another witness represents the same lag, r'-r=s'-s; the longer pair
adds the same legal common-tail sum to both sides, which cancels.
Thus c descends pointwise. For composition, align the two middle-history
lengths using the longer supplied legal path and cancel the middle sums.
This proves additivity without extending a terminal past its legal end.
Units have c=0, inverses negate c, and c(Fz,-1,z)=-kappa(z).

For a pair of history charts over one common target, the source-to-range
map is phi=(F^r|U)^{-1} composed with(F^s|V), on its exact common-image
domain. Weighted substitution in(4.2) gives for EVERY Borel B there

    mu(phi(B))=integral_B exp[-c(phi(w),r-s,w)] dmu(w).   (4.3)

This is each owner's own history-pair IMAGE. No counting multiplicity,
target-outgoing condition, full-measure restriction or positive roof appears.
The exact full-arrow kernels are the actual meeting triples with

    K_lag: r=s;
    K_clock: Q_r(z)=Q_s(w);
    K_joint: r=s and Q_r(z)=Q_r(w).                     (4.4)

Different witnesses of a triple give the same tests by descent. These
kernels can have non-unit arrows; their description is not just a loop test.

The whole source packet of w is

    O(w)=union_{s>=0:w in D_s} union_{r>=0} Pre_r(F^s w).(4.5)

This is exact and countable; all compatible infinite incoming histories
remain attached as in §3, not promoted to additional states or new packets.
The arrow set and packet relation are Borel, being countable unions of
equal-iterate Borel relations. No regular quotient or selector is assumed.

## 5. All component types, entire H, physical phases and repetitions

A finite maximal history ends at one terminal b. Its full packet is all
actual predecessors of b, with terminal endpoint uniquely determining
the packet. If z,w reach b in t_z,t_w steps, their unique arrow has
lag t_z-t_w and clock S_{t_z}(z)-S_{t_w}(w). A repeated iterate before
termination would instead produce an infinite legal cycle, so no such
packet has nonzero-lag source isotropy. In particular each(0,d) is its
own source packet, retaining all real heights and no positive return.

An infinite history is either eventually periodic or never repeats.
For a non-eventual source, distinct common-tail witnesses cannot have
different lags; otherwise it would acquire a periodic tail. Its source
isotropy is trivial and H={0}. Formula(4.5), not a periodic representative,
defines the entire packet, with exact common-tail orbit tests.

For ANY actual eventual core, let q be its actual least microstep period
and let nu_1,...,nu_t be its consumption digits counted on one primitive
traversal, including a possible closing edge. Necessarily t>=1: only
scan edges would strictly increase phase and never return. Thus

    B=product_{i=1}^t A_{nu_i}>1,  C=log B>0,
    Iso_G(z)={(z,mq,z):m in Z},
    c(z,mq,z)=mC,   ENTIRE H_z=C Z.                      (5.1)

All isotropy lags are multiples of q, by the least period on the tail;
every multiple is attained by extending actual legal histories around it.
Incoming sums cancel and cyclic rotation leaves the same C. Therefore
(5.1) is the entire image, not merely a subgroup supplied by a displayed
loop. This formula is conditional on an actual core; it does not solve
or search the unclassified multiple-consumption periodic equations.

For exact full-arrow phases, choose a reference b in a packet and an
actual arrow A_z=(z,l_z,b), beta_z=c(A_z). In an eventual packet all
arrows from w to z, and only those, have

    (lag,c)=(l_z-l_w+mq, beta_z-beta_w+mC),  m in Z.      (5.2)

Conjugation by A_z,A_w reduces any arrow to(5.1), proving completeness.
In terminal/non-eventual packets omit the m terms; the endpoint arrow
is unique. The full kernels impose zero lag, zero clock, or both on
the SAME pair in(5.2), consistent with(4.4).

Retain X times R_h with(w,h)->(z,h+c). Extension isotropy consists of
the zero-clock source loops. It is trivial in every eventual packet here
because C>0, and trivial in terminal/non-eventual packets as well.
Source isotropy qZ is NOT thereby erased. The exact all-real orbit test is

    same full source packet, and
    h_z-beta_z == h_w-beta_w modulo H.                  (5.3)

For H={0} this is equality of real values. For eventual packets it is
a real coset modulo C Z. Changing anchor arrows shifts beta by a loop
clock and preserves the test. Height translation on the orbit SET has
stabilizer EXACTLY H; its primitive in an eventual packet is C and all
positive repetitions are jC,j>=1. Forward traversal of the source cycle
j times has lag -jq and clock -jC; positive-lag isotropy has +jC.
No smooth quotient or substitution of a unit macro clock is involved.

## 6. Global symbolic classification of the one-consumption family

Take any cycle in the frozen family and rotate it so that its sole
consumption closes the cycle. Immediately after consumption its phase
is2. All other edges are scans, leaving its real value x unchanged.
The closing consumption must therefore satisfy L_n(x)=x with the TRUE
digit n=n(x), and its phases are consecutive2,...,d_*.

The equation has the UNIQUE solution

    x_n=(n-1)/(A_n-1).                                 (6.1)

It belongs to I_n for EVERY n>=2: x_n>1/n because
n(n-1)>A_n-1, and x_n<=1/(n-1) because
(n-1)^2<=A_n-1, equivalently n>=2. Equality at the upper endpoint occurs
only at n=2, giving x_2=1. Thus no limiting or falsely owned endpoint
creates or removes a cycle. The phase permissions now give all cases.

| Owner | Exactly which n occur | Consumption phase d_* | Least microperiod q | Primitive physical L |
| --- | --- | --- | --- | --- |
| M | Every prime n | n | n-1 | log[n(n-1)] |
| P | Every integer n>=2 | n | n-1 | log[n(n-1)] |
| C | Every composite n | smallest proper divisor l(n) | l(n)-1 | log[n(n-1)] |
| E | Every integer n>=2 | 2 | 1 | log[n(n-1)] |

M proof: its closing edge must be at d_*=n. All scans from2 through
n-1 are legal precisely when there is no proper divisor, equivalently
n is prime. A late composite restart can be legal as a TRANSIENT edge,
but cannot evade the earlier blocked phase on this cycle from2.

P proof: all scans2 through n-1 and the closing restart are legal for
every n. No other closing phase is a consumption for this owner.

C proof: a scan cannot pass a proper-divisor phase, since there C must
consume. Thus d_* must be the FIRST proper divisor of n, which exists
exactly when n is composite. Its least divisor l(n) is prime: if it were
composite, a smaller prime factor would also divide n. Other proper
divisors remain actual incoming consumption phases, not extra cycle cores.
For a prime digit, the scan reaches terminal phase n and cannot close.

E proof: every step consumes, so a least period containing exactly one
consumption has exactly one edge. Reset forces its cycle phase to be2.
Every d>2 is still an actual possible transient incoming source, not an
additional fixed core when the real value happens to equal x_n.

Conversely every table row supplies a legal cycle at x_n through exactly
the listed phases; its only consumption fixes x_n by(6.1). No shorter
positive return exists: before the closing edge the phase has not returned
to2 (and E has the minimal possible period1). This proves LEAST period,
not just a periodic word. The proof exhausts all n symbolically, with no
digit cutoff, and every cyclic rotation is the same core/packet.

## 7. Full incoming packets, kernels and all phases of these cycles

For any table entry let b_{O,n}=(x_n,2), q as in that row and A=A_n.
Its entire full source packet is EXACTLY

    O_{O,n}=union_{r>=0} Pre_r(b_{O,n}),                 (7.1)

where Pre uses that owner's full atlas in §2, not just the periodic
branch. Every phase of the cycle reaches b, and every object equivalent
to b eventually reaches that same cycle, proving both inclusions.
All real values, late phases and endpoint incoming are generated by the
explicit compositions(3.2) and their phase checks. Compatible infinite
incoming are exactly the sequences in(3.1), with existence characterized
in §3. Every listed cycle supports its indefinitely repeated own inverse
cycle, in addition to whichever other paths the complete atlas permits.

For z in(7.1), let t_z be its LEAST nonnegative arrival time at b and
K_z=Q_{t_z}(z). Then A_z=(z,t_z,b) is an ACTUAL anchor arrow with
beta_z=log K_z. On the core, t_b=0,K_b=1; at phase d>2 one has
t_z=d_*-d+1,K_z=A, because the path back to2 includes the closing edge.
This covers every actual scan phase, including C's shorter first-divisor
scan and E's sole core phase2.

All arrows from w to z are exactly

    k=t_z-t_w+mq,
    c=log K_z-log K_w+m log A,  m in Z.                 (7.2)

Thus K_lag requires m=(t_w-t_z)/q to be integral. K_clock requires
K_z A^m=K_w. K_joint requires BOTH with the same m. These formulas cover
the entire incoming packet, not only its core loops. In particular

    source isotropy=q Z;
    ENTIRE H=(log A)Z;
    extension isotropy={0};
    real physical phase=[h-log K_z] in R/(log A)Z.       (7.3)

The cycle has zero scan clocks and precisely one log A consumption, so
its primitive is log A, not an extra q log A and not generally log n. All positive physical
repetitions are j log A. A j-fold forward microcycle has lag -jq and
clock -j log A, while it remains the same source packet.
Every class in R/(log A)Z is retained. A representative of EACH coset
is only a coordinate; selecting a single coset would discard other
physical phases and is not done. The stabilizer remains the entire H.

Distinct allowed n in one owner give disjoint cores since their x_n lie
in disjoint I_n. Two distinct deterministic periodic cores cannot have a
common future, so their full packets(7.1) are distinct even after all
incoming is added. Also A_{n+1}-A_n=2n>0, so the primitives in this bounded
family are distinct within each owner. Equal primitives ACROSS owners
remain separately owned data, not pooled packets or evidence for MAIN.

## 8. Precommitted first MAIN witness and gate decision

Only after §6's complete symbolic classification apply the exact v1.1
prime test. A_n=n(n-1) is prime only for n=2: A_2=2, while for n>=3
it is a product of two integers>1. Logarithm is injective on positive
numbers. Accordingly M's n=2 core has primitive log2, but every prime
n>=3 core in this bounded family has a NONPRIME physical primitive.
Within this family there is no duplicated prime packet; this does not
claim uniqueness for unclassified families.

The first offending MAIN digit is therefore n=3, not chosen before the
symbolic classification. Its exact cycle is

    (2/5,2) -> (2/5,3) -> (2/5,2).                     (8.1)

Indeed n(2/5)=3, the first edge is a legal nondivisor scan, and the
closing consumption is L_3(2/5)=6(2/5)-2=2/5. The least microperiod is2.
In actual phase order the first cycle point is(2/5,2); its consumption
source is(2/5,3). Its source isotropy is2Z, primitive loop clock log6,
ENTIRE H=(log6)Z, extension isotropy0, and all heights have the phases
and complete incoming in(7.1)–(7.3). All repetitions are j log6.
Since6 is not prime, this is an exact positive-purity falsifier. No
rescaling, endpoint reassignment, packet merging or new density is used.

The controls are fully accounted for within the same gate: P/E contain
one core for every n, with their different microperiods, and C contains
one for every composite n with its own first-divisor period. P/E's n=2
cores have log2; all their n>=3 cores and every C core have nonprime
primitive log A_n. The controls are not substitutes for(8.1), which
belongs to the MAIN owner itself. No cross-owner primitive is counted
as a MAIN duplication.

Decision: STOP/FORK MAIN ANG-20260925-ADR01 at the frozen short gate,
because of the first exact positive nonprime primitive log6 in(8.1).
The inverse and history ownership checks succeed on the retained full
objects; the failure is positive-clock purity, not an owner mismatch or
absence of a positive primitive. It does not depend on treating a zero-H
or empty short window as global emptiness.

## 9. Limits, disclosure and freeze

This proves the exact all-digit ONE-consumption least-period classification
and its entire incoming/phase ledger, together with structural history
formulas for any actual eventual core. It does NOT classify all source
cycles, search two-consumption cores, establish all-prime coverage or
authorize changing the frozen dynamics. Other families may exist and
remain unclassified; they cannot erase the exhibited MAIN purity failure.
No geometric, determinant, operator or formal Route credit is awarded.

The lineage remains a genuine autonomous divisor-digit renewal mechanism,
but such lineage does not make log[n(n-1)] an endogenous log-prime ledger.
Classical NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED;
formal coordinates UNASSIGNED; Route B NOT INVOKED.

After FULL self-read and receipt, this raw freezes byte-immutably. Card
and scope remain unchanged. HOLD for root FULL raw read and DISTINCT
PAPER UNLOCK before any manuscript access or final CP2/CP3 comparison.
