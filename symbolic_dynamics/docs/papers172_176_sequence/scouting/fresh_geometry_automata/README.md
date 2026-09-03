# Fresh finite-geometry / automata discovery lane

**Audit date:** 2026-09-03 UTC  
**Role:** independent second discovery pass for P172--P176; no paper number is
allocated here  
**External lifecycle:** `HOLD_EXTERNAL`

## Outcome

This lane implements **18 genuinely different deterministic finite maps**.
None is stochastic, an incidence-parity linear map, a generic closure or
power, or a pruning process.  Exact complete boxes contribute 1,066,283
assertions.  The run is counterexample pressure and regression evidence, not
an all-parameter proof or a novelty certificate.

Only `D02_MPM`, minimum-pivot Mobius feedback on fixed-size subsets of
`P^1(F_p)`, survives the mathematical two-axis gate.  It has a proved sharp
two-step clock, a complete fixed/2-cycle atlas, and a target-sensitive
pivot-marked inverse polynomial.  It is retained as **one provisional amber
recommendation**, not a paper allocation: its literal rule did not appear in
the bounded primary-source search, but ordinary `PGL(2,p)` subset actions,
fixed Mobius dynamics, and P168 inverse-span dynamics are mandatory
zero-credit neighbours.  A search non-hit provides no novelty evidence.
The P166 `AQN` hostile gate is also deducted: adaptive state normalisation
followed by a classical group action is not itself a contribution.  MPM's
only residual is the exact two-stage containment tower and its nonuniform,
target-sensitive initial interval of admissible pivots; that distinction is
enough to avoid a direct transfer kill, but not enough for green status.

The initially strongest signal, `D01_ORT`, is deliberately killed.  Its
occurrence-rank update is precisely the set-partition-to-tableau construction
of Prasad and Ram, read back as the tableau's columns.  Their Definition 2.1,
Theorem 2.8, and Theorem 3.4 own the image, every-tableau fibre, and an
interlacing-marked fibre.  The residual identity `T^3=T` merely says that the
owned tableau is transposed on re-entry and is not enough for promotion.

## Artifacts

- `SCOUT_AND_KILL_LEDGER.md`: all 18 literal updates, exact pilots, and
  individual decisions.
- `MPM_THEOREM_PACKAGE.md`: all-prime theorem, full graph, every-target
  fibre, marked inverse, and `p=2` boundary.
- `ORT_OWNER_KILL.md`: exact theorem silhouette and direct-owner subtraction.
- `COLLISION_FIREWALL.md`: P1--P171 and within-batch engine comparison.
- `OWNER_SEARCH_LOG.md`: bounded primary-source search and ownership gate.
- `verify_breadth.py`, `CANONICAL.txt`, `REPLAY_LOG.md`: dependency-free
  replay and byte-identity record.
- `MANIFEST.json`, `SHA256SUMS`: machine-readable scope and integrity record.

## Replay

From the workspace root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers172_176_sequence/scouting/fresh_geometry_automata/verify_breadth.py \
  > /tmp/fresh_geometry_automata.txt
cmp -s /tmp/fresh_geometry_automata.txt \
  docs/papers172_176_sequence/scouting/fresh_geometry_automata/CANONICAL.txt
(cd docs/papers172_176_sequence/scouting/fresh_geometry_automata && \
  sha256sum -c SHA256SUMS)
```

The expected transcript terminus is:

```text
SYSTEMS 18
ASSERTIONS 1066283
RESULT PASS
```

No public posting, manuscript upload, author contact, priority statement, or
submission is authorized.
