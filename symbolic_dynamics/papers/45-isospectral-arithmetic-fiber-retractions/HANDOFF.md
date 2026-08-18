# P45 independent-writer-audit handoff

Status: `HOLD_FOR_INDEPENDENT_WRITER_AUDIT`

Audit only the candidate at `/tmp/paper45_writer_candidate`. Do not infer an
acceptance verdict from this writer-side record.

## External anchors

- `PAPER_MANIFEST.tsv` SHA-256:
  `2a9aff655b2040c61015b3f25394fa95bbb496d19b7a970854620b190c543893`
- `WRITER_REPORT.md` SHA-256:
  `fbcb1132bce7156c8fd76fcfbd12ddc9e9e679322ca43fef81a21f01d0c613ab`
- final `main.pdf` and `main_round2.pdf` SHA-256:
  `072bfb9de07b46f7705118ce8342b3f56a90fef45240ee24be33c9931b908783`
- protected50 snapshot SHA-256:
  `40c0d921d993b7e3401c2bdbbbe6eee3431aa4dc2f8c7603bf490b128c2794c4`

The previously reported intermediate PDF `33e6bad5709609d94d1da1ce911af9ab552009af52d5c4a02b3f9f4571f7333a`
was superseded by the phase-diagram repair and is not a final anchor.

## Suggested independent checks

1. Verify `WRITER_SEAL.json`, then recompute the handoff, report, and manifest
   hashes without trusting their contents first.
2. Run
   `python3 scripts/build_writer_manifest.py --root . --check`; require exactly
   43 manifest rows and no symlink, nonregular entry, cache, or transient build
   artifact.
3. Require `main.pdf` and `main_round2.pdf` to be byte-identical and match the
   final PDF hash above; retain the distinct round-zero and round-one PDFs.
4. Run `scripts/replay_protected50.py` with explicit candidate snapshot and
   authority paths; require `PASS`, static42, results8, and all 10 frozen fields.
5. Recheck the canonical result hashes and envelopes through
   `scripts/extract_canonical_results.py`, rebuild under epoch `1787011200`, and
   repeat font, text, bbox, and visual PDF checks.

The manifest intentionally excludes exactly four downstream closure files:
`PAPER_MANIFEST.tsv`, `WRITER_REPORT.md`, `HANDOFF.md`, and
`WRITER_SEAL.json`. The dependency direction is content to manifest to report
to handoff to seal. No manifest-covered artifact contains the seal hash.
