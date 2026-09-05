# Actual P202 Review A replays

Two fresh processes of the final independent verifier were executed by
qa/run_replays.sh on 2026-09-05 UTC. These are this reviewer's runs, not
author transcripts copied and relabelled. Earlier development executions
are not counted as either final replay.

| Execution | Actual UTC start | Actual UTC finish | Process result |
|---|---|---|---|
| Replay 1 | 07:04:54 | 07:05:24 | exit 0; REPLAY1.txt |
| Replay 2 | 07:05:24 | 07:05:55 | exit 0; REPLAY2.txt |

Each ran `python3 -B verify_independent.py` in the review directory, with
stdout recorded through tee and pipefail active. No author or Stage1
Python module was imported. The explicit `cmp REPLAY1.txt REPLAY2.txt`
exited zero. CANONICAL.txt is the same actual output, copied using
apply_patch; subsequent byte comparisons against both transcripts pass.

Verifier SHA-256:
3eb765f1027045bbe39e8959c0defaa41e7783fef181a573f072415c7762bb5b.
Both replay and canonical SHA-256:
c6962646a4a014f278ef8414883df8f95d8b33e8975ec60acfc7b22ff7a1a3c7.

Each process completes 12,775,204 exact assertions, all 797,160 words
through n=12, 24,577 bounded parking configurations and sharp words
n=3..180. The terminal output is literally:

```text
status=PASS
findings=critical:0,major:0,minor:0
```

The findings line records the separately completed manuscript audit;
Python does not certify global priority. The executable is deterministic
and standard-library-only. Suggested independent root replay, from the
project root:

```sh
set -o pipefail
python3 -B docs/papers197_201_sequence/reviews/p202_a/verify_independent.py | cmp - docs/papers197_201_sequence/reviews/p202_a/CANONICAL.txt
sha256sum -c docs/papers197_201_sequence/reviews/p202_a/PINNED_INPUTS.sha256
```

Package manifests use directory-relative paths, while input pins deliberately
use project-root-relative paths. Root replay is not claimed as already run
by this review package. OWNER_AMBER / HOLD_EXTERNAL persists.
