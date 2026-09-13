# Paper Plan

**Title**: Forced Period-Two Selector Exchange in Two-Mode Hamiltonian Product Shears

**Author placeholder**: Anonymous

**Article type**: proof-first mathematical dynamics article

**Venue status**: no submission venue selected at this stage

**Date**: 2026-08-25

**Main-body content-page target**: 26.0 pages exactly, inside the locked 22--30 content-page band and preferred 24--28 band

**Manuscript architecture**: abstract plus eight numbered sections; all theorem-critical proofs remain in the main body; no proof appendix; no figures, plots, datasets, code artifacts, empirical tables, or computational certificates

**Frozen theorem data**: over a characteristic-zero field \(K\), with integers \(m\ge2\), \(s\ge1\), and nonzero coefficients \(A,B,C,D\in K^\times\),

\[
V_m(q)=Aq_1^m q_2^2+Bq_1q_2^{2m},
\qquad
W_{m,s}(p)=Cp_1^{s(2m+1)+1}+Dp_2^{sm+1},
\]

\[
S(q,p)=(q,p+\nabla V_m(q)),
\qquad
T(q,p)=(q+\nabla W_{m,s}(p),p),
\qquad
F_{m,s}=T\circ S.
\]

The public contribution remains exactly the bounded delta

\[
\text{forced wall fixing}
\Longrightarrow
\text{strict period-two selector exchange}
\Longrightarrow
\text{two-step monodromy}
\Longrightarrow
\text{exact parity degree laws}.
\]

No venue-default structure, bibliography generation, empirical storyline, or appendix-proof migration is permitted in this plan.

## Public theorem frame

The introduction will front-load a single explicit main theorem statement for the frozen family and then prove it in a rigid order across \(\S\)2--\(\S\)6:

1. literal gradients, subtraction inverses, and symplecticity;
2. common wall \(r=2\), selector rows, and exact matrices \(A_-,A_+,B_m\);
3. corrected branch algebra and strict chamber exchange off the wall;
4. both temporal carry phases and arbitrary-nonzero top-form survival;
5. \(q_1\) visibility for \(n\ge1\), the exact monodromy \(P=(B_mA_+)(B_mA_-)\), both right eigenpairs, explicit determinant derivation, and \(\lambda_1(F_{m,s})=sm(2m+1)\);
6. recurrence, exact initials including corrected \(u_3\), wall gaps, full even-vector formula, both parity closed forms, and matrix-based integrality;
7. the bounded crossed-binomial iff lemma plus the explicit \((m,s)\) realization, and the six-hypothesis conditional period-\(k\) lemma as technique only;
8. the limitations and anti-claims firewall.

The paper never treats \(r=2\) as part of the theorem, never treats positivity as theorem evidence, never reverses the phase order, and never transfers proof burden to citations or computation.

## Claims--Evidence Matrix

Every public claim below is mapped to a specific main-body location and a local proof object. Citations serve only contextual positioning; they never certify selector inequalities, carry, visibility, matrix identities, or spectra.

### Headline claims

| ID | Role | Public claim | Main-body location | Exact local proof evidence |
|---|---|---|---|---|
| H1 | headline | The ordinary degree orbit for the explicit family crosses the wall \(r=2\) every step and alternates strictly between the chambers \(r<2\) and \(r>2\). | \(\S\)3 | Proposition 3.1 plus Corollary 3.2 using (3.1)--(3.7), with the corrected \(\ell_m(r)-1\) and \(2-\ell_m(r)\) identities and explicit wall exclusion. |
| H2 | headline | The selector story lifts to actual polynomial degrees: both carry phases close, arbitrary nonzero coefficients survive, and \(q_1\) is the visible total-degree coordinate for \(n\ge1\). | \(\S\)4--\(\S\)5 | Proposition 4.1, Proposition 4.2, and Proposition 5.1 using (4.1)--(4.9) and (5.1)--(5.4); no computation or positivity shortcut. |
| H3 | headline | The strict period-two selector exchange yields an exact two-step monodromy \(P=(B_mA_+)(B_mA_-)\) with both eigenpairs, explicit determinant derivation, and \(\lambda_1(F_{m,s})=sm(2m+1)\). | \(\S\)5 | Proposition 5.2 and Corollary 5.3 using (5.5)--(5.12), including the displayed \(ad-bc\) expansion before \(\det(P)=HL\). |
| H4 | headline | The visible degree sequence has exact recurrence, exact initials, exact wall gaps, full even-vector decomposition, odd visible closed form, and matrix-based integrality. | \(\S\)6 | Proposition 6.1, Proposition 6.2, and Proposition 6.3 using (6.1)--(6.13), including corrected \(u_3\). |

### Supporting theorem claims

| ID | Public claim | Main-body location | Exact local proof evidence | Scope limiter |
|---|---|---|---|---|
| C1 | \(S\) and \(T\) are polynomial symplectomorphisms. | \(\S\)2 | Lemma 2.1 from (2.3)--(2.9): literal gradients, subtraction inverses, Hessian-block Jacobians, \(J^\mathsf{T}\Omega J=\Omega\). | characteristic zero and nonzero coefficients only |
| C2 | The two competitive \(V\)-rows switch synchronously at \(r=2\). | \(\S\)2 | Lemma 2.2 from (2.10)--(2.14): both weighted differences equal \((m-1)(u_1-2u_2)\). | \(m\ge2\) |
| C3 | The selected first-phase matrices are exactly \(A_-\) and \(A_+\). | \(\S\)2 | Lemma 2.2 from the literal support rows (2.15)--(2.16). | no altered support profile |
| C4 | \(h_m(r)\) and \(\ell_m(r)\) are the exact projective branch maps. | \(\S\)3 | Proposition 3.1 from direct multiplication by \(sB_mA_\pm\) in (3.1)--(3.2). | phase order fixed as \(F=T\circ S\) |
| C5 | \(0<r<2\Rightarrow h_m(r)>2\) and \(r>2\Rightarrow 1<\ell_m(r)<2\). | \(\S\)3 | Proposition 3.1 from (3.3)--(3.5), with corrected formulas for \(h_m(r)-2\), \(\ell_m(r)-1\), and \(2-\ell_m(r)\). | wall excluded |
| C6 | The ordinary seed follows the strict itinerary \(-,+,-,+,\dots\). | \(\S\)3 | Corollary 3.2 from \(r_0=1\), (3.6), and the inequalities in Proposition 3.1. | seed-specific theorem |
| C7 | Fresh first-phase rows beat carried momentum coordinates. | \(\S\)4 | Proposition 4.1 from (4.1), (4.3), (4.4)--(4.7). | selector choice alone is insufficient |
| C8 | Fresh second-phase rows beat carried position coordinates. | \(\S\)4 | Proposition 4.1 from the chamberwise \(u_{n+1}=sB_mv_{n+1}\) inequalities in (4.8). | no asymptotic-in-\(s\) shortcut |
| C9 | Selected leading forms survive for arbitrary nonzero \(A,B,C,D\). | \(\S\)4 | Proposition 4.2 from (4.9): unique top source plus polynomial-domain argument. | positivity is not theorem evidence |
| C10 | \(q_1\) is visible for every \(n\ge1\). | \(\S\)5 | Proposition 5.1 from (5.1)--(5.3), including the corrected negative-chamber equality (5.2). | \(n=0\) stays tied |
| C11 | \(d_n=\deg(F_{m,s}^n)=u_{n,1}\) for \(n\ge1\). | \(\S\)5 | Proposition 5.1 from visibility plus exact carry and top-form transport; equation (5.4). | ordinary total degree only |
| C12 | \(P=(B_mA_+)(B_mA_-)\) has the displayed entries. | \(\S\)5 | Proposition 5.2 from (5.5)--(5.6), by direct multiplication in the correct order. | reversed product is different |
| C13 | \(H=m^2(2m+1)^2\) and \(L=2m(m+1)\) are the eigenvalues of \(P\). | \(\S\)5 | Proposition 5.2 from (5.7)--(5.11): both right eigenpairs, trace, and determinant derivation. | \(m\ge2\) |
| C14 | \(\lambda_1(F_{m,s})=sm(2m+1)\). | \(\S\)5 | Corollary 5.3 from the Perron eigenvalue of \(s^2P\) and (5.12). | not an entropy-equality claim |
| C15 | The visible degree sequence satisfies \(d_{n+4}=s^2(H+L)d_{n+2}-s^4HLd_n\). | \(\S\)6 | Proposition 6.1 from Cayley--Hamilton on \(s^2P\) together with visibility, via (6.1)--(6.6). | no minimal-polynomial claim |
| C16 | The even and odd wall gaps are exact powers of \(s^2L\). | \(\S\)6 | Proposition 6.2 from the left wall functional identities (6.7)--(6.9). | strict off-wall orbit only |
| C17 | Both parity subsequences admit explicit spectral closed forms. | \(\S\)6 | Proposition 6.3 from (6.10)--(6.12), including the full even-vector decomposition (6.11). | downstream from the matrix law |
| C18 | The crossed-binomial / diagonal-pure-power lemma forces the wall-fixing ratio. | \(\S\)7 | Lemma 7.1 from (7.1)--(7.5); Corollary 7.2 records the explicit \(m,s\) realization (7.6). | ansatz only |
| C19 | The conditional period-\(k\) selector-to-monodromy statement is correct as a technical lemma. | \(\S\)7 | Lemma 7.3 from the six displayed hypotheses and conclusion in (7.7)--(7.8). | nonheadline technique only |

### Boundary, nonclaim, and failure claims

| ID | Boundary claim | Main-body location | Exact local proof evidence | Public restriction |
|---|---|---|---|---|
| B1 | The wall \(r=2\) is a genuine tie boundary and is excluded from every strict theorem statement. | \(\S\)3 and \(\S\)8 | Equation (3.7) plus the boundary list in \(\S\)8. | no theorem on the wall |
| B2 | The theorem requires \(m\ge2\); at \(m=1\) the switching factor vanishes. | \(\S\)8 | Boundary item derived from the row-difference factor in (2.13)--(2.14). | no \(m=1\) extension |
| B3 | Zero coefficients change the support profile and leave the frozen theorem. | \(\S\)4 and \(\S\)8 | Proposition 4.2 uses nonzero coefficients; \(\S\)8 records the changed-support failure. | no vanishing-coefficient claim |
| B4 | Positive characteristic can kill derivative scalars, so the theorem is characteristic-zero only. | \(\S\)2, \(\S\)4, and \(\S\)8 | Lemma 2.1 and Proposition 4.2 depend on nonvanishing derivative scalars. | no positive-characteristic validity |
| B5 | Carry is indispensable; weighted support alone does not prove actual polynomial degrees. | \(\S\)4 and \(\S\)8 | Proposition 4.1 is explicit and cannot be skipped. | no tropical-only proof |
| B6 | Visibility is indispensable; without it \(u_{n,1}\) is only a candidate observable. | \(\S\)5 and \(\S\)8 | Proposition 5.1 is cited explicitly in the scalar degree step. | no implicit observable claim |
| B7 | The structural lemma does not itself prove carry, visibility, or actual polynomial degree transport. | \(\S\)7 and \(\S\)8 | Lemma 7.1 concludes only the iff ratio; separate-obligation warning appears immediately after the proof. | no overclaim beyond the ansatz |
| B8 | If \(R=1\) in the structural lemma, the ordinary seed lies on the wall and no strict seed theorem follows. | \(\S\)7 and \(\S\)8 | Corollary 7.2 plus the explicit \(R=1\) warning in the structural-lemma discussion. | no seed theorem from \(R=1\) |
| B9 | The paper claims strict period two only, not arbitrary periods, automata, or general selector fans. | \(\S\)1, \(\S\)7, and \(\S\)8 | Contribution list, Lemma 7.3’s conditional status, and the anti-claim list. | no period \(>2\) or automaton theorem |
| B10 | The period-\(k\) lemma is technical support, not the novelty headline. | \(\S\)1 and \(\S\)7 | Intro contribution framing plus Lemma 7.3 heading and proof. | no novelty inflation |
| B11 | The paper makes no first-Perron, first-tropical-switching, or absolute-priority claim. | \(\S\)1 and \(\S\)8 | Bounded positioning language only; contextual source plan forbids priority transfer. | no firstness claim |
| B12 | No theorem-critical claim is proved by citation, CAS, numerical spectra, scans, code, or data. | \(\S\)1 and \(\S\)8 | Evidence matrix plus zero-science statement in the conclusion/limitations firewall. | no computational proof |

## Planned manuscript structure and exact page budget

The manuscript itself has one abstract and exactly eight numbered sections.

| Manuscript component | Content pages |
|---|---:|
| Abstract | 0.5 |
| \(\S\)1 Introduction, theorem preview, and bounded positioning | 3.0 |
| \(\S\)2 Family, inverses, symplecticity, and support rows | 3.0 |
| \(\S\)3 Common wall, branch algebra, and strict selector exchange | 3.5 |
| \(\S\)4 Temporal carry and arbitrary-nonzero top homogeneous survival | 4.0 |
| \(\S\)5 \(q_1\) visibility, monodromy, determinant, and spectrum | 3.5 |
| \(\S\)6 Recurrence, wall gaps, parity closed forms, and integrality | 4.0 |
| \(\S\)7 Bounded structural lemma and conditional period-\(k\) lemma | 2.5 |
| \(\S\)8 Boundaries, coefficient scope, limitations, and conclusion | 2.0 |
| **Total** | **26.0** |

References are excluded from the 26.0-page count. There is no proof appendix.

## Section-by-section blueprint

### Abstract — 0.5 pages

The abstract will do four things and nothing else:

1. state the exact family \(V_m,W_{m,s},F_{m,s}=T\circ S\) with characteristic-zero and nonzero-coefficient scope;
2. state the strict period-two wall exchange off \(r=2\);
3. state the exact monodromy and degree-law outputs \(\lambda_1(F_{m,s})=sm(2m+1)\) and the stride-two recurrence;
4. state the bounded nature of the contribution: explicit family, true carry/visibility proof, exact parity laws, no priority claim.

It will not mention internal governance, hashes, local paths, reviewers, or any unselected venue.

### \(\S\)1 Introduction, theorem preview, and bounded positioning — 3.0 pages

Working subsection budget:

- 0.7 pages: problem setting and why stationary-selector predecessors do not cover this orbit;
- 0.8 pages: exact statement of Theorem 1.1 with the frozen family and public delta;
- 0.9 pages: bounded contextual positioning against Papers 20--23 and S01--S09;
- 0.6 pages: contribution list, section roadmap, and limitations firewall.

Planned content:

- Open with the contrast between the stationary-selector regime of Paper 20 and the present forced wall-crossing regime.
- State Theorem 1.1 in full, but defer proof to \(\S\)2--\(\S\)6.
- Front-load the four public contributions:
  1. explicit two-mode Hamiltonian product shears with a common wall \(r=2\);
  2. strict period-two selector exchange of the ordinary orbit;
  3. true polynomial carry / no-cancellation / visibility proof for arbitrary nonzero coefficients;
  4. exact two-step monodromy, recurrence, wall gaps, and parity laws.
- Include a bounded positioning paragraph on Papers 20--23 and a second bounded positioning paragraph on S01--S09; no standalone related-work section.
- Explicitly announce the anti-claims: no theorem on the wall, no period \(>2\), no general selector classification, no firstness claim, no computational certificate.

Planned theorem placement:

- **Theorem 1.1 (Main theorem)**: exact family, strict exchange, visibility, monodromy, dynamical degree, recurrence, and wall gaps.
- Final sentence of the section: “Sections 2--6 prove Theorem 1.1 in order; Section 7 records the bounded structural and conditional technique lemmas; Section 8 seals the scope boundary.”

### \(\S\)2 Family, inverses, symplecticity, and support rows — 3.0 pages

Working subsection budget:

- 0.5 pages: notation and exact family;
- 0.9 pages: literal gradients and subtraction inverses;
- 0.7 pages: symplecticity by Hessian blocks;
- 0.9 pages: support rows, common wall, and branch matrices.

Planned equations and displays:

- (2.1) \(V_m(q)\), \(W_{m,s}(p)\).
- (2.2) \(S(q,p)\), \(T(q,p)\), \(F_{m,s}=T\circ S\).
- (2.3)--(2.6) all four gradient coordinates.
- (2.7) the subtraction inverses \(S^{-1}\) and \(T^{-1}\).
- (2.8) Jacobian block forms with the symmetric Hessians.
- (2.9) \(J_S^{\mathsf T}\Omega J_S=\Omega\) and \(J_T^{\mathsf T}\Omega J_T=\Omega\).
- (2.10)--(2.13) weighted scores of the competitive rows and their common factor.
- (2.14) the exact wall \(r=u_1/u_2=2\).
- (2.15)--(2.18) \(A_-,A_+,B_m,C_-,C_+\).

Planned statements:

- **Lemma 2.1**: literal gradients, inverses, and symplecticity.
- **Lemma 2.2**: exact support rows, common wall, and selected matrices.

Proof-order note:

The section proves the family is an exact-gradient polynomial symplectomorphism before any degree argument begins. It then establishes the literal support ledger needed for the branch analysis. No citation or sample calculation substitutes for (2.3)--(2.18).

Transition to \(\S\)3:

The section closes with “With \(A_-,A_+,B_m\) fixed literally, the only remaining selector question is how the projective ratio moves across the wall.”

### \(\S\)3 Common wall, branch algebra, and strict selector exchange — 3.5 pages

Working subsection budget:

- 1.0 pages: derivation of \(h_m(r)\) and \(\ell_m(r)\);
- 1.2 pages: corrected branch-difference identities and chamber images;
- 0.7 pages: strict itinerary of the seed;
- 0.6 pages: explicit wall exclusion and theorem phrasing.

Planned equations and displays:

- (3.1) \(h_m(r)=\dfrac{2(2m+1)}{r+2m-1}\).
- (3.2) \(\ell_m(r)=\dfrac{(2m+1)((m-1)r+2)}{m(mr+1)}\).
- (3.3) \(h_m(r)-2=\dfrac{2(2-r)}{r+2m-1}\).
- (3.4) corrected \(\ell_m(r)-1=\dfrac{(m^2-m-1)r+3m+2}{m(mr+1)}\).
- (3.5) corrected \(2-\ell_m(r)=\dfrac{(m+1)(r-2)}{m(mr+1)}\).
- (3.6) the itinerary \(A_-,A_+,A_-,A_+,\dots\).
- (3.7) \(h_m(r)=2\iff r=2\) and \(\ell_m(r)=2\iff r=2\).

Planned statements:

- **Proposition 3.1**: exact branch formulas and strict chamber images.
- **Corollary 3.2**: strict seed itinerary and explicit wall exclusion.

Correction precedence locked here:

1. the corrected numerator in \(\ell_m(r)-1\) from the R1 correction;
2. the corrected factor \((m+1)\) in \(2-\ell_m(r)\) from the R2 correction.

Proof-order note:

The wall exclusion is not deferred to limitations; it is part of the main theorem phrasing in this section. The paper will explicitly say that the strict exchange theorem is off-wall only.

Transition to \(\S\)4:

The section ends by saying that branch exchange alone is not yet an actual polynomial-degree theorem; the carried coordinates must still be beaten in both phases.

### \(\S\)4 Temporal carry and arbitrary-nonzero top homogeneous survival — 4.0 pages

Working subsection budget:

- 0.8 pages: seed carry;
- 1.2 pages: later first-phase carry in both chambers;
- 1.0 pages: later second-phase carry in both chambers;
- 1.0 pages: top homogeneous parts and no cancellation for arbitrary nonzero coefficients.

Planned equations and displays:

- (4.1) \(A_-(1,1)^{\mathsf T}=(2m,2m)^{\mathsf T}>(1,1)^{\mathsf T}\).
- (4.2) \(sB_mA_-(1,1)^{\mathsf T}=(2m(2m+1)s,2m^2s)^{\mathsf T}>(1,1)^{\mathsf T}\).
- (4.3) carried momentum degrees \(\deg p_n=\bigl(u_{n,1}/(s(2m+1)),u_{n,2}/(sm)\bigr)\).
- (4.4)--(4.5) chamber-\(-\) first-phase inequalities.
- (4.6)--(4.7) chamber-\(+\) first-phase inequalities.
- (4.8) the chamberwise second-phase inequalities \(s(2m+1)v_1>u_1\) and \(smv_2>u_2\).
- (4.9) a displayed “unique selected top source + domain + nonzero derivative scalars” survival statement.

Planned statements:

- **Proposition 4.1**: exact temporal carry in both phases and both chambers, already at \(s=1\).
- **Proposition 4.2**: arbitrary nonzero coefficients and top homogeneous survival.

Locked proof requirements:

- both carry phases must appear separately;
- no large-\(s\) or asymptotic shortcut;
- positivity language is forbidden as theorem evidence;
- the manuscript must say explicitly that \(K[q_1,q_2,p_1,p_2]\) is a domain and the derivative scalars stay nonzero in characteristic zero.

Transition to \(\S\)5:

The section ends with: “Once the selected top forms are certified to survive, the remaining task is to identify a coordinate that sees the true total degree and to close the exact spectral law.”

### \(\S\)5 \(q_1\) visibility, monodromy, determinant, and spectrum — 3.5 pages

Working subsection budget:

- 1.0 pages: \(q_1\) versus \(q_2\) and both momentum coordinates;
- 0.9 pages: exact monodromy matrix and product order;
- 1.1 pages: both right eigenpairs, trace, and determinant derivation;
- 0.5 pages: dynamical degree conclusion.

Planned equations and displays:

- (5.1) \(u_{n,1}>u_{n,2}\) for every \(n\ge1\).
- (5.2) corrected negative-chamber visibility equality \(u_{n+1,1}=sm\,h_m(r_n)v_{n+1,2}>v_{n+1,2}\).
- (5.3) positive-chamber difference \(u_{n+1,1}-v_{n+1,2}>0\).
- (5.4) \(d_n=u_{n,1}\) for \(n\ge1\), with \(d_0=1\).
- (5.5) \(P=(B_mA_+)(B_mA_-)\).
- (5.6) the explicit \(2\times2\) matrix \(P\).
- (5.7) the \(H\)-eigenpair \(P(2,1)^{\mathsf T}=H(2,1)^{\mathsf T}\).
- (5.8) the \(L\)-eigenpair \(P\bigl(-(2m+1)(2m^2+m-2),m\bigr)^{\mathsf T}=L\bigl(-(2m+1)(2m^2+m-2),m\bigr)^{\mathsf T}\).
- (5.9) \(\operatorname{tr}(P)=H+L\).
- (5.10) the explicit determinant expansion
  \[
  2m(2m+1)\cdot m^2(4m^2+4m-1)-2m(2m+1)(2m^2+m-2)\cdot m^2
  =2m^3(m+1)(2m+1)^2.
  \]
- (5.11) \(\chi_P(t)=t^2-(H+L)t+HL\).
- (5.12) \(\lambda_1(F_{m,s})=\sqrt{\rho(s^2P)}=sm(2m+1)\).

Planned statements:

- **Proposition 5.1**: \(q_1\) visibility and true total degree.
- **Proposition 5.2**: exact monodromy matrix, both right eigenpairs, trace, and determinant.
- **Corollary 5.3**: dynamical degree.

Correction precedence locked here:

1. the negative-chamber visibility step must state the equality in (5.2) before taking the strict consequence;
2. the determinant line must show the \(ad-bc\) expansion before \(\det(P)=HL\).

Transition to \(\S\)6:

The section closes by noting that the spectral picture is not yet the full theorem; the actual degree sequence still needs recurrence, initials, wall gaps, and parity formulas written explicitly.

### \(\S\)6 Recurrence, wall gaps, parity closed forms, and integrality — 4.0 pages

Working subsection budget:

- 0.9 pages: exact vector laws and recurrence;
- 0.9 pages: initial vectors and corrected \(u_3\);
- 0.8 pages: wall-gap identities and their meaning;
- 1.0 pages: even/odd closed forms and integrality;
- 0.4 pages: summary bridge to the bounded structural lemma.

Planned equations and displays:

- (6.1) \(u_{2j}=(s^2P)^j(1,1)^{\mathsf T}\).
- (6.2) \(u_{2j+1}=sB_mA_-(s^2P)^j(1,1)^{\mathsf T}\).
- (6.3) \(d_{n+4}=s^2(H+L)d_{n+2}-s^4HLd_n\).
- (6.4) \(u_1\) and \(u_2\).
- (6.5) corrected
  \[
  u_3=
  \begin{pmatrix}
  8m^4(m+1)(2m+1)s^3\\
  2m^2(m+1)(2m-1)(2m^2+2m+1)s^3
  \end{pmatrix}.
  \]
- (6.6) \(d_0,d_1,d_2,d_3\).
- (6.7) \(\ell=(1,-2)\), \(\ell C_-=-2ms\,\ell\), \(\ell C_+=-(m+1)s\,\ell\).
- (6.8) \(\delta_{2j}=u_{2j,1}-2u_{2j,2}=-(s^2L)^j\).
- (6.9) \(\delta_{2j+1}=u_{2j+1,1}-2u_{2j+1,2}=2ms(s^2L)^j\).
- (6.10) the even visible closed form for \(d_{2j}\).
- (6.11) the full even-vector decomposition for \(u_{2j}\).
- (6.12) the odd visible closed form for \(d_{2j+1}\).
- (6.13) the matrix-based integrality explanation.

Planned statements:

- **Proposition 6.1**: parity-vector laws, scalar recurrence, and exact initials.
- **Proposition 6.2**: exact wall gaps.
- **Proposition 6.3**: parity closed forms and integrality.

Correction precedence locked here:

- the corrected second coordinate of \(u_3\) must appear wherever \(u_3\) is displayed;
- integrality must be derived from integer matrices / recurrence, not from denominator folklore.

Transition to \(\S\)7:

The section ends by separating the explicit-family theorem from the bounded structural and conditional lemmas that explain why the wall-fixing ratio is rigid and how a future period-\(k\) theorem would have to be formulated.

### \(\S\)7 Bounded structural lemma and conditional period-\(k\) lemma — 2.5 pages

Working subsection budget:

- 1.3 pages: crossed-binomial / diagonal-pure-power iff lemma;
- 0.4 pages: explicit specialization to the Paper 24 family;
- 0.8 pages: technical conditional period-\(k\) lemma and nonheadline warning.

Planned equations and displays:

- (7.1) \(V=Aq_1^a q_2^b+Bq_1^c q_2^d\), \(a>c\ge1\), \(d>b\ge1\), and \(W=Cp_1^{e+1}+Dp_2^{f+1}\).
- (7.2) \(R=(d-b)/(a-c)\) and \(L_{\mathrm{wall}}=aR+b=cR+d\).
- (7.3) \(g_{x,y}(r)=\dfrac ef \dfrac{(x-1)r+y}{xr+y-1}\).
- (7.4) \(g'_{x,y}(r)=-\dfrac ef \dfrac{x+y-1}{(xr+y-1)^2}<0\).
- (7.5) \(g(R)=R \iff \dfrac ef=\dfrac{R(L_{\mathrm{wall}}-1)}{L_{\mathrm{wall}}-R}\).
- (7.6) specialization \(R=2\), \(L_{\mathrm{wall}}=2m+2\), \((e,f)=s(2m+1,m)\).
- (7.7) the six hypotheses for the conditional period-\(k\) lemma.
- (7.8) the conclusion \(u_{k\ell+j}=D_jM^\ell u_0\), Cayley--Hamilton residue recurrences, and \(\lambda_1=\rho(M)^{1/k}\) under Perron-class visibility.

Planned statements:

- **Lemma 7.1**: bounded iff ratio inside the crossed-binomial / diagonal-pure-power ansatz.
- **Corollary 7.2**: exact realization of the explicit \(m,s\) family.
- **Lemma 7.3**: conditional period-\(k\) selector-to-monodromy lemma.

Locked warnings:

- Lemma 7.1 proves only the wall-fixing ratio inside the stated ansatz; it does not prove carry, top-form survival, or visibility.
- If \(R=1\), the ordinary seed lies on the wall and no strict seed theorem follows.
- Lemma 7.3 is purely technical and cannot be advertised as the paper’s headline novelty.

Transition to \(\S\)8:

The section ends by returning from the technique lemmas to the explicit-family firewall: what the paper proves, what it does not prove, and why the bounded contribution is still standalone.

### \(\S\)8 Boundaries, coefficient scope, limitations, and conclusion — 2.0 pages

Working subsection budget:

- 0.9 pages: assumption-failure examples and anti-claims;
- 0.6 pages: bounded comparison and limitation statements;
- 0.5 pages: conclusion.

Planned content:

- Collect the hard boundaries in one place:
  - \(r=2\) is excluded;
  - \(m=1\) collapses the switching factor;
  - zero coefficients change the support profile;
  - positive characteristic can kill derivative scalars;
  - omitting carry or visibility destroys the actual-degree theorem;
  - \(R=1\) in the structural lemma does not yield a strict seed theorem.
- Restate the bounded public contribution and bounded noncollision language.
- State explicitly that the paper does not offer any theorem beyond the explicit family and the bounded ansatz lemma.
- Conclude with the exact public-safe summary: explicit family, strict exchange, true carry/visibility, exact monodromy, exact parity laws.

Firewall sentence to include near the end:

“Everything theorem-critical has been proved in the main body; no appendix, computation, or citation transfer is required.”

## Planned mathematical tables and no-figure policy

The manuscript will contain hand-typeset tables only. It will contain zero figures, zero plots, zero diagrams, and zero empirical tables.

Mandatory manuscript tables:

| Table | Planned section | Purpose | Required rows |
|---|---|---|---|
| Table 1 — Selector and branch ledger | \(\S\)2--\(\S\)3 | Record the competitive rows, common wall, branch maps, and corrected branch differences in one auditable place. | mixed/pure rows for each derivative, \(A_-\), \(A_+\), \(B_m\), \(h_m\), \(\ell_m\), \(h_m-2\), \(\ell_m-1\), \(2-\ell_m\), chamber images |
| Table 2 — Carry and visibility ledger | \(\S\)4--\(\S\)5 | Separate base carry, later \(S\)-carry, later \(T\)-carry, and \(q_1\)-visibility comparisons. | seed carry, carried momentum degrees, chamber-\(-\) inequalities, chamber-\(+\) inequalities, negative-chamber visibility equality, positive-chamber visibility difference |
| Table 3 — Degree-law ledger | \(\S\)6 | Consolidate monodromy outputs without implying numerics. | \(P\), both eigenpairs, recurrence, \(d_0\) through \(d_3\), corrected \(u_3\), wall gaps, \(d_{2j}\), \(d_{2j+1}\), integrality source |
| Table 4 — Contextual neighbor comparison (optional if page pressure permits) | \(\S\)1 or \(\S\)8 | Compare mechanisms and boundaries only, with no fake quantitative bound columns. | Paper 20, Papers 21--23, S03--S09 grouped by mechanism, overlap, and exact boundary |

No hero figure is planned because the contribution is not geometric visualization, experimental comparison, or architecture design. The key relationships are exact formulas, inequalities, and scope boundaries; a diagram would cost space without carrying proof. Hand-typeset tables are the highest-signal format.

## Bounded contextual source plan (S01--S09 only)

Only the nine locked contextual source identifiers may appear, and only for bounded positioning.

| Source ID | Locked role | Allowed manuscript use | Forbidden use |
|---|---|---|---|
| S01 | general algebraic-entropy / degree-growth context | \(\S\)1 opening context sentence | no selector, carry, or symplectic proof transfer |
| S02 | reminder that degree sequences need not satisfy fixed recurrences in general | \(\S\)1 bounded context sentence | no proof of the present recurrence |
| S03 | closest public symplectic/tropical branch-switching neighbor | \(\S\)1 and optional Table 4 | no direct collision statement and no theorem proof transfer |
| S04 | closest public monodromy-style tropical degree mechanism | \(\S\)1 and optional Table 4 | no carry/no-cancellation/visibility transfer |
| S05 | strongest warning that periodic switching is not novel by itself | \(\S\)1 bounded novelty firewall | no novelty inflation or collision overstatement |
| S06 | polynomial symplectomorphism background | \(\S\)1 one-sentence class background | no proof of symplecticity or degree laws |
| S07 | weak-Perron / affine-triangular context | \(\S\)1 or \(\S\)8 bounded positioning | no first-realization language |
| S08 | general spectral context | \(\S\)1 context sentence | no proof of the explicit monodromy or visibility |
| S09 | current nearby affine-triangular neighbor | \(\S\)1 or optional Table 4 | no direct noncollision certificate beyond bounded review |

Source-policy rules:

1. No source outside S01--S09 is introduced in this plan.
2. No BibTeX, no citation-key fabrication, and no bibliography completion are authorized here.
3. No citation proves a headline claim; every proof-relevant row in the Claims--Evidence Matrix points to a local section, statement, and equation.
4. The theory-comparison table, if retained, compares mechanisms, scope, and boundaries only; it will not invent shared numerical bounds or fake benchmark columns.

## Papers 20--23 boundary and public-safe comparison policy

The introduction and conclusion must state the local predecessor boundary exactly as follows:

| Neighbor | What it already owns | Exact Paper 24 boundary |
|---|---|---|
| Paper 20 | two-mode Hamiltonian product shears with one stationary selector regime and one fixed complete-step matrix | Paper 24 keeps the two-mode proof grammar but replaces stationarity by strict wall crossing and a two-step cocycle |
| Paper 21 | stationary three-mode selector regime, exact cubic recurrence, and visible coordinate | Paper 24 is not a mode lift and has no stationary selector regime |
| Paper 22 | arbitrary-mode endpoint-spike cubic collapse with a common unit sector | Paper 24 is the opposite mechanism: fixed two-mode wall exchange, not collapse |
| Paper 23 | four-mode quartic escape beyond the collapse mechanism | Paper 24 has a different support profile and no quartic escape storyline |

The manuscript must never market the result as “another small matrix example.” The permitted standalone sentence is that the full \(m\)-family, the explicit wall-fixing ratio, the true carry/no-cancellation/visibility proof, and the exact parity laws together clear the standalone threshold.

## Anti-claims, failure examples, STOP rules, and zero-science contract

### Locked anti-claims

The manuscript must explicitly avoid claiming:

1. a theorem on the wall \(r=2\);
2. any classification beyond the crossed-binomial / diagonal-pure-power ansatz;
3. a maximal, necessary, unique, or complete selector fan;
4. arbitrary period words, period \(>2\), automaton realization, or arbitrary shear-word realization;
5. positive-characteristic validity;
6. inverse-degree, entropy-equality, integrability, genericity, periodic-point, arithmetic-orbit, or nonconjugacy theorems;
7. novelty of the abstract conditional period-\(k\) selector-to-monodromy principle;
8. first Perron realization, first weak-Perron realization, first tropical switching, first periodic switching, first symplectic shear, or absolute literature priority;
9. arbitrary finite supports, added monomials, vanishing coefficients, or reversed phase order.

### Failure examples that must remain visible

The conclusion/limitations section must mention these exact assumption-failure examples:

- \(r=2\): both competitive rows tie exactly;
- \(m=1\): the factor \((m-1)(u_1-2u_2)\) vanishes;
- one of \(A,B,C,D\) equals zero: the support profile changes;
- positive characteristic: derivative scalars may vanish;
- omitted carry proof: weighted support no longer certifies actual polynomial degrees;
- omitted visibility proof: \(u_{n,1}\) is only a candidate observable;
- \(R=1\) in the structural lemma: the ordinary seed lies on the wall.

### STOP rules for downstream drafting

Drafting must stop for review if any of the following appears:

1. the theorem is narrowed back to the singleton \(m=2\) example;
2. the period-two exchange is asserted without both carry phases, top-form survival, and \(q_1\) visibility;
3. the wall-fixing ratio is claimed outside the crossed-binomial / diagonal-pure-power ansatz;
4. the conditional period-\(k\) lemma becomes the headline;
5. any corrected branch identity, visible degree, spectrum, recurrence, initial value, corrected \(u_3\), wall gap, or parity formula drifts;
6. the determinant step states \(\det(P)=HL\) without either the explicit \(ad-bc\) expansion or a valid determinant-multiplicativity derivation;
7. the article stops fitting inside the locked 22--30 content-page band;
8. a forbidden directory, figure, dataset, computation, code artifact, build artifact, or external effect is smuggled in.

### Zero-science and zero-code contract

This paper-plan stage remains proof-only:

- no code, data, datasets, plots, figures, notebooks, CAS logs, or numerical tables;
- no finite scans in \(m\), \(s\), signs, or characteristics;
- no spectral numerics, floating-point eigenpairs, or recurrence fitting;
- no theorem evidence from experimentation of any kind.

Arithmetic recomputation by a reviewer is allowed only as falsification aid. Every accepted identity must have a written derivation in the manuscript body.

## Public-governance firewall

The eventual public manuscript must exclude:

- SHA-256 hashes, byte counts, LF counts, internal file paths, and lifecycle tokens;
- discussion of source-lock governance, reviewer identities, or repair history;
- any mention of publication locks, source trios, build chains, release pipelines, registry mutations, or batch-control state.

This plan itself authorizes none of the following:

- publication-stage scope files other than the conditional later possibility named below;
- publication lock authoring;
- manuscript or TeX/BibTeX authoring;
- figures, code, data, experiments, build, PDF, release, submission, upload, hosting, repository push, transport, messaging, identity disclosure, or Paper 25 work;
- any external effect.

## Draft-readiness checklist

The plan is ready for independent review only if all of the following remain true:

- exact title retained: `Forced Period-Two Selector Exchange in Two-Mode Hamiltonian Product Shears`;
- author placeholder remains `Anonymous`;
- no venue is selected;
- abstract plus exactly eight numbered sections are planned;
- public page budget still sums to 26.0 exactly;
- all theorem-critical proofs remain in the main body;
- \(K\), \(m\ge2\), \(s\ge1\), \(A,B,C,D\in K^\times\), \(V_m\), \(W_{m,s}\), \(S\), \(T\), and \(F_{m,s}=T\circ S\) are stated literally;
- the four correction precedences are frozen:
  1. corrected \(\ell_m(r)-1\),
  2. corrected negative-chamber visibility equality,
  3. corrected \(2-\ell_m(r)\),
  4. corrected second coordinate of \(u_3\);
- both carry phases, arbitrary-nonzero top-form survival, and \(q_1\) visibility for \(n\ge1\) are all explicit;
- \(P=(B_mA_+)(B_mA_-)\), both right eigenpairs, trace, explicit determinant expansion, \(\lambda_1\), recurrence, initials, corrected \(u_3\), wall gaps, full even vector, both parity closed forms, and integrality all have assigned proof locations;
- the bounded structural iff lemma, explicit \((m,s)\) realization, and six-hypothesis conditional period-\(k\) lemma are all present with scope warnings;
- only S01--S09 appear in contextual positioning;
- planned manuscript tables are exactly three mandatory hand-typeset mathematical tables plus one optional contextual comparison table, with no figures and no empirical tables;
- Papers 20--23 boundaries, anti-claims, failure examples, STOP rules, zero-science contract, and governance firewall remain explicit.

## Reviewer handoff

The sole next conditional path is:

`notes/INDEPENDENT_PAPER_PLAN_REVIEW.md`

Independent-review rule:

- if any conjunctive plan gate fails, the reviewer must `WRITE NOTHING`;
- if every conjunctive plan gate passes, the reviewer may write only the review artifact above and must end it with the exact terminal token `PAPER_PLAN_PASS`.

A validated `PAPER_PLAN_PASS` does not directly authorize publication governance, manuscript writing, source-trio work, TeX/BibTeX, figures, build, PDF, release, Paper 25, registry mutation, or any external effect. It makes only `notes/PUBLICATION_STAGE_SCOPE.md` eligible for a later separate parent transition.

PAPER PLAN AUTHOR STOP
