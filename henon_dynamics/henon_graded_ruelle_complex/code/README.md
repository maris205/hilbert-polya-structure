# Reproducibility code

Run the exact certificate, nonimporting checker, and mutation tests with:

```bash
./code/run_c22g.sh
```

`c22g_producer.py` uses exact rational and symbolic arithmetic.  The checker
does not import the producer. The test suite mutates the pinning convention,
product orientation, supertrace parity, chronological product, graph,
nuclearity status, all-word trace status, and determinant scope and requires
each mutation to be rejected. The certificate explicitly marks the
functional-analytic gates open. No finite-section spectrum, random sample,
target zero, prime table, or transition-matrix average is used.
