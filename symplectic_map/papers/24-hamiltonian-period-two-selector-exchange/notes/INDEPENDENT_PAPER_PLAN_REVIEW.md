# Independent Paper-Plan Review — Paper 24

## 1. Reviewer scope, independence, and opening state

I am a fresh independent Paper 24 paper-plan reviewer. I authored none of the
plan, the source lock, the source-lock review, the source-design files, the
source-design review, or the four candidate-review / correction records. I
read the full Paper 24 paper-plan skill, then applied the explicit governance
overrides for this project: proof-first mathematical dynamics article, no
selected venue, exact `26.0` content pages inside the locked `22--30` band,
and no default `8`/`9`-page conference leakage.

I performed no web lookup, no network action, no build, no code execution for
scientific evidence, no access to the excluded Paper 23 temporary roots named
in the review instruction, and no write before all conjunctive checks were
complete.

Opening project state was exactly:

| Item | Live fact |
|---|---|
| project path | `papers/24-hamiltonian-period-two-selector-exchange` |
| regular files | `14` |
| child directories | `4` (`experiments`, `notes`, `paper`, `refine-logs`) |
| symlinks | `0` |
| other objects | `0` |
| review artifact present at open | `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` absent |

I also rechecked UTF-8 / LF hygiene at open: every live project file was valid
UTF-8, LF-only, terminal-LF-terminated, BOM-free, CR-free, NUL-free, and free
of stray control corruption.

## 2. Exact live identities bound at review time

### 2.1 Paper-plan artifact

The plan under review is the ordinary mode-`0644` non-symlink file
`paper/PAPER_PLAN.md` with:

| bytes | LF | SHA-256 | terminal line |
|---:|---:|---|---|
| 36,690 | 586 | `ee5c320f800919543411b147b5d1484d33c577a56519121b9b4883fdff8122ad` | `PAPER PLAN AUTHOR STOP` |

This exactly matches the opening identity required by the review instruction.

### 2.2 Prior bound Paper 24 artifacts

I independently rederived the live identities of the bound predecessor
artifacts and found them stable:

| Artifact | bytes | LF | SHA-256 | terminal line / status |
|---|---:|---:|---|---|
| `experiments/source_lock.json` | 45,607 | 1 | `45ce6527917d7172ff10e87db1e716b6e7caa2de3fa3cfbd54cd73b034003232` | one compact JSON object |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | 16,630 | 490 | `1c733058483cb28370e4c6f283126c14305ce45de43010e7753a4d92a5f8ece8` | `SOURCE_DESIGN_PASS` |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | 24,533 | 754 | `a420a26fbf3a535aedafdfd701969db8084b932e2ae9e6d806570c460090abea` | `SOURCE_LOCK_PASS` |

The ten source-design files named in `author_file_allowlist` all matched their
locked byte counts, LF counts, hashes, UTF-8/LF hygiene facts, and mode
`0644` exactly:

| Source-design file | bytes | LF | SHA-256 |
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

### 2.3 Candidate and live governance identities

I rechecked the four immutable candidate provenance records:

| Record | bytes | LF | SHA-256 | terminal line |
|---|---:|---:|---|---|
| `BATCH_06_PAPER24_CANDIDATE_REVIEW_R1.md` | 30,703 | 878 | `b2802f24ca5de3d91b7ea5a1726a0cf12d6f36053055e24e3759124bfc8709c1` | `PAPER24_CANDIDATE_GATE_PASS_R1` |
| `BATCH_06_PAPER24_CANDIDATE_REVIEW_R1_CORRECTION.md` | 2,583 | 112 | `dabf9fa2873aa0124e2d510dc20b581b51a5648e0828f33bc2b7a41b2172730d` | `PAPER24_CANDIDATE_GATE_PASS_R1_CORRECTED` |
| `BATCH_06_PAPER24_CANDIDATE_REVIEW_R2.md` | 19,672 | 769 | `914b92255cd9aae2b8be4707484ebf63a72d1b40e1cf1fc356dd365676ed25bd` | `PAPER24_CANDIDATE_GATE_PASS_R2` |
| `BATCH_06_PAPER24_CANDIDATE_REVIEW_R2_CORRECTION.md` | 2,500 | 115 | `1c311a979b3c8fc396734bbd851f1a6c8ed5738a2f3005048688f623a6bcaf6b` | `PAPER24_CANDIDATE_GATE_PASS_R2_CORRECTED` |

The live root-governance records were:

| Live governance file | bytes | LF | SHA-256 |
|---|---:|---:|---|
| `BATCH_06_STATUS.md` | 123,648 | 1,807 | `2d94b69e0aeb4d05167d6d2eef378b54fb1e89ef3aa9c8da6567b7913463984f` |
| `BATCH_06_IDEA_REPORT.md` | 214,499 | 4,205 | `01d819accf58c383cbdf8c59a5461e15d5acd7b682caab912f7959303016dbc7` |

I read both through EOF. Their live addenda authorize the exact current gate:
the validated source-lock review opened exactly one proof-first author for
`paper/PAPER_PLAN.md`, and the resulting plan author-stop addendum opens only
this fresh independent review path with zero writes on a blocker and only a
later separate eligibility (not direct authority) for
`notes/PUBLICATION_STAGE_SCOPE.md`.

## 3. Plan-header and architecture audit

The plan passes the header-level governance checks exactly:

| Check | Result | Evidence |
|---|---|---|
| exact title retained | pass | `Forced Period-Two Selector Exchange in Two-Mode Hamiltonian Product Shears` appears literally in the title field |
| anonymous placeholder | pass | author field is exactly `Anonymous` |
| no selected venue | pass | venue line states no submission venue is selected |
| no default conference leakage | pass | no ICLR / NeurIPS / ICML selection, no default `8`/`9`-page venue budgeting, no venue-template structure |
| proof-first article type | pass | plan states proof-first mathematical dynamics article |
| main-body proofs only | pass | plan states all theorem-critical proofs remain in the main body and no proof appendix is planned |
| section architecture | pass | one abstract plus exactly eight numbered sections |
| page-band compliance | pass | exact `26.0` content pages inside the locked `22--30` band |

The page arithmetic is exact and explicit:

| Component | Pages |
|---|---:|
| Abstract | 0.5 |
| §1 | 3.0 |
| §2 | 3.0 |
| §3 | 3.5 |
| §4 | 4.0 |
| §5 | 3.5 |
| §6 | 4.0 |
| §7 | 2.5 |
| §8 | 2.0 |
| **Total** | **26.0** |

References are excluded from that total, and the plan does not move any
theorem-critical proof to an appendix.

## 4. Claims–evidence and logical-flow audit

The plan contains a full claims–evidence matrix divided into headline,
supporting, and boundary/failure claims. Every public claim is mapped to:

1. a named section location;
2. a local proposition / lemma / corollary;
3. specific equation ranges; and
4. an explicit scope limiter.

This is consistent with the locked `notes/CLAIMS_EVIDENCE_MATRIX.md` and with
the proof order frozen in `notes/PROOF_PACKAGE.md`.

The logical dependency order is also correct and proof-first:

1. gradients, subtraction inverses, and symplecticity;
2. selector rows, common wall, and exact matrices;
3. corrected branch algebra and strict chamber exchange;
4. both temporal carry phases;
5. arbitrary-nonzero top-form survival in a polynomial domain;
6. visible-coordinate certification of true total degree;
7. exact monodromy, both eigenpairs, trace, determinant derivation, and
   dynamical degree;
8. recurrence, initials, corrected `u_3`, wall gaps, parity laws, and
   integrality;
9. bounded structural iff lemma plus explicit family realization; and
10. the six-hypothesis conditional period-`k` lemma as technical support only.

That order respects the locked dependency firewall:

- selector exchange alone does not certify actual polynomial degrees;
- carry and visibility are separate indispensable obligations;
- the structural lemma does not substitute for carry or visibility; and
- the conditional period-`k` lemma remains downstream technique, not the
  novelty headline.

## 5. Mathematical fidelity audit against the lock and proof source

I independently compared the plan against the exact source lock and the proof
package. The plan preserves every theorem-critical frozen item I was required
to check.

### 5.1 Family, phase, symplecticity, and selector data

The plan keeps literal agreement on:

- characteristic-zero field \(K\);
- integers \(m\ge2\), \(s\ge1\);
- arbitrary nonzero coefficients \(A,B,C,D\in K^\times\);
- potentials
  \[
  V_m(q)=Aq_1^m q_2^2+Bq_1q_2^{2m},
  \qquad
  W_{m,s}(p)=Cp_1^{s(2m+1)+1}+Dp_2^{sm+1};
  \]
- phase order
  \[
  S(q,p)=(q,p+\nabla V_m(q)),
  \quad
  T(q,p)=(q+\nabla W_{m,s}(p),p),
  \quad
  F_{m,s}=T\circ S;
  \]
- standard symplectic form and Hessian-block verification;
- common wall \(r=2\);
- exact matrices \(A_-\), \(A_+\), \(B_m\), \(C_-\), and \(C_+\); and
- strict wall exclusion from every theorem statement.

### 5.2 Corrected branch algebra and correction precedence

The plan correctly freezes all four accepted corrections:

1. corrected
   \[
   \ell_m(r)-1=\frac{(m^2-m-1)r+3m+2}{m(mr+1)};
   \]
2. corrected negative-chamber visibility equality
   \[
   u_{n+1,1}=sm\,h_m(r_n)\,v_{n+1,2}
   \]
   before the strict inequality consequence;
3. corrected
   \[
   2-\ell_m(r)=\frac{(m+1)(r-2)}{m(mr+1)};
   \]
4. corrected second coordinate of
   \[
   u_3=
   \begin{pmatrix}
   8m^4(m+1)(2m+1)s^3\\
   2m^2(m+1)(2m-1)(2m^2+2m+1)s^3
   \end{pmatrix}.
   \]

It also preserves the strict itinerary
\(A_-,A_+,A_-,A_+,\dots\), the chamber images
\(0<r<2\Rightarrow h_m(r)>2\) and \(r>2\Rightarrow1<\ell_m(r)<2\), and the
rule that the wall is a genuine tie boundary rather than a theorem point.

### 5.3 Carry, no-cancellation, visibility, monodromy, and spectra

The plan explicitly assigns proof locations for:

- base carry;
- later first-phase carry in both chambers;
- later second-phase carry in both chambers;
- arbitrary-nonzero top homogeneous survival in a domain;
- \(q_1\) visibility against \(q_2\), \(p_1\), and \(p_2\) for every
  positive iterate, with \(d_0=1\) kept as the tied seed;
- the exact product
  \[
  P=(B_mA_+)(B_mA_-);
  \]
- both right eigenpairs, not just the Perron one;
- the trace identity;
- the required explicit \(ad-bc\) determinant expansion before concluding
  \(\det(P)=HL\);
- \(H=m^2(2m+1)^2\), \(L=2m(m+1)\), and
  \(\lambda_1(F_{m,s})=sm(2m+1)\).

The determinant presentation is stronger than the proof-package shorthand and
conforms to the source-lock tightening.

### 5.4 Recurrence, wall gaps, parity laws, and integrality

The plan keeps the exact parity-vector and scalar-law chain:

- \(u_{2j}=(s^2P)^j(1,1)^{\mathsf T}\);
- \(u_{2j+1}=sB_mA_-(s^2P)^j(1,1)^{\mathsf T}\);
- recurrence
  \[
  d_{n+4}=s^2(H+L)d_{n+2}-s^4HLd_n;
  \]
- initials \(d_0,d_1,d_2,d_3\);
- corrected full \(u_3\);
- both wall-gap identities;
- full even-vector decomposition;
- both parity closed forms; and
- integrality from integer matrices / recurrence rather than denominator
  folklore.

### 5.5 Structural lemma and conditional period-\(k\) lemma

The plan correctly keeps:

- the bounded crossed-binomial / diagonal-pure-power iff lemma;
- the exact ratio
  \[
  \frac ef=\frac{R(L_{\mathrm{wall}}-1)}{L_{\mathrm{wall}}-R};
  \]
- the explicit Paper-24 specialization
  \(R=2\), \(L_{\mathrm{wall}}=2m+2\), \((e,f)=s(2m+1,m)\);
- the explicit warning that \(R=1\) places the ordinary seed on the wall; and
- the conditional period-`k` statement only with all six hypotheses:
  strict selected-face gaps, strict carry, nonzero top homogeneous parts in a
  domain, linear degree maps, visibility of true total degree, and visibility
  of the Perron class.

The plan does not promote the conditional period-`k` lemma to the headline.

## 6. Decision on the equation-(6.10)–(6.12) freezing question

I independently assessed whether the plan’s handling of equations `(6.10)`–
`(6.12)` is sufficient even though it does not reprint the long rational
expressions in full.

My decision: this is sufficient at the planning stage and is not a blocker.

Reason:

1. the exact formulas themselves are already frozen upstream in the bound proof
   source `notes/PROOF_PACKAGE.md`, including the even visible closed form,
   the full even-vector decomposition, and the odd visible closed form;
2. the plan assigns those exact formulas to unique equation numbers,
   proposition ownership, section mass, and dependency context, so there is no
   competing formula slot left open;
3. the plan separately freezes the surrounding non-negotiables that control
   those formulas—\(P\), both eigenpairs, \(H\), \(L\), recurrence, initials,
   corrected `u_3`, wall gaps, and matrix-based integrality; and
4. the plan is a structure-and-proof-allocation document, not the theorem text
   itself.

Had the proof source been absent, or had the plan left multiple candidate
closed forms or omitted the even-vector decomposition anchor, I would have
classified the omission as an ambiguity blocker. Under the actual lock, it is
adequately frozen.

## 7. Page mass, table plan, and no-figure audit

The plan preserves standalone mass and article architecture:

- exact total content mass is `26.0` pages, comfortably inside the `22--30`
  lock and centered in the preferred `24--28` band;
- the introduction contains the theorem preview, bounded positioning, and
  limitations firewall;
- the conclusion section explicitly collects assumption failures and
  anti-claims; and
- all theorem-critical work is planned in the main body, not deferred.

The mathematical table plan is exact:

| Table status | Result |
|---|---|
| mandatory hand-typeset tables | exactly `3` |
| optional contextual comparison table | exactly `1` |
| empirical tables | `0` |
| figures / plots / diagrams | `0` |

The three mandatory tables are theorem-facing ledgers rather than empirical
objects, and the optional fourth table is bounded comparison only.

On the “hero figure” issue, the plan contains a single explanatory sentence
stating that no hero figure is planned. I do not classify that sentence as a
gate-breaking artifact because it creates no figure plan, no figure
dependency, no figure permission, and no new public claim. The controlling
visual policy remains zero figures. I record it only as a stylistic note.

## 8. Citation, boundary, anti-claim, and firewall audit

The citation and comparison surface is correctly bounded.

### 8.1 S01–S09 closure

The plan uses exactly the nine locked source identifiers `S01` through `S09`.
I found no `S10`, no new metadata source, no new bibliography artifact, no
BibTeX generation, no citation-key fabrication, no proof transfer from
citations, and no priority transfer. The allowed roles match the locked
citation ledger:

- S01, S02, S08 for general degree-growth / spectral context;
- S03, S04, S05 for closest public symplectic / tropical switching neighbors;
- S06 for polynomial symplectomorphism class background; and
- S07, S09 for weak-Perron / affine-triangular positioning.

### 8.2 Papers 20–23 boundary

The plan preserves the exact internal-boundary story:

- Paper 20: stationary two-mode predecessor grammar, not strict wall exchange;
- Paper 21: stationary selector and cubic visible-matrix story, not this
  period-two wall-crossing cocycle;
- Paper 22: arbitrary-mode cubic-collapse mechanism, not fixed two-mode wall
  exchange;
- Paper 23: four-mode quartic escape with a different support profile and no
  period-two wall exchange.

The plan also preserves the standalone-safe sentence that the contribution is
not merely “another small matrix example,” but the explicit conjunction of the
full \(m\)-family, forced wall fixing, true carry / no-cancellation /
visibility, and exact parity laws.

### 8.3 Anti-claims, failure cases, STOP rules, and zero-science status

The anti-claim firewall is intact. The plan continues to forbid claims about:

- the wall \(r=2\) itself as theorem territory;
- classification beyond the bounded ansatz;
- maximal or necessary selector fans;
- arbitrary periods, automata, or generalized shear words;
- positive characteristic;
- inverse-degree / entropy-equality / integrability / genericity /
  periodic-point / nonconjugacy theorems;
- novelty of the abstract conditional period-`k` principle by itself;
- firstness or absolute priority claims; and
- added supports, vanishing coefficients, reversed phase order, hidden
  computation, code, or data proof.

The failure examples remain explicit:

- \(r=2\);
- \(m=1\);
- one coefficient equal to zero;
- positive characteristic;
- omitted carry proof;
- omitted visibility proof; and
- \(R=1\) in the structural lemma.

The STOP rules remain explicit and correct, including drift in any corrected
branch identity, spectrum, recurrence, initial value, wall gap, parity
formula, or determinant presentation, as well as any forbidden artifact or
page-band failure.

Zero-science and zero-code status also remains explicit: no code, data,
datasets, plots, scans, numerical spectra, CAS certificates, notebooks, or
experiments support any theorem claim.

### 8.4 Public-governance firewall and permission tail

The plan’s public/governance firewall passes exactly:

- hashes, byte counts, LF counts, internal paths, lifecycle tokens, reviewer
  identities, and repair history are excluded from the eventual public paper;
- publication governance, source trio, manuscript / TeX / BibTeX, figures,
  code, data, experiments, build, PDF, release, submission, upload, hosting,
  repository push, transport, messaging, identity disclosure, Paper 25 work,
  and every external effect remain unauthorized at this stage;
- the sole next conditional path is this review artifact; and
- a successful review makes only `notes/PUBLICATION_STAGE_SCOPE.md` eligible
  for a later separate parent transition, without directly authorizing it.

## 9. Nonblocking notes

I found no conjunctive blocker.

Two items are worth recording as nonblocking:

1. the single “no hero figure is planned” sentence is stylistic and could be
   omitted later for terseness, but it does not create a figure plan or a
   permission leak; and
2. the plan freezes `(6.10)`–`(6.12)` by exact role, numbering, proposition,
   and proof-source binding rather than by reprinting the long formulas; under
   the actual source lock this is sufficient, but any later public-facing
   governance stage that restates those formulas should copy them verbatim from
   the proof package rather than paraphrasing them.

## 10. Scores

Independent paper-plan review scores:

| Dimension | Score |
|---|---:|
| identity / inventory confidence | 10.0 / 10 |
| theorem-fidelity confidence | 9.8 / 10 |
| claims–evidence / logical-flow confidence | 9.8 / 10 |
| page-budget / table-plan confidence | 9.9 / 10 |
| citation / boundary / permission confidence | 9.9 / 10 |

## 11. Final disposition

All conjunctive plan gates pass:

- opening identity and inventory pass;
- source-lock, source-lock-review, source-design-review, candidate, and live
  governance identities pass;
- title, anonymity, venue-free state, and exact `26.0`-page arithmetic pass;
- claims–evidence mapping and logical proof order pass;
- theorem-critical fidelity to the source lock and proof package passes,
  including the four correction precedences, both carry phases, visibility,
  both eigenpairs, explicit determinant derivation, recurrence, corrected
  `u_3`, wall gaps, parity laws, structural iff lemma, and six-hypothesis
  conditional period-`k` lemma;
- the three-mandatory-plus-one-optional nonempirical table plan passes;
- S01–S09 closure, Papers 20–23 boundary, anti-claims, failure cases, STOP
  rules, zero-science contract, and public-governance firewall pass; and
- the permission tail is exact: this review artifact is the sole conditional
  write, and only later separate eligibility (not direct authority) is
  created for `notes/PUBLICATION_STAGE_SCOPE.md`.

This file is therefore the sole authorized review artifact for the current
paper-plan gate.

PAPER_PLAN_PASS
