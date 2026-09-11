# Preserved documentary patch refusal

The first root batch-index patch expected a standalone line
`Status: P211_ADMITTED / ONE_RETAINED / FOUR_OPEN_SEATS` (with the actual
Markdown backticks and terminal period). The real status was the second
half of `complete final handoff. Status: ...`, so apply_patch rejected the
expected context before changing any file. The subsequent patch used the
actual complete line and succeeded. No historical file, scientific input
or execution record was changed by the refused patch. A later root-only
placement correction moved the newly written current-build paragraph above
the previous-round heading before documentary acceptance; no accepted
historical paragraph was altered.
