# C424–C428 exact release policy and unchanged-tool reuse

2026-09-09 UTC. This batch uses the unchanged, already reviewed
[exact payload tool](../../continuation_c414_c418_round2/release/exact_payload.py).
The coordinator read its complete 279-line source, 315-line tests,
100-line README and historical test report, and measured these hashes:

| Fixed dependency | SHA256 |
| --- | --- |
| exact_payload.py | `529ad136f29879c5bb659171127b45e7edb8e5b3c05044b4e43e035114cd444f` |
| test_exact_payload.py | `2c5dc213ba100b724b707ac34c0d364be5330710f3b5b0d7995ef06d61668434` |

The legacy schema `c414-c418-exact-payload-v1` is an unchanged format
identity, not this batch's ID or allowed root. The explicit current root
is `/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c424_c428`.
There is no need to copy or relabel old code, invoke old mathematics,
or change this format merely because the batch number changed.

## Reused failure-path evidence, not a new test run

The [historical receipt](../../continuation_c414_c418_round2/release/TEST_REPORT.md)
records normal and optimized Python runs of 21 unittest methods each
on 2026-09-07: exit 0, 0.553s and 0.638s. Its tested source hashes
match the unchanged implementation and tests above. This batch did
not rerun that suite and does not claim a new 21+21 PASS.

The suite includes missing/unexpected/ignored members, symlinks and
hardlinks, unsafe paths, duplicate/invalid canonical metadata,
no-overwrite publication, a second-preflight failure, real CLI
lifecycle and tampering with recomputed manifests/ledgers still
checked against the original external approval pin. These are actual
named historical tests, not a universal security guarantee.

Current Python is 3.12.3; platform Linux 5.15.0-78-generic x86_64.
The old and new roots currently report XFS with 4096-byte blocks.
Those observed version/platform categories support reuse of the
unchanged-code regression receipt, not proof of identical historical
interpreter bytes, mounts, environment variables or arbitrary platforms.
No release code change was made. New-tree inventory/check/seal/verify
must actually execute; an old payload's PASS cannot be reused.

## Exact contract and order

The ledger lists every actual regular payload file recursively,
including ignored build outputs, historical snapshots, hidden files
and bytecode if present. It excludes only its own root name
PAYLOAD_LEDGER.json and the root MANIFEST.sha256. The manifest includes
the approved ledger and every payload file, and excludes only itself.

All path components must meet the fixed ASCII policy. Symlinks,
multi-linked regular files, special files and unrepresented empty
directories are rejected. Nothing is silently filtered by Gitignore
or deleted to satisfy a checksum list. Any real conflict requires an
explicit scoped disposition before final approval.

Finish all five manuscript/evaluation/build gates and final in-tree
documentation, then stop every writer. Run inventory from outside the
payload and capture its candidate outside the payload. Review the
actual complete member set and preserve a literal approved ledger
SHA256 in an outside receipt before check/seal/verify. Install those
approved canonical bytes with apply_patch and compare with the
candidate. Never use a live rehash as a fresh trust pin.

Run check, then the one actual seal, then verify with that same pin.
Seal validates twice before atomic no-replace publication; existing
manifests are not overwritten. Independent final membership/digest
verification follows. After sealing, all new execution/Git receipts
belong outside the exact root; adding even an ignored file invalidates
membership. No write-time claim is prefilled as actual seal success.

Quiescent local-tree operation is required. This is byte/member
integrity, not authenticity against replacement of verifier plus pin,
mathematical correctness, hostile-concurrency protection or crash
rollback. Preserve failures and investigate rather than repinning.

Routine exact-path commit and synchronization to the configured
repository are authorized. Inspect remote advances for overlap first;
no force push, new remote, unrelated inherited file, other stream,
journal submission, third-party manuscript upload, Route B or C429.
