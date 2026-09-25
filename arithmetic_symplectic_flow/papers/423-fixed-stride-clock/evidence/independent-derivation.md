# Card-only raw derivation — Fixed-stride clocks and complete packets

Candidate: `ANG-AUDIT-20260923-FSC01`; batch O, round 4/5 (420–424).
Reviewer: `/root/nonlocal_source_review`; date: 2026-09-23.
Root separately released mathematics after fully reading the 103-line CP1.
Input: complete 83-line frozen card, reread through EOF before this derivation.
candidate-card.md SHA256 67af700efafe77b4c26c969239019b23008f6f4a4b4dfaa3d5fd76cd2faa0ee1
scope-review.md SHA256 f8e826b1e231e034cbb5108bc8598a4b73a15f0f625b268a7025e71e6438eb8b
Actual new scientific access: this card only; no author paper, README, ledger,
Outcome, author/helper answer, peer proof or sibling scientific output read.
Earlier shared-history/recovery exposure is disclosed in CP1, not concealed.
AI-assisted, inherited-model internal review: NOT_CALIBRATED, not blind,
cross-model, external or human peer review. Served identity is not attested.
Method: exact mathematical argument; no scientific code, numeric census,
network, external literature, Git, model change or publication operation.

## 1. The sampled owner's actual inverse and IMAGE

Write the parent's disjoint Borel source partition as (B_i), its inverse
theta_i:T(B_i)->B_i, and its fixed all-point version q_i on T(B_i).
All restrictions below use actual point sets, including null points.
For a length-k itinerary I=(i_0,...,i_{k-1}), define
D_I={x:T^r x in B_{i_r} for 0<=r<k} and E_I=T^k(D_I).
The D_I form a countable disjoint Borel partition of all X, since T is total.
T^k is injective on D_I: successively undo its k uniquely assigned branches.
Its inverse Theta_I is theta_{i_0} o ... o theta_{i_{k-1}} on E_I only.
The specified Borel inverse maps and their finite compositions make this an
actual Borel bijection; E_I can also be described by the Borel legality tests
for these inverse words. No full-image or surjectivity assumption is used.
For y in E_I, put x_r=T^r Theta_I(y), so x_k=y, and prescribe

    J_I(y)= product_{r=0}^{k-1} q_{i_r}(x_{r+1}).

Each factor is positive finite at every actual point, hence so is J_I.
The parent's IMAGE identity also implies its weighted form
integral_{theta_i E} f dmu = integral_E f(theta_i y) q_i(y) dmu(y)
for nonnegative Borel f: first indicators, then simple functions and monotone
limits. Restrict each step to the actual intermediate domain and apply this
formula k times. For EVERY Borel E subset E_I it gives

    mu(Theta_I E)=integral_E J_I dmu.

Thus this is the sampled owner's own Borel IMAGE, not a borrowed density.
For x in D_I, -log J_I(Rx)=sum_{r=0}^{k-1} kappa_T(T^r x)=S_k^T(x).
Consequently kappa_R=S_k^T and S_a^R=S_{ka}^T at every point.
No division by k occurs. No later almost-everywhere version selection occurs.
The measure remains the frozen mu; total preimage densities, when branches
overlap in range, are not substituted for individual inverse IMAGE versions.

## 2. Actual groupoids, cocycles and exact stride image

For either total owner U, let lambda(z,ell,w)=ell. Suppose two witnesses
(a,b) and (a',b') give the same triple. Their differences agree, so one pair
is the other plus (r,r), r>=0. The extra clock terms are identical because
U^a z=U^b w. Thus S_a(z)-S_b(w) depends on the actual triple, not its witness.
Identity and inverse clocks are 0 and -c. For composable witnesses (a,b)
from w to z and (u,v) from t to w, (a+u,b+v) witnesses the composite.
Expanding S_{a+u}(z)-S_{b+v}(t) and using
S_u(U^b w)-S_b(U^u w)=S_u(w)-S_b(w) proves clock additivity.
The forward arrow (Uz,-1,z) has clock -kappa_U(z), as frozen.
Every height object is retained, with (w,h)->(z,h+c); no quotient regularity
or positive suspension roof follows from this action-groupoid construction.

Define iota:G_R->G_T by (z,ell,w)->(z,k ell,w).
An R-witness (a,b) gives a T-witness (ka,kb), and own-clock compatibility is
c_R(z,ell,w)=c_T(z,k ell,w) by Section 1. Triple equality makes iota injective.
It preserves composition, units and inverses. Its EXACT image is

    iota(G_R)={g in G_T:lambda(g) in k Z}.

Indeed, a T-arrow of lag divisible by k has a witness (a,b) with a=b mod k.
Choose 0<=r<k so a+r and b+r are both divisible by k. Totality permits the
common point to advance r times, giving an R-witness and unchanged clock.
This padding argument is precisely why terminal partial maps are excluded.
If X is nonempty, a parent forward arrow has lag -1 and is outside the image
for k>=2, even if its source and range coincide. No surjectivity is claimed.
If X is empty, both groupoids and the positive ledger are empty.

For either U, the full kernels are exactly

    K_lag(U)={(z,0,w):U^a z=U^a w for some a>=0};
    K_clock(U)={(z,a-b,w):U^a z=U^b w, S_a(z)=S_b(w)};
    K_joint(U)=K_lag(U) intersect K_clock(U).

These are witness-invariant statements. K_lag can contain nonunit mergers;
K_clock need not equal K_lag, and a lag-zero merger need not have zero clock.
Under iota, K_lag(R)=K_lag(T) literally on lag-zero triples: pad a to a
multiple of k. Also iota(K_clock(R))=K_clock(T) intersect lambda^{-1}(k Z),
and iota(K_joint(R))=K_joint(T). These describe the FULL kernels, not a core
restriction. The pointwise arrow formulae below give their complete values
within every source component as well.

## 3. Isotropy, all incoming and the physical phase of any total owner

A source loop (z,ell,z) with ell!=0 gives an eventual periodic tail. Conversely
if z eventually enters a least-q cycle, its source isotropy is exactly q Z:
large enough witnesses realize every multiple of q, and any return difference
is a multiple of the least tail period. Noneventual points have isotropy {0}.
If the signed sum on that least cycle is C, the loop of lag n q has clock n C;
prefix clocks cancel on the tail. Thus the ENTIRE H_z is C Z, or {0} if C=0.
It is never enlarged by incoming branches; in this integer-lag groupoid it
cannot be a dense clock subgroup. Noneventual points have H_z={0}.
Extension isotropy at (z,h) consists of source loops of clock zero: it is
trivial for C!=0, is the entire q Z for C=0, and is trivial when noneventual.
These statements hold for every h, not just a selected height section.

Here is an explicit all-incoming description. On a source orbit choose a
reference x_* and one actual arrow g_z=(z,l_z,x_*) to every z; let b_z=c(g_z).
If x_* has eventual least period q and cycle sum C, EVERY arrow w->z is

    g_z u_n g_w^{-1}, with lag l_z-l_w+n q,
    clock b_z-b_w+n C, n in Z.

This is exhaustive by multiplying any arrow on the left/right by the two
reference inverses. The u_n are all source loops at x_*, not just forward
returns. For noneventual x_* there is exactly one arrow between each pair,
with lag l_z-l_w and clock b_z-b_w.
In these formulas, set the displayed lag to zero, clock to zero, or both,
to obtain all three kernels, including their nonunit elements.
The entire height quotient on the source orbit has phase

    [h-b_z] in R/H, with real translation [h-b_z]->[h-b_z+t].

Changing g_z changes b_z by an element of H; changing reference translates
the phase chart. Neither changes H or the number of source packets.
When H=C Z with C!=0 this is one circle of primitive |C| and repeats r|C|,
r>=1. When H=0 it is a free real line with no positive period, even though
zero-clock eventual components retain their nontrivial extension isotropy.
No global Borel choice of references or nice quotient is asserted.

## 4. ALL eventual packets under the fixed stride

Fix a parent least-q cycle p_j=T^j p_0, j mod q, with signed sum C.
Set g=gcd(q,k), q'=q/g and d=k/g. On the parent core R advances j by k.
There are exactly g distinct R cycles, indexed by j mod g; each has least
period q'. Over such a period R uses k q'=d q parent steps, hence its signed
sum is C_R=d C. This uses the actual sampled IMAGE clock proved in Section 1.

For ANY point z eventually entering this core, choose r>=0 and j with
T^r z=p_j. The class eta(z)=j-r mod q is independent of this choice: any
later arrival advances both j and r equally, and all arrivals can be aligned.
eta(Tz)=eta(z)+1 and eta(Rz)=eta(z)+k. The COMPLETE sampled basin assignment is

    B_s={z eventually entering this parent core: eta(z)=s mod g},
    s=0,...,g-1.

Each B_s is nonempty and contains the whole corresponding R core. For large
N with kN>=r, R^N z=p_{j+kN-r}; this lies in that core. Conversely any R
arrow must preserve the residue, since its parent lag is divisible by k.
All points in B_s share a common R tail after possibly unequal numbers of
steps around the same R cycle. Thus B_s are EXACTLY the g sampled source
orbits, with every incoming branch assigned; no other point joins this basin.
Eventual periodicity for R and T is equivalent: an R repetition is a T
repetition, and the preceding forward calculation proves the converse.

At every point of B_s, source isotropy for R is q' Z; its image in the parent
is lcm(q,k) Z=d q Z. The full H_R is d C Z. If C!=0, extension isotropy is
trivial and each B_s gives one primitive d|C| circle with all repeats.
If C=0, each B_s has H_R=0, source and extension isotropy q' Z, and one free
physical line: NO positive primitive is invented from that source cycle.

For fully explicit incoming phases, choose p_s in the s-th R core and let
R^{A_z}z=R^{J_z}p_s with 0<=J_z<q'. Set
l_z=A_z-J_z and b_z=S_{A_z}^R(z)-S_{J_z}^R(p_s).
Then every w->z in B_s has lag l_z-l_w+n q', clock b_z-b_w+n dC,
and physical phase [h-b_z] modulo dC Z, or h-b_z on R when C=0.
These describe all kernels by the tests in Section 3. They include tails,
zero clock, both loop directions and all height phases.
Different arrival times change l_z by a multiple of q' and b_z by the same
multiple of dC. A new core phase/reference only relabels/translates charts.

One can also check completeness directly in the parent formula of Section 3:
the congruence l_z-l_w+nq=0 mod k is solvable in n iff g divides l_z-l_w.
When solvable, its solutions form one residue class modulo d, so the retained clock
increments are exactly dC, not C unless d=1 or C=0.

Distinguish source-packet count from individual height-quotient fibers.
For C!=0, each of the g sampled circles maps to the parent circle as the
degree-d map R/(dC Z)->R/(C Z), up to a phase translation. Thus a given
parent height-groupoid orbit has g d=k sampled height-orbit lifts, while
the number of sampled closed physical-flow packets is g; k counts the fibers,
not the packets in general (the two counts agree when d=1).
For C=0, each sampled line maps by a translation to the parent line, giving
g lifts of each parent height orbit, not k when d>1. Nontrivial zero-clock
isotropy explains why this case must not be inferred from the nonzero case.

## 5. ALL non-eventually-periodic packets, including coalescences

Let O be ANY noneventual parent source orbit and choose x_* in O. The source
isotropy is trivial, so there is one actual arrow g_z=(z,l_z,x_*) per z.
Its lag l_z and clock b_z are unique even if it has several witness pairs.
The unique arrow w->z has lag l_z-l_w and clock b_z-b_w.
The forward arrow implies l_{Tz}=l_z-1 and b_{Tz}=b_z-kappa_T(z).
All k lag residues occur: x_*,Tx_*,...,T^{k-1}x_* have distinct residues,
using only total forward evolution, NOT the existence of backward preimages.

    O_r={z in O:l_z=r mod k}, r mod k,

are therefore exactly k nonempty sampled source orbits. The exact-image
theorem proves both directions: w,z lie in one sampled orbit iff their lags
are congruent. Its unique R arrow has lag (l_z-l_w)/k and clock b_z-b_w.
Every point and incoming branch lies in one of these k classes. If distinct
z,w coalesce at equal parent time, l_z=l_w, so their nonunit lag-zero arrow
survives in R. It also has zero clock exactly when b_z=b_w; no injectivity
assumption is inserted to discard these mergers.
All source and extension isotropies and all H are zero on every O_r.
The full physical phase is h-b_z in R; using a reference inside O_r only
adds a constant. Thus the entire parent free physical line splits into k
free lines, all mapping by translations to the parent line; no positive
period is generated. Each parent height orbit has exactly k such lifts.
This covers arbitrary noneventual common-tail components, not just forward
rays or bi-infinite bijective controls, and needs no smooth/Borel transversal.
Together Sections 4–5 exhaust X. There are no omitted terminating points
because the frozen T is total, and no appeal to an asymptotic attracting basin.

## 6. Rational-cycle necessary-target filter and its precise boundary

Assume EVERY nonzero parent cycle has M=exp(|C|) rational and >1.
Its g sampled closed packets each have primitive log(M^d), d=k/g.
If this equals log p for an ordinary integer prime p, write M=a/b reduced.
Then a^d=p b^d. Coprimality forces b=1; if d>=2, a^d cannot be prime.
Hence the only prime possibility is d=1 and M=p. But d=1 means g=k>=2,
so this parent packet produces k DISTINCT sampled packets at the same prime.
Their basins are disjoint; equal periods cannot license a quotient of them.
Thus every nonzero parent cycle either supplies a nonprime sampled primitive
or violates prime uniqueness. If there are no nonzero parent cycles, all
sampled H are zero and the positive ledger is empty, failing nonemptiness.
The conjunction of nonempty + prime-only + prime-unique is therefore
IMPOSSIBLE under this rational-cycle assumption and uniform k>=2.
Extra all-prime coverage cannot repair an already failed necessary condition.
Signed C is covered by absolute values; zero C remains in the full ledger.
The hypothesis concerns C on a full parent cycle, not each one-step multiplier.

Without rationality, M^d=p can hold with M=p^(1/d); the preceding reduced-
fraction argument is then unavailable. Control C below realizes that boundary
on its full carrier. It disproves any unconditional fixed-stride no-go.
It does NOT provide an arithmetic source, all-prime coverage or a reason to
choose an input radical. Solving M^d=p backwards from desired p is fitting,
not endogenous arithmetic; the class supplies no mechanism excluding this
PROVES_TOO_MUCH risk. Frozen all-point versions prevent silent changes during
this audit but do not by themselves establish their strong naturalness.

## 7. Expansion lemma used to report controls A and C completely

For F_a(x)=a x on ALL R, a>1, inverse y/a is an actual Borel bijection.
Lebesgue scaling gives mu(E/a)=a^{-1}mu(E) for EVERY Borel E, so its geometric
all-point version is 1/a and its own clock is b=log a, also at 0.
Directly for F_a^k(x)=a^k x, the inverse is y/a^k, IMAGE is a^{-k}, and own
clock is kb. This direct geometric check is independent of assuming clock
inheritance. Both maps are total bijections on the entire specified carrier.
Their full groupoids are respectively

    G_T={(a^{-ell}w,ell,w):w in R, ell in Z}, c_T=ell b;
    G_R={(a^{-k ell}w,ell,w):w in R, ell in Z}, c_R=k ell b.

Both lag kernels, clock kernels and joint kernels are exactly the units.
The only periodic point for either map is 0, since (a^n-1)x=0 forces x=0.
Invertibility implies that its entire incoming/eventual basin is just {0}.
For T at 0: source isotropy Z, H=bZ, extension isotropy {0}, phase h mod bZ,
one primitive b packet, repetitions rb. For R: source isotropy Z embedded
as kZ, H=kbZ, extension isotropy {0}, phase h mod kbZ, one primitive kb
packet, repetitions rkb. The circle map to the parent has degree k.

EVERY nonzero T source orbit has a unique representative epsilon u with
epsilon in {+1,-1} and 1<=u<a, and consists of x_n=epsilon u a^n, n in Z.
The half-open normalization includes u=1 and excludes u=a without deleting
any real point. Every arrow x_m->x_n has lag m-n and clock (m-n)b.
Parent phase is h+n b. R splits this orbit into k classes n=r mod k;
all arrows within one class have lag (m-n)/k and the SAME clock (m-n)b.
Using x_r as its own reference, the sampled phase is h+(n-r)b.
Each such class has source/extension isotropy {0}, H=0 and one free physical
line; there are no positive repetitions. No point can enter zero from here.
As epsilon,u,r vary these are ALL sampled nonzero source orbits, equivalent
to representatives epsilon u' with 1<=u'<a^k. This is a full, not local, ledger.

## 8. Control A — full 3x parent and 9x sample

Here a=3, k=2, b=log3. The parent's inverse is y/3, geometric IMAGE 1/3;
the sampled inverse is y/9, geometric IMAGE 1/9. Their own clocks are log3
and log9. Section 7's formulas apply on all real points, with no extra labels.
Parent zero: one least-1 cycle, source isotropy Z, H=log3 Z, extension
isotropy zero, phase h mod log3, primitive log3 and repeats r log3.
Sampled zero: one least-1 cycle, source isotropy Z, H=log9 Z, extension
isotropy zero, phase h mod log9, primitive log9 and repeats r log9.
The sampled source loop ell maps to parent 2ell; the circle cover has degree2.
Neither owner has other periodic or eventually periodic points.
For each epsilon,u with 1<=u<3, all nonzero parent points x_n=epsilon u3^n
form one orbit. The sampled orbits are precisely its even and odd n classes.
Incoming arrows, both real phase lines, zero isotropies/H and all-unit kernels
are given explicitly in Section 7 with k=2. This accounts for every real point.
M=3 is rational on the parent zero core, g=1,d=2; the sampled primitive
log9 is a composite logarithm. Sampled prime-only FAILS; nonemptiness holds.
The parent's sole log3 packet is not an endogenous arithmetic mechanism.

## 9. Control B — full labelled parent and three retained sampled cores

Put alpha=2^(1/3), b=log(alpha)=log2/3, labels j in Z/3.
The actual inverse of T(x,j)=(alpha x,j+1) is (y,j)->(y/alpha,j-1).
Summing Lebesgue scaling over all three labels gives inverse IMAGE alpha^{-1}
on EVERY Borel subset of R x Z/3, including all null core points.
Directly R(x,j)=(2x,j), inverse (y,j)->(y/2,j), has IMAGE 1/2 on the same
full measure space. Own clocks are b and log2=3b respectively.
For w=(y,j), the full groupoids and clocks are

    G_T: z=(alpha^{-ell}y,j-ell), ell in Z, c=ell b;
    G_R: z=(2^{-ell}y,j), ell in Z, c=ell log2.

These include EVERY incoming arrow; iota multiplies ell by3 and has exactly
the parent lag-3Z image. Both owners have all three kernels equal to units.
Periodicity requires x=0. Parent Gamma={(0,0),(0,1),(0,2)} is ONE least-3
cycle, signed sum C=3b=log2. For an arrow (0,j)->(0,i), the possible lags
are ell=j-i mod3, with clock ell b. Source isotropy at each zero is 3Z,
H=log2 Z, extension isotropy zero, phase [h+j b] mod log2 using (0,0)
as reference. There is one primitive log2 packet and repeats r log2.
Invertibility makes its full incoming basin exactly Gamma, with no nonzero
tails. The label change on one step is not an extra source loop of clock b.
For R each (0,j) is a separate least-1 core with basin {(0,j)}, source
isotropy Z, H=log2 Z, extension isotropy zero and phase [h] mod log2.
There are THREE distinct primitive log2 packets, each with repeats r log2.
Their maps to the parent circle are [h]->[h+j b], bijective individually;
no labels are quotiented. Here q=k=3,g=3,d=1, in agreement with Section 4.

Every nonzero parent source orbit has the UNIQUE normalized form

    x_n=(epsilon u alpha^n, j_0+n mod3), n in Z,
    epsilon=+1 or -1, 1<=u<alpha, j_0 in Z/3.

Normalize the absolute real coordinate to find n,u, then j_0=j-n; this
proves both coverage and uniqueness of this parent orbit parametrization.
Every arrow x_m->x_n has lag m-n and clock (m-n)b; parent phase is h+n b.
R splits it into r=0,1,2 classes n=r mod3, each with fixed label j_0+r.
Within each class the arrow lag is (m-n)/3, clock (m-n)b, and phase
h+(n-r)b=h+((n-r)/3)log2 using x_r as its own reference.
All these nonzero classes have H=0, trivial source/extension isotropy and
free physical real lines with no positive period. They exhaust all nonzero
sampled orbits, equivalently (epsilon u'2^m,j), 1<=u'<2, m in Z.
The intervals [1,alpha), [alpha,alpha^2), [alpha^2,2) supply the three
possible u'=u alpha^r and retain all endpoints with their proper owner.
Although the ONE-STEP multiplier alpha is irrational, the PARENT CYCLE
multiplier exp(C)=2 is rational. Hence B is INSIDE the rational-cycle filter.
The sampled ledger is nonempty and prime-only but prime uniqueness FAILS.

## 10. Control C — full irrational-parent boundary

Here a=sqrt3, k=2, b=log3/2. Actual inverse y/sqrt3 has geometric IMAGE
1/sqrt3; directly the sample R(x)=3x has inverse y/3 and geometric IMAGE 1/3.
Own clocks are log3/2 and log3 on all R, including zero. Section 7 proves
both IMAGE identities, full groupoids, all incoming and all-unit kernels.
For the parent zero core: least period1, source isotropy Z, H=(log3/2)Z,
extension isotropy zero, phase h mod (log3/2), primitive log3/2 and repeats
r log3/2. This primitive is not log of an ordinary integer prime.
For sampled zero: least period1, source isotropy Z, H=log3 Z, extension
isotropy zero, phase h mod log3, one primitive log3 packet, repeats r log3.
The source loop embedding multiplies lag by2 and the circle map has degree2.
No other periodic or eventually periodic points exist; zero's basin is {0}.
ALL nonzero parent orbits are x_n=epsilon u(sqrt3)^n with 1<=u<sqrt3.
Each splits into the even/odd sampled classes; their arrows and phases are
Section 7 with b=log3/2,k=2, and their H and both isotropies are zero.
All real points and both sampled free lines of every parent orbit remain.
Here M=sqrt3 is irrational, g=1,d=2. The sampled ledger meets the scoped
nonempty/prime-only/prime-unique NECESSARY condition with its single prime3.
It does NOT cover all primes, satisfy the rational-parent premise or admit
an arithmetic candidate. This external control delineates, not refutes, the
conditional theorem and rules out extending it to arbitrary parent multipliers.

## 11. Bounded disposition and freeze gate

Established from this card: own all-point sampled IMAGE and clock; exact
stride subgroupoid; full kernels, isotropies, incoming, H and phases; all
eventual and noneventual packet splitting; rational-cycle necessary-target
obstruction; and complete full-owner parent/sample ledgers for A, B and C.
The same-object ledger remains intact separately for T and its declared new
owner R; compatibility was proved, not inferred from common point names.
The proof does not add a section, a label quotient, a roof or a rescaled clock.
Portfolio: advance this bounded conditional filter; NO CANDIDATE ADMISSION.
T0/own geometric CLOCK COMPONENT only; arithmetic T1 NOT PASSED; T2 conditional.
T3 NOT AUDITED; classical NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.
Strong naturalness, endogenous prime source and any all-prime mechanism remain
unestablished. No novelty claim, venue criteria or publication certification.
This raw is frozen before manuscript access; CP2/CP3 are NOT PERFORMED.
Root must personally read the full raw before a separate PAPER UNLOCK.

EOF — card-only independent derivation complete; HOLD for manuscript unlock.
