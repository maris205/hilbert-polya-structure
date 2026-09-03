# Compile report

All three revision rounds were compiled twice from fresh temporary directories
with LuaLaTeX, `SOURCE_DATE_EPOCH=1788393600`, and the frozen trailer ID.  Each
pair was byte-identical, and `paper/main.pdf` is byte-identical to round 2.

| round | pages | bytes | SHA-256 |
|---|---:|---:|---|
| 0 | 2 | 41,303 | `a060ef72a42e7bf896128596f689470337caec33fc798d7e99eb891884bd3c3a` |
| 1 | 2 | 47,274 | `2185d3deee561d61e865c9fec4334eebfecf3a2617224cb31f077e393082ab2b` |
| 2 / main | 2 | 49,480 | `4c1e9b10af22eaff1401790668e797f32d41bd2151a95251d621473c75cf77e2` |

The round hashes are pairwise distinct.  Each PDF has seven font rows, all
embedded, subset, and Unicode-mapped.  Log gates found no warning, overfull or
underfull box, undefined reference, missing character, or missing glyph.
Every page rasterized nontrivially.  Extracted text contains no forbidden
control byte, literal `qquad`, unresolved `??`, or verification placeholder.
Visual review confirms that the former source-only orphan page is gone and the
two-page final layout is readable.
