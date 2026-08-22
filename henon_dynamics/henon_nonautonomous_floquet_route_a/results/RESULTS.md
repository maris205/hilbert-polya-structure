# Results

The exact producer reports 24 primitive admissible necklaces through block
period six, with counts

```text
n=1..6: 3, 0, 2, 4, 6, 9.
```

Transfer trace vectors:

```text
chronological_01  (-4, 74, -184, 2214, -7604, 73538)
reversed_10       (-4, 74,    8, 1702,  4556, 34370)
same_parameter_00 (-2, 38,  202, -986, 10538, -26626)
```

The determinant coefficients (low-to-high powers of `z`) are stored in the
JSON atlas for each control.  The chronological and reversed ledgers differ
on 17 primitive rows.  Every recorded control monodromy has determinant one.

These are exact finite symbolic/modeling results.  They are not a claim that
the candidate map has exactly these real periodic orbits.
