# Paper build

`main.tex` is controlled by `\CRevisionRound`.

- round 0: frozen generator and quartic upper bound;
- round 1: complete conditional-projection lower induction and sharp theorem;
- round 2: independent polynomial evidence, ownership, and Route-A closure.

The release gate builds every round twice from a clean temporary directory under fixed LuaLaTeX metadata, requires byte identity, scans settled logs and source control characters, checks revision tokens, embedded subset fonts, and rasterized pages, and requires the final PDF to equal round 2.
