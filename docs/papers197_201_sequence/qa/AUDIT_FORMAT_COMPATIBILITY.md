# Accepted-review serialization compatibility

2026-09-05 UTC. The terminal auditor was adapted to actual frozen evidence;
no accepted review transcript, report, source, code or manifest was rewritten
to fit a filename/serialization assumption.

- P197 B's immutable canonical ends with an explicit bounded-review PASS
  line and no stdout severity fields. Its separately hashed full report
  contains the exact open C0/M0/m0 census. The parser accepts precisely that
  explicit PASS line and, only when stdout contains no severity field at
  all, the explicit report census. Present nonzero/incomplete stdout counts
  cannot fall back to a passing report. The successful review-gate test
  reran the frozen verifier twice, byte-identically (4,833,354 each).
- P200 B names its accepted delta DELTA_ACCEPTANCE.md, not DELTA.md. The
  parser allows either name but still requires exactly one delta and checks
  its accepted decision. It does not create an extra duplicate delta.
  That explicit Decision label may follow a date on the same line. P200 B
  also pins absolute original-workspace paths; only that known root is
  relocated to the auditor's ROOT, preserving all hashes. Foreign absolute
  roots and parent traversal remain rejected. No scientific gate is waived.
  Its stdout likewise has an explicit bounded-review PASS and its hashed
  report carries the C0/M0/m0 census (comma separators, optional whitespace).
  Those two exact success forms are recognized, not an unrestricted match
  on the word PASS anywhere in a transcript.
- The cold-build helper accepts an explicit validated subset so Round2
  papers can complete their own two physical builds while a seat is open.
  This does not bypass the main terminal auditor's exact five-paper rule.

The first P197-B compatibility test required the report census at the
start of a line and failed on its real mid-line placement. The corrected
word-boundary matcher passed. These are parser fixes, not mathematical
repairs, new author revisions, or evidence of a completed batch.
