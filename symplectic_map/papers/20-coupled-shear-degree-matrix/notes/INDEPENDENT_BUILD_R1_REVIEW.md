# Paper20 — Independent Build R1 Review

Date: 2026-08-22 UTC

Role: independent build-receipt auditor; read-only over the frozen source and
the one parent-authorized deterministic build. No TeX command, rebuild, source
edit, or downstream publication action was performed by this reviewer.

## Receipt and source binding

`paper/BUILD_RECEIPT_R0.json` is strict canonical UTF-8 JSON (one LF, no BOM,
CR, NUL, duplicate keys, or nonfinite values), 4,259 bytes, SHA-256
`3e7da7d9b66c02f68864d04c177ff12317e52d87b3c38c7fc8748f95ca9e4d62`.
Its six source bindings were independently read and rehashed; every declared
byte count, LF count, and digest matches:

* `main.tex`: 37,423 bytes / 981 LF / SHA
  `2a27dc745bffa7c9efb2016edb416045216d9fcd8bad7beadf9143716eee2014`;
* `math_commands.tex`: 702 / 20 / SHA
  `37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582`;
* `references.bib`: 2,335 / 73 / SHA
  `529612c446e0a56919efb79dae7f80358f4f3fa1fc3424e6e15f7da2886c5eaf`;
* `PAPER_PLAN.md`: 22,064 / 397 / SHA
  `4dfcf82f8dae85502fced2f7b1d73d80e35ee242eee609dd74b5f59ca793adf3`;
* `BUILD_METADATA_R0.json`: 3,588 / 1 / SHA
  `75e94cc9da7dd738fd287db32994fb98863d65c00350201ac6c77e48d017cc9c`;
* `experiments/source_lock.json`: 11,847 / 1 / SHA
  `57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581`.

Receipt commands exactly equal the declared four-command template
(`pdflatex`, `bibtex`, `pdflatex`, `pdflatex`) and use the recorded deterministic
environment (`SOURCE_DATE_EPOCH=1787356800`, `FORCE_SOURCE_DATE=1`,
`LANG=C`, `LC_ALL=C`, `TZ=UTC`, no network). The epoch agrees with the PDF's
reported 2026-08-22 08:00 CST creation time. The source-lock and build-metadata
JSON objects also pass strict canonical round-trip checks. The parent supplied
the one-shot build authorization for this audit; the immutable pre-build lock
still records its historical `build_authorized:false` state, so any later
build/publication must bind an explicit authorization transition rather than
infer one from the receipt alone.

## Output readback and PDF checks

All six output rows in the receipt match the files on disk byte-for-byte,
including regular-file mode 0644. In particular, `main.pdf` is 380,574 bytes
with SHA-256
`ed58824860f77186210fee298b1631e7877868dc828b4b3a9cd048fcaa1545e9`.
`pdfinfo` reports 14 pages, Letter size, PDF 1.5, unencrypted, no JavaScript;
Ghostscript's null-page parser exits 0. `pdffonts` reports 24 rows and every
font is embedded and subsetted. The seven citation keys in `main.tex` equal the
seven BibTeX, `.bbl`, and `.aux` keys; independent label/reference checks have
no missing or extra labels, and the receipt's undefined-reference and
undefined-citation counts are both zero. Marker scans for `??`, `[?]`, `TODO`,
`TBD`, and `VERIFY` are empty. BibTeX reports zero warnings and the log has no
fatal, overfull, or emergency errors.

The extracted PDF confirms the receipt's split: the conclusion starts and ends
on page 14, and References begins later on that same page. Thus page 14 is not
a full substantive page; the substantive body through the conclusion occupies
strictly less than 14 full pages.

## Blocking plan mismatch

The frozen `PAPER_PLAN.md` (and `BUILD_METADATA_R0.json`) requires 24.0
substantive pages, with an authorized range of 22–26, measured through the
conclusion and excluding references. The built artifact has only 14 numbered
pages through the conclusion, with references already sharing page 14. It is
therefore at least eight pages below the hard minimum and cannot be treated as
a realization of the locked plan. This is a release/build-handoff blocker,
not a TeX parsing failure. Before any publication or further downstream
artifact, either expand the manuscript and rebuild or obtain an explicitly
authorized, hash-bound plan/metadata revision that changes the page gate.

## Nonblocking residual warnings

The receipt truthfully records three underfull boxes (the related-work table),
four hyperref PDF-string warnings (math tokens in bookmarks), and one final
`Label(s) may have changed` warning. The first two are cosmetic. The label
warning means final cross-reference stability is not independently certified;
if a strict zero-warning handoff is required, perform one separately authorized
stabilization pass and replace the receipt/output identities. No such pass was
performed here.

BUILD_R1_BLOCK
