# P69 Stage 2.5 integrity and priority audit

Audit date: 2026-08-26 (UTC)  
Manuscript: *Orientation-Sensitive Surface-Flat Shifts and Finite-Group Character Data*  
Audit posture: author-side integrity audit, not independent specialist review  
External state: **HOLD**

## 1. Executive verdict

**Overall verdict: PASS_WITH_NOTES.**

The stated flat-connection SFT, cover topology, rooted gauge count, two fixed-point
laws, finite-moment reconstruction, and the `D8`/`Q8`/`C3` examples are internally
coherent.  Exact finite controls replay byte-for-byte and agree with the manuscript's
displayed values.  All three stored bibliography records are authentic and their
metadata are verified; all five citation contexts are substantively faithful; there
are no ghost or dangling citations.  The paragraph-overlap screen covers 30.99% of
narrative units and every major section.  The semantic claim registry below audits all
26 identified claims, including all high-impact claims.

The notes are material to release posture but do not change the core theorem:

1. the Klug pinpoint should read “Theorem 3.1,” not “Theorem 3”;
2. the owner-subtraction discussion should add Snyder's lattice-TQFT proof and should
   cite representation-zeta literature for the already-standard inverse-degree sums;
3. the exact combined construction was not found only within the bounded searches
   recorded in `SOURCE_SEARCH_LEDGER.md`; collision risk is **MEDIUM**, and this audit
   is not a global priority certificate;
4. author identities/contributions, funding, competing interests, and human approval
   of the AI-use disclosure remain unresolved.

Accordingly, the mathematics receives **PASS within this author self-audit**, source
and priority framing receive **PASS_WITH_NOTES**, and external release remains
**HOLD pending objective corrections and specialist review**.

## 2. Audit scope, immutability, and protocol coverage

No manuscript, bibliography, or PDF source was edited in this audit.  The audit was
restricted to `stage2_5/`.  Baseline fingerprints were:

| File | SHA-256 |
|---|---|
| `main.tex` | `5a594b3109734abe2947539ebd8efd02c828ea06147e31fb8cd7222fff5e1e6c` |
| `references.bib` | `242f9c9dc4c565b82509426d2ce8f22d9dc9af514972f0850aa8ddbacfc06f22` |
| `sections/0_abstract.tex` | `ea3f0881c5ce96baeb1d0c2c27b355e19fe79d44b197b19d2f6b83eab618a45f` |
| `sections/1_introduction.tex` | `3da03f879fa0633c3073338d66bc3e9da0a1a031d018f071ecb77a423cd7f19b` |
| `sections/2_background.tex` | `1f6d305aa02a689e3859c85c8d31e1fd49f96e4ce9f951cf094e3d3f76b63317` |
| `sections/3_flat_shift.tex` | `cd51deda0e212524242d07cc140787c345e3d72f38b6ac25830a4df8595acca3` |
| `sections/4_subgroup_counts.tex` | `7ad02972e29dccf3787f9f59f645cfbd1eb34c4855b8bb21f7641d8cf449545d` |
| `sections/5_moment_recovery.tex` | `57a03e6e89e3c1b630f2361051eb9d794098a4a8cc1e11b1eca4d08f80a28e97` |
| `sections/6_dihedral_quaternion.tex` | `53e3781c2a3fe754018aefd19b43bd1f0b83e918349db19bd8e0fd2b758f1f27` |
| `sections/7_scope_controls.tex` | `f1ee3f875b6f61e36685dd4da74187e740bc3f22d84020f839703a9bf2c1a6f2` |
| `sections/8_conclusion.tex` | `eb50929e7b679abc8c09c8206226617038f1c66cc2435a23a9fb35ab2c87b842` |

Protocol coverage:

| Phase | Required surface | Audited surface | Status |
|---|---|---|---|
| A | 100% references | 3/3 entries, every stored field | PASS |
| B | at least 30% citation contexts | 5/5 contexts, 100% | PASS_WITH_PINPOINT_NOTE |
| C | 100% numerical/data/statistical surfaces | every table value, group datum, code assertion, frozen output, and manuscript locator | PASS; proof-regression controls only |
| D | at least 30% paragraphs and one per major section | 22/71 = 30.99%; abstract and Sections 1–8 represented | PASS_WITH_TOOL_LIMITATIONS |
| E | every HIGH-IMPACT claim plus at least `min(10,total)` | 26/26 semantic claims, including 20/20 HIGH-IMPACT | PASS |

For Phase E, `semantic completeness=not_machine_detectable`: semantic extraction is
model-mediated and cannot certify that no implicit claim was missed.  The registry is
therefore deliberately over-inclusive and audits every identified claim, not merely
the protocol minimum.

## 3. Phases A and B — bibliography and citation fidelity

The query-by-query record, direct URLs, field checks, and all five context decisions
are in [`SOURCE_SEARCH_LEDGER.md`](SOURCE_SEARCH_LEDGER.md).

Summary:

- `Klug2025`: **VERIFIED** against Cambridge, DOI, arXiv, and author records.
- `CarrollPenland2015`: **VERIFIED** against NYJM and arXiv.
- `CohenGoodmanStrauss2017`: **VERIFIED** against EMS, DOI, and arXiv.
- Ghost citations: none.
- Dangling bibliography records: none.
- Undefined compiled citations/references: none.
- Citation contexts: 4 `VERIFIED`, 1 `VERIFIED_WITH_PINPOINT_NOTE`.

The sole pinpoint note is objective: `sections/2_background.tex:55-58` cites closed
surface displays “following Theorem 3,” whereas the final Cambridge version numbers
the result Theorem 3.1.  The formula itself is supported: Klug Corollary 1, evaluated
at the identity, yields both manuscript formulas.  Klug is correctly described as the
chosen modern normalization source, while classical ownership is historical.

## 4. Phase C — theorem, table, and proof-regression consistency

### C1. Control classification and replay receipt

The project contains no empirical experiment, sampled dataset, fitted model,
statistical inference, or randomized run.  `code/verify_surface_flat_sft.py` is a
deterministic exact-integer/rational **proof-regression control**.  It directly
enumerates finite tuple distributions and checks selected instances of formulas whose
general validity rests on proofs and cited theorems.

Replay command:

```bash
python3 code/verify_surface_flat_sft.py
```

The replay was byte-identical to `code/verify_surface_flat_sft.out` and to the fenced
receipt in `CONTROL_RESULTS.md:13-29`.  Fingerprints at audit time:

| Artifact | SHA-256 |
|---|---|
| `code/verify_surface_flat_sft.py` | `1acc02c0d8fce337660c6c8b655a0803a8d856febaf721a37e299572ac3ac4e1` |
| `code/verify_surface_flat_sft.out` | `c8a56e4e9f692fa4bb97a535b2a683f2d220489f4e94d1dd99d5d01c87ed482d` |
| fresh replay | `c8a56e4e9f692fa4bb97a535b2a683f2d220489f4e94d1dd99d5d01c87ed482d` |

The terminal line is `ALL CHECKS PASS`.

This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

Here “experiment” in the required protocol sentence has no manuscript referent: P69
reports no experiment.  The sentence is retained verbatim to mark the C4 boundary.

### C2. Code-to-output-to-manuscript traceability

| Checked assertion | Code locator | Frozen output / package locator | Manuscript locator | Verdict |
|---|---|---|---|---|
| `D8` multiplication and group axioms | `code/verify_surface_flat_sft.py:17-25,72-80,228-232` | `code/verify_surface_flat_sft.out:1`; `CONTROL_RESULTS.md:14` | presentation and character calculation at `sections/6_dihedral_quaternion.tex:4-29` | PASS |
| `Q8` multiplication and group axioms | `code/verify_surface_flat_sft.py:27-49,72-80,228-232` | output line 2; control line 15 | `sections/6_dihedral_quaternion.tex:8-40` | PASS |
| exact commutator/square convolution | `code/verify_surface_flat_sft.py:83-118` | methodology `CONTROL_RESULTS.md:34-39` | Hom presentations at `sections/2_background.tex:60-80` | PASS |
| rooted gauge factors `|K|^(2m-1)` and `|K|^(n-1)` | `code/verify_surface_flat_sft.py:135-153` | `CONTROL_RESULTS.md:40-42` | proof `sections/3_flat_shift.tex:66-112`; specialization `sections/4_subgroup_counts.tex:62-80` | PASS |
| fixed formula exponents `4m`, `2n`, and `nu^(n+2)` | `code/verify_surface_flat_sft.py:121-132` | all group rows | `sections/4_subgroup_counts.tex:48-59` | PASS |
| `D8` fixed rows | `code/verify_surface_flat_sft.py:234-248` | output lines 3–4 | formulas/table `sections/6_dihedral_quaternion.tex:42-67` | PASS |
| `Q8` fixed rows | same | output lines 5–6 | same | PASS |
| orientable equality; nonorientable equality exactly at even `n` | `code/verify_surface_flat_sft.py:245-248` | output line 7 | `sections/6_dihedral_quaternion.tex:69-76` | PASS |
| `C3` group and FS signature `[1,0,0]` | `code/verify_surface_flat_sft.py:52-63,183-194` | output lines 8–9 | `sections/7_scope_controls.tex:60-77` | PASS |
| `C3` orientable and nonorientable laws | `code/verify_surface_flat_sft.py:196-210` | output lines 10–12 | Eq. (C3 control), `sections/7_scope_controls.tex:66-75` | PASS |
| `C3` trichotomy recovery `(1,0,2)` | `code/verify_surface_flat_sft.py:212-225` | output line 13 | `sections/7_scope_controls.tex:74-77` | PASS |
| `S3` independent-order orientable Hom check | `code/verify_surface_flat_sft.py:160-180` | output lines 14–15 | `sections/7_scope_controls.tex:63-64` | PASS |

### C3. Exact value audit

| Surface | Manuscript/predicted values | Direct enumeration | Status |
|---|---|---|---|
| `D8`, orientable `m=1..4` | `[17408, 68157440, 275951648768, 1126999418470400]` | identical | PASS |
| `D8`, nonorientable `n=1..5` | `[288, 17408, 1081344, 68157440, 4328521728]` | identical | PASS |
| `Q8`, orientable `m=1..4` | `[17408, 68157440, 275951648768, 1126999418470400]` | identical | PASS |
| `Q8`, nonorientable `n=1..5` | `[224, 17408, 1015808, 68157440, 4261412864]` | identical | PASS |
| `C3`, orientable `m=1..4` | `[243, 19683, 1594323, 129140163]` | identical | PASS |
| `C3`, nonorientable `n=1..5` | `[9, 81, 729, 6561, 59049]` | identical | PASS |
| `C3` normalized `P,Q,R` | `P=[3,3,3,3]`, `Q=[1,1]`, `R=[1,1,1]` | identical exact fractions | PASS |
| `S3` orientable Hom, genus 1–3 | `[18,486,16038]` | identical | PASS |

For the displayed `D8`/`Q8` table, direct substitution gives `O(1)=17408`,
`N_D8(1)=288`, `N_Q8(1)=224`, and both `N(2)=17408`.  The manuscript's odd-level
difference `2^(5n+1)` follows by subtracting the two signed two-dimensional terms and
also agrees with every checked odd row.

### C4. Four boundary audits requested for Stage 2.5

#### Surface-cover and coset convention

`sections/2_background.tex:6-27` uses the one-vertex `N3` complex with relator
`x1^2 x2^2 x3^2`, labels universal-cover vertices by the surface group, and takes
left cosets.  Under the stated left action `(h·z)(g)=z(h^-1 g)`, an `H`-fixed
configuration is constant on `Hg`, so the quotient edge `Hg -> Hgx_i` is consistent.
There is no left/right mismatch.  A degree-`V` cover has `V` vertices, `3V` edges,
and `V` faces, hence Euler characteristic `-V`, as used later.  **PASS**.

#### Nonorientable genus and index/divisibility

`sections/4_subgroup_counts.tex:4-42` proves: `H_n=ker(f mod n)` has index `n`;
`x3` lies in `H_n` but has odd orientation, so the cover is nonorientable; and
`chi=-n=2-(n+2)`, giving genus `n+2`.  The orientation kernel has index two and is
`pi_1(Sigma_2)`; `f` restricts surjectively because `x1 x3^-1` has even orientation
and `f=1`; hence `L_m` has total index `2m`, is orientable, and
`2-2g=-2m` gives `g=m+1`.  For `a|b`, kernel reduction gives
`H_b<=H_a` and `L_b<=L_a`, so “divisibility-directed families” is accurate.
**PASS**.

#### Rooted gauge identity and raw-count boundary

`sections/3_flat_shift.tex:66-112` uses based gauges, whose number is
`|K|^(V-1)`.  Freeness follows along a spanning tree from the root; the tree recursion
produces a unique tree-trivial representative; flat tree-trivial connections are in
bijection with `Hom(pi_1(Y),K)=Hom(H,K)`.  Thus
`|Fix_H(X_K)|=|K|^(V-1)|Hom(H,K)|`.  The manuscript explicitly does **not** quotient
by the full gauge group, whose stabilizers would depend on centralizers
(`sections/3_flat_shift.tex:114-119`).  **PASS**.

#### Indicator-zero recovery

`sections/5_moment_recovery.tex:88-126` first obtains
`s_d=c_d^+ + c_d^-` from even nonorientable moments.  At `n=2m+1`, including
`m=0`, the known bases `d^-2` have coefficients
`b_d=(c_d^+-c_d^-)/d`; `R_0,...,R_(r-1)` recover these coefficients by the
known-base Vandermonde clause, and multiplication by the already-known `d` recovers
the signed difference.  Finally `c_d^0=t_d-s_d`.  The exact `C3` control has degree
multiset `{1,1,1}`, indicators `[1,0,0]`, `P=3`, `Q=1`, `R=1`, and reconstructs
`(c_1^+,c_1^-,c_1^0)=(1,0,2)`.  **PASS**.

### C5. Qualitative P69/P70 comparison

The table at `sections/7_scope_controls.tex:22-44` was checked against the local P70
package.  P69 uses a nonorientable surface group, nonabelian finite-group edge labels,
raw flat connections, complex character degrees/FS indicators, and moment inversion.
P70 uses the discrete Heisenberg group, an additive finite-field principal kernel,
nullities on finite Heisenberg quotients, cross-characteristic block decomposition,
and modular rank jumps.  The claimed engine distinction is accurate.  The projects
share only the broad finite-index fixed-data strategy.  **PASS**.

## 5. Phase D — paragraph overlap and author overlap

The full 22-query ledger appears in `SOURCE_SEARCH_LEDGER.md`, Phase D.  The sample is
22/71 narrative paragraph units = **30.99%**, includes the abstract and Sections 1–8,
and uses exact 8–12-word strings.  Every query returned
`NO_EXACT_MATCH_IN_INDEXED_WEB`.  No result is elevated into an originality
certificate.

D2 status is exactly:

`NOT_RUN_AUTHOR_IDENTITIES_UNAVAILABLE`

Tool limitation: the audit used a general indexed web, not Turnitin, iThenticate,
Crossref Similarity Check, subscription full-text databases, or a complete historical
archive.  Exact-string searches may miss paywalls, nonindexed works, TeX/math or OCR
normalization, paraphrase, translation, and terminological variation.  Phase D is
therefore **PASS_WITH_TOOL_LIMITATIONS** and must be supplemented after authors are
known.

## 6. Phase E — semantic claim registry

Registry rule: all identified HIGH-IMPACT claims were audited, and every remaining
identified claim was also audited.  Coverage is 26/26; protocol floor is
`min(10,total)=10`.  As noted above,
`semantic completeness=not_machine_detectable`.

| ID | Impact | Claim and exact location | Provenance/evidence | Verdict |
|---|---|---|---|---|
| E01 | HIGH | Six-edge local holonomy defines a surface-group SFT, `sections/3_flat_shift.tex:6-46` | finite support and translated forbidden-list proof | VERIFIED_INTERNAL |
| E02 | HIGH | `H`-fixed points are raw flat connections on `H\N3~`, `sections/3_flat_shift.tex:51-64` | left-coset descent plus face holonomy | VERIFIED_INTERNAL |
| E03 | HIGH | rooted gauge identity, `sections/3_flat_shift.tex:66-112` | free based gauge action and spanning-tree bijection | VERIFIED_INTERNAL |
| E04 | HIGH | `H_n` index `n`, nonorientable genus `n+2`, `sections/4_subgroup_counts.tex:12-32` | surjective quotient, orientation character, Euler characteristic | VERIFIED_INTERNAL |
| E05 | HIGH | `L_m` index `2m`, orientable genus `m+1`, `sections/4_subgroup_counts.tex:34-41` | orientation kernel, restricted surjectivity, Euler characteristic | VERIFIED_INTERNAL |
| E06 | HIGH | orientable surface Hom formula, `sections/2_background.tex:60-73` | Klug Corollary 1 / classical Mednykh formula | VERIFIED_EXTERNAL |
| E07 | HIGH | nonorientable surface Hom formula, same locator | Klug Corollary 1 / classical Frobenius–Schur formula | VERIFIED_EXTERNAL |
| E08 | HIGH | orientable fixed law, `sections/4_subgroup_counts.tex:48-70` | E03 + E05 + E06; exact controls | VERIFIED |
| E09 | HIGH | nonorientable fixed law, `sections/4_subgroup_counts.tex:48-80` | E03 + E04 + E07; exact controls | VERIFIED |
| E10 | HIGH | orientable spectrum recovers `|K|`, `sections/5_moment_recovery.tex:62-74` | bounded positive moment factor and root limit | VERIFIED_INTERNAL |
| E11 | HIGH | orientable moments recover all degree multiplicities, `sections/5_moment_recovery.tex:76-86` | finite exponential-moment lemma | VERIFIED_INTERNAL |
| E12 | HIGH | even nonorientable moments recover self-dual multiplicities, `sections/5_moment_recovery.tex:88-102` | known-base Vandermonde with zero coefficients | VERIFIED_INTERNAL |
| E13 | HIGH | odd moments recover signs, including `m=0` and multiplication by known `d`, `sections/5_moment_recovery.tex:104-126` | explicit `b_d`, `R_0,...,R_(r-1)`, and reconstruction equations | VERIFIED_INTERNAL |
| E14 | HIGH | joint spectra determine order and degree/indicator multiset; converse, `sections/5_moment_recovery.tex:48-57,129-150` | E10–E13 and substitution | VERIFIED_INTERNAL |
| E15 | HIGH | `D8`/`Q8` degree and FS signatures, `sections/6_dihedral_quaternion.tex:4-40` | direct FS sums and finite group models | VERIFIED |
| E16 | HIGH | `D8`/`Q8` fixed formulas and odd/even separation, `sections/6_dihedral_quaternion.tex:42-76` | fixed laws, arithmetic, deterministic replay | VERIFIED_CONTROL |
| E17 | HIGH | `C3` exercises the `nu=0` trichotomy, `sections/7_scope_controls.tex:60-77` | exact root-of-unity indicator rule and replay | VERIFIED_CONTROL |
| E18 | HIGH | stored controls yield the printed values and `ALL CHECKS PASS`, `sections/7_scope_controls.tex:48-82` | byte-identical script replay and frozen receipt | VERIFIED_CONTROL |
| E19 | HIGH | P69 moment/FS engine differs from P70 Heisenberg/nullity engine, `sections/7_scope_controls.tex:22-44` | comparison against local P70 sources | VERIFIED_PACKAGE_COMPARISON |
| E20 | HIGH | bounded search found no exact combined collision, `sections/7_scope_controls.tex:84-90` | recorded alternate-term and exact-combination queries | SUPPORTED_WITHIN_SEARCH_ONLY |
| E21 | NORMAL | Carroll–Penland supplies group-SFT periodic/subgroup context, `sections/1_introduction.tex:26-28` | NYJM/arXiv abstract and introduction | VERIFIED_EXTERNAL |
| E22 | NORMAL | Cohen–Goodman-Strauss supplies surface-group SFT context, `sections/1_introduction.tex:28-30` | EMS/arXiv abstract | VERIFIED_EXTERNAL |
| E23 | NORMAL | Klug is modern normalization source, not classical owner, `sections/1_introduction.tex:31-35; sections/7_scope_controls.tex:13-20` | publisher introduction and explicit manuscript boundary | VERIFIED_WITH_PINPOINT_NOTE |
| E24 | NORMAL | recovered signature is not a finite-group classification, `sections/1_introduction.tex:125-131; sections/7_scope_controls.tex:6-11` | theorem output is expressly limited | VERIFIED_SCOPE |
| E25 | NORMAL | after order and number of bases are known, finite exact moments suffice, `sections/5_moment_recovery.tex:152-161` | recurrence/rational-function and Vandermonde argument | VERIFIED_INTERNAL |
| E26 | NORMAL | no external data; controls are not proof; declaration items unresolved, `sections/7_scope_controls.tex:79-82; sections/8_conclusion.tex:22-44` | package contents, deterministic code, declarations | VERIFIED_DISCLOSURE_WITH_UNRESOLVED_AUTHOR_FIELDS |

No high-impact claim depends solely on the finite control.  E18 is a claim about the
control receipt itself; E16/E17 use controls only as finite regression evidence in
addition to the general proof.

## 7. Integrity of the main mathematical mechanisms

### 7.1 Finite moment lemma and reconstruction

The first clause of the moment lemma identifies distinct nonzero bases and nonzero
coefficients from the full positive-index sequence by the poles and residues of a
rational generating function.  The second, known-base clause explicitly permits any
`r` consecutive nonnegative indices, including zero, and permits zero coefficients.
This exactly matches Step 3 and Step 4.  The order limit remains valid even when
several degree-one characters occur, because the normalized positive sum remains
between 1 and the number of irreducibles before taking the `1/(4m)` root.  **PASS**.

### 7.2 Fixed-law exponent bookkeeping

For `L_m`, index `V=2m` gives gauge factor `|K|^(2m-1)` and orientable genus `m+1`
gives Hom factor `|K|^(2m+1)`, hence `|K|^(4m)`.  For `H_n`, index `V=n` gives gauge
factor `|K|^(n-1)` and nonorientable genus `n+2` gives Hom factor `|K|^(n+1)`, hence
`|K|^(2n)` and indicator power `n+2`.  The degree exponents reduce to `-2m` and `-n`,
respectively.  All table formulas and code use those same exponents.  **PASS**.

### 7.3 No hidden gauge quotient

The theorem counts alphabet configurations / edge labels.  Based gauge fixing is a
counting bijection used to factor the raw set; it does not replace the state space by
gauge orbits.  The manuscript's warning about unbased stabilizers is mathematically
necessary and present.  **PASS**.

## 8. Priority search, nearest neighbors, and owner subtraction

At least three alternate-term queries were run for each of the five core claim
families, with additional exact-combination queries.  The full query strings and
direct URLs are in `SOURCE_SEARCH_LEDGER.md`.  The search was current through
2026-08-26.

Nearest-neighbor map:

| P69 surface | Nearest owners / sources | Owner-subtracted assessment |
|---|---|---|
| finite-group surface Hom formulas | Mednykh and Frobenius–Schur historically; Klug modern account; Snyder, Mulase–Yu, Turaev alternative topological/algebraic accounts | wholly cited/classical input, not P69 mass |
| lattice/finite-gauge edge-state formulation | Snyder <https://arxiv.org/abs/math/0703073>; Turaev <https://arxiv.org/abs/0706.0160> | close neighbor; flat/lattice bridge alone cannot be claimed |
| group-shift periodic/subgroup setting | Carroll–Penland <https://nyjm.albany.edu/j/2015/21-36.html> | established setting |
| surface-group SFTs | Cohen–Goodman-Strauss <https://ems.press/journals/ggd/articles/14944> | SFT existence/context established |
| inverse character-degree sums | representation-zeta literature, e.g. Liebeck–Shalev <https://doi.org/10.1112/S0024611504014935> | inverse-degree moment object established |
| Vandermonde recovery | elementary finite moment algebra | proof engine, not a standalone priority claim |
| `D8`/`Q8` indicators | standard character theory | control/example only |

Residual candidate contribution after subtraction: the combined theorem sequence
consisting of the explicit `N3` finite-type edge-holonomy model, the two
divisibility-directed cover families, the raw fixed-count identity, and joint recovery
of `|K|` plus the multiset `(degree, FS indicator)` from their selected spectra.

Exact collision verdict: **NOT_FOUND_WITHIN_BOUNDED_SEARCH**.  Collision risk:
**MEDIUM**, because the ingredients are individually close and the search tools do not
cover all mathematical literature.  This is expressly **not** a worldwide priority
certificate, not a specialist novelty clearance, and not authorization for release.

## 9. Seven-mode failure checklist

| Failure mode | Evidence checked | Verdict |
|---|---|---|
| 1. Implementation bug | group axioms, multiplication laws, exact convolution, independent formulas, frozen-output diff, hashes | CLEAR_WITHIN_FINITE_CONTROL_SCOPE; controls do not prove the theorem |
| 2. Hallucinated citation | 3/3 records field-verified; 5/5 contexts checked; aux/log check | CLEAR_WITH_MINOR_PINPOINT_NOTE (`Theorem 3` → `3.1`) |
| 3. Hallucinated experimental result | no empirical experiment exists; all reported numbers arise from deterministic enumeration | NOT_APPLICABLE_NO_EMPIRICAL_EXPERIMENTS |
| 4. Shortcut reliance | theorem rests on explicit proofs and cited classical formulas; code is labeled non-premise | CLEAR_WITH_DISCLOSED_BOUNDARY |
| 5. Bug reframed as insight | no code/formula discrepancy found; limitations and negative search are stated | CLEAR_WITHIN_AUDIT |
| 6. Methodology fabrication | definitions, proof chain, exact script, and frozen output are all present; no statistical method is claimed | CLEAR_THEORETICAL_METHOD |
| 7. Frame-lock | alternate-term searches surfaced lattice TQFT, gauge/state-sum, surface SFT, covering, and representation-zeta neighbors | PASS_WITH_NOTES; medium collision risk remains |

## 10. Authorship, disclosure, and release audit

| Field | Current status | Required action |
|---|---|---|
| Author names/order/affiliations | UNRESOLVED | responsible researchers authorize final list |
| Contributions | UNRESOLVED | supply and approve contributor statement |
| Funding | UNRESOLVED | author confirmation, including explicit “none” if applicable |
| Competing interests / COI | UNRESOLVED | author confirmation, including explicit “none” if applicable |
| AI-assisted drafting/checking | disclosed in `sections/8_conclusion.tex:40-44` and package declarations | human authors must verify and approve final wording |
| Human/animal/personal data | not used | no research-participant ethics issue identified |
| D2 author-overlap search | `NOT_RUN_AUTHOR_IDENTITIES_UNAVAILABLE` | rerun after author authorization |
| External dissemination | HOLD | no upload, contact, release, submission, or priority statement authorized |

## 11. Objective corrections and final disposition

### Required before external release

1. In `sections/2_background.tex:55-58`, change the Klug pinpoint from
   “Theorem 3” to “Theorem 3.1”; synchronize any duplicated pinpoint in package
   documentation.
2. Add Snyder's *Mednykh's Formula via Lattice Topological Quantum Field Theories*
   (<https://arxiv.org/abs/math/0703073>) to the bibliography and related-work /
   ownership discussion.  State that lattice/topological finite-gauge derivations of
   the surface formulas predate P69.
3. Add a suitable representation-zeta citation for the standard inverse-degree
   moment object; Liebeck–Shalev (<https://doi.org/10.1112/S0024611504014935>) is a
   verified candidate, though a specialist may select a more directly historical
   source.
4. Keep the novelty statement search-bounded; do not assert global priority.  Obtain
   specialist review across symbolic dynamics, surface topology, and finite-group
   representation theory.
5. Resolve authorship/contributions/funding/COI, approve the AI-use statement, and run
   the author-identity overlap check.

### Not required by this audit

- No correction to the core theorem, cover genera/indices, gauge factor, moment
  inversion, `nu=0` recovery, or `D8`/`Q8` separation was found.
- No existing `references.bib` field needs correction; the bibliography needs
  augmentation, not repair of its three stored records.
- The exact finite-control script and frozen values require no change.

### Final status

| Axis | Decision |
|---|---|
| Mathematical/proof consistency | PASS within author self-audit |
| Reference authenticity | PASS |
| Citation-context fidelity | PASS_WITH_ONE_PINPOINT_NOTE |
| Numerical/control integrity | PASS as proof-regression controls |
| Paragraph-overlap screen | PASS_WITH_TOOL_LIMITATIONS |
| Priority/novelty | SEARCH-BOUNDED, MEDIUM COLLISION RISK, no certificate |
| Declarations | UNRESOLVED |
| Overall | **PASS_WITH_NOTES** |
| External release | **HOLD** |

