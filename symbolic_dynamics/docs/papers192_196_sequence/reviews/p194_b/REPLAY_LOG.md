# P194 Review-B replay log

## Terminal status

`PASS / ACCEPTED_REPAIR / 0C-0M-0m OPEN / OWNER_AMBER / HOLD_EXTERNAL`

## Independent reviewer control

Two fresh processes ran:

```bash
set -o pipefail
PYTHONDONTWRITEBYTECODE=1 \
  python3 docs/papers192_196_sequence/reviews/p194_b/verify_review_b_p194.py \
  | cmp - docs/papers192_196_sequence/reviews/p194_b/CANONICAL.txt
```

Both exited zero.  Canonical receipt:

- Replay 1 ran the displayed verifier in a fresh process and matched
  `CANONICAL.txt` byte for byte.
- Replay 2 ran the same verifier in a second fresh process and matched both
  Replay 1 and `CANONICAL.txt` byte for byte.

```text
representation=sign rewrite / growth diagram / GT branching /
               cyclotomic product / Young poset / matchings
boxes=35 (k=1..7, n=1..5)
states/transitions/targets=34,636/34,636/34,636
components/fixed=235/235
assertions=16,194,669
control digest=54651eac45dd17bad67185edbe91e72ece5ba976b871fa483cbb860e6756878b
historical findings=0C/1M/0m, all resolved
open findings=0C/0M/0m
result=PASS
```

## Author-control regression

Two fresh processes ran:

```bash
set -o pipefail
PYTHONDONTWRITEBYTECODE=1 \
  python3 papers/194-least-raising-crystal-words/code/verify.py \
  | cmp - papers/194-least-raising-crystal-words/code/CANONICAL.txt
```

Both exited zero and reproduced the author's 618,419-assertion canonical
output byte for byte.

## Cold-build replay

Two fresh source-only temporary builds each ran the deterministic four-pass
`pdflatex/bibtex/pdflatex/pdflatex` recipe with
`SOURCE_DATE_EPOCH=1704067200` and `TZ=UTC`.  Both produced

```text
682eeced97037b899f91dc2b93afaaf514b6dcbf8f95d1225ddb87f4cce6203b  main.pdf
Pages: 5
File size: 372121 bytes
Page size: A4
PDF version: 1.5
```

The outputs are byte-identical to the accepted repaired `main.pdf`.  The
immutable four-page `main_round1.pdf` remains separately pinned at
`9f1b67680b4c915e5bd60d01730095d5d06817368244d83ecfc84d39a86bf207`.

## Source and package checks

```bash
sha256sum -c docs/papers192_196_sequence/reviews/p194_b/PINNED_INPUTS.sha256
cd docs/papers192_196_sequence/reviews/p194_b
sha256sum -c SHA256SUMS
```

Both checks pass after sealing.  `PINNED_INPUTS.sha256` uses only
workspace-root-relative paths.  `SHA256SUMS` uses only package-relative
paths, omits itself, and covers every other regular file in the ten-file
Review-B package.

Finite replay is falsification pressure only.  It is not proof, source
completeness, novelty evidence, owner clearance, or authorization for
external circulation.
