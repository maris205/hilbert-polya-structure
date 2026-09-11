# P172--P176 algebra/arithmetic independent scout

**Lane decision:** `EMPTY_GREEN_POOL`.  **External state:** `HOLD_EXTERNAL`.

This is a scouting package only.  It allocates no paper number, writes no
paper, and makes no novelty or priority claim.  Twenty literal finite maps
were enumerated.  After conservatively identifying the two obvious
parameter-level pairs (`A02/A19` as subspace squaring in two algebras and
`A07/A11` as cyclic power maps), the package still contains **18 distinct
update classes**.

Three mathematically clean rows received theorem-level pressure tests:

- `A01`, Frobenius meet on the full subspace lattice, has a sharp height,
  fixed-point formula, and every-target/every-time fibre formula, but these
  are the order-dual semilattice orbit-fold and Möbius engines already used
  by P110 and P128.  It is therefore an internal-transfer kill.
- `A03`, derivative--GCD erosion, has an exact characteristic-`p` exponent
  law and factor-degree Euler products for depth and all time-`t` fibres.
  The literal map and essentially this same theorem package already occur in
  the P127, P152, P157, and P162 scouting record, and the primitive belongs to
  square-free decomposition.  It is a hard repeat kill.
- `A16`, commutation with a fixed transposition, has a complete functional
  graph and a fixed-point-marked conjugator-fibre polynomial by
  support-overlap type.  Its update and uniform fibres are nevertheless the
  fixed-element commutator/centralizer-coset engine occupied by P119; Brandl
  and Fulman also make the external owner neighbourhood dense.  The new mark
  is too elementary to constitute a nontransferable second axis.

Thus the lane recommends **no candidate** for one of P172--P176.  The formulas
are retained as negative controls so later rounds do not rediscover them.

## Files

- `SCOUT_AND_KILL_LEDGER.md`: all 20 literal maps, early signals, inverse axes,
  and kill decisions.
- `PRESSURE_TESTS.md`: conjecture-to-proof pressure for `A01`, `A03`, and
  `A16`, including boundary checks and the P142/P119 comparisons.
- `OWNER_SEARCH_LOG.md`: bounded primary-source and internal-owner audit.
- `scout_algebra_arithmetic.py`: dependency-free exact enumerator.
- `CANONICAL.txt`: pinned deterministic transcript.
- `SHA256SUMS`: integrity manifest for this package.

## Replay

From the workspace root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers172_176_sequence/scouting/algebra_arithmetic/scout_algebra_arithmetic.py
PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers172_176_sequence/scouting/algebra_arithmetic/scout_algebra_arithmetic.py \
  | cmp -s - \
  docs/papers172_176_sequence/scouting/algebra_arithmetic/CANONICAL.txt
```

The expected terminus is `ASSERTIONS=419496` followed by `RESULT=PASS`.
The enumerated boxes are falsification controls, not proofs; the proofs of the
three pressure-tested statements are recorded separately.
