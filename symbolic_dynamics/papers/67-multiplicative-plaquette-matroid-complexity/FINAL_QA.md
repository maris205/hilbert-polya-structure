# P67 final quality-assurance report

**Freeze date:** 2026-08-25 UTC  
**Official GPT-5.4 XHigh Round-2 mathematics:** **PASS**  
**Release-package integrity after synchronization:** **PASS**  
**External-release verdict:** **HOLD — Stage 2.5 and specialist exact-neighbor gates remain**

## Review provenance and deliverables

- The two earlier independent cross-agent rounds retain their recorded
  provenance: `independent cross-agent review; requested GPT-5.4 child
  unavailable due agent thread cap`.
- Two subsequent official review rounds were completed with model provenance
  `gpt-5.4 xhigh`; no numerical reviewer score was supplied or invented.
- Official Round-1 repair and official Round-2 proof audit/resolution: PASS.
- Historical PDFs `main_round0_original.pdf`, `main_round1.pdf`,
  `main_round2.pdf`, and `main_pre_gpt54_round1.pdf`: preserved.
- Canonical PDFs `main.pdf`, `main_gpt54_round1.pdf`, and
  `main_gpt54_round2.pdf`: byte-identical and PASS.
- Improvement log and machine-readable state: PASS.
- Anonymous modular `amsart` source, proof package, claims/evidence ledger,
  citation audit, controls, and build instructions: PASS.

## Mathematical gate

- Unique `r a^i b^j` coordinates for coprime prime or composite multipliers:
  PASS.
- Mixed-difference integration and explicit global free-axis homeomorphism:
  PASS.
- Every finite projection has dimension
  `sum_r(|I_r|+|J_r|-c_r)`: PASS.
- Restricted coordinate-evaluation matroid is the direct sum of the root-wise
  graphic matroids: PASS.
- Indexed cycle equations are necessary and sufficient: PASS.
- Haar entropy, total correlation, forest independence, and pairwise
  independence: PASS.
- Prefix count `q^(L-floor(L/(ab)))` with separate extension and pivot-rank
  logic: PASS.
- Rectangle count `q^(M+N-1)` and defect `(M-1)(N-1)`: PASS.
- Formal bridge/cycle deletion and addition dichotomy: PASS.
- Arithmetic-prefix, exponent-box, and dynamical-entropy terminology remains
  separated: PASS.
- Open critical issues: 0.  Open major issues: 0.

## Source and scope gate

- 8 unique cited keys / 8 bibliography entries / 0 missing entries.
- Primary records rechecked for KPS (2012), Peres--Schmeling--Seuret--Solomyak
  (2014), Ban--Hu--Lin (2019), Ban--Hu--Lai (2021), Ban--Hu--Lai--Liao
  (2025), Mora Cuellar--Rojas Aravena--Yavicoli (2026), Whitney (1935), and
  Watanabe (1960).
- No “first” or worldwide novelty claim appears.
- Bounded search status remains `BOUNDED_NO_EXACT_COLLISION_LOCATED`, not a
  novelty certificate.

## Deterministic controls

`python3 code/verify_plaquette_matroid.py` ends in `ALL CHECKS PASS`:

- 10,000 root coordinates and 15 global-axis reconstructions;
- 320 prefix rank/count cases;
- all 12,288 subsets of `[1,12]` in three multiplier/field cases;
- 108 exponent rectangles;
- 11 edge deletion/addition transitions; and
- 9 exact Haar/forest/cycle enumerations.

Live output is byte-identical to both frozen output receipts.  Script SHA-256:
`d0a2d3a1bd0c743b375eaf7e2dc98b100ff08f30cd741641cb1fcd81ab98a158`;
output SHA-256:
`a44506264017a8e6250e123df4477898def6c23f560c67b4e829948967c0bb26`.
Finite controls remain regression evidence, not proof premises.

## Compilation and visual gate

- Stable `pdflatex / bibtex / pdflatex` build: PASS.
- Final log: zero undefined citations/references, rerun requests,
  multiply-defined labels, overfull boxes, underfull boxes, or badness
  warnings.
- PDF: 11 A4 pages, 405,543 bytes, 5,157 extracted words.
- Fonts: 28 records; every font embedded, subset, and Unicode-mapped.
- Title and author PDF metadata empty; creation/modification dates omitted.
- All 11 rendered pages inspected.  The title, theorem displays, indexed cycle
  formula (page 5), prefix proof (pages 6--7), one-edge corollary and geometry
  table (page 8), scope table (page 9), conclusion and references (pages
  10--11) are unclipped and legible.

## Frozen artifact identities

- Round 0:
  `c0a1a8c5965ff816380f190a50ec895dd533f71dc423abe86fdd56c3cc427034`.
- Round 1:
  `91f0cd6b9999aae7c3711b91c2dcd653e416eec9cc5c826907b381574f2543a5`.
- Prior cross-agent Round 2 and pre-official-Round-1 snapshot:
  `7bf54d3b56530decc051f56cfedc38684d432fca8c73474347d2ab33546bda7d`.
- Official GPT-5.4 XHigh Round 1, official Round 2, and canonical final:
  `48c3688f29062934ceb81f0b2077555b24ea23716e5224bd28ef5af7ae84729e`.

`main.pdf`, `main_gpt54_round1.pdf`, and `main_gpt54_round2.pdf` are
byte-identical.  `main_round2.pdf` is intentionally retained as the older
cross-agent snapshot and is not the canonical final.

## Remaining release risk

Equivalent formulations may occur under algebraic-action, coding-theory,
discrete-potential, or matroidal-probability terminology.  The exact-neighbor
search remains bounded.  External release is therefore **HOLD** pending Stage
2.5 and a specialist search with manual forward/backward citation review.
Neither remaining gate is claimed to have passed.

## Stage 2.5 correction overlay — 2026-08-26

The frozen identities above describe the pre-Stage-2.5 review snapshots. The
current canonical `main.pdf` was rebuilt after correction round 1 and is not
byte-identical to those historical PDFs. Its current identity is 11 A4 pages,
408,243 bytes, SHA-256
`ed2ffeedc97cc82d006bf540468ef7bf9c1655cad3f4600fb393f8d6451fc7da`.
All 11 bibliography records and 17 citation contexts close with zero
ghost/dangling keys; the final log is clean, every font is embedded/subset, and
the deterministic control remains byte-identical to its frozen receipt. The
objective source and owner-subtraction fixes are itemized in
`stage2_5/CORRECTION_ROUND_1.md`.

Author-side Stage 2.5 content status is **PASS_WITH_NOTES after correction
round 1**. Collision risk remains search-bounded **MEDIUM**; priority and
specialist clearance are not granted. External release remains **HOLD**.

## Strict ARS 0.1.27 post-correction closure — 2026-08-26

The current 33-claim registry selects 23 claims and expands to 27 strict
`evidence-row/1.0` tuples in exact registry/ref order: 11 source-bound exact
excerpt rows and 16 explicit anchorless empty-state rows.  The ARS builder and
source-map validator pass all 27 rows; the independent tuple-order replay also
passes.  Evidence rows, source map, and source manifest have SHA-256 values
`2ee12d21799c6b11084c476c7277b569a295dc5c668d2082319befb4aea34347`,
`b3329d9f580a9ba117948eecaa34f5988d2cbf0209eed074dcc02c5a9117ad68`,
and `a313c85ffa40643099bb150274a06010d3a527dad5ed4cee623d0d2dfa00a75a`.

The corrected-manuscript D1 screen is 26/85 paragraphs (30.59%) with all
seven major sections represented.  The E6 schema-valid empty state is
`skipped_no_revision_evidence`, because no ARS Revision-Evidence Bundle is in
scope; its SHA-256 is
`9bfee5c9683555f28d67575074e3fd2bfebf26fb27fa278a7bcf60cb7c7a33e1`.
The seven-mode disposition records seven `CLEAR`, zero `SUSPECTED`, and zero
`INSUFFICIENT EVIDENCE`; Mode 7 is bounded to the checked alternate-term and
owner-integration frame-lock mechanism, not global literature completeness.
The self-contained report
is `stage2_5/POST_CORRECTION_INTEGRITY_DISPOSITION.md`, SHA-256
`7d8d924be13ffa0cdd0aded72f0fbe35a7548460f50d1a522b39da257fa32e29`.

No manuscript or PDF changed in this strict sidecar closure.  Canonical
`main.pdf` remains 11 A4 pages, 408,243 bytes, SHA-256
`ed2ffeedc97cc82d006bf540468ef7bf9c1655cad3f4600fb393f8d6451fc7da`;
the compile log and deterministic control remain clean.  The artifact gate is
**PASS_WITH_NOTES**, while specialist clearance, human declarations, priority
clearance, and external release remain **HOLD**.
