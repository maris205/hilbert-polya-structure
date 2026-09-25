# Scope card — ASFS-SCOUT-20260914-39

| Field | Frozen state |
| --- | --- |
| Lineage arrow | prime/composite observable -> Eratosthenes sieve -> local symbolic update; direct source-side precursor before any Logistic/Henon/conservative lift |
| Source object | One-dimensional semi-infinite finite-state CA `A=(Q,delta,F)`, with a fixed left boundary cell and all other cells initially quiescent |
| Specific reported realization | Eight states and 301 listed local transition rules, with the fixed `C1` initialization in the cited construction |
| Arithmetic mechanism | Local waves cross out composites; the boundary output is `1` exactly at prime times and `0` otherwise |
| Permitted data | Finite rule table, fixed seed/boundary, ordinary integer time; no prime table, per-prime parameter, von Mangoldt weight, `log p`, or zero data |
| Candidate action | Global synchronous forward CA update on its stated half-line configuration carrier; inverse action not provided |
| Designated arithmetic state | `x_0`, the stated initialized configuration; `x_t=A^t x_0` |
| Clock / packet convention | Time `t` is the tested integer; no closed packet, positive roof, primitive-orbit convention, or repetition law |
| Symplectic base / suspension / zeta / operator | `NOT APPLICABLE` / absent; none may be borrowed from another record |
| A0 screen | Endogenous prime-symbolic generator: positive control only, not a classical P0 admission |
| A1 screen | Designated arithmetic trajectory is provably nonperiodic; complete periodic set of the global CA is `OPEN` and not inferred |
| Candidate state | Pre-P0 frozen screen; stop rather than a classical ASFS candidate |

The card distinguishes the CA's intrinsic fixed program from a reversible
universal simulator (record 011). It does not claim the rule table is canonical
among all prime generators, nor that a generic CA configuration has no periodic
orbit.
