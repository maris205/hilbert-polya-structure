# Results

The deterministic evidence SHA-256 is
`c3670de8df2b2171eba51ee5616550601c347c0315ee6867b90be98686328ac5`;
its internal payload SHA-256 is
`1de35607f6ca4219ddccc844ea5cfb3534d920ce757ff56bcedf898b56f9a973`.

| Evidence family | Rows |
|---|---:|
| exact case classifications | 14 |
| physical Ricci-flow cells | 68 |
| constant-volume conjugacy cells | 66 |
| singularity ledgers | 12 |
| near-endpoint asymptotics | 36 |
| permutation/common-scale controls | 14 |
| boundary faces | 8 |
| **total** | **218** |

The cases contain two all-flat families, five full-collapse Einstein families,
and seven partial-collapse families.  Mixed circle/curved products, unique
first clocks, two- and three-factor ties, and dimensions through nine occur in
the frozen grid.

The producer-independent checker passed 2,063 assertions.  It reconstructs
all factor clocks, collapse dimensions, curvature norms, volumes, diameters,
normalized scales, normalized-time quadratures, singular residues, and
covariance controls, exact Ricci and Riemann residues, and all 21 finite
partial-collapse normalized-time tails.  SymPy passed 20 identities.  Fresh
replay reproduced all 159,616 evidence bytes.  The hostile audit rejected
52/52 trials, including 51 repaired-hash semantic changes and one stale-hash
change.  Exact top/nested/row schemas, required lengths, and every major row
family have explicit attacks.

These finite cells are regression evidence and independent reconstruction,
not the proof of the all-real-parameter theorem.  The analytic proof is in
`THEOREM_PACKAGE.md` and `paper/main.tex`.
