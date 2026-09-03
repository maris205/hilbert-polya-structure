# P175 Hostile Review B — independent exact control

This directory is the executable evidence for the non-author,
non-Review-A hostile Review B of
`papers/175-diagonal-feedback-commutator/`.

## Independence boundary

`verify_review_b.py` imports no paper-author, Review-A, or scouting module.
It represents matrices as canonical sparse `(cell,value)` tuples decoded
from base-`q` integers.  Its finite fields are generic polynomial quotients,
including `GF(4)`, `GF(8)`, `GF(9)`, and `GF(16)`.  This differs from the
dense flat-tuple representations used by the author and Review A.

## Exact scope

The control first verifies field axioms and the scalar-equation `0/1/q`
trichotomy in `q=2,3,4,5,7,8,9,16`.  It then exhausts all sources and all
codomain targets in twelve boxes:

```text
(n,q) = (1,4), (1,8), (1,9), (1,16),
        (2,4), (2,8), (2,9), (2,16),
        (3,2), (3,3), (3,4), (4,2).
```

For each box it checks the literal update, square-zero collapse,
every-target aggregate and occupation-marked fibres, image criterion,
support census, weak-composition kernel, unique maximal zero fibre,
complete rooted tree, sharp height, all-time fibres, image tower, and fixed
censuses.  A separate colouring engine checks the exact complete-graph
multivariate Potts specialization and the chromatic occupation transform.

The canonical result is `2,559,272` assertions with status
`PASS_MATHEMATICS_OWNER_REFRAME_REQUIRED`.  The owner reframe is finding
`P175-B-M01` in the paper-local `HOSTILE_REVIEW_B.md`; `HOLD_EXTERNAL`
remains unchanged.

## Replay

From this directory run:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 python3 verify_review_b.py
```

The output must match `CANONICAL.txt` byte for byte.  Review B performed two
fresh processes and both matched.  Finite enumeration is a falsification and
regression control, not a proof of the all-parameter theorem and not an
owner/novelty certificate.
