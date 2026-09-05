# P197 improvement-loop recovery

Stage: ROUND2_FROZEN / INDIVIDUAL_TERMINAL_PASS / HOLD_EXTERNAL.
Round0 and Round1 pins: ROUND0_RECEIPT.md and ROUND1_RECEIPT.md.
Review A: accepted no change, root replay complete.
Review B: accepted no change after root replay; ROUND2_RECEIPT.md pins the
physical freeze. Both paper rounds are actual reviews, not Stage1 gates.
Two terminal source-only builds, all four final page views, complete
manifests and author/A/B double replays passed the retained-subset audit.
The exact audit output is under docs/papers197_201_sequence/qa/.
This is individual paper completion, not five-paper batch completion.

The auto-paper-improvement-loop skill structures two manuscript rounds.
Its default external GPT5.4 MCP is unavailable; no external manuscript
upload is authorized. Actual reviews use separate current-model agent
processes and independent code, not cross-model or human-expert certification.
The project protocol's distinct A/B reviewers overrides the weaker same-
reviewer default. Full raw reviews and deltas remain in their review folders.
