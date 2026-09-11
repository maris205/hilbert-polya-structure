# Actual archive-only audit

The following read-only command was actually executed from the workspace
root after the scientific run and documentation were written:

    python -I -B docs/papers211_215_sequence/scouting/finite_allocation_lane/audit_archived.py

Actual exit code: **0**. Complete stdout:

```json
{"archived_state_records": 5704, "audit": "ARCHIVED_CONSISTENCY_ONLY", "historical_raw_pairs": 8, "native_command_bindings": 7, "new_scientific_executions": 0, "pilot_input_raw_pairs": 4}
```

The audit read and compared raw current/historical copies and all four
pre-run frozen inputs. It checked seven actual command-result/output byte
and digest bindings and parsed all archived state records and their final
summary. It did not call the map, recreate its orbit graph, enumerate any
new scientific state or rerun the pilot. This record is an author artifact
inspection, not independent mathematical review or root acceptance. Its
stdout and actual exit are also available in the invoking tool response.

The final directory-relative `SHA256SUMS` is created only after this record
and `HANDOFF.md`; it excludes only itself. Historical pins are instead
workspace-relative. No relaxed path adapter or normalized equality is used.
