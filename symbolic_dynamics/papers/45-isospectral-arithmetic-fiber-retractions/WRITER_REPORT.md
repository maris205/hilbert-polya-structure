# P45 writer report

Candidate: `/tmp/paper45_writer_candidate`

Status: `HOLD_FOR_INDEPENDENT_WRITER_AUDIT`

This is a writer-side handoff, not an independent acceptance finding.

## Outcome

The candidate contains a complete 17-page paper on the paired all-$h$
arithmetic retractions, their exact common nonzero spectral ledger, the
isospectral-but-not-similar interval, saturated projection growth, Schatten
and self-commutator walls, two Weyl laws, and the primorial nonnormality
transition. The source states every endpoint strictly where the canonical
contract does and separates proved infinite statements from finite
recomputation evidence.

The final paper artifacts are:

- `main.pdf` and `main_round2.pdf` SHA-256
  `072bfb9de07b46f7705118ce8342b3f56a90fef45240ee24be33c9931b908783`;
- preserved round-zero PDF SHA-256
  `4bc233960f6da4467b7ebbe517466cd8a9407d23c86f0fed6d22703aa0dfa2a3`;
- preserved round-one PDF SHA-256
  `14fa5152e225102931628bab8193c27c3fb1fd6df75c697d312048d9f3861aed`.

Two fresh builds under the fixed epoch `1787011200` were byte-identical. The
final PDF has 17 A4 pages, 24/24 embedded and subsetted fonts with Unicode
maps, no Type 3 fonts, no unresolved references/citations, no box diagnostics,
zero unexpected C0 text bytes, zero replacement characters, and zero bbox
overflows among 7308 extracted words. All 17 pages were visually inspected;
the draft phase-diagram overlap was repaired and the final page 9 was checked
again at original raster resolution. Full measurements are in
`evidence/PDF_QA.md` (SHA-256
`eea54d15a9eb05b543890b064b6ed15468c495c37d55099fea50bd253fe845d3`).

## Reviews and evidence

The plan-review gate moved from 7.4/10 (`REVISE`) to 8.9/10 with no remaining
critical or major issue. The two required GPT-5.4 xhigh manuscript rounds were
completed: round one scored 7/10 and identified two major issues; their fixes
were implemented before round two, which scored 8/10 and reported zero
critical and zero major issues. Raw reviews and the change ledger are retained
in `reviews/` and `PAPER_IMPROVEMENT_LOG.md`.

Primary-source bibliographic verification and the canonical-result mapping are
retained in `evidence/SOURCE_VERIFICATION.md` and
`evidence/CANONICAL_RESULTS_LEDGER.md`. The regenerated canonical projection
has SHA-256
`e1042078bdc67d3d5c520fd029c45367813c16d0879c23681cf14ea48a0ee7e2`;
the exact generated finite table has SHA-256
`0b4d1765c239342c7ba5f9f625e8a53af95af7153934d17a7bce4f021e05361c`.

## Protected authority replay

The pre-write snapshot has SHA-256
`40c0d921d993b7e3401c2bdbbbe6eee3431aa4dc2f8c7603bf490b128c2794c4`.
The final read-only replay matched all 50 protected regular files, partitioned
as static42 plus results8, across bytes and all frozen fields: type, mode,
uid, gid, size, mtime_ns, inode, nlink, device, and SHA-256. The machine record
is `evidence/PROTECTED50_REPLAY.json` (SHA-256
`ecf348a6575a73e5c7d3cefd01448a7fa5b5daa9277c5b7efd9469291400b9ba`).
No authority path was written.

The Git perimeter was read only after the separately declared P44 publication
event. The observed repository HEAD was
`684b9ca9f996e409d36230ef03962711fe2754ac`; the P45 authority directory is
untracked as a whole in that repository, so the frozen full-metadata replay,
rather than index state, is the applicable P45 integrity test.

## Acyclic closure

`PAPER_MANIFEST.tsv` has 43 sorted content rows and SHA-256
`2a9aff655b2040c61015b3f25394fa95bbb496d19b7a970854620b190c543893`.
It deliberately excludes exactly itself, `WRITER_REPORT.md`, `HANDOFF.md`, and
`WRITER_SEAL.json`. The closure is acyclic:

1. content files are bound by `PAPER_MANIFEST.tsv`;
2. this report binds the manifest hash;
3. `HANDOFF.md` binds the manifest and report hashes;
4. `WRITER_SEAL.json` binds the manifest, report, and handoff hashes and is
   itself excluded.

No covered file records the eventual seal hash. Generated build directories,
cache bytecode, and an empty log directory were moved to the recoverable
disposable archive `/tmp/p45_generated_archive.WhvgsY`; the retained final log
and bibliography artifacts are manifest-covered under `evidence/`.
