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

## P202 evidence-only compatibility (2026-09-05 UTC)

This is a mechanical archive/parser task, not another P202 research review.
The P202 manuscript writer performs this compatibility work and is not
counted as paper reviewer A or B. No accepted paper/review source, code,
canonical, report, delta, manifest, or frozen snapshot is edited.

### Actual failures and exact adaptations

1. Root's actual evidence audit session 3245 reached the author status
   parser after the completed final cold builds and failed with
   `P202 author lacks an accepted status`. Direct evaluation of both old
   status expressions against the actual frozen canonical confirmed both
   were false. The unchanged P202 author transcript ends with
   `status=PASS_AUTHOR_CONTROL`, not a generic paper/review acceptance.
   Compatibility is restricted to label `P202 author`, verifier SHA-256
   `42c79767025b5da710aaccd8be170df964a14a65427470dd814cf3ce4081b850`,
   canonical SHA-256
   `a971574926784fa43f27df88b58979ba6724a11c6070a3484c7641ea56fd6446`,
   and that exact complete status line. No arbitrary `PASS_*` prefix or
   author-status-as-review acceptance is introduced. Its historical
   `review_A=NOT_STARTED; review_B=NOT_STARTED` line remains unchanged
   provenance; the final A and B packages are checked separately.

2. The next physical subset run, session 18973, passed the author replay
   and failed with `P202-a core-file cardinality failure`. P202 A preserves
   both `REVIEW_INTAKE.md` and its final `REVIEW_A.md`; the old filename glob
   treated the historical intake as a second verdict. The following run,
   session 40467, passed author/A and actually failed with the analogous
   `P202-b core-file cardinality failure`. B preserves its intake too.
   The parser now excludes only `REVIEW_INTAKE.md` in the exact P202 A/B
   roles, and only with these accepted hashes:

   - A intake: `d5d5fc29bba5bca288fc73a01284e9e4012f61564a6cf2d9467c53d3a73e312f`.
   - B intake: `28f27668feeab6dccf647dc58508bb00bfa4ccfcefc0c7b73c66b3b1db81f1a7`.

   Both intakes remain required by their complete manifests. Any changed
   intake hash, unexpected extra review file, missing final report, or
   multiple accepted deltas still fails. These are role distinctions, not
   deletion or rewriting of historical intake records.

3. Before this subtask, root had added the other observed P202 A format:
   `assertions 12775204` uses a space rather than `=`. The count expression
   accepts the known whitespace/equal serializations but still requires
   exactly one integer total. That root change is preserved here; the
   canonical is not rewritten to fit a preferred serialization.

### Gates retained and bounded regression checks

The successful output must still come from two real verifier executions
whose complete stdout equals the immutable canonical. Status recognition
does not bypass input pins, full manifest hashes/coverage, unique final
report and accepted delta, zero critical/major/minor counts, B replay
receipt, source citation checks, PDF/font/metadata checks, both final cold
build artifacts, or all-page render coverage. In particular, present
nonzero/incomplete stdout severity fields cannot fall back to a zero-count
report. The main auditor's five-admitted-paper rule is unchanged; the
subset remains explicitly not a completed five-paper batch.

Focused parser tests accepted the exact P202 author pair and rejected its
use as a different author or as a review, as well as wrong code/canonical
hashes. All three severity fields retained their zero/nonzero distinction.
The count parser recognized space/equal forms and still detected duplicate
totals. Artifact-only tests selected each exact final A/B report and rejected
an altered intake digest. Those focused tests stubbed verifier output to
isolate parsing; they are not recorded as mathematical verifier replays.

The final physical subset replay is recorded verbatim in
`P202_EVIDENCE_AUDIT.txt`. Its status applies only to evidence for P202, not
complete terminal manifests, research novelty, external release, or a
five-paper completion. No Git or recovery-index edit is part of this task.

The final real command was
`python -B docs/papers197_201_sequence/qa/audit_retained_subset.py 202 --evidence-only`.
Session 59824 exited zero (completion receipt `a9b1b6`). It reports 692
mechanical audit assertions, 4 pages, 5 citations, and author/A/B counts
3,962,690 / 12,775,204 / 8,456,463, each replayed twice. The two final cold
builds were already physically produced by root; this command checks those
artifacts rather than pretending to rebuild them. The saved output is the
concatenation of actual startup and completion stdout, written with
`apply_patch` and byte-compared with the retained tool output. The terminal
line is `status=EVIDENCE_PASS_NOT_FINAL`; full paper manifests and batch
completion remain separate obligations.
