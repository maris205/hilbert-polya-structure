# C144 source audit

## Source lock

The sole mathematical source is the frozen substitution
`sigma(0)=01`, `sigma(1)=10`.  Every word, finite-language table, obstruction
certificate, and periodic approximant is derived from that rule by the checked
local code.  The manuscript uses no external bibliography and makes no
literature-priority claim.

## Verified internal facts

- `t_n` is the parity of the binary digit sum of `n`.
- `t_(j*2^q+r)=t_j xor t_r` for `0<=r<2^q`.
- Consecutive aligned dyadic blocks are `w_q` or its complement.
- The exact language through width 16 is captured by four adjacent dyadic
  block types.
- The aperiodicity certificate for every proposed period `p` is algebraic and
  has no search-dependent theorem step.

## Evidence boundary

The all-period no-periodic-point result is proved in `THEOREM_PACKAGE.md`.
The tables through width 16, substitution level 12, and proposed period 32 are
replay sentinels only.  Macroscopic defect rows at levels 2 through 9 are exact
finite controls and are not promoted to an all-level theorem.

Scope literal: `NO_BAD_EULER_OR_ROOT_NUMBER`.  No prime or target-zero table,
arithmetic/local factor, root number, automorphy statement, Hilbert--Polya
operator, or Route-B input is used.
