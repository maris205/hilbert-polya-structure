# Independent Plan and Figure Integrity Review

Review date: 2026-08-14 UTC  
Verdict: `PASS`  
Scope: frozen Paper 7 plan, citation scaffold, and three-figure package only.

This was an independent, read-only gate over the plan and frozen package. No
plan, source, proof, result, figure, or manuscript file was edited. The only
project write is this review. Figure generators were exercised only inside an
automatically removed temporary copy. No network resource, external prime
table, Riemann-zero data, or approximate orbit data was accessed.

## Plan and claim--evidence gate

The reviewed plan has SHA-256
`b654c72f1596d5c39ddcf61b8ed6314d7e7d9e149a6d1e874b390d53f113d039`.
Its front matter correctly binds:

- source-lock v2:
  `205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1`;
- official registered result:
  `847564ffb9e69aee2018dfa179490fafa81b733ad58231dab9202b82623f3ce6`;
- strict result manifest:
  `6d9407408437954f52b4a1cb7f0caa50ca00bd22be9cf9a348a1bbb60c9a87e8`.

The C1--C10 claim matrix agrees with the frozen proof and official result:

- C1--C7 are assigned to explicit proof steps in the proof package, with the
  standard local contraction argument not presented as a priority claim.
- C3 includes the required integrality step rather than silently importing a
  stronger unpublished conclusion.
- C4 distinguishes exact Frobenius degree, exact dynamical period, and formal
  period.
- C5 identifies the degree-four polynomial only as a witness that the
  necessary two-coefficient filter is insufficient. It is never called an
  equality cycle.
- C6 does not reclassify a repeated return as an exact period-`nr` orbit.
- C7 retains the warning that a single-cycle polynomial need not lie in the
  base field.
- C8 matches the raw official JSON exactly: periods `2,...,7`, exact-set
  degrees `2,6,12,30,54,126`, cycle counts `1,2,3,6,9,18`, twelve
  zero-degree sign gcds, twelve nonzero exact norms, and twelve agreeing exact
  engines. Its status is explicitly development-seen reproduction and
  implementation falsification, not blind validation or theorem evidence.
- C9 is explicitly `OPEN` for every `n>=4`; finite absence is not promoted to
  an all-period result.
- C10 and the required nonclaim sentence keep rational equality, complex
  modulus, and characteristic-exponent equality separate. Prime orbits, zeta
  zeros, quantization, Route A, and Route B are not introduced as results.

The abstract logic, section plan, comparison table, figure plan, appendices,
and release gates preserve the same boundary. In particular, the manuscript
is instructed to state the all-period local valuation theorem as proof-backed,
the `n=2,3` rational-equality exclusion as local-obstruction-backed, the
`n=2,...,7` ledger as development-seen finite evidence, and the all-period
rational equality question as `OPEN_FOR_N_GE_4`.

## Citation gate

The current citation files are bound as follows:

| File | SHA-256 |
|---|---|
| `notes/CITATION_VERIFICATION.md` | `bb315de70ecbcd8ac6dbdeebd32d68cb6f99bd4749a1924e3ba2cdf6d77a41df` |
| `notes/CITATION_PLAN_AUDIT.md` | `1801df7e97bf3e4974c3a5d2bdc8d93e5b8fa920e9b623ed64c9476f1cc616aa` |
| `paper/references.bib` | `dbcb1de7f92643291e688308b472616107a0b376db24a250379f97826d5d53f1` |

Mechanical extraction found 12 unique BibTeX keys, 12 unique plan citation
keys, and 12 verified external-ledger headings. The three sets are identical:

`riveraletelier2026critical`, `benedettoetal2014attracting`,
`hutz2009good`, `rajagopalzhang2025uniform`, `morton1994rational`,
`buffgauthier2015quadratic`, `jixiezhang2026space`,
`murakami2024arithmetic`, `benedettogoksel2023part1`,
`benedettogoksel2024part2`, `wang2026prime`, and
`silverman2007arithmetic`.

There is no unused bibliography entry, missing plan key, duplicate key,
`[VERIFY]` marker, or fabricated public identifier for the local Batch-01
predecessor. The plan respects the verified usage boundaries: the 2026 papers
are contemporary comparison/context where stated, Wang is genealogy only,
and no cited source substitutes for the self-contained local proof.

## Figure input and semantic contracts

Static inspection found no network-capable import in any generator and no
hard-coded official degree, cycle-count, sign-certificate, or norm array. Each
generator calls the frozen input contract, checks candidate/source-lock
agreement, requires a passing exact-symbolic result with zero candidate
numerical runs, and rejects prime/zero access flags. Display formulas are
guarded by the corresponding frozen theorem/proof-contract fields; candidate
measurements and decisions are read from the registered JSON.

### Figure 1: theorem and open-boundary split

`fig1_boundary_map` checks T1--T3, the proof-certified all-period 2-adic
valuation status, the source/result equality of `OPEN_FOR_N_GE_4`, and the
`NOT_DECIDED` complex-modulus field. The rendered chain states residue
characteristic two, `0<|c|<1`, and exact `n>=2`; it then separates:

- the proved unit-cycle and valuation statements;
- the rational `2^n`-times-odd corollary;
- rational equality `Lambda_C=+/-2^n`, open for `n>=4`;
- modulus-only and exponent equality, both not decided.

The caption repeats the hypotheses and rationality boundary and identifies the
local argument as standard. No branch is visually or verbally promoted to a
theorem.

### Figure 2: registered development-seen ledger

`fig2_registered_ledger` reads all periods, degrees, cycle counts, target
orders, gcd degrees, norm-nonzero flags, engine-agreement flags, and hit flags
from `EXPERIMENT_RESULTS.json`. It fails unless the periods equal both the
source-locked range and the development-seen list and unless
`new_blind_periods=[]`.

The rendered values are exactly:

| `n` | 2 | 3 | 4 | 5 | 6 | 7 |
|---:|---:|---:|---:|---:|---:|---:|
| exact-set degree | 2 | 6 | 12 | 30 | 54 | 126 |
| exact-cycle count | 1 | 2 | 3 | 6 | 9 | 18 |

Both target rows, `B_n=+1` and `B_n=-1`, contain six cells with
`deg gcd=0`, `N!=0`, and engine agreement. The upper panel carries a prominent
`DEVELOPMENT-SEEN REPRODUCTION` badge; the footer reports zero new blind
periods and that all-period equality is open for `n>=4`. The caption explicitly
denies an all-period inference.

### Figure 3: Frobenius obstruction and insufficiency

`fig3_frobenius_filter` reads T4--T5, the passing Frobenius--Hensel proof
contract, the exact lift coefficients, the complete degree-2--4 irreducible
ledger, and the control records. It requires `n2_n3_obstructed=true`,
`degree_four_filter_insufficient=true`, and
`all_period_inference_allowed=false`.

The figure correctly shows the progression from exact Frobenius orbit to
unique Hensel lift, dynamics/Frobenius equality, local norm, and the necessary
coefficient gate. The degree-2 and degree-3 rows are obstructed. Of the three
degree-4 rows, only `T^4+T^3+1` passes, and its meaning is visibly marked
`necessary only`; the footer says equality remains open. The four displayed
control badges are derived from passing power-map, Chebyshev sign-path,
negative-target, and formal-period-pollution records.

## Independent temporary regeneration

The three generators and their two frozen JSON inputs were copied into an
isolated temporary package. With bytecode disabled, `PYTHONHASHSEED=0`, a
temporary Matplotlib configuration directory, and no project output path, all
three generators were run twice. Both passes completed successfully, created
no bytecode/cache object, and produced nine nonempty outputs. Every second-pass
file was byte-identical to the first pass and to the official package:

| Output | SHA-256 |
|---|---|
| `fig1_boundary_map.pdf` | `7833416a81defd8cf87b8275d651f0d99c7dd09b3c8e1396f128a0264c414e3e` |
| `fig1_boundary_map.svg` | `8e7ff7bc82bb5d05fdc3a7de1881b406a949101d66ffe1a6ade1c7482e15a7d8` |
| `fig1_boundary_map.png` | `e1bfad408999e1dcf3c287537bb22ad992bf5ec9a5e3c8dd27b06ee6ff626a86` |
| `fig2_registered_ledger.pdf` | `2d24d6d10abd800e2b4e1f91b1ecc22de4f9930463cc6655cd3486b9895062ee` |
| `fig2_registered_ledger.svg` | `200b1b2b79f454aacf77efaba566bdc5daf97396a6df33c1f3b5e996948ca707` |
| `fig2_registered_ledger.png` | `c366c34b782cdc87537d611372ad36ad78dfaf6a2af414d4d9098faa1ed5c7c2` |
| `fig3_frobenius_filter.pdf` | `cb2838bfa7e6fa8a10a6a480992d9fdd6e8704d87c184a341365bcc724aae7aa` |
| `fig3_frobenius_filter.svg` | `d8e79d9b4f4b95ed66fdb5bff68bbe8683deed713400582070057262be4d11c9` |
| `fig3_frobenius_filter.png` | `757317d82d766bed0567f5a74c05860051551fbc2fa430e4bd3e610b9d9d5230` |

This independently confirms the existing determinism audit rather than merely
trusting its recorded `pass` flag.

## Manifest, provenance, and rendering gate

The figure manifest has SHA-256
`cd4f4a2e831790657dac7b1a4c9706e8693101cb0f0d8b3830b36691a50940c8`.
It contains 12 input records and 20 artifact records. All 32 paths are current
regular nonsymlink files, and every recorded byte count and SHA-256 matches.
Top-level candidate id, source-lock hash, registered-result hash, finite
classification, and all-period open status match the frozen JSON;
`forbidden_sources_used=[]` and `pass=true`.

The bound determinism audit has SHA-256
`e883612c05f4f09463d522ef7ce6bed1d5a2d3ade7d988fe29f5467f8dd39be0`,
records two regenerations, no mismatch, and the same nine official hashes.
`FIGURE_PROVENANCE.md` contains the current manifest hash and accurately states
the development-seen and necessary-only boundaries.

Independent rendering checks found:

- all PDFs are one-page vector files; `pdfimages -list` finds no raster image
  object;
- every PDF font reported by `pdffonts` is embedded, subsetted, and
  Unicode-mapped;
- all SVG files parse as XML, preserve text as text, and contain no embedded
  image element;
- PNG previews are approximately 300 dpi, with dimensions 2721x1005,
  2035x1714, and 3163x1895 pixels for Figures 1--3 respectively;
- the three LaTeX captions are self-contained, have unique labels, state the
  required evidence boundaries, and use the PDF vector masters.

All three original-resolution previews were inspected visually. Text, arrows,
bars, markers, legends, certificate cells, table rows, badges, panel letters,
footers, and page margins are legible and nonoverlapping. No label is clipped,
no color is the sole carrier of a scientific decision, and no decorative plot
title competes with the manuscript captions.

## Disposition

`PASS`: the updated paper plan, 12-key citation scaffold, frozen figure-data
contracts, twice-reproduced outputs, manifest/provenance chain, vector/font
rendering, captions, and visual semantics are mutually consistent with the
official Paper 7 result and its open all-period boundary.

Exact blockers: none.
