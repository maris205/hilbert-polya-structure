# Paper27 final bounded local build correction

Status: AUTHOR_STOP_PENDING_CONTROL_REVIEW

Script SHA256: `03d845508e3c9c5415b8cab97fb24b7233be28144cb97e6aecbd46a206083d63`.
Tests SHA256: `90328d00ab57a0109f0872ce26efae4c3b635d1f1f77c2703aefec555289d4af`.

This is bounded compilation correction 3/3 under the existing user confirmation and paper-compile workflow, following the preserved actual failures documented in LOCAL_BUILD_20260905_RESULT.md and LOCAL_LAYOUT_BUILD_20260905_RESULT.md. No source changes occur: layout main `9fbc475fa435b66983fe97807e7fdf5544dbd9cc8952e892d0830848b39724a8`, frozen original and auxiliary sources, dependency lock, tools and PDF parser binding are unchanged. The independent layout-equivalence PASS remains applicable.

Exact new namespaces, not touched before independent prebuild review consumption:

- `build/final-20260905-evidence`
- `build/final-20260905-r0`
- `build/final-20260905-r1`

The complete delta from LOCAL_LAYOUT_BUILD_20260905.py is confined to:

1. These fresh paths and the new review/frozen-script basenames.
2. A narrow BibTeX-log predicate: exactly one `warning$ -- 0` counter after exactly one standard statistics heading is required. All trailer lines must be counter rows; no other warning/error/undefined-bearing line is exempt. Nonzero, malformed, duplicate, misplaced or missing counters fail. Publication exit-zero and all bibliography/key/style/database conditions are unchanged.
3. All seven boundary labels remain required, but their positive census moves from the interleaved layout extraction to an additional fixed local read-only `pdftotext -raw -enc UTF-8 ... -` invocation. Page count and References boundary must agree. The seven labels must occur once each, in order inside Section 8 before References; their literal or three exact independently inspected wrapped spellings are accepted, and all are forbidden afterward. Other content, provenance, reference and layout checks remain unchanged. No general dehyphenation or lossy normalization is introduced; the raw output bytes/hash and observed label spellings are retained in evidence/acceptance.

The extra PDFRAW command is an inspection, not a TeX/BibTeX publication pass; its intent/stdout/stderr/status/receipt follows the existing fixed admin environment, timeout and cleanup discipline. Actual raw output and census must agree across roots. All prior exact PDF/source/log/aux/bbl/blg comparisons, recorder-only root normalization, pre/post binding, exclusive writes, no root reuse, no cleanup and no automatic retry remain intact.

All 21 pure regression methods and read-only preflight passed before independent review. The main agent also checks the complete corrected predicates diagnostically against the preserved, finished layout r0 without rerunning publication or altering its failure. Independent code-delta PASS must bind the exact final script before LOCAL_FINAL_BUILD_20260905_REVIEW.md consumes it. Actual output review, warning disposition, visual inspection, lock supplement and final integrity still follow a successful dual build; code PASS is not release PASS.
