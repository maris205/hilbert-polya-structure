# P152 — local triad dynamics on triangular books

**Status: ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL.**

This short paper specializes the established p=1/3 local triad update to the
triangular book B(3,r)=K_{1,1,r} under the active imbalanced-triad
update-epoch clock. Its claim-bearing package is deliberately narrow:

- the joint absorption-time/spine-flip Chebyshev transform;
- the quadratic mean and its sharp starting-count extrema;
- the exact mean/parity feasible image and inverse, with one-statistic
  counterexamples; and
- a book-specific private-edge absorption certificate.

The update kernel, social-balance semantics, triadic-dual/XOR representation,
signed-book carrier and static switching classes, generic Bellman/resolvent
machinery, and generic convergence program are explicitly zero-credit
background.

## Exact control

~~~bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p152.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p152.py > /tmp/p152_replay.txt
cmp -s /tmp/p152_replay.txt verification_output.txt
~~~

The frozen Round-2 transcript contains **199,581** exact integer/rational
assertions and ends in PASS.  In addition to the Round-0 lanes, it tests the exact inverse
criterion against 7,335 bounded candidate pairs (7,266 rejected), checks both
single-statistic collisions, sums 8,190 exact private/spine word masses, and
checks 546 finite tail-bound instances.  Enumeration is counterexample
pressure, not a proof, owner certificate, novelty statement, or release gate.

## Rebuild

~~~bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

The settled current `main.pdf` and `main_round2.pdf` are byte-identical:
**5 A4 pages**, **338,933 bytes**, SHA-256
`6671feaadf044abe0e4597a0c81064d9e1bc7590e3891e2acbbd6bf94daec8f6`.
Two isolated source-only builds were also byte-identical to that artifact.
The historical `main_round1.pdf` remains unchanged at 339,258 bytes with
SHA-256
`2ac0da7bc87f8ce1fcc8d730eb95a9dd0c79c7bc870f5f7e40a30593bc2f59d9`.
The historical `main_round0_original.pdf` is preserved unchanged at 338,268
bytes with SHA-256
`f2c2476df00d223fdacaf8fb28954d5f620b10611087c3ff35b16ea158f17e57`.

## Package map

- main.tex and references.bib: anonymous amsart manuscript and five verified
  primary/author-hosted references.
- PAPER_PLAN.md, NARRATIVE_REPORT.md, and PROOF_PACKAGE.md: claim architecture,
  readable account, and expanded proof spine.
- CLAIMS_EVIDENCE.md and CONTROL_RESULTS.md: evidence ledger and exact-control
  scope.
- SOURCE_VERIFICATION.md: owner subtraction and bounded primary-source log.
- HOSTILE_REVIEW_A.md, HOSTILE_REVIEW_B.md, and IMPROVEMENT_LOG.md: both raw
  internal reviews and the evidence closing every finding.
- BUILD.md and FINAL_QA.md: deterministic build and Round-2 internal closure.
- verify_p152.py and verification_output.txt: paper-local falsifier and frozen
  deterministic transcript.

Review A returned 0 Critical / 0 Major / 2 Minor; both items closed in
Round 1.  Review B returned 0 Critical / 0 Major / 1 Minor; its candidate-
domain defect was repaired in Round 2 before any square root is formed.
No Critical, Major, or Minor item remains unresolved.  Internal acceptance
does not authorize posting, submission, circulation, author contact, or any
other external action.
