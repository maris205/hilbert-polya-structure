# SD-C23 exact experiment plan

## Frozen purpose

The experiment suite certifies the finite consequences of the successor-divisor graph rule

\[
n\longrightarrow d \quad\Longleftrightarrow\quad d\ge 2\text{ and }d\mid n+1,
\]

without using prime tables, target zeros, or fitted edge predicates. Infinite statements such as the sharp trace-class half-plane remain analytic theorems; the computations are exact regression certificates.

## Authority cutoffs

| ID | Certificate | Frozen scope |
|---|---|---:|
| E1 | Source edge and quotient-identity audit | sources through 4096 |
| E2 | Canonical cycle family | lengths through 2048 |
| E3 | Explicit quotient-family cycles | $2\le d,q\le16$ |
| E4 | Sparse unweighted traces and necklace inversion | $1\le r\le32$ |
| E5 | Exact cutoff flags | $N=7,15,31,63$ at every $r\le32$ |
| E6 | Exact weighted traces | $s=1,2,3$ and $r\le16$ |
| E7 | Newton versus primitive-product determinant coefficients | degree at most 16 |
| E8 | Full, spine, successor, and blacklist graph controls | 20 rows |
| E9 | Positive weight-inventory controls | 64 rows |
| E10 | Trace-class prefix diagnostics | 8 exponents and 7 cutoffs |
| E11 | Source/target firewall and AST audit | all authority code |
| E12 | Full regeneration and byte-determinism | two complete runs |

The current authority handoff freezes traces through order 32. A larger informal aspiration elsewhere is not part of this execution and is not used in any claim.

## Acceptance gates

All exact cutoff flags must agree with the theorem $N\ge2r-1$; every necklace reconstruction must match its rooted trace; the two determinant constructions must agree coefficientwise; the $q=\{1,2\}$ spine must retain cycles of every length $2$ through $32$; the successor-only graph must remain acyclic; all Route-A fields must pass the strict schema; and both complete runs must yield the same result-ledger SHA-256.

## Interpretation lock

Passing the suite confirms a genuine whole-operator Fredholm ledger on $\Re s>1/2$. It does not repair the degree-one mismatch with the marked prime Euler product, the all-length primitive-cycle flood, or the composite-square orbit norms. Route B remains locked.
