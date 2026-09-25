# 395 — Independent original-card mathematical audit

Candidate `ANG-20260922-SCR01`; batch `GEOMETRIC-FEEDBACK-20260922-J`, round 1/5.
Scientific input: card lines 1–93, read completely, SHA-256 `d2c74a3fda2d7cc57840bb66a7d367d8dd5852643254a721facb19dbb899d606`.
Original 79-line prefix: `48dd251e02a9249cc40c952a7f2f339fc883d731f19cf5ad0693b0082e5399c9`.
Scope report: 91 lines, SHA-256 `0e2906202b6fff3d0e03ef0f834a97f9951333ef33951877cc4ed8de43d319dd`.
CP1's missing target was explicitly clarified and accepted before root separately released this mathematical stage.
No manuscript, peer, scout, old proof or other new scientific output was read; no auxiliary or external source was used.
Conclusion: the full prescribed owner works, but MAIN's first frozen fixed cell has a wrong positive primitive; STOP / FORK.

## 1. Entire branch domains, inverse exhaustiveness and terminal incoming

Write d=gamma(a,b)>=1. For MAIN and R, the exact inverse domain is

    D_ab={(u,v):u,v>=0, du<1, dv<1, a+du>0}.

For D replace d by 1. For S additionally require b+dv>0.
These displayed domains already imply all reconstructed-source and digit checks in the card.
For MAIN, 1/x=a+du and y/x=b+dv; for R, 1/x=a+du and y=b+dv;
for S, 1/x=a+du and 1/y=b+dv. Half-open inequalities recover exactly the indicated floors.
The sources satisfy x>0,y>=0 for MAIN/D/R and x,y>0 for S.
Conversely any legal forward source has its unique digit pair and produces precisely this target domain.
Thus every displayed inverse satisfies both inverse identities and the list is exhaustive.
Different digit pairs cannot duplicate one predecessor because the source's digit pair is unique.
Every cell and inverse domain is Borel. No unit, (0,0)-digit cell, axis or floor cut is removed.

For each of the four owners, the entire forward image is Q=[0,1)^2, not all X.
Containment follows from 0<=du,dv<1 and d>=1. Surjectivity onto Q follows from branch (1,0)
for MAIN/D/R and branch (1,1) for S, all with d=1.
Every target in Q has countably infinitely many distinct predecessors:
use (a,b)=(1,b) for all b>=0 in MAIN/D/R and all b>=1 in S.
Targets outside Q have no predecessor, but remain objects; their own forward map is retained when nonterminal.

For MAIN/D/R the terminal set is {0} times [0,infinity); its incoming portion is {0} times [0,1).
At target (0,v) every inverse has a>=1 and dv<1 (d=1 in D), exactly as the above domains prescribe.
The formulas are (1/a,(b+dv)/a) for MAIN, (1/a,(b+v)/a) for D, and (1/a,b+dv) for R.
For S the terminal set is both axes, with incoming exactly its intersection with Q.
Its same domain formulas apply; at the origin they require a,b>=1 and give ALL (1/a,1/b).
For MAIN/D the origin has ALL predecessors (1/a,b/a), a>=1,b>=0; for R they are (1/a,b).
An outside-Q terminal has only its identity source orbit. No forward iterate beyond any terminal is invented.

## 2. Own every-Borel IMAGE and prescribed full-point clocks

Each rational inverse extends smoothly to the open positive-denominator region around its actual domain.
Factor MAIN's inverse into u->x=1/(a+du) and v->y=x(b+dv).
Their absolute one-dimensional factors are d x² and d x. Repeated substitution and Fubini therefore give
for EVERY Borel E in D_ab, including unbounded-measure cases, mu(theta E)=integral_E J dmu, where

    MAIN: J=d²/(a+du)^3=d²x³;       kappa=-2 log d-3 log x;
    D:    J=1/(a+u)^3=x³;          kappa=-3 log x;
    R:    J=d²/(a+du)^2=d²x²;      kappa=-2 log(dx);
    S:    J=d²/[(a+du)^2(b+dv)^2]=d²x²y²; kappa=-2 log(dxy).

Here (x,y) is the reconstructed source. R has second-coordinate factor d;
S has independent reciprocal factors d x² and d y², proving their OWN laws by the same substitution method.
Restriction to half-open cells, axes or any Borel subset preserves these identities.
All displayed J are strictly positive and finite at EVERY allowed point, including zero target remainders.
No log0 occurs: kappa is evaluated only at legal sources, and S sources have both coordinates positive.
At a terminal only S_0=0 is used; the inverse derivative at that terminal target is still defined as prescribed.
These boundary values are fixed by the card's rational-extension prescription, not by a.e. uniqueness.
The clock is not asserted globally positive: unbounded source strata can have negative kappa.
Neither global measure invariance nor a continuous/etale owner follows from these branchwise identities.

## 3. All finite histories and exact global kernels

A finite word p of digit pairs denotes I_p=theta_(p_0)...theta_(p_(m-1)).
Its full domain consists of targets for which EVERY successive reverse reconstruction satisfies its own D_ab.
This recursive finite list of explicit inequalities is Borel and is both necessary and sufficient.
Empty p has I_p=id and J_p=1. All incoming histories are retained, not just words continuing indefinitely forward.
Change of variables along the finite chain gives J_p as the product of the displayed pointwise factors.
For every Borel common-tail set, replacement I_q(t)->I_p(t) has IMAGE J_p(t)/J_q(t).

For explicit full kernel descriptions, put delta_p=product of d along p; in D use d=1 throughout.
MAIN and D have projective inverse matrices

    B_ab=[[0,0,1],[0,d,b],[d,0,a]],    det B_ab=-d².

For B_p=product B_ab let Lambda_p(u,v) be its bottom row applied to (u,v,1).
It is the product of the successive positive denominators, so J_p=delta_p²/Lambda_p³ on the entire actual domain.
For R use C_ad=[[0,1],[d,a]] on the first coordinate; its product denominator is Lambda_p(u).
The second coordinate is an affine map of slope delta_p, so J_p=delta_p²/Lambda_p².
For S use the products of C_ad and C_bd with denominators Lambda_p^x(u), Lambda_p^y(v);
then J_p=delta_p²/(Lambda_p^x Lambda_p^y)². Empty-word denominators are 1.
These are actual product matrices, not freely renormalized projective representatives.

On the actual arrow (I_p(t),|p|-|q|,I_q(t)), the cocycle is

    c=-log J_p(t)+log J_q(t).

Consequently the ENTIRE clock kernel is exactly the following sets of actual arrows on full common domains:

    MAIN/D: delta_p² Lambda_q³ = delta_q² Lambda_p³;
    R:      delta_p Lambda_q = delta_q Lambda_p;
    S:      delta_p Lambda_q^x Lambda_q^y = delta_q Lambda_p^x Lambda_p^y.

The ENTIRE lag kernel has |p|=|q| alone, without imposing these clock equalities.
The intersection imposes both conditions. Taking all finite p,q is an exact global description, not a finite sample.
In general the clock kernel and its lag intersection contain nonunit arrows.
For MAIN/D/R, theta_10(t) and theta_11(t) are distinct for every t in Q but have equal J and equal prefix length.
For S, theta_12(t,t) and theta_21(t,t), 0<=t<1, likewise give distinct endpoints with the same J.
Thus full arrow kernels must not be confused with the trivial extension isotropy proved below.

## 4. Actual partial tails, all isotropy and complete physical phases

The forward rule is deterministic on its declared domain. Any two presentations of the same triple have
equal changes in both iterate counts; the longer valid presentation pads both sides along the same actual tail.
The common added sums cancel, including when the common tail terminates (then no longer padding is legal).
Aligning the middle histories proves composition, and reversal changes the sign.
These arguments use the prescribed actual step at each cut, not equality of derivatives inferred on a null intersection.
Finite Borel branch-pair charts therefore give the full retained-lag Borel groupoid and cocycle.
An inverse arrow Tz->z has c=kappa(z); the forward arrow z->Tz has c=-kappa(z).
All extension arrows (w,h)->(z,h+c) are retained. Height translation commutes with them for EVERY real time.
It thus defines a complete action on the orbit SET, without a nice coarse topology or positive-roof assertion.

For ANY deterministic partial source here, nonzero isotropy is equivalent to an eventually periodic forward orbit.
If its least eventual source period is q, the entire source isotropy is qZ; otherwise it is {0}.
Terminating histories fall in the latter class, not in a fixed-point class.
For any actual least-q core p, let L=sum_(i<q)kappa(T^i p).
Transient terms cancel, so at every ancestor c(kq)=kL and H=L Z.

In fact L>0 for EVERY actual cycle in each owner, by a short image/domain argument, not a cycle census.
Every state of an actual cycle lies in Q. In MAIN/D/R its x is in (0,1) and a>=1.
For MAIN/R, d<=a and a x<=1; a zero first remainder would hit a terminal, so on cycles d x<1.
Hence MAIN's J=(dx)²x<1, D's J=x³<1 and R's J=(dx)²<1 along a cycle.
For S a cycle state has x,y in (0,1), a,b>=1 and d<=a,b; in particular dxy<=a x y<=y<1.
Its J=(dxy)²<1 as well. Every cycle sum is therefore strictly positive.
It follows that source-isotropy clock kernels and extension isotropy are trivial at ALL objects.
Every eventual core gives a genuine positive primitive L and repetitions kL; other sources have H={0}.
This conditional full ledger does not enumerate which higher cycles exist.

For any reference x, its complete source orbit is

    O_x={I_p(T^n x): n is a valid forward depth, p is any legal finite inverse word there}.

This gives every finite incoming history, including every terminal basin, with only actual triples retained.
It is countable. If T^r z=T^n x, the arrow z->x has c=S_n(x)-S_r(z).
Thus the phase of (z,h) is h+S_n(x)-S_r(z) modulo H_x; equality of phases is also sufficient for equivalence.
The quotient over O_x is R/H_x: a circle for an eventual core, a line otherwise.
For a fixed core p the full basin is union_(r>=0) T^(-r){p}, with all inverse words as above,
and phase h-S_r(z) mod L whenever T^r z=p. Each such basin is countably infinite by Section 1.
Distinct fixed cores cannot merge: every forward image of either core is itself.
Their complete incoming basins are disjoint, even when their times agree or are integer multiples.

## 5. Complete fixed sets in all four frozen cells

Set phi=(1+sqrt5)/2, alpha=1/phi=(sqrt5-1)/2,
beta=(sqrt3-1)/2, chi=(sqrt6-2)/2 and xi=sqrt5-2.
The exact fixed sets are:

| Digit cell | MAIN | D | R | S |
| --- | --- | --- | --- | --- |
| (1,0) | {(alpha,0)} | {(alpha,0)} | {alpha} times [0,1) | empty |
| (1,1) | empty | empty | empty | {(alpha,alpha)} |
| (2,2) | empty | empty | empty | {(beta,beta)} |
| (4,2) | empty | {(xi,alpha)} | empty | {(chi,beta)} |

Here is exhaustion including the half-open boundary checks, not just substitution of listed points.
MAIN fixedness on a cell requires d x²+a x=1 and (1-dx)y=b x.
The positive x root is unique; legal fixedness additionally requires dx<1 and dy<1.
The four x roots are alpha, alpha, beta, chi. Their y candidates are respectively
0, phi, 1+sqrt3, sqrt6/3. The last three fail dy<1; the first passes.
For D put d=1 in those equations: the x roots are alpha, alpha, sqrt2-1, xi;
the respective y values are 0, phi, sqrt2, alpha. Exactly the first and last satisfy y<1.
There is no missing free-y branch: dx=1 is forbidden by the fixed target's strict first-remainder inequality.

For R, the first fixed equation is again d x²+a x=1, while (d-1)y=-b.
At (1,0), d=1 and the equation imposes no extra condition; its exact own digit cell is 0<=y<1.
At (1,1) the equation is inconsistent; at (2,2) and (4,2) it requires y=-2, outside X.
For S, both coordinates are positive and solve d x²+a x=1 and d y²+b y=1 uniquely.
At (1,0), y=1 gives dy=1, excluded by the strict upper remainder bound and the claimed b=0 digit.
The other three rows give the listed positive roots and satisfy BOTH dx<1 and dy<1.
S's terminal axes are never added as fixed states; MAIN/D/R's permitted y=0 fixed point is not discarded.

## 6. Entire stabilizers, primitive lengths and nonmerging of these sets

Every listed point is an actual fixed core, so its least source period is 1, source isotropy Z,
H=L Z and extension isotropy {0}. Section 4 supplies its ENTIRE incoming basin and all real phases.
The exact positive generators are:

    MAIN (alpha,0):       L=3 log phi=log(2+sqrt5);
    D (alpha,0):          L=3 log phi;
    D (xi,alpha):         L=3 log(2+sqrt5)=9 log phi;
    R (alpha,y),0<=y<1:   L=2 log phi=log((3+sqrt5)/2);
    S (alpha,alpha):      L=4 log phi=log((7+3sqrt5)/2);
    S (beta,beta):        L=2 log(2+sqrt3)=log(7+4sqrt3);
    S (chi,beta):         L=2 log((2+sqrt6)(1+sqrt3)/2).

The final S exponential is 10+5sqrt3+4sqrt6+6sqrt2, irrational:
in Q(sqrt2,sqrt3), changing the sign of sqrt2 fixes the rational numbers and changes this value by a nonzero amount.
The other displayed exponentials are visibly irrational quadratic numbers; for D's second core it is 38+17sqrt5.
Thus all displayed generators fail the ordinary-integer-prime length diagnostic on their OWN controls.
The D42 primitive is three times D10's primitive, but belongs to another fixed core and is NOT its repetition packet.
R gives continuum many distinct equal-length packets: distinct y define distinct fixed states and disjoint basins.
Since that common length is not log of an ordinary prime, this is not separately presented as a per-prime multiplicity counterexample.
No R, D or S conclusion is substituted for MAIN's result.

## 7. Lineage, decisive target and scope

For the original integer interface, substitution of x=1/(n+rho), y=(m+eta)/(n+rho)
with 0<=rho,eta<1 gives exactly a=n,b=m, d=gcd(n,m), T=(rho/d,eta/d).
The proper-divisor condition m|n is exactly d=m; content affects both new coordinates and their later digit tests.
This establishes the stated concrete interface, not a novelty claim or a naturally unique design.

MAIN's retained y=0 fixed point in the FIRST frozen cell already has the entire primitive log(2+sqrt5).
Its exponential is not an integer, so the necessary target fails without a prime table, rescaling or higher-cycle search.
Its Lebesgue-null location does not excuse removal: the full carrier and rational-extension all-point clock were frozen explicitly.
The complete remaining precommitted cells and own controls were checked; no additional fixed-cell or higher-period census was started.
The positivity argument for arbitrary cycles is only the short general ledger identity required to determine extension isotropy.
Higher-cycle existence, coverage, full arithmetic multiplicity, strong naturalness and analytic owners remain unaudited beyond the stated results.
No smooth/etale quotient, invariant probability, universal real-map obstruction or repaired clock is claimed.
Classical NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; Route B NOT INVOKED.

The retained ARS three-checkpoint and same-owner rules govern this derivation; CP2/CP3 await separate manuscript unlock.
This is inherited-model/shared-history NOT_CALIBRATED internal work, not blind or external peer review.
No web, auxiliary, scientific numerical experiment, model change, old result transfer or other-file write was used.
The original and clarified cards and the CP1 report are preserved. Freeze this raw before author-manuscript access.
EOF — full prescribed Borel owner established; bounded necessary-target STOP / FORK.
