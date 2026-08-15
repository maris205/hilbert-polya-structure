# Paper 11 Figure Provenance

## Status and boundary

This publication-asset package contains exactly three deterministic figure
stems, each in PDF, SVG, and 300 dpi PNG form. It is a read-only rendering of
the frozen Paper-11 theorem/result chain and the independently audited scope
correction. It does not edit or execute the candidate, post-run analyzer,
registered result, source lock, proof package, or upstream Paper-10 terminal
package. It performs no new candidate run, analyzer run, parameter scan,
random draw, numerical logarithm, numerical value of $s$, or numerical value
of $q^{-s}$.

The package classification is
`EQUIVARIANT_RETENTION_COMPRESSION_TRADEOFF_CERTIFIED /
A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.

## Frozen evidence bindings

| Role | Relative path | SHA-256 |
|---|---|---|
| source lock v2 | `experiments/source_lock.json` | `331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b` |
| independent source rereview | `notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md` | `2f75d6934e3d61bdc941ee6689102a1cb08a959270a7cd87965579f1ec5cc622` |
| proof package | `notes/PROOF_PACKAGE.md` | `3d723fdb02c89f9b2f281da807bcd745c5991393d25e223f95d6673961c20948` |
| claims--evidence matrix | `notes/CLAIMS_EVIDENCE_MATRIX.md` | `0ea191ebb1f6f0f915db096a68606099d4a315d80d333adadd3e396b11885490` |
| novelty assessment | `notes/NOVELTY_ASSESSMENT.md` | `1dbd6e4dc07fbc1e126334f6484a71b77852f0583749ba64259bd0e603669c95` |
| frozen citation sidecar | `notes/CITATION_VERIFICATION.md` | `1bfc33598d9ff5e5a8636a9ba5f8365ef9c3176614ba90a2b64ae1eb6dc4154b` |
| post-run scope audit | `notes/INDEPENDENT_POSTRUN_SCOPE_AUDIT.md` | `f7b365c9e6c8933cf3cbcaf3c96692cbacdaabcc84400bdc629f1d482cb243e4` |
| raw registered result | `results/EXPERIMENT_RESULTS.json` | `bef8aa5d632ed11b1ca58a123bbfe967a5426e2049d862118a373e4c1dc005fe` |
| dual-tree result manifest | `results/result_manifest.json` | `a0b409061c34eff0d68fdc326fe4ec6ff9295895444b857ee161fd77e417292c` |
| independent result review | `results/INDEPENDENT_RESULT_INTEGRITY.md` | `c91737c8bf860bd559eebebe08420fc5d095800c47d132381f584e918e714a20` |
| separate analyzer review | `results/POSTRUN_ANALYZER_REVIEW.md` | `ba63afc8c88903f15ec6ac5d82f0cd65430710ca9c132b489a7cd4f70e7660a8` |
| official result report | `experiments/OFFICIAL_EXPERIMENT_RESULTS.md` | `06f547fdfbbfb3bd51a57041758a49f18acceca9dda8e19967c2364500d64918` |
| official validation report | `experiments/OFFICIAL_VALIDATION_REPORT.md` | `754a36c0e2e6b5c5002ecb8b3473d0af0e077b4f5b88da2bc6851bdafad23221` |
| Paper-10 final integrity | `../10-cat-centralizer-quotient/paper/FINAL_INTEGRITY.md` | `e0a4803ff8e2063ebf5766803212579b44cd80c15572b166c1389f0242f8e6ce` |
| Paper-10 pipeline state | `../10-cat-centralizer-quotient/paper/PIPELINE_STATE.json` | `dc7550b39e42cdeeeacd4ae64f9fb4142b0f2e2e4b315d0e73f1932077e0b09c` |
| Paper-10 terminal PDF | `../10-cat-centralizer-quotient/paper/paper_final.pdf` | `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378` |

`figure_data.py` hashes every item before strict JSON parsing. It rejects
duplicate keys, trailing data, floats, nonfinite values, altered lifecycle
counters, altered K001--K012 controls, an altered row order, an altered
$C_6$ control, or any change to the review and terminal dispositions.

## Scope-correction provenance

The independent scope audit verdict is `PASS_WITH_SCOPE_CORRECTION`. The
locked row $q=2$ has $(n_2,r_2,m_2)=(3,3,1)$, hence point-cardinality is
$(1-t^3)^{-1}$: it retains source support and has unit exponent. This is the
unique positive locked row/type pair. The authorized negative conclusion is
only family-uniform: no one scalar-reduction type has both properties over
all nine rows. The assets make the exception explicit and never use the
rejected per-row “none” claim. Since $r_2=r_4=3$, the exception is not
modulus-specific.

## Publication citation layer

The frozen source sidecar contains a historical bibliographic typo for Laura
Walton's paper. The DOI-authoritative record for
`10.1016/j.jnt.2018.03.023` is *Journal of Number Theory* **192** (2018),
386--405. `paper/CITATION_VERIFICATION.md` and `paper/references.bib` correct
that metadata only at the publication layer. No frozen source file is edited,
and the correction changes no theorem, result, novelty assessment, or
scientific claim. The publication bibliography has fourteen verified entries
and treats the 2008, 2013, 2015, and 2018 constructions as direct prior art;
the novelty score remains 2/10.

## Exact display transformations

- Figure 1 composes named carriers, an information ledger, and the four exact
  scalar pairs. Its point-cardinality row says “support $r_q$; exponent
  $m_q$; unit when $m_q=1$,” and it marks the $q=2$ exception and
  $r_2=r_4=3$.
- Figure 2 displays the frozen order $(2,3,5,7,11,4,6,9,10)$, the exact
  $(n_q,r_q,m_q)$ values, the collisions $r_2=r_4=3$ and
  $r_6=r_9=12$, and all 36 scalar pairs. Only the $q=2$ point-cardinality
  cell is starred.
- Figure 3 compares a regular orbit, a trivial one-point $BC$ action, and the
  separately typed effective $C_6/C_2\sqcup C_6/C_3$ control. It reports
  the action kernel, labelled-twist boundary, period-two/period-three source
  factors, and static inertia counts without making any scalar per-row claim.

All scientific numbers are exact integers or exact rational records. Figure
placement, color, hatch, and typography are presentation transformations
only.

## Deterministic build

Run from `paper/figures/`:

```sh
env PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 \
  SOURCE_DATE_EPOCH=1471132800 \
  MPLCONFIGDIR=/tmp/paper11_figures_mplconfig \
  python3 -B generate_all.py
```

The driver validates the frozen payload, renders all three generators twice,
requires byte-identical hashes for all nine outputs, verifies the exact
three-stem inventory, writes `DETERMINISM_AUDIT.json`, frames
`ASSET_TREE.json`, and builds `FIGURE_MANIFEST.json`. PDF metadata dates,
SVG identifier salt, font families, hash seed, and Matplotlib configuration
location are fixed. No bytecode cache is allowed in the asset tree.

## Figure-output identities

| Output | SHA-256 |
|---|---|
| `fig1_retention_hierarchy.pdf` | `f80ea5a21d46f7b419196689b96127efc37e842fc21b890b28a02f02a722c525` |
| `fig1_retention_hierarchy.svg` | `526db43696792ecfc5ece6fd87d239f1fbd799164aab146a2d90e99cb1445a85` |
| `fig1_retention_hierarchy.png` | `1ecc57c0778e351d9685d99425f5d8cbcfc42e4f12dd744ed3dcf0e4d2368739` |
| `fig2_nine_row_retention.pdf` | `9525b8c11d7da9fe00409bebc591d1d792867176e8a7e764c95bbbabafeba329` |
| `fig2_nine_row_retention.svg` | `1c3dd03ff9b974b660734908a9bc8a86630c4cae2284862d13ea221e5a1c1662` |
| `fig2_nine_row_retention.png` | `72f5d934cc0c30e2dc9de6524a179c5cdce6a146558ee99621d113d7e34f0afa` |
| `fig3_effectivity_counterexamples.pdf` | `aaef94b667ede3c309044f28be9c029ab2435b5a5d77031e292ed0dc257c8c5b` |
| `fig3_effectivity_counterexamples.svg` | `0b68eaaf213066156b8ab9bb11ecb975d5b73b499d407034af6ba5e8d1d1aa1a` |
| `fig3_effectivity_counterexamples.png` | `44941b2e72ac7154cb1ef32a3b65b029a906b9b032c5006b416e3d2a9a5aba56` |

These identities are checked again during the final two-run build and are
machine-bound in `FIGURE_MANIFEST.json` and `ASSET_TREE.json`.
