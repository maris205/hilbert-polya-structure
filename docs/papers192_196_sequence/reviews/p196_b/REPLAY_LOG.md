# P196 Review-B replay log

**Replay date:** 2026-09-04 UTC.  
**Platform:** Linux 5.15.0-78-generic x86_64; Python 3.12.3.  
**Reviewer implementation:** standard-library Python; no imported author or
Review-A module.

## Independent reviewer control

Command, run twice consecutively from the workspace root:

```bash
PYTHONDONTWRITEBYTECODE=1 \
python3 docs/papers192_196_sequence/reviews/p196_b/verify_review_b_p196.py \
  | cmp - docs/papers192_196_sequence/reviews/p196_b/CANONICAL.txt
```

```text
replay 1: exit 0, byte-equal, 8.047 seconds
replay 2: exit 0, byte-equal, 8.021 seconds
canonical SHA-256: 150ea6de7af70e714a9ba41efe9120500fb63814bcaf9d85b504838e1eaad1c6
verifier SHA-256: d23b9ccc374d09ca1814dcf7667d562eb2e6a4fb0f13ef737c98418250f5bc9c
```

Canonical coverage:

```text
representation: packed radix states + cyclic relation-matrix CSP
boxes: 32
states/transitions/targets: 41,704 / 41,704 / 41,704
core states: 3,205
higher-time labelled target checks: 208,300
fixed-iterate checks: 214
relation-matrix gap checks: 3,420
Faddeev--LeVerrier characteristic checks: 11 (q=2,...,12)
assertions: 421,266
control digest: c8be119f1e4581a44c20d14dd9792a66a4597e6d0889201dd6d5c9916a8408f5
result: PASS
```

The two `cmp` successes certify equality of every stdout byte, including the
coverage counters, digest, finding census, decision, and external gate.  No
`__pycache__` directory was produced.

## Frozen author control

The author program was treated only as a black-box regression control after
the Review-B implementation had passed:

```bash
cd papers/196-cyclic-godel-implication
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py | cmp - code/CANONICAL.txt
```

```text
author replay 1: exit 0, byte-equal, 7.236 seconds
author replay 2: exit 0, byte-equal, 7.209 seconds
author canonical SHA-256: f6c7bb13a0e43a97967ad4f97c3b1267ff292f8c6642393d66279de7b005a2fd
author verifier SHA-256: 87f990611f842a2a5bce280e13dc9fec810a6bae46dd2758c0e13af930ef6bfe
```

## Accepted Review-A control

Review A was also replayed as a pinned black box; it was not imported or used
to calculate Review-B results:

```bash
cd docs/papers192_196_sequence/reviews/p196_a
PYTHONDONTWRITEBYTECODE=1 python3 verify_review_a_p196.py | cmp - CANONICAL.txt
```

```text
exit: 0, byte-equal, 5.225 seconds
Review-A canonical SHA-256: fffc707f1e80dc5b7ff79e0cacbd6d2d175c827760789b0fd6e44862b91e9a37
Review-A verifier SHA-256: 0ef8d0867e10a7ed256ab223632e344ea151e1bb3df223d57579f799865e3966
```

## Input and package integrity commands

From the workspace root:

```bash
sha256sum -c docs/papers192_196_sequence/reviews/p196_b/PINNED_INPUTS.sha256
cd docs/papers192_196_sequence/reviews/p196_b
sha256sum -c SHA256SUMS
```

Both checks pass after final package sealing.  `PINNED_INPUTS.sha256` uses only
workspace-root-relative paths and contains no parent traversal.  `SHA256SUMS`
uses package-relative paths and covers every payload other than itself.

Final replay disposition: `ACCEPTED_NO_CHANGE`, `0/0/0`,
`OWNER_AMBER / HOLD_EXTERNAL`.
