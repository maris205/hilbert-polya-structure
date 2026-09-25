# DSA01 — frozen-card independent geometric derivation

Date: 2026-09-25, environment metadata.
Candidate: `ABF-20260925-DSA01`, package `487-divisor-scatterer-array`.
Reviewer: `pcr01_independent_review`, separate from author/helper.

## 0. Release, exact input and scope

This derivation follows DISTINCT RAW RELEASE after root's reported FULL
read of the 163-line CP1 report. Sole scientific input: original 91-line
candidate card, SHA-256
`a52c8793de88cd52dd03e0157e6aa755ec641c4ea0fa1ac16691f3865637de72`.
It was personally FULL read 1–91 EOF before scope review. The scope hash is
`1ee65ddee192a477b893d9710980d1787cf4568a3a8b44a4a56d70d562e984cf`.
No author paper/README/ledger, current peer/helper answer or old proof was
opened. No scientific program, numerical experiment, external source,
network, Git, PDF or old-file edit was used. No work on 490 is undertaken.

Retained ARS/local instruction reads and inherited reviewer exposures are
disclosed in CP1. This is a direct original-mathematics derivation, with
categorical evidence rather than a forced issue or numeric review score.
Same model and shared history: NOT_CALIBRATED, not blind/outcome-sealed,
human, external or cross-model validation. The card's prior author/design
exposures are not erased by separate reviewer authorship.

Only the two specified two-collision itineraries are classified. The
global owner and measure proofs are not a census of other collision words.
Physical elapsed time is retained throughout; no IMAGE logarithm or new
roof is substituted for flight time.

## 1. Full array geometry

Write c_{n,d}=(n,d), n,d>=1. MAIN assigns radius 1/4 exactly when
1<d<n and d divides n, and radius 1/8 otherwise. The two obstacle controls
assign respectively all radii 1/8 and radius 1/4 exactly for even n.
In every array the same elementary bounds hold:

    1/8 <= r_c <= 1/4,     |c-c'| >= 1 for c != c',
    dist(closed disk_c, closed disk_c') >= 1-1/4-1/4 = 1/2.

They apply separately to each frozen assignment, not by transferring an
already constructed MAIN flow to a different geometry. Any compact set
can meet only disks with centres in its bounded 1/4-neighbourhood, which
contains finitely many integer addresses. Thus the arrays are locally
finite. Their closed disks, and in particular their boundary circles,
are pairwise disjoint with a uniform positive gap.

Let Q be the plane minus all OPEN disks. It is closed; its boundary is
the locally finite union of the circles, all retained. It is path connected:
join two points by a straight segment, which encounters finitely many
disks. Whenever it traverses an open disk, replace that traversed portion
by an arc on the same boundary circle between the entry and exit points.
The circles are disjoint from every other closed disk, so these finitely
many replacements stay in Q. Tangencies need no replacement. This also
handles endpoints already on a boundary. No cell quotient or disjoint
integer-fibre carrier is introduced.

## 2. The exact boundary quotient as a measurable owner

Put Y=Q times S^1. On a boundary circle at q define nu=(q-c)/r and

    R_q v = v-2(v dot nu)nu.

This is an involution of S^1. The stated equivalence classes are singletons
in the interior; on the boundary they are {v,R_q v}, with a singleton at
grazing. Different q are never identified. Disjointness of circles makes
nu unambiguous. Thus this prescription is an actual equivalence relation,
with no hidden translation, word or time-reversal identifications.

Its quotient M has a concrete standard Borel description. Choose the
unique representative in

    B = (interior Q times S^1)
        union {(q,v):q in boundary Q, v dot nu >= 0}.

For negative normal component replace v by R_q v; for nonnegative normal
component keep it. At zero component the two representatives coincide.
This selector is Borel, since the locally finite boundary and its normal
field are Borel. It identifies exactly the equivalence classes. Conversely
the saturation of any Borel subset of B is that set together with its
reflected boundary part, hence Borel. Therefore the natural quotient
sigma-algebra is exactly the Borel structure represented by B. B is a
Borel subset of the original Polish product, giving a standard Borel
owner. This description keeps grazing and all boundary states; it is not
replacement by the regular collision section or by a full-measure subset.

## 3. Unique all-point physical execution and completeness

Take a state in its above positive-time representative. In the interior
use q(t)=q+t v at speed one until the first strictly future contact with
any closed obstacle disk. With p=v this is precisely H=|p|^2/2=1/2,
qdot=p and pdot=0 on the interior, not a global smooth boundary Hamiltonian.
At an initial boundary point use the prescribed
nonnegative-normal representative and do not recount the initial contact.
For that same disk,

    |q+t v-c|^2 = r^2+2tr(v dot nu)+t^2 > r^2, t>0.

So an outgoing or tangent ray immediately leaves that circle into Q and
cannot next hit the same disk without a different intervening collision.

A prospective contact with another disk is the first nonnegative root
of |q+t v-c|^2=r^2, with the tangent double root included. If a strictly
future contact exists at finite distance, its first time is attained:
on any bounded candidate flight segment only finitely many disks occur.
At an interior start the distance to the closed boundary is positive;
at a boundary start all other disks have positive uniform separation.
Thus no positive-time contacts accumulate at the starting instant.
If there is no next contact, the straight ray continues for all future
time; it is not a terminal or a deleted state.

At the first contact the incoming normal component is nonpositive.
For a negative component apply R_q, producing an outgoing vector; for a
zero component R_q v=v and the same tangent line continues. No time is
added. There is exactly one contact circle, since their boundaries are
disjoint. This defines the next flight uniquely, including a grazing hit.
There is no sliding boundary trajectory or stationary state hidden in the
rule: the displayed distance identity applies also to tangent departure.

Successive strictly future contacts are on different circles, and the
straight segment between them has length at least 1/2. Consequently a
bounded time interval has finitely many contact events, even if tangencies
are counted as events. There is at most one initial/first event plus a
number bounded by twice the elapsed time, up to an integer rounding.
No simultaneous impacts or finite-time collision accumulation can occur.
Position cannot escape to infinity in finite time because its speed is
one. Finite recursive execution therefore reaches every prescribed finite
positive time, with a continuing free ray if future contacts cease.

Define time reversal I[q,v]=[q,-v]. It is well defined on the quotient
because R_q(-v)=-R_q(v); it is an involution. Reversing every straight
segment and using R_q^2=id reverses each transverse collision. A tangent
segment reverses as a tangent segment without an extra rule. Consequently
negative-time execution is unique by the same construction, and

    I phi^t I = phi^{-t}.

Uniqueness at every state and autonomy give phi^{s+t}=phi^s phi^t and
phi^0=id, including starting/ending at a collision or grazing point.
Thus phi is a complete invertible all-point flow on the stated M.

Measurability is also direct. Each circle's prospective root/time and
contact point are Borel functions, allowing infinity for no contact.
The infimum over the countable array is Borel; a finite first contact is
attained at its unique obstacle, whose index is Borel by countable tests.
Reflections and the canonical boundary selector are Borel. On sets with
a specified finite event itinerary, the recursive execution and the
observation at time t are Borel in (t,z). Such countably many sets cover
every bounded time window by the event bound. Negative time uses I.
This proves a jointly Borel all-point flow, not an assertion of global
smoothness across collisions/grazing.

## 4. Own physical Liouville measure and regular section

The original measure on Y is dq_1 dq_2 dtheta, with angular Lebesgue
measure on S^1. Each boundary circle has planar measure zero; countably
many circles and their velocity fibres still have measure zero. Define
mu_M as its pushforward under the actual quotient map. It is sigma-finite,
has no extra boundary atoms, and no arithmetic weight is inserted.

Free flight (q,theta)->(q+t v(theta),theta) has Jacobian one: its derivative
is block triangular with identity position block and unchanged theta.
For the collision calculation choose oriented arc length s, unit tangent
tau(s), and nu(s). Incoming and outgoing transverse velocities are

    v_-(s,u)=-sqrt(1-u^2) nu(s)+u tau(s),
    v_+(s,u)= sqrt(1-u^2) nu(s)+u tau(s),    -1<u<1.

Reflection preserves the same u. The flux measure through either side
of the boundary is |v dot nu| ds dtheta = ds du in absolute coordinates,
because |du/dtheta|=|v dot nu|. More explicitly, the free-flight flow-box
coordinates (s,u,t) pull dq_1 dq_2 dtheta back, in absolute density, to
ds du dt. The initial determinant is the normal speed times ds dtheta;
free-flight Jacobian one transports it throughout the flow box.

On an actual regular collision-return branch, the next circle is fixed,
both impacts are transverse and there is no intervening contact. Its
flight length ell=|q'-q| is smooth locally. Differentiating the distance
along that branch gives

    d ell = v dot d q' - v dot d q = u' ds' - u ds.

The incoming tangential component u' equals the reflected outgoing one.
Taking another exterior derivative therefore gives

    T_collision^*(ds' wedge du') = ds wedge du.

This proves the exact asserted section two-form on each actual regular
branch, with its own two circles and flight, rather than assuming a global
return map. Flights with no next contact and grazing states need not be
on this section. They remain in the full physical owner.

The same calculation proves full-volume preservation through transverse
collisions. In flow-box coordinates crossing one such return replaces
(s,u,t) by (T_collision(s,u), t+constant-ell(s,u)). Since ds wedge du is
preserved, wedging with the last differential cancels its d ell term.
Hence ds du dt, and therefore dq_1 dq_2 dtheta, is preserved on the actual
regular fixed-time transport chart. Finite itineraries give the same
identity by composition; free legs use the preceding Jacobian-one map.

For completeness the exceptional sets used in this measure proof are
null, not removed from the owner. The set of free states that reach a
specified circle tangentially is covered by the two smooth parametrizations

    (s,t) -> (q_circle(s)-t v_tangent(s), v_tangent(s)),

one for each tangent direction, on countably many bounded parameter
patches. Their two-dimensional images have zero three-dimensional
Liouville measure. There are countably many circles. A first grazing hit
after finitely many transverse hits pulls such a null set back through
countably many regular finite-itinerary flow charts, which are local
volume-preserving diffeomorphisms. This is still null. There are only
finitely many hits in any bounded time interval; the choice of the first
grazing hit and previous finite itinerary is countable. Equivalently one
can choose a rational observation time after the last transverse event
and before that first grazing event, reducing to the same free tangency
locus. Starting at the boundary is null; ending there at a prescribed time
is null by regular flow boxes, with the grazing case already covered.

On the remaining countable regular charts the fixed-time map has the
proved volume identity. Time reversal supplies the same null-set statements
for inverse transport. Therefore the exceptional set and its transported
image are both null, and for EVERY Borel E in the full quotient,

    mu_M(phi^t E)=mu_M(E),   t in R.

This is preservation on the full owner, not a deletion of exceptional
states or an a.e. redefinition of their execution. All-point dynamics was
constructed independently in Section 3. The argument applies separately
to MAIN, DIVISOR-OFF and PARITY with their own actual disks and quotient.
It does not turn any of them into a global smooth ASFS suspension.

## 5. Full histories, actual arrows and physical phases

For each of these flows use exactly

    G_phi={(phi^t z,t,z): z in M, t in R}.

The source is z and range phi^t z; inverse time is -t and composition
adds physical times. Identical triples only are identified. A closed
orbit has distinct repetition arrows at different t even when its
endpoints agree. Every past/future of every state exists, including free
rays and grazing histories, by Section 3. No separate symbolic lift,
event-count clock or additional height-extension owner is introduced.

Its entire stabilizer is the actual set H_z={t:phi^t z=z}. For the
classified cycles below we prove H_z=L Z, so phases on the one physical
orbit are R/(L Z) and positive repetitions are kL. A phase is not a second
primitive packet, and neither equal time nor a translated itinerary
identifies different physical orbits. We make no stabilizer classification
for untested collision words merely from the existence of these cycles.

## 6. ALL two-collision closures for a specified pair of circles

Consider two disjoint disks with centres c_A,c_B, radii r_A,r_B and
D=|c_B-c_A|>r_A+r_B. Suppose an actual closed itinerary has exactly the
two boundary impacts a on A and b on B in one traversal, with no other
contact. The two free legs must be the segment from a to b and its reverse.
Put e=(b-a)/|b-a|. Reflection at b must change e into -e, and reflection
at a must change -e into e. The reflection equation forces these velocities
to be normal, not tangent: at b, e=-nu_B(b); at a, e=nu_A(a), using the
actual incoming/outgoing signs. Thus

    a=c_A+r_A e,      b=c_B-r_B e,
    c_B-c_A=(|b-a|+r_A+r_B)e.

The coefficient is positive. Consequently

    e=(c_B-c_A)/D,
    a=c_A+r_A e,  b=c_B-r_B e,
    ell=|b-a|=D-r_A-r_B.

This proves uniqueness over ALL boundary points and unit incidence angles,
not only a centre-line ansatz. Both incidence tangential components are
u=0. Grazing cannot reverse a nonzero unit vector and provides no additional
two-collision closure. Far-side normal candidates have the wrong physical
signs and cannot satisfy the displayed vector equation. Conversely these
two impacts give a valid two-bounce orbit whenever their segment is clear
of all other obstacles, which will be proved for each frozen pair below.

This argument also covers a periodic trajectory initially observed in a
free leg: choose its first A impact as phase origin. Exact closure after
the two-impact itinerary returns to that same impact state. Repeated
traversals of this already closed trajectory are repetitions of the same
orbit, not additional members of the classified two-collision family.
This does not classify longer words that have not closed after two impacts.

## 7. Hidden-contact exclusion in the FULL arrays

For either specified pair let c_A=(n,2), c_B=(n+1,2), with n=4 or 6.
The candidate segment lies on y=2 between n+r_A and n+1-r_B.
Any other centre (m,j) with j!=2 has distance at least 1 from this segment,
strictly larger than every obstacle radius. If j=2 and m is neither n nor
n+1, its horizontal distance from the segment is at least 1, again greater
than every radius. There are no other positive-integer centres between
the two endpoints. On the two selected disks themselves the segment meets
the boundary only at its own respective endpoint and never enters a disk.

Hence no third obstacle meets even the CLOSED segment, either transversely
or tangentially. This verifies the actual complete itinerary in the full
unbounded array, simultaneously for the three frozen radius assignments.
It is not a reduced two-obstacle owner or an exclusion based on a plotted
window. Combined with Section 6 it proves existence and complete uniqueness
of each specified two-collision family for each obstacle owner.

## 8. MAIN: exact times, ENTIRE H, phases and distinct packets

At the four named addresses the proper-divisor predicate is true at
(4,2) and (6,2), and false at (5,2) and (7,2). Thus each selected pair
has r_A=1/4, r_B=1/8 and D=1. The complete two-collision data are

| Itinerary | A impact a | B impact b | Outgoing at A / B | One-leg ell | Primitive L |
| --- | --- | --- | --- | --- | --- |
| C1 | (17/4,2) | (39/8,2) | (1,0) / (-1,0) | 5/8 | 5/4 |
| C2 | (25/4,2) | (55/8,2) | (1,0) / (-1,0) | 5/8 | 5/4 |

The incoming normal vectors at each impact are the negatives of the
displayed outgoing ones and are identified by the actual collision
quotient. Each row is one closed flow orbit, not a choice of one point
from an unclassified angle family.

To prove the ENTIRE H, start at a with its outgoing e=(1,0). For
0<t<ell the state is (a+t e,e). At t=ell it is the collision class at b.
For ell<t<2ell it is (b-(t-ell)e,-e). At t=2ell it returns to the original
collision class at a. No earlier phase equals it: the endpoints have
different positions, and the open legs have different velocities even
where their positions coincide. More generally this parametrization is
one-to-one on R/(2ell Z), with the boundary representative identifications
only at the intended endpoints. Therefore every state of the orbit has

    H_z=(5/4)Z,   least positive primitive L=5/4,
    all real phases R/((5/4)Z),   repetitions k(5/4), k>=1.

This is not merely an exhibited return or a period divided by the number
of collisions. Time reversal maps phase t to -t modulo L at the chosen
normal-impact origin. It is the SAME physical orbit, since the reverse
velocity is already the other leg (and the impact pair is identified).
Thus the actual classification supplies one packet per row, not two by
orientation and not a count divided by two without proof.

The C1 and C2 position segments are disjoint. They cannot belong to the
same flow orbit, since every position on either of these completely
described orbits lies on its own segment. Their translation by two spatial
units is not a quotient operation. Hence MAIN has TWO DISTINCT primitive
packets at exactly the same positive time L=5/4.

If that time is log p for an ordinary prime, uniqueness at that prime is
false. If it is not, prime-only purity is false. In either case the target
conjunction is refuted. No decision about exp(5/4), irrationality or
transcendence is used or claimed, and no other collision words are tested.

## 9. Three independently owned full controls

### 9.1 DIVISOR-OFF

All centres remain, all radii are 1/8, and its Q, quotient, complete
specular flow, time reversal, physical measure and regular section are
constructed by Sections 1–4 for that assignment. This is not MAIN with
its time labels changed. Section 6 classifies all impacts and angles;
Section 7 excludes contacts with every other obstacle.

| Itinerary | A impact | B impact | One-leg ell | ENTIRE H / primitive |
| --- | --- | --- | --- | --- |
| C1 | (33/8,2) | (39/8,2) | 3/4 | (3/2)Z; 3/2 |
| C2 | (49/8,2) | (55/8,2) | 3/4 | (3/2)Z; 3/2 |

Each has only normal incidence, outgoing (1,0) at A and (-1,0) at B.
The explicit two-leg phase proof applies with ell=3/4: all phases are
R/((3/2)Z), repetitions k(3/2), and time reversal is the same orbit.
The disjoint position segments prove two distinct equal-time packets.
The target purity-plus-uniqueness conjunction fails here too, without
evaluating whether the common time is log-prime.

### 9.2 PARITY

This owner uses radius 1/4 at every even-n centre, independently of d,
and radius 1/8 at odd-n centres. Its full geometric domain and its own
flow/quotient/measure are established by the same explicit all-point
construction, not identified with MAIN's global array.
For C1 and C2 its four radii happen to equal MAIN's four radii exactly.
The complete classification and hidden-contact proof therefore give
the same two rows as Section 8, with normal incidence, ell=5/8,
ENTIRE H=(5/4)Z, primitive 5/4, all phases and repetitions, one packet
per row, and distinct packets between rows. Time reversal again stays
inside each packet. MAIN and PARITY are NOT distinguished by these
frozen short tests. This is a limit of the test, not a global conjugacy
or equality claim for their different arrays.

### 9.3 COLLISION-OFF

The owner is the whole R^2 times S^1, without deleted disks or boundary
quotient. Its actual complete flow and inverse are

    phi^t(q,v)=(q+t v,v),     phi^{-t}(q,v)=(q-t v,v),   |v|=1.

It is jointly smooth and preserves its own dq_1 dq_2 dtheta by the
Jacobian-one calculation. I(q,v)=(q,-v) gives its time reversal. A return
requires t v=0, and since |v|=1 this forces t=0. Thus at EVERY state
H={0}, there are no positive primitives or repetitions, and all real
phases along each oriented free orbit form R, not a circle. Opposite
velocities give different free flow orbits, since the velocity never
changes; time reversal does not generally mean same-orbit equivalence.
There is no regular collision section or fictitious collision measure.
Its failure of positive nonemptiness is a statement about this control,
not a missing subset or a clock to be borrowed by MAIN.

## 10. Ownership, target boundary and decision

The proper-divisor address bit controls actual obstacle geometry and thus
actual reflection and admissible collision words in one connected full
domain. The original physical time, Liouville measure and collision
quotient were retained separately for each obstacle owner. No static
integer component, selected centre, logarithmic roof or borrowed operator
was used to manufacture an orbit or its time.

MAIN has positive closed packets and a decisive equal-time multiplicity
obstruction to the combined target. This proves failure of the required
purity-and-uniqueness conjunction without deciding which individual clause
fails at 5/4. It does not prove absence of all prime-log packets, classify
other periods, or decide all-prime coverage. Those global questions remain
OPEN / NOT AUDITED under the frozen two-word gate.

DIVISOR-OFF changes the actual times of the two families, showing a real
geometric effect of changing radii. PARITY gives precisely the same short
data as MAIN, so that effect is not specific evidence for a divisor-only
or prime-generating mechanism. The two-normal-reflection construction
works through ordinary two-circle geometry; the controls expose this
PROVES_TOO_MUCH limitation. COLLISION-OFF has no positive returns.

The proofs used global radius bounds and exact clearance, not a finite
numerical window. No perturbation campaign or arbitrary-radius robustness
theorem is claimed: exact equal times depend on the fixed pair separations
and radius sums. Radius choices, strong naturalness and behaviour of other
words remain open design/scientific questions. No radius retuning, change
of velocity scale, packet merging or new quotient is made as a repair.
The card's static arithmetic configuration is not trial division, a prime
generator, a Logistic/Henon conjugacy or classical dimensional-lift credit.

Outcome: OWNED COMPLETE BILLIARD; DISTINCT EQUAL-TIME TWO-COLLISION PACKETS
— STOP / FORK. T0 is established at the stated geometric/measurable and
measure-preserving level. T1 target is NOT PASSED. T2's stated full-flow
packet convention and two-itinerary classification are established, not
a global prime-orbit ledger. T3 NOT AUDITED; classical ASFS fields NOT
APPLICABLE; formal Route coordinates UNASSIGNED; Route B NOT INVOKED.
No trace, determinant, spectral or RH claim is made.

Freeze after complete self-read and hash receipt. HOLD for root's FULL
raw read and a distinct PAPER UNLOCK before any author-file comparison.
