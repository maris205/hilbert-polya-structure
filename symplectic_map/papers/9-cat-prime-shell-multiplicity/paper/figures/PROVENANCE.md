# Prime-shell figure provenance

Status: **ROUND-1 BOUNDED REVISION FROZEN FOR INDEPENDENT ROUND 2**  
Generated: 2026-08-15 UTC

## Scientific source binding

The figure loaders verify these immutable source artifacts before reading any
scientific value:

| Artifact | SHA-256 |
|---|---|
| `experiments/source_lock.json` | `662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49` |
| `notes/PROOF_PACKAGE.md` | `47216ad4021d3476bfd0850ebec24c9ceafb5af8c0573214182fd2d0da7b2daa` |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | `9509278ce55d908dba7d7cb4a809a335cc51d9364e8bfdfd1dc66be594775b8f` |
| `results/EXPERIMENT_RESULTS.json` | `448de06e92bd7ab4e5374e5d1f57413df45859cd3476ff14b2691b63ac364fab` |
| `experiments/OFFICIAL_EXPERIMENT_RESULTS.md` | `66bfefe9dcf5731cb89a0597deed5df322f9bc24f9fc3a592d4790a46d2a4dc0` |
| `experiments/OFFICIAL_VALIDATION_REPORT.md` | `32a1758362f94372a83588de63e2b5df33a8f7e45e0646de53154a2ca1afaab4` |
| `results/INDEPENDENT_RESULT_INTEGRITY.md` | `aa0c7db555f11920c7305be508f6cfff62375970e112e9f720111831da20b3bd` |
| `results/result_manifest.json` | `8ca12744638a47b6e4fa3239a60a19d79229d2b9596ae4fe4b2f66a399618f92` |

The asset package uses only the inherited fixed rows at
`p = 2, 3, 5, 7, 11` and proof-sourced all-prime statements. It neither
imports nor executes experiment candidate code. It performs no new prime or
modulus scan, no numeric `s` or `log p` evaluation, no composite scan, and no
centralizer computation.

## Figure-to-evidence map

| Figure | Evidence used | Scope boundary |
|---|---|---|
| Figure 1 | fixed period histograms, shell sizes `(3,8,24,48,120)`, and multiplicities `(1,2,4,6,24)` | five development-seen rows; uniqueness/all-odd-prime bounds are proof-sourced |
| Figure 2 | exact raw `p=5` factors, orbit-label factor, and symbolic repetitions `r=1,2,3` | raw-return and orbit-label constructions are explicitly not identified |
| Figure 3 | scalar obstruction, equal-weight power sums, fractional shell identity, selector costs, and one symbolic `J_2(q)` control | composite `q` is symbolic only; the follow-up centralizer route remains untested |

## Reproduction

From `paper/figures/`:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 \
SOURCE_DATE_EPOCH=1471132800 \
MPLCONFIGDIR=/tmp/paper9_figures_mplconfig \
python -B generate_all.py
```

The orchestrator performs two complete render passes, compares all nine
output hashes, runs PDF/SVG/PNG quality probes, and builds the strict manifest.

## Frozen output hashes

| Output | SHA-256 |
|---|---|
| `fig1_shell_profiles.pdf` | `16045d45187cb3e8fb81192203e1255f2ddc749e3a4faf6ffd45b256b67c6531` |
| `fig1_shell_profiles.svg` | `70271e420c1e908ac49fd251d1d01a86d436f4ea8e8c3c50dad514f4c1997b06` |
| `fig1_shell_profiles.png` | `579de982fe858081f5cda55a21d823755c5c1b9cae2b6b26395965dbe5c2bf20` |
| `fig2_product_semantics.pdf` | `39ddd9baaaa2fc5ce7026f1d5cb844ec3147cbd707959e5ada1f61ea12f2b0da` |
| `fig2_product_semantics.svg` | `a42fdaaefc2dda010ec1724196c18410e7ae1c615d5e5ef342fd9d8803b2f6ee` |
| `fig2_product_semantics.png` | `e7f32d6ccb2e2bbe759f51463a26031c9fc021daf05c6b6f16f1c486caeff79e` |
| `fig3_mechanism_boundary.pdf` | `2b0a72db9d8cea6d901a8f2e03d6f2a17c49a4d2a2cd217e36ccbf148d4806b4` |
| `fig3_mechanism_boundary.svg` | `dfb128561edec5263c368ee5227405ef7c4248e01af369a6620c01787bdbcf17` |
| `fig3_mechanism_boundary.png` | `9f469c0d2717925440f39d95fbb7247f641723dc3110fecf32b6125d49ff45fa` |

The final strict figure manifest has SHA-256
`23468908fb020e80677e7a5b8e8686c2d14edbec2dc1e74f06973940c12adb8e`;
the final two-run determinism audit has SHA-256
`a6aab23da51635f07e68104507a5ab55f49d64abdf33f70205e5317478b71129`.
Visual details are documented separately in `FIGURE_QA.md`.
