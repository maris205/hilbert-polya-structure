# Results

The canonical evidence has SHA-256 `750f10061bb31b956d1745cb52f24f5eefb15e41e462ddb441cb95fadc407a71` and self-excluding payload SHA-256 `54155768c4b983d5de2c66b042d481b86135aecc6c7506ee100e6aa6b79127d7`.

- analytic range: every `n>=3`;
- exact finite image: `H_n={(a,b):(-1)^b=(2/a)}`, order `2^(2n-2)`;
- adjacent restriction: surjective with kernel order four;
- nonzero fixed-root counts: `2`, `2^k` for `3<=k<n`, and `2^n`; never `1` or `4`;
- root-prime density: `7/24+1/(3*4^(n-1))`, limit `7/24`;
- finite receipts: 5,592,400 group elements and 95,910 prime--level cells.
- A0 controls: basepoint 3 has trivial intersection/full affine image; the
  11,184,800-pair full-affine ledger restores four fixed roots;
  five prime powers retain `Frob_p^r` repetition ownership while twenty
  mixed composites have no single-prime owner; empirical density earns no
  A0 credit.
- strict Route-A result: `A1_WEAK`, `A4_FORMAL_HINT`, overall
  `ROUTE_A_EXPLORATORY`.

The finite receipts validate implementations.  The proof in `proof/ANALYTIC_PROOF.md` establishes the all-level statements.
