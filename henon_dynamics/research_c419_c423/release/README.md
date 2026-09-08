# C419–C423 exact release policy and verifier reuse

This release includes the entire actual research_c419_c423 tree: admitted
proofs and sources, unsuccessful scoped scouting work, manuscripts, every
retained build/snapshot, actual review/revision records, final evaluations,
logs, PNGs and other ordinary files, even if Git normally ignores them.
This is a byte/member contract, not a proof of mathematical correctness.

## Fixed implementation and preserved historical tests

The coordinator read in full the previous batch's 279-line
[exact_payload.py](../../continuation_c414_c418_round2/release/exact_payload.py),
315-line [tests](../../continuation_c414_c418_round2/release/test_exact_payload.py),
complete implementation README, test receipt and nonauthor code review.
The [current reuse preflight](PREFLIGHT_REUSE.md) was also read completely.
The decision is to use that unchanged implementation at its original fixed
repository path; no cosmetic schema rename or new copy is required.

- Implementation SHA256: 529ad136f29879c5bb659171127b45e7edb8e5b3c05044b4e43e035114cd444f
- Test SHA256: 2c5dc213ba100b724b707ac34c0d364be5330710f3b5b0d7995ef06d61668434
- Literal schema: c414-c418-exact-payload-v1. This is a reused format identity,
  not this batch number or an embedded authorization for a root directory.
- Historical [test receipt](../../continuation_c414_c418_round2/release/TEST_REPORT.md):
  21 normal and 21 optimized unittest methods, actually run on 2026-09-07.
- Historical [nonauthor code review](../../continuation_c414_c418_round2/release/REVIEW_CODE.md):
  PASS within the stated trusted-pin, trusted-verifier, quiescent Linux/POSIX
  tree contract. It is not a new current-payload test or a security certificate.

The implementation/test bytes and recorded Python 3.12.3 Linux/POSIX
environment are unchanged. The same recorded local XFS setting applies.
Old environment evidence lacks a full executable/environment fingerprint;
no stronger byte-for-byte environment equivalence is claimed. There is no
new code change or expanded portability/race/security claim to trigger a
replacement suite. The old tests are explicitly reused, not relabeled as
42 new executions. Actual inventory/check/seal/verify for this final tree
and an independent exact-membership scan must still be performed anew.

## Exact scope, trust and operation

Only root PAYLOAD_LEDGER.json and MANIFEST.sha256 are reserved metadata.
The ledger excludes both; the manifest includes the ledger and excludes
itself. Names use the implementation's ASCII component policy. Symlinks,
nonregular files, multiply linked files and unrepresented empty directories
are rejected rather than silently filtered or removed. No Git allowlist
substitutes for actual payload membership.

Finish all writers and all reports before inventory. Capture the generated
candidate outside the payload. The coordinator reviews its actual members,
lengths and identities, installs its approved exact bytes via apply_patch,
and records its new literal SHA256 outside the payload, bound to this exact
root and the fixed verifier above. Do not compute a new trust pin from a
live ledger at verification time. No previous batch pin is reused.

From outside the payload, use python3 -B with the fixed implementation and
the absolute root /root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c419_c423:
inventory first, then check with the approved literal pin, then seal once,
then read-only verify with that same literal. The actual commands, exits,
counts and hashes belong in the coordinator's external release receipt.
Seal must never overwrite an existing manifest. A validation failure
precedes publication writes; an I/O failure during publication needs
investigation and is not an unconditional rollback guarantee.

After sealing, a nonauthor checker must independently enumerate actual
members and recompute lengths/hashes and canonical manifest contents,
without importing or calling the producer's preflight. A plain
sha256sum -c alone cannot exclude unexpected files. The post-seal report
must stay outside this payload: even one new internal report/cache would
invalidate exact membership.

The authoritative external completion/approval receipt will be
[C419–C423 release receipt](../../RELEASE_C419_C423.md). This link is
prospective until that file is actually created; this policy does not
preclaim a seal, successful check, final member count or Git commit.
All writer-stop and trusted-input assumptions are explicit. Hashes do not
prove authenticity against replacement of both the verifier and approval
pin, and no hostile-writer or atomic whole-tree-snapshot guarantee is made.
