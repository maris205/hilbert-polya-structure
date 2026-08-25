# C144 proof package

## Claim

Let `t_n` be the parity of the binary digit sum of `n`, and let `X_TM` be the
two-sided subshift whose language consists of the finite factors of `t`.
Then `X_TM` is nonempty, minimal, and contains no shift-periodic point.
Consequently `Fix(shift^n|X_TM)=0` for every `n>=1` and its Artin--Mazur zeta
is identically one.  The circulated finite approximants are periodic controls,
not periodic points of `X_TM`.

## Status

**PROVABLE AS STATED.**

## Assumptions and notation

- `w_q=t_[0,2^q)` and `bar(w_q)` is its bitwise complement.
- `L_TM` is the set of all finite factors of `t`.
- `X_TM={x in {0,1}^Z: every finite factor of x belongs to L_TM}`.
- A finite interval is `p`-periodic when symbols at positions separated by
  `p` agree whenever both positions lie in the interval.

## Dependency map

1. Binary concatenation gives the dyadic block identity.
2. Complementary adjacent pairs exclude `000` and `111`.
3. The dyadic identity and the triple exclusion prove uniform recurrence.
4. Uniform recurrence proves nonemptiness and minimality of the language
   subshift.
5. An odd-popcount multiple of every proposed period gives a forbidden window.
6. The forbidden-window bound passes from `t` to every point of `X_TM` through
   the definition of the language.

## Lemma 1: dyadic blocks and uniform recurrence

For `0<=r<2^q`, binary concatenation has no carries, so

```text
t_(j*2^q+r)=t_j xor t_r.                          (1)
```

Hence the aligned block of length `2^q` beginning at `j*2^q` is `w_q` when
`t_j=0` and `bar(w_q)` when `t_j=1`.  Also
`t_(2m)=t_m` and `t_(2m+1)=1-t_m`; every pair at positions `2m,2m+1` is
complementary.  Any three consecutive positions contain such a pair, so
neither `000` nor `111` occurs.

Fix a factor `u` of `t`, and choose `q` with `u` contained in `w_q` (increase
the substitution level containing its first occurrence).  Any interval of
length `4*2^q` contains three complete aligned `q`-blocks.  Their types are
three consecutive symbols of `t`, not all ones, so one block is `w_q` and
contains `u`.  Thus every factor has bounded gaps: `t` is uniformly recurrent.

## Lemma 2: nonemptiness and minimality

Choose shifts of `t` whose origins move to infinity and extend `t` arbitrarily
to the unused negative coordinates.  Compactness of `{0,1}^Z` gives a limit;
every finite factor of that limit is in `L_TM`, so `X_TM` is nonempty.

Let `x in X_TM` and fix `u in L_TM`.  By Lemma 1 there is `R` such that every
length-`R` factor of `t` contains `u`.  Every length-`R` factor of `x` belongs
to `L_TM` and therefore is a factor of `t`; it contains `u`.  Thus every point
of `X_TM` contains every word of `L_TM` with bounded gaps.  Its shift orbit
meets every nonempty cylinder, proving minimality.

## Theorem 3: no periodic point

Fix a proposed positive period `p`.  Choose an odd integer `k` strictly larger
than the binary length of `p`, and put

```text
d=p(2^k-1).
```

This is a multiple of `p`.  The decomposition

```text
d=(p-1)2^k+(2^k-p)
```

has disjoint high and low binary blocks.  The low `k` bits of `2^k-p` are the
bitwise complement of the `k`-bit expansion of `p-1`.  Therefore

```text
popcount(d)=popcount(p-1)+k-popcount(p-1)=k,
```

which is odd; hence `t_d=1` while `t_0=0`.

Let `b` be the binary length of `d`, so `d<2^b`.  Every interval of `t` of
length `2^(b+1)` contains a complete block aligned at a multiple `j*2^b`.
By (1), the symbols at offsets `0` and `d` in that block differ.  Their
distance is a multiple of `p`, so the interval cannot be `p`-periodic.

If a `p`-periodic point `x` belonged to `X_TM`, its length-`2^(b+1)` window
would occur in `t` by the definition of `X_TM`.  That occurrence would be a
`p`-periodic interval, contradicting the preceding paragraph.  Since `p` was
arbitrary, `X_TM` contains no periodic point.  It follows immediately that
all positive fixed-point and primitive-cycle counts vanish and

```text
zeta_TM(z)=exp(sum_(n>=1) 0*z^n/n)=1.             (2)
```

## Proposition 4: finite periodic approximants

Let `c_k=w_k^infinity`.  The least cyclic period of `c_k` is `2^k`: a smaller
period of the cyclic word must divide `2^k`, hence is at most `2^(k-1)`, but
the second half of `w_k` is the complement of the first.  Every non-seam
width-`m` window with `m<=2^k` is a factor of `t`; at most the `m-1`
seam-crossing rooted windows can be extrinsic.  Thus their invalid rooted
fraction is at most `(m-1)/2^k`.

The replay ledger sharpens this finite control: all audited widths at most 16
are intrinsic at levels 2 through 12, whereas at levels 2 through 9 every
rooted window of width `2^(k+1)+1` is extrinsic.  The latter is a checked
finite statement, not an extrapolated theorem.  Theorem 3 already proves that
none of the periodic `c_k` lies in `X_TM`.

## Route-A conclusion

The result is a proved first-layer obstruction:
`(A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, overall `ROUTE_A_REJECTED`.  Minimality
and uniform recurrence coexist with a complete primitive-periodic-orbit
vacuum.  No target divisor or global analytic structure, arithmetic/local
factor, operator lift, or Route-B authorization is claimed.
