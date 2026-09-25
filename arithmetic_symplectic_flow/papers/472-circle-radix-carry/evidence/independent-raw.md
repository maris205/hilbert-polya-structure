# CRC01 — independent card-only raw derivation

Candidate: `ANG-20260925-CRC01`, paper472, version1.
Batch: `SYMBOLIC-RETURN-20260925-Y`, round3/5; date2026-09-25.
Reviewer: `pcr01_independent_review`, separate from the current author.

## 0. Frozen inputs and scope

Scientific input is only the FULL-read102-line [candidate card](../candidate-card.md),
SHA256 `b7b36a6ad4028bc6fb5c50224dca33198400b99775438bd768fbc25194eafade`,
plus root's pre-proof confirmation that BOTH short gates apply separately
to ALL four owners M/G/C/R. The155-line [CP1 report](scope-review.md) has
SHA256 `8232787fe048fbc955fd6e8ef1ab9272b5d88f1827ebe093505a0fe74b1eca96`.
Root FULL-read CP1 before DISTINCT RAW RELEASE. Both hashes were rechecked
before writing. No current author paper/README/ledger, current helper/peer
answer, other card, or old proof was read for this derivation.

This is exact symbolic mathematics, not numerical evidence. Shared history
and earlier review exposure remain as disclosed in CP1: `NOT_CALIBRATED`,
not blind, human, cross-model, or external peer review. Only this raw file
is written. No scientific code, network, Git, PDF, or old-file edit is used.
The state height y and extension height h are distinct throughout.

## 1. Full carrier, actual source cells, and guards

Let X=T×[1,infinity), T=R/Z, with normalized Haar×Lebesgue measure mu.
Use xbar in[0,1). For integers n≥1 and0≤j<n define the half-open cell

    A_(n,j)={([x],y): n≤y<n+1, j/n≤xbar<(j+1)/n}.

These countably many disjoint Borel cells partition ALL X, including y=1,
integer heights, the seam x=0, and digit boundaries. On this cell put
d=gcd(n,j), with d=n when j=0. Always 1≤d≤n. Define P(n,j) as in the
card. M/C/R have source union of cells with P(n,j); G has every cell.
We now verify that the extra geometric guards remove none of these sources.

For M/G/R, output height is (y+j)/d≥n/d≥1. For C it is y+j≥1.
Thus every source passing its stated permission has output in X. In the
assigned oriented circle coordinate the fixed-cell forward affine germs are

    M/G: (xbar,y) -> (n xbar−j,(y+j)/d), determinant n/d;
    C:   (xbar,y) -> (n xbar−j,y+j),     determinant n;
    R:   (xbar,y) -> (xbar,(y+j)/d),     determinant 1/d.

All are positive and nonzero. These are FULL real2D determinants. The
affine extension on the assigned side also prescribes the germ at cuts,
the circle seam, and the lower height boundary. No derivative across a
discontinuity or unassigned null-point version is used. Hence the source
domains are exactly those stated above: G is total; M/C/R retain all
forbidden sources as terminal objects with units and their actual incoming.
No absorbing self-loop is added at a terminal.

At y=N and x=[a/N], with integers N≥2 and1<a<N, the representatives give
n=N and j=a, including the exact right-assigned digit face. The geometric
guards hold as just proved, and P is exactly a|N. The next height is an
actual transported continuous coordinate, not a passive stored integer.
This verifies the frozen interface without claiming intrinsic naturalness,
a classical lift, or a Logistic/Hénon conjugacy.

## 2. Complete Borel inverse atlases

For target ([xi],eta), use xibar in[0,1). For every n≥1,0≤j<n and
d=gcd(n,j), the actual inverse candidates and their exact domains are:

| Owner | Inverse candidate | Actual target domain, in addition to permission |
| --- | --- | --- |
| M/G | ([(xibar+j)/n],d eta−j) | (n+j)/d≤eta<(n+1+j)/d; every circle target |
| C | ([(xibar+j)/n],eta−j) | n+j≤eta<n+1+j; every circle target |
| R | ([xi],d eta−j) | j/n≤xibar<(j+1)/n and (n+j)/d≤eta<(n+1+j)/d |

Permission is P(n,j) for M/C/R and none for G. Every lower height endpoint
of these domains is at least1. The displayed domains are exactly the card's
reconstructed checks: source height lies in[n,n+1), its digit is j, and
its forward image is the given target. For M/G/C, xbar=(xibar+j)/n is
already in[j/n,(j+1)/n); no extra representative choice is hidden.
For R the digit check is instead a genuine constraint on the target circle.

All domains and images are Borel. In the Borel identification of T with
[0,1), they are explicit half-open rectangles and affine images of such
sets. A legal forward source has a unique actual(n,j), and solving its
two affine equations gives exactly the inverse in the table. Conversely
every passing candidate maps forward to the target. This proves both
directions of completeness without a bound on n or a selected branch.

Two different actual labels cannot count the same source: that source's
height floor and digit determine its unique label. This argument also
handles coinciding formal candidate formulas on special targets. Each
individual actual inverse is injective. No outgoing permission at the
TARGET is imposed; illegal objects can have many legal predecessors.
The inverse formulas act on the existing full X, not on extra label objects.

## 3. All-point IMAGE and the only permitted clocks

The prescribed inverse germ Jacobians, at EVERY actual inverse point, are

    J_M/G=d/n,       J_C=1/n,       J_R=d.

They are positive finite constants on the corresponding branch. Represent
the target circle by[0,1) and the appropriate source arc by its assigned
half-open interval. Affine substitution scales the circle coordinate by
1/n for M/G/C, and by1 for R; it scales height by d for M/G/R and by1
for C. Therefore for EVERY Borel B in the actual inverse domain,

    mu(theta(B))=integral_B J_theta dmu.

This is an exact Borel change-of-variables identity, including infinite
integrals. Cutting at the seam changes no measure and discards no object:
the seam is explicitly represented by0, and its prescribed J is the same
assigned affine germ value. The argument does not choose J only a.e.
Every integer-height and digit-face periodic point retains its stated J.

On each owner's actual source A_(n,j), the derived clocks are consequently

    kappa_M/G=log(n/d),    kappa_C=log n,    kappa_R=−log d.

M/G clocks are nonnegative and vanish exactly on j=0; C's vanishes exactly
on n=1; R's is nonpositive and vanishes exactly when d=1. No absolute-value
roof is substituted for these signed clocks. Terminals have no outgoing
kappa. The eventual least positive physical period will be obtained from
the ENTIRE isotropy clock subgroup, not from a chosen positive step.

## 4. Every history and exact full-object tests

For EACH owner U, let Pre_U(t) be all sources in section2 at target t.
Define

    I_U^0(t)={t},
    I_U^(m+1)(t)=union_(w in I_U^m(t)) Pre_U(w),  m≥0.

Induction gives v in I_U^m(t) iff v has m legal U steps and U^m v=t.
Indeed the last m steps start at Uv, and the complete one-step atlas
gives both directions of the induction. This works for every full-X target,
including terminals, and every depth, not just tested cores. Sets count
actual sources, not formal words with multiplicity. Coincidences across
different depths do not erase retained integer lags.

All infinite backward histories at t are EXACTLY sequences

    t_0=t,  t_(i+1) in Pre_U(t_i) for every i≥0.

This is the compatible inverse limit of the finite histories. Unrelated
nonempty levels do not by themselves prove existence of a compatible
infinite sequence. Every legal choice is retained; no preferred ancestor
or new boundary state is introduced. Forward histories are unique until
the first illegal source. A two-sided history additionally requires an
infinite legal forward continuation at its time0 object.

Let D_r be the legal r-step domain, with D_0=X. On a legal itinerary let
lambda_U be its actual forward determinant from section1 and set

    Lambda_0(v)=1,
    Lambda_r(v)=product_(i<r) lambda_U(U^i v),
    S_r(v)=log Lambda_r(v).

All domains and finite itinerary restrictions are Borel. The chain rule
gives inverse-history Jacobian 1/Lambda_r(v) at U^r v. Countably many
finite label itineraries cover all histories; the assigned affine germs
and any required Borel seam cuts prove every-Borel IMAGE at each depth.

Keep exactly the triples (v,r−s,w) with a legal meeting U^r v=U^s w.
Their source is w, range v. If another witness has the same lag, its depths
differ by a common shift. The added legal tail starts at the same meeting
point and contributes equally to both sums. Thus

    c(v,r−s,w)=S_r(v)−S_s(w)=log(Lambda_r(v)/Lambda_s(w))

descends to the actual triple. For composition, extend the two middle
histories to their larger depth, using the already legal middle segment.
The common middle sums cancel, proving additivity. Units have clock0;
inverse negates clock and lag. Forward(Uv,−1,v) has clock −kappa(v).
No forbidden terminal step or infinite tail was inserted in this proof.

An actual history-pair transport w→v is the v inverse history composed
with the w forward history on their actual common domain. Its absolute
Jacobian is Lambda_s(w)/Lambda_r(v)=exp(−c). Affine substitution, or its
finite composition on Borel seam pieces, proves EVERY-Borel pair IMAGE.
The same-triple descent proves independence of a later meeting witness.
It is not a new density or a sum of competing inverse densities.

The complete kernels, for each owner's own legal meetings, are

    K_lag:   r=s;
    K_clock: Lambda_r(v)=Lambda_s(w);
    K_joint: both conditions.

These equations describe full arrow sets, not just loops; duplicate
representations are identified as triples. The exact source-packet test
is existence of a legal r,s meeting. The exact extension-orbit test is

    (v,h_v) ~ (w,h_w)
    iff some legal r,s satisfy U^r v=U^s w and
         h_v−h_w=S_r(v)−S_s(w).

Sufficiency constructs the required arrow; necessity follows from the
arrow definition and composition. It is a full equivalence test with all
real heights, not only a one-step approximation or a chosen section.

## 5. Entire isotropy, phases, and all incoming packet types

For a deterministic partial U, a nonzero lag loop at v is equivalent to
eventual entry into a legal cycle. A witness U^r v=U^s v, r>s, produces
a repeated legal block; conversely a reached cycle can be repeated. If the
least source length is ell, all loop lags are exactly ell Z. Let C be the
clock sum over that least cycle. Cancellation of the incoming tail gives

    G_v^v=ell Z, c(v,k ell,v)=kC, ENTIRE H_v=CZ.

If no eventual cycle exists, source isotropy and H_v are trivial. Extension
isotropy is ell Z when C=0 and trivial when C≠0; a nonperiodic/terminal
packet also has trivial extension isotropy. A zero-clock loop is not a
positive period. If C≠0, the least positive generator is |C| and ALL positive
repeats are m|C|, m≥1. No smaller clock is licensed by intermediate phases
or by dividing C by ell. No rationality premise is needed.

For an eventual cycle choose a core point b, solely as phase reference.
The ENTIRE packet is union_(a≥0) I_U^a(b). Let d_v be the first arrival
at b and a_v=S_(d_v)(v). Every core phase reaches b, so none is removed.
All arrows within this packet are precisely

    (v,d_v−d_w+k ell,w), clock a_v−a_w+kC,  k in Z.

Any meeting can be extended to b; conversely arbitrary integer k is
realized by padding both arrivals with sufficiently many cycle repeats.
The full kernel tests are, respectively,

    d_v−d_w+k ell=0;   a_v−a_w+kC=0;   both.

Entire phase is [h−a_v] in R/CZ, using R when C=0. This verifies the
card's entry-phase orientation. Translation on this orbit SET has exactly
stabilizer H_v. Different source packets are not merged by equal C values,
and incoming branches or phase origins are not counted as new core packets.

If a packet terminates at e, each member has a unique arrival depth d_v
and clock a_v to e. Its arrows have lag d_v−d_w and clock a_v−a_w;
kernels impose equality of depth, clock, or both. H=0 and phase is real
h−a_v. The endpoint has depth0, with all actual predecessors retained.

For a forward-infinite non-eventually-periodic packet choose reference b.
There is a unique arrow lag k_v from b to v, since two different lags would
give nonzero isotropy at b. Let a_v be its clock. All arrows have lag
k_v−k_w and clock a_v−a_w; kernels are equality of these respective
labels, and real phase is h−a_v. No global measurable selector is asserted.
These terminal, nonperiodic infinite, and eventually cyclic cases exhaust
the full source packets. Section4 supplies all their incoming histories.
This is an exact unrestricted description, not a census of higher cycles.

## 6. ALL fixed states in W, separately for all four owners

W=T×[1,5) consists of the entire n=1,2,3,4 cells. On n=1 the only digit
is j=0,d=1. Every owner is the identity there. Thus the full band

    B_0=T×[1,2)

is an actual fixed set, including y=1 and every circle point. Its source
fixed loops are real map loops, not terminal units promoted to loops.

For normalized height transport in M/G/R, fixedness requires

    (d−1)y=j.

When n≥2,j=0 gives d=n and is impossible since y>0. When j≥1,d=1,
the equation is again impossible. When j≥1,d≥2 it would give
y=j/(d−1)≤n−1<n, contrary to floor y=n. This exhausts all digits and
cuts in n=2,3,4 without a circle-coordinate assumption. Therefore

    Fix_W(M)=Fix_W(G)=Fix_W(R)=B_0.

For C, height fixedness forces j=0. On n≥2 the actual source circle lies
in[0,1/n), so n xbar is the target representative in[0,1). Circle fixedness
then forces n xbar=xbar, hence x=0. Conversely every such point is legal
and fixed. Consequently

    Fix_W(C)=B_0 union union_(n=2,3,4) ({[0]}×[n,n+1)).

All left height endpoints are included and y=5 is excluded by W. No
additional representative at x=1 duplicates x=0. No other fixed points
inside W are omitted. This is the frozen W gate, not a requested extension
of the fixed classification to other height cells.

## 7. Complete incoming and clocks for EVERY found fixed core

For each individual b in B_0 and EACH owner U, define

    B_U(b)=union_(m≥0) I_U^m(b).

This is its entire full-X incoming source packet, with all depths and all
compatible infinite histories from section4. No restriction to W or the
same source cell is imposed. The constant backward core sequence exists;
all other compatible choices are retained by the same recursion.
Two different fixed b,b' give disjoint packets: a common future would
have to be both constant b and constant b'. Hence no member of the
continuous fixed band is selected as a representative for all the rest.

Each such core has ell=1 and C=0 in every owner. At EVERY ancestor,
source isotropy is Z, ENTIRE H=0, and extension isotropy is Z. For least
entry d_v and arrival clock a_v, every integer k gives an arrow

    (v,d_v−d_w+k,w), clock a_v−a_w.

Lag kernel has k=d_w−d_v; clock kernel has a_v=a_w with ALL k; joint
imposes both. Every real phase h−a_v remains, with no positive primitive
or positive repetition ledger. Incoming clocks need not be zero merely
because the core is zero-clock. The uniform recursion computes them from
the actual branch products, without an a.e. or sign simplification.

For C also treat EVERY b=([0],t), t in[n,n+1), n=2,3,4, separately.
Its full packet is B_C(b) by the same unrestricted definition; the first
arrival labels determine every clock and kernel as in section5. Here

    ell=1, C=log n, source isotropy=Z,
    ENTIRE H=(log n)Z, extension isotropy={0},
    phase [h−a_v] modulo(log n)Z,
    positive primitive log n, all repeats m log n.

These are distinct full packets for distinct fixed points, not different
phases of one packet. Thus each n=2 or3 already supplies a continuous
family of equal-prime-time control packets, violating uniqueness in that
control; n=4 additionally gives a nonprime primitive log4. Log4 cannot be
relabelled as the second repetition of an unproved log2 primitive at this
same core: its entire H is (log4)Z. These are C findings, not MAIN findings.

## 8. ALL points of the specified two-step word: M and G

Start in digit(n,j)=(3,1). Then y in[3,4), xbar in[1/3,2/3), d=1,
and the first M/G image is

    x_1=3xbar−1, y_1=y+1.

The target height automatically lies in[4,5). Digit(4,2) requires
x_1 in[1/2,3/4), equivalently xbar in[1/2,7/12). At that cell d=2,
and the second image has representatives

    x_2=4x_1−2=12xbar−6,  y_2=(y+3)/2.

Both xbar and x_2 lie in[0,1), so circle equality is actual equality of
these representatives; no additional modular root can be inserted.
Two-step periodicity forces 11xbar=6 and y=3. These satisfy all half-open
constraints, including the exact integer height faces. Thus the ONLY
starting point with this ORDERED source word, in either M or G, is

    v_0=([6/11],3),  v_1=([7/11],4),  Uv_0=v_1, Uv_1=v_0.

Both permissions hold, since1 divides3 and2 divides4. The guards were
already proved at all points. This is a least-two cycle because heights
3 and4 differ. v_1 is its other core phase, not a second core packet or a
second starting solution in the prescribed(3,1) cell. The source word
and equality equations exhaust every coordinate solution, not a search.

The two ORIGINAL-measure step clocks are log3 and log2. Hence the entire
least-cycle clock is C=log6, not either individual step clock and not C/2.
The generic entire-isotropy proof gives H=(log6)Z and positive primitive
log6. This is nonprime since6=2×3. It is an actual MAIN-owned obstruction
on retained integer-height faces; no control result is being transferred.

## 9. ALL points of the specified word: C and R

For C, the first step on(3,1) has x_1=3xbar−1 and y_1=y+1. Its(4,2)
step then gives height y_2=y+3, so it cannot return to y. In fact the
return height is outside the initial n=3 cell. Thus C has NO two-step
periodic point with the specified word, for any circle coordinate or cut.
Solving only a circle equation would not give an actual C periodic point.

For R the circle coordinate is unchanged. The first digit constraint is
xbar in[1/3,2/3); after height y+1 the(4,2) constraint is
xbar in[1/2,3/4). Their intersection is exactly[1/2,2/3). The second
height is again (y+3)/2, so returning height forces y=3. Therefore ALL
starting points with the prescribed ordered R word form the family

    v_0(t)=([t],3), v_1(t)=([t],4),  1/2≤t<2/3.

Every member is legal and has least source length2. t=1/2 is included
by the right digit assignment at n=4; t=2/3 is excluded because its
initial n=3 digit would be2. Both integer height boundaries are included.
There is no remaining circle equation, because R's circle map is identity.

The R step clocks are0 and−log2, hence C=−log2, ENTIRE H=(log2)Z,
positive primitive log2. The clock-zero first edge remains a genuine
nonzero-lag arrow, not a zero-clock cycle. Distinct t give distinct cycles
and full source packets; in particular R preserves x on every legal step.
This is a continuous family of duplicate prime-time control packets.
Its log2 must not replace MAIN's log6 or rescue MAIN admission.

## 10. ENTIRE incoming, kernels, and phases of the found two-cycles

For each found cycle and its OWN owner U, choose its displayed v_0=b.
Use B_U(gamma)=union_(a≥0) I_U^a(b). This includes v_1, every source
that eventually enters either core phase, all outside-W ancestors, and
every compatible infinite backward sequence. It excludes no source based
on its digit, coordinate sign convention, or nonrecurrent status. For M/G,
their basins use their DIFFERENT permissions; they are not equated merely
because the two core formulas coincide. For R each family member uses its
own b and the R inverse formula, not an M/G inverse tree.

For v in this full packet let d_v be the first arrival at b and
a_v=S_(d_v)(v). All arrows are precisely

    (v,d_v−d_w+2k,w), clock a_v−a_w+kC, k in Z,

with C=log6 for M/G and C=−log2 for each R family member. All entry
depths, both core phases, and arbitrary repeated traversals are present.
The three full kernel conditions are

    lag:   d_v−d_w+2k=0;
    clock: a_v−a_w+kC=0;
    joint: both.

Source isotropy at every ancestor is2Z. Its ENTIRE clock image is CZ;
extension isotropy is trivial because C≠0. The complete phase is
[h−a_v] modulo CZ. Every real phase is retained, physical translation has
least positive period |C|, and repetitions are all positive multiples.
Parity restrictions on lag0 and all possible clock cancellations are kept
by the displayed equations rather than replaced by a genericity claim.

For M there is one tested two-cycle packet, with primitive log6; G has
its own one tested packet with that period. For R there is one packet for
EVERY t in[1/2,2/3), each with primitive log2. These counts refer to the
tested cores, not a claim that no other full-X cycles exist. Histories,
incoming branches, rotated starting words, and phase coordinates are not
additional primitive packets. Distinct actual cores are never merged merely
because their primitive values coincide.

All other objects of every owner, including every terminal and every
unclassified forward-infinite packet, remain covered by sections2–5's
complete recursion, meeting test, kernel equations, isotropy classification,
and all-height phase test. Nothing is silently reduced to the displayed
fixed sets or two-cycle basins.

## 11. Gate outcome and limits

Both frozen gates have been completed separately for ALL four owners.
All four have the zero-clock fixed band B_0 in W; C additionally has its
entire three seam-height fixed families. M/G have the unique ordered-word
starting point and its least-two core; C has none; R has the full interval
family. Every found core has its whole full-X incoming and phase description.

MAIN owns the primitive log6 through its ENTIRE H=(log6)Z. This violates
the ordinary-prime primitive requirement, regardless of all other packets.
The required decision is STOP/FORK for CRC01, not BOUNDED OPEN on the
target and not an obstruction borrowed from a control. Permission retains
both bad-cycle digits and therefore fails to remove this recurrence.

The control comparison remains owner-specific: G retains the same bad
core without permission; C changes the height dynamics, removes that
two-step recurrence, but has its own positive fixed-family failures;
R changes the circle dynamics and produces duplicate log2 packets. None
of these changes is a permissible clock or formula repair of MAIN.
No additional period/cell search, altered measure, new parameter, or
new candidate is initiated. Other cycle classifications are not claimed.

Original-measure ownership and the stated history laws are proved locally.
Arithmetic T1 is NOT PASSED; T2 here is the exact packet/repetition law and
the bounded negative admission certificate. T3 is NOT AUDITED. Classical
fields are NOT APPLICABLE, formal coordinates UNASSIGNED, Route B NOT
INVOKED. No operator, trace, dynamical determinant, or RH result follows.
Strong naturalness and PROVES_TOO_MUCH remain distinct unproved obligations;
the selected word was outcome-unsealed as the card discloses.

After FULL self-read this card-only raw must freeze, with path/line/hash
receipt only and HOLD until DISTINCT PAPER UNLOCK. No current author
comparison or CP2/CP3 verdict appears here. No work on475 is authorized.
