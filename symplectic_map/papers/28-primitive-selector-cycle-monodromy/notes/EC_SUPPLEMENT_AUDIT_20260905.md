# Paper28 EC supplement: independent recording-integrity audit

Date: 2026-09-05.
Decision: `EC_SUPPLEMENT_RECORDING_INTEGRITY_PASS`.

Audited root: `notes/dependency-ec-supplement-20260905` only.
Exact `outcome.json` SHA-256:
`507016423515267d4ab5ab55e9e08cc2818391a4f4e00ec803b3870d75645535`.

The outcome retains its original decision
`EC_METRIC_CAPTURED_AUDIT_PENDING`; this separate audit does not rewrite it.

## Verified evidence

- Directory membership is exactly the six sealed outputs (`intent.json`,
  `independent-review.json`, `attempt.json`, `metadata-before.json`,
  `metadata-after.json`, `ecrm1095.tfm`) plus `outcome.json`. Every entry is a
  regular file opened without following a leaf symlink. There are no additional
  entries or failure artifact in this new root.
- All six sealed output byte counts and SHA-256 values exactly match the
  outcome. The snapshot has 3584 bytes and 12 LF bytes, with SHA-256
  `6a3850cd71bbb2f43d98b7eb6b47f925de25626f5f4a0648c2d9d7b4b774eb2a`.
- Before/after metadata files are byte-identical and their parsed records are
  equal. They record size 3584, mode 0644, uid/gid 0, and unchanged device,
  inode, timestamps and link count. This verifies stored recording consistency,
  not a new independent measurement of the live host file.
- Intent, attempt, review and outcome agree on the single exact target
  `/usr/share/texlive/texmf-dist/fonts/tfm/jknappen/ec/ecrm1095.tfm` and the
  4096-byte budget. The expected size, recorded host bytes read and actual
  snapshot length are all 3584, below that budget. The outcome records
  `no_retry: true`; the intent scope is one EC TFM with no subprocess,
  installation, manuscript edit or build.
- The copied independent review is byte-identical to the named original, with
  SHA-256 `1c5e6916b1728bff6d7db418f6936fe917f9b4454218b3c6df95f562085f6be1`,
  matching the intent. Its decision remains
  `EC_SUPPLEMENT_CAPTURE_REVIEW_PASS`.
- Current script and plan byte counts/hashes equal the bindings in outcome,
  intent and review. Actual `main.tex`, `math_commands.tex` and
  `references.bib` bytes, hashes and LF counts equal all three source records.
  No source or control change was found.

## Boundary

The auditor accessed only the exact new capture root, the already named local
capture controls/review, and the manuscript trio. No live host font content or
metadata, old build root or previous capture root was accessed. No capture or
build was run. Only this audit document was written; all capture records retain
their original bytes.

This PASS concerns the supplement recording integrity. It is not a build/PDF
PASS, a guarantee that no later dependency will be missing, or permission to
relax existing source, loader, isolation or acceptance requirements.
