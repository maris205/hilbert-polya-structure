# P211: two-build diagnostic disposition and bounded artifact acceptance

Root decision: CLOSE_THE_CENSUS_OMISSION_WITH_ADDITIVE_CORRECTION;
RETAIN_THE_REPORTED_TYPESETTING_WARNING_AS_NONBLOCKING_FOR_THE_REVIEWED_PDF.
This decision is effective with the successful documentary check in this
packet. It does not suppress the warning, certify its harmlessness, or
establish that internal font expansion operated as intended.

## Exact issue and correction

P211-COLD1-IO-D1 and P211-COLD2-DIAGNOSTIC-CENSUS both identify incomplete
saved warning summaries. The historical case-sensitive capital-W matcher
misses the lower-case pdfTeX warning. Both original final measurement
objects and all original logs remain unchanged. They are retained evidence,
not the current complete diagnostic census and not zero-warning claims.

The actual final log in EACH build contains one engine-warning emission:

    pdfTeX warning (font expansion): font should be expanded before its first use

It occurs at final main.log line608 (pass2 also has it at line624). Each
final log also has two underfull messages, at lines596 and602. There are
no final actual undefined-reference/citation, missing-character, overfull,
rerun-request or error/fatal diagnostics under the full received context
classification. Literal occurrences in loader metadata, BibTeX's warning$
counter, and the two microtype informational protrusion-setting contexts
are recorded with their contexts and are not silently counted as emissions.

The complete generated DOCUMENTARY_CHECK.json includes both builds' eighteen
log-role rows, exact byte pins, final warning multisets, original measurement
pins, retained notices and the additive current finding census. Cold2's full
new census is independently root-reconstructed. Its eighteen corresponding
raw files are each actually compared with cold1, then its complete context
classification is expressly reused for the byte-identical cold1 files.
This is disclosed metadata reuse, not another independently authored scan
or a new Python-auditor invocation. Old cold1 census classifications remain.

Both omission findings are resolved by this complete supplement and the
explicit disposition, not by modifying historical arrays or removing logs.
The engine warning survives as a reported known typesetting limitation;
it is not silently converted to a zero-warning result.

## Why the retained warning does not block this artifact

The accepted terminal scope is a readable, complete rendering of the pinned
reviewed mathematical manuscript with complete build/diagnostic provenance.
The current evidence consists of two actual source-only four-pass builds;
all native exit/input/output and ordered FLS/BibTeX roles received; resolved
final references/citations; 21 embedded/subset/Unicode-flagged font objects;
complete extracted text without the specified unresolved markers; the
actual five-page PDF and render-byte equality; and five actual page views.
The page-specific views found no visible clipping, collision, missing
symbol or unreadable bibliography at the inspected resolution. These are
separate observations; successful production or identical bytes alone is
not used as a typography-correctness proof.

No observed content/readability defect or failed required final build check
remains after the diagnostic accounting correction. The project does not
require proof of the engine's internal microtypographic state or equality
to an unspecified ideal rendering. Root therefore retains the warning as
nonblocking for this exact reviewed artifact. The residual internal-state
uncertainty is acknowledged, not proved away. This decision must not be
generalized to other inputs, engine versions or warning types. A later
specific content or layout defect reopens its affected scope.

The source desk supports a bounded late-expansion-setup interpretation in
the directly inspected current upstream implementation. It does NOT supply
an exact source/binary match: executed1.40.22 versus retrieved1.40.29. No
font/macro/character is identified from the saved warning, and the historical
microtype advice for versions earlier than1.40.4 is not applied. No causal
repair is inferred or attempted. These restrictions are deliberate reasons
not to assert harmlessness or an unsupported engine explanation.

## Controlling evidence and phase boundary

- [Cold1 complete originals/I/O/census](../p211_terminal_cold_artifact_root01/RECEPTION.md).
- [Cold2 complete originals/I/O/census](../p211_terminal_cold_artifact_root02/RECEPTION.md).
- [Received font-warning primary-source desk](../p211_font_warning_root01/RECEPTION.md).
- [Actual PDF/render pair and five views](../p211_terminal_pair_pages_root01/RECEPTION.md)
  and its [page-specific observations](../p211_terminal_pair_pages_root01/VISUAL_REVIEW.md).
- [Build1 complete capture reception](../p211_terminal_enable_root01/build_1/CAPTURE_RECEPTION.md)
  and [build2 complete capture reception](../p211_terminal_enable_root01/build_2/CAPTURE_RECEPTION.md),
  each following its own separately received refresh and enable stages.

Those original receipts retain their historical pending wording; this
additive decision is the current diagnostic/terminal-artifact disposition.
Full cold-artifact acceptance is now supplied only for their combined
accepted scope and unchanged inputs, with the reported notices above.
No new manuscript verdict, science, build, rendering or page view is implied.
The independent scientific replay dependency domain, current README/history
mapping and whole-paper manifest still require lifecycle reconciliation;
P211 is not marked complete by this artifact-only decision.

The symbolic-dynamics workflow governs change-sensitive verification.
paper-compile requires reporting, not suppressing, remaining warnings;
its generic cleanup/rebuild/venue suggestions do not override this project's
preservation rules or supply a reason to alter accepted sources. There was
no TeX change or fresh compilation. All sources, PDFs, logs, measurements,
failures, frozen rounds and old seals remain intact. OWNER_AMBER /
HOLD_EXTERNAL; no Git, external upload or specialist contact.
