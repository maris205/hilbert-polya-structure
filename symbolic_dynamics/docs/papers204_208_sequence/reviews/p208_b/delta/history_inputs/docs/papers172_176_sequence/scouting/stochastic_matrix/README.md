# Stochastic/matrix breadth lane for P172--P176

**Audit date:** 2026-09-03 UTC  
**Scope:** discovery evidence only; no paper number is allocated here  
**External lifecycle:** `HOLD_EXTERNAL`

## Outcome

The executable contains 23 exact pilots.  Five are deliberately retained
entry-firewall controls that reproduce already occupied literals and therefore
add zero to the batch count:

```text
M01 = historical RRO rank-one addition
H01 = historical RCR random-colour refinement
R01 = P143 row-inclusion residual
C01 = historical Schur-square code closure
C02 = historical R05 field-Gram feedback
```

After those deductions, this lane contributes **18 fresh literal systems**.
They received 31,397 exact candidate-specific assertions.  The complete
23-row executable makes 129,620 assertions, including the duplicate sentinels
and three global integrity checks.  A correct finite run is counterexample
pressure, not an all-parameter proof or a novelty certificate.

The strongest residual signal is `S01`, fresh-map self-image erosion.  Its
highest two subset sizes have the same diagonal eigenvalue and a forced
off-diagonal coupling, producing a genuine Jordan block for every `n>=2`.
`G05`, the quotient-leakage subspace chain, has a larger complementary-
dimension Jordan ladder and remains a theorem-spike candidate under heavy
finite-field-rank and internal-subspace subtraction.  `A01`, parity
pushforward under a fresh map, is a clean but owner-dense reserve.  None is a
paper recommendation without the owner and collision gates in this directory.

## Reproduce

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 docs/papers172_176_sequence/scouting/stochastic_matrix/verify_breadth.py \
  > /tmp/stochastic_matrix.json
cmp -s /tmp/stochastic_matrix.json \
  docs/papers172_176_sequence/scouting/stochastic_matrix/CANONICAL.json
(cd docs/papers172_176_sequence/scouting/stochastic_matrix && \
  sha256sum -c SHA256SUMS)
```

The verifier uses only the Python standard library and emits sorted,
deterministic JSON.  The expected canonical SHA-256 is
`fa39710708dadbeb2614b64da5ef87f158081e03a782c08164eb230ac174db8c`.

## Artifact map

- `SCOUT_AND_KILL_LEDGER.md` gives every literal update, exact pilot, and
  survive/kill decision.
- `COLLISION_FIREWALL.md` records the P1--P171 entry deductions and residual
  pairwise comparisons.
- `S01_THEOREM_PACKAGE.md`, `G05_THEOREM_PACKAGE.md`, and
  `A01_THEOREM_PACKAGE.md` state the three deepest theorem contracts,
  boundaries, proof routes, and stop conditions.
- `OWNER_SEARCH_LOG.md` assigns zero credit to direct and generic owners and
  records bounded searches without turning non-hits into novelty.
- `REPLAY_LOG.md`, `CANONICAL.json`, and `SHA256SUMS` provide the replay and
  integrity trail.

No public posting, manuscript upload, author contact, priority statement, or
submission is authorized.
