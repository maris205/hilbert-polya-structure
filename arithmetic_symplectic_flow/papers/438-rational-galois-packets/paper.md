# Admitted Galois conjugates of rational-dynamical packets: multiplicity, phases and field boundaries

Paper ID: `438-rational-galois-packets`.
Candidate ID: `ANG-AUDIT-20260923-RGP01`.
Date: 2026-09-23. Status: exact conditional filter and three complete external controls.
Outcome: `ADMITTED GALOIS PACKET FILTER ESTABLISHED; PHASE AND DOMAIN EXCEPTIONS RETAINED`
Portfolio: retain conditional filter / FORK; no arithmetic candidate admission.
Batch NONHOMOGENEOUS-FEEDBACK-20260923-R, round 4/5.
Classical NOT APPLICABLE; ARITHMETIC T1 NOT PASSED; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.

## Abstract

For the frozen partial rational-map class under Lebesgue measure, all actual inverse branches and their assigned all-point IMAGE clocks are constructed. An algebraic cycle is compared only with conjugates explicitly admitted through the same actual rational-formula itinerary. A prime primitive forces the signed return determinant to be one of ±p or ±1/p. Its admitted conjugate cycles then have the same entire clock group, but distinct points can instead be phases of one cycle. The number of conjugate packets and the rotation kernel give a conditional cyclic field restriction on the coordinate field, not on an arbitrary larger auxiliary field. Three full controls separate duplicate conjugate fixed packets, conjugates within a single prime-clock two-cycle, and failure of conjugate admission. Every control's periodic/nonperiodic histories, nonlinear clock kernel, isotropy and physical phases are retained. No automorphism or measure transport on the full real carrier is inferred.

## 1. Candidate identity and same-object ledger

| Item | Frozen object / scope |
| --- | --- |
| Carrier | Open X⊂R^d with ordinary Lebesgue μ |
| Actual map | Countably disjoint Borel legal pieces E_i; on E_i use its assigned rational-coefficient rational formula f_i |
| Germ ownership | Open U_i⊃E_i, no denominator or derivative determinant zero, image in X; no global injectivity assumed |
| Terminals | X∖⋃E_i remains, with identities and every incoming; no next-step clock |
| Inverses / IMAGE | Complete local injectivity atlas; own analytic inverse determinant at every actual point |
| Arithmetic test data | Finite totally real Galois K/Q, Γ=Gal(K/Q), a verified least-q algebraic cycle and the extra admission condition |
| Packets / physical time | Full actual point-lag groupoid, entire H, all real heights; least positive generator and repeats |
| Controls | A on R, B on R², C on (0,∞), each with its own Lebesgue measure and full map |
| Unconstructed fields | No positive roof, symplectic/Hamiltonian lift, transfer operator, trace, zeta or quantization |

Every determinant below is a derivative determinant of the same frozen branch owner, not a dynamical determinant or an externally assigned arithmetic clock. Signed and zero clock values remain permitted.

## 2. Question and strongest supported claim

The necessary benchmark is a nonempty positive ledger, all primitives log p for ordinary primes, and at most one packet per prime; all-prime coverage is additional. This audit gives a conditional obstruction if an admitted prime-clock algebraic core has more than one conjugate source cycle. It also gives an exact rotation/field boundary when all conjugates lie in one cycle.
Neither irrational coordinates alone nor a formal conjugate root forces a violation. The complete admission hypothesis and distinction between cycle phases and different cycles are essential. No unconditional failure or existence theorem for all rational maps, generic arithmetic source, field-norm clock substitution, or Route evaluation is asserted.

## 3. Inputs, lineage and exposure

Let x_j=T^j x, 0≤j<q, be a verified actual least-q cycle with x_j∈K^d and actual source piece E_(i_j). The extra hypothesis is

\[
 \sigma(x_j)\in E_{i_j}\quad
   \text{for every }\sigma\in\Gamma,\ 0\le j<q.                 \tag{1}
\]

It is actual membership in the specified piece, including its legal-germ conditions, not merely a formal equation or membership in another similarly written branch. Rational coefficients do not preserve order inequalities or source pieces. Write \(K_x=\mathbb Q(x^{(1)},\ldots,x^{(d)})\) for the coordinate field of the initial vector x; it need not equal K. Superscripts here denote vector coordinates, whereas x_j denotes a cycle phase.
The conditional lineage is prime-symbolic admissibility → rational nonhomogeneous geometry → actual packets. This paper supplies no missing symbolic source or arithmetic naturalness.
The [card](candidate-card.md) was read in full, 97 lines through EOF after release, SHA-256 6ec186a6e4cbb26fb743633b11904de36145b4a22e0b0531098ff0ef79dd1c8b.
Scouting read the full 430 batch summary, 110 lines, SHA e8480e2111f2d2182acca25a8225c16f542906a417e6de779faeab97eefc81cf; full 429 card, 105 lines including Outcome, SHA 7e20089a8100181637d997bc9425e2420ad1eb5db0e2fc47c860b7858f1f077a; and full 393 card, 89 lines including Outcome, SHA ac19239563de81003ef96fd51aa0ba888a8140be915622a66acbce543b979437.
An earlier local-isolation proposal was abandoned when root disclosed the overlap with 439; no file or proof was produced. Root then suggested this Galois direction. No 439 file, new peer/raw report or additional historical card was read. Shared design expectations and control feasibility were informal, not blind/sealed preregistration, a novelty claim or imported proof credit.

## 4. Complete actual inverse atlas and all-point IMAGE

Fix the rational-ball enumeration. For each i retain balls V_(i,n) contained in U_i on which f_i is injective, in their fixed enumeration order. Every point of E_i lies in one: the inverse function theorem provides an injective open neighborhood, and a rational ball inside it can contain the point. Define

\[
 P_{i,n}=E_i\cap\left(V_{i,n}\setminus\bigcup_{m<n}V_{i,m}\right),
 \quad Q_{i,n}=f_i(P_{i,n}),\quad
 \theta_{i,n}=(f_i|_{V_{i,n}})^{-1}|_{Q_{i,n}}.                \tag{2}
\]

The rational coordinates are analytic on their stated nonsingular domains with nonzero denominators. Each unrestricted ball map is an analytic diffeomorphism onto its open image. Thus P and Q are Borel, θ is an actual inverse, and the P's partition every legal source exactly once. The assembled T is Borel on its countable Borel source partition. Overlapping Q's preserve different actual predecessors; atlas labels do not multiply a source or an arrow. All actual inverse roots belong to this atlas, even if there are infinitely many across source pieces.
For every w∈Q set

\[
 J_{i,n}(w)=|\det D\theta_{i,n}(w)|
  =|\det Df_i(\theta_{i,n}w)|^{-1}>0,\qquad
 \mu(\theta_{i,n}F)=\int_F J_{i,n}\,d\mu
 \quad(F\subseteq Q\text{ Borel}).                            \tag{3}
\]

This follows by change of variables on the actual unrestricted ball diffeomorphism, restricted to F. The determinant is finite positive at every assigned point, including null cuts. The prescribed inverse germ fixes that version; an a.e. density alone would not do so. Compositions of actual restricted inverses have the product IMAGE factor by successive substitution and the derivative chain rule.
Consequently each legal v∈E_i owns

\[
 \kappa(v)=\log|\det Df_i(v)|,\quad
 R_m(v)=\prod_{j=0}^{m-1}|\det Df_{i(T^jv)}(T^jv)|,\quad
 S_m(v)=\log R_m(v),\quad R_0=1,\ S_0=0.                     \tag{4}
\]

Only legal finite paths have these products. A terminal next step and its clock are NOT DEFINED, not zero or absorbing dynamics. No target's outgoing permission is imposed on its incoming inverse branches.

## 5. Full histories, kernels, H and physical phases

Use every actual triple

\[
 \mathcal G_T=\{(z,m-n,w):T^mz=T^nw\text{ legally},
                    m,n\ge0\},\qquad c=S_m(z)-S_n(w).         \tag{5}
\]

Source is w and range z; equal triples are identified and integer lag retained. Equal-lag witnesses differ by a common index shift and have the same additional tail, which cancels in c. For composition, align the two middle indices along the already existing longer middle path; this proves closure and c-additivity without extending a terminal. A first-witness choice from the countable index pairs also makes c Borel. The forward arrow (Tv,−1,v) has clock −κ(v).
The exact kernels on the whole owner are

\[
 K_{\rm lag}=\{(z,0,w):T^mz=T^mw\text{ for some legal }m\},
 \quad K_c=\{(z,m-n,w)\in\mathcal G_T:R_m(z)=R_n(w)\},
 \quad K_{\rm joint}=K_{\rm lag}\cap K_c.                    \tag{6}
\]

Any actual witness gives the same test. Nonunit coalescence is not discarded. The complete predecessor set is \(I(w)=\{\theta_{i,n}(w):w\in Q_{i,n}\}\); set I⁰(w)={w} and I^(m+1)(w)=⋃_(v∈I^m(w))I(v). The source packet of w is exactly
\(\bigcup_{n:T^nw\ {\rm exists}}\bigcup_{m\ge0}I^m(T^nw)\).
This retains all depths and all real ancestors, not only algebraic ones.
A nonzero source isotropy lag forces unequal iterates of one state to agree, hence eventual periodicity. If its eventual core has least source period q, exactly qZ occurs as source isotropy. Let C be its signed q-step clock. Transient sums cancel, so the isotropy clock takes jq to jC and its **entire** image is H=CZ. Non-eventually-periodic and terminating packets have trivial source isotropy and H={0}.
Choose a reference point w in one packet and actual arrows g_z=(z,ℓ_z,w), with b_z=c(g_z). For an eventual q-cycle, every arrow from u to z has uniquely the lag ℓ_z−ℓ_u+jq and clock b_z−b_u+jC, j∈Z, by composition with reference isotropy. For a non-eventual packet there is only the j=0 term. This specifies every kernel as well: impose the lag, clock, or both zero equations.
The additive extension contains all (z,h) and arrows (w,h)→(z,h+c). Its complete phase over a source packet is \(h-b_z\in\mathbb R/H\). Reference changes alter only its origin/mod-H representative. Extension isotropy is qZ if C=0, trivial if C≠0, and trivial on non-eventual packets. Unrestricted height translation has stabilizer exactly H. Thus C≠0 yields one physical circle with primitive |C| and repeats n|C|, n≥1; H={0} yields a free line. Distinct source packets never merge by sharing a clock. This is a set-level description, not a nice quotient or measurable-selector assertion.

## 6. Admitted conjugate cycles and their owned determinant

Rational evaluation commutes with σ on K wherever its denominators do not vanish. Under (1), induction using the actual branch i_j gives
\(T^j(\sigma x)=\sigma(x_j)\) for j≤q. Each conjugate has the same least period q: an earlier return would, on applying σ^(-1) to its coordinate equality, give an earlier return of x. This is a statement about algebraic core coordinates, not an automorphism of R.
Differentiating a rational function with rational coefficients again gives rational functions with rational coefficients. Therefore the signed return determinant

\[
 D_x=\prod_{j=0}^{q-1}\det Df_{i_j}(x_j)\in K^\times,\quad
 C_x=\log|D_x|,\quad H_x=C_x\mathbb Z                         \tag{7}
\]

is owned by this actual cycle and its full incoming packet. At the admitted σ-cycle the signed determinant is σ(D_x). No automorphism is applied to a real logarithm or moved through an absolute value; after the algebraic determinant comparison its own real clock is computed afresh.
If a positive primitive of this packet equals log p, p an ordinary prime, the entire-H formula yields

\[
 |\log|D_x||=\log p
 \quad\Longleftrightarrow\quad
 D_x\in\{p,-p,p^{-1},-p^{-1}\}.                              \tag{8}
\]

In particular D_x is rational, hence every admitted conjugate determinant equals D_x itself. All admitted conjugate cores then have the same signed C_x, full H, primitive and repetitions. The reciprocal cases are essential: a contracting signed cycle sum also has positive physical primitive log p.
A field norm cannot replace (7): it multiplies conjugate determinants, rather than giving this single owner's return determinant. In particular (8) concerns D_x itself; an arithmetic statement about its norm is not a clock proof. D_x=±1 gives C_x=0 and no positive primitive. Without the prime premise the values log|σ(D_x)| need not agree.

## 7. Packet count, rotation kernel and the correct field

Let O={x_0,…,x_(q−1)}. The finite union of its admitted conjugate cores carries the coordinatewise Γ action, which commutes with T there by (1) and rational evaluation. It is not an action on arbitrary real ancestors. Two periodic cores sharing a point are the same source cycle; two different cores have disjoint full incoming packets, because a deterministic future cannot enter both.
Define distinct subgroups

\[
 \Gamma_O=\{\sigma:\sigma O=O\},\qquad
 \Gamma_x=\{\sigma:\sigma x=x\}=\operatorname{Gal}(K/K_x).
                                                                    \tag{9}
\]

There are exactly \([\Gamma:\Gamma_O]\) conjugate source cycles, hence that many distinct full packets. Distinct conjugated seeds need not mean distinct cycles. For σ∈Γ_O define its unique rotation r(σ) modulo q by σx=T^(r(σ))x. Commutation on the core shows r(στ)=r(σ)+r(τ) mod q. Its kernel is exactly Γ_x, so Γ_x is normal **in Γ_O**, and

\[
 \Gamma_O/\Gamma_x\hookrightarrow\mathbb Z/q\mathbb Z
 \quad\text{is cyclic};\qquad
 [K_x:\mathbb Q]=[\Gamma:\Gamma_O]\,[\Gamma_O:\Gamma_x].       \tag{10}
\]

The coordinate field is the same at every phase: rational forward evaluations put every x_j in K_x, while the remaining q−j steps recover x rationally from x_j. Thus Γ_x fixes the whole core and (10) introduces no hidden extra coordinate field.
More precisely, let F=K^(Γ_O). The Galois fixed-field correspondence and the proved normality identify \(K_x/F\) as a cyclic Galois extension of degree \([\Gamma_O:\Gamma_x]\), dividing q. The integer \([\Gamma:\Gamma_O]\) is the packet count, not automatically one.
If this positive-prime core is compatible with uniqueness per prime, (8) and the packet count force Γ_O=Γ. Then **K_x/Q**, not necessarily K/Q, is cyclic Galois and its degree divides q. Equivalently the restriction action on K_x is the cyclic rotation image, with kernel Γ_x. If additionally K=K_x, only then does this force Γ itself cyclic with |Γ| dividing q. A larger auxiliary K may have a nontrivial kernel and noncyclic Γ.
These are necessary conditions, not sufficient arithmetic admission. Nontrivial rotation can preserve a single packet, as control B will show. If (1) fails, the full-Γ count/field conclusion is not available; this does not by itself invalidate the remaining real owner. No Galois isomorphism or measure transport of its real incoming basins is claimed.

## 8. Complete cubic controls A and C: own inverses and dynamics

For A take all R; for C take all (0,∞), each with its own dx and actual total map

\[
 f(t)=\frac{t(t^2+2)}4,\qquad d(t)=f'(t)=\frac{3t^2+2}4>0.    \tag{11}
\]

The polynomial is strictly increasing with limits ±∞, and sends the positive half-line onto itself. Hence on each stated carrier the equation s³+2s−4t=0 has exactly one admissible root s=θ(t), the complete inverse. Its analytic germ has
\(J(t)=4/(3\theta(t)^2+2)\), positive finite everywhere; change of variables gives every-Borel IMAGE on that owner's own carrier. Its clock is κ(t)=log d(t), allowed to be negative or zero. C has neither zero nor negative objects; these were not deleted from A after calculation.
All fixed points solve t(t²−2)=0. A therefore has exactly \(0,\sqrt2,-\sqrt2\); C has exactly \(\sqrt2\). An increasing real map has no higher source cycles: f(t)>t forces all future iterates strictly increasing, and f(t)<t forces them strictly decreasing. Thus this fixed list is the complete periodic list for each owner. Bijectivity makes each fixed source's entire incoming packet a singleton.

| Owner / fixed source | Signed determinant D | Signed cycle clock C | Entire H; positive primitive |
| --- | --- | --- | --- |
| A at 0 | 1/2 | −log2 | (log2)Z; log2 |
| A at ±√2 | 2 | log2 | (log2)Z; log2 |
| C at √2 | 2 | log2 | (log2)Z; log2 |

Every such source has isotropy Z and trivial extension isotropy at every height; all its phases are h mod log2. A has exactly THREE positive physical packets, all primitive log2, failing uniqueness. C has exactly ONE, so the necessary nonempty/prime-only/unique conditions hold there; all-prime coverage fails. Neither is a lineage-admitted arithmetic candidate.
For the probe field Q(√2), A admits both fixed conjugates and they are different singleton packets, illustrating Γ_O≠Γ for q=1. C's conjugate −√2 is not a source object; its extra admission hypothesis fails. The class conclusion cannot be used to add that missing packet or to reject C by an assumed full-Γ action.

## 9. Complete cubic nonperiodic packets, signed kernels and phases

Define f^n for every integer n using the unique inverse, and \(D_n(t)=(f^n)'(t)>0\). These exact derivatives satisfy the composition rule and include negative n, without a finite numerical cutoff. Every actual arrow is precisely

\[
 (z,k,w),\quad z=f^{-k}(w),\qquad
 c(z,k,w)=-\log D_{-k}(w).
 \quad\text{For }k>0:\ c=\log D_k(z).                        \tag{12}
\]

The lag and joint kernels are units. The following describes the **entire** clock kernel, including nonperiodic sources. For each k≥1,
\(D_k(t)=\prod_{j=0}^{k-1}d(f^j(t))\) is even, continuous and strictly increasing for t>0: f^j is strictly increasing and positive there, and every positive factor d(f^j(t)) strictly increases. Its values at 0 and √2 are 2^(−k) and 2^k. Therefore it has a unique a_k∈(0,√2) with D_k(a_k)=1.
At positive lag k the only zero-clock arrows of A are

\[
 (\varepsilon a_k,\ k,\ \varepsilon f^k(a_k)),\quad
 \varepsilon\in\{1,-1\};                                   \tag{13}
\]

C retains exactly the ε=1 arrow on its own carrier. Negative-lag zero-clock arrows are precisely their inverses; lag zero gives all units. This is an exact infinite algebraic derivative-root prescription, not an empirical enumeration. The roots are nonfixed, so the nonunit kernel arrows do not create extension isotropy. No selected inverse or artificial zero clock was introduced.
For any positive-lag arrow (z,k,f^k z), its clock is negative, zero or positive according as |z| is below, equal to or above a_k; inverse arrows reverse that sign. C uses only positive z.
To classify every remaining source packet, write t=εr with r>0. For A both signs occur; for C only ε=1. The intervals \(0<r<\sqrt2\) and \(r>\sqrt2\) are invariant. In the inner interval f(r)<r, forward iterates tend to 0 and backward iterates tend to √2; in the outer interval f(r)>r, forward iterates tend to ∞ and backward iterates tend to √2. These endpoint claims follow from monotonicity and the complete fixed-point equation; a finite interior limit would have to be another fixed point.
Each inner orbit has a unique representative a∈[3/4,1), since f(1)=3/4, and each outer orbit has a unique representative a∈[2,3), since f(2)=3. The half-open images f^n of these intervals tile their respective invariant intervals: the successive endpoints are strictly ordered, have the just-proved limits, and cannot overlap except at the assigned single side of an endpoint.
Thus all nonperiodic packets have unique indices (inner/outer, ε,a) and consist of
\(\{\varepsilon f^n(a):n\in\mathbb Z\}\).
They have no source isotropy, no extension isotropy, and H={0}. Every depth-m predecessor is exactly f^(−m)(t); there are no transient branches into the fixed points. The sign notation here uses the explicit real oddness of f, not an extension of a field automorphism to R.
At t=εf^n(a), the reference arrow from εa to t has lag −n and clock −log D_n(a); derivatives are even by oddness of f and its inverse. The complete physical phase is therefore

\[
 \zeta=h+\log D_n(a)\in\mathbb R.                            \tag{14}
\]

Its equality within one packet is necessary and sufficient for an extension arrow by (12). All real ζ occur, and height translation is free. Equations (12)–(14) classify every history, clock kernel and phase for both full owners, not just their algebraic probes.

## 10. Complete plane control B and its conjugate phase exception

Set \(a(x)=x^2+x+3=(x+1/2)^2+11/4>1\) and
\(P(x)=a(x)a(-x)=x^4+5x^2+9>1\). On all R²,

\[
 F(x,y)=(-x,a(x)y),\quad
 F^{-1}(X,Y)=\left(-X,\frac{Y}{a(-X)}\right),\quad
 J(X,Y)=a(-X)^{-1},\quad \kappa(x,y)=\log a(x)>0.             \tag{15}
\]

Direct substitution proves global bijectivity; the full derivative is triangular with signed determinant −a(x), including its y-dependent off-diagonal entry. Thus (15) is its own everywhere-positive finite inverse IMAGE, with the every-Borel identity by change of variables. There are no terminals, poles or omitted branches.
For every integer n, including negative n, direct composition gives

\[
 F^{2n}(x,y)=(x,P(x)^n y),\qquad
 F^{2n+1}(x,y)=(-x,a(x)P(x)^n y).                            \tag{16}
\]

The complete groupoid is \((F^{-k}w,k,w)\), every k∈Z. With w=(x,y), the full signed-arrow clock is

\[
 c(k;x,y)=
 \begin{cases}
 n\log P(x),&k=2n,\\
 n\log P(x)+\log a(-x),&k=2n+1.
 \end{cases}                                               \tag{17}
\]

The backward iterate's multiplier of y in (16) is e^(−c); its derivative has the same absolute determinant. Formula (17) follows from its actual IMAGE, not a separately inserted multiplier. Its sign is the sign of k when k≠0, since every forward κ is positive; this also follows directly from a(x),a(−x)>1. Therefore lag, clock and joint kernels are all units.
Periodicity forces y=0 by applying an even iterate of (16). There is one fixed point (0,0); for each b=|x|>0 there is exactly one least-two source core {(b,0),(−b,0)}. These are the complete periodic cores, with no extra incoming because F is bijective.

| B source stratum | Source isotropy | Entire H / primitive | Extension isotropy / all phases |
| --- | --- | --- | --- |
| (0,0) | Z | (log3)Z; log3 | trivial; h mod log3 |
| y=0, abs(x)=b>0 | 2Z | (log P(b))Z; log P(b) | trivial; h+δ(x)log a(b) mod log P(b), δ=0 for x>0 and 1 for x<0 |
| y≠0 | trivial | {0}; no positive period | trivial; h+log abs(y)∈R, with source packet index below |

The two-phase formula uses the actual forward clock −log a(b) from (b,0) to (−b,0); it is not a constant half-period roof. P(b) is strictly increasing on b>0, from 9 to ∞. Hence B has one log3 packet and exactly one two-cycle packet for each real primitive length L>log9, with all repetitions nL. Different b's never merge. In particular b=1 gives an actual primitive log15, so the full owner's prime-only condition fails.
The frozen probe b=√2 has signed cycle determinant
\((5+\sqrt2)(5-\sqrt2)=23\), and primitive log23. Its two Galois conjugates are exactly the two phases of ONE source cycle, not two packets. Both are fully admitted in R². Here Γ_O=Γ, Γ_x is trivial, K_x=Q(√2) is cyclic of degree two and q=2. This is the allowed rotation case, not arithmetic admission or repair of the log15 counterexample.
The field norm of this rational D=23 from Q(√2) is 23²; replacing its clock by the logarithm of that norm would double the actual primitive.
All remaining points have y≠0 and are non-eventually-periodic. For x=0, each complete orbit is uniquely indexed by (ε,r), ε=sign y and r∈[1,3), with points (0,ε3^n r), n∈Z. For x≠0, choose b=|x|>0 and the positive-x phase of the orbit. Each orbit has a unique index (b,ε,r), r∈[1,P(b)), and all of its states are

\[
 (b,\varepsilon P(b)^n r),\qquad
 (-b,\varepsilon a(b)P(b)^n r),\quad n\in\mathbb Z.           \tag{18}
\]

The half-open fundamental intervals give uniqueness exactly as for multiplicative positive scaling. Formula (16) supplies every predecessor at every depth. In (17) the y-coordinate changes by e^(−c), so \(h+\log|y|\) is invariant under every extension arrow and is a complete real phase within each such source packet. Every height phase remains and translation is free. No Galois transport of these generally nonalgebraic real histories has been used.

## 11. Gate assessment and decision

| Gate / boundary | Evidence | Status |
| --- | --- | --- |
| T0 | Complete atlas, own every-Borel IMAGE, actual lag groupoid and all histories | Established for the conditional inputs and each control |
| T1 clock component | Actual rational derivative products and all-point versions | COMPONENT ONLY; ARITHMETIC T1 NOT PASSED |
| T2 conditional filter | Admitted conjugate packet count, rotation kernel, K_x/F and K_x/Q boundaries | Established under the stated hypotheses, not a universal no-go |
| A / B / C | Three log2 packets / one conjugate-phase log23 core amid adverse full ledger / nonadmitted conjugate boundary | Complete external controls; no candidate promotion |
| T3 / classical / formal / B | No operator or formal evaluation | NOT AUDITED / NOT APPLICABLE / UNASSIGNED / NOT INVOKED |

The geometric, algebraic and domain controls retain adverse data rather than selecting a root or core. A's reciprocal determinant case prevents losing negative signed clocks; B prevents confusing conjugate phases with multiplicity; C prevents silently transporting inequalities. Arithmetic-table shuffles are inapplicable without an admitted arithmetic source. Naturalness and PROVES_TOO_MUCH remain open for a future grammar.
Decision: retain the conditional filter and FORK the portfolio. Apply the multiplicity/field obstruction only after exact conjugate admission and an owned primitive have been checked. No new candidate, enlarged search, discarded real state, field-norm replacement, external roof, operator rescue or additional round is authorized by this paper.

## Reproducibility and evidence

[Frozen card](candidate-card.md), [claim ledger](claim-ledger.md), [package README](README.md), [paper template](../paper-template.md). The proofs are exact rational evaluation, elementary Galois group/field arguments, analytic change of variables, monotone dynamics and complete derivative-product identities. Infinite equations (12)–(14) specify all signed lags and phases, not a numerical census. No effective decision algorithm for arbitrary Borel source pieces or qualifying atlas balls is claimed.
Actual local operations were sed -n, wc -l, sha256sum, scouting rg searches, and read-only author-file ID/Outcome/link/hash checks. Only apply_patch writes the three authorized author files. No scientific code/numerics, network/API/literature campaign, Git, PDF, publication, upload or operator experiment occurred. Root owns the card append, integration and subsequent review/checkpoint decisions; mechanical checks certify neither mathematics nor private reading histories.

## AI assistance, access and ethics disclosure

AI author /root/batch_clock_scope_review supplied the disclosed abandoned and replacement definition scouting, mathematical derivation, drafting and self-checking. Proof-stage scientific reading was the complete frozen 97-line 438 card; the paper template was reread, with previously read local/ARS author instructions retained. Earlier outcome exposures are recorded in §3. No scope/raw/peer or other current manuscript was read.
Named bounded author aid /root/batch_clock_scope_review/ccg_cotangent_probe checked proposal-definition ambiguities through messages only, without files/tools or proofs, and after release supplied only card-based A/C cubic dynamics, inverse IMAGE, all kernels and phases. Its actual receipt reports sed of the full 97-line 438 card through EOF and sha256sum matching §3, with no other files/tools, writes, scientific code, network or agents. It is a shared-history author aid, not a reviewer seat. /root supplied freeze, authorization, integration and separately controlled internal-review coordination; no external verification is certified by those roles.
AI agents supplied mathematical derivation, drafting, self-checking and internal workflow review. Same-model/shared-history work is **NOT_CALIBRATED**, not blind or cross-model validation. **No human or external verification is certified.** Human-authorship contributions, funding, conflicts and institutional endorsements were not supplied and remain unspecified. No human-subject or personal-data research is involved. Venue criteria and publication authority are unavailable (criteria_binding_unavailable); no publication-readiness claim is made.
