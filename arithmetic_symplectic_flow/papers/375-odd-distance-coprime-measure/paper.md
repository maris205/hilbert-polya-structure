# Hard odd-distance coprime histories fail positive inverse-image admission

**Paper ID:** 375-odd-distance-coprime-measure.  
**Candidate:** ANG-20260922-ODC01; batch HARD-NONLOCAL-20260922-F, round 1/5.  
**Date / status:** 2026-09-22; EXACT MEASURED SOURCE; STRICTLY POSITIVE IMAGE FAIL; CLOCK NOT DEFINED; STOP.  
**Route:** classical A0/A1/A2 NOT APPLICABLE; T3 NOT AUDITED; formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

The complete hard odd-distance coprime history space admits the frozen invariant, full-support mixture probability and all its actual legal prefix inverses. Its strictly positive inverse-image requirement nevertheless fails. A legal prefix sends a positive-mass alternating tail to a zero-mass singleton, and the prescribed restricted-cylinder density tends to zero. Removing all atomic mixture components does not repair the problem: the specified positive-mass empirical-tail set has zero-mass prefix-7 image, and its frozen density vanishes at every point of that set. Nonnegative image densities do exist, so the obstruction is strict positivity, not absence of absolute continuity. The full source, incoming histories and source isotropy remain established. MAIN and DROP-SINGLETONS have no admitted physical clock; two other controls have their own complete clock ledgers.

## 1. Frozen question and same-object boundary

The original 88-line [candidate card](candidate-card.md) has SHA-256 e7e4fa21a66ebd823d391720731a1448867f6d488dfe4399755979621d0fa149. Root released this mathematical audit after the [CP1 scope review](evidence/scope-review.md). No card definition is changed here. The question is whether this full hard source and this mixture own a finite strictly positive all-point IMAGE law, before any physical clock is constructed.

| Item | Frozen owner and restriction |
| --- | --- |
| Arithmetic lineage | Common-divisor witness exclusion -> all odd-separated positions -> actual legal prefix domains |
| Source | All x in A^N0, A={2,3,...}, with gcd(x_i,x_j)=1 for every odd j-i |
| Probability | The stated finite-alphabet alternating product mixture on that whole source |
| Inverses | Every legal prefix insertion, with its actual full domain |
| Version | The prescribed ratios of domain-restricted cylinders, at every legal tail |
| Source arrows | Actual triples retaining integer lag, not labels for alternative witnesses |
| Clock gate | Strictly positive every-Borel IMAGE and its prescribed full-point version must both pass |
| Unavailable fields after failure | Physical clock, extension, physical stabilizers and physical packets NOT DEFINED |
| Controls | FIXED-TWO, ARITHMETIC-OFF and DROP-SINGLETONS, each with its own law |

The arithmetic constraint is nonlocal but parity-specific. Neither the law's finite-set mixing labels nor a typical component label is added as a source coordinate. No prime alphabet, external prime-time roof, sieve conjugacy, geometric lift or strong naturalness conclusion is asserted.

## 2. The entire hard source and all actual inverses

Let S_e(x) and S_o(x) be the sets of symbols appearing at even and odd positions. The defining condition is equivalent to gcd(s,u)=1 for every s in S_e(x), u in S_o(x), regardless of whether these sets are finite. Each forbidden coordinate pair defines an open cylinder condition, so X is closed in the countable product of the discrete alphabet, with its subspace topology and Borel sigma algebra.

**Proposition 1 (full source owner).** The left shift T:X->X is a continuous surjection. For every a>=2, its actual inverse domain and branch are
\[
E_a=\{y\in X:\gcd(a,y_{2j})=1\ \hbox{for every }j\geq0\},\qquad I_a(y)=ay.
\]
Each E_a is closed and Borel, and I_a:E_a->[a] is a homeomorphism. These are all inverse branches.

**Proof.** Shifting preserves odd differences between retained coordinates and therefore preserves every cross-parity gcd condition. For any y, the symbol y_1 is coprime to every even-coordinate symbol of y, so y_1y is a legal preimage. Inserting a imposes exactly the displayed conditions: its odd-distance partners are y_0,y_2,...; all other pairs are already legal in y. Coordinate insertion is continuous and its inverse on the clopen cylinder [a] is T. Each E_a is the intersection of its clopen coordinate conditions. Every preimage begins with a unique a, which proves completeness. QED.

Closed does not mean open here. For any a take b=a+1 and c=a(a+1)+1, and choose a prime divisor r of a. Then y=(bc)^infinity belongs to E_a. Replacing a sufficiently distant even entry b by r preserves membership in X, because gcd(r,c)=1, but violates E_a. Every cylinder neighborhood of y therefore meets X outside E_a. In particular T cannot be treated as a local homeomorphism at ay by assuming its branch image is open; no etaleness is inferred.

For a word u of length m, its entire domain is
\[
D_u=\{t\in X:u\text{ obeys its internal odd-distance conditions, and }
\gcd(u_i,t_j)=1\text{ whenever }i<m,\ j\geq0,\ m+j-i\text{ is odd}\}.
\tag{1}
\]
Empty words have domain X; internally illegal words have empty domain. Every D_u is closed, I_u(t)=ut is a homeomorphism onto [u], and these are exactly all inverses of all iterates T^m, by applying the source condition to every old and inserted coordinate pair.

## 3. The frozen mixture: normalization, invariance, support and atoms

Let V contain the ordered pairs of nonempty finite sets (S,U) with every cross pair coprime. Put code(S)=sum_(a in S)2^(a-2), q(S,U)=2^(-code(S)-code(U)), B=sum_V q(S,U), and w=q/B. Let nu_(S,U) have independent uniform S symbols at even sites and uniform U symbols at odd sites, and mu=sum_V w nu_(S,U).

**Proposition 2 (complete measured source).** The recipe defines a shift-invariant probability on the full Borel space X with full topological support. Its point atoms are exactly x=(s,u)^infinity with gcd(s,u)=1, and
\[
\mu\{(s,u)^\infty\}=w_{\{s\},\{u\}}
=2^{-(2^{s-2}+2^{u-2})}/B.
\tag{2}
\]
The total atomic mass is strictly between zero and one.

**Proof.** Finite nonempty sets have codes exactly the positive integers, by unique binary expansion. Thus sum_S 2^(-code(S))=1, so B<=1; the legal pair ({2},{3}) gives B>0. The excluded pair ({2},{2}) has positive weight, so B<1. Each product law is carried by X, the weights sum to one, and their countable mixture is a Borel probability. Independence and the parity swap give T_*nu_(S,U)=nu_(U,S). Symmetry of V and q proves T_*mu=mu.

Any nonempty legal finite cylinder has finite parity-symbol sets. When one is absent, fill it from any legal continuation, for example using a symbol one greater than the product of the already specified opposite-parity symbols. The resulting nonempty finite pair lies in V and its component gives the cylinder positive probability. Thus support is all X, not only histories using finitely many symbols. For example, X includes unbounded histories with odd sites constantly 2 and increasing odd integers at even sites; no such histories are deleted even though this mixture assigns the whole finite-alphabet class probability one.

If either |S| or |U| exceeds one, the probability of any specified path tends to zero along longer cylinders on that parity. Only singleton-singleton components have point masses, and each supplies exactly its own alternating history. This proves (2). There are positive singleton weights, but also a positive genuinely nonatomic component, for example S={2,4}, U={3,5}. The total atomic mass is therefore in (0,1). In a countable-coordinate space any Borel atom selects a unique full-mass coordinate cell successively and hence a singleton of the same mass. Thus this calculation also determines the actual measure-theoretic atom status. QED.

## 4. Every restricted denominator and the actual image measures

Let C_N(y) fix the first N symbols, and let A_N(y), U_N(y) be the sets seen on even and odd positions in that prefix. Write e=ceil(N/2), o=floor(N/2). Under nu_(S,U), the event E_a has probability one if all s in S are coprime to a, and zero otherwise: in the latter case infinitely many independent even draws would have to avoid a nonempty subset of S.

Consequently, with a perpendicular symbol meaning pairwise coprimality,
\[
\mu(E_a\cap C_N(y))=
\frac1B\sum_{\substack{(S,U)\in V,\ S\perp a\\A_N(y)\subset S,\ U_N(y)\subset U}}
q(S,U)|S|^{-e}|U|^{-o}.
\tag{3}
\]
The numerator has the exact form
\[
\mu(I_a(E_a\cap C_N(y)))=
\frac1B\sum_{\substack{(S,U)\in V\\A_N(y)\subset S,\ U_N(y)\cup\{a\}\subset U}}
q(S,U)|S|^{-e}|U|^{-(o+1)}.
\tag{4}
\]
Here the labels in (4) are swapped from the prefixed path's parity labels, using q(S,U)=q(U,S); they are not extra source coordinates.

For every y in E_a and every finite N, (3) is positive. Choose finite parity sets from y containing its specified prefix and at least one symbol on each parity; the even set is entirely coprime to a, so that component contributes positively. The numerator equals the mass of the nonempty allowed cylinder [a,y_0,...,y_(N-1)] and is positive by full support. The N=0 case has the same argument with an empty specified prefix. Thus all frozen finite ratios exist and are positive.

For any Borel D contained in E_a, independence of the first coordinate and the tail, followed by the same label swap, proves the exact every-Borel image law
\[
\lambda_a(D):=\mu(I_aD)=
\sum_{(S,U)\in V}w_{S,U}\frac{\mathbf1_{\{a\in U\}}}{|U|}\nu_{S,U}(D)
\leq\mu(D).
\tag{5}
\]
The image is Borel since I_a is a homeomorphism onto [a]. This proof is directly for Borel D, not merely for cylinders. Equation (5) establishes absolute continuity and a nonnegative IMAGE density; it does not establish strict positivity. It also bounds every finite ratio in (3)--(4) by one.

## 5. Precommitted singleton and all-point version tests

Take y=(3,2)^infinity. Both 2 and 4 are legal predecessors. Formula (2) gives the actual complete singleton masses
\[
\mu\{y\}=\frac1{8B},\quad
\mu\{I_2y\}=\frac1{8B},\quad
\mu\{I_4y\}=\mu\{(4,3,2,3,2,3,\ldots)\}=0.
\tag{6}
\]
The last history is not (4,3)^infinity: its even coordinates are not constant, so every component gives its singleton probability zero.

**Proposition 3 (intrinsic positive-IMAGE failure).** The prescribed restricted-cylinder limits at y are j_2(y)=1 and j_4(y)=0. No strictly positive Borel IMAGE density for I_4 can satisfy the required identity on its entire domain.

**Proof.** E_a intersect C_N(y) decreases to {y}, and its injective insertion images decrease to {I_a y}. Continuity from above of the finite measure, together with the positive limiting denominator in (6), gives the stated limits. Every finite ratio remains positive by Section 4; that does not force a positive limit. On the whole singleton Borel set D={y}, any IMAGE version must satisfy
\[
0=\mu(I_4D)=\int_D j_4\,d\mu=j_4(y)/(8B).
\]
Strict positivity is impossible independently of the chosen limit prescription. QED.

Both constant-parity phases are retained. More generally, for y=(s,u)^infinity with gcd(s,u)=1 and any legal a coprime to s, the same continuity argument gives
\[
\lim_N\frac{\mu(I_a(E_a\cap C_N(y)))}{\mu(E_a\cap C_N(y))}
=\begin{cases}1,&a=u,\\0,&a\ne u.\end{cases}
\tag{7}
\]
For the phase (2,3)^infinity, predecessor 3 returns to (3,2)^infinity with the same positive mass; predecessor 5 has zero singleton image and limit zero. Predecessors 2 and 4 are not legal on that phase, and are not assigned artificial density values.

MAIN therefore fails both the frozen strict-positivity condition and the existence of any alternative everywhere strictly positive Borel IMAGE version. Nonnegative densities still exist by (5). No assertion about convergence at all other legal points is necessary or made after this decisive failure.

## 6. Entire actual source histories, lag kernel and source isotropy

These source fields do not require clock admission. Retain exactly
\[
G=\{(z,m-n,y):m,n\geq0,\ T^m z=T^n y\},
\]
with source y and range z, composition (z,l,y)(y,k,x)=(z,l+k,x), inverse (y,-l,z) and units (x,0,x). Padding the two common-middle exponents to their maximum proves closure under composition. Equal triples alone are identified, so differing witnesses do not multiply arrows and nonzero isotropy lag is never discarded.

**Proposition 4 (full source ledger).** For every x in X,
\[
\mathcal O_G(x)=\{uT^n x:n\geq0,\ u\text{ any finite prefix satisfying (1)}\},
\qquad
\ker\ell=\{(z,0,y):T^n z=T^n y\text{ for some }n\geq0\}.
\tag{8}
\]
If x is not eventually periodic, its source isotropy is trivial. If its eventual tail has least period d, its entire source isotropy is {(x,kd,x):k in Z}.

**Proof.** A witness equality writes z as a finite prefix followed by T^n x, and each such legal prefix supplies a witness; this proves the first formula. Lag zero means that the two exponents are equal, proving the second. Equality of two distinct shifts is exactly eventual periodicity. Thereafter the differences of equal shifts are precisely multiples of the least tail period, and every such multiple is realized after the preperiod. QED.

Every admissible periodic history has EVEN least period. An odd period would repeat a symbol at an odd distance, contradicting gcd(a,a)=a>1. For an even-length word w, its infinite repetition is admissible exactly when every even-position letter of w is coprime to every odd-position letter. Primitive source words are precisely those admissible words with no shorter period, identified by cyclic rotation only; orientation reversal is not separately quotiented. Constants are forbidden. A primitive-d source cycle has all d phases and source repetitions rd; all legal incoming prefixes in (8), including null histories, remain in its source orbit. Distinct primitive necklaces define distinct eventual-periodic source orbits.

In particular the 23 source orbit includes both atomic alternating phases and every legal incoming history, including the zero-mass state I_4(32)^infinity. Its source isotropy is exactly 2Z at every such eventually alternating state. These are SOURCE statements, not physical closed-orbit claims.

**Clock-dependent fields for MAIN:** kappa, A_m, c, its clock kernel and clock/lag intersection, the clock extension and its isotropy, physical H, physical packets and physical repetition times are all NOT DEFINED. Neither zero nor an infinite-time substitution is made after failed admission. No cocycle descent or finite-history positive clock law is claimed for this owner.

## 7. FIXED-TWO and ARITHMETIC-OFF: separate admitted controls

**FIXED-TWO.** Its entire carrier consists of (23)^infinity and (32)^infinity, each with mass 1/2. T interchanges them, so this own atomic probability is invariant and has full support. The only inverse branches are I_2 on the phase beginning 3 and I_3 on the phase beginning 2; all other domains are empty. Every nonempty restricted cylinder on either domain is its singleton, whose insertion image also has mass 1/2. Thus its prescribed limits equal one everywhere and every-Borel IMAGE holds. All finite legal insertions likewise have density one.

Here kappa_F=A_(F,m)=c_F=0 on all actual histories; descent and composition are exact. The full lag groupoid has arrows (z,l,y) with z=T^l y, the endpoint determined by parity. Its clock kernel is the entire groupoid; its lag kernel and their intersection are exactly the units. Source isotropy and extension isotropy at every real height are both 2Z. All legal incoming prefixes remain one of these two phases. The extension preserves height, so its orbit set is R, physical height translation has H_F={0}, and no positive physical period exists. The source period is 2 and source repeats have lag 2r and clock zero, not closed physical-time periods. This zero clock is a proved admitted control result, not a value assigned to MAIN.

**ARITHMETIC-OFF.** Its carrier is all A^N0 with its own independent marginal rho(a)=1/[a(a-1)]. The marginal sums to one by telescoping. Product cylinders define an invariant full-support probability, and every length-N cylinder has mass at most 2^(-N), so the source is nonatomic. All inverse domains are the full carrier, and all finite prefixes are legal.

Its own cylinder prescription is constantly j_(O,a)=rho(a)>0; multiplication of product-coordinate masses proves every-Borel IMAGE. These locally constant versions apply at every tail, including null periodic histories. A finite prefix u has IMAGE J_O(u)=product_(i<|u|)rho(u_i), so with W_O(u)=product_(i<|u|)u_i(u_i-1),
\[
c_O(ut,|u|-|v|,vt)=\log[W_O(u)/W_O(v)].
\tag{9}
\]
Common-tail factors cancel under witness padding and composition, proving descent and the cocycle law on actual lag triples. The full clock kernel consists of arrows with equal W_O products, the lag kernel of those with equal prefix lengths, and their intersection imposes both. Empty products equal one. For example, prefixes 4 and 23 have equal product 12 and different lags, while 23 and 32 give distinct zero-lag, zero-clock endpoints; replacement cancellations are not suppressed.

All source incoming histories are uT^n x with arbitrary finite u. Source isotropy is trivial on non-eventually periodic x and is dZ on eventual primitive-d histories. For a primitive word w,
\[
L_O(w)=\sum_{i<d}\log[w_i(w_i-1)]>0,\qquad
c_O(x,kd,x)=kL_O(w).
\]
Every extension unit (x,h) is retained; extension isotropy is trivial. Physical height translation has full stabilizer H_x={0} on non-eventual histories and L_O(w)Z on eventual ones. For each complete source orbit, connecting arrows identify all incoming height offsets modulo exactly H_x, so the corresponding part of the orbit set is R/H_x. Every primitive necklace gives one physical packet, all its cyclic and real height phases are present, and written repetitions have time rL_O(w) with least time L_O(w). Constants are admissible here: 2 has time log 2, but 3 has time log 6, a wrong prime primitive. These owned control clocks and words are not transferred to MAIN.

## 8. DROP-SINGLETONS: full support without atoms does not repair admission

Let V_* be the same allowed finite-set pairs with |S|,|U|>=2, B_*=sum_(V_*)q(S,U), and mu_* its separately normalized mixture. The pair ({3,5},{2,4}) is legal, so 0<B_*<=B<1. Symmetry again proves shift invariance. Every component cylinder has mass at most 2^(-N), so the mixture is nonatomic.

Its support is still the ENTIRE X. Given a finite legal prefix, choose nonempty finite parity sets from a legal continuation. Enlarge S, if necessary, by a new integer congruent to 1 modulo the product of U; then enlarge U by a new integer congruent to 1 modulo the product of the enlarged S. The choices can be made arbitrarily large and distinct from existing letters. Both sizes reach at least two without violating any cross-coprimality or changing the prefix, yielding a positive component contribution. For domain-restricted denominators at any y in E_a, choose new even symbols congruent to 1 modulo a times the product of U; the same construction keeps S perpendicular to a. Thus every restricted denominator remains positive. Numerators are positive by full support.

The full source, T, closed domains (1), actual triples, lag kernel and entire source isotropy are exactly the source definitions proved in Sections 2 and 6; only the probability has changed. Equations (3)--(5) hold afresh with V_*, B_* and its own weights. In particular nonnegative IMAGE remains available. No MAIN density is imported.

Let D be the entire precommitted Borel set: all even coordinates lie in {3,5}, all odd coordinates in {2,4}, and the empirical laws on the two parities converge to the respective uniform laws. Coordinate restrictions and countable limit conditions make D Borel; every y in D belongs to E_7. Its actual mass and whole insertion-image mass are
\[
\mu_*(D)=\frac{2^{-15}}{B_*}>0,\qquad \mu_*(I_7D)=0.
\tag{10}
\]

**Proof of (10).** Positive probability for infinitely many draws all lying in the indicated sets requires S subset {3,5}, U subset {2,4}. Both cardinalities are at least two, hence these sets must be exactly those displayed. Their codes are 10 and 5. In this component the required empirical frequencies hold with probability one. For completeness, for each symbol, the variance of its empirical frequency at k^2 draws is at most 1/(4k^2). Chebyshev's bound and summability give almost-sure convergence on this subsequence for every rational error tolerance; interpolation between k^2 and (k+1)^2 proves convergence at all lengths. Apply this finite list of conclusions on both parities.

The full image I_7D=[7] intersect T^(-1)D is Borel. A component giving this image positive mass would need its even alphabet to contain 7, from the first coordinate, and to be contained in {2,4}, from all infinitely many subsequent even coordinates. This is impossible. Each component image mass, and therefore the mixture image mass, is zero. QED.

The prescribed version also fails at EVERY point of D. For y in D, sufficiently long prefixes have shown both letters on each parity. The restricted denominator in (3) then has the component ({3,5},{2,4}) contribution (2^(-15)/B_*)2^(-N). In the swapped-label numerator (4), every contributing S has size at least two and every U contains {2,4,7}, hence has size at least three. Since normalized weights sum to one,
\[
0<
\frac{\mu_*(I_7(E_7\cap C_N(y)))}{\mu_*(E_7\cap C_N(y))}
\leq\frac{2^{15}B_*}{3}\left(\frac23\right)^{\lfloor N/2\rfloor}
\longrightarrow0.
\tag{11}
\]
Finite positivity also follows from the legal numerator pair ({3,5},{2,4,7}) in those swapped labels. Thus the frozen j_7 limit is zero everywhere on D.

Independently of that version, any strictly positive Borel density would give integral_D j_7 dmu_*>0: the sets {j_7>=1/k} cover D, so one has positive mass. This contradicts (10). DROP-SINGLETONS therefore has an intrinsic strictly-positive IMAGE failure on a positive-mass atomless set, not merely a removable null-path defect. Its kappa, c, clock kernel and intersection, extension and extension isotropy, physical H, packets and physical repetitions are all NOT DEFINED. Its source fields remain intact; no clock is set to zero.

## 9. Results, limitations and bounded decision

| Owner / obligation | Exact result | Boundary |
| --- | --- | --- |
| MAIN full source and measure | Entire hard X, full support, invariant mixed atomic/non-atomic law, all inverses | Mixing labels are not source coordinates |
| MAIN IMAGE | Every restricted denominator positive; j_2=1, j_4=0 at the frozen tail; no strictly positive version | Nonnegative IMAGE exists by (5) |
| MAIN source ledger | All incoming prefixes, even primitive source words, full lag kernel and source isotropy | Physical fields NOT DEFINED |
| FIXED-TWO | Own IMAGE=1; c=0; extension isotropy 2Z; H={0} | No closed positive-time physical packet |
| ARITHMETIC-OFF | Own product IMAGE and complete positive-clock packet ledger | Wrong prime primitive log 6 |
| DROP-SINGLETONS | Own full-support nonatomic law; positive D has zero prefix image; all its prescribed limits vanish there | Strict positivity fails intrinsically; physical fields NOT DEFINED |
| T3 / formal Route | No analytic audit or formal evaluation | T3 NOT AUDITED; classical NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED |

**Decision: STOP this measured owner at clock admission.** The hard arithmetic source and its probability are genuine defined objects; full support and the existence of nonnegative transport do not imply the strict positivity required by its clock contract. The adverse DROP control rules out attributing this particular obstruction solely to atomic mixing components. It is not a no-go theorem for every probability on this source or every hard nonlocal source. Strong naturalness remains OPEN. No post-hoc measure replacement, branch deletion, all-point version patch, time rescaling or physical construction is made.

This completes the bounded scientific obligations of round 1/5. Any next candidate requires its own frozen card; no old field or theorem credit transfers. No sixth round or external action is authorized by this paper.

## Reproducibility and disclosures

The [frozen card](candidate-card.md), [CP1 scope review](evidence/scope-review.md) and exact proofs above supply all mathematical inputs and methods. No scientific numerical run, cutoff, external source search, dataset, publication artifact or Git operation was used. The author read all 88 card lines through EOF, the full CP1 and the repository template; no 375 raw or peer derivation was read. A bounded author-side helper independently derived the displayed singleton and empirical-set calculations from the card only. This assistance is disclosed as author-side work, not the separate raw review.

The design expectation and shared history are disclosed in the card. Model-assisted execution is NOT_CALIBRATED, not blind discovery or external peer review; actual served model is not independently attested. ARS evidence/claim discipline was applied in the bounded writing role; criteria_binding_unavailable, with no venue-readiness claim.

Data availability: all mathematical input and proof are in this package. Ethics: no human or animal subjects or personal data. Contributions (CRediT): AI-assisted formal analysis and writing are disclosed without assigning human authorship. Funding and conflicts: no declarations supplied; absence is not presumed.
