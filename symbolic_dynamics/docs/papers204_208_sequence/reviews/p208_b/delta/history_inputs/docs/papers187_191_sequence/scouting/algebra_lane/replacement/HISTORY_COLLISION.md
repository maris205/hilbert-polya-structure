# P1--P186 history and permanent-kill firewall

This file records the local history-first screen run before promotion.  The
original trees were read only.  The screen used `rg` over P102--P186 scouting,
phase-1 firewall, owner-gate, and Stage-2 documents, with literal formulas and
mechanism terms rather than carrier names alone.

Representative command families were:

```text
rg -n -i "permanent kill|literal update|state-dependent|power map|stabilizer|gcd erosion|equal cardinality|kernel|coset|standard closure" docs/papers*_sequence --glob '*.md'
rg -n -i "rectangular band|Brandt semigroup|adjacent product|semigroup word" docs/papers*_sequence --glob '*.md'
rg -n -i "subtract.*minimum|minimum positive|distinct positive levels|normalize.*minimum" docs/papers*_sequence --glob '*.md'
rg -n -i "Hurwitz|commuting.*swap|free reduction|integer averaging|consensus" docs/papers*_sequence --glob '*.md'
```

## Exclusions applied before denominator freeze

- The attractive permutation-symmetric update “subtract the current minimum
  positive coordinate” was not admitted.  It is exactly the earlier `CSR`
  composition-subtraction system, already killed with depth equal to the
  number of distinct parts.
- No stabilizer, subgroup-generation, normalizer, gcd/lcm erosion, equal-size
  merge, scalar/matrix/group power map, standard closure, or globally linear
  map with kernel-coset fibres was admitted.
- Nilpotent image/kernel towers, determinant/adjugate feedback, Gram and
  commutator maps, annihilators, Newton--Hensel lifts, state-selected finite
  differences, support pruning, record/prefix feedback, and generic
  canonicalization remained zero-credit mechanisms.

## Frozen source bindings used by the pilot

| source | SHA-256 | role |
|---|---|---|
| `docs/papers187_191_sequence/HISTORICAL_COLLISION_SEED.md` | `19440c86bd1663367f6aba05600a4b137fe9420855bd0c58aeb5dc954b021a3f` | global occupied-surface seed |
| `docs/papers157_161_sequence/scouting/combinatorial/SCOUT.md` | `8e45d2b1d5d0f5dd21904141b9878488972d2d010a5ab62c0f6f7127da00b5fd` | CSR and related permanent kills |
| `docs/papers142_146_sequence/scouting/combinatorial/SCOUT.md` | `4ed0adffbf60751c96772ad3e3908a83820def5418991c783cf0e86419f20e2e` | shift-register and local-relaxation kills |
| `docs/papers177_181_sequence/scouting/algebra_lane/COLLISION_FIREWALL.md` | `a20b5ba9f623bcc844706d2dd7fe10311160e879622d6edca361899431d0293d` | linear/power/valuation exclusions |
| `docs/papers162_166_sequence/scouting/replacement_nonlinear_algebra/SCOUT.md` | `c70e3da15106495e5bda56373b81bf07a8393fff19b12d38a674aaf38b5fa23f` | nonlinear finite-algebra failure modes |
| `docs/papers172_176_sequence/scouting/algebra_arithmetic/SCOUT_AND_KILL_LEDGER.md` | `2a8e024e6f6c8c6029b74387e4634141ed547d13cbfaf85bf50becab60a060a8` | stabilizer and semigroup-adjacent kill history |

`pilot.py` hard-fails if any of these bytes drift.  Their canonical
path/hash aggregate is
`ba0f87f6d97bf8d9c2508a07dbd256b9f25a373fb99a3e24f31de94b876fb458`.

## Candidate-level collision results

| candidate | nearest occupied or permanent-kill mechanism | result |
|---|---|---|
| `R01/BSE` | generic cyclic boundary/support erosion and local compatibility-run transfer | **Partial collision, not a full kill after strengthening.**  The statement “a site survives iff a forward compatible run survives” receives zero credit.  The residual exact package is the parity-dependent Brandt fixed/tail classification plus the all-target gap product and the closed spectrum of the zero-output constraint matrix. |
| `R02/RBW` | P142--P146 shift-register-thin exclusions | Rectangular-band multiplication simply preserves every left coordinate and shifts right coordinates toward the boundary.  The semigroup name does not create a second proof engine. |
| `R03/CSA` | P108 capped Fibonacci addition plus established additive cellular-automaton/Pascal machinery | Replacing a two-register Fibonacci recurrence by a cyclic Pascal convolution is a genuine literal change but not enough separation when the inverse side remains a generic local transfer matrix. |
| `R04/HUR` | standard Hurwitz/braid action; P1--P186 group-action-only kills | It is literally one Hurwitz generator on pairs, hence a permutation with singleton fibres. |
| `R05/CSW` | finite group action/involution-only exclusions | Commutation is merely a gate between identity and coordinate swap; all fibres are one. |
| `R06/MGR` | state-gated finite linear actions, including prior determinant/rank-gated action-only kills | Rank is preserved and only selects identity versus a three-cycle rotation.  There is no transient or inverse axis. |
| `R07/IAV` | classical consensus/averaging plus prior load-balancing exclusions | The sum Lyapunov function gives convergence, but exact depth/basin structure is graph- and rounding-sensitive; no uniform inverse atlas emerged. |
| `R08/PFR` | free-group normal forms and standard terminating rewriting | Parallel scheduling changes the clock only.  Endpoint correctness and reduction fibres remain owned by free reduction/rewrite theory. |
| `R09/RPX` | P125-adjacent product exchange and action-only involutions | Rectangular-band identities make the map an involution immediately; every fibre is singleton. |
| `R10/BPA` | zero propagation/local compatibility pruning | Brandt multiplication turns survival into adjacent index matching; the observed clock is another path-compatibility erosion without a separate inverse theorem. |

## Required mechanism subtraction for R01

The following comparisons concern proof engines, not carrier names.

| occupied paper | occupied engine | R01 subtraction |
|---|---|---|
| P104 | iid products of two real monomial contractions; occupation normal form, tilted two-state transfer, Lyapunov/CLT data | R01 is a deterministic finite cellular map.  It has no random matrix product, singular value, pressure, or additive-functional limit theorem.  Its transfer matrices index adjacent Brandt source letters and count labelled inverse fibres. |
| P105 | simultaneous least-label deletion and predecessor/successor surgery on permutation cycles; longest-cycle depth and threshold-matching reverse fibres | R01 neither changes a permutation carrier nor selects labels globally.  It freezes a matrix unit or replaces it by zero from one local inverse test; the inverse gap product has no ordered-label threshold. |
| P147 | variable-length composition dynamics replacing every maximal equal run `s^r` by `rs`; logarithmic clock and adjacent-divisor-path fibres | R01 preserves the cyclic carrier length, performs no merge, and has linear run erosion.  Its fibres are cyclic local-constraint products, not divisor paths. |
| P159 | deletion of all odd-degree vertices; binary incidence rank, nilpotent transfer powers, graph image layers | R01 has no graph deletion or parity-linear `F_2` inverse.  Its matrix powers are alphabet-level nonnegative constraint matrices, and the decisive spectrum comes from Brandt inversion. |
| P183 | random incoming-star copy on fixed labelled digraphs; conflict deletion, independent-set absorption, support/first-occurrence endpoint kernel | R01 is synchronous and deterministic, with neither random histories nor graph support selection.  Its one-step inverse is a cyclic source-word constraint, not an action-history or endpoint-kernel count. |

This subtraction does **not** make the support-erosion normal form new; that
half remains zero credit.  It explains why the exact semigroup inverse axis is
not mechanically inherited from those five papers.  R01 therefore remains
`PROVISIONAL / OWNER_AMBER / HOLD_EXTERNAL / UNNUMBERED`; all nine other rows
are killed.  Literal nonidentity alone would not have sufficed.
