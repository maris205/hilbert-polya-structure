# Independent Paper-Plan, Citation, and Figure Review

**Review date:** 2026-08-15 UTC  
**Reviewer role:** fresh independent asset reviewer  
**Scope:** Paper 10 planning, citation metadata, deterministic publication
figures, provenance, and scientific semantics only  
**Candidate execution:** none  
**Network access:** none  
**Files changed by this review:** this review file only

## Bound review object

The reviewed package is bound to the following frozen identities:

| Object | SHA-256 | Recomputed |
|---|---|---|
| `paper/figures/ASSET_TREE.json` | `16df3d3468ad0c19c75c4fdc796f7b68e709a8bd79ea4f381a40ea1b815fa2a2` | yes |
| `PAPER_PLAN.md` | `972c13d2551e51bb2781bf7f177314812460c161af0ce1daa748eeff413cbe8a` | yes |
| `notes/CITATION_VERIFICATION.md` | `b4596ed56aee5eb47314221bba681098e45011a3fdc9dafc201315e597a1bfc6` | yes |
| `paper/references.bib` | `64bb83a541b728965f4a67045108d1fed814582f93b312b13e4c607500635308` | yes |
| `paper/figures/FIGURE_MANIFEST.json` | `a54fad8c7cdc23e0b49543147924670a73f8a2e8c54373230837fe0706572209` | yes |

All 25 files framed by `ASSET_TREE.json` were independently rehashed and
matched their declared byte counts and SHA-256 values.  The following eleven
external frozen evidence objects were also independently rehashed and matched
the bindings used by the figure loader:

- source lock `aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2`;
- proof package `2eafe71f32c452ff8a20a6818ccb43082e02b866db7353e26c36ff432f1b2a4c`;
- novelty assessment `6ee0fe2aff13c2d4329496e32f2d6aa190a92a3c3b4904168a21828b646de0a5`;
- claims--evidence matrix `03424a71fc8716618545a6c7c8b0fd05f5ad744cff034255ab0337012da0303d`;
- independent source review `a551784d205d9ef52ce6a493ab66cb7295a4a9dadbeb8bb2353fc58e3011dff5`;
- deployment review `990b1762e2aea6c379288854cca918cc4bbe87b7ea7ccadef7458ecfcf6988f0`;
- raw result `8dceb1b8a63db462c1fd55a242ea35de974f73b6c80da68517b91c9eebb214ff`;
- independent result review `29264a8fd97d3acf4435ed807294bffcda0844a48728d8572083d92a3bcf5b58`;
- strict result manifest `db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658`;
- official result report `1ece7db3fbee75bcecaecb0ad05f89fe88699c4231bea80581f382f33ed3aa6e`;
- official validation report `f94dbfb28a71aea4dac5e89a8bc2a622bba092b66098c2fc2217ceba19a8ad5a`.

## Independent regeneration and mechanical QA

I copied the complete Paper-10 project into two independently created
temporary trees and ran `paper/figures/generate_all.py` once in each tree.
Each invocation itself performed the required two rendering passes.  Both
trees reported exactly three stems and nine rendered outputs.  Within each
tree all nine files were byte-identical across the two internal passes;
across the two isolated trees, all nine outputs and
`FIGURE_MANIFEST.json` were also byte-identical.  The cross-tree manifest
digest was the frozen
`a54fad8c7cdc23e0b49543147924670a73f8a2e8c54373230837fe0706572209`.

The independently reproduced output hashes were:

| Output | SHA-256 |
|---|---|
| `fig1_quotient_layers.pdf` | `466a128dda7072368974f9b2eee82f7cf69e6d542a4d39f3fb1c36339f7d33aa` |
| `fig1_quotient_layers.svg` | `edfbf4893d2c7e08d0109082e7a1eec9faae104696e60560751315d7fc6d5d7e` |
| `fig1_quotient_layers.png` | `87ae66cbeab07aa7302367ef43bdf268e8254f11b00deac721443b1bebf40b3f` |
| `fig2_nine_modulus_ledger.pdf` | `f86ff8e50c5a138996c8f379fa0309ddc6071cffca1d540b81e07304dae2dd73` |
| `fig2_nine_modulus_ledger.svg` | `5747cc8f5a8f30eeb4017441c0be932ab7ee6c4a92b53c4b39a466039780d61c` |
| `fig2_nine_modulus_ledger.png` | `6a5845706c035454533a1d39bd6f8daa439d3615189f4f4ec7220182ed2a59c3` |
| `fig3_clock_semantics.pdf` | `0df9de8544c05e60749d456244c2920ac15c03a8bc5f5011a66f8d2c5e8cee33` |
| `fig3_clock_semantics.svg` | `894b31b8ad935a49d7ad3a1179a256bb4526e6da6dc1da372756af853bfd849d` |
| `fig3_clock_semantics.png` | `80d305f71a458713876f77d40db1f309bd732798d0c1f3ca1ec2291dcdb2ff92` |

Independent file inspection confirmed:

- every PDF is one page, contains zero raster-image objects, has zero Type-3
  fonts, and uses three embedded, subset, Unicode-mapped CID TrueType fonts;
- every SVG parses as XML, has selectable text (50, 107, and 49 text nodes),
  and contains zero image nodes;
- the PNGs are respectively 2160x1440, 2160x1530, and 2160x1470 RGBA at
  299.9994 dpi in both dimensions;
- there is no bytecode cache in the reviewed figure directory;
- the figure loader imports no candidate implementation, and its frozen
  input gate rejects changed hashes, modulus order, lifecycle counts,
  forbidden counters, failed controls, or altered quotient semantics.

Original-resolution inspection found no clipping, unintended overlap,
unreadable text, hidden annotation, or color-only scientific distinction.
The registered order `2,3,5,7,11,4,6,9,10`, the prime/composite divider,
and the `n/a` composite reversor cells are all visually unambiguous.

## Scientific and narrative audit

The plan is appropriately conservative.  It assigns all-$q$ authority to
the proof, calls the nine rows development-seen falsification controls, fixes
novelty at 2.5--3/10, enumerates direct prior collisions, and expressly
disclaims a new centralizer classification, zeta construction, Hecke result,
prime selector, Route-B result, or impossibility theorem for enriched
quotients.  The terminal classification remains exactly

`CENTRALIZER_CYCLIC_TORSOR_CERTIFIED / A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.

The displayed nine-modulus ledger agrees with the frozen source and result
records.  Its cardinalities obey, row by row,

`|E_q| = |CV_q| + discard`, `|CV_q| = |C_q|`,
`|C_q| = |C_q^1| |im N_q|`, and
`|CV_q| = ord_q(A) * (# cyclic A-orbits)`.

The norm-image counts are `1,2,2,6,10,2,2,6,2`, in agreement with
`phi(q)` away from five and `phi(q)/2` at moduli divisible by five.  The
full cyclic quotient count is one at all five prime and all four composite
controls.  Full-shell and cyclic-locus counts remain separated at `q=5,11,10`.
The five prime reversing counts are `1,1,2,1,2`; composite reversing cells
are correctly marked unaudited rather than zero.

Figure 3 correctly separates three different data items:

1. the source period `ord_q(A)`;
2. native primitive period one on either coarse quotient because
   `A in C_q^1 subset C_q`; and
3. the externally supplied specialization `z -> q^(-s)` or length `log q`.

The composite cards correctly show that the one-class mechanism is not an
intrinsic prime selector.  The enriched Burnside, equivariant, orbifold,
stacky, groupoid, twisted-sector, and Hecke boundaries remain explicitly
live and untested.

## Citation inventory and metadata audit

The bibliography contains exactly 14 unique keys, exactly the locked set.
It contains 11 DOI-bearing `@article` records and three arXiv-only `@misc`
records; 13 entries carry an e-print identifier, with Gaspari 1994 the sole
published record without one.  Titles, years, journals, volumes, issues,
pages, DOI strings, and arXiv identifiers otherwise agree with the bounded
metadata lock.

One publication-blocking metadata defect remains.  Four fields contain a
literal ASCII quotation mark in place of the required TeX umlaut command:

- line 2: `Neum{"a}rker` is currently stored as `Neum{"a}rker` **without
  the backslash before the quotation mark** (byte sequence `{`, `"`, `a`,
  `}`);
- lines 15 and 28: `P{"a}r` is likewise stored without that backslash;
- line 69: `f{"u}r` is likewise stored without that backslash.

In exact source spelling, the defective tokens are `Neum{"a}rker`,
`P{"a}r`, and `f{"u}r` with the character after `{` being U+0022 rather
than a TeX control sequence.  They will not reliably typeset the verified
metadata *Neumärker*, *Pär*, and *für*.  Repair may use valid escaped TeX
(`Neum{\"a}rker`, `P{\"a}r`, `f{\"u}r`) or UTF-8.  Because
`references.bib`, the asset tree, and figure manifest are hash-bound, this
repair requires regeneration and a fresh asset review.

## Figure wording blocker

Figure 1, panel C, places **“never mixed”** in the `noncyclic strata` column
for the reversor extension.  Read literally, this says that noncyclic strata
are never merged.  That contradicts the frozen split-prime statement: at
`p=11` the fixed reversor swaps and merges the two punctured-eigenline
orbits.  The proved statement is narrower: reversing symmetry never mixes
the cyclic locus with its noncyclic complement.  The cell should therefore
say, for example, **“not mixed with CV”**, while retaining the separate fact
that the split eigenline orbits may merge.  This wording is claim-bearing,
so it is a release blocker rather than a cosmetic suggestion.  Repairing it
also changes the figure generator/output hashes and requires regeneration.

## Required bounded repair

Only the following asset-layer repair is required; no scientific source,
candidate, code, result, modulus, or claim change is authorized:

1. correct the four malformed umlaut encodings in `paper/references.bib`;
2. replace Figure-1 panel-C `never mixed` with wording that explicitly means
   cyclic and noncyclic loci are not mixed;
3. rebuild the three-format figure package, asset tree, and figure manifest;
4. request a fresh independent asset review against the new hashes.

All other reviewed plan, provenance, determinism, quality, and scientific
semantics checks pass.

**Final asset-review verdict: REPAIR REQUIRED.**  `ASSET_PASS` is withheld
until both release blockers are corrected and the regenerated package passes
a fresh independent review.
