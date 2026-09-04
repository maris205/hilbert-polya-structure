# Replacement theorem-spike gate

## Sole provisional survivor: R01/BSE

This contract is not a paper-number assignment and not a novelty claim. It is
the one replacement candidate that survived internal theorem closure and
bounded exact attack. Status remains
`PROVISIONAL / OWNER_AMBER / HOLD_EXTERNAL / UNNUMBERED`.

Let

```text
B_n = {0} union {(a,b): 1<=a,b<=n},
(a,b)(c,d) = (a,d) if b=c, and 0 otherwise.
```

Write `u*=(b,a)` for the inverse matrix unit of `u=(a,b)`. On cyclic words
`x in B_n^m`, with indices modulo `m`, define the natural local sandwich map

```text
T(x)_i = x_i x_(i+1) x_i.
```

### Temporal theorem contract

Put `g_i=1[x_i!=0 and x_(i+1)=x_i*]`. For every `n,m>=1`, every source,
every coordinate, and every `t>=0`,

```text
T^t(x)_i = x_i  iff  product_(j=0)^(t-1) g_(i+j)=1,
T^t(x)_i = 0    otherwise.
```

The empty product handles `t=0`. Thus every orbit terminates at a fixed word.
Besides `0^m`, fixed words are the full alternating-inverse words, so

```text
Fix(n,m) = 1+n    if m is odd,
Fix(n,m) = 1+n^2  if m is even.
```

For a nonfixed nonzero source, if `L(x)` is its longest cyclic run of good
edges, then its exact tail is `L(x)+1`; `0^m` and the all-good words have tail
zero. For `n>=2`, the sharp maximum tail is `m` for odd `m` and `m-1` for
even `m`. Indeed, an off-diagonal unit realizes a single bad closing edge
when `m` is odd, whereas on an even cycle “exactly one bad edge” contradicts
inversion around the other `m-1` edges. Two bad edges are realizable. In the
degenerate `n=1` case the maximum is `max(0,m-1)`.

In particular, the boundary boxes are not silently excluded:

- `m=1`: there are `n+1` fixed states; each diagonal target has one source,
  every off-diagonal target is empty, and the zero target has `n^2-n+1`
  sources. The maximum tail is one for `n>=2` and zero for `n=1`.
- `m=2`: there are `n^2+1` fixed states. A nonzero fixed word is `(u,u*)`;
  every other word reaches `0^2` in one step. Hence the zero fibre is
  `(n^2+1)^2-n^2`, and the maximum tail is one.

### Independent every-target inverse contract

Let `Q=B_n`, `q=n^2+1`, and for every output letter `y` define the `q x q`
zero-one matrix

```text
M_y(u,v) = 1[u v u = y].
```

Then every labelled target `y=(y_0,...,y_(m-1))` has the exact fibre

```text
|T^(-1)(y)| = tr(M_(y_0) M_(y_1) ... M_(y_(m-1))).
```

This is strengthened beyond the generic trace statement. Let `A=M_0`. If
the nonzero target sites, in cyclic order, are `i_1,...,i_s`, and `h_j` is the
number of zero target sites strictly after `i_j` and before `i_(j+1)`, then

```text
|T^(-1)(y)| = product_j (A^h_j)_( y_(i_j)* , y_(i_(j+1)) ).
```

For the all-zero target the answer is `tr(A^m)`. Put `r=n^2`, let `s_0=2`,
`s_1=r`, and `s_m=r s_(m-1)+s_(m-2)`. Directly decomposing the matrix-unit
alphabet under inversion gives

```text
tr(A^m) = s_m + (-1)^m ((r+n)/2-1) + (r-n)/2.
```

Equivalently, the two exceptional eigenvalues are the roots of
`z^2-rz-1`; eigenvalue `-1` has multiplicity `(r+n)/2-1`, and eigenvalue
`+1` has multiplicity `(r-n)/2`.

The gap product also characterizes the labelled image. Consecutive nonzero
target letters must alternate by inversion; across exactly one zero the next
nonzero letter must differ from the previous one; gaps of at least two zeros
impose no further restriction because every entry of `A^2` is positive.
Finally, since `sum_y M_y` is the all-ones matrix,

```text
sum_(y in Q^m) |T^(-1)(y)| = tr(J_q^m) = q^m.
```

This is the required exact mass conservation, not a sampled normalization.

### Proof routes and axis separation

The temporal proof is induction on the good-edge indicator and gives the
run-erasure normal form. It receives no originality credit by itself. The
inverse proof instead partitions a source word by pinned adjacent letters,
then multiplies zero-output transition counts across target gaps. The closed
zero-fibre formula uses the involution eigenspaces of matrix-unit inversion.
The second route is not needed for the temporal theorem and returns every
labelled target, including empty fibres.

### Internal-history subtraction

- P104 is an iid real-matrix cocycle with singular-value and pressure laws;
  R01 is a deterministic finite local map and its transfer matrices count
  cyclic predecessors.
- P105 performs global least-label permutation surgery; R01 uses no global
  label order and no variable cycle carrier.
- P147 merges equal composition runs and has a logarithmic/divisor-path
  package; R01 preserves carrier length and has inversion-gap fibres.
- P159 deletes odd-degree graph vertices and uses binary incidence rank; R01
  has no graph parity or kernel-rank inverse.
- P183 is a stochastic incoming-copy graph chain with random-history endpoint
  kernels; R01 is deterministic and synchronous.

The generic support/run-erasure component remains an occupied motif. The
provisional claim is only that the semigroup-specific parity and exact inverse
package is not mechanically supplied by these papers.

## Rejected near-miss: R02/RBW

For a rectangular band `(i,j)(k,l)=(i,l)`, the boundary word update merely
shifts right coordinates: `T^t(x)_r=(a_r,b_min(r+t,m))`. Its sharp tail and
fibres are forgotten-coordinate counts from the same projection. This is a
thin shift register and remains killed.

## Rejected near-miss: R03/CSA

For `T(x)_i=min(a,x_i+x_(i+1))`, Pascal induction yields capped cyclic
binomial convolution. This is too close to P108's capped Fibonacci engine,
and the inverse side did not exceed a generic local-rule transfer. It remains
killed despite its clean bounded signals.

`R04`, `R05`, `R06`, and `R09` are action-only permutations or involutions;
`R07` has no closed all-parameter inverse or clock; `R08` is standard free
reduction under a parallel schedule; and `R10` has only zero propagation.
