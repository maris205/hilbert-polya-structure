# P212 B DATA receiver SOURCE handoff

Status: SOURCE_ONLY_AWAITING_ROOT_RECEPTION_AND_DATA_GRANT.

Owned deliverable: CHECK.cjs, PLAN.md, INPUT_PINS.sha256, HANDOFF.md and the nonself SHA256SUMS sealing those four payloads. Eighteen existing SOURCE inputs are pinned; source-only native hash inventory was obtained without opening actual run/native/grant/current-runtime evidence. CHECK.cjs has been manually read in full as source and has not been parsed or executed by a runtime. No DATA receipt exists in this package at source handoff.

Root should receive the entire four-payload package and eighteen pins, then decide whether to grant the exact prospective invocation in PLAN.md. The receiver is read-only except for stdout/stderr; execution result preservation belongs to the separately granted DATA step. Do not treat this document or a future outer zero exit as semantic reception without the full report and its bound raw evidence.

Scope: full saved first-run capture and whole scientific output only, using the already adopted ordinary-runtime policy. No producer rerun, host discovery, canonical edit, strict-run grant, manuscript mutation, build, review completion, or external action is included.
