# Paper 24 — Publication-Stage Scope

Date: 2026-08-25 UTC  
Project root: papers/24-hamiltonian-period-two-selector-exchange  
Candidate ID: hamiltonian_period_two_selector_exchange_v2  
Artifact role: human-readable publication-governance contract, not public
article prose  
Authoring status: scope-only author stop; no publication-stage PASS,
publication lock, bibliography, manuscript source, build, PDF, release, or
external effect is authorized

## 1. Authority, role separation, and upstream gate

This file is the sole project write of a fresh publication-scope author who
authored none of the candidate reviews, source-design files, source-design
review, source lock, source-lock review, paper plan, paper-plan review, or
current root governance records. Before writing, the author read through EOF:

1. the complete local `research-lit` skill instructions, used here only for a
   bounded official-source bibliographic recheck;
2. the exact fifteen-file Paper 24 project universe;
3. the four immutable Paper 24 candidate-review / correction records;
4. both current Batch 06 root ledgers; and
5. the Paper 22 and Paper 23 publication-stage scope artifacts only as
   structural warnings against lifecycle, metadata, and permission drift.

Paper 23 is terminal and contributes no mathematical semantics, metadata,
permissions, or scope shortcuts here. The only mathematical object frozen
below is Paper 24's two-mode characteristic-zero product-shear family.

The current scope-authoring root identities are exact:

| Record | SHA-256 | Bytes | LF | Controlling fact |
|---|---|---:|---:|---|
| BATCH_06_STATUS.md | 759d09d03ba79eb2ea8bcfe8206911eff4c13640a96e0ef6d709de558128420c | 124,890 | 1,825 | Gate `PAPER24_PUBLICATION_SCOPE_AUTHORING`; Paper 24 queue `PAPER_PLAN_PASS_PUBLICATION_SCOPE_OPEN` |
| BATCH_06_IDEA_REPORT.md | 25972bea637e2e68de47cea69310f7436cfeebb0056f121046b605d5aa668cf2 | 217,452 | 4,259 | Append-only Paper 24 paper-plan PASS and publication-scope-only permission |

The stable plan and lock chain is exact:

| Project record | SHA-256 | Bytes | LF | Exact terminal or role |
|---|---|---:|---:|---|
| paper/PAPER_PLAN.md | ee5c320f800919543411b147b5d1484d33c577a56519121b9b4883fdff8122ad | 36,690 | 586 | `PAPER PLAN AUTHOR STOP` |
| notes/INDEPENDENT_PAPER_PLAN_REVIEW.md | 4d642580cad2dec337249cb0a11acbb662ae640a8d5faf44077f6ec2be354d68 | 20,521 | 483 | `PAPER_PLAN_PASS` |
| experiments/source_lock.json | 45ce6527917d7172ff10e87db1e716b6e7caa2de3fa3cfbd54cd73b034003232 | 45,607 | 1 | strict-canonical schema `paper24.source_lock.v1`; self digest and bytes are null |
| notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md | a420a26fbf3a535aedafdfd701969db8084b932e2ae9e6d806570c460090abea | 24,533 | 754 | `SOURCE_LOCK_PASS` |
| notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md | 1c733058483cb28370e4c6f283126c14305ce45de43010e7753a4d92a5f8ece8 | 16,630 | 490 | `SOURCE_DESIGN_PASS` |

The immutable candidate provenance is exact:

| Root candidate record | SHA-256 | Bytes | LF | Exact terminal |
|---|---|---:|---:|---|
| BATCH_06_PAPER24_CANDIDATE_REVIEW_R1.md | b2802f24ca5de3d91b7ea5a1726a0cf12d6f36053055e24e3759124bfc8709c1 | 30,703 | 878 | `PAPER24_CANDIDATE_GATE_PASS_R1` |
| BATCH_06_PAPER24_CANDIDATE_REVIEW_R1_CORRECTION.md | dabf9fa2873aa0124e2d510dc20b581b51a5648e0828f33bc2b7a41b2172730d | 2,583 | 112 | `PAPER24_CANDIDATE_GATE_PASS_R1_CORRECTED` |
| BATCH_06_PAPER24_CANDIDATE_REVIEW_R2.md | 914b92255cd9aae2b8be4707484ebf63a72d1b40e1cf1fc356dd365676ed25bd | 19,672 | 769 | `PAPER24_CANDIDATE_GATE_PASS_R2` |
| BATCH_06_PAPER24_CANDIDATE_REVIEW_R2_CORRECTION.md | 1c311a979b3c8fc396734bbd851f1a6c8ed5738a2f3005048688f623a6bcaf6b | 2,500 | 115 | `PAPER24_CANDIDATE_GATE_PASS_R2_CORRECTED` |

### Exact fifteen-file input universe

Immediately before this scope write, the project contained exactly the
following fifteen regular files:

| Relative path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| experiments/EXPERIMENT_PLAN.md | bfd644a19d15f51a4c7eca6323909852d38e7477afac73aea77b02642ffb6f94 | 7,098 | 186 |
| experiments/EXPERIMENT_TRACKER.md | 61e34652fdea217b0da4f7774478f243ca806fb88a97e18f09d767e24fbe8db0 | 3,459 | 59 |
| experiments/source_lock.json | 45ce6527917d7172ff10e87db1e716b6e7caa2de3fa3cfbd54cd73b034003232 | 45,607 | 1 |
| notes/CITATION_VERIFICATION.md | 66558b974ebdcc0fd7627c52c4caee0c80b404514d06f622ededd9b9a8900fb9 | 6,694 | 93 |
| notes/CLAIMS_EVIDENCE_MATRIX.md | 28f8f3dd6add8617a63c16b5d6956d5a1214dc453a2416721dca824faba00dc5 | 7,040 | 114 |
| notes/INDEPENDENT_PAPER_PLAN_REVIEW.md | 4d642580cad2dec337249cb0a11acbb662ae640a8d5faf44077f6ec2be354d68 | 20,521 | 483 |
| notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md | 1c733058483cb28370e4c6f283126c14305ce45de43010e7753a4d92a5f8ece8 | 16,630 | 490 |
| notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md | a420a26fbf3a535aedafdfd701969db8084b932e2ae9e6d806570c460090abea | 24,533 | 754 |
| notes/NOVELTY_ASSESSMENT.md | e873bcdc57c0f39e04b950bf9221c894993370c1accd313cbcb05495fa92fb2c | 5,532 | 119 |
| notes/PROOF_PACKAGE.md | b6df4be9e9a00a5ae71e48505b007a59fea70bcff3046661af804714378963bf | 18,290 | 1,048 |
| notes/RESEARCH_QUESTION.md | 5dc091d3500800610360512f464a877adb51c1f83857c8335a28dccebd35ef7d | 5,052 | 132 |
| paper/PAPER_PLAN.md | ee5c320f800919543411b147b5d1484d33c577a56519121b9b4883fdff8122ad | 36,690 | 586 |
| refine-logs/FINAL_PROPOSAL.md | bf04aa95c67b19bc876c594b8162534c7000f12a92fc696017d36bf9cf7e96bf | 4,773 | 175 |
| refine-logs/INITIAL_PROPOSAL.md | 7e5d64d5c4d3029d8d9d10f82c5dee41e66c5c2fb9cc3271e203657eeb74a8dc | 3,971 | 148 |
| refine-logs/REVIEW_SUMMARY.md | b2357b00fb2a9e05dbc96db775be9ef6a243e164b5b720525ecef9b3bd220c82 | 4,233 | 102 |

The ten source-design author files total 66,142 bytes and 2,176 LF. Their
byte-sorted text ledger is 1,038 bytes with SHA-256
51364bd0e7c56055f17956248cc9f12bd10de6679638e8a90411394e89b51e88,
and their uint64-big-endian length-framed stream is 66,590 bytes with
SHA-256 ca447f74449cee1f04c9f6181c2325b2350a975e59a8624aa8705b350f7e8e67.

This scope freezes what a later publication lock may bind. It does not itself
authorize that lock, a manuscript, TeX/BibTeX authoring, a bibliography file,
compilation, PDF, release, or any external action.

## 2. Exact anonymous public and metadata identity

The following title string is exact and immutable across the public article,
the future source `\title{...}` field, the rendered title, PDF title
metadata, bookmarks that reproduce the title, and any permitted running-title
representation:

Forced Period-Two Selector Exchange in Two-Mode Hamiltonian Product Shears

No shortened title, changed capitalization, subtitle split, project number,
alternate punctuation, internal codename, or hidden private title may replace
it in the source, rendering, or PDF metadata. If a document class
mechanically requires a running title, that field must contain the same full
title unless a later independent source review verifies a nonidentifying
class-imposed truncation; no author, project, or governance marker may be
introduced.

The identity and date fields are frozen as follows:

- visible author text: exactly `Anonymous`;
- source author field: exactly `Anonymous`;
- source date field: exactly empty, implemented as `\date{}`;
- visible date: absent;
- PDF title metadata: exactly the full title above;
- PDF author metadata: exactly empty;
- PDF creator metadata: exactly empty;
- PDF producer metadata: exactly empty; and
- no author footnote, thanks mark, corresponding-author marker, affiliation,
  email, ORCID, acknowledgment, funding statement, grant number,
  contribution statement, conflict statement, venue marker, or hidden identity
  field.

The anonymity and public-governance firewall applies to all future public
bytes, including:

- TeX comments and unused macros;
- BibTeX comments, unused fields, strings, preambles, cross-references, file
  fields, abstract fields, note fields, URL fields not frozen below, and
  attachment metadata;
- PDF document information, XMP, bookmarks, headers, footers, annotations,
  hyperlinks, embedded-file names, and attachment metadata;
- source filenames exposed in rendered text or metadata;
- bibliography notes, local-file paths, and build-host traces; and
- any generated auxiliary source that could survive into a public package.

No real name, affiliation, private URL, local path, SHA-256 value, byte/LF
count, inventory count, reviewer role, model name, PASS/STOP token, Batch 06
or Paper 20--24 numbering, candidate score, lifecycle history, permission
history, source-lock schema, queue state, or submission venue may enter the
public trio, rendered article, bibliography, bookmarks, headers, comments, or
metadata.

## 3. Frozen family, phase order, and theorem contract

Let \(K\) be an arbitrary field of characteristic zero, and let \(m\ge2\) and
\(s\ge1\) be integers. Put

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
F_{m,s}=T\circ S,
\]

with arbitrary nonzero coefficients \(A,B,C,D\in K^\times\).

The phase order is immutable: \(S\) acts first and \(T\) acts on the updated
\(p\)-coordinates. The subtraction shears

\[
S^{-1}(q,p)=(q,p-\nabla V_m(q)),
\qquad
T^{-1}(q,p)=(q-\nabla W_{m,s}(p),p)
\]

appear only as inverse formulas. They are not alternate forward families.

The future article must write the gradients literally:

\[
\partial_{q_1}V_m=mAq_1^{m-1}q_2^2+Bq_2^{2m},
\qquad
\partial_{q_2}V_m=2Aq_1^mq_2+2mBq_1q_2^{2m-1},
\]

\[
\partial_{p_1}W_{m,s}=(s(2m+1)+1)Cp_1^{s(2m+1)},
\qquad
\partial_{p_2}W_{m,s}=(sm+1)Dp_2^{sm}.
\]

For the standard symplectic matrix

\[
\Omega=\begin{pmatrix}0&I_2\\-I_2&0\end{pmatrix},
\]

the public proof must derive, not cite, the Hessian-block identities

\[
J_S=\begin{pmatrix}I_2&0\\H_V&I_2\end{pmatrix},
\qquad
J_T=\begin{pmatrix}I_2&H_W\\0&I_2\end{pmatrix},
\]

with symmetric Hessians \(H_V=\nabla^2V_m\) and \(H_W=\nabla^2W_{m,s}\), and
must check

\[
J_S^{\mathsf T}\Omega J_S=\Omega,
\qquad
J_T^{\mathsf T}\Omega J_T=\Omega.
\]

The exact main theorem must remain equivalent to the following ten-item
contract and must not be weakened, generalized, or reordered into a
citation-dependent story:

1. \(F_{m,s}\) is a polynomial symplectomorphism of \(K^4\).
2. The actual \(q\)-degree orbit of the ordinary seed
   \(u_0=(1,1)^{\mathsf T}\) switches strictly between the two chambers
   \(r=u_1/u_2<2\) and \(r>2\).
3. The selected first-phase matrices are
   \[
   A_-=\begin{pmatrix}0&2m\\1&2m-1\end{pmatrix},
   \qquad
   A_+=\begin{pmatrix}m-1&2\\m&1\end{pmatrix},
   \qquad
   B_m=\operatorname{diag}(2m+1,m).
   \]
4. Writing
   \[
   C_-=sB_mA_-,
   \qquad
   C_+=sB_mA_+,
   \qquad
   P=(B_mA_+)(B_mA_-),
   \]
   the exact parity formulas are
   \[
   u_{2j}=(s^2P)^j(1,1)^{\mathsf T},
   \qquad
   u_{2j+1}=sB_mA_-(s^2P)^j(1,1)^{\mathsf T}.
   \]
5. For every \(n\ge1\), the first position coordinate is strictly maximal
   among all four coordinate degrees, hence
   \[
   d_n:=\deg(F_{m,s}^n)=u_{n,1}
   \qquad(n\ge1),
   \]
   with \(d_0=1\) as the tied seed.
6. The two eigenvalues of \(P\) are
   \[
   H=m^2(2m+1)^2,
   \qquad
   L=2m(m+1),
   \]
   so
   \[
   \lambda_1(F_{m,s})=sm(2m+1).
   \]
7. The visible degree sequence satisfies
   \[
   d_{n+4}=s^2(H+L)d_{n+2}-s^4HL\,d_n,
   \]
   with
   \[
   d_0=1,\qquad d_1=2m(2m+1)s,
   \]
   \[
   d_2=2m(m+1)(2m-1)(2m+1)s^2,
   \qquad
   d_3=8m^4(m+1)(2m+1)s^3.
   \]
8. The exact wall gaps are
   \[
   u_{2j,1}-2u_{2j,2}=-(s^2L)^j,
   \qquad
   u_{2j+1,1}-2u_{2j+1,2}=2ms(s^2L)^j.
   \]
9. Inside the crossed-binomial / diagonal-pure-power ansatz, strict chamber
   exchange forces the wall-fixing ratio
   \[
   \frac ef=\frac{R(L_{\mathrm{wall}}-1)}{L_{\mathrm{wall}}-R}.
   \]
10. The abstract period-\(k\) selector-to-monodromy statement is valid only
    as a conditional technique lemma with explicit selector, carry,
    noncancellation, linearity, and visibility hypotheses.

### Literal support rows, common wall, exact matrices, and corrected branch algebra

For a positive degree vector \(u=(u_1,u_2)^{\mathsf T}\), write
\[
r=\frac{u_1}{u_2}.
\]

The two competitive first-phase weighted differences must be displayed
literally:

\[
(m-1)u_1+2u_2-2mu_2=(m-1)(u_1-2u_2),
\]

\[
mu_1+u_2-\bigl(u_1+(2m-1)u_2\bigr)=(m-1)(u_1-2u_2).
\]

Therefore the common wall is exactly \(r=2\), the selected matrices are
exactly \(A_-\), \(A_+\), and \(B_m\) above, and the complete-step matrices
are exactly

\[
C_-=s\begin{pmatrix}
0&2m(2m+1)\\
m&m(2m-1)
\end{pmatrix},
\qquad
C_+=s\begin{pmatrix}
(m-1)(2m+1)&2(2m+1)\\
m^2&m
\end{pmatrix}.
\]

The projective branch maps must be written exactly as

\[
h_m(r)=\frac{2(2m+1)}{r+2m-1},
\qquad
\ell_m(r)=\frac{(2m+1)\bigl((m-1)r+2\bigr)}{m(mr+1)}.
\]

The three corrected branch-difference identities are immutable:

\[
h_m(r)-2=\frac{2(2-r)}{r+2m-1}>0
\qquad(0<r<2),
\]

\[
\ell_m(r)-1=
\frac{(m^2-m-1)r+3m+2}{m(mr+1)}>0
\qquad(r>2),
\]

\[
2-\ell_m(r)=
\frac{(m+1)(r-2)}{m(mr+1)}>0
\qquad(r>2).
\]

Consequently

\[
0<r<2\Longrightarrow h_m(r)>2,
\qquad
r>2\Longrightarrow1<\ell_m(r)<2,
\]

and from the ordinary seed \(u_0=(1,1)^{\mathsf T}\) the unique strict
selector word is
\[
A_-,A_+,A_-,A_+,\ldots
\]
with complete-step matrices
\[
C_-,C_+,C_-,C_+,\ldots.
\]

The wall itself is a genuine tie boundary:

\[
h_m(r)=2\iff r=2,
\qquad
\ell_m(r)=2\iff r=2.
\]

It is excluded from every strict theorem statement.

## 4. Carry, visibility, monodromy, and exact degree-law contract

Selector choice and actual polynomial degree transport are separate proof
obligations. The future article must retain the following exact carry and
leading-form structure.

### Base carry, later carry, and arbitrary-nonzero top-form survival

The base carry displays are mandatory:

\[
A_-(1,1)^{\mathsf T}=(2m,2m)^{\mathsf T}>(1,1)^{\mathsf T},
\]

\[
sB_mA_-(1,1)^{\mathsf T}
=\bigl(2m(2m+1)s,\ 2m^2s\bigr)^{\mathsf T}>(1,1)^{\mathsf T}.
\]

For \(n\ge1\), the carried momentum degrees are exactly

\[
\deg p_n=
\left(
\frac{u_{n,1}}{s(2m+1)},
\frac{u_{n,2}}{sm}
\right).
\]

In the negative chamber \(r_n<2\), the fresh first-phase degrees are

\[
v_{n+1}=
\begin{pmatrix}
2mu_{n,2}\\
u_{n,1}+(2m-1)u_{n,2}
\end{pmatrix},
\]

and the required chamberwise inequalities are

\[
2mu_{n,2}>\frac{u_{n,1}}{s(2m+1)},
\qquad
u_{n,1}+(2m-1)u_{n,2}>\frac{u_{n,2}}{sm}.
\]

The pure second phase then yields

\[
u_{n+1}=
\begin{pmatrix}
s(2m+1)\cdot2mu_{n,2}\\
sm\bigl(u_{n,1}+(2m-1)u_{n,2}\bigr)
\end{pmatrix},
\]

with the exact fresh-position inequalities

\[
2m(2m+1)su_{n,2}>u_{n,1},
\qquad
sm\bigl(u_{n,1}+(2m-1)u_{n,2}\bigr)>u_{n,2}.
\]

In the positive chamber \(r_n>2\), the fresh first-phase degrees are

\[
v_{n+1}=
\begin{pmatrix}
(m-1)u_{n,1}+2u_{n,2}\\
mu_{n,1}+u_{n,2}
\end{pmatrix},
\]

with exact inequalities

\[
(m-1)u_{n,1}+2u_{n,2}>\frac{u_{n,1}}{s(2m+1)},
\qquad
mu_{n,1}+u_{n,2}>\frac{u_{n,2}}{sm},
\]

followed by

\[
u_{n+1}=
\begin{pmatrix}
s(2m+1)\bigl((m-1)u_{n,1}+2u_{n,2}\bigr)\\
sm\bigl(mu_{n,1}+u_{n,2}\bigr)
\end{pmatrix},
\]

and the exact fresh-position inequalities

\[
s(2m+1)\bigl((m-1)u_{n,1}+2u_{n,2}\bigr)>u_{n,1},
\qquad
sm\bigl(mu_{n,1}+u_{n,2}\bigr)>u_{n,2}.
\]

The conclusion is rigid: both phases beat carried coordinates in both
chambers already for \(s=1\). No large-\(s\) asymptotic shortcut is
permitted.

The arbitrary-nonzero-coefficient theorem is not a positivity theorem. The
future manuscript must say explicitly that at every phase a unique selected
source has strictly highest degree, its top homogeneous part is a nonzero
scalar multiple of products or powers of earlier nonzero top parts, the
polynomial ring \(K[q_1,q_2,p_1,p_2]\) is a domain, \(A,B,C,D\) are nonzero,
and characteristic zero keeps all derivative scalars nonzero. Therefore
cancellation is impossible. Positivity language is forbidden as theorem
evidence.

### Visibility, exact monodromy, determinant obligation, and parity laws

The visibility proof must retain the exact scope boundary \(n\ge1\). The
article must state

\[
u_{n,1}>u_{n,2}
\qquad(n\ge1),
\]

because both branch images exceed \(1\), and then compare \(q_1\) against
both momentum coordinates.

In the negative chamber, the corrected exact equality is mandatory:

\[
u_{n+1,1}=sm\,h_m(r_n)\,v_{n+1,2}.
\]

Only after this equality may the article conclude
\[
u_{n+1,1}>v_{n+1,2}.
\]

In the positive chamber, the second comparison must remain

\[
u_{n+1,1}-v_{n+1,2}
=s(2m+1)\bigl((m-1)u_{n,1}+2u_{n,2}\bigr)
-(mu_{n,1}+u_{n,2})>0.
\]

Together with
\[
u_{n+1,1}=s(2m+1)v_{n+1,1}>v_{n+1,1},
\]
this certifies that \(q_1\) is strictly maximal among
\(q_1,q_2,p_1,p_2\) for every positive iterate.

The exact two-step monodromy is

\[
P=(B_mA_+)(B_mA_-)
=
\begin{pmatrix}
2m(2m+1)&2m(2m+1)(2m^2+m-2)\\
m^2&m^2(4m^2+4m-1)
\end{pmatrix}.
\]

Both right eigenpairs are frozen:

\[
P\begin{pmatrix}2\\1\end{pmatrix}
=H\begin{pmatrix}2\\1\end{pmatrix},
\qquad
H=m^2(2m+1)^2,
\]

\[
P\begin{pmatrix}
-(2m+1)(2m^2+m-2)\\
m
\end{pmatrix}
=L\begin{pmatrix}
-(2m+1)(2m^2+m-2)\\
m
\end{pmatrix},
\qquad
L=2m(m+1).
\]

The trace identity is

\[
\operatorname{tr}(P)=H+L=4m^4+4m^3+3m^2+2m.
\]

The determinant statement may not appear as a bare equality. A public proof
must show either the explicit \(ad-bc\) expansion

\[
2m(2m+1)\cdot m^2(4m^2+4m-1)
-2m(2m+1)(2m^2+m-2)\cdot m^2
=2m^3(m+1)(2m+1)^2,
\]

or a correct determinant-multiplicativity derivation from the displayed
factors before concluding

\[
\det(P)=H\,L=2m^3(m+1)(2m+1)^2.
\]

The actual two-step monodromy \(C_+C_-=s^2P\) therefore has eigenvalues
\(s^2H\) and \(s^2L\), and the exact dynamical degree law is

\[
\lambda_1(F_{m,s})=\sqrt{\rho(s^2P)}=sm(2m+1).
\]

The parity-vector laws, stride-two recurrence, initials, wall gaps, and
closed forms are all frozen:

\[
u_{2j}=(s^2P)^j(1,1)^{\mathsf T},
\qquad
u_{2j+1}=sB_mA_-(s^2P)^j(1,1)^{\mathsf T},
\]

\[
d_{n+4}=s^2(H+L)d_{n+2}-s^4HL\,d_n,
\]

\[
u_1=
\begin{pmatrix}
2m(2m+1)s\\
2m^2s
\end{pmatrix},
\qquad
u_2=
\begin{pmatrix}
2m(m+1)(2m-1)(2m+1)s^2\\
4m^3(m+1)s^2
\end{pmatrix},
\]

\[
u_3=
\begin{pmatrix}
8m^4(m+1)(2m+1)s^3\\
2m^2(m+1)(2m-1)(2m^2+2m+1)s^3
\end{pmatrix},
\]

\[
d_0=1,\quad
d_1=2m(2m+1)s,\quad
d_2=2m(m+1)(2m-1)(2m+1)s^2,\quad
d_3=8m^4(m+1)(2m+1)s^3,
\]

\[
\ell=(1,-2),\qquad
\ell C_-=-2ms\,\ell,\qquad
\ell C_+=-(m+1)s\,\ell,
\]

\[
u_{2j,1}-2u_{2j,2}=-(s^2L)^j,
\qquad
u_{2j+1,1}-2u_{2j+1,2}=2ms(s^2L)^j.
\]

The even and odd visible closed forms remain frozen as

\[
d_{2j}
=\frac{s^{2j}}{4m^3+4m^2-m-2}
\left(
4(m+1)(2m^2-1)H^j
-(2m+1)(2m^2+m-2)L^j
\right),
\]

\[
u_{2j}
=\frac{s^{2j}}{4m^3+4m^2-m-2}
\left(
2(m+1)(2m^2-1)H^j\begin{pmatrix}2\\1\end{pmatrix}
+L^j\begin{pmatrix}
-(2m+1)(2m^2+m-2)\\
m
\end{pmatrix}
\right),
\]

\[
d_{2j+1}
=\frac{2m(2m+1)s^{2j+1}}{4m^3+4m^2-m-2}
\left(
2(m+1)(2m^2-1)H^j+mL^j
\right).
\]

Integrality must be explained only from the integer matrix formulas above, or
equivalently from the integer-coefficient stride-two recurrence and integer
initial data. Rational-looking denominators in the closed forms are not a
license for divisibility folklore.

## 5. Structural lemma, conditional period-\(k\) lemma, corrections, boundaries, and anti-claims

### Bounded structural lemma and technical conditional lemma

The crossed-binomial / diagonal-pure-power structural lemma remains bounded to
the ansatz

\[
V=Aq_1^a q_2^b+Bq_1^c q_2^d,
\qquad
a>c\ge1,\qquad d>b\ge1,
\]

\[
W=Cp_1^{e+1}+Dp_2^{f+1}.
\]

The common wall and wall weight are

\[
R=\frac{d-b}{a-c},
\qquad
L_{\mathrm{wall}}=aR+b=cR+d.
\]

The selected branch maps are

\[
g_{x,y}(r)=\frac ef\frac{(x-1)r+y}{xr+y-1},
\qquad
g'_{x,y}(r)=
-\frac ef\frac{x+y-1}{(xr+y-1)^2}<0,
\]

and the global wall-fixing criterion is

\[
g(R)=R
\iff
\frac ef=\frac{R(L_{\mathrm{wall}}-1)}{L_{\mathrm{wall}}-R}.
\]

For the explicit Paper 24 family,

\[
(a,b,c,d)=(m,2,1,2m),
\qquad
R=2,
\qquad
L_{\mathrm{wall}}=2m+2,
\qquad
\frac ef=\frac{2m+1}{m},
\]

so the integral realizations are exactly
\[
(e,f)=s(2m+1,m)
\]
for positive integers \(s\).

This lemma proves only the wall-fixing exponent ratio inside the stated
ansatz. It proves neither carry, actual polynomial degree transport,
top-form survival, nor visibility. If \(R=1\), the ordinary seed lies on the
wall and no strict seed theorem follows.

The conditional period-\(k\) selector-to-monodromy lemma is frozen as a
technical downstream statement only. Its six hypotheses must remain explicit:

1. every phase has a unique selected face with a strict gap over all
   unselected faces on the claimed domain;
2. every selected fresh row strictly beats every carried coordinate in its
   target block;
3. all selected top homogeneous parts remain nonzero in a domain;
4. the selected faces induce linear degree maps \(C_0,\dots,C_{k-1}\);
5. a coordinate or linear functional sees the true total degree on the
   residue classes used; and
6. the Perron class of the monodromy is visible to that coordinate or
   functional.

Only under those hypotheses may the article conclude

\[
u_{k\ell+j}=D_jM^\ell u_0
\]

for \(M=C_{k-1}\cdots C_0\), the visible residue recurrences from
Cayley--Hamilton, and

\[
\lambda_1=\rho(M)^{1/k}.
\]

This remains technical support only. It is not the headline novelty claim of
Paper 24 and not an arbitrary-period realization theorem.

### Frozen correction precedence, failure boundaries, and anti-claims

The four candidate-review corrections are immutable:

1. the corrected numerator in
   \[
   \ell_m(r)-1=\frac{(m^2-m-1)r+3m+2}{m(mr+1)};
   \]
2. the corrected negative-chamber visibility equality
   \[
   u_{n+1,1}=sm\,h_m(r_n)\,v_{n+1,2}
   \]
   before the strict inequality consequence;
3. the corrected factor \((m+1)\) in
   \[
   2-\ell_m(r)=\frac{(m+1)(r-2)}{m(mr+1)};
   \]
4. the corrected second coordinate of
   \[
   u_3=
   \begin{pmatrix}
   8m^4(m+1)(2m+1)s^3\\
   2m^2(m+1)(2m-1)(2m^2+2m+1)s^3
   \end{pmatrix}.
   \]

The theorem fails or narrows under the following exact changes:

- on the wall \(r=2\), both competitive \(V\)-rows tie exactly;
- if \(m=1\), the switching factor \((m-1)(u_1-2u_2)\) collapses;
- if any of \(A,B,C,D\) vanishes, the support profile changes;
- in positive characteristic, derivative scalars may vanish;
- if the carry proof is omitted, weighted support no longer certifies actual
  polynomial degrees;
- if the visibility proof is omitted, \(u_{n,1}\) is only a candidate
  observable; and
- in the structural lemma, \(R=1\) places the ordinary seed on the wall.

The future public source and PDF must not state or imply:

1. a theorem on the wall \(r=2\);
2. any classification beyond the crossed-binomial / diagonal-pure-power
   ansatz;
3. any maximal, necessary, unique, or complete selector fan;
4. arbitrary period words, period \(>2\), automaton realization, or arbitrary
   shear-word realization;
5. positive-characteristic validity;
6. inverse-degree, entropy-equality, integrability, genericity,
   periodic-point, arithmetic-orbit, or nonconjugacy theorems;
7. novelty of the abstract conditional period-\(k\)
   selector-to-monodromy principle;
8. first Perron realization, first weak-Perron realization, first tropical
   switching, first periodic switching, first symplectic shear, or absolute
   literature priority;
9. arbitrary finite supports, added monomials, vanishing coefficients, or
   reversed phase order;
10. proof by CAS output, floating-point spectra, finite iterate tables,
    scans, code, or data; or
11. any public claim that Papers 20--23 belong in the bibliography or public
    metadata.

Source progression and later source authoring must stop and return to
governance if any of the following occurs:

- the theorem is narrowed back to the lone \(m=2\) example;
- the period-two exchange is asserted without both carry phases, top-form
  survival, and \(q_1\) visibility;
- the wall-fixing ratio is claimed outside the crossed-binomial /
  diagonal-pure-power ansatz;
- the conditional period-\(k\) lemma becomes the headline;
- any corrected branch identity, visible degree, spectrum, recurrence, initial
  value, corrected \(u_3\), wall gap, or parity formula drifts;
- the determinant line states \(\det(P)=HL\) without either the explicit
  \(ad-bc\) expansion or a valid determinant-multiplicativity derivation;
- the article no longer fits the locked 22--30 content-page band or the exact
  26.0-page target stated below;
- a forbidden figure, asset, dataset, computation, code artifact, build
  artifact, venue marker, or external effect appears; or
- the source list expands beyond S01--S09 or S09's publication status is
  silently changed without a new governance check.

## 6. Exact public article contract

The public article consists of one abstract followed by exactly eight numbered
main sections. References are excluded from the content-page target. All
theorem-critical proofs remain in the main body. There is no proof appendix.

The exact content-page target is 26.0 pages:

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

The eight numbered section titles are exact and immutable:

1. Introduction, theorem preview, and bounded positioning
2. Family, inverses, symplecticity, and support rows
3. Common wall, branch algebra, and strict selector exchange
4. Temporal carry and arbitrary-nonzero top homogeneous survival
5. \(q_1\) visibility, monodromy, determinant, and spectrum
6. Recurrence, wall gaps, parity closed forms, and integrality
7. Bounded structural lemma and conditional period-\(k\) lemma
8. Boundaries, coefficient scope, limitations, and conclusion

The abstract may do only four things:

1. state the exact family \(V_m,W_{m,s},F_{m,s}=T\circ S\) with
   characteristic-zero and nonzero-coefficient scope;
2. state the strict period-two wall exchange off \(r=2\);
3. state the exact monodromy and degree-law outputs
   \(\lambda_1(F_{m,s})=sm(2m+1)\) and the stride-two recurrence; and
4. state the bounded nature of the contribution: explicit family, true
   carry/visibility proof, exact parity laws, and no priority claim.

No figures, plots, diagrams, images, screenshots, generated assets, empirical
tables, code listings, experimental panels, or appendixed proof fragments are
permitted.

The manuscript must contain exactly three mandatory hand-typeset mathematical
tables and no fourth table:

| Table | Planned section | Purpose | Required rows |
|---|---|---|---|
| Table 1 — Selector and branch ledger | \(\S\)2--\(\S\)3 | Competitive rows, common wall, branch maps, and corrected branch differences in one auditable place | mixed/pure rows for each derivative, \(A_-\), \(A_+\), \(B_m\), \(h_m\), \(\ell_m\), \(h_m-2\), \(\ell_m-1\), \(2-\ell_m\), chamber images |
| Table 2 — Carry and visibility ledger | \(\S\)4--\(\S\)5 | Separate base carry, later \(S\)-carry, later \(T\)-carry, and \(q_1\)-visibility comparisons | seed carry, carried momentum degrees, chamber-\(-\) inequalities, chamber-\(+\) inequalities, negative-chamber visibility equality, positive-chamber visibility difference |
| Table 3 — Degree-law ledger | \(\S\)6 | Consolidate monodromy outputs without implying numerics | \(P\), both eigenpairs, recurrence, \(d_0\) through \(d_3\), corrected \(u_3\), wall gaps, \(d_{2j}\), \(d_{2j+1}\), integrality source |

The optional contextual comparison table from the plan is omitted at
publication stage and must not appear in the public article. Citation screens,
claims matrices, collision tables, file inventories, hashes, review
histories, permission ledgers, dashboards, and governance artifacts may not
become public tables or prose.

The exact public contribution list remains the four-item plan framing:

1. explicit two-mode Hamiltonian product shears with a common wall \(r=2\);
2. strict period-two selector exchange of the ordinary orbit;
3. true polynomial carry / no-cancellation / visibility proof for arbitrary
   nonzero coefficients; and
4. exact two-step monodromy, recurrence, wall gaps, and parity laws.

## 7. Bounded official-source metadata recheck and exact nine-source allowlist

A bounded official-source bibliographic recheck was completed on 2026-08-25
UTC before this scope was written. It used only official publisher, DOI, and
arXiv pages for the already-frozen S01--S09 pool. It did not add a tenth
source, did not run an expanded novelty search, did not perform a full-text
theorem audit of any source, and did not prove absolute noncollision or
priority.

Its exact disposition is:

- metadata audit: PASS;
- source count: exactly nine;
- tenth source: forbidden and absent;
- proof transfer: false;
- priority claim: false;
- novelty expansion: false; and
- external write, author contact, or network effect beyond read-only metadata
  fetches: zero.

The exact future citation keys are frozen. S01--S08 must be future `@article`
records. S09 must be a future `@misc` record unless a later governed metadata
transition explicitly replaces that status. ArXiv and version-of-record forms
count as one source and one bibliography entry, never as separate citations.

### S01 — BellonVialletAlgebraicEntropy

- Authors: M. P. Bellon and C.-M. Viallet.
- Title: Algebraic Entropy.
- Version of record: Communications in Mathematical Physics 204(2), 425--437
  (1999).
- Published DOI: 10.1007/s002200050652.
- Official arXiv identifier: chao-dyn/9805006v3, dated 1998-06-03.
- Permitted role: baseline algebraic-entropy and degree-growth context only.
- Access actually used: official Springer metadata page plus official arXiv
  abstract/submission-history page; bounded metadata only, not a full theorem
  audit.
- URLs: https://doi.org/10.1007/s002200050652 and
  https://arxiv.org/abs/chao-dyn/9805006.

### S02 — HasselblattProppMonomialDegreeGrowth

- Authors: Boris Hasselblatt and James Propp.
- Title: Degree-growth of monomial maps.
- Version of record: Ergodic Theory and Dynamical Systems 27(5), 1375--1397
  (2007).
- Published DOI: 10.1017/S0143385707000168.
- Official arXiv identifier: math/0604521v5, dated 2007-07-11.
- Permitted role: caution that general degree sequences need not satisfy a
  fixed linear recurrence; monomial-map results do not prove the present
  polynomial recurrence.
- Access actually used: official Cambridge metadata page plus official arXiv
  abstract/submission-history page; bounded metadata only, not a full theorem
  audit.
- URLs: https://doi.org/10.1017/S0143385707000168 and
  https://arxiv.org/abs/math/0604521.

### S03 — FordyHoneSymplecticCluster

- Authors: Allan P. Fordy and Andrew Hone.
- Title: Symplectic Maps from Cluster Algebras.
- Version of record: SIGMA 7, Paper 091, 12 pages (2011).
- Published DOI: 10.3842/SIGMA.2011.091.
- Official arXiv identifier: 1105.2985v2, dated 2011-09-22.
- Permitted role: closest public symplectic and tropical branch-switching
  neighbor; different birational cluster class.
- Access actually used: official SIGMA article page plus official arXiv
  abstract/submission-history page; bounded metadata only, not a full theorem
  audit.
- URLs: https://sigma-journal.com/2011/091/ and
  https://arxiv.org/abs/1105.2985.

### S04 — FordyHoneClusterPoisson

- Authors: Allan P. Fordy and Andrew Hone.
- Title: Discrete Integrable Systems and Poisson Algebras From Cluster Maps.
- Version of record: Communications in Mathematical Physics 325(2),
  527--584 (2014).
- Published DOI: 10.1007/s00220-013-1867-y.
- Official arXiv identifier: 1207.6072v2, dated 2012-08-23.
- Permitted role: closest public monodromy-style tropical degree mechanism;
  no local carry, no-cancellation, or visibility theorem for the present
  shears.
- Access actually used: official Springer metadata page plus official arXiv
  abstract/submission-history page; bounded metadata only, not a full theorem
  audit.
- URLs: https://doi.org/10.1007/s00220-013-1867-y and
  https://arxiv.org/abs/1207.6072.

### S05 — IshibashiKanoSignStableEntropy

- Authors: Tsukasa Ishibashi and Shunsuke Kano.
- Title: Algebraic entropy of sign-stable mutation loops.
- Version of record: Geometriae Dedicata 214(1), 79--118 (2021).
- Published DOI: 10.1007/s10711-021-00606-1.
- Official arXiv identifier: 1911.07587v5, dated 2021-04-21.
- Permitted role: strongest warning that periodic tropical switching is not
  novel by itself; different cluster-transformation formalism.
- Access actually used: official Springer metadata page plus official arXiv
  abstract/submission-history page; bounded metadata only, not a full theorem
  audit.
- URLs: https://doi.org/10.1007/s10711-021-00606-1 and
  https://arxiv.org/abs/1911.07587.

### S06 — JaneczkoJelonekPolynomialSymplectomorphisms

- Authors: Stanisław Janeczko and Zbigniew Jelonek.
- Title: Polynomial symplectomorphisms.
- Version of record: Bulletin of the London Mathematical Society 40(1),
  108--116 (2008).
- Published DOI: 10.1112/blms/bdm112.
- Official arXiv identifier: none verified in the bounded official-source
  recheck.
- Permitted role: polynomial symplectomorphism class background only; no
  exact degree law or period-two selector-exchange theorem is supplied.
- Access actually used: official DOI / journal metadata page only; bounded
  metadata only, not a full theorem audit.
- URL: https://doi.org/10.1112/blms/bdm112.

### S07 — BlancVanSantenAffineTriangular

- Authors: Jérémy Blanc and Immanuel van Santen.
- Title: Dynamical degrees of affine-triangular automorphisms of affine
  spaces.
- Version of record: Ergodic Theory and Dynamical Systems 42(12),
  3551--3592 (2022), online 2021-10-01.
- Published DOI: 10.1017/etds.2021.90.
- Official arXiv identifier: 1912.01324v2, dated 2021-03-13.
- Permitted role: weak-Perron realization and weighted-degree comparison
  context; Paper 24 must not claim first realization.
- Access actually used: official Cambridge metadata page plus official arXiv
  abstract/submission-history page; bounded metadata only, not a full theorem
  audit.
- URLs: https://doi.org/10.1017/etds.2021.90 and
  https://arxiv.org/abs/1912.01324.

### S08 — DangFavreSpectralInterpretations

- Authors: Nguyen-Bac Dang and Charles Favre.
- Title: Spectral interpretations of dynamical degrees and applications.
- Version of record: Annals of Mathematics 194(1), 299--359 (2021),
  published online 2021-06-23.
- Published DOI: 10.4007/annals.2021.194.1.5.
- Official arXiv identifier: 2006.10262v2, dated 2021-05-11.
- Permitted role: general spectral context only; the explicit visible
  monodromy remains a local proof.
- Access actually used: official Annals metadata page plus official arXiv
  abstract/submission-history page; bounded metadata only, not a full theorem
  audit.
- URLs: https://annals.math.princeton.edu/2021/194-1/p05,
  https://doi.org/10.4007/annals.2021.194.1.5, and
  https://arxiv.org/abs/2006.10262.

### S09 — ShaoSunDimensionFour

- Authors: Enbo Shao and Xiaosong Sun.
- Title: Dynamical degrees of affine-triangular automorphisms in dimension
  four.
- Official arXiv identifier: 2509.14584v1, dated 2025-09-18.
- Official arXiv DOI: 10.48550/arXiv.2509.14584.
- Version-of-record, journal, and published DOI status as of 2026-08-25 UTC:
  no journal reference, version-of-record page, or non-arXiv publisher DOI
  was verified in this bounded official-source recheck. This is an
  access-limited metadata finding, not an absolute theorem that no later
  publication exists.
- Future record type: `misc`.
- Permitted role: current nearby affine-triangular neighbor in a different
  class; no direct collision certificate beyond the bounded review.
- Access actually used: official arXiv abstract/submission-history page plus
  exact-title official-source search limited to publication-status discovery;
  bounded metadata only, not a full theorem audit.
- URL: https://arxiv.org/abs/2509.14584.

### Citation use and final identity-check rules

The exact nine keys above are the complete future bibliography: each must
appear exactly once as its frozen record type, none may be omitted or
duplicated, and there is no tenth source. No citation may prove or replace a
gradient, symplecticity calculation, support row, selector, wall inequality,
carry comparison, top-form-survival step, visibility inequality, matrix
product, eigenpair, determinant derivation, recurrence, wall-gap law, parity
closed form, or boundary audit.

The future contextual synthesis must be organized by mathematical question,
not as a source-by-source novelty parade. It may say only that the bounded
screen and official metadata recheck located no direct conflict with the
complete frozen package through 2026-08-25 UTC if it also says the screen was
nonexhaustive. It may not claim firstness, priority, uniqueness, or full
theorem noncollision.

Immediately before any later source-only author writes the source trio, a
final identity check is mandatory. It must reverify:

1. all nine exact keys;
2. author spelling, order, and diacritics;
3. article versus `misc` record types;
4. titles, years, journals, volumes, issues, pages, DOIs, and URLs;
5. the exact arXiv version strings recorded above;
6. that S09 still has the latest verified official arXiv version and the
   currently verified publication-status statement;
7. that no tenth source has appeared in the proposed bibliography; and
8. that no direct collision or deeper access claim has silently replaced the
   bounded review language.

On any conflict, the source author must stop and return to governance. It may
not silently repair metadata, add or swap a citation, deepen an access claim,
expand novelty, or begin TeX/BibTeX authoring.

No `references.bib` file is created or authorized by this scope.

## 8. Public/private firewall and sanitization/build-verification obligations

The public article must reproduce every theorem-critical definition and proof
locally, but it must reveal none of the private governance material used to
freeze them. The public/private field firewall is exact:

- public bytes may contain only the anonymous theorem narrative, formulas,
  tables, and the nine frozen bibliography entries;
- private bytes include all hashes, inventories, queue names, lifecycle
  records, reviews, source-lock material, candidate-review history, internal
  predecessor bookkeeping, and every local path outside the permitted future
  bibliography URLs above;
- private predecessor lineage to Papers 20--23 may inform the bounded
  comparison language but may not enter the public bibliography,
  acknowledgments, comments, metadata, or numbering; and
- no identity, venue, funding, acknowledgment, or internal review signal may
  survive in the public trio, bibliography, rendered PDF, bookmarks, or
  auxiliary metadata.

Later source-only and build-only actors, if separately authorized by future
governance, must satisfy all of the following verification obligations:

1. the source trio remains UTF-8, LF-only, BOM-free, CR-free, and NUL-free;
2. the title, author, and `\date{}` identity fields match Section 2 exactly;
3. the bibliography contains exactly S01--S09 once each, in the frozen record
   types, with no hidden note/file/abstract fields and no tenth source;
4. no acknowledgment, venue marker, funding text, local path, hash, queue
   string, reviewer name, or comment leak survives in `paper/main.tex`,
   `paper/math_commands.tex`, `paper/references.bib`, or any generated PDF
   metadata;
5. the rendered PDF title equals the exact full title above;
6. the rendered PDF author, creator, and producer metadata are each empty;
7. bookmarks, headers, footers, and hyperlinks reveal no internal
   identifiers, paths, usernames, machine names, or build-tool traces;
8. the public article still contains zero figures/assets and exactly the three
   mandatory mathematical tables above; and
9. the build verifier treats any metadata leak, table-count drift,
   bibliography drift, or title/author/date drift as a blocker.

This scope authorizes none of those later actions now. It only freezes the
obligations.

## 9. Canonical lifecycle dependency, permission chain, and later publication-lock contract

The only valid lifecycle order is exactly:

SOURCE_DESIGN_PASS -> source_lock.json -> SOURCE_LOCK_PASS -> PAPER_PLAN.md -> PAPER_PLAN_PASS -> PUBLICATION_STAGE_SCOPE.md -> PUBLICATION_STAGE_PASS -> publication_lock.json -> PUBLICATION_LOCK_PASS -> separate root transition -> exact source trio

No stage may be skipped, reordered, merged, or treated as inherited
downstream authority. In particular:

- `PAPER_PLAN_PASS` authorizes only this scope stage, not publication lock,
  manuscript, bibliography, or build;
- a valid `PUBLICATION_STAGE_PASS` has only one eligibility effect: after a
  separate parent/root transition, it may make
  `experiments/publication_lock.json` eligible for one distinct lock-only
  author;
- no future PASS automatically authorizes the public source trio, a build,
  PDF, release, submission, upload, hosting, repository push, transport,
  identity disclosure, or any external effect.

At this author stop, the sole possible subsequent project write is:

`notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md`

It may be created only by a fresh independent reviewer who authored none of
this scope or any bound upstream input. The reviewer must read and hash the
stable scope and all fifteen upstream files, recheck both current root
identities, replay the complete mathematical contract, independently audit the
exact nine-source metadata and access limitations, validate the public/private
firewall, and verify the exact inventory and permissions.

If any conjunctive check fails, the disposition is exactly:

`WRITE NOTHING`

The reviewer may not create a failure report inside the project, repair this
scope, or issue a partial PASS. Only if every check passes may the reviewer
create the sole path above. Its final nonempty line must be exactly:

`PUBLICATION_STAGE_PASS`

Only after a valid `PUBLICATION_STAGE_PASS` and a separate root transition may
a distinct publication-lock author create exactly one path:

`experiments/publication_lock.json`

The future lock must be strict-canonical UTF-8 JSON with one physical compact
JSON line and exactly one terminal LF; no duplicate keys, floating-point or
nonfinite values, BOM, CR, NUL, trailing record, or symlink substitution;
recursively code-point-sorted object keys; byte-exact canonical round trip
under two independent strict implementations; and explicit null self
SHA-256/byte fields.

At the publication-lock author stop, the three future public source paths must
still remain absent. The fresh publication-lock reviewer's sole possible write
will be:

`notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md`

A blocker again requires `WRITE NOTHING`. Only a full independent review may
create that path and end it exactly:

`PUBLICATION_LOCK_PASS`

Only a separate later root transition after a valid
`PUBLICATION_LOCK_PASS` may open one source-only author invocation for the
exact trio:

- `paper/main.tex`;
- `paper/math_commands.tex`; and
- `paper/references.bib`.

Even that later transition would not by itself authorize code, figures,
assets, experiments, datasets, a build, a PDF, release, submission, upload,
public hosting, repository push, transport, messaging, identity disclosure,
or any external effect. Those remain closed until separately and explicitly
opened by later governance.

## 10. Zero-science, no-code, and no-external-effect lock

This scope stage has exactly zero scientific experiment, numerical run,
floating-point spectrum, parameter sweep, finite-iterate table, CAS or
symbolic certificate, dataset, plot, figure, asset generation, GPU action,
code execution for theorem evidence, build, PDF action, external upload,
author contact, submission, transport, public hosting, repository push,
message, identity disclosure, or release.

The bounded metadata recheck in Section 7 was read-only bibliographic
verification only. It was not theorem evidence, not a novelty expansion, and
not a scientific run.

Read-only local hashing, inventory checking, text parsing, formula review, and
official metadata lookup do not authorize a headline theorem beyond the frozen
object, and they do not authorize any downstream stage. Nothing in this scope
is publication consent or communication authority.

## 11. Exact scope-author-stop inventory

Immediately before this sole write, the project contained exactly:

- fifteen regular files;
- four child directories;
- zero symlinks; and
- zero other filesystem objects.

After this sole write, the project must contain exactly:

- sixteen regular files;
- the same four child directories;
- zero symlinks; and
- zero other filesystem objects.

The four child directories are exactly:

- experiments;
- notes;
- paper; and
- refine-logs.

The sixteen regular files at scope-author stop are exactly:

- experiments/EXPERIMENT_PLAN.md;
- experiments/EXPERIMENT_TRACKER.md;
- experiments/source_lock.json;
- notes/CITATION_VERIFICATION.md;
- notes/CLAIMS_EVIDENCE_MATRIX.md;
- notes/INDEPENDENT_PAPER_PLAN_REVIEW.md;
- notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md;
- notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md;
- notes/NOVELTY_ASSESSMENT.md;
- notes/PROOF_PACKAGE.md;
- notes/PUBLICATION_STAGE_SCOPE.md;
- notes/RESEARCH_QUESTION.md;
- paper/PAPER_PLAN.md;
- refine-logs/FINAL_PROPOSAL.md;
- refine-logs/INITIAL_PROPOSAL.md; and
- refine-logs/REVIEW_SUMMARY.md.

At this author stop, all of the following exact future paths are absent:

- notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md;
- experiments/publication_lock.json;
- notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md;
- paper/main.tex;
- paper/math_commands.tex; and
- paper/references.bib.

Every build, PDF, auxiliary, code, data, figure, asset, result, release,
submission, transport, and external-action artifact is also absent and
unauthorized.

The scope author must now perform stable readback, report this file's
external SHA-256, byte count, LF count, terminal line, and exact inventory to
the governing parent, and stop. This author claims no independent PASS.

PUBLICATION SCOPE AUTHOR STOP
