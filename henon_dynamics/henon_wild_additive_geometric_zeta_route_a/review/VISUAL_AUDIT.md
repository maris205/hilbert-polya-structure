# Actual visual audit

On 2026-09-05 the implementing agent rasterized the final five-page PDF at 100 dpi and viewed every page. It additionally viewed the scope/reference final pages of rounds 0 and 1. All three rounds are fully rasterized by the release gate.

Following the independently found and repaired checker type-coercion gap, the rebuilt final PDF 045a29475418bc1de741e5058f7d69f7e24bd25c2e01f6c3408473c2959e3481 was rasterized at 85 dpi and all five pages were viewed again. The revised page-four process paragraph correctly states the resolved gap and 58/58 attacks, without clipping or scope reversal. The five pages respectively contain bilingual source framing, geometric/extension proofs, the boundary proof, evidence/controls/scope and references. The last reference-only page is not an empty or padded theorem page; the body occupies four pages.

Observed: legible Chinese glyphs, six keywords per language, correctly rendered nested exponents and the noninteger-residue sign, no clipped formula or table, no overprinted text and no unresolved reference marker. The target exclusions form a coherent paragraph. Route B remains disabled is a separate complete sentence in every round, so page breaks do not reverse its meaning.

Each settled compiler log has zero warnings; all 16 fonts in each round are embedded and subset. These automated facts are also regenerated in paper/COMPILE_REPORT.md. Visual judgement is a human-facing inspection record, not a deterministic semantic proof.
