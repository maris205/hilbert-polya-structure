# Final bounded local build: independent control-delta review

Reviewed SHA256: 03d845508e3c9c5415b8cab97fb24b7233be28144cb97e6aecbd46a206083d63
Decision: PASS

Date: 2026-09-05 (UTC)
Scope: bounded independent review of the complete code/test delta from the
previous layout-control script, SHA256
`a38c05bb7d33e3800ea4ea2aff8d5836a135e5c1ebdfd0d7749c3cd140dad9d5`,
and `LOCAL_FINAL_BUILD_20260905_PLAN.md`. This is correction 3/3 as scoped by
that plan, not an old-root retry, final artifact review, source-equivalence
re-review, or assertion of actual successful output. Prior failure and
diagnostic observations were supplied as context; this reviewer did not read
their build/evidence paths or independently certify those observations.

## Code delta and disposition

1. **Fresh identities are explicit.** Lines 21–22 select only
   `build/final-20260905-evidence`, `build/final-20260905-r0`, and
   `build/final-20260905-r1`. The new gate and frozen-script basenames are
   consistent with the new script. There is no old-root reuse, alternate suffix,
   cleanup, or overwrite. Layout main remains bound to
   `9fbc475fa435b66983fe97807e7fdf5544dbd9cc8952e892d0830848b39724a8`;
   source selection, preserved-original-main check, auxiliary sources, and all
   dependency/tool/parser bindings are unchanged.

2. **BibTeX exception is restricted to the standard zero statistic.** Lines
   413–426 require exactly one standard statistics heading and exactly one
   literal `warning$ -- 0` after it. Every subsequent line must have the counter
   row grammar. Only that exact zero-counter line is exempt from the existing
   warning/error/undefined test; all other lines remain subject to it. Missing,
   duplicate, misplaced, nonzero, malformed, or decorated counters fail.
   Citation/style/database checks and publication exit-zero requirements remain
   unchanged. Treating this zero-count built-in statistic as non-diagnostic
   fixes an error in classification rather than waiving a real warning.

3. **Seven boundary requirements are relocated, not removed.** The positive
   boundary census moves from spatial `-layout` text to the separately captured
   content-order `-raw` text. Lines 436–464 require the expected page count,
   the same unique References page, a unique Section 8 heading before that
   page, and exactly one occurrence of each of the seven labels in their
   prescribed order inside that section. Labels after References fail.
   Acceptance permits the literal labels and only these three fixed aliases:
   `Positive coor- dinates`, `Literal re- flected label`, and
   `Positive- support can- cellation control`. There is no general
   dehyphenation, arbitrary cell-text omission, or relaxed label set.
   The alias spellings are explicitly listed in the plan/code; their reported
   occurrence in prior actual output was not inspected by this reviewer.

4. **PDFRAW is a bounded read-only inspection.** Line 629 runs the already-bound
   `/usr/bin/pdftotext` with fixed `-raw -enc UTF-8 <root>/main.pdf -` argv through
   existing admin-environment, capture, timeout, cleanup, exit-zero, and empty-
   stderr checks. It is not another publication command or a PDF write.
   Its complete stdout is preserved by the normal receipt path, and its exact
   hash plus observed boundary spellings enter the acceptance result at line
   633. Existing whole-result equality at line 650 therefore compares both
   across roots. Terminal bindings and root nonmutation checks remain in force.

The complete textual diff contains no further substantive control or acceptance
changes beyond these edits and renamed gate/script paths. The original four
publication passes, immutable snapshots/manifests, strict zero-overfull and
actual-diagnostic rejection, all other layout text/content/security checks,
warning-review requirement, PDF checks, citation census, exact required product
comparison, and recorder-only root-prefix transformation remain unchanged.
The complete semantic reference-suffix and visual/content review remains
mandatory after successful runtime checks; these predicates do not claim to
replace it. No blocking defect was found in this delta.

## Independently performed verification

All Python invocations used `-I -B`. No build/evidence pathname—old, failed, or
new—was opened, listed, or statted. No publication command, `--build`, network
operation, or PDF write was performed. The sole file written by this reviewer
is this new report; previous scripts and failure/review records were preserved.

- Full production-script diff and test-file diff reviewed.
- Test-file SHA256 verified:
  `90328d00ab57a0109f0872ce26efae4c3b635d1f1f77c2703aefec555289d4af`.
- All 21 regression methods and their table-driven cases passed.
- Built-in self-test passed: 2 positive and 11 negative cases.
- Read-only preflight exited zero; unchanged dependency-frame SHA256
  `27f807a21bce6c72d09f189b200c1212d3629ef4550d9ad203740eef4a8fb726`
  and PDF runtime SHA256
  `66cb425ff3a012c077f5ee1f8b8e7019f8f4d8c471635a2cfc98acdbb3ee6a2b`
  were confirmed alongside all source/tool bindings.
- Four additional independent in-memory negative cases passed: zero counter
  before its heading; a nonzero warning counter after a zero counter; all seven
  boundary labels reversed; and a wrapped boundary alias after References.
- Final candidate rehash remained exactly the Reviewed SHA256 above; the
  predecessor script hash also remains its previously reviewed value.

This PASS is an exact-hash prebuild control decision only. It does not alter any
old failure, demonstrate successful dual-root compilation, approve publication,
or authorize any further retry beyond the bounded plan.
