# Final QA report — P162–P166

**Audit record:** 2026-09-03.  **Scope:** exactly the five final Round-2
packages, with prior round PDFs checked for preservation.  **Decision:**
`PASS_INTERNAL / HOLD_EXTERNAL`.

## Exact author-verifier replay

Each paper-local verifier was run afresh from the final workspace with Python
bytecode disabled.  Every stdout stream matched its retained canonical file
byte for byte.

| paper | verifier | assertions | canonical transcript SHA-256 | batch replay |
|---:|---|---:|---|---|
| P162 | `code/verify.py` | 1,712,974 | `c31ec0a098bab52241eb2765bd6fef0669fdacdb4486ca69bea9dfc56fbab62b` | exact match / PASS |
| P163 | `code/verify.py` | 1,430,898 | `21d2dc8e66580e7b78ef9c4bd2bda3eaa393757ee466497a62defb0f15700434` | exact match / PASS |
| P164 | `code/verify.py` | 1,154,387 | `dddbb6ba053c908fb60321b717867da925bdd2c9af3d723f93175367a180997f` | exact match / PASS |
| P165 | `code/verify.py` | 605,733 | `0fc0aac73b62b039fb9e82918a141927b33fb2aecb8b1f28ae3940c1481590bd` | exact match / PASS |
| P166 | `code/verify.py` | 17,017,929 | `7ef213d9334acc39c835f9c9da4b52f4581b423e76de82406d65ece73c55cc06` | exact match / PASS |

Total: **21,921,921 exact author assertions** and five of five canonical
transcript matches.  The larger reviewer-owned lanes are kept separate.

## Ten deterministic source-only builds

Two fresh directories per paper were populated with only `main.tex` and
`references.bib`.  Each completed the declared
`pdflatex / bibtex / pdflatex / pdflatex` sequence with halt-on-error.  Every
cold pair matched internally and every output matched its live `main.pdf`
byte for byte.

| paper | pages | bytes | final PDF SHA-256 | font rows | isolated builds |
|---:|---:|---:|---|---:|---|
| P162 | 4 | 399,828 | `730c4a57cb1c3f787c0cc8b142d4dbf62da4d2b06bc1c42d5c30d00eb8e20b62` | 30 | 2/2 exact |
| P163 | 5 | 424,998 | `899e7c6b24f3a6e99041d05410db75c1de152f4d98b2e90d10e4619927b216bf` | 32 | 2/2 exact |
| P164 | 4 | 301,337 | `b1fb98834db37564a50869c1fd637ceb78a5565104fb1dbb096dbd9a6b9c2f26` | 23 | 2/2 exact |
| P165 | 4 | 288,837 | `f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a` | 23 | 2/2 exact |
| P166 | 4 | 294,007 | `f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c` | 24 | 2/2 exact |

Total: **10/10 source-only builds**, **21 A4 pages**, **1,709,007 bytes**,
and **132/132 font rows** embedded, subsetted, and Unicode mapped.  Scans of
all ten settled logs and ten BibTeX outputs found zero genuine warning,
error, undefined citation/reference, rerun request, overfull or underfull
box, or bad box.

## Preserved PDF rounds

| paper | Round 0 SHA-256 | Round 1 SHA-256 | Round 2/current SHA-256 |
|---:|---|---|---|
| P162 | `e496ce1be3084e61616494cab2ca405238adfa575a6484db93029f8dae01de46` | `730c4a57cb1c3f787c0cc8b142d4dbf62da4d2b06bc1c42d5c30d00eb8e20b62` | `730c4a57cb1c3f787c0cc8b142d4dbf62da4d2b06bc1c42d5c30d00eb8e20b62` |
| P163 | `899e7c6b24f3a6e99041d05410db75c1de152f4d98b2e90d10e4619927b216bf` | `899e7c6b24f3a6e99041d05410db75c1de152f4d98b2e90d10e4619927b216bf` | `899e7c6b24f3a6e99041d05410db75c1de152f4d98b2e90d10e4619927b216bf` |
| P164 | `db26e57e610577cdff03c348fa3ce794165e3268393350d7d2f55b14e98070ae` | `b1fb98834db37564a50869c1fd637ceb78a5565104fb1dbb096dbd9a6b9c2f26` | `b1fb98834db37564a50869c1fd637ceb78a5565104fb1dbb096dbd9a6b9c2f26` |
| P165 | `f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a` | `f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a` | `f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a` |
| P166 | `f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c` | `f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c` | `f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c` |

For all five papers, `main.pdf` and `main_round2.pdf` are byte-identical.
P162's Round-0 to Round-1 change is the closed abstract qualifier.  P164's
change consists of the two closed proof expansions.  P163, P165, and P166
are no-change freezes across every round.

## PDF, visual, anonymity, and lifecycle QA

All 21 final pages were rasterized at 144 dpi and inspected.  No clipping,
overlap, missing glyph, malformed display, illegible formula/table/reference,
margin excursion, or page-boundary defect was found.  Batch checks also
confirmed:

- A4 media boxes of `595.276 x 841.89 pt` for all five PDFs;
- blank identifying title, author, subject, and keyword metadata fields;
- no encryption, interactive form, or JavaScript;
- exactly one `\\author{Anonymous}` declaration in every source and an
  anonymous visible byline;
- no email, affiliation, ORCID, personal acknowledgement, username, or
  workspace path; P162 and P163 contain only a neutral no-external-funding
  declaration with no identifying attribution;
- at least one visibly extractable `HOLD_EXTERNAL` token in every PDF; and
- all cited references visibly rendered with no unresolved citation marker.

## Review closure

| review | Critical | Major | Minor | assertions | closure |
|---|---:|---:|---:|---:|---|
| Hostile Review A, aggregate | 0 | 0 | 3 | 16,331,340 | P162 one and P164 two local findings closed in Round 1 |
| Hostile Review B, aggregate | 0 | 0 | 0 | 26,261,154 | five accepts; no Round-2 change requested |

No paper has an unresolved review finding.  The reviewer counts remain
separate from the 21,921,921 author assertions and do not inflate the
paper-local verification total.

## Integrity notes and manifest closure

Final closure found one artifact-provenance defect rather than a manuscript
defect: P162's two retained cold-log filenames described an earlier byte
count.  Two independent final-source builds reproduced the current PDF hash,
and the logs were mechanically replaced.  Lifecycle headers in several
supporting documents were also normalized to Round 2.  Neither operation
changed a theorem source, bibliography, verifier, canonical transcript, or
PDF.

Three historical `PINNED_INPUTS.sha256` files contain expected mismatches at
mutable live paths after normal Round advancement.  They remain unchanged as
review-time receipts.  The exact affected paths and the immutable inputs that
still validate are listed in `HISTORICAL_PIN_VALIDATION_NOTE.md`; no final QA
claim treats those historical pin files as current-tree manifests.

The five final paper-local `SHA256SUMS` files contain **32, 28, 28, 32, and
34** non-self entries and pass **154/154**.  The batch
`CANONICAL_PDF_MANIFEST.sha256` covers exactly P162–P166 and passes **5/5**.

## Release boundary

Final QA establishes internal theorem-package and artifact integrity only.
It does not establish novelty, priority, ownership completeness, freedom to
operate, or external readiness.  No upload, posting, circulation, contact,
or submission is authorized.  All five manuscripts remain anonymous
internal accepts under `HOLD_EXTERNAL`.
