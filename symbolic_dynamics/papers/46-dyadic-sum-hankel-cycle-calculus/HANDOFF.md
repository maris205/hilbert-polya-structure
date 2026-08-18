# P46 independent-writer-audit handoff

Status: `HOLD_FOR_INDEPENDENT_WRITER_AUDIT`

Audit the exact P46 writer overlay; do not infer an installation or
publication verdict from this writer-side record.

## External anchors

- `PAPER_MANIFEST.tsv` SHA-256:
  `20f1331409e52d1cf5725268e729aa32f093042e8af43f3e90020859e7216ba8`
- `WRITER_REPORT.md` SHA-256:
  `df66d32f66dfbfd2e2ad183ea48386a31db41597a4dfc14054853013d2c6c96c`
- final `main.pdf` and `main_round2.pdf` SHA-256:
  `8772e8c9649bea045bace7b369d446ff51f5c9a7eb95c7e1bc957a9ff2f02d6e`
- portable protected-State-A manifest SHA-256:
  `5bc0050ccec0c77b9ca1f3ec0d4c95e381003e091a1ec738e5616676115c1fcc`
- protected-State-A replay SHA-256:
  `623d39ec942ac81537121ad0b03a1d447222fe2f7e8879dd1e5731fdb92dc3f8`

The earlier PDF
`db4edcb3c366736f1812948beca8472c13914e815815dd3f353b0c9771ccef3c`
was permanently withdrawn after text-extraction QA and is not a valid anchor.

## Required independent checks

1. Verify `WRITER_SEAL.json`, then independently recompute the handoff,
   report, and manifest hashes without trusting their embedded values.
2. Run `scripts/build_writer_manifest.py --root ABS_ROOT --check`; require
   exactly 49 self-excluding rows, 53 final regular files, exact directory
   closure, mode 0644 files, mode 0755 directories, and no symlink, cache,
   snapshot copy, protected path, or undeclared file.
3. Require `main.pdf` and `main_round2.pdf` to be byte-identical and match the
   final hash.  Preserve the distinct round-zero and round-one PDFs.
4. Rebuild twice under epoch `1787011200`; require the final PDF and
   bibliography to reproduce, then repeat log, font, text, bbox, page-size,
   and visual checks.
5. Run `scripts/replay_protected_statea.py` with explicit manifest, authority,
   Stage0 snapshot, State-A snapshot, and new `/tmp` output paths.  Require
   exact 83 nodes, 60 regular files, 23 directories, Stage0 58, outputs 25,
   two equal live captures, and zero mismatch/extra/mutation.
6. Re-run `scripts/extract_canonical_results.py` from an exact State-A output
   tree and require byte-identical canonical summary and results ledger.

The manifest intentionally excludes exactly four downstream closure files:
`PAPER_MANIFEST.tsv`, `WRITER_REPORT.md`, `HANDOFF.md`, and
`WRITER_SEAL.json`.  The dependency direction is content to manifest to
report to handoff to seal.  No manifest-covered artifact records the seal
hash.  All four closure files belong to the final publication writer overlay.
