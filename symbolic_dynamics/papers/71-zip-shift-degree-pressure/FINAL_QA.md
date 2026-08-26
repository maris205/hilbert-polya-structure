# P71 final quality-assurance report

**Manuscript:** *Degree Pressure, Multifractal Fibres, and Profile Rigidity for Full Zip Shifts*  
**Package QA through:** 2026-08-26 UTC  
**Official GPT-5.4 XHigh mathematics:** **PASS**  
**Package integrity:** **PASS**  
**External-release verdict:** **HOLD -- specialist source gate, unresolved declarations, and release authorization pending**

## Review-track provenance

- Supplemental cross-agent track: two rounds, scored 7.0/10 and 9.0/10.
  Those scores belong only to `reviews/ROUND1_HOSTILE_REVIEW.md` and
  `reviews/ROUND2_PROOF_AUDIT.md` and their resolutions.
- Official `gpt-5.4 xhigh` track: two rounds, both unscored.  Round 1 returned
  PASS/no source change; Round 2 independently returned mathematics PASS/no
  source change.
- No score from the supplemental track is attributed to the official track.
- Pre-loop, supplemental, and official artifacts remain separately named and
  preserved.

## Mathematical gate

- Local-degree indexing, inverse branches, explicit natural extension,
  invariant lift, and entropy preservation: PASS.
- Pressure/equilibrium equality cases, derivative identities, periodic
  alignment, zeta identity, and coefficient-sensitive profile recovery: PASS.
- The multifractal upper bound uses variable-length
  Carathéodory--Bowen covers; the exact Bowen-cylinder identity and Bernoulli
  local-entropy lower bound close both directions: PASS.
- Endpoint values, Legendre duality, profile-conjugacy equivalence, and the
  uniform-profile boundary: PASS.
- Open critical, major, or minor official-review issues: 0.

## Owner-subtraction gate

- Lamei--Mehdipour retain ownership of the zip-map/formal-system setting.
- Martins--Mattos--Varão retain ownership of the metric/folding-entropy
  formulae used in the pressure bridge.
- Mehdipour--Jangjooye Shaldehi retain ownership of the uniform full-zip
  boundary case.
- The active-neighbour audit is bounded and non-certifying; no priority or
  worldwide-novelty claim is made.

## Control gate

`python3 code/verify_degree_pressure.py` terminates with `ALL CHECKS PASS`.
Its live output is byte-identical to `code/verify_degree_pressure.out`.
Script SHA-256:
`6de6496c78ca610d955f7b6a4aa08d31f162b0c7ad3bfcbaf80bcb787119aab2`;
output SHA-256:
`4ade498585b0750acea4b487dec11b7c19b2e322f8a5ef1d4262d6c4f39f2aba`.
These finite computations are regression evidence, not proof premises.

## Compilation and visual gate

- Authoritative build: three total `pdflatex` runs---one initial run, BibTeX,
  then two further `pdflatex` runs.
- Clean build reproduced the canonical PDF byte-for-byte.
- Log scan: zero undefined citations/references, rerun requests,
  multiply-defined labels, package/LaTeX warnings, overfull boxes, underfull
  boxes, or badness warnings.
- Official Round-2 frozen PDF: 9 A4 pages, 405,962 bytes, 4,291 extracted words.
- Fonts: 28 records; every font is embedded, subset, and Unicode-mapped.
- PDF title and author metadata are empty; creation/modification dates are
  omitted.
- All 9 official Round-2 frozen pages were visually inspected.  The abstract, model,
  pressure theorem, periodic/profile theorem, metric convention, spectrum
  proof, examples, scope, conclusion, and references are legible and
  unclipped.

## Frozen artifact identities

- Original baseline `main_round0_original.pdf`:
  `7f51cb14af412305849f1929f0a4bfec0c7a72a48fbd5082b4d7429446b939b2`.
- Supplemental cross-agent Round 1 `main_round1.pdf`:
  `2610aac081aba4ff9032f66a6e821a819b004f04503545ad748742b72b3b6c64`.
- At the official Round-2 freeze, canonical `main.pdf`, supplemental
  `main_round2.pdf`, official pre-Round-1/Round-1 snapshots, and
  `main_gpt54_round2.pdf`:
  `ff85975c69b7848ff8675edde2e753ed9deb6cd377f37aeeb60669d403026bcf`.

The byte equality of the canonical aliases does not merge their review
provenance or import the supplemental 9.0/10 score into the official track.

## Remaining release gate

Equivalent or overlapping formulations may exist in current or in-press
extended-shift/zip-shift thermodynamic work. Strict ARS 0.1.27 Stage 2.5
integrity closure is complete with notes. The specialist exact-neighbor/source
gate remains pending, and actual author identities/roles plus funding, COI,
and AI-assistance disclosures remain unresolved. External release is therefore
**HOLD**; neither priority nor specialist clearance is claimed.

## Stage 2.5 correction overlay — 2026-08-26

The frozen identities above are historical pre-Stage-2.5 snapshots. The
corrected current `main.pdf` is 9 A4 pages, 409,426 bytes, SHA-256
`971b33083dc14ceb99831f94786167c1186bf9b8365557472fb2a9f493174a9e`.
All nine bibliography records and nineteen citation contexts close with zero
ghost/dangling keys; the final log is clean, all fonts are embedded/subset,
and the deterministic output remains byte-identical to its receipt.

Author-side Stage 2.5 content status is **PASS_WITH_NOTES after correction
round 1**. The pressure portion retains **HIGH** collision risk because the
public project page exposes an overlapping objective but no theorem text;
priority and specialist clearance are not granted. External release remains
**HOLD**.

## Strict ARS 0.1.27 closure overlay — 2026-08-26

- Self-contained disposition:
  `stage2_5/POST_CORRECTION_INTEGRITY_DISPOSITION.md`.
- Active batch passport/declaration pointer:
  `docs/papers67_71_sequence/stage2_5/MATERIAL_PASSPORT.yaml`.
- Current source/context coverage: 9/9 bibliography records and 19/19 citation
  contexts; ghost and dangling counts are zero.
- Phase E: 29 selected claims expand to 31 exact claim/ref tuple rows. Eight
  rows bind session-held cited-source excerpts; twenty-three are explicit
  anchorless empty-state rows for no-reference claims. Full tuple join and ARS
  runtime replay pass with zero mismatches. No row uses the manuscript as its
  cited source.
- Phase D1: 22/70 current paragraph-like blocks (31.43%), including the
  abstract and every major section. This remains a bounded overlap heuristic.
- E6: exact-schema sidecar status `skipped_no_revision_evidence`; no Revision-
  Evidence Bundle was supplied, so no stronger drift claim is made.
- Seven-mode integrity disposition: all seven modes `CLEAR`. The `HIGH`
  pressure-collision risk, human declarations, and specialist source gate
  remain separate release conditions.

Internal integrity disposition is **PASS_WITH_NOTES**. External release remains
**HOLD**.
