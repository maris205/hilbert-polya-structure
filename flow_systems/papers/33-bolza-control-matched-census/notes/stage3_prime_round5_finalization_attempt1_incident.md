# P33 Stage 3′ Round 5 finalization attempt 1 incident

- Classification: `OUTER_FINALIZER_FIELD_RENDERING_MISMATCH`
- Phase 1, Phase 2A, or Phase 2B evidence changed: `no`
- Manuscript, science/results, Route, or initial-system state changed: `no`
- Terminal output emitted before stop: `no`

The first terminal-finalizer invocation stopped fail-closed before writing any terminal receipt because its independent author-field reconstruction expected the older phrase `They additionally state as their limitation rationale:`. The immutable Round-5 Phase-2B matrix uses the semantically explicit phrase `Decline justification:` and had already passed the official ARS synthesis checker. The outer finalizer was corrected to require that exact Round-5 rendering while retaining byte-exact comparison of the author response and decline justification. This correction does not modify, retry, or reinterpret either evidence phase.
