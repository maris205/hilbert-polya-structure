# P32 Stage 4′ finalization attempt 2 incident

- Classification: `ORCHESTRATOR_BUNDLE_SCHEMA_ADAPTER_DEFECT`
- Patch, applied draft, or writer artifact changed: `no`
- Preview build started: `no`
- Canonical/science/Route state changed: `no`

The second orchestration-helper invocation completed the independent token replay and generated provisional post-apply audit views, then stopped fail-closed when the official `revision-evidence-bundle/1.0` validator rejected the helper's extra `bytes` members in artifact references. The underlying paths and SHA-256 values were correct; the official schema accepts only `path` and `sha256` in that bundle. The helper was corrected to use a schema-specific artifact serializer and will regenerate the derived views from the same immutable patch/apply chain. This is an outer-wrapper correction, not a patch re-emission, scientific retry, evidence retry, or Stage 4.5 run.
