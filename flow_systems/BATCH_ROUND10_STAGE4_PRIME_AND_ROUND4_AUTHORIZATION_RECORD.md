# Round 10 Stage 4′ execution / preparation and Stage 3′ Round 4 authorization record

- Recorded at: `2026-09-03T15:40:38Z`
- Author event: `BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHOR_EVENT_20260903.txt`
- Author-event SHA-256: `111505020ac13b92ac253361e21777de8343455edd9ed3a4436fe924600cb812`
- Exact author instruction: `确认，下一轮`
- Interpreted only against `BATCH_ROUND10_STAGE3_PRIME_ROUND3_MANDATORY_CHECKPOINT.md` (SHA-256 `dff758cae93c8fba9c17d9b26cbe6c07ae3584d7645aa0db357ab75a73fee94e`).

## Authorized track A — P30/P31 Stage 4′ execution

- Execute exactly the existing request `BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.json` (SHA-256 `a35002ccadc74ef1f05d79b5cd7a81bff728664c27bab679504780fcb91dd688`) and its Markdown rendering (SHA-256 `4b42e929286be28655f0afa74145370399eed4e7d00f9d205d480db70f8dc03a`).
- Authority is limited to the request's 13 `will_address` residual items, 37 exact block/operation targets, and listed implementation branches.
- Produce versioned Stage 4′ patch/apply/build/response/evidence artifacts. Preserve every registered ClaimIntent surface byte-for-byte because the request grants no claim-strength replacement.
- Stop for a new decision if an exact target is insufficient, an apply/build/integrity check fails beyond the contract's allowed retry, scientific numbers would change, or the requested implementation would require structural or collateral scope not listed in the request.

## Authorized track B — P29/P32 Stage 4′ request preparation only

- Prepare hash-bound, item-by-item Stage 4′ authorization requests from each paper's controlling Round-3 Major Revision/B4 record and traceability.
- List exact proposed targets, allowed operations, implementation branches, bindings, and validation results.
- Do not emit a revision patch, apply manuscript/bibliography edits, build a new revision, alter registered claims, or refresh any result. Execution requires a later exact author confirmation.

## Authorized track C — P33 Stage 3′ Round 4

- Start one wholly fresh contract-1.1 re-review round with a new round id, new input manifest/freeze, and fresh model contexts.
- Preserve the evidence-before-persuasion order: revision-blind Phase 1; persuasion-blind Phase 2A; Phase 2B only after a valid Phase 2A commitment.
- Apply the one-lint-retry Phase-1 rule and the no-retry-after-evidence Phase-2A rule; fail closed on a semantic or structural Phase-2A defect.
- Run the official checker before surfacing any decision. Preserve every Round-3 artifact byte-for-byte, including the abort and invalid-audit incident records.
- Review-side artifacts only: manuscript, bibliography, PDF, experiments, results, registered claims, initial-system definition, and Route state are immutable.

## Frozen roadmap and terminal bindings

- Route A evaluator: `skills/route-a-evaluator.md`, SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
- Route B evaluator: `skills/route-b-evaluator.md`, SHA-256 `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.
- Round-3 final audit: SHA-256 `b61f44535bd83b84da163391f30225de1b6afba5aa1434babb0bcca808c5b692`.
- Round-3 final receipt: SHA-256 `f6eb05b19724b868b5aacb3dfbfb28ec56995675effd5984176bd9aea202f53e`.
- Formal Route-A coordinates and Route-B entry permission remain unchanged.

## Explicitly not authorized

- No P29/P32 Stage 4′ patch or manuscript write.
- No Stage 4.5, Stage 5, Stage 6, canonical promotion, submission, Route advancement, Route-B invocation, new scientific execution, result refresh, new initial system, or system-family change.
- No modification of the five canonical manuscript/bibliography/PDF triples.
