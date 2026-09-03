# Test report

## Required lanes

- Producer: canonical evidence generated with 17 coefficient, 7 tail, 4 root, and 162 Fourier rows.
- Independent checker: 199 exact ledger rows reconstructed; producer import forbidden by design.
- SymPy: 60 exact symbolic checks of quotient coefficients, coefficient ordering, Turán equivalence, critical expansion, Fourier modes, and zero flux.
- Replay: two isolated temporary-directory productions are byte-identical to the checked artifact.
- Hostile audit: 71 of 71 attacks rejected.
- Optimized execution: all six entry points reject both `python -O` and `python -OO`.

## Strict parsing and ownership

JSON parsing rejects duplicate keys, nonfinite constants, and non-object roots. YAML parsing rejects duplicates, anchors, aliases, merge keys, non-string keys, implicit timestamps, unknown fields, and type substitutions. Repaired-hash mutations target identities, source/evaluator locks, model conventions, theorem fields, collision/nonclaim/source ownership, Route-A fields, scope flags, every ledger, and the finite-evidence boundary.

## Publication checks

The final release gate requires:

- exactly 28 physical files and 27 manifest payloads;
- two fresh fixed-epoch LuaLaTeX builds for each of three substantively distinct rounds;
- byte-identical checked PDFs and `main.pdf == main_round2.pdf`;
- no LaTeX/package warnings, overfull or underfull boxes, undefined references/citations, rerun requests, or missing glyphs;
- all fonts embedded and subset;
- clean extracted text with round sentinels and no unexpected control bytes, `qquad`, `??`, draft markers, or missing-glyph text (Poppler's known DC2/DC3 mapping for two Type-1 large-integral glyphs is explicitly normalized and visually checked);
- successful rasterization of every page.

The manifest gate is run once with `--write` and twice without writes after all artifacts settle.
