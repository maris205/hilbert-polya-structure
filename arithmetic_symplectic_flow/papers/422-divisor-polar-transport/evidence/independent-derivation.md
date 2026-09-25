# DPT01 — card-only independent derivation

## 1. Authority, inputs and boundary

This is the raw mathematical review of `ANG-20260923-DPT01`, after root's separate card-only release.
Sole scientific input: `candidate-card.md`, all 95 lines through its scientific-prefix EOF, SHA256 `9570756fe6d588c990fef6cdd7dd625c0bc23e4b0b41ca716822b1f59654bb9f`.
The original card was fully read at CP1 and fully reread for this derivation; no author paper, package README, claim ledger, outcome, peer answer or sibling proof was read.
Frozen CP1: `scope-review.md`, 60 lines, SHA256 `54f183c775c34ff44ac0ba51c0e6a15f3b25c71b62f67f0a3e4f068e583c8ec1`.
ARS router/workflow/reviewer/runtime and this stream's controlling instructions are retained from full reads; no additional scientific inputs were used.
This is inherited-model/shared-history internal review, `NOT_CALIBRATED`, not blind or external/human peer review.
Method: exact algebra, smooth local change of variables and deterministic-history arguments; no scientific code, numerical evidence, external literature, Git or new agent.
Only this raw evidence file is written. The frozen card and scope report are unchanged; manuscript access remains on HOLD after freezing.

## 2. Complete own inverse atlas

Write a legal source as `(n,UP)` with `P>0`, `U=Rot(theta)`, `n=dq` and
`theta in I_dq=[2 pi(d-1)/(dq),2 pi/q)`. This half-open interval includes every assigned lower endpoint.
For MAIN/C/S the target register is `m=d+q`; for H it is `m=dq`.
Put `D=diag(d,1/d)`, except that S uses `D=I`. Let `r=q` for MAIN/S/H and `r=1` for C.
The matrix formula on this source cell is `B=P D U^r`.
For any proposed target `B` with positive determinant, its left polar factors are `R=(BB^T)^(1/2)>0`, `V=R^-1 B in SO2`.
The equation for `P` is `R^2=P D^2 P`. Set `Q=D P D`; then `Q^2=D R^2 D`.
The unique SPD root gives exactly `P=D^-1(D R^2 D)^(1/2)D^-1`, with no omitted SPD solutions.
For `W=R^-1 P D`, one has `WW^T=I` and `det W=det P/det R=1`, so `W in SO2`.
Consequently `Z=W^-1 V in SO2`, and `B=P D Z`. Every solution is obtained by solving `U^r=Z`.
For MAIN/S/H, let `phi=Arg Z in[0,2 pi)` and enumerate all `q` roots `theta_j=(phi+2 pi j)/q`, `0<=j<q`.
Every `j>=1` fails the required strict bound `theta<2 pi/q`; the remaining `j=0` passes precisely when
`phi/(2 pi) in[1-1/d,1)`. This is a proved exhaustion of the frozen all-root recipe, not a selected-root replacement.
Thus their actual inverse is `(m,B) -> (dq,Rot(phi/q)P)` on that exact domain; H has `dq=m`.
For C the unique root is `U=Z`, and its exact domain is `phi/(2 pi) in[(d-1)/(dq),1/q)`.
For S, `P=R`, `W=I`, `Z=V`; the same all-root exhaustion and its own arithmetic checks apply.
MAIN/C/S enumerate all positive pairs `d+q=m`, and H enumerates all positive divisors `d|m`, `q=m/d`.
Each actual source has unique right polar factors and unique floor digit, so identical actual preimages cannot be double counted.
Each source cell is injective: its angular image under multiplication by `r` has length at most `2 pi`, with one endpoint excluded, and `P -> R` is bijective.
All domains are Borel. The target's ability to take a further step is never imposed as an inverse-domain condition.
There is no inverse with `det B<=0`; there is no register-zero inverse, and MAIN/C/S additionally have no register-one inverse.
H register one is included. All permission-failure targets and their actual incoming arrows remain in the source.

## 3. All-point flat-four-dimensional IMAGE

First justify all germs without excluding repeated eigenvalues. On symmetric matrices the derivative of `X -> X^2` at SPD `X` is `L_X(Y)=XY+YX`.
For positive eigenvalues `lambda_1,lambda_2`, `det_Sym2 L_X=4 det(X) tr(X)>0`, including equality of the eigenvalues.
The inverse function theorem and the unique SPD root therefore give smooth square-root and polar maps everywhere on the SPD/positive-determinant loci.
The displayed inverse makes `P -> R=(P D^2 P)^(1/2)` a smooth diffeomorphism of SPD matrices.
Every actual angular root has a local smooth inverse germ, with angular derivative `1/r`; the discontinuous principal-Arg selector is not differentiated.
At an assigned seam or sector boundary the germ is the extension of that particular fixed-index matrix formula. No boundary point is deleted or made terminal.

The reference measure is the original four-entry Lebesgue measure. For `P=[[a,b],[b,e]]>0` and `A=Rot(theta)P`, direct four-entry differentiation gives
`dA=(a+e) dtheta da db de = tr(P) dtheta dP`.
For left polar coordinates `B=R Rot(psi)` the analogous density is `tr(R) dpsi dR`.
These are derived coordinate densities, not a replacement of the stipulated flat measure by a polar product measure.
Congruence `P -> Q=D P D` has determinant `(det D)^3=1` on `Sym2`.
Differentiating `Q^2=D R^2 D` and taking symmetric-coordinate determinants gives
`det(D_P R)=det(L_Q)/det(L_R)=tr(Q)/tr(R)`, since `det Q=det R=det P`.
Locally write `W=Rot(omega(P))`. Then `psi=omega(P)+r theta`, so the `(theta,P)->(psi,R)` determinant is `r det(D_P R)`.
Combining this with the two flat polar densities yields the actual four-entry forward determinant
`K_F(n,UP)=abs det_R4 DF = r tr(D P D)/tr(P)`, and hence `J_inverse=1/K_F` evaluated at that inverse source.
In coordinates this is the following full-class formula, with `a>0,e>0,ae-b^2>0` unrestricted:

| Owner | `K_F=exp(kappa)` |
| --- | --- |
| MAIN | `q(d^2 a+d^-2 e)/(a+e)` |
| C | `(d^2 a+d^-2 e)/(a+e)` |
| S | `q` |
| H | `q(d^2 a+d^-2 e)/(a+e)` |

Every value is strictly positive and finite. In particular, `det D=1` does not make MAIN/C/H volume preserving, and `log q` alone is generally not their clock.
The counting-register factor is one on each fixed branch. Thus these are also the counting-times-flat-measure Radon–Nikodym values.
Countably many angular/matrix coordinate neighborhoods cover each fixed-index germ; disjointify their Borel restrictions and then enumerate all integer indices.
On overlapping neighborhoods for the same assigned inverse value, inverse-function uniqueness gives the same local germ and determinant.
At a principal-Arg seam the global selector can jump, but its assigned germ and Jacobian remain defined; piecewise chart restrictions give the same Borel image law.
Ordinary local change of variables and countable additivity prove `mu(I_alpha E)=integral_E J_alpha dmu` for EVERY Borel subset of each actual inverse domain.
This includes null boundaries and repeated-eigenvalue points, with their stipulated all-point version, not merely an almost-everywhere choice.
For a Borel set `A` in the legal forward domain, let `N_A(y)` be the number of its actual immediate predecessors of `y`.
The finite inverse atlas proves `F(A)` Borel and gives `mu(F(A))=integral 1_{N_A>0} dmu`, while `integral_A K_F dmu=integral N_A dmu`.
This distinguishes the union IMAGE from the multiplicity-weighted IMAGE; no images of overlapping branches are counted as disjoint without justification.

## 4. Actual histories, kernels, entire H and phases on the full source

For each owner use only its own legal steps and write `R_a(x)=product_{j=0}^{a-1} K_F(F^j x)`, `R_0=1`, `S_a=log R_a`.
The actual retained-lag groupoid is exactly the card's `G={(x,a-b,y):F^a x=F^b y}`, with legal finite histories, equal triples identified.
If two presentations have the same lag, their indices differ by a common integer; cancelling the common meeting-point tail gives the same
`c(x,a-b,y)=log R_a(x)-log R_b(y)`.
Aligning the two histories of the middle state proves composition and cocycle additivity; only existing legal tails are used, including for histories ending at a terminal.
The inverse triple changes the sign of `c`. The forward step arrow `(Fx,-1,x)` has clock `-kappa(x)`.
The inverse-history IMAGE density is `1/R_a(x)`; an actual history bisection from `y` to `x` has IMAGE density `R_b(y)/R_a(x)=exp(-c)`.
All equality loci and their countable chart refinements are Borel. Each depth has finitely many actual inverse choices at a given state, so each full source orbit is countable.

The complete kernels, always restricted to actual meeting triples, are:
`ker(c)`: `R_a(x)=R_b(y)`;
`ker(lag)`: `(x,0,y)` with `F^a x=F^a y` for some legal `a`;
`ker(c) intersect ker(lag)`: those same equal-depth meetings with `R_a(x)=R_a(y)`.
Clock equality alone is not an arrow, and clock-zero arrows are not silently identified with identities.
At any source point, nontrivial source isotropy exists exactly when its forward history eventually enters an actual full-state cycle.
If that cycle has least source period `k`, the source isotropy is `k Z` and, for one traversal with signed clock `lambda=sum_cycle kappa`,
the ENTIRE clock image is `H_x=lambda Z`. Transient prefixes cancel from every isotropy clock.
At all other points the source isotropy is trivial and `H_x={0}`. This is a complete pointwise characterization, not a claim to locate all higher cycles.
For the extension `(y,h)->(x,h+c)`, nonzero `lambda` gives trivial extension isotropy and physical least positive return `|lambda|`, with repetitions `r|lambda|`.
If `lambda=0`, the full source isotropy `k Z` remains ineffective extension isotropy, while height translation has no nonzero period.
In particular `H_x={0}` is not an assertion that source isotropy is trivial.

Define `Pred_0(z)={z}` and `Pred_{a+1}(z)=union_{w in Pred_a(z)} {all actual own immediate inverses of w}`.
The exact entire source orbit is `union_{b: F^b z legal} union_{a>=0} Pred_a(F^b z)`.
These formulas retain every incoming branch and every intermediate permission check; they truncate neither depth nor matrix scale.
Register-zero and nonpositive-determinant points are isolated terminal source orbits; permission-failure terminals can have the full inverse trees above.
Every orbit that ends at a terminal has trivial source/extension isotropy and `H={0}`, even when its inverse tree is infinite.
For a reference core, all physical height phases are `R/H`, with no choice of a distinguished height.
If `F^a x=f` for a fixed core, the core phase is `h-S_a(x) mod H_f`.
More generally, if `F^a x=F^j f_0` on a reference cycle, it is `h+S_j(f_0)-S_a(x) mod H_{f_0}`.
No nice coarse quotient, classical suspension, symplectic owner or global operator is asserted by these set/Borel formulas.

## 5. Exhaustion of the four complete fixed sets

A fixed point must be legal, since terminals have identities but are not artificial fixed points of the partial map.
For MAIN/C/S, fixed memory requires `dq=d+q`, or `(d-1)(q-1)=1`, hence exactly `d=q=2`, `n=4`, `theta in[pi/2,pi)`.
Write `P=[[a,b],[b,e]]>0`, `delta=ae-b^2`, and `J=Rot(pi/2)=[[0,-1],[1,0]]`.
For the MAIN/H fixed equation `UP=P D U^q`, equivalently `P^-1 U P=D U^q`, its lower-left entry is
`sin(theta)(a^2+b^2)/delta = d^-1 sin(q theta)`.
For MAIN's only possible sector, the left side is positive and the right side is nonpositive; therefore `Fix(MAIN)=empty`.
More generally this rules out ALL H fixed points with `d>1,q>=2`: `0<theta<2 pi/q<=pi` and `q theta in[2 pi(1-1/d),2 pi)`.

If `D=I` and `UP=P U^q`, then comparison of products with their transposes gives `UP^2 U^T=P^2`.
Uniqueness of the SPD root implies `UPU^T=P`, so `U` commutes with `P` and `U=U^q`.
For S's required `q=2`, this forces `U=I`, outside `[pi/2,pi)`. Thus `Fix(S)=empty`.

For exponent one and `d>1`, the fixed equation is `UPU^T=P D`.
Symmetry forces `P D=D P`, so `b=0`; trace equality then forces `e=d a`.
The off-diagonal equation is `(a-e) cos(theta) sin(theta)=0`. The central rotations cannot satisfy the diagonal equations, leaving exactly `U=+J` or `-J`.
Conversely each of these two rotations with `P=diag(a,d a)`, `a>0`, satisfies the matrix fixed equation; only the own sector remains to be checked.
For C's `d=q=2` sector only `+J` is admitted. Its complete fixed set is therefore
`Fix(C)={(4,A_a): A_a=J diag(a,2a), a>0}`.
At every such core `K_C=3/2`, so `kappa_C=log(3/2)` and the entire `H=log(3/2) Z`.

For H with `d=1`, the preceding `D=I` argument gives commuting `U,P` and `U^(q-1)=I`.
If `q>=2`, the sector `0<=theta<2 pi/q` allows only `theta=0`; these are all cores `(n,P)`, `n=q>=2`, `P>0`.
At each such core `K_H=n`, `kappa_H=log n`, and the entire `H=log n Z`.
If `q=1`, then `n=1` and every angle is in the digit-one sector. Its complete fixed family consists of the following disjoint parameters:
`(1,P)` for every SPD `P`; `(1,-P)` for every SPD `P`; and `(1,a Rot(theta))` for `a>0`, `theta in(0,2 pi)\{pi}`.
Indeed a noncentral planar rotation commutes with an SPD matrix exactly when the matrix is scalar; central rotations commute with every SPD matrix.
All these unit-register fixed cores have `K_H=1`, `kappa_H=0`, entire `H={0}`, and retained source/extension isotropy `Z`.
For H's remaining possibility `q=1,d>1`, the exponent-one calculation gives `P=diag(a,d a)`, `U=+J` or `-J`.
The actual sector `[2 pi(1-1/d),2 pi)` excludes `+J` and admits `-J` exactly for `d=2,3,4`, including the lower endpoint for `d=4`.
Thus the remaining complete H fixed families are
`(d,B_{d,a})`, where `B_{d,a}=-J diag(a,d a)`, `d in{2,3,4}`, `a>0`.
Their clock factors are `h_d=(d^2-d+1)/d=d-1+1/d`, namely `3/2`, `7/3`, `13/4`.
The entire `H=log(h_d) Z` at each such core. The cases just exhausted cover every register, angle and SPD matrix, not merely an assumed diagonal section.

## 6. Complete fixed-core incoming and packet ledger

For C put `B_a=J diag(2a,a)`. The full basin of the fixed core `(4,A_a)` is exactly the four-state chain
`(1,B_a) -> (2,A_a) -> (3,B_a) -> (4,A_a) -> (4,A_a)`.
To verify completeness, at target `(4,A_a)` one has `R=diag(2a,a)`, `V=J`.
The inverse pairs `(d,q)=(1,3),(2,2),(3,1)` have `P=diag(2a/d,a d)`, `W=I`, `U=J`; their own floor test retains exactly the first two.
At target `(3,B_a)`, pairs `(1,2),(2,1)` similarly retain only `(1,2)`; target register two has only `(1,1)`, and register one has no inverse.
Thus there is no unlisted predecessor. Each transient step has `d=1`, hence `kappa_C=0`.
The whole four-state basin has source isotropy `Z`, trivial extension isotropy, entire `H=log(3/2) Z`, and all phases `h mod log(3/2)`.

For each H unit-register fixed core, the only inverse index is `d=q=1`; the unique inverse is that same core. These basins are singletons.
Their phase space is the whole real height line, with no positive physical period and retained ineffective source isotropy `Z`.
For an H positive-SPD core `(m,B_0)`, `m>=2`, the following gives its COMPLETE first inverse layer, not just its self-loop.
For every `e|m` put `q=m/e`, `R=B_0`, `V=I`,
`P_e=D_e^-1(D_e B_0^2 D_e)^(1/2)D_e^-1`, `W_e=B_0^-1 P_e D_e`, `phi_e=Arg(W_e^-1)`.
Retain precisely those divisors with `phi_e/(2 pi) in[1-1/e,1)`; the incoming point is `(m,Rot(phi_e/q)P_e)`.
The divisor `e=1` gives the core itself. Other divisors are tested by this exact formula, not assumed absent; memory hold is not a global injectivity assertion.
For an H extra core `(m,-J diag(a,m a))`, `m in{2,3,4}`, its COMPLETE first inverse layer is
`(m,Rot(3 pi/(2q)) diag(m a/e,a e))` for EVERY `e|m`, `q=m/e`.
Indeed `R=diag(m a,a)`, `V=-J`, `W=I`, `phi=3 pi/2`, and every such `e<=4` passes `3/4>=1-1/e`.
Here `e=m` is the core itself, while the other divisors are genuine incoming points.
For both positive H families, EVERY deeper predecessor is exactly the recursion `Pred_a` using the full own atlas in section 2.
This is an exact full-basin specification with finite explicit branch domains at each node, not a finite-depth census or a choice of backward orbit.
Every point in these basins has source isotropy `Z`, trivial extension isotropy and the ENTIRE fixed-core clock group; its phase is `h-S_a(x)` modulo that group.

Distinct fixed cores cannot be source-groupoid equivalent: any two fixed futures that meet would have to be the same core.
Consequently different scales, SPD matrices, or other fixed-core parameters give distinct physical packets even when their lengths coincide.
C has continuum many fixed-core packets at `log(3/2)`, no fixed-core packets at other positive lengths, and repetitions `r log(3/2)` of each individual packet.
H has continuum many fixed-core packets at each `log n`, `n>=2`, and at each of `log(3/2)`, `log(7/3)`, `log(13/4)`.
The three latter factors are distinct nonintegers, so they do not collide with the integer-length fixed families or with one another; equal-length SPD/scale multiplicity remains continuum.
Every positive fixed packet has all phases in its own `R/L Z` and repetitions `rL`; zero-clock unit families keep all real phases and do not become positive packets.
MAIN and S have no fixed-core basin or fixed-core packet. These statements enumerate the entire FIXED sector only, not unexamined higher-period sectors.

## 7. Bounded verdict and freeze boundary

All four owners have positive finite all-point inverse-germ IMAGE versions for the stipulated flat measure; no seam, repeated eigenvalue or legal state causes an ownership stop.
The full ordered polar law, register rule, floor permission and every inverse branch stay with the same owner throughout.
The MAIN fixed gate is empty and therefore cannot decide the full positive ledger. Its status is `BOUNDED OPEN / FORK`, not global failure, no-period theorem or arithmetic success.
C and H display their own non-prime times and excess packet multiplicities; these are changed-owner control results and are not transferred into MAIN.
S's empty fixed sector likewise implies no assertion about its higher cycles. The generic entire-H characterization above supplies the full-source contract without a new cycle census.
The lineage interface is the frozen divisor/quotient rule acting on actual polar geometry, not a detached symbolic roof; fixed basis, designed sectors and strong naturalness remain OPEN.
Only the owner/clock component is established here; arithmetic T1 is NOT PASSED, T2 is bounded, T3 is NOT AUDITED, classical fields are NOT APPLICABLE, formal coordinates UNASSIGNED and Route B NOT INVOKED.
No new architecture, parameter tuning, physical measure, prime target data or selected representative has been introduced.
This raw derivation is to be frozen after full self-read and a measured hash, then held for root's full read and separate PAPER UNLOCK.

EOF — card-only raw derivation; no author or peer manuscript exposure.
