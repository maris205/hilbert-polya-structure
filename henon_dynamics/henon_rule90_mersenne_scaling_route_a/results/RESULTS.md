# C150 results

- All-scale theorem: for every `r>=1`, `L=2^r-1` gives `a^(L+1)=a`.
- Kernel/image dimensions: `1` and `L-1`.
- Dynamics: every state enters the image in one update; periodic set equals
  image; exactly half of all states are periodic; every period divides `L`.
- Counts: exact polynomial-gcd fixed formula and Möbius-resolved primitive
  cycles.
- Replay: `r=1..8`, 8 family rows and 27 divisor-period cells.
- Negative control: `L=2^s`, `s=1..8`, nilpotent with only zero periodic.
- Independent checker: 153 assertions; SymPy: 276 exact checks.
- Mutation audit: 44 repaired-hash plus one stale-hash rejection.

Evidence SHA-256: `8ea85c5644c028c23c0dc004d4674e98c760c86554c8ce124fd18d88ee0bee06`.
