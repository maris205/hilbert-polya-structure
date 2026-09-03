# P173 Hostile Review B control

This directory contains an independent exact control for P173, *Random
Quotient-Leakage Erosion*.  The control was written for Hostile Review B and
does not import the author verifier, scout code, or Review-A code.

## Independent representation

The literal finite-state check represents each subspace by the incidence
bitset of its normalized projective points.  An ambient matrix acts directly
on those projective points.  The update keeps precisely the source points
whose image is zero or is again a source point.  This is materially different
from storing complete vector sets and from the RREF/annihilator machinery used
by the earlier controls.

The formula-level check is a second, non-enumerative layer.  It constructs the
dimension quotient over exact rational arithmetic, computes powers by binary
matrix multiplication, and identifies Jordan blocks from nullity growth of
`(Q-lambda I)^r`.  The proof obstruction is also checked directly by the
positive right-eigenvector recursion across every complementary pair.

## Coverage

- Complete literal enumeration for `q=2`, `n=0..4`, through epoch 6.
- Complete literal enumeration for `q=3`, `n=0..3`, through epoch 5.
- Every ambient matrix, every labelled source, every labelled target, the
  ambient lift fibre, the dimension quotient, the diagonal, nestedness, and
  every-time labelled powers are checked in those boxes.
- Exact formula, spectrum, Jordan-nullity, Jordan-obstruction, boundary, and
  absorption checks for
  `q in {2,3,4,5,7,8,9,11}` and `n=0..14` (120 boxes).
- The `n=0` one-block endpoint and the `n>=1` two-eigenvector endpoint are
  separate sentinels.

The largest literal box is `q=2,n=4`: 67 labelled subspaces, 65,536 ambient
endomorphisms, and 4,390,912 source-map updates.  The complete run performs
**9,995,101 assertions**.

## Replay

From this directory, run:

```bash
python3 verify_review_b.py > /tmp/p173_review_b.stdout
cmp CANONICAL.txt /tmp/p173_review_b.stdout
sha256sum -c MANIFEST.sha256
```

A successful run is byte-identical to `CANONICAL.txt` and ends with:

```text
ASSERTIONS=9995101
RESULT=PASS_INTENDED_FORMULAS; MANUSCRIPT_BOUNDARY_AND_SOURCE_GATES_EXTERNAL
```

Passing finite boxes is counterexample pressure only.  It does not replace
the proofs, settle owner subtraction, or authorize external circulation.

## Review disposition

The exact mathematics survived this control, but Hostile Review B records two
Major owner/collision repairs and one Minor proof-wording repair.  In
particular, Van Peski's Theorem 3.3.4 directly supplies a labelled descending
subspace chain through kernels of uniform square maps, and sibling P172 owns
much of the shared fresh-map erosion proof shell.  The precise zero-credit and
non-transfer boundaries are in the paper-local `HOSTILE_REVIEW_B.md`.

Lifecycle remains:

```text
SPIKE_2_COLLISION_RISK / HOLD_EXTERNAL
```
