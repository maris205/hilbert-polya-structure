# C149 proof package

## Claim and status

Let `X_TM` be the two-sided Thue--Morse language subshift and let `C_ell` be a
tagged cycle of length `ell`.  On
`Y=X_TM sqcup C_1 sqcup C_2 sqcup C_3 sqcup C_5`, use the shift on `X_TM` and
cyclic successor on each `C_ell`.  Then, for every `n>=1`,

```text
Fix_Y(n)=sum_(ell in {1,2,3,5}, ell|n) ell,
zeta_Y(z)=product_(ell in {1,2,3,5})(1-z^ell)^(-1).
```

There is exactly one primitive cycle at each length `1,2,3,5` and no other
primitive cycle.  The space is compact but not minimal.  More generally, a
nonempty finite disjoint periodic attachment to any nonempty aperiodic
component destroys minimality.  **PROVABLE AS STATED.**

## Lemma 1: the infinite component has no periodic point

Write `t_n` for binary digit-sum parity.  Binary concatenation gives
`t_(j2^q+r)=t_j xor t_r` for `0<=r<2^q`; aligned dyadic blocks are the word
`w_q` or its complement.  For a proposed period `p`, choose odd
`k>bit_length(p)` and put `d=p(2^k-1)`.  Since

```text
d=(p-1)2^k+(2^k-p),
```

the lower `k` bits complement the `k`-bit form of `p-1`, so
`popcount(d)=k` is odd.  Thus `t_d != t_0`, although `d` is divisible by
`p`.  Let `b=bit_length(d)`, so `d<2^b`.  Every interval of `t` of length
`2^(b+1)` contains a complete block aligned at some `j*2^b`.  At offsets `0`
and `d` in that block, the dyadic identity gives respectively
`t_j xor t_0` and `t_j xor t_d`, which are opposite.  Their distance is the
multiple `d` of `p`, so no such interval is `p`-periodic.  A `p`-periodic
point in the language subshift would have a length-`2^(b+1)` window that
occurs in `t`; that occurrence would be a forbidden `p`-periodic interval.
Hence the Thue--Morse component contributes no fixed point at any positive
period.

## Theorem 2: all-period orbit ledger

On a cycle `C_ell`, the `n`th power fixes all `ell` points exactly when
`ell|n`; otherwise it fixes none.  Disjoint components add fixed counts, and
Lemma 1 supplies zero from `X_TM`, proving the formula.  Möbius inversion
recovers exact-period points.  Directly, each declared component is one orbit
of least period `ell`, so the only nonzero exact-period counts are
`P(ell)=ell` for `ell=1,2,3,5`; division by `ell` gives one primitive cycle.

For formal `z`,

```text
sum_(n>=1) Fix_Y(n)z^n/n
 = sum_ell sum_(q>=1) z^(ell q)/q
 = -sum_ell log(1-z^ell).
```

Exponentiation proves the rational zeta product as a formal power series (and
analytically for sufficiently small `|z|`).

## Proposition 3: topology and unavoidable cost

A finite topological disjoint union of compact spaces is compact.  Each tagged
cycle is finite, hence closed, and invariant.  It is also a proper nonempty
subset because `X_TM` is nonempty and disjoint.  A dynamical system with a
proper nonempty closed invariant subset is not minimal.  The same argument
works for any nonempty finite union of attached periodic cycles.  This is a
plain nonminimal disjoint union, not an almost-minimal extension.

## Route-A conclusion

The attachment produces an exact nonempty finite skeleton, but it is freely
declared rather than intrinsic to the minimal symbolic source.  Its elementary
rational zeta has no frozen target comparison or downstream structure.  The
strict tuple is `(A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, overall
`ROUTE_A_REJECTED`; `route_b_invocation_allowed=false`.
