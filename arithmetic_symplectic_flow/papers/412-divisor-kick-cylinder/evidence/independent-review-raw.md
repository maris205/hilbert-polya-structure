# 412 independent raw proof — divisor-kick cylinder

Candidate `ANG-20260923-DKC01`; card-only mathematics after root's separate RAW RELEASE.
Sole scientific input: `candidate-card.md`, all 94 lines through EOF, SHA256 `ee718599f0ca4697601e212684056e47be13023dd21c9cf4d97423f8d0e5d925`.
Frozen CP1: `scope-review.md`, 56 lines, SHA256 `0aa28643b5b9190c4c0b13175648efacf108d5a2f4b349cbb9a5c7514c0123ec`.
Actual access: the complete frozen card was reread after release and its hash checked; the retained CP1 was hash-checked. No author manuscript, README, ledger, helper, peer, sibling proof, or other new scientific package was read.
Retained ARS/stream instructions and previous task history govern method/exposure only. Internal shared-history, inherited-model review is **NOT_CALIBRATED**, not blind or external peer review.
All arguments below are exact. No scientific code, numerical scan, external source, auxiliary delegation, fitted parameter, replacement measure, or higher-period census is used.

## 1. Full source cells and exhaustive own inverse atlases

Let `C=(R/Z)×R`, `X=N_0×C`, and `μ=#×Haar×dp`, with circle Haar normalized to mass one.
For positive integers d,q put n=dq and define the circle arc

`A_dq={θ:(d−1)/(dq)≤rep(θ)<1/q}`.                            (1)

The common legal source cells of MAIN T and K,V,H are `B_dq={dq}×A_dq×R`.
They partition the legal source: every n≥1 and θ determines exactly d=1+floor(n rep θ); legality is exactly d dividing n, after which q=n/d is unique.
All arcs include their lower digit cut and exclude their upper cut. For d=q=1 the arc is the whole circle. Every momentum, including zero and both signs, remains.
The other states remain terminal objects with identity histories and every actual incoming; no absorbing forward loop is added. In particular n=0 has no legal step.

For a target z=(m,β,v), set `θ=β−v mod1`. For each d,q≥1 define

`E_dq^F={m}×{(β,v):β−v mod1∈A_dq}`,
where `m=d+q` for T,K,V and `m=dq` for H.                   (2)

These are the COMPLETE actual target domains of the corresponding source cells. The own inverses are

`I_dq^T(z)=(dq,θ,d[v−sin(2πqθ)])`,
`I_dq^K(z)=(dq,θ,dv)`,
`I_dq^V(z)=(dq,θ,v−sin(2πqθ))`,
`I_dq^H(z)=(dq,θ,d[v−sin(2πqθ)])`, on its H target domain.   (3)

Indeed θ lies in A_dq exactly when its assigned floor digit is d at n=dq. Thus the inverse source is legal, and each own momentum formula gives output momentum v and angle θ+v=β. The own memory output agrees with (2).
Conversely a legal source lies in one unique B_dq. Its output recovers θ=β−v, and solving its own momentum equation gives (3). Both inverse identities, injectivity on each branch, and exhaustion follow.
Different branch descriptions cannot represent one predecessor: that predecessor's register and assigned digit determine d,q uniquely. The target images may nevertheless overlap across different predecessors.
For T/K/V the complete one-step enumeration at memory m≥2 is every d=1,…,m−1, q=m−d, with the test in (2); memories zero and one have no incoming.
For H at memory m≥1 the enumeration is every d dividing m and q=m/d, with the same own test; memory zero has no incoming.
All maps and domains are Borel. The per-target inverse enumeration is finite, with no artificial cutoff. A target lacking a predecessor keeps its own independently determined forward status.

H is in fact globally injective on its legal domain: at any fixed target memory m, θ=β−v determines the unique digit d=1+floor(m rep θ); there is one predecessor if d divides m, and none otherwise. This does not make H total or delete its terminals.

## 2. Full counting–cylinder IMAGE and prescribed point clocks

For fixed d,q the geometric inverse in (3) extends to a smooth diffeomorphism of the WHOLE cylinder C. Integer q makes the sine well-defined on R/Z.
Use local continuous angle lifts, never differentiate rep. Put `s'=2πq cos(2πqθ)`. The real derivative matrices for T/H, K, and V respectively are

`[[1,−1],[−d s',d(1+s')]]`,
`[[1,−1],[0,d]]`,
`[[1,−1],[−s',1+s']]`.

Their absolute determinants are, at EVERY actual target point,

`J_T=J_K=J_H=d`, `J_V=1`.                                  (4)

All are positive finite. These are derivatives of the prescribed cylinder extensions, including every seam and null digit cut, not derivatives of a discontinuous representative.
For completeness, the inverse factors into `(β,v)↦(β−v,v)` followed by `(θ,v)↦(θ,d(v−sin(2πqθ)))`, or its own K/V version. The first is a Haar-preserving shear; the second is a momentum translation and scaling by d for T/K/H, or translation alone for V.
Fubini and one-dimensional change of variables therefore prove the full-cylinder IMAGE, and restriction to every Borel E in (2) gives

`μ(I_dq^F(E))=∫_E J_F dμ`.                                 (5)

The fixed target register is sent bijectively to the fixed source register. Both singleton counting masses are one; no additional register determinant or index is present. Infinite measure is allowed in (5).
To distinguish overlapping images from multiplicities, for arbitrary Borel A in the legal domain define
`N_A(z)=Σ_dq 1_{E_dq^F}(z)1_A(I_dq^F z)`, with each summand zero outside its own domain.
Then `F(A)={N_A>0}` is Borel, `μ(F(A))=∫1_{N_A>0}dμ`, whereas
`∫N_A dμ=Σ_dq μ(F(A∩B_dq))=∫_A exp(κ_F)dμ`.                (6)
The latter is a multiplicity identity, not an assertion that branch image unions are disjoint.

Consequently the OWN signed step clocks are

`κ_T=κ_K=κ_H=−log d`, `κ_V=0`, on legal steps only.          (7)

For T/K/H a legal step has clock zero exactly when d=1. V has zero clock on every legal step. A terminal has no step clock, although its length-zero history has sum zero.
Negative step clocks are not replaced by positive roofs; physical return groups below use the actual signed cocycle and their own least positive generators.

## 3. All legal histories, full kernels, and entire isotropy

For T,K,H and every legal history length a≥0 put
`D_a^F(z)=∏_{j<a}d(F^jz)`, `D_0=1`, so `S_a=−log D_a`.
For V use the separate convention `W_a^V=1`; for the other owners set `W_a^F=D_a^F`. Thus in all cases `S_a=−log W_a`.
Use precisely the actual meeting triples

`G_F={(z,a−b,w):F^a z=F^b w, both histories legal}`,
`c_F(z,a−b,w)=log(W_b(w)/W_a(z))`.                          (8)

Length zero exists everywhere; a positive history may end at a terminal. Equal triples are identified, not labelled branch words.
Two witnesses of the same triple differ by a common increment in a,b. Their added legal future begins at the same meeting state, so the added log products cancel. This proves descent.
To compose arrows, extend the shorter of their middle histories to the longer legal one; the equality already present supplies the necessary corresponding extension on the other side. The middle sums cancel. Thus composition is legal even with finite terminal lifetimes, and c is additive with the correct inverse sign.
Finite-iterate equality loci are Borel. Finite incoming lists at each step give finite predecessor sets at each fixed depth and countable full source fibers.
Finite-history inverse charts have IMAGE `exp(−S_a)=W_a`; a branch-pair chart has range/source IMAGE `exp(−c_F)`. These follow from the own all-point chain products in (4)–(5), not a new almost-everywhere choice.

The COMPLETE global kernels, with actual meetings and legality required throughout, are

`ker c_F=⋃_{a,b}{(z,a−b,w):F^a z=F^b w, W_a(z)=W_b(w)}`,
`ker lag_F=⋃_a{(z,0,w):F^a z=F^a w}`,
`ker c_F∩ker lag_F=⋃_a{(z,0,w):F^a z=F^a w,W_a(z)=W_a(w)}`. (9)

They are exhaustive criteria, not selected subgroups. For V, `ker c_V=G_V` and the intersection is its whole lag kernel. Clock zero does not force zero lag or unit arrows.
For H, injectivity makes its lag kernel and hence the intersection consist exactly of units. Cancelling common iterates reduces every H arrow to one actual forward segment or its reverse; its clock is zero exactly when every digit in that segment is one. This also retains all actual all-d=1 cyclic isotropy, without a cycle census.
The extension retains ALL X×R_h, with `(w,h)→(z,h+c_F)`. Its corresponding kernels are the full lifted ones.

A source has nonzero isotropy if and only if its actual forward history is eventually periodic: a nonzero meeting lag repeats a full state, and any such repeat supplies a legal cycle. Let k be the eventual least source period and let

`D_C=∏_{j=0}^{k−1}d(f_j)` for T,K,H, and `D_C=1` for V.

Then source isotropy is exactly kZ, its clock on jk is `−j log D_C`, and

`H_z=(log D_C)Z`,
`extension isotropy=kZ if D_C=1, and units otherwise`.      (10)

Transient products cancel; all multiples of k occur and no smaller nonzero source lag can occur. If the point is not eventually periodic, source and extension isotropy are units and H={0}, including every terminal-ending history.
For D_C>1 the physical least positive return is log D_C, with repetitions j log D_C, j≥1. For D_C=1 there is no positive primitive, but source/extension isotropy kZ remains.
Every actual T/K cycle has D_C>1: an all-d=1 cycle would change memory n to n+1 at every step, which cannot close. This is an equality-case argument, not a higher-period census.
For H, a cycle has zero clock exactly when every cycle digit is one. Since H is injective, eventual periodicity is already periodicity: the unique predecessor of each cycle point is its preceding cycle point, so a transient cannot enter it. No higher H cycle locations are asserted.
For V, H_z={0} at EVERY source, while source/extension isotropy may still be nonzero at eventual cycles. No absence-of-cycles conclusion follows from zero clock.

## 4. Complete MAIN, K, and V fixed sets

For these three owners a fixed memory obeys `dq=d+q`, equivalently `(d−1)(q−1)=1`. Thus d=q=2 and n=4, with assigned angle

`1/4≤rep θ<1/2`.                                          (11)

A fixed momentum must equal its output v, and the angle equation requires this same real momentum to be an integer k. These conditions are necessary and sufficient when combined with the own momentum law.
For MAIN they give `sin(4πθ)=k/2`. On (11) the sine argument traverses [π,2π), so the sine is nonpositive. The COMPLETE fixed set is therefore

`f_0=(4,1/4,0)`,
`f_−=(4,7/24,−1)`, `f_+=(4,11/24,−1)`,
`f_2=(4,3/8,−2)`.                                        (12)

Indeed k can only be 0,−1,−2; k=0 has the retained lower endpoint 1/4 but not the excluded upper endpoint 1/2; k=−1 has exactly the two displayed roots; k=−2 has exactly 3/8.
All four satisfy the original digit, divisibility, momentum, and circle equations. Their own signed clock is −log2, source isotropy is Z, extension isotropy is trivial, and ENTIRE H is (log2)Z.

For K the own fixed momentum equation is `k=k/2`, so k=0 and no angle condition remains beyond (11):

`Fix(K)={(4,θ,0):1/4≤rep θ<1/2}`.                          (13)

Every point has own J=2 and the same source/extension isotropy and entire H=(log2)Z. This is a full interval of cores, not a chosen centre.
For V the own equation is `sin(4πθ)=0`, while every integer k remains allowed:

`Fix(V)={(4,1/4,k):k∈Z}`.                                 (14)

Each has its OWN J=1, clock zero, H={0}, and source/extension isotropy Z. The full positive and negative momentum ladder is retained; none is a positive physical primitive packet.

## 5. Complete MEMORY-HOLD fixed set

H imposes no equation n=d+q. Write n=dq, put `t=q rep θ`, and let p=k∈Z as required by the angular fixed equation. The COMPLETE fixed conditions are

`1−1/d≤t<1`, `sin(2πt)=(d−1)k/d`,
`(n,θ,p)=(dq,t/q,k)`.                                    (15)

They are necessary by the assigned digit and momentum equations and sufficient by direct substitution into H. All d,q are positive integers.
For d=1 the sine must vanish on [0,1). This gives the complete zero-clock fixed family

`U={(q,σ/(2q),k):q≥1, σ∈{0,1}, k∈Z}`.                     (16)

It includes the circle seam and all integer momenta. Every such core has source/extension isotropy Z, H={0}, and all real physical phases. The own inverse of a fixed H point is only itself.

For d=2 equation (15) gives exactly the four pairs

`(t,k)∈{(1/2,0),(7/12,−1),(11/12,−1),(3/4,−2)}`,
with `(n,θ,p)=(2q,t/q,k)` for EVERY q≥1.                   (17)

For d≥3 the interval in (15) lies strictly between 1/2 and 1, so its sine is negative and nonzero. The bound `|k|≤d/(d−1)<2` forces k=−1.
Put `u=1−t∈(0,1/d]`; then the remaining equation is

`sin(2πu)=(d−1)/d`.                                      (18)

For d=3 its ascending root is in (0,1/4), while the descending root lies beyond 1/3: the endpoint sine is sqrt(3)/2>2/3. Thus only the ascending root is allowed.
For d=4,5,6 sine is strictly increasing on (0,1/d]. Its endpoint is respectively 1, at least sqrt(3)/2, and sqrt(3)/2, each strictly exceeding (d−1)/d. Hence each case has exactly one allowed root.
There are no d≥7 roots. Concavity of sine on [0,π/2], with its tangent at π/4, gives
`sin(2π/7)≤(sqrt(2)/2)(1+π/28)<4sqrt(2)/7<6/7`.
Here π<4 follows, for example, from `π/4=∫_0^1(1+x²)^(−1)dx<1`; the last inequality is the exact square comparison 2<9/4. For d≥7, every allowed u has `sin(2πu)≤sin(2π/7)<6/7≤(d−1)/d`, excluding (18).
Thus, in addition to (16)–(17), the COMPLETE H fixed set consists exactly of

`(dq,[1−arcsin((d−1)/d)/(2π)]/q,−1)`,
`d∈{3,4,5,6}`, `q≥1`,                                    (19)

where arcsin is its principal value in (0,π/2). All angle predicates were checked above; no root or endpoint is selected away.
Every core in (17)–(19) has OWN signed clock −log d, source isotropy Z, trivial extension isotropy, and entire H=(log d)Z. The derivation excludes every other fixed momentum, angle, and register without numerical cutoffs.
Distinct parameters recover distinct source states: the memory and angle recover the assigned digit d and quotient q, then t and k. In particular equal-time cores are not merged.
The positive FIXED-sector multiplicity of H is countably infinite at each of log2, log3, log4, log5, log6, and zero at every other positive length. This concerns fixed cores only, not a classification of higher-period packets.

## 6. Complete incoming, fixed basins, and all phases

For any target z define `Pred_0(z)={z}` and let `Pred_{a+1}(z)` be the union of ALL own inverses (3) of every point in Pred_a(z), with their exact tests (2).
This gives every finite incoming layer, not arbitrary inverse words. The full source orbit is

`Orb_F(z)=⋃_{b≥0:F^b z legal} ⋃_{a≥0} Pred_a(F^b z)`.        (20)

Every actual meeting triple supplies such an ancestor of a forward iterate, and conversely every term supplies a triple. This includes terminal endpoints, infinite nonperiodic histories, and all unclassified higher-cycle basins.
For a fixed core f its full source orbit is precisely its basin `B_f=⋃_a Pred_a(f)`, since its only future is f. Distinct fixed cores have disjoint basins because their constant futures cannot meet.

For clarity the full first layer at every T/K/V fixed core is explicit. At target (4,θ,k), with the relevant fixed θ and integer k, the recovered angle is θ. The only possible branch indices are (d,q)=(1,3),(2,2),(3,1).
The self branch (2,2) is always present; (3,1) is never present at these fixed angles; (1,3) is present exactly when rep θ<1/3, including the lower fixed endpoint 1/4.
For MAIN this gives exactly one extra predecessor `(3,1/4,1)` of f_0 and one extra predecessor `(3,7/24,−1+sqrt(2)/2)` of f_−. The other two fixed cores have no nonself predecessor.
For K it gives the extra `(3,θ,0)` precisely at `1/4≤rep θ<1/3`; elsewhere the only predecessor is self.
For V every fixed `(4,1/4,k)` has exactly the extra predecessor `(3,1/4,k+1)` in addition to itself.
Every target of memory three has exactly one T/K/V predecessor of memory two: at recovered angle α=β−v choose (d,q)=(1,2) for rep α<1/2 and (2,1) otherwise. These two arcs partition the entire circle, with the seam and lower cut assigned.
Every target of memory two has exactly one such predecessor of memory one, using d=q=1 on the whole circle. Memories zero and one have no predecessors. Each momentum is exactly its own formula (3).
Consequently MAIN's f_0 and f_− each have exactly four states in their basin; f_+ and f_2 have singleton basins. K has four-state basins when θ<1/3 and singleton basins otherwise. Every V fixed core has a four-state basin. This is the entire fixed incoming ledger, not a depth truncation.
For H, global injectivity and the self predecessor imply that EVERY fixed basin is a singleton. All other H incoming histories remain governed by (2)–(3) and (20).

For an arbitrary source orbit choose a reference o and an actual arrow g:z→o. All extension phases are `h+c_F(g) mod H_o`: choices differ exactly by reference isotropy, and composing that isotropy realizes every subgroup adjustment.
For a fixed basin, if F^a z=f, the arrival arrow is `(f,−a,z)`, with clock `−S_a(z)`. Its exact phase is

`h−S_a(z)=h+log W_a(z) mod H_f`.                            (21)

Different arrival times add fixed-cycle clocks and hence give the same phase class. For an eventual cycle f_j=F^j f_0, arrival F^a z=f_j gives `h+S_j(f_0)−S_a(z) mod H_o`, with the same orientation.
Height translation is ordinary addition on R/H_o. Thus each fixed basin with nonzero H supplies ONE full physical circle packet, all phases, and every integer repetition; different basins remain different packets even at the same length.
Zero-clock fixed basins retain source/extension Z and all phases on a free R line, not a positive primitive. Off eventual cycles H=0 but source isotropy is trivial. These are distinct cases and both remain in the full source ledger.
The COMPLETE positive FIXED-sector multiplicities are: MAIN four at log2; K continuum many at log2; V none; H as stated after (19). No other positive fixed-sector lengths occur. Higher-period multiplicities are not inferred from this fixed census.

## 7. Decisive gate, lineage, and stop

MAIN itself owns four distinct fixed basins with ENTIRE H=(log2)Z, so each has actual least positive time log2. Incoming cannot shorten this generator or merge the basins, and the signed clock −log2 is not rescaled.
The necessary target permits at most one actual packet per ordinary prime. These four MAIN packets therefore decide **STOP / FORK by duplicate prime-2 packets**. This is neither a control-based inference nor an empty-window argument; MAIN's positive ledger is nonempty.
The retained seam/cut convention matters: f_0 uses the actual lower digit face. No such point is discarded or assigned a different clock. The other three fixed cores are retained with their negative momenta.
For each proper-divisor strip specified in the card, the floor readout is exactly d for every real p, so its MAIN permission is precisely d dividing n. Its actual q drives the sine, and the full updated state is reread. This proves the stated divisor-symbolic-to-geometric feedback mechanism, not strong naturalness or a prime-only filter.
All four owners keep the same-object ledger intact. Strong naturalness and arbitrary-encoding risks remain OPEN. Classical fields are NOT APPLICABLE; T3 NOT AUDITED, formal Route UNASSIGNED, Route B NOT INVOKED.
No higher-period census, invariant probability, trace/zeta/operator, global all-prime coverage, new candidate, or round 415 is supplied or started. The integer bound in the H fixed proof is an exact exhaustion theorem, not scientific numerics.

EOF — DKC01 card-only raw complete; preserve this evidence and HOLD for root's full read and separate PAPER UNLOCK.
