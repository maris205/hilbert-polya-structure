# HCS-P66: Boundary cohomology anomaly

P66 proves that marked reflection packet pressure is not invariant under the
usual symbolic cohomology relation. For a continuous transfer function `u`,

```text
A_J(u)=int (u-u∘sigma) d eta_J,
P_J(f+u-u∘sigma)=P_J(f)-A_J(u).
```

The anomaly functional has norm exactly `2`. Explicit radius-`r` cylinders
give `A_J(2u_r-1)=2(1-2^-r)`, approaching the norm. In contrast every finite
periodic orbit sum of a coboundary telescopes to zero, so orbit-averaged
pressure is exactly gauge invariant at every period.

**Status:** boundary anomaly, norm two, and orbit invariance `PROVED`;
uniqueness of uniform cyclic averaging `OPEN`; Route A exploratory; Route B
not authorized. Reproduce with `bash code/run_c66.sh`; see
[`paper/paper.pdf`](paper/paper.pdf).
