# Round 10 Paper 33 — Stage 4′ scope-expansion authorization request

Workflow date: **2026-09-04**

Status: `AWAITING_EXPLICIT_AUTHOR_CONFIRMATION`

This request is the fail-closed successor to the original P33 Stage 4′ request.
It does not itself authorize execution. The original execution stopped before
any bibliography append, patch emission or application, revised draft/PDF, or
build because completed notes-side support made two unlisted manuscript blocks
stale. The exact machine-readable request is
`BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION.json`,
SHA-256
`100c97df01c356a52e3dea39ab327873f544d3ac6b32107f1576ae4dcb02db65`,
57284 bytes.

## Exact scope

The successor request preserves, byte for byte as JSON objects, all seven
original residual items and their **39 item-target mappings over 35 unique
`replace_block` pairs**. It also preserves the seven original supporting
operations and their deny lists. It adds exactly two new issue-action mappings:

- `REV-P33-SCOPE-001` → `B0041/replace_block@597eb230d326`, solely to
  reconcile the completed commit/identifier replay and synthetic conformance
  with the former blanket no-retrieval/no-fixture wording while retaining every
  scientific, production-validator, census, and result-refresh negative.
- `REV-P33-SCOPE-002` → `B0124/replace_block@3f69d3822846`, solely to extend
  the AI-assistance disclosure through the authorized 4 September support work
  while retaining `anchor=none` and `claim_to_passage=INCONCLUSIVE` for all 48
  source uses.

The exact total is therefore **41 mapped pairs with item/action provenance,
37 unique block/operation pairs, all `replace_block`, and seven support
operations**. There is no target, operation, claim-strength, collateral, or
scientific-execution authorization beyond that set.

| Block | Frozen old hash | Item/action provenance |
|---|---|---|
| `B0007` | `36066564a7f8` | `REV-P33-013` |
| `B0010` | `c96a54aac5fd` | `REV-P33-013` |
| `B0015` | `cfe8ae896686` | `REV-P33-008` |
| `B0020` | `512a0f15dddc` | `REV-P33-013` |
| `B0025` | `173e02e1eb10` | `REV-P33-008` |
| `B0026` | `231a6b4c1b49` | `REV-P33-003`, `REV-P33-008` |
| `B0027` | `a9417c34e6c7` | `REV-P33-008` |
| `B0029` | `a198b5981f00` | `REV-P33-008` |
| `B0030` | `c06ca91759a8` | `REV-P33-008` |
| `B0032` | `32208669ff00` | `REV-P33-008` |
| `B0033` | `4fa49ff27493` | `REV-P33-008` |
| `B0036` | `21389545e66a` | `REV-P33-003`, `REV-P33-008` |
| `B0037` | `c107f2d5d147` | `REV-P33-008` |
| `B0041` | `597eb230d326` | `REV-P33-SCOPE-001` |
| `B0043` | `00905a35d081` | `REV-P33-008` |
| `B0044` | `9714c4b0ddf6` | `REV-P33-003`, `REV-P33-008` |
| `B0045` | `182f58bfa1ab` | `REV-P33-008` |
| `B0051` | `452573d2ac85` | `REV-P33-007` |
| `B0052` | `3cca919f4b69` | `REV-P33-007` |
| `B0057` | `ba435a21ed08` | `REV-P33-006` |
| `B0059` | `c1201f6b9f62` | `REV-P33-006` |
| `B0061` | `abf5b53a56d8` | `REV-P33-005` |
| `B0062` | `bac5109800ae` | `REV-P33-006` |
| `B0067` | `e226039d3f69` | `REV-P33-003`, `REV-P33-008` |
| `B0072` | `6a60496cf945` | `REV-P33-005` |
| `B0073` | `7561adb417bc` | `REV-P33-013` |
| `B0077` | `5dfc655bda88` | `REV-P33-008` |
| `B0087` | `23030f518a91` | `REV-P33-002` |
| `B0091` | `88633eee5336` | `REV-P33-008` |
| `B0100` | `2c1d5fda7edb` | `REV-P33-013` |
| `B0106` | `9757770c80d4` | `REV-P33-008` |
| `B0107` | `dedce0ac4fc8` | `REV-P33-003` |
| `B0108` | `686299793396` | `REV-P33-005` |
| `B0109` | `1dc16ad56b86` | `REV-P33-013` |
| `B0123` | `ad4ad7c72508` | `REV-P33-002` |
| `B0124` | `3f69d3822846` | `REV-P33-SCOPE-002` |
| `B0128` | `fad762064c89` | `REV-P33-006` |

## Completed support and retained limitations

- The commit-pinned artifact inventory replay matched **43/43** files exactly.
- The source-use matrix contains exactly **48 rows over 20 sources**. It has
  **0 exact passage locators** and **48 explicit bounded-unavailability rows**;
  every use remains passage-level `INCONCLUSIVE`.
- The synthetic conformance set contains exactly **2 valid and 12 invalid**
  canonical fixtures, with **14/14** expected dispositions matched. These are
  synthetic schema fixtures, not producer output, a surface census, or a
  scientific result.
- Separate BP/CP enumeration and coverage-ledger contracts were validated as
  contracts only. No producer was run.
- Production BP/CP components, adapters, predicate kernels, theorem encodings,
  and production build hashes remain explicitly unavailable. Independence is
  not established.
- The two correction records remain prospective. `paper/references.bib` has
  not been changed and the five manuscript bindings have not been applied.

The complete support bundle is bound in the JSON request by path, SHA-256, and
byte count. The support validation passed 73 checks with zero failures. The
scope-stop incident is
`papers/33-bolza-control-matched-census/notes/stage4_prime_round5_scope_stop_incident.md`,
SHA-256
`c4addb60f10d4c7e288e4b475e0cabee9e9febbbc0a5c97c6bb6ca2966fac1d8`.

## Superseded noncontrolling carriers

The pre-stop provisional roadmap, author choices, claim-surface manifest, and
author adjudication are retained only as
`NONCONTROLLING_SUPERSEDED_DUE_TO_UNLISTED_TARGETS`. They must not be supplied
to a patch applier. After confirmation of this exact successor request, a
fresh successor authority chain must be generated and hash-bound before any
bibliography or manuscript mutation.

## Frozen boundaries and next gate

The base draft remains SHA-256
`8a4ea5ff994db83b91c2f14ca5a8425e6e2f954cbc7c87faf7edf27ec98b99d4`;
the bibliography remains
`12143967175abb0d325e16d156b1bc227e51f886009e7acd64691e84b92cb5e0`;
the canonical manuscript remains
`b407441c07091ad38fb7e918721d31d2c4e3d897db9a705d92d9ff1f231f96d3`;
and the canonical PDF remains
`487a8838d9d422e00dcf3e896c9231b96c58fedfc2cdeb2265045f8d11d70031`.
No producer/census/scientific experiment or result refresh, canonical
promotion, Route or initial-system change, Stage-3′ re-review, or Stage 4.5 is
authorized.

Reply `确认` to authorize exactly the JSON request at SHA-256
`100c97df01c356a52e3dea39ab327873f544d3ac6b32107f1576ae4dcb02db65`.
Any byte change to that JSON requires a new confirmation.
