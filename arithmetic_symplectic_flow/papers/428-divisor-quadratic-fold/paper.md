# Divisor quadratic folding: an owned composite primitive in the frozen four-cell gate

Paper ID: `428-divisor-quadratic-fold`.
Candidate ID: `ANG-20260923-DQF01`.
Date: 2026-09-23. Status: exact owner construction and negative target result.
Outcome: `OWNED FOLD CLOCK; COMPOSITE PRIMITIVE — STOP / FORK`
Portfolio: **STOP / FORK**. Batch `SYMMETRY-FEEDBACK-20260923-P`, round 4/5.
Arithmetic T1 NOT PASSED; classical A0–A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.

## Abstract

The frozen partial map on full Lebesgue three-space couples a floor-based divisor test to all three components of a quadratic fold. Its regular polynomial germs give countably many actual inverse branches, every-Borel IMAGE identities, and an explicitly fixed all-point signed clock. The complete four-cell fixed-point gate contains exactly two MAIN cores, with entire clock groups log(2)Z and log(27)Z. The latter owns a composite primitive, not a repetition of a log(3) orbit. Removing arithmetic permission retains this obstruction; removing quotient feedback instead retains two distinct log(2) packets. Full incoming, source and extension isotropy, all phases, and all kernels are kept. These exact counterexamples stop the necessary prime target without a higher-period census, an imported roof, or a claim about other architectures.

## 1. Candidate identity and same-object ledger

| Item | Frozen owner and status |
| --- | --- |
| Carrier and measure | Full X=R³, Borel structure, Lebesgue³; terminals retained |
| Actual map | MAIN partial divisor quadratic fold below; not a symplectic map |
| Arithmetic source | Current floors A,B,C; N=A²+C; signed divisibility and quotient |
| Inverses and clock | All regular actual polynomial roots; specified germ IMAGE; κ=log of absolute forward determinant |
| Physical construction | Actual lag groupoid on X and its additive action on all X×R; set-level height-translation quotient |
| Packets and repetitions | Full source orbit, entire H, least positive generator when nonzero; multiplicity retained |
| Controls | G permission-OFF and Q quotient-feedback-OFF, each on its own full X and measure |
| Classical roof/lift | Positive roof, symplectic form, suspension manifold, Hamiltonian/contact/quantum lift NOT APPLICABLE / not constructed |
| Analytic owner | No transfer operator, trace, zeta or Fredholm determinant; T3 NOT AUDITED |

All determinants below are finite-dimensional derivatives of this owner's actual polynomial germs, not dynamical or operator determinants. Signed and zero increments are permitted; no positive suspension is inferred.

## 2. Question and strongest claim

The necessary target is a nonempty positive packet ledger supported on logarithms of ordinary primes, with at most one packet at each prime. All-prime coverage is additional. We prove MAIN fails prime support: one full actual packet has primitive log(27). This is a global counterexample to that necessary condition, not a global classification of all cycles. The frozen four-cell classification, inverse construction and packet formulas are exact; strong naturalness and unexamined dynamics remain open.

No zero data, prime tables, manually assigned prime roofs, per-prime parameters, arbitrary rescaling, or selected inverse roots enter the result. No formal Route coordinate, universal fold no-go, novelty theorem, or inherited proof credit is asserted.

## 3. Definitions, arithmetic interface and provenance

Write v=(x,y,z), A=⌊x⌋, B=⌊y⌋, C=⌊z⌋, N=A²+C. For every integer q put

\[
 P_q(v)=(yz-qx,zx-qy,xy-qz),\qquad
 \Delta_q(v)=\det DP_q(v)=-q^3+q(x^2+y^2+z^2)+2xyz.                 \tag{1}
\]

Indeed DP_q has diagonal −q and off-diagonal entries z,y,x, whose direct determinant expansion gives (1).
MAIN is defined exactly when B≠0, B divides N, q=N/B, and Δ_q(v)≠0; then Tv=P_q(v).
G uses r=N mod |B|, 0≤r<|B| and q_G=(N−r)/B when B≠0, and q_G=0 when B=0; only Δ_(q_G)≠0 is required.
Q retains MAIN's arithmetic permission but uses P_0 and requires Δ_0=2xyz≠0. It does not retain the unused test Δ_(N/B)≠0.
All three are Borel partial deterministic maps on full X. A failed source has no next step or next-step κ: these are NOT DEFINED, not zero or absorbing dynamics. Identities and every actual incoming arrow remain.

On every full cell with floors (A,B,C)=(0,d,n), n≥2 and 1<d<n, N=n and MAIN arithmetic permission is exactly d|n. This is a genuine proper-divisor symbolic observable; geometric regularity is a separate test. The quotient enters every actual output coordinate, whose new floors feed the next test. The lineage is divisor admissibility → simultaneous geometric deformation. The choice A²+C, fold, measure and critical termination are design inputs, not consequences of a prime-recurrence theorem.

The authoritative [card](candidate-card.md), original 99 lines, was read to EOF after proof release; SHA-256 `2e9f6f1bf43f2984aaf4d10f9a9be56c38b9414e0009ec15980387dd7347cfa0`.
The design scout had read full cards 319 (212 lines, `e3f758ccba332ff40d9782458c5798bdc57aeeb8406fa2efce6e9be2fe03f768`) and 421 (112 lines, `07de79d19fc96b8c468ecb55ac4c0f8225f32d64f987bb30a2fc2aed51a1d56c`); no old proof is imported. Registry summaries and shared author history were exposed. Informal fixed-point/sign expectations influenced the four cells: this is not blind or sealed preregistration.

## 4. All-point actual inverse atlas and IMAGE

For MAIN or G let E_q be its own legal source set with its uniquely determined geometric coefficient q. For Q use one set E_0 consisting of all its legal sources, irrespective of the unused arithmetic quotient. These are Borel, disjoint within each owner, and partition its legal domain.
Fix the card's rational-ball enumeration. For q keep precisely balls U_(q,i) on which P_q is injective and Δ_q never vanishes, preserving the enumeration order. Every regular point belongs to one: the inverse function theorem gives an open injectivity neighborhood, inside which a rational ball can contain that point. No effective algorithm for deciding qualifying balls is claimed.
Define the actual branch sources

\[
 V_{q,i}=E_q\cap\bigl(U_{q,i}\setminus\bigcup_{j<i}U_{q,j}\bigr),
 \quad W_{q,i}=P_q(V_{q,i}),\quad
 \theta_{q,i}=(P_q|_{U_{q,i}})^{-1}|_{W_{q,i}}.                    \tag{2}
\]

The unrestricted map on each U is an analytic local diffeomorphism and is injective, hence a diffeomorphism onto its open image. Therefore V and W are Borel and θ is an actual inverse on its Borel domain. The V's partition all legal sources. Thus (2) retains every legal root exactly once as a source; overlapping target domains correctly retain different predecessors, not artificial atlas-label multiplicity.
At each w∈W set

\[
 J_{q,i}(w)=|\det D\theta_{q,i}(w)|=|\Delta_q(\theta_{q,i}w)|^{-1}>0.
 \quad \mu(\theta_{q,i}E)=\int_E J_{q,i}(w)\,d\mu(w)             \tag{3}
\]

for **every Borel E⊂W**. Finiteness and positivity hold pointwise by regularity. The formula is the change-of-variables identity for the analytic diffeomorphism on U, restricted to E; it remains valid for unbounded integrals and for floor-face subsets. Derivatives in (3) mean the polynomial inverse germ, not a derivative across a discontinuous floor interface. Overlapping germ charts for the same q and source give the same determinant. The frozen germ prescription, not the measure identity alone, fixes values on null strata.
Composing actual inverse branches on their restricted Borel domains gives an inverse of the corresponding legal iterate. Change of variables applied successively, or the germ chain rule, gives the product of their J's for every Borel test. In particular, for legal v define

\[
 \kappa(v)=-\log J(Tv)=\log|\Delta_{q(v)}(v)|,
 \quad D_m(v)=\prod_{j=0}^{m-1}|\Delta_{q(T^jv)}(T^jv)|,
 \quad S_m(v)=\log D_m(v),\quad D_0=1,\ S_0=0.                \tag{4}
\]

For Q every geometric q in (2)–(4) is zero. Products exist only along legal finite iterates; none is assigned to a nonexistent step. The all-point clock is finite but not assumed positive.

## 5. Full groupoid, kernels, incoming and physical phases

For each owner independently let

\[
 \mathcal G=\{(v,m-n,w):T^mv=T^nw\text{ with both iterates legal},\ m,n\ge0\},
 \qquad c(v,m-n,w)=S_m(v)-S_n(w).                              \tag{5}
\]

Equal triples, not witnesses or atlas labels, are identified. Source is w, range v, inverse negates the lag, and multiplication adds lags at matching endpoints. The set is Borel as a countable union of Borel iterate-equality conditions.
If two witnesses have the same lag, their two indices differ by a common integer; after exchanging witnesses take it nonnegative. Their common additional tail starts at the same state, and its clock cancels, proving c well defined. Choosing the first witness in a fixed enumeration of nonnegative index pairs also shows c is Borel. For composable witnesses (m,n) and (a,b), align n and a by extending the shorter along the longer's existing middle trajectory. This proves closure and c-additivity without extending beyond a terminal. Thus the forward arrow (Tv,−1,v) has clock −κ(v).

Here are exact global kernel descriptions, without incorrectly collapsing nonunit coalescence arrows:

\[
 K_{\rm lag}=\{(v,0,w):T^mv=T^mw\text{ for some legal }m\},
 \quad K_c=\{(v,m-n,w)\in\mathcal G:D_m(v)=D_n(w)\},
 \quad K_{\rm joint}=K_{\rm lag}\cap K_c.                     \tag{6}
\]

In K_c one may use any witness by well-definedness. In K_joint one may use a same-time witness and require D_m(v)=D_m(w).
For a target w the complete predecessor set is

\[
 I(w)=\bigcup_{q\in\mathbb Z}\{v:P_q(v)=w,\ v\in E_q\};\qquad
 I_Q(w)=\{v:P_0(v)=w,\ v\in E_0\}.                           \tag{7}
\]

Equivalently use every θ in (2) defined at w. Each I(w) is countable since each branch contributes at most one point. Set I⁰(w)={w}, I^(m+1)(w)=⋃_(u∈I^m(w))I(u). No q cutoff or root selection is present. A target need not itself be legal. The full source packet of w is exactly ⋃_(n:T^nw exists)⋃_(m≥0)I^m(T^nw), directly by (5); hence no incoming or forward-tail object is omitted.

For completeness this also gives the full isotropy and phase classification, even on unclassified packets. A nonzero source isotropy lag forces two unequal iterates of the same point to coincide, hence eventual periodicity. Conversely, if the eventual least source period is r, source isotropy is rZ: after reaching the cycle equality of iterates occurs precisely at differences divisible by r, and arbitrarily late witnesses realize each such difference. Let C be the clock sum over that cycle. Its complete clock group is H=CZ and c maps jr to jC; transient sums cancel. If the trajectory never becomes periodic, including trajectories that terminate, source isotropy and H are both {0}.

More explicitly choose a reference w in any source packet and one actual reference arrow g_v=(v,ℓ_v,w), with b_v=c(g_v). For an eventual r-cycle **every** arrow from u to v has the unique form

\[
 (v,\ell_v-\ell_u+jr,u),\qquad c=b_v-b_u+jC,\quad j\in\mathbb Z. \tag{8}
\]

Indeed compose with g_v^(-1) and g_u to get all reference isotropy. For a non-eventual packet there is exactly the j=0 term, with no r-term. Formula (8) specifies all global kernels in packet coordinates: impose respectively ℓ_v−ℓ_u+jr=0, b_v−b_u+jC=0, or both. It retains any cancellation and nonunit zero-lag arrows rather than presuming their absence.
The additive extension has all objects (v,h)∈X×R and arrows (w,h)→(v,h+c). Extension isotropy is ker(c|source isotropy): trivial for C≠0, all rZ for C=0, and trivial on non-eventual packets. Its orbit classes over one source packet have complete phase h−b_v∈R/H. Changing reference arrows changes b_v by H and changing reference changes the phase origin, not H or the dynamics.
Height translation descends for every real t. On an eventual packet with C≠0 its stabilizer is exactly H=CZ, giving ONE physical circle with least positive time |C| and repetitions k|C|, k≥1. For C=0, or a non-eventual packet, all phases form a free translation line; zero-clock source isotropy remains present but creates no positive period. These statements concern a set-level quotient, not a manifold or positive-roof suspension.

## 6. Complete frozen four-cell calculation

Write D_(a,b,c)=[a,a+1)×[b,b+1)×[c,c+1). For a∈{1,2}, the positive cell D_(a,a,a) has N=a²+a and MAIN/G coefficient q=a+1. The signed cell D_(-a,a,-a) has N=a²−a and MAIN/G coefficient q=a−1. All four cells satisfy arithmetic permission throughout; thus MAIN and G have identical actual restrictions there, though they differ globally. Q has geometric q=0 in every cell, with its own regularity test.
Every coordinate in these cells is nonzero. The fixed equations are yz=sx, zx=sy, xy=sz, where s=q+1>0 for all these cases. Multiplying the first by x and the second by y gives s x²=s y², and similarly x²=z². Writing the common absolute value t>0, the equations force t=s and sign(xyz)>0. Conversely all such signed triples satisfy the equations. This proves completeness over continuous coordinates, not merely integer testing.
For MAIN/G, the positive cells require t=a+2, outside [a,a+1). In each signed cell, the simultaneous constraints t∈(a−1,a] from x,z and t∈[a,a+1) from y force t=a; with q=a−1 this gives exactly p_a=(−a,a,−a). At p_a, conjugating DP_(a−1) by diag(−1,1,−1) gives diagonal 1−a and off-diagonal a. Its eigenvalues are a+1,1−2a,1−2a, so

\[
 \Delta_{a-1}(p_a)=(a+1)(2a-1)^2;
 \quad \Delta_0(p_1)=2,\quad\Delta_1(p_2)=27.                  \tag{9}
\]

These included left-face points are regular legal fixed sources. For Q, t=1; the first positive cell contains u=(1,1,1), the first signed cell contains p_1, and neither second cell contains a fixed point. Both surviving Q determinants are Δ_0=2. The complete ledger is therefore:

| Whole half-open cell | MAIN fixed set; absolute determinant | G fixed set; absolute determinant | Q fixed set; absolute determinant |
| --- | --- | --- | --- |
| D_(1,1,1) | empty | empty | {u}; 2 |
| D_(-1,1,-1) | {p_1}; 2 | {p_1}; 2 | {p_1}; 2 |
| D_(2,2,2) | empty | empty | empty |
| D_(-2,2,-2) | {p_2}; 27 | {p_2}; 27 | empty |

No continuous fixed family is hidden inside these cells: the nonzero-coordinate algebra lists every solution, and the half-open inequalities include the left faces and exclude the right faces exactly.
The regularity distinction is substantive: u=(1,1,1) has MAIN/G coefficient 2 and Δ_2(u)=−8+6+2=0, so is terminal for those owners despite passing arithmetic permission. Q instead has Δ_0(u)=2 and retains u as a legal fixed point. No MAIN/G next-step clock is assigned at u, and Q does not inherit their critical exclusion.

## 7. Entire tested packets, controls and adverse findings

For MAIN or G and each p_a, let B_a=⋃_(m≥0)I^m(p_a) using that owner's unrestricted (7). This is the exact full source packet, not a window-restricted basin. If v∈B_a choose its least arrival t_v≥0 and put b_v=S_(t_v)(v), L_a=log|Δ_(a−1)(p_a)|. The reference arrow (v,t_v,p_a) runs FROM p_a TO v. All arrows between v,w∈B_a and their clocks are

\[
 (v,t_v-t_w+j,w),\qquad c=b_v-b_w+jL_a,\quad j\in\mathbb Z.   \tag{10}
\]

Thus source isotropy is Z at every incoming state, extension isotropy is trivial, and the **entire** H is L_a Z. Lag, clock and joint kernels are given by the two explicit zero equations in (10); no unknown incoming cancellation is discarded. Every height is represented by phase h−b_v mod L_a. Additional roots or arbitrarily deep incoming chains from outside the four cells cannot shrink H. The basins B_1 and B_2 are disjoint: a deterministic forward trajectory cannot eventually equal two different fixed points.
For MAIN and independently for G, L_1=log2 and L_2=log27 are primitive. Although log27=3log3, log3∉(log27)Z. Consequently the second packet is not an iterate of a hidden log3 packet. Since 27=3³ is composite, this single real packet disproves MAIN's prime-only target. G retains the same obstruction even with divisibility permission removed; agreement is local to the frozen cells, not an assertion that the full owners coincide.

Q admits an additional exact incoming simplification. A regular P_0 predecessor must have xyz≠0 and target coordinates w_i≠0 with w_1w_2w_3=(xyz)²>0. Conversely under those target conditions its only polynomial predecessors are

\[
 x=\pm\sqrt{w_2w_3/w_1},\qquad y=w_3/x,\qquad z=w_2/x,       \tag{11}
\]

filtered by Q's own floor divisibility. Substitution proves sufficiency; x²=w_2w_3/w_1 proves completeness. For either tested core p∈{u,p_1}, (11) gives {p,−p}. All four points pass Q permission: their floors (1,1,1), (−1,−1,−1), (−1,1,−1), (1,−1,1) give N=2,0,0,2 and B=±1. Their |Δ_0| is 2. Each −p has coordinate product −1, so has no polynomial predecessor at all. Hence the complete Q basin is exactly {p,−p}, with p fixed and −p→p.
In each Q basin every triple (v,k,w), k∈Z, is an actual arrow and c=k log2: in (10) t_p=0,t_(-p)=1,b_v=t_v log2. All three kernels coincide with all zero-lag arrows on that two-point basin, including nonunits (p,0,−p). Source isotropy is Z, extension isotropy trivial, H=(log2)Z, and every phase is h mod log2. The two basins are disjoint and cannot be identified by equal clock or sign labels. Q therefore retains **two** different primitive log2 packets. Its prime uniqueness condition fails; deleting quotient feedback is not a target rescue.

The arithmetic control G, geometric-feedback control Q, and the all-root/floor-face ownership checks separate permission, feedback, and measure-version selection. Erasing the null left-face cores would change the frozen owner/version, not improve it. No density shuffle, parameter fit, clock rescaling or numerical robustness claim is made. PROVES_TOO_MUCH risk is not discharged by a log2 occurrence: it already occurs twice in the simpler Q owner, while MAIN permits a composite primitive.

## 8. Gate assessment and decision

| Gate | Exact evidence | Status and limit |
| --- | --- | --- |
| T0 | Full Borel owners, all-root regular atlas, terminals, actual groupoid | Established for MAIN/G/Q; same-object intact |
| T1 clock component | Every-Borel IMAGE and fixed all-point inverse-germ version | Established COMPONENT ONLY; ARITHMETIC T1 NOT PASSED; strong naturalness OPEN |
| T2 | Full fixed gate and complete incoming/H/phase/repetition descriptions | Necessary prime support FAIL for MAIN/G; tested prime uniqueness FAIL for Q |
| T3 | No owned operator/trace/zeta supplied or tested | NOT AUDITED |
| Classical/formal/B | No classical symplectic suspension or formal evaluation | NOT APPLICABLE / UNASSIGNED / NOT INVOKED |

Decision: STOP this frozen candidate and FORK the portfolio. No new candidate ID is proposed here, no evidence is transferred, and no higher-period or other-cell campaign is authorized by this negative result. Other cells and cycles remain unclassified; they cannot remove the retained log27 counterexample. The exact source mechanism and clock ownership are useful negative-control evidence, not accumulated target credit.

## Reproducibility, evidence and limitations

[Candidate card](candidate-card.md), [claim ledger](claim-ledger.md), [package README](README.md), and the [paper template](../paper-template.md) supply identity, status and navigation. All mathematics is exact analytic/algebraic derivation in §§3–7. Equations (2) and (7) are complete mathematical prescriptions, not effective algorithms; no certified numerical root enumerator, q cutoff, precision experiment or higher-cycle census is claimed. No scientific code, external API, literature campaign, PDF, Git operation, publishing or zero/operator experiment was used.
Read/verification commands were `sed -n`, `rg -n`, `wc -l`, and `sha256sum` on authorized local instruction/card/author surfaces, plus a read-only Node local-link/identity/hash checker; these mechanical checks do not test mathematical truth. Author writes used `apply_patch` only. The root owns card append and batch integration; author files do not certify later review/checkpoint completion. New review material was not read by the author.

## AI assistance, access, ethics and publication boundary

AI agent `/root/batch_clock_scope_review` supplied definition scouting, mathematical derivation, drafting and self-checking. Its actual proof-stage scientific read was the complete 99-line frozen 428 card; prior scout exposures and hash receipts are recorded in §3. It also read local plan/template instructions and registry/overview entries, with the already-read ARS author workflow retained. It did not read the new review/raw/peer artifacts or sibling manuscripts.
Bounded author aid `/root/batch_clock_scope_review/ccg_cotangent_probe` supplied the card's four-cell algebra, own core determinants and Q incoming check. Its actual receipt reports only `sed` of the complete 99-line 428 card through EOF and `sha256sum`, matching §3; no other file/tool operations, writes, scientific code, network or additional agents. Its contribution is shared-history author assistance, not independent peer validation. `/root` supplied freeze, authorization and integration, and arranges a separately access-controlled internal review; those roles are not represented here as completed external verification.
AI agents supplied mathematical derivation, drafting, self-checking and workflow-level internal review. The design/shared-history process is **NOT_CALIBRATED**, not blind, cross-model, human or external validation. **No human or external verification is certified.** No human-authorship contribution, institutional endorsement, funding or conflict declaration has been supplied; those remain unspecified. No human-subject or personal-data study is involved. Venue-specific criteria and publication authorization are unavailable (`criteria_binding_unavailable`); this Markdown research record makes no publication-readiness claim.
