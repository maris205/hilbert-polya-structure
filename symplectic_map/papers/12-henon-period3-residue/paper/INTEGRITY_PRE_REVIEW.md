# Pre-Review Terminal Integrity Record

- Date: 2026-08-16 UTC
- Candidate/lifecycle: `henon_period3_residue_proof_note_v1`
- Canonical path base: `papers/12-henon-period3-residue`
- Terminal author-side state:
  `READY_FOR_FRESH_INDEPENDENT_MANUSCRIPT_REVIEW`

This is the terminal author-side integrity node for the package sent to a
fresh independent manuscript reviewer. It is not an independent manuscript
verdict and does not authorize finalization or submission. This record does
not hash itself and no earlier node points to it.

## Integrity root

| Node | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `de706b358a6b1fdec47da2ab88704ab8011ed22a1dd7de560b8912d0c845a617` |
| `paper/math_commands.tex` | `40a7fe009279e803be822ad2a3fcae56793b2b5c098e0876800e51d1b4f24510` |
| `paper/references.bib` | `f1b6fe0807e33debf87c8be19e1b81b2a4a10f886fd9f4ae1d20bf264e978adc` |
| `paper/manuscript.pdf` | `bb3cd34efbff6ec3c2bc2803b0c68b30b701d79833d5a9b4eebeb68d101da949` |
| `paper/paper_pre_review.pdf` | `bb3cd34efbff6ec3c2bc2803b0c68b30b701d79833d5a9b4eebeb68d101da949` |
| `paper/manuscript.log` | `59ba77a6c79c066ef00435790911d415e6b28e487cb4e012e850faaf3bde0988` |
| `paper/manuscript.blg` | `be7f60aae83be2fe4e5cc3d0d2898fcd73661df5e2333ae4173dc63bb971ad61` |
| `paper/manuscript.bbl` | `ac0ae8c4f0de3188e42f6f0b17775eb1cf90468431b048986ba23caa12dd522a` |
| `paper/manuscript.aux` | `67a5988dcf5b5359a7933f077ca2a7f92b39f82f5ceb7b8dd23200a935da3824` |
| `paper/manuscript.out` | `7b918498371e32fa96c359d8d5fbdf195fa62091df38d36b9b6df9882a9593d1` |
| `paper/PAPER_CONFIGURATION.md` | `9e1d8439e3faa1db334d4eee9c19bf98a23e7fe5d01357123b85afbaa94aa987` |
| `paper/CLAIM_MANIFEST.json` | `d212ca5cde6580087e34c69fe19d3706d140f0cc45d5d662ba9065fe8b1fb8cb` |
| `paper/PROOF_ONLY_PASSPORT.json` | `cc5fbd4836f589a3f5316c69b085868b53f24fa1bf5c95488a4a8010bf3eea6b` |
| `paper/FIGURE_PACKAGE.json` | `46c3e73993342be77edbcb3eb4566ed60486ddf9d1a14ceecbacf1e1b7beb0c0` |
| `paper/PLAGIARISM_MANIFEST.json` | `ada038c79338466dd05b2a0cc57094539884acfe2fdf0dfac6d3e608cf81366b` |
| `paper/PIPELINE_STATE.json` | `a72bc3afba6284abcf318cd9831dec12ffb36415fbd1729033c19656b4aaf6a4` |
| `paper/AUTHOR_PRE_REVIEW_AUDIT.md` | `ed741017ac3820e02b8a990afab2cd973daac089c786ad5072fc71d17d4bbfd4` |

All JSON nodes parse under duplicate-key rejection. Every digest above was
recomputed from the named ordinary file. `paper/manuscript.pdf` and
`paper/paper_pre_review.pdf` are byte-identical. `paper_final.pdf` is absent.

## Frozen authorities and independent upstream gates

| Authority | SHA-256 | Bound status |
|---|---|---|
| Proof-only manuscript lock | `2c7f056b7f9566f754a06c30417105c0b1cefb2d0081f4bca8bb3a00adbf8eeb` | closed eight-file allowlist |
| Source lock v2 | `2fa930f697f6040cb16916d2b4dba7ec591a712882c108848e9eecf53608e1c2` | immutable |
| Source-lock rereview R2 | `5e66edcd7f33769f748c8b6bd6582aa7e05b3325329839c46bf3627945803d11` | `SOURCE_LOCK_PASS` |
| Proof package | `36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9` | sole scientific authority |
| Claims/evidence matrix | `5630610bb637e155fa631eb2d9c4b36c6ea334ae976a6ef39a53dd733b8c62de` | immutable |
| Novelty assessment | `c497dc4e2c404fbbfc3c89450991964d1049f06288a051bc647a15005a66146a` | bounded no-hit only |
| Proof-only manuscript scope | `d0dc07976e9631e5d30ffe6d20f1e4d7d76aea4c04d1d42598e3b594d0fc23b9` | immutable |
| Registered-audit postmortem | `6648a0c3642d24eac1e22f3cc7349a805209d3293b556d6d5d5cbd873d0f831b` | provenance only |
| Independent proof-only handoff | `407cec5bf295c29330c24ae461dca86ad1bf54d77f44d477d83a821bf7e41711` | `PROOF_ONLY_HANDOFF_PASS` |
| Paper plan | `e4876a50d172ccfb857b3c6667a0be85d12105f4d7da63da393531a36cef9d31` | frozen |
| Citation contract | `997ca84ee7d868f34cacc783993f10d1b82b86c71fbdc1c9b80f38bcf5199bfd` | exact ten-key migration |
| Canonical bibliography | `f1b6fe0807e33debf87c8be19e1b81b2a4a10f886fd9f4ae1d20bf264e978adc` | immutable, 11 entries |
| Figure manifest | `3adc970996ea7a6e1dc043a554c88b8007f4fe203aa30a522b0a4663dcb31096` | frozen |
| Repaired asset tree | `a5006ef63be3bcc585567276f05f063fd6786c6170081e0eea8ec0ca128598ee` | frozen |
| Asset review R1 | `d6bc5c624d371752f06ff1d8a8ae27367a7b4c2370b4ab2f19b52cbe24d95ed6` | immutable repair-required history |
| Asset review R2 | `7b633dd001f1ae086863826612a15d74325406f1eaf2b95fc49e49eddd7ae404` | `ASSET_PASS` |

## R0 history and authorized transition

The R0 manuscript reviewed by the asset gate remains bound at SHA-256
`f3c535739046e61378ec8896b70e6d30652a7654213894e1556d221e511d3022`.
The current source differs only by the authorized citation-key migration,
three exact frozen figure blocks, the necessary graphics import, and
layout/cross-reference-only repairs recorded in
`paper/PAPER_CONFIGURATION.md`. The shared commands and bibliography are
unchanged. No science, caption, figure asset, or upstream record changed.

## Reproducibility and package QA

Two fresh isolated clean builds are byte-identical for PDF, LOG, BLG, BBL,
AUX, and OUT. The terminal logs contain zero LaTeX, package, pdfTeX, BibTeX,
citation, reference, duplicate-destination, overfull-box, and underfull-box
warnings.

Closed checks:

- anonymous 11 pt single-column note, 19 pages;
- Figures 1--3 at pages 3, 7, and 9 and exact to the frozen LaTeX blocks;
- 91 unique labels, 43 referenced targets, zero missing target;
- 11 canonical BibTeX entries, 10 cited keys, only optional
  `BianchiHe2026` unused;
- 38 embedded/subset/Unicode-mapped font rows, Type-3 fonts 0;
- raster image objects 0 and three vector figure PDFs;
- all three original figures and 19 of 19 integrated pages visually checked;
- zero forbidden high-index diagnostic value and no registered-evidence,
  universal-nonvanishing, global-quartic, cutoff, or historical-priority
  overclaim;
- zero project-local normalized visible-prose 12-word shingle overlap against
  Papers 1--11 and the available initial proposal, with the explicit boundary
  that this is only a heuristic.

## Acyclic provenance graph

The binding direction is:

`frozen proof-only authorities + independent upstream gates + frozen assets`

`-> manuscript sources + bibliography + figures`

`-> deterministic PDF + build artifacts`

`-> base pre-review metadata`

`-> PIPELINE_STATE.json`

`-> AUTHOR_PRE_REVIEW_AUDIT.md`

`-> INTEGRITY_PRE_REVIEW.md`.

This terminal record contains no digest for itself. The base records do not
point to the pipeline, the pipeline does not point to the author audit, and
the author audit does not point to this record.

## Release boundary

- `ready_for_fresh_independent_manuscript_review`: `true`
- `independent_manuscript_review_completed`: `false`
- `finalization_authorized`: `false`
- `submission_authorized`: `false`
- `paper_final_pdf_created`: `false`

The package is frozen at
`READY_FOR_FRESH_INDEPENDENT_MANUSCRIPT_REVIEW`. Any subsequent change to a
bound file invalidates this record and requires downstream hashes and QA to
be regenerated. Work must now stop for a fresh independent manuscript
review.
