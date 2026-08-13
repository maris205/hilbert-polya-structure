# Paper 06 Experiment Plan

## Frozen objective

Test whether the unique minimal tensor atom F₂, equipped with its canonical
maximal-entropy Parry kernel K₂ = J₂/2, supplies a source-internal
Archimedean sector while preserving the complete SD-C07 prime-power trace
ledger. The primary and only system family is Symbolic Dynamics. No
Riemann-zero data are allowed.

The candidate evaluated after the gates pass is SD-C08:

```text
SD-C07 tensor-atom base
+ canonical minimal F2 Parry Markov fiber
+ Hellinger half-density
+ sign-additive tilted cyclic trace
```

## Claims and falsifiers

### E1 — stationary ledger

For K₂ = J₂/2 and A_s = direct-sum_p p^(-s) K₂, verify

```text
K₂^r = K₂,
tr K₂^r = 1,
det(I₂ - p^(-s) K₂) = 1 - p^(-s).
```

Falsifier: any power-trace or determinant-block failure beyond binary64
roundoff. Compare with uniform K₃ and K₄, biased rank-one K₂, and a
reversible kernel with nonzero second eigenvalue.

### E2 — same tilted cyclic trace

The code uses the cyclic representative

```text
H_cyc(u) = K₂ diag(exp(-iu), exp(iu)).
```

Verify on the frozen grid that tr H_cyc(u)^N = cos(u)^N. At u = 0 this is
the stationary ledger; at u = t/sqrt(N) it is the exact characteristic
function of the standardized binary sign Birkhoff sum.

The manuscript uses the symmetric representative

```text
H_sym(z) = exp(zQ/2) K₂ exp(zQ/2),  Q = diag(-1,1).
```

After the convention z = iu, H_sym and H_cyc are cyclic/similar
representatives with identical power traces and characteristic
determinants. They are not two different candidate objects.

### E3 — binary Archimedean limit

For odd N in {31,127,511,2047,8191,32767}, compute exactly from binomial
probabilities

```text
M_N(s) = E |S_N / sqrt(2 pi N)|^(s-1).
```

Use the frozen grid Re(s) in {0.25,0.5,1,1.5,2,3} and Im(s) in
{0,2,6,12}. The target is

```text
M_N(s) -> pi^(-s/2) Gamma(s/2),  Re(s)>0.
```

Also score cos(t/sqrt(N))^N -> exp(-t²/2) for t in {0.5,1,2,4} and the
local CLT on |z| <= 3. Report the complete grid, including the slow
negative-moment/high-frequency corner.

### E4 — representation-dimensional specificity

For K_q = J_q/q, q = 3,4, put the q symbols at the vertices of a centered
regular simplex in dimension d = q-1. Compute the exact multinomial radial
law and compare it both with the binary target and with

```text
M_d(s) = (pi d)^(-(s-1)/2)
         Gamma((d+s-1)/2) / Gamma(d/2).
```

Success means the canonical radial controls approach their native
dimension-shifted Gamma factors while remaining separated from the binary
factor. Scalar projections are proves-too-much controls, not canonical K_q
sectors.

### E5 — Hellinger/chiral obstruction

For each recovered atom p, verify

```text
B_p(s) = [[0, p^(-s)], [p^(-(1-s)), 0]],
B_p(s)^2 = p^(-1) I₂.
```

On s = 1/2 + it, verify unitary diagonal gauge equivalence to X/sqrt(p),
where X = [[0,1],[1,0]], and the fixed spectrum {+p^(-1/2),-p^(-1/2)}.
This forbids interpreting t as spectral motion. J₂ is reserved for the
all-ones matrix in K₂ = J₂/2; X is the swap matrix.

### E6 — auxiliary global-inventory normalization

At atom cutoffs 64,128,256,512,1024,2048,4096, solve sum_a a^(-h) = 1,
test Hellinger product/conjugacy, common Schatten thresholds, and the r = 1
term deleted by paired det₂. Run shifted, additive, and 32 matched-random
inventory controls. This branch is an obstruction control and is not the
internal F₂ Parry fiber of SD-C08.

## Data, precision, and controls

- Tensor atoms are recovered as finite multiplication indecomposables; no
  prime table is loaded.
- No training or fitted parameters exist.
- No Riemann-zero list, target-root cutoff, or root score exists.
- Algebraic ledgers use direct finite matrix identities; probability and
  complex-grid diagnostics use IEEE-754 binary64.
- All seeds are fixed in code and all random controls are reported.

## Frozen outputs

Exactly seven result artifacts are produced:

1. `results/summary.json`;
2. `results/k2_prime_blocks.csv`;
3. `results/mellin_cutoffs.csv`;
4. `results/mellin_grid.csv`;
5. `results/characteristic_local_clt.csv`;
6. `results/parry_cutoffs.csv`;
7. `results/parry_controls.csv`.

## Decision rule

Pass E1--E4 and retain E5--E6 as explicit obstructions to assign SD-C08
the stage status:

```text
GO_A3_ARCHIMEDEAN_FACTOR / STOP_GLOBAL_COMPLETION
```

The result remains a same-trace, same-source Mellin--Fredholm factorization.
Without a single unified determinant, continuation, functional equation,
pole removal, and moving divisor, Route B stays locked.
