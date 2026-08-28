# Paper plan — HCS-C220

**Title:** Open TASEP: a finite matrix-Ansatz stationary measure and
all-boundary phase atlas
**Type:** exact stochastic-process theorem with executable audit
**Clock:** physical continuous time; bulk hop rate one
**Scope:** NO_BAD_EULER_OR_ROOT_NUMBER
**Main claim:** one finite-\(L\), all-\(\alpha,\beta\) theorem links the DEHP
algebra, closed \(Z_L\), uniform current, thermodynamic phases, and absorbing
faces, with independent rational nullspace validation.

## Claims and evidence

| claim | evidence | status |
|---|---|---|
| finite generator and unique interior stationary law | exact producer/checker and nullspaces | proved |
| DEHP weights and closed \(Z_L\), including \(\alpha=\beta\) | rewrite recursion and SymPy divided differences | proved |
| \(J_L=Z_{L-1}/Z_L\) and bond-current equality | exact rational rows | proved |
| LD/HD/MC/coexistence/critical atlas (positive-rate coexistence and CRIT_CORNER) | source theorem statement; finite rows are sentinels | analytic theorem, not finite-data inference |
| zero-rate and \(L=0,1\) boundaries | explicit absorbing rows and symbolic controls | proved |

## Structure

1. Motivation and frozen process.
2. Relation to exclusion and matrix-product methods.
3. Generator and DEHP algebra.
4. Finite normalization, current, and exact checks.
5. Thermodynamic phase boundaries and singular faces.
6. Reproducibility, Route-A boundary, and limitations.

The appendix records the independent checker protocol and hostile mutation
families.  The paper contains no target data and no claim that a finite
enumeration establishes the thermodynamic limit.
