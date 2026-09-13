# Independent Source-Lock Review — Paper 24

## 1. Reviewer role, scope, and zero-write restart

I am a fresh independent source-lock reviewer for
`papers/24-hamiltonian-period-two-selector-exchange`. I authored none of the
ten source-design files, none of the four root candidate review/correction
records, none of the independent source-design review, none of
`experiments/source_lock.json`, and none of the live governance records.

I read the required research-review skill instructions first, then performed a
local no-network, no-delegation audit of exactly the artifacts named by the
lock contract:

- the ten author files named in the allowlist;
- `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md`;
- `BATCH_06_PAPER24_CANDIDATE_REVIEW_R1.md`;
- `BATCH_06_PAPER24_CANDIDATE_REVIEW_R1_CORRECTION.md`;
- `BATCH_06_PAPER24_CANDIDATE_REVIEW_R2.md`;
- `BATCH_06_PAPER24_CANDIDATE_REVIEW_R2_CORRECTION.md`;
- `BATCH_06_STATUS.md` through EOF;
- `BATCH_06_IDEA_REPORT.md` through EOF; and
- `experiments/source_lock.json`.

I initially made a zero-write interpretation error: I treated the full live
`BATCH_06_STATUS.md` as if it had to preserve the historical authoring snapshot
as a byte-identical file prefix. After rereading the controlling governance
rule in `BATCH_06_STATUS.md` lines 173–175 and the lock’s own
`snapshot_semantics` text, I resumed the same review without any intermediate
write. The controlling rule is narrower:

- `BATCH_06_STATUS.md` is a controlled lifecycle dashboard;
- its Material Passport, current queue state, and current permissions may
  change only at a validated transition; and
- only the Activity Log is append-only.

This distinction resolves the only earlier blocker. No source-design,
candidate, or lock byte changed between the zero-write interpretation and this
resumed review.

## 2. Opening live identities and inventory

At review opening, the project inventory was exactly:

- 12 regular files;
- 3 child directories (`experiments`, `notes`, `refine-logs`);
- 0 symlinks; and
- 0 other objects.

The review path
`papers/24-hamiltonian-period-two-selector-exchange/notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md`
was absent at opening, as required.

All forbidden directories named by the lock were absent:

- `build`
- `code`
- `data`
- `figures`
- `manuscript`
- `paper`
- `publication`
- `release`
- `results`
- `submission`
- `transport`

The live bound identities I recomputed are:

| Artifact | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `experiments/source_lock.json` | 45,607 | 1 | `45ce6527917d7172ff10e87db1e716b6e7caa2de3fa3cfbd54cd73b034003232` |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | 16,630 | 490 | `1c733058483cb28370e4c6f283126c14305ce45de43010e7753a4d92a5f8ece8` |
| `BATCH_06_PAPER24_CANDIDATE_REVIEW_R1.md` | 30,703 | 878 | `b2802f24ca5de3d91b7ea5a1726a0cf12d6f36053055e24e3759124bfc8709c1` |
| `BATCH_06_PAPER24_CANDIDATE_REVIEW_R1_CORRECTION.md` | 2,583 | 112 | `dabf9fa2873aa0124e2d510dc20b581b51a5648e0828f33bc2b7a41b2172730d` |
| `BATCH_06_PAPER24_CANDIDATE_REVIEW_R2.md` | 19,672 | 769 | `914b92255cd9aae2b8be4707484ebf63a72d1b40e1cf1fc356dd365676ed25bd` |
| `BATCH_06_PAPER24_CANDIDATE_REVIEW_R2_CORRECTION.md` | 2,500 | 115 | `1c311a979b3c8fc396734bbd851f1a6c8ed5738a2f3005048688f623a6bcaf6b` |
| live `BATCH_06_STATUS.md` | 120,498 | 1,763 | `1ca8427a3ba4a7119f7f34e94b4069405a7d9cc3096f939e919e6efe564144a5` |
| live `BATCH_06_IDEA_REPORT.md` | 207,276 | 4,071 | `cbac43f7aaef62b39393c6fe550112a9c56de089206df7b69703708d819c6dde` |

The excluded independent source-design review remained an ordinary mode-0644
non-symlink file and ended exactly with `SOURCE_DESIGN_PASS`.

## 3. Ten-file author package, aggregate, and excluded review binding

I rehashed every author file in the ten-path allowlist. All ten matched the
lock table exactly:

| Relative path | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `experiments/EXPERIMENT_PLAN.md` | 7,098 | 186 | `bfd644a19d15f51a4c7eca6323909852d38e7477afac73aea77b02642ffb6f94` |
| `experiments/EXPERIMENT_TRACKER.md` | 3,459 | 59 | `61e34652fdea217b0da4f7774478f243ca806fb88a97e18f09d767e24fbe8db0` |
| `notes/CITATION_VERIFICATION.md` | 6,694 | 93 | `66558b974ebdcc0fd7627c52c4caee0c80b404514d06f622ededd9b9a8900fb9` |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | 7,040 | 114 | `28f8f3dd6add8617a63c16b5d6956d5a1214dc453a2416721dca824faba00dc5` |
| `notes/NOVELTY_ASSESSMENT.md` | 5,532 | 119 | `e873bcdc57c0f39e04b950bf9221c894993370c1accd313cbcb05495fa92fb2c` |
| `notes/PROOF_PACKAGE.md` | 18,290 | 1,048 | `b6df4be9e9a00a5ae71e48505b007a59fea70bcff3046661af804714378963bf` |
| `notes/RESEARCH_QUESTION.md` | 5,052 | 132 | `5dc091d3500800610360512f464a877adb51c1f83857c8335a28dccebd35ef7d` |
| `refine-logs/FINAL_PROPOSAL.md` | 4,773 | 175 | `bf04aa95c67b19bc876c594b8162534c7000f12a92fc696017d36bf9cf7e96bf` |
| `refine-logs/INITIAL_PROPOSAL.md` | 3,971 | 148 | `7e5d64d5c4d3029d8d9d10f82c5dee41e66c5c2fb9cc3271e203657eeb74a8dc` |
| `refine-logs/REVIEW_SUMMARY.md` | 4,233 | 102 | `b2357b00fb2a9e05dbc96db775be9ef6a243e164b5b720525ecef9b3bd220c82` |

From those exact ten byte-sorted relative POSIX names, I independently
recomputed:

- total bytes: `66,142`;
- total LF: `2,176`;
- standard uint64-big-endian framed stream bytes: `66,590`;
- framed SHA-256:
  `ca447f74449cee1f04c9f6181c2325b2350a975e59a8624aa8705b350f7e8e67`;
- sorted text ledger bytes: `1,038`; and
- sorted text ledger SHA-256:
  `51364bd0e7c56055f17956248cc9f12bd10de6679638e8a90411394e89b51e88`.

The excluded source-design review identity also matched exactly:

- bytes: `16,630`;
- LF: `490`;
- SHA-256:
  `1c733058483cb28370e4c6f283126c14305ce45de43010e7753a4d92a5f8ece8`;
- terminal line: `SOURCE_DESIGN_PASS`.

It was correctly excluded from the ten-file author aggregate.

## 4. Candidate provenance and correction precedence

I reverified all four candidate provenance records and their terminal lines
from bytes, not from prompt text.

The immutable PASS records remained:

- R1 terminal line: `PAPER24_CANDIDATE_GATE_PASS_R1`
- R1 correction terminal line: `PAPER24_CANDIDATE_GATE_PASS_R1_CORRECTED`
- R2 terminal line: `PAPER24_CANDIDATE_GATE_PASS_R2`
- R2 correction terminal line: `PAPER24_CANDIDATE_GATE_PASS_R2_CORRECTED`

The exact correction-precedence audit remained:

1. R1-C1 supersedes only the local numerator omission in
   \(\ell_m(r)-1\), with controlling identity
   \[
   \ell_m(r)-1=\frac{(m^2-m-1)r+3m+2}{m(mr+1)}.
   \]
2. R1-C2 supersedes only the local strict-sign misuse in the negative chamber,
   with controlling equality
   \[
   u_1'=s m h_m(r) v_2,
   \]
   followed by the strict consequence \(u_1'>v_2\).
3. R2-C1 supersedes only the local missing factor in
   \[
   2-\ell_m(r)=\frac{(m+1)(r-2)}{m(mr+1)}.
   \]
4. R2-C2 supersedes only the unused second-coordinate transcription of
   \(u_3\), with controlling identity
   \[
   u_{3,2}=2m^2(m+1)(2m-1)(2m^2+2m+1)s^3.
   \]

I found no fifth correction and no drift in selectors, chamber images, carry
inequalities, visible degrees, matrices, eigenvalues, recurrence, scores, or
PASS outcomes.

## 5. Strict canonical JSON audit in two independent implementations

### 5.1 Python implementation

I implemented a strict Python audit with two layers:

1. raw-byte gate:
   - UTF-8 decoding only;
   - no BOM;
   - no CR byte;
   - no NUL byte;
   - exactly one terminal LF;
   - exactly one physical JSON line before the terminal LF; and
   - no lone surrogate code points in the decoded text;
2. strict parse and canonical round trip:
   - duplicate-key rejection before materialization using an
     `object_pairs_hook`;
   - nonfinite-token rejection via `parse_constant`;
   - canonical re-encoding with compact separators;
   - recursive key sorting by the JSON encoder; and
   - byte-exact comparison against the original lock bytes.

Results:

- bytes: `45,607`;
- LF: `1`;
- BOM: absent;
- CR: absent;
- NUL byte: absent;
- one physical JSON record: yes;
- one terminal LF: yes;
- UTF-8: valid;
- lone surrogates: absent;
- canonical round-trip bytes: exact match.

Adversarial Python cases rejected:

- duplicate key;
- `NaN`;
- `Infinity`;
- `-Infinity`;
- BOM-prefixed input;
- CRLF input;
- trailing whitespace before LF;
- extra record after the object;
- missing terminal LF; and
- noncanonical key order.

### 5.2 Custom Node implementation

I separately implemented a custom recursive Node parser/encoder rather than
relying on `JSON.parse` for duplicate detection. The Node audit enforced:

- raw-byte rejection of BOM, CR, and NUL;
- exactly one terminal LF and one physical JSON record;
- manual string parsing with escape handling and lone-surrogate rejection;
- manual integer-only number parsing;
- manual duplicate-key rejection per object;
- recursive object representation preserving source order;
- code-point-order validation of object keys during encoding; and
- byte-exact comparison of the canonical re-encoding against the original
  bytes.

Results:

- byte-exact round trip: pass;
- schema string present: `paper24.source_lock.v1`;
- duplicate key adversary: rejected;
- `NaN` adversary: rejected;
- `Infinity` adversary: rejected;
- BOM adversary: rejected;
- CR adversary: rejected;
- NUL-byte adversary: rejected;
- extra-record adversary: rejected;
- missing-terminal-LF adversary: rejected; and
- noncanonical key-order adversary: rejected.

### 5.3 Canonical contract conclusions

Both independent implementations agreed on the same lock facts:

- root type is `object`;
- arrays preserve semantic order rather than being sorted;
- compact separators are canonical;
- recursive Unicode code-point key order holds;
- self bytes and self SHA-256 are correctly `null`;
- future review bytes/LF/SHA-256 are correctly `null`; and
- the lock bytes are exactly the canonical bytes they claim to be.

## 6. Governance audit and correction of the initial zero-write interpretation

### 6.1 Historical snapshots versus live governance

The lock binds historical authoring snapshots:

- `BATCH_06_STATUS.md` snapshot:
  `119001` bytes / `1742` LF /
  `f1ef5255b562e4fa02ce11c8342ff6c40ff0113ad1b07e6f5ea692512867d95a`
- `BATCH_06_IDEA_REPORT.md` snapshot:
  `203867` bytes / `4007` LF /
  `d2e89058d5c6157cc5f95a937061b186d20778dc2f52330215a5f92c66b898ce`

The lock also states that these are historical authoring-context snapshots,
not a claim that mutable governance roots must retain those hashes forever.

### 6.2 Live `BATCH_06_IDEA_REPORT.md`

The live Idea Report remains append-only in the way the governance rules
require. I verified directly that the first `203867` bytes of the live file
hash exactly to the bound snapshot digest
`d2e89058d5c6157cc5f95a937061b186d20778dc2f52330215a5f92c66b898ce`.

So the live Idea Report is the historical source-lock-author snapshot plus an
authorized appended addendum describing the source-lock author stop and review
gate.

### 6.3 Live `BATCH_06_STATUS.md`

My initial blocker came from a whole-file-prefix test on the live Status file.
That test was too strict under the Status file’s own governance section. The
controlling text in lines 173–175 is explicit:

- the Status file is the controlled lifecycle dashboard;
- its Material Passport, current queue state, and current permissions may
  change at a validated transition; and
- only the Activity Log is append-only.

I therefore re-audited the live Status file under the correct contract.

The live controlled fields show one unique Paper-24 transition state:

- line 13:
  `- Current gate: `PAPER24_SOURCE_LOCK_REVIEW``
- line 32:
  the unique Paper-24 queue row whose stage prose is
  “strict-canonical source lock authored and parent-validated; only fresh
  independent source-lock review is open” and whose state code is
  `SOURCE_LOCK_AUTHOR_STOP_REVIEW_OPEN`

I verified that the live current-gate string occurs exactly once and the live
Paper-24 queue row occurs exactly once.

I then verified that the Status Activity Log has a unique EOF suffix at lines
1743–1763: a 21-line appended source-lock-author-stop entry beginning

`- 2026-08-25: A Paper-24 source-lock author distinct from the ten-file author`

and ending with

`Paper planning and every later or external effect remain closed.`

That suffix is:

- 21 LF lines;
- 1,508 bytes; and
- located exactly at EOF.

### 6.4 Authorized live governance conclusion

Under the combined controlling contracts, the live governance state is
authorized:

1. the append-only Idea Report preserved its historical authoring snapshot as a
   true prefix and then appended the source-lock author-stop addendum;
2. the Status file changed only in fields that its own lines 173–175 allow to
   change at a validated transition:
   - current gate,
   - current queue row, and
   - appended Activity Log entry; and
3. all bound Paper 24 project bytes, candidate bytes, and lock bytes remained
   unchanged.

So the earlier whole-file-prefix blocker was an overread of the Status
contract, not a genuine governance contradiction.

## 7. Self-null exclusion, future-review nulls, and rejected unbound value

I rechecked the lock’s self-reference safeguards:

- `self_identity_exclusion.bytes` is `null`;
- `self_identity_exclusion.sha256` is `null`;
- future review bytes are `null`;
- future review LF is `null`; and
- future review SHA-256 is `null`.

Those nulls are correct and required.

I also verified that the rejected unbound value
`f19ac071e017b252a7ff6d96e627a16607373cafc2e5f8c2f26dbb3842321b91`
appears only in the dedicated rejected-error object with

- `accepted=false`;
- `nonbinding=true`; and
- an explicit prohibition on use as an accepted identity.

I found no bound governance, source-design, or candidate byte that ever made
that value controlling.

## 8. Independent theorem and proof replay

I independently rederived the theorem-critical mathematics rather than copying
conclusions forward.

### 8.1 Literal gradients, inverses, and symplecticity

For
\[
V_m=Aq_1^m q_2^2+Bq_1q_2^{2m},
\qquad
W_{m,s}=Cp_1^{s(2m+1)+1}+Dp_2^{sm+1},
\]
I rederived the literal gradients:
\[
\partial_{q_1}V_m=mAq_1^{m-1}q_2^2+Bq_2^{2m},
\qquad
\partial_{q_2}V_m=2Aq_1^m q_2+2mBq_1q_2^{2m-1},
\]
\[
\partial_{p_1}W_{m,s}=(s(2m+1)+1)Cp_1^{s(2m+1)},
\qquad
\partial_{p_2}W_{m,s}=(sm+1)Dp_2^{sm}.
\]

I rechecked the subtraction inverses and the symmetric-Hessian block argument:
\[
J_S=
\begin{pmatrix}I_2&0\\H_V&I_2\end{pmatrix},
\qquad
J_T=
\begin{pmatrix}I_2&H_W\\0&I_2\end{pmatrix},
\]
with symmetric Hessians \(H_V,H_W\), and verified
\[
J_S^{\mathsf T}\Omega J_S=\Omega,
\qquad
J_T^{\mathsf T}\Omega J_T=\Omega.
\]
So \(S\), \(T\), and \(F_{m,s}=T\circ S\) are exact polynomial
symplectomorphisms in the standard form.

### 8.2 Common wall, branch matrices, and strict exchange

I rederived the two synchronous selector differences:
\[
(m-1)u_1+2u_2-2mu_2=(m-1)(u_1-2u_2),
\]
\[
mu_1+u_2-\bigl(u_1+(2m-1)u_2\bigr)=(m-1)(u_1-2u_2).
\]

Therefore the common wall is exactly \(r=u_1/u_2=2\), with branch matrices
\[
A_-=\begin{pmatrix}0&2m\\1&2m-1\end{pmatrix},
\qquad
A_+=\begin{pmatrix}m-1&2\\m&1\end{pmatrix},
\qquad
B_m=\operatorname{diag}(2m+1,m).
\]

I rechecked the complete-step matrices
\[
C_-=sB_mA_-,
\qquad
C_+=sB_mA_+,
\]
and the exact branch maps
\[
h_m(r)=\frac{2(2m+1)}{r+2m-1},
\qquad
\ell_m(r)=\frac{(2m+1)((m-1)r+2)}{m(mr+1)}.
\]

I reverified all three corrected difference identities:
\[
h_m(r)-2=\frac{2(2-r)}{r+2m-1},
\]
\[
\ell_m(r)-1=\frac{(m^2-m-1)r+3m+2}{m(mr+1)},
\]
\[
2-\ell_m(r)=\frac{(m+1)(r-2)}{m(mr+1)}.
\]

Hence:

- \(0<r<2 \implies h_m(r)>2\);
- \(r>2 \implies 1<\ell_m(r)<2\);
- the ordinary seed \(u_0=(1,1)^{\mathsf T}\) follows the strict itinerary
  \(A_-,A_+,A_-,A_+,\ldots\); and
- the wall \(r=2\) is a true tie boundary and is excluded.

### 8.3 Actual carry, top-form survival, and visibility

I independently checked both temporal carry phases:

- base carry at the seed;
- later first-phase carry in both chambers; and
- later second-phase carry in both chambers, already at \(s=1\).

I rechecked the no-cancellation/domain argument for arbitrary nonzero
\(A,B,C,D\): selected top homogeneous parts remain nonzero in a domain, so
the theorem is not a positivity-only statement.

For visibility, I rechecked that \(q_1\) strictly dominates \(q_2\) and both
momentum coordinates for every positive iterate. In the negative chamber I
reused the corrected equality
\[
u_{n+1,1}=sm\,h_m(r_n)\,v_{n+1,2},
\]
which implies \(u_{n+1,1}>v_{n+1,2}\) because \(h_m(r_n)>2\), \(m\ge2\),
and \(s\ge1\). In the positive chamber I rechecked
\[
u_{n+1,1}-v_{n+1,2}
=s(2m+1)\bigl((m-1)u_{n,1}+2u_{n,2}\bigr)-(mu_{n,1}+u_{n,2})>0.
\]

So
\[
d_n=\deg(F_{m,s}^n)=u_{n,1}\quad(n\ge1),
\]
with \(d_0=1\) as the tied seed.

### 8.4 Monodromy, determinant expansion, spectrum, recurrence, and wall gaps

I rederived
\[
P=(B_mA_+)(B_mA_-)
=
\begin{pmatrix}
2m(2m+1)&2m(2m+1)(2m^2+m-2)\\
m^2&m^2(4m^2+4m-1)
\end{pmatrix}.
\]

I rechecked both eigenpairs:

- \(H=m^2(2m+1)^2\) with right eigenvector \((2,1)^{\mathsf T}\);
- \(L=2m(m+1)\) with right eigenvector
  \((-(2m+1)(2m^2+m-2),\,m)^{\mathsf T}\).

I rechecked the trace:
\[
\operatorname{tr}(P)=4m^4+4m^3+3m^2+2m=H+L.
\]

I also explicitly checked the displayed determinant expansion rather than
accepting the identity as a bare equality:
\[
2m(2m+1)\cdot m^2(4m^2+4m-1)
-2m(2m+1)(2m^2+m-2)\cdot m^2
=2m^3(m+1)(2m+1)^2.
\]
Since \(H\,L=2m^3(m+1)(2m+1)^2\), this gives
\[
\det(P)=H\,L.
\]

Therefore the actual two-step monodromy \(C_+C_-=s^2P\) has eigenvalues
\(s^2H\) and \(s^2L\), and
\[
\lambda_1(F_{m,s})=\sqrt{\rho(s^2P)}=sm(2m+1).
\]

I rechecked the parity-vector laws
\[
u_{2j}=(s^2P)^j(1,1)^{\mathsf T},
\qquad
u_{2j+1}=sB_mA_-(s^2P)^j(1,1)^{\mathsf T},
\]
and the stride-two recurrence
\[
d_{n+4}=s^2(H+L)d_{n+2}-s^4HL\,d_n.
\]

The initial values I rederived are
\[
d_0=1,
\quad
d_1=2m(2m+1)s,
\]
\[
d_2=2m(m+1)(2m-1)(2m+1)s^2,
\]
\[
d_3=8m^4(m+1)(2m+1)s^3.
\]

I also rechecked the corrected third vector:
\[
u_3=
\begin{pmatrix}
8m^4(m+1)(2m+1)s^3\\
2m^2(m+1)(2m-1)(2m^2+2m+1)s^3
\end{pmatrix}.
\]

For wall gaps, with \(\ell=(1,-2)\), I reverified
\[
\ell C_-=-2ms\,\ell,
\qquad
\ell C_+=-(m+1)s\,\ell,
\qquad
\ell P=L\,\ell.
\]
Hence
\[
u_{2j,1}-2u_{2j,2}=-(s^2L)^j,
\qquad
u_{2j+1,1}-2u_{2j+1,2}=2ms(s^2L)^j.
\]

### 8.5 Parity closed forms, integrality, structural lemma, and conditional lemma

I rechecked the even-vector spectral decomposition, the odd visible closed
form, and the matrix-based integrality logic. The correct integrality argument
comes from integer matrices and integer initial data, not from handwaving about
closed-form denominators.

I independently rederived the bounded crossed-binomial lemma:

- synchronous switching wall \(R=(d-b)/(a-c)\);
- wall level \(L_{\mathrm{wall}}=aR+b=cR+d\);
- branch derivative
  \[
  g'_{x,y}(r)=-\frac ef\frac{x+y-1}{(xr+y-1)^2}<0;
  \]
- wall-fixing iff ratio
  \[
  \frac ef=\frac{R(L_{\mathrm{wall}}-1)}{L_{\mathrm{wall}}-R}.
  \]

For the explicit family I rechecked the realization
\[
R=2,
\qquad
L_{\mathrm{wall}}=2m+2,
\qquad
(e,f)=s(2m+1,m).
\]

I also rechecked that the conditional period-\(k\) selector-to-monodromy
lemma is valid only under all six hypotheses named in the proof package:

1. strict selected-face gaps;
2. strict carry over carried coordinates;
3. nonzero selected top homogeneous parts in a domain;
4. linear induced degree maps;
5. a coordinate or linear functional that sees the true total degree; and
6. visibility of the Perron class to that coordinate or functional.

Its status remained technical and nonheadline, exactly as the lock requires.

## 9. Citation, collision, anti-claim, zero-science, and permission replay

### 9.1 Citation boundary

I rechecked the bounded source ledger and access limitations:

- exactly S01–S09 are bound;
- source-design author network calls: `0`;
- source-lock author network calls: `0`;
- the bounded search cutoff is `2026-08-25` UTC;
- no citation transfers proof of theorem-critical local identities; and
- no absolute priority or exhaustive noncollision claim is authorized.

The role grouping remained correct:

- S01, S02, S08 for general degree-growth/spectral context;
- S03, S04, S05 for the closest public symplectic/tropical switching
  neighbors;
- S06 for polynomial symplectomorphism class background; and
- S07, S09 for weak-Perron/affine-triangular proximity.

### 9.2 Internal and external collision boundary

I rechecked the P20–P23 boundary:

- P20 is the direct owned predecessor but stationary, not a strict
  period-two chamber-exchange result;
- P21 has a stationary selector and cubic recurrence, not a wall-exchange
  cocycle;
- P22 is the opposite mechanism, a cubic collapse story rather than a
  fixed two-mode wall exchange; and
- P23 has a different support profile and no period-two wall exchange.

The accepted Paper-24 delta remained the same conjunction:

1. rigid crossed-binomial wall fixing;
2. strict period-two selector exchange of the ordinary orbit;
3. true polynomial carry plus arbitrary-nonzero-coefficient top-form
   survival; and
4. exact two-step monodromy with recurrence, wall gaps, parity laws, and
   dynamical degree.

### 9.3 Anti-claims, STOP rules, and zero-science

I rechecked the anti-claim lock and found no forbidden drift. In particular,
the frozen package still forbids claims about:

- the wall \(r=2\) itself as part of the strict orbit;
- classification beyond the crossed-binomial / diagonal-pure-power ansatz;
- arbitrary period words or period \(>2\);
- positive characteristic validity;
- inverse-degree/entropy-equality/integrability/genericity/nonconjugacy
  theorems;
- novelty of the abstract conditional period-\(k\) lemma in isolation;
- absolute firstness or priority claims;
- hidden computation, scans, data, or code proof; and
- any external effect.

I also rechecked the scientific execution contract. The bound counts remain
zero for:

- code files;
- experiments;
- datasets;
- figures;
- tables;
- GPU runs;
- numerical runs;
- finite iterate searches;
- scans; and
- network calls for theorem evidence.

### 9.4 Permission boundary

The live permission state remained exactly consistent with a fresh independent
source-lock review:

- authorized write count max: `1`;
- authorized write path:
  `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md`;
- source-lock review authorized: `true`;
- source-lock modification authorized: `false`;
- source-design modification authorized: `false`;
- code/data/experiment/manuscript/build/release/publication/transport/upload
  all unauthorized; and
- any blocker would require zero writes.

## 10. Remaining issues and nonblocking notes

I found no conjunctive blocker after the governance reinterpretation.

Two downstream presentation items remain nonblocking exactly as already frozen:

1. any public proof should display either the explicit one-line determinant
   expansion or a determinant-multiplicativity derivation before concluding
   \(\det(P)=HL\); and
2. later public-facing governance may restate the ten-row identity table for
   readability, although the lock already satisfies the stronger identity
   requirement through `author_file_allowlist`.

Neither item affects theorem validity, canonicality, permissions, or lock
passing status.

## 11. Scores

Inherited candidate scores remained unchanged:

| Record | Scores |
|---|---|
| R1 | novelty `7.9/10`; standalone `8.0/10`; proof plausibility `9.4/10` |
| R2 | proof confidence `9.3/10`; standalone value `7.8/10` |

This independent source-lock review’s own confidence scores are:

| Dimension | Score |
|---|---:|
| identity/inventory audit confidence | 10.0 / 10 |
| canonical JSON audit confidence | 10.0 / 10 |
| governance interpretation confidence | 9.7 / 10 |
| theorem/proof replay confidence | 9.7 / 10 |
| citation/collision/permission replay confidence | 9.8 / 10 |

## 12. Final disposition

All conjunctive checks now pass:

- exact source and candidate identities pass;
- exact inventories and forbidden absences pass;
- strict canonical JSON and dual independent round-trip tests pass;
- self-null exclusion and future-review nulls pass;
- scientific proof replay passes;
- citation, collision, anti-claim, zero-science, and permission replay pass;
- live governance is an authorized lifecycle consumption under the combined
  Status and Idea Report contracts; and
- no blocker requiring zero-write remains.

This file is therefore the sole authorized review artifact for the current
lock gate.

SOURCE_LOCK_PASS
