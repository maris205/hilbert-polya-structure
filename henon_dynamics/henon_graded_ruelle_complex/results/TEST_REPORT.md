# Test report

Command:

```bash
./code/run_c22g.sh
```

Environment:

- Python 3.12.3
- SymPy 1.14.0
- exact rational and symbolic arithmetic

Result:

- producer: pass;
- nonimporting checker: 12/12 checks pass;
- unit and mutation tests: 9/9 pass.

The mutation suite explicitly rejects:

- the reversed mixed-pinning convention;
- unshifted \((-1)^k\) determinant parity;
- reversed synthetic matrix chronology;
- reversed product-contour orientation;
- deletion of a state edge and its two parameter blocks;
- promotion of the conditional quotient to an entire scalar determinant;
- false promotion of image ratios to nuclear order zero; and
- false promotion of the open all-word kernel trace.

No numerical spectrum or cutoff scan was run.
