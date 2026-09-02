# Manuscript build

`main.tex` uses `CRevisionRound`.  Round 0 contains the complete equilibrium and linear-spectrum theorem and proof, including the resonance-safe meaning of linear boundedness and corrected historical ownership.  Round 1 adds boundary and both-sign audits.  Round 2 adds four exact critical rank cells, independent executable evidence, strict JSON/YAML hostile closure, Route-A firewall, limitations, and declarations.

Each round is compiled twice in isolated fresh directories, two LuaLaTeX passes per build, with fixed epoch `1788307200`.  The manifest demands byte identity, clean settled logs, embedded subset fonts, page/text contracts, and `main.pdf == main_round2.pdf`.
