# C153 proof package

## Claim and status

**Status: PROVABLE AS STATED, WITH AN UNNORMALIZED TRACE NONLIMIT.**  The
all-parameter rank law, macroscopic escape rate, fixed-period equality-merged
cluster sets, normalized trace limit, and controls all follow from the frozen
gate.  An ordinary unnormalized fixed-period trace limit does not exist in
general; period two is an exact counterexample.

## Frozen notation

Let `omega=(-1+i*sqrt(3))/2`, let

```text
F3[j,l]=omega^(j*l)/sqrt(3),  P=diag(1,0,1),  A=F3^*P,
```

and on `H_k=(C^3)^(tensor k)` set

```text
B_k(v0 tensor ... tensor v_(k-1))
 =v1 tensor ... tensor v_(k-1) tensor A*v0.       (1)
```

One application is one clock tick.  For `m>=0`, write `t_m=Tr(A^m)` except
that `t_0=2` denotes the power sum of the two nonzero eigenvalues.

## Dependency map

1. The one-qutrit characteristic polynomial proves `rank(A^m)=2` for all
   positive `m`.
2. The exact tensor-factor action of `B_k^n` proves every rank and the escape
   exponent.
3. Cycle contraction of the factor permutation proves the gcd trace formula.
4. Elementary gcd subsequences give every divisor class infinitely often;
   equality merging gives the exact cluster set.
5. Finiteness of that set proves normalized trace decay, while parity at
   period two refutes a general unnormalized limit.

## Theorem 1: all-parameter image rank

For every `k>=1` and `n>=0`,

```text
rank(B_k^n)=2^min(n,k) 3^(k-min(n,k)).             (2)
```

**Proof.**  Direct computation gives

```text
chi_A(lambda)=lambda*(lambda^2-tau*lambda+q0),
tau=sqrt(3)/6-i/2,  q0=-1/2-sqrt(3)*i/6.
```

Since `q0!=0`, zero is a simple eigenvalue and the other two eigenvalues are
nonzero.  The generalized zero eigenspace therefore has dimension one, so
`rank(A^m)=2` for every `m>=1`; of course `rank(A^0)=3`.

Write `n=qk+r`, where `q>=0` and `0<=r<k`.  Iterating (1) on a pure tensor
gives the exact identity

```text
B_k^n(v0,...,v_(k-1))
 =(A^q v_r,...,A^q v_(k-1),
   A^(q+1)v_0,...,A^(q+1)v_(r-1)).                 (3)
```

For `q=0`, exactly `r=n` factors have positive powers of `A`, so tensor-rank
multiplicativity gives `2^n 3^(k-n)`.  For `q>=1`, all `k` powers are positive,
giving `2^k`.  These are precisely the two cases in (2).  At `n=0`, (3) is
the identity and (2) gives full rank `3^k`. ∎

## Corollary 2: macroscopic escape exponent

Define the rank-survival fraction

```text
S_k(n)=rank(B_k^n)/3^k=(2/3)^min(n,k).
```

For `alpha>=0` and `n_k=floor(alpha*k)`,

```text
lim_(k->infinity) k^(-1) log S_k(n_k)
 =min(alpha,1) log(2/3).                            (4)
```

Equivalently, the positive escape exponent is
`E(alpha)=min(alpha,1)log(3/2)`.  Indeed,
`min(floor(alpha*k),k)/k -> min(alpha,1)`, and (4) follows from the exact
formula.  At `alpha=0`, `n_k=0`, so `S_k=1` and `E(0)=0`.

## Theorem 3: fixed-period trace cluster set

For all `n,k>=1`, with `d=gcd(n,k)`,

```text
Tr(B_k^n)=t_(n/d)^d,                               (5)
t_0=2, t_1=tau, t_m=tau*t_(m-1)-q0*t_(m-2).
```

Consequently, at fixed `n` the full cluster set as `k->infinity` is the set of
distinct values obtained after equality-merging

```text
C_n={t_(n/d)^d : d divides n}.                     (6)
```

Every divisor class occurs infinitely often.

**Proof.**  In a basis matrix element of `B_k^n`, the shift constraints join
factor positions along the cycles of addition by `n` modulo `k`.  There are
`d` cycles.  Each cycle contracts `n/d` ordered copies of `A`, giving one
factor `Tr(A^(n/d))`; multiplying the independent cycles proves (5).  The
quadratic factor of `chi_A` gives the displayed recurrence.

For a fixed divisor `d|n`, choose

```text
k_j=d*(1+j*(n/d)),  j>=0.
```

Then `gcd(n,k_j)=d*gcd(n/d,1+j*n/d)=d`, and `k_j` is unbounded.  Thus each
divisor class supplies an infinite constant subsequence.  Conversely (5)
shows that no value outside the divisor list can occur.  If distinct divisors
give the same complex number, they describe one cluster value, which is why
(6) is a set rather than a multiset. ∎

## Corollary 4: normalized decay and an unnormalized obstruction

For every fixed `n>=1`,

```text
3^(-k) Tr(B_k^n) -> 0.                             (7)
```

Indeed the numerator belongs to the finite set `C_n`, hence is bounded
independently of `k`, while `3^k` diverges.

The normalization is essential.  At `n=2`, odd `k` have `d=1` and even `k`
have `d=2`, giving

```text
t_2     = 5/6 +(sqrt(3)/6)i,
t_1^2   =-1/6 -(sqrt(3)/6)i,
t_2-t_1^2=1+(sqrt(3)/3)i=-2q0 !=0.                 (8)
```

Thus the odd and even subsequences are distinct constants, so
`Tr(B_k^2)` has no limit as `k->infinity`.  C153 claims only (7), not a
general unnormalized convergence theorem.

## Controls and Route-A boundary

For `P=I_3`, the one-site gate is `F3^*`, so the closed parent is unitary,
every power has full rank `3^k`, and the escape exponent is zero.  Projector
order is an isospectral control: `A_right=P F3^*=F3 A F3^*`, and uniform
tensor conjugation preserves every rank and trace cluster.  Moving the hole to
`P0=diag(0,1,1)` gives

```text
chi_A0(lambda)=lambda*(lambda+i)*(3lambda+sqrt(3))/3.
```

Its zero root is simple and its other roots are nonzero, hence
`rank(A0^m)=2` for every positive `m`; the rank law survives, although the
trace values change.  Rank escape therefore does not determine trace geometry.

The strict tuple is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)`.  The finite
subunitary gates have the natural closed unitary parent and the same explicit
clock, but C153 constructs no self-adjoint or antiunitary limit and no full
growing-`k` secular limit.  It asserts no target divisor, functional equation,
counting law, prime-like map, arithmetic/local datum, Euler factor, root
number, automorphy, Hilbert--Polya operator, or Route-B authorization.
