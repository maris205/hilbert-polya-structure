# Paper 49 final writer closure

## Status

`HOLD_FOR_INDEPENDENT_WRITER_AUDIT`

This is a writer-owned closure only.  It does not claim installation,
authority acceptance, or an independent final verdict.  The sole active
writer package is `/tmp/paper49_writer_candidate/FINAL_WRITER_OVERLAY`;
material elsewhere in the writer candidate is retained as historical evidence.

## Active manuscript

- Title: *Hausdorff Dimension of Complete Cyclic Markov Hom Tree-Shifts with
  One-Level and Canonical (L)-Level Forced-Chain Transient Feeders*.
- PDF: `main.pdf`.
- PDF SHA-256:
  `aa2a5df28cd7139d9e19aea9bb035cd03f5d787e36260d8a52ed2d33ead930a4`.
- Format: 19 A4 pages, anonymous, 33 embedded fonts with ToUnicode maps.
- Build: fixed `SOURCE_DATE_EPOCH=1787270400`, four pdfLaTeX passes and one
  BibTeX pass, zero warning lines.

No theorem, exposition source, figure data, bibliography, or PDF was changed
during this repair.  The only executable changes isolate replay Python
children from the caller environment and make the writer-seal check use the
same trusted interpreter discipline.  The closure evidence records those
changes and the withdrawal of the superseded writer anchors.

## Protected Stage-A binding

The protected authority tree was captured twice before semantic parsing and
the captures were byte-identical.  The active capture contains 75 regular
files and 21 directories including its root, with no symlink or nonregular
node.  Its Stage-A source is exact to the frozen Stage0 candidate by relative
path, bytes, type, mode, and mtime; its only delta is the canonical State-A
output namespace of 9 files and 4 directories.

The portable relative protected-tree manifest is
`evidence/PROTECTED_STAGEA_TREE.tsv`, SHA-256
`b5f6e48c3e6b61ca0fbf3bdb76153d93930f1b383c005dc102fd71c0724b8e22`.
The replay receipt is `evidence/PROTECTED_STAGEA_REPLAY.json`, SHA-256
`d8d7c57457e567774783deea98a6bac4a87b8d7b787101d7b9b4e48a2fff9715`.
It binds:

- Stage0 static manifest
  `9498faaa791a619345eef6f61c0a677725423d0d04df515931d7e9c3913f5b4a`;
- Stage0 preoutput seal
  `c214342e7a10664f53ff82f5fdf458ca58fb94caf8e479d5c8527062c9b82cb3`;
- Stage0 input lock
  `6dde8bf6106747beba9d905e784e0cb7eefe9a5837a962435f9a2dd6fedfb8b5`;
- installed run summary
  `7d69e6aa9617869a4e80a83bfa5dc2168d9461641c739e2de28a6cbdf0a5bbe7`;
  and
- production/independent science bytes
  `c3512ccc3f609c5c6f97fa55999270eee19db433d15aca8deefa285e7fcf60c1`.

The protected authority, Stage0 source candidate, Git tree, README, and mirror
were read only throughout this closure.

## Independent evidence bound, not adopted as a writer verdict

`evidence/INDEPENDENT_AUDIT_ANCHORS.json`, SHA-256
`ab70bd5d8c2eca1d2a5f0c941bf201ee5fb2535fc13dd04853f6e2a53ed94b6c`,
binds two external audit records:

- the independent authority post-output result
  `9f4a9d308e71671be29240f1864fb640ceb6e67b8b72e6b185d72748b005b671`,
  whose exact verdict is `P49 INDEPENDENT POST-OUTPUT CLEAN`; and
- the fresh independent writer re-audit manifest
  `3c883d01ad29874b91c70393b43b60661ea5bbe2bbf0040187d1e7cc61aa9041`,
  whose exact verdict is `WRITER PRE-INSTALL CLEAN`.

These strings are quoted provenance.  The active writer status remains the
hold stated above.

## Withdrawn closure and repaired replay blocker

The immediately preceding writer closure is explicitly withdrawn in
`evidence/WITHDRAWN_WRITER_ANCHORS.json`, SHA-256
`a25130862caf2484c52f29f61d0b4f4b649bc182f6facb1821ea7ea8e3498aca`.
It binds the old manifest
`aeaf00dce2d44dca5748e5f284760993916e241cdbadc18ee66fb7d4b3e78423`,
old report
`78388a8ea6b4de098772a0533ffc68d716faa491ea0a5a32057f5f6fdf189871`,
old handoff
`ae966ee87c48aa0bd1a1538de124e9adb8d4ac0a073bcfd0922f92bf56514a83`,
and old writer seal
`e3d6e6def706438494b2f8f1fc4d6a567b23d492a5e8f3efe39d97fd6ccdbed6`.
The subsequent independent audit returned the quoted verdict
`P49 WRITER HOLD` because Python children inherited a hostile caller
`PYTHONPATH`.

All Python children in `tools/replay_overlay.py` now use the resolved trusted
`sys.executable` with `-I -B`; every child receives a newly constructed,
lane-local environment with independent HOME, TMP, and cache roots, and with
`PYTHONPATH` and `PYTHONHOME` explicitly absent.  The Bash build entry point is
absolute.  `tools/build_writer_seal.py` applies the same interpreter and
environment discipline to its manifest check.

The former overlay `STATUS.txt`, SHA-256
`e6f537351cfe6d3226d3616cb722f99237bbdd6e146b84acdb409319db04a4b1`,
was removed rather than renamed because it was the sole path collision with a
different protected Stage-A file.  The active status exists only in this
report, `HANDOFF.md`, and `WRITER_SEAL.json`; the overlay therefore contains
no divergent protected-path collision.

## Portable replay and PDF QA

Two fresh overlay clones independently regenerated all figure data, each
passed 153 arithmetic assertions, and each produced the same bibliography,
normalized compile log, build receipt, and active PDF bytes.  The independent
replay receipt is `evidence/INDEPENDENT_REPLAY.json`, SHA-256
`9408e1125e41f6d7fbd4c3bebe582c238c34ea215e3ef262f9ef8464651e546c`.
Its bundled immutable input is `inputs/level_l.json`, SHA-256
`cf8ae3ee10fd798d937bed725b6a55ad0635e5dcdfdb29fb0c1070f2290a63f9`.

The path-neutral PDF hard-gate receipt is `evidence/PDF_QA.json`, SHA-256
`c29e590845092312b0c05c6593bee8646822bf7ff952aa0c8ccfcd933c5dca51`.
Both fresh PDFs passed all six text extractors with zero illegal C0, DEL, C1,
U+FFFD, or PUA code points; raw bbox and bbox-layout streams parsed as strict,
unsanitized XML; all 7,968 words were in bounds; all 19 pages were A4; and no
Type 3, unembedded, or missing-ToUnicode font remained.  The historical visual
inspection covering all 19 pages is bound in `evidence/VISUAL_QA.md`.

The repaired runner was also replayed from a hostile caller that supplied
shadow `json` and `hashlib` modules, `sitecustomize.py`, a bogus
`PYTHONHOME`, fake `python3` and `bash` executables, and a failing `BASH_ENV`.
No hostile marker was loaded.  Normal and hostile runs returned the same
success sentinel and reproduced byte-identical PDF, BBL, build receipt, and
all five frozen replay-evidence files in both lanes.  The canonical regression
receipt is `evidence/REPLAY_ISOLATION_REGRESSION.json`, SHA-256
`5f37918ef21f7f4db6e5403717a374c2095bef3f782e8a0f84f466129ea85f01`.

## Package closure

`PAPER_MANIFEST.tsv`, SHA-256
`7339a573f0312b99689d2b92d313811c30523911e20875863e6e27b524022ab5`,
is self-excluding and contains 67 entries: the root, 8 descendant directories,
and 58 regular content/evidence files.  It excludes exactly itself,
`WRITER_REPORT.md`, `HANDOFF.md`, and `WRITER_SEAL.json`, which form the acyclic
closure tail.  All directories are mode 0755 and all regular files are mode
0644; there are no symlinks, nonregular nodes, caches, or unapproved auxiliary
build files.

Dependency order is content/evidence, manifest, report, handoff, then raw
writer seal.  A fresh independent writer audit is still required before any
next-stage use.
