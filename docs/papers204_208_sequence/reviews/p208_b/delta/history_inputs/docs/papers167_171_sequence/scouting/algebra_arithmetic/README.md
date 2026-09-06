# P167--P171 algebra/arithmetic scouting lane

Status: **one provisional survivor, `QIS = GREEN_OWNER_THIN`; sixteen kills**.

This directory is a scouting hand-off only.  It does not allocate a paper
number and does not assert publication novelty.  The lane tested 17 distinct
literal finite maps after auditing the P1--P166 portfolio and its recent kill
ledgers.  The only system with a closed sharp clock, complete recurrent graph,
and an independent all-time fibre axis is quartic inverse-span dynamics.

## Provisional survivor

For a prime `p`, let `K = F_{p^4}` and let `X_p` be the complete lattice of
`F_p`-linear subspaces of `K`.  Define

```text
J(A) = span_Fp { a^{-1} : a in A, a != 0 },   J(0)=0.
```

The early anomaly is exact:

- at `p=2`, every non-subfield plane goes `plane -> hyperplane -> K`, so the
  sharp maximum tail is two;
- at every odd prime, the same plane goes directly `plane -> K`, so the sharp
  maximum tail is one;
- all recurrent states are zero, `K`, lines, and scalar copies of `F_{p^2}`;
  all periods are one or two;
- the entire functional graph, Artin--Mazur zeta function, and every target's
  `t`-step fibre are explicit.

The caution is substantial: Kolomeec--Bykov already classify the subspaces
whose patched inverse image is a subspace, and earlier finite-geometry papers
describe inverse images of projective lines.  The candidate therefore survives
only as an owner-thin **dynamical synthesis** pending a stricter external
novelty decision.

## Files

- `SCOUT_AND_KILL_LEDGER.md`: 17 literal systems, exact pilot signatures, and
  kill reasons.
- `COLLISION_FIREWALL.md`: internal-system and proof-engine comparison.
- `QIS_DERIVATION_PACKAGE.md`: formulas and theorem spine.
- `QIS_PROOF_PACKAGE.md`: proof decomposition, including the exact external
  classification lemma used.
- `QIS_OWNER_SEARCH.md`: primary-source-only preliminary search and owner
  subtraction.
- `verify_scout.py`, `SCOUT_CANONICAL.txt`: breadth pilot and pinned output.
- `verify_qis.py`, `QIS_CANONICAL.txt`: independent exhaustive verifier and
  pinned output for `p=2,3,5`.

## Replay

From the repository root:

```bash
python3 docs/papers167_171_sequence/scouting/algebra_arithmetic/verify_scout.py
python3 docs/papers167_171_sequence/scouting/algebra_arithmetic/verify_qis.py
```

Both scripts use only the Python standard library.  On the scouting machine
the breadth run took below one second and the independent QIS run took about
four seconds.
