# Binomial–Bernstein feedback: an owned clock with a sub-log-2 primitive

Paper ID: `310-binomial-bernstein-divisor-flow`.
Candidate ID: `ANG-20260920-BBD01`. Date: 2026-09-20.
Status: `OWNED BERNSTEIN CLOCK; SUB-LOG-2 FIXED PACKET — STOP / FORK`.
Evidence class: exact ownership and complete fixed-root theorem;
negative direct-prime-time gate. Classical A0/A1/A2 NOT APPLICABLE;
formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

Current integer roots determine a binomial composition count and
a normalized cumulative polynomial action. Real position selects a
divisor probe; its quotient changes the next roots and real
function. We retain all interval fibres, terminal states and unit
endpoint atoms. Integration by parts, exact inverse enumeration and
stratified change of variables prove the full partial Borel owner
and its own clock. Binomial growth leaves only four possible
fixed integer roots. Their full fibres contain identity states,
strictly asymptotic nonreturns, atomic fixed points and one positive
fixed packet at (3,3,1/2). Its least time is log(15/8),
strictly below log 2. Full tail equivalence cannot turn it
into a repetition or merge it with another fixed core.
Three controls own their changed geometry, orientation and permission.
The first target gate therefore decides STOP / FORK, without
a changing-root period census. Strong naturalness remains OPEN.

## 1. Identity, question and same-object lineage

The original [card](candidate-card.md) is the sole frozen definition;
its source is the final definition in the [309 frontier](../309-content-power-complement-flow/evidence/scout-record.md).
The earlier uncompleted binomial sketch was withdrawn before any
ID or audit. Exact input and review locks are in [evidence](evidence/README.md).

| Item | Same-object owner | Boundary |
| --- | --- | --- |
| Carrier | Y=positive-integer pairs x [0,1], full standard Borel structure | All roots/seeds/terminals retained |
| Measure | Counting roots x (interior Lebesgue + delta_0 + delta_1) | NOT the integral kernel below |
| Arithmetic | N_(a,b)=binom(a+b-2,a-1), q=1+floor(b*x), q|N | Actual permission and quotient feedback |
| Geometry | Normalized integral P_(a,b), then roots (b,N/q) | Actual real action, not passive scale |
| Clock/time | Inverse IMAGE and full retained-lag real extension | Derivative inside, atomic ratio at endpoints |
| Packets | Full isotropy time image and least positive generator | No equal-time or chosen-seed quotient |
| Classical geometry | Symplectic base, roof and mapping torus | NOT APPLICABLE |
| Analytic/later owner | No operator, zeta, determinant or trace | T3 NOT SUPPLIED / NOT PURSUED |
| Controls | GEOMETRY-OFF, OUTPUT-REFLECT, PERMISSION-OFF | Each owns its changed source |

The [prior-work interface](../../docs/prior_work/README.md) is divisor-symbolic
admissibility -> composition count -> current real factor probe ->
quotient-root and real-function feedback. Choosing a-1 positions among
a+b-2 gives the two-letter count N. At root (2,n),
N=n for every n>=1, and the probe range includes all
factors of n. This is an inspection interface, not a
restriction of the carrier. The same roots determine both exponents
of P and the count in its exact normalization below.

Question: does this full candidate own an admissible primitive
clock at the complete fixed-root gate? Choosing the binomial source,
cumulative integral, probe scale, quotient update and layered measure
remains engineering design, not proved arithmetic necessity. No prime
selector, table, zero data, fit, per-prime parameter or inserted
roof is used. No Logistic/Henon conjugacy or conservative lift follows.

## 2. Integral action, actual inverse and all branches

### 2.1 Exact normalization and inverse

Write Z_(a,b)=integral_0^1 t^(a-1)*(1-t)^(b-1) dt.
For a>1, integration by parts gives
Z_(a,b)=(a-1)*Z_(a-1,b+1)/b; the base case is
Z_(1,b)=1/b. Induction yields

    Z_(a,b)=(a-1)!*(b-1)!/(a+b-1)!,
    K_(a,b)=1/Z_(a,b)=(a+b-1)*N_(a,b).

Thus P_(a,b)(x)=K_(a,b)*integral_0^x t^(a-1)*(1-t)^(b-1) dt
is a polynomial with endpoints 0,1 and derivative

    P'_(a,b)(x)=K_(a,b)*x^(a-1)*(1-x)^(b-1)>0 for 0<x<1.

It is continuous and strictly increasing on the entire [0,1],
so its frozen inf prescription Q is exactly its unique inverse.
Q is continuous on [0,1] and continuously differentiable inside,
with Q'(y)=1/P'(Q(y))>0. Endpoint limits give
integral_0^y Q'(t) dt=Q(y), including y=1; hence Q
is absolutely continuous despite possible endpoint derivative singularities.
These facts justify full Borel substitution, not only pointwise inversion.
The normalizer belongs to the FUNCTION, not to the fibre measure.

### 2.2 Actual domain, images and complete predecessors

At z=(a,b,x), put q=1+floor(b*x). If q|N,
define Tz=(b,N/q,P_(a,b)(x)); otherwise z is terminal.
The source cell is I_(b,q)=[(q-1)/b,q/b) for q<=b,
and I_(b,b+1)={1}. At every permitted q its exact
image at root (b,N/q) is

    [P_(a,b)((q-1)/b),P_(a,b)(q/b)) for q<=b,
    {1} for q=b+1.

Strict monotonicity proves these domains, including all cut and atom
conventions. At target (B,C,y), ALL predecessors are

    (A,B,Q_(A,B)(y)), A>=1, C divides N_(A,B),
    q=N_(A,B)/C in {1,...,B+1}, y in that branch image.

Necessity follows from the root equations and digit. Conversely
the inverse image condition reconstructs the permitted digit and
substitutes back. Different A predecessors remain even on overlapping
targets; terminals may have incoming arrows and are not removed.

This also gives an exact rootwise image enumeration. If B=1,
N_(A,1)=1 for every A, so the image is [0,1)
at C=1, and empty at every C>1. The inverse
seeds there are y^(1/A), retaining all A. If B>=2,
N_(A,B)>=A, so only A<=C*(B+1) can occur. The
full image is the FINITE union of precisely the permitted
branch intervals/singletons above for those A. The bound follows
because binom(A+B-2,B-1)>=binom(A,1)=A, or directly
by the product formula; it does not truncate a hidden infinite tail.

Consequently T is partial Borel and countable-to-one, not onto:
for example (1,2,0) has no predecessor. Nor is it ordinary
continuous on its domain. At root (2,2), the two digits
on either side of x=1/2 are both permitted, but the
target root changes from (2,2) to (2,1). No etale
or local-homeomorphism category is asserted.

## 3. Same-measure layered IMAGE and complete time

### 3.1 Interior versus atomic factors

For any actual inverse branch and 0<y<1, IMAGE is

    J_I(y)=Q'_(a,b)(y)=1/[K_(a,b)*Q(y)^(a-1)*(1-Q(y))^(b-1)].

It is positive finite at every interior point in that domain.
At endpoint 0 or 1 in the inverse domain, IMAGE is
1, the actual source/target unit-atom mass ratio. Splitting any
Borel target set into interior and endpoint parts, absolute-continuous
substitution and the atomic ratios prove the full IMAGE law.
No whole-branch ratio substitutes for this nonconstant density.

At internal cut points the analytic branch derivative supplies the
frozen all-point version; it is not uniquely determined by an
a.e. class. At endpoint atoms an interior derivative limit is
not used. In particular a zero derivative of P at an
endpoint does not make its atomic clock infinite or undefined.
For each defined forward step let rho(z)=P'_(a,b)(x)
inside and rho(z)=1 at endpoints. Then kappa=log rho
is the inverse-arrow clock. No rho is evaluated on an
undefined terminal forward step.

### 3.2 Actual partial histories and packet convention

The full retained-lag owner is G={(z,m-k,w):T^m z=T^k w},
source w and range z, with all iterates defined and T^0
on every terminal. Borel iterate equalities and countable finite-
iterate fibres give a countable Borel groupoid. Composition aligns
already existing middle histories; it never invents a terminal successor.
There are no independent history labels or free polynomial arrows.

For D_m(z)=product_(i<m) rho(T^i z), D_0=1, the
actual branch-pair IMAGE and clock are

    J(z,m-k,w)=D_k(w)/D_m(z),
    c(z,m-k,w)=log D_m(z)-log D_k(w).

Defined histories preserve interior versus atomic strata. Finite chain
rules apply inside; actual unit mass ratios apply at atoms.
Common legal future factors cancel in different presentations of
one triple, including the prescribed null-cut values. Alignment proves
composition and all-Borel branch-pair IMAGE. This is not global
invariance of mu under the many-to-one partial map.

All extension objects Y x R remain, with arrows
(w,h)->(z,h+c). Translation h->h+t is complete and jointly
Borel and commutes with arrows. We use only set-level quotient
time, not an unproved coarse topology. At a state z,
source isotropy, H_z=c(G_z^z), and extension kernel are
different objects. Only H_z=L Z with least L>0 gives
a positive primitive packet; r*L repeats that SAME packet.

## 4. Complete fixed-root fibres, exact returns and first obstruction

### 4.1 Only four roots can remain fixed

An ordered integer root unchanged by a step requires a=b=c=n
and q=N_n/n, where N_n=binom(2n-2,n-1). The necessary
condition q<=n+1 implies N_n<=n(n+1). For n=1,2,3,4,
the exact N_n are 1,2,6,20. For n=5, N_5=70>30;
further,

    N_(n+1)/N_n=4-2/n > (n+2)/n for n>=5.

Induction proves N_n>n(n+1) for EVERY n>=5. Thus no
fixed root was omitted by stopping this enumeration at four.
Their unique root-preserving digits are respectively 1,1,2,5.

The low-order real maps needed are

    P_11(x)=x,
    P_22(x)=3*x^2-2*x^3,
    P_33(x)=10*x^3-15*x^4+6*x^5.

Their fixed-point differences factor exactly as

    P_22(x)-x=x*(1-x)*(2*x-1),
    P_33(x)-x=x*(1-x)*(2*x-1)*(1+3*x*(1-x)).

The latter extra factor is positive on [0,1]. Applying the
actual digit cells, not merely solving unconstrained polynomials, gives:

| Root n | Digit q | Full one-step root-preserving fibre | ALL fixed seeds | Infinite fixed-root staying seeds |
| --- | --- | --- | --- | --- |
| 1 | 1 | [0,1) | Every x in [0,1) | [0,1) |
| 2 | 1 | [0,1/2) | 0 | [0,1/2) |
| 3 | 2 | [1/3,2/3) | 1/2 | {1/2} |
| 4 | 5 | {1} | 1 | {1} |
| n>=5 | None | Empty | None | Empty |

At n=4 only endpoint 1 has the required digit 5;
P_44(1)=1, so its fixed state really exists. The main
unit endpoint (1,1,1) is instead terminal; no extra loop
or duplicate unit branch is added.

### 4.2 Staying is not exact recurrence

At n=2, for 0<x<1/2, one has 0<P_22(x)<x.
Every such orbit stays in that interval and decreases strictly.
Its limit is zero, since any limit must be a fixed
point below 1/2. No finite iterate reaches zero. Thus ALL
these staying states have trivial source isotropy, H=0 and
trivial extension isotropy, despite convergence to a fixed state.

At n=3, P'_33(x)=30*x^2*(1-x)^2>=40/27>1
on [1/3,2/3]. The mean-value theorem gives
|P_33(x)-1/2|>=(40/27)*|x-1/2| there. If all
iterates stay in the bounded digit interval, x must equal
1/2. This proves the entire staying entry, not a chosen
central seed. The unit and endpoint entries are immediate from
their actual full actions. No changing-root period census is implied.

### 4.3 Fixed isotropy, primitive time and full-tail identity

Every listed fixed state has source isotropy the literal group Z.
Unit states have rho=1. At (2,2,0) and (4,4,1),
the endpoint atoms give rho=1, notwithstanding zero ordinary
derivatives there. These states have H=0 and extension isotropy Z.

At z_*=(3,3,1/2), N=6 and q=2, so the
fixed root is genuinely allowed. Its actual interior factor is

    rho(z_*)=30*(1/2)^4=15/8,
    H_(z_*)=log(15/8) Z, extension kernel={0}.

Thus the least positive time is L=log(15/8), with repeats
r*L on that SAME packet. Every isotropy lag is an
integer multiple of the fixed-state return, so there is no
smaller positive generator supplied by another presentation.

Different fixed states have different constant forward tails; no
equality of their iterates can merge them. Compositions of finite
inverse excursions remain actual tail arrows and cannot create
additional equivalences. Finite predecessors of z_* have the same
clock-isotropy image by conjugation, not extra core packets or
shorter times. Physical time cannot connect distinct source-tail classes.

For completeness, put f=P_22 on I=(0,1/2). It is
an increasing differentiable bijection I onto I, with positive
derivative, so all integer iterates f^ell exist there. Two
staying states z_x=(2,2,x) and z_y=(2,2,y) are
full-source tail equivalent exactly when y=f^ell(x) for some
ell in Z: common forward iterates imply this by invertibility,
and the converse is an actual tail arrow. No two such
classes merge merely because both converge to zero. The arrow
z_x -> z_(f^ell(x)) has lag -ell and clock
-log|(f^ell)'(x)|; its extension sends h to h minus
that log derivative. This follows directly from the finite chain
rule, including negative ell by inversion. All finite predecessors
attach to these actual classes without merging them with one
another or with a fixed core. Thus the nonperiodic staying
fibres retain their full phase equivalence as well as trivial isotropy.

Since 1<15/8<2, this genuine primitive has

    0<log(15/8)<log 2.

It is not log of any prime or integer >=2, nor
a positive integer repetition of such a time. The direct
prime-time target therefore fails at the frozen first gate. A
new global time normalization would change the candidate, not
reinterpret this fixed clock. Higher changing-root returns are NOT
PURSUED; no universal asymptotic or other-carrier impossibility follows.

## 5. Three separately owned controls

### 5.1 GEOMETRY-OFF

Keep main roots and partial domain but real output x. At
target (B,C,y), enumerate the same A and q=N_(A,B)/C,
but use inverse (A,B,y) on the OWN target I_(B,q),
including the endpoint singleton when allowed. Every interior and
atomic IMAGE is 1, so the entire cocycle and ALL H
vanish. ALL fixed and infinite fixed-root staying states are the
full root-preserving fibres in the table, now every point fixed.
Each has source/extension Z. No P-image interval or main
attraction result is transferred.
Every distinct fixed state is a separate constant-tail core; its
finite predecessors do not identify it with another such core.

### 5.2 OUTPUT-REFLECT

Keep the main domain/roots and use 1-P_(a,b)(x). Its
OWN real target is (1-P(q/b),1-P((q-1)/b)] for
q<=b, or {0} for q=b+1. Inverse seed is
Q_(a,b)(1-y). Interior IMAGE is its absolute derivative;
endpoint IMAGE is the actual unit mass ratio. Actual histories
therefore own a layered cocycle, not transferred main itineraries.

The same root equation leaves n=1,2,3,4. At n=1,
the unique fixed seed is 1/2; infinite staying seeds are
(0,1), with midpoint source/extension Z and other seeds 2Z,
all H=0. Zero maps to terminal one, not a two-cycle.
The unit source classes are exactly {x,1-x}, a singleton
at the midpoint; the two noncentral phases belong to ONE
class with zero-clock arrows. No inverse excursion merges different pairs.
At n=2 every x<1/2 maps to a real point >1/2,
so there is no infinite fixed-root staying state or fixed point.
At n=3 only 1/2 stays: absolute deviation expands by at
least 40/27 while in the permitted interval. It is fixed,
with source Z, least time log(15/8) and extension zero.
At n=4 the only root-preserving seed 1 maps to 0,
which has a different next quotient root; it is neither fixed
nor infinitely staying. These exhaust the control's fixed-root test,
not its changing-root periodic ledger.

### 5.3 PERMISSION-OFF

On ALL x in [0,1] use T_A=(b,N_(a,b),P_(a,b)(x)),
without a divisibility permission or quotient. At (B,C,y),
enumerate ALL A with N_(A,B)=C, and use inverse
(A,B,Q_(A,B)(y)) on the ENTIRE [0,1]. Its own
layered IMAGE is inverse derivative inside and atomic ratio 1
at endpoints. In particular seed 1 is no longer a terminal.

Fixed roots require N_n=n, which holds exactly for n=1,2.
Indeed N_3=6>3 and the same ratio formula keeps N_n>n
thereafter. Both complete fibres [0,1] now stay indefinitely.
At n=1 every point is fixed with source/extension Z and H=0.
At n=2 the ALL fixed seeds are 0,1/2,1. Endpoints
have zero H and source/extension Z; the midpoint has source Z,
least time log(3/2) and extension zero. Every other n=2
seed is strictly monotone toward an endpoint and never reaches it,
so source/H/extension isotropy are all zero. This is exact
asymptotic nonrecurrence, not a finite-resolution stopping decision.
On each of (0,1/2) and (1/2,1), f=P_22 is
a differentiable bijection with positive derivative. The full source
classes are precisely its integer-iterate classes, with the same
lag and extension formula derived in Section 4.3. Classes
cannot cross sides or merge with 0, 1/2 or 1;
each of those fixed cores remains separate. Finite predecessors
do not change these relations among the stated staying cores.
Other changing-root returns are not classified for this control.

## 6. Gate assessment and decision

| Gate | Result for BBD01 | Boundary |
| --- | --- | --- |
| T0 | Full partial Borel source, complete inverses, layered IMAGE and real extension | Not onto or ordinary continuous; no etale claim |
| T1 | Actual composition/divisor/real feedback owns its clock | Stronger arithmetic naturalness OPEN |
| T2 | ALL fixed states and complete fixed-root staying sets; positive primitive log(15/8) | Direct-prime target fails; changing-root periods NOT PURSUED |
| T3 | NOT SUPPLIED / NOT PURSUED | No borrowed trace or operator |
| Classical/formal | A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED | No geometric lift or Route credit |

Portfolio: **stop direct prime-time promotion; retain the owned integral
clock and complete fixed-root obstruction; fork a different architecture**.
The controls distinguish transport, orientation and permission; they do
not force this composition count, function or measure. No unconstructed
arbitrary-data PROVES_TOO_MUCH theorem is claimed. The same-object ledger
is intact; no endpoint, attracting trajectory or inconvenient packet
was removed to change the verdict.

## Reproduction and AI-assisted review disclosure

Inputs are the frozen formulas, full carrier and measure. Methods
are integration by parts, monotone inversion, stratified change of
variables, binomial growth, polynomial factorization and actual-tail isotropy.
No scientific numerical command, precision/period cutoff, external literature
lemma or prime/zero data is used. See [claim ledger](claim-ledger.md),
[evidence/locks](evidence/README.md), [internal review](evidence/independent-review.md),
[source/frontier record](evidence/scout-record.md) and [package index](README.md).
ARS raw-card, synthesis and adverse checkpoints are native inherited-
model/shared-context AI-assisted scrutiny, not external peer review,
independent-error evidence or formal verification; no venue calibration.
Positive 304, old packages, mirrors and Phase-I sources unchanged;
241/242 paused; goal active. Markdown only; no publication, upload or commit.
