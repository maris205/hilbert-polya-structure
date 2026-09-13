# Current proof-source selection and dependency map: internal arithmetic package

Date: 2026-09-08. Version: V2.
Document kind: `AUTHOR_SOURCE_SELECTION`.

This document selects the current mathematical proof route after the accepted
finite-positive, block/endpoint, and negative-adjoint replacements. It is an
author-side source map, not a new proof, independent mathematical check, or formal
candidate review. Its author participated in organizing this route and must not
subsequently be counted as an independent checker of that organization.
The original dependency map, author sources, reports, corrections, and decisions
remain unchanged.

## 1. How to read this map

The controlling manifest determines exactly which excerpts a future reader may
open. A link here identifies a file; it is **not recursive reading permission**.
Historical instructions inside a linked source to read another file, a whole
report, or a whole packet do not enlarge the manifest. If a necessary proof
excerpt is absent from the manifest, report that omission rather than silently
following further links or replacing the proof by an acceptance summary.

The original author IDs A01--A23 and A01s are preserved. The added author IDs are
F2, O2, R, N, T, I4, P, E, and M. Here **R means the positive terminal recurrence**
and **T means the third-first-layer proof**; the earlier positive decision called
its terminal source T, but that historical local alias is not used here.
Source M is the first-forcing moment-reuse proof, whereas module M9 below is an
organizational label. Historical report IDs R01--R18 are distinct from source R.

“Retain” means retain the actual argument with its object, finite ranges,
integrality, and errors. It does not mean reproduce all versions of that argument.
“Replaced” means no longer required by this selected route, not false or deleted.
The new sources occupy or share existing proof duties; they are not independent
additional scientific claims. Conversely, neither a source title nor its final
formula substitutes for its necessary proof paragraphs.

## 2. Unchanged mathematical contract

For every prime \(p\ge5\), integer \(a\ge2\), and primitive \(p^a\)-th root
\(\zeta\), keep the same positive-kick weighted map
\[
y'=y+\epsilon\sin q+2\lambda\epsilon^2\sin(2q),\qquad q'=q+y',
\]
and the SUM action
\[
\mathcal A=\sum_{j=0}^{s-1}
\left\{\tfrac12(q_{j+1}-q_j)^2-\epsilon\cos q_j
-\lambda\epsilon^2\cos(2q_j)\right\},\qquad s=p^a.
\]
The actual elimination is the unique small zero-mean transverse branch at a fixed
denominator and fixed compact parameter set. No denominator-uniform analytic
neighborhood is asserted. Degree--frequency filtering of that branch, rather
than a constructed root polynomial, gives the diagonal recurrence.

Write
\[
h=D_1=2-\zeta-\zeta^{-1},\quad \rho=-h,\quad L=\rho\lambda,
\quad K^+=\mathbb Q_p(h),\quad\mathcal O^+=\mathbb Z_p[h],
\]
\[
m=(p-1)/2,\quad M=p^{a-1}m=v_h(p),\quad D=3m+1=p+m,
\quad\chi=(-1)^{m+1},\quad v_h(h)=1.
\]
The residue field is \(\mathbb F_p\). With \(V_n=\rho^nv_n(L/\rho)\) and
\(d_n=-D_n/h\), the actual finite recurrence is
\[
d_nV_n=-\tfrac12[x^{n-1}]e^V-L[x^{n-2}]e^{2V},\qquad V_1=1/2.
\]
Negative coefficient indices mean zero. For \(k=1,2,3\),
\[
\mathcal B_k=-[x^{kp-1}]e^V-2L[x^{kp-2}]e^{2V}=2d_{kp}V_{kp}.
\]
All internal propagators are nonzero because \(3p<p^a\); the modes at
\(p,2p,3p\) are not projected out. These polynomials cancel the specified actual
diagonal jet, not the whole spatial harmonic, final periodic resonance, or an
invariant under arbitrary symplectic conjugacy. The invertible change from the
raw parameter polynomial is
\(\mathcal B_k(L)=\rho^{kp-1}\mathcal B_{kp\mid p^a}(L/\rho)\).
It preserves factors, fields, multiplicities, and common roots, while
\(v_h(\lambda)=v_h(L)-1\). The signs of root-cluster valuations refer to L.

The four dependent conclusions of the original whole-package contract remain:

1. \(S=h^{-D}p^2\mathcal B_3\in\mathcal O^+[L]\) has actual degree D and a
   unique factorization \(S=P_{\rm cl}U_{\rm cl}\), with P monic of degree m,
   \(\overline P_{\rm cl}=L^m\), and U of degree p with unit constant residue.
   Its complete lower Newton polygon is
   \((0,m-1)\longrightarrow(m,0)\longrightarrow(D,M-m)\).
   The two factors are irreducible and separable over \(K^+\); S is squarefree.
2. Positive roots and distinct positive-root differences have valuation
   \(t_+=(m-1)/m\). For \(\kappa^m=-16\chi h^{m-1}\),
   \(E=K^+(\kappa)=K^+(\alpha_j)=\operatorname{Spl}_{K^+}(P_{\rm cl})\)
   is cyclic, tamely totally ramified, of degree and ramification index m and
   residue degree one. Roots admit labels
   \(\alpha_j=\omega_j\kappa+O(h)\), \(\omega_j\in\mu_m\subset K^+\).
3. Every negative root has valuation \(t_-=-(M-m)/p\). Each single-root field
   has degree and ramification index p and residue degree one, hence is wildly
   totally ramified. Its compositum with E has degree and ramification index mp
   and residue degree one. Equality or normality of the negative single-root
   fields, their full splitting field, and its Galois group are not determined.
4. \(\mathcal B_1,\mathcal B_2,\mathcal B_3\) are pairwise coprime over
   \(K^+[L]\). The actual degree of \(\mathcal B_2\) is p; a smaller-degree
   shortcut is not available.

The point-value consequence is retained, including both critical circles.
Put \(b_-=M-m\); for any nonzero parameter \(\ell\) in any finite extension,
with \(t=v_h(\ell)\),
\[
v_h(S(\ell))=
\begin{cases}
Dt+b_-,&t<t_-,\\
mt_-+b_-+\sum_{k=1}^{p}v_h(\ell-\beta_k),&t=t_-,\\
mt,&t_-<t<t_+,\\
(m-1)t_++\max_jv_h(\ell-\alpha_j),&t=t_+,\\
m-1,&t>t_+.
\end{cases}
\]
At zero the value is \(m-1\); roots allow \(+\infty\).
Also \(v_h(\mathcal B_3)=D-2M+v_h(S)\) and
\(v_h(V_{3p})=m+1-2M+v_h(S)\).
The negative critical-circle sum is not replaced by a single maximum or by
unknown pairwise negative-root distances. These dependent conclusions and this
consequence are one package, not separate scientific targets.

## 3. Current forward modules and necessary author paragraphs

The M1--M10 labels preserve the original organizational roles. They are not a
prescribed section count. Definitions and assumptions needed to parse each cited
proof paragraph accompany that paragraph in the manifest; a historical input
list is not an instruction to import the entire historical dependency tree.

### M1. Actual branch, local ring, and normalization

Retain A01 Notation and Proof Steps 1--2 for the actual diagonal recurrence;
A01s Assumptions and Proof Step 1 for the analytic zero-mean elimination;
A02 Notation and Proof Step 1 for local ramification and propagator levels.
Retain A07 Step 9 only for the exact tripling identity (58),
\(d_{3p}=d_p(3+hd_p)^2\), and its valuation when converting to \(V_{3p}\).
This node has no downstream mathematical premise. Numerical root scans, parity
improvements, primitive-orbit counts, and full-denominator classifications are
not selected by these references.

### M2. Whole first internal layer, not just its highest coefficient

Retain A02 Proof Steps 2--6, especially the nonstationary action (11), reflection
defect (12), finite square-propagator evaluation (13)--(14), and the **formal**
identity (15):
\[
\mathcal B_1(H,L)=\chi H^m(2-L^m)+H^{m+1}R_1+pT_1.
\]
Retain its actual specialization, first-entry height, and proof that all first
forcing roots have L-valuation zero. M1 precedes this node. The formal identity
is necessary for the later H-Euler derivative, A04's second endpoint, and A23's
pure-even doubling calculation. Source M does not replace this complete first
layer. A02 Step 7's detailed Frobenius factor-degree classification is not
required by the selected whole-package conclusions.

### M3. Finite factorial algebra, two real entries, and the full coupled bridge

Use this staged order, keeping each displayed duty:

| Stage | Necessary source proof | Output and restriction |
| --- | --- | --- |
| Common finite algebra | N Assumptions and Steps 1--3, (1)--(9), N1--N2 | Free basis of \(R[x,\eta]/(x^p-p\eta,\eta^3)\), injection, carries, one factorial identity for both bands, and the complete four-source finite exponential product. Only fixed \(P_1=1/2\), \(\alpha=1,2\); arbitrary auxiliary amplitudes do not satisfy the asserted scalar Frobenius simplification. |
| First actual entry and block | M2 followed by N Step 4 through (11) | The true \(pV_p\) entry, known-prefix unit induction, first block integrality, and its first model comparison. The full actual block is not assumed integral before induction. |
| Actual second endpoint and second entry | A04 Proof Steps 3--7, (18)--(37), after N's first comparison | Real shifts, pairing defects, first response, nonstationary second action, and the two contributions \((2-L^m)+L^m=2\). This gives \(h^{-2m}p\mathcal B_2\) integral with residue 2, first/second coprimality, and the \(2p\) entry. N does not prove this endpoint by itself. |
| Second actual block and coupled comparison | N Step 4 after (11), Steps 5--6, (12)--(15), N3a--N3b | Second prefix induction, old-block square, both actual/model constant distinctions, square-difference factorization, and the common error \(h^{M-m}\). Neither nonunit entry is treated as a unit step. |
| Full response bridge | A06 Notation, Proof Steps 4--7, especially (26)--(45) | Unshifted derivative bases, exact Q-coupling elimination, first and second propagator differences, full response equations including \(-Ky^2\), and legitimate actual transfer. The accurate coupled equations remain available above the precision of their first displayed truncations. |

N replaces the factorial/closure/comparison proofs formerly repeated in A03,
A05, A04 Steps 1--2, and A06 Steps 1--3. Their facts remain present through N;
those whole old files are not additional mandatory core readings. Definitions
of J, K, the two models, and their zero constants are stated once.
The raw block comparison really is only \(h^{M-m}\): an extra endpoint defect
of order \(h^m\) is needed before asserting error \(h^M\).

### M4. Actual third endpoint, full-H response, first layer, and separation

Retain A07 Notation and Proof Steps 1--3: the actual third SUM-action Euler
identity (15), all omission bounds, both actual pairing defects (16), the
\(h^M\) bridge (17), **all four terms** in (18), real paired defects (19)--(20),
the finite shift parameter and fixed-ring argument (21)--(24).
Retain Step 4 through (29) (lines 374--398) for the independent-shift unit model
and defining response equations. Retain the exact first-pair identity in Step 5
(lines 482--487); its low-H approximation must not replace the full pairing.

Retain A09 Notation, Proof Step 1, and Step 2 through (16) (lines 95--241):
the exact full-H t,q solutions are proved by differentiated low equations,
Chebyshev identities, and unit triangular uniqueness; the cubic coefficient
contains all four terms, including its first paired term. The historical input
table's old first-layer coefficient is not used by this forward proof.

After the shared finite/operator node described under M5, use T Steps 1--7.
Its all-L, mod-H-squared section comes from the **untruncated average identity**,
not from extending a total-degree quotient. F2 leaves the coefficients c,d,e
unassigned; the operator removes d. T Steps 3--6 prove T3 using the same finite
pure-even/linear-odd blocks, the \(J_{\rm odd}\) certificate, both ordered
pairings, the exact \(4^{-m}\) scaling, and the finite convolution S=0.
T Step 7 reconnects the actual error and proves
\(\overline S=-3\chi L^m/64\). The minimum-prime precision check remains.

Retain A08 Proof Steps 1--2 and Steps 5--7 for the bounded-degree DVR lifting,
uniqueness, actual degree/nonzero constants, **full model parameter-degree
argument**, and monic quotient comparison. In Step 7 retain the factor/quotient
transfer, not its superseded coarse root bounds as new outputs. The actual
degree and model-degree proofs are different obligations; I4 replaces neither.
T3 is now a forward input for source M, not a quantity inferred from S's unit.

### M5. Shared finite/operator foundation and the positive critical consumer

This foundation is placed before its consumers in M4 and here; the module label
does not impose a circular chronological order.

| Duty | Necessary source proof | Downstream use and limit |
| --- | --- | --- |
| Strictly precritical moments | F2 Notation and Proof Steps 1--5, (3)--(22), including (16a) | Finite even-space invertibility, original-normalization translation, two-exponential interface, index-polynomial degree bounds, and finite power sums give \([H^kL^j]W=\delta_{j0}(k!)^2/(2k+1)!\) only for \(k+j<m\). It starts from M2's actual low recurrence and Chebyshev data, not the third unit. |
| Complete averaged operator, proved once | O2 Notation and Proof Steps 1--4, especially (3), (11)--(12), and (15)--(20), with A09's exact response | Actual finite triangular integrality, amplitude homogeneity, true reflection-defect bounds, exact averaged weight ODEs, and every weight-derivative cancellation. Its untruncated average identity supplies T's mod \(H^2\) section and the critical total-degree calculation separately. |
| True critical reflection and unknown critical moments | O2 Steps 2, 5--6, especially (10)--(12), (24)--(26) | The nonzero odd correction \(3\chi H^m/16\) is retained. The critical finite moment is defined by triangular integrality before the Euler multiplier \(m(m+1/2)=0\) removes it. It is not assumed zero or given a critical rational kernel. |
| Terminal coefficient | R, “Finite terminal proof,” (3)--(7), with its fixed inputs | One finite recurrence and factorial pairing give \((H-4)\mathscr DV=\chi H^m\), hence \(\mathcal F_3=3\chi H^m/32\) modulo \((H,L)^{m+1}\). This replaces O2 Step 7, not Steps 1--6. Positive-L disappearance is limited to the stated total degree. |
| Quartic interface and constant | I4 Assumptions, Notation, and Proof §§1--5 | First prove full-parameter polynomial existence and \(O(H^{4m+1})\) error; then compute \(E_4(0)=-3/32\) from the same finite constant-section drivers and self-adjoint pairing. The positive-L coefficients are not declared zero; their closed forms are unnecessary for these consumers. |
| Actual coefficients and positive domain | A13 Proof Step 4 and Step 5; Step 6 only before the final \(p\ge7\) translation paragraph | Combine cubic and quartic constants to \(-3/4\), check \(M\ge4m+1\), transfer through \(e_*=M-D\ge m\), then prove the positive Newton edge, Kummer/Hensel identification, irreducibility, distances, and cyclic splitting. The complete point-value terminal is A23 Step 5. |

For F2, retain the precise derivative/translation interpretation supplied by its
independent report: Proof Step 2 for the q0 exception; Proof Step 3 for the
auxiliary-variable coefficient proof before truncation; Proof Step 4 for the
two-ideal exponential interface. Ordinary polynomial positive N-derivatives
carry \(G^2-1\); q0 requires order at least two, since \(Nq_0=G\).
Only ideal-preserving derivations descend to the indicated quotients.

The selected input to A13 Step 4 is now the polynomial/constant/error interface
from I4, not the old positive-L closed formula displayed in its (22). The same
coefficient proof uses only polynomial existence, the constant, and the error.
Its actual constant and the monic coefficient-transfer proof are written once,
even though I4 §5 also records their consumer interface.

### M6. Three separate negative-side coefficient windows

These are distinct proofs with separate windows, not one unnamed lemma:

| Window | Necessary source proof | Required output / hazard |
| --- | --- | --- |
| Common high parameters \(j>m\) | A14 Assumptions/Notation and Proof Steps 1--5 | \(p[L^j]\mathcal B_3\in h^m\); retain the full actual entry \(q=pV_p\), defect/response errors, and high-parameter projection **before** division by p. |
| Upper window \(p<j\le D\) | A15 Notation and Proof Steps 1--6; Step 7's quotient transfer and boundary check | \(p[L^j]\mathcal B_3\in h^{2m}\); retain actual entries, resonance-error comparison, finite high equations, true shifts, and complete Ward endpoint. Its \(t^p=0\) window does not prove \(j=p\). |
| Boundary \(j=p\) | A16 Notation and Proof Steps 1--5, plus “Conditional coefficient transfer and boundary checks” | The same height at the missing boundary, using the additional \(t^p\) factorial band, distinct constants 1 and 1/2, and distinct Ward weights. Retain the actual comparison and pure-even doubling (20)--(21) in Step 5. |

M1--M4 supply their unchanged actual inputs; no old energy evaluation is needed
once its current endpoint output and bridge are supplied. Retain the final
monic descending comparisons giving \(v_h(u_r)\ge M-p\) for \(1\le r\le m\)
and \(v_h(u_r)\ge M-m-1\) for \(m<r<p\).

### M7. Raw highest-weight foundations before finite comparison

The order is mandatory:

1. A17 Notation and Proof Steps 1--2 provide the actual highest-weight
   extraction, complete endpoint with factor 16, original even/odd equations,
   low integrality, and the unnormalized pollution bound \(-2m\).
2. Before any reference comparison, retain the raw even normalized high-band
   integrality paragraph in A17 Step 4, lines 199--201, and raw odd normalized
   integrality/support in Step 6, lines 236--242. These are recurrence arguments,
   not consequences of the reference lemma.
3. A18 Notation fixes the finite zero-layer low functions and allowed odd
   inverse indices. Its finite-reference lemma in Step 1, lines 142--192,
   and Step 2 give exact matching below p, the finite factorial estimate, and
   the actual comparison window. This replaces A17's old global rational
   reference (12)--(16); it does not prove its own prior integrality premise.
4. Retain A17 Step 3 and the derivative portions of Steps 5--6 after the finite
   comparison has supplied their input, or the identical full low-derivative
   argument in A19 Step 3. The base-derivative identity is proved once; its
   actual high-band comparison and raw support are not omitted.
5. Retain A18 Proof Step 4, (17)--(19), with its finite \(\mathscr H\) definition:
   \(w_0,a_0,w_1,a_1\), their low equations, unit uniqueness, and all used
   finite denominators remain necessary inputs to E.

No new shared-proof identification between T's low solutions and A18 is claimed.
The selected A18 reference gives only its stated precision; the next ghost layer
requires A21. Old unknown global \(R_{m+1,0}\) pole discussions and obsolete
intermediate-height evaluations are not new prerequisites.

### M8. Full formal Ward identity and the actual quadratic driver

Retain A19 Notation and Proof Steps 1--3, (9)--(24), including its low-band
formal integrality, true quadratic constant shift, base-derivative solutions,
complete formal Ward equations, both product identities, and
\[
B_{\rm low}=-4^m[L^m]\mathcal B_1(H,L),\qquad
\text{linear endpoint}=-\lambda_H(H\partial_H-m)B_{\rm low}.
\]
H-differentiation occurs on formal integral coefficients before specialization.
This full Ward identity is not replaced by P's mod-H-squared pairing.

After M9's A21 ghost comparison, retain A22 Notation and Proof Steps 1--3
through (12), together with Step 8. They supply the same auxiliary high system,
unit triangular uniqueness, residual factor \(H^{2m}\), the accurate shifts
\[
\Delta_n=\lambda_HS_n-4H^{2m}-2H^pd_n,
\qquad \lambda_H^2/H^{2m}=16-4H\pmod{H^2},
\]
and the complete direct drivers. These actual source terms, including both
quadratic shift types and linear-shift feedback, are proved once and then used
by P/E. A22's later same-named residual sources obtained by inserting old
\(X_0,Y_0\) are not the direct sources used by E.

### M9. The same first nonzero actual highest coefficient

| Duty | Necessary current proof | Output / nonreplacement boundary |
| --- | --- | --- |
| First-forcing next layer | Source M Notation and Proof Steps 1--5, with T3 already proved in M4 | Same-recursion amplitude mapping, nonstationary Euler identity, reflected next weight, both ordered endpoints, scaling, weight difference \(Q=2\mathscr W_{\rm top}-2H\Sigma_2(0)\), finite zero-order sum, and formal/actual transfer. This gives the same \([L^m]\mathcal B_1\) next layer and thus Ward's linear contribution \(-1/4\). |
| Real first ghost | A21 Assumptions/Notation and Proof Steps 1--5, especially (10)--(27); Step 6 retains the direct/feedback sign separation | First error is evaluated after multiplying by p and proving integrality; exact low matching and new-precision product support produce both actual high equations and their common scaling. The full endpoint correction is zero; direct and response terms are not separately zero. |
| Parametric crossed adjoint | P Assumptions/Notation and Proof Steps 1--3 plus Step 5 | True reflection modulo \(H^2\), the finite reverse pairing, variable weights \(2\mathcal Qa,4\Theta w\), and the complete endpoint-to-direct-source identity. Step 5 connects to the already retained actual system. P does not replace A21 or the full Ward proof. |
| Both quadratic endpoint coefficients | E Assumptions, finite-kernel notation, and Proof Steps 1--4, (3)--(17) | Direct two-order source expansion, changing adjoint weights, zero-layer evaluation, **both R,J kernels and their polynomial coefficients**, and the legitimate fixed-interval single sum give \(\mathcal C_H=-H/2\pmod{H^2}\). These are proof content, not just a quoted scalar. |
| Final actual assembly | P Step 5, (14)--(16), E's output, M's formal output, A19's Ward link, A21's actual equality, and A22 Step 8 | Add the linear \(-1/4\), quadratic \(-1/2\), and net ghost zero in the same \(H^p\) layer; use \(4^D\equiv4\), then the legitimate integral actual comparison to get \(p[L^D]\mathcal B_3=-3h^p/16+O(h^{p+1})\). No modular relation is divided by p. |

Retain \(2m+2=p+1\), \(M-2m\ge3m\ge p+1\), high-product support, and the
minimum case \(p=5,a=2\). The residual identification with an \(H^{2m}\)-multiple
is a coefficient-module identification, not inversion of \(H^{2m}\).
The pairing uses even indices through m with zero constant and odd indices
strictly below m: neither \(d_0^{-1}\) nor a forbidden odd \(1/p\) enters.
T3 remains proved once in M4; M's mapping, weight subtraction, zero-order sum,
and transfer remain distinct mandatory arguments here.

The present selection replaces A19 Steps 4--5's explicit quadratic zero-layer
solutions and zero sum, A22 Steps 4--6's old adjoint/six-kernel summation, and
A20 Steps 3--4's linear-odd expansion/double sum. All still-needed Euler,
reflection, endpoint-weight, and transfer duties from A20 are now proved in M;
the old full A20 is not an extra core proof to reproduce.

### M10. All structural consumers and exact point values

Retain A23 Proof Steps 1--5 with its exact scientific definitions and inputs.
Step 1 consumes M6's distinct intermediate bounds and M9's scalar to prove
strict chord inequalities and \(v_h(u_p)=M-m\). Step 2 proves negative
irreducibility/separability, each wild single-root field, and its compositum
with the already proved positive cyclic field.

Step 3 must retain the actual degree-p second forcing, its pure-even extraction,
exact doubling map, and M2's **constant first-layer** input, giving
\([L^p]\mathcal B_2=4\chi h^m+O(h^{m+1})\).
Step 4 compares the highest/constant ratios with residues 2 and 4 after the
same nonzero scale; it then combines M3's first/second coprimality and M2's
unit-circle roots with both third-forcing clusters. Source M's highest
next-layer coefficient is not a replacement for this constant first layer.
Step 5 proves the full point-value formula in §2 from the actual factorization,
including both critical circles, zero, and infinite values at roots.

## 4. Forward sharing and noncircular placement

One valid forward schedule is:

```text
M1 -> M2 -> N first block -> A04 second endpoint -> N second block -> A06
                  |                                              |
                  +-> F2 finite moments                          +-> A07 -> A09
                                  \                                  /
                                   +---- O2 full averaged identity --+
                                          |                 |
                                          v                 v
                                   T / T3 -> A08     O2 critical + R + I4
                                          |                 |
                                          |                 v
                                          |                A13
                                          v
                              M first-forcing reuse

M1/M2 -> A17 raw integrality/support -> A18 finite comparison/low solutions
                                             |
                                             v
                              A19 full Ward -> A21 real ghost
                                             |
                                             v
                               A22 true driver -> P -> E

A14 common window + A15 upper window + A16 boundary window
             + A08/A13 + same-endpoint Ward/M/ghost/P/E assembly -> A23
```

Arrows express prerequisite use, not independent proof counts. O2's complete
average derivation is one shared proof with different valid sections; its
critical odd correction is not discarded by that sharing. The raw negative
foundations do not depend on the new highest scalar. M only uses T3 forward;
T3 was obtained from its own finite equations, not the final third-forcing unit.
Definitions of the positive moment W, the negative even band W, F2's coordinate
\(u=x/4\), and highest-weight \(u=Lx^2/4\) stay distinct.

## 5. Stable author-source index

Only the selected portions in §3 are current core inputs. An inactive-core entry
preserves an ID and historical provenance, not a reading obligation.

| ID | Exact source | Current role |
| --- | --- | --- |
| A01 | [Actual diagonal recurrence](PAPER30_TWIST_ROOT_COUNTEREXAMPLE_PROBE_V1_20260907.md) | M1 selected entrance only. |
| A01s | [Analytic elimination supplement](PAPER30_TWIST_REDUCTION_PARITY_NOTE_V1_20260907.md) | M1 Step 1 only. |
| A02 | [First internal local structure](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_PROBE_V1_20260907.md) | M1--M2; formal first-layer input retained. |
| A03 | [Original first factorial block](PAPER30_TWIST_PRIME_POWER_POST_POLE_BLOCK_PROBE_V1_20260907.md) | Core factorial/closure duties replaced by N; ID retained. |
| A04 | [Actual second internal endpoint](PAPER30_TWIST_PRIME_POWER_SECOND_INTERNAL_FORCING_PROBE_V1_20260907.md) | Steps 3--7 retained; preliminary comparison now N. |
| A05 | [Original second factorial block](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_BLOCK_PROBE_V1_20260907.md) | Core factorial/closure duties replaced by N; ID retained. |
| A06 | [Full coupled response bridge](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_RESPONSE_BRIDGE_PROBE_V1_20260907.md) | Full response duties retained; initial factorial/comparison duties now N. |
| A07 | [Actual third action and endpoint](PAPER30_TWIST_THIRD_FORCING_GENERAL_PRIME_PROBE_V1_20260907.md) | Actual bridge, four terms, finite shift retained; first-layer evaluation now T. |
| A08 | [Fixed-degree factor separation](PAPER30_TWIST_THIRD_FORCING_ROOT_CLUSTER_SEPARATION_PROBE_V1_20260907.md) | Actual degree, model degree, separation, and quotient transfer retained. |
| A09 | [Exact full-H response](PAPER30_TWIST_THIRD_FORCING_GENERAL_NEXT_LAYER_PROBE_V1_20260907.md) | Step 1 and complete cubic interface retained; later moments excluded. |
| A10 | [Original full quartic evaluation](PAPER30_TWIST_THIRD_FORCING_FOURTH_SHIFT_RESIDUE_PROBE_V1_20260907.md) | Current needed interface proved by I4; stronger closed result preserved outside core. |
| A11 | [Original higher rational structure](PAPER30_TWIST_THIRD_FORCING_HIGHER_RESPONSE_STRUCTURE_PROBE_V1_20260907.md) | Current precritical/critical uses replaced by F2/O2/R; negative reference now A18. |
| A12 | [Original critical projection](PAPER30_TWIST_THIRD_FORCING_CRITICAL_PROJECTION_PROBE_V1_20260907.md) | Current projection/operator duties proved by O2/R. |
| A13 | [Positive cluster and cyclic field](PAPER30_TWIST_THIRD_FORCING_UNIFORM_POSITIVE_CLUSTER_PROBE_V1_20260907.md) | Actual transfer, positive domain, distances retained with new upstream inputs. |
| A14 | [Common high-parameter window](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HIGH_PRECRITICAL_PROOF_V1_20260908.md) | Separate mandatory M6 window. |
| A15 | [Upper high-parameter window](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_UPPER_HIGH_CRITICAL_PROBE_V1_20260908.md) | Separate mandatory M6 window and quotient transfer. |
| A16 | [Boundary high-parameter window](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_BOUNDARY_HIGH_PROOF_V1_20260908.md) | Separate mandatory M6 boundary and doubling. |
| A17 | [Raw highest-weight foundations](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_PRECRITICAL_PROOF_V1_20260908.md) | M7 raw integrality/support retained before reference; not the failed older top draft. |
| A18 | [Finite reference and low solutions](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_POSTCRITICAL_PROBE_V1_20260908.md) | M7 finite comparison and \(w_0,a_0,w_1,a_1\) retained. |
| A19 | [Full formal Ward identity](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_SECOND_POSTCRITICAL_PROBE_V1_20260908.md) | Steps 1--3 retained; old quadratic explicit evaluation replaced by P/E. |
| A20 | [Original first-forcing next layer](PAPER30_TWIST_FIRST_FORCING_TOP_NEXT_LAYER_PROOF_V1_20260908.md) | Target identity preserved; selected full duty now supplied by M and M2. |
| A21 | [Actual first ghost](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HP_GHOST_PROBE_V1_20260908.md) | Actual first error, high equations, common scaling, and full endpoint retained. |
| A22 | [Actual next-layer quadratic system](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HP_RESPONSE_PROBE_V1_20260908.md) | Steps 1--3 through (12) and Step 8 retained; old six-kernel route not selected. |
| A23 | [Complete structure and coprimality](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_NEWTON_AND_COPRIME_PROOF_V1_20260908.md) | All structural and point-value consumers retained. |
| F2 | [Finite strict-precritical moments V2](PAPER30_TWIST_POSITIVE_FINITE_MOMENT_DIAGNOSIS_V2_20260908.md) | M5 finite construction, shared precritical input. |
| O2 | [Complete averaged operator V2](PAPER30_TWIST_POSITIVE_UNIFIED_CRITICAL_OPERATOR_PROBE_V2_20260908.md) | M5 Steps 1--6, complete average shared; Step 7 replaced by R. |
| R | [Finite terminal recurrence](PAPER30_TWIST_POSITIVE_TERMINAL_RECURRENCE_REPLACEMENT_V1_20260908.md) | M5 terminal coefficient only. |
| N | [Finite factorial normal form](PAPER30_TWIST_FACTORIAL_BLOCK_NORMAL_FORM_DIAGNOSIS_V1_20260908.md) | M3 common algebra, staged blocks, and comparisons. |
| T | [Third first-layer operator proof](PAPER30_TWIST_THIRD_FIRST_LAYER_OPERATOR_DIAGNOSIS_V1_20260908.md) | M4 first layer and T3; T3 reused by M9. |
| I4 | [Minimal full-parameter quartic interface](PAPER30_TWIST_FOURTH_SHIFT_MINIMAL_INTERFACE_PROOF_V1_20260908.md) | M5 full polynomial/error interface and required constant. |
| P | [Parametric crossed adjoint](PAPER30_TWIST_NEGATIVE_PARAMETRIC_ADJOINT_PROOF_V1_20260908.md) | M9 finite pairing and same-system interface. |
| E | [Direct quadratic endpoint evaluation](PAPER30_TWIST_NEGATIVE_PARAMETRIC_ADJOINT_EVALUATION_V1_20260908.md) | M9 direct sources, both kernels, and finite single sum. |
| M | [Same-object highest-moment reuse](PAPER30_TWIST_FIRST_FORCING_NEXT_LAYER_MOMENT_REUSE_V1_20260908.md) | M9 mapping, weight difference, finite sum, and actual transfer. |

## 6. Mathematical report roles and correction boundaries

Reports document the stated nonauthor checks; they do not replace source proofs
or constitute an independent check of this new selection. Historical R01--R18
bindings remain as in the controlling manifest, restricted to retained duties:
R01 for A01/A01s, R02 for A02, R03 for A04, R05 for retained A06/A07, R06 for
A08, R07 for A09's full-H interface, R08 for retained A13, R09--R14 for the
corresponding A14--A19 portions, R16 for A21, R17 for retained A22's actual
system/error, and R18 for A23. R04 and R15 do not become additional core proof
requirements merely because their old author IDs remain in the index.
The precise excerpts and any preserved historical-boundary readings are set by
the manifest, not by this paragraph.

| Manifest ID | Report / interface record | Mathematical role only |
| --- | --- | --- |
| RF | [Finite-moment independent check](PAPER30_TWIST_POSITIVE_FINITE_MOMENT_INDEPENDENT_CHECK_V1_20260908.md) | F2's finite construction, translation, mixed-ideal exponential interface, degree bounds and scaling; its Proof Steps 2--4 give the precise readings used above. |
| RO | [Unified-operator independent check](PAPER30_TWIST_POSITIVE_UNIFIED_CRITICAL_OPERATOR_INDEPENDENT_CHECK_V1_20260908.md) | Full average identity, all derivative terms, and actual critical reflection. Historical literal-format failures remain recorded; current O2 supplies the corrected bytes. |
| RR | [Terminal-recurrence independent check](PAPER30_TWIST_POSITIVE_TERMINAL_RECURRENCE_INDEPENDENT_CHECK_V1_20260908.md) | Source R's finite terminal replacement, conditional on the separately checked operator input; not a repeat of the whole operator proof. |
| DPLUS | [Positive replacement dependency check](PAPER30_TWIST_POSITIVE_REPLACEMENT_DEPENDENCY_CHECK_V1_20260908.md) | Composition and deletion boundaries, especially raw negative integrality before finite reference. |
| RN | [Normal-form independent check](PAPER30_TWIST_FACTORIAL_BLOCK_NORMAL_FORM_INDEPENDENT_CHECK_V1_20260908.md) | N1--N3, with the stated first/second actual entries and A04 endpoint retained. |
| RT | [First-layer independent check](PAPER30_TWIST_THIRD_FIRST_LAYER_OPERATOR_INDEPENDENT_CHECK_V1_20260908.md) | T's full-parameter section, finite highest moments, scaling and actual first-layer connection. |
| RI4 | [Quartic-interface independent check](PAPER30_TWIST_FOURTH_SHIFT_MINIMAL_INTERFACE_INDEPENDENT_CHECK_V1_20260908.md) | I4's polynomial existence, finite constant pairing and actual coefficient precision. |
| DI4 | [Quartic consumer check](PAPER30_TWIST_FOURTH_SHIFT_MINIMAL_INTERFACE_DEPENDENCY_V1_20260908.md) | Current consumers need polynomial existence, the constant and the uniform error, not the positive-L closed coefficients. |
| RP | [Parametric-adjoint independent check](PAPER30_TWIST_NEGATIVE_PARAMETRIC_ADJOINT_INDEPENDENT_CHECK_V1_20260908.md) | P's finite pairing, genuine reflection and actual-system interface. |
| RE | [Direct-evaluation independent check](PAPER30_TWIST_NEGATIVE_PARAMETRIC_ADJOINT_EVALUATION_INDEPENDENT_CHECK_V1_20260908.md) | E's new direct two-order computation, both kernels, finite sum and smallest prime. |
| RM | [Moment-reuse independent check](PAPER30_TWIST_FIRST_FORCING_NEXT_LAYER_MOMENT_REUSE_INDEPENDENT_CHECK_V1_20260908.md) | M's same-object map, changed weights and formal/actual transfer using accepted T3. |
| DMINUS | [Negative replacement dependency check](PAPER30_TWIST_NEGATIVE_ADJOINT_REPLACEMENT_DEPENDENCY_CHECK_V1_20260908.md) | Connections to the same complete endpoint and all A23 consumers; its separate mathematical conditions belong to the corresponding new-proof checks. |

Acceptance decisions govern the choice but are not mathematical proof sources
in this map. No whole decision file is imported here. Their allowed excerpts,
if required, are assigned separately by the controlling manifest.

Preserve these mathematical distinctions in any subsequent presentation:

- The failed original `NEGATIVE_TOP_COEFFICIENT_PROBE_V1_20260907` is not A17.
  Its invalid direct reduction of the ordinary post-pole odd band and incomplete
  high-band/support reasoning remain a failure of that original proof. A17 is
  the separately checked successor; another author's alternative proof does not
  retroactively certify the failed bytes.
- The noncore `GENERAL_NEXT_LAYER_ROOT_BOUND` V1 domain-trace assertion was too
  strong. Its narrow V2 wording correction does not change A09's full-H response
  or create a new field conclusion. Neither old root-bound version is a current
  core input.
- The old A22 adjoint/convolution route had a finite-residue interpretation, not
  a characteristic-zero equality of the original response endpoint. Its
  recorded nonzero p-multiple defect is not erased by adopting P/E. The current
  P identity is instead proved in \(\mathbb F_p[H]/(H^2)\); it is not an
  all-order or characteristic-zero adjoint identity.
- F2 and O2 are the typography-corrected V2 sources, not mathematical rewrites
  of their V1 proofs. The q0 derivative exception and the coefficientwise
  auxiliary-variable translation argument remain explicit. Literal old
  formatting failures are not relabeled as failures of the corrected formula
  or silently relabeled as successful original bytes.
- A19's first-forcing formal reference is **A02 Step 4, equation (15)**.
  A23's pure-even doubling reference is **A16 Step 5, equations (20)--(21)**,
  not its old short-reference Step 4. A23 independently fixes its own scaling.
- The boundary second forcing has actual degree p. Its two ratio residues are
  2 and 4; the third highest endpoint rescales with \(4^D\equiv4\), not 16.
  Independent auxiliary-computation errors that were corrected in a report
  must not be reassigned as author mathematical failures.

The negative full splitting field, negative pairwise distances, second forcing's
complete Newton polygon/simple-root classification, final-period resonance
polynomials, real bifurcation interpretations, and noncore \(p\ge7\) root
translation are not obtained by this selection. Finite examples and symbolic
residual checks are auxiliary, not replacements for the universal proofs.

## 7. Coverage and handoff

All mandatory mathematical duties named in the unchanged contract and in the
accepted replacements have a selected source paragraph above: actual objects
and entries; complete second and third endpoints; full response and model
degree; finite precritical/critical proofs; all three negative windows; raw
integrality before reference; finite low solutions; full Ward; actual ghost;
accurate quadratic drivers; P/E/M with all finite proof content; and all A23
structural, ratio, and point-value consumers.

There is no unresolved source-locator ambiguity identified by this author
mapping. The controlling manifest must still encode the exact permitted
excerpts, including the sub-Step A17 raw-integrality paragraphs and the F2
translation clarification. This statement records mapping coverage only; it
does not establish a new mathematical result or independent acceptance.

Preparation read coverage: the original dependency map in full; original
scientific brief §§1--4; all three replacement decisions in full for selection;
F2, R, N, T, I4 in full; O2 definitions/Proof Steps 1--6 and its replacement
boundaries; and P/E/M in full in the preceding same-thread source inventory.
Actual retained A04/A06/A07/A08/A09/A13/A17/A18/A19/A21/A22 interfaces and A23
were directionally read as selected above. Unchanged entrance/window locators
were inherited from the original map and checked by section/identity location;
this was not a fresh full reading or mathematical recheck of every legacy file.
Only this new map was written.
