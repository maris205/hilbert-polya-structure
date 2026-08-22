# C67 exact pilot report

The bounded pilot starts from the frozen C64 self-mark matrix and the C66
restricted Smith certificate.  Exact rational inversion (with no floating
point arithmetic) gives the following named-coordinate orders:

```text
coordinate profile:       [36,12,6,6,2,2,36,6,16,8,6,12,2,2,36,36]
transpose profile:        [1,4,2,2,2,2,36,6,16,8,2,4,2,2,2,2]
global denominator:       144
nonzero inverse entries:  43
```

The pilot checks both exact identity products, the denominator minimality
criterion column-by-column and row-by-row, and compatibility with the C66
Smith invariants and determinant.  It is a selection and falsification
artifact only: the producer and the independent checker recompute every
quantity from the bound source bytes.  The independent rational/SymPy path,
clean replay, and 12 hostile mutations are recorded in `results/TEST_REPORT.md`.

The result is restricted to the named 16-type mark map under
`NO_BAD_EULER_OR_ROOT_NUMBER`; no full table-of-marks or arithmetic claim is
made.
