# C429–C433 exact release policy

2026-09-09 UTC. Status: **POLICY_PREPARED; FINAL_BUILD_AND_SEAL_GATES_PENDING**.
This is prospective policy, not a receipt that a release was sealed.
Five contracts are admitted; no completed paper is counted at this point.
The user's continuous-run rule makes five completed papers a checkpoint,
not a stopping condition or permission for external publication.

## Explicit root and unchanged verifier

The only intended payload root is
`/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c429_c433`.
The environment's initial `henon_zeta` directory is not this repository.
The coordinator must verify that exact absolute root and the relevant
Git state before invoking any release action. No unverified shell
variable, wildcard root, or similarly named directory is a substitute.

This batch reuses, without copying or changing, the established
[exact-payload verifier](../../continuation_c414_c418_round2/release/exact_payload.py).
Root completely read its 279-line source, 315-line tests, 100-line
README and complete historical test report, and recomputed both code hashes:

| Dependency | SHA256 |
| --- | --- |
| `exact_payload.py` | `529ad136f29879c5bb659171127b45e7edb8e5b3c05044b4e43e035114cd444f` |
| `test_exact_payload.py` | `2c5dc213ba100b724b707ac34c0d364be5330710f3b5b0d7995ef06d61668434` |

The old schema string `c414-c418-exact-payload-v1` identifies an
unchanged data format, not the authorized batch or root. The generic
tool does not independently know which mathematical batch the user
intended. Root selection is an explicit coordinator responsibility.
The verifier plus the literal outside approval pin is the trust boundary;
this is not a digital signature or an authenticity certificate.

## Reused regression receipt and actual new-tree checks

The [historical test receipt](../../continuation_c414_c418_round2/release/TEST_REPORT.md)
records 21 unittest methods under normal Python and 21 under optimized
Python on 2026-09-07, both exit 0. It binds the unchanged hashes above.
This batch has not rerun that suite and does not claim a new test run.

The actually read suite covers ignored/hidden/binary members, missing
and unexpected members, root/ancestor/file symlinks, hardlinks, special
files, empty directories, unsafe paths, duplicate/noncanonical/invalid
metadata, no-overwrite publication, second-preflight failure and real
CLI lifecycle. Recomputed manifests or ledgers still fail against the
original external pin after payload tampering. These are named tested
cases, not universal security or hostile-concurrency claims.

Observed current environment: Python 3.12.3, Linux 5.15.0-78-generic
x86_64. Both the historical and intended roots currently report XFS,
4096-byte filesystem blocks. These matching observed categories and
code hashes justify reusing the regression receipt, not a claim of
identical historical interpreter bytes or environment variables.
No release code or reusable build driver is changed. If such code
changes, its actual affected failure paths must be tested before use.

Every inventory, check, seal and verify for the **new actual tree**
must still execute. A prior payload's success cannot be reused.

## Final manuscripts and payload membership

Before inventory approval, finish both actual manuscript passes with
adjudicated repairs, changed-citation checks, evaluation acceptance,
and final source readback. Build every final paper twice in explicitly
named previously nonexistent directories with the recorded deterministic
settings; compare bytes and inspect actual text, fonts and final logs.
View every page of each selected final PDF. Archive the actual inputs,
commands, successes and failures; do not clean or overwrite earlier
baselines, review snapshots or build records. A paper-local preparation
or review log does not itself establish final reproducibility.

The ledger includes every actual regular file recursively under the
intended root: research reports, admitted proofs, evaluations, source,
PDFs, immutable reviews, real snapshots, ignored build auxiliaries,
images, hidden files and bytecode if present. There is no implicit
Gitignore filter or cache exclusion. The only ledger exclusions are
its own root filename `PAYLOAD_LEDGER.json` and root `MANIFEST.sha256`.
The manifest includes the approved ledger and every payload file,
excluding only itself.

All path components use the verifier's ASCII policy. Symlinks,
multi-linked regular files, special files and unrepresented empty
directories are rejected, not silently omitted or deleted. Any actual
conflict must receive an explicit scoped disposition. Merely rerunning
inventory to approve an unexplained change is not remediation.
C430's relative C431 companion source/PDF dependency must remain in
the shared distribution. This repository-layout release is not a claim
that an isolated C430 PDF is a complete standalone proof package.

## Approval, sealing and post-seal records

Finish all in-tree documentation and stop every writer. Work from
outside the exact root using `python3 -B`. Capture the stdout inventory
candidate outside the root; shell redirection into a root metadata file
would create that file before the scan and is not permitted.
Review the complete member set and preserve a literal approved ledger
SHA256 in a receipt outside the root. Install the approved canonical
ledger bytes with `apply_patch` and compare them with the candidate.
Do not use a fresh live rehash as a verification trust pin.

Run `check`, then one actual `seal`, then `verify`, all against that
same literal pin. The seal performs two full preflights before atomic
no-replace publication; an existing manifest is never overwritten.
Then perform independent exact-member/digest reconstruction and final
read-only verification. Preserve failures rather than deleting them
or silently repinning.

All post-seal execution, synchronization and checkpoint receipts belong
outside this root. Adding or editing even an ignored file afterwards
invalidates its exact membership or bytes. Quiescent-tree operation is
required; the tool is not a filesystem snapshot, hostile-writer defense
or crash rollback. A crash during publication may leave an artifact
that requires investigation. Hashes establish byte/member identity,
not mathematical correctness, independent originality or peer review.

Routine exact-path commit and synchronization to the configured remote
are authorized after these gates. Inspect remote advancement before
integration; do not force-push, add remotes, include inherited unrelated
material, modify another stream, submit a manuscript, upload to an
external review service or enter Route B. Save the completed checkpoint
and continue authorized Hénon/Route-A research in a new unsealed batch
when useful; do not reopen this sealed payload for the next batch.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
