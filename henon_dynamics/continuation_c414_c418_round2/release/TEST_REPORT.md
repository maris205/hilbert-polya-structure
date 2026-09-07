# Release verifier implementation and test receipt

Status: implementation tests PASS; coordinator review and actual release sealing
remain separate. This is an author/testing receipt, not an independent review
or a claim that the five-paper release has been built or sealed.

## Scope and prior inspection

Implemented only `release/exact_payload.py`, `release/test_exact_payload.py`,
`release/README.md`, and this report in the new continuation tree. The real-tree
`PAYLOAD_LEDGER.json` and `MANIFEST.sha256` were not generated. No paper, global
state, evaluation, Git index, old mathematical checker, or old build was changed
or run by this implementation task. Tests create and automatically clean up
their own named temporary fixtures outside the real release tree.

Before implementation, the current BATCH_PLAN release gate, prior C409–C413
artifact ledger/final-build report, nearby continuation release infrastructure,
and the earlier C393 manifest program and short smoke-test pattern were inspected
read-only. There was no sound generic drop-in reuse: the C393 program invokes
old domain-specific lanes and does not enforce this task's path/symlink contract.
The new tool is a separate standard-library byte/member gate.

## Executed checks

Environment: Linux/POSIX filesystem, Python 3.12.3. Working directory:
`/root/autodl-tmp/hilbert-polya-structure`. Test date: 2026-09-07 UTC.

```text
python3 -B henon_dynamics/continuation_c414_c418_round2/release/test_exact_payload.py
Ran 21 tests in 0.553s
OK
exit code: 0

python3 -B -O henon_dynamics/continuation_c414_c418_round2/release/test_exact_payload.py
Ran 21 tests in 0.638s
OK
exit code: 0
```

The optimized run matters because validators use explicit exceptions; disabling
Python assertions must not bypass any check. The suite also launches a separate
optimized-process tamper case and a complete CLI check/seal/verify/reseal lifecycle.

The final 21 test methods were:

```text
test_cli_check_seal_verify_and_reseal_lifecycle
test_cli_inventory_and_missing_pin_are_read_only
test_fifo_hardlink_empty_directory_and_unsafe_actual_name
test_file_directory_dangling_and_metadata_symlinks
test_inventory_includes_ignored_hidden_and_binary_files
test_malformed_json_rejected_even_with_matching_pin
test_manifest_corruptions_and_existing_manifest_never_overwritten
test_missing_and_unexpected_members
test_missing_ledger_and_invalid_pin
test_no_replace_publication_cleans_only_own_temporary
test_noncanonical_ledger_rejected_with_matching_pin
test_optimized_python_still_rejects_tamper_without_writes
test_recomputed_ledger_and_manifest_cannot_bless_payload_with_old_pin
test_recomputed_ledger_cannot_bless_unsealed_tamper_with_old_pin
test_recomputed_manifest_cannot_bless_payload_tamper
test_root_and_ancestor_symlinks
test_same_length_payload_tamper_rejected
test_schema_types_totals_order_and_entry_shapes
test_second_preflight_failure_cannot_publish
test_success_manifest_includes_ledger_excludes_itself_and_preserves_payload
test_unsafe_and_self_referential_ledger_paths
```

Several methods contain independent adversarial subcases; the count of 21 is
the number of unittest methods, not a count of all mutation inputs. These include
duplicate keys, malformed UTF-8/JSON, NaN, wrong schema, missing/unknown fields,
Boolean/float/negative integer fields, incorrect totals, wrong/uppercase digest
forms, duplicate/unsorted paths, absolute/traversal/control/non-ASCII/alias paths,
metadata self-reference, noncanonical whitespace/newlines, extra ignored files,
missing files, missing/extra/duplicated/reordered manifest entries, omitted ledger,
manifest self-inclusion, and no-overwrite behavior for valid and invalid seals.

Each rejected sealing fixture takes a before/after snapshot of member names,
file types/modes/link counts, symlink targets, and regular-file bytes, and asserts
that the publishing function was never called. Reads may update filesystem
access times; that is not included in the no-write claim. The second-preflight
failure is injected to confirm that the first successful pass does not publish.
The publication-only no-replace test additionally preserves an existing
manifest and confirms cleanup of only the publisher's own new temporary file.

Tampering is tested at three distinct boundaries: changed payload alone; changed
payload plus recomputed manifest; and changed payload plus recomputed ledger and
manifest. The latter remains rejected by the original external approval pin.
Malformed ledgers are also tested with matching hashes, so rejection cannot be
attributed merely to a changed hash.

## Tested source identities

```text
529ad136f29879c5bb659171127b45e7edb8e5b3c05044b4e43e035114cd444f  exact_payload.py
2c5dc213ba100b724b707ac34c0d364be5330710f3b5b0d7995ef06d61668434  test_exact_payload.py
ff574e92a53130bdb1e6fdc0523eb49787ca64584e947041db5cecb497f8273c  README.md
```

This report does not include its own hash, which is recorded in the handoff.
The coordinator's final payload ledger should include all four files and any
subsequent review receipt; the manifest will then include that ledger as well.

## Exact coordinator responsibilities

The coordinator must independently review code/contract and decide whether the
file/path policy fits the actual quiescent payload. They must finish the five
papers' proof/manuscript/source reviews, two fresh deterministic builds,
text/font/warning checks and actual all-page visual inspection before approving
the final inventory. They then review the stdout-only candidate ledger outside
the payload, install the approved canonical ledger, preserve its literal SHA-256
outside the tree, run `check`, run the actual `seal`, run `verify`, and perform
an independent exact-member/digest check. Post-seal receipts belong outside the
sealed tree. Do not rehash a changed live ledger and treat that value as trusted.

This implementation makes no claim of authenticity against replacement of both
the verifier and external approval pin, mathematical/evaluation validity, or
protection against hostile concurrent writers. It requires a quiescent tree.
All validation rejection happens before publication writes; crash/storage errors
during publication are a different case and can leave an artifact requiring
coordinator investigation. Existing manifests are never replaced automatically.
