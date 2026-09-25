# PCS01 — frozen-card independent raw derivation

Candidate: ANG-AUDIT-20260925-PCS01. Paper477, Batch Z round3/5.
Reviewer: `/root/rcr01_independent_review`, 2026-09-25 UTC.
Stage: DISTINCT RAW RELEASE after root FULL-read CP1; manuscript LOCKED.
Same-model/shared-history NOT_CALIBRATED; not blind, human or external review.

## 0. Inputs, method and non-exposure

Sole new scientific input: `candidate-card.md`, FULL1–107/EOF, SHA-256
`268785812acefa8584806e1969a4b7781fb0d1b3bac353febba3aca8ead671ba`.
Own CP1 has163 lines, SHA-256
`14e5432fe7a0555e18466b8c83c01bd69fad4fcc4fb95db12554a09202e6c01a`.
No author paper/README/ledger, current helper/peer result, old proof or
additional scientific file was read. Earlier shared history and the
previously disclosed468 summary exposure remain inherited, not erased.
The card's scout/helper disclosures remain disclosures, not sources reopened.

ARS router was personally refreshed FULL1–488/EOF, with a smaller reread
of1–179 and180–265 repairing a truncated combined output. Deep workflow
was refreshed1–305,306–602/EOF; runtime1–113/EOF; DA1–192/EOF;
fallacies1–192/EOF; anti-leakage1–83/EOF. Local instructions and applicable
plan ranges were personally read in CP1 and retained. This is a bounded
original-proof adaptation, not a literature review or full writing-protocol
activation. No numeric scores, forced issue quota, external citations,
scientific code/numerics, network, Git, PDF, other writes or Paper480.

All assertions below are derived analytically from the frozen hypotheses.
Elementary finite-dimensional change of variables and Lebesgue regularity
are used explicitly; no invariant probability or regular quotient is added.

## 1. Actual label dynamics and the complete inverse skeleton

Write s=(n,d). The source transition is exactly the card's three-case a.
For a target label (m,e), its COMPLETE predecessor-label set is:

- If3<=e<=m: {(m,e-1)} when e-1 does not divide m, and empty otherwise.
- If e=2: {(m,m)} together with {(jm,m):j>=2}.

Indeed an advance preserves n and increases d by one, a lowering has new
label(d,2) with d a proper divisor of old n, and a restart has label(n,2).
These exhaust the three forward cases and are mutually distinct sources.
The empty case is a lack of incoming, not an illegal outgoing source.

For a class member, partition each D_s into the supplied countable Borel
pieces U_{s,b}, on which f_s is injective, with inverse v_{s,b} on its
actual image V_{s,b}. At target((m,e),y), take precisely the preceding
old labels s and all b for which y belongs to V_{s,b}; output(s,v_{s,b}(y)).
Repeated representations of the same source are not extra predecessors.
The selected partition/chart prescription supplies its actual positive
finite J_{s,b}(y); a branch count is never multiplied into that J.
No condition on the target's outgoing legality is imposed.

For every Borel A subset of that exact target chart, the hypothesis is

    mu(v_{s,b}(A)) = integral_A J_{s,b}(y) dmu(y).

The notation includes the source/target labels. This is an image formula
for an individual inverse, not the pushforward density of a many-to-one F.
Labels and branches together are countable, even where infinitely many
old labels enter one target. The predecessor enumeration is exact and
untruncated at every real fibre value, including prescribed boundaries.

The label's first coordinate never increases and strictly decreases at
each lowering. If an orbit ceased lowering at a composite n, its eventual
full scan beginning at2 would meet a proper divisor and lower again.
Thus every label reaches a prime p and then traverses precisely

    C_p=((p,2),(p,3),...,(p,p)),   L_p=p-1.

Conversely these are cycles because no proper divisor is encountered.
No cycle at composite n or any other label cycle exists. This proof uses
the actual divisibility transition, not a prime predicate supplied to F.
Late starting phases can choose different eventual primes; one must not
replace the resulting p(s) by the least prime factor of the initial n.

Let p(s) be the actual eventual prime, t_s the LEAST nonnegative time
with a^{t_s}s=(p(s),2), and R_s the number of restart steps d=n before
that arrival. These are finite current-orbit quantities. For a core label
(p,2+j), 0<=j<L_p, t_s=0,R_s=0 if j=0, and t_s=L_p-j,R_s=1 if j>0.
For arbitrary r>=0 let R_r(s) count restarts in the first r steps.
No finite cutoff enters any of these definitions.

## 2. Borel histories, original-measure IMAGE and pointwise descent

Set D_0=X, D_{r+1}={z in D_r:F^r z lies in D_1}; F^r is used only on D_r.
The branch partition makes F Borel on the Borel legal domain D_1.
Induction makes every D_r and F^r Borel. Each finite branch itinerary
gives a Borel piece on which F^r is injective with its composed inverse;
there are countably many such itineraries for each r.
Their images and inverses are Borel: locally a C1 diffeomorphism is a
homeomorphism, whose Borel restrictions have Borel images, and the
countable local charts and finite compositions preserve that property.

Define the prescribed pointwise quantities, with S_0=0,

    kappa(z)=-log J_actual(Fz),
    S_r(z)=sum_{i=0}^{r-1} kappa(F^i z)  on D_r.

They are finite real Borel functions on their domains. Composition of
the supplied inverse IMAGE formulas gives, on any itinerary inverse v_r,

    mu(v_r(A)) = integral_A exp(-S_r(v_r(u))) dmu(u).       (2.1)

This holds for EVERY Borel A in the actual target image. It follows by
successively applying change of variables; the product of the prescribed
inverse determinants is exactly exp(-S_r). There is no a.e. replacement
of the pointwise version, nor an assumption that F globally preserves mu.

Define G as the actual triples (z,k,w) for which some legal r,s>=0 satisfy
k=r-s and F^r z=F^s w. Source is w and range is z. Equal triples only are
identified, so distinct integer lags remain distinct arrows.
For a representative set c=S_r(z)-S_s(w).

If a second representative has the same lag, r'-r=s'-s=t. For t>=0,
both longer histories legally continue from the same common endpoint,
so S_{r'}(z)=S_r(z)+S_t(F^r z), with the same additional sum on w.
They cancel. For t<0 reverse the comparison. Hence c descends POINTWISE.
For composable arrows, align the two middle-object histories by extending
the shorter one along the longer supplied legal history. The matching
middle sums cancel, proving additivity. Such extension is justified by
the longer legal witness; no terminal is padded beyond its legal end.
Units have c=0, inverses negate c, and

    c(Fz,-1,z)=-kappa(z).                                (2.2)

A history-pair chart, from source w to range z, is
phi=(F^r|U)^{-1} composed with (F^s|V), restricted to the actual
common-image intersection. Apply (2.1) and the reciprocal forward
change of variables. For EVERY Borel A in this exact source chart,

    mu(phi(A)) = integral_A exp(-c(phi(w),r-s,w)) dmu(w).  (2.3)

All boundaries remain assigned by the original prescribed branches.
If charts represent the same triple, pointwise descent gives the same c.
Countably many history-pair charts cover all arrows. Thus G is Borel:
equivalently, for each integer k it is the countable union of the Borel
equalizer relations for legal r,s with r-s=k.

Every point has countably many immediate predecessors. Define exactly

    Pre_0(v)={v},
    Pre_{r+1}(v)=union_{u in Pre_r(v)} Pre_1(u).

At each step use §1, with its actual fibre inverse domains. This gives ALL
legal r-step incoming sources, including incoming to an illegal target.
The full source packet is exactly

    O(w)=union_{s>=0:w in D_s} union_{r>=0} Pre_r(F^s w). (2.4)

Each set here is countable, so O(w) is countable. All its arrows are kept
by recording the corresponding integer r-s and the sum difference, then
identifying equal triples. Formula(2.4) is not a finite-depth sample.

Inverse IMAGE makes every inverse branch send a mu-null Borel set to a
null set; the countable union proves that every legal F^{-r} does so.
Forward branches also preserve null sets: mu(A)=integral_{F(A)}J=0
and J>0 everywhere imply mu(F(A))=0. Neither fact asserts invariance.

## 3. All component types, kernels, entire H and real phases

A finite maximal forward history ends at an illegal object. It has no
nonzero isotropy. An infinite history which is not eventually periodic
also has no nonzero isotropy: F^r z=F^s z with r>s would exhibit a
periodic tail. Conversely, an eventual cycle of least SOURCE period q
gives precisely isotropy lags qZ at each object of the full packet.
To see completeness, compare sufficiently late witnesses on the cycle;
their length difference must be a multiple of its least period.

Let C be the actual sum of kappa over that primitive source cycle.
C is unchanged by cyclic rotation; telescoping the common initial
history shows that for every packet object

    Iso_G(z)={(z,mq,z):m in Z},  c(z,mq,z)=mC,
    H_z=c(Iso_G(z))=C Z.                                 (3.1)

This is the ENTIRE image, not a preferred subgroup or selected repetition.
Positive lag mq has clock mC; following the forward cycle m times has
lag -mq and clock -mC. For non-eventual or terminal packets both the
isotropy lag group and H are {0}. A periodic fibre can have least period
larger than its label period; q must not be replaced by p-1 in this class.

More explicitly, a source cycle must lie over C_p. The actual partial
L_p-step return g_p at(p,2), on its legal return domain, determines all
cycles: a least m-period point of g_p gives a least q=mL_p source cycle,
including its intermediate scan phases. A member's finite histories may
end before reaching a prime label. An infinite legal history eventually
runs on C_p, and is eventual periodic exactly when its actual g_p orbit
is eventually periodic. Otherwise it is non-eventual. These are exact
tests in the specified fibre law, not a promise of roots for arbitrary g_p.

For a full-arrow description, fix an object b in a packet and choose
one ACTUAL arrow A_z=(z,l_z,b) to each z, with beta_z=c(A_z).
For a terminal component one may choose its terminal b and take
l_z=the legal time to b, beta_z=the corresponding sum. For a non-eventual
component use any actual histories to b; their lag and clock are unique.
For an eventual component choices can differ by(mq,mC), as in(3.1).
Every arrow from w to z is exactly

    (lag,clock)=(l_z-l_w+m q, beta_z-beta_w+m C)           (3.2)

in an eventual packet, m ranging through ALL integers. In the other
two component types there is just the pair(l_z-l_w,beta_z-beta_w).
Proof: A_z^{-1} g A_w is isotropy at b, and this construction is reversible.
It neither merges distinct lags nor identifies different source packets.

Thus the full lag kernel imposes l_z-l_w+mq=0, the full clock kernel
imposes beta_z-beta_w+mC=0, and the joint kernel imposes BOTH on the
same integer m. In non-eventual/terminal packets omit m terms.
These are exact endpoint conditions, not merely an isotropy calculation.
Lag-kernel isotropy is always trivial; clock-kernel isotropy is qZ if
C=0 and trivial otherwise; joint-kernel isotropy is always trivial.

The height extension retains every(z,h) in X times R, with arrow
(w,h)->(z,h+c). Its source isotropy at(z,h) consists precisely of source
isotropy arrows whose clock vanishes: qZ for C=0, trivial for C!=0,
and trivial for non-eventual/terminal packets. No quotient regularity is
asserted. Exact all-real orbit tests are:

    same source packet, and
    h_z-beta_z == h_w-beta_w modulo H.                   (3.3)

For H={0} this means equality of real numbers. Consequently the complete
height-translation stabilizer of an extension orbit is EXACTLY H, and
extension orbits over a fixed packet are the SET of real cosets R/H.
The general terminal/non-eventual/every-periodic phase tests and all
repetitions follow from(3.1)–(3.3), without deleting any null object.

## 4. Question1: the nonzero-return-clock saturation is null

For q>=1 define Fix_q={z in D_q:F^q z=z}. Its Borelness follows from
the Borel diagonal and F^q. Then

    P_q=Fix_q minus union_{1<=j<q} Fix_j

is Borel and is precisely the least-source-period-q set. S_q is Borel,
so P_q^x={z in P_q:S_q(z)!=0} and all legal predecessor sets are Borel.
In particular E^x in the card is a countable union of Borel sets.

Partition P_q by the countably many legal q-step branch itineraries.
On one such Borel piece B, F^q is the identity. Its itinerary inverse
is therefore the identity on B as an ACTUAL point map, even though its
chosen ambient derivative need not be the identity at every point of B.
For every Borel A subset B, formula(2.1) becomes

    mu(A)=integral_A exp(-S_q(z)) dmu(z).                 (4.1)

X is sigma-finite, with bounded boxes in each countably many label fibres.
On a finite-measure box, if exp(-S_q)>=1+epsilon on a positive-measure
subset, (4.1) is impossible on that subset. The same applies to
exp(-S_q)<=1-epsilon. Taking countably many rational epsilon and boxes
proves exp(-S_q)=1 a.e. on B. Taking all itinerary pieces gives

    mu(P_q^x)=0, for every q>=1.                         (4.2)

This does not differentiate an identity on a non-open set, subtract two
infinities, assume an invariant measure, or change a boundary derivative.
Countable inverse nonsingularity proved in §2 then yields

    mu(E^x)=0.                                         (4.3)

The union includes r=0 and EVERY predecessor depth and label. By §3,
pointwise E^x is exactly the set of objects whose eventual primitive
cycle has C!=0, equivalently {z:H_z!={0}}. Any object in that packet
eventually reaches its same cycle, and cyclic sums agree. Thus no part
of a nonzero-clock periodic packet is lost from the definition of E^x.

This is a restriction on original-measure support of NONZERO PERIODIC
return clocks. It is not a claim that kappa or the clock of every arrow
vanishes a.e., nor that every pointwise periodic return clock is zero.

## 5. Question2: positive P_q gives continuum many zero-H packets

Suppose mu(P_q)>0, finite or infinite. By(4.2), the Borel subset
P_q^0={z in P_q:S_q(z)=0} still has positive measure. Some bounded box
in some single label fibre meets it in a positive finite-measure Borel
set: otherwise their countable union would be null. No normalization of
mu, invariance, or finite total measure is required.

Here is the needed cardinality argument, beyond nonatomicity alone.
A positive finite-Lebesgue-measure Borel subset of R^k contains a compact
positive-measure subset by regularity. Within any positive-measure
compact set choose two disjoint positive-measure compact subsets of
arbitrarily small diameter: sufficiently small grid boxes have volume
less than half its measure, hence at least two cells meet it positively;
inner regularity supplies compact subsets within two disjoint cells.
Repeat inside each chosen subset, with diameters tending to zero.
Each infinite binary sequence has a unique nested-intersection point,
and two distinct sequences give distinct points. Therefore the original
Borel set has at least continuum many points; at most continuum follows
from its embedding in R^k. In particular |P_q^0|=continuum.

Any full source packet meeting P_q has EXACTLY q points in P_q:
two periodic points with a common future belong to the same cycle;
all q cyclic points are present, and no preperiodic extra point is in P_q.
For a packet meeting P_q^0 they all have zero return sum, and (3.1)
shows that the ENTIRE isotropy-clock group is {0} throughout the packet.
Partitioning continuum many points into these q-element intersections
therefore gives continuum many distinct full packets with H={0}.
There cannot be more, since X itself has cardinality continuum.

The packet relation is Borel by §2, and each full packet is countable by
(2.4); it is not secretly a positive-measure uncountable orbit. If a
representative is desired only for this cardinality proof, order the
standard Borel X by a fixed label ordering followed by lexicographic
fibre ordering and choose the least of the q cyclic points. Comparisons
with its finitely many Borel iterates give a Borel transversal of P_q^0.
No global smoothness or topological quotient is needed.

Answer: exactly continuum many H={0} full packets already MEET P_q^0.
This is a periodic multiplicity conclusion, stronger than merely showing
that countably many countable packets cannot support positive measure.
It does not identify those packets with one another.

## 6. Control-owned inverses, original IMAGE and forward sums

All three controls have total fibre domain, so D_r=X for every r; there
are no illegal terminal objects. At target((m,e),y), e>=3, the inverse
is((m,e-1),y) if e-1 does not divide m, otherwise none. At e=2 the
complete inverse list is the following; j ranges over EVERY integer>=2.

| Owner | Own restart predecessor | Lowering predecessors |
| --- | --- | --- |
| A | ((m,m),y) | ((jm,m),y) |
| B | ((m,m),y/2) | ((jm,m),y) |
| C | ((m,m),y-1) | ((jm,m),y) |

Each inverse has the WHOLE real line as its actual target domain.
All are restrictions of affine C1 diffeomorphisms; single-label source
pieces give a countable Borel partition and a complete uniform atlas.
For original counting times Lebesgue, each inverse J is1 except B's
own restart inverse, whose J is1/2 EVERYWHERE, including y=0.
Translation/scaling of any Borel set gives respectively its same length
or half its length; hence the required every-Borel IMAGE holds, including
null sets and infinite measure. Infinite lowering multiplicity is not J.

With R_r(s) as defined in §1, direct induction on the actual steps gives

| Owner | F^r(s,x) | S_r(s,x) |
| --- | --- | --- |
| A | (a^r s,x) | 0 |
| B | (a^r s,2^{R_r(s)}x) | R_r(s) log2 |
| C | (a^r s,x+R_r(s)) | 0 |

These include every scan step; B has kappa=log2 exactly at a restart,
whereas A and C have kappa=0 everywhere. Applying §2 to these proved
own atlases yields every-point descent and every-Borel history IMAGE
for each control separately, with no inherited unverified premise.
Their complete incoming recursion is exactly the displayed inverse list
iterated as(2.4); there is no real-value, label, phase or depth restriction.

## 7. Control A — all fibres periodic after the finite label entry

Each prime p and EVERY x in R give exactly one primitive source cycle
C_p times{x}, with least period L_p=p-1 and sum C=0. There are no other
cycles: a periodic label must be on C_p and the fibre never changes.
Every source point is eventually periodic; none is terminal or
non-eventual. The full source packet is exactly

    O_{p,x}={(s,x):p(s)=p}.

Every such object reaches((p,2),x), and distinct p or x cannot merge.
This description includes all incoming branches, not just the cycle.
There are continuum many distinct packets for each p, each countable.

Choose b=((p,2),x). The actual anchor arrow for z=(s,x) has
l_z=t_s, beta_z=0. For w=(v,x), all arrows have

    k=t_s-t_v+mL_p,   c=0,   m in Z.                    (7.1)

Thus K_clock=G; K_lag=K_joint consists of those arrows with k=0,
which exist exactly when t_s==t_v modulo L_p. Source isotropy and
height-extension isotropy are L_p Z; ENTIRE H={0}. Heights belong to
the same extension orbit exactly when p,x agree AND h_z=h_w.
All real heights give distinct phases. A primitive forward return has
lag -L_p and clock0; its m-fold forward repetition has lag -mL_p,clock0.

P_q is C_{q+1} times R if q+1 is prime and empty otherwise. In the
nonempty case its original measure is infinite, while P_q^x and E^x
are empty. This supplies the positive/infinite-measure multiplicity case
without an invariant-measure argument or identifying different fibres.

## 8. Control B — null periodic cores and complete nonzero-fibre packets

On C_p, one complete label return sends x to2x and has sum log2.
After m returns it sends x to2^m x. Thus a source point is periodic
exactly when it is a prime-core point with x=0; its LEAST period is
L_p, not a multiple chosen from a nonprimitive label repetition.
Every x=0 point is eventually periodic, and EVERY x!=0 point is
non-eventual, since multiplication by positive powers of2 cannot fix it.
There are no terminals and no additional cycles at negative fibres.

### 8.1. The full zero packet for each prime

For each p the full zero packet is O_{p,0}={(s,0):p(s)=p}. Its anchor
at((p,2),0) has l_z=t_s, beta_z=R_s log2. Every arrow from(v,0) to(s,0)
is precisely

    k=t_s-t_v+mL_p,
    c=(R_s-R_v+m) log2,   m in Z.                       (8.1)

The lag kernel requires m=(t_v-t_s)/L_p to be an integer. The clock
kernel requires m=R_v-R_s. The joint kernel requires both, equivalently
t_s-L_p R_s=t_v-L_p R_v, with that same m. These formulas give the full
endpoint kernels, not just loops. Source isotropy is L_p Z with clock
m log2. ENTIRE H=(log2)Z, and extension isotropy is trivial.
All real extension phases are h-R_s log2 modulo(log2)Z, equivalently
h modulo(log2)Z; the equivalence does not shrink the entire H.
Positive-lag primitive isotropy has clock log2, whereas the primitive
forward return has lag -L_p and clock -log2. Repetition multiplies both.

### 8.2. Every nonzero fibre, phase and incoming

Let z=(s,x), x!=0, p=p(s), and xi_z=2^{R_s}x, its fibre at the first
anchor arrival. Write uniquely

    xi_z=epsilon u 2^{j_z},
    epsilon in{-1,+1},   1<=u<2,   j_z in Z.

Its full source packet is determined EXACTLY by(p,epsilon,u), and is

    {(s,epsilon u 2^{j-R_s}):p(s)=p, j in Z}.            (8.2)

Necessity follows because each label-anchor return multiplies by2.
For sufficiency two arrival exponents can be made equal by sufficiently
many further nonnegative label returns on each side. Hence all objects
listed in(8.2), and only those, have a common future. Each packet is
countable; there are continuum many for each p and each sign.

With b=((p,2),epsilon u), an actual anchor arrow has

    l_z=t_s-j_z L_p,
    beta_z=(R_s-j_z)log2=log(u/|x|).                    (8.3)

For j_z>=0 compare the first arrival of z with j_z returns of b.
For j_z<0 add -j_z returns to z and compare with b. This proves existence
with nonnegative legal witness lengths in both cases. Non-eventuality
shows uniqueness of lag and clock between any two endpoints.
All arrows from w=(v,y) to z have

    k=l_z-l_w,
    c=beta_z-beta_w=log(|y|/|x|).                        (8.4)

K_lag imposes l_z=l_w. K_clock imposes |x|=|y|, equivalently x=y within
this same-sign packet. K_joint imposes both. Source and extension
isotropy are trivial, ENTIRE H={0}, despite possible NONZERO arrow clocks.
The complete real phase is h-beta_z; equivalently h+log|x| for a fixed
packet. Equal(p,epsilon,u) and equal h+log|x| are necessary and sufficient
for extension-orbit equality. No nonzero source cycle or periodic
repetition is hidden by the multiplicative quotient notation.

For B, P_q=C_{q+1} times{0} if q+1 is prime, otherwise empty. All its
points have return sum log2 and all P_q have measure0. Their entire
incoming union is E^x=Q times{0}, also null. Thus the every-point
nonzero periodic clocks SURVIVE the theorem; no null core is deleted.
The period L_p varies with p while its return clock is always log2,
not log p. Outside E^x there are continuum many non-eventual zero-H
packets per p, not periodic packets inferred from Question2's hypothesis.

## 9. Control C — all source packets non-eventual, with exact phases

At the prime-label anchor, one label return sends x to x+1. No nonzero
number of returns fixes any real x. Thus there are NO source cycles,
every point is non-eventual, and there are no terminals. This is not
altered by the periodic label skeleton or the identically zero clock.

For z=(s,x) let xi_z=x+R_s, and write uniquely xi_z=u+j_z with
0<=u<1 and j_z in Z. Its full packet is exactly

    O_{p,u}={(s,u+j-R_s):p(s)=p, j in Z}.                (9.1)

Indeed future anchor returns add integers, and any two such integers
can be aligned with nonnegative extra returns. Necessity follows from
the same additive law. Equivalently p(s)=p and x modulo Z=u.
Each packet is countable, with continuum many per p.

For b=((p,2),u), the same signed-exponent argument as in §8 gives an
ACTUAL anchor arrow with l_z=t_s-j_z L_p and beta_z=0. Every arrow has

    k=l_z-l_w,   c=0.                                  (9.2)

K_clock=G; K_lag=K_joint imposes l_z=l_w. Source and extension isotropy
are trivial, ENTIRE H={0}. Two height objects are in the same orbit
exactly when p and u agree and their real heights are equal. These are
all real phases; there are no periodic source repetitions to count.
P_q, P_q^x and E^x are all empty for every q. Formula(9.1) and §6's
recursive inverses retain every actual incoming at every scan phase.

## 10. Result, stress tests and exact limitation

Both conditional questions are answered within the frozen class:
nonzero-periodic-clock saturation is original-mu null; positive P_q,
including infinite measure, yields continuum many DISTINCT full periodic
packets with entire H={0}. The proofs used countable chart coverage,
sigma-finite original measure, actual periodic identity and finite cycle
intersection, not an invariant probability, a representative-only atlas,
or a quotient-topology argument. Full incoming and allpoint versions stay.

The three controls separate different potential overclaims: A has full
real families of zero-clock cycles, B has actual null nonzero-clock
cycles plus non-eventual fibres with nonzero arrow clocks, and C has
zero clock but no source cycles at all. In particular:

- A measure-null exceptional set is not an empty pointwise ledger.
- H={0} does not imply c vanishes on every non-loop arrow.
- A label cycle is not by itself a full source cycle.
- A logarithmic return clock is not automatically the required log p.
- A family of periodic points is not one packet merely because it shares p.

Conditional audit ADVANCE: this measure-support screen has a proved
answer and the three owned controls satisfy the full frozen obligations.
STOP any inference of positive-original-measure support for nonzero
periodic clocks in this class. This is NOT a prime MAIN-candidate pass,
does not exclude isolated null prime packets or all arithmetic flows,
and does not authorize choosing a new fibre after seeing the outcome.
The same object and original measure remained fixed in each owner.
Classical fields NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED;
formal coordinates UNASSIGNED; Route B NOT INVOKED.

This raw is to freeze after FULL self-read and hash receipt. Scope/card
remain immutable. HOLD for root FULL raw read and DISTINCT PAPER UNLOCK
before reading author surfaces or producing CP2/CP3 final comparison.
