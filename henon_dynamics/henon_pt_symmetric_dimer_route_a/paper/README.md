# C297 manuscript artifacts

`main.tex` is the single conditional source for three substantive rounds.

- Round 0 proves the exact three-chamber propagator and dynamical atlas.
- Round 1 adds the projective Riccati flow and sharp conserved-metric boundary.
- Round 2 adds the complete face table, independent evidence, literature
  ownership, Route-A verdict, and scope firewall.

`main.pdf` is byte-identical to `main_round2.pdf`.  Every archived round is
built twice in isolated directories with two LuaLaTeX passes per build under
`SOURCE_DATE_EPOCH=1788307200`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.
