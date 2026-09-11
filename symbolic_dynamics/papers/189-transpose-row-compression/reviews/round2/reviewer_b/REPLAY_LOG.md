# P189 Review-B Replay Log

## Scope

This note records two fresh verifier replays performed from the repository
root on 2026-09-04, plus the repo-root pinned-input verification.  It expands
the replay summary already stated in `REVIEW.md` without changing the Review-B
conclusion.

## Canonical target

```text
CANONICAL.txt SHA-256:
9b0302b918a3d0e905d50ca4e9780594f68023d39f8f7252d47364c6848cbdf9

CANONICAL.txt lines/bytes:
53 / 2921
```

The expected terminal invariants are:

```text
exact_assertions=1493195
critical_findings=0
major_findings=0
minor_findings=0
verdict=PASS
external_status=OWNER_AMBER/HOLD_EXTERNAL
```

## Fresh replay record

The replays were launched from repo root with `PYTHONDONTWRITEBYTECODE=1` and
the package-local verifier path:

```bash
python3 papers/189-transpose-row-compression/reviews/round2/reviewer_b/verify_review_b.py
```

Execution window:

- replay batch start: `2026-09-04T09:59:53Z`
- replay 1 complete: `2026-09-04T10:00:11Z`
- replay 2 complete: `2026-09-04T10:00:28Z`

Fresh output hashes:

```text
run1.txt:
9b0302b918a3d0e905d50ca4e9780594f68023d39f8f7252d47364c6848cbdf9

run2.txt:
9b0302b918a3d0e905d50ca4e9780594f68023d39f8f7252d47364c6848cbdf9
```

Both replay outputs matched each other byte for byte and each matched
`CANONICAL.txt` byte for byte via `cmp`.

## Repo-root input pin check

The repo-root command

```bash
sha256sum -c papers/189-transpose-row-compression/reviews/round2/reviewer_b/PINNED_INPUTS.sha256
```

returned `OK` for all pinned inputs:

- `papers/189-transpose-row-compression/main.tex`
- `papers/189-transpose-row-compression/references.bib`
- `papers/189-transpose-row-compression/main_round1.pdf`
- `papers/189-transpose-row-compression/code/verify_p189.py`
- `papers/189-transpose-row-compression/code/CANONICAL.txt`
- `papers/189-transpose-row-compression/reviews/round1/reviewer_a/verify_review_a.py`
- `papers/189-transpose-row-compression/reviews/round1/reviewer_a/CANONICAL.txt`

## Conclusion

The hardened Review-B package replay remains stable:

- two fresh repo-root verifier runs reproduced the frozen canonical output;
- exact assertion count remained `1493195`;
- verdict remained `PASS`;
- findings remained `critical=0`, `major=0`, `minor=0`;
- external status remained `OWNER_AMBER/HOLD_EXTERNAL`.

This replay log is evidentiary for the exact pinned object only.  It is not a
novelty, priority, ownership-clearance, or external-release statement.
