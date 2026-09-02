# Round 10 Stage 2.5 isolated fault-injection receipt

Execution time: `2026-09-02T17:38:27Z`  
Command: `python3 tools/round10_stage2_5_fault_injection.py`  
Decision: **PASS — clean baseline accepted; 4/4 injected faults rejected**

The current unmodified P29 Phase-A/B and claim-core carriers were accepted
first. Four mutations were then tested strictly in memory or under disposable
temporary directories:

| Case | Expected | Observed |
|---|---|---|
| Change batch `stage3_authorized` from `false` to `true` | REJECT | REJECT |
| Replace the Phase-A/B manuscript binding with a zero SHA-256 | REJECT | REJECT: stale binding |
| Upgrade one anchorless evidence row to an injected URL | REJECT | REJECT: invalid/unregistered anchor |
| Change official E6 from `skipped_no_revision_evidence` to `completed` with an unresolved zero hash | REJECT | REJECT: stale/blocking drift carrier |

No registered workspace artifact was mutated by this test. The validator
SHA-256 was
`7c2fc5ff680ea477265be87120f8a5d223b755f47278d5b8634b55d4b74f7867`.
This negative-control receipt is a fail-closed implementation check, not a
claim of theorem correctness, scientific reproducibility, or global semantic
completeness.

This check verifies disclosure and claim-to-provenance fidelity. It does not
judge whether the experiment was correctly designed, run, statistically
adequate, or reproducible by ARS.
