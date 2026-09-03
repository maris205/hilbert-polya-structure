# Paper artifacts

- `main.tex`: one source with conditional revision sections.
- `main_round0_original.pdf`: operator/discriminant, Floquet, and negative
  atlas revision.
- `main_round1.pdf`: adds the full positive atlas, gap asymptotic, and IDS/DOS.
- `main_round2.pdf`: adds evidence, source/collision audit, and Route-A scope.
- `main.pdf`: byte-identical copy of round 2.
- `COMPILE_REPORT.md`: deterministic build and PDF audit.

The release script compiles each revision twice from a fresh temporary
directory with LuaLaTeX and the fixed epoch `1788393600`; checked-in bytes must
match both builds.
