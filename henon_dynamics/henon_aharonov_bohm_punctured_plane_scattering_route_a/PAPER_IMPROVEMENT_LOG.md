# Improvement and correction record

The three versions implement the substantive growth in PAPER_PLAN.md. The first audit fixes the origin domain and complete transform. The next audit adds the full forward distribution. The final audit adds the local/global heat distinction, ordinary determinant obstruction, and explicit physical time-reversal class.

Actual issues found and resolved:

- The C379 author independently found that the proof's heat-tail first-order formula needed the fundamental flux cell or a cutoff larger than the absolute general flux. The proof now states both alternatives.
- The peer asked for a precise reference for the complete wave-operator input. The manuscript identifies Pankrashkin–Richard Lemma 7 and separates that imported theorem from the sign derivation.
- The symbolic Abel check initially omitted the constant minus one from its expected rational expression. The check failed, and the expected expression was corrected to the full two-half-axis difference. The analytic proof already retained that constant.
- Initial PDF text extraction revealed legacy mathematical-font control bytes. Unicode mathematical fonts were selected to preserve extractable equations; the PDF gates were rerun rather than relaxed.

These are internal and author-swapped checks within the current model family. No external model, human referee, journal decision, or independent error-process claim is represented.

Engineering G3 follow-up: root requested an actual writable-release YAML attack test. The existing checker already pinned raw YAML bytes; the release script now also calls that strict gate before any artifact work. Three actual `--write` attacks (unknown key, false to integer zero, unquoted date) were executed and rejected. The actual settled compiler logs were renamed byte-for-byte from ignored `.log` suffixes to tracked `.txt` suffixes. No theorem source, mathematical claim, evaluation bytes, evidence bytes, or PDF bytes changed in this follow-up.
