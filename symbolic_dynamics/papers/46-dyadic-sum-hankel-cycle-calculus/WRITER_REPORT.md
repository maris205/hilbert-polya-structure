# P46 writer report

Candidate: `SD-C48` / paper 46 writer overlay

Status: `HOLD_FOR_INDEPENDENT_WRITER_AUDIT`

This is a writer-side closure record, not an independent publication
acceptance or authority-write authorization.

## Outcome

The candidate contains a complete 16-page paper on the dyadic-sum weighted
Hankel operator, its sharp boundedness, compactness, Hilbert--Schmidt and
trace-class thresholds, the typed 2-adic direct sum, determinant products,
and the complete fixed-ordered-label cycle solver.  The manuscript keeps the
complex left--right phase identity separate from conjugacy, proves the
combined-eigenvalue `det_2` product within its legal ideal regime, states the
even-cycle positivity interval explicitly, and never treats finite replay as
proof of an infinite theorem or as a priority finding.

The final paper artifacts are:

- `main.pdf` and `main_round2.pdf` SHA-256
  `8772e8c9649bea045bace7b369d446ff51f5c9a7eb95c7e1bc957a9ff2f02d6e`;
- preserved round-zero PDF SHA-256
  `2ddd1ca55ae73f18bcb732166c536f92c2963584ed4750446e2afc7e98eaa568`;
- preserved round-one PDF SHA-256
  `ab8b1ea5c7d98834dbe2ebb9389bad7dd6ab213d68ce8787226d06ca249136f2`.

The post-review ToUnicode repair permanently withdrew the earlier PDF
`db4edcb3c366736f1812948beca8472c13914e815815dd3f353b0c9771ccef3c`;
that byte string is not a manifest or seal anchor.

Two clean writer builds and two additional isolated closure-audit builds
produced the exact final PDF.  The closure-audit builds also reproduced the
final bibliography SHA-256
`2bd8b051f978b0124a143c8cdc064218a7e9ff4740990dc16df302554439c6f7`.
The final compile log is warning-free.  The final PDF has 16 A4 pages, 27/27
embedded, subsetted, Unicode-mapped fonts, no Type 3 font, and zero out-of-page
word boxes among 7,634 bbox-layout words.  Default, layout, and raw text
extraction each has zero illegal C0/DEL, C1, or replacement characters.  Full
measurements are in `evidence/PDF_QA.md` (SHA-256
`7031e8b61d2cbd6e79a5d97edafe60eb55658adc3f1e54a7fb8c6f6dc1c0988d`).

## Reviews and evidence

The same-reviewer plan gate reached 9.2/10, `PLAN_READY`, with zero critical
and zero major issue.  Manuscript round one identified no false theorem but
required a trace-norm compression bridge and direct-sum typing repairs.  Both
were implemented before round two, which returned `Ready` with zero critical
and zero blocking major issue.  Raw reviews and the complete change ledger
are retained byte-for-byte in `reviews/` and `PAPER_IMPROVEMENT_LOG.md`.

The finite integration projection remains evidence rather than proof.  Its
canonical results ledger SHA-256 is
`a0f669a865382da47776754d0a785d81fd7243fbb4f1d5f270dddeb5acfbe7a6`;
the writer summary and generated replay table are independently reproducible
from the exact State-A outputs.

## Protected State-A replay

`PROTECTED_STATEA_TREE.tsv` covers exact 83 nodes: 60 regular files and 23
directories, partitioned as the exact 58-node Stage0 tree plus the exact
25-node State-A `outputs/` tree.  Its SHA-256 is
`5bc0050ccec0c77b9ca1f3ec0d4c95e381003e091a1ec738e5616676115c1fcc`.

Two repeated read-only live-authority captures, the sealed Stage0 snapshot,
and the sealed State-A output snapshot all matched the manifest with zero
missing, extra, kind, mode, size, or byte mismatch.  The machine record is
`evidence/PROTECTED_STATEA_REPLAY.json` (SHA-256
`623d39ec942ac81537121ad0b03a1d447222fe2f7e8879dd1e5731fdb92dc3f8`).
No authority path was written.

## Exact installable overlay

The curated payload excludes `protected_stage0/**`,
`canonical_state_a_snapshot/**`, all superseded root snapshot ledgers,
draft/preflight documents, LaTeX auxiliary/cache files, and the publication
control namespace.  All 53 final writer files are regular mode 0644 and all
necessary writer directories are mode 0755.

`PAPER_MANIFEST.tsv` has 49 sorted content rows and SHA-256
`20f1331409e52d1cf5725268e729aa32f093042e8af43f3e90020859e7216ba8`.
It deliberately excludes exactly itself, `WRITER_REPORT.md`, `HANDOFF.md`, and
`WRITER_SEAL.json`.  The acyclic dependency is content to manifest to report
to handoff to seal.  No manifest-covered artifact contains the writer-seal
hash, and all four downstream closure files are themselves included in the
publication writer-overlay manifest.
