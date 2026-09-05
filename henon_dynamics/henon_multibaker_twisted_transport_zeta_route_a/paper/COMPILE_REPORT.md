# Compilation and PDF audit

Executed on 2026-09-05 with LuaLaTeX and fixed epoch 1788566400. Each of the
three rounds was built twice in separate fresh directories, each with two
passes. PDF bytes agree within each pair. The final `main.pdf` equals Round 2.

| Round | Pages | Embedded and subset fonts | SHA-256 |
|---|---:|---:|---|
| 0 | 2 | 7 | `40d2fc73539a7ca88ce65d52004f2b7bfab273037051dc62bf51ddc8417281b1` |
| 1 | 4 | 7 | `5343e0e1de2a908aefe62d3ce66487bd174236fbc7aa631a1cbb77fa3e94aece` |
| 2 | 5 | 8 | `c1b9500e5dc5fdb83f6dc3b8163f49d0e70a4810137fcd7f6baa54a123ac9089` |

All settled logs are retained as compile_round0.txt through compile_round2.txt.
They contain no layout, missing-glyph, undefined-reference or citation warnings.
Every font is embedded and subset. All 11 round pages rasterize successfully.
Text extraction has no control characters other than newline/page breaks,
no unresolved markers, and six English and six Chinese keywords in each round.

The initial legacy math font produced nonprinting text-extraction codes in
binomial delimiters. Switching to Unicode mathematics fixed extraction; an
unsupported set-difference glyph was replaced by an explicit membership
definition. No warning was hidden or suppressed. There is no venue-specific
page limit, no submission claim, and no omitted figure asset.

Visual inspection of the final first page and the diffusion/relaxation page
confirmed readable bilingual text, complete formula rendering, clear theorem
boundaries and no clipping or overlap. The automated raster audit covers all
pages and all rounds; the visual inspection is explicitly a selected-page
check rather than a claim to manually inspect every raster.
