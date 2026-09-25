# Independent internal review — quotient/remainder reciprocal flow

Candidate ID: ANG-20260920-QRF01.
Paper ID: 299-quotient-remainder-reciprocal-flow. Date: 2026-09-20.
Status: OWNED RECIPROCAL IMAGE CLOCK; UNIT PACKET AND WRONG PRIME TIMES — STOP / FORK.

## 1. Bindings, actual access order and review scope

The entire original 154-line card was read and hash-verified before
any manuscript access. Original frozen SHA-256:

    30b59f86e36d599376d6c96cc0969eadedc4ec3c695bed60a74c2007d5b49577

This binds the frozen bytes, not any later administrative appendix.
Complete raw ownership, density/version, fixed-point and control findings
were sent before opening the manuscript. The subsequent full paper read
covered 330 lines, with verified SHA-256:

    e247008a12ab104e6302aa42e0979eef82510bd4a4f215151e1d23af93eb62c4

ARS's three checkpoints were raw-card derivation, manuscript comparison
and final adverse review. The native auxiliary atomic_clock_scope checked
only FACTOR-OFF and QUOTIENT-READOUT from the raw card, including their
endpoint versions. It received no reviewer conclusions or manuscript.
Its control results were checked against the reviewer's local derivations
before manuscript access. Main-source owner, density and fixed points
were derived separately by the reviewer.

This is inherited same-model/shared-context internal review, not external
peer review, formal verification or independent-error evidence. The
card's admitted definition-stage endpoint/fixed-point considerations are
not recast as blind ideation. Older comparison and provenance files were
not independently reread or used as theorem inputs in this audit.
No auxiliary files, scientific runs or external lookups were produced.
Only this report was written, with no other main-return classification.

## 2. Checkpoint 1 — complete partial Borel owner

The arithmetic readout is the greatest prime divisor for q>=2,
derived from divisibility atoms and existence of a minimal nontrivial
divisor. Thus h_q=0 exactly for q=0,1 or prime q. At a composite
q, writing q=d(q)*k with k>=2 gives h_q=d(q)(k-1)>=2.
This proves nonnegativity, the absence of h_q=1 and the exact terminal
set stated in the manuscript. Terminal objects retain their identity.

The floor inequalities give precisely the frozen B_(q,k), with strict
left and retained right endpoints. Solving the reciprocal gives the
strict inverse r=d(q)+1/w-q on exactly E_(q,k); no image endpoint
or singleton restriction is completed by adding arrows.
The value 1 has no preimage, so the map is not onto.
These branch images already describe all arrows needed for the audit.

The value coordinate is a Borel bijection with [0,infinity), carrying
counting–Lebesgue measure to Lebesgue measure. It is not claimed to
be a homeomorphism across integer cells. The measure is sigma-finite,
nonatomic and full-support in the stated product topology.

Finite partial-iterate domains are Borel. Defined equal-iterate sets
with retained lag form a Borel subset of X x Z x X. Countably
many injective branches imply countable finite-iterate fibres and
countable groupoid source/range fibres. Actual finite branch pairs
cover the relation without introducing other fractional-linear maps.

Partial composition is legitimate: aligning the middle counts to their
maximum uses the longer already-defined middle itinerary. Equality of
the shorter terminal states propagates its required extra steps to the
other endpoint. No illegal iteration past a terminal or onto hypothesis
is used. The triple groupoid laws and their structure maps are Borel.

## 3. Checkpoint 1 — IMAGE density and all-point version

Ordinary change of variable on an actual inverse branch gives

    J_theta(w)=1/w^2,
    a(q,r)=1/[q+r-d(q)]^2 for the forward branch.

The second expression is evaluated only at nonterminal points.
For A_m the product of forward derivatives along a DEFINED m-step
itinerary, A_0=1, the branch pair from y to x has

    J(x,m-k,y)=A_k(y)/A_m(x),
    c(x,m-k,y)=log A_m(x)-log A_k(y).

The IMAGE identity holds on every Borel subset of each actual domain.
The pointwise formula additionally uses the explicitly frozen analytic
completion. Deterministic one-step branches specify its endpoint factors;
common extension of equal-lag presentations cancels equal added factors.
Middle-count alignment proves multiplicativity and additivity, including
at null restrictions. J is positive and finite; c is finite but need
not be positive.

For example (4,0)->(0,1/2) has forward derivative 1/4.
The corresponding inverse density at value 1/2 is 4, with clock
-log 4, not +log 4. The inverse image interval (1/3,1/2] has
a one-sided analytic limit there. No absolute-value clock is substituted.

A.e. IMAGE data cannot determine a derivative on an isolated null chart.
FACTOR-OFF's singleton at (1,0) is the essential control: its value
J=1 comes from the frozen analytic reciprocal completion, not from
the vacuous zero-measure IMAGE identity. Main fixed points, in contrast,
lie inside positive-measure source/target branch intervals, where
continuous density and full support determine their null-point values.
No unrestricted uniqueness claim for all null restrictions is made.

The cocycle extension and all its structure maps are Borel. Real
translation on the added coordinate commutes with the arrows, is jointly
Borel and exists for every positive or negative time. The derived step
(x,s)->(Tx,s-log a(x)) has the same retained-lag extension.
Only the full orbit SET action is asserted, not a standard Borel or
Hausdorff coarse quotient, continuous topological flow or positive roof.

## 4. Checkpoint 1 — all fixed points and entire isotropy

The fixed equation in the value v=q+r is v(v-d(q))=1.
For d>=1 its unique positive solution alpha_d is strictly between
d and d+1. At q=0 the solution v=1 is outside that cell.
Thus q must equal d(q)>=1: precisely q=1 or a prime.
These are all fixed points, with no fixed integer endpoint.

At each x_q=(q,alpha_q-q), every source lag in Z occurs and
a(x_q)=alpha_q^2. Consequently

    H_(x_q)=(2 log alpha_q)Z,
    alpha_q=(q+sqrt(q^2+4))/2.

This is the full time group, not a selected loop. Its least positive
element is 2 log alpha_q and its fixed-object extension isotropy is
trivial. Distinct fixed cores cannot acquire a common forward tail
through finite preimages, so they give different packets. Real phases
do not create additional copies of one core.

The unit q=1 already supplies an unwanted primitive. Prime q=p
has time strictly larger than 2 log p, not log p. The manuscript's
stronger displayed-family claim also checks: a rational root of the
monic polynomial z^2-qz-1 would be integral, whereas alpha_q is
strictly between consecutive integers. Since alpha_q^2=q alpha_q+1,
its square is irrational too. None of these fixed-core times is log N
for an integer N. No absence theorem for OTHER main returns is inferred.

## 5. Checkpoint 2 — complete manuscript and controls

The full manuscript agrees with the raw findings. FACTOR-OFF is the
complete reciprocal involution on positive values, with only 0 terminal.
Its forward two-step derivative is v^(-2)*(1/v)^(-2)=1.
All isotropy clocks vanish. Source and extension isotropy are Z at
v=1, 2Z at other v>0, and trivial at v=0; every H is {0}.
Thus discrete cycles do not give positive cyclic-time packets.

QUOTIENT-READOUT has u=r, all integer endpoints terminal, its own
inverse density 1/w^2 and forward derivative 1/r^2. Its fixed
points are the same formula x_q for EVERY integer q>=1.
Each has H=(2 log alpha_q)Z and a distinct packet. Only its fixed
points, not higher or eventual returns, are classified. At (1,0)
this control is terminal, unlike FACTOR-OFF's zero-clock fixed point.

The manuscript additionally follows the designated main endpoint
(4,0)->(0,1/2)->(2,0), then termination. The forward derivatives
1/4 and 4 have product one. This is a finite path, not a periodic
return. A terminal or a state reaching one cannot have nonzero
retained-lag isotropy, since an unequal-iterate equality would create
a repeatable cycle. This bounded endpoint check does not classify
other main returns. No manuscript correction was requested.

## 6. Checkpoint 3 — strongest counterarguments and verdict

The strongest version objection concerns arbitrary null endpoint values.
It is valid as a general warning, but does not defeat this frozen
construction: the analytic completion is explicit and composition
consistent, while the decisive main fixed points are branch interiors.
Deleting the singleton control or claiming a.e. uniqueness everywhere
would instead conceal the real boundary.

The unit packet cannot be discarded, and different fixed cores cannot
be merged by matching lengths or factor labels. Even deleting the unit
would leave the proved wrong prime-core times. The owned measured
construction is therefore valid but fails the target without any
need for further orbit searches or analytic rescue.

**Verdict: no outstanding blocking issue or requested correction.**
STOP / FORK at the fixed-point gate. Other main returns and coarse
structure remain unclassified; stronger naturalness stays OPEN.
No universal no-go, T3/operator/quantum result or classical lift is
asserted. Formal Route coordinates are unassigned; Route B is not
invoked. Earlier packages and paused 241/242 remain unchanged.
