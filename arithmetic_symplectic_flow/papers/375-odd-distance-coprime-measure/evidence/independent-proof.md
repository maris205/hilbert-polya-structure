# 375 — Independent hard-history and IMAGE-admission derivation

Candidate: **ANG-20260922-ODC01**.
Result: **full stationary source law exists; strictly positive IMAGE admission fails — STOP / FORK**.
The failure is intrinsic to positivity for this map and measure, not merely a removable null-point version defect.
MAIN's real clock, its kernel, extension, H and physical packets are **NOT DEFINED**, not zero.

## 1. Input and actual scope

After root read the 76-line scope report and explicitly released mathematics, I reread the entire 88-line
candidate-card.md through EOF and measured SHA-256
`e7e4fa21a66ebd823d391720731a1448867f6d488dfe4399755979621d0fa149`.
That original card was the sole scientific file read; no manuscript, peer/scout proof, outcome or old proof
was accessed. The scope report remains unchanged. Applicable ARS instructions and broad history are retained.
This is inherited-model/shared-history internal derivation, **NOT_CALIBRATED**, not blind or external peer review.
The card already disclosed the author's expectations; agreement cannot establish independent errors.
No auxiliary, external source, scientific numerical experiment or model change was used. Only this file is written.

## 2. Full source, inverse domains and actual source ledger

Write E(x)={x_(2j):j>=0} and O(x)={x_(2j+1):j>=0}. Membership in X means exactly that
every element of E(x) is coprime to every element of O(x); both sets may be infinite.
The odd-distance pair conditions are clopen coordinate conditions, so X is closed and Borel in A^N_0.
It is nonempty, metrizable and second-countable. Its first-coordinate projection is onto A, using
(a,a+1)^infinity, hence X is noncompact. No finite-alphabet restriction has been imposed.
T is a continuous self-map: shifting preserves odd differences between retained coordinates.
Its predecessors are exactly I_a(y)=ay for a>=2 with y in
E_a=intersection_(j>=0){y:gcd(a,y_(2j))=1}. These are closed Borel domains.
I_a is a homeomorphism from E_a onto X intersect {x_0=a}, with inverse T on that image.
Every y has infinitely many predecessors: a=(y_1)^k is legal for every k>=1. Thus T is onto, with no terminals.

Closed inverse domains need not be open. At y=(3,5)^infinity, y belongs to E_2; replacing a sufficiently
remote even coordinate by 2 stays in X but leaves E_2, without changing any prescribed finite prefix.
Thus E_2 is not a neighborhood of y. In particular local-homeomorphism/etale ownership is not inferred.

For a finite word u of length m, I_u(y)=uy is legal exactly when u itself obeys all its odd-distance
gcd tests and gcd(u_i,y_j)=1 whenever m+j−i is odd. This lists ALL m-step predecessors and domains.
The whole source orbit of x is {u T^n x : n>=0, u finite, u T^n x in X}; no illegal prefix is included.
The actual lag triples form a countable-fiber Borel groupoid: equality of iterates is Borel, and the
displayed prefix domains enumerate every arrow. Equal triples, not different written witnesses, are identified.
The full lag kernel is {(z,0,y):T^m z=T^m y for some m>=0}; it contains nonidentity merging histories.

For a displayed periodic word w of length n, w^infinity belongs to X iff n is even and
gcd(w_i,w_j)=1 for every pair of opposite-parity positions in that word.
Necessity for odd n follows from repeating the same symbol at the odd distance n; for even n all
odd-separated positions reduce to opposite parities modulo n, proving both directions of the criterion.
Reducing a legal word to its least period gives an even q. Its literal core is its q cyclic rotations.
All legal eventually periodic ancestors of that core have ENTIRE source isotropy qZ, not just the
literal periodic points. Noneventually-periodic states have zero isotropy, by the equality-of-tails criterion.
Different primitive cyclic words cannot merge unless they are cyclic rotations of the same primitive word.
These are source classifications only; no physical times or clock-dependent kernels follow from them.

## 3. Normalization, stationarity, support and every atom

The map S->code(S) is a bijection from nonempty finite subsets of A to positive integers, by binary expansion.
Therefore sum_S 2^(−code(S))=1. The prescribed normalizer satisfies 0<B<=1, since V is a subset
of all ordered pairs and contains ({2},{3}). Every component is a probability supported on X.
Countable mixing defines a Borel probability on the full X; labels are not source coordinates.
T_*nu_(S,U)=nu_(U,S), and w_(S,U)=w_(U,S), so T_*mu=mu.

Every nonempty relative prefix cylinder has positive mass: take its observed even and odd value sets,
filling an empty set from an actual point of that cylinder. These finite sets are cross-coprime and
define a component assigning positive probability to that cylinder. Hence mu has full topological support.
For any y in E_a the same construction uses even values all coprime to a, so
mu(E_a intersect C_N(y))>0 for EVERY N, including N=0, even at unbounded histories.
Almost every sampled history uses a finite pair of alphabets, but unbounded histories remain in X.

A component has a singleton atom only if |S|=|U|=1. Otherwise infinitely many specified coordinates
each have probability at most 1/2, and any singleton has mass zero. Thus the COMPLETE atom list is
x=(s,u)^infinity, gcd(s,u)=1, with mass

\[
\mu\{(s,u)^\infty\}=\frac{2^{-2^{s-2}-2^{u-2}}}{B}.
\]

All other singletons have zero mass. The atomic part has positive but not total mass: components with
at least one larger alphabet have positive weight and are nonatomic. Every source orbit is countable.
A period-two source class has precisely its two alternating atoms and their summed mass; every other
source class has zero mass. These statements retain, rather than discard, every null incoming history.

## 4. Exact restricted ratios and intrinsic MAIN failure

Put e_N=ceil(N/2), o_N=floor(N/2), and
p_N(S,U;y)=1_{even prefix in S, odd prefix in U}|S|^(−e_N)|U|^(−o_N).
Under nu_(S,U), the event E_a has probability one when a is coprime to every s in S, and zero otherwise:
in the latter case avoiding a forbidden symbol at infinitely many independent even positions has probability zero.
Consequently the prescribed restricted-cylinder denominator and numerator are exactly

\[
D_N=\sum_{(S,U)\in V}w_{S,U}\,1_{\gcd(a,S)=1}p_N(S,U;y),\qquad
N_N=\sum_{(S,U)\in V}w_{S,U}\frac{1_{a\in U}}{|U|}p_N(S,U;y).
\]

Here gcd(a,S)=1 means coprimality with every member of S. D_N>0 and 0<=N_N/D_N<=1.
More generally, for EVERY Borel D subset E_a, direct conditioning on the first coordinate and swapping
the component labels gives the exact identity

\[
\mu(I_aD)=\sum_{(S,U)\in V}w_{S,U}\frac{1_{a\in U}}{|U|}\nu_{S,U}(D)\le\mu(D).
\]

There is an ordinary nonnegative IMAGE density, not a singularity obstruction to all densities.
An explicit version is 1_{a in U}/|U| on the disjoint typical component sets F_(S,U) defined in §6,
and zero on their null complement. The empirical-law justification there proves this every-Borel assertion.
It is strict positivity on the full actual inverse domain that fails.

Take y=(3,2)^infinity and x=(2,3)^infinity. Both have mass alpha=1/(8B)>0.
Both a=2 and a=4 are legal at y. I_2 y=x has mass alpha; z=I_4 y=(4,3,2,3,...) has mass zero.
The restricted cylinders decrease to {y}, and their injective prefix images decrease to {I_a y}.
Continuity from above therefore gives the actual frozen limits j_2(y)=1 and j_4(y)=0.
At the other source phase x, the legal closing prefix 3 similarly has j_3(x)=1.
The singleton Borel tests read alpha=1·alpha for the closing branch and 0=j_4(y)alpha for prefix 4.
Thus ANY strictly positive density satisfying the Borel IMAGE law is impossible, independently of its version.
More generally an alternating atom has derivative one at its closing prefix and zero at every other legal prefix.
The test class has source isotropy 2Z at x,y,z and all its legal ancestors; z has no literal return.
Its total mu mass is 2alpha. None of this defines MAIN's H: global clock admission has already failed.
No infinite logarithm, selected recurrent subsource or a.e. repair is substituted for the frozen real clock.
MAIN c, clock kernel/intersection, extension isotropy, H, physical phases and packets remain NOT DEFINED.

## 5. FIXED-TWO and ARITHMETIC-OFF own controls

**FIXED-TWO.** The only states are x=(23)^infinity and y=(32)^infinity, each mass 1/2.
T exchanges them; I_2 has domain {y}, I_3 domain {x}, and all other prefix domains are empty.
Both singleton IMAGE ratios and all restricted-cylinder ratios equal one, proving every-Borel/all-point admission.
The real clock is identically zero on the full retained two-state action groupoid.
Source and extension isotropy are 2Z; H=0. The full clock kernel is the whole groupoid;
lag kernel and its intersection with the clock kernel are just identity arrows.
Every integer-labelled incoming arrow is retained with predecessor determined by parity.
Both source phases give a single free physical line with phase h, not a positive period-two physical packet.
Prefix 4 is not legal in this changed two-state owner; no zero-mass residual source is silently retained.

**ARITHMETIC-OFF.** On full A^N_0, rho(a)=1/(a−1)−1/a sums to one and gives a nonatomic,
full-support stationary product probability. Every prefix I_a has the whole carrier as domain and
EVERY-Borel IMAGE rho(a); every cylinder ratio is exactly rho(a)>0, including null periodic paths.
Let Q_m(z)=product_(i<m) z_i(z_i−1). The actual history clock and IMAGE are
c(z,m−n,y)=log(Q_m(z)/Q_n(y)) and J=Q_n(y)/Q_m(z).
Product laws prove all history IMAGE identities; common-tail cancellation proves descent and composition.
Full ker(c) tests equality of Q products, ker(lag) tests m=n, and the intersection tests both.
These kernels need not coincide: prefixes (4) and (2,3) have equal Q=12 and unequal length;
one-letter prefixes 2 and 3 have equal length but different Q; (2,3) and (3,2) give a nonidentity intersection arrow.
All incoming states are arbitrary finite prefixes of shifted tails. Eventual least word period q gives
ENTIRE source isotropy qZ, H=tau Z for tau=sum log[a_i(a_i−1)]>0, and trivial extension isotropy.
Noneventually-periodic histories have zero source isotropy and H. Primitive cyclic A-words classify
all positive packets, one per necklace, with repetitions k tau and no merging of distinct necklaces.
For T^m z=T^j o at a periodic reference o, phase is h−A_m(z)+A_j(o) modulo tau; free orbits use the
corresponding real anchor phase. These are orbit-set statements, not quotient-manifold claims.
For the named alternating class, q=2 and tau=log12; prefix 4 is an ancestor, with its own j_4=1/12.
Constant 3 is itself a primitive log6 packet in this control. These control times are not MAIN times.

## 6. DROP-SINGLETONS: full support and nonatomicity do not repair admission

Let V_+ restrict both alphabet sizes to at least two and let B_+ be its normalizer.
Then 0<B_+<=1, witnessed by S_*={3,5}, U_*={2,4}; symmetric weights again give shift invariance.
Every component is nonatomic, hence their countable mixture mu_+ is nonatomic on the same full X.
To extend a finite legal cylinder, enlarge its nonempty finite even set S until |S|>=2 by choosing
new integers 1+k product(U), then enlarge U with integers 1+k product(S), avoiding already chosen values.
Cross-coprimality is preserved throughout. For a restricted E_a cylinder use product(U union {a})
when enlarging S. Thus mu_+ has full support and EVERY legal restricted-cylinder denominator is positive.
All source domains, incoming histories, lag kernel and even-period source-isotropy criteria in §2 remain unchanged.

For any finite pair (S,U), define F_(S,U) by all even coordinates lying in S, all odd in U,
and the two empirical laws being uniform on these respective sets. These are pairwise disjoint Borel sets.
Under nu_(S,U) they have probability one; under every other component they have probability zero.
An elementary justification needs no external ergodic theorem: for each symbol indicator, Chebyshev at
sample sizes n^2 gives summable deviation probabilities. The union bound on the remaining tails yields
almost-sure convergence along squares; the intervening counts differ by at most 2n+1 and give full convergence.
Apply this to the finitely many symbols in each component and both parity sequences.
This also supplies the full-measure typical sets and explicit nonnegative density asserted in §4.

The frozen test set F=F_(S_*,U_*) has mass w'_(S_*,U_*)=2^(−15)/B_+>0, since the codes are 10 and 5.
It is contained in E_7. In I_7 F the even empirical law is uniform on {2,4}, the odd law on {3,5},
but the first even coordinate is 7. Only the swapped component could have those empirical laws,
and it assigns zero probability to that initial 7. Hence mu_+(I_7 F)=0.
No strictly positive Borel IMAGE density can integrate to zero on this positive-measure domain set.
The obstruction is therefore intrinsic to this control's measured owner, not caused by singleton atoms.

Its prescribed version fails directly as well. For y in F, eventually both 2 and 4 occur in its odd prefix.
A numerator component allowing prefix 7 must then have at least three odd-alphabet symbols, while every
even alphabet has at least two. Thus N_N<=2^(−N)(2/3)^floor(N/2), whereas
D_N>=w'_(S_*,U_*)2^(−N), using the legal base component. The restricted ratio tends to zero at EVERY y in F.
The component identity in §4 still proves every-Borel nonnegative IMAGE densities for this own law;
it does not prove the required strict positivity. Its real clock and all clock-dependent fields are NOT DEFINED.

## 7. Bounded decision and strongest positive alternative

The hard nonlocal source is real, its complete law is stationary and full-support, and it has legal even
source cycles. These positive results do not guarantee positive mass for every legal predecessor image.
MAIN already fails the stronger singleton Borel test, not merely a prescribed-limit test; removing atoms
in the separate control still leaves a positive-measure Borel obstruction. Changing latent labels into
coordinates, pruning legal histories or reweighting the law would define a different owner.
No general impossibility for hard nonlocal sources or ordinary nonnegative densities is proved.
All frozen source/control obligations are resolved without a physical-period census after MAIN's failure.
Strong naturalness remains OPEN; T3 NOT AUDITED; classical coordinates NOT APPLICABLE;
formal UNASSIGNED and Route B NOT INVOKED. No missing obligation blocks this scoped STOP / FORK.
Manuscript CP2/CP3 remains a later task; no manuscript was used to generate this report.
