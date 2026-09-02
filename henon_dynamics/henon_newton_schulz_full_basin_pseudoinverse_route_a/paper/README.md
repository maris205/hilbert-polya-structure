# Manuscript artifacts

`main.tex` is controlled by `CRevisionRound` and produces three substantive archives:

- round 0: full square basin and all Jordan boundaries;
- round 1: Moore–Penrose iff basin and all canonical-alpha faces;
- round 2: exact evidence, collision, Route-A, and nonclaim closure.

`main.pdf` is a byte-identical alias of round 2. The release checker performs two fresh deterministic builds per round, rejects settled warnings, verifies revision tokens, requires embedded subset fonts, and rasterizes every page.
