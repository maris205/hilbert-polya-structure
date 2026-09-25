# CFT01 — released card-only independent derivation

Candidate: ANG-20260925-CFT01. Date: 2026-09-25.
Bounded result: all four measured-history owners are established; MAIN has a fixed-origin primitive log 6 and therefore fails the frozen ordinary-prime-only condition. STOP / FORK; no owner modification or higher-period census.
Internal inherited-model/shared-history work, NOT_CALIBRATED; not blind, external peer review, cross-model or independent-error certification.

## 1. Inputs, chronology and limits

The sole scientific input read for this derivation was the clarified `candidate-card.md`, lines 1–90 through EOF, after DISTINCT RAW RELEASE: 90 lines, 5,039 bytes, SHA-256 `2205c8e385b779d3d6722a98adad100bd31c46ab921edcc287cf67a2f50043a5`. Its original 80-line prefix is bound by SHA-256 `f31cc1d52765aee14cb4f654dcb76e0098a7c29d8382cc7d81e5700a55370cab`. The pre-proof clarification fixes actual positive lengths, ordinary primes, no rescaling/merging, and separate target clauses.

The 59-line scope report, SHA-256 `a24f4fb6cbee2ad5829754bfd05b03110f526f9b0db4247cf5e9a51f61eb9dc6`, remains unchanged. Root reported its full read before releasing mathematics. Previously fully read ARS router/deep-research/DA/runtime/fallacy/anti-leakage and local guidance are retained as disclosed there. Older infinite-word and factor/history research remains inherited context, not a newly read proof or a theorem transferred to this card.

No author manuscript, README, ledger, appended outcome, peer/helper answer or old scientific file was read. No auxiliary, network, scientific code/numerics, Git or PDF was used. Only this new raw file is written. Proofs below are elementary and self-contained. CP2 manuscript comparison and CP3 final-surface review await root's full raw read and a distinct PAPER UNLOCK.

## 2. Full probability and complete own inverse systems

Put R(n)=n(n+1), so ρ(n)=1/R(n)=1/n−1/(n+1). Summing through N gives 1−1/(N+1), hence total mass one. The consistent cylinder masses ∏ρ(n_i) define the stated product probability: one concrete construction recursively partitions [0,1) into consecutive half-open children with relative lengths ρ(1),ρ(2),… at every node, and records the unique successive child labels of each point. Cylinder preimages have exactly the prescribed product lengths, so the pushforward of Lebesgue probability is a Borel probability on X. Finite-prefix cylinders generate the product Borel sigma-algebra and determine that measure.

Every nonempty cylinder has positive mass, proving full support. For every word z, its length-N cylinder has mass at most 2^(−N), so μ({z})=0 by decreasing continuity. Thus the probability is nonatomic even though each letter has positive mass. All words, including null periodic words, remain source points.

Each of M/G/P/D is total on X and maps to X: gcd is a positive integer and divides both input letters; no zero or terminal is introduced. Each map is continuous in the discrete product topology, hence Borel, since finitely many output coordinates depend on finitely many input coordinates. On a fixed source three-letter cylinder, it replaces that prefix by a fixed two-letter prefix and leaves the whole tail unchanged.

For y=(u,v,η), all own inverse branches are EXACTLY the following; indices are positive integers, with u,v fixed before treating a measure chart.

| Owner | Parameter condition | Inverse image |
| --- | --- | --- |
| M | g divides v, gcd(h,u)=1 | (gh,gu,v/g,η) |
| G | a≥1 | (a,u,v,η) |
| P | g,h≥1, gcd(h,u)=1 | (gh,gu,v,η) |
| D | g divides u and v, gcd(h,u/g)=1 | (gh,u,v/g,η) |

For M/P, gcd(gh,gu)=g exactly under the displayed coprimality condition; substitution gives the target. For D, write u=gq, so gcd(gh,u)=g iff gcd(h,q)=1; the same substitution verifies both coordinates. G simply prepends its source first letter. Conversely, any actual source has uniquely determined g=gcd(a,b) and h=a/g (or its first letter in G). Solving its own output equations gives the corresponding row and all its constraints. Hence Tθ=id on the target cylinder and θT=id on that source cylinder, each source belongs to its unique actual branch, and nothing is omitted.

Every target has countably infinitely many predecessors: for M/P/D use g=1 and h=1+ku, k≥0; G permits every a. These sources are distinct, and the full index sets are countable. Thus all four maps are onto X, with no missing target, restriction on target outgoing steps, or finite inverse cutoff.

## 3. Every-Borel IMAGE and clocks at every word

For a fixed-prefix inverse θ:[u,v]→[a,b,c], let i_2(η)=(u,v,η) and i_3(η)=(a,b,c,η). For EVERY Borel E⊂[u,v], the tail set A=i_2^(−1)(E) is Borel and θE=i_3(A). Product factorization gives

\[
\mu(E)=\rho(u)\rho(v)\mu(A),\qquad
\mu(\theta E)=\rho(a)\rho(b)\rho(c)\mu(A)=J_\theta\mu(E).
\]

These factorization identities hold first on all finite-prefix tail cylinders and then on every Borel tail set by the equality-of-finite-measures monotone-class argument. The finite-prefix cylinders, together with the empty set, form an intersection-closed generating family. Thus IMAGE is not asserted merely from one cylinder ratio.

The fixed all-point version is the constant J_θ=ρ(a)ρ(b)ρ(c)/[ρ(u)ρ(v)] on that entire target cylinder. It is finite and strictly positive, including at null periodic words. The integral law alone would not determine its null values uniquely; the frozen prescription does. Disjoint branch refinements give the law for arbitrary actual injective chart unions, not a sum of all predecessors in a single density. No global measure invariance of M/P/D is claimed from these branch laws.

The actual step clock is

\[
\kappa(z)=\log\frac{R(a)R(b)R(c)}{R(u)R(v)}.
\]

Its signs need not be assumed. Write a=gh,b=gu with gcd(h,u)=1 when examining an input. G has κ=log R(a). P has exp κ=R(a)R(b)/R(b/g)≥R(a)≥2. For M,

\[
e^{\kappa_M}=R(gh)\frac{(gu+1)(c+1)}{(u+1)(gc+1)}.
\]

For g=1 this is R(a). For g>1, (gu+1)/(u+1)≥1 and (c+1)/(gc+1)>1/g, so it is greater than R(gh)/g=h(gh+1)≥3. Therefore κ_M≥log 2, with equality exactly when a=1. G and P also have positive clocks. D instead gives

\[
e^{\kappa_D}=\frac{h(gh+1)(c+1)}{gc+1}>1,
\]

because it is at least (g+1)(c+1)/(gc+1)>1. This verifies strict positivity for every actual step of all four owners rather than discarding potential zero/negative values. No common positive lower bound for D is claimed; with a=b=c=g the displayed ratio tends to one. This is not a separately imposed suspension roof or a completeness argument based on a roof bound.

## 4. Full actual histories and all-point history-pair law

All D_r=X. Put S_r=Σ_{i<r}κ(T^iz), S_0=0, and retain exactly G_T={(z,r−s,w):Tʳz=Tˢw}, with source w and range z. Equal triples, not inverse words, are identified. Two witnesses of a triple differ by a common extension of both depths; their additional sums begin at the same common future and cancel. Thus c=S_r(z)−S_s(w) is well defined. Aligning the shared-point depths proves additivity under composition; inverse changes its sign, and (Tz,−1,z) has c=−κ(z).

For an explicit whole-history check, write z=(z_0,z_1,…) and F_m(z)=∏_{i=0}^{m−1}ρ(z_i). After r steps, the tail from output position 2 onward is exactly (z_{r+2},z_{r+3},…). The product of actual inverse densities telescopes to

\[
J_r(z)=\frac{F_{r+2}(z)}{F_2(T^rz)},\qquad
S_r(z)=-\log J_r(z).
\]

Induction proves this: at the next step the previous output first two weights cancel the next input first two weights, and the new third input is z_{r+2}. The r=0 ratio is one. On a fixed prefix of length r+2, Tʳ is a tail-preserving bijection onto a fixed two-letter cylinder. For two histories meeting at the same output, the chart w→z replaces a prefix of length s+2 by one of length r+2 and has density

\[
\frac{F_{r+2}(z)}{F_{s+2}(w)}=e^{-c(z,r-s,w)}.
\]

The preceding every-Borel prefix argument proves this on the full chart, including every prescribed null-word value. Countably many fixed-prefix history charts cover all arrows. G_T is a countable Borel groupoid: each fixed-depth equality is Borel and each fibre is a countable union of countable inverse generations. The orbit SET, not an assumed nice quotient, is used below.

The exact full-arrow kernels are K_lag={actual arrows with r=s}, K_c={actual arrows with F_{r+2}(z)=F_{s+2}(w)}, and their intersection. These tests are representation independent by the cocycle proof. They do not say that all such arrows are identities, or that all branch densities at one target coincide.

## 5. Entire source/extension groups, incoming and phases

For every source z, nonzero isotropy lag is equivalent to eventual entry into a finite cycle. If its least source period is q, the full source isotropy is qZ, not merely the lag of one chosen loop. Put L=Σ_{i=0}^{q−1}κ(TⁱP) on that cycle. Then c(z,kq,z)=kL, the ENTIRE time group is H_z=LZ, and L>0 by §3. If no forward iterates repeat, source isotropy and H_z are both trivial. Hence extension isotropy ker(c|Iso_G) is trivial everywhere for these four owners, including nonfixed ancestors of fixed points.

The finite-history identity supplies a conditional check for any actual cycle: when T^qP=P, exp L=∏_{i=2}^{q+1}R(P_i). This is a telescoping consequence for a cycle IF it exists, not a search for or classification of new cycles. It is not needed to replace the decisive fixed gate below.

The extension arrow sends (w,h) to (z,h+c). Translation by t in height preserves the equivalence relation and is defined for all real t. At a source component its return group is exactly H_z: translation returns precisely when an isotropy arrow supplies that height difference. If H_z=LZ with L>0, there is one complete physical translation circle of primitive L and repetitions jL, j≥1. If H_z=0 there is a free translation line, not a positive-period orbit. The source period q is not the physical period L.

Define Inv⁰(y)={y} and Invⁿ⁺¹(y)=⋃_{x∈Invⁿ(y)}Inv(x), using ALL rows and indices in §2. Induction proves this equals all depth-n predecessors. All incoming triples to range y are (y,r−n,z) with z∈Invⁿ(Tʳy), r,n≥0. Every witness appears. Compatible infinite incoming histories are exactly sequences y_0=y, Ty_{i+1}=y_i chosen from this tree, without an index/depth cutoff or a new ideal boundary in X.

Two sources are equivalent iff some actual forward iterates meet. Lifted states (z,h),(w,h') are equivalent iff some such r,s also satisfy h−h'=S_r(z)−S_s(w). More explicitly, choose a reference o in a source component and an actual arrow o→z with clock A_z. All arrow times z←w form A_z−A_w+H_o; hence the complete phase is h−A_z modulo H_o. This includes all real phases and does not collapse distinct components that happen to have equal time groups.

As a scope check, an eventually T-periodic word must be eventually periodic in its ordinary tail, by the tail identity in §4. Thus a strictly increasing word is a source with H=0 for all four owners, and the global height-action kernel is trivial. This is a direct tail implication, not a higher-period census or an assertion that arbitrary ordinary-tail equivalence is this groupoid's equivalence.

## 6. ALL global fixed infinite words

Let z=(a,b,c,z_3,…) be fixed. For every owner, equality in positions i≥2 forces z_i=z_{i+1}; therefore the entire tail from c onward is a single positive integer n. This is DERIVED from the full infinite-word equation, not assumed as a test family. Write n^∞ for that constant tail and g=gcd(a,b). The remaining two coordinate equations give:

| Owner | Complete fixed words | Whole fixed clock |
| --- | --- | --- |
| M | m_n=(n,n²,n^∞), n≥1 | λ_n=log[n(n+1)] |
| G | g_n=n^∞, n≥1 | λ_n=log[n(n+1)] |
| P | p_a=(a,a²,(a²)^∞), a≥1 | ν_a=log[a²(a²+1)] |
| D | d_a=(a,a,1^∞), a≥1 | log 2 |

For M, a=b/g and b=gn imply a=n, then gcd(n,gn)=n forces g=n and b=n². Conversely these values satisfy the actual gcd and map. For G, the shift fixed equation forces the whole word constant. For P, b=n and a=b/g imply b=ag, while gcd(a,ag)=a forces g=a and n=a². For D, a=b and b=gn imply g=a and a=an, hence n=1 with arbitrary a≥1. Substitution proves every listed word fixed and exhausts all cases, including the unit word.

At a fixed word, the output first two letters equal a,b, so the density cancels to ρ(n), where n is the derived tail value. This yields exactly the clocks in the table. All are positive; no zero-clock fixed state or terminal exists. No constant-word selection can substitute for the nonconstant-prefix families m_n, p_a or d_a.

## 7. Full fixed-core packets, kernels and multiplicity

For any fixed f in §6 let B_f=⋃_{N≥0}Inv^N(f), using its OWN atlas. This is exactly the entire source component of f: an actual common future with a fixed word is that word. It is countable because each inverse generation is countable, and infinite because even the direct inverse fibre is infinite by §2. It is μ-null but none of its points or histories is deleted. Different fixed cores have disjoint components by deterministic forward evolution.

For z∈B_f choose any N with T^Nz=f and put λ=κ(f), β(z)=S_N(z)−Nλ. Extra fixed steps show β is independent of N. Every integer lag between any z,w∈B_f is realized by extending both histories beyond entry, and

\[
G_T|_{B_f}=B_f\times\mathbb Z\times B_f,\qquad
c(z,k,w)=\beta(z)-\beta(w)+k\lambda.
\]

Thus the FULL component lag kernel has k=0, clock kernel has β(z)−β(w)+kλ=0, and joint kernel has both. Every ancestor has source isotropy Z, entire H=λZ and trivial extension isotropy. The complete phase is [h−β(z)]∈R/(λZ); equivalently use h−S_N(z). All phases lie on ONE physical circle per fixed core, with primitive λ and repetitions jλ. There is no extra packet for each predecessor and no merging of different f's.

These descriptions are constructive full-X incoming formulas, not an unspecified set of ancestors: all integer branch conditions, tail-preserving maps, depth recursion, completeness and exact phase tests have been given. For G specifically, B_{g_n} is exactly all words eventually equal to n, because G is the ordinary left shift. M/P/D use their different complete inverse recursions; this proof does not import G's basin or infer a groupoid isomorphism from equal fixed times.

MAIN has exactly one fixed-origin packet for each n≥1, at the strictly increasing lengths log[n(n+1)]; G has its own one-per-n fixed-origin ledger at the same lengths, but different fixed words for n≥2. P has one fixed-origin packet for each a≥1 at its strictly increasing lengths log[a²(a²+1)]. D has countably infinitely many distinct fixed-origin packets all at log 2. In D, the distinct d_a are even ordinary-eventually-equal tails, yet cannot be G_T-equivalent: any forward iterate of each is itself. This explicitly refutes a tail-based or equal-time packet collapse.

## 8. Decisive bounded gate and strongest positive case

For MAIN the unit word m₁ has H=(log 2)Z and a genuine primitive log 2. But m₂=(2,4,2^∞) is an actual fixed word: its source gcd is 2, its map returns (2,4,2^∞), and its density is ρ(2)=1/6. Its ENTIRE H=(log 6)Z therefore makes log 6 the positive primitive, not a repetition of a hidden shorter period. Since 6 is not an ordinary prime, the frozen necessary prime-only condition fails. No rescaling or alternate measure is used.

More generally every MAIN fixed core n≥2 has composite n(n+1); the two integer factors are both greater than one. The positive fixed ledger is nonempty and has no duplicate lengths within this fixed family, but its nonprime primitive alone suffices for STOP / FORK. This is not a claim that the higher-period inventory is exhausted by fixed words.

The strongest favourable interpretation is retained: the gcd operation genuinely changes future arithmetic, all four original-measure owners and full-point clocks exist, and MAIN really contains a prime-2 primitive. Yet G already reproduces the fixed-clock length list, while D gives a different duplicate-prime failure and P its own nonprime fixed lengths. These are own-control diagnoses, not interchangeable MAIN proofs. Deleting null periodic words, using an a.e.-modified density, choosing only m₁ or merging labels would change the frozen owner.

The authorized fixed gate is complete. No additional periodic-word search or higher-period existence/classification was performed; any conditional cycle identity above is an exact history consequence only. Strong naturalness, global higher-period inventory and analytic/operator ownership remain unestablished here. Classical NOT APPLICABLE; T1 target NOT PASSED; T3 NOT AUDITED; formal Route coordinates UNASSIGNED; Route B NOT INVOKED. No 485 or other object is initiated.

EOF — complete card-only raw; freeze after full self-read. HOLD for root full read and a distinct PAPER UNLOCK. Scope/card/author files untouched.
