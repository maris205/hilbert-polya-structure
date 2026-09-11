# P215 Review A build01 artifact DATA accepted

2026-09-11 UTC. Independent read-only checker final invocation chunk `1ae5fd`
exited zero and passed 536 checks. The exact tree has 160 regular files, zero
symlinks, 15 controller/supervisor exit roles all zero, and 25 stderr files
inside the build tree all empty. Root's binding-side captures remain separate.

All eight cold sources match the accepted source manifest. Runtime/source
before and after records agree. All 67 unique absolute final-FLS inputs occur
in the fresh 227-row runtime manifest. Eight pass snapshots, final products,
bibliography and extracted text close. All 16 fonts are embedded, subset and
Unicode mapped. Six page PNGs are present.

The final PDF is 200,921 bytes, SHA256
`ff04cdb46b6072398119a962a9038303d3665222da048c8eb14a103105d55f85`.
The sole 52-byte diagnostic line is exactly
`main.log:3: file:line:error style messages enabled.` It reports pdflatex's
enabled diagnostic formatting and is not an error message, warning, undefined
reference, box overflow or missing glyph.

Two checker failures remain preserved: `f3a185` incorrectly expected 26
stderr files inside the tree, and `d6ef09` incorrectly reused P214's 58-input
FLS constant instead of P215's actual 67. `INITIAL_FAILURE.md` and
`SECOND_FAILURE.md` record the exact corrections. Neither failure changed the
build or weakened current coverage. HOLD_EXTERNAL.
