# Affine full-torus periodic admission and the nonempty prime-unique ledger gate

**Paper ID:** 403-affine-torus-admission.  
**Candidate ID:** ANG-AUDIT-20260922-ATA01; batch NONLINEAR-RETURN-20260922-K, round 4/5.  
**Date:** 2026-09-22. Conditional architecture audit, not an arithmetic candidate.  
Outcome: `AFFINE PERIODIC ADMISSION ESTABLISHED; NONEMPTY PRIME-UNIQUE LEDGER STOP`
**Route:** classical NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.

## Abstract

An affine torus endomorphism with nonsingular integer linear part has a periodic point exactly when its translation class in the quotient by the image of I minus the linear part is torsion. This criterion is proved without a fixed-centre assumption or a spectral expansion hypothesis. For the separately frozen full-fibre architecture, a nonempty positive primitive ledger cannot simultaneously contain only logarithms of ordinary integer primes and at most one distinct packet per prime. A full finite torsion grid supplies the obstruction only after a fixed point has been established; it is not substituted for the carrier. Exact inverse-sheet IMAGE laws are distinguished from all-sheet Haar transport. Three complete controls illustrate an irrationally shifted doubling map, a rational rotation producing only longer cycles, and an irrational rotation with an empty positive ledger. All kernels, incoming histories, isotropy and height phases retain their actual owners.

## 1. Frozen owner, question and scope

The sole scientific input is the full 74-line [candidate card](candidate-card.md), SHA-256 `798ef503ad37a6204ab611af6ddea3263f10fffb7e426eefe560be2e54e6a380`, read through EOF before proof after root's CP1 release. All mathematics is rederived for this affine class; no result from the linear predecessor or another new manuscript is imported.

Let X be standard Borel, T a deterministic possibly partial Borel map with countably many injective Borel branches and Borel inverses. At each legal x, fix Borel data A(x) in M_n(Z) with nonzero determinant and b(x) in T^n, n>=1. The COMPLETE owner is
\[
Y=X\times\mathbb T^n,\qquad F(x,v)=(Tx,A(x)v+b(x)),\qquad
\tau(x,v)=\log d(x),\quad d(x)=|\det A(x)|.
\tag{1}
\]
All boundaries, terminals and legal histories remain. A terminal has no next step or step clock; the empty iterate has clock zero. Since d is a positive integer, tau is nonnegative, not necessarily positive.

| Ledger row | Exact owner / missing structure |
| --- | --- |
| Geometry and volume | Full flat torus in every fibre, its normalized Haar volume; no base probability or smooth volume on all Y |
| Inverse ownership | Every actual base inverse and ALL fibre solutions, with no selected centre, subgroup or section |
| Clock and extension | Full-fibre local volume Jacobian; actual common-tail cocycle and every real height |
| Periodic packets | Full least source period, complete physical H, multiplicity and repetitions |
| Arithmetic and analytic | No supplied prime-symbolic source, positive suspension, operator or trace owner |
| Controls | S, R and I each own their full torus, Haar measure and geometric clock |

The two questions are periodic admission for an exact affine monodromy, and compatibility of a NONEMPTY positive ledger with prime-only lengths plus uniqueness per prime. Neither a periodicity criterion nor an empty ledger supplies arithmetic admission or prime coverage.

## 2. Every inverse sheet, full IMAGE transport and prefix composition

For one fixed nonsingular integer A and shift b, f(v)=Av+b is onto: a representative of w-b has a real inverse under A. Its fibre solutions are
\[
v=A^{-1}(\widetilde{w-b}+j)\pmod{\mathbb Z^n},\qquad
j\in\mathbb Z^n/A\mathbb Z^n.
\tag{2}
\]
The lattice quotient is finite because det(A) Z^n is contained in A Z^n by the adjugate identity. If its cardinality is N, the union of N coset translates of a fundamental domain for Z^n is a fundamental domain for A Z^n. Comparing its volume N with the covolume |det A| gives N=d=|det A|. Thus (2) contains exactly d points. Fixed half-open representatives and coset representatives give d disjoint Borel inverse sheets, with every cut boundary assigned. Local torus charts have forward derivative A and inverse derivative A^(-1), hence pointwise volume Jacobians d and 1/d at EVERY point. A discontinuous global sheet selection is not asserted to be a single smooth inverse across its cut.

Writing m for the fibre's own Haar measure, change of variables in these flat charts, partitioned along their cuts, gives for every Borel target E and sheet I_j
\[
m(I_jE)=d^{-1}m(E),\qquad m(f^{-1}E)=m(E).
\tag{3}
\]
The first is the inverse-sheet IMAGE law. The second sums ALL sheets and is a preimage/Haar-transport law; it does not set the local clock to zero. On a Borel source C where f is injective, m(fC)=d m(C). For arbitrary C the exact statement is instead
\[
d\,m(C)=\int\#(C\cap f^{-1}\{w\})\,dm(w).
\tag{4}
\]
To prove (4), split C among the disjoint sheets, apply the injective formula and sum their image indicators, preserving multiplicity. Images of different sheets can overlap, so the injective IMAGE formula cannot be applied to arbitrary C. Translations preserve flat volume, establishing the same laws for every b, including irrational shifts.

These are fibrewise assertions only. In the full owner, refine the countable base inverse branches by the countably many possible integer matrices and their finite sheet labels. The formulas above, with Borel representatives for b, give Borel inverses and retain every solution. No measure on X or all of Y is inferred.

For a legal prefix of length k write A_j=A(T^jx), b_j=b(T^jx). Exact composition gives
\[
F^k(x,v)=(T^kx,B_k(x)v+\beta_k(x)),\quad
B_k=A_{k-1}\cdots A_0,\quad
\beta_k=\sum_{j=0}^{k-1}A_{k-1}\cdots A_{j+1}b_j.
\tag{5}
\]
Empty products are I, B_0=I and beta_0=0. The shift sum is well-defined on the torus because every coefficient is integer. Direct composition gives B_(k+l)=B_l(T^kx)B_k(x) and beta_(k+l)=B_l(T^kx)beta_k(x)+beta_l(T^kx). Consequently
\[
Q_k(x)=|\det B_k(x)|=\prod_{j<k}d(T^jx),\qquad
S_k(x,v)=\log Q_k(x).
\tag{6}
\]
Every inverse prefix has exactly Q_k fibre solutions over each chosen base history, with sheet Jacobian 1/Q_k and the corresponding full Borel laws (3)--(4).

## 3. Actual groupoid, full kernels, all isotropy and height phases

Use ALL triples (z,k-l,w) satisfying F^kz=F^lw for valid finite iterates, identifying equal triples but retaining the lag. For z=(x,v), w=(y,u), a witness means BOTH T^kx=T^ly and equality of the two affine expressions (5). Its clock is
\[
c(z,k-l,w)=\log Q_k(x)-\log Q_l(y).
\tag{7}
\]
Two witnesses of the same triple differ by a common padding length. The longer witness guarantees that this padding exists; both clock sums add the same sum from their identical common tail. Thus (7) descends even for partial F. Aligning common middle exponents proves composition additivity, and inverse arrows negate c.

The COMPLETE clock kernel consists of these actual common-tail arrows with Q_k(x)=Q_l(y). The lag kernel consists of those with k=l; their intersection requires both equal lengths and equal determinant products. Lag-zero arrows can connect different points and need not have zero clock when their base histories differ. In particular none of these kernels is silently replaced by a group of local germs or by the units.

For a least base cycle x of length ell, let its exact monodromy (5) be g(v)=Bv+beta and put Q=|det B|. A point of least g-period r gives a full F-cycle of least period ell r: a full return must first return to the base phase, so its length is divisible by ell, and then the remaining condition is precisely a g-return. Distinct g-cycles give distinct full F-cycles. They cannot merge at another phase or through incoming histories, since deterministic periodic cycles with a common future are the same cycle.

At EVERY lifted point eventually entering such a cycle, source isotropy is exactly ell r Z and its clock at lag j ell r is j r log Q; preperiod sums cancel. A point not eventually periodic has trivial source isotropy, including all terminal histories. Hence, on all heights,
\[
H_z=\begin{cases}(r\log Q)\mathbb Z,&\text{eventual cycle as above},\\
\{0\},&\text{not eventually periodic},\end{cases}
\qquad
\operatorname{Iso}_{\rm ext}=\operatorname{Iso}_{\rm source}\cap\ker c.
\tag{8}
\]
Thus extension isotropy is trivial if Q>1, equals ell r Z if Q=1, and is trivial at non-eventually-periodic points. For Q=1 the group H is {0}, not R. All of these statements retain every fibre inverse and base incoming history.

The extension has all (z,h) in Y times R and arrows `(w,h)->(z,h+c)`. Fixing a reference point of a complete source orbit identifies its extension orbit set with R/H: connecting arrows give the height offsets and isotropy gives exactly their ambiguity. Therefore positive primitive time is r log Q when Q>1; its repetitions are j r log Q within that one packet. If H={0}, the physical orbit is R with no positive period. Equal times do not identify different source cycles. A nonzero clock on an arrow between different sources is not itself a physical return.

## 4. Exact affine periodic-admission equivalence

**Theorem 1.** For g(v)=Bv+beta with B nonsingular integer, put K=(I-B)T^n and let pi:T^n->T^n/K. Then g has a periodic point if and only if pi(beta) is torsion.

**Proof.** K is a compact, hence closed, subgroup, so the quotient is defined. Since pi(Bv)=pi(v), iteration gives pi(g^rv)=pi(v)+r pi(beta). A periodic point therefore makes pi(beta) torsion.

Conversely, suppose m pi(beta)=0 for some positive integer m. Choose u with m beta=(I-B)u. Multiplication by m on a torus is onto, so choose a with ma=u. Set t=beta-(I-B)a. Then mt=0, and translation by a conjugates g to v->Bv+t. This conjugate preserves the finite group T^n[m]. Every map of a nonempty finite set has a periodic point, by repetition in a forward sequence. Bijectivity of this particular finite-grid map is unnecessary. Translating back gives a periodic point of g. QED.

This proof covers root-of-unity, unipotent, neutral and nonexpanding directions without a spectral split. It does NOT presume a fixed affine centre: fixed points exist exactly when pi(beta)=0. For full periodic degeneracies, put beta_r=sum_(j=0)^(r-1) B^j beta. Then
\[
\operatorname{Fix}(g^r)=\{v:(I-B^r)v=\beta_r\},\qquad
\operatorname{Per}_r(g)=\operatorname{Fix}(g^r)\setminus
\bigcup_{1\leq j<r}\operatorname{Fix}(g^j).
\tag{9}
\]
Every nonempty fixed set in (9) is one coset of ker(I-B^r). If I-B^r is nonsingular, it has |det(I-B^r)| points by the lattice argument of Section 2. If it is singular, its real nullspace projects locally injectively to a positive-dimensional family in the kernel, so the nonempty fixed set has continuum cardinality. Equations (9) preserve all overlaps and least-period cancellations; they do not assert that every r occurs. Eventual-periodic points are exactly the union of all finite preimages of these exact-period sets.

## 5. Nonempty prime-only and unique-per-prime ledger is impossible

**Theorem 2.** No frozen owner (1) can have a NONEMPTY positive primitive ledger satisfying both: every primitive time is log p for an ordinary integer prime p, and at most one distinct primitive packet occurs for each prime.

**Proof.** Any positive packet comes from an eventual full cycle by (8), hence from a least-r monodromy orbit over a least base cycle. Its time is log(Q^r). For this to equal log p, elementary integer factorization forces Q=p and r=1. Therefore, if both proposed conditions held, a base cycle contributing any positive packet would have prime Q, at least one fixed point of g, no longer g-cycle, and at most one fixed point.

Let a be that established fixed point. Only NOW use the identity g(a+v)=a+Bv. Take the integer d=Q+1. Since gcd(d,det B)=1, the adjugate identity and Bezout's identity make B invertible modulo d. It therefore permutes the finite group T^n[d], which contains nonzero points because n>=1 and d>1. Choose one such point u. Then a+u is periodic under g. If its least period is greater than one, its positive primitive multiplier Q^r is composite. If its least period is one, it is a second fixed point and supplies another packet with the same prime multiplier Q. Both alternatives violate a required condition. These points are witnesses in the FULL fibre, not a replacement of that fibre by a grid. QED.

The case split is exhaustive. Q=1 gives only zero return clocks, regardless of periodicity. Q>1 with no periodic fibre gives no positive packet. Q>1 with any periodic fibre violates prime-only lengths or uniqueness, as proved above. Incoming histories cannot rescue or merge the offending packets. Thus an EMPTY positive ledger can satisfy both conditions vacuously, but nonemptiness cannot. No claim of prime coverage was used, and no claim about nonlinear fibres or geometry-dependent base permission follows.

## 6. Three separate full-carrier controls: transport and complete kernels

Write a=sqrt(2) mod 1, L=log 2 and Delta_2=Z[1/2]/Z. S acts on the full circle by 2x+a; R and I act on the full T2 by `(2x,y+alpha)`, with alpha=1/2 and a respectively. Each owns normalized Haar measure. Their full local forward Jacobian is 2 at every point, so tau=L and c(z,n,w)=nL.

For S use the Haar-preserving coordinate u=h(x)=x+a; then h F_S h^(-1)(u)=2u. Its complete depth-m inverse sheets are `I_(m,j)(w)=(h(w)+j)/2^m-a`, 0<=j<2^m. For R and I they are `I_(m,j)(u,v)=((u+j)/2^m,v-m alpha)`. Targets have fixed half-open representatives. These formulas give every incoming, not a chosen inverse. For each control's OWN measure, every sheet has IMAGE `m(I_(m,j)E)=2^(-m)m(E)` for every Borel E, all sheets give `m(F^(-m)E)=m(E)`, and arbitrary source C obeys the multiplicity formula (4) with degree 2^m. Their all-point local Jacobians come from the displayed affine maps, including all chart-boundary points.

For n_+=max(n,0), n_-=max(-n,0), the FULL actual arrows are exactly
\[
(z,n,w)\in G_S\iff 2^{n_+}h(z)-2^{n_-}h(w)\in\Delta_2,
\]
\[
((x,y),n,(x',y'))\in G_\alpha\iff
y'=y+n\alpha\pmod1\ \text{and}\ 
2^{n_+}x-2^{n_-}x'\in\Delta_2.
\tag{10}
\]
Indeed witnesses are k=m+n_+, l=m+n_-, and the dyadic condition is exactly annihilation of the remaining horizontal difference by some 2^m. Since c=nL, clock kernel, lag kernel and their intersection coincide: for S they are all `(z,0,w)` with z-w in Delta_2; for R/I they are all `((x,y),0,(x',y))` with x-x' in Delta_2. These include nonunit merger arrows, but their intersection with source isotropy is always units. Thus extension isotropy is trivial everywhere for all three controls.

## 7. Complete control periods, multiplicities, incoming and phases

**S.** The exact iterate is F_S^m(x)=2^m(x+a)-a. A point is eventually periodic exactly when u=h(x) is rational modulo 1: an eventual equality forces `2^m(2^r-1)u=0`, and a rational denominator loses its power of 2 under iteration before entering a finite odd-denominator permutation. If the reduced denominator is 2^e d with d odd, its preperiod is e and its eventual least period is q=ord_d(2), with ord_1(2)=1. Actual periodicity means e=0. Equivalently least q means `(2^q-1)u=0` and `(2^j-1)u!=0` for all 1<=j<q.

At every such eventually periodic point source isotropy is qZ and entire H=qL Z; otherwise both are trivial. Extension isotropy is trivial everywhere. The full fixed set is {-a}; the exact-two set is {1/3-a,2/3-a}, one source cycle and one primitive log-4 packet. All primitive packets are exactly the least-q doubling cycles transported by h^(-1), with time qL. This predicate classifies every packet; every q occurs, since 1/(2^q-1) has least period q (for q=1 this is zero modulo 1). Thus the unique log-2 packet does not prevent composite primitive multipliers. Each packet retains all incoming sheets, all source phases and R/(qL Z); its repetitions are j qL. Non-eventually-periodic source orbits give physical R.

**R.** F_R^m(x,y)=(2^m x,y+m/2). Eventual periodicity is exactly x rational modulo 1, with arbitrary y. For denominator 2^e d, d odd, its preperiod is e and eventual least period q=lcm(ord_d(2),2); actual periodicity means e=0. This follows because a return requires both the doubling congruence and an even number of half-turns. Source isotropy is qZ and H=qL Z at every eventual-periodic point, and both are trivial otherwise; extension isotropy remains trivial everywhere.

There are NO fixed points. The entire exact-two set is `{0,1/3,2/3} times T`. Its two-cycle packets are indexed by `(T/<1/2>) disjoint union T`: the first family has x=0; the second has the unique x=1/3 representative of a cycle exchanging 1/3 and 2/3. Both retain all other phases. More generally the exact-q set is all odd-denominator x with `lcm(ord_d(2),2)=q`, times the whole circle; primitive packets are precisely its quotient by actual F_R cycles. Every possible q is even, and every even q occurs with continuum-many distinct packets, using a least-q doubling cycle and arbitrary y. All their multipliers 2^q are composite. Full incoming sheets preserve the same H, all real phases are R/(qL Z), and repetitions remain attached to the same packet. Irrational x gives physical R orbits, not positive packets.

**I.** F_I^m(x,y)=(2^m x,y+ma). Any eventual return of length q>0 would require q sqrt(2) to be an integer, impossible. Thus EVERY point is non-eventually-periodic; fixed and exact-two sets are empty. Source and extension isotropy are trivial and H={0} at every point and every height. All inverse sheets and the nonunit kernels (10) remain; nonzero-lag arrows between different sources do not become physical returns. Every physical orbit is R, and the positive ledger is EMPTY. It satisfies the two tested conditions only vacuously, without prime coverage.

For the admission test, S has trivial quotient by (I-2)T and a genuine fixed centre. For R/I, the quotient is exactly the second-coordinate circle: the translation class is respectively the nonzero torsion element 1/2 and the nontorsion element a. These independently owned controls therefore distinguish periodic admission without a fixed centre from no periodic admission. All three are onto, globally defined and exactly two-to-one; no terminal or inverse branch is omitted.

## 8. Gate assessment, limits and decision

| Gate / control | Exact disposition |
| --- | --- |
| Conditional T0 | Full affine fibres, every inverse sheet and actual histories have one explicit owner |
| Conditional T1 | Geometric determinant clock and exact affine-prefix composition established; arithmetic naturalness NOT ESTABLISHED |
| Conditional T2 | Torsion quotient criterion proved; nonempty prime-only unique-packet ledger impossible in the frozen class |
| S / R / I | Shifted doubling has a composite primitive; rational rotation delays returns; irrational rotation leaves the positive ledger empty |
| Robustness / PROVES_TOO_MUCH | Exact all-point and full Borel laws, no cutoff; assigned coefficients and selected subsets supply no arithmetic admission |
| Formal / analytic | Classical NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; Route B NOT INVOKED |

**Decision: STOP the nonempty prime-unique ledger claim for this full affine-fibre architecture; retain the exact periodic-admission criterion.** This is not inherited credit from the linear case. It neither admits a concrete prime-symbolic source nor rules out nonlinear fibres, geometry-dependent permission or other freshly frozen owners. Empty positive ledgers and Q=1 degeneracies remain visible rather than being labelled successful prime coverage. No novelty, operator or RH claim follows.

## Reproducibility, exposure and disclosure

The [claim ledger](claim-ledger.md) and [overview](README.md) index these exact proofs. Methods are flat change of variables, lattice index, affine composition, finite torsion grids and exact least-period predicates. There are no scientific numerical runs, precision/cutoff choices, prime tables, fitted roofs, zero data, external references, PDFs, Git mutations or publication actions. Mechanical hash, line, identity/Outcome and relative-link checks concern files, not theorem validity.

The author read the card and current instructions through EOF, retained shared research context, and read no other new main/raw/peer material. The actual author-helper access receipts are:

| Agent identity | Bounded task | Reported actual access |
| --- | --- | --- |
| `/root/batch_clock_scope_review/ccg_cotangent_probe` | Derive S/R/I transport, periods, kernels, isotropy, incoming and phases | Read the full 74-line 403 card and verified the frozen hash above; no other paper file, reviewer material, numerical experiment, network or write |
| `/root/batch_clock_scope_review/hch_exact_series` | Derive the torsion-quotient admission criterion and finite-grid packet obstruction | Newly read only the full 403 card with sed and verified its hash with sha256sum; no other new file, reviewer material, network, numerical work or write |
| `/root/batch_clock_scope_review/hch_exact_series/affine_packet_lemma` | Derive the multiple-fixed-or-higher-period lemma and prime-length/multiplicity consequence | Fresh task with fork_turns=none; received only its parent's explicit mathematical statement; no tool calls or file reads, including no card, manuscript, raw or reviewer material |

These are author-side mathematical assistants, not independent reviewers. Internal work is shared-history NOT_CALIBRATED. ARS bounded claim/evidence discipline is used; criteria_binding_unavailable and no venue-readiness assertion. Root owns card integration and CP2/CP3.

**AI-use disclosure:** AI agents supplied the mathematical derivation, drafting and author-side internal checking; the separate internal-review workflow is likewise AI-assisted. No human or external verification is certified.

Data availability: all inputs and exact methods are stated. Ethics: no human/animal subjects or personal data. Contributions: AI-assisted analysis and writing without assigning human authorship. Funding/conflicts: no declarations supplied, not presumed absent. This is round 4/5 of the authorized batch, not permission for a further batch.
