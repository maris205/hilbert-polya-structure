# Root cross-class scout — P152–P156

**External status:** `HOLD_EXTERNAL`.  This ledger is exploratory.  Exact
computation is counterexample pressure, not proof or ownership clearance.

## Intake ledger

| id | literal system | early signal | disposition |
|---|---|---|---|
| R01 | binary parity-match sieve: retain `w_i` iff `w_i=i (mod 2)` and reindex | unique alternating fixed word in every length; apparent sharp clock `floor(log2 n)+1`; exact one-step fibres; binomial terminal layers | **KILL / owner-heavy negative control**: Piergallini's alternating erasing substitution is a close direct positional-parity erasure owner, and the proof mechanism is too close to excluded parity/run word systems |
| R02 | erase all fixed points of a permutation and standardize | exact idempotence: simultaneous erasure never creates a new fixed point | **KILL**: one-step closure, below paper threshold |
| R03 | retain both local maxima and minima of a permutation, endpoints included | fast contraction and alternating terminals | **KILL**: literal/mechanism collision with P149 endpoint-peak extraction |
| R04 | delete the largest label of every permutation cycle and standardize | clock is maximum cycle length; cycle-size fibres are explicit | **KILL**: transfers from P105 cycle-minimum pruning plus classical restriction consistency |
| R05 | repeatedly quotient graph vertices with identical closed-neighbourhood rows | bounded stabilization and reconstructible blow-ups | **KILL**: generic partition refinement/closure; too close to P135 and P143 |
| R06 | peel convex-hull layers from a finite planar configuration | depth layers and endpoint core | **KILL**: classical onion decomposition restated dynamically; no independent inverse theorem |
| R07 | iterate graph line construction | many exact census recurrences on regular graphs | **KILL**: construction-driven generic graph iteration and owner saturation |
| R08 | characteristic-two polynomial map `x -> x^2+x` | trace-controlled image and linearized tails | **KILL**: generic Frobenius-linear dynamics, explicitly excluded |
| R09 | strip repeated polynomial factors by `f -> f/gcd(f,f')` | exact squarefree endpoint | **KILL**: idempotent classical algorithm |
| R10 | simultaneous top-trading-cycle deletion in a preference profile | finite round clock and terminal unmatched set | **KILL**: classical algorithm dynamically relabelled; inverse profile is not clean |
| R11 | synchronous dominated-row/column peeling of a rook board | core depth and fixed boards | **KILL**: generic core pruning and occupied relation/subspace proof mechanism |
| R12 | normalize cyclic integer gaps by their gcd after differencing | arithmetic contraction | **KILL**: collision with translation–GCD P128 and Euclidean queues P131 |
| R13 | iterate hypergraph blocker after clutter reduction | period two after normalization | **KILL**: static duality/involution, below progress threshold |

The root lane therefore contributes **no finalist**.  This is an admissible
breadth outcome: the three independent specialist lanes, not a quota per lane,
must furnish the five pairwise separated survivors.

## R01 exact profile retained as a negative control

For a binary word `w=w_1...w_n`, use one-based indexing and put

\[
 T(w)=(w_i: w_i=1\text{ for odd }i,\; w_i=0\text{ for even }i).
\]

The fixed words are exactly `1010...` (including the empty word).  If a target
`u=u_1...u_m` is prescribed, each preimage is uniquely specified by an
increasing index sequence whose parities are `u_1,...,u_m`; every selected bit
is forced to match its position and every unselected bit is forced to mismatch.
Consequently the one-step fibre is counted by the exact recurrence

\[
 F_i(j)=F_{i-1}(j)+[i\bmod2=u_j]F_{i-1}(j-1),\qquad F_0(0)=1.
\]

The smallest source length reaching `u` is found greedily by choosing the
smallest increasing positions with the required parities.  Exhaustive data
through length 18 support

\[
 \max_{|w|=n}\tau(w)=\lfloor\log_2 n\rfloor+1,
 \qquad
 \#\{w: |w|=n,\ |T^\infty(w)|=m\}
   ={n\choose\lfloor(n-m)/2\rfloor}.
\]

These observations are deliberately **not** promoted.  The closest retrieved
owner is Riccardo Piergallini, *The simplest erasing substitution*, whose map
deletes one symbol and replaces retained symbols according to the parity of
their original positions, proves logarithmic finite-word vanishing bounds, and
develops sections/fibres.  R01 is not asserted identical to that map, but the
carrier, parity-erasure mechanism, clock engine, and inverse surface are too
close for this portfolio.

Primary-source retrieval:

- Riccardo Piergallini, *The simplest erasing substitution*, author-hosted PDF,
  <https://mat.unicam.it/piergallini/home/papers/erasingmap.pdf>.

## R02 structural negative theorem

Let `D(pi)` delete every fixed entry `pi(i)=i` and standardize the remaining
permutation.  If a surviving entry at old position `i` and old value `pi(i)`
became fixed, the counts of deleted diagonal points before `i` and before
`pi(i)` would have to differ by `i-pi(i)`.  This is impossible because the
surviving endpoint of the intervening interval is not deleted.  Thus `D^2=D`.
The exact theorem is clean, but it is only a one-step closure and is therefore
kept as a threshold calibration, not a paper candidate.

## Replay

`verify_root_scout.py` exhausts R01 through length 18, independently compares
enumerated and recurrence fibres through length 11, and exhausts R02 through
permutation size 10.  `CANONICAL.txt` is the frozen transcript.

