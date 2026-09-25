# Full finite-sheet monodromy and the rational prime-packet obstruction

Paper ID: `413-finite-sheet-monodromy`  
Candidate ID: `ANG-AUDIT-20260923-FSM01`  
Date / status: 2026-09-23; exact conditional class audit, not candidate admission.  
Outcome: `FINITE-SHEET MONODROMY ESTABLISHED; RATIONAL NONTRIVIAL PRIME-UNIQUE LEDGER STOP`

Classical A0–A2: NOT APPLICABLE. Formal Route: UNASSIGNED. Route B: NOT INVOKED. T3: NOT AUDITED.

## Abstract

For the frozen full finite-sheet permutation extension, counting measure contributes no additional inverse IMAGE factor: its prescribed all-point clock is exactly the parent clock. A parent least cycle of length q and signed clock C lifts once for each monodromy permutation cycle of length r, with least period qr and entire clock group rC Z. All incoming histories and physical height phases are retained. If every nonzero parent physical multiplier exp(abs(C)) is rational and d>=2, a nonempty ledger cannot have only prime-log primitives with at most one packet per prime. If there is no nonzero parent cycle, the positive ledger is empty instead. Three complete full-real-line controls distinguish duplicate prime packets, one composite-time packet, and an irrational-parent exception to any unconditional prohibition. This is a finite-memory realization filter, not an arithmetic source or an admitted flow.

## 1. Identity and same-object ledger

| Item | Frozen owner and scope |
| --- | --- |
| Parent | Standard Borel X, sigma-finite mu, partial deterministic Borel T:D->X, countable disjoint injective pieces P_i and actual inverses I_i |
| All-point input | Fixed positive finite Borel q_i on T(P_i), satisfying mu(I_i E)=integral_E q_i dmu for every Borel E |
| Full extension | Y=X times {1,...,d}, nu=mu times counting; F(x,j)=(Tx,sigma(x)j), fixed Borel sigma:D->S_d |
| Clock | On each actual refined inverse, the frozen version is q_i(y); kappa_F(x,j)=-log q_i(Tx) |
| Physical carrier | All actual integer-lag common-tail arrows, their clock cocycle and all Y times R heights |
| Primitives | One positive-time packet for each source orbit with nonzero entire H; phase space R/H, least positive time and all repetitions |
| Classical geometry | Symplectic form, positive roof, mapping torus, Hamiltonian/contact realization: NOT APPLICABLE |
| Analytic owner | Operator, trace, zeta and determinant: NOT DEFINED / NOT AUDITED |
| Controls | Three separate owners A, B, C on full R times {1,2}; no source, clock or theorem transfer |

The lineage role is the arrow finite symbolic memory/admissibility -> geometric realization with its full intrinsic packet ledger. No prime-symbolic parent is supplied. Generic controls are EXTERNAL CONTROLS, not main candidates.

## 2. Question and claim boundary

The question is whether this full finite-state extension can satisfy the necessary target: a nonempty positive primitive ledger, every least time log p for an ordinary integer prime, and at most one distinct packet for each p. All-prime coverage would be an additional obligation.
The strongest negative theorem requires d>=2 and rational exp(abs(C)) for EVERY nonzero-clock parent cycle. It says nothing prohibitory about irrational parent multipliers or about d=1. The full monodromy formulas hold without that rational restriction, and include signed and zero clocks.
No step is forced positive; a real clock extension is not automatically a positive-roof suspension. No primality labels, per-prime parameters, zero data, external roof or selected sheet are inserted. No novelty, canonical all-point version, strong naturalness, operator, Route or RH claim is made.

## 3. Definitions, inputs and provenance

The scientific input is exactly the [frozen card](candidate-card.md), first 88 lines, SHA-256 `a3fcaecf9fcaab1f2c7052346ac0aab015adf1cd78ccc678f3de725d49e9e8bb`. Derivation began after the root's explicit CP1 release. No numerical experiment, census, literature search or sibling-paper result is an input.
Write D_m for the points with m legal T steps, D_0=X. Put A_0(x)=id and A_m(x)=sigma(T^(m-1)x)...sigma(x), so F^m(x,j)=(T^m x,A_m(x)j). Let s_m(x)=sum_{a=0}^{m-1} kappa(T^a x); then S_m(x,j)=s_m(x), with S_0=0.
Terminal objects remain in Y; their next-step clock is NOT DEFINED, not zero. IMAGE identities alone determine versions only almost everywhere: the all-point q_i and the no-reassignment lift rule are independent frozen data. The following proof verifies those versions, not their canonicity.

## 4. Exact ownership, groupoid and phase proofs

### 4.1 Full Borel IMAGE and incoming branches

Set P_(i,pi)={x in P_i:sigma(x)=pi}. For each source sheet j the actual inverse is J_(i,pi,j)(y,pi j)=(I_i y,j), with y in T(P_(i,pi)). This image is Borel because T restricted to P_i has its prescribed Borel inverse; it equals {y in T(P_i):I_i y in P_(i,pi)}.
For an arbitrary Borel E in this branch image, write E={(y,pi j):y in E_0}. Then

`nu(J_(i,pi,j) E)=mu(I_i E_0)=integral_(E_0) q_i(y) dmu(y)=integral_E q_i(y) dnu(y).`

Thus the stipulated positive finite all-point q_i is an owned inverse IMAGE version; kappa_F=kappa composed with the base projection. No factor d appears: this is one actual inverse branch, not the measure of the union of all predecessors. Borel disjoint unions follow by countable additivity. For a finite legal inverse word, repeated substitution gives IMAGE density exp(-S_m(z)) at y=F^m z on that word's actual image.
Every immediate predecessor of (y,k) is (x,sigma(x)^(-1)k), for EVERY x in D with Tx=y. More generally every m-step predecessor is (x,A_m(x)^(-1)k) for EVERY x in D_m with T^m x=y. These formulas are both necessary and sufficient. They include all histories leading to terminals; none is selected or discarded. Countably many branch words give countably many actual predecessors at each depth.

### 4.2 Actual lag groupoid, cocycle and complete kernels

Let G consist of all triples g=(z,l,w), l=m-n, with m,n>=0 legal and F^m z=F^n w; source w, range z. Equal triples, not their witnessing words, are identified. Inverse reverses z,w and l. Multiplication adds l when the middle object agrees.
To verify closure, compose witnesses (m,n) for z,w and (p,q) for w,v. With t=max(n,p), extend the shorter middle itinerary to t; the resulting witness for z,v is (m+t-n,q+t-p). All extensions are legal because the middle orbit already has t steps.
Define c(g)=S_m(z)-S_n(w). Two witnesses for the same triple differ by (m',n')=(m+t,n+t), after ordering them. Their added sums start at the same common tail and cancel, proving well-definedness even for partial maps. The same aligned-witness argument proves c(gh)=c(g)+c(h).
In this convention (z,1,Fz) has clock kappa_F(z); the arrow implementing forward transport z->Fz has lag -1 and clock -kappa_F(z). Signed cycle sums and positive generators below respect this convention.
The lag cocycle is ell(g)=l. On the FULL G, without eventual-periodicity restrictions, the exact kernels are

`K_ell={(z,0,w): some legal F^m z=F^m w};`
`K_c={(z,m-n,w): F^m z=F^n w and S_m(z)=S_n(w)};`
`K_ell intersect K_c={(z,0,w): some legal F^m z=F^m w and S_m(z)=S_m(w)}.`

These need not be unit groupoids: equal-time merging, for example, can survive in K_ell. No lag or clock quotient is silently taken. All witnesses give the same tests by the preceding proof.

### 4.3 Entire isotropy and physical phases, including nonperiodic histories

For any partial deterministic map, nonzero source isotropy is equivalent to eventual periodicity: F^m z=F^n z with m>n exhibits a cycle; conversely an eventual cycle supplies such equalities. If its least length is N, every isotropy lag is a multiple of N and every multiple occurs using a sufficiently late witness. If its signed cycle clock is D, additivity gives

`G_z^z = N Z, c(z,kN,z)=kD, H_z=c(G_z^z)=D Z.`

Here integer lags are retained even if D=0. If z is not eventually periodic, including every terminating history, G_z^z={0} and H_z={0}. A terminating source packet is exactly all finite predecessors of its final terminal; it cannot acquire a periodic stabilizer.
The height extension has arrows (w,h)->(z,h+c(g)) on ALL Y times R. Its isotropy at (z,h) is ker(c|G_z^z): zero if D!=0, all N Z if D=0, and zero in the nonperiodic case. Thus H=0 does not erase ineffective source isotropy.
For completeness fix one reference z_* in a source packet and an arrow g_z=(z,k_z,z_*) for every z in it; put b_z=c(g_z). This is an orbitwise description, not an assertion of a global Borel selector. All arrows from w to z are exactly g_z u g_w^(-1), u in G_(z_*)^(z_*). Consequently all physical extension orbits in this source packet are labelled by

`[h-b_z] in R/H_(z_*).`

Different choices change labels only by a fixed reference translation and elements of H. Height translation acts transitively on R/H with stabilizer exactly H. If H=D Z with D!=0 there is ONE closed physical packet, all its phases, primitive L=abs(D), and repetitions kL (k>=1). If H=0 the physical height orbit is a line, not a zero-length closed orbit.
More explicitly in an eventual packet, all arrows from w to z have lag k_z-k_w+nN and clock b_z-b_w+nD, n in Z. Thus K_c imposes b_z-b_w+nD=0, K_ell imposes k_z-k_w+nN=0, and their intersection imposes both, for ALL incoming objects. In a nonperiodic packet there is just the unique arrow g_z g_w^(-1), with these differences and no n term. This also describes all kernels and phases outside cycles.

## 5. Monodromy, multiplicities and the rational gate

### 5.1 Full monodromy theorem

Fix a parent least-q cycle gamma=(x_0,...,x_(q-1)), C=sum kappa(x_s), and Pi=A_q(x_0). Decompose Pi into ALL of its disjoint permutation cycles O. If O has length r and j in O, its lifted core is

`Gamma_O={(x_s,A_s(x_0) Pi^t j): 0<=s<q, 0<=t<r}.`

These are qr distinct points. A return to (x_0,j) must take a multiple of q parent steps, and after v laps its sheet is Pi^v j, so the least lifted period is exactly qr. The signed sum is rC, since each parent lap has sum C independently of the sheet. Hence every object eventually reaching this core has source isotropy qr Z and ENTIRE H=rC Z. Its extension isotropy is zero for C!=0 and qr Z for C=0; its physical primitive exists exactly when C!=0 and equals r abs(C).
The full source packet is E_O=union_(m>=0) F^(-m)(Gamma_O), using the complete predecessor formula of §4.1. Every lifted point over a parent history eventually entering gamma belongs to exactly one E_O. These sets are disjoint: two deterministic futures cannot eventually reach different cores. Each E_O is one common-tail source orbit, since its core is a cycle. Distinct permutation cycles therefore remain distinct packets even when they have equal r and equal time. They are not divided by a multiplicity factor.
No other periodic source packet exists: an eventual lifted cycle projects to an eventual parent cycle, and the finite permutation on that cycle forces every sheet over an eventual parent history eventually into one of these cores. Parent histories that are not eventually periodic lift only to histories that are not eventually periodic, and termination is preserved; §4.3 retains their complete source and height packets.
Changing the parent reference to x_s conjugates the monodromy by A_s(x_0): Pi_s=A_s Pi A_s^(-1). This follows by splitting the ordered product around the cycle and cancelling the prefix. It bijects permutation cycles with the same lengths. The displayed lifted core is the same set with a shifted starting point; cyclic summation leaves C unchanged. Thus source packets, entire H, primitive lengths, multiplicities, incoming and repetitions are independent of reference phase. No sheet numbering has physical significance.

### 5.2 Rational nontrivial extension obstruction

Assume d>=2 and M=exp(abs(C)) is rational >1 for every nonzero-clock parent cycle. Suppose such a parent cycle exists. For one of its monodromy cycles of length r, the primitive has exp(L)=M^r.
If L=log p with p an ordinary integer prime, write M=A/B with coprime positive integers A,B. The equality A^r=p B^r forces B=1: any prime divisor of B would also divide A. Then A^r=p forces r=1 and A=p. This is an exact integer argument, not a numerical comparison of logarithms.
Therefore a permutation cycle of length r>1 already violates the prime-only requirement. If every permutation cycle has length 1, there are exactly d>=2 distinct lifted packets, each with L=abs(C). If that time is not prime-log, prime-only fails; if it is log p, uniqueness for p fails. Thus any nonzero parent cycle defeats at least one of these two requirements.
If no nonzero parent cycle exists, §5.1 and §4.3 show that the entire positive ledger is empty, including when cycles are absent or all have C=0. Prime-only and uniqueness may then hold vacuously, but the target's nonemptiness does not. In every case the THREE requirements together are impossible under these hypotheses.
The proof does not transfer to d=1, which contributes no forced duplicate. It also does not cover an irrational M: M^r=p is possible with M=p^(1/r). The all-point version hypothesis remains essential; no almost-everywhere assertion is substituted at periodic points.

## 6. Three full controls and adverse findings

### 6.1 Each control's complete owner

For EACH fixed pair (a,pi) in A=(2,id), B=(2,(12)), C=(sqrt(2),(12)), take full R times {1,2} with its own Lebesgue-times-counting measure and global F(x,j)=(a x,pi j). The actual inverse is (y,k)->(y/a,pi^(-1)k).
For any Borel E, decomposing by target sheet gives nu(F^(-1)E)=a^(-1)nu(E). On each actual single-sheet inverse the same substitution proves the IMAGE identity with the prescribed all-point density 1/a, including y=0. Its OWN clock is log a at EVERY point. No probability normalization or inherited density is used.
Invertibility gives the full groupoid

`G={(F^(-l)w,l,w): w in R times {1,2}, l in Z},  c=l log a.`

Indeed F^m z=F^n w is equivalent to z=F^(-(m-n))w, and every integer lag has nonnegative witnesses. Since log a>0, K_c=K_ell=their intersection=units on the full source; the corresponding extension kernels are also units. All m-step incoming objects are exactly (a^(-m)y,pi^(-m)k), with no missing branches or terminals.
For x!=0, equality a^n x=x is impossible for n>=1. Invertibility then excludes eventual periodicity. Their source and extension isotropy and H are zero. Their entire source packets can be enumerated exactly, without a census: uniquely write x=epsilon a^n u, epsilon in {+1,-1}, 1<=u<a, n in Z, and put j_0=pi^(-n)j. The invariant (epsilon,u,j_0) labels the full orbit {F^v(epsilon u,j_0):v in Z}. Within it the real phase h+log(abs(x)) labels height-extension orbits, because c=l log a cancels the change of log(abs(x)). Height translation is free; none contributes a positive closed packet.
At x=0, the permutation cycles of pi are all periodic cores, and their only predecessors stay in the same zero core. For a sheet cycle of length r choose j_0 and write j=pi^s j_0, 0<=s<r. Source isotropy is r Z, entire H=r log(a) Z and extension isotropy is zero. The complete phase is [h+s log a] modulo r log a, obtained from the reference arrow of lag -s. All repetitions are k r log a. This describes every point, not only a selected zero fibre or phase.

### 6.2 Exact control outcomes

| Control | Full positive packet ledger | Adverse conclusion |
| --- | --- | --- |
| A: a=2, pi=id | Two different zero fixed-point packets, each primitive log 2; each H=log 2 Z and source isotropy Z | Prime-only but duplicate prime-2 packets; uniqueness FAIL |
| B: a=2, pi=(12) | One zero two-cycle packet, primitive 2 log 2=log 4; H=log 4 Z, source isotropy 2 Z | Multiplicity one does not repair the composite primitive; prime-only FAIL |
| C: a=sqrt(2), pi=(12) | One zero two-cycle packet, primitive 2 log sqrt(2)=log 2; H=log 2 Z, source isotropy 2 Z | Meets the three necessary ledger conditions, NOT all-prime coverage or candidate admission |

Every row has extension isotropy zero, includes both zero sheets, every height and all nonzero real orbits described above. In B, log 4 is the PRIMITIVE, not a repetition of a missing log 2 packet. In C, log sqrt(2) is a one-step clock, not a closed primitive; the single closed primitive is log 2. The full source and clock kernels remain units in all rows despite nontrivial source isotropy.
The parent multiplier in C is sqrt(2), not rational: if sqrt(2)=A/B in lowest terms, A^2=2B^2 forces A even and then B even, a contradiction. Thus C is an explicit boundary comparator, not a counterexample to §5.2. Its frozen coefficient supplies no endogenous prime mechanism; it realizes only the prime-2 necessary ledger. It prevents a PROVES_TOO_MUCH conclusion that no finite cover can ever have a prime-log packet.
Ownership controls are full-sheet retention, branch IMAGE versus total predecessor measure, nonzero-orbit retention and source-isotropy versus effective-height separation. Signed/zero-clock and d=1 boundaries are handled by the theorem, not by positive-clock controls A–C. Shuffled arithmetic labels are inapplicable without a parent arithmetic source. Strong naturalness and the broader PROVES_TOO_MUCH programme remain OPEN.

## 7. Gate assessment

| Gate | Evidence and status | Limit |
| --- | --- | --- |
| T0 | CONDITIONAL OWNER ESTABLISHED; full source, inverse IMAGE versions and actual lag groupoid, §§1–4 | Given all-point parent data, not a newly admitted arithmetic carrier |
| T1 | CONDITIONAL CLOCK INHERITANCE ESTABLISHED; no extra sheet clock, §4.1 | Prime origin and canonical version not supplied; rational-class target STOP in §5.2 |
| T2 | COMPLETE CONDITIONAL MONODROMY / H / MULTIPLICITY ESTABLISHED, §§4–6 | d>=2 rational class cannot meet nonempty prime-only unique target; C lies outside it |
| T3 | NOT AUDITED | No operator, trace or determinant |
| Classical A0–A2 / formal Route | NOT APPLICABLE / UNASSIGNED | No formal evaluation or inherited credit |
| Route B | NOT INVOKED | Not used to repair the stopped target |

## 8. Conclusion and decision

STOP the nontrivial rational-parent full-permutation extension as a way to obtain the necessary nonempty prime-unique ledger. Preserve the monodromy theorem as a breadth-search filter. Any future FORK must name a genuine prime-symbolic parent and separately freeze its changed class or multiplier assumptions; no new fork candidate or round is created here. Control C only keeps the irrational boundary open. The one-object ledger is intact for the conditional construction and independently for each control; they are never assembled into one candidate.

## Reproducibility / evidence index and limitations

The [card](candidate-card.md), this complete proof, [claim ledger](claim-ledger.md) and [package README](README.md) are the scientific record. Exact finite permutation and integer arguments replace precision and cutoff settings. Controls are global on full R times {1,2}; the conditional theorem quantifies over all legal histories, not an enumerated sample. No empirical output, scientific code, simulation, external API, literature search, PDF, publication or Git operation was performed.
Read/check methods: `sed -n '1,240p' papers/413-finite-sheet-monodromy/candidate-card.md`, `wc -l` and `sha256sum` for the frozen input; `apply_patch` for only the three authorized author surfaces; full EOF self-read plus line/hash, local-link, ID and identical-Outcome checks at handoff. Mechanical checks verify bytes and links, not mathematical truth. Root owns card append and CP2/CP3 integration; this author does not certify those later gates.
Limitations: the parent source, measure and versions are assumptions; finite memory is not a prime mechanism; no broad lift impossibility, canonicity, novelty, naturalness or analytic theorem is established. The paper makes no claim that all physical quotients are Hausdorff manifolds or positive suspensions.

## AI assistance, contribution and integrity disclosure

Root `/root` proposed the audit and owns freeze, release and integration. Author `/root/batch_clock_scope_review` refined definitions, read the frozen 88-line card through EOF, derived the general theorem, drafted these three surfaces and performed internal consistency checks. Current scientific access was card-only plus this author's own outputs; repository/template and ARS instructions were read or retained. No current reviewer/raw/peer, sibling-paper or old-paper research file was read for this derivation.
Author helper `/root/batch_clock_scope_review/ccg_cotangent_probe` was assigned only the three frozen full controls. Its actual access receipt reports only `sed` of the complete 88-line card and `sha256sum` confirming the above digest; no other files, writes, scientific code, network or further agents. Its returned formulas were checked against §§4–6; it is author assistance, not an independent reviewer. Shared historical context is retained, so neither author nor helper is blind; calibration is NOT_CALIBRATED, not cross-model or human peer review.
AI agents supplied mathematical derivation, drafting, checking and AI-assisted internal review. No human or external verification is certified. Informal monodromy expectations influenced the pre-freeze design, as recorded in the card; this is not sealed preregistration. ARS was used for bounded evidence/claim discipline and explicit disclosure, not a full publication pipeline; `criteria_binding_unavailable`, no venue-alignment or submission-readiness claim.
Data availability: all exact definitions and proofs are in this package; no dataset or hidden numerical evidence. Ethics: no human/animal subjects or personal data. Contributions: the above are AI task-provenance receipts, not a determination of human authorship or CRediT attribution. Funding and conflicts of interest: no human declarations supplied; UNKNOWN, not certified absent.
