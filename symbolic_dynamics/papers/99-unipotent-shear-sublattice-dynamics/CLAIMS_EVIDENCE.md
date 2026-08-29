# Claims and evidence — P99

| Claim | Analytic evidence | Independent deterministic control |
|---|---|---|
| unique HNF coordinates | projection to the second coordinate, horizontal intersection, residue reduction, and determinant index | enumerates all canonical triples for `1<=N<=120`, checks coordinate range/index, and verifies raw/canonical basis mutual containment; uniqueness itself is analytic |
| exact shear action | images of the two HNF generators under `U` followed by one residue reduction | compares raw sheared-basis canonicalization against the closed action on 11,973 states |
| complete cycle inventory | translation by `c=N/a` on `Z/aZ` has `gcd(a,c)` cycles of length `a/gcd(a,c)` | literal permutation-orbit enumeration for every `1<=N<=120` |
| every fixed count | the time-`n` translation is zero exactly when `a | n(N/a)`, equivalently `h_a | n` | enumerates every HNF phase independently for all `1<=N<=120` and `1<=n<=2N` |
| Möbius temporal recovery | `F_N(n)=sum_{m|n}m C_N(m)` followed by integer Möbius inversion | reconstructs all cycle counts for `1<=m<=N` and `1<=N<=120`, including integrality |
| finite zeta product | a length-`m` permutation cycle contributes `(1-z^m)^(-1)` | cycle/fixed logarithmic identity is checked at 14,520 time-index pairs; six exact zeta-exponent inventories are frozen as regressions |
| state accounting | each divisor layer has `a` phases, hence `sum_{a|N}a=sigma_1(N)` | HNF count and weighted cycle count checked independently at all 120 indices |
| prime-power cycle sparsity | substitute `a=p^j`, `c=p^(r-j)` into the gcd/period formulas | layer formula and closed sparse inventory agree for `p in {2,3,5,7}`, `1<=r<=10` |
| valuation staircase | `p^j | n p^(r-j)` iff `2j<=r+v_p(n)` | 680 valuation/unit cases compare the layer condition with the closed geometric sum |
| rigorous index recovery | the `a=N,c=1` layer is one `N`-cycle; all other periods are at most `a<N` | maximal period `N` and multiplicity one checked for every general and prime-power case |

## Owner-subtracted boundary

- Cohen is cited for the classical Hermite-normal-form setting.
- Grunewald--Segal--Smith are cited for the broader finite-index subgroup and
  subgroup-zeta framework.
- Artin--Mazur are cited for the periodic-point zeta framework.
- The manuscript makes no ownership claim for `sigma_1(N)` subgroup
  enumeration, HNF algorithms, subgroup zeta functions, or Hecke theory.

The residual statement is limited to the explicit fixed-index temporal
ledger for this shear: divisor-layer cycles, fixed/zeta formulas, the
prime-power valuation staircase, and temporal recovery.  A bounded owner
audit is negative evidence only.  External release and priority language
remain **HOLD**.
