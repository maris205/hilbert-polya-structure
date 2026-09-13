# Paper 21 R0 Build-Receipt Canonical Repair

Date: 2026-08-22 UTC

This receipt-only repair responds to the exact blocker in
`INDEPENDENT_BUILD_R1_R0_REPAIR_REVIEW.md`. It changes no source, PDF,
generated build output, metadata object, temporary root, command, measured
value, page count, permission, or status.

## Predecessor and repaired identity

- Blocked receipt: `paper/BUILD_RECEIPT_R0.json`, SHA-256
  `48e61f31636c3e70f26da61b74fa9655c22a3ac954b9ae56b877cdebedcd5537`,
  7,339 bytes, one LF.
- Blocking review: `notes/INDEPENDENT_BUILD_R1_R0_REPAIR_REVIEW.md`,
  SHA-256
  `90d4c0ac6aa682dbd1ca0df5d1a3d75c42ba56d2a4df341643db888bf753be1c`,
  7,319 bytes, 148 LF, terminal `BUILD_R1_R0_REPAIR_BLOCK`.
- Repaired receipt: `paper/BUILD_RECEIPT_R0.json`, SHA-256
  `3899ee597562861623bd161a00063fc683f5f998499c677fd7e85e842f1a6e96`,
  7,339 bytes, one LF.

## Sole byte-level change

The final four keys of `$.checks` changed from the noncanonical order

```text
root_outputs_byte_identical,
underfull_hbox_count,
undefined_citation_count,
undefined_reference_count
```

to the declared ascending Unicode order

```text
root_outputs_byte_identical,
undefined_citation_count,
undefined_reference_count,
underfull_hbox_count
```

All four values are unchanged. No key was added or removed. No array order,
path, root snapshot, hash binding, byte count, LF count, command, environment,
authorization, source binding, PDF fact, or build status changed.

Strict parsing succeeds. Re-encoding the complete decoded value with recursive
canonical key order, compact separators, UTF-8, and one terminal LF reproduces
all 7,339 bytes exactly and has the same SHA-256
`3899ee597562861623bd161a00063fc683f5f998499c677fd7e85e842f1a6e96`.
The PDF remains SHA-256
`b02785a088008c3938652c28857347246dbf15e800d71269be7fdcd987e65fe3`;
the source remains SHA-256
`34074c5965086d79145bf2b273398c4c17fdc264b6f5e3555fd1b9a2bd27c7b2`.

This ledger does not grant build R1 PASS. A fresh replacement review must
rehash the repaired receipt and all bound artifacts. Rebuilding, source edits,
release, transport, and external effects remain closed.

`BUILD_RECEIPT_R0_CANONICAL_REPAIR`
