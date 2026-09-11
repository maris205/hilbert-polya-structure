# P211 Round1 plan — bounded static infrastructure review

2026-09-08 UTC. Outcome: no blocking static discrepancy found in the named
PLAN_ONLY preparation. This note is not a new mandatory gate, execution
authorization, freeze acceptance, manuscript review or acceptance of future A
evidence. No adapter, saved checker, scientific program or build was invoked;
no physical input copies were made.

## Checked against original infrastructure

The [plan](../p211_round1_preparation/PLAN.md) and
[role draft](../p211_round1_preparation/ROLE_SELECTION_DRAFT.json) are internally
consistent with the accepted infrastructure and role contracts.

| Question | Evidence-backed conclusion |
|---|---|
| Exact author baseline | All 32 distinct name/size/hash rows equal the accepted [SOURCE_INPUTS_AFTER.json](../p211_round0_execution01/SOURCE_INPUTS_AFTER.json), and their names equal the literal NAMES list in the accepted recorder source. Their metadata byte sum is 1,819,014, matching the old RESULT. No paper payload body was opened or rehashed |
| Five-payload preparation | Actual directory membership is exactly five ordinary payload files plus SHA256SUMS. All five payload hashes and all ten INPUTS.sha256 entries match. The current plan has 11 distinct existing file links |
| Symbolic count | If A's final nonself manifest has N payloads, its copied package has N+1 files. Round1 therefore has N+33 payloads and N+34 files including its outer manifest; B's complete Round1 input set has N+34 rows before separately declared external inputs |
| Complete A selection | The ten required filenames are a minimum role set, not the complete selection. The draft requires every finally accepted A payload, its own manifest and all additional/failed evidence. Exact A membership and acceptance remain null |
| Historical status | [Root's Round0 reception](../p211_round0_root_reception/RECEPTION.md) supplies acceptance. The old execution RESULT correctly remains historically pending; this plan does not rewrite it |
| Final delta prerequisite | The same A must accept its exact repaired or no-change delta, with current zero-open findings and root original reception. Initial output/canonical/strict-pair success alone cannot substitute for final review/delta acceptance |
| Live-author guard | Round0 is the proposed physical author source, but current author bytes and the accepted delta's before/after author key must also match the unchanged 32-entry baseline. Any changed or extra author file stops this narrow plan |
| Deferred execution | Binding is disabled; every execution-binding field and every exact A acceptance/membership field checked is null. No future destination or A-tree readiness was tested |

The accepted ledger digest is
3a0257d637b721607339dc623aa2890bb24f86ed003e8dc1d0e40194cedfde5f.
The draft's historical Round0 manifest metadata agrees with the accepted
RESULT and root reception: 2,799 bytes and
459459486a82c8f787d04e5e7fcb81e6c01b3abef320d1e82ea4cbb30ea8a8bd.
This is metadata agreement, not a new physical Round0 audit.

## Recorder adaptation and path bases

I fully read the accepted 209-line
[freeze.py](../p211_round0_execution01/freeze.py), without importing or
executing it. It performs top-level writes and Round0-specific actions, so the
plan's instruction to derive and pin a separate later adapter is necessary.

Its old PAPER.rglob inventory would now include the existing Round0 tree.
The draft correctly requires pruning only the exact known
paper-root/frozen_round0 subtree before the ordinary author inventory check.
That is not a wildcard exclusion of all frozen names or arbitrary nested
directories. After creation, exactly the new Round1 tree must be accounted
for. Unexpected files, directories, symlinks or special entries cannot be
silently ignored by reusing a files-only recursive expression. These are
already stated implementation obligations, not checks performed here.

The scoped adapter must also replace the old 32-only copy loop, distinguish
author and A destination roles, and bind actual A/external dependencies rather
than blindly replaying the six hard-coded Round0 package selections. The plan
states these deltas and preserves the accepted recorder/source histories.

The manifest and document bases are correctly kept distinct:

- The new outer SHA256SUMS is Round1-relative, includes review_a/SHA256SUMS
  as a payload, and excludes only itself.
- The unchanged inner review_a/SHA256SUMS is A-directory-relative and must
  be checked with the copied A directory as cwd.
- A's INPUT_PINS.sha256 keeps the workspace-root-relative historical Round0
  paths it actually reviewed; copying it does not rebase those pins.
- Copied author and A documents resolve links using their declared original
  document locations. Embedded historical copies require their explicit
  original-version mapping. Explicit historical Round0 links remain historical.

The plan further requires exact physical cp/cmp operations, ordinary-file and
distinct-inode checks, complete source/external before-after keys, inner and
outer native hash checks, and preservation of any partial failure. None of
those future operations or assertions is certified by this static review.

## Actual preparation records and their limits

The original NATIVE_READS.json contains 12 cmd/result tool records; its
eleventh record retains the new-directory ls exit 2. That observation is not
a successful future-freeze preflight. CHECKS_NATIVE.json retains three actual
flat metadata/pin/link checks, each with a recorded zero exit.

For eight stable source-read records, the archived decoded UTF-8 output
equals the entire currently pinned infrastructure file byte-for-byte:
recorder, old plan, root reception, role contract, artifact contract, accepted
ledger, old result and hostile-review protocol. Their complete original
sources were read. Archived navigation excerpts and line counts remain
historical observations; they are not required to match newer STATE/PIPELINE
content. The earlier truncated STATE display is still disclosed.

These preparation records contain command strings and tool-result envelopes,
not separately captured original native argv/cwd/environment/raw process
streams. Their scope is documentary preparation, not an execution-ready
runtime certificate. The flat link check originally excluded the not-yet-made
CHECKS_NATIVE.json; the final five-payload seal includes that file, and the
current 11-link check includes it.

[EVIDENCE.json](EVIDENCE.json) preserves this review's two actual read-only
hash-check calls and the metadata comparison call, with their complete tool
returns and a 16-file metadata/input census. No saved preparation checker was
run. The observed preparation seal is
3c01d38cc3ba10783f53d0e2b8ab663b8615740a60a27beb0891f1c3f776a305.

## Authorship and boundary

I did not author this rational_scout Round1 plan or role draft. I did author
the linked earlier Round0 plan and P211 build infrastructure. I therefore do
not claim independent certification of those earlier contributions; their
separate accepted receptions remain the authority.

Earlier build work included reading all nine author TeX/Bib files, including
mathematical text. That familiarity remains disclosed. In this task I read
only infrastructure, role/claim-scope metadata and preparation records: no A
tree and no P211 manuscript/proof/verifier/canonical/PDF body was reopened,
and no P211 mathematical contribution was made.

Only this new note directory was written. No children, copies, central edits,
Git operation, A/B manuscript review or external action occurred. The project
skill kept this at change-sensitive metadata/contract review; it did not add
an acceptance gate. Actual A/delta reception and any later fully bound freeze
remain root's separate decisions.
