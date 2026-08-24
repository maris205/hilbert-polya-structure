# HCS-C130: irrational-roof suspension Route-A package

This directory is a closed, content-addressed structural certificate for one
frozen mixing suspension.  The base is the full binary shift, the roof values
are `1` and `sqrt(2)`, and the two-state bivariate matrix is

```text
M(u,v) = [[u,v],[u,v]],     det(I-M) = 1-u-v.
```

The one-variable specialization is the entire exponential polynomial

```text
d_tau(s) = 1-exp(-s)-exp(-sqrt(2)*s).
```

The package proves the all-period primitive dynamical Euler/trace identity,
separates clock sectors by the Q-linear independence of `1,sqrt(2)`, and
retains the important limitation that distinct primitive necklaces can share
one symbol-count sector.  The rational-roof control `(1,2)` restores both
cross-sector time collisions and the vertical period `2*pi*i`.

## Reproduce

Run from this directory:

```bash
python3 code/c130_suspension_producer.py
python3 code/c130_suspension_checker.py
python3 code/c130_sympy_crosscheck.py
python3 code/c130_replay.py
python3 code/c130_mutation.py
```

The paper is `paper/main.pdf`.  Exact results, hostile-test coverage, and the
formal theorem are recorded in `results/RESULTS.md`,
`results/HOSTILE_AUDIT.md`, and `THEOREM_PACKAGE.md`.

## Strict boundary

The Route-A tuple is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall
`ROUTE_A_EXPLORATORY`; `route_b_invocation_allowed` is `false`.
The literal scope firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.  “Euler” in this
package always means the intrinsic primitive-orbit product of the frozen
suspension.  No arithmetic Euler factor, root number, target divisor,
automorphy claim, or Hilbert--Polya operator is supplied.
