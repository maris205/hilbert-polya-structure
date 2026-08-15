# Paper 8 Figure Provenance and Quality Record

Status: **PASS**  
Frozen date: **2026-08-14 UTC**  
Machine manifest: `FIGURE_MANIFEST.json`  
Machine-manifest SHA-256:
`e292df2cd1d9d2c19675bc36cf30ed75e88e730fca17c7cd47420285be07fb2c`

## Scope firewall

This package visualizes only the frozen Paper 8 theorem/proof and the
manifest-bound exact raw result. Figure generation did not run the candidate,
compute any period above 12, access a prime table or zero dataset, alter a
scientific source, or create a new scientific result. The final result
manifest is `PASS` with SHA-256
`045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f`.

Hash-locked inputs:

| Input | SHA-256 |
|---|---|
| `notes/PROOF_PACKAGE.md` | `ee02fe72071c0bbea26f5f34c28130374fe1a919195cfbe154f6f5a39ab420af` |
| `results/EXPERIMENT_RESULTS.json` | `0d8054ad36ad8cdef1496948cf5dd98d6a1a55c186d68124f45a5e6e35bddaa0` |
| `results/result_manifest.json` | `045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f` |
| `experiments/OFFICIAL_EXPERIMENT_RESULTS.md` | `4cf1645505a835a9d0aa62d84e7b6b47fc708b1347a954eeac26eb9710b9187d` |
| `experiments/OFFICIAL_VALIDATION_REPORT.md` | `ac9ac741cffd89dc8ab32db654ae59dc901b823a4b496be0607c7ce05fd403c3` |

## Reproduction

From this directory, run:

```bash
PYTHONDONTWRITEBYTECODE=1 python -B generate_all.py
```

`generate_all.py` invokes each independent per-figure generator twice under
`PYTHONHASHSEED=0`, `SOURCE_DATE_EPOCH=1471132800`, and disabled bytecode
writes. It requires all nine second-run PDF/SVG/PNG hashes to equal the
first-run hashes before writing `FIGURE_MANIFEST.json`. The frozen run passed
with all nine files byte-identical. No `__pycache__` or `.pyc` artifact is
present in the figure package.

## Figure-to-evidence map

- `fig1_carrier_bridge`: `PROOF_PACKAGE.md` Steps 1--3 and assertion flags in
  `general_theorem_contract`. The exact registered audit is explicitly
  limited to $1\le n\le12$; the range $n>12$ is theorem-only and the locked
  `tail_periods_computed` list is empty. Flatters' imported positive
  norm-one result and Paper 8's separate negative-trace conversion are
  visually distinguished.
- `fig2_standard_cat_boundary`: `ledger_records` and `boundary_summary` in
  `EXPERIMENT_RESULTS.json`. The exception set is parsed from JSON. Primitive
  carriers, the ramified $p=5$ Jordan repair at $n=10$ (20 points / 2
  cycles), and no-carrier cases $1,6,12$ use redundant color, glyph, and hatch
  encodings. Determinant magnitude is not encoded.
- `fig3_capacity_specificity`: `clock_specificity` in
  `EXPERIMENT_RESULTS.json` and `PROOF_PACKAGE.md` Steps 7--9. Exact strings
  and integer/rational witnesses are used; no logarithm or eigenvalue is
  numerically approximated. The three frozen perturbations illustrate the
  general coprime-sequence proof and are not presented as a sampled proof of
  discontinuity.

## Frozen output hashes

| Figure | PDF | SVG | 300 dpi PNG |
|---|---|---|---|
| Figure 1 | `b6c0b975bc45e94da0c3e012498a507df9378239726adb2f654f6bb0225dc4ed` | `d56200f919428b99e3955f775b02b67af468905d64ca2f921f740eb74c11923e` | `2f5531531cce2ab3a8b264b5bc8d2998875a4644b67ddcf85681b966507b87ba` |
| Figure 2 | `9983862ebabd20ba783441fd121925950ffffc14a9f0c397b5c1ff379d2e1789` | `7189fd770a731a70d2d4c17a2d26e4fb911fd48ab113c84712829298dcb75df4` | `6406a12408bf77c938bcead284aeb17a36408d31a046db546272737c2fc8d21e` |
| Figure 3 | `b5205fbf59daf6f693318c8820419b79f2e5edc4824a0269f73d6675e0548f2f` | `c14d2790a6ce30a041543f75718de72bfcb5536ceaed40d2fdde493c461270ec` | `db6dc23956e4bf957fd7a174a93c2b349f7f44121fcee4a2562e5dcd4981d111` |

## Automated quality checks

- PDF: each file is a one-page vector graphic, contains zero raster image
  objects under `pdfimages -list`, and embeds/subsets all DejaVu Serif fonts
  according to `pdffonts`.
- SVG: each file parses as XML, contains no `<image>` node, and preserves
  selectable text (`27`, `89`, and `39` `<text>` nodes for Figures 1--3).
- PNG: fallbacks are RGBA at reported $299.9994\times299.9994$ dpi
  (the standard 300 dpi metadata tolerance), with dimensions
  `2160x1065`, `2160x1305`, and `2160x1140` pixels.
- Environment recorded by the machine manifest: Python 3.12.3,
  Matplotlib 3.10.5, and Pillow 11.3.0.

## Original-resolution visual QA

All three final PNGs were inspected at original resolution after the frozen
two-run generation. **PASS** criteria and observations:

1. Figure 1: all arithmetic and routing arrows terminate at their intended
   nodes; the positive and negative trace routes are separated; the three
   parity indices are legible; no box, label, or panel heading is clipped;
   the computed/theorem boundary at 12 remains visually explicit.
2. Figure 2: all twelve determinant cells and carrier cells are legible with
   no cross-cell text collision; Jordan and excluded cases remain distinct
   in grayscale through glyph/hatch redundancy; the mod-$2,3,5$ labels and
   exact point/cycle counts do not crowd the axes.
3. Figure 3: prime/composite branches, exact perturbation labels, and the
   orbit/native comparison are legible; the base-order annotation is offset
   from the dashed line; mathematical text renders without raw TeX tokens;
   no panel heading or right-edge content is clipped.

The publication path is the PDF. SVG is the editable/selectable-text vector
alternative, and PNG is only the 300 dpi compatibility fallback.
