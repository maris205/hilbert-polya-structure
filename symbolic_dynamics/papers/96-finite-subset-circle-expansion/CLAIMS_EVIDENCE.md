# Claims and evidence — P96

| Claim | Analytic evidence | Independent deterministic control |
|---|---|---|
| finite invariant set = unique disjoint union of base cycles | general finite-permutation observation, positively cited to Higuera--Illanes; specialized here to the base circle map | literal cycle decompositions of multiplication by `Q` on `Z/LZ` for five registered `(Q,k)` cases |
| base orbit inventory `O_l(Q)` | `#Fix(m_Q^l)=Q^l-1` and Möbius inversion | observed literal cycle counts equal the Möbius formula at every length in all registered grids |
| binary Euler quotient | each base cycle is independently absent or present once; `(1+u^l)=(1-u^(2l))/(1-u^l)` | truncated integer multiplication of all factors `(1+u^l)^O_l` through degree 9 |
| exact-cardinality formula `E_j(Q)` | coefficient extraction from `(1-Q*u^2)/((1-Q*u)(1+u))` | all `2 <= Q <= 8`, `1 <= j <= 9`; literal grid-cycle selection in five cases; direct enumeration of 189,245 actual grid subsets in three cases |
| parity-split total fixed count | finite sum of `E_j(Q)` and evaluation of `sum_{j=1}^k (-1)^j` | all partial sums for `2 <= Q <= 8`, `1 <= k <= 9`, plus literal cycle and literal subset totals |
| alternating Artin–Mazur zeta factors | substitute `Q=d^n` into the alternating fixed polynomial and sum `sum_n (d^r z)^n/n` | formal factor exponents and logarithmic coefficients checked for `2<=d<=7`, `1<=k<=9`, `1<=n<=15` |
| exact temporal orbit census | least-period decomposition followed by Möbius inversion and division by orbit length | divisibility, nonnegativity, and fixed-count reconstruction for `2 <= d <= 5`, `1 <= k <= 7`, periods through 12 |
| prime-orbit asymptotic | dominant term `d^(k m)`; every proper divisor is at most `m/2` | exact temporal tables provide finite falsification checks; asymptotic proof is analytic |
| entropy `k log d` | standard uniformly finite-to-one application of Bowen’s factor inequality; retained as a control, not residual novelty | fiber bound is combinatorial and independent of periodic enumeration; no numerical entropy estimate is used as proof |
| parameter recovery, including `k=1` | nearest positive pole is `d^(-k)` and nearest positive zero is `d^(-(k-1))` | formal factor probe checks the pole/zero signs, their ratio, and recovery for `2<=d<=7`, `1<=k<=9` |
| multiplicity control on `SP^k(S^1)` | ordinary Euler transform gives coefficient `Q^(k-1)(Q-1)` | separate negative-binomial factor multiplication through degree 9 for `2 <= Q <= 8` |

## Owner-subtracted boundary

- Tuffley owns the topology, homotopy type, induced degree, and related
  finite-subset-space structure for `exp_k(S^1)`.
- Akin–Auslander–Nagar, Higuera–Illanes, and Gómez-Rueda–Illanes–Méndez provide broad qualitative
  induced hyperspace/symmetric-product dynamics; Fernández–Good–Puljiz own
  admissible-period results.
- Tan studies rotational subsets and rotation-number refinements for circle
  multiplication maps.
- Bowen and Kwietniak–Oprocha supply the general entropy background; Rallis,
  Blanco Gómez–Hernández-Corbato–Ruiz del Portal, and Crabb concern
  fixed-index/Lefschetz constructions for symmetric powers and related
  functors.

The residual claim is limited to the circle-multiplication specialization and
rational collapse of binary cycle selection, its exact cardinality and parity
consequences, the resulting Artin–Mazur factorization/temporal census, and
zeta rigidity.  External release and absolute novelty language remain
**HOLD**.
