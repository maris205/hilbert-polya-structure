# HCS-C160: Rule-90 maximal-subgroup sieve

For every Mersenne circumference, this package replaces C155's union over all
proper clocks by an exact inclusion--exclusion over maximal subgroups of the
finite time group.  For every Mersenne-prime source length `L>3`, it proves

```text
period support = {1,L},
P_L(1)=1,
P_L(L)=2^(L-1)-1,
zeta_g(z)=1/((1-z)(1-z^L)^((2^(L-1)-1)/L)).
```

No infinitude of Mersenne primes is claimed.  Source-length factorization is
not an arithmetic Euler/local factorization.

Run producer, checker, SymPy cross-check, replay, and mutation audit from the
repository root.  Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is disabled.
