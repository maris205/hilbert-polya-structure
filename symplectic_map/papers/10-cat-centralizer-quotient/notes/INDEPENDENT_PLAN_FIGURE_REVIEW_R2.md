# Independent Paper-Plan, Citation, and Figure Review: Round 2

**Review date:** 2026-08-15 UTC  
**Reviewer role:** fresh independent bounded-repair and regression reviewer  
**Scope:** the two Round-1 asset blockers, regenerated figure assets,
determinism, provenance, plan/citation bindings, and scientific semantics only  
**Candidate execution:** none  
**Network access:** none  
**Files changed by this review:** this Round-2 review file only

## Bound review object

This review first recomputed the identities supplied for the bounded repair.
Every identity matched byte for byte:

| Object | SHA-256 | Recomputed |
|---|---|---|
| Round-1 independent review | `97f971328996efae866356bdc2c4715a68fcb470dcbe64029d7758d1ec73256a` | yes |
| `paper/figures/ASSET_TREE.json` | `33b8e1d767221529ff2b97fddca0145b1f9724cae924c37afa2847ecfc2bc9d6` | yes |
| `paper/references.bib` | `1ccce7ade3079ca995f00058f4811bdd02a9062d8038b27be2f967f480fe8699` | yes |
| `paper/figures/FIGURE_MANIFEST.json` | `1a2c7de68772ddeb5c614d0ade89a48710e93a3e5a5ff4a393db5c6f3cd4c2ab` | yes |
| Figure-1 PDF | `ac8b29c810881e6383fb3f8b7cb55c602e052ef1677def5643d540b8ee12feb3` | yes |
| Figure-1 SVG | `4d2a340a59b52c440bc9c408a76f06d840ade8d7d900febf88a5cd91d6764d28` | yes |
| Figure-1 PNG | `70ceb2f65befdfd558bc241ff4edb24dc76a9375bb7e9669b1cba4f1e13ebfce` | yes |

All 25 files framed by the new asset tree were independently rehashed and
matched both their declared byte counts and SHA-256 values.  Its eleven
external frozen-evidence bindings also matched.  In particular, the source
lock, proof, novelty, claims matrix, source review, deployment review, raw
result, result review, result manifest, official report, and official
validation hashes are unchanged from Round 1.  The old Round-1 review itself
is preserved at the bound digest above.

## Round-1 blocker closure

### Exact UTF-8 bibliography metadata

`paper/references.bib` is valid UTF-8.  Direct code-point inspection found
exactly the intended repaired strings:

- `Neumärker`: one occurrence;
- `Pär`: two occurrences, one in each Kurlberg record;
- `für`: one occurrence in *Monatshefte für Mathematik*.

Equivalently, the file contains three U+00E4 code points and one U+00FC code
point, with no U+FFFD replacement character.  The malformed Round-1 ASCII
spellings `Neum{"a}rker`, `P{"a}r`, and `f{"u}r` occur zero times.

The bibliography has exactly 14 unique keys.  They match the fourteen
source-lock headings in `notes/CITATION_VERIFICATION.md`, in the same order:

`BaakeNeumaerkerRoberts2013`, `KurlbergRudnick2000`,
`KurlbergRosenzweigRudnick2007`, `GuseinZadeLuengoMelle2015`,
`Zegowitz2017`, `Miles2017`, `Gaspari1994`,
`BaakeRobertsWeiss2008`, `Marais2014`, `Stasinski2016`,
`NoferiniWilliams2024`, `TanLi2025`, `Chandra2026`, and `Walton2018`.

### Figure-1 reversor semantics

The repaired Figure 1 says both **`pairs d,-d`** and **`not mixed with CV`**
in its reversor row.  These phrases were verified in the generator, SVG
selectable text, and independently extracted PDF text.  The obsolete phrase
`never mixed` is absent.

The two cells now make the intended distinction exactly: the reversor may
pair the labels $d$ and $-d$ inside the noncyclic complement, while it does
not mix that complement with the cyclic locus $\mathrm{CV}_q$.  This is
consistent with the split-prime control: at $q=11$, Figure 2 shows three
full-centralizer shell orbits but two reversing-group shell orbits, so the two
noncyclic punctured-eigenline orbits may merge while the cyclic orbit remains
separate.  The figure trace, provenance, and QA text all state the same
narrow semantics; none claims that noncyclic orbits can never merge.

Both Round-1 release blockers are therefore closed without a scientific
source, candidate, result, modulus, or claim change.

## Independent isolated regeneration

I constructed two fresh temporary trees containing only the framed asset
package and the exact frozen inputs required by its read-only figure loader.
I invoked `paper/figures/generate_all.py` once in each tree.  Each invocation
performed its own two rendering passes, so the audit covered two isolated
complete builds and four internal render passes.

Both isolated builds:

- reported `PASS`;
- produced exactly three stems and exactly nine PDF/SVG/PNG outputs;
- were internally byte-deterministic across their two passes;
- reproduced all nine reviewed workspace outputs byte for byte;
- reproduced `DETERMINISM_AUDIT.json`, `ASSET_TREE.json`, and
  `FIGURE_MANIFEST.json` byte for byte;
- matched one another for all nine outputs and all three audit/manifest
  objects; and
- created no bytecode cache.

The independently reproduced output hashes are:

| Output | SHA-256 |
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

The cross-build manifest digest is the bound
`1a2c7de68772ddeb5c614d0ade89a48710e93a3e5a5ff4a393db5c6f3cd4c2ab`.

## Mechanical, vector, font, and visual regression

Independent inspection of the final files confirmed:

- every PDF is one page, contains zero raster-image objects and zero Type-3
  fonts, and uses three embedded, subset, Unicode-mapped CID TrueType fonts;
- every SVG parses as XML, contains zero image nodes, and retains selectable
  text (51, 107, and 49 text nodes respectively);
- the PNGs are respectively 2160x1440, 2160x1530, and 2160x1470 RGBA at
  299.9994 dpi in each direction; and
- no bytecode cache exists in the reviewed figure directory.

All three PNGs were freshly inspected at original resolution.  Text and
mathematics are legible; no panel, label, callout, marker, or annotation is
clipped or unintentionally overlapped.  Claim-bearing distinctions do not
depend on color alone: they are repeated through text, hatching, borders,
markers, geometry, ordering, or exact annotations.  The corrected Figure-1
reversor row is fully visible.  Figure 2 retains the registered modulus order,
prime/composite divider, exact quotient counts, and `n/a` composite reversor
cells.  Figure 3 continues to distinguish source periods, native
period-one quotient dynamics, external modulus specialization, prime
non-specificity, and the live untested enriched boundary.

## Plan, citation, science, and scope regression

The following Round-1 scientific/planning anchors are unchanged:

| Object | SHA-256 |
|---|---|
| `PAPER_PLAN.md` | `972c13d2551e51bb2781bf7f177314812460c161af0ce1daa748eeff413cbe8a` |
| `notes/CITATION_VERIFICATION.md` | `b4596ed56aee5eb47314221bba681098e45011a3fdc9dafc201315e597a1bfc6` |
| Figure-2 PDF | `f86ff8e50c5a138996c8f379fa0309ddc6071cffca1d540b81e07304dae2dd73` |
| Figure-2 SVG | `5747cc8f5a8f30eeb4017441c0be932ab7ee6c4a92b53c4b39a466039780d61c` |
| Figure-2 PNG | `6a5845706c035454533a1d39bd6f8daa439d3615189f4f4ec7220182ed2a59c3` |
| Figure-3 PDF | `0df9de8544c05e60749d456244c2920ac15c03a8bc5f5011a66f8d2c5e8cee33` |
| Figure-3 SVG | `894b31b8ad935a49d7ad3a1179a256bb4526e6da6dc1da372756af853bfd849d` |
| Figure-3 PNG | `80d305f71a458713876f77d40db1f309bd732798d0c1f3ca1ec2291dcdb2ff92` |

The nine-row cardinality and quotient ledger remains unchanged.  It keeps
the full shell separate from the cyclic locus, reports one full cyclic
quotient class for prime and composite controls alike, marks composite
reversor entries unaudited rather than zero, and attributes all-$q$ authority
to proof rather than finite rows.  The clock figure still separates source
period, native quotient period one, and the externally supplied
$z\mapsto q^{-s}$ or $\log q$ label.  No enriched Burnside, equivariant,
orbifold, stacky, groupoid, twisted-sector, Hecke, transfer, Fredholm, or
quantum construction is claimed or tested.

The terminal classification is unchanged:

`CENTRALIZER_CYCLIC_TORSOR_CERTIFIED / A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.

No manuscript, source/proof, candidate implementation, execution result, or
registered lifecycle file was modified or reclassified during this review.

**Final asset-review verdict: ASSET_PASS.**
