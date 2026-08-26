# Paper improvement log

## Prior independent-review provenance

`independent cross-agent review; requested GPT-5.4 child unavailable due agent thread cap`

P67 was first reviewed by a cross-agent who did not author it.  At that earlier
checkpoint, the requested nested GPT-5.4 reviewer could not be started because
the root agent tree had reached its hard thread cap.  The quoted provenance
applies only to those two earlier rounds.  Two official `gpt-5.4 xhigh` rounds
were subsequently completed and are recorded below; no numerical score was
supplied or invented.

## Round 0 — frozen baseline

Artifact: `main_round0_original.pdf` (10 pages).

SHA-256:
`c0a1a8c5965ff816380f190a50ec895dd533f71dc423abe86fdd56c3cc427034`.

The baseline contained the full root decomposition, free-axis
homeomorphism, finite-shape rank/matroid theorem, Haar formulas, prefix law,
and exponent-rectangle law.  The hostile review found one false mathematical
sentence and several proof/source presentation defects.

## Round 1 — hostile theorem and source audit

Review: `reviews/ROUND1_HOSTILE_REVIEW.md`.

Verdict: **MAJOR REVISION; theorem contract retained**.

Closed issues:

- Corrected the false claim that deleting a cycle edge raises projection
  dimension.  The repaired bridge/cycle dichotomy appeared on page 7 of the
  Round-1 PDF.
- Defined the coordinate-dependence matroid as the vector matroid of the
  restricted evaluation maps `epsilon_n:x -> x_n` (page 2).
- Rewrote the matrix proof to identify the evaluation-row matroid with the
  column matroid of the transposed oriented incidence matrix, including the
  characteristic-two case (page 5).
- Replaced “a spanning forest” by “a maximal spanning forest” for a matroid
  basis (page 5).
- Recast the triangular prefix argument as a local row-rank cross-check and
  explicitly retained the global extension theorem as the extension step
  (page 6).
- Added Ban--Hu--Lin (2019), Whitney (1935), and Watanabe (1960); cited the
  standard matroid and total-correlation ingredients and neutralized
  ownership-sounding manuscript prose (pages 1, 5, and 9--10).
- Synchronized the proof package, claims/evidence ledger, source audit, paper
  plan, and configuration.

Verification:

- deterministic controls: `ALL CHECKS PASS`;
- stable LaTeX/BibTeX build: clean;
- Round-1 PDF: 10 pages, 403,261 bytes;
- artifact: `main_round1.pdf`;
- SHA-256:
  `91f0cd6b9999aae7c3711b91c2dcd653e416eec9cc5c826907b381574f2543a5`.

## Round 2 — independent proof reconstruction

Review: `reviews/ROUND2_PROOF_AUDIT.md`.

Verdict: **ACCEPTABLE AS AN INTERNAL HOLD DRAFT AFTER LIMITED FIXES**.

Closed issues and strengthening:

- Replaced the cycle-sign ellipsis by the indexed identity
  `sum_l(z_(i_l,j_l)-z_(i_(l+1),j_l))=0`, with `i_(k+1)=i_1`
  (page 5).
- Added Peres--Schmeling--Seuret--Solomyak (2014) as direct context for a
  two-generator multiplicative semigroup, bringing the verified bibliography
  to eight cited primary records (pages 1, 9--11).
- Promoted the corrected deletion/addition statement to a formal one-edge
  rank-update corollary with proof (page 8).
- Added eleven deterministic edge-update transitions: four cycle-edge
  deletions, three bridge deletions, and four additions (control discussion on
  page 10).
- Standardized the finite random-vector notation in the rectangle Haar
  formula and removed the remaining ambiguous scope pronoun.
- Synchronized all theorem, proof, control, citation, and claim ledgers.

Final verification:

- 10,000 root-coordinate checks, 15 global reconstructions, 320 prefix cases,
  12,288 arbitrary finite projections, 108 rectangles, 11 edge updates, and
  9 exact Haar enumerations: all pass;
- frozen control output and live output: byte-identical;
- final LaTeX log: zero undefined citations/references, rerun requests,
  multiply-defined labels, overfull boxes, underfull boxes, or badness
  warnings;
- 8 cited keys / 8 bibliography entries;
- 28 fonts, all embedded and subset;
- all 11 pages visually inspected;
- at the close of that cross-agent round, the then-current `main.pdf` and
  `main_round2.pdf` were byte-identical.

Cross-agent Round-2 snapshot SHA-256:
`7bf54d3b56530decc051f56cfedc38684d432fca8c73474347d2ab33546bda7d`.

## Status after the prior cross-agent rounds

No open critical or major proof issue remains in the bounded two-round audit.
External release remains **HOLD** for specialist exact-neighbor review in
multiplicative symbolic dynamics, algebraic actions, finite-field coding, and
matroidal probability.

## Official GPT-5.4 XHigh Round 1 — integrity cleanup

Review: `reviews/GPT54_XHIGH_ROUND1_HOSTILE_REVIEW.md`.  Resolution:
`reviews/GPT54_XHIGH_ROUND1_RESOLUTION.md`.

The official reviewer found no new theorem-level failure and identified three
verified integrity defects.  All were fixed: the missing backslash before
`\qquad` in the evaluation-map display, the undefined `V_r` in Table 1, and
the malformed C9 evidence cell.  Controls and a stable build pass.  The
pre-review PDF is `main_pre_gpt54_round1.pdf`; the revised artifact is
`main_gpt54_round1.pdf`, byte-identical to `main.pdf`, with SHA-256
`48c3688f29062934ceb81f0b2077555b24ea23716e5224bd28ef5af7ae84729e`.

At that Round-1 checkpoint, official GPT-5.4 XHigh Round 2 had not yet run.
External release remained **HOLD**.

## Official GPT-5.4 XHigh Round 2 — proof audit and release synchronization

Review: `reviews/GPT54_XHIGH_ROUND2_PROOF_AUDIT.md`.  Resolution:
`reviews/GPT54_XHIGH_ROUND2_RESOLUTION.md`.

The official reviewer independently rederived every theorem family and
returned mathematics **PASS** with no critical or theorem-level issue.  The
single major issue was release-package integrity: the live official-Round-1
PDF had hash `48c368...`, while several QA and freeze records still described
the older cross-agent snapshot with hash `7bf54d...`.

The canonical final is now explicitly `main.pdf`, byte-identical to
`main_gpt54_round1.pdf` and `main_gpt54_round2.pdf`, with SHA-256
`48c3688f29062934ceb81f0b2077555b24ea23716e5224bd28ef5af7ae84729e`.
The older `main_round2.pdf` and `main_pre_gpt54_round1.pdf` remain preserved as
historical artifacts.  QA text, PDF metadata, font/log receipts, plan, build
instructions, state, and the checksum manifest were regenerated against the
canonical artifact.  Exact controls and a clean deterministic build pass; no
manuscript source was changed in Round 2.

Official GPT-5.4 XHigh rounds completed: **2**.  Mathematics: **PASS**.
Release-package integrity after synchronization: **PASS**.  External release
remains **HOLD** pending Stage 2.5 and specialist exact-neighbor review; neither
gate is claimed to have passed.
