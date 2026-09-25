# Hard coprime histories: an owned conditional clock with a wrong primitive

**Paper ID:** 374-hard-coprime-history-control.  
**Candidate:** ANG-CONTROL-20260922-HCH01; batch MEASURED-HISTORY-20260922-E, round 5/5.  
**Date / status:** 2026-09-22; EXACT OWNER THEOREMS; PRECOMMITTED PRIMITIVE TARGET FAIL; STOP.  
**Route:** classical A0/A1/A2 NOT APPLICABLE; T3 NOT AUDITED; formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

The full nearest-neighbor coprime shift carries the frozen reversible Markov probability and its actual inverse-image law, including every null periodic history. Their continuous cylinder version defines an additive clock on actual lag triples, not a supplied word roof. This paper determines all inverse branches, clock and lag kernels, source and extension isotropy, incoming histories and physical stabilizers. The entire packet of the alternating word 23 has least physical time strictly between log 2 and log 3, so it cannot meet the frozen prime-log target. Three separately owned controls distinguish admission, degeneracy and measure dependence. The results concern an orbit set with height translation; no smooth flow, separated quotient, invariant flow measure or trace object is asserted.

## 1. Identity, question and frozen ownership

The original 88-line frozen prefix of the [candidate card](candidate-card.md) has SHA-256 d970a8ed78a30f2bd70323c88b322ecdfe7d4b5abdd5b2490d029e4fb82755bd; later appended outcome text is not part of that input hash. Root released mathematics after the [CP1 scope review](evidence/scope-review.md). The question is whether its own full-point conditional clock gives the precommitted packet a least time log p, without discarding legal words, incoming states or heights.

| Item | Owner and boundary |
| --- | --- |
| Arithmetic lineage | Common-divisor witness exclusion -> adjacent hard admission -> full histories with an owned reversible conditional law |
| MAIN source | All admissible histories on A={2,3,...}, their shift T and the frozen rho-Markov probability |
| Inverses and IMAGE | Every legal prefix insertion; density proved for every Borel set, with one specified continuous all-point version |
| Clock | Negative logarithm of that inverse transport, on actual triples retaining integer lag |
| Physical action | All X times R, modulo the clock extension; height translation on the orbit SET |
| Packets | Primitive cyclic words, all legal incoming prefixes, all source phases, all height phases and repetitions |
| Controls | UNCONSTRAINED, FINITE-TWO and GEOMETRIC-LAW, each with its own full measure and clock |
| Unavailable owners | Classical symplectic/contact/Hamiltonian/quantum geometry NOT SUPPLIED; analytic T3 NOT AUDITED |

This is expressly a nearest-neighbor / Markov boundary CONTROL, not an infinite-memory construction. The lineage statement in the card identifies a local deformation, not an equivalence to the full-history sources of 367/371; no result or external log-symbol roof from 065 is used. Strong arithmetic naturalness and all-prime coverage are not inferred.

## 2. The complete probability source

Write a~b for gcd(a,b)=1. For MAIN let q(a)=rho(a)=1/[a(a-1)]. For the separately frozen GEOMETRIC-LAW let q(a)=rho_G(a)=2^(1-a). Both are strictly positive probabilities on A, by telescoping and geometric summation respectively. In this section and Sections 3--6, q denotes either separately instantiated law, never a mixture or a replacement of MAIN.

Define
\[
Z_q(a)=\sum_{b\sim a}q(b),\quad C_q=\sum_a q(a)Z_q(a),\quad
\pi_q(a)=q(a)Z_q(a)/C_q,\quad P_q(a,b)=q(b)\mathbf1_{a\sim b}/Z_q(a).
\]

**Proposition 1 (probability and topology).** Every denominator is positive and finite; pi_q is stationary and reversible for P_q. The allowed-cylinder prescription defines a unique full-support, nonatomic probability mu_q on
\[
X=\{x\in A^{\mathbb N_0}:x_i\sim x_{i+1}\ \hbox{for every }i\},
\]
and T is a surjective, measure-preserving left shift.

**Proof.** The legal neighbor a+1 gives Z_q(a)>0, while the forbidden self-neighbor a gives Z_q(a)<=1-q(a)<1. Consequently 0<C_q<1 and all row sums and the pi_q sum equal one. Directly,
\[
\pi_q(a)P_q(a,b)=q(a)q(b)\mathbf1_{a\sim b}/C_q
=\pi_q(b)P_q(b,a).
\]
Summing in a proves stationarity. The finite-dimensional masses
pi_q(x_0) times the product of the successive P_q transitions are consistent under summing the last symbol, hence define the countable-coordinate probability. Equivalently, independent uniform coordinates, partitioned initially by pi_q and subsequently by the relevant row of P_q, construct this measure. Forbidden pairs have probability zero; their countable union has probability zero, so the resulting probability is carried by X. Cylinder agreement determines uniqueness. Summing the first symbol, using stationarity, proves shift invariance on cylinders and then on all Borel sets.

The product of the countable discrete alphabets is metrizable with cylinder basis; X is closed because a forbidden adjacent pair is an open condition. Every nonempty allowed cylinder has positive mass and extends indefinitely by alternation between its last symbol and that symbol plus one. Thus support is all X. Every tail y has the legal predecessor y_0+1, proving surjectivity.

Each state a has at least two distinct legal neighbors a+1 and 2a+1. Hence every allowed P_q(a,b) is strictly less than one. To exclude point atoms without assuming a uniform transition bound, suppose mu_q({x})=delta>0. Shift invariance gives mu_q({T^j x})>=delta for every j. There can be only finitely many distinct such points, so the path is eventually periodic. For its periodic tail v, the product of transitions around a least period is strictly less than one; the masses of successively longer cylinders about v therefore tend to zero. Thus mu_q({v})=0, contradicting mu_q({v})>=delta. Any Borel atom in this countable-coordinate space would select a unique full-mass cell at each successive coordinate, leaving a singleton of the same mass. There are no such singletons, so the probability is nonatomic, including on every periodic and eventually periodic history. QED.

## 3. Every inverse branch and every-Borel IMAGE

For a in A put E_a={y in X:a~y_0}. The insertion I_a(y)=ay is a homeomorphism E_a->[a], where E_a and [a] are clopen in X. The restrictions T:[a]->E_a are its inverses. Every preimage of y begins with exactly one legal a, so this lists all inverse branches.

For a finite word u=(u_0,...,u_(m-1)), including the empty word, let D_u be all tails t such that ut is admissible, and I_u(t)=ut. An internally illegal word has empty domain. A nonempty legal word has domain E_(u_(m-1)); the empty word has domain X. All finite compositions are exactly these I_u; no recurrent subsystem or preferred prefix is selected.

**Proposition 2 (actual transport).** For every Borel B contained in E_a,
\[
\mu_q(I_aB)=\int_B j_{q,a}(y)\,d\mu_q(y),\qquad
j_{q,a}(y)=P_q(y_0,a).
\tag{1}
\]
More generally, for every Borel B contained in D_u,
\[
\mu_q(I_uB)=\int_B J_{q,u}(t)\,d\mu_q(t),\qquad
J_{q,u}(t)=\prod_{i=0}^{m-1}P_q(s_{i+1},s_i),\quad s=ut.
\tag{2}
\]
Empty products equal one. These versions are positive, finite and locally constant on their entire domains, and are uniquely determined among continuous versions there.

**Proof.** For a tail cylinder beginning b_0,...,b_l, divide the mass of its a-prefixed cylinder by its mass. The ratio is pi_q(a)P_q(a,b_0)/pi_q(b_0)=P_q(b_0,a), by detailed balance. Both sides of (1) are finite measures of B, agree on the cylinder generating class in E_a, and thus agree on every Borel B. Images are Borel because I_a is a homeomorphism onto [a]. Repeating this argument, or telescoping detailed balance along u, gives (2); the ratio is the product of the reverse transitions, not an assumed forward-arrow roof.

Each density depends only on the first tail symbol. If two continuous versions agreeing almost everywhere differed at any tail, continuity would give a relatively open set on which they differ. Full support gives that set positive measure, a contradiction. Thus the cylinder law and continuity select the stated value even at each null periodic history; an arbitrary measurable null-set alteration is not this frozen version. QED.

## 4. The actual lag owner, cocycle and full kernels

Retain exactly the triples
\[
G=\{(z,\ell,y):\ell=m-n,\ m,n\geq0,\ T^m z=T^n y\}.
\]
Source is y, range is z. Only equal triples are identified. Multiplication is (z,l,y)(y,k,x)=(z,l+k,x), inverse is (y,-l,z), and units are (x,0,x). Repeated witnesses do not create extra arrows, while nonzero lag with equal endpoints remains a distinct arrow.

Set kappa_q(x)=-log P_q(x_1,x_0), A_(q,m)(x)=sum_(i<m)kappa_q(T^i x), and A_(q,0)=0. Each kappa_q is finite, strictly positive and locally constant. Define
\[
c_q(z,m-n,y)=A_{q,m}(z)-A_{q,n}(y).
\tag{3}
\]

**Proposition 3 (descent and all finite histories).** Formula (3) is independent of its witnesses, reverses sign on inverses and is additive under composition.

**Proof.** Two witness pairs for the same lag differ by adding the same integer to m and n. For nonnegative addition, the extra A-sums follow the identical common tail and cancel; negative addition follows by reversing that comparison. For composition, pad the middle exponents to the larger of them. The same middle A-sum then cancels, giving (3) for the composite. Units and inverses follow directly.

On a prefix-replacement branch I_v(t)->I_u(t), equation (2) gives the every-Borel image density J_(q,u)(t)/J_(q,v)(t)=exp(-c_q). Indeed integrate this ratio against J_(q,v) dmu_q on the common tail domain. Thus every finite-history cocycle value comes from the actual transport. No extra normalization or a different measure is introduced. QED.

For an explicit exhaustive kernel test, write
\[
W_q(u;t)=J_{q,u}(t)^{-1}
=\prod_{i<m}\frac{Z_q(s_{i+1})}{q(s_i)},\qquad W_q(\varnothing;t)=1.
\]
Every actual arrow has a representation (ut,|u|-|v|,vt), with both insertions legal. Its complete kernels are
\[
\begin{aligned}
\ker c_q&=\{(ut,|u|-|v|,vt):W_q(u;t)=W_q(v;t)\},\\
\ker\ell&=\{(ut,0,vt):|u|=|v|\},\\
\ker c_q\cap\ker\ell&=\{(ut,0,vt):|u|=|v|,\ W_q(u;t)=W_q(v;t)\}.
\end{aligned}
\tag{4}
\]
These are equality conditions on explicit finite products, not tests restricted to periodic points. All witnesses are included and identical triples are counted once. To make the cancellation test independent of the common tail value, pad both words so they are nonempty, put D_q(a)=Z_q(a)/q(a), and let N_a(u) count occurrences of a in u. Then
\[
\exp c_q=\frac{Z_q(v_0)}{Z_q(u_0)}
\prod_{a\geq2}D_q(a)^{N_a(u)-N_a(v)},\qquad
\ell=\sum_a(N_a(u)-N_a(v)).
\tag{5}
\]
Only finitely many factors differ from one. Telescoping the Z factors proves (5), and common padding changes neither expression. Equations (4)--(5) determine membership on every arrow exactly; no independence assumption about the logarithms is made.

The kernels need not be unit arrows. For example, prefixes (2,3,5,2) and (2,5,3,2), with common tail beginning 3, are distinct, admissible and have the same initial symbol and symbol counts. Their replacement is in the intersection in (4). Conversely, prefixes 2 and 5 with common tail beginning 3 have lag zero but weight ratio q(5)/q(2), which is not one for either law. Positivity on a single insertion does not justify ignoring such replacement cancellations.

## 5. Entire isotropy, heights, incoming states and repetitions

**Proposition 4 (full packet ledger).** If x is not eventually periodic, its source isotropy is trivial. If its eventual tail has least period d, source isotropy is exactly {(x,kd,x):k in Z}. Let w be that primitive cyclic word and put
\[
L_q(w)=-\sum_{i=0}^{d-1}\log P_q(w_{i+1},w_i)
=\log\prod_{i=0}^{d-1}\frac{Z_q(w_i)}{q(w_i)}>0,\qquad w_d=w_0.
\tag{6}
\]
On this isotropy, c_q(x,kd,x)=kL_q(w).

**Proof.** A nonzero isotropy lag means two different shifts of x coincide, exactly eventual periodicity. On an eventual least-d tail, every equality of shifts has lag divisible by d, and every multiple is realized by taking shifts after the finite preperiod. The difference of A-sums is k complete cycle sums; preperiod terms cancel. Each reverse transition is strictly less than one, so (6) is positive. QED.

The extension has every unit (x,h) in X times R and arrows
(y,h)->(z,h+c_q(z,l,y)). Its isotropy at (x,h) consists of the source isotropy arrows with c_q=0. Proposition 4 shows that the ENTIRE extension is isotropy-free for MAIN and GEOMETRIC-LAW, including all null periodic states. This does not imply that physical time is free on the orbit set.

On Q_q=(X times R)/G let physical time act by [x,h]->[x,h+t]. The action is well-defined because height translation commutes with every extension arrow. Its full stabilizer is
\[
H_x=\{t:[x,h+t]=[x,h]\}
=c_q(G_x^x)
=\begin{cases}\{0\},&x\text{ not eventually periodic},\\
L_q(w)\mathbb Z,&x\text{ eventually periodic with primitive word }w.
\end{cases}
\tag{7}
\]
The equality uses an arrow with both source and range x, not an arbitrary incoming arrow. It is independent of h.

For every x its entire source orbit is
\[
\mathcal O(x)=\{uT^n x:n\geq0,\ u\text{ any finite word whose concatenation is legal}\}.
\tag{8}
\]
This follows in both directions from the witnesses T^m z=T^n x. Choosing any connecting arrow from x to z identifies the height over z with h+c_q of that arrow; two choices differ by precisely H_x. Thus the entire part (O(x) times R)/G is, as a set with physical action, R/H_x. Incoming prefixes change the height offset, not H_x, and are all retained. No quotient topology or invariant measure on Q_q is claimed.

A cyclic word is admissible exactly when every successive pair, including the closing pair, is coprime. Its primitive version is its shortest period, not its written length. No constant word is admissible, since gcd(a,a)=a>1. Each primitive admissible necklace, modulo cyclic rotation only, gives one periodic physical packet with all its incoming histories and all height phases. Distinct necklaces have distinct source orbits; orientation reversal is not separately identified unless already a cyclic rotation. A word w repeated r times has written length rd and clock rL_q(w), but belongs to the same packet with least positive time L_q(w). Non-eventually periodic histories yield free R-orbits. This is the full classification without a high-period enumeration.

## 6. The precommitted MAIN packet and exact obstruction

The history x=(23)^infinity is legal and has least source period 2. Its entire source orbit is the set (8), equivalently every legal finite prefix followed by either alternating phase. Proposition 4 gives all source isotropy 2Z, trivial extension isotropy, and
\[
H_x=L\mathbb Z,\qquad L=\log Q,\qquad Q=12Z(2)Z(3).
\tag{9}
\]
Every real height is included; the physical packet is one R/LZ with these incoming states, not two selected phase packets.

**Proposition 5 (wrong primitive, exact bounds).** The least time satisfies log 2<L<log 3.

**Proof.** Directly from rho,
\[
Z(2)=\sum_{k\geq1}\frac1{2k(2k+1)}>\frac14\sum_{k\geq1}\frac1{k(k+1)}=\frac14.
\]
For k>=4 bound the summand strictly above by 1/[(2k-1)(2k+1)], whose tail telescopes to 1/14. Consequently
\[
Z(2)<\frac16+\frac1{20}+\frac1{42}+\frac1{14}
=\frac{131}{420}<\frac5{16}.
\]
The excluded mass for Z(3) is S=sum_(k>=1)1/[3k(3k-1)]. Since 3k-1>=k+1, strictly for k>=2, S<(1/3)sum1/[k(k+1)]=1/3. On the other hand S>1/6+1/30+1/72=77/360>1/5. Therefore 2/3<Z(3)<4/5. Combining positive inequalities gives
\[
2=12(1/4)(2/3)<Q<12(5/16)(4/5)=3.
\]
The logarithm is strictly increasing, proving the claim. QED.

There is no prime between 2 and 3. Hence this packet has no least time log p in the frozen normalization. Using a repeated traversal, omitting incoming histories, selecting one height or multiplying the clock would not change the proved least time of this frozen packet. Promotion stops here; no all-prime coverage claim or general census is needed to obtain this scoped failure.

## 7. Three separately owned adverse controls

**UNCONSTRAINED.** The source is all A^N0, with its own product measure rho and T. Each row is P_U(a,b)=rho(b), pi_U=rho. Cylinder consistency and summing the first symbol give its probability and invariance; every cylinder is positive and every singleton has mass at most (1/2)^n along length-n cylinders, so the source is nonatomic. All inverse domains are X_U. Direct cylinder ratios give every-Borel IMAGE j_(U,a)=rho(a), uniquely continuous on the full domain. For every finite prefix,
\[
J_U(u)=\prod_{i<|u|}\rho(u_i),\quad W_U(u)=\prod_{i<|u|}u_i(u_i-1),\quad
c_U(ut,|u|-|v|,vt)=\log[W_U(u)/W_U(v)].
\]
Its full clock kernel is equality of these integer products, its lag kernel is equal prefix length, and their intersection imposes both. For example 4 and 23 have equal product 12 but different lengths; prefixes 23 and 32 give a nonunit zero-lag, zero-clock arrow. The same common-tail cancellation proves descent and composition for this own measure. Source isotropy is dZ on each eventual primitive-d word and trivial otherwise; its clock image is L_U(w)Z with L_U(w)=sum log[w_i(w_i-1)]>0. Extension isotropy is trivial everywhere. Formula (8), with every prefix allowed, retains all incoming histories; heights form R/H, with H=L_U(w)Z or {0}. All primitive words, including constants, are admissible. Constants a have least time log[a(a-1)]; the entire 23 packet has least time log 12. Cyclic phases and r repetitions obey the same explicitly derived rL_U law. None of these source words or times is transferred to MAIN.

**FINITE-TWO.** The only histories are x=(23)^infinity and Tx=(32)^infinity. The stationary measure gives each mass 1/2; both are atoms and constitute full support. T interchanges them. I_2 is defined solely on the phase beginning 3, and I_3 solely on the phase beginning 2. Every legal branch and finite composition preserves the mass of its singleton domain, so its own every-Borel IMAGE is identically one. Thus kappa_F=A_F=c_F=0 on all actual arrows. Precisely, G_F consists of (z,l,y) with z=T^l y (parity determines the endpoint); ker c_F=G_F, ker lag consists only of units, and their intersection consists only of units. Source isotropy and extension isotropy at every height are both 2Z, not discarded copies of the identity arrow. The entire source orbit has both phases; legal prefixes add no other histories. The orbit set is R with all heights retained, H_F={0}, and physical height translation has no positive period. The primitive source word 23 has source repeats 2r and clock repeats zero; these are not closed physical-time repetitions. This control's deterministic clock degeneracy is not MAIN's nonatomic positive clock.

**GEOMETRIC-LAW.** Instantiate Sections 2--5 with q(a)=2^(1-a), its own Z_G,C_G,pi_G,P_G and mu_G. Those proofs directly establish its normalized reversible probability, full support and nonatoms, every legal inverse domain, every-Borel IMAGE P_G(y_0,a), continuous values on all null histories, finite-history products and cocycle. Its complete kernels are (4)--(5) with those G quantities; source isotropy is dZ on eventual primitive-d tails, extension isotropy is trivial, and H_G=L_G(w)Z with the exact (6) using G quantities, or {0} on non-eventual tails. Every admissible necklace, incoming prefix, cyclic phase, real height and repeated traversal is retained.

For its entire 23 packet,
\[
Z_G(2)=\sum_{k\geq1}2^{-2k}=\frac13,\quad
Z_G(3)=1-\sum_{k\geq1}2^{1-3k}=\frac57,\quad
L_G(23)=\log\frac{Z_G(2)Z_G(3)}{\rho_G(2)\rho_G(3)}
=\log\frac{40}{21}.
\]
Therefore 0<L_G(23)<log 2. Its full H is this L_G times Z, with source isotropy 2Z and trivial extension isotropy, for both phases and all legal incoming histories. This second wrong primitive is a measure-dependence control, not an optimized replacement.

## 8. Gate assessment, limitations and final-round decision

| Obligation | Evidence | Scoped assessment |
| --- | --- | --- |
| T0 | Propositions 1--3; actual triples and all-Borel inverse transport | Full stated measured owner established |
| T1 | Genuine hard coprime admission and own conditional law; all-point clock | Operational ownership established; strong naturalness OPEN |
| T2 | Entire kernels, isotropy, H, incoming states, necklaces and repetitions | Exact full ledger; frozen least-prime-time target FAIL by Proposition 5 |
| T3 | No operator, trace, determinant or analytic target audit attempted | NOT AUDITED |
| Classical / formal Route | No classical geometric owner or formal evaluation | A0/A1/A2 NOT APPLICABLE; coordinates UNASSIGNED; B NOT INVOKED |

The local coprime rule retains only adjacent witness information. Keeping all infinite histories does not change its nearest-neighbor conditional memory. It is not evidence of an infinite-memory mechanism or escape from Markov splicing. All results are exact for the frozen law; no numerical search, finite cutoff, floating-point estimate, prime table, supplied prime time or parameter tuning entered the argument. General multiplicative relations among the Z-values are neither presumed nor needed: the exhaustive finite-product kernel criteria retain every possible equality.

**Decision: STOP.** Preserve the measured-source, IMAGE and packet theorems as boundary-control results; do not promote this owner after its precommitted wrong primitive. The same-object ledger remains intact. This completes the fifth round's author-side scientific obligations; the batch handoff must await the user after integration and review, with no sixth round authorized here.

## Reproducibility and disclosures

All inputs are the [frozen card](candidate-card.md); release provenance is the [CP1 scope review](evidence/scope-review.md). Proofs above provide the complete derivation and exact inequalities; there is no scientific program, dataset, external literature campaign or publication artifact. The author read the full original 88-line card, 75-line CP1 and repository template; no 374 raw or peer derivation was read. An isolated author-side helper checked the exact series bounds and a nonatomicity argument, with a bounded child derivation on nonatomicity; these were author-side assistance, not independent review. This is shared-history model-assisted research, NOT_CALIBRATED and not external peer review; criteria_binding_unavailable, with no venue alignment or readiness claim.

Data availability: every mathematical input and method is in this package. Ethics: no human or animal subjects or personal data. Author contributions (CRediT): AI-assisted formal analysis and writing are disclosed; human authorship and allocations are not assigned here. Conflicts of interest and funding: no declarations supplied, so neither absence of conflicts nor funding status is asserted. No external upload, model change, Git operation or publication was performed by this author task.
