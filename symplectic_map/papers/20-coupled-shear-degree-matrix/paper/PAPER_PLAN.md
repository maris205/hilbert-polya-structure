# Paper20 — Proof-First Paper Plan

## 1. Locked article identity and artifact boundary

**Working title:** *Coupled Hamiltonian Shear Degree Matrices in \(\mathbb A^4\): an Asymmetric \(g\ge 5\) Family*

**Paper type:** self-contained algebraic-dynamics theory paper. The main body is proof-first; it contains no empirical study, numerical experiment, CAS certificate, dataset, or implementation claim.

This plan is downstream of the frozen source lock at
papers/20-coupled-shear-degree-matrix/experiments/source_lock.json:

- lock SHA-256: 57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581;
- lock bytes/LF: 11,847 / 1;
- ten-author source aggregate: SHA 3b27fe493832559e90ac5dcb059628492074574fe9492d12e500f7da107f7e90, 45,416 bytes, 873 LF;
- source-design review receipt: notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md, SHA c4f456c8d9aee5ac9364abf91dc140e9a0261b09cf1922491a773e8c7d87f2c5, 9,484 bytes, provenance-only and excluded from the author aggregate;
- source-lock review receipt: notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md, SHA b6ba83186b7e8c5db548376c5478260bb6d1b3e3d84d8ff0944f641c185a513a, terminal verdict SOURCE_LOCK_PASS.

PAPER_PLAN.md is a newly authorized downstream planning artifact. It is not inserted into the ten-file source aggregate, does not alter source_lock.json, and does not unlock manuscript, code, figures, experiments, build, transport, upload, or publication paths. The only write authorized in this stage is this file. After its stable hash is reported, the author stops and requests an independent plan review.

## 2. Reader promise and headline theorem

The paper will make one narrow, checkable promise:

> For every integer \(g\ge5\), an explicit composition of two canonical polynomial shears on \(\mathbb A^4\) has an exact two-phase Newton-degree recurrence governed by a positive \(2\times2\) matrix \(C_g=B_gA_g\). The recurrence is protected by an invariant ratio cone, strict old-term dominance, and coefficientwise no-cancellation; the visible coordinate then yields
> \[
> \deg(F_g^n)=e_2^{\mathsf T}C_g^n(1,1)^{\mathsf T},\qquad
> \lambda_1(F_g)=(\sqrt g+1)^2.
> \]
> The value is strictly smaller than the product \((g-1)^2\) of the two elementary shear degrees. “Non-product” is asserted only for the displayed coordinate split and this degree comparison, not as a universal non-conjugacy theorem.

The opening page should state the theorem before discussing broad context. Every later claim is either a consequence of the seven internal lemmas below or a bounded contextual comparison. No external source is used as proof of the recurrence, symplecticity, exceptional set, or novelty.

## 3. Exact mathematical object and notation

Let \(K\) be algebraically closed with \(\operatorname{char}K=0\), let \(g\in\mathbb Z\) with \(g\ge5\), and use coordinates
\[
(q_1,q_2,p_1,p_2)\in\mathbb A^4_K,\qquad
\omega=dq_1\wedge dp_1+dq_2\wedge dp_2.
\]

Define
\[
V(q)=q_1^2q_2^2+q_1^g,\qquad
W(p)=p_1^2p_2^2+p_2^g,
\]
\[
S(q,p)=(q,p+\nabla V(q)),\qquad
T(q,p)=(q+\nabla W(p),p),\qquad
F_g=T\circ S.
\]

The coordinate formula must appear before any degree shorthand:
\[
\widehat p_1=p_1+2q_1q_2^2+gq_1^{g-1},\qquad
\widehat p_2=p_2+2q_1^2q_2,
\]
\[
F_{g,1}=q_1+2\widehat p_1\widehat p_2^2,\qquad
F_{g,2}=q_2+2\widehat p_1^2\widehat p_2+g\widehat p_2^{g-1},
\]
\[
F_{g,3}=\widehat p_1,\qquad F_{g,4}=\widehat p_2.
\]

For \(F_g^n\), write
\[
u_n=(\deg(q_1\circ F_g^n),\deg(q_2\circ F_g^n))^{\mathsf T}.
\]
Let \(v_{n+1}\) be the degree vector after the \(S\)-phase and before the \(T\)-phase. The phase distinction is mandatory: \(v_{n+1}\) is not \(u_n\), and the completed step returns to \(u_{n+1}\).

The selected Newton-face rows are fixed by the displayed support monomials:
\[
A_g=\begin{pmatrix}g-1&0\\2&1\end{pmatrix},\qquad
B_g=\begin{pmatrix}1&2\\0&g-1\end{pmatrix},
\]
\[
C_g=B_gA_g=
\begin{pmatrix}g+3&2\\2(g-1)&g-1\end{pmatrix}.
\]
These are degree-transfer matrices from actual gradient monomials, not arbitrary Jacobian matrices and not a generic Newton-fan construction.

Use the half-open cone
\[
\mathcal C_g=\{u\in\mathbb R_{>0}^2:1\le r=u_2/u_1<(g-2)/2\}.
\]
The initial vector is \(u_0=(1,1)^{\mathsf T}\).

## 4. Theorem and proof dependency order

The main theorem will be preceded by seven lemmas in the following order. Cross-references must use these identifiers consistently.

### L1 — Canonicality and explicit inverses

Show
\[
S^{-1}(q,p)=(q,p-\nabla V(q)),\qquad
T^{-1}(q,p)=(q-\nabla W(p),p),
\]
so \(S,T,F_g\) are polynomial automorphisms. Compute
\[
S^*\omega=\sum_i dq_i\wedge d(p_i+\partial_iV)
=\omega+\sum_{i,j}\partial_{ij}V\,dq_i\wedge dq_j=\omega
\]
by Hessian symmetry; repeat for \(T\). Record that \(\operatorname{char}K=0\) is not needed for this differential identity but is needed later for positive coefficients.

### L2 — First-shear selector

For \(u\in\mathcal C_g\), compare the two first-row candidate degrees
\[
u_1+2u_2,\qquad (g-1)u_1.
\]
The strict upper-cone inequality gives
\(u_1+2u_2<(g-1)u_1\), so \(q_1^g\) is selected. The second row selects \(q_1^2q_2^2\), giving \(v=A_gu\). Include the carried \(p\)-coordinate inequalities, including the base case \(u_0=v_0=(1,1)\), rather than silently dropping old terms.

### L3 — Second-shear selector

For \(v=A_gu\), the first \(T\)-row selects \(p_1^2p_2^2\). The second row compares
\[
2v_1+v_2\quad\text{with}\quad(g-1)v_2.
\]
Since
\[
v_2/v_1=(2+r)/(g-1)\ge3/(g-1)>2/(g-2)
\]
for \(g\ge5\), the \(p_2^g\) face is strict. Thus \(u^+=B_gv\). Explicitly record the carried \(q\)-degree gaps
\[
v_1+2v_2-u_1>0,\qquad (g-1)v_2-u_2>0.
\]

### L4 — Two-stage cone invariance

For \(r=u_2/u_1\), derive
\[
f_g(r)=\frac{(g-1)(2+r)}{g+3+2r}.
\]
Show \(f_g(1)>1\), and at \(R=(g-2)/2\),
\[
f_g(R)=\frac{(g-1)(g+2)}{2(2g+1)}<R
\]
because the cleared difference is \(g(g-4)>0\). Since \(f_g\) is increasing, \(f_g([1,R))\subset[1,R)\). Also prove \(C_gu>u\) componentwise.

The proof must explicitly reject the tempting but false single strict cone
\(\{Au>v,\ Bv>u\}\): after the \(S\)-phase the protocol has the exact phase-return equality \(v_{n+1}=A_gu_n\). The invariant object is a two-stage cone with a phase label, not a strict inequality across the phase boundary.

### L5 — Old-term dominance and no-cancellation

First prove strict gaps for every carried coordinate. In the \(S\)-phase use
\[
\max\{v_{1,n},u_{1,n}+2u_{2,n}\}<(g-1)u_{1,n},\qquad
v_{2,n}<2u_{1,n}+u_{2,n}.
\]
In the \(T\)-phase use
\[
u_{1,n}<v_{1,n+1}+2v_{2,n+1},\qquad
\max\{u_{2,n},2v_{1,n+1}+v_{2,n+1}\}
<(g-1)v_{2,n+1}.
\]
The induction uses L4 and the componentwise growth \(C_gu>u\); the base step is checked directly from \(u_0=(1,1)\).

Then state the no-cancel lemma in coefficientwise form. Every coefficient generated from the initial coordinate monomials is a nonnegative integer, and selected terms have positive coefficients. Strict face gaps isolate their degrees; characteristic zero prevents a positive integer coefficient from becoming zero. The proof must not claim uniqueness of a monomial when only positivity is needed.

### L6 — Complete-step recurrence and degree visibility

Combine L2–L5:
\[
v_{n+1}=A_gu_n,\qquad
u_{n+1}=B_gv_{n+1}=C_gu_n.
\]
Use
\[
C_g-A_g=
\begin{pmatrix}4&2\\2g-4&g-2\end{pmatrix}>0
\]
to show the final \(q\)-degrees dominate the preceding \(p\)-degrees. L4 gives \(u_{n,2}>u_{n,1}\) for \(n\ge1\). Therefore \(q_2\) is a visible Perron coordinate and
\[
\deg(F_g^n)=e_2^{\mathsf T}C_g^n(1,1)^{\mathsf T},\qquad n\ge1.
\]
This is the visibility step; it cannot be replaced by a spectral-radius assertion alone.

### L7 — Perron–Frobenius and dynamical degree

Compute
\[
\operatorname{tr}C_g=2g+2,\qquad
\det C_g=(g-1)^2,\qquad
\operatorname{disc}=16g.
\]
Hence
\[
\lambda_\pm=g+1\pm2\sqrt g=(\sqrt g\pm1)^2.
\]
Because \(C_g\) is strictly positive, Perron–Frobenius gives a positive dominant eigenvector. Since \(e_2\) and \((1,1)^{\mathsf T}\) see that class by L6,
\[
\lim_{n\to\infty}\deg(F_g^n)^{1/n}
=\rho(C_g)=(\sqrt g+1)^2.
\]

## 5. Headline theorem statement

State exactly:

**Theorem (asymmetric coupled-shear degree matrix).** For every integer \(g\ge5\), \(F_g=T\circ S\) is a symplectic polynomial automorphism of \(\mathbb A^4_K\), its degrees obey
\[
\deg(F_g^n)=e_2^{\mathsf T}C_g^n(1,1)^{\mathsf T}\quad(n\ge1),
\]
and
\[
\lambda_1(F_g)=(\sqrt g+1)^2.
\]
Each elementary shear has polynomial degree \(g-1\), while
\[
(\sqrt g+1)^2<(g-1)^2\qquad(g\ge5).
\]
The mixed monomials make the displayed coordinate support connected, so the map is not a product with respect to this coordinate split. No assertion is made about conjugacy to products in other coordinates.

The proof invokes L1–L7 in order and no external theorem beyond the standard definition of the first dynamical degree and Perron–Frobenius.

## 6. Proof-first section and page plan

The target is 24 substantive pages, measured from the first page through the conclusion and excluding references, acknowledgements, and any optional appendix. There will be no experiments, figure generation, or computational appendix. A single hand-typeset comparison table is permitted; it is not an experimental result.

| Section | Substantive target | Required contents and proof checkpoint |
|---|---:|---|
| Abstract and theorem preview | 0.5 pp | Family, exact recurrence, \(\lambda_1\), narrow non-product meaning, explicit limitation. |
| 1. Introduction | 2.0 pp | What/why/so-what; degree growth versus canonicality; one-sentence contribution; four falsifiable contributions; preview of \(A_g,B_g,C_g\). |
| 2. Bounded related work and collision boundary | 1.5 pp | Planar degree-product context, higher-dimensional context, spectral terminology, nearest 4D coupled-Hénon neighbor; P12–P19 boundary table. |
| 3. Fixed family and phase notation | 2.5 pp | Potentials, coordinate formula, phase labels, degree vectors, actual support rows, cone, and the distinction between gradient rows and Jacobian rows. |
| 4. Symplecticity and inverse maps | 1.5 pp | L1 with pullback calculation and triangular inverses; no appeal to citation as proof. |
| 5. First Newton-face selector | 2.5 pp | L2, carried-term comparisons, strict face gap, base case, and exact meaning of \(A_g\). |
| 6. Second selector and complete-step matrix | 2.5 pp | L3, \(v=A_gu\), exact \(B_g\), multiplication \(C_g=B_gA_g\), and half-step matrix warning. |
| 7. Two-stage cone invariance | 2.5 pp | L4, fractional-linear ratio map, endpoint inequalities, componentwise growth, phase-return equality. |
| 8. Old-term dominance and no-cancellation | 2.0 pp | L5, all displayed inequalities, coefficientwise positivity, characteristic-zero role, no hidden genericity. |
| 9. Exact recurrence and visibility | 2.0 pp | L6, \(C_g-A_g\), \(q_2\) dominance, total-degree identity, induction closure. |
| 10. Perron root and dynamical degree | 1.5 pp | L7, characteristic polynomial, PF accessibility, limit. |
| 11. Non-product comparison and \(g=5\) audit | 2.0 pp | Strict comparison with \((g-1)^2\), connected support at the declared split, explicit \(C_5\) sanity line. |
| 12. Limitations, anti-claims, and conclusion | 1.0 pp | What is not proved, STOP conditions, bounded future work, concise restatement. |
| **Total** | **24.0 pp** | Proof obligations remain in the main body; no experiment section. |

### 6.1 Abstract and introduction deliverables

The abstract must contain the exact family and result, not generic “Newton polytope” language. The introduction must front-load:

1. the map \(F_g\) and why canonical shears impose a meaningful constraint;
2. the gap between a half-step transfer picture and the complete matrix \(B_gA_g\);
3. the two-stage cone and strict old-term gaps;
4. the visible-coordinate argument needed to turn \(\rho(C_g)\) into total degree;
5. the limited meaning of non-product.

The introduction will end with contributions that are all internally provable:

- an explicit symplectic automorphism family and inverse formula;
- a uniform two-phase selector/cone proof for every \(g\ge5\);
- an exact degree recurrence and closed-form dynamical degree;
- a strict, coordinate-scoped comparison against the elementary degree product.

### 6.2 Related-work and citation scaffolding

Organize related work by question, not paper-by-paper:

- planar degree-product and normal-form background: S01;
- higher-dimensional degree-growth context: S02 and S03;
- dynamical-degree/spectral terminology: S03 and S05;
- plane valuation/compactification historical context: S04;
- nearest four-dimensional coupled-Hénon hyperbolicity neighbor: S06.

S07 may be used only as a clearly labeled survey/context pointer if needed. Citations are verified in notes/CITATION_VERIFICATION.md and are not proof authority. Do not claim that any source proves the \(g\ge5\) family, the finite selector, the cone, the matrix root, or priority.

### 6.3 Main proof presentation

Every selector inequality should be shown once in a boxed or otherwise visibly separated display, followed immediately by the carried-term comparison it controls. The proof must keep phase labels \(q\)-phase, intermediate \(p\)-phase, and complete-step return visible in notation. The matrix warning belongs adjacent to the computation
\[
B_gA_g=
\begin{pmatrix}1&2\\0&g-1\end{pmatrix}
\begin{pmatrix}g-1&0\\2&1\end{pmatrix}
=
\begin{pmatrix}g+3&2\\2(g-1)&g-1\end{pmatrix}.
\]
Do not introduce the off-diagonal stacked matrix as if it were the theorem matrix; if it is displayed for comparison, state that it encodes two half-steps and requires a period correction.

### 6.4 Explicit \(g=5\) audit

Include one symbolic, non-experimental check:
\[
A_5=\begin{pmatrix}4&0\\2&1\end{pmatrix},\quad
B_5=\begin{pmatrix}1&2\\0&4\end{pmatrix},\quad
C_5=\begin{pmatrix}8&2\\8&4\end{pmatrix},
\]
\[
\rho(C_5)=6+2\sqrt5<16=(5-1)^2.
\]
This is a hand calculation, not a numerical experiment or CAS certificate. It is included to make the phase order and non-product comparison immediately checkable.

## 7. Non-product comparison: exact boundary

The word “non-product” has three and only three allowed uses:

1. \(V\) and \(W\) contain mixed support monomials \(q_1^2q_2^2\) and \(p_1^2p_2^2\), so the support graph is connected in the displayed split;
2. the complete transfer matrix \(C_g\) has off-diagonal entries and is not the diagonal matrix of two independent scalar recurrences;
3. the measured dynamical degree is strictly below \(\deg(S)\deg(T)=(g-1)^2\).

The paper will not claim non-conjugacy to a product under arbitrary polynomial or symplectic coordinate changes, nor classify all coupled shears. The comparison is with the product baseline only, not with a universal theorem about all Hénon-like maps.

## 8. P12–P19 collision matrix

At the locked object boundary every row is EMPTY. The manuscript should reproduce this compact table and its boundary language.

| Ledger | Neighboring object | Paper20 boundary | Status |
|---|---|---|---|
| P12 | Residue/period-three arithmetic and clock strata | No residue classes, period-three data, or arithmetic clocks | EMPTY |
| P13 | Primitive exact-period covers and cyclic orbit quotients | No periodic points, orbit quotients, or dynatomic schemes | EMPTY |
| P14 | Support-one torus escape and finite-rank map geometry | No torus survivors, character lattices, or escape classification | EMPTY |
| P15 | Pure-trace/Jacobian fibers and quasi-finite loci | No trace coordinates, Jacobian fibers, or ramification | EMPTY |
| P16 | Support-size torus escape bounds | No support-size counting or finite-rank torus map | EMPTY |
| P17 | Fixed-lag shift-like recurrence and torus-coset dimension | No recurrence variety, lag word, character extinction, or coset dimension | EMPTY |
| P18 | Marked trace coordinates and scheme-theoretic boundary ramification | No trace marking, boundary scheme, or branch divisor | EMPTY |
| P19 | Maximum-dimensional translates, coefficientwise moduli, support-one GCD obstruction | No translates, GCD obstruction, effective height, or periodic classification | EMPTY |

The text must add that the table is a bounded ledger result, not an exhaustive priority search. P1–P11 remain outside the object boundary and are not silently reclassified.

## 9. Claims–evidence matrix for drafting

| Claim ID | Draft claim | Internal evidence location | External citation role | Stop if |
|---|---|---|---|---|
| C01 | \(S,T\) are canonical polynomial automorphisms | L1 | None | Pullback or inverse is incomplete |
| C02 | The displayed coordinate formula is exact | Section 3 | None | Any derivative or phase label differs |
| C03 | \(S\) selects \(A_g\) on \(\mathcal C_g\) | L2 | None | A tie or carried term is untracked |
| C04 | \(T\) selects \(B_g\) after \(v=A_gu\) | L3 | None | The \(p_2^g\) inequality fails |
| C05 | \(f_g\) preserves the half-open cone | L4 | None | Endpoint or monotonicity proof is missing |
| C06 | \(C_g=B_gA_g\) is the complete-step matrix | L4/L6 | None | Half-step matrix is substituted |
| C07 | Old terms are strictly dominated | L5 | None | Any displayed gap is non-strict |
| C08 | No cancellation occurs | L5 | None | Sign/characteristic assumption is omitted |
| C09 | \(u_{n+1}=C_gu_n\) exactly | L6 | None | Induction does not close |
| C10 | \(q_2\) sees total degree | L6 | None | PF accessibility is only asserted |
| C11 | \(\rho(C_g)=(\sqrt g+1)^2\) | L7 | None | Matrix arithmetic is not shown |
| C12 | \(\lambda_1(F_g)\) equals that root | L6/L7 | S03/S05 context only | Visibility or limit is absent |
| C13 | Each shear has degree \(g-1\) | Section 3/L2/L3 | None | Degree convention is ambiguous |
| C14 | The displayed split is coupled and non-product in the narrow sense | Section 11 | None | Universal conjugacy language appears |
| C15 | \(g=5\) audit is consistent | Section 11 | None | Arithmetic check disagrees |
| C16 | P12–P19 rows are empty at scope | Section 8 | None | A neighboring object is overclaimed |
| C17 | Citation roles are context-only | Related work | S01–S07 | A citation is promoted to proof |
| C18 | Anti-claims and STOP rules are visible | Section 12 | None | A forbidden claim remains |
| C19 | No experiments or implementation evidence are needed | Artifact boundary | None | Numerical/CAS language enters proof |
| C20 | Source lock and permissions remain unchanged | Front matter/end matter | Source lock only | Plan edits lock or downstream paths |

## 10. Anti-claims and hard STOP conditions

The final paper plan must carry these anti-claims forward verbatim in substance:

- no theorem for arbitrary sparse potentials, arbitrary coefficients, or arbitrary shear words;
- no positive-characteristic specialization;
- no classification of all symplectic polynomial automorphisms or all finite Newton fans;
- no equality claim between algebraic, topological, arithmetic, or measure-theoretic entropy;
- no periodic-point counts, trace/multiplier/centralizer/invariant-curve theorem, torus translate, or arithmetic-moduli statement;
- no universal non-conjugacy-to-product theorem;
- no numerical or CAS output as a proof certificate;
- no absolute novelty, firstness, or exhaustive priority claim.

Stop drafting and return to proof review if any of these occur:

1. a selector tie or untracked carried coordinate appears at any iterate;
2. the proof uses one strict cone across both phases despite \(v_{n+1}=A_gu_n\);
3. the half-step matrix is used without the complete-step/period correction;
4. coefficient signs or characteristic assumptions permit cancellation;
5. \(e_2\) is not shown to reach and observe the Perron class;
6. mixed support disappears or the map becomes block-separable at the declared object;
7. a source is cited as proving the new recurrence or as establishing priority;
8. the plan expands into experiments, code, figures, main.tex, references.bib, build, release, or transport.

## 11. Permissions and lifecycle

This stage has exactly one authorized write: paper/PAPER_PLAN.md. The following remain forbidden:

- changing any source-locked author file;
- changing experiments/source_lock.json;
- creating main.tex, references.bib, source code, data, figures, results, build artifacts, or transport;
- running CAS, numerical, symbolic, or scientific experiments;
- uploading, publishing, or making a release claim.

The independent plan reviewer must read the frozen source lock, this plan, and the bounded author package; independently check the theorem statement, phase recurrence, all selector and dominance inequalities, page arithmetic, collision table, citation roles, anti-claims, and permission boundary; and write its own review artifact only after the author stop. The author must not edit this plan while that review pass is active.

## 12. Final plan acceptance checklist

Before handing off for review, verify:

- [ ] The theorem uses exactly \(g\ge5\), \(\mathbb A^4_K\), the displayed \(V,W,S,T,F_g\), and \(C_g=B_gA_g\).
- [ ] L1–L7 are ordered and every main claim has an internal proof location.
- [ ] Symplecticity and explicit inverse maps are both planned.
- [ ] The two-stage cone, phase-return equality, and ratio endpoint inequalities are explicit.
- [ ] Old-term dominance and coefficientwise no-cancellation are separate proof obligations.
- [ ] \(C_g\), PF positivity, and \(e_2\)-visibility are all required before the dynamical-degree conclusion.
- [ ] The non-product comparison is narrow and strict, with no universal conjugacy claim.
- [ ] P12–P19 collision rows and bounded-citation roles are explicit.
- [ ] Anti-claims and every hard STOP rule are carried into the conclusion.
- [ ] The substantive page total is exactly 24.0 pages, within the authorized 22–26 range.
- [ ] No experiment, figure, code, build, release, or transport path is enabled.
- [ ] The source-lock path, SHA, aggregate identity, review receipts, and downstream-file boundary are recorded.
- [ ] After this file is hashed, AUTHOR STOP is declared and independent plan review is requested.
