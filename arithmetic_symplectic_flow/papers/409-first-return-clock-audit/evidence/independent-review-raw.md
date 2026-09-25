# FRC01 — card-only independent raw derivation

Candidate `ANG-AUDIT-20260923-FRC01`; Paper409; batch round5/5.
Conclusion: the frozen induction/ownership contract is proved with its stated
sufficient PMR hypothesis; none of the controls authorizes a new arithmetic source.

## 0. Authority, access and method

Root explicitly released raw mathematics after reading all98 scope-report lines.
The sole scientific input was the clarified card, reread fully through line94.
candidate-card.md SHA256 9e0220ef714ed52af183a5db5ad4f722ec984eef7364654d6a4274ead513cfee — 94 lines.
Original85-line prefix SHA256 bb233bb504c4fa265df1807f7b0377397dfb3a571199c2ef3bff28a8bc1d9069.
scope-review.md SHA256 296d444b1ec7217c03a43930c560f38ce46d9d8958aabd3a1734be517216a30d — 98 lines.
The CP1 record remains unchanged. Retained ARS and local instructions apply.
No author manuscript, README, ledger, peer output, other new package or197
was read. Root's design exposure stated in the card is not independent evidence.
Root later notified that author surfaces and an Outcome append existed; none
was opened. A prefix-only recheck retained the clarified94-line input hash.
No external source, scientific code, numerical experiment or auxiliary agent
was used. Shell commands only read inputs and measure existence/receipts.
AI supplied this exact derivation and drafting. Shared history is retained;
not blind/cross-model/external review. Served model identity/settings are not
independently attested; no human verification is certified. NOT_CALIBRATED.
Method: Borel branch construction, weighted IMAGE composition, actual-triple
algebra, visit counting and exhaustive symbolic formulas for the three controls.

## 1. First-return owner and its every-Borel inherited IMAGE

Let P_i be the assigned disjoint Borel source partition, Q_i=T(P_i), and
theta_i:Q_i->P_i the actual inverse. Its frozen positive finite Borel density
J_i satisfies mu(theta_i E)=integral_E J_i dmu for every Borel E subset Q_i.
Legal forward domains D_n are Borel; on D_n write

    S_n(x)=sum_{j<n} kappa(T^j x),  S_0=0.

Every step uses its uniquely assigned piece. In particular this does not infer
pointwise values from an a.e. density or introduce a clock at a T terminal.

For n>=1 and a legal source itinerary word i=(i_0,...,i_{n-1}), define E_{n,i}
to consist of x in B with that itinerary, T^n x in B and T^j x outside B
for 1<=j<n. These countably many Borel sets partition D_B. Each T^n is
injective on its word; its restricted image F_{n,i}=T^n(E_{n,i}) is Borel
and its inverse theta_{n,i}:F_{n,i}->E_{n,i} is Borel, as for injective
Borel maps between standard Borel spaces. Thus R is a countably piecewise
injective partial Borel map on ALL B, with no-return points retained as terminals.
r=n on E_{n,i}; rho=S_n there is a finite Borel function only on D_B.
If B is empty all these induced objects are empty, not a nonempty packet owner.
If D_B is empty but B is not, all its points remain and only unit arrows exist.

Every actual first-return inverse occurs in these words: endpoints are in B,
all proper intermediate forward points are outside B, and each step is legal.
For w in F_{n,i}, with x=theta_{n,i}(w), put

    J^R_{n,i}(w)=product_{j<n} J_{i_j}(T^{j+1}x)=exp(-S_n(x)).       (1)

The one-step IMAGE identity extends to nonnegative Borel integrands by simple
functions and monotone convergence. Applying that weighted identity successively
to the n inverse branches yields, for every Borel E subset F_{n,i},

    mu_B(theta_{n,i} E)=integral_E J^R_{n,i} dmu_B.                 (2)

Restricting source and target to B changes no integral: both lie in B, and
mu_B is mu restricted to B. Sigma-finiteness is retained. Different word
images can overlap; (2) is a branch IMAGE law, not a global many-to-one image law.
If mu(B)=0, (2) is still true but does not determine pointwise densities;
the positive finite product in (1) is the inherited version at EVERY point.
Since the source partition and first return are unique, a legal R edge has
one assigned value, and -log J^R(Rx)=rho(x). No new null-set version is chosen.

For legal R^m x define r_m(x)=sum_{j<m}r(R^j x), r_0=0. Induction gives

    R^m x=T^{r_m(x)}x,   S^R_m(x)=S_{r_m(x)}(x).                  (3)

The r_m are strictly increasing in m wherever defined. Their values enumerate
EXACTLY the nonnegative legal T times at which the forward path from x in B
lies in B, including time0. A legal time in B cannot be skipped by first return.

## 2. Actual groupoids, descent, kernels and extension

For either partial map F=T or R, take all triples (x,m-n,y) with legal
F^m x=F^n y, identifying equal triples. Units include every source terminal.
If two presentations have equal lag, their depth differences are the same
integer; after orienting it positively, the added common forward tail cancels
from the two clock sums. Hence c_F=S^F_m(x)-S^F_n(y) descends to actual triples.
For composable presentations meeting y at depths n and p, extend both to
L=max(n,p); their common tail gives the composite and adds their clocks.
Inversion negates lag and clock. The countable Borel branch construction
retains all legal inverse histories, not arbitrary extra free branch words.

For either owner the entire kernels are the exact sets

    K_F={g=(x,m-n,y):F^m x=F^n y, S^F_m(x)=S^F_n(y)},
    M_F={(x,0,y):some legal n has F^n x=F^n y},
    K_F intersect M_F={(x,0,y):some legal n has F^n x=F^n y,
                                             S^F_n(x)=S^F_n(y)}. (4)

They include all units and use all depths. The extension on the full source
times R is (y,h)->(x,h+c_F(g)) for every h. Each finite-itinerary transport
has IMAGE density exp(-c_F), by forward/inverse weighted branch composition.
No smooth manifold or regular quotient is inferred from these Borel facts.

## 3. Phi: injective clock-preserving morphism, not lag identity

For g=(x,m-n,y) in G_R set

    Phi(g)=(x,r_m(x)-r_n(y),y) in G_T|B.                          (5)

Its parent meeting is R^m x=R^n y. If a second R presentation increases both
depths by d, the additional d returns start at this same meeting point and
have the same cumulative base length. Their contributions cancel in (5).
Thus Phi is well-defined. Common-return refinement proves the morphism law:
the common added elapsed lengths cancel just as the added return counts do.
For example using L=max(n,p) to compose two arrows, (3) yields the sum of
their two base-lag differences. Units and inverse are preserved as well.
Equation (3) gives the exact clock identity c_T(Phi(g))=c_R(g).

For injection, suppose (m,n) and (a,b) represent arrows with the same Phi.
Their endpoints agree and r_a(x)-r_m(x)=r_b(y)-r_n(y). After interchanging
the pairs assume a>=m, hence b>=n by strict increase. From the common point
R^m x=R^n y, the two continuations run for the SAME number of base steps.
Their successive visits to B are the same actual visits. Thus they contain
the same number a-m=b-n of returns, giving a-b=m-n. The R triples coincide.
This works for finite paths and terminals; it does not presuppose infinite returns.

All formulas are Borel: one may choose the first valid depth-pair presentation
in a countable enumeration; presentation independence makes the choice harmless.
The lag cocycles are NOT identified: lag_T composed with Phi is r_m-r_n,
not generally m-n. Clock kernels obey Phi(K_R)=Phi(G_R) intersect K_T.
In contrast Phi(M_R) uses differences r_m(x)-r_m(y), possibly nonzero.
One cannot automatically identify lag kernels or their clock-kernel intersections.

Under PMR, take any parent arrow (x,k-l,y) with x,y in B and meeting u.
Choose the stipulated s>=0 with legal T^s u in B. The times k+s and l+s
are visits to B, so by the exact visit enumeration they equal r_m(x),r_n(y)
for some legal m,n. The corresponding R arrow maps to the original parent
triple: (k+s)-(l+s)=k-l. Hence PMR suffices for surjectivity onto G_T|B.
No converse or necessity of PMR is claimed. Without PMR an earlier alternative
presentation might still represent an arrow; failure of this sufficient test
alone is not a proof of nonsurjectivity. Control C proves its own failure below.

## 4. Entire periodic/incoming/phase ledger and the section boundary

For any deterministic partial F, nonzero source isotropy occurs exactly at
eventually periodic points: F^m x=F^n x, m>n, gives a legal periodic tail.
If its least cycle length is q, the entire source isotropy is qZ. For the
cycle clock C_F, c_F(kq)=kC_F, including at every finite-entry incoming point.
Thus H_F=C_F Z; extension isotropy is 0 when C_F!=0 and qZ when C_F=0.
Terminal-reaching or infinite non-eventually-periodic points have source and
extension isotropy0 and H=0. This retains zero cycles rather than deleting them.

For any source component choose reference b and an arrow g_x=(x,k_x,b).
The full extended orbit SET on that component is R/H_b with phase
[h-c_F(g_x)]. Different choices differ exactly by H_b. All phases occur;
height translation has ENTIRE stabilizer H_b. When C_F!=0 the primitive is
|C_F| and repetitions are n|C_F|, n>=1; when H=0 this is a free R orbit.
No global Borel section or smooth quotient is asserted. Equal periods cannot
merge disjoint source components, since extension arrows still require source arrows.

Let O be a least-q parent cycle meeting B in d=|O intersect B|>=1 points.
First return follows these d points in their cyclic order, so the induced
least period is d, and r_d at each marked cycle point is q. The d disjoint
return segments concatenate to the original q-cycle, proving

    C_R=sum rho over the induced cycle = sum_O kappa = C_T=C.      (6)

The complete induced incoming basin is B intersect the complete parent basin
of O: any legal finite entry to O subsequently reaches a marked cycle point;
all its visits to B are first-return iterates. The reverse inclusion is immediate.
At each such point source isotropies are respectively dZ and qZ, Phi(kd)=kq,
but H_R=H_T=CZ and the extension-isotropy alternatives are exactly those above.
This conclusion needs no global PMR: within this basin every parent meeting
can continue to O intersect B, so the required refinements exist there.

Fix b_0 in O intersect B and write the marked vertices b_j=T^{t_j}b_0,
0=t_0<...<t_{d-1}<q. If T^N x=b_j with x in B, N is an induced visit time.
The shared parent/induced phase is

    [h-S_N(x)+S_{t_j}(b_0)] modulo C Z.                           (7)

All entry choices agree modulo C. For C<0 the positive generator uses the
opposite lag orientation; C=0 leaves real phases and nontrivial cycle isotropy.

If O misses B, it supplies no induced periodic cycle. Its incoming B points
can belong to that parent orbit yet eventually stop returning to B. Thus
meeting every parent groupoid orbit does not itself preserve periodic cores.
By contrast, PMR plus meeting every parent orbit makes the full extended
orbit sets equivalent with the SAME height action: move each parent point to
B by a parent arrow; surjectivity of Phi identifies exactly the same B pairs.
This componentwise argument requires no chosen global measurable transversal.
Without those guarantees any claim about the FULL parent must retain missing
cores and other omitted components explicitly, not replace X by B silently.

## 5. Control A — label switch, elapsed time two

Put L=log2. On X_A={0,1} times R, each label branch maps x->2x into the
opposite label and has actual inverse x->x/2. Counting times Lebesgue gives
mu(theta E)=mu(E)/2 for every Borel subset of its target label. J=1/2 and
kappa=L everywhere; all inverse iterates switch labels and divide by powers of2.
The full map is a bijection, with no source terminals or omitted predecessors.

Its complete groupoid is

    G_A={((j,x),k,(j+k mod2,2^k x)): j=0,1; x in R; k in Z},
    c_A=kL;   K_A=M_A=K_A intersect M_A=units.                    (8)

The two zero points form the sole least-period2 cycle, with entire incoming
basin consisting of those two points. Their source isotropy is 2Z, H=2L Z,
extension isotropy0. This is ONE packet, primitive 2L=log4, with all phases
[h+jL] modulo 2L and repetitions n log4. Every nonzero point is neither
periodic nor eventually periodic, since 2^q x=x would force x=0.
For any nonzero reference b, write z=T^n b uniquely; its component phase
h+nL is real, its isotropies and H are0. All bi-infinite source orbits remain.

On B={0} times R, r=2 everywhere; R(0,x)=(0,4x), rho=2L and J_R=1/4.
The unique return inverse word divides by4, with its own every-Borel IMAGE.
The full induced relation is ((0,x),k,(0,4^k x)), c_R=2kL, kernels all units.
At0 its source isotropy is Z, extension isotropy0 and H=2L Z. Nonzero points
have isotropies/H zero, components 4^Z x and real phases h+2nL relative to
a reference. There are no induced terminals and exactly one periodic packet.

PMR holds: a meeting on label0 is already in B; one on label1 returns in
one more step. Every parent orbit and its periodic core meet B. The parent
restriction consists exactly of even base lags, and Phi sends k to 2k onto it.
The physical primitive stays log4, NOT log2. Changing its clock to log2 per
return would change the owner. Parent and induced both fail the prime-only
benchmark despite nonempty, unique positive packet support.

## 6. Control B — a whole component is excluded by the section

Set d_0=2,d_1=3 and L_j=log d_j. Each full label line owns the linear
bijection x->d_j x, inverse x/d_j, all-point J_j=1/d_j and every-Borel
IMAGE. There are no cross-label inverse histories and no parent terminals.
The complete parent relation is

    G_B={((j,x),k,(j,d_j^k x)): j=0,1; x in R; k in Z},
    c_B=kL_j;   K_B=M_B=K_B intersect M_B=units.                  (9)

Each (j,0) is a fixed point with basin {(j,0)}, source isotropy Z,
extension isotropy0 and entire H=L_j Z. Thus the parent has exactly TWO
positive packets, log2 and log3, separately with all phases modulo L_j and
repetitions nL_j. Every nonzero point has both isotropies and H zero;
its full component is d_j^Z x with real phase h+nL_j relative to a reference.

On B_sec={0} times R, r=1 everywhere, R(0,x)=(0,2x), J_R=1/2, rho=log2.
The complete induced relation is the j=0 part of (9), with the same clocks,
unit kernels, complete nonzero components and phases. Its sole positive
packet is (0,0), source isotropy Z, extension isotropy0 and H=log2 Z.
There are no induced terminals. PMR holds with s=0 for every meeting from
B_sec; Phi is onto G_T|B_sec and here preserves the integer lag as well.
But the section misses ALL label1 components, including its fixed core.
The log3 packet has not vanished from the full parent and cannot be omitted
from a parent claim. Parent and induced meet the finite necessary prime,
nonempty and uniqueness tests, but neither supplies eventual all-prime coverage.

## 7. Control C — complete relation and clocks on the full parent

Write beta_a=beta_t=1, beta_b=3/2 and eta_sigma=log beta_sigma; L=log2.
The only target label of a forward edge is t. Every (t,w) has exactly the
three legal predecessors (a,w/2),(b,w/3),(t,w/2); a/b targets have none.
Each inverse has every-Borel IMAGE factor respectively 1/2,1/3,1/2 for
counting times Lebesgue. These are their all-point versions, giving clocks
L on a,t and log3 on b. The parent is total but not onto the full three-label X.
For n>=1 its exact iterate and clock sum are

    T^n(sigma,x)=(t,2^n beta_sigma x),
    S_n(sigma,x)=nL+eta_sigma;  S_0=0.                            (10)

Every length-n inverse history into (t,w), n>=1, ends at exactly one of
(a,w/2^n), (b,w/(3*2^(n-1))), (t,w/2^n). Backwards, the word stays in t
until its last possible switch to a/b, since a/b have no incoming. This
describes all finite inverse words; there is no exponential free-word surplus.

For arbitrary labels sigma,tau the entire groupoid is the exact set

    G_C={((sigma,x),k,(tau,y)): beta_tau y=2^k beta_sigma x},
    c_C=kL+eta_sigma-eta_tau.                                   (11)

Necessity follows from (10) after extending a meeting to positive depths.
Conversely any displayed relation has a presentation with m,n>=1, m-n=k,
using (10). Thus it includes units, all zero-depth presentations and every
integer lag, not only arrows entering t in a preferred way. Its full-label
transport y->x has IMAGE factor (beta_tau/beta_sigma)2^(-k)=exp(-c_C),
again with the actual counting-times-Lebesgue measures.

The complete kernels can now be simplified, not merely sampled:

    M_C={((sigma,x),0,(tau,y)): beta_tau y=beta_sigma x},
    K_C={((sigma,x),0,(tau,x)): sigma,tau both in {a,t}
                                         OR sigma=tau=b},
    K_C intersect M_C=K_C.                                     (12)

Indeed c=0 requires 2^k beta_sigma=beta_tau; no ratio 3/2 or2/3 is an integer
power of2, so k=0 and the indicated equal-beta labels are exhaustive. Then
(11) forces y=x. In particular K has nonunit a/t arrows, whereas M also has
a/b arrows with rescaled x and nonzero clock. No kernel is silently discarded.

The sole periodic core is (t,0), a fixed point. Its entire finite-entry basin
is {(a,0),(b,0),(t,0)}. At EVERY one of these points source isotropy is Z,
c on a loop k is kL, H=LZ and extension isotropy0. There is exactly one
positive parent packet, primitive log2, all repetitions n log2 and phases
[h-eta_sigma] modulo L. Strictly preperiodic a0/b0 retain the whole source
isotropy; lack of a forward return to their own vertex does not remove it.

All other components have a nonzero dyadic-class parameter u: they consist
of (sigma,2^n u/beta_sigma), all labels and n in Z. Choosing reference (t,u),
their real phase is h+nL-eta_sigma, by the arrow of lag -n to that reference.
Their source/extension isotropies and H are0, since a nonzero loop would
require 2^k=1. This exhausts every parent point and all its incoming/phases.

## 8. Control C — induced terminals are not the parent restriction

The section B={a,b} times R meets EVERY parent source component just listed,
but misses the sole periodic core (t,0). Every forward step from B goes to t
and all later steps stay there. Thus D_B is empty: R has no legal step and
every B point is an induced terminal. Its inherited rho has empty domain,
not an artificially assigned zero edge value; the only clock sum is S^R_0=0.
There are no first-return inverse words. Induced IMAGE consists only of the
identity/unit transports of the unchanged measure mu_B, not a fabricated branch.

    G_R=K_R=M_R=K_R intersect M_R=all units on B.                 (13)

Every induced source/extension isotropy and H is0. The extended quotient is
B times R itself, one free real-height orbit per B state and NO positive packet.
No parent incoming arrow has been retained under the false name of an R edge.

By contrast, the FULL parent restriction to B is (11) with sigma,tau in {a,b}.
Its clock kernel and its clock/lag intersection are units; its lag kernel
includes every cross-label arrow with beta_tau y=beta_sigma x. At a0 and b0
it retains source isotropy Z and H=LZ, and they are connected, hence still
one parent-restriction packet. At nonzero points it has all the dyadic and
cross-label arrows from (11), with H0 and inherited full real phases.
Phi maps (13) only to units, and is NOT onto that restriction: for example
((a,0),1,(a,0)) is an actual parent loop via depths2 and1, absent from G_R.
The nonunit zero-lag arrow ((a,x),0,(b,2x/3)) is also missing for every x.

PMR fails concretely: x=y=(a,0), k=l=1 meets u=(t,0), which never enters B.
This counterexample proves failure of surjectivity here independently of
merely failing the sufficient hypothesis. Orbit-completeness of B alone
therefore cannot justify replacing the parent's entire return ledger by R's.
The parent has one prime packet and meets the finite necessary benchmark;
the induced owner has empty positive support and FAILS its nonempty condition.
Neither has all-prime coverage. The lost parent packet is explicitly retained
in the full-parent ledger, not declared nonexistent.

## 9. Closure, scope and hold

The prescribed first-return IMAGE and clock are inherited on every point,
including null sections. Phi is an injective clock-preserving morphism, not
an identification of lag conventions; PMR is proved sufficient only. Core
intersections preserve the complete clock group, repetitions and phases.
A shows elapsed-time conservation, B shows an omitted component despite PMR,
and C shows an orbit-full section missing a periodic core and all R returns.
All three controls retain their own full-source measures, inverses, clocks,
kernels, terminals, isotropy, H and heights; no full owner is replaced silently.

This establishes only a conditional ownership tool for a separately admitted
symbolic/geometric source. No lineage, endogenous prime generation, naturalness,
operator or universal no-go is established by these external controls.
Classical NOT APPLICABLE; T3 NOT AUDITED; formal Route UNASSIGNED;
Route B NOT INVOKED. All proof is exact; no cutoff or scientific code is used.
No blocker in the clarified contract was found. Portfolio: complete and stop
this bounded fifth-round audit; any later source/fork needs separate authority.
Freeze this raw file and preserve CP1. HOLD for root's complete raw read and
separately explicit PAPER UNLOCK; no author surface may be read beforehand.

EOF — card-only independent raw; AI-assisted, shared-history NOT_CALIBRATED.
