# RAE01 — card-only independent admission-exit derivation

## 1. Authority and exposed inputs

Audit `ANG-AUDIT-20260924-RAE01`, Paper 445, concerns the EXACT unchanged `ANG-20260923-DRC02` owner.
Root separately released raw mathematics after fully reading CP1. Sole scientific file read for this raw: the full 89-line card, reread after release, SHA256 `272374c01e2576df1e0c274c353b11d9cb47d87c895d2adad7723b0ff7b8d0ad`.
Frozen CP1 `scope-review.md`: 71 lines, SHA256 `983bf5da78bd90036eeacbef8f878eb68b498c5e19255857a3379cf2a21547fc`.
Prior 442 card/raw/final-manuscript review and mathematical context are retained and disclosed; this is not a fresh blind discovery or sealed prediction. The arguments needed here are re-established from the present full definitions.
No current author paper, README, ledger, helper answer, peer result or other scientific file was read. No old file is changed.
Inherited-model shared-history internal review is `NOT_CALIBRATED`, not external/human/cross-model verification. Retained fully read ARS/stream instructions govern scope and disclosure, not validity certification.
Only this raw is written with apply_patch. No scientific numerical code, network, Git, PDF, auxiliary agent, enlarged gate or new candidate is used.

## 2. Exact full owners and both inverse sheets

All three object spaces are the entire real plane with original Lebesgue measure. Write `R=x^2+y^2`, `s=1+R`, `n=abs(floor x)`, `d=abs(floor y)`.
On `A={n,d>=1,d|n}`, put q=n/d. MAIN is `T=(1+d*x/s,-1+q*y/s)` on `D=A intersect {R!=1}`.
G is the same radial formula with constant d=q=1 on R!=1 and no arithmetic guard. N is `(1+d*x,-1+q*y)` on A alone, with no critical-circle restriction.
Labels are read once at the original source of each step; later geometry supplies the next labels. Every outside-domain point remains a terminal object with units and all incoming, not an absorbing loop.

For fixed radial labels and target (X,Y), put `a=(X-1)/d`, `b=(Y+1)/q`, `t=a^2+b^2`.
A source satisfies `z=lambda*(a,b)`, lambda=1+R, and `t*lambda^2-lambda+1=0`.
For 0<t<1/4 its two roots are exactly the frozen
`lambda_in=2/(1+sqrt(1-4t))`, `lambda_out=2/(1-sqrt(1-4t))`.
They satisfy `1<lambda_in<2<lambda_out`, so the sources respectively have R<1 and R>1 and are distinct.
Conversely the quadratic identity makes `1+|lambda*(a,b)|^2=lambda`, proving forward substitution and both inverse identities.
At t=0 the vector equation forces the sole finite source z=0; the inner formula has lambda=1. There is no outer infinity.
At t=1/4 the sole reconstruction has R=1 and is not radial-legal. For t>1/4 there is no real source; these exhaust all possible nonnegative t.
The inner inverse is analytic on the full target ellipse t<1/4, including t=0, with derivative `diag(1/d,1/q)` there. The outer inverse is analytic on 0<t<1/4 only.
Thus each fixed-label forward radial map is a diffeomorphism from the open unit disk or its exterior onto that ellipse or its punctured version, respectively.
MAIN admits each of ALL positive (d,q) reconstructions exactly when the original-source floors are n=dq,d and its own guard holds. These actual domains are Borel restrictions of the analytic sheets.
Every legal source supplies its unique label and radius sheet; hence the atlas is complete without a label cutoff. Distinct actual predecessors are retained, while equal actual points are not multiplied by labels.
In particular MAIN rejects the t=0 origin by arithmetic admission. G instead uses only d=q=1 with both own radial sheets, and retains its regular origin.
For N, ALL positive labels give the affine inverse `((X-1)/d,(Y+1)/q)`, restricted only by its own reconstructed floors. Fixed-label affine substitution proves both identities and complete coverage.
No radial condition is added to N; its allowed circle points remain. For every owner an inverse may land at a source whose target has no further step.

## 3. Full planar IMAGE, every Borel set and all-point versions

For the fixed-label radial smooth germ, with B=diag(d,q),
`D T=B*((1+R)I-2zz^T)/(1+R)^2`, and `det_R2 D T=dq*(1-R)/(1+R)^3`.
Indeed the radial/tangential eigenvalues of the middle radial derivative are `(1-R)/(1+R)^2` and `1/(1+R)`; its matrix at zero gives the same determinant.
This is the full planar determinant, including both off-diagonal entries; multiplying by B contributes dq, not a guessed radial weight.
At the reconstructed actual source, the prescribed inverse densities are
`J_MAIN=(1+R)^3/[dq*abs(1-R)]`, `J_G=(1+R)^3/abs(1-R)`, `J_N=1/(dq)`.
They are positive and finite at EVERY actual branch point. On the inner t=0 germ the value is 1/(dq), and G has J=1 there.
At floor cuts the fixed-label/sheet analytic germ is used, not a derivative of floor or an arbitrary a.e. value. The excluded radial critical source receives no next-step density/clock.
Ordinary change of variables on each full sheet diffeomorphism, then restriction to any Borel actual target subset E, proves `mu(theta E)=integral_E J dmu`.
The affine N argument is identical with its own determinant. Infinite measure and null cut sets are covered; no altered measure, atomic label factor or selected branch is inserted.
Targets may have several distinct predecessors; the branch laws are not combined into a multiplicity-free union Jacobian.
Write K=1/J_actual(Tz). On legal steps the OWN factors and clocks are
`K_MAIN=n*abs(1-R)/(1+R)^3`, `K_G=abs(1-R)/(1+R)^3`, `K_N=n`, and `kappa=log K`.
Terminals have no next-step kappa. G's clock is zero at the origin only, and negative at every other legal source. N's is zero exactly on legal n=1 states.
MAIN's clock is strictly negative at every legal source: if R<1, legality forces n=1; if r=sqrt(R)>=1, `n<=r+1<=1+r^2`, hence `K_MAIN<1` off the excluded circle.
This sign statement neither replaces the clock by zero nor asserts existence of any cycle.

## 4. General actual histories for EACH owner

Let D_O^(j) be the points with j legal steps, with D_O^(0)=X. Set `P_j(z)=product_{i<j}K_O(T_O^i z)`, `S_j=log P_j`, P_0=1, S_0=0.
Use exactly `G_O={(z,r-s,w):T_O^r z=T_O^s w legally}`, source w, range z, with equal actual triples identified and integer lag retained.
The Borel partial maps and countable inverse atlases make the legal meeting loci Borel and source/range fibres countable.
Two witnesses of the same lag differ by a common shift. Extend the shorter to the longer existing legal pair; the common future adds identical sums, so `c=S_r(z)-S_s(w)` descends.
For composition align the middle histories at their larger legal depth; the already existing middle segment transfers across the matching equality and its sums cancel.
This proves additivity and inversion without illegally continuing a terminal. The actual forward arrow `(Tz,-1,z)` has clock `-kappa(z)`.
On a fixed-history bisection the repeated branch IMAGE factor from w to z is `P_s(w)/P_r(z)=exp(-c)`.
The FULL kernels for each owner, always restricted to actual legal meeting arrows, are
`ker c: P_r(z)=P_s(w)`;
`ker lag: (z,0,w) with T^j z=T^j w legally for some j`;
`ker c intersect ker lag: those equal-depth meetings also satisfying P_j(z)=P_j(w)`.
These include merging non-loop arrows; equality of products without an actual meeting is not an arrow.

Nonzero source isotropy is equivalent to eventual actual legal periodicity: unequal repeated iterates produce a legal cycle, and conversely an eventual cycle produces such iterates.
For least tail period k and signed whole cycle sum C, the source lag group is kZ, `c(mk)=mC`, and ENTIRE `H_z=CZ`, with transient prefixes cancelled.
Terminating and infinite non-eventually-periodic states have unit source isotropy and H={0}.
In the full extension `(w,h)->(z,h+c)`, isotropy is the c-kernel on source isotropy: kZ if C=0, only units if C!=0, and units for non-eventual states.
Physical height-translation stabilizer of the extension orbit is exactly H. Only C!=0 gives primitive abs(C) and repetitions m*abs(C), positive integer m; C=0 is not a zero-period primitive.
For arbitrary O define Pred_0(p)={p} and Pred_(j+1)(p) by ALL admitted own inverse labels/sheets over Pred_j(p).
The complete component of z is `union_{s legal} union_{r>=0} Pred_r(T^s z)`; for a periodic core point p it is `union_r Pred_r(p)`.
If `T^a z=T^b p`, transport to p gives phase `h+S_b(p)-S_a(z) mod H_p`; witness changes differ by H_p. Zero H leaves a real phase.
No global selector, quotient regularity, invariant physical measure or classical suspension is assumed in these statements.

## 5. MAIN: exact uniform admission exit within the frozen gate

The proof is global over every source sign and floor boundary. Write u=abs(x), v=abs(y); the source convention gives `d<=v+1`.
Since `2uv<=u^2+v^2` and `2u<=u^2+1`,
`u(v+1)<=u^2+(v^2+1)/2 < 1+u^2+v^2`.
Thus EVERY legal MAIN output (X,Y) satisfies `0<X<2`, because `abs(d*x/(1+R))<1`.
Arithmetic legality forces each input coordinate into `(-infinity,0) union [1,infinity)`; the remaining intervals have a zero floor magnitude.

Case 1: x<0. The same strict bound gives `0<X<1`, so the output has n'=0 and is terminal, regardless of y or the output radius.
Case 2: x>=1 and y<0. Then `1<X<2` while `Y=-1+q*y/(1+R)<-1`.
Hence n'=1 and d'>=2; d' cannot divide n', so this output too is terminal. No negative integer endpoint is omitted.
Case 3: x>=1 and y>=1, with the actual arithmetic permission. Here d<=y, n<=x and d>=1.
Using `xy/(1+x^2+y^2)<1/2`, both positive fractions obey
`0<d*x/(1+R)<=xy/(1+R)<1/2`,
`0<q*y/(1+R)=n*y/[d*(1+R)]<=xy/(1+R)<1/2`.
Therefore `1<X<3/2` and `-1<Y<-1/2`. The output has EXACT n'=d'=q'=1 and radius squared greater than 1, so it is legal.
It now lies in Case 2 and its NEXT output is terminal. These alternatives exhaust every legal source.

Define `Q=A intersect ([1,infinity) x [1,infinity))`. Since every Q-point has R>=2, Q is wholly inside D.
The recursive iterate domains are exactly `D^(0)=X`, `D^(1)=D`, `D^(2)=Q`, `D^(3)=empty`; consequently D^(8)=empty as asked.
The bound is sharp in legal-step count: Q is nonempty, e.g. `(1,1)->(4/3,-2/3)->(41/29,-35/29)` has two legal transitions and then terminal floor magnitudes (1,2).
This exact rational chain only shows sharpness; the global inequalities, not that example or any finite census, prove the bound.
Every object reaches a terminal in at most TWO legal applications, so no third legal application is possible. No step beyond the frozen eight-step gate was investigated or needed.

## 6. MAIN entire terminal classes, kernels, H and height phases

Let E0=X\D be the full terminal set. Define the exact remaining depth
`tau(z)=0 on E0`, `tau(z)=1 on D\Q`, `tau(z)=2 on Q`.
Put `e(z)=T^{tau(z)}z` and `B(z)=S_{tau(z)}(z)`, so e(z) is its unique terminal and B=0 at terminal objects.
Every step satisfies `tau(Tz)=tau(z)-1`, `e(Tz)=e(z)` and `B(z)=kappa(z)+B(Tz)`.
The full source component over EACH terminal p is exactly
`C_p={p} union Pred_1(p) union Pred_2(p)=e^{-1}({p})`.
Pred_1 consists of legal depth-one ancestors, Pred_2 of depth-two ancestors, and every deeper predecessor set is empty by D^(3)=empty, not by an imposed inverse cutoff.
All d,q and both sheets remain checked at each allowed depth. Terminals with no predecessors stay singleton components; critical and arithmetic-failure terminals remain equally present.

The actual MAIN groupoid now has the explicit full description
`G_MAIN={(z,tau(z)-tau(w),w):e(z)=e(w)}`,
with `c(z,tau(z)-tau(w),w)=B(z)-B(w)`.
Proof: an actual meeting has the same eventual terminal and the same remaining depth after that meeting, forcing the displayed lag; cancelling the common remaining clock gives the displayed c.
Conversely the legal terminal meeting at depths tau(z),tau(w) supplies this arrow. Thus no extra history-word arrows survive and none of the actual merging arrows is removed.
The COMPLETE MAIN kernels are accordingly:
`ker lag: e(z)=e(w), tau(z)=tau(w)`;
`ker c: e(z)=e(w), B(z)=B(w)`;
`ker lag intersect ker c: e(z)=e(w), tau(z)=tau(w), B(z)=B(w)`.
These are exact actual arrow sets, with their uniquely determined lags; no assertion that all kernels are units is substituted for them.

Every source isotropy arrow has z=w and hence lag 0: all source isotropy is trivial. Equivalently any cycle would permit three legal applications, contradicting the proved bound.
Thus there are NO source cycles of ANY period, no eventual cycles, ENTIRE H_z={0} at EVERY object, and only unit extension isotropy.
For an extension point (z,h), the invariant phase is `eta=h-B(z)`. An arrow changes h by B(z)-B(w), preserving eta, and takes every object to its terminal representative.
The orbit SET is therefore in explicit bijection with pairs `(p,eta)`, p in E0 and eta in R. Physical time sends `(p,eta)` to `(p,eta+t)` and has no positive return.
This finite-terminal description is a proved set-level phase parametrization; no additional topological quotient or global-measurable-selector theorem is claimed.
The coboundary expression for c does NOT replace the frozen clock by zero. For example kappa(1,1)=-log27, so its legal forward arrow has clock log27 but is not a loop or primitive physical return.
The entire positive primitive ledger is empty; failure is nonemptiness, not a fabricated wrong-prime period. No repeated packet or positive repetition law exists for MAIN.

## 7. Independent G/N control fixed gates and complete G incoming

G's fixed equations are `(s-1)x=s`, `(s-1)y=-s`; the origin is not fixed, so x=-y=a>1.
Thus `2a^3-2a^2-1=0`. This polynomial is strictly increasing for a>1, negative at 1 and positive at 3/2; exactly one such root exists.
Conversely that root gives the legal fixed point `p=(a,-a)` with `rho=2a^2>2`. These equations exhaust the FULL G fixed set, without an arithmetic condition or selected centre.
The two actual inverse sheets at p are exactly p and `b=p/rho=(1/(2a),-1/(2a))`, since radial paired sources have reciprocal squared radii and direct substitution gives T_G b=p.
Every legal G output has first coordinate strictly between 1/2 and 3/2: equality in `2|x|<=1+x^2+y^2` occurs only at excluded unit-circle axis points.
But b_x<1/2, so b has no predecessor. The ENTIRE incoming source class of p is precisely {p,b}, at all inverse depths.
Write `gamma=log[(rho-1)/(1+rho)^3]<0`, `beta=log[(1-rho^{-1})/(1+rho^{-1})^3]<0` and `L=-gamma>0`.
Their absolute Jacobians give `beta-gamma=2 log rho`, hence `0<2 log rho<L`. Signed planar determinants have opposite signs; clocks use their absolute values.
Both objects have source isotropy Z, ENTIRE H=gamma Z=LZ, trivial extension isotropy, and all phases R/LZ with repetitions mL.
For explicit arrows let nu(p)=0,nu(b)=1,A(p)=0,A(b)=beta. Every ordered pair admits every integer lag k and
`c(z,k,w)=A(z)-A(w)+(k-nu(z)+nu(w))*gamma`.
This follows by meeting at the fixed point after the legal arrival depth, then adding fixed steps. Phase is `h-A(z) mod L`; the forward b->p clock is -beta.
The strict interval for beta-gamma excludes zero-clock cross arrows; this class's clock and joint kernels contain exactly its two units, while its lag kernel contains all four zero-lag ordered pairs.
It is ONE full fixed-core packet and one physical circle, not two packets from the two source points.

Its multiplier is irrational: the cubic for a has no rational root among ±1,±1/2, so a has degree three over Q.
Reduction by `a^3=a^2+1/2` gives `(1+2a^2)^3=34a^2+10a+13`.
If `exp(L)=(1+2a^2)^3/(2a^2-1)=m` were rational, then `(34-2m)a^2+10a+(13+m)=0`, an impossible nonzero quadratic relation.
This is an own G arithmetic defect, not a MAIN witness. More importantly for this audit, the actual legal G fixed recurrence shows that radial compression WITHOUT MAIN's permission does not force universal exit.

N's fixed x equation is `(1-d)x=1`. It is impossible for d=1; for d>=2 it forces `x=-1/(d-1)` in [-1,0), whose actual n is 1, contradicting n=dq>=2.
Thus the complete N fixed set is empty, including all signed boundaries and its arithmetically admitted circle points. There is no N fixed core with a basin to fabricate.
N retains its own affine inverse/IMAGE, step log n, all general kernels and conditional eventual-cycle H from §4. No G/N higher-period census or global N exit claim is made.

## 8. Exact gate outcome and stopping boundary

The requested MAIN D^(8)-emptiness question is settled by the stronger exact certificate D^(3)=empty and D^(2)=Q nonempty.
For this unchanged owner the entire MAIN source is terminating; the whole positive physical ledger is empty, while terminal objects, incoming arrows and nonzero arrow clocks remain intact.
Outcome: `UNIFORM ADMISSION EXIT; EMPTY MAIN POSITIVE LEDGER — STOP / FORK` for this new audit question, with arithmetic nonemptiness failure proved rather than inferred from fixed-point absence.
This does not rewrite 442's frozen bounded OPEN result: its scope lacked the separately authorised uniform-exit proof now supplied here.
The G/N controls keep their own definitions and conclusions. No control clock or recurrence is transferred to MAIN; no map, source, density, clock or primitive convention has been repaired.
Strong naturalness and PROVES_TOO_MUCH remain OPEN; arithmetic T1 NOT PASSED; T3 NOT AUDITED; classical NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.
No enlargement of eight, numerical census, new candidate or further-period control classification is undertaken.
After full self-read and measured freeze, report RAW READY and HOLD for root's full raw read and a DISTINCT PAPER UNLOCK. Current author/helper/peer surfaces have not informed this derivation.

EOF — RAE01 card-only raw; exact three-step-domain emptiness, complete terminal ledger, independently owned fixed controls.
