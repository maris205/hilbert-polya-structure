# C160 source audit

## Frozen source

Rule 90 acts on a cyclic binary ring of Mersenne length `L=2^r-1` by
multiplication with `a=x+x^(-1)`.  The source clock is one cellular-automaton
update on the complete periodic image `im(a)`.  Labeled states, exact-period
states, and geometric cycles remain distinct normalizations.

## Hard-gate decision

C155 proved full-period concentration with a union over every proper clock.
C160 was required to produce a strictly stronger all-parameter theorem or
change model.  It passes without a pivot:

- for every Mersenne `L`, the non-full-period set is an exact union over only
  the maximal subgroups of the finite time group, with full inclusion--
  exclusion and Bonferroni bounds;
- for every Mersenne length `L>3` that is prime, the only periods are `1` and
  `L`, the zero state is the only short orbit, and the complete finite zeta is
  closed form.

No statement asserts that infinitely many Mersenne primes exist.

## Use of source-length factors

The distinct ordinary integer prime divisors of `L` index maximal subgroups
of the finite cyclic time group.  They are computed from each source length,
not read from an external table.  They are not target primes, arithmetic
local factors, or Euler factors.

## Scope firewall

No target zero or prime table, arithmetic/local data, root number, automorphy
claim, target functional equation/counting law, Hilbert--Pólya operator, or
Route-B input is used.  Literal scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is disabled.
