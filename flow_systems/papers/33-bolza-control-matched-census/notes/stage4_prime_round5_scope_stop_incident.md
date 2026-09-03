# P33 Stage 4′ Round-5 scope-stop incident

Date: 2026-09-04 UTC  
Disposition: `FAIL_CLOSED_UNLISTED_TARGETS_REQUIRED`

The exact execution request
`BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33.json` (SHA-256
`ff160416cd8316326d2ef15b806f41479e63e299e0523899dbe93dc2e0da1650`)
authorized 39 item-target mappings over 35 unique `replace_block` pairs and
seven notes-side support operations.  The support operations were executed
without a producer, owner census, scientific experiment, result refresh, or
canonical promotion.  Before bibliography mutation or patch emission, a
manuscript-wide consistency audit found two unlisted blocks that the support
work would make stale.

## Exact additional targets required

- `B0041`, old hash `597eb230d326`, `replace_block`.  Its sentence “No
  retrieval ... occurred during revision” conflicts with the completed
  43-row commit-pinned artifact replay and 20-source bounded identifier replay;
  its statement that no fixture was executed conflicts with the synthetic-only
  2-valid/12-invalid conformance run.  The scientific-computation and
  production-validator negatives remain true and must be retained.
- `B0124`, old hash `3f69d3822846`, `replace_block`.  Its AI-assistance
  disclosure ends on 2 September 2026 and therefore omits the authorized
  4 September support work.  Its passage boundary remains true: all 48 uses
  retain `anchor=none` and `claim_to_passage=INCONCLUSIVE`.

`B0055`, `B0064`, and `B0066` were separately audited and remain compatible:
the common production schema is still a design specification, all production
components remain unavailable, independence is not established, and P33-RC-1
closure remains zero of seven.  Synthetic fixture conformance and contract-only
coverage schemas are not production closure.

## Stop action

No entry was appended to `paper/references.bib`; no Stage-4′ patch, revised
draft, apply report, PDF, or build log was emitted; no scientific or Route
state changed.  The following provisional Round-2 carriers were created before
the scope audit and are retained only as
`NONCONTROLLING_SUPERSEDED_DUE_TO_UNLISTED_TARGETS` incident evidence:

- `stage4_prime_round5_revision_roadmap.json`, SHA-256
  `31add6d38185529e4ff2647efba07a855811983f48a5ec6890ac9eb413e8198a`;
- `stage4_prime_round5_author_choices.json`, SHA-256
  `fff31c8a9fecc52b922e433515a12293344855f4f86875b60333f1b431b85e9a`;
- `stage4_prime_round5_claim_surface_manifest.json`, SHA-256
  `ac84c58906324544cc9ac81167b376c81f3a516c6ee94aac72a4d0a338ce7452`;
- `stage4_prime_round5_author_adjudication.json`, SHA-256
  `3a9f904849ee94889bde0c25d3c202ae824ef07cb956d4f340c1484a3fb815bd`.

They must not be supplied to the patch applier.  A new exact request must carry
all original mappings and support scopes and add exactly
`B0041/replace_block` and `B0124/replace_block`; after a new author
confirmation, a fresh successor roadmap, claim-surface manifest, choices, and
adjudication must be generated.  Any further target requires another stop and
new authorization.
