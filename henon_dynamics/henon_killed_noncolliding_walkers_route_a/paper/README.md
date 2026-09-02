# Manuscript builds

`main.tex` is parameterized by `\CRevisionRound`.

- `main_round0_original.pdf`: determinant and complete spectrum.
- `main_round1.pdf`: adds absorption, QSD, and Doob conditioning.
- `main_round2.pdf`: adds boundary, evidence, scope, source, and AI-use audit.
- `main.pdf`: byte-identical to round 2.

The release program performs two fresh LuaLaTeX passes for each of two fresh
builds per round under `SOURCE_DATE_EPOCH=1788393600`, compares archived
bytes, rejects layout/reference warnings, checks fonts and text sentinels, and
renders every page with Poppler.
