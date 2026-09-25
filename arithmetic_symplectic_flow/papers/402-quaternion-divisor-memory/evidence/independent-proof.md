# 402 independent raw proof — ordered quaternion memory and full IMAGE

Candidate `ANG-20260922-QDM01`; card-only mathematics after root's explicit release.
Sole scientific input: `candidate-card.md`, complete clarified 100 lines, SHA256 `84694a5fc334bec368850e6ea542344ba4723a0aaf39c92fb0e37d39247cd921`.
Original 87-line prefix SHA256 `cbadef459e4a5e990e71119af26ad3ddf6bba7db04f0eedd0303a532d78255a4` is preserved.
Frozen CP1: `scope-review.md`, 72 lines, SHA256 `9c1dbb8fcb2a1334d90ea8efb826a335ee296da2bf228c4d3a5e223cdeec96ee`.
Actual scientific access: the entire clarified card reread through line 100 and EOF; no manuscript, README, ledger, author proof, or peer output was read.
Retained ARS and stream instructions govern method only. Internal shared history/model: **NOT_CALIBRATED**, not blind or external peer review.
No numerical experiment, external source, auxiliary delegation, fitted measure, new carrier, or higher-period census is used.

## 1. Complete ordered inverse relations

Write `N(q)=q conjugate(q)=|q|²` for the real Euclidean squared quaternion norm. Quaternion multiplication is associative, and `N(pq)=N(p)N(q)`.
The lattice Lambda is closed under addition and multiplication; a nonzero quaternion has a unique two-sided inverse.
Put `C=[0,1)^4`, `C*=C\{0}`, and write every z uniquely as `D+R`, with `D∈Lambda`, `R∈C`.
All four owners have exactly the card's legal domain: `D≠0`, `R≠0`, `B≠0`, and `D^(-1)(A+B)∈Lambda`.
No extra exclusion of A or A+B is introduced. In particular zero quotients and their subsequent terminal states remain.

For MAIN at target `(P,Q,w)`, the COMPLETE inverse domain for each `D∈Lambda\{0}` is

`E_D={P,Q∈Lambda, P≠0, w≠0, P w^(-1)∈C*}`,
`I_D(P,Q,w)=(DQ−P, P, D+P w^(-1))`.                         (1)

Indeed the proposed source has floor D, remainder `P w^(-1)`, and left quotient `D^(-1)((DQ−P)+P)=Q`.
Its forward continuous coordinate is `(P w^(-1))^(-1)P=w`; the order follows from `(ab)^(-1)=b^(-1)a^(-1)`.
Conversely an actual predecessor has `P=B`, `DQ=A+B`, and `R w=B`, forcing exactly (1). Thus no further hidden source test removes an element of E_D.
For fixed D, the integer-memory map `(P,Q)↦(DQ−P,P)` is injective: P is recovered from the second coordinate and Q by left multiplication by `D^(-1)`.
Different D give different source floors, even if their discrete memories happen to agree.

MEMORY-HOLD has inverse, for each D≠0,

`I_D^H(A,B,w)=(A,B,D+B w^(-1))`,
`E_D^H={B≠0, w≠0, B w^(-1)∈C*, D^(-1)(A+B)∈Lambda}`.        (2)

Its memory map is the identity on the admitted memory pairs. The same ordered inversion verifies both inverse identities; the additional divisibility predicate is not dropped.
DIVIDEND-OFF has inverse

`I_D^O(P,Q,w)=(DQ−P,P,D+w^(-1))`,
`E_D^O={P≠0, w≠0, w^(-1)∈C*}`.                              (3)

ORDER-REVERSED has inverse

`I_D^V(P,Q,w)=(DQ−P,P,D+w^(-1)P)`,
`E_D^V={P≠0, w≠0, w^(-1)P∈C*}`.                             (4)

For V, `P(w^(-1)P)^(-1)=w`; replacing `w^(-1)P` by `P w^(-1)` would generally be incorrect.
Equations (2)–(4) are necessary and sufficient by solving each OWN forward equation, with the same discrete injectivity argument for O/V as for MAIN.
All domains are Borel: discrete predicates are countable and inversion is real analytic away from zero. Every inverse is Borel and injective.
These formulas apply at ALL targets, including forward terminals. A target failing an inverse predicate is retained as an object, not removed.
For example MAIN/O/V targets with second memory Q=0 can have forward-map predecessors with A+B=0; targets with first memory zero have no forward-map predecessor but can still have a legal forward step and nonidentity groupoid arrows.
No owner has a nonidentity incoming arrow to a state with continuous coordinate zero, since every actual image coordinate is nonzero; such states retain their isolated identity objects.
All finite incoming histories are precisely finite compositions of (1)–(4) using that owner's successive exact domains, plus the empty history. No norm cutoff or infinite-history completion is applied.

## 2. Four-dimensional derivatives and the full counting factor

Differentiating `q q^(-1)=1` gives `D(inv)_q[h]=−q^(-1) h q^(-1)`.
Left multiplication by a and right multiplication by b scale Euclidean lengths by `|a|` and `|b|`; their absolute real four-dimensional determinants are `|a|^4` and `|b|^4`.
Consequently inversion has absolute determinant `|w|^(−8)`. These exponents have been derived from the actual four-dimensional transport, not supplied as arithmetic weights.
The owned inverse densities, on their respective complete domains, are

`J_MAIN(P,Q,w)=J_V(P,Q,w)=|P|^4/|w|^8=N(P)^2/N(w)^4`,
`J_H(A,B,w)=|B|^4/|w|^8=N(B)^2/N(w)^4`,
`J_O(P,Q,w)=1/|w|^8=1/N(w)^4`.                              (5)

All are positive finite at EVERY actual inverse point. The analytic extension exists through each assigned cube face because w and the required multiplier are nonzero.
The equality of the norm formulas for MAIN and V does not identify their inverse domains, products, or orbit relations.
For each fixed memory pair and D, the continuous inverse is a translation of inversion followed or preceded by multiplication by a nonzero quaternion.
It is therefore the restriction of a real-analytic diffeomorphism; ordinary real change of variables proves its every-Borel IMAGE identity on that restricted domain.
Now partition an arbitrary Borel E in the full inverse domain by its countably many target memory pairs.
The discrete memory injection in Section 1 makes their source memory slices disjoint. Summing the four-dimensional identities yields

`μ(I_D(E))=∫_E J_D dμ` for `μ=counting_(Lambda²) × Lebesgue_4`. (6)

The same argument applies to H's identity memory map and the own O/V maps. Infinite values on both sides are allowed.
No lattice-index factor appears: an injective map of counting atoms onto its admitted subset has counting density one, even if that subset is a proper sublattice congruence class.
No measure value is fitted and no cube-face value is patched. The frozen analytic version, not measure-theoretic uniqueness on a null set, determines (5) there.

## 3. Full actual groupoids, global kernels, H, and phases

For one specified owner F, let `x_j=F^j x=(A_j,B_j,z_j)` and `R_j=z_j−floor(z_j)` along a legal history.
Its actual step clock follows from its OWN density:

`κ_F(x)=2log N(B)−4log N(R)` for MAIN/H/V,
`κ_O(x)=−4log N(R)`.                                         (7)

Define the following positive finite products on every legal length-m history, with empty product one:

`P_m^F(x)=∏_{j=0}^{m−1} N(B_j)/N(R_j)^2` for MAIN/H/V,
`P_m^O(x)=∏_{j=0}^{m−1} N(R_j)^(−2)`.                        (8)

Then `S_m(x)=2log P_m^F(x)`. In particular no positivity of individual step clocks is presumed.
The source is exactly

`G_F={(x,k,y): ∃ legal m,n≥0, k=m−n, F^m x=F^n y}`,
`c_F(x,k,y)=2log(P_m^F(x)/P_n^F(y))`.                         (9)

Equal triples are identified; no free quaternion-word arrows are added. The sets of legal histories and finite-iterate equalities are Borel, so G_F is Borel.
Countably many D choices at each inverse step imply countable arrow fibers. All points of the uncountable full carrier still remain.
Composition is obtained by aligning the two legal histories of a common endpoint at their longer meeting time; the paired endpoint extends along the same legal segment, including in the presence of terminals.
Two presentations of an identical triple have the same length difference, so their lengths differ by a common integer increment. The appended legal tail contributes the same sum on both sides.
This proves that c descends. Alignment also proves cocycle additivity, equivalently cancellation of the shared factors in (8).

Here are the COMPLETE GLOBAL kernels, always restricted to the actual equality/legality in (9):

`ker c_F = ⋃_{m,n} {(x,m−n,y): F^m x=F^n y, P_m^F(x)=P_n^F(y)}`,
`ker lag_F = ⋃_m {(x,0,y): F^m x=F^m y}`,
`ker c_F∩ker lag_F = ⋃_m {(x,0,y): F^m x=F^m y, P_m^F(x)=P_m^F(y)}`. (10)

These explicit norm-product tests include all non-isotropy arrows; they do not replace the full source relation by equality of norms.
The real extension has all states `(x,h)` and arrows `(y,h)→(x,h+c_F(x,k,y))`. Its lag/clock kernels and intersection are the corresponding full lifts of (10).
Forward arrival `F^m y=x` gives `(x,−m,y)` with clock `−S_m(y)`; the reverse incoming-history arrow has clock `+S_m(y)`.

A nonzero source isotropy lag is equivalent to eventual arrival at a legal cycle, for a repeated finite segment can then be repeated indefinitely.
If the eventual cycle has least source period p, all isotropy lags are exactly `pZ`. Let K be the sum of the OWN κ over that one least cycle, without an incoming prefix.
Every presentation of its isotropy generator has clock K; the finite approach cancels. Therefore the full pointwise classification is

`source isotropy=pZ`, `H_x=K Z`,
`extension isotropy=pZ if K=0, and units if K≠0`.              (11)

If x has no eventual cycle, source and extension isotropy are units and `H_x={0}`. This includes all terminal classes.
For K≠0, the least positive physical time is `|K|`, with all positive repetitions `j|K|`; for K=0 there is no positive generator, even though source/extension isotropy persists.
Formula (11) is an exact all-point conditional classification, not a classification or census of higher-cycle locations.
For every source class and reference o, all arrows `g:x→o` give the coset `{h+c(g)}` of `H_o`.
Two transport choices differ by isotropy, and every isotropy clock occurs by composition. Thus the entire phase set is `R/H_o`, not a selected height or inverse history.
It is a circle of least period `|K|` when K≠0, and a free translation line when H=0. No smooth quotient, invariant extension measure, or positive suspension is asserted.

## 4. Complete MAIN and ORDER-REVERSED fixed sets

Any MAIN or V fixed point has `A=B=Q=b≠0`. Its memory equation is `Db=2b`, hence `D=2` by right multiplication by `b^(-1)`.
Write `R=r+u` with `0≤r<1` and `u∈[0,1)^3`. MAIN's fixed transport forces

`b=R(2+R)=R²+2R`.                                           (12)

V instead forces `b=(2+R)R`, which is the SAME expression only because the fixed-set memory equation has already forced the real D=2.
Thus equality of their fixed loci does not assert that the full noncommutative owners agree.
Put `s=1+r∈[1,2)`, and write `b=b_0+b_1 i+b_2 j+b_3 k`. Equation (12) gives

`b_0=s²−1−|u|²`, `b_j=2s u_j (j=1,2,3)`.

Here is a finite, exact, exhaustive index set without a sampled census.
Choose `b_0∈{−2,−1,0,1,2}`, `(b_1,b_2,b_3)∈{0,1,2,3}³`, and let `V=b_1²+b_2²+b_3²`.
Set

`t=(b_0+1+sqrt((b_0+1)²+V))/2`, `s=sqrt(t)`.

Retain precisely those b≠0 for which `1≤s<2` and every `b_j<2s`; define `u_j=b_j/(2s)` and `R_b=(s−1)+u`.
Exclude `R_b=0` explicitly. Call the resulting finite index set I.
Then the COMPLETE fixed sets of MAIN and V are, each in its own owner,

`{ f_b=(b,b,2+R_b) : b∈I }`.                                 (13)

Necessity: `−3<b_0<3`, `0≤b_j<4`, and `s^4−(b_0+1)s²−V/4=0` follow from (12) and the cube.
The only positive root for s² compatible with `s≥1` is the displayed t. Sufficiency follows by substituting its exact root and cube predicates back into (12).
This gives at most one R per b and includes every axis/cube-face case; no quaternion root has been selected from a larger unrecorded solution set.
At f_b put `U_b=N(R_b)` and `Z_b=N(2+R_b)`. Their difference is `4s>0`, and (7) gives

`K_b=κ(f_b)=2log(Z_b/U_b)>0`.                                 (14)

Their full source isotropy is Z, extension isotropy is trivial, and their full incoming basins have H=`K_b Z` and all phase points `R/(K_b Z)`.
The equality of K_b for MAIN/V is verified from their own densities, not transferred together with their different incoming histories.

## 5. Complete MEMORY-HOLD fixed set, including all degenerate roots

For H choose arbitrary `D∈Lambda\{0}`, `B∈Lambda\{0}`, and `Q∈Lambda`.
Every fixed point, and only a fixed point, is

`(A,B,z)=(DQ−B,B,D+R)`, where `R∈C*` solves `R²+RD=B`.         (15)

To turn (15) into an exhaustive root parameterization, write `D=a+v`, `B=b+w`, `R=t+u`, with vector parts in R³.
The required real t lies in `[0,1)`; put `α=2t+a` and `c=w−t v`. Quaternion multiplication gives exactly

`α u+u×v=c`, `t²+a t−|u|²−u·v=b`.                            (16)

The following three cases enumerate ALL roots, always retaining `u∈[0,1)^3` and `(t,u)≠0`.
(i) If α≠0, take ALL real t in `[0,1)` satisfying the scalar equation in (16) after substituting

`u=[α c+v×c+v(v·c)/α]/(α²+|v|²)`.                           (17)

This is the inverse of `α I−[v]_cross`; multiplication verifies it directly, and its determinant is `α(α²+|v|²)≠0`.
(ii) If α=0 and v≠0, retain t only when `c·v=0`; set `u_0=(v×c)/|v|²` and take ALL real roots λ of

`λ²+λ=(t²+a t−|u_0|²−b)/|v|²`, `u=u_0+λv`.                  (18)

(iii) If α=0 and v=0, require w=0 and take the ENTIRE sphere `|u|²=t²+a t−b` intersected with the cube.
Because D≠0 is an integer in this case, `t=−a/2∈[0,1)` forces `D=−1`, `t=1/2`.
The nonempty cube spheres occur exactly for `B=−k`, `k∈{1,2,3}`, with

`R=1/2+u`, `|u|²=k−1/4`, `u∈[0,1)^3`.                       (19)

These cases include scalar, noncentral, repeated, and positive-dimensional roots. The cross-product identity and real equation prove both necessity and sufficiency, rather than invoking an incomplete choice of quaternion square root.
Substitution into (15) gives left quotient Q and `R^(-1)B=D+R`, so all permissions and actual fixed equations hold.
Conversely any H fixed point recovers its unique D, B, R, and `Q=D^(-1)(A+B)`; hence the parameterization does not create duplicate source states.

For every such fixed core define

`K_{D,R}=2log(N(D+R)/N(R))`.                                 (20)

This is its OWN clock from `N(B)=N(R)N(D+R)`. All cores have source isotropy Z.
If K≠0, H=`K Z`, extension isotropy is trivial, and the fixed basin gives one positive primitive packet of time `|K|` with its whole phase circle.
If K=0, H=0, extension isotropy remains Z, and the whole phase line remains. Zero clock does not erase these fixed source cores.
In particular EVERY core in (19), with arbitrary Q, has `N(D+R)=N(R)=k` and K=0. Each sphere contains an open spherical patch inside the cube around its equal-positive-coordinate point, so it is nonempty and uncountable.

For completeness the fixed-sector positive packet multiplicities can be characterized exactly without a high-period census.
For fixed D,B, case (i) has finitely many t: after substitution the real equation is a nonzero rational equation; as t tends to infinity, u tends to `−v/2`, so its left side minus b has leading term t² and is not identically zero.
Case (ii) has at most two λ roots, and case (iii) has only K=0. Thus nonzero-clock base roots across all D,B form a countable set.
For every realized `L=|K|>0`, arbitrary Q in (15) gives countably infinitely many DISTINCT fixed cores with that same L. The countable upper bound makes this multiplicity exactly countably infinite in the fixed-core sector.
The realized values are exactly the positive absolute values of (20) for roots (16)–(18); no values are inferred from integer labels alone.
There are continuum many zero-clock fixed cores because of (19); their phase lines are not positive primitive packets.

## 6. Complete DIVIDEND-OFF fixed set

O's memory equation again forces `A=B=b≠0` and `D=2`, but its OWN transport imposes `R^(-1)=2+R`.
Thus `R²+2R=1`. Its imaginary part is `2(1+r)u=0`, so u=0 and the only allowed real root is `R=sqrt(2)−1`.
Consequently

`Fix(O)={(b,b,1+sqrt(2)): b∈Lambda\{0}}`.                     (21)

Every listed state is legal and fixed. From O's OWN density,

`K_O=−4log N(R)=8log(1+sqrt(2))=:L_0>0`.                     (22)

The fixed-core sector has exactly countably infinitely many different packets of this length, one for each nonzero b, with all repetitions and phases.
Each has source isotropy Z, trivial extension isotropy, and H=`L_0 Z`. None of these facts is a claim about every higher-period O cycle.

## 7. All fixed basins, collisions, incoming phases, and the decisive witness

For ANY of the four owners and ANY fixed core f above, its entire source class is exactly

`B_f=⋃_{m≥0}{x: F^m x=f by a legal history}`.                 (23)

A common iterate with f must itself equal f, proving both inclusions. Every element of (23) is generated by the complete inverse domains of Section 1.
For `F^m x=f`, its phase at f is `h−S_m(x)` modulo `K_f Z`; changing the meeting time changes it only by that subgroup.
If K_f=0 the phase is an unquotiented real number and the retained source/extension isotropy is still Z.
Different fixed cores have disjoint source classes, since their constant forward tails cannot meet; equal clocks never identify them.
Thus there is exactly one positive primitive packet per fixed core with K_f≠0, containing ALL its incoming states and height phases. Repetitions are `j|K_f|` for all integers j≥1.

For MAIN and V the exact fixed-sector multiplicity at L>0 is

`m_fixed(L)=#{b∈I : 2log(Z_b/U_b)=L}`.                        (24)

This finite parameter count retains every collision. For instance b=i,j,k all belong to I: their common `s²=(1+sqrt(2))/2` lies between 1 and 4, and their single nonzero u coordinate is `1/(2s)<1`.
They are three distinct fixed cores with equal norms and hence equal positive clock, not three representatives of one source orbit.
For H the exact positive fixed-sector multiplicities and zero-clock continua are as in Section 5; for O they are as in Section 6.
These are fixed-sector multiplicities only. Unclassified higher cycles could add packets at a coincident time; they cannot remove these owned packets.

MAIN has the explicit legal fixed core

`f=(1,1,1+sqrt(2))`, `D=2`, `R=sqrt(2)−1`.                   (25)

It lies on allowed cube faces, not outside the full carrier. Its four-dimensional density, not a one-dimensional real-slice density, yields `K_f=L_0` in (22).
By the full isotropy result, this is the LEAST positive physical time of its whole basin, not merely a displayed period or lag weight.
Its exponential is

`exp(L_0)=(1+sqrt(2))^8=577+408sqrt(2)`,                      (26)

which is irrational and therefore not an ordinary integer prime. This single actual MAIN packet already violates the clarified necessary target.
V owns the same fixed core and time by its separate calculation. H also has fixed cores `(2Q−1,1,1+sqrt(2))` for every Q∈Lambda, with the same positive L_0; these are its own memory-held packets.
The O and H controls do not supply evidence against MAIN in place of (25); MAIN's violation has been independently proved on its own full extension.

## 8. Lineage, decision, and exact limits

For `A=n−1`, `B=1`, `D=d` with positive integers n,d and d≠0, the left quotient is the real number `n/d`; it belongs to Lambda exactly when ordinary d divides n.
For EVERY remainder `R∈C*`, the point `z=d+R` has exactly that floor and passes the remaining MAIN permissions. The proper-divisor subcase is `1<d<n`.
This verifies the stated lineage on whole admissible remainder cells without replacing Y by its real/integer slice. The quotient written into the next B memory genuinely enters later reciprocal-dividend transport whenever that next step is legal.
All memory signs, zero sums, zero quotients, terminals, null cube faces, incoming branches, and phase points remain in the same-object ledger.
The root parameterizations are exact full sets with predicates, not a finite numerical sample. No higher-cycle search or theorem about their locations was needed.
Portfolio: **STOP / FORK — complete measured owner, but an actual MAIN fixed basin has a nonprime positive primitive time.**
The conclusion is not inferred from a zero-clock control, missing positive fixed points, or a claimed failure of global coverage. The direct witness (25) decides it.
Strong naturalness remains OPEN; floors, the coordinate lattice, memory update, and multiplication order are design choices, not a literature-novelty or nonconjugacy theorem.
Classical fields NOT APPLICABLE; T3 NOT AUDITED; formal coordinates UNASSIGNED; B NOT INVOKED. No roof, operator, measure fitting, publication, or new candidate is supplied.

EOF — clarified-card-only raw proof complete; await root's full read and separate PAPER UNLOCK.
