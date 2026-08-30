# P25 Stage 4 Round 1 draft-writer receipt

Status: **RE-EMITTED — NOT APPLIED**

## Emitted artifacts

- Revision patch: `notes/stage4_revision_patch_round1.json`
  - Patch format: `1.1`
  - Authorization context: `review_roadmap`
  - Revision round: `1`
  - SHA-256: `f26b1731e31057d7d11e3e732405c8e66af65e08586aa14a5b873957fc9b1f20`
- Provisional response: `notes/stage4_response_to_reviewers_provisional.json`
  - Six roadmap items are present in immutable order `REV-001` through
    `REV-006`.
  - Its top-level patch binding points to the re-emitted patch SHA-256 above.
  - SHA-256: `1a2d05671f15caf1c88aabf2f2097420863c5fbec71dfaf6ed3d80c90cc26bb8`
- This receipt: `notes/stage4_revision_patch_round1_writer_receipt.md`

The writer emitted sidecars only. It did not run the revision-patch applier,
did not edit `notes/stage3_revision_base.tex` or `paper/manuscript.tex`, and did
not refresh any canonical result.

## Layout-only re-emission receipt

The prior marker-stripped preview bound to patch SHA-256
`ecf0d81969e1cd406f2cb4cd779f0361b2b73d62993e2c0d715a4da0bbd42a3b`
reported exactly one overfull hbox, `190.90196 pt`, localized to the long
Data/code availability pointer in the already-authorized B0109 replacement.
This re-emission supersedes that proposed sidecar without applying either
version.

Only the TeX wrapping of that B0109 pointer has changed. The lock and receipt
are now rendered with breakable `\path{...}` forms, and the read-only command
uses `\texttt{bash }\path{...}` so the executable token and path remain
line-safe. The scientific meaning and all three literal paths are unchanged:

- `experiments/stage4_reproducibility_lock.json`
- `experiments/stage4_reproducibility_receipt.json`
- `experiments/reproduce_stage4.sh`

The other 13 operations are byte-exact as JSON values relative to the previous
emission. B0109's operation metadata, roadmap IDs, old hash, explicit empty
authorization arrays, and every declaration outside the pointer formatting
are unchanged. The six provisional reviewer responses are also byte-exact;
only the top-level current patch-format, path, and SHA-256 binding fields were
added.

A non-landed synthetic marker-stripped layout preflight reused the exact prior
Stage-4 revised source, substituted only this pointer rendering, and ran
`lualatex`, `bibtex`, `lualatex`, `lualatex`. It produced 13 pages with zero
overfull hboxes, undefined citations, undefined references, missing glyphs, or
fatal errors. The synthetic PDF SHA-256 was
`f206b8a20888fa17aab38386d977f689d5071dcdc0843413b7b32f56a5e8fb8e`;
the final synthetic log SHA-256 was
`4f35f94b19f0e5a818c9074bfae9a8f32695e1fa79cd6011b0e2940686fd2b86`.
These are preview-only receipts, not landed manuscript or Stage-5 artifacts.

## Exact handoff bindings

The following values are transcribed from
`notes/stage4_writer_handoff.json` (SHA-256
`5cd268c3e9bb5d975838fafbba24fadacdbc8e8fb1fd15f1715ee942d35342b5`):

- Handoff type: `round9-stage4-writer-bindings/1.0`
- Paper number: `25`
- Revision round: `1`
- Base draft: `notes/stage3_revision_base.tex`
  - Patch binding: `4c3af7046334`
  - Full SHA-256:
    `4c3af70463340eab57c7ed9db6b88c2a6d64f88b2f03b058b3527573da375f70`
- Block manifest: `notes/stage3_revision_base.block-manifest.json`
  - SHA-256:
    `4f386b130e29c032ecbef86fd06e21fcfde36c7737b8f79801c3bbcb1e307f30`
- Immutable roadmap: `notes/stage3_revision_roadmap.json`
  - SHA-256:
    `ec77e5a53f2d5e937909732992be8139cbc2486f86fa5aa0faec1b54a8cd37a2`
- Author adjudication: `notes/stage4_author_adjudication.json`
  - SHA-256:
    `5986e259fe58d8fcb37ff32aef0a0339b345f0508450f2d33a3aa309f28f4d49`
- Author decision digest:
  `57f8b52fb9a9d3ade03e04ec7f6d6d2d62f570c3ffb58c6b3064a71793519781`
- Claim-surface manifest: `notes/stage4_claim_surface_manifest.json`
  - SHA-256:
    `323d27b42fb2e1208cd477297123b45370460913195ac5792d61ded5884b25b9`
  - Registered surfaces: `6`
  - Unregistered claim-drift review required: `true`
- Authorization request SHA-256:
  `174cf1b035c55f72cdc06f1df6eb5e39138cbc9982ed1fb97457189a964ecd63`
- Raw author event: `../../BATCH_ROUND9_STAGE4_AUTHOR_EVENT_20260830.txt`
  - SHA-256:
    `5e5ad1b6ff2a62060368877016ad4b14f869f22a3e38f9a703672ea52ecd067f`

The handoff-supplied target hashes are:

| Block | Old hash | Block | Old hash |
|---|---:|---|---:|
| B0013 | `d4569fec69be` | B0015 | `bd1ef5389fb0` |
| B0018 | `fd225459987f` | B0026 | `28a41736cfa9` |
| B0033 | `c8ddc7bbec09` | B0062 | `7f313af72a0c` |
| B0078 | `04a8cba3eb38` | B0079 | `61d82ee9a8f1` |
| B0082 | `99c2c8f35be2` | B0084 | `2a4cd47f1c21` |
| B0090 | `6318f3fc7ef7` | B0091 | `ad32fd20ae29` |
| B0102 | `f57e86956bf2` | B0105 | `9a4da6700070` |
| B0108 | `75d40a455331` | B0109 | `1b51cc5d1c90` |

All patch-level base, roadmap, adjudication, author-decision, claim-surface,
and per-operation old-hash bindings were copied from this handoff. No binding
was invented or recomputed for patch authority.

## Authorized operation coverage

The patch contains 14 unique `replace_block` operations:

| Roadmap item | Authorized blocks used by the emitted patch |
|---|---|
| REV-001 | B0013, B0026, B0033, B0105, B0108 |
| REV-002 | B0018, B0033, B0090, B0091, B0108 |
| REV-003 | B0015, B0078, B0079, B0102, B0108 |
| REV-004 | B0082, B0109 |
| REV-005 | B0109 |
| REV-006 | B0082, B0109 |

Overlapping targets are emitted once and cite every roadmap item whose
authorized change they implement. Every operation carries explicit empty
`claim_strength_changes` and `collateral_authorization_ids` arrays. The
heading-only targets B0062 and B0084 are deliberately untouched. No operation
falls outside an accepted item's exact target/operation subset, so no
pre-drafting escalation was required.

## Scientific and integrity boundaries

- The exact protected texts for C-004/B0078, C-005/B0079, and C-006/B0082
  occur byte-for-byte and exactly once within their respective replacements.
  The in-memory post-patch audit also found all six registered surfaces
  C-001--C-006 byte-exact and exactly once.
- B0109 preserves Funding, Conflict of Interest, Author contributions, Ethics,
  and AI-Assisted Research Disclosure byte-for-byte. Within Data and code
  availability, its first two sentences are unchanged; only the obsolete
  integrity-pointer sentence is replaced by the current lock, receipt, and
  read-only command.
- The 2,241-row replay is classified only as solver and reproducibility
  validation. It is not presented as additional proof of noncohomology, an
  infinite owner census, or demonstrated physical impact.
- The new four-object map distinguishes the physical billiard flow, unit-roof
  symbolic suspension, semiclassical construction, and exact boundary-channel
  multiple-scattering determinant by state space, owner, clock or weight, and
  determinant status.
- The unit-roof symbolic Route-A tuple is retained. The physical Route-A tuple
  remains unassigned. No Route-B result, determinant equality, or credit
  transfer is introduced.
- No bibliography key is added. The emitted comparison reuses only
  `Livsic1972`, `BowenLanford1970`, `Ruelle1976`, and `Wirzba1999`, with hidden
  reference and anchor layers attached to the new citation surfaces.
- There is no claim-strength authorization, collateral authorization,
  structural move, canonical-result refresh, or scientific-value change.

## Stage-4 reproducibility support consumed

- Machine-readable lock:
  `experiments/stage4_reproducibility_lock.json`, SHA-256
  `8848177095735a88437d7f335835f5ff6b200e701dbd75cb15370200522cb198`
- Validation receipt:
  `experiments/stage4_reproducibility_receipt.json`, SHA-256
  `5e5fd3123bc18d563c586a1fc8820bc7561416216e045e1426a175d4d6b94743`
- Lock validator: `code/stage4_reproducibility_lock.py`, SHA-256
  `cd9e9bcf025381381cb6d57369afd4995080c84049edd66d6b1b461e04159a66`
- Fail-closed tests: `code/test_stage4_reproducibility_lock.py`, SHA-256
  `ee23b6d7abb61f2792b324ea9d6852c4cf106e8bd685b93c006e6d27e1ef8e29`
- Read-only command: `experiments/reproduce_stage4.sh`, SHA-256
  `54f0d42013ffb15dcc0b817fb0df0e2b7ec2ae1f39d93fe69aef2851d269d6f5`

The consumed receipt records 75/75 passing tests, a closed 68-file inventory,
and a byte-identical validation replay of 2,241 rows: 747 rows per geometry,
three period-two matches and 744 disagreements per geometry. These are
reproducibility facts only.

## Read-only validation result

Validation passed for:

1. JSON parsing of the patch and provisional response;
2. the current ARS revision-patch 1.1 JSON Schema;
3. the anchored base, manifest, roadmap, adjudication, and claim-manifest
   digests;
4. all 110 anchored base block hashes;
5. 14/14 unique operations and their handoff-supplied old hashes;
6. exact author target/operation authority for REV-001--REV-006;
7. all six registered claim surfaces, byte-exact and exactly once;
8. declaration preservation outside the Data and code pointer;
9. reuse-only bibliography keys;
10. validation-only replay language, Route-A ownership, and unified lock
    pointers; and
11. the non-landed marker-stripped layout preflight, with `0` overfull hboxes
    after the B0109 pointer-format correction.

The provisional response contains the judgment content for all six items and
omits post-apply mechanical claims. Final landed block IDs and net word-count
change remain the deterministic applier/orchestrator's responsibility.
