# Claims–evidence matrix — P148

**Status: ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL.**

| Statement in the theorem package | Analytic evidence | Exact pressure | Round-2 credit treatment |
|---|---|---|---|
| `E` is a self-map of `PT_{<=N}` but not size preserving | only vertices are deleted; promoted blocks retain order | closure checked for every source through 11 vertices | zero credit: forgetting plane order is exactly Soo--Khoussainov--Linz outward-contraction, Definition 6.6 |
| `E^k` retains original depths divisible by `2^k` | induction with labelled survivors, nearest retained ancestry, and contour order | full labelled skeleton checked for every source and two ranks past absorption | theorem retained as support; cheap unordered all-rank consequence of iterating the direct owner, therefore zero contribution credit |
| `tau(T)=ceil(log2(h(T)+1))` | deepest path realizes every depth; singleton iff `2^k>h` | every state through 11 vertices | cheap unordered clock consequence; zero contribution credit |
| maximum clock `ceil(log2 n)` | `h<=n-1`; path witness | every exact layer and explicit path | cheap extremal consequence; zero contribution credit |
| fibre series `y^I/(1-y)^(2m-1)` | recursive bijection `F_U=A_d product_j F_{U_j}` from reversible ordered nonempty blocks and empty gaps | every target/source-size pair through 11; local factors coefficientwise | **residual:** complete ordered every-target size-refined inverse |
| exact-size image iff `m+I<=n` | nonvanishing criterion for the exact fibre coefficient | exact image sets through 11 | **residual:** exact-layer image criterion |
| `H=z+z^2H/(1-H)` and image series `H/(1-z)` | weighted leaf/internal-root plane-tree specification | coefficients and cumulative image counts through degree 11 | generic specification zero credit; its target-minimum-weight application is the **residual algebraic-series axis** |

The only internally scored claim is the conjunction

```text
ordered every-target size-refined inverse
+ exact-layer image criterion
+ algebraic image series.
```

Hostile Review A: **1 Critical / 0 Major / 2 Minor**.  After the direct-owner
gate was reopened and repaired, Hostile Review B: **0 / 0 / 0, ACCEPT**.
The exact audit reports 216,905 assertions; computation is counterexample
pressure, not proof, novelty evidence, or owner clearance.  External status
remains `HOLD_EXTERNAL`.
