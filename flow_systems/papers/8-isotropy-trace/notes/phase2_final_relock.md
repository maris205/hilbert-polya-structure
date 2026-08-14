# Paper 8 Phase-2 final mechanical re-lock

Date: 2026-08-14  
Scope: hash-ledger correction only; no mathematical or Route revision  
Decision: **PASS**

## 1. Why this separate record is necessary

`phase2_final_gate.md` was frozen before the final mechanical-status addendum
was appended to `phase2_domain_da_review.md`.  Its row

```text
phase2_domain_da_review.md -> c22f090f...
```

therefore identifies the independently reviewed pre-addendum snapshot, not
the current bytes of that review file.  The current review has SHA-256

```text
05fecacd1215990ff79a66d69670f0ff57510dc5d7466d68588bb4c4a890c014.
```

The addendum's sentence saying that all six hashes in the earlier final gate
still matched disk is mechanically false for its own file after the append.
That sentence is superseded by this record.  It is a self-versioning artifact
issue only: a file cannot retain its pre-append hash after receiving an
addendum.  The reviewed content, verdict, active tuple, source audits, scope,
and stop conditions did not change.

The earlier files are preserved byte-for-byte so that every downstream proof
which cites their historical SHA remains auditable.  This re-lock, rather
than an edit to either historical file, records the current release state.

## 2. Current exact-byte ledger

| Artifact | Current SHA-256 | Status |
|---|---|---|
| `research_protocol.md` | `e1149ebd9609de24e0df00dcaeafdbcd31ee973e8ebe04b15cf86541f8084535` | active, exact match |
| `candidate_lock.md` | `8a5a460bac51843e532c9894fcb99470247c7de7833449c3660813ccd183d64e` | active, exact match |
| `phase2_domain_amendment.md` | `412e6d24c43ab5a995d135c6ecb207f5225414fac223fcf63080486af6fc3de3` | active, exact match |
| `phase2_source_topology_audit.md` | `f76dc87df56bacc54ea420447b28cb37020fc2625fa97d2eca2f173278ee83a3` | exact match |
| `phase2_groupoid_source_audit.md` | `39fcd460018a38a2b23107b0cb2f59195b7fa4110ad6742b66a334af0f4bad42` | exact match |
| `phase2_trace_source_audit.md` | `101d447a238cbf9ec6ea33a78b3f6be7456a1be30fdc206e13db91697d75c5f0` | exact match |
| `phase2_novelty_search.md` | `28862717c996b60a7c9e210cae65a78ee1a42d035dafadb8f6f8e59435df0bca` | exact match |
| `phase2_domain_relock.md` | `47d50ff8cb6c7d86cffa5ea95c75c00a6193e10d47d3f61a19ccea02ab3e5fb8` | reviewed content snapshot, exact match |
| `phase2_domain_da_review.md` | `05fecacd1215990ff79a66d69670f0ff57510dc5d7466d68588bb4c4a890c014` | final report including status addendum |
| `phase2_final_gate.md` | `22fd0376ad8e69e6816b3d005d88f4cde2cc5f4b243749c95aa2f19ab8164a3f` | historical authorization gate, exact match |

The pre-addendum content hash `c22f090f...` remains a valid historical
review snapshot recorded in `phase2_final_gate.md`; it is not the current
file hash and must not be labelled as one in any release table.

## 3. Mechanical and scope verdict

The three active files differ from their content-reviewed bytes only by the
registered status transition to `RE-LOCK PASS`; reversing that transition
recovers the independently reviewed content tuple documented in the final
addenda.  Phase 3 was and remains authorized only for the actual one-orbit
program and separately typed scalar records.

This re-lock does not authorize or claim:

- packet Hausdorffness or local compactness;
- a packet groupoid completion, packet Radon disintegration, or packet normal
  trace;
- transport of the one-orbit finite corner or no-normal-extension theorem to
  the packet;
- a global all-prime operator or trace;
- a determinant, A3, A4, or Route-B credit; or
- any change from packet-level `NOT_TESTABLE` absent the required same-map
  bridge.

Final mechanical re-lock: **PASS**.  Open Critical / Major / Minor findings:
`0 / 0 / 0`.
