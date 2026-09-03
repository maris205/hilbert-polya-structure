# P33 Stage 3-prime Round 5 Phase 2A outer-validator incidents

- Classification: `VALIDATOR_RULE_DEFECT_ONLY`
- Evidence-emitter failure: `no`
- Evidence regeneration or retry: `no`
- Official verdict record modified: `no`
- Phase 2B started: `no`

The first invocation of the new outer validation helper stopped before producing a validation artifact because its locally implemented routing assertion required `verified_by` to be a member of every item's `source_reviewer_labels`. That assertion mishandled the Devil's Advocate source item `REV-P33-013`: under the established ARS re-review routing used by the preceding Round-2 and Round-3 validators, the expected verifier is the first non-DA source seat, or `EIC` when the only source label is `DA`.

The second invocation passed all schema, binding, frozen-input, item, and scope checks reached before stopping on a Markdown receipt-marker spelling mismatch: the helper expected machine-style `emitter_invocation_count=1`, while the immutable receipt says `Emitter invocation count: \`1\``. The semantic-audit JSON already carries the machine-readable value and passed. The helper was corrected to recognize the receipt's exact existing prose; neither the receipt nor any evidence artifact was changed.

The immutable Phase-2A verdict had already been emitted exactly once and had passed the official Draft 2020-12 verdict schema. Its `REV-P33-013` row correctly records `verified_by=EIC`. No verdict, anchor, rationale, residual, payload, receipt, or manuscript byte was changed in response to either helper failure. The helper alone was corrected and rerun against the same evidence bytes. These are outer-validator implementation incidents, not Phase-2A evidence retries or lint-guided regenerations.
