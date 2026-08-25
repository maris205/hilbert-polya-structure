# C162 theorem package

## Source identity

For `Re(s)>0`, C157 proved

```text
W_D(s)=s/(2*pi) sum_(m in Z^2)(s^2+4|m|^2)^(-3/2)
       -1/4-1/(exp(pi*s)-1),                                  (1)
```

with the principal power and locally normal convergence.

## Theorem: renormalized full-trace branch amplitude

Let `N>=1`, `t_N=2 sqrt(N)`, and
`r_2^src(N)=#{m in Z^2:|m|^2=N}`.  Then

```text
lim_(epsilon down to 0) epsilon^(3/2) W_D(epsilon-i t_N)
 =exp(i*pi/4) r_2^src(N)/(8*pi*N^(1/4)).                       (2)
```

At negative time the limit is the complex conjugate.

**Proof.**  A matching vector has denominator

```text
s^2+4N=epsilon(epsilon-2 i t_N).
```

Therefore its normalized contribution tends to

```text
(-i t_N)/(2*pi)*(-2 i t_N)^(-3/2)
 =exp(i*pi/4)/(8*pi*N^(1/4)),                                 (3)
```

where the phase follows from the principal branch.  There are exactly
`r_2^src(N)` matching vectors.

It remains to justify passage through the infinite nonmatching sum.  Fix
`t_N` and `0<epsilon<=1`.  Outside a radius chosen so that
`4|m|^2>=2(t_N^2+1)`,

```text
|s^2+4|m|^2| >= 4|m|^2-|s|^2 >= 2|m|^2.
```

Thus the tail is uniformly bounded by a constant times
`sum_(m!=0)|m|^(-3)`, which converges in two dimensions.  The finitely many
nonmatching shells have denominators bounded away from zero as epsilon tends
to zero.  Dominated convergence and the factor `epsilon^(3/2)` kill all of
them.

At an even shell time the subtraction term in (1) may have a simple pole, but
its normalized size is only `O(epsilon^(1/2))`.  The Weyl, constant, and other
bounded terms also vanish.  This proves the full-trace limit, not merely an
individual-summand limit.  The negative-time statement follows by conjugation.

## Consequences and boundary

The normalization separates the `-3/2` clean-family branch from any coincident
simple pole.  It recovers the aggregate source lattice-shell multiplicity,
including axes, signs, collisions, and repetitions.  It is not an isolated
primitive-orbit stability amplitude.

The strict tuple is `(A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`:
`sqrt(Delta_D)` is a natural self-adjoint source operator, but clean families
are not isolated and no target trace/divisor/counting law, arithmetic
local/Euler factor, root number, automorphy, Hilbert--Polya construction, or
Route-B authorization is claimed.
