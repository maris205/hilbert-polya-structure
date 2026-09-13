# Independent Source-Design Review — Paper 24

Date scope: 2026-08-25 UTC.

Reviewer role and independence statement:

- I am independent of the ten-file source-design author package and of both
  candidate reviewers.
- I read only the authorized Paper 24 ten-file package under
  `papers/24-hamiltonian-period-two-selector-exchange/{experiments,notes,refine-logs}`
  together with the authorized governance records
  `BATCH_06_STATUS.md`, `BATCH_06_IDEA_REPORT.md`,
  `BATCH_06_PAPER24_CANDIDATE_REVIEW_R1.md`,
  `BATCH_06_PAPER24_CANDIDATE_REVIEW_R1_CORRECTION.md`,
  `BATCH_06_PAPER24_CANDIDATE_REVIEW_R2.md`, and
  `BATCH_06_PAPER24_CANDIDATE_REVIEW_R2_CORRECTION.md`.
- I did not read, list, stat, glob, or touch the excluded roots
  `/tmp/paper23-r0-A.DyWKGR`, `/tmp/paper23-r0-B.dsQvTx`,
  `/tmp/paper23-r0-repair-A.BzlBNd`, `/tmp/paper23-r0-repair-B.TVRci7`, or
  `/tmp/paper23-r1-evidence-recovery.h8tfL9eu`.
- I used no web or network access and made no write before this review file.

## 1. Scope, method, and instruction-level correction

This review is a bounded offline source-design gate for the frozen Paper 24
family

\[
V_m=Aq_1^m q_2^2+Bq_1q_2^{2m},
\qquad
W_{m,s}=Cp_1^{s(2m+1)+1}+Dp_2^{sm+1},
\]

with characteristic-zero field, integers \(m\ge2\), \(s\ge1\), and arbitrary
nonzero coefficients \(A,B,C,D\).

Method:

1. verify the exact opening inventory and file hygiene;
2. rehash every source file and the aggregate package;
3. verify candidate-review provenance bindings;
4. rederive the selector, carry, visibility, monodromy, determinant, spectrum,
   recurrence, wall-gap, and parity formulas independently;
5. audit claim/evidence separation, anti-claims, theorem boundaries, and
   citation-boundary discipline;
6. decide whether any remaining defects are gate blockers or merely downstream
   tightening items.

Instruction-level correction handled in this resumed review:

- The first invocation was correctly zero-write because the task instruction
  supplied aggregate SHA-256
  `f19ac071e017b252a7ff6d96e627a16607373cafc2e5f8c2f26dbb3842321b91`,
  which does not match the live ten-file package under the standard
  uint64-big-endian length-framed rule.
- The parent later corrected only the review instruction, not the source
  package. The authoritative contract for the frozen ten-file package is:
  66,142 content bytes, 2,176 LF, 66,590 framed bytes, aggregate SHA-256
  `ca447f74449cee1f04c9f6181c2325b2350a975e59a8624aa8705b350f7e8e67`.
- I independently confirmed that the old `f19ac...` value is absent from
  `BATCH_06_STATUS.md`, `BATCH_06_IDEA_REPORT.md`, and all ten Paper 24 source
  files. It is therefore not a frozen governance or source identity.

## 2. Exact inventory and identity audit

### 2.1 Opening inventory

The live Paper 24 source-design package contains exactly:

- 10 regular files;
- 3 directories: `experiments`, `notes`, `refine-logs`;
- 0 symlinks;
- 0 other objects.

This matches the authorized ten-file source-design universe.

### 2.2 Encoding and newline hygiene

All 10 source files are:

- valid UTF-8;
- LF-only;
- terminated by a final LF;
- free of NUL bytes.

No source file contains an independent-pass token.

### 2.3 Candidate-review provenance bindings

I independently rehashed the four Paper 24 candidate-review records and
confirmed exact agreement with the values recorded in governance and in the
source package:

| Artifact | SHA-256 | Bytes | LF | Terminal line |
|---|---|---:|---:|---|
| `BATCH_06_PAPER24_CANDIDATE_REVIEW_R1.md` | `b2802f24ca5de3d91b7ea5a1726a0cf12d6f36053055e24e3759124bfc8709c1` | 30,703 | 878 | `PAPER24_CANDIDATE_GATE_PASS_R1` |
| `BATCH_06_PAPER24_CANDIDATE_REVIEW_R1_CORRECTION.md` | `dabf9fa2873aa0124e2d510dc20b581b51a5648e0828f33bc2b7a41b2172730d` | 2,583 | 112 | `PAPER24_CANDIDATE_GATE_PASS_R1_CORRECTED` |
| `BATCH_06_PAPER24_CANDIDATE_REVIEW_R2.md` | `914b92255cd9aae2b8be4707484ebf63a72d1b40e1cf1fc356dd365676ed25bd` | 19,672 | 769 | `PAPER24_CANDIDATE_GATE_PASS_R2` |
| `BATCH_06_PAPER24_CANDIDATE_REVIEW_R2_CORRECTION.md` | `1c311a979b3c8fc396734bbd851f1a6c8ed5738a2f3005048688f623a6bcaf6b` | 2,500 | 115 | `PAPER24_CANDIDATE_GATE_PASS_R2_CORRECTED` |

### 2.4 Live ten-file source identities

I independently rehashed the entire source-design package:

| Relative path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `experiments/EXPERIMENT_PLAN.md` | `bfd644a19d15f51a4c7eca6323909852d38e7477afac73aea77b02642ffb6f94` | 7,098 | 186 |
| `experiments/EXPERIMENT_TRACKER.md` | `61e34652fdea217b0da4f7774478f243ca806fb88a97e18f09d767e24fbe8db0` | 3,459 | 59 |
| `notes/CITATION_VERIFICATION.md` | `66558b974ebdcc0fd7627c52c4caee0c80b404514d06f622ededd9b9a8900fb9` | 6,694 | 93 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `28f8f3dd6add8617a63c16b5d6956d5a1214dc453a2416721dca824faba00dc5` | 7,040 | 114 |
| `notes/NOVELTY_ASSESSMENT.md` | `e873bcdc57c0f39e04b950bf9221c894993370c1accd313cbcb05495fa92fb2c` | 5,532 | 119 |
| `notes/PROOF_PACKAGE.md` | `b6df4be9e9a00a5ae71e48505b007a59fea70bcff3046661af804714378963bf` | 18,290 | 1,048 |
| `notes/RESEARCH_QUESTION.md` | `5dc091d3500800610360512f464a877adb51c1f83857c8335a28dccebd35ef7d` | 5,052 | 132 |
| `refine-logs/FINAL_PROPOSAL.md` | `bf04aa95c67b19bc876c594b8162534c7000f12a92fc696017d36bf9cf7e96bf` | 4,773 | 175 |
| `refine-logs/INITIAL_PROPOSAL.md` | `7e5d64d5c4d3029d8d9d10f82c5dee41e66c5c2fb9cc3271e203657eeb74a8dc` | 3,971 | 148 |
| `refine-logs/REVIEW_SUMMARY.md` | `b2357b00fb2a9e05dbc96db775be9ef6a243e164b5b720525ecef9b3bd220c82` | 4,233 | 102 |

Package totals:

- content bytes: 66,142;
- LF count: 2,176.

Under the standard byte-sorted relative-path framing rule

\[
\mathrm{uint64\_be}(|name|)\,\|\,name\,\|\,\mathrm{uint64\_be}(|content|)\,\|\,content
\]

the aggregate package is:

- framed bytes: 66,590;
- SHA-256: `ca447f74449cee1f04c9f6181c2325b2350a975e59a8624aa8705b350f7e8e67`.

This matches the corrected authoritative contract supplied in the resumed task.

## 3. Independent theorem and proof audit

I independently rederived the main algebraic spine and found the theorem
package mathematically coherent as frozen.

### 3.1 Exact symplecticity and inverses

The literal gradients are correct:

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

The subtraction inverses are exact, the shear Jacobians have the standard
block-triangular Hessian form, both Hessians are symmetric, and the map is an
exact-gradient polynomial symplectomorphism.

Verdict: PASS.

### 3.2 Selector wall, branch matrices, and strict period-two exchange

Both first-phase competitive differences equal

\[
(m-1)(u_1-2u_2),
\]

so the common selector wall is exactly \(r=u_1/u_2=2\). The selected matrices
are exactly

\[
A_-=\begin{pmatrix}0&2m\\1&2m-1\end{pmatrix},
\qquad
A_+=\begin{pmatrix}m-1&2\\m&1\end{pmatrix},
\qquad
B_m=\operatorname{diag}(2m+1,m).
\]

The projective branches are exactly

\[
h_m(r)=\frac{2(2m+1)}{r+2m-1},
\qquad
\ell_m(r)=\frac{(2m+1)((m-1)r+2)}{m(mr+1)}.
\]

I independently rechecked the corrected identities

\[
\ell_m(r)-1=
\frac{(m^2-m-1)r+3m+2}{m(mr+1)},
\qquad
2-\ell_m(r)=
\frac{(m+1)(r-2)}{m(mr+1)}.
\]

Hence \(0<r<2\Rightarrow h_m(r)>2\) and \(r>2\Rightarrow1<\ell_m(r)<2\), with
the wall \(r=2\) correctly excluded as a genuine tie boundary. The ordinary
seed \((1,1)^{\mathsf T}\) therefore follows the strict period-two itinerary
\(-,+,-,+,\ldots\).

Verdict: PASS.

### 3.3 Actual carry, unique top forms, no cancellation, and \(q_1\) visibility

The package does not stop at tropical selector choice. It proves the two
separate temporal carry obligations:

- first-phase fresh selected rows beat the carried momentum coordinates;
- second-phase pure-power rows beat the carried position coordinates.

These inequalities are written explicitly in both chambers and are valid already
at \(s=1\); the proof does not rely on an asymptotic-large-\(s\) shortcut.

The arbitrary-nonzero-coefficient claim is proved by a domain/top-homogeneous
argument rather than a positivity argument: once the selected top source is
unique and strictly above both the losing derivative term and the carried
coordinate, its top homogeneous part survives over a domain. Characteristic
zero is used exactly to prevent derivative scalars from vanishing.

The visibility argument is also complete. In particular, the negative-chamber
comparison uses the corrected exact identity

\[
u_{n+1,1}=sm\,h_m(r_n)\,v_{n+1,2},
\]

before concluding strict dominance. The positive-chamber comparison with the
second momentum coordinate is given by direct expansion. Thus \(q_1\) is
strictly maximal among all four coordinates for every \(n\ge1\), and

\[
d_n=\deg(F_{m,s}^n)=u_{n,1}
\]

is justified for positive iterates, with the tied seed \(d_0=1\) handled
separately.

Verdict: PASS.

### 3.4 Monodromy, determinant, trace, eigenvalues, recurrence, wall gaps

The exact two-step monodromy is

\[
P=(B_mA_+)(B_mA_-)
=
\begin{pmatrix}
2m(2m+1)&2m(2m+1)(2m^2+m-2)\\
m^2&m^2(4m^2+4m-1)
\end{pmatrix}.
\]

I independently verified:

- \(P(2,1)^{\mathsf T}=H(2,1)^{\mathsf T}\) with
  \(H=m^2(2m+1)^2\);
- \(\operatorname{tr}(P)=H+L\) with \(L=2m(m+1)\);
- \(\det(P)=HL\);
- therefore the second eigenvalue is \(L\);
- the actual two-step map \(C_+C_-=s^2P\) has eigenvalues \(s^2H\) and
  \(s^2L\);
- \(\lambda_1(F_{m,s})=sm(2m+1)\).

The source package also correctly gives

\[
u_{2j}=(s^2P)^j(1,1)^{\mathsf T},
\qquad
u_{2j+1}=sB_mA_-(s^2P)^j(1,1)^{\mathsf T},
\]

the stride-two recurrence

\[
d_{n+4}=s^2(H+L)d_{n+2}-s^4HL\,d_n,
\]

the initial values

\[
d_0=1,\quad
d_1=2m(2m+1)s,\quad
d_2=2m(m+1)(2m-1)(2m+1)s^2,\quad
d_3=8m^4(m+1)(2m+1)s^3,
\]

and the corrected third vector

\[
u_3=
\begin{pmatrix}
8m^4(m+1)(2m+1)s^3\\
2m^2(m+1)(2m-1)(2m^2+2m+1)s^3
\end{pmatrix}.
\]

The wall-gap identities

\[
u_{2j,1}-2u_{2j,2}=-(s^2L)^j,
\qquad
u_{2j+1,1}-2u_{2j+1,2}=2ms(s^2L)^j
\]

follow from the left-eigenvector equalities for \((1,-2)\), which I
recomputed independently.

Verdict: PASS.

### 3.5 Parity closed forms and integrality logic

The parity closed forms in `notes/PROOF_PACKAGE.md` are algebraically
consistent with the matrix law. I independently checked the displayed even and
odd formulas against the spectral decomposition and found no discrepancy.

The integrality logic is also correct: it is grounded in the exact integer
matrix formulas for \(u_{2j}\) and \(u_{2j+1}\), equivalently in the
integer-coefficient recurrence plus integer initial data, not in informal
denominator-divisibility heuristics.

Verdict: PASS.

### 3.6 Bounded structural lemma and conditional period-\(k\) lemma

The crossed-binomial / diagonal-pure-power lemma is correctly bounded. It
proves synchronous switching at the wall

\[
R=\frac{d-b}{a-c},
\]

and the wall-fixing ratio

\[
\frac ef=\frac{R(L_{\mathrm{wall}}-1)}{L_{\mathrm{wall}}-R},
\]

but it explicitly does not claim that chamber exchange alone proves temporal
carry, actual polynomial degree transport, or visibility. The \(R=1\) failure
boundary is also stated.

The period-\(k\) selector-to-monodromy statement is kept technical and
conditional: unique strict faces, strict carry, nonzero leading forms, linear
face maps, and visible Perron class are all named hypotheses. The package does
not oversell this lemma as the public novelty claim.

Verdict: PASS.

## 4. Claim/evidence/nonclaim audit

The package maintains a clean division between:

- literal identities and supports;
- chamber inequalities;
- carry and visibility inductions;
- top-homogeneous survival;
- exact arithmetic for the monodromy, determinant, spectrum, recurrence, and
  parity laws;
- bounded novelty and portfolio claims.

The theorem is anchored to the explicit \(m,s\)-family and the standard seed.
The wall \(r=2\), positive characteristic, zero coefficients, \(m=1\),
period-\(>2\) realizations, general selector-fan claims, and literature
priority are all explicitly locked out.

I found no hidden enlargement from the accepted candidate scope.

Verdict: PASS.

## 5. Citation-boundary and novelty audit

`notes/CITATION_VERIFICATION.md` is source-design adequate for this stage.

Why it passes:

- it binds the exact four candidate-review artifacts that control the public
  novelty boundary;
- it explicitly states that the source-design author performed no new network
  lookup;
- it distinguishes corrected R1 as the bounded public-source ledger and R2 as
  an offline proof review;
- it records identifiable bibliographic anchors for the cited public neighbors
  (DOI and/or arXiv identifiers together with source names and role);
- it maps each citation only to bounded positioning claims, not to theorem
  proof steps;
- it explicitly blocks absolute-priority language, novelty inflation of
  tropical switching, and misuse of Paper 20 lineage.

This is enough for a source-design gate because the paper is not yet at the
bibliography-authoring stage. A later manuscript stage may format and expand
bibliographic details, but no source-design blocker remains in the current
citation ledger.

Verdict: PASS.

## 6. Permission and anti-claim audit

The package remains proof-only and does not silently open downstream stages.

Confirmed:

- no source lock, paper plan, manuscript, TeX, BibTeX, figure, code, data,
  build, PDF, release, Paper 25 work, submission, upload, hosting, push,
  transport, message, or identity disclosure is authorized;
- the experiment files are explicitly zero-science analytic verification
  scaffolds;
- the anti-claim ledgers across `RESEARCH_QUESTION.md`,
  `CLAIMS_EVIDENCE_MATRIX.md`, `NOVELTY_ASSESSMENT.md`, and `FINAL_PROPOSAL.md`
  are consistent with the corrected candidate gates.

Verdict: PASS.

## 7. Remaining issues: blocker analysis

I found two residual issues worth recording. Neither is a gate blocker.

### 7.1 Omitted one-line expansion behind \(\det(P)=HL\)

`notes/PROOF_PACKAGE.md` states the determinant identity correctly but does not
show the short expansion or multiplicative determinant factorization on the
page. I independently recomputed the determinant from the displayed matrix and
confirmed

\[
\det(P)=2m^3(m+1)(2m+1)^2=HL.
\]

Classification: nonblocking downstream tightening item.

Reason: the displayed matrix is explicit, the determinant identity is true, the
second-eigenvalue step is sound once that determinant is written out, and no
other argument depends on hidden computation. A later manuscript or lock stage
should add the missing line for presentation completeness.

### 7.2 No per-file hash table inside `refine-logs/REVIEW_SUMMARY.md`

`refine-logs/REVIEW_SUMMARY.md` enumerates the exact ten authorized paths and
the candidate-review provenance but does not itself include a ten-row source
hash/bytes/LF table.

Classification: nonblocking downstream tightening item.

Reason: the exact ten-path universe is fixed, the package contains no extra
objects, this review independently bound every live file identity and the live
aggregate package identity, and the omission does not alter theorem content,
permissions, or anti-claims. It is weaker handoff ergonomics than the more
verbose Paper 23 addendum style, but it does not prevent a fresh reviewer from
auditing the actual frozen source-design universe. Future governance stages may
prefer to restate the ten-row table for stylistic consistency.

## 8. Scores

Independent source-design scores:

| Dimension | Score |
|---|---:|
| theorem/proof integrity | 9.5 / 10 |
| source-design completeness | 8.9 / 10 |
| citation-boundary discipline | 9.3 / 10 |
| lifecycle/governance cleanliness | 8.4 / 10 |

Rationale:

- the proof spine is short, explicit, and independently reproducible;
- the package keeps the candidate-correction arithmetic fixed correctly;
- the novelty ledger is disciplined and bounded;
- the only weaknesses are presentation-level tightening items, not theorem or
  permission failures.

## 9. Terminal verdict

All real source-design gates pass under the corrected authoritative aggregate
contract:

- exact authorized inventory: PASS;
- live file identities and corrected aggregate identity: PASS;
- full theorem/proof package: PASS;
- claim/evidence separation and anti-claims: PASS;
- citation-boundary discipline: PASS;
- permission discipline: PASS;
- residual issues classified nonblocking.

This review therefore authorizes the Paper 24 source-design stage to close and
the next lifecycle stage to be considered by a distinct authorized role.

SOURCE_DESIGN_PASS
