# SD-C24 implementation notes

## Sparse construction

The graph constructor factors only `n+1` and returns divisor/quotient pairs.
Simple cycles use a sparse depth-first search rooted at their unique minimum;
rooted traces propagate sparse `(vertex, holonomy)` dictionaries. No
`N^r` Cartesian product is formed.

The confinement theorem puts every period-`r` closed word below `2r-1`, so
the rooted and group-trace ledgers are exact at their stated orders. The
post-freeze atom list is declared only in the artifact generator. It never
appears in `edges_from`, `edge_quotient`, or the transfer matrix constructor.

## Exact conventions

- Matrix columns are sources and rows are targets.
- Directed cycles are identified by rotation, not reflection.
- Temporal primitive roots are separated before rotations are counted.
- Group-algebra coefficients and integer gauge controls use `Fraction`.
- Finite determinants are computed independently by Gaussian elimination and
  by Newton identities from power traces.
- The neutral determinant uses only the coefficient of identity holonomy;
  since that trace vanishes at every positive power, the determinant is one.

## Analytic boundary discipline

The diagnostic prefixes illustrate the separate failure mechanisms
`Re(s)<=1/2` and `Re(s+u)<=1/2`; they do not establish convergence. For the
pure cofactor operator, boundedness is asserted only for the proved control
range `Re(u)>1`. In the intermediate range the ledger says boundedness is
unclaimed and records only the conditional noncompactness theorem.

Nonunitary gauge similarity is checked only entrywise on finite prefixes and
is explicitly not promoted to an infinite-dimensional bounded similarity.
Unitary imaginary-parameter gauges are valid similarities and their finite
determinants agree to the recorded tolerance.

## Reproducibility

All JSON is key-sorted and contains no runtime timestamps. CSV files use LF
line endings. `PYTHONDONTWRITEBYTECODE=1`, `PYTHONHASHSEED=0`, and the disabled
pytest cache keep the artifact tree deterministic. The SHA ledger covers every
Python source and every result file except the ledger itself.
