# Paper improvement log

External release remains **HOLD**.  No review or revision in this log is a
priority or submission-readiness certificate.

## Supplemental cross-agent track (scored)

| Round | Provenance | Score/verdict | Main outcome | Frozen PDF |
|---|---|---|---|---|
| 0 | author package | baseline | Original 8-page draft | `main_round0_original.pdf` |
| 1 | independent cross-agent hostile review; GPT-5.4 child unavailable at thread cap | 7.0/10, major revision | Bowen proof upgraded to exact cylinder/Carathéodory/local-entropy argument; natural-extension and periodic indices closed | `main_round1.pdf` |
| 2 | independent cross-agent proof audit; requested GPT-5.4 child unavailable due agent thread cap | 9.0/10, internal theorem pass | Defined the diagonal metric value and named the Bernoulli lower-bound measure | `main_round2.pdf` |

- Raw reviews: `reviews/ROUND1_HOSTILE_REVIEW.md` and
  `reviews/ROUND2_PROOF_AUDIT.md`.
- Detailed resolutions: `rounds/ROUND1_RESOLUTION.md` and
  `rounds/ROUND2_RESOLUTION.md`.
- Pre-loop internal artifacts are preserved under `reviews/PRELOOP_*` and
  `rounds/PRELOOP_*`.

The 7.0/10 and 9.0/10 values belong only to this supplemental track.

## Official GPT-5.4 XHigh track (unscored)

| Round | Verdict | Source change | Review | Resolution |
|---|---|---:|---|---|
| 1 | mathematics PASS | 0 | `reviews/GPT54_XHIGH_ROUND1_HOSTILE_REVIEW.md` | `rounds/GPT54_XHIGH_ROUND1_RESOLUTION.md` |
| 2 | mathematics PASS | 0 | `reviews/GPT54_XHIGH_ROUND2_PROOF_AUDIT.md` | `rounds/GPT54_XHIGH_ROUND2_RESOLUTION.md` |

No numerical score was supplied for either official round, and none is
inferred from the supplemental reviews.  Round 2 independently reconstructed
the pressure, equilibrium, natural-extension, periodic/zeta, profile-rigidity,
and Bowen-spectrum theorem chains and affirmed the Round-1 no-change
disposition.

## Canonical artifact and verification

At the official Round-2 freeze, `main_pre_gpt54_round1.pdf`,
`main_gpt54_round1.pdf`, `main_gpt54_round2.pdf`, and the supplemental
`main_round2.pdf` were byte-identical. Their preserved historical SHA-256 is
`ff85975c69b7848ff8675edde2e753ed9deb6cd377f37aeeb60669d403026bcf`.
The later Stage 2.5 bibliography and source-boundary corrections intentionally
changed only the current canonical `main.pdf`; it is 9 pages, 409426 bytes,
SHA-256
`971b33083dc14ceb99831f94786167c1186bf9b8365557472fb2a9f493174a9e`.
Historical review PDFs were not overwritten.

Official GPT-5.4 XHigh rounds completed: **2**.  Mathematics: **PASS**.
Package integrity: **PASS**.  The deterministic control, clean reproducible
build, log/citation/font/text/visual checks, alias comparisons, and checksum
manifest all pass.  No manuscript source changed in official Round 2.

## Stage 2.5 correction and strict ARS 0.1.27 closure

The bibliography/source-boundary corrections and deterministic rebuild are
recorded in `stage2_5/CORRECTION_ROUND_1.md`. The self-contained strict
disposition is `stage2_5/POST_CORRECTION_INTEGRITY_DISPOSITION.md`.

- current references/contexts: 9/9 and 19/19 verified;
- Phase E: 29 selected claims, 31 exact tuple rows, 8 cited-source excerpts,
  23 anchorless no-reference rows, zero tuple mismatches, runtime replay PASS;
- Phase D1: 22/70 current blocks (31.43%);
- seven-mode integrity result: all `CLEAR`;
- disposition: `PASS_WITH_NOTES` for internal integrity.

The pressure portion retains `HIGH` collision risk because the official UFV
project page exposes an overlapping objective but no theorem text. Actual
author identities/roles and funding, COI, and AI-assistance disclosures remain
unresolved. The specialist exact-neighbor/source gate remains pending.
External release remains **HOLD**.
