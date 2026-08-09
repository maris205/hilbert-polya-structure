# Test report

**Date:** 2026-08-09
**Command:** `./code/run_c24.sh`
**Outcome:** `PASS`

The release command regenerated the exact producer certificate, ran the
independent checker, and executed nine regression/mutation tests.

Producer summary:

```json
{"states":7,"primitive_cycles":828,"eventually_positive":146,"character_singular":21}
```

Independent checker:

```text
literal_source_lock                         PASS
seven_state_fourteen_edge_graph            PASS
mobius_trace_completeness_oracle           PASS
independent_eventual_positive_ledger       PASS
singular_character_locus_counts            PASS
claim_boundary_and_center_sign             PASS
```

Mutation/regression suite:

```text
Ran 9 tests
OK
```

The tests explicitly reject a transposed edge convention, right-multiplied
chronology, move-word-only orbit identity, proper-power promotion,
phase-dependent positivity selection, and silent finite assignment to the
21 character-singular cycles.

The LaTeX note compiled with `latexmk -pdf -interaction=nonstopmode
-halt-on-error main.tex`.  The final log contains no undefined references,
LaTeX warnings, or overfull/underfull boxes.  The PDF has five pages.
