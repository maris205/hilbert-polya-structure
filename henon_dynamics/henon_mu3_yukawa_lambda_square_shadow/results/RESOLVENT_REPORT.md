# HCS-C62 G3 resolvent report

Status: `PREFREEZE_G3_PASS`.

All 21 lambda-orbits now have explicit factorized marker carriers. Each
carrier stores every orbit pair and the monic product form

```text
Product_(i,j in orbit) (T - (512*X_i + X_j))
```

with zero-based pair labels and split-prime witness `p=692717`. Every marker
value is below the prime and all values in every orbit are distinct. The
checker verifies the exact orbit totals `51040` and `51360` and refuses any
claim of expanded characteristic-zero coefficients.

This is a marker-resolvent prefreeze result, not yet an arithmetic field
resolvent or release theorem.

