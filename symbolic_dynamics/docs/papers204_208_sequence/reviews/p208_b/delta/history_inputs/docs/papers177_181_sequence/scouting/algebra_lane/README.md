# P177--P181 algebra lane

**Final lane status:** `SCOUT_COMPLETE / ONE_PROMOTE / ONE_RESERVE /
HOLD_EXTERNAL`.

This directory is an independent breadth search over deterministic finite
algebraic, finite-field, matrix, and arithmetic systems.  It does not allocate
a paper number and does not modify any paper directory.

## Result

After reading the P1--P176 title inventory and the two preceding collision
packages, the lane tested eleven raw literal maps.  Two were exact historical
rediscoveries and are retained only as firewall sentinels.  The valid breadth
count is therefore **nine fresh systems**:

- `C01/SFD` is the sole recommendation;
- `C02/SST` is a theorem-level reserve, downgraded for P166 proof-engine
  transfer and direct matrix-cycle-index ownership;
- seven fresh candidates are killed; and
- `C04/VTM` and `C06/PCM` are excluded rediscovery controls.

The recommended literal is

\[
T_p(f)(x)=f(x+f(0))-f(x)
\quad\text{on all }f:\mathbb F_p\to\mathbb F_p.
\]

It has sharp height \(p\), image tower
\(\operatorname {im}T_p^t=(\tau-1)^tV_p\), an exact fibre for every target
and every time, explicit depth shells, and a complete transition Jordan
inventory with exactly \(p-1\) blocks \(J_p(0)\).  Classical
finite-difference and augmentation-ideal algebra are explicitly subtracted;
the residual is the current-state direction word and its unique anchored
reverse lift.

## Files

- [`SCOUT_AND_KILL_LEDGER.md`](SCOUT_AND_KILL_LEDGER.md): all raw and fresh
  candidates, exact signals, and decisions.
- [`COLLISION_FIREWALL.md`](COLLISION_FIREWALL.md): P1--P176 mechanism
  subtraction and the two exact rediscoveries.
- [`THEOREM_SPIKES.md`](THEOREM_SPIKES.md): rigorous SFD proof and the
  downgraded SST theorem package.
- [`OWNER_SEARCH_LOG.md`](OWNER_SEARCH_LOG.md): bounded primary-source owner
  audit with explicit nonhit semantics.
- [`verify_algebra_lane.py`](verify_algebra_lane.py): independent exact
  verifier.
- [`CANONICAL.txt`](CANONICAL.txt): frozen verifier transcript.
- [`SELF_CHECK.md`](SELF_CHECK.md): final mathematical and artifact audit.
- [`MANIFEST.json`](MANIFEST.json) and [`SHA256SUMS`](SHA256SUMS): inventory
  and byte hashes.

## Reproduce

```bash
cd /root/autodl-tmp/symbolic_dynamics/docs/papers177_181_sequence/scouting/algebra_lane
PYTHONDONTWRITEBYTECODE=1 python3 verify_algebra_lane.py
cmp -s CANONICAL.txt <(PYTHONDONTWRITEBYTECODE=1 python3 verify_algebra_lane.py)
sha256sum -c SHA256SUMS
```

The canonical run reports:

```text
TRANSITION_DIGEST=30db71534328fcb0a43b8d0a2ce7acda3fc271808e057b851a5c5adfa6038cc9
TRANSITIONS=900976
FRESH_TRANSITIONS=884933
RAW_BOXES=104
FRESH_BOXES=92
ASSERTIONS=1375295
RAW_CANDIDATES=11
FRESH_CANDIDATES=9
REDISCOVERY_SENTINELS=2
RESULT=PASS
```

All source nonhits remain `OWNER_THIN`.  Nothing here authorizes external
posting, circulation, or submission.
