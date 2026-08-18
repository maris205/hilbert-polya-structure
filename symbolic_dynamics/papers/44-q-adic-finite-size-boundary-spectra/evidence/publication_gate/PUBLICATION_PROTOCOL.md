# Paper 44 dual-state publication protocol

## Scope and trust boundary

This overlay repairs the publication gate without modifying or weakening the
sealed legacy core.  The 58-row `STATIC_TREE_MANIFEST.json`, its pre-output
seal, the legacy runner, the direct `audit_integrity.py`, and the frozen
external auditor remain byte-identical.  The publication layer recognizes
three exact, mutually exclusive states:

The operator must hold exclusive ownership or an external exclusive lease on
the target for the complete audit/stage/install invocation.  The scripts make
an immediate prewrite full-tree comparison, but that comparison and the next
rename are not an inter-process atomic compare-and-swap.  Without exclusive
ownership, another writer in that narrow interval could be overwritten.

1. `PREDECESSOR_STATE_A_EXACT` is the already installed predecessor writer
   overlay, identified by its exact manifest and seal hashes, with the legacy
   State-A output tree.  It is accepted only as the source of the bounded
   overlay-upgrade transaction.
2. `PUBLISHED_STATE_A_EXACT` is the superseding overlay with the unchanged
   State-A output semantics.  Direct legacy `FINAL A` must pass with the
   historical final-tree hash.
3. `PUBLISHED_STATE_B_EXACT` is the superseding overlay plus a State-B output
   tree.  Direct legacy `FINAL B` must pass, and each of `code_commit`,
   `source_commit`, and `source_lock.code_commit` must equal one exact
   out-of-band Stage1 commit.

The legacy frozen auditor is not taught about publication paths.  It must
return canonical `REJECT/STATIC_TREE_MISMATCH` on every exact published
overlay state.  The publication auditor records this as
`EXPECTED_REJECT_STATIC_TREE_MISMATCH_SUPERSESSION`; any other legacy result is
a publication failure.

## Two external anchors and an acyclic seal

Every call supplies the publication-seal SHA-256 as strict lowercase hex64.
State B additionally supplies the Stage1 commit as strict, nonzero lowercase
hex40.  The auditor hashes the raw seal before parsing it.  The seal and all
manifest-covered evidence contain neither external value, so no future commit
or State-B tree hash is frozen into this candidate.

`WRITER_MANIFEST.sha256` contains C-sorted SHA-256 rows for every regular
overlay file except itself and `PUBLICATION_OVERLAY_SEAL.json`.  The excluded
seal binds that manifest, the bridge contract and code, the generic smoke
evidence, the final PDF, the legacy anchors, and the predecessor anchors.  The
seal SHA-256 is communicated only out of band.  This is the acyclic graph:

```text
overlay bytes + bridge code + generic evidence
                 -> self-excluding writer manifest
                 -> excluded publication seal
                 -> out-of-band seal SHA-256

out-of-band Stage1 H1 -> three State-B Route fields
full published root + State-B outputs -> self-excluding PAPER_MANIFEST
```

No mutable program authenticates itself.  The mandatory bootstrap in
`STATEB_COMMANDS.md` first copies the seal into a private directory, hashes and
parses that single immutable snapshot, verifies a copied writer manifest, and
then copies and re-verifies the auditor, transactions, and smoke runner.  Only
those read-only controller copies are executed.  The transaction and bridge
invoke their sibling controller auditor, never an auditor selected from the
source or target tree.

## Bounded overlay upgrade

`publication_transaction.py` accepts only an exact predecessor State A or an
already exact superseding state.  It audits the new source, copies every byte
to a same-filesystem staging tree, re-audits the stage, and computes the
bounded changed/added/obsolete path set.  Forced-late failure exits 86 before
the first target write.  Installation uses per-path atomic replacement and
retains backups until an exact post-audit succeeds.  An injected mid-install
failure restores every replaced path and exits 87.  A second exact invocation
performs zero replacements.  Non-overlay legacy and output bytes, modes,
inodes, ownership, links, sizes, and modification times are preserved.
Immediately before the first target write, a full logical-tree prewrite
comparison rejects any change that occurred during staging.  The mandatory
external exclusive-target precondition covers the remaining compare/write
interval.

## State-B bridge

`stateb_bridge.py` first audits an exact superseding State A.  It creates an
exact disposable projection of the frozen 58-row legacy core and invokes the
unchanged legacy runner there with external H1.  This is the only context in
which the frozen static preflight is expected to pass.  It then places those
outputs in a disposable copy of the full published root, rebuilds
`outputs/PAPER_MANIFEST.sha256` over the full root including the writer
overlay (excluding the legacy seal and the manifest itself), and requires both
direct legacy `FINAL B` and the publication audit to pass.

Only the fully certified `outputs` directory is installed.  Linux
`renameat2(RENAME_EXCHANGE)` exchanges it with the State-A directory in one
atomic namespace operation.  Forced-late failure exits 86 before exchange.
An injected post-exchange failure exchanges the original directory back,
re-audits exact State A, and exits 87.  Repeating an exact State-B transition
performs zero exchanges.  Immediately before exchange, a full target-tree
prewrite comparison rejects any staging-period change without writing.  The
mandatory external exclusive-target precondition covers the remaining
compare/exchange interval.

## Negative and governance evidence

The cold smoke suite checks predecessor upgrade late/rollback/first/second,
State-B late/rollback/first/second, direct full-root certification, and eight
physical State-B attacks: missing, wrong, and uppercase H1; a fully valid
wrong-H1 Route reclose; a paper-manifest reclose over modified output; writer
and seal reclose; auditor and seal reclose; and mixed A/B provenance.  Missing,
wrong, and uppercase publication-seal anchors are also rejected before trust.

Before execution, `--write-evidence-template` emits only a replay checklist
with `execution_observations_recorded=false`.  Only a completed fail-fast smoke
run may replace it with exact observed dispositions and
`execution_observations_recorded=true`.  The resulting
`PUBLICATION_SMOKE_EVIDENCE.json` contains no external anchors or State-B tree
hash.  It is evidence for a fresh independent audit, not a self-issued
authority decision.  The candidate status is
`HOLD_FOR_INDEPENDENT_STATEB_PUBLICATION_AUDIT`.

Normal source and publication audits reject the unexecuted checklist.  The
temporary `--allow-unexecuted-checklist` escape is accepted only together with
`--relocated-disposable` below `/tmp`, solely to bootstrap the first smoke run;
it is absent from final replay and publication commands.
