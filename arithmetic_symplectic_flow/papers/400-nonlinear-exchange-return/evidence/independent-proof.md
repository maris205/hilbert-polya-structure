# Card-only independent proof — NER01

Candidate: `ANG-20260922-NER01`; package400.
Stage: released original-card mathematics, before PAPER UNLOCK.
Review type: internal, inherited model and shared history; `NOT_CALIBRATED`.
This is neither blinded discovery, external peer review nor error-independent evidence.

## 1. Inputs, access and obligations

- `candidate-card.md`: original84 lines, read completely through its original EOF;
  SHA256 `2074eb5583fd84c8cfabb8ebb02160ba560e6887c1b6e493eff94c71b38d21eb`.
- Existing CP1 `scope-review.md`:77 lines;
  SHA256 `a3acf9d5ff2ccdd4c2385f57bd396a4ffa2a704b6f99cc3673831ee598522bd5`.
- CP1 preceded mathematics. Root reported reading CP1 completely and explicitly
  released card-only mathematics; no PAPER UNLOCK has been received.
- Only the card supplied new scientific definitions. The applicable ARS router,
  workflow/DA/runtime/fallacy instructions and stream ownership rules were retained
  from their complete readings in this continuing review. No older theorem transfers.
- No manuscript, README, ledger, author proof, peer proof or other new scientific
  file was read. No auxiliary, web, scientific numerical run or model override was used.
- The card discloses prior scout exposure; this review does not erase that provenance.

All statements below concern the full nonnegative quadrant with the frozen Lebesgue
measure and pointwise inverse-Jacobian prescription. No null points are removed.
The classification stops at complete fixed and two-step returns, except for short
identities giving conditional cycle clocks or a global control potential.

## 2. Complete inverse domains, images and boundaries

Write a=floor x, b=floor y, d=gamma(a,b). For a target (u,v), every predecessor
must have v>0 and second source coordinate u>=0. Put b=floor u. The reconstructed
first coordinates for MAIN, L and N are respectively

    r_M=(d+u)/v-d*u,   r_L=(d+u)/v,   r_N=(1+u)/v-d*u.

For every a>=0, take d=gamma(a,b) and retain exactly a<=r<a+1. These inequalities
are the complete domains: r>=0 follows; L has r>0 automatically. A reconstructed
MAIN/N source cannot be the origin, since u=0 gives r=d/v or1/v>0.
Substitution verifies each forward equation, and solving that equation proves
exhaustion. Source floors are unique, so two retained digit labels never duplicate
one predecessor. All these domains and maps are Borel, including assigned cuts.
D instead has the single inverse r_D=(1+u)/v-u, on u>=0, v>0, r_D>=0.
Its entire image is u*v<=1+u with u>=0,v>0; no digit names are added to this owner.

The preceding tests are exact image criteria, not merely necessary bounds.
For b>=1, enumerate only d dividing b, reconstruct r, and require
gamma(floor r,b)=d. There are at most as many predecessors as divisors of b.
For b=0, first test a=0,d=1. For a>=1, d=a and the exact inequalities are

    MAIN: 0 <= a*(1/v-u-1)+u/v < 1;
    L:    0 <= a*(1/v-1)+u/v < 1;
    N:    0 <= (1+u)/v-a*(1+u) < 1.

These are countable inverse systems; MAIN and L are not finite-to-one.
For MAIN infinitely many predecessors occur precisely, within b=0, when
v=1/(1+u) and 0<=u<(sqrt(5)-1)/2. Otherwise the nonzero-slope inequality permits
only finitely many a; at zero slope with u(1+u)>=1 it permits none.
For L the infinite case is v=1, 0<=u<1. For N all fibres are finite.
No target with v=0 has any predecessor in any owner.

MAIN/D/N have only the origin terminal, with no incoming nonidentity arrow.
Every other forward history is infinite: the new second coordinate is positive;
a horizontal point moves to the vertical axis, then to the interior, and a vertical
nonorigin point moves directly to the interior. Interior histories stay interior.
L has the entire vertical axis terminal. A horizontal positive source enters it
in one step, while interior histories remain interior. Terminal L basins have depth
at most one because horizontal targets have no predecessors.
For MAIN and L, a vertical target (0,v) has predecessors exactly when v>1/2:
for v>1 its unique predecessor is (1/v,0); for v=1 they are all (a,0), a>=1;
for 1/2<v<1 they are (a/v,0) for integers a>=1 with a/(a+1)<v<=1.
For D and N every (0,v),v>0 has the unique predecessor (1/v,0).
These statements retain terminal incoming for L and do not extend its forward domain.

## 3. Every-Borel IMAGE and full-point clock

An inverse has form theta(u,v)=(r(u,v),u), so det Dtheta=-partial_v r>0:

    J_M=J_L=(d+u)/v^2;       J_D=J_N=(1+u)/v^2.

Fix a branch. Swap coordinates and apply the one-dimensional reciprocal change
of variables v -> r at each fixed u, followed by Tonelli. This proves
mu(theta E)=integral_E J for every Borel subset of its actual domain, including
unbounded E and infinite integrals. Restricting the rational diffeomorphism to
half-open cuts or axes does not invalidate this law. Finite positivity at every
assigned boundary point is supplied by the displayed extension, not by a.e. uniqueness.
The law is branchwise; it is not a claim that the many-to-one whole map preserves mu.

Along a legal trajectory write its successive coordinate sequence as x_i, so the
state at step i is (x_i,x_(i+1)) and x_(i+2)>0. Put n_i=d_i for MAIN/L and n_i=1
for D/N. Then each owner's own clock is

    kappa_i=2 log x_(i+2)-log(n_i+x_(i+1)).

All logarithms here have positive arguments, including axes and cuts.
For MAIN/D/N, with e_i=d_i for MAIN/N and e_i=1 for D, equivalently
kappa_i=log x_(i+2)-log(x_i+e_i*x_(i+1)). For L it is
log x_(i+2)-log x_i, where legal x_i>0. These are not declared positive roofs.

## 4. Actual histories, full kernels and incoming phases

Let I_p be a finite composition of actual inverse branches, with every intermediate
domain tested, and allow the empty history. Put

    K_m(z)=product_(0<=i<m) (n_i+x_(i+1))/x_(i+2)^2,   K_0=1.

For an actual arrow (z,m-n,w), T^m z=T^n w, one has
c=log(K_n(w)/K_m(z)). The branch-pair IMAGE from w to z is K_m(z)/K_n(w).
This follows from repeated every-Borel changes of variables; inverse branches of
each finite iterate are injective on their complete history domains.
Two representations of the same actual triple differ by common padding of their
valid histories; the appended factors agree and cancel. For composition, align the
two valid middle histories and cancel. Neither argument iterates past a terminal.
It also applies on null intersections without assuming different ambient branch
extensions have equal Jacobians there. Hence c is a full-point Borel cocycle on the
actual retained-integer-lag groupoid, not on a freely named history space.

The full lag kernel consists of the triples witnessed with m=n. The full clock
kernel consists of the actual triples with K_m(z)=K_n(w); their intersection imposes
both conditions. These exact global descriptions do not assert a finite cell census.
For all four owners the legal forward arrow (1,0)->(0,1) has clock zero but nonzero
lag and is not a unit; for L its range is terminal. Thus the full clock kernel is
not merely the isotropy kernel. Equal clock values do not identify source states.

For any reference r its entire source orbit/incoming set is

    O_r={ I_p(T^n r) : n is legal and p is any finite legal inverse history }.

The corresponding arrow to r has lag n-|p| and is determined by the actual triple;
the inverse arrow has lag |p|-n. This enumerates every incoming branch, including
arbitrarily deep predecessors, and shows countability. It is not ordinary eventual
tail equivalence without the specified dynamics. Height translation commutes with
every extension arrow for all real times, so the quotient SET has a complete action;
no topological, Hausdorff or contact upgrade is made.

For any deterministic partial owner, a state eventually entering a least-q cycle
has source isotropy qZ. Otherwise its source isotropy is0. In particular terminal
basins have isotropy0. If C is the sum of kappa around that actual cycle, then
c(kq)=kC, H=CZ, with transient contributions cancelling. Extension isotropy is
qZ when C=0 and trivial when C!=0. These are whole groups, not one-loop samples.
The lag kernel within any source isotropy group is trivial, as is its intersection
with the clock kernel; this does not make the full arrow lag kernel trivial.
If T^r z=T^n x, the phase relative to x is h+S_n(x)-S_r(z) modulo H_x.
For a fixed core p this becomes h-S_r(z) modulo H_p. Distinct cores merge only
when their actual source orbits coincide, never merely because their clocks agree.

Every actual MAIN/D/N cycle is interior. Summing the alternative clock and using
cyclic product cancellation gives the exact, strictly negative cycle value

    C=-sum_i log(1+e_i*x_(i+1)/x_i) < 0.

Consequently every such cycle, if it exists, has positive primitive time -C,
and every MAIN/D/N extension isotropy group is trivial. This identity does not
classify higher cycles or establish their existence or their target times.

For L there is a full-source Borel potential, including its terminal boundary:

    B(x,y)=log(x*y) if x,y>0;
    B(x,0)=log x if x>0;  B(0,y)=log y if y>0;  B(0,0)=0.

Direct substitution gives kappa=B(Tz)-B(z) at every legal point, both interior
and horizontal. Hence c(z,k,w)=B(w)-B(z) on the entire L groupoid.
ALL L return-time groups are0, and extension isotropy equals source isotropy.
Its full clock kernel is B(z)=B(w), with equal lag additionally for the intersection.
The complete phase over each L source orbit is h+B(z), up to a reference constant,
and its physical quotient is a real line. This proof uses its own frozen measure
and does not transfer the result to MAIN or replace any clock by a chosen density.

## 5. Exhaustive fixed and legal two-step return sets

A fixed point or legal T^2 return must be interior: every output has positive
second coordinate, and the second iterate has positive first coordinate.
If T^2(x,y)=(x,y), then necessarily T(x,y)=(y,x). Symmetry of gamma implies that
the two contents agree, including on the assigned integer cuts. The equations are

    MAIN: x^2+d*x*y=d+y,  y^2+d*x*y=d+x;
    D:    x^2+x*y=1+y,    y^2+x*y=1+x;
    L:    x^2=d+y,        y^2=d+x;
    N:    x^2+d*x*y=1+y,  y^2+d*x*y=1+x.

Subtracting gives (x-y)(x+y+1)=0 in every case, so x=y=t>0.
MAIN's diagonal equation factors as (t-1)((1+d)*t+d)=0; D is its d=1 case.
Both therefore have only t=1, with actual d=1. N obeys (1+d)t^2=t+1:
d>=1 forces t<=1, while d>1 would force t<1 and thus actual d=gamma(0,0)=1,
a contradiction. N also has only t=1.
For L, t^2=t+d forces t>1. With a=floor t>=1, actual d=a and
t=(1+sqrt(1+4a))/2. The lower cut a<=t is equivalent to a(a-2)<=0;
the upper cut t<a+1 holds for a>=1. Thus a=1 or2, giving phi=(1+sqrt5)/2 or2.

Therefore MAIN/D/N have Fix(T)=Fix(T^2)={(1,1)}. L has
Fix(T_L)=Fix(T_L^2)={(phi,phi),(2,2)}. ALL exact least-two return sets are empty.
This proves exhaustiveness over the quadrant, not merely over selected digit cells.

## 6. Entire incoming and packets of every discovered core

For MAIN/N, the target (1,1) has b=1, forcing d=1 for every possible a;
the reconstructed r=1. D has the same unique predecessor directly.
Thus each one's full source orbit and basin of p=(1,1) is the singleton {p}.
For each, J(p)=2, kappa(p)=-log2, source isotropy Z, H=log2 Z and extension
isotropy0. Its one positive primitive packet has length log2, repetitions k log2,
and all phases R/(log2 Z). Negative c on the positive lag generator is consistent
with this positive generator of the ENTIRE return group.

For L, the target (phi,phi) has b=1, hence d=1 and the unique predecessor itself.
Its basin is a singleton. The target (2,2) has exactly two immediate predecessors:
(2,2) from d=2,a=2, and (3/2,2) from d=1,a=1.
Its COMPLETE basin is {I_p(2,2):p any finite actual L inverse history}, with the
explicit inequalities of section2 at every generation. This is an exact exhaustive
countable description with no depth cutoff; it includes more than the fixed point.
No claim of finiteness or countable infinitude is needed. The two L basins cannot
merge because their deterministic forward histories enter different fixed points.
Every state in either basin has source isotropy Z, H=0 and extension isotropy Z.
The phases are h+B(z)-log(phi^2) and h+B(z)-log4 respectively, in R, not circles.
They are not positive physical primitive packets, despite their source fixedness.
All terminal L orbits instead have source and extension isotropy0, and the same
potential formula supplies their complete real phases and all depth-one incoming.

## 7. Lineage, bounded decision and strongest counterargument

On a full cell (n+xi,m+eta), d=gcd(n,m), so m divides n iff d=m. The MAIN
update uses that same d in numerator and cross denominator, and its new real state
supplies the next digits. Thus the stated arithmetic readout is genuinely present
without a prime table or an extra passive root. Its choice remains a design choice.

The complete MAIN short-return window has exactly one positive primitive packet,
of length log2; it supplies neither a nonprime primitive nor repeated prime-2 copies.
The strongest positive reading is therefore genuine: the specified short window
is consistent with the necessary prime target, and its nonemptiness is proved.
It is NOT all-prime coverage, global packet uniqueness or a complete periodic ledger.
Those remain OPEN, and no further census is authorized by this card.
Conversely, D and N preserve this same prime-2 probe, so the probe does not show
that either content occurrence is necessary for that local result. L's global
zero-time obstruction belongs only to L and cannot be used to convict MAIN.

Scoped decision: owner and full short-return audit established; MAIN's global
target remains bounded OPEN. Close this gate without a manufactured negative,
and retain the card's bounded STOP/FORK boundary rather than extend the census.
Strong arithmetic naturalness is OPEN. Classical fields are NOT APPLICABLE,
T3 NOT AUDITED, formal Route coordinates UNASSIGNED, and Route B NOT INVOKED.
No unresolved definition/owner correction was found. CP2/CP3 await separate
PAPER UNLOCK; this original-card proof does not pre-approve any manuscript.

EOF — card-only independent derivation frozen after full readback.
