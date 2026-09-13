# Paper28 EC successor: independent failure-recording audit

Date: 2026-09-05.
Recording decision: `FAILURE_RECORDING_INTEGRITY_PASS`.
Build decision remains `BUILD_FAILED_PRESERVED_NO_RETRY`.

Audited execution root: `build-capsule-ec-20260905` only.
Failure file: `evidence/failure.json`, 32589 bytes, SHA-256
`f0cbab3c24f680994fbb47efe5b12be14f6c3870f3937ef31818543ac1bf77f7`.

## Recording checks

- Independently traversed the actual evidence directory without following
  symlinks and checked exact membership, types, modes, ownership, file byte
  counts and SHA-256 values against `failure.json`'s `sealed_evidence`.
  All 126 rows match: 10 directories and 116 regular files containing
  11758204 bytes. The sole exclusion is `failure.json` itself, consistently
  absent from its prior-evidence seal; its independently supplied hash matches.
- The actual final `r0/work` tree exactly matches the sealed
  `r0-09-validator/work-manifest.json`: 46 rows and 3864677 regular-file bytes.
  This includes the acceptance report and retained page/report artifacts;
  integrity checking is not visual approval.
- Copied controls match the opening contract. The copied independent review
  matches opening `review_sha256`, namely
  `553feaa07a5479ec47b62bec31041334dc6bf2c6810d8533410282fc5da13fc5`.
- Actual manuscript originals and their isolated `/source` copies match the
  opening and failure source bindings, including byte lengths, SHA-256 and LF.
  The failure's supplemental rebind equals the opening object. The current
  recorded supplement outcome, audit and six sealed outputs match that object;
  the isolated EC metric also matches its 3584-byte/hash/LF identity.
- The sealed pre-execution and failure readonly-input manifests are equal as
  parsed records, with 6908 rows, agreeing with `r0_readonly_unchanged: true`.
  The EC entry records root ownership and readonly mode0444. This audit checks
  these recorded manifests and independently rechecks the source/EC files;
  it does not claim a second complete scan of every captured runtime resource.

## Actual execution and failure

Stages `01-latex` through `08-pdftext` each record exit0; `09-validator` records
exit1. All nine children were spawned and reaped, with no timeout, exception or
cleanup error. Their intents retain the opening source/environment/limit
bindings. The third/fourth stages' aux/out/bbl identities agree. The final-log
record has no fatal LaTeX/BibTeX entries and preserves seven underfull lines
for later visual disposition. The final LaTeX log records 22 pages and 751019
PDF bytes; its normal rerunfilecheck message says the output file is unchanged.

The actual PDF SHA-256 is
`a6778a8ead3004a9b14784d02e1c98c9a59d5a837231ece670da03dff0c8bf63`.
The actual `r0/work/report/acceptance.json` has 92407 bytes and SHA-256
`a59a59bb64a355f039d516562742140b21c2a9de7a8ee997e0e425dc6da94517`;
both match their retained records. Validator stdout agrees with this report,
and its stderr is empty.

The report remains `automated_status: FAIL`, with 166 recorded findings:
163 `invalid_internal_link`, one `unsafe_pdf_key`, one
`pdf_single_terminal_eof`, and one `content_page_gate_22_30`. It records 22
total pages, 20 content pages, and References beginning on physical page21.
These are preserved validator observations, not independently reclassified
defects in this recording audit.

The failure stage is exactly `r0/09-validator`; `completed_roots` is empty,
and an exact read-only check confirms that `r1` does not exist. There is no
two-root success or final local acceptance. No missing-dependency conclusion
or additional recapture need follows from this validator-stage failure.

## Scope and next authority boundary

Only this new audit document was written. The reviewer did not execute a
controller, capture, build, retry or PDF parser; alter source, validator or
acceptance requirements; inspect another build/failure root or live-host
font; reopen mathematical review; or make any external write.

PASS concerns faithful recording of the failed execution only. Diagnosis of
validator semantics, and any proposed new source/validator revision requiring
user approval, are separate from this audit. The preserved failure must not
be relabeled a build PASS or used to authorize an automatic repair/retry.
