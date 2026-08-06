# Results

Run

```bash
python ../code/c12c_audit.py --max-period 35 --out-dir .
```

to regenerate:

- `dihedral_counts.csv`: exact-period point, cyclic-orbit, reversor-class,
  chiral-doublet, and coarse dihedral-orbit counts;
- `certificate.json`: period-six normalization certificate, invariant-sector
  projection, and source-table consistency audit.

All computations are exact.  The symbolic portion certifies polynomial
identities over \(\mathbb Z[A,\sigma]\); the counting portion uses integer
arithmetic.  The genus conclusion additionally uses the mathematical fact
that the certified conic parametrization is birational; it is not inferred
from a hard-coded JSON integer.

The counts refer to generic algebraic/complex periodic points, not bounded
real orbits at the Paper-5 fitted parameter.
