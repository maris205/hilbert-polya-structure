# P141 improvement log

Current status: `ROUND-B OWNER-SUMMARY REPAIR COMPLETE / GO_INTERNAL
(OWNER-THIN) / HOLD_EXTERNAL`.

## Round A — 2026-09-01 UTC

**Review input:** `HOSTILE_REVIEW_A.md`. **Historical theorem/artifact
disposition:** `PASS / HOLD_EXTERNAL`; this was not owner clearance and was
later narrowed by the batch owner audit and hostile review B.

### Finding disposition

Hostile review A reported zero critical, zero major, and zero minor repair
items within its then-frozen scope. It independently checked the owned support subtraction, weighted
reverse-stick law, hazard/simplex inverse, nonidentifiability, accepted-size
PGF, marginals/nesting, and the four-statistic clock firewall.

### No source repair

No change was made to:

- `main.tex`;
- `references.bib`;
- `code/verify.py`;
- `code/verification_output.txt`;
- the current `main.pdf` bytes.

Only Round-A status/audit documentation was updated, and the unchanged current
PDF was copied to `main_round1.pdf`. This records a PASS; it does not fabricate
a repair, novelty finding, or owner clearance.

### Artifact identity

`main.pdf`, `main_round0_original.pdf`, and `main_round1.pdf` are byte-identical
at 254,394 bytes with SHA-256
`e87ba3878dc55e24b90c135ef2b356aae0a0ef8d33274354213c25c0d5d2b0f6`.
The manuscript source remains SHA-256
`b312ca8becfcc405de8276195058b9876c8631ae0119b882a5bf4973db2d7f6e`.
Canonical replay remains 750,181/750,181 assertions passing.

## Round B — 2026-09-01 UTC

**Review input:** `HOSTILE_REVIEW_B.md` and the frozen batch
`FINAL_OWNER_AUDIT.md`. **Disposition before repair:** `REPAIR /
HOLD_EXTERNAL`. **Disposition after the requested documentary repair:**
`GO_INTERNAL (OWNER-THIN) / HOLD_EXTERNAL`.

### Mathematical and artifact result

Hostile review B independently reattacked the endpoint law, inverse/simplex
map, PGF, marginals, statistic firewall, verifier, isolated build, and PDF. It
found no theorem or artifact defect. Therefore `main.tex`, `references.bib`,
`code/verify.py`, `code/verification_output.txt`, and `main.pdf` remain
unchanged.

### Documentary ownership repair

The paper-local summaries now say explicitly that this is a **specialized
exact-law note** built on fully owned threshold-graph support,
RSA/random-greedy process, and Plackett/exponential weighted order. Theorem
3.1's reverse-stick endpoint law, together with its inverse/simplex, PGF, and
marginal consequences, is labelled **owner-thin and folklore-risky**. A
bounded absence of a direct printed owner is recorded only as a non-hit: it is
not novelty, priority, or owner clearance.

The unchanged current PDF is frozen as `main_round2.pdf`. Documentary changes
and the exact unchanged-source boundary are itemized in
`OWNER_REPAIR_LOG.md`.
