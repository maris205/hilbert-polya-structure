# Factor-history clocks: no continuous IMAGE version and measurable period freedom

**Paper ID:** 384-factor-clock-version-gate.  
**Candidate:** ANG-AUDIT-20260922-FVG01; batch FULL-TRANSPORT-20260922-G, round 5/5.  
**Date:** 2026-09-22.  
Outcome: `CONTINUOUS VERSION STOP; MEASURABLE IMAGE AND VERSION FREEDOM ESTABLISHED`
**Route:** classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED; T3 NOT AUDITED.

## Abstract

This audit derives the full measured factor-history owner from the two frozen cards, rather than inheriting an IMAGE theorem. The resulting every-Borel IMAGE law has a finite positive Borel version at every legal tail. No such version can be continuous on the inverse domain E_2: every neighborhood of the alternating tail contains two positive-measure families of component-typical histories with uniformly separated densities. Nevertheless, changing the normalized version on the entire null eventual-23 class preserves all measured transport and yields a family of full retained-lag clocks. Its primitive 23 time varies strictly with the version. Each of the three precommitted parameters has a wrong prime primitive, with exact rational bounds. All incoming histories, phases, isotropy, kernels and other source orbits are retained.

## 1. Frozen definitions and scope of the audit

The original 55 lines of the [384 card](candidate-card.md) have SHA-256 e97733825ca454eb8a1d1fa51203001d8a5c4854aebb45cc3862ab4d0530f0b2. The sole conditional-source input is the complete original 70-line definition prefix of the [380 card](../380-factor-allocation-history/candidate-card.md), SHA-256 b5fda99de6457de81fcc6338c4e6ba9102b92402c815e3a8902e8365f5ba753b; later appended outcomes are outside this input hash and were not read. No 380 main paper, result, raw derivation or peer report is used. Root released mathematics after accepting CP1; the proofs below discharge the needed source-law dependency themselves.

The source is all
\[
X=\{x\in\{2,3,\ldots\}^{\mathbb N_0}:\gcd(x_i,x_j)=1\text{ whenever }j-i\text{ is odd}\},
\]
with product-subspace topology, its full Borel sigma algebra, and left shift T. Every actual inverse is I_a(y)=ay on E_a={y:gcd(a,y_(2j))=1 for all j>=0}. The lineage under audit is divisor-based hard admission -> complete factor-allocation probability -> identifiability of its full-point clock, not a new prime-flow candidate.

| Item | Frozen owner and limit |
| --- | --- |
| Arithmetic/source | All odd-distance coprime histories; every legal inverse and null history |
| Probability | The fair independent irreducible-factor allocation mixture specified below |
| BASE version | j_a(y)=rho(a)/Z(y), with Z summed over all legal predecessors |
| Modified versions | Entire eventual-23 class O; t=1/2,1,2 frozen separately, with the displayed full family |
| Clock owner | The exact version, actual lag triples and all X times R; no borrowed roof |
| Physical action | Height translation on the orbit SET only; no manifold or quotient-topology assertion |
| Limits | Naturalness OPEN; no target fitting, canonical-version promotion, operator or T3 audit |

Allocation labels remain integration variables. None is added to the source. The controls defined in 380's card are not this audit's three controls and are not evaluated or credited here.

## 2. Independent construction of the measured source

Let P be the integers >=2 irreducible under multiplication, determined by ordinary divisibility. Elementary integer factorization supplies each integer's finite irreducible-factor set; P is countably infinite. Give theta in {0,1}^P the fair product law beta. The two constant allocations have probability zero. For each other allocation let S_i(theta) comprise the integers whose factors all have color i, and put
\[
\rho(a)=\frac1{a(a-1)},\qquad Z_i(\theta)=\sum_{a\in S_i(\theta)}\rho(a),\qquad
q_i(\theta,a)=\frac{\rho(a)\mathbf1_{a\in S_i(\theta)}}{Z_i(\theta)}.
\]
The component nu_theta has independent even q_0 and odd q_1 coordinates; mu=int nu_theta d beta. Every nonconstant allocation, including prior-null ones, is allowed in this recipe; exclusion of the two degenerate integration labels removes no point of X.

**Proposition 1 (probability, support, nonatoms).** This recipe is measurable, defines a shift-invariant probability on the full X, has full support, and is nonatomic.

**Proof.** The sum of rho is one by telescoping. Each color contains an irreducible and all its powers, so 0<Z_i<1 and its normalized alphabet contains at least two positive-probability symbols. Membership of a in S_i depends on finitely many allocation bits. The series defining Z_i has uniform tail bounded by sum_(a>N)rho(a)=1/N, hence is measurable (indeed continuous on the allocation product). Component cylinder probabilities are finite products of measurable q_i. The cylinder probability extensions and a monotone-class argument make theta->nu_theta(D) measurable for every Borel D, so the integral is a probability.

Opposite-color integers have disjoint factors, making each component supported on X. Shifting swaps colors: T_*nu_theta=nu_(1-theta). The fair prior is invariant under complementation, proving stationarity. For any nonempty allowed cylinder, the factors of its even and odd symbols are disjoint. Assign these finitely many factors the respective colors. This event has positive prior mass; each of its nondegenerate components gives the cylinder positive probability. Thus mu has full support without deleting unbounded or null histories.

For a fixed nonconstant theta, each parity distribution has two positive masses and therefore maximum single-symbol probability at most some r_theta<1. Every specified length-N cylinder then has probability at most r_theta^N. Hence nu_theta has no point atoms, and mu({x})=int 0 d beta=0 for every x. Any Borel atom in this countable-coordinate space would select a unique full-mass coordinate cell successively and thus a singleton of the same mass. Therefore mu is nonatomic. QED.

For completeness, X is closed since every forbidden pair is an open condition; T is a continuous self-map. It is onto because y_1 is a legal predecessor of every y. Each E_a is closed Borel, and I_a:E_a->[a] is a homeomorphism with inverse T. These are all actual inverses, but E_a is not assumed open. Every finite inverse is I_u(t)=ut on D_u={t:ut belongs to X}; its domain requires all internal odd-distance prefix pairs and all odd-distance prefix/tail pairs to be coprime.

## 3. Full-point positivity and every-Borel IMAGE, proved here

For every y in X let L(y)={a:y in E_a}, Z(y)=sum_(a in L(y))rho(a). The powers of y_1 all belong to L(y), so it is infinite. Thus 0<Z(y)<=1 and the declared
\[
j_a(y)=\rho(a)/Z(y),\qquad y\in E_a,
\tag{1}
\]
is Borel, finite and strictly between zero and one. Its sum over every legal a is one. Borelness follows from the closed E_a and a countable sum; the least legal predecessor a_0(y) is also Borel, since {a_0=a}=E_a minus the union of E_b for b<a.

Let R be the Borel set of histories in which every irreducible p occurs as the letter p infinitely often in one of the two parities. A letter cannot occur in both parities because of the hard gcd rule. Under any nonconstant nu_theta, every irreducible has positive probability at its assigned parity, and the probability of avoiding it after any given site is zero. A countable intersection proves nu_theta(R)=1. On R the observed parity defines a Borel recovered allocation theta_y, with theta_y=theta almost surely in that component. Every factor of an even symbol has color zero; every zero-color factor is observed at even sites. Consequently
\[
L(y)=S_1(\theta_y),\quad Z(y)=Z_1(\theta_y)\qquad(y\in R).
\tag{2}
\]
This is a function of the existing history, not an enlarged state space; X outside R is fully retained.

**Proposition 2 (every-Borel IMAGE).** For every a and every Borel D contained in E_a,
\[
\mu(I_aD)=\int_D j_a(y)\,d\mu(y).
\tag{3}
\]

**Proof.** Independence of the first coordinate gives nu_theta(I_aD)=q_0(theta,a)nu_(1-theta)(D). Complementing the fair allocation in the integral yields
\[
\mu(I_aD)=\int
\frac{\rho(a)\mathbf1_{a\in S_1(\eta)}}{Z_1(\eta)}\nu_\eta(D)\,d\beta(\eta).
\]
For nu_eta-almost every y, (2) holds, and membership in E_a is equivalent to a in S_1(eta). This integrand is exactly the integral of the full-point function (1) over D. Images are Borel because insertion is a homeomorphism onto [a]. The argument applies directly to every Borel D, not just cylinders. QED.

No assertion that mu uniquely determines (1) at null points follows from (3). Its all-point specification comes from the frozen card. Continuity is a separate question addressed next.

## 4. No continuous IMAGE version at the alternating tail

Put y_*=(3,2)^infinity and K=sum_(k>=1)rho(2^k). Let P_40 be the finite set of irreducibles at most 40, of cardinality r. Within the ORIGINAL prior use the finite-coordinate events
\[
Q_-=\{\theta(2)=1,\ \theta(p)=0\ (p\in P_{40}\setminus\{2\})\},
\quad
Q_+=\{\theta(2)=\theta(5)=1,\ \theta(p)=0\ (p\in P_{40}\setminus\{2,5\})\}.
\]
Each has mass 2^(-r)>0 and forces theta(3)=0. These are proof subsets of the unchanged prior; 40 is a tail-bound threshold, not a carrier cutoff or fitted parameter.

For C_n the prefix cylinder of y_*, define
B_n^sign=C_n intersect R intersect {theta_y in Q_sign}, for sign in {+,-}. These Borel sets lie in E_2, and
\[
\mu(B_n^\pm)=\int_{Q_\pm}
\left(\frac{\rho(3)}{Z_0(\theta)}\right)^{\lceil n/2\rceil}
\left(\frac{\rho(2)}{Z_1(\theta)}\right)^{\lfloor n/2\rfloor}d\beta(\theta)
\geq2^{-r}\rho(3)^{\lceil n/2\rceil}\rho(2)^{\lfloor n/2\rfloor}>0.
\]
Thus entire component-typical histories of both kinds occur with positive mu mass in every relevant neighborhood, not merely along two chosen null sequences.

On B_n^-, every legal integer other than a power of 2 exceeds 40; hence Z<=K+1/40. On B_n^+, all powers of 2 and also 5 are legal, so Z>=K+1/20. Therefore, uniformly in n,
\[
j_2|_{B_n^-}\geq H:=\frac{1/2}{K+1/40}>
L:=\frac{1/2}{K+1/20}\geq j_2|_{B_n^+},
\qquad H-L=\frac1{80(K+1/40)(K+1/20)}>0.
\tag{4}
\]

**Theorem 3 (continuous-version stop).** No finite strictly positive IMAGE version for I_2 is continuous on E_2, or even continuous at y_*.

**Proof.** Any such Borel version h satisfying (3) agrees with j_2 mu-almost everywhere on E_2, by uniqueness of densities. Remove that single null exceptional set from B_n^- and B_n^+; both remain nonempty. Choosing one point from each gives sequences converging to y_* in E_2, with h-values separated by the fixed positive gap in (4). Continuity would require h(y_*)>=H and h(y_*)<=L, a contradiction. QED.

Proposition 2 discharges the theorem's IMAGE dependency within this paper. A continuous representative necessarily has vanishing essential oscillation as its neighborhoods shrink; (4) violates this necessary condition. This is not merely a discontinuity of the chosen null value. Nor is it nonexistence of a measurable version; (1) already supplies one on EVERY legal point.

## 5. Null-class family: separate all-point versions with the same transport

Let O be the whole eventual-tail equivalence class of (23)^infinity. Explicitly it comprises every legal finite prefix followed by either alternating phase. It is a countable union of singletons, hence Borel, and mu(O)=0 by Proposition 1. Its class is saturated under every actual lag arrow and every legal insertion: y belongs to O if and only if any legal ay does. No point is removed.

For each fixed t>0 set r(y)=rho(a_0(y)), D_t(y)=Z(y)+(t-1)r(y), and define
\[
j^t_a(y)=
\begin{cases}
\rho(a)t^{\mathbf1_{a=a_0(y)}}/D_t(y),&y\in O\cap E_a,\\
j_a(y),&y\in E_a\setminus O.
\end{cases}
\tag{5}
\]
These are different frozen VERSION owners, not modifications to 380's card. BASE is t=1, DECREASE t=1/2 and INCREASE t=2; no t is chosen from target data.

**Proposition 4 (complete measurable admission).** Each family member has finite strictly positive Borel values, all-point sum one, every-Borel IMAGE and all finite-history transport.

**Proof.** The denominator in (5) is the sum of its positive numerators over all legal a and is finite. There are at least two legal a, so every j^t_a<1. All functions and O are Borel. Each j^t_a equals (1) outside the mu-null O, so its integral over every Borel D is the same as in (3), including D contained in O. For a legal word u and its entire domain D_u, successive application of this identity gives
\[
\mu(I_uD)=\int_D J^t_u(v)d\mu(v),\quad
J^t_u(v)=\prod_{i<|u|}j^t_{u_i}\bigl(T^{i+1}(uv)\bigr),\qquad D\subset D_u\text{ Borel}.
\tag{6}
\]
Induction uses the preceding branch's exact change-of-measure identity; no typical-tail restriction is introduced. The empty prefix has density one. QED.

All these versions fail the continuous requirement of Theorem 3. Their measurable transport and positivity nevertheless hold everywhere in the frozen sense. Normalization and every-Borel IMAGE alone cannot identify a unique full-point version.

## 6. Full actual-lag clocks, kernels, isotropy and incoming states

For each version define kappa_t(x)=-log j^t_(x_0)(Tx)>0 and A^t_m(x)=sum_(i<m)kappa_t(T^i x), with A^t_0=0. Retain
\[
G=\{(z,m-n,y):T^m z=T^n y,\ m,n\geq0\},\qquad
c_t(z,m-n,y)=A^t_m(z)-A^t_n(y).
\tag{7}
\]
Equal triples alone are identified. Padding both witnesses by the same nonnegative integer adds equal common-tail sums, proving descent. For multiplication, pad the two middle exponents to their maximum; their A-sums cancel. Thus c_t is additive, has zero unit value and reverses sign under inversion. Formula (6) gives the finite-prefix replacement IMAGE ratio exp(-c_t), on every Borel subset of each such branch.

All source incoming states are uT^n x with u any legal finite prefix. Every arrow has the form (uv,|u|-|w|,wv). Put W_t(u;v)=1/J^t_u(v). The ENTIRE kernels are
\[
\begin{aligned}
\ker c_t&=\{(uv,|u|-|w|,wv):W_t(u;v)=W_t(w;v)\},\\
\ker\ell&=\{(uv,0,wv):|u|=|w|\},\\
\ker c_t\cap\ker\ell&=\{(uv,0,wv):|u|=|w|,\ W_t(u;v)=W_t(w;v)\}.
\end{aligned}
\tag{8}
\]
These exact finite-product equalities include every legal representation and retain all replacement cancellations, not just isotropy. Witness padding leaves the tests unchanged. They assume no independence of logarithms.

Source isotropy is trivial for non-eventually periodic x, and exactly {(x,kd,x):k in Z} when its eventual tail has least period d: equality of distinct shifts is equivalent to eventual periodicity, and all differences are multiples of the least period. An admissible periodic word must have even least period, since an odd repetition would place a symbol at an odd distance from itself. For even d, admissibility is precisely coprimality of every even-position letter with every odd-position letter. Constants are forbidden; primitive necklaces are identified by cyclic rotation only.

Let L_t(w) be the sum of kappa_t over the least-period cycle w. It is strictly positive and independent of cyclic phase. On every incoming state of its source orbit, c_t(x,kd,x)=kL_t(w), because preperiod terms cancel. The extension keeps ALL (x,h) in X times R and arrows (y,h)->(z,h+c_t(z,l,y)). Its isotropy is trivial everywhere: source-isotropy values kL_t vanish only for k=0.

Height translation commutes with every extension arrow, so physical time [x,h]->[x,h+s] is well-defined on the orbit set. Its ENTIRE stabilizer is
\[
H_x=c_t(G_x^x)=
\begin{cases}L_t(w)\mathbb Z,&x\text{ eventually periodic with primitive }w,\\
\{0\},&x\text{ not eventually periodic}.
\end{cases}
\tag{9}
\]
Indeed equality of [x,h+s] and [x,h] requires an arrow with both endpoints x. For a whole source orbit, connecting arrows identify height offsets modulo exactly H_x; two choices differ by source isotropy. The corresponding entire part of the orbit set is therefore R/H_x as a set with translation action. This retains every incoming prefix, every source phase and every real height. A word w written r times gives lag rd and time rL_t(w), in the SAME packet with least positive time L_t(w). No smooth or separated quotient is inferred.

## 7. The full primitive 23 packet and the three fixed controls

Let
\[
U=\sum_{\substack{a\geq2\\3\nmid a}}\rho(a),\qquad
V=\sum_{\substack{a\geq2\\a\ {\rm odd}}}\rho(a),\qquad
\alpha=2U-1>0,\quad\beta_0=6V-1>0.
\]
At tail (3,2)^infinity the least legal predecessor is 2, with normalizer U; at tail (2,3)^infinity it is 3, with normalizer V. Both traversals receive the t factor. Therefore
\[
Q_t=(1+\alpha/t)(1+\beta_0/t),\qquad L_t(23)=\log Q_t.
\tag{10}
\]
The source least period is exactly 2. On the ENTIRE O, source isotropy is 2Z, extension isotropy is trivial, and H=L_t(23)Z. All legal incoming states and both source phases give one physical packet R/L_t(23)Z, not one packet per chart. Its r-fold traversal has time rL_t(23).

**Theorem 5 (version-dependent least time).** L_t(23) is strictly decreasing and continuous for t>0, tends to infinity as t tends to zero, and tends to zero as t tends to infinity.

**Proof.** Both alpha and beta_0 are positive because each legal alphabet contains more than its least symbol. Formula (10) gives
dL_t/dt=-alpha/[t(t+alpha)]-beta_0/[t(t+beta_0)]<0 and the displayed limits. QED.

This proves time nonidentifiability from the measured transport; no parameter realizing a target time is selected. The three PRECOMMITTED owners have the following exact results:

| Version | Q_t and full 23 stabilizer | Exact least-time location |
| --- | --- | --- |
| DECREASE, t=1/2 | Q=(4U-1)(12V-1); H=(log Q)Z | log 5<L<log 6 |
| BASE, t=1 | Q=12UV; H=(log Q)Z | log 2<L<log 3 |
| INCREASE, t=2 | Q=(2U+1)(6V+1)/4; H=(log Q)Z | 0<L<log 2 |

**Exact bounds for the table.** Write S=1-U=sum_(k>=1)1/[3k(3k-1)]. Its first three terms sum to 77/360, so U<283/360<4/5. For k>=5, the summand is less than 1/[9k(k-1)]; hence
S<1/6+1/30+1/72+1/132+1/36=329/1320<1/4, proving U>3/4.

Also V=sum_(k>=1)1/[2k(2k+1)]. For k>=4, compare below with 1/[4k(k+1)] and above with 1/[(2k-1)(2k+1)]. The two tails telescope to 1/16 and 1/14, giving
509/1680<V<131/420, and therefore 3/10<V<5/16. Thus for t=1/2,
26/5<Q<3088/525<6, with 26/5>5. For t=1, 27/10<Q<3, with 27/10>2. For t=2, 1<Q<299/160<2. All inequalities are strict positive-series bounds, not approximations or scientific numerical runs.

Each fixed control therefore has a wrong prime primitive in the frozen normalization. This is additional target evidence, not the reason measurable IMAGE is admitted or continuity is rejected.

## 8. Other orbits and the exact non-inference boundary

O is saturated, so every arrow outside it has both endpoints and every history along its witnesses outside O. Equations (5)--(8) are consequently IDENTICAL to BASE on all of G restricted to X minus O, not merely almost everywhere. Its inverse densities, clock values, kernels restricted there, extension arrows and physical times are unchanged. There are no arrows crossing between O and its complement.

For an admissible primitive necklace w other than 23, let E and F be its even- and odd-position letter sets, let d be its even least period, and write Z_E=sum_(a coprime to every b in E)rho(a), similarly Z_F. Its unchanged time in EVERY version is
\[
L_t(w)=L_1(w)=\frac d2\log(Z_EZ_F)-\sum_{i<d}\log\rho(w_i)>0.
\tag{11}
\]
This is the cycle sum from (1), not a borrowed period; positivity follows term by term from j<1. Every incoming history of that necklace has the same H=L_1(w)Z. Non-eventual orbits still have H={0}. This covers all source orbits and all repetitions without a high-period census.

| Audit item | Outcome and limitation |
| --- | --- |
| Measured source / every-Borel IMAGE | Established independently here; no conditional source theorem remains borrowed |
| Continuous I_2 version | STOP: impossible already at (3,2)^infinity |
| Measurable normalized versions | Entire family established, including all three fixed controls |
| Full-point clock identification by mu | Fails: same transport has different least times on the whole null class O |
| Other source-orbit scope | Completely retained; all arrows outside O unchanged pointwise |
| Classical / formal / analytic | NOT APPLICABLE / UNASSIGNED / T3 NOT AUDITED; B NOT INVOKED |

**Decision: STOP the continuous-version requirement; retain the measurable audit and version-freedom theorem.** No measurable clock is ruled out by the continuity result. Conversely, full support, measurable positivity, normalization and exact IMAGE do not canonically determine a null-periodic time. Identifying that time would require additional full-point selection structure; this audit supplies none. This does not say every possible regularity condition fails, that all null modifications give normalized clocks, or that every arithmetic dynamics is obstructed. No version is promoted to canonical, no t is fitted to a prime, and 380's frozen version is unchanged.

## Reproducibility, exposure and final-round boundary

Scientific inputs were exactly the two linked cards, read completely through their last lines. The author retains earlier internal research context but read no main, raw, peer or batch log for this audit. One bounded author-side helper independently derived the continuity obstruction from those same cards conditional on IMAGE; Section 3 supplies that dependency with its own proof. This is author-side assistance, not the separate review. Shared-history model work is NOT_CALIBRATED, not blind discovery, external peer review or a novelty claim.

Proofs use exact probability identities, finite-history formulas and summable rational bounds. No external literature search, scientific numeric scan, new parameter selection, Git operation, upload or publication artifact was used. ARS's scoped claim/evidence discipline was retained; criteria_binding_unavailable, with no venue-readiness claim.

Data availability: all inputs and proofs are in this package and the linked source card. Ethics: no human/animal subjects or personal data. Contributions: AI-assisted formal analysis and writing are disclosed without assigning human authorship. Funding/conflicts: no declarations supplied; absence is not presumed.

This is round 5/5. After integration and CP2/CP3, the batch must hand off and await the user; no sixth round is authorized here.
