# Exact payload release boundary

This small standard-library Python tool implements only the byte/member release
gate in `../BATCH_PLAN.md`. It does not prove mathematics, approve citations,
build PDFs, inspect pages, run evaluations, update indexes, stage Git, or certify
authenticity. The coordinator owns those gates and the actual release seal.
No real-tree ledger or manifest is produced by the implementation/testing task.

## Contract and trust

The root files `PAYLOAD_LEDGER.json` and `MANIFEST.sha256` are reserved metadata.
The canonical JSON ledger lists every other actual regular file recursively,
including ignored logs, TeX auxiliary files, PNGs, bytecode and hidden files.
It records each relative path, exact byte length and SHA-256, plus totals.
The manifest lists the same payload **and the ledger**, excludes itself, and
is a sorted, exact `sha256sum`-style byte string with a final LF. Nothing uses
Git's tracked/ignored classification, and nothing deletes old author artifacts.

The ledger's SHA-256 is an external approval pin supplied explicitly to `check`,
`seal` and `verify`. Review the candidate and preserve that exact literal hash
outside the payload before sealing. Never substitute a fresh hash of the live
ledger at verification time. A tampered payload with a recomputed manifest, or
even a recomputed ledger and manifest, fails against the original approved pin.
Changing both the trusted pin and verifier is outside this integrity boundary;
the scheme is not a digital signature or independent proof of authenticity.

Paths use nonempty slash-separated ASCII `[A-Za-z0-9_.-]+` components other than
`.` and `..`. Absolute paths, traversal, aliases through duplicate separators,
backslashes, spaces, control bytes, non-ASCII names, and colons are rejected.
Symlinks (including root/ancestor and dangling links), nonregular files, and
regular files with multiple hard links are rejected. Directories must be exactly
ancestors of files: unrepresented empty directories are rejected, not deleted.
Canonical JSON rejects duplicate/unknown keys, wrong types (including Boolean
integers), invalid totals, unsorted/duplicate paths and self-reference. Binary
payload contents are unrestricted; only metadata has a 16 MiB read limit.

The tree must be quiescent while inventoried, approved, checked and sealed.
Nonfollowing file-descriptor traversal and metadata stability checks reject
ordinary changes during a scan. Sealing completes two full read-only preflights
before creating any output or temporary file, then uses atomic no-replace
publication. Any existing manifest, valid or not, blocks sealing without
overwriting it. A publication error cleans up only its own newly created temp.
Preflight rejection performs no writes. This is not a filesystem snapshot or
a defense against a hostile concurrent writer; after publication, the
coordinator must verify again. A crash or storage failure during publication
can leave a manifest or temporary file; investigate it rather than rerunning
inventory to approve the changed state. No unconditional rollback is claimed.

## Coordinator handoff

1. Finish all mathematical/manuscript/citation reviews, deterministic fresh
   builds, text/font/warning checks, and visual inspection of every final page.
   Finish release documentation and receipts that belong inside the payload.
   Stop all writers. Leave every actual author artifact present.
2. Review this verifier, its tests and test report. Use a reviewed copy of the
   verifier and preserve the approval pin separately. Run with `python3 -B`
   to avoid generating bytecode in the release root.
3. Run `inventory ROOT` to **stdout** and capture/review the candidate outside
   `ROOT`. Do not redirect stdout to either metadata file inside `ROOT`: the
   shell creates the file before scanning. Check exact membership and policy
   acceptance, then write the approved bytes to `ROOT/PAYLOAD_LEDGER.json`
   with the authorized file-edit mechanism. Record the literal hash outside
   the payload. The coordinator, not this utility, approves the ledger.
4. Run `check ROOT --ledger-sha256 APPROVED_LITERAL` (read only), then
   `seal ROOT --ledger-sha256 APPROVED_LITERAL` (manifest creation only).
5. Run `verify ROOT --ledger-sha256 APPROVED_LITERAL` (read only) and an
   independent exact-member/digest check. Keep the post-seal receipt outside
   the sealed tree; adding even a report or ignored file inside invalidates
   exact membership. The ledger excludes itself and the manifest; the
   manifest includes the ledger and excludes itself.

Example invocations from the repository root (replace `ROOT` and
`APPROVED_LITERAL`; these are deliberately not executable shell variables):

```text
python3 -B henon_dynamics/continuation_c414_c418_round2/release/exact_payload.py inventory ROOT
python3 -B henon_dynamics/continuation_c414_c418_round2/release/exact_payload.py check ROOT --ledger-sha256 APPROVED_LITERAL
python3 -B henon_dynamics/continuation_c414_c418_round2/release/exact_payload.py seal ROOT --ledger-sha256 APPROVED_LITERAL
python3 -B henon_dynamics/continuation_c414_c418_round2/release/exact_payload.py verify ROOT --ledger-sha256 APPROVED_LITERAL
python3 -B henon_dynamics/continuation_c414_c418_round2/release/test_exact_payload.py
```

Each non-inventory command exits 0 only on PASS; rejection exits nonzero.
`inventory` is a candidate generator, not a validation or approval of any
preexisting metadata. `check` requires no manifest; use `verify` after sealing.
An intentional post-approval change requires coordinator review and a new
explicit approval; the tool neither silently repins nor replaces a seal.

## Prior-pattern assessment

The C409–C413 release ledger and final-build report recorded a one-off exact
inventory, not a reusable generic verifier. No reusable verifier was found in
the nearby C399–C413 continuation trees. The earlier
`henon_quadratic_generic_arboreal_route_a/code/c393_release_manifest.py` couples
release work to old mathematical/evaluation lanes and its traversal does not
reject symlinks; importing or invoking it would violate this task's scope.
Its canonical-data/strict-type ideas and the corresponding short smoke-test
pattern were inspected read-only. No old mathematical checks or builds ran.
The new tool isolates the required member/digest boundary and uses explicit
exceptions rather than assertions, so checks remain active under `python -O`.
