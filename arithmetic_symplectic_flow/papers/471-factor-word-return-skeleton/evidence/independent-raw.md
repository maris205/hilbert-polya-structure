# 471 — original-card independent derivation

Date: 2026-09-25. Candidate: **ANG-20260925-FWR01**.
Scientific input: original `candidate-card.md`, **101 lines / 6080 bytes**, SHA-256 **`5f7989f2062a2fbb66a251b20d8646e010b3d94e4788e00a72be5dc1a3218820`**.
Result: the four prescribed measured-history owners are well defined. The entire product-6 fixed/two-step window is classified. MAIN has two distinct full packets of the same primitive `log 2`, so its necessary multiplicity target **FAILS — STOP / FORK**. This is not a higher-period classification.

## 1. Access and proof boundary

The root reported reading the complete 58-line CP1 report, SHA-256 `baab89cffc05fbdd46d0f48f6a0b91e5b75d227171922cc4622ff4c38ef67117`, accepted PASS, and issued DISTINCT RAW RELEASE. I then reread only the original card lines 1–101 through original EOF and remeasured that prefix hash. The complete current-candidate instruction reads recorded in CP1 are retained.
No current author/helper/peer mathematics, manuscript, README, ledger, appended outcome, old proof or sibling scientific file was accessed. Collision descriptions are only the card's disclosed design history, not newly opened scientific sources. There was no web/network, scientific code/numerics, auxiliary, Git, PDF or model change.
Only this raw file is written. This is exact elementary derivation on the frozen definitions, not a borrowed old theorem. Same-model/shared-history execution remains **NOT_CALIBRATED**, without blindness, error-independence, cross-model or external-peer claims. CP2/CP3 await separate authorization after raw freeze.

## 2. Full carrier, legal maps, terminals, and product

Let `L(w)` be word length, `P(w)=∏a_i`, with `P(empty)=1`. The set W of all finite words over integers at least 2 is countable; `X=W×[0,1]` with counting times Lebesgue measure is a sigma-finite Borel measured space, not a normalized probability. Every endpoint and every unsorted word belongs to it.
For each owner enumerate exactly its frozen finite operation list and write its actual output as `V_j(w)`. For O this is `sort(R_j(w))`; the source w is never sorted or quotiented. Let its own list length be `h(w)`. For `h>0`, define

`I_(w,j)=[j/h,(j+1)/h)` for `j<h−1`, and `I_(w,h−1)=[(h−1)/h,1]`.

These form an exact disjoint partition of `[0,1]`. On that branch `T(w,x)=(V_j(w),hx−j)`. The target interval is `[0,1)` for a nonlast rank and `[0,1]` for the last. In particular, an interior cut uses its right branch and `x=1` uses the last branch. The formula never calls a nonexistent rank when h=0.
Every split/merge preserves P, and sorting also preserves it. Thus ALL legal histories and inverse histories preserve P. Each step changes L by exactly one, even for O. Every fixed set is consequently empty; this direct length observation is not a search outside the frozen window.
For MAIN/O, a word of length at least two has a merge, while a singleton has an operation exactly when its letter has a proper divisor. Their terminal words are the empty word and singleton primes; product preservation shows that these terminal components have no incoming. For S, all words of length at most one are terminal. For K, exactly words whose letters are all prime, including the empty word, are terminal. Their incoming is not discarded and is determined below.
All maps and domains are Borel by their countable word/branch decomposition. No continuity across interval cuts, étale topology, smooth flow, regular coarse quotient or geometric lift is claimed.

## 3. Exhaustive inverse atlas and EVERY-Borel IMAGE

For a target word v, an inverse of a split must be obtained by merging an adjacent pair of v; an inverse of a merge must expand one letter c of v into an ordered pair `(a,b)` with `a,b≥2,ab=c`. There are finitely many such proposals at each fixed finite target word. Rebuild each predecessor's complete OWN list and retain exactly ranks giving the target output. S retains only merge-forward proposals, K only split-forward proposals, and MAIN both.
For O, first require the target word to be sorted. Enumerate its finitely many distinct word permutations u, apply the two reverse operations to u, then rebuild the actual O list and test `sort(R_j(w))=v`. This also recovers unsorted predecessors. No nonsorted target has an O inverse, but such targets remain genuine source objects with their own possible forward step.
For every retained `(w,j)` define the actual inverse

`θ_(w,j)(v,y)=(w,(j+y)/h(w))`, with `y∈[0,1)` if `j<h−1`, and `y∈[0,1]` if `j=h−1`.

Recheck actual forward equality and deduplicate identical predecessor points. At y=1 only the last rank qualifies; admitting the other formal endpoints would create false predecessors. Conversely every actual forward source has its own rank and a reverse edit in this enumeration, so the atlas is complete. Each target has finitely many actual predecessors; no cutoff has been imposed.
All domains and images of these inverse branches are Borel in the component product space. On a target component of mass one, ordinary affine substitution gives for EVERY Borel subset E of its actual target interval

`μ(θE)=Leb((j+E)/h)=(1/h)Leb(E)=∫_E (1/h)dμ`.

The inverse affine germ on the real line has derivative `1/h` at every point, including endpoints. Since both word components have counting mass one, the prescribed full modulus is exactly `J=1/h` and the clock is `κ=log h≥0` on legal sources. It vanishes exactly on h=1 branches. Terminal steps have no clock evaluation.
This is a branchwise EVERY-Borel law, not global invariance of a many-to-one map. Disjoint countable refinements give the law for any actual branch atlas. Null endpoints do not disappear, and their fixed positive germ values are not claimed to be uniquely determined by an a.e. Radon–Nikodym class. Duplicate output words do not identify distinct interval preimages or distinct source words.

## 4. Entire histories, kernels, inverse generations and phases

For each owner let `D_m` be the m-step legal domain and, on it, put `Q_m(z)=∏_{i<m}h(T^iz)`, with `Q_0=1`, and `S_m=log Q_m`. The actual Borel groupoid is the set of retained triples `(z,m−n,w)` with `T^mz=T^nw` legally; equal triples are identified, not their witness histories.
Two witnesses for a fixed triple change both depths by the same integer. At the larger pair of depths they add identical legal common-tail factors. Therefore `c(z,m−n,w)=log(Q_m(z)/Q_n(w))` descends at every point. Aligning existing middle histories proves composition and additivity without extending a terminal. Inversion negates lag and c; the forward arrow `(Tz,−1,z)` has c=`−κ(z)`.
A first-witness choice from a countable enumeration proves c is Borel. On any refined history-pair branch from w to z, the inverse substitution factors give modulus `Q_n(w)/Q_m(z)=exp(−c)`. Iterating the branchwise law proves EVERY-Borel IMAGE; products of the frozen affine germs also give equality of pointwise versions at endpoints and null intersections.
The full kernels are exactly: `ker lag` requires an actual equal-depth meeting; `ker c` requires `Q_m(z)=Q_n(w)`; their joint kernel requires both. These are all-arrow tests, not merely tests on self-arrows. Equal clock values do not merge unrelated source classes.
Define `Inv^0(B)=B` and `Inv^(r+1)(B)=⋃_{y∈Inv^r(B)}Inv(y)` using the complete own atlas. Induction proves that this is exactly the set of sources with an r-legal-step image in B. The full source orbit of z is `⋃_{n:T^nz exists}⋃_{r≥0}Inv^r({T^nz})`. All incoming arrows to z are `(z,n−r,w)` with those legal n and `w∈Inv^r({T^nz})`.
Compatible infinite pasts are exactly sequences `z_0=z,z_(−j−1)∈Inv(z_(−j))` at every depth. This describes the entire finite-branch choice tree, not its finite truncation or a completion by limit states. If every depth of such a finitely branching tree is nonempty, a child with arbitrarily deep descendants exists at each level, giving a coherent infinite path. No claim that every object satisfies that premise is made.
All source classes are countable. Product preservation forbids incoming from a different P component. For a fixed P, word length is bounded by `2^L≤P` and each letter divides P, so there are finitely many possible words; the interval coordinate is nevertheless never truncated or restricted to a finite set.
If a forward orbit is not eventually periodic, its source isotropy is zero, since a nonzero self-lag would exhibit equal legal iterates. Otherwise, for its actual least-period p cycle with one-cycle clock K, the ENTIRE source group is `pZ` and `c(z,np,z)=nK`, `H_z=KZ` at every ancestor; transient factors cancel. Here `K≥0`, and K=0 precisely when every h on that cycle is one. This conditional statement asserts no further cycle existence.
Source/extension isotropy are distinct: extension isotropy is the kernel of c on source isotropy, hence all `pZ` for K=0 and zero for K>0. If anchor-to-z has clock A(z), all real extension phases are `h−A(z) mod H`; the complete arrow clock coset proves necessity and sufficiency. Translation stabilizer is ENTIRE H. For K>0 its positive primitive is K with all positive integer repeats; K=0 has no positive primitive, even if source isotropy survives. Each nonzero-H source class gives one closed height-translation packet with its full phase circle, not one packet per chosen phase.

## 5. Own global termination and complete ledger for S and K

S decreases L at every legal step and reaches its singleton terminal after `L−1` steps for nonempty words. Its step clock is `log(L−1)` when `L≥2`. Define `B_S(w,x)=log((L−1)!)` for `L≥1` and 0 for the empty word. Then `κ_S=B_S−B_S∘T` on every legal step and the FULL history cocycle is `c_S(z,k,w)=B_S(z)−B_S(w)`.
K increases L by one while preserving P. The bound `2^L≤P` forces finite termination at a prime-letter word, for every actual interval coordinate including endpoints. Let `N_K(z)` be its first terminal time and define the finite Borel sum `B_K(z)=S_(N_K(z))(z)`. Then likewise `κ_K=B_K−B_K∘T` and `c_K(z,k,w)=B_K(z)−B_K(w)` on its whole actual groupoid.
For either owner, two objects are in the same full source class exactly when their actual terminal state, including its interval coordinate and word, is the same. The inverse atlas gives all of that class. Source and extension isotropy and ENTIRE H are zero globally. Its real phase is `h−B_owner(z)` relative to the terminal anchor; no quotient by a nonzero time lattice is taken.
For S an actual arrow's unique lag is `L(z)−L(w)`; for K it is `L(w)−L(z)`. The full lag kernel is equality of these lengths within an actual class, clock kernel is equality of B, and joint kernel requires both. These can contain nonidentity arrows despite trivial isotropy. K's global clock is not asserted identically zero.
There are no infinite backward histories for either: S inverses increase L with fixed P and K inverses decrease L. The precise finite inverse recursion remains valid at all depths and becomes empty beyond these bounds. This is a direct same-owner monotonicity argument for the required histories, not another product/period census.

## 6. Exhaustive product-6 state space and actual one-step laws

For P=6, `2^L≤6` gives `L≤2`; the empty word has P=1. The only words are `A=(6)`, `B=(2,3)`, `C=(3,2)`. This proves whole-component completeness before solving returns. Denote a state by A_x, B_x or C_x, for every `x∈[0,1]`.
At A, the actual MAIN split ranks are d=2 then d=3; B and C have only their one adjacent merge. Define the CLOSED-interval map `g(x)=2x` on `[0,1/2)` and `g(x)=2x−1` on `[1/2,1]`. In particular g(1)=1, not 0.

| Owner | ALL product-6 forward rules and clocks |
| --- | --- |
| M | `A_x→B_(2x)` for x<1/2, `A_x→C_(2x−1)` for x≥1/2, each with κ=log2; `B_x,C_x→A_x` with κ=0 |
| S | `B_x,C_x→A_x` with κ=0; every A_x terminal |
| K | Same two A branches as M, κ=log2; every B_x and C_x terminal |
| O | `A_x→B_(g(x))` on both actual ranks, κ=log2; `B_x,C_x→A_x` with κ=0; C remains an unsorted source, not a quotient representative |

The full incoming rules, on ALL y∈[0,1], are correspondingly:

| Owner | Inv(A_y) | Inv(B_y) | Inv(C_y) |
| --- | --- | --- | --- |
| M | `{B_y,C_y}` | `{A_(y/2)}` if y<1; empty if y=1 | `{A_((1+y)/2)}` |
| S | `{B_y,C_y}` | Empty | Empty |
| K | Empty | `{A_(y/2)}` if y<1; empty if y=1 | `{A_((1+y)/2)}` |
| O | `{B_y,C_y}` | `{A_((1+y)/2)}` plus `{A_(y/2)}` exactly when y<1 | Empty |

These are the unrestricted full-X inverses for these targets: product preservation excludes every other component and the three-word exhaustion excludes every other word. In particular M's B_1 and O's C_1 have no predecessors but are legal, not terminals. These tables also specify every compatible finite or infinite backward history by repeated actual choices.

## 7. ENTIRE fixed and two-step sets, not selected examples

All four fixed sets are empty by length change. For M, two steps from A give A_(g(x)); fixedness of g yields only x=0 from its first branch and x=1 from its last. Starting at B returns to B only through the first A branch, forcing x=0; starting at C requires the last A branch, forcing x=1. Therefore

`Fix(T_M²)={A_0,B_0,A_1,C_1}`: precisely the cores `{A_0,B_0}` and `{A_1,C_1}`.

For O, two steps from A and B return to the same word with coordinate g(x); each has exactly x=0,1. No two-step image has word C, so no C is in Fix(T_O²). Thus

`Fix(T_O²)={A_0,B_0,A_1,B_1}`: precisely the cores `{A_0,B_0}` and `{A_1,B_1}`.

Each displayed cycle has least period two, since there is no fixed point. For S and K no product-6 state has two legal steps: after their only possible step it is terminal. Hence both `Fix(T_S²)` and `Fix(T_K²)` are empty. Terminal units add nothing. No interior solution or assigned endpoint has been omitted.

## 8. Full incoming packets of the four discovered M/O cores

Put `D={k/2^n:n≥0,0≤k<2^n}`. The points of `[0,1)` that eventually reach 0 under g are exactly D: iterating its affine branches gives a dyadic fraction for any preimage of 0, and every such dyadic fraction reaches 0. Conversely g maps `[0,1)` into itself, so its only points eventually reaching 1 are x=1.
For EACH of M and O, the complete basin/source packet of its lower core is

`ℬ_0={A_x,B_x,C_x:x∈D}`,

and the complete basin/source packet of its upper core is

`ℬ_1={A_1,B_1,C_1}`.

The first is countably infinite; the second has three points, not just its two core points. M has the state B_1 as its additional upper ancestor, while O has C_1. The symbols `ℬ_0,ℬ_1` denote basins, not individual states.
These are full-X basins, not merely forward-invariant pieces of the tested component: the inverse table and product invariant prove no other predecessor exists. There is exactly one cyclic core per basin. The lower and upper basins cannot meet any common future because one eventually has coordinate 0 and the other coordinate 1. Equality of their return groups does not merge them.
There are exactly two discovered packets per owner in the frozen window. The dyadic ancestors do not supply additional packets, and the phase continuum along one closed height-translation orbit does not supply additional geometric copies. No assertion is made about other product-6 periods or other products.

## 9. ENTIRE M/O arrow sets, kernels, phases and primitive multiplicity

Let `λ=log2` and `e(A_x)=0`, `e(B_x)=e(C_x)=1`. Along every legal product-6 M/O step the flag alternates, and the clock is λ exactly when its initial flag is 0. On an actual meeting triple of lag k, cancellation of the common final flag therefore gives

`c(z,k,w)=(k+e(w)−e(z))λ/2`.

Within either complete basin just found, the ENTIRE arrow set between z,w is exactly all integers `k≡e(w)−e(z) (mod2)`. Necessity is flag alternation; sufficiency follows by continuing both tails on the same two-cycle beyond their entry times. Thus no hidden incoming branch changes the minimal self-lag or supplies a smaller positive generator.
For every incoming object, source isotropy is `2Z`, with `c(z,2n,z)=nλ`; ENTIRE `H=λZ` and extension isotropy is trivial. The positive primitive is λ, with all positive integer repetitions. This is not inferred from one convenient subgroup or a single forward clock.
Within each basin, the full clock kernel is exactly `k=e(z)−e(w)`. The full lag kernel consists of k=0 arrows between points of equal flag; the joint kernel is this same lag kernel. In particular these kernels are not all units: distinct same-flag ancestors have zero-lag, zero-clock arrows. On the upper basin the two distinct length-two states B_1,C_1 already give such a nonidentity joint arrow.
Choose the core A endpoint as anchor. For every incoming z the actual connector of lag `e(z)` has clock zero. Consequently the COMPLETE phase test is simply `h mod λ` within that basin. Different basins remain different packets for every phase. The two discovered MAIN source packets each give one closed height-translation orbit of primitive `log2`; they violate the frozen at-most-one-packet-per-prime condition.

## 10. Complete own S/K product-6 classes and phases

For S, for each y∈[0,1] the entire class is `{A_y,B_y,C_y}`, with terminal anchor A_y. All its arrows have clock zero; their unique lag is `e(z)−e(w)`. The full clock kernel is the entire class groupoid; lag and joint kernels connect the equal-flag objects, including B_y and C_y. Source/extension isotropy and H are zero, and the phase is the real height h without periodic identification. There are no source cycles or positive primitives.
For K, the full classes are `{B_y,A_(y/2)}` for 0≤y<1, the singleton `{B_1}`, and `{C_y,A_((1+y)/2)}` for 0≤y≤1. Each listed two-point class has a single forward step from A to its terminal; no class is a two-cycle. The half-open missing inverse at B_1 is essential.
In these K classes, the unique arrow lag is `e(w)−e(z)` and c is that lag times λ. Its lag, clock and joint kernels are units. Source/extension isotropy and H are zero. With the terminal anchor, the full real phase is h at the terminal and `h−λ` at its A predecessor. Its nonzero step clock is not a positive closed-orbit time. These conclusions use K's own count and inverse domains, not MAIN's completion of a return.

## 11. Decisive gate, strongest positive case, and limits

The original measured owner, all-point germ convention and full retained histories survive. MAIN's entire product-6 short window has two distinct nonmerging packets whose identical ENTIRE positive primitive is `log2`. This is an owned duplicate at an ordinary prime, so the necessary MAIN multiplicity clause fails: **STOP / FORK**. There is no need to search for a nonprime or a longer word, and no prime-only support or all-prime coverage claim is made for the global ledger.
The strongest positive reading remains substantive: proper-divisor rewriting feeds the current interval ports and subsequent word dynamics, and each measure/clock belongs to that same object. S/K isolate the two rewrite directions using their own complete terminating histories; O retains its own unsorted sources and also has its two calculated packets. None of those controls supplies the MAIN verdict by transfer.
Identifying x=0 with x=1, deleting endpoints as null, forgetting actual word order, choosing only one source packet, or replacing the all-point clock by an a.e. version changes the frozen object. It is not a resolution of this multiplicity obstruction. The failure does not prove every factor-word construction impossible; strong naturalness and PROVES_TOO_MUCH remain OPEN.
No longer-period/product census, new target threshold, new measure, modified port width, operator, physical roof or formal Route evaluation was performed. Classical NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED; formal coordinates UNASSIGNED; Route B NOT INVOKED. CP2/CP3 remain pending a distinct PAPER UNLOCK.
After complete self-read and the returned line/hash receipt, this raw file is frozen. Any later erratum must be separately disclosed; it must not be silently revised after manuscript exposure. HOLD for the root's full raw read and explicit unlock.

EOF — FWR01 card-only raw; complete frozen gate and own-control obligations, no unresolved proof blocker.
