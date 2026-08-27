# P28 pipeline state

Date: **2026-08-27**

| Item | Status |
|---|---|
| ARS Stage 1 | **IN PROGRESS** |
| Continuous-time object | **FROZEN** — unit-speed Bolza magnetic flow at `b=1/2` |
| Flux / base-bundle degrees | **`[PROVED]`** — `b=0,+1/2,-1/2` maps to `0,+1,-1`; negative field uses `L^*` |
| Global magnetic potential | **`[PROVED]`** — nonzero flux implies nonexact field |
| Phase owner | **`[PROVED]` / FROZEN** — line-bundle holonomy modulo `2 pi` |
| Semiclassical family | **FROZEN / NO ROUTE CREDIT** — `H_N=Δ^{L^N}` on `L²(Σ_B,L^N)`, `N→∞` |
| Operator dependence | **`[PROVED]`** — operator and Hilbert space change with `N` |
| Semiclassical trace regime | **`[OPEN]`** — energy-window scaling and trace distribution not yet frozen |
| Semiclassical orbit ownership | **`[OPEN]` / `NOT_ESTABLISHED`** — no same-owner trace claim |
| Fixed degree-one candidate | `Δ^L` tracked separately; `FIXED_OPERATOR_HIGH_ENERGY_TRACE=OPEN` |
| Fixed-candidate orbit ownership | `FIXED_OPERATOR_MAGNETIC_ORBIT_OWNERSHIP=NOT_ESTABLISHED` |
| Bold hypothesis | **`[HEURISTIC]`** — arithmetic-specific phase cancellation |
| First controls | **FROZEN DESIGN** — degree `0,+1,-1`, dual-bundle field reversal, and non-arithmetic metric |
| Round-2 owner lemma | **`[PROVED]`** — changing bundles, duality, antiunitary reversal, domain, repetition, and no fixed-owner credit transfer |
| Round-2 owner ledger | **EXECUTED / REPLAY PASS** — 12 rows, `N=1,2,4,8`, 7/7 tests |
| Magnetic-orbit ledger | **NOT RUN** — owner ledger contains no orbit or spectrum data |
| Evidence tokens | `[PROVED]|[HEURISTIC]|[MODELING_CHOICE]|[OPEN]` |
| Proposal stage | Stage 1 / Route A A0--A1 |
| Formal Route-A tuple | UNASSIGNED |
| Route-B evaluation | NOT RUN |
| Route-B invocation allowed | `false` |
| Manuscript | NOT STARTED |

Next gate: source-bind one exact rescaled operator, energy-window convention,
and trace distribution before enumerating any magnetic orbit. The completed
owner lemma does not promote either semiclassical or fixed-operator
magnetic-orbit ownership beyond `[OPEN]`; its exact pipeline state remains
`NOT_ESTABLISHED`.
