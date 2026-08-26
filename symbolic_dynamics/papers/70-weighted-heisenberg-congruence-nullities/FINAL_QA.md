# P70 final quality-assurance report

**Manuscript:** *Weighted Three-Term Shifts on Finite Heisenberg Quotients*  
**Freeze date:** 2026-08-25 UTC  
**Official mathematical verdict:** **PASS AS STATED**  
**Official package verdict:** **PASS**  
**Review stage:** **two official rounds complete; Stage 2.5 source gate pending**  
**External-release verdict:** **HOLD -- specialist source audit required**

## Review provenance

- The earlier two-round audit is an independent cross-agent track and is
  labelled as such in its raw reviews and resolutions.
- `reviews/GPT54_XHIGH_ROUND1_HOSTILE_REVIEW.md` is the distinct official
  GPT-5.4/xhigh review. It found no CRITICAL or MAJOR theorem defect and one
  MINOR control-coverage overclaim; that issue is resolved in
  `rounds/GPT54_XHIGH_ROUND1_RESOLUTION.md`.
- `reviews/GPT54_XHIGH_ROUND2_PROOF_AUDIT.md` is the official follow-up. It
  found no CRITICAL, MAJOR, or MINOR issue, passed the Round-1 fixes, hidden-
  hypothesis audit, and stale-artifact audit, and requested no manuscript
  change. Its disposition is recorded in
  `rounds/GPT54_XHIGH_ROUND2_RESOLUTION.md`.
- Neither official review supplied a numeric score.

## Mathematical gate

- The left-coset/right-translation convention is computed on matrix
  coefficients, producing exactly the displayed blocks without an implicit
  transpose, inverse, or dual.
- All irreducible modules over the algebraic closure of the ground field are
  constructed, proved irreducible and inequivalent, and exhausted by the
  squared-degree sum.
- The character gcd term, clock--shift determinant, exact zero/one nonlinear
  nullity, regular multiplicities, and descent of nullity were retraced.
- The earlier cross-agent Round 2 found no CRITICAL or MAJOR issue. Its sole
  MINOR was implemented:
  `(Vx)_j=x_{j-1}` now makes the cyclic recurrence exact.
- The official Round-1 revision changes no proof step: hashes of Sections
  2--5 remain identical to the pre-review manifest.
- Official Round 2 independently reconstructed every theorem dependency and
  returned mathematical `PASS AS STATED` and package `PASS`. No source file
  in the manuscript or proof package changed after that audit.

## Owner-subtraction gate

- The complex/unitary scope of the cited Stone--von Neumann source is stated;
  cross-characteristic completeness is proved locally.
- Abelian/resultant and integer `1+a+b` precedents are attributed only at
  their actual scope. The bounded search is not a priority certificate.

## Control gate

`python3 code/verify_weighted_heisenberg.py` terminates with
`ALL WEIGHTED HEISENBERG CONTROLS PASS`. Ten full quotient matrices and four
direct clock--shift blocks check both Fermat strata. Script SHA-256:
`a476ddddca2d9373c1412039e86dac64457354740e530ff3e20ab7ade4e5b1e1`.
The direct blocks test the determinant and zero/one-nullity lemmas; the full
matrices exercise the displayed group law, selected finite operator, final
nullity, and regular multiplicity on sample tuples. Total-nullity comparison
alone does not distinguish right translation from the dual left convention;
that convention is settled analytically in Remark 3.4.
Fresh control stdout matches `code/verification_output.txt` line-for-line.

## Compilation and visual gate

- Clean deterministic build: exactly three `pdflatex` runs total
  (`pdflatex -> bibtex -> pdflatex -> pdflatex`); every exit was zero.
- Final PDF: 7 A4 pages, 317,844 bytes, 3,244 extracted words.
- Log scan: zero undefined citations/references, multiply-defined labels,
  package warnings, overfull boxes, and underfull boxes.
- Every listed font is embedded and subset; PDF Author metadata is empty.
- Visual inspection: pages 1, 4, 5, 6, and 7; introduction, character and
  nonlinear proofs, revised control limitation, tables, scope statement,
  conclusion, and references are legible and unclipped.
- Final PDF SHA-256:
  `e20e1151597684736d72deeac8875d4be0e5e95d95ef2c187468d07f734f3ac5`.
- Preserved pre-official-review PDF:
  `main_pre_gpt54_round1.pdf`,
  SHA-256 `60594bc494ccede978caedbfa82f13e73f1daa78ff33bf6d8edd5071b2e37442`.
- Official Round-1 freeze: `main_gpt54_round1.pdf`, byte-identical to
  `main.pdf`.
- Official Round-2 freeze: `main_gpt54_round2.pdf`, also byte-identical to
  `main.pdf`. Equality of the two official hashes is expected because Round 2
  requested no manuscript change.

## Remaining gate

The two-round official mathematical/package audit is complete. Stage 2.5
remains pending only because the source search is bounded rather than a
worldwide exact-statement audit. No priority claim is authorized.

## Stage 2.5 correction overlay — 2026-08-26

The artifact identities above are historical pre-Stage-2.5 snapshots. The
corrected current `main.pdf` is 7 A4 pages, 345,028 bytes, SHA-256
`61398af7a4ab61ea3ace029ec315721d4a855bf8f60986c84b2fdc94d9bd0142`.
All seven bibliography records and fourteen citation contexts close with zero
ghost/dangling keys; the final log is clean, all fonts are embedded/subset,
and the deterministic control remains byte-identical to its receipt. The
direct finite-Heisenberg owner subtraction is recorded in
`stage2_5/CORRECTION_ROUND_1.md`.

Author-side Stage 2.5 content status is **PASS_WITH_NOTES after correction
round 1**. Residual collision risk is **MEDIUM-HIGH** under the bounded search;
priority and specialist clearance are not granted. External release remains
**HOLD**.

## Strict ARS 0.1.27 post-correction closure — 2026-08-26

The current 35-claim registry selects 30 claims and expands to 34 strict
`evidence-row/1.0` tuples in exact registry/ref order: 13 source-bound exact
excerpt rows and 21 explicit anchorless empty-state rows.  The ARS builder and
source-map validator pass all 34 rows; the independent tuple-order replay also
passes.  Evidence rows, source map, and source manifest have SHA-256 values
`1cb809cd125ffc5f6be47248dab1f23a5113d173eb9a94d53754baf40a1680fd`,
`a2deaaf2f8819af4e6d54309c7659569cf634fd957d7fe8784d8d63346465fa2`,
and `14f9c903f12486141ccd27166f7c5a5308f46c80579bc8d891db448edbaaccec`.

The corrected-manuscript D1 screen is 14/46 paragraphs (30.43%) with all
eight major sections represented.  The E6 schema-valid empty state is
`skipped_no_revision_evidence`, because no ARS Revision-Evidence Bundle is in
scope; its SHA-256 is
`d7383f574fd4e30ad6eb44e56ec95aea1b51149063451cf083cbc7bd13affa69`.
The seven-mode disposition records seven `CLEAR`, zero `SUSPECTED`, and zero
`INSUFFICIENT EVIDENCE`; Mode 7 is bounded to the checked alternate-term and
owner-integration frame-lock mechanism, not global literature completeness.
The self-contained report
is `stage2_5/POST_CORRECTION_INTEGRITY_DISPOSITION.md`, SHA-256
`894a83176afc14769a73357ca55d76fb32b778b8e374e9689a9a702f91f4d370`.

No manuscript or PDF changed in this strict sidecar closure.  Canonical
`main.pdf` remains 7 A4 pages, 345,028 bytes, SHA-256
`61398af7a4ab61ea3ace029ec315721d4a855bf8f60986c84b2fdc94d9bd0142`;
the compile log and deterministic control remain clean.  The artifact gate is
**PASS_WITH_NOTES**, while specialist clearance, human declarations, priority
clearance, and external release remain **HOLD**.
