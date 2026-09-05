# Executed deterministic compile and visual audit

All three substantive revisions were compiled twice in independent fresh
directories, with two LuaLaTeX passes per build, fixed epoch 1788566400 and
FORCE_SOURCE_DATE=1. The two PDF byte streams agree for each revision.
The actual settled second-pass logs are retained, without whitespace
normalization, in compile_round0.txt, compile_round1.txt and compile_round2.txt.

| Revision | Pages | SHA-256 |
|---|---:|---|
| Round zero | 3 | 6606f0b62551723634dcc30a563722724e1ae8a5755a7db98f1ab9f4b2dc28d6 |
| Round one | 4 | d6e6218b229ee8457730122ccbe7877acec5429acb0aca7452281c5f62f0788a |
| Round two and main | 5 | 2b7f8516da85c121c8039ae2761cb79702d024280c36034888b761c966f6a7c2 |

Round zero proves complete quotient presentations and resonance. Round one
adds the integer covolume lemma, component formula and accessed-version
counterexample. Round two adds the continuous primitive stratum, arithmetic
entropy, exact Dirichlet tails and the rank-two/every-rank-one cardinality
obstruction. Text inspection verifies the corresponding section changes;
these are not three covers around the same content.

All settled logs pass the warning gate: no LaTeX/package warning, undefined
reference, missing character, overfull or underfull box remains. Poppler
checks find nine embedded, subset fonts in every revision, including the
Droid Sans Fallback CJK face. Extracted text has both abstracts, six English
and six Chinese keywords, valid round markers and no unresolved placeholder.
Every page in every revision was rasterized successfully at 60 dpi.

Actual final visual inspection is separate: all five pages of the final
SHA above were rendered at 90 dpi to /tmp/c388-final-visual-GTKK9o and
opened with view_image on 2026-09-05. Page 1 has complete bilingual abstracts,
keywords and the source relation. Page 2 has complete quotient and resonance
statements. Page 3 has the covolume proof, Gram matrix, table and minimal
matrix. Page 4 has the source correction boundary, torus phases and the
Jensen/Fourier and tail formulas. Page 5 has the ordinary-zeta obstruction,
denominator-labelled evidence boundary, a complete same-page scope paragraph,
and all three references. No missing glyph, cropping, overlapping object or
misleading split of a negative scope statement was observed.

The first compile attempt failed on a malformed title linebreak escape.
It was repaired by using ordinary title text with automatic wrapping.
No compiler diagnostic was suppressed. A subsequent successful rebuild
incorporated the explicit cross-denominator duplicate disclosure. The source
and final PDF above are now frozen for release reconstruction.

The release driver independently rebuilds all three double builds during
both write and nonwrite verification; its manifest carries the final font,
text, page-count and raster receipts. Actual primary-source PDF inspection
and its unavailable structural-preflight dependency are documented separately
in review/SOURCE_PAGE_RECEIPT.md.
