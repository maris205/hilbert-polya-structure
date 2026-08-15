# HCS-P67: Unique gauge-invariant orbit sampler

P67 proves that uniform cyclic averaging is not merely a convenient repair
of P66's boundary anomaly. On every primitive `n`-cycle it is the **unique**
normalized real linear sampler annihilating all coboundaries. If a normalized
weight vector is nonuniform, a one-site transfer function exposes its gauge
anomaly.

Combining this theorem with P64's orbit equidistribution gives, for every
continuous potential `f`,

```text
P_f(s)=(1/2)log(2)-s int f d mu_B.
```

The finite packet and limiting pressure are exactly cohomology invariant and
Lipschitz in `f`. This is a canonical sparse-packet pressure, not ordinary
topological pressure or an arithmetic trace.

**Status:** sampler uniqueness and universal pressure `PROVED`; arithmetic
trace `OPEN`; Route A exploratory; Route B not authorized. Reproduce with
`bash code/run_c67.sh`; see [`paper/paper.pdf`](paper/paper.pdf).
