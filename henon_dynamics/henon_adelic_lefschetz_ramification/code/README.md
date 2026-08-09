# Exact first-gate code

Run:

```bash
./code/run_c23.sh
```

The producer constructs the rank-\(2^n\) fixed algebra in the square-free
monomial basis, forms multiplication by the chronological monodromy trace,
and tests the Lefschetz element over degree-good prime fields.  Its modular
rank routine is exact.

The checker does not import the producer. It reconstructs the four decisive
algebras with the same certified quotient presentation, but replaces the
producer's rank routine by SymPy's finite-field `DomainMatrix` backend and
adds direct rational fixed-point enumeration. Independence is claimed for
the rank backend, not for the quotient normal-form design.

No prime is fitted: the release scans every degree-good prime through 43 and
reports all rows. The former broad gate through 251 is cancelled after the
fixed-word tower is identified as a cyclic-resultant baseline. Further work
requires an explicit pre-registered cross-word theorem.
