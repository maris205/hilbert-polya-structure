# P68 final quality-assurance report

**Manuscript:** *Product Classification and Phase Rigidity for Complete-Bipartite Hom-Shifts*  
**Package QA through:** 2026-08-26 UTC  
**Official GPT-5.4 XHigh mathematics:** **PASS**  
**Package integrity:** **PASS**  
**External-release verdict:** **HOLD -- specialist source gate, unresolved declarations, and release authorization pending**

## Review-track provenance

- Supplemental cross-agent track: two rounds, scored 4.5/10 and 9.1/10.
  Those scores belong only to `reviews/ROUND1_HOSTILE_REVIEW.md` and
  `reviews/ROUND2_PROOF_AUDIT.md` and their resolutions.
- Official `gpt-5.4 xhigh` track: two rounds, both unscored.  Round 1 returned
  PASS/no source change; Round 2 independently returned mathematics PASS/no
  source change.
- No score from the supplemental track is attributed to the official track.
- Pre-loop, supplemental, and official artifacts remain separately named and
  preserved.

## Mathematical gate

- A single global checkerboard phase controls every globally extendible finite
  pattern, with the empty shape handled separately: PASS.
- The radius-one product-conjugacy code and inverse use symbol-detected anchors
  and commute with odd and even translations in every `d>=1`: PASS.
- Entropy necessity, degenerate part sizes, finite-dependence rigidity,
  subgroup sufficiency, pressure/equilibrium equality cases, and finite-index
  periodic counts: PASS.
- Open critical, major, or minor official-review issues: 0.

## Owner-subtraction gate

- The public checkerboard-phase/MME background remains attributed to
  Chandgotia's lecture notes.
- The Chandgotia--Thorat four-cycle-free obstruction retains its exact
  hypothesis; complete bipartite graphs with both parts nontrivial lie outside
  that hypothesis.
- The one-sided Hom-shift category remains excluded.
- The bounded source search is not represented as a priority or
  worldwide-novelty certificate.

## Control gate

`python3 code/verify_complete_bipartite.py` terminates with `ALL CHECKS PASS`.
Its live output is byte-identical to `code/verify_complete_bipartite.out`.
Script SHA-256:
`42c3e23e2cfd27618ccca28155be4f854010a05850fc7c1af2b1b8fe96aac8bd`;
output SHA-256:
`918c56ef57b9c09ce27872e58a3e76667766351378e40b5d450d9cbced2a0bbf`.
The finite enumerations are regression evidence, not proof premises.

## Compilation and visual gate

- Authoritative build: three total `pdflatex` runs---one initial run, BibTeX,
  then two further `pdflatex` runs.
- Clean build reproduced the canonical PDF byte-for-byte.
- The third run produced the canonical PDF and a stable AUX file.  One extra
  no-op diagnostic pass left both byte-identical and cleared TeX's conservative
  label-rerun advisory; it is not part of the authoritative three-run recipe.
- Log scan: zero undefined citations/references, rerun requests,
  multiply-defined labels, package/LaTeX warnings, overfull boxes, underfull
  boxes, or badness warnings.
- Official Round-2 frozen PDF: 7 A4 pages, 348,062 bytes, 3,509 extracted words.
- Fonts: 24 records; every font is embedded, subset, and Unicode-mapped.
- PDF title and author metadata are empty; creation/modification dates are
  omitted.
- All 7 official Round-2 frozen pages were visually inspected.  The abstract,
  global-phase count, dimer classification, finite-dependence theorem,
  pressure/equilibrium proof, periodic formula, scope, conclusion, and
  references are legible and unclipped.

## Frozen artifact identities

- Original baseline `main_round0_original.pdf`:
  `e072cc764f80e28accb3a3a586246a6e82219e1e3bf9f7f1ec494221dbe84479`.
- At the official Round-2 freeze, canonical `main.pdf`, supplemental
  `main_round1.pdf` and `main_round2.pdf`, official pre-Round-1/Round-1
  snapshots, and `main_gpt54_round2.pdf`:
  `b96ac6118ad81839eb796ad5640357ce710ff9e1372411bfa7931883dd3ac7c6`.

The byte equality of the canonical aliases does not merge their review
provenance or import the supplemental 9.1/10 score into the official track.

## Remaining release gate

Equivalent formulations may occur under hom-shift, graph-homomorphism,
checkerboard-code, one-sided, finite-dependence, or pressure terminology.
Strict ARS 0.1.27 Stage 2.5 integrity closure is complete with notes. The
specialist exact-neighbor/source gate remains pending, and actual author
identities/roles plus funding, COI, and AI-assistance disclosures remain
unresolved. External release is therefore **HOLD**; neither priority nor
specialist clearance is claimed.

## Stage 2.5 correction overlay — 2026-08-26

The frozen identities above are historical pre-Stage-2.5 snapshots. The
corrected current `main.pdf` is 7 A4 pages, 348,079 bytes, SHA-256
`9527da716429ba4644271086dee8eebdd5a1c201a73cb2a0a39046cc957de61a`.
All four bibliography records and ten citation contexts close with zero
ghost/dangling keys; the final log is clean, all fonts are embedded/subset,
and the deterministic output remains byte-identical to its receipt.

Author-side Stage 2.5 content status is **PASS_WITH_NOTES after correction
round 1**. The residual collision risk is **MEDIUM** under the bounded search;
priority and specialist clearance are not granted. External release remains
**HOLD**.

## Strict ARS 0.1.27 closure overlay — 2026-08-26

- Self-contained disposition:
  `stage2_5/POST_CORRECTION_INTEGRITY_DISPOSITION.md`.
- Active batch passport/declaration pointer:
  `docs/papers67_71_sequence/stage2_5/MATERIAL_PASSPORT.yaml`.
- Current source/context coverage: 4/4 bibliography records and 10/10 citation
  contexts; ghost and dangling counts are zero.
- Phase E: 23 selected claims and 23 exact tuple rows. Three rows bind
  session-held cited-source excerpts; twenty are explicit anchorless
  empty-state rows for no-reference claims. Full tuple join and ARS runtime
  replay pass with zero mismatches. No row uses the manuscript as its cited
  source.
- Phase D1: 18/58 current paragraph-like blocks (31.03%), including the
  abstract and every major section. This remains a bounded overlap heuristic.
- E6: exact-schema sidecar status `skipped_no_revision_evidence`; no Revision-
  Evidence Bundle was supplied, so no stronger drift claim is made.
- Seven-mode integrity disposition: all seven modes `CLEAR`. Human declarations
  and the specialist source gate remain separate release conditions.

Internal integrity disposition is **PASS_WITH_NOTES**. External release remains
**HOLD**.
