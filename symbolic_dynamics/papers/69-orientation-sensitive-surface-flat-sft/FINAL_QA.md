# P69 final author QA with ARS 0.1.27 Stage-2.5 strict closure

**Manuscript:** *Orientation-Sensitive Periodic Spectra of Surface-Group
Flat-Connection Shifts*  
**Current audit date:** 2026-08-26 UTC  
**Official Round-2 core-proof audit:** **PASS**  
**Package-wide Round-2 compliance after synchronization and author replay:**
**PASS**  
**Stage 2.5 overall:** **PASS_WITH_NOTES**  
**Strict cited-source tuple gate:** **PASS**  
**Stage 3 checkpoint:** **NOT CLEARED / HOLD**  
**External release:** **HOLD**

This report is an author-side build, synchronization, and proof-state audit.
It does not claim a new independent reviewer verdict, specialist clearance,
priority clearance, or release authorization. The official Round-2 review is
preserved at reviews/GPT54_XHIGH_ROUND2_PROOF_AUDIT.md.

The Round-2 build/snapshot sections below are retained as historical receipts.
The final current-surface authority is the Stage-2.5 overlay and
`stage2_5/POST_CORRECTION_INTEGRITY_DISPOSITION.md`.  No manuscript source or PDF
was changed during the strict-closure pass.

## Official review and resolution gate

- The 398-line official Round-2 proof audit is present and unmodified.
- Its core-mathematics verdict is **PASS**: no critical or major mathematical
  defect survived its proof reconstruction.
- Its pre-synchronization full-package verdict was **PARTIAL FAIL**, solely
  because the Chinese abstract and stale extracted-text receipts retained
  superseded terminology.
- The author response is recorded in
  rounds/GPT54_XHIGH_ROUND2_RESOLUTION.md.
- Neither official review supplies a numerical score; none is inferred.

## Package synchronization gate

- BILINGUAL_ABSTRACT.md now uses 子群族 and 非定向族.
- qa/final_text.txt and qa/final_text.new.txt were regenerated from the
  current PDF and are byte-identical.
- A package-wide text search outside immutable reviews/** finds zero matches
  for the prohibited English and Chinese false-nesting expressions.
- DECLARATIONS.md now exists and accurately records data/code, authorship,
  funding/interests, ethics, AI use, authorization, Stage 2.5, and HOLD state.
- Current configuration, build instructions, cumulative log, workflow state,
  visual receipt, and checksum manifest are synchronized.
- Package-wide Round-2 compliance after these fixes and author replay: **PASS**.

## Historical official Round-2 deliverable and snapshot gate

- Official Round-2 snapshot: main_gpt54_round2.pdf.
- main.pdf, main_gpt54_round2.pdf, and main_gpt54_round1.pdf are
  byte-identical because Round 2 required no manuscript-source change.
- Official Round-1 pre-review and revised PDFs remain preserved.
- main_round2.pdf is the earlier internal typesetting/source-role snapshot,
  not the official GPT-5.4/xhigh Round-2 snapshot.
- Configuration, narrative, plan, claims/evidence ledger, argument blueprint,
  proof package, bilingual abstract, citation audit, controls, figure decision,
  declarations, build instructions, author resolutions, and state JSON are
  present.
- The rejected Rudin--Shapiro memo remains clearly marked “NOT MANUSCRIPT
  CONTENT.”

## Core mathematical gate

- The local six-edge surface relator defines the claimed SFT: proof closed.
- The left-shift/left-coset convention agrees with the quotient cellulation.
- Rooted spanning-tree gauge fixing gives
  \[
  |\operatorname{Fix}_H(X_K)|
  =|K|^{[\Lambda:H]-1}|\operatorname{Hom}(H,K)|.
  \]
- Both all-modulus probes are divisibility-directed families, with cover
  genera \(n+2\) nonorientable and \(m+1\) orientable.
- The Frobenius--Schur--Mednykh substitutions give the fixed laws with powers
  \(4m\), \(2n\), \(n+2\), and \(-n\).
- The finite-moment lemma explicitly permits \(m_0=0\).
- Theorem 5.2 Step 4 uses \(R_0,\ldots,R_{r-1}\) to recover
  \(b_d=(c_d^+-c_d^-)/d\), then multiplies by known \(d\) to obtain the signed
  multiplicity difference.
- The root limit and three finite moment systems recover \(|K|\) and all
  \((d,\nu)\) multiplicities, including \(\nu=0\).
- The \(D_8/Q_8\) orientable equality and odd-nonorientable separation remain
  proved.
- Klug is the chosen modern normalization account; classical ownership remains
  with Mednykh and Frobenius--Schur.

## Exact finite-control gate

Running python3 code/verify_surface_flat_sft.py gives:

- \(D_8,Q_8,C_3,S_3\) group-axiom checks: PASS;
- direct orientable/nonorientable counts versus character formulas: PASS;
- \(D_8/Q_8\) equality and parity split through the stored ranges: PASS;
- \(C_3\) indicator signature \([1,0,0]\): PASS;
- \(C_3\) reconstruction
  \((c_1^+,c_1^-,c_1^0)=(1,0,2)\): PASS;
- terminal status ALL CHECKS PASS.

qa/control_replay.txt is byte-identical to
code/verify_surface_flat_sft.out, with SHA-256
c8a56e4e9f692fa4bb97a535b2a683f2d220489f4e94d1dd99d5d01c87ed482d.
The controls are regression evidence, not proof premises.

## Historical official Round-2 deterministic build and text gate

- Build: pdflatex -> bibtex -> pdflatex -> pdflatex, with
  SOURCE_DATE_EPOCH=1787616000; every command exited zero.
- PDF: 10 A4 pages, 371,616 bytes.
- PDF SHA-256:
  09216444bcc5abd911b88d3ac28416ca5a547efe236b0a22b5fc39781a676b08.
- Layout-preserving text: 576 lines, 4,894 words, 38,387 bytes.
- Text receipt SHA-256:
  1465d6a3a90dfd782976dc80fcb5392d3a4ed8bf5b297cd11bdd91e251b331b8.
- Final log: zero warnings, errors, undefined citations/references,
  multiply-defined labels, overfull boxes, or underfull boxes.
- Malformed exponent prefix caret-brace-comma: zero source matches.
- Bibliography: 3 cited keys, 3 entries, zero missing.
- Fonts: 23 records, all embedded and subset.
- PDF Author metadata: empty; volatile creation/modification dates omitted.
- Current receipts: qa/pdfinfo.txt, qa/pdffonts.txt, qa/final_text.txt, and
  qa/control_replay.txt.

## Visual gate

Author-side original-resolution inspection of newly rendered pages 1, 5, 7,
9, and 10 passed:

- page 1: abstract/main laws and “families” terminology;
- page 5: cover-family topology and exact fixed laws;
- page 7: corrected known-base Step 4;
- page 9: source firewall, P69/P70 separation, and \(C_3\) control;
- page 10: HOLD posture, conclusion, declarations, and bibliography.

No clipping, overlap, missing glyph, malformed exponent, or unreadable table
was observed. Image hashes and page-by-page checks are recorded in
qa/GPT54_XHIGH_ROUND2_VISUAL_RECEIPT.md.

## Snapshot hashes

- Round-0 original:
  9cac82112588407f1dbc1bc3e18099d58e67e3a0fcddafda74da1c7202be7b8c
- Pre-official-Round-1:
  1ef742b0bd882e179185db0d57413c65cde496d53711495eff5b96c9e3cd386e
- Official Round 1:
  09216444bcc5abd911b88d3ac28416ca5a547efe236b0a22b5fc39781a676b08
- Official Round 2/current:
  09216444bcc5abd911b88d3ac28416ca5a547efe236b0a22b5fc39781a676b08
- Control script:
  1acc02c0d8fce337660c6c8b655a0803a8d856febaf721a37e299572ac3ac4e1
- Stored/replayed control output:
  c8a56e4e9f692fa4bb97a535b2a683f2d220489f4e94d1dd99d5d01c87ed482d

After the strict Stage-2.5 metadata was sealed, `SHA256SUMS` was regenerated as
the comprehensive current package manifest and replay-checked file by file.

## Residual gates

No Round-2 theorem/proof or package-synchronization defect remains from the
supplied audit.  Stage 2.5 has an author-side **PASS_WITH_NOTES** disposition, but
independent specialist/collision review remains pending, including
symbolic-dynamics literature, surface-cover conventions, and
finite-group/Frobenius--Schur framing. Human authorship, funding,
competing-interest, citation, priority, submission, and release approval also
remain pending. No priority claim is made. External release remains **HOLD**.

## Stage 2.5 correction overlay — 2026-08-26

The snapshot hashes and generated receipts above document the pre-Stage-2.5
review freeze. The corrected current `main.pdf` is 11 A4 pages, 377,379
bytes, SHA-256
`93462a17e92207d9dfbccc55d6ac543391c55a8950d5057a50e9a3b9996c2766`.
All seven bibliography records and twelve citation contexts close with zero
ghost/dangling keys; the final log is clean, all fonts are embedded/subset,
and the deterministic control remains byte-identical to its receipt.

Author-side Stage 2.5 content status is **PASS_WITH_NOTES after correction
round 1**. The bounded residual collision risk is **MEDIUM**; priority and
specialist clearance are not granted. External release remains **HOLD**.

## ARS 0.1.27 strict-closure overlay — 2026-08-26

The post-correction disposition is
`stage2_5/POST_CORRECTION_INTEGRITY_DISPOSITION.md`.  Its active declaration
authority is exactly
`docs/papers67_71_sequence/stage2_5/MATERIAL_PASSPORT.yaml`, SHA-256
`097d6d3cc38d0dc8a97889ba40966bd82d422c8a4c4bc8ae0851015b85ea6f99`.
The passport declares `no_experiments_declared`, empty experiment provenance, proof-
regression controls rather than experiments, and external `HOLD`; its own
verification status is `VERIFIED` for the bounded Stage-2.5 gate.  No duplicate
human declaration, priority clearance, or release authorization was inferred.

Current identity:

- `main.pdf`: 11 A4 pages, 377,379 bytes, SHA-256
  `93462a17e92207d9dfbccc55d6ac543391c55a8950d5057a50e9a3b9996c2766`;
- source bundle: 12 bytewise path-sorted, workspace-relative GNU `sha256sum`
  lines for `main.tex`, `references.bib`, `sections/*.tex`, and `code/*.py`;
  1,693-byte stream SHA-256
  `4b5662953e295cf61e9a0bfcf8b5a0d89651778da522e90196300eaad27a85be`;
- claim view `stage2_5/draft_for_claim_registry_round1.md`: 34,047 raw bytes,
  SHA-256
  `276cb82f2fcb4d2aaa70a609bb999c0297261ad1fbfd870e3785fc2b08c8760b`;
- active registry: 38 claims, 35 selected, SHA-256
  `a183b820506a697012a6b1cbe43a4918125a57920cdf7c7ef1407cddfcc4c5ba`.

Strict Phase-E replay is **PASS**: 37/37 expected tuples in exact registry order,
all 35 selected claims have claim-level verdict `VERIFIED`, all 37 rows are
`VERIFIED`, 12 positive rows are bound to genuine session-held cited-source
excerpts, 25 no-reference rows retain explicit anchorless excerpt states, and there
are zero manuscript-self evidence rows or serious claim verdicts.  The evidence row
file SHA-256 is
`b094e0edd17f00e221b0b507c954aabdef5813f99c2b5ce72df8d7201b96bd90`;
the tuple replay SHA-256 is
`faabf3baceed133cf1eda5edffff21f015d8503b68fcb24a7635b16abbbe1c8b`.
For the 25 anchorless rows, the claim verdict comes from the current internal
proof/proof-control audit while the empty excerpt remains anchorless.  The verdict
does not upgrade provenance or replace the empty source-evidence state with
manuscript self-evidence.

The current A/B audit closes 7/7 bibliography records and 12/12 citation contexts,
with zero ghost or dangling keys.  The wrong Roettger author-page PDF was excluded;
strict positive evidence uses the genuine Elsevier title/coredata surface, and its
limited access is disclosed.  D1 samples 24/70 current narrative paragraphs
(34.2857%), represents all section files, and reports no exact indexed-web match;
the result remains tool-limited.  D2 is exactly
`NOT_RUN_AUTHOR_IDENTITIES_UNAVAILABLE`.

The E6 sidecar
`stage2_5/claim_strength_drift_findings_round1.json`, SHA-256
`3fc83321dc858c80faf5348e44f0120d25e3fc9a284ca186ce7ab2fc55ba0f19`,
validates against the exact `claim-strength-drift-findings/1.0` schema but truthfully
records `skipped_no_revision_evidence` and a null Revision-Evidence Bundle hash.
Its empty findings list is not evidence of no semantic drift.  Because no prior
block-anchored Revision-Evidence Bundle exists, this schema-valid skip is the
prescribed non-blocking first-pass branch.  The Stage-2.5 gate is therefore
complete and Stage 3 awaits explicit user confirmation.  Medium search-bounded
collision risk, absent specialist review, D2, and unresolved human
authorship/funding/COI/release decisions keep external release **HOLD**.
