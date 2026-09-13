# Paper28 successor validator: directed regression report

Date: 2026-09-05. Directed-test status: **103/103 PASS**, command exit0.
This is predicate regression evidence, not PDF/build or local acceptance.

## Exact tested files

- `PDF_ACCEPTANCE_SUCCESSOR_20260905.py`: 50632 bytes, SHA-256
  `af6125f5c7499e437f9e56aa54197bcadd3402e3a33d4607a9a1319a3e72f464`.
- `PDF_ACCEPTANCE_SUCCESSOR_TESTS_20260905.py`: 20509 bytes, SHA-256
  `20ed9a29da6eca1151acfcb4680cf4b2e33df70424516150ab6c9606d454cb7b`.
- Frozen predecessor remains SHA-256
  `e173a8a54d051f8d296b5d1319a44bdea0f30d3ab0be91cc16747027bf9a126c`.
- Successor `main.tex` is bound to SHA-256
  `7beb4f783cd370dc4b0d9d1e9178e3e48ce1ef9ed1497e0e9883b10739d4a1f9`.
  The other two source hashes, title, terminal sentence, 8+32 headings and
  exact bookmark correspondence remain unchanged. The content gate is still
  **22 through 30 pages inclusive**, excluding References.

Command:

```text
/root/miniconda3/bin/python3.12 -I -S -B notes/PDF_ACCEPTANCE_SUCCESSOR_TESTS_20260905.py --recorded-fixtures
```

Full stdout results, individual case names and fixture hashes are preserved in
`PDF_ACCEPTANCE_SUCCESSOR_TEST_REPORT_20260905.json`.

## Narrow implementation delta and evidence

1. `internal_link_page` admits kind4 only with an explicit nonempty `nameddest`,
   successful `Document.resolve_names()` entry, in-range integer page and exact
   agreement with the link's own page. It does not convert URI, Launch, remote
   GoTo or PDF Named actions. Missing, malformed, mismatched and out-of-range
   targets fail. All 163 actual recorded named links pass the corrected helper.
   This follows the [official named-link kinds](https://pymupdf.readthedocs.io/en/latest/vars.html#link-destination-kinds)
   and [destination-resolution interface](https://pymupdf.readthedocs.io/en/latest/document.html#Document.resolve_names).
2. `catalog_open_action` admits only a resolved, unchained local GoTo with an
   explicit actual page reference and a valid finite-parameter view. The
   exception applies only to the verified catalog's own OpenAction key;
   OpenAction remains in the global unsafe-key set. URI (even allowlisted),
   JavaScript, Launch, remote actions, Next chains, non-page references and
   malformed views fail. Recorded xref161 targeting page xref162 with `/Fit`
   passes. Adobe documents [catalog GoTo startup views](https://opensource.adobe.com/dc-acrobat-sdk-docs/library/pdfmark/pdfmark_Examples.html)
   and their [view parameters](https://opensource.adobe.com/dc-acrobat-sdk-docs/library/pdfmark/pdfmark_Actions.html).
3. `pdf_physical_structure` checks the existing producer's single classic-xref,
   direct-stream-length format, not a general PDF service. It binds startxref
   to the complete xref/trailer, matches raw and MuPDF trailers, and covers the
   physical body by indexed object spans. Stream bytes are opaque by exact
   Length; object gaps accept only declared whitespace. Trailer Prev/XRefStm,
   appended documents or self-contained appended xref without Prev, unindexed
   objects, wrong offsets/identities/lengths, and trailing data are rejected.
   The actual 21 CMap EOF markers remain stream data; its physical terminal
   structure passes. The prefix interface preserves the old complete-object
   grammar and never swallows a trailing comment on behalf of the envelope.

An initial 103-case run exposed two variants of one boundary condition:
Length+1 could consume the producer's separate stream-ending newline. The
implementation now explicitly requires the independent LF/CRLF delimiter
after exactly Length bytes, matching all 62 actual streams; the same final
103 cases pass. The failure was corrected in code, not removed from tests.

## Preserved boundaries

Unchanged-function/constant AST checks and the predecessor's memory-only
self-tests pass. Existing metadata, anonymity, provenance, unsafe-action,
source/bibliography, geometry, font, heading, rendering and content-boundary
checks remain; the new source hash and the three described checks are the
only intentional behavioral changes. The old report's genuine 20-content-page
failure is explicitly retained as a negative regression.

Tests read exact preserved PDF/report fixtures but never call either old or
new validator `run`, import PyMuPDF/fitz, render pages, build, capture, install,
retry, or modify a PDF/source/old root. The test process performs zero file
writes; these report files were saved separately after it finished. The new
validator still requires its independently reviewed captured execution profile
and actual new build evidence. No acceptance is granted here.
