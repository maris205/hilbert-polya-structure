# A4.14 — representative local-complement implementation smoke

Certificate date: 2026-08-06 (UTC)  
Protocol: `R401-VAL-L2-S0`  
Milestone status: **`PASS_IMPLEMENTATION_SMOKE`**  
Final programme status: **null**

## 1. Licensed outcome

Let

\[
B_{\rm loc}=[-0.02,0.02]\times[0.12,0.17]
\times[-0.08,0.08]\times[0.64,0.69]
\]

in reduced coordinates \((Q_-,Q_+,P_-,T)\).  For each of the three frozen
representative parameter slabs `S000`, `S025`, and `S050`, let \(X_i\) be
the exact decimal L1 plan box containing the already certified fast-branch
root.  The accepted R401-VAL-L2-S0 archive proves, independently at 128 and
256 MPFR bits, that every point in the exact eight-shell cover of

\[
 B_{\rm loc}\setminus\operatorname{int}(X_i)
\]

is excluded either by an empty validated energy contraction or by a
displayed necessary-return residual separated from zero.  Together with the
accepted L1 Krawczyk inclusion, this gives exactly one reduced return root in
\(B_{\rm loc}\) for every parameter in each of these three selected slabs.

This is a finite, representative-domain computer-assisted statement.  Its
milestone name remains `PASS_IMPLEMENTATION_SMOKE` because the other 48 L1
slabs were not run under this protocol.  No interpolation from the three
selected slabs is permitted.

## 2. Frozen logical decomposition

For every selected slab, the checker independently reconstructs the eight
standard coordinate shells.  Successively restricting the prefix
coordinates to the protected box gives

\[
 B_{\rm loc}=X_i\cup\bigcup_{k=0}^{3}
   \bigl(C_{i,k,L}\cup C_{i,k,U}\bigr),
\]

with boundary overlap allowed and no gap.  Every nonterminal node is split
at the exact decimal midpoint of the coordinate having greatest width
relative to its frozen parent-domain width.  The fixed coordinate order
breaks ties.  The independent checker reconstructs every root shell, split,
parent--child union, depth, path, and leaf count using exact rational
arithmetic.

A terminal leaf is licensing only in one of two cases.

1. `ENERGY_EXCLUDED`: interval Newton in \(Q_+\) gives an empty intersection
   with a gap strictly exceeding \(10^{-30}\) at 128 bits or \(10^{-60}\)
   at 256 bits.
2. `RETURN_EXCLUDED`: at least one component of the direct, mean-value, or
   preconditioned necessary-return enclosure omits zero by more than the same
   frozen logical margin.

`ROOT_CANDIDATE`, invalid/conflicting output, flow failure, depth exhaustion,
node exhaustion, or any unresolved leaf would have made the run
non-licensing.  None occurred.

## 3. Production result

The producer used 24 workers, a maximum depth of 40, and a per-tree budget of
20,000 evaluated nodes.  CAPD was pinned at commit
`731079217a9254ea2948d742df2b170895effe7f`, whose version file reports
6.1.0, with MPFR/GMP and directed-rounding flags.  The six trees contain
3,016 evaluated nodes in total: 183 terminal energy exclusions, 1,349
terminal return exclusions, and 1,484 internal split nodes.

| Bits | Slab | Parameter interval | Nodes | Max depth | Energy excluded | Return excluded | Root / invalid / unresolved |
|---:|:---:|:---:|---:|---:|---:|---:|:---:|
| 128 | S000 | `[0.0000, 0.0021]` | 486 | 29 | 18 | 229 | 0 / 0 / 0 |
| 128 | S025 | `[0.0499, 0.0521]` | 546 | 35 | 31 | 246 | 0 / 0 / 0 |
| 128 | S050 | `[0.0994, 0.1010]` | 574 | 36 | 44 | 247 | 0 / 0 / 0 |
| 256 | S000 | `[0.0000, 0.0021]` | 436 | 27 | 18 | 204 | 0 / 0 / 0 |
| 256 | S025 | `[0.0499, 0.0521]` | 488 | 31 | 31 | 217 | 0 / 0 / 0 |
| 256 | S050 | `[0.0994, 0.1010]` | 486 | 31 | 41 | 206 | 0 / 0 / 0 |

The adaptive partitions need not agree across precisions.  Both precision
levels nevertheless cover the same exact decimal domains and reach the same
domain-level verdict.  The producer wall time for all six sequential trees
was 8,592.9 seconds; wall time is telemetry and not an acceptance gate.

## 4. Independent replay

The independent checker does not import the producer and does not rerun the
ODE integration.  From the archived outward decimal proof objects it
reconstructs:

- the accepted upstream L1 release and protected-box containments;
- all six exact shell covers and binary tree geometries;
- every printed energy-Newton contraction and empty-intersection gap;
- every displayed direct, mean-value, or preconditioned separating
  component;
- the exact six-pair production matrix, terminal counts, manifest hashes,
  source hashes, and producer/checker authority split.

It completed **89,962 exact-decimal checks with zero failures** and assigned
`PASS_IMPLEMENTATION_SMOKE`.  The producer itself assigned only
`PASS_S0_PRODUCER`; both producer and checker leave `final_status` null.

## 5. Proof objects

The authoritative archive is
`results/r401_val_l2_s0_local_complement/`.  Its principal objects are:

- `summary.json` and `R401_VAL_L2_S0_REPORT.md`;
- `trees/{128,256}/{S000,S025,S050}.json`;
- every raw stdout/stderr transcript under `raw/`;
- `manifest.json`;
- `independent_checker.json` and `INDEPENDENT_CHECKER_REPORT.md`;
- `POSTCHECK_STATUS.json`;
- `RELEASE_PROVENANCE.json`.

The release-bound binary has SHA-256
`b768de84247cd847a3c1b518ec08a7bcfc766e31c20c01bcdd0c75b06d319d53`.
The release provenance binds the exact frozen protocol, source, producer,
checker, contract test, upstream L1 authority, result manifest, and this
certificate.

## 6. Non-promotion boundary

A4.14 does **not** establish any of the following:

- local-complement exclusion on `S001`--`S024` or `S026`--`S049`;
- a phase/flow-box cover or uniqueness modulo time translation on a complete
  energy shell;
- the global shell return-exclusion tree;
- the independent event-projected determinant/Taylor-width cross-check;
- a quantitative analytic trace threshold containing \(\delta=0.01\);
- endogenous periods \(r\log p\), von-Mangoldt weights, an Euler product,
  zeta zeros, a Hilbert--Polya operator, or RH.

The next admissible promotion is a separately reviewed and prospectively
frozen 102-tree all-slab protocol.  The S0 archive may determine that future
run's preregistered resource budget, but no held-out outcome may be used to
tune the proof rules.
