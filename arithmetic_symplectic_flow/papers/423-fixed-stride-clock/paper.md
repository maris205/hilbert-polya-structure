# Fixed-stride IMAGE clocks and complete packet splitting

Paper ID: `423-fixed-stride-clock`  
Candidate ID: `ANG-AUDIT-20260923-FSC01`  
Date / status: 2026-09-23; exact conditional class audit, not arithmetic admission.  
Outcome: `FIXED-STRIDE PACKET TRANSPORT ESTABLISHED; RATIONAL PRIME-UNIQUE LEDGER STOP`

T0 and clock COMPONENT only; arithmetic T1 NOT PASSED. T2 conditional. T3 NOT AUDITED. Classical A0–A2 NOT APPLICABLE; formal Route UNASSIGNED; Route B NOT INVOKED.

## Abstract

For the frozen total map T and uniform stride k>=2, the new full owner R=T^k has its own inverse IMAGE clock equal to the integrated k-step clock. Its actual groupoid embeds precisely as the parent arrows whose integer lag lies in k Z. A parent least-q cycle with signed sum C gives d=gcd(q,k) sampled source packets, each of least period q/d and entire clock group ((k/d)C) Z. Every non-eventually-periodic parent packet splits into exactly k sampled packets; lag-zero coalescences remain. Under rational exp(abs(C)) for every nonzero parent cycle, the sampled ledger cannot be simultaneously nonempty, prime-only and unique per prime. Three complete full-source controls separate clock multiplication, packet splitting and the irrational-parent boundary. No source is deleted, and no endogenous prime source, positive suspension or operator is supplied.

## 1. Identity and same-object ledger

| Item | Frozen owner |
| --- | --- |
| Full source | Standard Borel X, sigma-finite mu; no restriction or extra sheets |
| Parent T | TOTAL deterministic Borel map; fixed countable disjoint injective branch partition P_i and actual Borel inverses theta_i |
| Parent versions | Positive finite Borel q_i at EVERY actual inverse target, satisfying mu(theta_i E)=integral_E q_i dmu for every Borel E |
| New evolution | R=T^k for one fixed integer k>=2, on the same complete X and mu |
| Sampled versions | Full k-step itinerary partition, actual inverse words and prescribed inverse-chain products, proved to own IMAGE below |
| Physical carrier | Each owner's own actual integer-lag groupoid and all X times R heights |
| Classical / analytic fields | Symplectic form, mapping torus, Hamiltonian/contact lift: NOT APPLICABLE; trace/operator/determinant: NOT AUDITED |
| Controls | A, B, C each has its own complete parent and sampled owner |

The lineage filter is prime-symbolic fixed batching / non-overlapping block evolution -> actual clock and complete packet retention. This class supplies no arithmetic parent. Fixed-stride sampling is not overlapping higher-block recoding, first-return restriction or a finite-sheet extension. Those distinctions do not transfer results from another owner.

## 2. Question, strongest claim and exclusions

The exact transport theorem determines groupoids, kernels, all source packets and physical returns for T and R. The negative target theorem additionally assumes that EVERY nonzero parent cycle has rational physical multiplier exp(abs(C))>1. Its target is the conjunction of nonemptiness, prime-only primitives and at-most-one packet per prime; all-prime coverage is stronger and separate.
No theorem here prohibits an irrational-parent sampler. The k=1 boundary is not covered by the negative theorem. No per-cycle stride, fitted roof, division of a clock by k, selected core, label quotient, prime table or endpoint modification is permitted. Partial maps with terminal points are outside the frozen class: totalness is used explicitly, not silently supplied. Signed/zero clocks are allowed and are not called a positive-roof suspension.

## 3. Inputs, definitions and provenance

The [frozen card](candidate-card.md), first 83 lines, has SHA-256 `67af700efafe77b4c26c969239019b23008f6f4a4b4dfaa3d5fd76cd2faa0ee1`. Derivation began after root's explicit CP1 release. The card records the pre-freeze targeted collision reads of 409 and 413; neither proof is imported.
Write kappa_T(x)=-log q_i(Tx) on the unique assigned P_i and S^T_n(x)=sum_(j<n) kappa_T(T^j x), S^T_0=0. Every sum is defined because T is total. All-point versions are frozen data; IMAGE alone does not canonically fix values on null periodic points.
For a legal word w=(i_0,...,i_(r-1)), its cylinder is P_w=intersection_(j<r) T^(-j)P_(i_j). Empty cylinders contribute no branch. On each nonempty cylinder T^r is injective, with the actual inverse theta_w=theta_(i_0)...theta_(i_(r-1)) on T^r(P_w). Its target domain is given by the finite Borel tests that every successive inverse lies in the next actual inverse domain; thus the domain and composite are Borel. The countable cylinders partition all X at every finite depth.

## 4. Own IMAGE, complete groupoids and kernels

### 4.1 Composed inverse IMAGE, not an inherited one-step clock

On T^r(P_w), the actual target domain of theta_w, define the all-point product

`Q_w(y)=product_(j=0)^(r-1) q_(i_j)(T^(j+1) theta_w(y)).`

For r=2 this is q_(i_0)(theta_(i_1)y) q_(i_1)(y); every factor is evaluated on its actual domain. The parent Borel IMAGE identities imply the corresponding substitution formula for nonnegative Borel functions, first for indicators, then simple functions, then monotone limits. Repeated substitution therefore proves

`mu(theta_w E)=integral_E Q_w(y) dmu(y)`

for EVERY Borel E in the actual inverse-word domain. Q_w is positive and finite at every point. This is an IMAGE proof for each branch, not an assertion that the union of all preimages has that same density.
For R the words have length k; its prescribed Q_w consequently owns its actual inverse IMAGE. At x in P_w,

`kappa_R(x)=-log Q_w(Rx)=S^T_k(x),   S^R_n(x)=S^T_(kn)(x).`

There is no averaging or division by k. For each owner, every finite incoming history is its full actual inverse-word set. In particular R^(-a){y}=T^(-ka){y}, including ALL such predecessors. Parent predecessors at other depths remain points of X; their sampled packet assignment is determined below, not removed.

### 4.2 Actual cocycles and the exact image of the lag embedding

For U=T or R, let G_U contain every actual triple (z,a-b,w) with U^a z=U^b w. Range is z, source is w; equal triples are identified. Multiplication adds integer lag. To compose witnesses (a,b) and (e,f), align their common middle orbit at t=max(b,e); witness (a+t-b,f+t-e) proves closure. All steps exist by totalness.
Define c_U(z,a-b,w)=S^U_a(z)-S^U_b(w). Two witnesses for one triple differ, after ordering, by adding the same number of steps to both exponents. Added sums start at the same common tail and cancel. This proves descent; the aligned-witness argument proves additivity. The forward arrow (Uz,-1,z) has -kappa_U(z), consistent with the card's sign convention.
The map

`Psi:G_R -> G_T,   (z,l,w) -> (z,kl,w)`

is an injective groupoid map and preserves the clock, by S^R_n=S^T_(kn). Its image is EXACTLY {g in G_T:ell_T(g) in k Z}.
For the converse inclusion, take a parent witness (a,b) with a-b divisible by k. Choose t in {0,...,k-1} so that a+t and b+t are both divisible by k. Advance the meeting point by t legal parent steps; the resulting R witness is ((a+t)/k,(b+t)/k). Totalness is the precise reason this advance is always legal. Clock compatibility follows by cancellation of the added tail.
For nonempty X and k>=2 this image is proper: every x has the parent lag-one arrow (x,1,Tx). No assertion of full-parent surjectivity or of first-return invariance is made.
Clock compatibility also extends Psi to the height groupoids, with the identity on all X times R objects. It does not assert injectivity of the induced map on physical orbit classes; the complete packet splitting below retains its distinct sampled preimages.

### 4.3 Complete kernels and retained coalescences

For EACH owner U, on all of its objects and arrows,

`K_ell(U)={(z,0,w): U^a z=U^a w for some a>=0};`
`K_c(U)={(z,a-b,w): U^a z=U^b w and S^U_a(z)=S^U_b(w)};`
`K_joint(U)={(z,0,w): U^a z=U^a w and S^U_a(z)=S^U_a(w) for some a}.`

These formulas are witness-independent by §4.2. They do not assume injectivity of T or equal clock and lag kernels. The exact transport identities are

`Psi(K_ell(R))=K_ell(T);`
`Psi(K_c(R))=K_c(T) intersect {ell_T in k Z};`
`Psi(K_joint(R))=K_joint(T).`

The first and third use the full image theorem and the fact that lag zero is a multiple of k. Thus every nonunit lag-zero coalescence remains; an arbitrary residue restriction does not discard these arrows. These are identities of actual subgroupoids, not of a quotient that has erased lag.

## 5. All packets, entire H and the rational filter

### 5.1 Parent isotropy and physical phases

For a total deterministic U, a nonzero isotropy lag is equivalent to eventual periodicity: U^a x=U^b x, a>b, exhibits a periodic tail. If its eventual core has least period N and signed cycle sum D, exactly the lags N Z occur, using late enough witnesses; their clocks are nD. Thus its ENTIRE H is D Z. A non-eventually-periodic point has source isotropy and H equal to zero.
The height extension uses all (w,h)->(z,h+c_U(g)). Its isotropy is the kernel of c_U on source isotropy: zero when D!=0, all N Z when D=0, and zero in a non-eventual packet. Zero cycle clock does not erase nontrivial source isotropy.
To include every incoming and height phase, fix a reference x_* in a source packet and choose g_x=(x,l_x,x_*) FROM x_* TO x, with b_x=c_U(g_x). Every arrow y->x is g_x u g_y^(-1), u in the reference isotropy group. All physical extension orbits over this source packet are therefore labelled by [h-b_x] in R/H.
In an eventual packet the complete arrow list has lag l_x-l_y+nN and clock b_x-b_y+nD, n in Z. Clock, lag and joint kernels impose the corresponding zero equations. In a non-eventual packet there is a unique arrow between two sources, with just the two differences. No global Borel choice of references or nice quotient manifold is asserted.
Height translation is transitive on R/H and has stabilizer H. For D!=0 there is ONE positive primitive packet per source packet, with least time abs(D) and repetitions r abs(D), r>=1. For H=0 the physical orbit is setwise a real translation line, not a zero-length closed packet. Distinct source packets with equal D remain distinct.

### 5.2 Every eventual basin and its sampled splitting

Fix a parent least-q cycle O={x_j:j modulo q}, Tx_j=x_(j+1), with C=sum_(j<q) kappa_T(x_j). Its full parent basin is B_O=union_(a>=0) T^(-a)O, which is one actual parent source packet.
If T^a x=x_j, define eta(x)=j-a modulo q. Advancing the landing time changes j and a by the same amount, so eta is independent of the landing choice. Within B_O the complete parent arrow test is

`(z,l,w) in G_T  iff  l = eta(w)-eta(z) modulo q.`

Necessity follows by comparing eventual phases at a common tail. Conversely for any such integer l choose sufficiently large nonnegative a,b with a-b=l, after both sources enter O; their phases then coincide. This proves the full test, not only its restriction to core points.
Put d=gcd(q,k). By §4.2, sampled arrows must solve

`k l = eta(w)-eta(z) modulo q.`

This congruence has a solution iff eta(z)=eta(w) modulo d: dividing by d leaves coprime coefficients, and multiplication by k/d permutes the residues modulo q/d. Hence the full parent basin splits into EXACTLY d sampled packets

`B_(O,r)={x in B_O:eta(x)=r modulo d},   0<=r<d.`

Each is nonempty, containing x_r. Its core consists of the parent phases r+nk modulo q; their least return count under R is N=q/d. All transient objects in that class eventually reach that core under R, because sufficiently large multiples of k pass their parent entry time. Thus B_(O,r) is also exactly the full R-incoming saturation of that core.
One sampled core traversal makes kq/d parent steps, namely k/d complete parent cycles. Its signed sum is D=(k/d)C, independent of r. Equivalently, parent isotropy q Z intersect k Z is lcm(q,k) Z, and rescaling lag by k gives

`G_R,x^x=(q/d) Z;   c_R(x,nq/d,x)=n(k/d)C;   ENTIRE H_R,x=((k/d)C) Z.`

Extension isotropy is zero for C!=0 and the full (q/d) Z for C=0. Every one of the d source packets remains in either case. When C!=0, each has primitive (k/d)abs(C) and all repetitions; when C=0, each has a free height line with retained ineffective source isotropy.
For every sampled packet choose its own reference arrows as in §5.1. They give ALL incoming phases R/(((k/d)C) Z) and all kernel equations, with N=q/d and D=(k/d)C, without selecting a phase or merging equal-time packets.
Changing the parent reference phase shifts eta by a constant and permutes the residue labels r. Cyclic summation leaves C unchanged. The actual core sets, packet count, H and repetition convention are thus reference-independent. Eventual periodicity for T and R is equivalent: an R-periodic tail is a T-periodic tail, and a finite T-cycle is permuted by R.

### 5.3 Every non-eventual packet splits into k packets

Let O be a parent non-eventually-periodic source packet. Fix w in O. There is one actual parent arrow g_z=(z,l_z,w) for every z in O: two different lags between the same sources would produce nonzero isotropy at w. Set b_z=c_T(g_z).
Every arrow y->z has parent lag l_z-l_y and clock b_z-b_y. By the exact image theorem, it is sampled precisely when l_z=l_y modulo k; its R lag is (l_z-l_y)/k and its clock remains b_z-b_y. Thus the sampled classes are O_r={z:l_z=r modulo k}.
ALL k residue classes occur: T^j w has the parent reference arrow (T^j w,-j,w), for j=0,...,k-1. These are distinct points because a repetition would make w eventually periodic. Hence there are exactly k sampled packets, not merely at most k.
Within each O_r, source and extension isotropy and H are zero; the complete physical phase is h-b_z in R. Clock kernel imposes b_z=b_y, lag kernel imposes l_z=l_y, and their intersection both. Distinct points with the same lag, including nonunit coalescences, are retained. A changed reference only relabels residues and translates phases; it does not change the count.
Sections 5.2–5.3 exhaust X: every point either has a periodic tail or does not. No extra positive packet can arise from an infinite non-eventual history, and no terminal case is hidden in this total-map theorem.

### 5.4 Rational-cycle obstruction to the joint target

Assume k>=2 and M=exp(abs(C)) is rational >1 for EVERY nonzero parent cycle. For any such cycle, let d=gcd(q,k) and a=k/d. Each of its d sampled packets has exp(L)=M^a.
If L=log p for an ordinary integer prime p, write M=A/B in lowest positive integer terms. A^a=p B^a forces B=1, since any prime divisor of B would divide A. Then A^a=p forces a=1 and A=p. Thus a>1 already violates prime-only support.
If a=1 and the time is prime-log, then d=k>=2 and the d distinct sampled packets all have the same prime time. Uniqueness fails. If that time is not prime-log, prime-only fails instead. Therefore every nonzero parent cycle prevents the two support/uniqueness requirements from holding together.
If there is no nonzero parent cycle, every eventual sampled cycle still has zero clock and every non-eventual packet has H=0. The positive ledger is empty; support and uniqueness may be vacuous, but nonemptiness fails. This completes the obstruction for the THREE requirements jointly, without assuming a parent cycle exists.
The proof does not cover irrational M: M^a can equal a prime without a=1. Nor does it cover k=1, where no forced multiple packet count follows. Removing residue classes or dividing the integrated clock by k would change the frozen owner; neither is a repair inside this audit.

## 6. Three complete, independently measured controls

### 6.1 Full formulas for each parent and sampled owner

Use the following common notation only to derive each specified map explicitly: X=R times Z/s with Lebesgue times counting, and Q(x,j)=(b x,j+r), b>1. For s=1 this is simply the full real line. In the frozen controls the pairs (parent;sampled) are

| Control | Parent (s,b,r) | Sampled (s,b,r) |
| --- | --- | --- |
| A | (1,3,1) | (1,9,2) |
| B | (3,2^(1/3),1) | (3,2,3) |
| C | (1,sqrt(3),1) | (1,3,2) |

For EACH displayed owner its actual global inverse is Q^(-1)(y,j)=(y/b,j-r). Decomposing any Borel set by target label and substituting y/b proves its OWN inverse IMAGE factor 1/b, including the frozen derivative version at y=0. Thus each owns clock lambda=log b, and its complete depth-m incoming set is the single point (b^(-m)y,j-mr). The sampled identities are proved from these actual sampled inverses, not copied from a parent clock.
The complete groupoid for EACH row and column is

`G_Q={((b^(-l)y,j-rl),l,(y,j)): y in R, j in Z/s, l in Z},  c_Q=l log b.`

Invertibility proves the equivalence with every common-tail witness and realizes every integer lag. Therefore all three kernels K_c, K_ell and K_joint are units for all six owners. Every extension isotropy group is trivial, since log b>0.
For x!=0 there is no periodic or eventually periodic point: b^n x=x with n>0 is impossible, and invertibility rules out a preperiodic point entering zero. Every nonzero source packet is classified exactly by writing uniquely x=epsilon b^n u with epsilon in {+1,-1}, 1<=u<b, n in Z, and setting j_0=j-rn modulo s. Its invariant is (epsilon,u,j_0), and the full orbit is {Q^v(epsilon u,j_0):v in Z}. No nonzero real point or label is lost.
In every such packet source isotropy and ENTIRE H are zero; its complete height phase is h+log(abs(x)) in R. Indeed an arrow of lag l changes log(abs(x)) by -l log b and height by +l log b. Height translation is free. This classifies all nonzero physical orbits of parent and sampled controls, not just their periodic ledgers.
At x=0, the label permutation j->j+r has g=gcd(s,r) cycles of least length N=s/g (with g=1 for s=1). Its complete incoming remains in its own zero core. For one such core choose j_0 and write j=j_0+rt, t modulo N. Source isotropy is N Z, ENTIRE H=N log b Z, extension isotropy zero, and the full phase is [h+t log b] modulo N log b. Its primitive is N log b with repetitions nN log b. These zero cores and the preceding nonzero packets exhaust all six sources; there are no terminals or zero-clock periodic cores in these controls.

### 6.2 Exact positive ledgers and adverse distinctions

| Control | Complete parent positive ledger | Complete sampled positive ledger | Decision |
| --- | --- | --- | --- |
| A | One fixed core, L=log 3, H=log 3 Z, source isotropy Z | One fixed core, L=log 9, H=log 9 Z, source isotropy Z | Prime-only STOP by clock multiplication |
| B | One least-3 core containing all three zero labels, L=log 2, H=log 2 Z, source isotropy 3 Z | Three distinct fixed cores, each L=log 2, H=log 2 Z, source isotropy Z | Prime uniqueness STOP by actual packet splitting |
| C | One fixed core, L=log sqrt(3), H=log sqrt(3) Z, source isotropy Z | One fixed core, L=log 3, H=log 3 Z, source isotropy Z | Necessary sampled target holds, outside rational-parent hypothesis |

The sampled log 9 in A is primitive for that owner, not a repetition of a sampled log 3 packet. In B the parent 3-cycle is primitive, while all sampled cores are fixed; its three identical times do not identify three packets. Every non-eventual parent packet splits into k=2,3,2 sampled packets respectively, as also follows directly by restricting its integer iterate index to those residues.
In C, sqrt(3) is irrational: a reduced equality A/B=sqrt(3) gives A^2=3B^2, forcing 3 to divide A and then B. Its parent multiplier is therefore genuinely outside the rational condition. Its sampled owner supplies only the prime-3 necessary ledger, not all-prime coverage, an endogenous prime source or candidate admission. C prevents promotion of §5.4 to an unconditional acceleration no-go.
All controls retain both zero and nonzero sources, their complete incoming and all real phases. The main theorem, not the positive controls, handles arbitrary signed and zero parent cycle sums. Full inverse-word ownership, lag-zero retention, primitive/repetition separation and the irrational boundary are the applicable controls. Arithmetic-label randomization has no supplied arithmetic parent to test.

## 7. Gate assessment and limitations

| Gate | Exact status | Limit |
| --- | --- | --- |
| T0 | CONDITIONAL FULL OWNERS AND EXACT LAG IMAGE ESTABLISHED | Parent hypotheses and totalness required |
| T1 component | OWN COMPOSED IMAGE CLOCK ESTABLISHED; ARITHMETIC T1 NOT PASSED | No endogenous prime source or canonical null-set version supplied |
| T2 | COMPLETE CONDITIONAL PACKET SPLITTING / H / PHASES ESTABLISHED | Rational k>=2 joint target STOP; irrational boundary remains |
| T3 | NOT AUDITED | No operator, trace or determinant |
| Classical / formal Route | NOT APPLICABLE / UNASSIGNED | No evaluation or inherited credit |
| Route B | NOT INVOKED | No rescue of the stopped target |

This is not a theorem for partial maps, variable strides, section induction or overlapping block recoding. The full groupoid kernels, including possible coalescences, are retained rather than forced to be units because the controls are invertible. Strong naturalness and the origin of a prime-symbolic parent remain OPEN. No novelty or general geometric impossibility is claimed.

## 8. Conclusion and decision

STOP nontrivial fixed-stride sampling under the stated rational-cycle hypothesis as a route to a nonempty prime-only unique ledger. Retain the full-owner transport theorem as a breadth-search filter. C requires the irrational boundary to remain explicit, not to be admitted as an arithmetic candidate. A future FORK needs a separately frozen source and assumptions; none is started here. The same-object ledger is intact for each parent/sample pair, with the new evolution and its new integrated clock named explicitly; no cross-control assembly occurs.

## Reproducibility / evidence index

The [card](candidate-card.md), [claim ledger](claim-ledger.md), [README](README.md) and complete proofs above supply the exact record. All statements are affine, integer, permutation or groupoid derivations; there is no numerical precision/cutoff or finite orbit scan. No scientific numerical run/code, literature campaign, external API, operator computation, Git, PDF or publication was performed.
Input and artifact checks use `sed -n '1,160p' papers/423-fixed-stride-clock/candidate-card.md`, full EOF self-reads, `wc -l`, `sha256sum`, local-link checks and first-20-line Candidate ID/single identical Outcome checks. Only the three authorized author files are written using `apply_patch`. Mechanical checks verify bytes and links, not mathematical truth. Root owns card append and CP2/CP3 integration; these gates are not pre-certified by the author.

## AI assistance, access and integrity disclosure

Root `/root` proposed the batch and owns freeze/release/integration. Author `/root/batch_clock_scope_review` designed this scoped audit after targeted registry keywords and the two complete collision-card reads recorded in the frozen card, then read the full 83-line 423 card, derived the general theorem and drafted/self-checked the three author files. No old theorem was imported. Post-release scientific file inputs were the frozen 423 card and this author's outputs; instructions/template and ARS guidance were read or retained. No current reviewer/raw/peer or sibling manuscript was read.
Bounded author aid `/root/batch_clock_scope_review/ccg_cotangent_probe` received definitions only through the 423 card and was assigned the three complete controls, not the general theorem. Its actual access receipt reports only `sed` of the entire 83-line card and `sha256sum` matching the above digest; no other files, writes, scientific code, network or additional agents. Its returned formulas were checked against §6; this is author assistance, not independent review. Shared historical context remains: NOT_CALIBRATED, not blind or cross-model validation.
AI agents supplied mathematical derivation, drafting, checking and AI-assisted internal review. No human or external verification is certified. The card and scout record design exposure; they are not sealed preregistration. ARS supplied bounded claim/evidence and disclosure discipline, not a full publication pipeline; `criteria_binding_unavailable`, no venue or submission-readiness claim.
Data availability: all exact definitions/proofs are in this package; no dataset or hidden numerical evidence. Ethics: no human/animal subjects or personal data. Contributions: named AI task provenance does not establish human authorship or CRediT attribution. Funding and conflicts: no human declarations supplied; UNKNOWN, not certified absent.
