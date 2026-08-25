# C164 source audit

## Frozen source and clock

The dynamical source is exactly C159's binary Thue--Morse S-gap shift.  If
`t_s` is binary digit-sum parity, then

```text
S={s>=0:t_s=1},            C={10^s:s in S},
F(z)=sum_(s in S) z^(s+1).
```

One left shift is one source clock tick; a branch `10^s` returns after
`s+1` ticks.  The all-zero fixed orbit contributes the separate scalar block
`[z]`.  No clock is fitted or rescaled.

## Three objects kept separate

1. The **induced owner** is the analytic first-return family on the Hilbert
   space whose coordinates are the source code branches.  Its branch
   decomposition, trace-norm convergence, all trace powers, and Fredholm
   determinant are proved.
2. The **uninduced adjacency** advances one position per clock tick and adds
   the Thue--Morse return row.  A universal theorem shows it is noncompact on
   every diagonal weighted Hilbert realization on which it is bounded.
3. A one-dimensional scalar chosen after knowing `(1-z)(1-F(z))` would make
   a tautological determinant identity.  Such a scalar equality is not used
   as ownership evidence.

## Evidence ownership

The only input is the frozen Thue--Morse parity and its renewal branches.
The all-parameter proof is analytic.  The first 128 bits, degree-48 formal
series, 32 branch rows, and a bounded weight example are deterministic
regression sentinels, not extrapolations.

## Scope firewall

The package reads no target zero or prime table and introduces no arithmetic
local data.  It asserts no Euler factor, root number, automorphy, target
functional equation or counting law, unitary/Hamiltonian realization,
self-adjoint lift, or Hilbert--Pólya operator.  Route B is disabled.  Literal
scope:

```text
NO_BAD_EULER_OR_ROOT_NUMBER
```
