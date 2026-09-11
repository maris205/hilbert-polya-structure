# Carry-normalisation replacement scout

Status: **KILL_INTERNAL_DIRECT_MECHANISM — HOLD_EXTERNAL**.

## Literal system and exact signal

For a radix `b >= 2`, width `n`, and weighted mass `M`, the carrier is

```
C(b,n,M) = {a in N^(n+1) : sum_i b^i a_i = M}.
```

One synchronous step replaces each non-top coordinate by its residue modulo
`b` and carries its quotient one place to the left.  Exact enumeration proves
the following candidate package.

1. The unique fixed point is the truncated base-`b` expansion of `M`.
2. The time-`t` image consists exactly of states whose first
   `min(t,n)` coordinates are below `b`.
3. The one-step fibre above `y` is zero when `y_0 >= b`; otherwise it is
   `(y_n+1) product_{i=1}^{n-1} min(b,y_i+1)`.
4. The maximum transient depth is
   `min(n,floor(log_b M))` for `M>0`, and is zero for `M=0`.

The canonical scout checks all radices `2,3,4`, widths `1,...,5`, and masses
`0,...,40`, plus six larger boundary cases: **99,357 assertions pass**.

## Fatal collision

This is not a fresh paper candidate.  It is the single-tower/fixed-support
coordinate version of the **parallel Glaisher compression** candidate already
developed and killed in the P122--P126 round.  In particular, the earlier
hostile gate already proves the same bulk-parallel quotient/remainder update,
exact image tower, product fibre, and logarithmic clock, and concludes:

- Latapy's *Partitions of an Integer into Powers* (DMTCS, 2001) directly owns
  the identical `b`-ary partition carrier and elementary firing mechanism;
- classical Glaisher/Pathak theory owns the digit-tower decomposition and
  terminal normal form; and
- after those facts and the internal P100/P113/P115 mechanism overlap are
  subtracted, the scheduling residue is below paper scale.

The prior controlling file is
`docs/papers122_126_sequence/phase1/HOSTILE_GATE_PARALLEL_GLAISHER.md`.
Changing from an unbounded finite-support tower to a fixed top coordinate
does not create a new dynamical engine; the top coordinate merely stores the
remaining quotient.

## Decision

**Permanent kill for P157--P161.**  Retain the verifier as a regression and
historical-collision control.  Do not assign a paper number, draft a
manuscript, or claim a novelty non-hit.

