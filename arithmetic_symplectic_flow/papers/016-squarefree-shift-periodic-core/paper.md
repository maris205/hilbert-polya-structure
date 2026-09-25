# A natural squarefree sieve closure has no nonzero periodic symbolic orbit

**Paper ID:** `016-squarefree-shift-periodic-core`  
**Record ID:** `ASFS-SCOUT-20260913-14`  
**Date / status:** `2026-09-13; PRE-P0 NEGATIVE RESULT`  
**Route state:** `No frozen candidate; Route A coordinates not evaluated; Route B NOT INVOKED`

## Abstract

The squarefree indicator is a natural sieve-derived symbolic object: it marks
the integers not eliminated by any prime-square divisibility test. This screen
asks whether its shift closure restores meaningful periodic symbolic orbits.
It does not. A direct congruence argument proves that every periodic point is
`0^infinity`. Thus this canonical `B`-free extension has a still stronger A1
obstruction than the prime-indicator closure: no periodic word containing a
survivor exists. It is not a finite-dimensional symplectic candidate and stops
before P0.

## 1. Construction and lineage

Let `eta(n)=1` if `n` is squarefree and `eta(n)=0` otherwise, and form the
shift orbit closure `X_sf=closure{sigma^j eta}`. The retained programme path is

```text
prime-square sieve constraints -> symbolic survivor word -> autonomous shift closure.
```

This is a natural sieve closure, not an arbitrary arithmetic substitution. It
does not itself provide the required Logistic/Hénon/symplectic lift; it tests
whether that route can first obtain a nondegenerate symbolic periodic ledger.

## 2. Periodic-core theorem

**Proposition.** The only periodic point of `X_sf` is `0^infinity`.

**Proof.** Let `x` in `X_sf` have period `q>0` and suppose `x_r=1` for some
residue `r mod q`. Choose shifts `n_i` for which `sigma^{n_i}(eta)` converges
to `x`. Choose a prime `p` not dividing `q`, then pass to a subsequence on
which `n_i` has one fixed residue modulo `p^2`, say `c`. Since `q` is
invertible modulo `p^2`, there is an integer `k` with
`c+r+kq=0 mod p^2`. The `r+kq` coordinate of every term of that subsequence is
therefore zero, because its underlying integer is divisible by `p^2`. Passing
to the limit gives `x_{r+kq}=0`, contradicting periodicity and `x_r=1`. Hence
no periodic `x` contains a one. The all-zero point belongs to the closure
because factorial intervals provide zero blocks of arbitrary length. QED.

The cylinder argument works equally with a two-sided indexing convention; only
the translation direction changes.

## 3. Gate consequence

The result blocks the desired orbit structure already at its natural symbolic
source. A suspension or Hénon realization cannot borrow periodic points from a
different full shift, nor can it call `0^infinity` a prime/squarefree orbit.
There is also no specified smooth finite-dimensional symplectic map, positive
roof, or same-object repetition law.

| Gate | Evidence | Status | Decision |
| --- | --- | --- | --- |
| P0 | symbolic source only | not admitted | stop |
| A0 | squarefree sieve is genuine provenance, but supplies no prime clock | scoped FAIL | no promotion |
| A1 | exact absence of nonzero symbolic periodic points | scoped FAIL | no lift/orbit computation |
| A2 | no same-object orbit ledger | NOT EVALUATED | unassigned |
| Route B | no Route-A-ready candidate | NOT INVOKED | prohibited |

## Evidence index

- [Candidate scope card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Phase-I prior-work index](../../docs/prior_work/README.md)
