# BPR01 — released original-card independent derivation

Candidate: ANG-20260925-BPR01. Date: 2026-09-25.
Bounded verdict: MAIN owns a positive primitive log(3/2) at 0^∞, not an ordinary-prime logarithm. STOP / FORK. All four owners and the entire seven-cylinder fixed gate are treated below; no higher-period census is performed.
Same inherited model/shared history, NOT_CALIBRATED; not blind, external peer review, cross-model or independent-error certification.

## 1. Exact input and stage record

The sole scientific input read after DISTINCT RAW RELEASE was `candidate-card.md`, original lines 1–84 through EOF: 84 lines, 4,679 bytes, SHA-256 `fe59e005a560c186b3c666509318e1043bcc5ab16b8a19348d7acbe8e15b28ee`. The preceding 48-line scope report has SHA-256 `5185487c9c6a85c050622343a98223529e74557b6b727e30f36ddc014937ba43`; root reported reading it fully before release. Neither input is changed.

Previously personally read ARS/router/deep-research DA/runtime/fallacy/anti-leakage and local instructions are retained as disclosed in CP1. Earlier binary/history/Markov-related work remains inherited context, not new proof input. No author paper, README, ledger, peer/helper answer, old scientific file or appended outcome was read. No auxiliary, network, scientific code/numerics, Git, PDF or other-file edit occurred. Only this raw report is written. Manuscript comparison and final-surface review remain locked until root full raw read and DISTINCT PAPER UNLOCK.

## 2. Parse, original probability and full own inverse atlases

Let t=1^∞. For x≠t, the first zero has a finite, unique index n; the following n bits give the unique w and the remaining infinite tail η. Thus A=1^n0w, |w|=n, gives a disjoint countable prefix-cylinder partition of X\{t}. The finite root exists because w itself is an admissible prefix; minimum length selects a unique root. The empty case is separately defined. Each owner replaces A by its specified B: r(w), w, empty, or r(sort(w)). In all cases |B|≤n<|A|=2n+1.

The initial probabilities sum to one and every transition row sums to one. The prescribed finite-cylinder probabilities are therefore consistent and define the Markov probability on the full Borel source. A direct construction partitions a unit interval first in proportions π, and recursively in proportions given by the last symbol's transition row; recording its successive binary choices has precisely those cylinder probabilities. Every finite cylinder has positive mass. A length-m cylinder has mass at most (1/2)(2/3)^(m−1), so every singleton has measure zero by continuity from above. In particular no periodic or terminal word is removed.

For EVERY n≥0 and EVERY w∈{0,1}^n, the actual inverse chart of each owner is

\[
I_{n,w}:[B]\longrightarrow[A],\qquad B\eta\longmapsto A\eta,
\]

using that owner's B, with [empty]=X. It is a prefix homeomorphism, T I=id on the ENTIRE target cylinder and I T=id on its source cylinder. Conversely any predecessor has its unique parse (n,w), so is exactly the indicated inverse value; the source partition prevents duplicate descriptions of one actual predecessor. Charts with the same B can have different actual sources and are all retained. No target-outgoing guard is imposed: t belongs to the domain whenever B is empty or consists entirely of ones.

The n=0 inverse y↦0y proves every target has incoming. In fact every target has countably infinitely many predecessors: for F, take w to be its length-n prefix for every n; for M/O use w equal to n repetitions of its first bit for every n≥1; for C every (n,w) is available. Their different first-zero indices make these sources distinct. All sources remain nonterminal because A contains a zero. Hence each owner is onto X from its proper domain X\{t}, not a total map at t.

## 3. Every-Borel Markov seam law, not just cylinder mass

For a finite word s and a Borel tail set E, prefixing gives the exact identity

\[
\mu(sE)=\int_E K(s,\eta_0)\,d\mu(\eta),\qquad K(\varnothing,b)=1.
\]

For nonempty s this follows first by multiplying the initial, internal-transition and last-to-first-tail factors on each finite tail cylinder. The division by π_(η₀) replaces the initial tail weight already present in μ(E); it is not division by μ(E). On each first-tail-bit class the factor is constant. Equality of the resulting finite measures extends from the intersection-closed finite-prefix cylinders (and the empty set) to every Borel E. This proves the formula even when E is null.

For an actual replacement Bη↦Aη and any Borel F⊂[B], write E={η:Bη∈F}. The preceding identities for B and A then give

\[
\mu(I_{n,w}F)=\int_F\frac{K(A,\eta_0)}{K(B,\eta_0)}\,d\mu.
\]

Thus the card's J is the correct every-Borel IMAGE density. Its value is prescribed on every tail, including t and periodic points; this pointwise version is not uniquely forced by measure equality on null sets. Both K factors are finite positive because π and all transitions are positive. Tail-first-bit refinement makes each density constant on an actual finite-prefix chart. No iid replacement, summed predecessor density or global T-invariance is used.

For an exact computational-free expression, let e(s,b) count equal neighbouring symbols along s followed by b, among its |s| edges; e(empty,b)=0. Since π is uniform,

\[
K(s,b)=2^{e(s,b)}/3^{|s|},\quad
J=\frac{2^{e(A,b)-e(B,b)}}{3^{|A|-|B|}},\quad
\kappa=(|A|-|B|)\log3-[e(A,b)-e(B,b)]\log2.
\]

These are each owner's actual values, with b=η₀, not an assumed common clock across controls. They are finite at every legal source. No terminal step clock is defined at t; its identity arrow has c=0. Positivity needed for each tested fixed core will be proved below, rather than inserted as a roof assumption.

## 4. Legal histories, partial composition, IMAGE and full kernels

Define D₀=X and D_{r+1}={x∈D_r:Tʳx≠t}. These are precisely legal r+1-step domains. Set S₀=0 and S_r=Σ_{i<r}κ(Tⁱx) there. Retain G={(x,r−s,y):Tʳx=Tˢy legally}, source y/range x, with equal triples only.

If two witnesses represent the same triple, their depths differ by the same integer. Assume the second is longer. Its existence guarantees that the common endpoint of the shorter witness has the necessary legal extension; the added S sums on both sides are identical and cancel. No extension beyond a terminal is invented. For composition, align the shared-point depths at their maximum: the longer existing shared history guarantees that the required extension of the other pair is legal. Hence c=S_r(x)−S_s(y) descends and adds, inversion negates it, and c(Tx,−1,x)=−κ(x).

Finite compositions of prefix replacements refine to prefix replacements: two intermediate cylinders are disjoint or one prefix extends the other, and the latter case is handled by the corresponding finite tail refinement. Finite histories thus have countably many actual finite-prefix charts covering their entire legal domains, including a final terminal target when allowed. Prefixing factors satisfy K(UV,b)=K(U,V₀)K(V,b) for nonempty V, so products of actual densities give the density of the composed prefix replacement at EVERY tail. The every-Borel result in §3 therefore proves that a history-pair chart from y to x has density exp(−S_r(x)+S_s(y))=exp(−c), including null and terminal endpoints.

Fixed-depth equality and all branch conditions are Borel. The countable inverse atlas yields countable source/range fibres, so this is a countable Borel groupoid. The exact full-arrow kernels are: lag kernel r=s; clock kernel S_r(x)=S_s(y); joint kernel both, always on actual triples. These tests descend by the proved cocycle identity. They are not in general identity arrows and are distinct from their restrictions to isotropy.

All incoming is explicit: Inv⁰(y)={y}, Invⁿ⁺¹(y)=⋃_{v∈Invⁿ(y)}Inv(v), using ALL n,w indices of the own atlas without the core-window bound. Induction gives exactly every depth-n predecessor. All arrows incoming to range x are (x,r−s,y) with x∈D_r and y∈Invˢ(Tʳx). Compatible infinite incoming histories are exactly sequences x₀=x, Tx_{j+1}=x_j from this tree, not extra completion points. The inverse y↦0y always allows continuation backward, but is not a selection replacing the other histories.

Two sources are equivalent exactly when some legal forward iterates meet. Lifted points (x,h),(y,h') are equivalent exactly when such witnesses also give h−h'=S_r(x)−S_s(y). The extension is on all X×R and translation commutes with every arrow, so the physical real action is defined on the orbit SET for all times. No nice quotient, positive suspension roof or analytic operator is needed or claimed.

For any source with an eventual least cycle of period q, Iso_G=qZ and H=ΛZ, where Λ is that cycle's complete κ-sum; transient sums cancel. Every unequal self-meeting gives such a cycle, so terminal-reaching or aperiodic sources instead have Iso_G=H={0}. If Λ≠0, the positive physical primitive is |Λ| and repetitions are j|Λ|; extension isotropy is trivial. If Λ=0, extension isotropy is qZ but no positive physical return exists. These are ENTIRE group criteria, not existence or classification claims about untested higher cycles.

For a general component choose reference o and one actual arrow o→x of clock A_x. Arrow times x←y are A_x−A_y+H_o, so all real phases are represented by h−A_x modulo H_o. The global height-action kernel is trivial because the retained terminal component has H=0. No ordinary-tail or finite-word-period quotient is substituted.

## 5. Terminal incoming and its entire component

The complete first preimages of t for M/F/O are 1^n0 1^∞, n≥0: B can prefix t only when w is all ones (or empty). For C they are ALL 1^n0w1^∞, |w|=n. The same atlas supplies their full unbounded further generations and all fixed pointwise seam values. In every owner, 01^∞→t has J=K(0,1)=1/3 and step clock log 3. This is a terminal incoming clock, NOT a positive primitive.

For all four owners, the entire terminal basin E₁ is exactly the set of words with finitely many zeros. Indeed each legal step removes the header zero; the output B has at most as many zeros as w, so the finite zero count strictly decreases. Such a word reaches t in finitely many steps. Conversely a finite rewrite changes only a finite prefix, so infinitely many zeros cannot all disappear in finitely many steps. This short monotonicity proof classifies the terminal basin, not higher periods.

Let N(x) be the first terminal hitting time, A(x)=S_{N(x)}(x), with N(t)=A(t)=0. Every two points of E₁ have exactly the lag N(x)−N(y) between them, with c=A(x)−A(y). Any earlier common future extends legally to t and yields precisely these differences; equality at t proves the converse. Thus source and extension isotropy are trivial, H=0 everywhere on E₁, the real phase is h−A(x), and there is one free translation orbit, no positive periodic packet. Its full lag kernel has N(x)=N(y), clock kernel A(x)=A(y), and joint kernel both. The identical basin SET across controls does not identify their hitting depths, clocks or groupoids.

## 6. Exhaustive full-cylinder fixed equations

On any tested branch, a fixed word solves Aη=Bη, with |A|>|B|. Necessarily B is a prefix of A; otherwise the first |B| symbols disagree for EVERY η. If A=BV, cancellation gives Vη=η, which has the UNIQUE solution η=V^∞. Conversely x=BV^∞ is in [A] and is fixed. Thus this criterion solves the entire cylinder, not a chosen constant tail, and no minimal finite-word period is assumed.

At this fixed point b=V₀. Cancellation of the common B Markov seam gives

\[
J_{\rm fixed}=\prod_{i=0}^{d-1}P_{V_i,V_{i+1\bmod d}}
=2^{e_V}/3^d,\quad L=-\log J_{\rm fixed}>0,\qquad d=|V|.
\]

For B empty the same expression follows directly from K(V,V₀); otherwise the first transition from the last B bit to V₀ cancels. Each factor is at most 2/3, proving strict positivity. Even if V is a repeated finite word, this does not by itself divide the physical primitive: the actual source fixed point has integer isotropy Z and the entire H computed in §7.

The following table lists every solution in each tested full cylinder. A dash means NO fixed word in that whole cylinder. An entry gives the full source word and its own fixed J; its time is −log J. M and O coincide in this WINDOW only, not as global maps.

| Source cylinder A | B_M / B_F / B_O | M and O: fixed word; J | F: fixed word; J | C: fixed word; J |
| --- | --- | --- | --- | --- |
| 0 | empty / empty / empty | 0^∞; 2/3 | 0^∞; 2/3 | 0^∞; 2/3 |
| 100 | 0 / 0 / 0 | — | — | (100)^∞; 2/27 |
| 101 | 1 / 1 / 1 | (10)^∞; 1/9 | (10)^∞; 1/9 | (101)^∞; 2/27 |
| 11000 | 0 / 00 / 0 | — | — | (11000)^∞; 8/243 |
| 11001 | 01 / 01 / 01 | — | — | (11001)^∞; 8/243 |
| 11010 | 10 / 10 / 01 | — | — | (11010)^∞; 2/243 |
| 11011 | 1 / 11 / 1 | 1(1011)^∞; 4/81 | 11(011)^∞; 2/27 | (11011)^∞; 8/243 |

To check exhaustion explicitly, in rows 100/11000 the nonempty B starts with 0 rather than A's 1; in row 11001 the same mismatch occurs; in row 11010, M/F demand initial 10 rather than 11 and O demands initial 01. They have no solution. Row 101 leaves V=01 for M/F/O. Row 11011 leaves V=1011 for M/O and V=011 for F. Row 0 leaves V=0. C always has B empty and leaves V=A. These are all seven rows and all four owners.

The cyclic equal-edge counts behind the table are: V=0 has (d,e)=(1,1); V=01 has (2,0); V=1011 has (4,2); V=011 has (3,1). For C, A=100 and 101 have (3,1); A=11000,11001,11011 have (5,3); A=11010 has (5,1). Multiplying the exact transition factors yields the displayed rational J values, without scientific code or numerical approximation. The terminal t is not fixed: its only isotropy arrow is the identity, while all incoming arrows in §5 remain present.

## 7. Entire incoming, kernels, phases and packet counts of all found cores

For any table core f, take its own unrestricted basin B_f=⋃_{N≥0}Inv^N(f). This is EXACTLY the whole source component of f, because any common future with a fixed point equals it. Every point of B_f subsequently has all forward iterates and cannot terminate. The basin is countably infinite: every one-step inverse fibre is countably infinite and every finite generation is countable. It is μ-null but all its points and incoming histories are retained.

Set λ=κ(f)>0 and β_f(x)=S_N(x)−Nλ whenever T^Nx=f. Additional fixed steps prove independence of N. For every x,y∈B_f, all integer lags k occur by extending beyond entry, and

\[
G|_{B_f}=B_f\times\mathbb Z\times B_f,\qquad
c(x,k,y)=\beta_f(x)-\beta_f(y)+k\lambda.
\]

Therefore the entire lag kernel has k=0; clock kernel has the displayed right side zero; joint kernel has both. At EVERY ancestor source isotropy is Z, H=λZ and extension isotropy is trivial. The full phase is h−β_f(x) modulo λZ, equivalently h−S_N(x). Each basin supplies exactly ONE physical translation circle with primitive λ and repetitions jλ. Distinct fixed cores cannot meet forward and therefore cannot merge, regardless of equal clocks, ordinary word periods or tail descriptions.

As a concrete phase safeguard, for M/F/O the core f=(10)^∞ has λ=log 9. Its ancestor x=(01)^∞ reaches it in one n=0 step of clock log 3, with β_f(x)=−log 3. Both sources still have ENTIRE H=(log 9)Z. The arrival offset log 3 is not an isotropy return, and does not halve the physical primitive. This statement is not transferred to C.

The window thus gives M and O three distinct full packets of times log(3/2), log 9 and log(81/4). F gives three of times log(3/2), log 9 and log(27/2). C gives seven: one at log(3/2), two at log(27/2), three at log(243/8), and one at log(243/2). These are window packet counts, not full higher-header or higher-period classifications. The complete inverse recursion and phase formulas above, with all n≥0, provide full-X incoming for EACH of these cores.

## 8. Decisive gate, strongest positive case and limitations

MAIN's 0^∞ core is an actual fixed point in [0], with all-point J=2/3 and ENTIRE H=log(3/2) Z. Its actual positive primitive is log(3/2), not log p for any ordinary integer prime. This alone refutes purity and triggers STOP / FORK. Independently the other MAIN window times log 9 and log(81/4) are also nonprime logarithms; log 9 is not relabelled a prime-3 repetition because its entire physical return group has least positive element log 9.

There is genuine ownership and positive nonemptiness: the original Markov law, complete inverse charts, cocycle and full phase orbits are well defined, and compression/reparsing is an actual finite-word operation. Nevertheless the adverse [0] primitive is shared by all controls, before nonempty root compression is used. Primitive finite words, prime lengths or transition denominator 3 do not furnish the ordinary-prime physical ledger. For the card's lineage checks, w=0011 has composite length 4 but no period 1 or 2, so r(w)=w; w=00 has prime length 2 but r(w)=0. Both remain actual payloads with all tails; these word tests assert no extra dynamical return. Deleting null cores, adjusting Markov weights, selecting a phase/representative or adding a roof would change the frozen object.

Arithmetic naturalness, causal specificity of compression and PROVES_TOO_MUCH remain separate limitations. M/O's matching window is not global equivalence; the controls are not pooled. The proof is exact for the frozen seven full cylinders and for all inverse/history ownership, but does not classify other fixed-header locations or higher periods. Global uniqueness/coverage are not certified by this bounded result. No tuning, simulation or robustness extrapolation was performed.

No owner repair or new candidate is made. Classical fields NOT APPLICABLE; arithmetic target NOT PASSED; T3 NOT AUDITED; formal coordinates UNASSIGNED; Route B NOT INVOKED. No round490 is initiated. Raw does not substitute a chosen periodic tail or an iid clock for the frozen source.

EOF — complete released card-only raw; full self-read and freeze receipt precede HOLD for root full read and DISTINCT PAPER UNLOCK. Scope/card/author files untouched.
