# Exact control results — P114

Command:

```bash
python3 code/verify.py
```

Result: `PASS: 400,105 exact assertions`.

The verifier exhausts all rooted-forest parent functions on every subset of
`[n]` for `0<=n<=6`.  The largest lane has 26,830 states.  It checks:

- phase and fixed counts;
- literal termination, endpoint roots, and every depth histogram;
- every endpoint basin and every bounded-height CDF;
- every target's literal one-step predecessor count;
- the `n=0,1` depth-zero boundaries and, for `n>=2`, the sharp maximum and
  `n!` deepest count;
- the global basin-partition identity.

All arithmetic in the EGF route is exact rational arithmetic.  No random
sampling, floating-point fitting, or sequence interpolation is used.
