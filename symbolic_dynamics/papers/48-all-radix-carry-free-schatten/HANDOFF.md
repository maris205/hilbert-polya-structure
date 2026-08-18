# Paper 48 independent-writer-audit handoff

Status: `HOLD_FOR_INDEPENDENT_WRITER_AUDIT`

Audit the exact writer overlay at
`/tmp/paper48_writer_candidate/FINAL_WRITER_OVERLAY`.  Do not infer CLEAN,
installation, publication, Git, README, mirror, or authority-write permission
from this writer-side handoff.

## External anchors

- `PAPER_MANIFEST.tsv` SHA-256:
  `dc202c75ce087f944f42ab39f6ba75d616a100dcc4e6822a2a8154d0f6269efa`;
- `WRITER_REPORT.md` SHA-256:
  `a5342c0cb6d9c2f40b4913453782eedab53afce12d69ccf8f7c7ea4bfa962d6e`;
- final PDF SHA-256:
  `5bb755f9b2b0eaf56c79b8de5e94253bc9e7ed4b8d6ef9fd4c815f832cf54573`;
- portable protected-State-A manifest SHA-256:
  `2c45b1c5cf683855b1a7b798edb719e9ab117d3223aa1d5cf4678efb12f16191`;
- protected-State-A replay SHA-256:
  `d3db2a0579a96606da778c86f217849f2931b456f9e1e3556c307bd946c4d36c`;
- structured PDF-QA SHA-256:
  `35ca8645da483bf30c098a9f5c66db83f75dd01dc423b180ec434805e6021ed1`;
- canonical summary SHA-256:
  `f3105dfe1733bcd8aa240d9ebcf9125acc44704a96d7c5682fbf991381548b3d`;
- canonical results-ledger SHA-256:
  `dd1fbc2ee0fb16bf4df7ff74cbc2dc59fa00e02e18d545f3b782c1ee4f55fc62`.

## Protected inputs for audit

- live authority:
  `/root/autodl-tmp/hilbert-polya-structure/symbolic_dynamics/papers/48-all-radix-carry-free-schatten`;
- externally produced post-output audit:
  `/tmp/p48-post-output-independent-audit.YT2CT8`;
- candidate-only frozen Stage-0/A/B inputs:
  `/tmp/paper48_writer_candidate/frozen_inputs`.

These paths are inputs only.  The writer did not modify them, except that the
last path is its own `/tmp` frozen-copy workspace.

## Required independent checks

1. Verify `WRITER_SEAL.json`, then independently recompute the handoff,
   report, and manifest hashes without trusting embedded values.
2. Run
   `python3 -I -B scripts/build_writer_manifest.py --root ABS_OVERLAY --check`.
   Require exactly 50 manifest-covered content rows, 54 final regular files,
   11 directories including the root, modes 0644/0755, and no extra node.
3. Independently parse the protected TSV and capture the live authority
   twice.  Require 75 nodes (57 regular, 18 directories), exact 59-node
   Stage 0, exact 16-node `outputs/`, and State-A tree `c23b5903...`.
   Then run `scripts/capture_protected_statea.py --check` with explicit live
   authority, frozen Stage 0, raw post-output verdict, and an isolated copy of
   this overlay.  Do not treat the verdict or finite replay as proof.
4. Re-run `scripts/extract_canonical_results.py` twice: live-A/frozen-B and
   frozen-A/frozen-B.  Require byte-identical summary `f3105dfe...` and ledger
   `dd1fbc2e...`, with 1,965 rows per lane, 8,010 digit intervals, and 420
   shell rows.
5. In two fresh isolated overlay copies, run
   `python3 -I -B scripts/generate_paper_assets.py`, then run
   `bash build.sh` from `paper/`.  Require byte-identical generated assets and
   PDFs, with final PDF `5bb755f9...` at fixed epoch 1787011200.
6. Run `scripts/check_pdf_qa.py` using the two fresh PDFs.  Independently
   repeat Poppler default/layout/raw, PyMuPDF, unsanitized raw-bbox XML,
   fonts, citations, final-log, A4/16-page, exact Unicode page-count, and
   visual checks.  Require all illegal Unicode counts zero and minimum page
   7/value 1,180.
7. Verify the bounded repairs directly: semantic/glyph mappings, Lucas DOI
   volume 6, the one-sided `N_0` shift, and Unicode rather than byte page
   counts.  Confirm the withdrawn `daaf6435...` PDF is absent and the only
   publication PDF is `5bb755f9...`.
8. Read the raw plan and two-round manuscript reviews without silently
   transferring the historical round-2 ACCEPT disposition to the repaired
   PDF.  Independently audit the nonregression anchors.
9. Recheck that analytic arguments own all infinite endpoints and trace
   statements, while finite PASS, mutation, protected-tree, and machine
   certificate records remain validation/provenance evidence only.

## Self-excluding closure

The manifest excludes exactly four downstream closure files:
`PAPER_MANIFEST.tsv`, `WRITER_REPORT.md`, `HANDOFF.md`, and
`WRITER_SEAL.json`.  All four belong to the final writer overlay.  The
dependency direction is content to manifest to report to handoff to seal;
the seal is self-excluded.  A positive independent writer audit may recommend
the next root-controlled step, but this handoff itself authorizes none.
