# DRC02 — card-only independent derivation

## 1. Authority, inputs and exposure

Candidate `ANG-20260923-DRC02`; Paper 442; batch `ADMISSION-CLOCK-20260923-S`, round 3/5.
Root separately released raw mathematics after fully reading the 66-line CP1 report.
Sole scientific input: `candidate-card.md`, original full 104 lines, SHA256 `e647f39374bfa5c4cc7b94cc0708ce41203f8a831d92c4859dbac37c175ac7d8`.
The full card was reread after release. Frozen `scope-review.md`: 66 lines, SHA256 `c9994c5e334682f0b9b7c76ab0e681f60b56c481994f08b0bb7d074e3ab7439d`.
No author paper, README, ledger, current outcome, peer report, helper result or older scientific proof was read.
Retained stream/ARS instructions and shared history remain disclosed. This is same-inherited-model internal review, `NOT_CALIBRATED`, not blind or human/external peer review.
Only this raw file is written. All arguments below are exact algebra, change of variables and actual partial histories; no scientific numerical code, network, Git, PDF, auxiliary agent or higher-period census is used.

## 2. Full partial maps and complete inverse atlas

Every owner has the complete object set X=R2 and original Lebesgue measure. Write `rho=x^2+y^2`, `s=1+rho`, `c0=(1,-1)`.
For MAIN/N, `n=abs(floor x)`, `d=abs(floor y)`; permission A is `n,d>=1` and `d|n`, with `q=n/d`.
MAIN uses `F=c0+diag(d,q) z/s` on A with rho!=1. G uses the same radial law with d=q=1 on rho!=1, without any arithmetic guard.
N uses `F_N=c0+diag(d,q) z` on A, without inheriting the radial critical-circle exclusion.
The displayed coefficients are read at the original source and fixed throughout its step; every later step recomputes its own readout.
Every point outside an owner's forward domain remains a terminal object, with its unit and all actual incoming. A target need not have a next step.

First solve a fixed-label radial map, independently of arithmetic admission. For target `(X,Y)` let `a=(X-1)/d`, `b=(Y+1)/q`, `t=a^2+b^2`.
Any source has `z=s(a,b)` and `t=rho/(1+rho)^2`; equivalently, for lambda=s, `t lambda^2-lambda+1=0`.
For `0<t<1/4` the two solutions are exactly
`lambda_in=2/(1+sqrt(1-4t))`, `lambda_out=2/(1-sqrt(1-4t))`.
They give distinct actual points: `1<lambda_in<2<lambda_out`, hence respectively rho<1 and rho>1.
Conversely each solution satisfies `lambda=1+lambda^2 t`, so substitution gives the exact forward identity and its asserted radius.
At t=0, the equation `z/(1+rho)=0` forces z=0; only lambda_in=1 is finite. There is no outer source or added infinity.
At t=1/4 both algebraic roots give lambda=2 and rho=1, excluded from the radial forward domain. At t>1/4 there is no real source.
These cases exhaust all targets, since t is nonnegative and every source supplies the equation above.

The inner map is a real-analytic diffeomorphism from rho<1 onto the open scaled target ellipse t<1/4, including t=0.
Indeed its displayed inverse is analytic there, with a nonzero denominator at t=0; its derivative at that target is `diag(1/d,1/q)`.
The outer map is an analytic diffeomorphism from rho>1 onto `0<t<1/4`, with the displayed outer inverse. It has no finite extension as t tends to zero.
Both statements follow from the inverse identities and the nonvanishing derivatives computed below, not from a presumed global injectivity across the two sheets.
MAIN now retains, for EVERY positive integer pair `(d,q)`, each reconstructed point satisfying exactly `abs(floor x)=dq`, `abs(floor y)=d`, its own rho!=1 condition and forward identity.
These actual domains are Borel: the inverse functions are analytic on their open sheet domains and floor/readout conditions are Borel.
Conversely every legal MAIN source has its unique pair `(d,q)` and its unique inner/outer radius, and is recovered by that branch. This proves all-label/all-sheet exhaustion.
At t=0 every MAIN label reconstructs the inadmissible origin, so no MAIN predecessor is silently supplied there.
G instead retains the same two radial sheets with its sole pair `(1,1)` and no arithmetic test. Its inner t=0 source IS the legal origin.
Distinct sheets cannot coincide away from the excluded critical radius. Different admitted arithmetic labels cannot encode the same source because its readout is unique.

For N and each positive integer pair `(d,q)`, the inverse is `((X-1)/d,(Y+1)/q)`.
This is a global affine inverse for the fixed pair; restrict it only to the Borel target set with the required reconstructed `n=dq,d`.
Every N legal source is recovered uniquely by its own pair, including any arithmetically permitted critical-circle source. No radial check is imported.
There is no index or inverse-depth cutoff for MAIN/N, and no redundant arithmetic labels for G. Branch failure never creates or removes an object.

## 3. Full two-dimensional IMAGE and prescribed all-point clocks

For a fixed radial label the complete derivative in the original x,y coordinates is

```text
        1/s^2 [ d(1-x^2+y^2)       -2dxy       ]
              [    -2qxy       q(1+x^2-y^2)  ].
```

Its determinant is `dq*(1-rho)/s^3`: the numerator determinant before division by s^4 is `dq*(1-rho)*(1+rho)`.
Thus on each actual MAIN inverse sheet
`J=s^3/[dq*abs(1-rho)]`, evaluated at the reconstructed source.
For G the own formula is `J_G=s^3/abs(1-rho)`. For N the full forward derivative is `diag(d,q)`, and the own inverse J is `1/(dq)`.
All these values are finite and strictly positive at EVERY admitted branch point. The radial critical sources are not assigned an infinite or zero next-step clock.
The inner analytic germ at t=0 yields exactly `J=1/(dq)`; for G this is J=1. This is a genuine germ value, not an isolated density repair.
Assigned integer cuts use the fixed-label/fixed-sheet germ, not a derivative of floor. Neither MAIN nor N is asserted globally smooth or globally injective.
For any Borel E in one actual inverse domain, ordinary R2 change of variables on the encompassing sheet diffeomorphism (or N affine inverse) gives
`mu(theta(E))=integral_E J dmu`.
This covers arbitrary Borel subsets, including null cut sets and infinite measures. Countably many domains cover every actual source; no changed density or atomic floor factor is used.
Target domains can overlap with distinct predecessors. Their individual IMAGE identities do not become one multiplicity-free Jacobian for the union map.
The own forward IMAGE factors and signed clocks on LEGAL sources are
`K_MAIN=n*abs(1-rho)/(1+rho)^3`, `K_G=abs(1-rho)/(1+rho)^3`, `K_N=n`, and `kappa=log K=-log J_actual(Fz)`.
The formulas use the original-source labels, and terminal objects have no next-step kappa.

G has K=1 exactly at its regular origin and 0<K<1 at every other legal source.
MAIN has 0<K<1 at every legal source: for rho<1, legality forces n=1; for radius r>=1, `n<=r+1<=1+r^2`, giving `K<1` away from the excluded circle.
N has kappa=log n>=0, zero precisely on its legal n=1 states. This is its OWN affine measure law, not the radial clock with a missing term.
These sign statements do not assert existence or exhaustion of cycles. No signed step clock is relabelled as a positive suspension roof.

## 4. All legal histories, kernels and physical returns

For each owner O, let D_0=X and D_j be the states with j legal steps; F^0 is the identity even at terminals.
On D_j put `P_j(z)=product_{i<j} K(F^i z)`, `S_j(z)=log P_j(z)`, with P_0=1 and S_0=0.
Use exactly `G_O={(z,r-s,w):z in D_r,w in D_s,F^r z=F^s w}`, identifying equal triples, with source w and range z.
This is a countable Borel groupoid: the legal meeting loci are Borel, and each forward target has countably many actual predecessors under every finite inverse depth.
For equal triples, two witnessing pairs differ by the same integer shift. Extend the shorter pair only to the longer LEGAL pair; after their common meeting both sides traverse the same existing segment.
The extra sums cancel, proving well-defined `c=S_r(z)-S_s(w)`. In a composition, align the middle histories at their larger legal time; equality transfers the existing middle segment to the other side.
This proves actual composition and cocycle additivity without continuing a terminal illegally. Inversion negates c, and `(Fz,-1,z)` has `c=-kappa(z)`.
On every fixed-history bisection, repeated change of variables gives IMAGE factor `P_s(w)/P_r(z)=exp(-c)` from source w to range z.

The COMPLETE kernels, always restricted to actual legal meetings, are:
`ker lag = {(z,0,w):F^r z=F^r w legally for some r}`;
`ker c = {(z,r-s,w):F^r z=F^s w legally and P_r(z)=P_s(w)}`;
`ker lag intersect ker c = {(z,0,w):F^r z=F^r w legally and P_r(z)=P_r(w) for some r}`.
These include non-loop arrows. Product equality alone supplies no meeting, and zero lag does not mean equal sources in a noninjective owner.
Inverse domains and clocks in these formulas are always those of the same O; N does not inherit G's or MAIN's exclusions.

Nonzero source isotropy exists exactly at states with an actual eventually periodic full-state future.
An unequal repeated legal iterate gives a finite cycle all of whose steps are legal forever; conversely an eventual cycle supplies repeated iterates.
For its least period k and whole signed cycle sum C, source isotropy has lag group kZ, `c(jk)=jC`, and ENTIRE `H_z=CZ`.
Minimal period gives the lag group and cancellation of the transient prefix gives the clock image; neither a selected loop nor a selected subgroup is used.
A terminating or infinite non-eventually-periodic state has only unit source isotropy and H={0}.
For the full extension `(w,h)->(z,h+c)`, isotropy is the source-isotropy c-kernel: kZ if C=0 and only units if C!=0; the non-eventual cases have only units.
Physical height-translation stabilizer on the orbit SET is exactly H, because returning to the same extension orbit over a source uses a source-isotropy arrow.
Only C!=0 gives a least positive primitive `L=abs(C)` and repetitions mL for positive integers m. C=0 leaves no positive return, even if ineffective source isotropy remains.
This is a set-level construction only; no Hausdorff quotient, selected section, invariant physical measure or symplectic structure is assumed.

Define `Pred_0(p)={p}` and `Pred_{j+1}(p)` as ALL passing actual own inverse sheets/labels over `Pred_j(p)`.
For any source z its complete component is `union_{s legal at z} union_{r>=0} Pred_r(F^s z)`.
For a periodic core point p this equals `union_r Pred_r(p)`; every legal incoming tree is included, and every node recomputes its own readout.
If `F^a z=F^b p`, the transported height phase is `h+S_b(p)-S_a(z) mod H_p`. Different witnesses differ by the entire H_p.
For a non-eventual reference source the same formula has H=0 and yields a real phase, not a zero-period primitive.

In particular every terminating component has one terminal p. Let tau(z) be its exact number of steps to p and `B(z)=S_{tau(z)}(z)`, with tau(p)=B(p)=0.
Its arrows are exactly `(z,tau(z)-tau(w),w)`, with `c=B(z)-B(w)`; earlier meetings give the same lag and sum by cancellation.
Thus terminal-component lag, clock and joint kernels are respectively equality of tau, equality of B, and both equalities. Its complete physical phase is `h-B(z)` in R.
This retains every incoming into critical or arithmetically forbidden objects while assigning those terminal objects no outgoing step and no artificial loop.

## 5. GLOBAL fixed-set exhaustion for MAIN

The following bound holds for EVERY legal source, without a finite window or a sign restriction.
Put A=abs(x), B=abs(y). The signed-floor convention gives `d<=B+1`.
Since `2AB<=A^2+B^2` and `2A<=A^2+1`,
`A(B+1)<=A^2+(B^2+1)/2 < 1+A^2+B^2`.
Consequently `abs(d*x/(1+rho))<1`, so the first MAIN output always lies STRICTLY between 0 and 2.
At any legal fixed point this forces `0<x<2` and n>=1, hence `1<=x<2` and n=1. Divisibility then forces d=q=1.
Now the fixed y equation is `y=-1+y/s`, so `y=-s/(s-1)<-1`, since x>=1 gives s>1.
But then `abs(floor y)>=2`, contradicting the already forced d=1.
Therefore `Fix(MAIN)=empty` on the complete real plane, including all integer boundaries and negative-source alternatives; terminal objects are not absorbing fixed points.
This is a fixed-set exhaustion, not a classification of higher periods. No global absence of positive returns is inferred from it.
There are consequently no MAIN fixed cores for which a fixed-core basin/H could be listed; all other actual incoming and possible eventual-cycle ledgers remain exactly §4.

## 6. GLOBAL fixed-set exhaustion for N

The N fixed x equation is `(1-d)x=1`. For d=1 it is impossible; for d>=2 it forces `x=-1/(d-1)` in [-1,0).
Every such x has `abs(floor x)=1`, including the boundary x=-1, contradicting d>=2 and d|n.
Thus `Fix(N)=empty` globally, with no assumption about y or removal of the critical circle.
The contradiction precedes any restriction to a chosen positive cell or centre. Terminal N points do not become fixed by definition.
This own-control fixed-set result and its affine clock do not supply MAIN's result. No N higher-period classification or global positive-ledger conclusion is asserted.

## 7. G: unique global fixed core, its entire incoming and clock

At a G fixed point, `(s-1)x=s` and `(s-1)y=-s`. The origin is not fixed, so s>1, x=-y=a>1.
Substitution gives `f(a)=2a^3-2a^2-1=0`. Conversely every a>1 solving this equation gives a fixed point.
On a>1, `f'(a)=2a(3a-2)>0`; `f(5/4)=-7/32<0`, `f(4/3)=5/27>0`.
Hence there is exactly one such a, specified algebraically with `5/4<a<4/3`. Its rho=2a^2>1, so it passes G's own domain.
Therefore the COMPLETE global G fixed set is the single point `p=(a,-a)`; no arithmetic condition is imposed on it.

Write `R=2a^2` and `b=p/R=(1/(2a),-1/(2a))`.
The radial identity `z/(1+|z|^2)=(z/|z|^2)/(1+1/|z|^2)` shows that p and b have the same G image p.
They are exactly the two sheet inverses of p, since R>1 and |b|^2=1/R<1. Both are legal and distinct.
The full G image is the open disk `|z-c0|<1/2`: this follows from the proved radial inverse coverage, with the centre supplied by the inner origin.
But `|b-c0|^2=2(1-1/(2a))^2>1/2>1/4` because a>1. Thus b has NO predecessor under G.
It follows inductively that every positive-depth predecessor set of p is exactly `{p,b}`, and its full source component/basin is exactly `{p,b}`.
No omitted terminal, other radial sheet or deeper incoming can enlarge this component. This is exact basin exhaustion, not a finite search.

At p, the signed core sum and primitive are
`C=kappa_G(p)=log[(R-1)/(1+R)^3]<0`, `L=-C=log[(1+R)^3/(R-1)]>0`.
Both p and b have source isotropy Z and ENTIRE H=LZ, by eventual-period-one prefix cancellation; their extension isotropy is trivial.
At b, the own clock is `kappa_G(b)=C+2 log R`, because its absolute forward Jacobian is R^2 times the absolute forward Jacobian at p; their signed determinants have opposite signs.
Thus phase at p is h mod LZ for p, and `h-kappa_G(b)=h-2 log R mod LZ` for b. Every real phase remains; b is an incoming point, not a second physical packet.
There is exactly ONE fixed-core source packet for G and one physical circle at that primitive, with repetitions mL. No claim about other G periodic cores is made.

For completeness within this two-point component, let delta=2 log R. Since R>1 and G's determinant at b is strictly below 1, `0<delta<L`.
All arrows between either ordered pair have every integer lag ell. On p->p or b->b their clock is ell*C; on b->p it is ell*C-delta; on p->b it is ell*C+delta.
The latter signs follow directly from a one-step prefix at b; in particular its forward arrow has lag -1 and clock `-kappa_G(b)`.
Hence the clock kernel restricted to this basin consists only of units; its lag kernel has all four zero-lag ordered-pair arrows, and its joint kernel has only units.

The G primitive is not log of an ordinary integer, although this is only a control fact.
The cubic for a is irreducible over Q: its only rational-root candidates are ±1 and ±1/2, none of which is a root.
Reduction by `a^3=a^2+1/2` gives `(1+2a^2)^3=34a^2+10a+13`.
If `J_p=(1+2a^2)^3/(2a^2-1)` were rational m, a would satisfy `(34-2m)a^2+10a+(13+m)=0`, a nonzero polynomial of degree at most two.
That contradicts the cubic degree. Therefore J_p is irrational and L=log J_p is not log of an ordinary prime. This control failure is not transferred to MAIN.

## 8. Bounded disposition and freeze boundary

All three owners have proved complete actual inverse atlases, positive finite prescribed full-R2 branch IMAGE, legal-history cocycles and exact general kernels/H/phase descriptions.
MAIN's and N's GLOBAL fixed sets are empty; G's is the unique algebraic point above with its complete two-point incoming component and exact entire clock group.
The full states, critical/other terminal objects, null floor faces, both actual sheets and all arithmetic labels are retained; no clock, measure or source repair was used.
The frozen fixed gate yields no positive MAIN fixed core and no decisive MAIN prime-time counterexample. MAIN higher periods and its global positive packet ledger remain OPEN in this bounded audit.
Disposition: `OWNED TWO-SHEET RADIAL IMAGE; GLOBAL FIXED SET EMPTY — BOUNDED OPEN / FORK` for MAIN, not a global no-return theorem and not an arithmetic success.
G's positive non-integer fixed multiplier and N's empty fixed set are separately owned control results; neither converts MAIN's bounded OPEN into a global failure theorem.
Naturalness and PROVES_TOO_MUCH remain OPEN; arithmetic T1 NOT PASSED; T3 NOT AUDITED; classical NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.
No higher-period census, manual prime fitting, selected fibre, altered critical guard or new candidate is pursued. ARS constrains scope/disclosure, not mathematical certification.
After full self-read and measured freeze, report only RAW READY and HOLD for root's full raw read and a DISTINCT PAPER UNLOCK; no author or peer result has informed this file.

EOF — DRC02 card-only raw; complete global fixed sets, complete inverse ownership and bounded MAIN OPEN / FORK.
