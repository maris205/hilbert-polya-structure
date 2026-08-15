# HCS-P68: Canonical reflection-packet Euler product

P68 promotes P67's unique gauge-invariant cyclic sampler to the explicit
packet product

```text
Z_f(z,s)=product_(n odd)(1-z^n exp(-s n b_n(f)))^(-D_n).
```

Its logarithmic derivative has an exact primitive/repetition divisor ledger.
At `s=0` the radius is `2^(-1/2)`, and near the positive boundary

```text
log Z_0(z)=1/[sqrt(2)(1-sqrt(2)z)]+analytic.
```

Therefore `Z_0` has an exponential essential singularity. The construction
is a canonical analytic germ, but it is neither the full `D_infinity` Lind
zeta nor a meromorphic Fredholm determinant at the entropy boundary. It also
retains periodwise means rather than individual orbit-weight distributions.

**Status:** Euler product, repetition law, radius, and boundary type
`PROVED`; arithmetic trace `OPEN`; Route A exploratory; Route B not
authorized. Reproduce with `bash code/run_c68.sh`; see
[`paper/paper.pdf`](paper/paper.pdf).
