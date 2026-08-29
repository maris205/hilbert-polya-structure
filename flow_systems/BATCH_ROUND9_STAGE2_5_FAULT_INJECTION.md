# Round 9 Stage 2.5 isolated fault-injection receipt

Execution time: `2026-08-29T06:35:47Z`
Command: `python3 tools/round9_stage2_5_fault_injection.py`
Decision: **PASS — all injected provenance faults failed closed**

The current unmodified Paper-24 scholar intake and its complete experiment
transcription were accepted first. Three isolated mutations were then tested:

| Case | Expected | Observed |
|---|---|---|
| Change `declared_by` from `scholar` to `agent` in memory | REJECT | REJECT |
| Change one alignment verdict from `ALIGNED` to `OVERSTATED` in memory | REJECT | REJECT |
| Replace one source-map artifact SHA-256 with a zero hash in a temporary paper copy | REJECT | REJECT: stale source artifact `code/round2_bianchi_ledger.py` |

No registered workspace artifact was mutated by the test; faults existed only
in memory or under a disposable temporary directory. The test does not assert
scientific correctness or general reproducibility.

This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.
