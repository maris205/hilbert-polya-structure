# Independent Paper-Plan and Figure-Asset Review

**Candidate:** `cat_equivariant_retention_tradeoff_v1`  
**Review date:** 2026-08-15 UTC  
**Mode:** fresh independent read-only review of the frozen publication plan,
citation package, figure generators, rendered assets, provenance graph, and
result bindings  
**Authority:** this report authorizes manuscript integration only; it does not
authorize a candidate/analyzer rerun, a new arithmetic row, or a scope change  
**Verdict:** `ASSET_PASS`

## 1. Frozen review frame

The following review inputs were present as regular files and matched the
assigned SHA-256 identities exactly.

| Role | Path | SHA-256 |
|---|---|---|
| paper plan | `PAPER_PLAN.md` | `9a6ebb212e175775673e97bfc8b5eb18a2e8f760c756cdfc21583b0fb296124c` |
| publication citation verification | `paper/CITATION_VERIFICATION.md` | `29681de3379801d1f376ecaa3b3cfc0d366964666852bff8b08faaf3cd67d3ca` |
| publication bibliography | `paper/references.bib` | `d88a3de08479c46174831a7d562405835800822850505f455831925ff06691d7` |
| figure manifest | `paper/figures/FIGURE_MANIFEST.json` | `e3a8d1d36ba8c4959b080a9661b242c40195ea08d27690fc8ee899b487cfd6dc` |
| asset tree | `paper/figures/ASSET_TREE.json` | `95bb23519a427ef6a73a6a04b1aef6861aa4c5e4f6b844e7866bf9c43e52b28c` |
| determinism audit | `paper/figures/DETERMINISM_AUDIT.json` | `3f5f3dcd6fd9f2ffa6782b2d383f6e4d4178e74709b1ceb384f91c99957325ea` |
| figure QA | `paper/figures/FIGURE_QA.md` | `f3188fd4511bdf513bdfe9c79e7833ed324f07579c125c31fe82f91492418e7c` |
| provenance | `paper/figures/PROVENANCE.md` | `9efeae7cd81e4e3d548609f5b019e3cace99781de28f11020a1e49ee5180fdc8` |
| figure trace | `paper/figures/FIGURE_TRACE.json` | `a66e8302b085091faec02fb50165a300506aa29b176de731af4b4797db218d1b` |
| LaTeX inclusion contract | `paper/figures/latex_includes.tex` | `bad78636f7e25f94a2d2cae50f299e4b7a46feb1ad890526a1128ae5d554671b` |
| postrun scope audit | `notes/INDEPENDENT_POSTRUN_SCOPE_AUDIT.md` | `f7b365c9e6c8933cf3cbcaf3c96692cbacdaabcc84400bdc629f1d482cb243e4` |
| strict result manifest | `results/result_manifest.json` | `a0b409061c34eff0d68fdc326fe4ec6ff9295895444b857ee161fd77e417292c` |

I made no change to the manuscript, plan, bibliography, source lock, proof,
candidate code, analyzer code, registered result, or frozen figure package.
No network access, candidate run, analyzer run, experiment run, parameter
scan, or numerical analytic evaluation was performed. Regeneration below was
confined to two disposable copies of the frozen evidence trees.

## 2. Independent scientific recomputation and scope-correction gate

I reconstructed the nine rows directly from
`results/EXPERIMENT_RESULTS.json`, independently of the display payload. The
registered order and exact triples are

| $q$ | $n_q$ | $r_q$ | $m_q=n_q/r_q$ |
|---:|---:|---:|---:|
| 2 | 3 | 3 | 1 |
| 3 | 8 | 4 | 2 |
| 5 | 20 | 10 | 2 |
| 7 | 48 | 8 | 6 |
| 11 | 100 | 5 | 20 |
| 4 | 12 | 3 | 4 |
| 6 | 24 | 12 | 2 |
| 9 | 72 | 12 | 6 |
| 10 | 60 | 30 | 2 |

For every row, the raw formula engine and the independently enumerated engine
agree on the four scalar support--exponent pairs

\[
  (r_q,m_q),\qquad (r_q,1/r_q),\qquad (1,n_q),\qquad (1,1).
\]

Testing all 36 row/type pairs gives exactly one pair with source support and
unit exponent:

\[
  (q,j,S_j,E_j)=(2,\kappa\mathrm{pt},3,1).
\]

No scalar-reduction column has both properties in all nine rows. The exact
retained-order collisions are

\[
  r_2=r_4=3,\qquad r_6=r_9=12.
\]

Thus the unique $q=2$ point-cardinality factor
$(1-t^3)^{-1}$ is a real local exception, the authorized negative claim is
only family-uniform, and the exception is not modulus-specific. The
structural control also independently reconstructs as an effective
$C_6/C_2\sqcup C_6/C_3$ action with kernel one, exact labelled-twist
recovery, source supports $3$ and $2$, no period-six source factor, stack
components $BC_2\sqcup BC_3$, and five static inertia sectors.

These computations agree with the controlling
`PASS_WITH_SCOPE_CORRECTION` audit. They support the scoped terminal
classification and do not support the rejected per-row nonattainment
sentence.

## 3. Plan, figure, and caption semantics

### Plan

The title, one-sentence contribution, claims--evidence matrix, abstract plan,
section plan, figure plan, and conclusion plan consistently separate:

- the unique locked $q=2$ scalar exception;
- family-uniform nonattainment across the nine locked rows;
- non-identification of the modulus through $r_2=r_4=3$; and
- the stronger labelled-carrier result from any intrinsic common
  modulus/prime clock.

The plan does not revive the forbidden statement that every row lacks a
source-support/unit-exponent pair. Its A0 statement is the absence of a
common intrinsic modulus/prime clock, not the absence of every local
one-cycle factor. The novelty calibration remains 2/10 and the nonclaims
exclude a new equivariant/orbifold/enhanced/stacky zeta, a universal no-go
theorem, a cross-$q$ canonical coefficient ring, an analytic evaluation, and
Route B.

### Figure 1 and caption

The carrier hierarchy is explicitly definition-sensitive rather than a
universal dominance order. The point-cardinality branch reads “support
$r_q$; exponent $m_q$; unit when $m_q=1$.” The formula panel visibly marks
$q=2$ as the sole locked row/type exception, and the same callout records
$r_2=r_4=3$. The footer and LaTeX caption state only the family-level
conclusion. The caption names the 2008, 2013, 2015, and 2018 constructions as
prior art.

### Figure 2 and caption

All 27 displayed values reproduce the exact nine $(n_q,r_q,m_q)$ triples in
the registered order. The collision panel joins only $(q,r)=(2,3)$ with
$(4,3)$ and $(6,12)$ with $(9,12)$. All 36 scalar cells agree with the raw
formulas. There is exactly one star, border, and crosshatch, at the $q=2$
point-cardinality cell $(3,1)^\star$. Both the figure footer and caption say
that there is no family-uniform starred column and that $r_2=r_4$ prevents
modulus identification. The caption correctly limits the rows to exact
implementation/falsification controls and makes no fit or all-$q$ inference.

### Figure 3 and caption

The regular, trivial, and effective-$C_6$ cases correctly display their
action kernels, labelled-twist recovery, source periods, quotient stacks,
and static inertia counts. The effective control visibly has period-three
and period-two factors but no period-six factor. It is labelled as a
separately typed structural control, not a tenth arithmetic modulus or a
candidate. Neither the figure nor its caption makes a scalar per-row
nonattainment claim.

A direct search of the plan, generators, rendered SVG text/comments, trace,
provenance, QA record, manifest, and LaTeX captions found no forbidden
unqualified per-row “none” claim.

## 4. Citation closure and Walton correction

The BibTeX file contains exactly fourteen unique keys, and the publication
citation-verification record contains the same fourteen keys in the same
order. Every entry has the expected author/title/year/venue identity and its
required DOI, arXiv identifier, volume, article/page field, and
construction/boundary role where applicable. The roles remain properly
partitioned:

- four direct construction records for the 2008 point-order, 2013 labelled,
  2015 orbit-order/orbifold, and 2018 enhanced carriers;
- four quotient/acting-group/centralizer boundary records; and
- six 2023--2026 frontier-context records that are not used as originality
  or implementation authority.

In particular, `Walton2018` is correctly recorded in the publication layer
as *Journal of Number Theory* **192** (2018), 386--405, DOI
`10.1016/j.jnt.2018.03.023`. The frozen design sidecar and source lock
reproduce the historical **189**, 202--223 typo, while
`paper/CITATION_VERIFICATION.md`, `paper/references.bib`, the plan, provenance,
and manifest explicitly preserve the correction-only boundary. No theorem,
result, novelty, or scope claim is changed by the bibliographic repair.

## 5. Asset graph, regeneration, and deterministic closure

I independently recomputed every path, byte count, and SHA-256 entry in the
25-file publication asset tree, all 16 external frozen-evidence bindings, all
16 figure-manifest source bindings, nine generator/include hashes, four
documentation hashes, three planning hashes, nine rendered-output
identities, and all thirteen non-self records in the result manifest. Every
entry resolves to the declared regular file and matches exactly. The asset
directory contains exactly three figure stems and nine rendered outputs; it
contains no bytecode cache.

I then copied Papers 10 and 11 into two separate temporary trees and invoked
the frozen `generate_all.py` once in each tree. Each invocation performed its
own two complete renders. Both invocations reported `PASS`; within each tree
all nine outputs were byte-identical across its two renders. Across the two
trees, and against the frozen package, the following twelve files were
byte-identical:

- all nine PDF/SVG/PNG outputs;
- `DETERMINISM_AUDIT.json`;
- `ASSET_TREE.json`; and
- `FIGURE_MANIFEST.json`.

The frozen output identities independently reproduced were:

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

## 6. Mechanical and original-resolution visual QA

Independent inspection confirmed:

| Stem | PDF pages / size | PDF fonts | PDF raster objects | SVG text / path / image nodes | PNG pixels / dpi |
|---|---|---:|---:|---:|---:|
| `fig1_retention_hierarchy` | 1 / 518.4 x 378 pt | 5 embedded, subset, Unicode; no Type 3 | 0 | 94 / 78 / 0 | 2160 x 1575 / 299.9994 |
| `fig2_nine_row_retention` | 1 / 518.4 x 421.2 pt | 4 embedded, subset, Unicode; no Type 3 | 0 | 137 / 107 / 0 | 2160 x 1755 / 299.9994 |
| `fig3_effectivity_counterexamples` | 1 / 518.4 x 349.2 pt | 6 embedded, subset, Unicode; no Type 3 | 0 | 35 / 38 / 0 | 2160 x 1455 / 299.9994 |

All SVGs parse as XML, retain selectable text and vector paths, and contain
no image node. All PNGs are RGBA and pass the 300 dpi tolerance.

I inspected all three PNGs at original resolution. No clipping, collision,
overlap, illegible annotation, broken arrow, or semantic ambiguity was
observed. The registered row order, all bar/cell labels, the unique star,
both collision pairs, and the structural-control namespace are legible.
Color-dependent distinctions are repeated by labels, position, marker
shape, borders, line style, or hatch. The three figures use consistent serif
and math typography, and no manuscript-style decorative title or chart junk
is present.

## 7. Final disposition

No blocking scientific, quantifier, citation, provenance, determinism,
vector, typography, accessibility, caption, or visual defect was found. The
frozen package satisfies the corrected scope gate and is authorized for
manuscript integration without modification.

`ASSET_PASS`
