# Independent card-only proof — divisor-driven complete torus covering

Candidate `ANG-20260922-DTC01`; batch `NONUNIT-RETURN-20260922-I`, round 3/5.
Sole scientific input: `candidate-card.md`, full 97 lines, SHA256 `b55d995aea2d95e131a184d17a9d2a4790e44209a09347edd0bb371bb15efed0`.
Root explicitly released mathematics after reading CP1. No author manuscript, peer/scout, old382 text/proof or other new package was read.
Internal inherited-model/shared-history **NOT_CALIBRATED**, not blind or external peer review. ARS and stream instructions are retained.
No network, scientific numerics, delegation, Git, PDF, new architecture or wider cycle census; only this raw report is written.

## 1. Entire arithmetic path source

For s=(a,b) coprime positive and d|(a+b), the next pair is (b,c), c=(a+b)/d>0.
Since gcd(b,a+b)=1, also gcd(b,c)=1. Thus every declared edge really remains in S; d=1 is always legal.
For each root the finite-prefix tree is finitely branching and has no dead end. Always choosing d=1 supplies an infinite continuation of every prefix.
Give each root path space X_s its cylinder topology; it is compact by the finite-branching diagonal argument.
In the ambient discrete-root/discrete-edge sequence space, every illegal transition is a finite-prefix witness, so X is closed there.
The full X is the countable coproduct of all X_s, not one chosen recurrent root or a compactification by extra states.
At a target root r=(b,c), a preceding edge with label d must start at s=(dc−b,b).
Its exact conditions are dc>b and gcd(dc−b,b)=gcd(d,b)=1, using gcd(c,b)=1; conversely these conditions give a valid source and d|(dc).
They are precisely the card's complete incoming arithmetic domains. Infinitely many choices exist: d=1+kb is coprime to b and eventually satisfies dc>b.
Each such prefix is a homeomorphism X_r onto its actual first-edge cylinder. Shift is total, continuous and onto; all roots and all infinite paths remain.

## 2. Whole torus map and every inverse sheet

The integer matrix A_d=[[0,−d],[1,0]] induces the torus map (x,y)↦(−dy,x), with determinant d>0.
Given target representatives (u,v)∈[0,1)^2, its complete solutions are x=v and y=(k−u)/d mod1, 0<=k<d.
Substitution proves A_d I_{d,k}(u,v)=(u,v). Conversely any preimage has exactly one such residue k modulo d.
Different k give distinct torus points; at u=0 the list is exactly y=k/d, including y=0. No coordinate-cut value is excluded.
Together with the unique preceding arithmetic state for d, these are exactly all full-Y predecessors; different d give different first-edge paths.
On the actual image of each sheet, applying F and then that sheet is the identity. Global sheets are Borel bijections, not globally smooth choices of representatives.
Around EVERY torus point the actual map has a smooth invertible local lift with matrix A_d and Jacobian d; the inverse local Jacobian is 1/d.
These local covering charts, including charts crossing a representative cut, prove all-point fibre ownership. No singularity of the torus map is inferred from the cut.
Every fibre map is a d-sheeted covering of the connected torus; its full domain, not selected inverse-sheet centres, is retained.
For a legal arithmetic prefix alpha of length n with labels d_0,...,d_{n−1}, put Delta(alpha)=Π_i d_i, with empty product 1.
Its forward fibre matrix is M_alpha=A_{d_{n−1}}...A_{d_0}, determinant Delta(alpha); iterating the complete inverses gives exactly Delta(alpha) distinct preimages of each fibre target.
Every finite inverse history is a legal backward arithmetic prefix plus all of its residue-sheet choices. Intermediate domains, every unit d=1 and every torus point are included.
Since arithmetic incoming exists at every root and A_d is onto, F is total and onto. It is continuous, being the declared skew product on first-edge cylinders.

## 3. Own probability, support and symbolic atom/stationarity checks

The root sum satisfies 0<1/4<=C=Σ_{(a,b)∈S}2^{−a−b}<=Σ_{a,b>=1}2^{−a−b}=1.
Thus eta is a positive probability on all roots. Each Z_s is positive finite and Σ_{d|a+b}P_s(d)=1.
The consistent cylinder masses eta(s_0)Π_{i<n}P_{s_i}(d_i) define the stated Markov probability rho on the full countable-state path space.
Every legal cylinder has positive mass, so rho has full support; rho times normalized flat Haar lambda_2 is the full-support probability mu on Y.
Neither stationarity nor a symbolic atom claim is needed for this construction; both can be checked directly without assuming them.
If a path uses d>=2 infinitely often, its transition product is zero because each such transition has probability <=1/2.
If it uses only finitely many such edges, it eventually follows d=1. Its coprime pair modulo2 is nonzero and cycles with period3 under (a,b)↦(b,a+b).
Consequently a+b is even infinitely often, Z_s>=1+1/2 there, and its unit-edge probability is <=2/3 infinitely often. Its path mass is again zero.
Thus EVERY symbolic singleton is null; the cylinder partitions separate points and show rho is atomless. This is a proved property, not a substituted source law.
The law is not stationary. The shifted mass of root(1,1) is

    C^{-1} Σ_{d>=2} 2^{−d}/(d Z_{(d−1,1)}) <= (3C)^{-1}Σ_{d>=2}2^{−d}=1/(6C),

because d Z_{(d−1,1)}>=d+1>=3. Its original root mass is 1/(4C), strictly larger.
Thus rho and also mu are not invariant under their respective full forward maps; no invariant flow measure is inferred.
All these null paths and torus points nevertheless remain in the candidate and in every all-point statement below.

## 4. Every-Borel IMAGE and the distinct geometric clock

For an arithmetic edge e:s→r with divisor d and every Borel B⊂X_r, the Markov cylinder formulas, then the monotone-class extension, give

    rho(prepend_e B)=[eta(s)P_s(d)/eta(r)]rho(B).

On each Borel torus sheet, lambda_2(I_{d,k}E)=d^{-1}lambda_2(E) for every Borel E⊂T².
Indeed partition the representative square into the affine pieces of the displayed inverse; each has determinant magnitude 1/d. Boundary pieces and their images have Haar measure zero and are retained.
Product rectangles and monotone-class extension therefore give, for EVERY Borel E⊂X_r×T²,

    mu(I_{e,k}E)=j_{e,k} mu(E),   j_{e,k}=eta(s)P_s(d)/(d eta(r))>0.

This includes arbitrary null restrictions and all cut values, not only open sets or almost-everywhere-selected source points.
For a complete prefix/sheet history alpha ending at root r, the full IMAGE factor is

    j_alpha = [eta(s_0)/eta(r)] [Π_i P_{s_i}(d_i)] / Delta(alpha).

All inverse, composition and word consistency follow from the actual bijective sheets and these telescoping factors.
Separately, the complete FIBRE inverse-area factor is 1/Delta(alpha) on every local history chart. The frozen geometric clock is therefore tau=log d and S_n=log Delta_n.
It does not depend on a root-density replacement, stationary law, selected orbit or rescaling. Unit steps have exactly tau=0.
At the constant2 edge based at (1,1), Z=3/2 and P(2)=1/3, so the FULL j is 1/6 while the FIBRE clock is log2, not log6.
No smooth total-Y volume, positive-roof suspension or full-measure modular clock is substituted for this prescribed geometric clock.

## 5. Actual groupoid, clock and constructive descriptions of ALL kernels

Write Delta_m(z) for the product of the first m actual labels of the full state z, Delta_0=1.
For g=(z,m−n,w) with F^m z=F^n w, the frozen formula is c(g)=log[Delta_m(z)/Delta_n(w)].
If another witness has the same lag, both lengths differ by the same integer; extending the shorter witness multiplies numerator and denominator by the same common-tail product.
Thus c is presentation-independent on the actual equal-triple groupoid. Common extensions at an intermediate meeting prove addition under composition; inversion negates c.
Composition/inversion of arrows themselves follows by aligning the two intermediate forward histories. Units are (z,0,z); no free sheet-word labels are retained.
The arrow set is Borel and source fibres are countable, by countably many finite arithmetic histories and their finite sheet sets.
Locally the arrow w→z is inverse along its z-history after forward motion along its w-history, hence its FIBRE Jacobian is Delta_n(w)/Delta_m(z).
Therefore c is minus its logarithm, with the correct arrow orientation; the full Markov IMAGE factor for such a local arrow is a different ratio of j-history factors.
In particular a prefix arrow (z,n,F^n z) has +log Delta_n(z); the forward arrow (F^n z,−n,z) has −log Delta_n(z).

Here is a complete finite-history parametrization rather than a list of tested kernel loops.
Take ANY common full target u∈Y and ANY two admissible complete inverse histories alpha,beta ending over u, including all residue sheets and empty histories.
Put z=I_alpha u, w=I_beta u, m=|alpha|, n=|beta|. This produces every actual arrow (z,m−n,w); equal triples alone are identified.
In this parametrization the entire kernels are

    ker c:                 Delta(alpha)=Delta(beta);
    ker lag:               |alpha|=|beta|;
    ker c intersect ker lag: BOTH conditions.

The common FULL target/sheet condition is essential; equality of symbolic products alone is not an arrow criterion.
Unit-only prefixes have product1 and remain in ker c, including nonzero-lag arrows. Distinct residue sheets for the same d=2 prefix give nonunit arrows in the intersection.
The two kernels are not equal: prefixes with d=2 and d=3 into root(1,1), with any sheets over the same target, have equal length but clock log(2/3).
These exact prefix-product conditions cover every source point, including all nonperiodic states and all null restrictions.

## 6. Full isotropy, its clock kernel, all incoming phases and physical packets

For any of these deterministic full maps, source isotropy is {0} unless the FULL state is eventually periodic.
Indeed a nonzero-lag self-meeting is exactly a repeated forward state. If the eventual least full period is q, all self-meeting lags and only those lags form qZ.
For MAIN's clock (and A/C on their own full states), choose a preperiod r and put D=Π_{i=r}^{r+q−1}d_i, L=log D. Then c(q)=S_{r+q}−S_r=L; the prefix cancels. U uses its own determinant1 clock, proved separately below.
Thus on source isotropy c(jq)=jL: if D>1 its kernel and extension isotropy are {0} and H=LZ; if D=1 its kernel/extension isotropy are qZ and H={0}.
For a non-eventually-periodic full state, source/extension isotropy and H are all {0}; this is now a defined-clock result, not an inference from an absent clock.
In MAIN, an all-unit arithmetic cycle cannot exist: at d=1 the root sum changes from a+b to a+2b>a+b.
Hence any eventual full cycle in MAIN has D>1. Extension isotropy is therefore trivial at ALL MAIN states, even though periodic source isotropy is nontrivial.
These statements concern the least JOINT period; a symbolic period by itself is insufficient to determine q or D over that full cycle.

For a MAIN core cycle C of q full states, its entire source orbit is O_C=union_{r>=0}F^{-r}(C).
Every such state is obtained from some core state by all legal arithmetic prefixes and all of their fibre sheets; conversely a common meeting with the core is exactly eventual entry into C.
Two distinct forward core cycles cannot share a source orbit, since iterates of either cycle stay on it and cannot meet the other.
All incoming arrows to any z are (z,m−n,I_alpha(F^m z)) for every m>=0 and every admissible inverse history alpha of length n, with equal triples identified.
Passing through arbitrary additional incoming prefixes therefore does not add smaller isotropy lags or enlarge H; conjugation preserves both lag and scalar loop clock.
For a general source orbit choose any reference state o ONLY to describe coordinates. For an arrow g:x→o, the full physical phase is h+c(g) modulo H_o.
Changing that arrow changes the phase by an element of H_o, and any two lifted points are equivalent exactly under this condition.
Thus the full extension orbit SET over each source orbit is R/H_o, with all real phases retained and time given by translation; no topological separation or invariant measure is asserted.
If H=LZ with L>0, there is one positive primitive physical packet for that source orbit, of least time L; repetitions have times jL, j>=1.
If H={0}, its physical orbit is a free real line, regardless of whether source/extension isotropy is nontrivial.
No reference-state choice removes an orbit or a phase: all source orbits, not a selected family, carry this description.

## 7. Entire MAIN constant2 probe: exact period one and two

The arithmetic path xi_* constantly repeats (1,1)--2-->(1,1), so its base least period is1 and its entire fibre evolves by A=A_2.
A(x,y)=(−2y,x). Fixed points require y=x and 3x=0 mod1, giving exactly v_j=(j/3,j/3), j=0,1,2.
They have full joint least period1, source isotropy Z, trivial isotropy clock kernel/extension isotropy, and entire H=(log2)Z.
Since they are different fixed full states, their core cycles cannot meet. They therefore give THREE distinct primitive packets of time log2, each with all phases R/(log2)Z.

A²=−2 I, so its full fixed set is precisely {(i/3,j/3):i,j∈{0,1,2}}.
On this nine-point set A interchanges the two coordinates, since −2j=j mod3. The three diagonal points are already fixed.
The remaining six points have exact least period2 and form exactly the THREE cycles

    C_{ij}={(i/3,j/3),(j/3,i/3)},   0<=i<j<=2.

Their full joint source isotropy is 2Z, c(2)=2log2=log4, the kernel of c ON THAT ISOTROPY and the extension isotropy are trivial, and ENTIRE H=(log4)Z.
Each two-point cycle gives ONE primitive physical packet, not two; its phases are R/(log4)Z. The three different cycles remain three different packets.
Arrows between its two core states shift phase by log2 but are not isotropy at either state, so they do not make log2 a physical return.
Repetitions are jlog2 for each fixed packet and jlog4 for each exact-two packet; coinciding times never identify packets from different source cycles.

For each of these six core cycles, all incoming states are the full union in §6: every legal arithmetic prefix ending at (1,1), with every fibre preimage of every core phase.
A prefix alpha contributes Delta(alpha) preimages per core torus point, with its actual matrix M_alpha; repeated witnesses are not additional packets.
If F^r w=p_j=A^j p_0 on a q=1 or2 core, the phase at p_0 is h−log Delta_r(w)+jlog2 modulo qlog2.
This follows from the forward incoming clock −log Delta_r(w) and the arrow p_j→p_0 with clock jlog2, and proves full-prefix/phase compatibility explicitly.
All other torus points in the constant2 fibre remain; they are not declared period1/2 or removed. Their owner and general full-H rule are already defined without a further period census.
The necessary target fails twice: three packets at log2 exceed the allowed one-per-prime multiplicity, and log4 is not log of an ordinary prime.
Stop the MAIN target here. Complete only the three frozen controls below; no rescaling, new roof, larger cycle search or T3 construction follows.

## 8. U INDEX-ONE: own full source, IMAGE and zero determinant clock

U retains the full arithmetic X with the same stipulated eta/P law, but its actual fibre map is A_1(x,y)=(−y,x) at EVERY arithmetic edge.
For each admissible incoming arithmetic divisor d there is now exactly one fibre predecessor (v,−u), not d geometric sheets.
All prefix histories remain, with fibre map A_1^n and inverse A_1^{−n}; the arithmetic domain filters of §1 remain unchanged.
Own Haar preservation and Markov prefix summation give j^U_e=eta(s)P_s(d)/eta(r), and j^U_alpha=[eta(s_0)/eta(r)]Π P_{s_i}(d_i), on EVERY Borel set.
The actual geometric determinant is1 everywhere; tau_U=0 and c_U=0 on the entire actual groupoid, independently of the numerical arithmetic divisor labels.
Thus ker c_U=G_U; ker lag is the full synchronous relation, and its intersection with ker c_U is that relation.
Since A_1 is invertible, a synchronous arrow requires equal fibre points as well as equal-depth arithmetic tails; all these arrows, not only units, are retained.
Full source arrows satisfy a common arithmetic tail and the actual condition A_1^m v=A_1^n w, equivalently v=A_1^{−(m−n)}w.
This gives all incoming arrows and their own kernels without importing MAIN's d-sheet inverses.
A_1 has exact fibre period1 at (0,0),(1/2,1/2), period2 at (0,1/2),(1/2,0), and period4 at every other torus point, because A_1²=−I and A_1⁴=I.
If the arithmetic path is eventually least p-periodic, the full U state has eventual least period lcm(p,r_v); otherwise it is not eventually periodic.
Its source isotropy is that full-period subgroup; its clock kernel within isotropy and extension isotropy are the WHOLE source subgroup.
Nevertheless H={0} at every point. The full physical quotient is (Y_U/G_U)×R with unshifted height, all phases and free real-line time orbits.
This includes the constant arithmetic2 fibre and every one of its A_1 source cycles; none supplies a positive primitive physical packet or positive repetition.
For example its constant2 sheet has full j=1/3 but tau_U=0, again distinguishing Markov IMAGE from geometric time.

## 9. A ARITHMETIC-OFF: unrestricted iid prefixes and its own full probe

The source is the ENTIRE N_positive^N with the iid law p_d=2^{−d}, whose probabilities sum to1; all cylinders have positive measure and singleton mass is at most 2^{−n} at depth n.
Thus it is a full-support atomless probability on this different full symbolic carrier. Every d>=1 may be prepended, with no coprimality, root or dc>b filter.
On its full torus fibre the actual map is A_d, with exactly the d complete inverse sheets in §2; its OWN full IMAGE is j^A_{d,k}=2^{−d}/d on every Borel set.
For a prefix alpha, j^A_alpha=Π_i2^{−d_i}/Delta(alpha); local fibre determinant gives its OWN tau_A=log d and c_A=log(Delta_m/Delta_n).
All arrows and the three full kernel descriptions of §5 are obtained using these unrestricted prefixes and their actual shared torus targets, not MAIN's arithmetic domains.
For an eventual FULL cycle of length q, H=(log D)Z and the source/extension-isotropy alternatives of §6 apply to its own cycle product D.
Unlike MAIN, D=1 cycles exist here: their symbolic core is constant1 and their fibre has A_1 period1,2 or4. All eventual incoming states to these cores retain source/extension isotropy and H={0}.
All other eventual cycles have D>1 and trivial extension isotropy; non-eventual states retain the general H={0} rule. No unit state is discarded.
For the constant2 symbolic core, its entire torus map is literally A_2; solving its fixed and square-fixed equations again gives the three diagonal fixed points and three off-diagonal two-cycles of §7.
Those are respectively THREE packets at log2 and THREE at log4, with full source periods1 and2, the corresponding exact H, trivial extension isotropy, all phases and the stated repetitions.
Its full incoming to these cores is now ALL positive-integer prefixes with ALL geometric sheets. Distinct core cycles still cannot meet, by their own forward dynamics.
The incoming phase formula of §7 follows from its own prefix product; no MAIN prefix restriction or IMAGE factor is inherited.
At its constant2 sheet the full j is1/8 while the geometric time is log2. Both the excess log2 multiplicity and wrong primitive log4 are control-specific failures of the same necessary target.

## 10. C CIRCLE-COVER: complete one-dimensional ownership and probe

C retains MAIN's full arithmetic X/eta/P, but its whole fibre is T and the actual map is t↦dt mod1; its own product of full-support rho with circle Haar is a full-support probability.
For each admitted arithmetic predecessor d, its entire inverse family is t=(u+k)/d, 0<=k<d, using u∈[0,1); the half-open interval images include every cut value once.
These are all solutions, distinct modulo1. Own normalized circle Haar gives lambda_1(I_k E)=lambda_1(E)/d for every Borel E.
The own Markov×Haar IMAGE is therefore eta(s)P_s(d)/(d eta(r)), with full history factor eta(s_0)Π P/(eta(r)Delta), now proved for these one-dimensional charts.
The actual derivative is d at every local circle chart, so the index clock is log d; no torus-area or two-dimensional orbit formula is transferred as a geometric justification.
All prefix inverses remain; the fibre forward map for a prefix is multiplication by Delta. Actual groupoid arrows must meet in the full circle state.
Its complete kernels are the equal-product/equal-length/intersection parametrizations of §5 using these actual circle inverse histories and common FULL circle targets.
Its full-state source period q and cycle product D give source isotropy qZ and H=(log D)Z; D>1 for every eventual cycle because the retained arithmetic source has no all-unit cycle.
Thus extension isotropy is trivial at every C point; non-eventual states have H={0}. All incoming histories and real phases remain as in the general actual-orbit construction.
On the ENTIRE constant2 circle, fixed points solve 2t=t mod1, giving only t=0; all points fixed by its square satisfy 3t=0, giving 0,1/3,2/3.
The remaining two points 1/3 and2/3 form ONE exact-period-two cycle. Full joint periods are respectively1 and2, not merely symbolic period1.
The fixed point gives ONE packet with H=(log2)Z; the two-cycle gives ONE packet with H=(log4)Z. Their source isotropy is Z and2Z, and both extension-isotropy groups are trivial.
All admissible arithmetic prefixes and all Delta preimages of each core point give the complete incoming basins; they do not identify these distinct cycles or shorten their H.
Their physical phases are R/(log2)Z and R/(log4)Z; prefix clocks and repetitions follow the same oriented sum rule, now for the actual circle sheets.
Thus this control avoids the torus's fixed-packet excess in this probe but still fails the necessary target through the primitive log4 packet.
Every other circle point and every unit step remains in the source; no additional periodic census or selected circle section is used.

## 11. Scoped outcome and freeze

MAIN owns its full divisor-path torus extension, full-support Markov×Haar probability, all-point fibre clock, every-Borel full sheet IMAGE, entire arrow/kernels and full-state H rule.
The prescribed complete constant2 probe decisively fails the target by both multiplicity and a composite primitive time; all three changed controls have been completed on their own owners.
This is a one-way divisor-selected covering, not strong bidirectional feedback, a new long-memory mechanism, a smooth total-Y volume or an endogenous uniqueness/naturalness theorem.
Strong naturalness remains OPEN. Classical NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; Route B NOT INVOKED.
Portfolio: **STOP / FORK** for this frozen necessary prime-packet target. No change of measure, null-point clock, rescaling, representative selection or borrowed analytic object is made.
Scope and card are unchanged. This raw report freezes before any separately authorized manuscript access.

EOF — full card-only proof and three own controls; MAIN target STOP / FORK; entire period1/2 fibres retained; internal NOT_CALIBRATED; await PAPER UNLOCK.
