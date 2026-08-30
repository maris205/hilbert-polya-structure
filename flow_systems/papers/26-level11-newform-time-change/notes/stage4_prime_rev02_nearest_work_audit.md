# P26 Stage 4′ REV-02 nearest-work audit

## Scope and bindings

- Roadmap item: `REV-02` (`must_fix`).
- Current base draft: `notes/stage4_revision_round1.tex`, SHA-256 `dea8f3af92bde625008f2987922b3b69d2856abe3b796fdd2af319bf6db3bf37`.
- Stage-4′ roadmap: `notes/stage4_prime_revision_roadmap.json`, SHA-256 `65590089ab2eca9b227047620a484c2fbc70a56c8b9b50d8c00aea404f236f1f`.
- Exact authorization request (resolved from this sidecar): `../../../BATCH_ROUND9_STAGE4_PRIME_AUTHORIZATION_REQUEST.md`, SHA-256 `d2e94cd10b1ca12204c8747b5bc0895f6c642e3a3ff7c08194016ed62fd461ec`.
- Unified author event (resolved from this sidecar): `../../../BATCH_ROUND9_STAGE4_PRIME_AND_P25_AUTHOR_EVENT_20260830.txt`, SHA-256 `fc4de4ab870bcb6ff3f1c0c9fc6eb9f389edbfbb2d6b01a79a063d21f80365dd`.
- Fresh check date: 2026-08-30 UTC.

This is a bounded nearest-work comparison, not a systematic review or a global priority certificate.

## Verified sources

### Katok (1985)

Svetlana Katok, “Closed Geodesics, Periods and Arithmetic of Modular Forms,” *Inventiones Mathematicae* 80 (1985), 469--480, DOI `10.1007/BF01388727`.

The Springer record verifies the author, title, journal, volume, pages, and publication year. Constantinescu and Nordentoft identify Katok as an early general nonvanishing antecedent for periods of holomorphic automorphic forms over closed geodesics. This is a nearest antecedent for the manuscript's geodesic-period object. It does not formulate the manuscript's Hecke cycle-pushforward owner decomposition, distinguish branch-cycle degree from formal product repetition, or provide the registered finite quadratic-moment obstruction.

Primary records:

- `https://link.springer.com/article/10.1007/BF01388727`
- `https://doi.org/10.1007/BF01388727`

### Constantinescu and Nordentoft (2025)

Petru Constantinescu and Asbjørn Christian Nordentoft, “Non-vanishing of Geodesic Periods of Automorphic Forms,” *Geometric and Functional Analysis* 35 (2025), 1108--1146, DOI `10.1007/s00039-025-00715-z`.

The open Springer article studies arithmetic statistics and nonvanishing of geodesic periods for primitive closed geodesics. Its main results include asymptotic nonvanishing statements for Hecke--Maaß forms and corresponding results for holomorphic forms on finite-covolume Fuchsian groups with a cusp. The owner is a primitive closed geodesic ordered by length, not the manuscript's frozen correspondence-component multiset. The article does not supply the manuscript's finite Hecke-output taxonomy, declared multiplicity convention, degree-wise quadratic moment test, or target-blind matched-control decomposition.

Primary record:

- `https://link.springer.com/article/10.1007/s00039-025-00715-z`

## Exact contribution boundary

The two sources close the missing modern period-literature layer without supporting a priority claim. The safe manuscript comparison is:

1. Katok and Constantinescu--Nordentoft study existence, prevalence, or distributional nonvanishing of closed-geodesic periods.
2. The current paper instead asks whether a Hecke eigenperiod relation descends to scalar primitive-Euler recurrences on one frozen finite correspondence-component multiset.
3. Neither nearest work supplies the paper's owner decomposition, branch-degree/repetition separation, `2/2/134` finite taxonomy, `51/55` failures, or matched exact control audit.
4. The result remains finite and non-global: no complete primitive-owner census, determinant, global priority, A2 promotion, or Route-B claim follows.

## Exact append-only bibliography audit

The two appended records in `paper/references.bib` were compared field by field with the authorization request. `Katok1985` contains exactly `author`, `title`, `journal`, `year`, `volume`, `number`, `pages`, and `doi`, with `number = {3}`. `ConstantinescuNordentoft2025` contains exactly `author`, `title`, `journal`, `year`, `volume`, `pages`, and `doi`. No third entry and no edit to an existing entry is included in this Stage-4′ bibliography scope.

## Verdict

`SUPPORTED_WITH_BOUNDED_SCOPE`. Both bibliography entries are verified for existence and metadata, and the comparison is source-aligned. This audit does not establish exhaustive contemporary coverage.
