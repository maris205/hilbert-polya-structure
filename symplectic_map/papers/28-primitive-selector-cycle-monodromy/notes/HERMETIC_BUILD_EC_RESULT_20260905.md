# Paper28 EC successor: actual build and acceptance failure

Date: 2026-09-05. The once-only controller execution ended exit1 at
`r0/09-validator` (session83081, now ended). It is not to be polled or rerun.
Only `build-capsule-ec-20260905/r0` was materialized; r1 was not reached.

## Actual progress

The captured EC metric resolved the first-pass fontenc failure. All four fixed
LaTeX/BibTeX passes and pdfinfo/pdfmeta/pdffonts/pdftotext exited0. All nine
children, including the validator, were spawned and reaped without timeout.
The final log gate had no fatal LaTeX/BibTeX findings; seven underfull hbox
lines at source line258 remain for future visual disposition. Auxiliary
convergence passed before the inspection steps.

The actual preview PDF is `build-capsule-ec-20260905/r0/work/main.pdf`,
751019 bytes, SHA-256
`a6778a8ead3004a9b14784d02e1c98c9a59d5a837231ece670da03dff0c8bf63`.
It has 22 physical letter-size pages, anonymous metadata, empty creator and
producer, no JavaScript reported by pdfinfo, and no encryption. It has not
received local acceptance or two-root deterministic verification.

The validator exited1 and rendered all22 page images before returning. Its
acceptance report SHA-256 is
`a59a59bb64a355f039d516562742140b21c2a9de7a8ee997e0e425dc6da94517`
(92407 bytes). The terminal content marker is on page20, with References
starting on the fresh page21 and continuing through22. Main-agent inspection
of page-020.png confirms the end-of-content location; this was not a full
visual review of all pages.

## Findings distinguished by cause

There are166 findings in four classes:

| Finding | Count | Read-only diagnosis |
| --- | ---: | --- |
| `content_page_gate_22_30` | 1 | Real locked-delivery mismatch:20 content pages, below22. |
| `invalid_internal_link` | 163 | The validator accepts only LINK_GOTO(kind1); all flagged links are named destinations(kind4), with matching recorded destination names/pages in range. |
| `unsafe_pdf_key` / OpenAction | 1 | Catalog xref701 points to xref161, whose action is an in-document GoTo with destination `[162 0 R /Fit]`; the code rejects the key unconditionally. |
| `pdf_single_terminal_eof` | 1 | The code globally counts raw `%%EOF` bytes. This PDF contains21 such markers inside embedded CMap streams plus its one terminal PDF marker. |

The last three classes identify overly broad validation predicates rather than
evidence of broken links, executable startup content or22 separate PDF endings.
They do not cancel the genuine content-page failure. PyMuPDF's
[official link-kind reference](https://pymupdf.readthedocs.io/en/latest/vars.html#link-destination-kinds)
defines kind4 as a named location; its
[link reference](https://pymupdf.readthedocs.io/en/latest/link.html)
also describes internal named destinations. This diagnosis uses actual recorded
objects/destinations plus the frozen validator's source, not a modified test
or a new parser execution on the failed PDF.

## Preserved identities and next scope

The controller reports the readonly input namespace unchanged; the before and
failure input manifests are byte-identical. The manuscript trio and EC
supplement also passed failure-time rebind. Failure.json is32589 bytes,
SHA-256 `f0cbab3c24f680994fbb47efe5b12be14f6c3870f3937ef31818543ac1bf77f7`.
The exact consumed review SHA-256 was
`553feaa07a5479ec47b62bec31041334dc6bf2c6810d8533410282fc5da13fc5`.
All frozen controls, captures, original sources and this failed root remain
unchanged. Independent recording audit completed with
`FAILURE_RECORDING_INTEGRITY_PASS` in
`HERMETIC_BUILD_EC_FAILURE_AUDIT_20260905.md`, SHA-256
`cd5cf6e6e84e3998f3633769a66e358b421241569a80a9cfefe9ba761a5979ef`.
It verified126 sealed evidence rows and the46-row final work snapshot; it
does not change the actual build/PDF acceptance failure.

The confirmed single-metric recovery has now been consumed. Further work needs
a new source/validator successor scope: add substantive exposition/proofs to
meet the existing22–30 content-page requirement, correct the three demonstrated
validator predicates while retaining real safety checks, independently review
the changes and build in fresh roots. Do not pad pages by typography, lower
the existing requirement, alter this failed PDF, repair/rerun its root, or
silently rewrite the frozen validator. No such new implementation has run.

Paper27 remains the sole accepted paper in Batch07 (1/5); Papers29–31 remain
pending. No submission, upload, hosting, push or external message occurred.
