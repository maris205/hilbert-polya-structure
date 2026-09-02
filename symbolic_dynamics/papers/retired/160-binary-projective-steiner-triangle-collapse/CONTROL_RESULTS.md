# Exact control results — P160 Round 0

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p160.py
```

The frozen transcript records 4,836,144 passing assertions.  The verifier:

- enumerates all ordered triples for ranks 2 through 6;
- checks closure and every literal edge;
- checks the four classes, exact depth and period, and aggregate counts;
- checks every target indegree;
- independently compares every block's actual source set with
  `(t,t+z,t+y)` for all allowed `t`;
- checks fixed points of iterates 1 through 7;
- checks coordinate and linear equivariance generators, literal weak
  components, the first five fibre moments, the exact fibre histogram, and
  rank recovery; and
- freezes a short hash of each complete edge table.

No random sampling, floating point, third-party package, or network access is
used.  Enumeration proves no all-rank or ownership statement.
