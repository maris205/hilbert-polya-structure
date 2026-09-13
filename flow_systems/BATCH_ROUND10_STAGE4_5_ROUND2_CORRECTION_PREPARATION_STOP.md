# Round 10 correction preparation — stopped before patch emission

Date: 2026-09-05 UTC. Status: **STOPPED_ON_OFFICIAL_VALIDATOR_FAILURE**.

## Confirmed scope and observed failure

The author confirmed the correction scope request SHA-256 `d9be18e2199dd64100a1482018eb9bf77586e2548ba751cc0c2b57e06195f992`. The raw event and scope record are preserved as `BATCH_ROUND10_STAGE4_5_ROUND2_CORRECTION_SCOPE_AUTHOR_EVENT_20260905.txt` and `BATCH_ROUND10_STAGE4_5_ROUND2_CORRECTION_SCOPE_AUTHORIZATION_RECORD.md`. This scope includes the explicit stop condition: **Any failed official validator, independent replay, or isolated build.**

The main agent's new preparation helper attempted to validate schema-current integrity correction lists before emitting any files:

```text
PYTHONDONTWRITEBYTECODE=1 python3 tools/prepare_round10_stage4_5_round2_correction_patches.py
exit_code: 1
revision_roadmap.ContractError: integrity correction EA-003 proposed_targets: target rows must use canonical block/operation order
```

The helper at failure has SHA-256 `e30adabbbd64763c59f10cdabf750c06736ce13f42cb43d14c4fcc3183d07459`. The failing call is the installed ARS 0.1.28 `revision_roadmap.validate_integrity_correction_list`, not an application to a manuscript.

Cause: the helper retained the frozen request's physical draft order for P31's S23/S24 targets, `B0016, B0112, B0037, B0038`. ARS `_validate_target_list` requires canonical numerical block order, `B0016, B0037, B0038, B0112`. These are exactly the same four block/operation pairs. The error belongs to the main agent's preparation adapter; it is not a scientific finding or a request to expand manuscript scope.

## Writes and safety state

The helper constructs and validates the entire batch in memory before producing an apply_patch payload. It failed before returning that payload. Therefore no canonical issue-list adapters, writer handoffs, scope receipt JSON, patches, revision logs, successor manuscripts, bibliography successors, or official apply reports were emitted. All three writing agents were stopped; each confirmed no file writes.

Written in this preparation turn: the exact user-event transcription, its scope-authorization explanation, the new preparation helper, this stop record, and a continuation-note update. No existing manuscript or scientific artifact was modified.

Post-failure read-only checks passed: all five base drafts/manifests/blocker-source hashes still match the confirmed request; 119 locked file bindings and all protected boundaries replay; changed protected files = 0; successor drafts = 0. Stage 4.5 Round 3 has not begun. The completed Round-2 audit remains valid and immutable.

## Proposed bounded recovery — awaiting short author confirmation

The next unqualified author reply `确认`, after this recovery is presented, authorizes only:

1. Fix this preparation helper so each derived issue's `proposed_targets` uses ARS's canonical block/operation order before validation. Preserve the exact set of targets and operations, all finding mappings and source hashes, and the request's physical-order evidence. Do not edit the original request, base manuscripts, old manifests, ARS validator, or any scientific data.
2. Re-run the preparation checks. If they pass, emit the five source-accounted issue-list adapters and writer handoffs, then complete the actual five patch documents within the already confirmed 66-block scope, together with the already exact single P30 Bib operation and a unified patch-review package.
3. Present the concrete patch bytes and their exact digests once for the author, as required by the current integrity-correction apply protocol. Do not invent exact patch approval from the earlier scope confirmation; no official apply occurs before this exact-patch confirmation.

Any other official-validation failure, scope mismatch, scientific-value change, structural escalation, claim strengthening or unlisted edit still stops. This recovery does not authorize Stage 5/6, canonical promotion, README/status mutation, Git, new science or a new paper batch.

This is a one-defect recovery proposal, not a claim that the fix has already been made. The faulty helper remains unchanged at the hash above pending author direction.
