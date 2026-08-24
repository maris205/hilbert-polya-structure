# C130 theorem package

## Definition 1 (frozen suspension)

Let `B=[[1,1],[1,1]]` and let `Sigma_B` be the two-sided full binary shift.
Set `tau(0)=1` and `tau(1)=sqrt(2)`.  The suspension is

```text
X^tau = (Sigma_B x R)/((x,t+tau(x)) ~ (sigma(x),t)).
```

For a closed word `w`, let `N_j(w)` count symbol `j` and put
`ell(w)=N_0(w)+sqrt(2)N_1(w)`.  With destination-symbol weights, define

```text
M(u,v)=B diag(u,v)=[[u,v],[u,v]].
```

## Theorem 1 (all-period primitive Euler/trace owner)

For every integer `n>=1`,

```text
Tr M(u,v)^n
  = (u+v)^n
  = sum_{k=0}^n binom(n,k) u^(n-k) v^k.
```

In the total-degree completion of `Z[u,v]`,

```text
Delta(u,v) := det(I-M(u,v)) = 1-u-v
 = product_[gamma primitive] (1-u^N0(gamma) v^N1(gamma)).
```

After `u=exp(-s)` and `v=exp(-sqrt(2)s)`,

```text
d_tau(s)=1-exp(-s)-exp(-sqrt(2)s)
        = product_[gamma primitive] (1-exp(-s ell(gamma))).
```

The product and logarithmic trace series converge absolutely for
`Re(s)>h`, where `h>0` is the unique solution of
`exp(-h)+exp(-sqrt(2)h)=1`.  The explicit left side extends to an entire
exponential polynomial, and `zeta_tau=1/d_tau` is meromorphic.

### Proof

The matrix has eigenvalues `u+v` and `0`, giving the determinant and the
trace formula.  Alternatively, `Tr M^n` sums all rooted binary closed words of
length `n`; a word with `k` symbols `1` contributes `u^(n-k)v^k`, and there
are `binom(n,k)` such words.  For `|u|+|v|<1`,

```text
-log det(I-M)=sum_{n>=1} Tr(M^n)/n.
```

Every rooted closed word is uniquely a repetition of a primitive cyclic word.
Regrouping the absolutely convergent series by primitive root yields
`sum_gamma sum_m w(gamma)^m/m`; exponentiation gives the product.  The same
regrouping is valid formally because each total degree sees finitely many
primitive words.  Under the Laplace specialization,
`|exp(-s)|+|exp(-sqrt(2)s)|<1` precisely for real part greater than `h`,
which proves the analytic convergence statement.  No period cutoff occurs.

## Theorem 2 (clock-sector separation, not orbit separation)

The map

```text
(a,b) in Z^2  ->  a+b*sqrt(2)
```

is injective.  Consequently distinct symbol-population vectors of arbitrary
closed words have distinct suspension times.  This does not separate orbits
inside one vector: the primitive period-six necklaces `000111` and `001011`
both have counts `(3,3)` and roof `3+3sqrt(2)`.

Moreover, the entire function `d_tau` has no nonzero imaginary period.

### Proof

Equality `a+b sqrt(2)=c+d sqrt(2)` implies
`a-c=(d-b)sqrt(2)`.  Irrationality forces both integer differences to vanish.
For periodicity, suppose `d_tau(s+iT)=d_tau(s)` for all `s`.  For real
`s=sigma`, subtract and divide by `exp(-sigma)`.  Letting `sigma` tend to
infinity gives `exp(-iT)=1`; the remaining coefficient gives
`exp(-i sqrt(2)T)=1`.  Thus both `T/(2pi)` and `sqrt(2)T/(2pi)` are integers,
which is possible only for `T=0`.

## Proposition 3 (rational-roof control)

Keep the base and determinant convention but replace the roof by `(1,2)`.
Then

```text
d_rat(s)=1-exp(-s)-exp(-2s)=1-q-q^2,  q=exp(-s),
d_rat(s+2*pi*i)=d_rat(s).
```

The count sectors `(2,0)` and `(0,1)` collide at roof time `2`: the first is
the second repetition of primitive fixed orbit `[0]`, while the second is the
primitive fixed orbit `[1]`.

### Proof

Both claims follow by direct substitution.  Integer roof lengths factor
through the single lattice variable `q`; hence vertical `2pi*i` periodicity
and cross-sector aggregation return together.

## Exact boundary

Theorems 1--2 and Proposition 3 concern only the frozen symbolic suspension.
They do not produce an arithmetic Euler product, root number, target divisor
match, functional equation, counting law, orbit-level inverse within a sector,
or natural self-adjoint lift.  The strict tuple is therefore
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, and Route B remains unauthorized.
