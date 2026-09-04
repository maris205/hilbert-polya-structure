# P191 Review A — deterministic replay receipt

## Reviewer control

The reviewer control is process-separated from the author implementation and
imports no author code.  Its frozen identities are:

```text
verify_review_a.py
  SHA-256: d85c52c2ca1edae596d60342945887c07af87a6717b27c4e313a752bb4c44f26
  lines: 367
  bytes: 13449
CANONICAL.txt
  SHA-256: 545f9e9a3d6d9fbbbebff84ebea3778375d8d1857b98a733f6f3eae5eca08a02
  lines: 35
  bytes: 3639
```

From the repository root, two separately launched fresh post-delta Python
processes ran the following comparison:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  papers/191-prefix-divisibility-cuts/reviews/round1/reviewer_a/verify_review_a.py \
  | cmp -s - \
  papers/191-prefix-divisibility-cuts/reviews/round1/reviewer_a/CANONICAL.txt
```

Both comparisons returned status zero:

```text
fresh reviewer replay 1: PASS (exit 0)
fresh reviewer replay 2: PASS (exit 0)
canonical stdout: 35 lines / 3639 bytes
canonical stdout SHA-256: 545f9e9a3d6d9fbbbebff84ebea3778375d8d1857b98a733f6f3eae5eca08a02
assertions per replay: 2864221
```

## Input and author control

Running `sha256sum -c` on `PINNED_INPUTS.sha256` returned `OK` for the five
immutable Round-0 inputs and the accepted corrected source ledger.  A
separately launched clean execution of the frozen author verifier also matched
the frozen author `code/CANONICAL.txt` byte for byte (exit zero).  That author
replay is a package-integrity receipt only; the reviewer theorem attacks and
finding classification come exclusively from the independent reviewer
implementation and proof rederivation.

## Preserved finding history and accepted outcome

The frozen Round-0 review outcome was:

```text
FORMAL_COUNTEREXAMPLES=0
CRITICAL=0
MAJOR=0
MINOR=1
FINDING=P191-A-MI-01_OEIS_HISTORY_DATE_IN_SOURCE_LEDGER
OWNER=OWNER_AMBER
LIFECYCLE=HOLD_EXTERNAL
VERDICT=MINOR_REVISION_REQUIRED
```

After binding the requested-only ledger delta, the final output is:

```text
FORMAL_COUNTEREXAMPLES=0
CRITICAL=0
MAJOR=0
MINOR=0
HISTORICAL_FINDING=P191-A-MI-01_OEIS_HISTORY_DATE_IN_SOURCE_LEDGER
DELTA=P191-A-MI-01_ACCEPTED
OWNER=OWNER_AMBER
LIFECYCLE=HOLD_EXTERNAL
VERDICT=PASS_DELTA_ACCEPTED
```

The two-run receipt does not convert finite computation into proof or bounded
owner-search non-hits into novelty or release clearance.
