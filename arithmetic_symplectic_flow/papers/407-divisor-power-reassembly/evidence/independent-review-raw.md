# 407 independent raw proof — divisor-power reassembly

Candidate `ANG-20260923-DPR01`; card-only exact mathematics after root's separate release.
Sole scientific input: `candidate-card.md`, all 105 lines, SHA256 `52ad8cc8d271c49317cf7245aed09ef3d421d2245b3b091c0f6c5054c96b25a1`.
Frozen CP1: `scope-review.md`, 56 lines, SHA256 `ba0b1daa99dd6cb23b93b1a88ae24cf99ecfee449e9503a3d7766cf062a7b6ad`.
Actual scientific access: the card reread in full through line 105, its blank final line and actual EOF. No Paper, README, Ledger, author result, helper proof, or peer output was read.
Retained ARS and stream instructions govern method only. Shared history and inherited model: internal **NOT_CALIBRATED**, not blind or external peer review.
No scientific code, numerical scan, external source, auxiliary delegation, new carrier, measure fitting, or higher-period census is used.

## 1. Full domains and complete inverse atlases

The carrier remains `X=N_0×[0,1]²`, with counting-times-two-dimensional Lebesgue measure.
For n≥1 and x,y<1, `d=1+floor(nx)` lies in `{1,…,n}`, and `r=nx−(d−1)` lies in `[0,1)`.
MAIN/L/H require r>0 and d dividing n, with q=n/d; G requires r>0 but uses q=floor(n/d), without divisibility. Thus every actual q is a positive integer.
For each owner, `e=1+floor(qy)∈{1,…,q}` and `s=qy−(e−1)∈[0,1)`.
The source digit cells are disjoint; r=0 is terminal but s=0 is legal. All forbidden steps retain their objects, identities, and actual incoming histories.

Write `V_d=[(d−1)/d,1)` and `E_m,d={m}×(0,1)×V_d`.
For MAIN and each d,q≥1, 1≤e≤q, the target register is m=d+e and the complete inverse domain is exactly E_m,d, with

`I_dqe(m,u,v)=(dq,(d−1+u^(1/q))/(dq),(e−1+s)/q)`,
`s=dv−(d−1)`.                                                (1)

Indeed r=u^(1/q) belongs to (0,1); multiplying its source x by dq recovers d−1+r and therefore its exact floor digit d.
The proposed source y lies in `[0,1)` and has qy=e−1+s with s∈[0,1), so its exact second digit is e, including s=0.
The register dq makes MAIN's divisibility test automatic. Substitution in the forward map returns `(m,u,v)`.
Conversely each actual predecessor uniquely recovers d,q,e and its positive r, hence (1). There is no hidden further exclusion within E_m,d.

L has the SAME allowed integer triples and domains E_m,d, but its OWN inverse is (1) with r=u in place of u^(1/q).
H has target register m≥1, source register n=m, and enumerates every d dividing m, q=m/d and 1≤e≤q.
Its inverse geometry is (1), with dq=m; its target domain is E_m,d, without imposing m=d+e. There is no H predecessor to register zero.
G enumerates every n≥1, 1≤d≤n, q=floor(n/d), 1≤e≤q, m=d+e, and has the OWN inverse

`I_nde^G(m,u,v)=(n,(d−1+u^(1/q))/n,(e−1+s)/q)` on E_m,d.       (2)

The same floor and remainder checks prove (2) necessary and sufficient; no equation n=dq is introduced.
Every inverse branch is injective and Borel. Its displayed target rectangle is Borel, and its coordinate functions are continuous there.
Different actual predecessors cannot be duplicate branch descriptions: the source register and its assigned floor digits determine all branch indices uniquely.
For MAIN/L and G, a fixed target can require an unbounded register/quotient enumeration; the formulas include it without a cutoff.
The terminal boundaries n=0, x=1, y=1, and x=0 have no nonidentity incoming and no forward steps, since actual images have positive register, first coordinate in (0,1), and second coordinate below 1.
Other illegal digit-cut or divisibility states can have incoming and are not deleted. Target y=0 is fully allowed when d=1 and s=0.

## 2. Owned all-point IMAGE and signed step clocks

On any fixed branch, differentiate the displayed inverse extension in u>0 and v. For MAIN/H,

`dx/du=u^(1/q−1)/(d q²)`, `dy/dv=d/q`,
`J_MAIN=J_H=q^(−3)u^(1/q−1)`.

L instead has `dx/du=1/(dq)` and therefore `J_L=q^(−2)`.
G has `dx/du=u^(1/q−1)/(nq)` and therefore `J_G=d/(nq²)·u^(1/q−1)`.
All off-diagonal derivatives vanish. These are the OWN two-dimensional determinants; equal expressions do not identify different owner domains.
Every J is positive finite at every actual point, including v=(d−1)/d, where s=0. A possible limiting divergence as u tends to zero does not create a value at u=0, which is not an actual inverse point.
On its open analytic extension each inverse is a diffeomorphism onto its image; ordinary change of variables applies to every Borel subset of E_m,d, including boundary subsets.
The fixed target register m is sent bijectively to the fixed source register n. The corresponding counting factor is exactly one, not m/n, n/m, or a continuous register derivative.
Thus, for EVERY Borel E in a complete actual branch domain,

`μ(I(E))=∫_E J dμ`.                                         (3)

This proves full counting-times-Lebesgue IMAGE, not just a density with an unexamined register. All prescribed face values come from the analytic extension; none is patched.
Different source cells are disjoint, so preimage identities may be summed with their proper indices. Overlapping forward branch images are unions, not an uncorrected sum of their measures.

For a legal state ξ=(n,x,y), its OWN step multiplier W=exp(κ)=1/J(Fξ) is

`W_MAIN(ξ)=W_H(ξ)=q³r^(q−1)`,
`W_L(ξ)=q²`,
`W_G(ξ)=(nq²/d)r^(q−1)`.                                   (4)

All are positive finite. The logarithm can be signed; no one-step clock is assigned to a terminal.
In particular q=1 steps of MAIN/L/H have clock zero without deleting their retained lags or actual states. G's q=1 clock is instead log(n/d), calculated from its own domain and density.

## 3. Full generic-history, kernel, isotropy, and phase ledger

For one specified owner F and every legal length a≥0, put

`P_a^F(ξ)=∏_{j=0}^{a−1} W_F(F^j ξ)`, `P_0=1`, `S_a=log P_a`.
`G_F={(ξ,k,η): ∃ legal a,b≥0, k=a−b, F^aξ=F^bη}`,
`c_F(ξ,k,η)=log(P_a^F(ξ)/P_b^F(η))`.                         (5)

The weights in (4), not supplied prime labels, make (5) explicit for all four owners and every finite legal history.
Equal triples are one arrow. Two presentations of the same actual triple have the same lag and differ by a common increment of a,b; their added legal tail is the same, so its contributions cancel.
Composition aligns the two legal middle histories at their longer meeting time and cancels their shared sum. This proves descent and additivity without extending a terminal beyond its lifetime.
Legal finite-iterate equality sets are Borel. The inverse index sets are countable, hence the actual arrow fibers are countable. No free digit-word or infinite-history extension is used.

The COMPLETE global kernels, with legality and actual meetings imposed throughout, are

`ker c_F=⋃_{a,b}{(ξ,a−b,η):F^aξ=F^bη, P_a^F(ξ)=P_b^F(η)}`,
`ker lag_F=⋃_a{(ξ,0,η):F^aξ=F^aη}`,
`ker c_F∩ker lag_F=⋃_a{(ξ,0,η):F^aξ=F^aη, P_a^F(ξ)=P_a^F(η)}`. (6)

These exact product conditions include non-isotropy arrows; equality of products alone does not enlarge the source relation.
The full real extension sends `(η,h)` to `(ξ,h+c_F(ξ,k,η))`. Its corresponding kernels are the full lifts of (6).
Forward arrival `F^aη=ξ` is `(ξ,−a,η)`, with clock `−S_a(η)`; the inverse-history direction has clock `+S_a(η)`.

Nonzero source isotropy is equivalent to eventual arrival at a legal cycle: a repeated forward state produces a repeatable segment, and the converse supplies every multiple of the least cycle period.
If the eventual cycle has least source period p and full product `A=∏_{j=0}^{p−1}W_F(f_j)`, then

`G_{F,ξ}^ξ=pZ`, `H_ξ=(log A)Z`,
`extension isotropy=pZ if A=1, and units otherwise`.          (7)

If there is no eventual cycle, source and extension isotropy are units and H={0}. A terminating history cannot acquire isotropy from alternative incoming branches.
For A≠1 the least positive physical return is `|log A|`, with all repetitions `j|log A|`, j≥1. For A=1 there is no positive generator, although the source and extension isotropy survives.
This is an all-state conditional characterization, not a census of higher-cycle locations. It also accounts for the entire remainder outside the fixed basins below.
For L, specifically, A is the square of the integer product of the actual cycle q values. A cycle cannot have every q=1, since each such L step changes n=d to n+1. Hence every existing L cycle has A>1; no locations or counts are inferred from this fact.

For every target u define `Pred_0(u)={u}` and form `Pred_{a+1}(u)` from ALL own inverse branches of every state in `Pred_a(u)` whose exact domains are satisfied.
This is the full finite-incoming ledger. The whole source orbit of u is `⋃_{a,b≥0}Pred_a(F^b u)`, over all legal b.
For a reference o in a source orbit, all actual arrows g:ξ→o give the single phase coset `{h+c(g)}` modulo H_o. Two choices differ by isotropy, and composing isotropy realizes every element of that coset.
Thus the entire height-translation orbit is R/H_o. This means a circle of least time `|log A|` when A≠1, or a free line when H=0; it is a statement about the orbit SET, not a claimed smooth or invariant-measure quotient.

## 4. Scalar fixed equations used without numerical root selection

For a power owner at a fixed state, x=r^q and nx=d−1+r, so

`n r^q−r=d−1`, `0<r<1`.                                    (8)

For MAIN/H with n=dq and q≥2, denote the unique solution by ρ_dq.
Existence and uniqueness are exact: dividing (8) by r gives `dq r^(q−1)−1−(d−1)/r=0`, a strictly increasing function on (0,1).
Its limit at zero is negative (−1 for d=1, minus infinity for d>1), and its value at one is d(q−1)>0.
In particular `ρ_1q=q^(−1/(q−1))`. No finite or approximate root test is used.

Every fixed second coordinate, for any of the four owners, must satisfy

`(d−q)y=d−e`, `y∈V_d=[1−1/d,1)`, `s=dy−(d−1)`.             (9)

These conditions are also sufficient for its assigned second digit: `qy=e−1+s` with `0≤s<1`.
They preserve the lower boundary s=0 and exclude the terminal upper boundary y=1.

## 5. COMPLETE MAIN fixed set and its exact fixed-sector packets

MAIN's fixed register gives `dq=d+e`, hence `e=d(q−1)∈{1,…,q}`.
There is no q=1 solution. For q=2, d is 1 or 2; for q≥3, necessarily d=1.
For d=1 and every q≥2, (8)–(9) give the single core

`f_q=(q, q^(−q/(q−1)), (q−2)/(q−1))`.                       (10)

Its second remainder equals y and lies in [0,1); q=2 therefore retains the legal s=0 boundary point.
For d=q=2,e=2, put

`ρ=(1+sqrt(17))/8`, `ρ²=(9+sqrt(17))/32`.

The remaining COMPLETE family is

`g_t=(4,ρ²,t)`, `1/2≤t<1`.                                 (11)

Indeed (8) is `4ρ²−ρ−1=0`, and (9) is an identity precisely on this entire allowed second-digit interval.
There are no other fixed states: the register alternatives above are exhaustive, (8) has the stated unique legal roots, and (9) supplies all y values.
Every state listed is legal under the original floor/divisibility checks; no terminal is counted as a fixed forward step.

Using MAIN's OWN (4),

`κ(f_q)=log(q³ρ_1q^(q−1))=2log q`,
`κ(g_t)=log(8ρ)=log(1+sqrt(17))=:L_*`.                       (12)

All these clocks are positive. At every listed fixed core source isotropy is the full Z, extension isotropy is trivial, and the entire H is its displayed clock times Z.
Distinct fixed cores have disjoint full source basins. Thus in the FIXED-CORE sector there is exactly one packet at each time 2log q, q≥2, and continuum many at L_*.
There is no collision between these two types: q² is an integer, whereas 1+sqrt(17) is not. Other fixed-sector lengths have multiplicity zero.
This does not prohibit additional higher-period packets at any of these lengths; they are outside the frozen census.

## 6. COMPLETE POWER-OFF fixed set

L's fixed register has the same two integer alternatives as MAIN, but its OWN first equation is x=r, so `(n−1)x=d−1`.
For d=1,n=q≥2 it forces x=0 and r=0, which is illegal. These proposed fixed points are not repaired by adding a terminal self-loop.
For d=q=2,n=4 it forces x=1/3; (9) leaves exactly `1/2≤y<1`.
Consequently

`Fix(L)={(4,1/3,t):1/2≤t<1}`.                               (13)

Every point is legal, with r=1/3. Its OWN density q^(−2) gives κ=log4, H=(log4)Z, source isotropy Z, and trivial extension isotropy.
The fixed sector has continuum many distinct full packets at log4, with all phases and repetitions, and no other fixed packets.

## 7. COMPLETE MEMORY-HOLD fixed set, including the unit sheet

H keeps n, so no equation n=d+e may be imposed. Write n=dq using its own permission.
For q=1, d=n and the first equation is `(n−1)x=n−1`. If n>1 it forces the terminal x=1, so there is no legal fixed point.
If n=d=q=1, however, the WHOLE legal sheet is fixed:

`S_0={(1,x,y):0<x<1, 0≤y<1}`.                               (14)

Here e=1,r=x,s=y and H acts as the identity. Its OWN J=1 gives clock zero, H_ξ={0}, source isotropy Z, and extension isotropy Z at every real height.
The own inverse atlas at register one has only d=q=e=1, so each of these fixed source cores has no other point in its source orbit; its complete physical phase set is a free R line, not a positive primitive packet.
This positive-area sheet is retained, including y=0, and is not used to infer any MAIN obstruction.

For q≥2 the first coordinate is exactly `x=ρ_dq^q`, with ρ_dq from Section 4.
To solve (9) completely, write `a=1−y∈(0,1/d]`; then `e=q+(d−q)a`.
If d>q this is greater than q and impossible. If d=q it forces e=q and leaves the entire interval V_d.
If d<q, put k=q−e=(q−d)a. Then k is an integer satisfying `1≤k≤floor(q/d)−1`; such values exist exactly when q≥2d.
The remaining COMPLETE H fixed set is therefore the disjoint union of

`h_d,t=(d²,ρ_dd^d,t)`, `d≥2`, `1−1/d≤t<1`,                 (15)
and
`h_dqk=(dq,ρ_dq^q,1−k/(q−d))`,
`d≥1, q≥2d, 1≤k≤floor(q/d)−1`.                             (16)

For (16), e=q−k and `s=1−dk/(q−d)∈[0,1)`, verifying every boundary and second-digit predicate.
Each actual fixed state recovers n,d,q and its y, hence these parameters do not create duplicate source states. Different divisors for the same n occupy different source digit cells.
At every core in (15)–(16), its OWN positive step multiplier is

`A_dq=q³ρ_dq^(q−1)=(q²/d)(1+(d−1)/ρ_dq) ≥ q²>1`,            (17)

with equality in the first inequality exactly when d=1. Thus these and only these H fixed cores have positive primitive time log A_dq.
Their source isotropy is Z, extension isotropy is trivial, and their entire H=(log A_dq)Z. Their full phases are the corresponding circles.
All possible same-time coincidences are retained by the exact fixed-sector multiplicity formula

`m_H(L)=# { (d,t): d≥2, t∈V_d, log A_dd=L }`
`       +# { (d,q,k): d≥1, q≥2d, 1≤k≤floor(q/d)−1, log A_dq=L }`, `L>0`. (18)

Here # denotes cardinality and addition is cardinal addition, so any realized diagonal interval contributes continuum many distinct packets.
For example the d=1 terms already supply q−1 distinct fixed cores at time 2log q; other parameters with an equal time are not removed or silently identified.
The zero-clock sheet (14) contributes no positive primitive to (18) but keeps its entire ineffective isotropy and all phase lines.

## 8. COMPLETE DIVISIBILITY-OFF fixed set

G must be solved with q=floor(n/d), not n=dq. The fixed register gives e=n−d and `1≤n−d≤floor(n/d)`.
For d=1, n≥2 is arbitrary and q=n,e=n−1, yielding exactly the cores f_n in (10).
For d≥2 the inequality implies `(d−1)n≤d²` and n≥d+1. Thus d=2 permits n=3 or 4, while d≥3 permits only n=d+1.
Whenever n=d+1 (d≥2), q=e=1, and (9) forces y=1, an excluded forward step. These terminal states are retained but are not fixed points.
The sole remaining case is d=2,n=4,q=e=2, which gives exactly the family g_t in (11).
Therefore the complete G fixed set happens to equal MAIN's (10)–(11), as a subset of the full carrier.
At every one of these fixed cores n=dq actually holds, so G's OWN multiplier `(nq²/d)r^(q−1)` equals the separately proved values in (12).
Its own fixed-sector H, source/extension isotropy, phase circles, and multiplicities follow accordingly, with its OWN full inverse histories.
This equality on the fixed loci is not an identification of the full maps, inverse domains, or source basins. The discarded-divisibility states remain in G's full owner and its generic ledger (4)–(7).

## 9. Entire fixed basins, incoming phases, repetitions, and decision

For any listed fixed core f of one specified owner, its full source orbit is exactly

`B_f=⋃_{a≥0}Pred_a(f)={ξ:F^aξ=f for some legal a}`.            (19)

A common future with f must equal f, because its forward orbit is constant. This proves both inclusions and retains every checked incoming layer.
Every ξ∈B_f has full source isotropy Z and H_ξ=κ(f)Z, not a subgroup chosen from one inverse branch.
If κ(f)≠0, extension isotropy is trivial and the entire basin makes ONE primitive height-translation packet with all phases `R/(|κ(f)|Z)` and repetitions j|κ(f)|, j≥1.
If κ(f)=0, extension isotropy remains Z and all phases form the unquotiented real line; there is no positive primitive.
For any hitting time a, the exact phase coordinate is `h−S_a(ξ) mod κ(f)Z`. Additional time at f changes it only by that subgroup, so no incoming path shortens the positive primitive.
Two distinct fixed cores cannot have meeting constant futures, so their basins and packets are distinct even when their clocks agree.
Equations (1)–(2) and the own L/H substitutions give every first predecessor, and the recursion in Section 3 gives every deeper legal predecessor without selecting representatives.
Explicitly, at a fixed target `(m,u,v)`, MAIN/L take every `1≤d≤m−1`, `e=m−d`, and ALL `q≥e` with `v∈V_d`; G instead takes ALL `n≥d` with `floor(n/d)≥e` and uses its own formula (2). H takes all `d|m`, `q=m/d`, `1≤e≤q`, with `v∈V_d`.
The generic product and eventual-cycle formulas also retain all non-fixed-basins, higher-cycle basins if any, infinite nonperiodic histories, terminal classes, and their phases. No claim of absence is substituted for an unclassified locus.

The simplest MAIN witness is the fully legal fixed point

`f_2=(2,1/4,0)`, with `d=1,q=2,e=1,r=1/2,s=0`.

Its MAIN two-dimensional inverse density at the target is `2^(−3)(1/4)^(−1/2)=1/4`, so the ENTIRE H is `(log4)Z` and its primitive time is log4.
Since 4 is not an ordinary integer prime, this actual MAIN packet decides the necessary-target failure. Its legal s=0 face cannot be deleted or assigned a replacement density.
The full MAIN family (11), mandated by complete fixed-set auditing, independently has nonprime multiplier 1+sqrt(17) and continuum equal-time multiplicity; it is not a separate prime-time multiplicity example.
No control is used in place of MAIN's direct counterexample, and no global coverage or empty-window inference is needed.

For the declared lineage, every `1<d<n`, `(d−1)/n<x<d/n`, and `0≤y<1` has precisely that first digit and positive r. MAIN permission there is exactly d dividing n; when allowed, the quotient sets both the power and the next digit grid.
The resulting geometry and second digit determine the written-back register. This proves the stated deformation, not strong naturalness, a prime detector, or a conservative realization.
Portfolio: **STOP / FORK — owned all-point IMAGE clock, but a wrong positive MAIN fixed primitive.**
The same-object ledger remains intact. Strong naturalness and encoding risks remain OPEN; classical NOT APPLICABLE, T3 NOT AUDITED, formal Route UNASSIGNED, B NOT INVOKED.
No higher-period census, tuning, prime table, replacement roof, operator, new candidate, or sixth round is started.

EOF — DPR01 clarified-scope card-only raw complete; await root's full read and separate PAPER UNLOCK.
