# Paper 27 Stage-2.5 experiment-provenance gap

Stable issue: **`P27-IL-SERIOUS-EXP-DECL-1` — SERIOUS / BLOCKING**.

The manuscript reports project-owned computational executions, tests, finite classifications, or certificates. The repository contains substantial source, result, freeze, test, validation, and receipt artifacts, but ARS does not permit an agent to infer or sign the scholar-owned intake decision from those files.

Required closure sequence:

1. The scholar explicitly confirms `status=experiments_declared`, `declared_by=scholar`, and the confirmation time for Paper 27.
2. Transcribe the already frozen Round-2--8 experiment packages into schema-valid `experiment_provenance[]`; do not invent omitted runs or results.
3. Bind experiment-backed registered claims through `planned_experiment_ids[]` and generate `experiment_alignment_results[]`.
4. Re-run C4/D7 and the seven failure modes on the exact resulting passport.

Required boundary: **This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.**
