# Manuscript artifacts

`main.tex` holds three substantive conditional versions. `main_round0.tex`, `main_round1.tex`, and `main_round2.tex` select domain/spectrum, full scattering, and heat/symmetry/obstruction endpoints respectively. `main.pdf` is byte-identical to `main_round2.pdf`.

Build with `python3 -B ../code/c383_release_manifest.py --build-pdfs`. Each round is compiled in two fresh directories with two LuaLaTeX passes, a fixed source epoch, Unicode math, and an embedded CJK font. Settled logs, page counts and hashes are retained. The release checker rejects text extraction controls and missing-glyph/reference warnings rather than suppressing them.

The real settled logs are `build_round0.txt`, `build_round1.txt`, and `build_round2.txt`; only their filename suffix differs from LuaLaTeX's `.log` output. They are included in the release manifest and are not ignored by Git.
