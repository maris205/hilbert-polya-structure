# Actual compile and visual report

Engine: LuaLaTeX with the installed TeX Gyre Pagella text/math and Droid Sans
Fallback CJK fonts. Fixed epoch 1788566400; optional PDF metadata suppressed.
Each round was built twice in unrelated fresh directories, with two TeX passes
per build. Corresponding PDF bytes matched. All three settled logs have zero
layout, missing-character, citation, reference or rerun warnings and are kept
as compile_round0.txt, compile_round1.txt and compile_round2.txt.

| Round | Pages | PDF SHA256 |
|---|---:|---|
| zero | 3 | 1b9011fdee5bf951edd0e6074bae13dfbbd4cc2984b60ec9928bbfd0443615f1 |
| one | 4 | 02e7c87e766889215e37c2d7ed04661de3514fa9a394fe1fbf606839ce73d04c |
| two / main | 5 | 21ae04e9ec91e508ec4a3ac7cdccb058e70cb03c815047035786a93c103e0db2 |

All final five pages were actually rasterized at 90 dpi and viewed with the
image-viewing tool. Page one: complete bilingual abstract, six bilingual
keywords and source attribution. Page two: lattice formulas, rationality
lemma and Farey induction. Page three: physical clock, return matrix and
floor-wall example. Page four: integrability, fixed-family stopping theorem,
exact evidence population and intact negative scope paragraph. Page five:
scope literal, round marker and bibliography. No visible missing glyph,
cropping, overlap or sign-loss pagination was observed.

The final negative paragraph stays entirely on page four. The final page
contains references rather than hidden mathematical claims. Extracted-text,
embedded/subset-font and every-page raster gates also run on all three
versions in each release. Main PDF is exactly the round-two PDF.
No conference submission or external acceptance is claimed.
