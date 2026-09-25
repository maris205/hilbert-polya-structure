# Integer-slope interval realization, endpoints and the recurrent grammar gate

Paper ID: `418-integer-slope-realization`  
Candidate ID: `ANG-AUDIT-20260923-ISR01`  
Date / status: 2026-09-23; exact conditional class audit, not candidate admission.  
Outcome: `INTERVAL REALIZATION AND IR GRAMMAR CRITERION ESTABLISHED; NO ARITHMETIC CANDIDATE ADMISSION`

Classical A0–A2: NOT APPLICABLE. Formal Route: UNASSIGNED. Route B: NOT INVOKED. T3: NOT AUDITED.

## Abstract

For the frozen full countable Markov interval map, each integer slope d owns inverse IMAGE density 1/d and clock log d. A finite graph closed word has one affine fixed point in the closure of its starting interval, but it is a real periodic point only if it belongs to the actual half-open domain. The explicit interior-realization hypothesis IR on simple graph cycles rules out all such endpoint exceptions. Under IR, prime-only primitive support is equivalent to every cyclic strongly connected component being a singleton self-loop with prime digit. Nonemptiness and prime uniqueness require, respectively, a nonempty cyclic-vertex set and injectivity of its prime digits. These are restrictions on a supplied grammar, not an endogenous prime grammar. The proof retains the full actual groupoid, every incoming and terminal history, all kernels and height phases. Three complete controls distinguish a prime singleton, a composite primitive, and full doubling with excluded endpoint codes and every exact period.

## 1. Candidate identity and same-object ledger

| Item | Frozen owner |
| --- | --- |
| Carrier / measure | FULL X, a union of disjoint nonempty bounded intervals I_v=[a_v,b_v); Lebesgue measure restricted to X |
| Partial map | On active I_v, T(x)=d_v x+beta_v with fixed integer d_v>=2; other cells terminal |
| Actual graph | Edges only from active vertices; T(I_v) is exactly the disjoint union of its target cells, including endpoints; no parallel edges |
| Inverses / clock | Actual affine inverses and their stipulated all-point derivative versions; clock proved from their own IMAGE, not a separate roof |
| Source and physical packets | All legal common-tail integer-lag triples, their owned cocycle and all X times R heights |
| Classical / analytic owner | Symplectic form, positive suspension construction, Hamiltonian/contact lift: NOT APPLICABLE; operator, trace and determinant: NOT AUDITED |
| Controls | Full separately owned A, B, C, with their own actual inverse IMAGE identities |

The lineage role is symbolic digits/admissibility -> full interval geometric realization. This audit supplies no missing prime-symbolic grammar. Its generic controls are EXTERNAL CONTROLS; satisfying a necessary packet condition does not admit them as arithmetic candidates.

## 2. Question and strongest supported claim

The conditional theorem characterizes prime-only support, nonemptiness and at-most-one-packet-per-prime under the stated IR hypothesis. Without IR it instead gives an exact realization test for every finite closed word. All-prime coverage is a separate condition, never inferred from nonemptiness.
No finite graph or finite orbit census is assumed. Infinite escaping graph paths remain in the full owner when realized, but are not closed paths. The graph is the actual image-transition graph; terminals have NO outgoing edges, including formal ones. No prime table, per-prime parameter adjustment, independent roof, selected invariant subsystem, endpoint deletion, inherited clock/operator or formal Route claim is used. No novelty or strong-naturalness claim is made.

## 3. Definitions, inputs and provenance

Input is the [frozen card](candidate-card.md), first 92 lines (original 85 plus CP1 clarification), SHA-256 `508624072f638f23fe35f1d03e50013f9219200f92b692653c02f529725695ed`. Proof began after explicit root CP1 release. No reviewer/raw/peer, sibling or old research manuscript was read for this derivation.
Let D_m be the points with m legal steps, D_0=X. For x in D_m let P_m(x)=product_(j=0)^(m-1) d_(v(T^j x)), with P_0=1. The itinerary v(T^j x) is unique by the disjoint half-open partition. A nonexistent step at a terminal has clock NOT DEFINED, not zero.
IR says that the inverse-word fixed point of EVERY simple directed cycle, including a self-loop, is interior to its starting interval. It is not supplied by the Markov identity; §5 uses it as an additional hypothesis and §6 checks it separately for each control.

## 4. Exact ownership and the complete actual ledger

### 4.1 Borel IMAGE and all incoming

On its actual image T(I_v), let J_v(y)=(y-beta_v)/d_v. For EVERY Borel E in that image, affine substitution gives

`mu(J_v E)=d_v^(-1) mu(E)=integral_E d_v^(-1) dmu.`

This verifies the frozen positive finite all-point derivative version, including included endpoints. The identity alone determines versions only almost everywhere; the actual derivative version is separately fixed by the card. Thus kappa(x)=log d_v on I_v and S_m(x)=log P_m(x). Measure is sigma-finite; no probability normalization is needed.
For any finite path v_0->...->v_m and y in I_(v_m), J_(v_0)...J_(v_(m-1))(y) is an actual m-step predecessor. Each application is defined by the exact image identity, and every predecessor has precisely such an itinerary. This is the COMPLETE incoming set, including paths ending at terminals. At a fixed depth and target, distinct branch words cannot share an initial point, since its itinerary is deterministic. On each such inverse branch the full Borel IMAGE factor is 1/(product_(j<m) d_(v_j)), by repeated substitution. No total-preimage density is confused with a single-branch IMAGE density.

### 4.2 Actual lag, cocycle descent and full kernels

Set G={(z,m-n,w):T^m z=T^n w, both iterates legal}, source w and range z; equal triples are identified and integer lag is retained. Multiplication adds lag. For composable witnesses (m,n) and (p,q), align the middle iterate at t=max(n,p), yielding witness (m+t-n,q+t-p); all extra steps exist on the common middle tail.
Set c(z,m-n,w)=log P_m(z)-log P_n(w). Witnesses with the same lag differ by adding the same nonnegative number of steps to both exponents, after ordering them. Added sums begin at the same tail and cancel. This proves descent; aligned witnesses also prove additivity. The forward arrow z->Tz has lag -1 and clock -kappa(z), whereas (z,1,Tz) has clock kappa(z).
Writing ell for lag, the COMPLETE kernels are

`K_ell={(z,0,w): some legal T^m z=T^m w};`
`K_c={(z,m-n,w): T^m z=T^n w and P_m(z)=P_n(w)};`
`K_ell intersect K_c={(z,0,w): T^m z=T^m w and P_m(z)=P_m(w) for some legal m}.`

The tests do not depend on the witness. Product equality is the clock-kernel test, while zero lag is the lag-kernel test; the two are not identified by definition. Neither is silently quotiented out; equal-time merging can give nonunit arrows, as control C demonstrates.

### 4.3 Entire H, source/extension isotropy and every height phase

If T^m z=T^n z with m>n, z is eventually periodic. Conversely if its eventual core has least period q, exactly the lags q Z occur in source isotropy, using sufficiently late witnesses. If the core digit product is Q, then Q>=2^q>1 and

`G_z^z=q Z, c(z,kq,z)=k log Q, ENTIRE H_z=log Q Z.`

Points not eventually periodic, including all terminating points, have source isotropy and H equal to zero. All height-extension isotropy is trivial: on a nontrivial source isotropy group, c is injective because Q>1. There is no zero-clock periodic core in this expanding class, but all nonperiodic H=0 objects remain.
The height extension uses ALL arrows (w,h)->(z,h+c(g)). In a source packet choose reference z_* and arrows g_z=(z,k_z,z_*), with b_z=c(g_z). Every arrow w->z is g_z u g_w^(-1), u in G_(z_*)^(z_*). Thus all physical extension orbits are labelled by [h-b_z] in R/H. This is an orbitwise parametrization, not a claim of a global Borel section or a Hausdorff quotient manifold.
For an eventual q-cycle packet, all arrows w->z have lag k_z-k_w+nq and clock b_z-b_w+n log Q, n in Z. K_ell and K_c impose the corresponding zero equations; their intersection imposes both. In a nonperiodic packet there is one arrow between any two sources, with the differences and no n term. These formulas cover every incoming object, not just core phases.
Height translation acts transitively on R/H with stabilizer H. Each eventual source packet therefore contributes ONE closed physical packet, primitive L=log Q and repetitions kL, k>=1. Distinct source packets with the same Q stay distinct. An H=0 packet gives a free real translation orbit, not a zero-length closed orbit. A terminating packet is exactly the full finite-predecessor set of its unique terminal.

## 5. Endpoint realization and the IR grammar theorem

### 5.1 Every finite word: actual realization, minimality and multiplicity

For a closed word W=(v_0,...,v_(n-1),v_n=v_0), let D_W=product d_(v_j) and let the unrestricted forward affine composition be f_W(x)=D_W x+B_W. The inverse word J_W=J_(v_0)...J_(v_(n-1)) has slope D_W^(-1)<1, maps I_(v_0) into itself and extends continuously to its closure. Its unique fixed point is

`xi_W=-B_W/(D_W-1) in [a_(v_0),b_(v_0)].`

To see membership in the closed interval without an existence assumption, J_W(a)>=a and J_W(b)<=b. The affine function J_W(x)-x has strictly negative slope, so its unique zero lies between a and b. If xi_W<b_(v_0), start with x_n=xi_W and apply the inverse branches backwards; the image identities put each x_j in its ACTUAL I_(v_j), with x_0=x_n. This is a legal periodic orbit with precisely W's itinerary. Conversely any such orbit must solve f_W(x)=x and hence equal xi_W. Thus right-endpoint equality is the only excluded case; an included left endpoint is legal.
This criterion also checks every intermediate digit. On closures, if one phase lies on a boundary, every next phase lies on the corresponding left boundary or every next phase on the corresponding right boundary. Indeed J_v maps the interior of a target interval into the interior of its source interval; positive slope excludes switching left and right endpoints. Cycling propagates the assertion through the word. Consequently an excluded word has every phase at an excluded right endpoint, and a legal boundary word has every phase at an included left endpoint. No endpoint is deleted from X to force a coding claim.
A realized word W is primitive exactly when its least word repetition length is n. One direction follows from the unique actual itinerary of a shorter point cycle. Conversely if W=U^r, T^(length U)(xi_W) has the same W itinerary and is another fixed point of its inverse word; uniqueness makes it xi_W. Thus it has the shorter period. Cyclic rotations give phases of the same source core; distinct primitive cyclic words give distinct cores. Together with §4 this is a complete positive-packet description without IR, not a purported conjugacy for all infinite graph paths.

### 5.2 What IR supplies

IR actually makes EVERY finite closed word interior-realized. If a closure fixed point were a left or right boundary point, the boundary propagation just proved would hold along the entire finite word. Extract a simple directed cycle from that closed walk. Its boundary coordinates would give a boundary fixed point of its own inverse word, contradicting IR. Thus no finite closed word has a boundary exception under IR. This argument uses only finite walks, even when the graph is countable.
Call an SCC cyclic if it contains a finite directed cycle. An SCC with two distinct vertices has an edge v->w with v!=w inside it. Append a shortest path from w back to v; that path has no repeated vertex and first reaches v at its end, giving a simple cycle of length at least two. By IR this gives a least-period q>=2 orbit. Its clock product is a product of q integers >=2 and therefore composite. Hence prime-only support forbids every such SCC.
If a cyclic SCC is a singleton, its cycle must be a self-loop. By IR that loop has one actual fixed point, with primitive log d_v, which is prime-log exactly when d_v is an ordinary prime. Conversely, if all cyclic SCCs are such singleton self-loops with prime digits, every finite closed word stays in one of them: mutually reachable vertices of a closed word lie in one SCC. It is a repetition of that self-loop, not a longer primitive. No nonperiodic or infinite escaping history supplies another positive packet by §4.3.
Therefore, UNDER IR, prime-only support is equivalent to: EVERY cyclic SCC is a singleton self-loop whose digit is prime. Subject to this condition, the full positive ledger is nonempty iff the cyclic-vertex set is nonempty, and has at most one packet per prime iff the digit map on those vertices is injective. If there are no cyclic vertices, support and uniqueness hold vacuously but nonemptiness fails. All-prime coverage additionally requires that digit map be onto the ordinary primes, hence a bijection when uniqueness holds. This is a condition on supplied frozen data, not permission to build the grammar from a prime table.
Transient composite digits are not ruled out; they affect incoming clocks but are not additional closed packets. Outside IR the exact test in §5.1 remains valid, but this graph-only equivalence is not asserted. IR is sufficient for the stated grammar rule, not claimed necessary for any individual candidate's prime-only ledger.

## 6. Three full controls

### 6.1 A: full partial doubling with terminals

Owner A is X=[-1,1), D=[-1/2,1/2), T=2x, with terminal E=[-1,-1/2) union [1/2,1). Its own actual global inverse from X into D is J(y)=y/2; for every Borel B subset X, mu(JB)=mu(B)/2. The all-point version is 1/2 and clock log 2. Every depth-m predecessor is exactly y/2^m, and D_m=[-2^(-m),2^(-m)) with T^m x=2^m x.
The only periodic or eventually periodic point is 0, fixed with source isotropy Z, entire H=log 2 Z and trivial extension isotropy. Every x!=0 terminates: expansion of its nonzero absolute value eventually leaves D. Its unique terminal t belongs to E and its complete source packet is {t/2^m:m>=0}. This includes asymmetric endpoints exactly as frozen: -1/2 is active and maps to -1, while +1/2 is terminal.
The complete groupoid is {(2^(-l)w,l,w):l in Z, w and 2^(-l)w in X}; legal witnesses follow by repeated actual inverse. Its clock is l log 2, so K_c=K_ell=their intersection=units. A terminal packet phase at (t/2^m,h) is h-m log 2 in R. At 0 the phase is h modulo log 2. The full ledger has one log 2 primitive packet and its repetitions k log 2; no longer least source cycle exists.
The active vertex has its self-loop and exits to the two terminals, which have no outgoing edges. Its fixed point 0 is interior, so IR holds. A meets nonempty prime-only uniqueness as an EXTERNAL CONTROL, not an endogenous source or all-prime coverage.

### 6.2 B: alternating components, composite primitive

Owner B is the frozen two-component X and two active branches. Write x=3e+t with e in {0,1}, t in [-1,1). Then T(e,t)=(1-e,2t) exactly when t in [-1/2,1/2). Its actual inverse of every target is (e,t)->(1-e,t/2), and its OWN IMAGE identity on every Borel set is division by 2. Thus its all-point clock is log 2, with every depth-m predecessor (e+m mod 2,t/2^m).
The two centers (0,0) and (1,0), corresponding to real points 0 and 3, form one least two-cycle; neither is fixed. All other points terminate by expansion of abs(t). Each terminal (e,t), t in E from A's displayed interval set, owns exactly {(e+m mod 2,t/2^m):m>=0}; this formula follows directly from B's inverse, not a transfer of A's clock or theorem.
The complete groupoid consists of (z,l,w) with t_z=2^(-l)t_w, e_z=e_w-l mod 2, and both endpoints in B's full X. Its clock is l log 2; all three kernels are units, and all extension isotropy is trivial. Off-center source isotropy and H are zero. On the center core they are 2 Z and log 4 Z. The core phase is [h+e log 2] modulo log 4; at depth m above a terminal it is h-m log 2 in R. Thus one log 4 packet is PRIMITIVE, with repetitions k log 4, not a repetition of a nonexistent log 2 packet.
The only simple graph cycle alternates the active cells. Its two fixed-point phases are 0 and 3, interior to their cells (the return affine maps are 4x and 4x-9). Hence IR holds. The prime-only gate fails through an actual interior composite primitive, not a missing endpoint.

### 6.3 C: full half-open doubling and all periods

Owner C has X=D=[0,1), lower and upper branches 2x and 2x-1. Its actual inverses on EVERY y in X are J_0(y)=y/2 and J_1(y)=(y+1)/2. Each owns Borel IMAGE factor 1/2 at all points, so its clock is log 2; the union of both inverse images has measure mu(B), a different identity. Every depth-m incoming set is exactly {(y+k)/2^m:0<=k<2^m}. There are no terminals.
Induction gives T^m x={2^m x}. Consequently the complete source groupoid and kernels are

`G={(z,m-n,w): m,n>=0 and 2^m z-2^n w is an integer}, c=(m-n) log 2;`
`K_c=K_ell=their intersection={(z,0,w): z-w is dyadic rational}.`

Here z,w always lie in [0,1). Equal fractional parts are precisely the integer test, giving both necessity and sufficiency. Equal lag witnesses give the same triple. The kernels are not units: 0 and 1/2, for example, merge after one step. Every extension isotropy group is nevertheless trivial.
For EACH n>=1 the complete fixed set of T^n is

`Fix(T^n)={k/(2^n-1): 0<=k<2^n-1}.`

The exact-period-n subset removes Fix(T^r) for every proper divisor r of n; a period dividing n is the only possibility for a T^n-fixed point. If E_n denotes its size, E_1=1 and E_n=(2^n-1)-sum_(r|n,r<n) E_r, so the exact number of primitive period-n packets is E_n/n. This is an all-n integer identity, not a census. For every n>=2, x=1/(2^n-1) has least period n, since (2^r-1)x lies strictly between 0 and 1 for 0<r<n. The unique fixed point is 0. Each exact-n packet has source isotropy n Z, ENTIRE H=n log 2 Z, all phases modulo n log 2, primitive n log 2 and repetitions k n log 2.
Every rational x is eventually periodic. In lowest terms write its denominator as 2^s b with b odd. After exactly s steps it has odd denominator b; multiplication by 2 permutes residues modulo b. For b>1 its least eventual period is the least q>=1 with 2^q=1 modulo b; for b=1 it reaches 0, of period 1. Conversely eventual equality of two iterates forces (2^m-2^n)x integer and hence x rational. Thus the irrational points are exactly the non-eventually-periodic set; none is discarded.
For each periodic core gamma, its entire source packet is union_(m>=0){(p+k)/2^m:p in gamma,0<=k<2^m}; distinct cores remain distinct. If T^a z=p_j=T^j p_0 on a least-n core, set k_z=a-j. The complete height phase is [h-k_z log 2] modulo n log 2, independent of the landing choice. For each irrational reference w its full packet consists of all z with 2^m z-2^n w integer for some m,n. The unique reference arrow is g_z=(z,k_z,w), FROM w TO z, with clock k_z log 2; therefore h-k_z log 2 is the unrestricted real phase. Its source isotropy and H are zero. These formulas supply all incoming, packets and phases of the full source.
For coding, the actual binary itinerary is the unique expansion not eventually all 1. Indeed x=sum_(j>=0) epsilon_j/2^(j+1), obtained by iterating the branch equation with a remainder bounded by 2^(-m). Conversely a sequence not eventually all 1 has every shifted binary value in [0,1), and the half-open branch rule reads its digits. An eventually-all-1 tail has shifted value 1 and is not an actual itinerary. Thus dyadic endpoints use the eventually-0 expansion; the alternative ending in all 1 is excluded, not a second orbit. The all-1 fixed word has closure point 1 outside X; the all-0 word gives the legal left endpoint 0.
The actual graph has both edges from each of its two vertices. IR FAILS: its two self-loop fixed points are 0 (included left boundary) and 1 (excluded right boundary), neither interior. The word 01 does realize the least two-cycle {1/3,2/3}, with primitive log 4, while 00 only repeats the fixed point. Thus C's prime-only gate fails by an actual composite primitive independently of the unavailable IR graph criterion. Its many higher periods are fully retained by the all-n description.

## 7. Controls, adverse findings and gate assessment

Geometry/ownership controls compare single-branch IMAGE with total preimages, preserve complete real carriers and terminals, distinguish source isotropy from extension isotropy, and retain all equal-time kernels and phases. Coding controls distinguish actual itineraries, word repetitions and excluded endpoint codes. A and B satisfy IR; C explicitly fails it, so IR is not smuggled in from adjacency. There is no parent arithmetic source for an arithmetic-label shuffle. Strong naturalness and PROVES_TOO_MUCH remain OPEN for any future claimed endogenous prime grammar.

| Gate | Exact status | Boundary |
| --- | --- | --- |
| T0 | CONDITIONAL FULL OWNER / IMAGE ESTABLISHED | Frozen geometry and graph assumed; all-point version prescribed |
| T1 | OWN GEOMETRIC CLOCK COMPONENT ESTABLISHED; NO ARITHMETIC T1 PASS | No endogenous prime grammar supplied; component result only |
| T2 | ENDPOINT REALIZATION AND IR GRAMMAR CRITERION ESTABLISHED | Graph equivalence requires IR; A necessary-ledger only, B/C prime-only STOP |
| T3 | NOT AUDITED | No same-owner operator/trace |
| Classical A0–A2 / formal Route | NOT APPLICABLE / UNASSIGNED | No formal evaluation |
| Route B | NOT INVOKED | Not used as a rescue |

## 8. Conclusion and decision

STOP this bounded audit after recording the exact filter; no arithmetic candidate is admitted or advanced. B and C fail prime-only support, while A supplies only an external necessary-ledger control. A future FORK would need a separately frozen prime-symbolic grammar and independently verified realization data, not a chosen list of prime slopes or removal of unwanted periodic points. No new candidate or additional round is created. The one-object ledger remains intact for the conditional construction and separately for each control.

## Reproducibility / evidence index and limits

The [card](candidate-card.md), [claim ledger](claim-ledger.md), this full proof and [README](README.md) contain the exact inputs and results. Definitions, integer identities and affine substitutions replace precision/cutoff choices. No scientific numerical run, scientific code, orbit census, literature search, external API, Git, PDF, publication or other candidate computation was performed. No theorem is inferred from a finite check.
Read/check methods: `sed -n '1,180p' papers/418-integer-slope-realization/candidate-card.md`, `wc -l`, `sha256sum`; `apply_patch` writes only the three authorized author surfaces. Full EOF self-read, frozen-prefix hash, local-link and first-20-line Candidate ID/identical Outcome checks accompany handoff. These mechanical checks certify artifact consistency, not mathematics. Root owns card append and CP2/CP3 integration, not pre-certified here.
Limits: IR is conditional, supplied digits may have no endogenous arithmetic origin, generic infinite coding is not asserted, quotient-manifold/suspension geometry is not constructed, and no novelty or analytic operator result is claimed. Terminal steps are never given an artificial zero clock.

## AI assistance and integrity disclosure

Root `/root` proposed the audit and owns freeze/release/integration. Author `/root/batch_clock_scope_review` supplied the definition scout, read the clarified 92-line frozen card through EOF, derived the general proof and A/B controls, integrated C and drafted/self-checked only these three surfaces. Current scientific inputs were that card and author derivations; repository/template and ARS instructions were read or retained. No reviewer/raw/peer, sibling or old research manuscript was read.
Author aid `/root/batch_clock_scope_review/ccg_cotangent_probe` was assigned only full control C. Its actual access receipt reports only `sed` of the full 92-line card and `sha256sum` matching the above digest; no other files, writes, scientific code, network or further agents. Its returned formulas were checked against §6.3; this is author assistance, not an independent review. Shared historical context is retained. The work is NOT_CALIBRATED, not blind, cross-model, human or external peer review.
AI agents supplied mathematical derivation, drafting, checking and AI-assisted internal review; no human or external verification is certified. Informal composite-cycle expectations influenced design before freeze, as the card records, so this is not sealed preregistration. ARS supplied bounded claim/evidence and disclosure discipline, not a full publication pipeline; `criteria_binding_unavailable`, no venue or submission-readiness claim.
Data availability: exact definitions and proofs are in this package; no dataset or hidden numerical outputs. Ethics: no human/animal subjects or personal data. Contributions: named AI task receipts above do not establish human authorship or CRediT attribution. Funding and conflicts: no human declarations supplied; UNKNOWN, not certified absent.
