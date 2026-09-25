# Internal exact review — reciprocal factor-quotient feedback

Candidate: ANG-20260920-RFQ01.
Package: 306-reciprocal-factor-quotient-flow.
Status: OWNED RECIPROCAL CLOCK; NON-PRIME FIXED-PACKET TIMES — STOP / FORK.
Verdict: PASS for the scoped owner and complete fixed-family theorem.
Calibration: NOT_CALIBRATED; no venue-specific criteria binding supplied.

## Inputs, access order and execution scope

I first read the entire original 156-line [card](../candidate-card.md),
before any 306 manuscript or scout access. Its actual SHA-256 is

    26c55f23a9fe68f8ed6d04379738e10b009fa90d1cfe5a51c8a9d0445744e33f

The complete independent raw branch/clock, all-fixed-state and three-control
findings were sent to root and acknowledged before manuscript access.
I then read the complete 319-line [paper](../paper.md), with verified
comparison-input SHA-256

    eb13640718ccd9b0ca143fffcf29eab636ac38917af5c07a95162b959233c8b4

After the one minor directional precision edit below, I read back
the changed passage and verified the final 319-line manuscript hash:

    0dfd6ab7d5b0ea70167fb879852df1261cdee6fac46c8799e4d1109edf3ea427

This final version is the report's binding. The unchanged mathematics
was not re-run or represented as a fresh independent review round.

The original card's first 156 lines were rehashed at manuscript review
and still match the freeze. Administrative appends are not raw inputs.
The author received raw results before manuscript comparison; this
was not ideation-blind or an independent-error experiment.

The native auxiliary atomic_clock_scope read only the raw card and
checked SCALE-OFF, UNIT-TRANSPORT and FACTOR-OFF. It did not receive
main proof work, manuscript, scout or peer answers. Its receipt copied
the correct literal sha256sum output. No metadata correction arose in
this round. I independently derived and checked the main theorem and
all three controls; the auxiliary corroboration is controls-only.

ARS supplied the raw, synthesis and final-adverse checkpoints.
This is inherited-model/shared-context internal scrutiny, not external
peer review, cross-model verification, formal verification or evidence
of independent error processes. No old return theorem or clock was
imported. No external lookup, scientific numerical computation, new
architecture, general main-period census or T3 work was performed.
Only this reviewer-owned report was written.

## Checkpoint 1 — independent raw-card results

**Ownership passes; the all-fixed-family gate stops target promotion.**

### Actual branches and complete partial owner

For every allowed a,b,j, the half-open source digit interval
(1/(j+1),1/j] maps bijectively onto [0,1/c), with ac=b+j.
At target (B,C,t), every predecessor is exactly

    (A,B,1/(j+C*t)), j=A*C-B>=1, 0<=t<1/C.

All such A are retained and give different predecessor roots.
There are infinitely many for each allowed target. Thus the full
image is the union over ALL B,C>=1 of their intervals [0,1/C),
not the full carrier. Every zero-seed state has incoming arrows,
but none has a forward step. Failed-divisibility states are also
retained as terminals; an incoming history does not complete them.

The domain and branches are Borel; the partial map and its defined
iterates are countable-to-one. Reciprocal digit boundaries can change
the discrete next root, so usual-topology continuity or an etale
owner does not follow from the locally compact carrier.

### Nonconstant IMAGE and null-point consistency

Ordinary monotone substitution gives, for EVERY Borel E in a branch,

    mu(I(E))=integral_E C/(j+C*t)^2 dmu.

The whole-interval mass ratio C/[j(j+1)] is only an average,
not the pointwise density. At a defined source state,
D(z)=1/(c*x^2) is the forward absolute derivative.
Write D_m for the product along m actually defined steps, with D_0=1.
For an arrow w->z represented by T^m z=T^n w,

    J=D_n(w)/D_m(z),
    c_time=log D_m(z)-log D_n(w).

The sign of a general branch clock is not assumed positive.
The retained-lag equalizer relation is a countable Borel groupoid.
To compose histories, extend the shorter middle history only along
the longer history already known to exist. This never crosses an
undefined terminal step. Two presentations of the same triple differ
by a common legal future; its identical derivative factors cancel.

This proves pointwise presentation independence and the cocycle law,
including endpoint or null-domain restrictions. On such restrictions,
the value is the frozen derivative of the specified analytic history,
not a derivative forced by the restricted map on a singleton or by
an a.e. Radon–Nikodym class. At target seed zero, an inverse has
finite positive derivative C/j^2; no forward derivative at zero
is evaluated. Actual inverse and forward derivatives reciprocate.

The extension keeps every Y x R object and every arrow.
Translation of the real time coordinate is complete, jointly Borel
and commutes with arrows. Only the set-level quotient action is used.
No Hausdorff or standard-Borel coarse quotient, embedded circle or
continuous quotient flow is inferred.

### ALL fixed states, least time and packet nonmerging

Fixed root equality forces a=b=c=n and j=n(n-1).
The unit n=1 requires the forbidden digit zero. For n>=2,
the seed equation is

    n*x^2+j*x-1=0.

Its unique positive root x_n lies in (0,1/n): the polynomial
is increasing there, negative at zero and positive at 1/n.
Then 1/x_n=j+n*x_n with 0<n*x_n<1 verifies the actual digit,
not just formal algebraic solvability. Neither endpoint is fixed.
These are ALL fixed states over all retained roots and seeds.

At each z_n=(n,n,x_n), source isotropy is Z and

    L_n=-log(n*x_n^2)>log n>0,
    H_(z_n)=L_n Z,
    extension fixed-object isotropy=0.

The least positive generator is L_n itself. Higher multiples are
repetitions of this same packet, not new primitive states.
Different fixed cores have different constant actual tails.
Finite inverse excursions cannot merge them: composing such arrows
would imply an impossible equality of their constant tails.
Transient preimages in a core's source orbit have the same isotropy
clock image and do not create a second packet for that core.

The raw calculation also gave, with lambda_n=1/(n*x_n^2),

    lambda_n+1/lambda_n=K_n=n*(n-1)^2+2>=4.

In the raw proof, K_n^2-4 lies strictly between (K_n-1)^2
and K_n^2, proving irrationality of lambda_n.
Thus every fixed-family primitive time is NOT log of an integer.
Already n=2 gives L_2=log(2+sqrt(3)), a decisive failure
without assuming that an integer root is the corresponding prime.
The complete fixed family is countable, with one packet per such
fixed core; this is NOT a complete higher-period packet ledger.
No broader main return census was undertaken.

### Three separately owned controls

SCALE-OFF has target [0,1) in each (B,C) fibre and inverses
1/(j+t) for all A with j=AC-B>=1. Its own IMAGE is
1/(j+t)^2 and its forward absolute derivative is 1/x^2.
Its ALL fixed states have n>=2,j=n(n-1) and unique seed
y_n solving y_n^2+j*y_n=1. Since 1/y_n=j+y_n and
0<y_n<1, digit consistency holds. Source isotropy is Z,
least positive time is -2 log y_n, and extension isotropy is
zero. Different fixed cores do not merge. No other periods are
classified by this fixed-family result.

UNIT-TRANSPORT's inverse target interval is (1/(j+1),1/j],
with j=AC-B>=1, and the inverse seed map is identity.
At a specified target its digit fixes the only possible A=(B+j)/C;
if this is not a positive integer there is no predecessor.
Zero-seed targets have no incoming inverse in this control.
Own IMAGE is one, so EVERY time group is zero.
ALL fixed states are (n,n,x), n>=2, on the complete
half-open interval with digit n(n-1). Every such point has
source and extension isotropy Z; zero time does not erase it.

FACTOR-OFF has inverse targets precisely C>B and 0<=t<1/C.
With j=C-B, every A>=1 yields predecessor (A,B,1/(j+Ct)).
Its own IMAGE is C/(j+Ct)^2, not an imported constant clock.
The second root strictly increases at EVERY defined step.
Hence no two distinct defined iterates agree: there are no
periodic or eventually periodic states, and ALL source isotropy,
time groups and extension isotropy are trivial.
Incoming terminal arrows do not change this result.

Each control uses its own forward derivative products, target domains,
endpoint prescription and legal-history cocycle. FACTOR-OFF's zero
time groups follow from absent isotropy, not a globally zero cocycle.

## Checkpoint 2 — full manuscript comparison

**PASS; the one nonblocking directional wording suggestion is closed.**

Sections 2–3 match the complete branch enumeration, full Borel
change-of-variables law and partial-history argument above.
The null-intersection proof uses an explicit analytic prescription
plus legal common-future cancellation, not a.e. uniqueness.
The Borel carrier/groupoid/time distinctions remain intact.

Section 4 proves all fixed states with domain consistency and
derives their full isotropy images before calling them primitive.
Its rational-root argument is an alternative valid proof that
lambda_n is an irrational quadratic unit: the monic integer
polynomial has constant term one and lambda_n>1.
The composite example lambda_4=19+6*sqrt(10) is exact.
Packet distinctness comes from full tails, not unequal numbers
or an assumed root-to-prime identification.

Section 5 has all three correct changed-source inverse domains,
IMAGE laws, fixed strata and source-isotropy distinctions.
Section 6 correctly stops only the direct prime-time target.
No full main periodic ledger, universal impossibility or naturalness
closure is claimed.

The sole suggested precision edit concerns Section 3's wording
"inverse branches arriving there" immediately after discussing seed
zero. The inverse is evaluated AT a zero-seed target and goes
TO the positive predecessor seed 1/j. I requested "inverse branches
evaluated at a zero-seed target" instead. J_I(0)=C/j^2
and the underlying mathematics were already correct; this was not
an ownership or theorem blocker. Root adopted exactly this wording.
Targeted readback confirmed the correction and the final hash above.
No other manuscript correction was requested.

## Checkpoint 3 — strongest adverse reading and scope

The substantive positive result is real: a genuine factor/digit
feedback source owns a nonconstant measured clock and explicit
primitive packets. Their algebraic-unit times could have interest
under another arithmetic question. None of that makes the present
direct log-prime target pass, because the actual fixed packets
already have noninteger exponentials and cannot be relabelled away.
Conversely, the mismatch does not disprove approximate statistics,
alternative models or future interpretations of quadratic units.

A second strong objection is that a.e. IMAGE data alone cannot
determine the clock at null recurrent points. That objection would
matter without an all-point rule, but this card freezes analytic
branch derivatives and endpoint composition before proof. The
manuscript checks their consistency; it does not claim the choice
is forced by arithmetic or arbitrary Borel measure data.

The controls demonstrate recurrence and time dependence for their
actual changed actions, not universal necessity of reciprocal/floor,
quotient feedback, measure or endpoint normalization.
Retiming, deleting unit/composite roots or selecting seeds would
change the owner. None is used to rescue the stopped candidate.

No critical or major mathematical correction was identified.
The sole minor precision request is resolved; no issue remains open.
The fixed-family theorem supports STOP / FORK at its exact scope,
with the full same-object ledger retained and naturalness OPEN.
T3, classical lifts and formal Route coordinates remain unassigned.
