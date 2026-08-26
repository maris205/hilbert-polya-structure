# Round 1 resolution

All three internal hostile-review findings were resolved.

| Finding | Resolution | Location |
|---|---|---|
| R1.1 divisibility-directed terminology | Added an explicit statement that `a|b` implies `H_b<=H_a` and `L_b<=L_a`, and explained why all moduli are retained | `sections/4_subgroup_counts.tex` |
| R1.2 minimality phrasing | Removed “smallest nonabelian order” and retained only “small explicit order-eight example” | `sections/8_conclusion.tex` |
| R1.3 overfull path | Shortened the filename in manuscript prose | `sections/7_scope_controls.tex` |

After revision, the exact control script and full `pdflatex -> bibtex ->
pdflatex x2` build were rerun.  Final QA is recorded in `FINAL_QA.md`.

