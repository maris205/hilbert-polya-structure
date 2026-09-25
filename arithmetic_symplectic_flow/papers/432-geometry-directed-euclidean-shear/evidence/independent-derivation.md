# GES01 — card-only independent derivation of the global gate

## 1. Authority, exact inputs and boundary

Candidate `ANG-20260923-GES01`; root separately released mathematics after fully reading the final CP1 report.
Sole scientific input: clarified `candidate-card.md`, all 101 lines through actual EOF, SHA256 `76da0d903c9a3f31beb80302dbbc3846f204d03131945fd6e33c36417e6aaf66`.
The original 93-line prefix is SHA256 `613852dd3ad20e2d2adf6f8bf67ccb18403670464cdd34e653c131c587ba3090`; the appended control-name clarification changes no formula or domain.
Frozen scope: `scope-review.md`, 76 lines, SHA256 `ac0d2a75af905facf2650561af3308fe7be2ff4a5c19119a43fcde497ca1e8d4`.
The entire clarified card was reread after release. No author paper, README, claim ledger, outcome, peer answer, helper output or sibling proof was read.
Previously read stream/ARS instructions and shared history remain retained. This is inherited-model internal review, `NOT_CALIBRATED`, not blind or human/external peer review.
Only this raw evidence file is written. Methods are exact inequalities, change of variables and structural dynamics; no scientific numerical code, external source, Git, auxiliary agent or cycle census is used.

## 2. Full laws, output closure and divisor interface

Every owner keeps `X=N0^2 x [0,infinity)^2`, `mu=counting^2 x dx dy`, and legal domain `D={a,b>=1,x,y>0}`.
At a legal point, `t=x/(x+y)` lies strictly between 0 and 1 and `Q>=1`, so `1<=k=1+floor(Qt)<=Q`.
If `a>=b`, including the tie, `Q=floor(a/b)` and `a-kb>=a-Qb>=0`; the unchanged b is positive.
If `a<b`, `Q=floor(b/a)` and `b-ka>=b-Qa>=0`; the unchanged a is positive.
Both monomial shears keep x,y strictly positive and finite. Thus MAIN maps every legal point into X, possibly onto an integer-axis terminal but never onto a real axis or the integer origin.
C has the same valid integer output and unchanged positive geometry. H keeps its positive integers and positive geometry, so H maps D into D.
All points outside D remain terminals, not artificially fixed points. No target legality test is added.

The sector `k=Q` is exactly `t>0` with `t>=(Q-1)/Q`, equivalently `x>0,y>0,x>=(Q-1)y`; it is nonempty for every Q.
For Q=1 this is the whole positive quadrant. At Q>1 the lower cut is included.
On that sector, the updated larger integer is the Euclidean remainder in `[0,min(a,b))`, and is zero exactly when the smaller divides the larger.
Conversely a zero updated integer forces the chosen k to equal that integer quotient. All other k sectors remain part of the actual execution.
This verifies the stated divisor/remainder interface, not prime generation or naturalness. C still uses geometric k-selection; H, unlike MAIN/C, does not execute the integer subtraction.

## 3. Complete actual inverse domains

Write a target as `(A,B,u,v)` with nonnegative integer A,B. No owner has an incoming branch when `u=0` or `v=0`, since every legal output has positive real coordinates.
For MAIN, fix every integer `k>=1`. On side L require `B>0`, put `p=floor(A/B)`, and reconstruct
`(a,b,x,y)=(A+kB,B,u/v^k,v)`.
The source is positive and is on side L automatically; its quotient is `Q=k+p` and its t is `u/(u+v^(k+1))`.
Its EXACT digit-domain inequalities are
`(p+1)u >= (k-1)v^(k+1)` and `p u < k v^(k+1)`.
They are precisely `k-1 <= Qt < k`; equality in the lower inequality and strictness in the upper are essential.
On side R require `A>0` and `B+(k-1)A>0`, put `p=floor(B/A)`, and reconstruct
`(a,b,x,y)=(A,B+kA,u,v/u^k)`.
The second side condition is exactly the strict R convention; it rejects the false R tie when `B=0,k=1`.
Here `Q=k+p`, `t=u^(k+1)/(u^(k+1)+v)`, and the EXACT digit conditions are
`(p+1)u^(k+1) >= (k-1)v` and `p u^(k+1) < k v`.
All these branches additionally require `u,v>0`. These formulas include every integer-axis target that actually has a predecessor; `(A,B)=(0,0)` has none.

C uses the same integer reconstruction and side conditions, but real source `(u,v)`.
For either side, with its respective `p=floor(A/B)` or `floor(B/A)`, its own exact digit inequalities are
`(p+1)u >= (k-1)v` and `p u < k v`.
C therefore does not inherit MAIN's monomial source readout or its inverse domain. At a fixed target these inequalities bound k above, but no such bound is imposed in advance on MAIN.

For H require `A,B>=1,u,v>0`; the side and `Q=floor(max(A,B)/min(A,B))` are fixed by its held integers.
Enumerate ALL `1<=k<=Q`, retaining the unchanged integer pair.
On its L side the reconstructed real source is `(u/v^k,v)` and the exact domain is
`(Q-k+1)u >= (k-1)v^(k+1)` and `(Q-k)u < k v^(k+1)`.
On its R side the reconstructed source is `(u,v/u^k)` and the exact domain is
`(Q-k+1)u^(k+1) >= (k-1)v` and `(Q-k)u^(k+1) < k v`.
These are again exactly the frozen source digit checks, now with H's own fixed Q rather than MAIN's reconstructed quotient.

Substitution verifies forward equality for every admitted branch. Conversely, the actual side, k and integer update of any predecessor force exactly one of these reconstructions.
Thus both inverse identities and completeness hold. A source has a unique side, Q and k, so identical actual points are not multiplied by labels.
All displayed inequalities define Borel domains; all target next-step permissions remain irrelevant.
The full atlas is countable, not assumed finite-to-one. For example, MAIN target `(0,B,u,v)` with `B>=1,u>0,0<v<1` admits every sufficiently large L index k because `(k-1)v^(k+1)->0`.
This gives infinitely many distinct immediate predecessors, all retained. The exact inequalities, not a finite index table, govern every subsequent inverse level.

## 4. Own all-point flat-measure IMAGE and clocks

For fixed integer/side/k data, MAIN/H have the positive-quadrant diffeomorphisms
`(x,y)->(x y^k,y)` on L and `(x,y)->(x,x^k y)` on R.
Their forward determinants are respectively `y^k` and `x^k`; their displayed inverse germs have determinants `v^-k` and `u^-k`.
Thus `J_L(u,v)=v^-k`, `J_R(u,v)=u^-k`, and the legal source clocks are `kappa_L=k log y`, `kappa_R=k log x`.
C's own real germ is the identity, giving `J_C=1` and `kappa_C=0` on every legal C step.
All these values are strictly positive and finite in the Jacobian column at EVERY actual inverse point, including assigned digit cuts and integer-axis targets.
The monomial germs are smooth on the whole positive quadrant and agree on local chart overlaps with the same fixed data; no floor or jumping selector is differentiated.
Each branch maps one counting slice to its reconstructed counting slice with weight one. An integer label supplies no extra determinant or clock.
Change of variables for these global quadrant diffeomorphisms, followed by Borel restriction and countable summation over slices, proves
`mu(theta E)=integral_E J dmu` for EVERY Borel E in every actual inverse domain, including infinite measure and null boundaries.
No logarithmic reference density replaces dxdy. The all-point version is the prescribed germ derivative, not a freely filled-in a.e. version.
For a Borel set E in an owner's legal domain, let `N_E(w)` count all actual immediate predecessors in E, possibly infinitely many.
The countable injective Borel branch atlas gives `mu(F(E))=integral 1_{N_E>0} dmu` and `integral_E exp(kappa) dmu=integral N_E dmu` by countable additivity/Tonelli.
Overlapping target images are not treated as disjoint, and no single unqualified density is assigned to their union.
There is no next-step clock at a terminal. Real-axis points have no incoming and hence only their unit arrows; the germ formula is never evaluated at zero.

## 5. The two precommitted global identities

For MAIN/C put `V=a+b`. A legal L step decreases V by `kb>=1`; a legal R step decreases it by `ka>=1`.
Integers remain nonnegative and at least one stays positive. Therefore every MAIN/C trajectory starting in D terminates after at most `a+b-1` steps.
Geometry remains positive, so a trajectory starting in D ends on an integer axis. The subtraction also preserves `gcd(a,b)`, so the terminal nonzero integer is exactly the initial gcd.
All other starting points are already terminals. No MAIN/C state is periodic or eventually periodic as a partial-map state; terminal identities are not added loops.
This is a well-founded argument on the full unbounded carrier, not a finite experiment or a fixed-state-window inference.

Define `Psi(a,b,x,y)=log(xy)` wherever `x,y>0`, including both integer axes.
For MAIN/H, a legal L step changes Psi by `log(x y^(k+1))-log(xy)=k log y`; a legal R step changes it by `k log x`.
These are precisely the independently derived own clocks. Hence `kappa=Psi(Fz)-Psi(z)` and `S_m(z)=Psi(F^m z)-Psi(z)` for every legal finite history, including a terminal final target.
C's separately derived clock is identically zero; its geometry is constant, so it also preserves Psi on the positive-real locus.
At an actual MAIN/H meeting `F^m z=F^n w`, the whole cocycle is therefore
`c(z,m-n,w)=Psi(w)-Psi(z)`.
For C it is identically zero. Real-axis components are handled separately as isolated units, never by taking log0 or assigning a fabricated terminal step clock.
In particular, for EVERY owner and EVERY state, the ENTIRE isotropy-clock image is `H_z={0}`. This is an all-arrow conclusion, not only a zero clock observed on selected loops.
MAIN/H step clocks need not vanish; exactness of the cocycle, rather than stepwise zero, excludes their nonzero isotropy returns.

## 6. Actual full groupoids and kernels

Use exactly the card's triples `(z,m-n,w)` with legal meeting histories and equal actual triples identified; source is w and range is z.
For equal-lag presentations, a common additional meeting tail adds identical sums, proving descent. Aligning the two middle legal histories proves composition, additivity and inverse sign, even for terminal meetings.
The forward arrow `(Fz,-1,z)` has clock `-kappa(z)`. No labels become free generators.
Every equality locus is Borel and the countable inverse atlas gives countable source/range fibers and source orbits over all depths, even with infinite immediate MAIN fibers.
Composed inverse IMAGE has density `exp(-S_m)`; a branch-pair arrow from w to z has density `exp(S_n(w)-S_m(z))=exp(-c)`.
The full generic kernels, always on actual meetings, are `ker c={S_m(z)=S_n(w)}`, `ker lag={(z,0,w):F^m z=F^m w}`, and their intersection with both equal-depth conditions.

For MAIN/C let `N(z)` be the exact finite terminal depth and `tau(z)=F^{N(z)}(z)`; already-terminal states have N=0.
Two states are source-equivalent exactly when they have the SAME full terminal state, including its real coordinates, not merely the same gcd.
The unique actual lag between them is `N(z)-N(w)`. Thus their full groupoid is exactly
`{(z,N(z)-N(w),w):tau(z)=tau(w)}`.
It is principal: all source and extension isotropy is trivial.
On a positive-real MAIN component, the clock kernel additionally requires `x_z y_z=x_w y_w`; the lag kernel requires `N(z)=N(w)`; the joint kernel requires both.
For C the entire groupoid is its clock kernel, and the joint kernel equals its lag kernel. Isolated real-axis units are included in all kernels without a logarithm.

For every owner define `Pred_0(p)={p}` and `Pred_{j+1}(p)` as the union of ALL actual own inverse branches of every point of `Pred_j(p)`.
The full source orbit is `union_{b:F^b p defined} union_{j>=0} Pred_j(F^b p)`.
For MAIN/C it is exactly `union_j Pred_j(tau(p))`. Every intermediate cut and side check is the one in section 3, without index or depth truncation.
Integer-origin terminals and all real-axis terminals are isolated. Other MAIN/C integer-axis terminals retain exactly the inverse trees specified above, which may be infinite.

## 7. Complete H source classification, incoming and kernels

At fixed positive integers, H's side and Q are fixed, while k is recomputed from the evolving geometry at every step.
On L, y is constant and `x_{j+1}=x_j y^(k_j)`, `1<=k_j<=Q`.
If y=1 every point is fixed. If y>1, `x_j>=x_0 y^j` grows strictly to infinity; if `0<y<1`, `0<x_j<=x_0 y^j` decreases strictly to zero without ever reaching the real axis.
On R, x is constant and `y_{j+1}=y_j x^(k_j)`.
If x=1 every point is fixed. If x>1 the y coordinate increases strictly to infinity; if `0<x<1` it decreases strictly to zero and remains positive at every finite step.
Therefore the COMPLETE periodic source set is the fixed set
`P_H={a>=b>=1, x>0, y=1} union {1<=a<b, x=1, y>0}`.
There are no other periodic or eventually-periodic legal states. Every other legal H history is infinite and strictly monotone in the indicated coordinate.
Every terminal of H is isolated: its integer registers cannot be reached from positive registers, and real axes cannot be reached from positive geometry.
No nonfixed point can enter `P_H`, since its nonunit constant multiplier is preserved. A fixed core's only actual predecessor is itself, including when several formal k labels give the same monomial value before the unique digit check.
Consequently each fixed core has a singleton basin, source isotropy `Z`, zero clock on every isotropy arrow and retained extension isotropy `Z`.
Every other H state has trivial source and extension isotropy. ALL have entire `H_z={0}`, not just the monotone states.

For completeness, write `K_m(z)=sum_{j<m} k(F_H^j z)`, with `K_0=0` on legal H components.
On L, `F_H^m(a,b,x,y)=(a,b,x y^K_m(z),y)`; on R it is `(a,b,x,x^K_m(z) y)`.
Thus H's full lag kernel consists exactly of equal-depth meetings with the same held integers and constant coordinate and, for some m,
`x_z y^K_m(z)=x_w y^K_m(w)` on L, or `y_z x^K_m(z)=y_w x^K_m(w)` on R, together with the isolated terminal units.
The readout sums use every actual iterate; this exact condition does not assume global injectivity or omit overlaps of different inverse branches.
For an H arrow on L, `c=log(x_w/x_z)` with the same y; on R, `c=log(y_w/y_z)` with the same x.
Accordingly its clock kernel consists EXACTLY of all unit arrows plus the full isotropy `Z` at every point of `P_H`; no clock-zero arrow joins distinct H source states.
The H joint lag/clock kernel is exactly the units. In particular source isotropy at the fixed cores is not confused with the lag-zero kernel.
All incoming to every nonfixed H orbit is precisely the unrestricted recursion in section 6 with H's own finite k atlas at each held-register node; no chosen backward path or MAIN descent is substituted.

## 8. All physical phases, multiplicity and decisive verdict

The extension retains all `(z,h)` and actual arrows `(w,h)->(z,h+c)`. Height translation is an action on the full orbit SET, with no topology or classical suspension asserted.
On every positive-real MAIN/H component the quantity `h+Psi(z)` is invariant under groupoid arrows; translating height shifts it by the actual translation amount.
Equivalently, with representative p and actual arrow from z to p, the full phase is `h+Psi(z)-Psi(p)` in R, with no nonzero-period identification.
For MAIN one may take the unique full terminal p=tau(z); this phase remains valid when p lies on an integer axis. C's full phase at its terminal representative is simply h.
For H fixed cores and all isolated terminals the phase is the entire real height h; the fixed cores additionally retain their ineffective source/extension isotropy Z.
Real-axis terminals use h directly. They are not evaluated in Psi, deleted as null states or made absorbing loops.
These phases describe every extension orbit over every source class. Distinct source classes are never merged by equal phase, equal arithmetic invariant or equal clock values.
For ALL three owners, height translation has stabilizer exactly the whole `H_z={0}` at EVERY point; every physical height orbit is free, not closed.
The multiplicity of positive primitive packets at EVERY positive time is therefore exactly zero, and there are no positive-primitive repetitions.
H's continuum of source fixed points does not become a continuum of positive physical packets or a collection of invented zero-period primitives.
For scale, each owner has continuum many nonclosed height orbits: already the isolated integer-origin states with positive geometry give continuum distinct source classes, and the entire carrier has only continuum cardinality.

MAIN's globally empty positive ledger FAILS the frozen nonempty target. This is `OWNED SHEAR IMAGE CLOCK; GLOBAL EMPTY POSITIVE LEDGER — STOP / FORK`, not a vacuous arithmetic pass or merely a fixed-window OPEN result.
MAIN's termination and exact all-arrow clock proof are its own results. C's termination/identity clock and H's different source periodicity/exact clock were proved independently for their full owners.
The full source, current-state feedback, own inverse IMAGE, actual histories, kernels, entire H, incoming and phases remain one-object consistent. No measure, parameter, cut or terminal rule was repaired.
Strong naturalness and novelty remain unestablished; arithmetic T1 is NOT PASSED, T3 NOT AUDITED, classical NOT APPLICABLE, formal Route UNASSIGNED and B NOT INVOKED.
The precommitted structural global gate is complete; no numerical or higher-period census, new candidate or 435 work is undertaken.
After full self-read and hash receipt, freeze this raw and HOLD for root's full read and a separate PAPER UNLOCK. ARS supplies scope/provenance discipline, not external mathematical certification.

EOF — clarified-card-only raw; all three positive ledgers empty, MAIN STOP / FORK by its global gate.
