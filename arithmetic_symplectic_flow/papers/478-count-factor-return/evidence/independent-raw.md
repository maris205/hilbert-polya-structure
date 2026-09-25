# CFR01 — card-only independent derivation

Candidate: ANG-20260925-CFR01. Date: 2026-09-25. Stage: released original-card mathematics, before manuscript access.
Disposition: the owner is well defined; MAIN has countably infinitely many distinct fixed-origin primitive packets of length log 2. The frozen duplicate-prime gate therefore gives STOP / FORK, not arithmetic admission.
Internal same-model/shared-history work, NOT_CALIBRATED; not blind, external peer review or independent-error validation.

## 1. Inputs, chronology and method

The sole newly read scientific input is `candidate-card.md`, original lines 1–103 through EOF: 103 lines, 5,451 bytes, SHA-256 `0ed468c07a3ccf3f84806aa5bfbabe89ad12b08cc716c465e3bc0093e012fc03`. It was reread in full and measured after DISTINCT RAW RELEASE. The prior 53-line CP1 report, SHA-256 `31a538ca40f347e37ad993a0540c769ca56d23d2e76f4b6b6034b77a220ec47d`, remains unchanged; root reported reading it fully before this release.

ARS 3.22.0 router was refreshed in full, lines 1–250/251–488 EOF. The previously fully read deep-research workflow, DA, runtime, fallacy and anti-leakage instructions and local AGENTS/plan remain applicable; their exact reads are recorded in CP1. This task uses direct elementary proofs, not an external theorem or numerical experiment. Extensive older research history is inherited but no old proof was reread or substituted for this card's derivation.

No manuscript, README, claim ledger, appended outcome, peer/helper result or other candidate scientific file was read. No auxiliary, browser, scientific code/numerics, Git or PDF was used. Only this new raw report is written. CP2/manuscript comparison and CP3/final-surface review have not occurred. Root must read this frozen raw before a distinct PAPER UNLOCK.

## 2. Full domains and exact inverse fibres

Write E={(0,0,u):0≤u≤1}, Y=X\E. Every owner is a single-valued Borel map on all Y; every image is in Y. Thus D₀=X, Dᵣ=Y for r≥1. E has no incoming arrow from another point and no legal positive iterate; its states are terminals, not fixed loops. All nonempty count states, including units and axes, have a legal next step for every u.

For targets y=(c,d,v) with c,d∈N₀ and v∈[0,1], the following is the COMPLETE one-step inverse table. Rows are individual actual sources, not a summed branch density. An absent row contributes nothing.

| Owner and side | Counts (a,b) | Required count conditions | Recovered u and target interval |
| --- | --- | --- | --- |
| M/C red | (c−d,d) | c>d≥0 | u=pv; v∈[0,1) if d>0, v∈[0,1] if d=0 |
| A red | (c,d) | c>0,d≥0 | u=pv; v∈[0,1) if d>0, v∈[0,1] if d=0 |
| M/A blue factor | (cd,c) | c≥2,d≥2 | u=p+(1−p)v; v∈[0,1] |
| M/A blue swap | (d,c) | c>0,d≥0 and not B(d,c) | same blue formula and interval |
| C blue | (d,c) | c>0,d≥0 | same blue formula and interval, without the B exclusion |
| U red | (c−d,d) | c≥d≥0,c>0 | u=v/2; v∈[0,1) |
| U blue factor | (cd,c) | c≥2,d≥2 | u=(1+v)/2; v∈[0,1] |
| U blue swap | (d,c) | c,d≥0,c+d>0 and not B(d,c) | u=(1+v)/2; v∈[0,1] |

Here p is always the recovered predecessor's a/(a+b), not the target's cut. Solving the red count equation yields the first, second and sixth rows. A nonempty MAIN/C red side requires a>0, whereas U allows a=0; this explains strict versus weak c>d. Solving factor output (b,a/b)=(c,d) yields (cd,c); B holds exactly under c,d≥2. Solving swap output yields (d,c), and its original branch exclusion is essential. Finally solve the affine interval equation. At a positive interior cut, red cannot attain v=1, blue does attain both endpoints; axis p=1 red and p=0 blue retain their entire closed intervals. These steps prove necessity and sufficiency of every row.

This table is also an exact image test: a target is in the image precisely when at least one row applies. Each fibre is finite, with at most three actual predecessors; no source-side multiplicity is collapsed. In M/C/A, every target with c=0 is missing, whereas every c>0,d=0 target has exactly (c,0,v) and (0,c,v). For all owners E has empty inverse fibre. U has vertical-axis predecessors supplied by its blue row; substituting MAIN's c>0 blue restriction would be incorrect.

No discontinuous or null-boundary convention is repaired here. Branch domains and ranges are the actual half-open/closed sets just listed. All count tests are on a countable discrete set; all interval formulas and side tests are Borel.

## 3. Every-Borel IMAGE and the fixed all-point clock

On one inverse row I, the interval slope j is p for M/C/A red, 1−p for their blue rows, and 1/2 for U. It is strictly positive on its actual domain. Each source and target count component has counting mass one. Therefore, for EVERY Borel B in that row's target domain,

\[
\mu(I(B))=\int_B j\,d\mu.
\]

This is ordinary one-dimensional affine change of length on the specified interval, including arbitrary Borel subsets. Single endpoints and cuts have zero measure on both sides, so they satisfy the same integral identity. The affine germ prescribes their positive j nevertheless. Summing over disjoint count components or Borel refinements proves the corresponding law for any injective union of actual rows; overlapping predecessor branches must not be treated as one injective map. No global T-invariance follows.

The pointwise version is j itself at every actual point, not a uniquely forced representative of an a.e. derivative. Thus κ=−log j gives log((a+b)/a) on nonempty M/C/A red sides and log((a+b)/b) on their blue sides, and κ=log 2 everywhere on U's domain. Zero denominators occur only on empty sides and are never evaluated. For M/C/A, κ≥0, with κ=0 exactly on the two nonempty axes; for U it is always positive. All these statements include u=0,1 and every cut.

## 4. Actual histories, IMAGE pairs, kernels and entire time groups

Define S₀=0, Sᵣ(z)=Σ_{i=0}^{r−1}κ(Tⁱz) on Dᵣ and Wᵣ(z)=exp Sᵣ(z). Use precisely G={(z,r−s,w):Tʳz=Tˢw legally}. If two representatives have the same triple, their lengths differ by a common integer. Extending the shorter pair adds the same legal future sum from the common endpoint to both S values. Hence

\[
c(z,r-s,w)=S_r(z)-S_s(w)=\log\frac{W_r(z)}{W_s(w)}
\]

is well defined. For nonterminal arrows common extensions are always legal because Y is invariant; a terminal admits only its identity. The same common-extension argument proves additivity under composition and negation under inverse. In particular (Tz,−1,z) has c=−κ(z), not +κ(z).

A fixed finite history has an injective affine inverse with derivative exp(−Sᵣ). For two histories ending at a common y, the actual map from the w-history to the z-history has derivative exp(−Sᵣ(z)+Sˢ(w))=exp(−c). Its every-Borel IMAGE law follows by the same affine argument. This includes histories whose target-domain intersection is only a null endpoint: the germs prescribe the ratio there, and the exact cocycle, not a measure-a.e. assertion, ensures consistency. Countably many history restrictions give the Borel history-pair atlas. G is a countable Borel groupoid; no étale, smooth or Hausdorff coarse quotient is asserted.

The EXACT full-arrow kernels are: K_lag consists of arrows represented with r=s; K_c consists of arrows with Wᵣ(z)=Wˢ(w); K_joint requires both. These tests are representation independent. They are not in general identity arrows and must not be confused with isotropy kernels. For U specifically c=k log 2 for EVERY arrow of lag k, so K_c=K_lag=K_joint.

For every source z, Iso_G(z) is the subgroup of integer differences r−s between equal legal forward iterates. If no iterates repeat, it is {0}. Otherwise let q be the eventual cycle's actual least period and L its complete κ-sum. Then Iso_G(z)=qZ, c(z,nq,z)=nL, and the ENTIRE time group H_z=LZ, including the case L=0. Indeed any unequal return forces an eventual cycle, and equality on that cycle has exactly the integer multiples of its least period. This is an exact global conditional ledger, not a classification or existence assertion for unsearched higher cycles.

Extension isotropy at (z,h) is ker(c|Iso_G(z)): qZ when L=0, trivial when L>0, and trivial for nonrepeating sources. Height translation on the extension orbit set returns at t exactly when t∈H_z. Thus positive primitive length is L when L>0, with repetitions nL, not the source period q or the existence of nontrivial zero-clock source isotropy. E has trivial source/extension isotropy and H=0. Nonnegativity shows any zero-clock cycle in M/C/A stays on the axes and therefore is a horizontal-axis fixed core; this is a direct one-step observation, not a higher-period census.

All incoming histories are constructive: Inv⁰(y)={y}, Invⁿ⁺¹(y)=⋃_{x∈Invⁿ(y)}Inv(x), with Inv exactly §2. Induction proves completeness without label or depth cutoff. Compatible infinite predecessor histories are all sequences selected from this tree satisfying the actual edge equations; they are retained, not added as new ideal source points. Two sources share a G-component iff some legal forward iterates meet. Two lifted points (z,h),(w,g) are equivalent iff such r,s satisfy h−g=Sᵣ(z)−Sˢ(w). This is the full exact incoming/orbit/phase test for every source.

More generally, in a component choose a reference o and one arrow g_z:o→z, with A_z=c(g_z). Every arrow time z←w is A_z−A_w+H_o. Therefore the complete phase is h−A_z in R/H_o; translation adds t to this phase. Choice of paths changes A_z only by H_o. This describes all real phases without selecting one section or deleting null sources.

## 5. Exhaustive fixed-state calculation

M/C red can fix counts only if b=0; then a≥1, p=1 and every u is fixed. U red also needs b=0 but its interval doubling fixes only u=0. A red fixes counts by definition; with a,b≥1 its interval equation forces u=0, while b=0 allows every u. A factor-blue fixed count pair would require b=a, contradicting the strict proper-divisor test. A swap-blue fixed count pair has a=b=m≥1; the interval equation then forces u=1 for every owner. These arguments cover both axes, every unit, cut and endpoint, and exclude E.

Consequently the following lists are GLOBAL and exhaustive, not probes:

| Owner | Fixed states | Own κ at the core |
| --- | --- | --- |
| M and C | f_{a,u}=(a,0,u), a≥1, 0≤u≤1; d_m=(m,m,1), m≥1 | 0 on f; log 2 on d |
| A | the same f and d; additionally r_{a,b}=(a,b,0), a,b≥1 | 0 on f; log 2 on d; log(1+b/a) on r |
| U | e_a=(a,0,0), a≥1; d_m=(m,m,1), m≥1 | log 2 on both families |

## 6. Complete basins and phases of every listed fixed core

For any owner and fixed core f, let B_f=⋃_{n≥0}Invⁿ(f), N(z) the first hitting time of f, A(z)=S_{N(z)}(z), λ=κ(f), and β(z)=A(z)−N(z)λ. The union is EXACTLY the entire G-component of f: meeting a forward iterate of a fixed point means eventually reaching it. Distinct fixed cores cannot share a component, by single-valued forward evolution.

For all z,w∈B_f and all k∈Z, (z,k,w) exists and

\[
c(z,k,w)=\beta(z)-\beta(w)+k\lambda.
\]

To prove existence, take sufficiently large r,s past both entrances with r−s=k. The sum after entrance is its length times λ, giving the formula. Thus on this FULL component: K_lag has k=0; K_c has β(z)−β(w)+kλ=0; K_joint has k=0 and β(z)=β(w). Source isotropy is Z at EVERY ancestor, not only at f. H=λZ; extension isotropy is Z for λ=0 and trivial for λ>0. Phase is h−A(z) modulo λZ (equivalently h−β(z)); for λ=0 it is a real phase. One positive-λ core gives exactly one primitive height-translation orbit, with all phases on its circle and repetitions nλ. A zero-λ source component gives a free translation line, not a positive primitive.

The unrestricted recursion already supplies complete basins; the following descriptions make their boundaries and multiplicities explicit.

**M/C/A horizontal cores.** B_{f_{a,u}}={(a,0,u),(0,a,u)} exactly. The inverse table gives these two predecessors of the horizontal point and none of the vertical point; both edge clocks are zero. Hence A=β=0, H=0, source and extension isotropy Z, and phase h. In particular the lag-zero arrow between the two distinct source points is a nonidentity joint-kernel arrow. These cores form a continuum of zero-time components, not positive-time packets.

**C diagonal cores.** B_{d_m}={d_m}. At target v=1 every positive-count red inverse is disallowed, and C's only blue predecessor is the same diagonal point. Thus each core is one primitive log 2 packet, H=(log 2)Z and extension isotropy trivial.

**M/A/U diagonal cores.** Along any backward chain from d_m the counts stay strictly positive; every inverse there at v=1 is blue and also has u=1. For m=1 the basin is the singleton d₁. For m≥2 it is exactly

\[
B_{d_m}=\{(m^r,m^s,1):r,s\ge1,\ \gcd(r,s)=1\}.
\]

Necessity follows by starting at (m,m): a blue inverse is either the permitted swap or (c,d)↦(cd,c), both preserving positive power form and coprime exponents. Sufficiency is the subtractive Euclidean algorithm on (r,s): if r>s, the actual proper-divisor branch sends it to (s,r−s); otherwise the actual nonfactor branch swaps it. The maximum decreases after at most a swap plus a subtraction until the exponents agree; coprimality then gives (1,1). This proves the full basin without searching other cycles. The basin is countably infinite for m≥2, yet is only ONE packet, not one per ancestor. Each has H=(log 2)Z and the phase in the general formula. U has β=0 identically; M/A use their own sums A, not U's clock.

**A red cores.** For each r_{a,b}, a,b≥1, the exact full basin is the unrestricted Inv-union above, with A's rows, λ=log(1+b/a), and the displayed β/phase/kernel formula. Every basin is countably infinite. It is at most countable by finite branching. It has a nonself direct blue predecessor at an interior cut: use swap when not B(b,a), and use factor (ab,a) when B(b,a) (then a,b≥2). This predecessor has positive interval coordinate and positive counts. Repeated A-red inverse steps on that same component multiply its coordinate by its cut p∈(0,1), producing infinitely many distinct ancestors. No diagonal u=1 or axis core lies in this basin; deterministic distinct fixed cores cannot merge.

For each rational q>1, write q−1=u/v in lowest positive integer terms. Exactly the red-core count pairs (a,b)=(kv,ku), k≥1, have λ=log q. They give countably infinitely many distinct fixed-origin packets at that time. The d_m family supplies further packets at log 2. For example r_{2,1} has primitive log(3/2), which is a control's nonprime time, not a MAIN conclusion.

**U horizontal cores.** No point with both counts strictly positive can map onto an axis, so the full basin of e_a stays on the two axes. Put P=the smallest subset of [0,1) containing 0 and closed under v↦v/2 and v↦(3+v)/4. Then

\[
B_{e_a}=\{(a,0,v):v\in P\}\ \cup\ \{(0,a,(1+v)/2):v\in P\}.
\]

Indeed a horizontal target at v has red predecessor (a,0,v/2) and blue predecessor (0,a,(1+v)/2); a vertical target has only its blue horizontal predecessor. Two successive blue inverse steps give (3+v)/4. These are exactly all inverse possibilities and prove the formula. Each basin is countably infinite, excludes u=1, has λ=log 2 and β=0, and is disjoint from every diagonal basin. All its source points have isotropy Z, H=(log 2)Z, trivial extension isotropy and phase h modulo log 2.

## 7. Multiplicity, strongest positive case and frozen stop

MAIN and C each have the fixed diagonal core d_m for EVERY m≥1. Distinct d_m cannot be history-equivalent. Each produces precisely one primitive log 2 packet; its length is derived from its actual half-cut Jacobian, and no shorter return exists because the entire group is (log 2)Z. Thus already d₁ and d₂ certify duplicate-prime packets, and the full fixed list supplies countably infinitely many. This is fixed-origin multiplicity, not a claim that all longer-cycle packets have been classified.

The strongest positive case is genuine: MAIN's count geometry owns its IMAGE law, retained-lag cocycle and extension, and its diagonal primitives really have prime-2 length. Also MAIN's nontrivial factor basins differ from C's singleton basins. Nevertheless their distinct core components cannot be merged by calling their identical lengths one packet, selecting one m, discarding u=1 as null, or dropping retained lag. All positive fixed-origin basins here are countable and μ-null, but the frozen full-point source expressly retains them.

A's additional red-core times and U's additional horizontal positive packets belong to those controls only. The M/C/A axis source loops have zero entire time group and cannot be promoted to physical positive returns. Conversely U's positive horizontal fixed packet must not be erased using MAIN's zero-axis clock. These own-owner contrasts establish what changes and what does not under each frozen control.

The MAIN fixed gate is decisively negative through duplicate log 2 packets: STOP / FORK. No ownership counterexample or mandatory card repair was found. Higher-period existence/classification, any other positive lengths, coverage, canonical arithmetic naturalness and stronger spectral/operator claims remain unproved here; there was no higher-period search. T3 NOT AUDITED, formal Route coordinates UNASSIGNED, Route B NOT INVOKED. No outcome about another candidate follows.

EOF — completed released card-only raw; the freeze receipt follows full self-read. HOLD for root full read and a distinct PAPER UNLOCK. Scope/card/author files remain untouched.
