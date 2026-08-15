# Paper 10 Figure Provenance

## Scope and authority

This directory contains the complete figure-only asset package for
*A Centralizer-Quotient Audit for Cat-Map Torsion Shells*.  It contains
exactly three scientific figure stems, each emitted as publication PDF,
selectable-text SVG, and 300 dpi PNG.  The package does not contain or
authorize a new candidate run, modulus scan, matrix search, numerical value
of $s$, numerical logarithm, or construction on the equivariant/stacky/Hecke
boundary.

All theorem authority remains in the frozen proof; the nine finite rows are
implementation and falsification controls only.  The terminal scientific
classification is

`CENTRALIZER_CYCLIC_TORSOR_CERTIFIED / A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.

## Frozen evidence bindings

The read-only loader rejects any digest mismatch before returning display
records.  The complete bound set is:

| Frozen input | SHA-256 |
|---|---|
| `experiments/source_lock.json` | `aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2` |
| `notes/PROOF_PACKAGE.md` | `2eafe71f32c452ff8a20a6818ccb43082e02b866db7353e26c36ff432f1b2a4c` |
| `notes/NOVELTY_ASSESSMENT.md` | `6ee0fe2aff13c2d4329496e32f2d6aa190a92a3c3b4904168a21828b646de0a5` |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `03424a71fc8716618545a6c7c8b0fd05f5ad744cff034255ab0337012da0303d` |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | `a551784d205d9ef52ce6a493ab66cb7295a4a9dadbeb8bb2353fc58e3011dff5` |
| `results/CODE_REVIEW.md` | `990b1762e2aea6c379288854cca918cc4bbe87b7ea7ccadef7458ecfcf6988f0` |
| `results/EXPERIMENT_RESULTS.json` | `8dceb1b8a63db462c1fd55a242ea35de974f73b6c80da68517b91c9eebb214ff` |
| `results/INDEPENDENT_RESULT_INTEGRITY.md` | `29264a8fd97d3acf4435ed807294bffcda0844a48728d8572083d92a3bcf5b58` |
| `results/result_manifest.json` | `db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658` |
| `experiments/OFFICIAL_EXPERIMENT_RESULTS.md` | `1ece7db3fbee75bcecaecb0ad05f89fe88699c4231bea80581f382f33ed3aa6e` |
| `experiments/OFFICIAL_VALIDATION_REPORT.md` | `f94dbfb28a71aea4dac5e89a8bc2a622bba092b66098c2fc2217ceba19a8ad5a` |

`figure_data.py` reads only the source lock, raw exact-result JSON, strict
result manifest, proof markers, and the two independent review dispositions
after validating all eleven files above.  It never imports or invokes the
candidate.  It also requires one registered audit, zero candidate numerical
runs, the frozen modulus order, every registered control passing, and all
forbidden execution/evaluation counters remaining zero.

## Transformations

| Figure | Read-only transformation | Scientific boundary |
|---|---|---|
| `fig1_quotient_layers` | Select the frozen $q=5,11$ discard controls and combine them with proof-checked torsor, quotient, norm-fiber, reversor, and identity-map labels. | The torsor/clock statements are all-$q$ proof claims; the displayed discard values are controls. The reversor may pair $d$ with $-d$ but does not mix the noncyclic complement with $\mathrm{CV}_q$. Enriched quotients are outside scope, not rejected. |
| `fig2_nine_modulus_ledger` | Preserve the registered order $(2,3,5,7,11,4,6,9,10)$ and directly plot exact integer fields for $E$, $\mathrm{CV}$, $C$, $C^1$, source $A$-orbits, and quotient counts. | The rows verify the fixed implementation; no fit, interpolation, extrapolation, or all-$q$ inference is performed. Composite reversor cells remain `n/a`. |
| `fig3_clock_semantics` | Plot the exact source orders against the proof/result-checked coarse quotient period one, then diagram the abstract factor and external modulus specialization. | $q^{-s}$ and $\log q$ are symbolic labels only. Burnside/orbifold/stacky/groupoid/twisted-sector and Hecke refinements remain live and untested. |

The transformation scripts are independent and share only
`figure_data.py` and `paper_plot_style.py`.  All scientific quantities are
exact integers or symbolic expressions; there is no random state and no
floating-point scientific computation.

## Deterministic rendering

Run from the workspace root:

```bash
PYTHONDONTWRITEBYTECODE=1 python papers/10-cat-centralizer-quotient/paper/figures/generate_all.py
```

The driver renders every stem twice with `PYTHONHASHSEED=0`,
`SOURCE_DATE_EPOCH=1471132800`, a fixed SVG hash salt, a private Matplotlib
configuration directory, fixed PDF/SVG metadata, and bytecode disabled.  It
requires byte-identical hashes across both runs and exactly nine output
files.  It then checks PDF fonts/vector content, SVG structure/selectable
text, PNG dimensions/DPI, frames `ASSET_TREE.json`, and writes the strict
figure manifest.

Final rendering environment: Python 3.12.3, Matplotlib 3.10.5, Pillow
11.3.0, Linux/glibc 2.35.  Publication includes use the PDF files; SVG and
PNG are editable/fallback assets.

## Frozen output identities

| Artifact | SHA-256 |
|---|---|
| `fig1_quotient_layers.pdf` | `ac8b29c810881e6383fb3f8b7cb55c602e052ef1677def5643d540b8ee12feb3` |
| `fig1_quotient_layers.svg` | `4d2a340a59b52c440bc9c408a76f06d840ade8d7d900febf88a5cd91d6764d28` |
| `fig1_quotient_layers.png` | `70ceb2f65befdfd558bc241ff4edb24dc76a9375bb7e9669b1cba4f1e13ebfce` |
| `fig2_nine_modulus_ledger.pdf` | `f86ff8e50c5a138996c8f379fa0309ddc6071cffca1d540b81e07304dae2dd73` |
| `fig2_nine_modulus_ledger.svg` | `5747cc8f5a8f30eeb4017441c0be932ab7ee6c4a92b53c4b39a466039780d61c` |
| `fig2_nine_modulus_ledger.png` | `6a5845706c035454533a1d39bd6f8daa439d3615189f4f4ec7220182ed2a59c3` |
| `fig3_clock_semantics.pdf` | `0df9de8544c05e60749d456244c2920ac15c03a8bc5f5011a66f8d2c5e8cee33` |
| `fig3_clock_semantics.svg` | `894b31b8ad935a49d7ad3a1179a256bb4526e6da6dc1da372756af853bfd849d` |
| `fig3_clock_semantics.png` | `80d305f71a458713876f77d40db1f309bd732798d0c1f3ca1ec2291dcdb2ff92` |

Any later change to an output, generator, planning artifact, citation asset,
documentation artifact, asset-tree frame, or bound evidence hash invalidates
this provenance and requires a fresh independent asset review.
