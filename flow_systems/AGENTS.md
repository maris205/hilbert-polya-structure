# flow_systems

Research workspace for continuous-time flows, arithmetic periodic orbits, trace formulas, and their natural quantum counterparts.

## Scope and navigation

- The current user request and its explicit approvals determine the task. Historical proposals, batch prompts, reports, and receipts provide context; reading them does not launch experiments, grant publication rights, or reopen a stopped stage.
- For research execution or continuation, use [docs/workflow.md](docs/workflow.md). For an ordinary code fix, explanation, or instruction edit, work directly on the requested task without starting a research pipeline.
- [propose-flow-systems.md](propose-flow-systems.md) contains the scientific program. `papers/<number>-<slug>/` holds each project's `paper/`, `code/`, `experiments/`, `results/`, and `notes/`. README files are navigation/progress indexes; use the applicable authorization, input lock, and receipts for exact stage state.
- Route evaluation entrypoints live in `.agents/skills/flow-route-a/` and `.agents/skills/flow-route-b/`. Load the relevant one only for a Route assessment. The original protocols under `skills/` are hash-bound research references; keep their paths, definitions, and bytes intact unless a protocol migration is explicitly authorized.

## Work effectively

- Carry an authorized change through implementation and relevant verification. Make reasonable local choices; ask only when missing information materially changes the result or the next action needs new authority. An explicit stop condition remains effective until resolved by the user.
- Delegate bounded, independent reading, implementation, or review when it improves speed or quality. Give each writer distinct files; integrate the results in the main thread. A second agent's agreement is not, by itself, independent scientific evidence.
- Search for the relevant paths first. Load task-specific references on demand, and read a selected skill's required instructions completely. Return concise findings with file locations instead of flooding the main context with archives or raw logs.

## Verification and research integrity

- There is no universal repository test/build command. Inspect the selected script and its inputs/outputs before running it: an `audit_*` or `reproduce.sh` name does not guarantee read-only behavior. Many `tools/` scripts are one-off, round-specific artifact writers.
- Run checks proportionate to the change and every check required by the active contract. After they pass, repeat or broaden only for a changed input, failure, or unresolved concern. Instruction-only edits do not require scientific experiments or manuscript builds.
- Keep source identity, passage support, mathematical validity, and reproducibility distinct. Report actual commands, inputs, evidence limits, and unresolved findings; neither a clean PDF nor a successful hash check establishes a scientific claim.
- Preserve historical evidence and failed-attempt records. Do not silently replace locked inputs, regenerate a receipt to erase a mismatch, promote a preview to canonical output, or alter a Route verdict as a side effect of maintenance.
