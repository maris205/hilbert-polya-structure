# Paper 12 Figure and Citation QA

## Author-side verdict

`PASS_PENDING_INDEPENDENT_ASSET_REVIEW`

This is an asset-author QA verdict, not the independent `ASSET_PASS` required
for manuscript integration and finalization. No independent verdict is
self-issued here.

## Original-resolution visual inspection

The final PNG originals and grayscale conversions were inspected at their
native pixel dimensions after the last deterministic regeneration.

| Figure | Native PNG | Color inspection | Grayscale inspection | Result |
|---|---:|---|---|---|
| `fig1_theorem_architecture` | 2160 x 1515 | no clipping or overlap; $S_m(a,1)$ specialization explicit; firewall and no-theorem-arrow branch clear | dashed firewall, hatched audit, text labels, and line styles remain distinct | PASS |
| `fig2_weighted_two_term_law` | 2160 x 1500 | four supports, elimination reasons, two-term law, quartic identity, and `OPEN` box readable | `SURVIVES`/`REMOVED` text, crossed terms, and hatched `OPEN` box preserve all claim distinctions | PASS |
| `fig3_step9_certificate_pipeline` | 2160 x 1665 | all seven stages legible and uncropped; (9.14), $j\geq1$, separate $j=0$, $H/A/D$, and `OPEN` are visible | numbered stages, hatched separate-$j=0$ box, and crosshatched `OPEN` box remain distinct | PASS |

No figure contains an internal decorative title. The letters A/B/C are panel
markers, and all scientific framing is in the exact LaTeX captions.

## Mechanical publication checks

- Exactly three stems and nine format outputs are present.
- PDF, SVG, and PNG files are generated from the same Matplotlib vector
  scene for each stem.
- PDF pages are single-page vector diagrams with no raster image objects.
- PDF fonts are embedded, subset TrueType/CID fonts; Type 3 fonts are absent.
- SVG files parse as XML, contain selectable text, and contain no raster image
  nodes.
- PNG metadata reports 299.9994 dpi on both axes, within the 300 dpi
  tolerance; modes are RGBA.
- Fonts and line weights remain readable at full-column width.
- Okabe--Ito colors are redundant with text, borders, dashes, cross-outs, and
  hatches; grayscale meaning does not depend on hue.
- There are no axes, legends, hidden units, decorative 3-D effects, or
  empirical values.
- Captions are self-contained and state the comparison, theorem scope, and
  limitations.

Machine-extracted font, vector, page-size, XML, and raster details are frozen
per output in `FIGURE_MANIFEST.json`.

## Scope and semantic checks

- Figure 1 uses $S_m(a,1)$, not an ambiguous $S_m$, for the
  epsilon-one period-three specialization.
- The nilpotent qualifications for periods one and two remain visible.
- The quartic result is always restricted to the complete normalized fiber
  with formal fixed-point trace multiset $0^4$.
- Universal $D_m\neq0$ is marked `OPEN` in Figures 2 and 3.
- No all-degree period-three separation, all-quartic theorem, or global
  $P(4)=3$ statement appears.
- Figure 3 retains identity (9.14), the incoming-transfer step, and the
  genuinely separate $j=0$ case.
- No figure states or implies Q/R agreement, a successful registered audit,
  a coefficient diagnostic match, a result pass, or scientific runtime
  support.
- No prohibited diagnostic value is exposed or reconstructed.

## Exact caption and label checks

The three stems, labels, and full captions in `latex_includes.tex` match
`figure_contract.json` and the exact contract in `PAPER_PLAN.md`:

| Stem | Label |
|---|---|
| `fig1_theorem_architecture` | `fig:theorem-architecture` |
| `fig2_weighted_two_term_law` | `fig:weighted-two-term-law` |
| `fig3_step9_certificate_pipeline` | `fig:step9-certificate-pipeline` |

Any change to a stem, label, caption, formula, or scope phrase requires a new
asset freeze and independent review.

## Citation-key contract

`paper/references.bib` contains exactly these 11 canonical PascalCase keys:

```text
BianchiHe2026
CantatDujardin2026
CattaniDickensteinSturmfels1996
CvitanovicHansenRolfVattay1998
DullinMeiss2000
FriedlandMilnor1989
GuillotRamirez2019
Huguin2024
Hutz2010
Hutz2020
Ueda2004
```

The frozen draft has ten lowerCamel placeholders. After `ASSET_PASS`, the
manuscript author may apply only the exact lowerCamel-to-PascalCase map in
`paper/CITATION_KEY_CONTRACT.json`. `BianchiHe2026` is optional and has no
frozen-draft placeholder. Duplicate BibTeX aliases are not permitted, and the
asset author did not edit `paper/manuscript.tex`.

The exact manuscript placeholder domain is:

```text
cantatDujardin2026MultiplierRigidity
cattaniDickensteinSturmfels1996Residues
cvitanovicHansenRolfVattay1998Beyond
dullinMeiss2000GeneralizedHenon
friedlandMilnor1989DynamicalProperties
guillotRamirez2019Multipliers
huguin2024ModuliMultipliers
hutz2010DynatomicCycles
hutz2020MultipliersInvariants
ueda2004FixedPoints
```

The normal record builder removes LaTeX comments, parses every manuscript
`\cite...{}` command, and requires exact set equality with this map domain.
The frozen record reports no missing key and no extra key. Cardinality alone
is not accepted, and any unparsed citation command fails the build closed.

## R1 repair and R2 gate

R1 is preserved unchanged at
`notes/INDEPENDENT_PLAN_FIGURE_REVIEW.md`, SHA-256
`d6bc5c624d371752f06ff1d8a8ae27367a7b4c2370b4ab2f19b52cbe24d95ed6`,
with verdict `REPAIR_REQUIRED`. The sole blocker was the old disjoint
placeholder-map domain. The citation contract changed from
`e73c0c75310cdb60706bed900ac90308cd27320a9d9ce6d53b2fc7e73ce82f92`
to `997ca84ee7d868f34cacc783993f10d1b82b86c71fbdc1c9b80f38bcf5199bfd`;
the manuscript and bibliography were not edited. No existing record schema
has a review-history slot, so the R1 binding is recorded here and in
`PROVENANCE.md` for the fresh R2 review.

## Required next action

Obtain a fresh independent R2 review that binds the final asset tree and returns
the exact verdict `ASSET_PASS` before any manuscript integration,
finalization, or submission step.
