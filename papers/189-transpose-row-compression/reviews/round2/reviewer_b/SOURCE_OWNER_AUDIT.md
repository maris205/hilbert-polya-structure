# P189 Review-B Source and Owner Audit

## Scope

This note expands the source, citation, scope, and owner-status parts of
`REVIEW.md` into a standalone audit record for the bound Round-1 object.

Reviewed inputs were pinned on 2026-09-04 in `PINNED_INPUTS.sha256` and are
limited to:

- `papers/189-transpose-row-compression/main.tex`
- `papers/189-transpose-row-compression/references.bib`
- `papers/189-transpose-row-compression/main_round1.pdf`
- `papers/189-transpose-row-compression/code/verify_p189.py`
- `papers/189-transpose-row-compression/code/CANONICAL.txt`
- `papers/189-transpose-row-compression/reviews/round1/reviewer_a/verify_review_a.py`
- `papers/189-transpose-row-compression/reviews/round1/reviewer_a/CANONICAL.txt`

The author verifier/canonical and Review-A verifier/canonical were used only to
bind the reviewed object and compare declared controls.  No Review-A conclusion
was inherited.

## Source-claim scope

The manuscript source declares the literal rule and scope at
`main.tex:63-88` and `main.tex:294-317`.  The active claim boundary is:

- square `n x n` binary matrices only;
- displayed row and column labels retained;
- synchronous update only;
- transpose occurs after row compression;
- the scoped object is the exact conjunction of the literal map, the
  four-iterate clock, and the target-local inverse laws.

The manuscript explicitly excludes or declines to claim:

- rectangular variants;
- any rule that sorts inside the literal update;
- asynchronous schedules;
- random kernels;
- unlabelled quotients;
- novelty, priority, or circulation authorization.

Review B confirmed those fences remain explicit in the bound source and match
the rendered PDF.

## Citation-key audit

At `main.tex:79-82`, the source cites exactly four bibliography keys:

- `Miller2013`
- `KouteckyOnn2020`
- `DasDasSen2016`
- `Andrews1998`

Review B rechecked that the local `references.bib` contains exactly those four
keys and no extras.  The local records matched the corresponding primary or
official references consulted on 2026-09-04:

- Cambridge University Press:
  <https://www.cambridge.org/core/books/theory-of-partitions/7BC70DD4C1A06AA6179CEDEAD2F0C2DC>
- ScienceDirect:
  <https://www.sciencedirect.com/science/article/pii/S0012365X12005195>
- ScienceDirect:
  <https://www.sciencedirect.com/science/article/pii/S0012365X15003647>
- arXiv:
  <https://arxiv.org/abs/2011.09932>

This check validated bibliographic identity and citation scope only.  It did
not attempt to transfer novelty or contribution ownership from those sources.

## Owner-status boundary

At `main.tex:84-88` and `main.tex:297-299`, the manuscript states that the
bounded owner search did not locate the exact conjunction of claims, but also
states that this non-hit is not novelty or priority evidence and that external
circulation remains on hold.

Review B confirmed that:

- the source still contains `OWNER_AMBER / HOLD_EXTERNAL`;
- the rendered PDF still contains the same owner-status language;
- no package artifact upgrades that bounded statement into a novelty,
  clearance, freedom-to-operate, or release authorization claim.

## Review-B conclusion

No source-scope, citation-set, or owner-status defect was found in the bound
Round-1 object.  The conclusion remains:

- verdict: `PASS`
- findings: `critical=0`, `major=0`, `minor=0`
- external status: `OWNER_AMBER/HOLD_EXTERNAL`

This note is a standalone audit record, not a publication or ownership
clearance decision.
