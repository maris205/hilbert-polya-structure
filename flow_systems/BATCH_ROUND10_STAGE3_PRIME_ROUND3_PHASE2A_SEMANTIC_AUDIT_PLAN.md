# Round 10 Stage 3′ Round 3 Phase 2A semantic-audit plan

Frozen before any Round-3 Phase 2A evidence verdict is emitted: `2026-09-03T13:22:00Z`.

## Bound Phase-1 artifacts

| Paper | Precommitment SHA-256 |
|---|---|
| P29 | `134f71c83b49364d9157687f34ddc1c95df3f6fb3d14b80ec7bdab30e97f1a0a` |
| P32 | `e6ec53f7a193560d90b786610488589d660035c72a3e10e249efed1f09a7116d` |
| P33 | `66a8badeac6e7284ffceb9c2f1ac218c578ed4b40237ae258c56ce6d370deab6` |

Batch Phase-1 validation SHA-256: `4e801d653f5cddedbb55010cc21681ce9e85633910383104d4d1752cec823dc6`.

## Precommitted audit rule

1. One fresh-context primary semantic auditor examines every Phase-2A row against the exact bound Phase-1 operationalization and the permitted evidence surfaces. The Response to Reviewers and all Round-1/Round-2 re-review artifacts remain withheld.
2. The primary auditor records one closed supported verdict for every row and flags every difference from the immutable Phase-2A record. It does not edit that record.
3. If there is no difference, that paper passes the semantic gate.
4. Every disputed row, and only a disputed row, receives one additional fresh-context blind tie-break. The tie-break sees the precommitment, original/revised manuscript evidence and patch/apply chain for that row, but neither the primary-audit recommendation nor the Response to Reviewers.
5. If the tie-break agrees with the committed Phase-2A verdict, the record remains controlling and the paper passes. If it differs, the paper aborts as `phase2a_lint_failed`; no retry, rewrite or Phase 2B is permitted.
6. Non-disputed rows remain controlled by the immutable committed record. Same-family fresh contexts are role-separated, not claimed to be independent error processes.

This plan authorizes review-side audit artifacts only. It grants no manuscript, bibliography, result, experiment, Route, or later-stage write authority.
