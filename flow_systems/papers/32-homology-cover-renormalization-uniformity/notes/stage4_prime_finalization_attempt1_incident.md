# P32 Stage 4′ finalization attempt 1 incident

- Classification: `ORCHESTRATOR_HELPER_ARGUMENT_DEFECT`
- Patch, applied draft, or writer artifact changed: `no`
- Build started: `no`
- Canonical/science/Route state changed: `no`

The first orchestration-helper invocation stopped before token replay, response finalization, revision-bundle construction, or preview build. Its local Ruby wrapper passed `chdir: nil` to `Open3.capture3`, which Ruby rejected before launching the first subprocess. The helper had emitted only a deterministic role/layout-lineage sidecar; that sidecar is regenerated from the same immutable inputs after correcting the wrapper to omit the option when no working directory is requested. This incident is not a patch re-emission, scientific retry, or Stage 4.5 run.
