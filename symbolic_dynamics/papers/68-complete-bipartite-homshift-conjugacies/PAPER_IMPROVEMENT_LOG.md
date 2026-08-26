# Paper improvement log

External release remains **HOLD**.  No review or revision in this log is a
priority or submission-readiness certificate.

## Supplemental cross-agent track (scored)

| Round | Provenance | Score/verdict | Main outcome | Frozen PDF |
|---|---|---|---|---|
| 0 | author package | baseline | Original 7-page draft; false disconnected-shape formula present | `main_round0_original.pdf` |
| 1 | independent cross-agent hostile review; GPT-5.4 child unavailable at thread cap | 4.5/10, major revision | Global-phase formula/control corrected; dimer memory and Gibbs equality clarified | `main_round1.pdf` |
| 2 | independent cross-agent proof audit; requested GPT-5.4 child unavailable due agent thread cap | 9.1/10, internal theorem pass | Full dependency trace passed; no further manuscript edit required | `main_round2.pdf` |

- Raw reviews: `reviews/ROUND1_HOSTILE_REVIEW.md` and
  `reviews/ROUND2_PROOF_AUDIT.md`.
- Detailed resolutions: `rounds/ROUND1_RESOLUTION.md` and
  `rounds/ROUND2_RESOLUTION.md`.
- Pre-loop internal artifacts are preserved under `reviews/PRELOOP_*` and
  `rounds/PRELOOP_*`.

The 4.5/10 and 9.1/10 values belong only to this supplemental track.

## Official GPT-5.4 XHigh track (unscored)

| Round | Verdict | Source change | Review | Resolution |
|---|---|---:|---|---|
| 1 | mathematics PASS | 0 | `reviews/GPT54_XHIGH_ROUND1_HOSTILE_REVIEW.md` | `rounds/GPT54_XHIGH_ROUND1_RESOLUTION.md` |
| 2 | mathematics PASS | 0 | `reviews/GPT54_XHIGH_ROUND2_PROOF_AUDIT.md` | `rounds/GPT54_XHIGH_ROUND2_RESOLUTION.md` |

No numerical score was supplied for either official round, and none is
inferred from the supplemental reviews.  Round 2 independently reconstructed
the checkerboard phase/count, product-conjugacy, finite-dependence subgroup,
pressure/equilibrium, and periodic-data theorem chains and affirmed the
Round-1 no-change disposition.

## Canonical artifact and verification

At the official Round-2 freeze, `main_round1.pdf`, `main_round2.pdf`,
`main_pre_gpt54_round1.pdf`, `main_gpt54_round1.pdf`, and
`main_gpt54_round2.pdf` were byte-identical. Their preserved historical
SHA-256 is
`b96ac6118ad81839eb796ad5640357ce710ff9e1372411bfa7931883dd3ac7c6`.
The later Stage 2.5 bibliography-title correction intentionally changed only
the current canonical `main.pdf`; it is 7 pages, 348079 bytes, SHA-256
`9527da716429ba4644271086dee8eebdd5a1c201a73cb2a0a39046cc957de61a`.
Historical review PDFs were not overwritten.

Official GPT-5.4 XHigh rounds completed: **2**.  Mathematics: **PASS**.
Package integrity: **PASS**.  The deterministic control, clean reproducible
build, log/citation/font/text/visual checks, alias comparisons, and checksum
manifest all pass.  No manuscript source changed in official Round 2.

## Stage 2.5 correction and strict ARS 0.1.27 closure

The bibliography correction and deterministic rebuild are recorded in
`stage2_5/CORRECTION_ROUND_1.md`. The self-contained strict disposition is
`stage2_5/POST_CORRECTION_INTEGRITY_DISPOSITION.md`.

- current references/contexts: 4/4 and 10/10 verified;
- Phase E: 23 selected claims, 23 exact tuple rows, 3 cited-source excerpts,
  20 anchorless no-reference rows, zero tuple mismatches, runtime replay PASS;
- Phase D1: 18/58 current blocks (31.03%);
- seven-mode integrity result: all `CLEAR`;
- disposition: `PASS_WITH_NOTES` for internal integrity.

Actual author identities/roles and funding, COI, and AI-assistance disclosures
remain unresolved. The specialist exact-neighbor/source gate remains pending.
External release remains **HOLD**.
