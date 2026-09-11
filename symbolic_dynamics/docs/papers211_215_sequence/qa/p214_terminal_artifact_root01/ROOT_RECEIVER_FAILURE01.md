# P214 terminal root receiver failure 01

2026-09-11 UTC. Root's first combined reception command was invalid as a
whole PASS. It requested `P214_FINAL_QA.md` from the batch root instead of its
actual terminal-root directory, then invoked the independent one-use checker
against its existing exclusive `RESULT.json`. The checker correctly failed
with `EEXIST`. Because later commands were separated by semicolons, the final
successful 342-row manifest check masked that intermediate failure in the
shell's overall exit status.

The manifest's individually printed `OK` rows retain direct evidence, but the
combined command and failed checker receive no PASS credit. No artifact was
changed. Root uses a disclosed exact checker copy whose sole diff is the new
exclusive output name `ROOT_RESULT.json`.
