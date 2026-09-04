# Paper build

`main.tex` uses `\CRevisionRound` to produce three substantive artifacts:

- round 0: Chambers phase-collapse theorem;
- round 1: spectral preimage, edge multiplicity, symmetries, and boundaries;
- round 2: evidence, collision/source audit, limitations, and Route-A gate.

The release gate builds each round twice with LuaLaTeX under the fixed epoch,
requires byte identity, rejects warnings, and makes `main.pdf` byte-identical
to round 2.
