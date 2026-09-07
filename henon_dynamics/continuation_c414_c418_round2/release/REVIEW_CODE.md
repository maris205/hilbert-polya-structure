# Nonauthor review of the exact-payload release code

Date: 2026-09-07 UTC. Verdict: **PASS within the declared quiescent-tree,
trusted-verifier and externally pinned-ledger contract. No blocking code
or test-claim defect identified; no source revision required.**

This is an independent current-team static code review, not the author's
test receipt, a security certification or a real-tree sealing result.
The reviewer did not implement these files. Root and the code author
confirmed that all four reviewed inputs were frozen before this report
was finalized. Only `release/REVIEW_CODE.md` was written by this review;
no code, tests, paper, evaluation, global state or Git index was changed.

## Exact inspected inputs

The reviewer read all four files completely: 279 lines of implementation,
315 lines of tests, 100 lines of README and 122 lines of final test report
(816 lines total). Fresh read-only SHA256 checks after freeze confirmation
gave:

| Input | SHA256 |
|---|---|
| [exact_payload.py](exact_payload.py) | `529ad136f29879c5bb659171127b45e7edb8e5b3c05044b4e43e035114cd444f` |
| [test_exact_payload.py](test_exact_payload.py) | `2c5dc213ba100b724b707ac34c0d364be5330710f3b5b0d7995ef06d61668434` |
| [README.md](README.md) | `ff574e92a53130bdb1e6fdc0523eb49787ca64584e947041db5cecb497f8273c` |
| [TEST_REPORT.md](TEST_REPORT.md) | `cd685942b2283815fdd5672f5a8d65c50e5b879efa6e36f29c4ee6ae74762665` |

No module import, producer test, optimized test, inventory, check, seal or
verify command was executed by this reviewer. The reported 21 normal
and 21 optimized test-method executions remain explicitly author-side
evidence, not fresh reviewer runs.

## 1. Exact membership, path policy and canonical metadata

**Pass.** `scan` traverses actual directory entries rather than Git's
tracked/ignored list. Hidden files, ignored build artifacts and binary
payloads are included. Its file-descriptor traversal does not follow
root, ancestor, directory, regular-file or dangling symlinks. Regular
files with multiple hard links and nonregular members are rejected.
The ASCII component grammar rejects traversal, duplicate separators,
control characters and ambiguous path spellings. Directory membership
is separately required to equal the ancestors of the file members, so
unrepresented empty directories cannot silently escape the policy.

`preflight` compares the actual and expected payload path sets for exact
equality, then compares every path/byte-length/digest entry. Thus checking
only listed files, or ignoring an unexpected auxiliary file, cannot yield
a PASS. Reserved names are the two *root* metadata files; a similarly
named file in a subdirectory remains ordinary payload.

The ledger excludes both root metadata files. The expected manifest
includes all payload entries plus the ledger, excludes itself, and is
compared as the exact canonical sorted byte string. Missing, duplicate,
reordered, extra or self-including manifest lines are not normalized away.

The ledger parser checks the exact top-level and entry shapes, strict
integer types rather than accepting Booleans, nonnegative lengths and
totals, lowercase 64-digit hashes, strictly sorted unique paths, and
canonical JSON bytes. Duplicate JSON keys are rejected during parsing.
Malformed ledgers with a matching supplied digest still have to pass
these structural checks. The scanner's metadata read limit does not
silently truncate a ledger or manifest; oversize metadata is rejected.

## 2. External trust pin and recomputed-digest tampering

**Pass under a fixed external approval pin.** `parse_ledger` first checks
the supplied literal pin's format and equality to the raw ledger digest.
Neither `check`, `seal` nor `verify` derives a new trusted value from the
live ledger. `inventory` is correctly documented as a candidate generator,
not as an approval of its output or existing metadata.

The recomputed-digest claims have the necessary distinctions:

- Changing payload bytes alone fails the ledger's length/digest comparison,
  including a same-length change.
- Changing payload bytes and recomputing only the manifest does not change
  the approved ledger; the payload comparison still fails.
- Recomputing the ledger and manifest as well fails the original external
  ledger pin before the altered ledger can become authority.

These are the actual boundaries exercised by the corresponding tests;
they are not the weaker assertion that an unrecomputed hash detects a
changed file. Integrity still depends on both the originally approved pin
and the reviewed verifier remaining trusted. Replacing either trust input
or approving a new pin is outside this review's guarantee; a checksum is
not a signature or independent proof of authenticity.

## 3. Validation before writes and no-overwrite publication

**Pass.** The CLI's `seal` route performs two complete read-only preflights
and compares their returned approved data before calling the publisher.
No payload, metadata output or temporary file is created on those
validation paths. Reads may update access times, as the documentation
states. Running with `-B` is important to keep Python's own import cache
out of the protected tree.

The publisher creates a new random temporary with exclusive creation
and no-follow flags, writes and flushes its contents, and fsyncs it.
Publication uses a same-directory hard link to the final manifest name,
not an overwriting rename or replace. An existing destination therefore
cannot be overwritten by that publication operation. The normal cleanup
unlinks only the publisher's newly created temporary; it does not delete
or rewrite payloads or an existing manifest.

The preflight's manifest-absence rule rejects valid and invalid existing
seals alike. The separate direct-publisher test checks the no-replace
operation itself rather than relying only on the earlier absence check.
The injected second-preflight failure verifies that one successful
preflight is not enough to authorize publication.

Publication I/O failures are a different boundary from validation
rejections. An error after the manifest link is created, a failed cleanup
or a process/storage crash can leave an artifact even if the command does
not return success. The README and report explicitly disclose this and
do not promise unconditional rollback. Such an artifact requires
investigation, not silent reinventory, repinning or overwriting.

## 4. Concurrent-writer and operational boundary

**Pass with the stated limitation retained.** Descriptor traversal and
before/after metadata checks catch observed file replacement, mutation
during a file's read, and directory-entry changes during traversal. They
do not turn a recursive scan into a filesystem snapshot. For example,
an in-place write after a file's last hash check need not change its
parent directory's metadata. The interval after the second preflight
and before publication also remains outside an atomic whole-tree snapshot.

Consequently, two passes are not proof that every possible concurrent
change is detected, and this review does not make that claim. The
explicit requirement to stop all writers while inventorying, approving,
checking and sealing is essential. The documented post-publication
verification and independent exact-member check remain necessary.
Hostile concurrent modification is expressly outside the contract.

The implementation uses Linux/POSIX descriptor and publication facilities
matching the recorded test environment; cross-platform portability is
not inferred. Whether the real payload satisfies the strict name,
link-type and nonempty-directory policy must still be checked by the
coordinator. This source-code PASS is not a real-tree policy PASS.

## 5. Test coverage and receipt accuracy

**Pass as bounded author-test evidence.** All 21 named unittest methods
are present. Their assertions cover the success lifecycle, hidden and
ignored/binary members, missing and extra files, fixed-pin tampering,
malformed and noncanonical metadata with matching pins, path aliases,
symlinks including root/ancestor links, FIFO and hard-link rejection,
empty directories, existing/corrupt manifests, and no-replace publication.

Rejected-seal fixtures compare the declared before/after snapshots and
assert that the publisher was not called. The snapshots cover member
names, file types/modes/link counts, symlink targets and bytes; they are
not a claim to compare every filesystem timestamp. Optimized-process
tests are relevant because the implementation uses explicit exceptions,
not removable Python assertions, for validation.

The second-preflight change is correctly called an injected failure in
the report, not a comprehensive race test. The count of 21 refers to test
methods and is not promoted to exhaustive branch or mutation coverage.
The normal/optimized timings and exit statuses are attributed to the
author's report. This review did not rerun them or independently certify
every historical test-process detail.

## Adjudication and remaining coordinator work

No required revision emerged from this independent inspection. The code
and its declared claims are suitable for the specified byte/member gate,
provided the reviewed verifier, fixed external approval pin and quiescent
tree conditions are maintained.

The coordinator must still finish all payload writers, include this review
in the candidate inventory, approve that exact inventory outside the tree,
install the approved ledger, and execute the authorized check/seal/verify
and independent exact-member/digest checks. A post-seal receipt must remain
outside the sealed payload. The code does not establish the existence of
five complete papers, their mathematical validity, review or evaluator
grades, worldwide priority or target arithmetic progress.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
