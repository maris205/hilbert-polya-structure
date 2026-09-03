# Round 10 Stage 4′ correction-execution authority — attempt 2 incident

- Workflow date: `2026-09-04 UTC`
- Scope: authorization-record and input-freeze construction only.
- Result: fail-closed before any authorization record, receipt, freeze, manuscript, bibliography, result, Route, or initial-system write.

The builder initially looked for aggregate P33 count fields that are not stored
on the request's paper object. The immutable request instead carries the count
through its seven `items[].proposed_targets[]` arrays. The validator was changed
to derive `39` item-target mappings and `35` unique block IDs from those frozen
arrays. No request byte, author instruction, target, or scientific content was
altered.
