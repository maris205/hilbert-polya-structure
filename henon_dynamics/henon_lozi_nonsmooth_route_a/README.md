# C116 — Nonsmooth Lozi Route-A pilot

This package freezes the exact rational Lozi map

\[
L(x,y)=\left(1-2|x|+\frac12y,\ x\right),
\]

with symbols `0` for `x<0` and `1` for `x>0`; the switching line `x=0`
is excluded before enumeration.  Every binary word of length one through
eight is solved as an affine return and then checked against every strict sign
inequality.  The rooted admissible counts are

```text
2, 4, 2, 8, 22, 40, 58, 128,
```

and cyclic canonicalization leaves `37` certified primitive necklaces.  The
first pruning occurs at period three, so the preferred parameters
`a=2, b=1/2` were retained.

Separately frozen diagnostic weights `rho_0=1/2`, `rho_1=2/3` define a
240-dimensional direct sum of the 37 certified cycle blocks.  Its traces
reproduce the weighted and unweighted ledger only through power eight.  This
is a finite cycle-atlas prefix, not a global Markov matrix.

```text
A1 = A1_PARTIAL_CERTIFIED
A2 = A2_CERTIFIED_PREFIX
A3 = A3_NOT_ADDRESSED
A4 = A4_FAIL
```

## Reproduce

```bash
python3 code/c116_lozi_producer.py
python3 code/c116_lozi_checker.py
python3 code/c116_sympy_crosscheck.py
python3 code/c116_replay.py
python3 code/c116_mutation.py
python3 code/c116_release_manifest.py
```

The manuscript is [paper/main.pdf](paper/main.pdf), and the exact receipt is
`results/c116_lozi_evidence.json`.
