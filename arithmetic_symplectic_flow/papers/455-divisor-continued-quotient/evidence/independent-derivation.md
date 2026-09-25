# 455 — independent card-only derivation

Candidate `ANG-20260924-DCQ01`; batch `RECURRENCE-OWNER-20260924-V`, round 1/5, exactly 455–459.
This raw follows the distinct release after root's full CP1 read. No author surface has been accessed.
Sole scientific input: the complete original 87-line `candidate-card.md`, reread through EOF, SHA256 `1ea6c5d9d88b6ea7dfd9431443c580552b4ccb3b3163c87765a3f44d2d8b9e77`.
Frozen CP1: `evidence/scope-review.md`, 75 lines, SHA256 `1d9aa4aecb34df083063124a65351f1ee431fae98cca063b2b495b84d7d586a3`.
The six ARS files and local governance were personally refreshed at CP1; their exact read scope is recorded there and retained here.
Prior 442/445/450 and broader shared-history exposure remain disclosed. No old proof, current author/peer/helper answer, Outcome, or sibling scientific package was opened for this derivation.
Same inherited model, **NOT_CALIBRATED**: non-blind internal AI work, not human/external/cross-model verification or a claim of independent errors.
No scientific code, numerical census, network, Git, PDF, delegation, new owner, or period≥2 census was used.

## 1. Full owners and boundary objects

Let X=[0,1]² with original area measure μ. For x,y>0 put n=⌊1/x⌋≥1 and d=⌊1/y⌋≥1, and A={x,y>0,d divides n}.
M has domain A and q=n/d; O has domain (0,1]² and q=max(1,⌊n/d⌋); N has domain A and q=n.
Every legal q is an integer with 1≤q≤n. The common update is T(x,y)=(u,v)=(1/x−n,1/(q+y)).
Thus 0≤u<1 and 0<v<1, proving type X→X. All source laws and reciprocal cells are Borel.
Both axes and all other illegal sources remain terminal objects, with units and every incoming history. No absorbing loop is added.
The x=1/n cuts give u=0 and remain legal where their other source tests hold; their finite-expansion targets are retained terminal objects.
The measure is the original finite, non-atomic area measure on the whole closed square; no continued-fraction density is substituted.

## 2. Complete inverse atlas and exact image sets

Let C=[0,1)×(0,1). For Z=(u,v)∈C define
Q(v)=⌈1/v⌉−1, Y(v)=1/v−Q(v), D(v)=⌊1/Y(v)⌋.
Then Q≥1, 0<Y≤1, D≥1. The inequality 0<1/v−q≤1 has exactly the integer solution q=Q(v).
In particular v=1/k, k≥2, has q=k−1 and Y=1; using ⌊1/v⌋ instead would incorrectly lose this assigned boundary.
Every predecessor has y=Y(v), and for its first digit n≥1 has x=1/(n+u), whose actual digit is n because 0≤u<1.
Consequently the complete predecessor sets are:

- M: the unique θ_{DQ,Q}(Z)=(1/(DQ+u),Y), for every Z∈C.
- O: θ_{n,Q}(Z) for all n∈L(Q,D), where L(1,D)={1,…,2D−1} and L(Q,D)={QD,…,(Q+1)D−1} when Q≥2.
- N: θ_{Q,Q}(Z) if D divides Q, and no predecessor otherwise.

For O, Q=1 means ⌊n/D⌋≤1, whereas Q≥2 means QD≤n<(Q+1)D. These are exactly its own max-quotient rule, including n<D branches.
For M, reconstructed n=DQ is exactly the source divisibility/quotient law. For N, reconstructed n=Q must pass its independent D|Q admission test.
Direct substitution gives Tθ(Z)=Z, and the forced y and x equations give θ(Tz)=z for every legal source with its actual digits.
Outside C there is no predecessor for any owner: every actual output has u<1 and 0<v<1.
Hence the full image of M and O is C; that of N is {Z∈C:D(v)|Q(v)}. Every object outside those images remains in X.
The inverse formulas show that M and N are globally injective partial maps. O is not: for Q≥2,D≥2 its target has D distinct legal predecessors.
All inverse domains are Borel, as are the source restrictions. The integer functions Q,Y,D include their literal ceiling/floor boundary conventions.
Equivalently each fixed-(n,q) branch is restricted by q=Q(v) and the corresponding displayed n test; this enumerates all original labels without a cutoff.
No incoming state is selected or discarded. In particular the u=0 axis can have predecessors, while v=0, v=1, and u=1 have none.
The whole v=0 edge is terminal and has no incoming; u=1 or v=1 points can still have legal outgoing steps according to their own source law.

## 3. Every-point area IMAGE and signed clock

The fixed-label analytic inverse is θ_{nq}(u,v)=(1/(n+u),1/v−q).
It is an ambient diffeomorphism from (-n,∞)×(0,1/q) onto (0,∞)², with inverse (x,y)↦(1/x−n,1/(q+y)).
Its derivative is diagonal with entries −1/(n+u)² and −1/v². Thus the prescribed all-point inverse factor is
J_{nq}(u,v)=1/[(n+u)²v²]>0, finite at every actual branch point, including u=0 and v=1/(q+1).
For every Borel E in the actual branch domain, change of variables on this ambient diffeomorphism gives μ(θ_{nq}E)=∫_E J_{nq}dμ.
The actual branch restriction keeps both sets in X, so this is an identity for the original area measure, including arbitrary Borel boundary subsets.
The analytic formula fixes its value at null states rather than inferring an arbitrary version from the a.e. measure identity.
At a legal source, n+u=1/x and v=1/(q+y), so
κ(x,y)=−log J_{nq}(Tz)=−2 log[x(q+y)]=2 log(v/x).
It is signed and can vanish; it is not replaced by an assumed positive roof. There is no clock for a nonexistent terminal step.

A useful identity, derived directly from this same map, retains rather than changes that clock.
Put F(x,y)=2 log(1+xy) on all X and, on legal sources,
Δ(z)=2 log[(1+xy)/(1+xy−x(n−q))].
The denominator equals x(q+y+u)>0. Since 1≤q≤n, Δ≥0, with equality exactly when n=q.
The identity 1+uv=[1+xy−x(n−q)]/[x(q+y)] proves
κ(z)=F(Tz)−F(z)+Δ(z).
For N, q=n, so Δ≡0 and κ_N=F∘T_N−F. This is an algebraic potential identity for the frozen area clock, not use of a new reference measure.

## 4. Actual histories, cocycle descent, and full kernels

For owner U let D_U^r be the domain of the legal r-fold iterate, with D_U^0=X. Let S_r(z)=Σ_{j=0}^{r−1}κ_U(U^jz), S_0=0.
Keep G_U={(z,r−s,w):U^rz=U^sw legally, r,s≥0}, source w and range z, identifying only equal actual triples.
Two witnesses of the same triple differ by equal added depths; their common legal tail adds the same clock to both S sums and cancels.
Aligning the two middle depths when composing arrows is legal because the longer middle history exists; its prefix sum cancels, proving additivity.
Therefore c(z,r−s,w)=S_r(z)−S_s(w) descends, units have clock zero, and reversal changes the sign.
The forward arrow (Uz,−1,z) has c=−κ_U(z), exactly as frozen.
Legal iterates and clocks are Borel. Each fixed pair (r,s) supplies a Borel equality relation, so their countable union supplies the actual Borel groupoid and cocycle.

For an explicit all-state kernel test define P_r(z)=∏_{j=0}^{r−1}x_j(q_j+y_j)>0, P_0=1, along its own legal history.
Then S_r=−2 log P_r, and c(z,r−s,w)=2 log[P_s(w)/P_r(z)]. Consequently:

- ker lag consists exactly of (z,0,w) with a legal equal-depth meeting U^rz=U^rw for some r≥0.
- ker c consists exactly of actual (z,r−s,w) with P_r(z)=P_s(w).
- The joint kernel consists exactly of (z,0,w) with a legal equal-depth meeting and P_r(z)=P_r(w).

These are full membership formulas with explicit finite products on all legal histories, not selected branches or a fixed-point-only claim. The product test is witness-independent by descent.
For M and N, injectivity simplifies every arrow: k≥0 means w=U^kz legally and c=S_k(z); k<0 means z=U^(−k)w and c=−S_{−k}(w).
Their lag and joint kernels are therefore units. Their clock kernels are not presumed to be units.
For M, the above normal form makes its clock kernel exactly units and all connecting segments with P_|k|=1, with the stated orientation.
For N, the potential identity improves the global formula to c(z,k,w)=F(w)−F(z).
Thus ker c_N consists of all actual triples with x_z y_z=x_w y_w, while its lag and joint kernels are units.
For O, the equal-depth relation can contain different points; its full kernels are the meeting/product formulas above and the explicit fixed-basin specialization below.

## 5. Entire incoming sets, isotropy, and all phases

Let I_U(B) be the union of all actual inverse candidates from Section 2 over every target in B, and I_U^0(B)=B.
Iterate this recursion with no depth cutoff. The entire source class of z is
[z]_U=⋃_{s≥0:z∈D_U^s} ⋃_{r≥0} I_U^r({U^s z}).
This is exactly the legal-meeting relation; it includes finite expansions, terminal classes, all branches and all incoming depths, not a finite census.
For terminal t it reduces to ⋃_{r≥0}I_U^r({t}). Every z in that class has a unique depth ν(z) to t.
With B(z)=S_{ν(z)}(z), its exact arrows are (z,ν(z)−ν(w),w), c=B(z)−B(w).
Its source/extension isotropy is trivial, H_z={0}, and all extension phases are η=h−B(z)∈R with free translation.
This also covers isolated terminal points; terminal B is the empty sum, not a terminal step clock.

For any owner, a source state has nonunit isotropy exactly when its forward history is eventually periodic.
A nonzero self-meeting produces such an eventual cycle; conversely a tail reaching a least-p cycle supplies every isotropy lag mp, m∈Z.
Division by the least eventual period proves that these are all the lags. If K is the clock sum around that actual least cycle, the shared prefix cancels and
G_z^z={(z,mp,z):m∈Z}, c(z,mp,z)=mK, ENTIRE H_z=KZ.
For a non-eventually-periodic state isotropy is units and H_z={0}. M/N injectivity excludes off-cycle feeders; O does not have that simplification.
The potential telescopes around every cycle, so K=ΣΔ≥0. K=0 exactly when n=q at all cycle steps; for M this means d=1 at all such steps.
For N, H_z={0} for every state directly from its global potential, without a higher-period source census.
Extension isotropy at (z,h) is the zero-clock part of source isotropy: all pZ when K=0, only units when K>0, and units in the non-eventually-periodic case.
These exact structural alternatives apply to all objects; they do not enumerate or claim the existence of any period≥2 cycle.

For a source class choose an anchor a and actual arrows a→z with clocks b_z only to express coordinates.
The invariant η=h−b_z modulo H_a parametrizes all extension orbits over that class: changing a connecting arrow changes b_z by isotropy clock, and the converse follows by composing those arrows with isotropy.
This is not a global measurable-selector claim and discards no state or height. Translation acts by η↦η+t.
If H={0}, the physical action on that class is a free line; if H=KZ with K>0, it is one full circle packet of primitive K and repeats jK, j≥1.
Distinct source classes remain distinct physical packets even if their lengths coincide. Zero-clock source isotropy survives without creating a positive return.
For N one can take the concrete phase h+F(z), so its full extension orbit set is its source-orbit set times R and physical translation is free everywhere.

## 6. Complete GLOBAL fixed sets of all three owners

For every integer j≥1 let α_j=(√(j²+4)−j)/2. It lies in (0,1), satisfies 1/α_j=j+α_j, and hence has literal reciprocal digit j.
It is strictly decreasing in j because t↦1/t−t is strictly decreasing on (0,1).
It is irrational: for j≥2, j²<j²+4<(j+1)², and j=1 gives √5. Thus these points are not reciprocal-cut endpoints.
A fixed point must solve x=1/x−n and y=1/(q+y), so necessarily x=α_n and y=α_q. Its second reciprocal digit is then d=q.
This exhausts all positive solutions; axes are illegal sources, and no terminal identity is a map fixed point.

- M: q=n/d=n/q, hence n=q². Its complete fixed set is {f_q=(α_{q²},α_q):q≥1}.
- O: q=max(1,⌊n/q⌋). For q=1 this forces n=1; for q≥2 it forces q²≤n<q(q+1). Uniformly its complete fixed set is {g_{nq}=(α_n,α_q):q≥1, q²≤n≤q²+q−1}.
- N: q=n and d=q=n, so its own d|n test always holds. Its complete fixed set is {e_n=(α_n,α_n):n≥1}.

All converses pass the exact source and digit tests. This is an exhaustive unbounded integer parametrization, not a finite cell window or numerical census.
Every fixed point is in the open square; the retained cuts and boundary contribute no additional fixed point by the same equations.

## 7. M and N — entire fixed incoming classes and phases

At f_q, the inverse target data are Q=q, Y=α_q, D=q, so M's unique inverse uses n=q² and reconstructs f_q.
Therefore I_M^r({f_q})={f_q} for all r≥0: each whole fixed-core source class is a singleton, not a selected representative of a larger basin.
Its source isotropy nevertheless retains every integer lag k. Put
L_q=κ_M(f_q)=2 log(α_q/α_{q²}), so c(f_q,k,f_q)=kL_q and ENTIRE H=L_q Z.
For q=1, L_1=0: source and extension isotropy are Z, clock kernel is all these lag arrows, lag/joint kernels are units, and phase is all h∈R with free physical translation.
For q≥2, L_q>0: extension isotropy and clock/lag/joint kernels on that component are units; phase is h modulo L_q, one full primitive circle packet with repeats jL_q.
Distinct q label distinct source components and are not merged if their recorded lengths coincide.

At e_n, N's inverse target data are Q=D=n; D|Q holds and its only inverse is e_n.
Thus I_N^r({e_n})={e_n} for every depth. Its source isotropy is Z but κ_N(e_n)=0 and ENTIRE H={0}.
All source isotropy survives as extension isotropy at every height; the clock kernel is all lag arrows, lag/joint kernels are units, and every real phase is retained with no positive physical period.
The global N potential already proves H=0 beyond these cores, but does not enumerate its other source periodic data.

## 8. O — full fixed incoming trees, kernels, and multiplicity

Fix a legal pair (n,q) from Section 6; write a=α_n, b=α_q and S_q={q²,…,q²+q−1}.
At any target with second coordinate b, inverse data are Q=D=q and Y=b, so its complete O inverse alphabet is exactly S_q, including S_1={1}.
Define f_m(t)=1/(m+t). The entire fixed-core source class is precisely
C_{nq}={(f_{m_1}∘⋯∘f_{m_h}(a),b):h≥0, every m_i∈S_q}.
Every listed point passes its own O digit law, and inverse recursion shows that every finite-depth incoming point is listed. No closure or infinite-word completion is added.
These points have irrational first coordinate: each finite word is a nonsingular integer Möbius transformation of the irrational a.
The disjoint literal reciprocal cells recover each first digit; cancelling common prefixes proves two words give the same point exactly when their only extra suffix consists of copies of the core digit n.
Accordingly the empty word is the core; every other point has a unique canonical word with last digit different from n, whose length is its first-entry depth τ.
For depth h≥1 there are exactly (q−1)q^(h−1) distinct points. Thus q=1 has only its core, while each q≥2 core has its full countably infinite incoming tree.
Different (n,q) give disjoint source classes because a deterministic forward orbit cannot enter two distinct fixed cores.

Let A(z)=S_{τ(z)}(z) denote the prefix clock to the core, and let L=2 log(b/a)=κ_O(g_{nq}). Define β(z)=A(z)−τ(z)L.
For every z,w∈C_{nq} and every k∈Z there is exactly the actual triple (z,k,w); enough common fixed-tail iterations realize that lag.
Prefix cancellation gives the complete clock formula c(z,k,w)=kL+β(z)−β(w).
All source isotropy is Z even at nonperiodic incoming points; its clock image is ENTIRE H=LZ because the prefix cancels in every self-arrow.
The exact full fixed-basin kernels are therefore:

- ker lag: every (z,0,w), z,w∈C_{nq}.
- ker c: every (z,k,w) with kL+β(z)−β(w)=0.
- Joint kernel: every (z,0,w) with β(z)=β(w).

The potential is explicitly finite-word computable without science code. If the canonical word has length h and matrix
[[A_w,B_w],[C_w,D_w]]=∏_{i=1}^h [[0,1],[1,m_i]], then ∏_{j=0}^{h−1}x_j=1/(C_w a+D_w).
This follows by differentiating its Möbius composition, whose determinant has absolute value one, and comparing with the product of derivatives x_j².
Since the second coordinate remains b, A(z)=2 log[b^h(C_w a+D_w)] and β(z)=2 log[a^h(C_w a+D_w)]; the empty word has β=0.
These expressions make the displayed kernel tests exact equations for every finite word, not an assumption that all feeders have the core phase.

For q=1, necessarily n=1 and C_{11} is a singleton with L=0: source/extension isotropy Z, H={0}, real phase h, and no positive physical primitive.
For q≥2, n≥q²>q, so L>0. Extension isotropy is trivial at every incoming state and phase is h−β(z) modulo L.
The ENTIRE infinite incoming tree supplies one circle packet of primitive L and repeats jL, not one packet per feeder, chosen root, or phase.
Thus the positive fixed-packet ledger is the indexed multiset {2 log(α_q/α_n):q≥2, q²≤n≤q²+q−1}; equal numerical lengths, if any, retain their different (n,q) packets.
MAIN's corresponding indexed fixed ledger is {L_q:q≥2}; N has no positive fixed packet. No higher-period ledger is inferred from these families.

## 9. Decisive MAIN gate and nonclaims

MAIN's q=2 core is actual and has no other incoming state. Its positive primitive L_2 has
exp(L_2)=(α_2/α_4)²=(3−2√2)/(9−4√5).
This number is not rational. If it were r∈Q with r>0, then 4r√5−2√2=9r−3; squaring would make 16r√10 rational, contradicting irrationality of √10.
Therefore L_2 cannot equal log p for any ordinary integer prime p. Its status as the least positive generator of ENTIRE H has already been proved, not inferred from one clock sample.
The full MAIN positive ledger is nonempty but violates the frozen prime-log purity requirement: **STOP / FORK** on this owner's own fixed packet.
The O/N controls are separate results and supply no transferred negative credit. Unit/zero-clock cores, all finite-expansion states, every null boundary, and full incoming phases remain.
There is no claim of an all-period classification, all-prime coverage, global uniqueness at higher periods, new invariant reference measure, strong naturalness, novelty, or a universal no-go.
The same original area measure, maps, actual lag, analytic-germ clock version, extension time, and packet convention own every result above.
Classical NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED; formal UNASSIGNED; Route B NOT INVOKED. No round 460 is authorized.
Only this raw file was written. Card and CP1 remain unchanged, and no author surface has been accessed.

EOF — independent raw complete; freeze after full self-read and SHA256 receipt. HOLD for root's full read and DISTINCT PAPER UNLOCK.
