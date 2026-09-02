# Open-fresh P165 idea ledger

**Gate:** `GREEN_OWNER_THIN` for one candidate only.  
**External lifecycle:** `HOLD_EXTERNAL`.  
**Search date:** 2026-09-03.

This was a bounded two-candidate scout, not a request to fill a paper number.
The third allowed slot was deliberately left unused once one system crossed
the mathematical gate.  Search non-hits are not novelty evidence, and this
file authorizes neither a novelty claim nor external circulation.

## Pre-admission firewall

The following mechanisms were rejected before receiving candidate IDs and do
not count as extra systems in this ledger:

- Schur squares/powers of linear codes: already a direct-owner and internal
  kill in the P102--P106 and current nonlinear-algebra ledgers.
- Code hulls `C -> C cap C^perp` and `C -> C+C^perp`: repeatedly audited as
  one-step orthogonality retractions.
- Dyck/Motzkin coordinate erosion, parallel peak contraction, and path
  rotation normalizers: respectively collide with P160/P144, rooted-tree
  peeling, or the already killed Vervaat/cycle-lemma lane.
- Hypergraph clique/2-section completion, blocker duality, lower shadows,
  core peeling, and complement-after-closure: closure, involution, shadow, or
  pruning templates already occupied or killed before P165.

## The two admitted literal systems

| ID | carrier and literal update | first exact signal | theorem attack | owner/internal result | decision |
|---|---|---|---|---|---|
| `OF01/PDI` | labelled finite posets; replace `P` by the strict inclusion order of its strict principal downsets | on `n=1..5`, state counts `1,3,19,219,4231`, image counts `1,3,13,75,601`, fixed counts `1,3,13,75,541`, maximum tails `0,0,1,1,2` | inflationary convergence; fixed points are weak orders, hence ordered-Bell census | no direct literal owner located in the bounded search, but the map is a principal-row inclusion completion adjacent to P143; arbitrary-target roots remain a coupled poset-realization problem | **`KILL_NO_INDEPENDENT_TARGET_AXIS`** |
| `OF02/SDS` | `q`-ary linear codes in a fixed ambient space; shorten on the union of supports of all words with weight strictly below twice the current minimum distance | binary maximum depths for `n=0..7` are `0,1,1,2,2,2,2,3`; ternary depths through `n=4` agree; all enumerated images depend exactly on target distance and zero-coordinate count | exact doubling clock; all-time/every-target image criterion; simultaneous minimum-dimension/minimum-support inverse classification and count | low-weight hitting-set shortening is directly owned and receives zero credit; no source found for the literal iteration or the all-time image/extremal inverse conjunction; no literal P1--P164 collision | **`GREEN_OWNER_THIN`** |

## Decision discipline

`PDI` was not rescued by its attractive ordered-Bell fixed census: fixed
points and inflationary termination are the same forward axis, while the
one-step root problem did not factor targetwise.  `SDS` survives only with the
narrow ceiling in [SCOUT.md](SCOUT.md): standard shortening, the fact that
removing all low-weight words raises distance, and generic finite-map
termination receive zero contribution credit.  Its status means “send to an
independent hostile gate,” not “novel,” “publishable,” or “allocated P165.”

The exact evidence is [verify_scout.py](verify_scout.py), frozen in
[CANONICAL.txt](CANONICAL.txt).
