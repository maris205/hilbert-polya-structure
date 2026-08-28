# Control Results

Command:

```text
python3 code/verify_socle_shift.py
```

Recorded release output:

```text
finite-chain-ring socle-product exact controls
q=2 abstract: a=1:(0, 4, 0, 8); a=2:(2, 12, 8, 48); a=3:(0, 32, 0, 256); a=4:(4, 80, 64, 1280); a=5:(0, 192, 0, 6144)
q=3 abstract: a=1:(0, 24, 0, 288); a=2:(6, 108, 216, 3888); a=3:(0, 432, 0, 46656); a=4:(18, 1620, 5832, 524880); a=5:(0, 5832, 0, 5668704)
q=4 abstract: a=1:(0, 72, 0, 2592); a=2:(12, 432, 1728, 62208); a=3:(0, 2304, 0, 1327104); a=4:(48, 11520, 110592, 26542080); a=5:(0, 55296, 0, 509607936)
q=5 abstract: a=1:(0, 160, 0, 12800); a=2:(20, 1200, 8000, 480000); a=3:(0, 8000, 0, 16000000); a=4:(100, 50000, 1000000, 500000000); a=5:(0, 300000, 0, 15000000000)
q=2 concrete: Z/2^r Z and F_2[t]/(t^r), r=2,...,6, layerwise collapse PASS
q=3 concrete: Z/3^r Z and F_3[t]/(t^r), r=2,...,6, layerwise collapse PASS
q=5 concrete: Z/5^r Z and F_5[t]/(t^r), r=2,...,6, layerwise collapse PASS
q=4 concrete: F_4[t]/(t^r), r=2,...,6, valuation boundary PASS
ALL EXACT CONTROLS PASSED: 700,499 assertions
```

## Exact coverage

- **20 abstract systems:** every pair
  `(q,a) in {2,3,4,5} x {1,2,3,4,5}`.
- **Valuation data:** all layer cardinalities, every layer target, the SCC
  involution, and every component's equal Perron square.
- **Linear algebra:** exact rational rank of the valuation quotient and exact
  integer-polynomial expansion of `det(I-zQ)`.
- **Periods:** exact traces through period 10 and exact recovery from periods
  one through four.
- **Dual implementations:** for `p=2,3,5` and lengths `r=2,...,6`, every
  element of `Z/p^r Z` and `F_p[t]/(t^r)` is placed in its valuation layer.
  Every nonzero element is multiplied by a canonical representative of every
  target layer; the resulting product valuation and socle-boundary predicate
  are checked exactly.
- **Nonprime implementation:** `F_4=F_2[u]/(u^2+u+1)` and
  `F_4[t]/(t^r)` are implemented directly for `r=2,...,6`.
- **Collapse:** an explicit layerwise bijection is checked at every vertex in
  each prime-residue dual model, together with the characteristic witness
  proving that the two rings are not isomorphic.

No floating-point arithmetic is used.  The banner `ALL EXACT CONTROLS PASSED`
therefore applies to every assertion made by the program.  The program does
not enumerate every ordered pair in the largest concrete rings; the
all-pairs conclusion is proved by the leading-valuation argument in Lemma 2.1
and guarded computationally by every element against every valuation target.
