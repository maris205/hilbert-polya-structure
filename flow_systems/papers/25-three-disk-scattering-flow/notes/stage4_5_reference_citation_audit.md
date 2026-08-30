# Paper 25 Stage 4.5 Fresh Reference and Citation Audit

## Scope and bindings

- Mode: Stage 4.5 fresh Phase A/B audit only.
- Draft: `notes/stage4_revision_round1.tex`.
- Draft SHA-256: `39a643c05b4820b782e45a5ec240caa7223ad444229e8a89bdcc98791ce23835`.
- Bibliography: `paper/references.bib`.
- Bibliography SHA-256: `de776cc0bf16e6c837917f4a289f8c07b8b4f7e9146183b9a9e0e6294db99e6`.
- Source snapshot: `notes/stage4_5_reference_source_snapshot.json`.
- Captured at: `2026-08-30T12:21:18Z`.
- This is not the global Stage 4.5 verdict. Phases C--E and the seven-mode failure checklist are outside this artifact.

## Denominators

| Population | Checked | Result |
|---|---:|---|
| Registered references | 8/8 | 8 existence VERIFIED; 0 NOT_FOUND; 0 DOI misdirection |
| Registered citation commands | 13/13 | 13 supported; 0 distorted; 0 unverifiable |
| Reference-list entries cited in the manuscript | 8/8 | 0 orphan references |
| Citation keys resolved in the bibliography | 13/13 commands | 0 dangling citations |

## Phase A: fresh reference verification

All eight entries were checked from fresh DOI metadata and an official publisher, society, repository, or author-hosted primary record. Reverse Crossref `filter=updates:<doi>` queries were run separately because a work object's forward relation can omit a publisher correction.

| Key | Primary record | Existence and metadata | Current update observation |
|---|---|---|---|
| `GaspardRice1989Semiclassical` | [DOI](https://doi.org/10.1063/1.456018) | VERIFIED: Gaspard and Rice; JCP 90(4), 2242--2254 (1989) | Publisher correction [`10.1063/1.457672`](https://doi.org/10.1063/1.457672), JCP 91(5), 3279 |
| `GaspardRice1989Exact` | [DOI](https://doi.org/10.1063/1.456019) | VERIFIED: Gaspard and Rice; JCP 90(4), 2255--2262 (1989) | Publisher correction [`10.1063/1.457670`](https://doi.org/10.1063/1.457670), JCP 91(5), 3280 |
| `Wirzba1999` | [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0370157398000362) | VERIFIED: Physics Reports 309(1--2), 1--116 (1999) | No update record found in the named query |
| `Ikawa1988` | [Centre Mersenne](https://aif.centre-mersenne.org/articles/10.5802/aif.1137/) | VERIFIED: Annales de l'Institut Fourier 38(2), 113--146 (1988) | No update record found in the named query |
| `BowenLanford1970` | [AMS volume record](https://bookstore.ams.org/PSPUM/14) | VERIFIED: R. Bowen and O. E. Lanford III; PSPUM 14, 43--49 (1970) | No update record found in the named query |
| `Ruelle1976` | [Springer](https://link.springer.com/article/10.1007/BF01403069) | VERIFIED with MINOR precision note: publisher/Crossref record includes issue 3 | No update record found in the named query |
| `CvitanovicEckhardt1989` | [APS](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.63.823) | VERIFIED: PRL 63(8), 823--826 (1989) | No update record found in the named query |
| `Livsic1972` | [MathNet/Steklov](https://www.mathnet.ru/eng/im2373) | VERIFIED with MINOR precision note: authoritative record exposes `A. N.`, not the expanded given name | No update record found in the named query |

The six zero-result update queries are observations over the named Crossref/publisher sources, not evidence that no update could exist anywhere.

## Correction-impact check for the two Gaspard--Rice sources

### `10.1063/1.456018`

The correction at [`10.1063/1.457672`](https://doi.org/10.1063/1.457672) changes Equations (4.15) and (4.22) and one sentence on page 2254. The manuscript's only context, line 73, makes the broad claim that periodic-orbit and semiclassical constructions organize resonances of the chaotic repellor. It does not reproduce the corrected formulas or depend on the corrected sentence. The context remains supported.

### `10.1063/1.456019`

The correction at [`10.1063/1.457670`](https://doi.org/10.1063/1.457670) changes Equation (5.4), several Appendix equations or symbols, and typographical omissions. The manuscript's contexts at lines 75 and 160 rely on the abstract-level multiple-scattering matrix, determinant, and resonance characterization. They do not reproduce a corrected formula. Both contexts remain supported.

Neither corrected paper has a retraction, expression-of-concern, or reinstatement record in the fresh named queries.

## Phase B: 100% citation-context verification

| Context ID | Draft line | Citation key | Manuscript use | Verdict |
|---|---:|---|---|---|
| P25-B-001 | 71 | `Ikawa1988` | Periodic rays and Poincare maps in exterior-wave decay analysis | SUPPORTED |
| P25-B-002 | 73 | `GaspardRice1989Semiclassical` | Periodic-orbit semiclassical organization of three-disk resonances | SUPPORTED; correction does not alter this claim |
| P25-B-003 | 75 | `GaspardRice1989Exact` | Exact scattering uses a multiple-scattering matrix/determinant rather than the manuscript's symbolic adjacency determinant | SUPPORTED; correction does not alter this claim |
| P25-B-004 | 132 | `Livsic1972` | Constant-cohomology implies equal periodic means; manuscript uses only the necessary telescoping direction | SUPPORTED |
| P25-B-005 | 133 | `BowenLanford1970` | Reciprocal determinant for a finite-type shift | SUPPORTED |
| P25-B-006 | 134 | `Ruelle1976` | Flow-zeta/operator construction retains actual periods and weights | SUPPORTED |
| P25-B-007 | 135 | `Wirzba1999` | Established separation of symbolic, classical, semiclassical, and exact multiscattering objects | SUPPORTED |
| P25-B-008 | 150 | `BowenLanford1970` | Reciprocal-determinant finite-type shift zeta | SUPPORTED |
| P25-B-009 | 152 | `Ruelle1976` | Flow timing and dynamical weights are not discarded | SUPPORTED |
| P25-B-010 | 160 | `GaspardRice1989Exact` | Three-hard-disk S-matrix resonances use the multiscattering determinant | SUPPORTED; correction does not alter this claim |
| P25-B-011 | 162 | `Wirzba1999` | Exact determinant structure and non-interchangeable semiclassical/cumulant limits | SUPPORTED |
| P25-B-012 | 278 | `CvitanovicEckhardt1989` | Effectiveness of periodic-orbit quantization/cycle methods | SUPPORTED |
| P25-B-013 | 328 | `Livsic1972` | Periodic sums as the standard cohomological obstruction | SUPPORTED |

No source is treated as supporting the manuscript's new two-witness theorem, minimax bound, computational replay, Route-A tuple, or any Hilbert--Polya claim.

## Proposed MINOR controls

The four rows below are bibliography controls. They do not require a manuscript claim rewrite and do not change any experiment or canonical result.

| ID | Severity | Exact target | Proposed operation | Reason |
|---|---|---|---|---|
| `IL-MINOR-1` | MINOR | anchored bibliography `B0001` | `replace_block` | Add the published erratum note for `10.1063/1.456018` |
| `IL-MINOR-2` | MINOR | anchored bibliography `B0002` | `replace_block` | Add the published erratum note for `10.1063/1.456019` |
| `IL-MINOR-3` | MINOR | anchored bibliography `B0006` | `replace_block` | Add official issue number 3 to `Ruelle1976` |
| `IL-MINOR-4` | MINOR | anchored bibliography `B0008` | `replace_block` | Normalize the unverified initials expansion to authoritative `A. N.` |

The source `paper/references.bib` and manuscript remain unchanged. The exact proposed changes live only in `notes/stage4_5_integrity_patch_round1.json` and cannot be applied without a complete author authorization bound to that patch's exact SHA-256.
