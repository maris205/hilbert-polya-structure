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
| Full all-`N` / arbitrary-twist trace regime | **`[OPEN]`** — no uniform energy-window theorem frozen |
| Full all-`N` / arbitrary-twist orbit ownership | **`[OPEN]` / `NOT_ESTABLISHED`** |
| Round-3 subtype | **`[MODELING_CHOICE]` / FROZEN** — source-compatible square root, even `N=2m` |
| Round-3 operator/window | **SOURCE BOUND** — `sqrt(Delta^(L^N)+N^2/4)`, center `(sqrt(5)/2)N`, `O(1)` transformed window |
| Round-3 classical shell | **`[PROVED]`** — principal Hamiltonian `sqrt(|p|^2+1/4)` at the frozen center gives `|p|=1` |
| Round-3 clock map | **`[PROVED]`** — `T_trace=(sqrt(5)/2)T_physical`; the physical clock remains unit speed |
| Round-3 source/project flow map | **`[PROVED]`** — `q=2p`, pullback `omega_source=2 omega_project`, pullback `H_source=2 H_project` |
| Round-3 signed-field orbit ownership | **`[PROVED]` under frozen subtype** — source Theorem 3 for `+1/2`; antiunitary dual for `-1/2` |
| Full all-`N` / arbitrary-twist ownership | **`[OPEN]` / `NOT_ESTABLISHED`** |
| Round-3 contract validation | **PASS / REPRODUCIBLE** — 12 rows, 8/8 tests, two byte-identical runs, tree SHA-256 `a28bf68d0da5c34350224031428f18f325af0d11619df95f2509741475275f3d` |
| Round-4 Bolza group lock | **SOURCE LOCKED / REPLAY PASS** — four published opposite-side-pairing generators, exact polygon relator, 120-decimal residual `1.534e-117` |
| Round-4 primitive seed | **`[PROVED]` under frozen subtype** — four systolic inverse-paired primitive axis owners per field; `f_j` and `f_j^-1` remain nonconjugate facts but receive one axis-owner ID in this schema |
| Round-4 signed-`k` ledger | **EXECUTED / REPRODUCIBLE** — equation-(19) branches `k=+-1,+-2,+-3`; 24 branches per field, 48 rows total, zero orientation owner credit, 12/12 tests, two byte-identical builds, tree SHA-256 `b2387be3d4acc6485cd7f0e2d89eeaae9a36dace1ddf2d451d7f51ed3680bfd4` |
| Round-4 completeness | **INCOMPLETE BY DESIGN** — four explicit side-pairing primitives only; not a complete Bolza primitive or systolic spectrum |
| Round-4 arithmetic labels | **NONE** — no target data and no rational-prime/prime-ideal assignment |
| Fixed degree-one candidate | `Δ^L` tracked separately; `FIXED_OPERATOR_HIGH_ENERGY_TRACE=OPEN` |
| Fixed-candidate orbit ownership | `FIXED_OPERATOR_MAGNETIC_ORBIT_OWNERSHIP=NOT_ESTABLISHED` |
| Bold hypothesis | **`[HEURISTIC]`** — arithmetic-specific phase cancellation |
| First controls | **FROZEN DESIGN** — degree `0,+1,-1`, dual-bundle field reversal, and non-arithmetic metric |
| Round-2 owner lemma | **`[PROVED]`** — changing bundles, duality, antiunitary reversal, domain, repetition, and no fixed-owner credit transfer |
| Round-2 owner ledger | **EXECUTED / REPLAY PASS** — 12 rows, `N=1,2,4,8`, 7/7 tests |
| Magnetic-orbit ledger | **FIRST SEED EXECUTED** — inverse-paired axis owners and theorem-derived signed-`k` period/action/stability branches; no trajectory integration or complete spectrum |
| Evidence tokens | `[PROVED]|[HEURISTIC]|[MODELING_CHOICE]|[OPEN]` |
| Proposal stage | Stage 1 / Route A A0--A1 |
| Formal Route-A tuple | UNASSIGNED |
| Route-B evaluation | NOT RUN |
| Route-B invocation allowed | `false` |
| Manuscript | NOT STARTED |

Next gate: extend the four-axis-owner-per-field seed to a source-locked bounded-length
conjugacy census with a certified normal-form/completeness rule, then instantiate
the matched non-arithmetic metric.  This progress applies only to the frozen
signed-field even subsequence; zero field, odd `N`, full all-`N`, arbitrary
twists, and fixed `Delta^L` remain open or `NOT_ESTABLISHED`.  The formal
Route-A tuple remains unassigned and Route B remains disallowed.
