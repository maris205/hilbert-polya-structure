# Local build acceptance-code prebuild review

Reviewed SHA256: 9638c09a43e0c2dc32d6f8b2792be17fc5a8859ac6e59c6e8d7d22b69222b76c
Decision: FAIL

Date: 2026-09-05 (UTC)
Scope: independent bounded static/code acceptance review of the 611-line
`LOCAL_BUILD_20260905.py`, its local plan, and
`BUILD_PROFILE_RECOVERY.md` Sections 5–9. This is not an artifact, mathematics,
or publication-release review. The approved replacement of the Host/Runner
control chain, single-writer assumption, and additional local read-only
PyMuPDF/pdffonts inspections are accepted premises.

No build/evidence pathname was opened, listed, or statted. No publication
command, old runner, `--build`, network operation, or PDF write was performed.
Tests loaded the new module with Python `-I -B` and used in-memory strings;
the existing self-test reported 2 positive and 11 negative cases passing.
The fixed source's title/structure and the bound pdfTeX executable's printable
header string were also inspected read-only.

## Findings

1. **Blocking false FAIL: the mandatory normal pdfTeX header is rejected.**
   Lines 335–337 reject any case-insensitive `error` substring. The fixed
   publication argv includes `-file-line-error`, whose normal diagnostic-mode
   header is `file:line:error style messages enabled.` (the executable contains
   this string with a leading space). Passing that line plus an otherwise
   accepted synthetic final log to `log_check` produces
   `FINAL_LOG:1:file:line:error style messages enabled.`. Thus a healthy final
   TeX log is rejected. Permit only this exact known administrative line
   (including the tool's expected leading-space spelling), preserve rejection
   of genuine errors, and add positive/negative regression tests. The broad
   inherited profile predicate must be interpreted as actual error evidence,
   not a request to reject the explicitly required diagnostic mode itself.

2. **False-FAIL risk confirmed at the recorder predicate: valid dot-relative
   root-local spellings are rejected.** Lines 308–310 accept `main.aux` or the
   exact absolute root prefix plus `main.aux`, but reject `./main.aux` (and
   similarly `./math_commands.tex`). An in-memory phase-3 recorder naming
   `INPUT ./main.aux` fails with `FLS_LOCAL:./main.aux`, although it denotes
   exactly the allowed root-local file. TeX/Kpathsea recorder spellings can be
   dot-relative; no actual recorder was accessed in this review, so this is
   not a claim about an observed new-build recorder. Accept a single `./`
   prefix for validation of the fixed allowlist only. Continue rejecting
   `..`, arbitrary paths, aliases, and undeclared products. Preserve original
   recorder bytes in snapshots and cross-root comparison: this validation
   spelling accommodation must not add a second comparison normalization.

3. **Non-release acceptance gap: proof text after References is not rejected
   by the automated text predicate.** Lines 374–381 establish that anchors
   occur before the sentinel, while lines 383–385 check only numeric reference
   labels in the suffix. A synthetic 26-page text with all required anchors in
   the first 24 pages, References and labels 1–20 on page 25, and a repeated
   `1 Introduction` heading plus explicit proof prose on page 26 passes
   `text_check` (SHA256
   `78b0901a9d36a5f71355497bcb566ddb91ae0c48b3e64df84cc6f9d1e1fc1c4a`).
   Section 7 requires no proof content after the sentinel. This isolated
   predicate test does not demonstrate a whole-pipeline false PASS against
   the frozen source/PDF, and the plan correctly retains an independent
   output review. Nevertheless, add a conservative check for repeated known
   section/content anchors after References and explicitly retain suffix
   inspection in that mandatory review. Do not treat the automated
   `OUTPUT_CHECKS_PASS` status as complete proof/reference-placement acceptance.

## Checks that align with the retained contract

- Lines 44–55 and 478–495 preserve the four fixed publication commands and
  their order, three time-indexed log/aux/fls snapshots, BibTeX bbl/blg
  snapshots, and five root manifests. There is no fifth pass or retry.
- Lines 195–225, 479–483, and 509 rebind live sources, installed source copies,
  fixed executable/link chains, and the 87-logical/86-final dependency lock.
- Lines 273–293 enforce the root product universe, source/product modes,
  link-one regular files, and empty five-cache directories. Line 485 enforces
  BibTeX recorder-byte preservation.
- Lines 326–360 implement the 24–28 proof-page sentinel bound, final PDF size
  and page checks, twenty-way source/bib/aux/bbl citation census, and strict
  BibTeX diagnostics. Residual warnings are retained, not silently waived;
  their semantic disposition remains explicitly pending independent review.
- Lines 392–464 cover PDF framing, fixed metadata/epoch, portrait geometry,
  embedded non-Type3 fonts, parser repair/warning rejection, forbidden object
  tokens, non-font-stream provenance, and extracted-text geometry. These
  read-only auxiliary checks are an intentional permitted addition, not an
  unauthorized PDF rewrite or extra publication pass.
- Lines 514–539 compare required source/PDF/auxiliary bytes exactly, compare
  recorder snapshots using only the corresponding absolute-root replacement,
  and project only the recorder-bound `main.fls` SHA field in each manifest.
  The R024/R033/R044/R054 recorder mapping is correct; metadata, font census,
  warnings, sentinel/pages, and extracted-text hash are compared through the
  complete result object. No extra content normalization was found.

This decision applies only to the exact reviewed SHA above. A corrected script
needs a new hash-bound review decision before the independent prebuild gate can
open; this FAIL does not authorize or imply a build attempt.
