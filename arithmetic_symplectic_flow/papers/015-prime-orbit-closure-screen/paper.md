# Prime-symbolic orbit closure: periodic points without an arithmetic orbit ledger

**Paper ID:** `015-prime-orbit-closure-screen`  
**Record ID:** `ASFS-SCOUT-20260913-13`  
**Date / status:** `2026-09-13; PRE-P0 NEGATIVE SCREEN`  
**Route state:** `No frozen candidate; Route A coordinates not evaluated; Route B NOT INVOKED`

## Abstract

Rather than use an advancing sieve stage as a clock, form the shift-orbit
closure of the actual prime/composite indicator word. This is a canonical
autonomous symbolic object directly descended from the programme's starting
point. It has exactly one periodic point: `0^infinity` belongs to the closure
because factorials give arbitrarily long composite runs, while a congruence
argument excludes every periodic word containing a prime symbol. That is
adverse evidence, not A1 credit. The fixed point has no prime label or
endogenous logarithmic period, and no finite-dimensional symplectic map or roof
is supplied. Stop before P0.

## Construction and exact calculation

Define `a_n=1` for prime `n` and `a_n=0` otherwise, and set
`X_p=closure{sigma^j(a):j>=0}`. For every `L>=1`, the integers
`(L+1)!+2,...,(L+1)!+(L+1)` are composite. Hence the prime word contains zero
blocks of every length. Shifting to their beginning as the length tends to
infinity gives `0^infinity` in `X_p`; the shift fixes it.

## Exact periodic-core obstruction

**Proposition.** The only periodic point of `X_p` is `0^infinity`.

**Proof.** Let `x` in `X_p` have period `q>0` and suppose `x_r=1` at one
residue `r mod q`. Take shifts `n_i` with `sigma^{n_i}(a)` converging to `x`.
First suppose these shifts are unbounded. Choose a prime `p` not dividing `q`
and pass to a subsequence having `n_i=c mod p`. Choose a sufficiently large
nonnegative `k` with `c+r+kq=0 mod p` (add multiples of `p` to any solution).
For all sufficiently large `i`, the positive integer
`n_i+r+kq` is a multiple of `p` larger than `p`, hence composite. The relevant
coordinate of every approximant, and therefore `x_{r+kq}`, is zero. This
contradicts periodicity and `x_r=1`.

If the shifts are bounded, a constant subsequence makes `x` an actual shift of
the prime indicator. The same choice of `p` and a sufficiently large
nonnegative solution of `n+r+kq=0 mod p` gives a composite coordinate
where periodicity would demand a one. Thus no periodic `x` contains a one.
The factorial-block argument above supplies `0^infinity`, completing the proof.

## Why the periodic core does not pass A0 or A1

The sole fixed point is a limiting all-composite word, not a prime, prime power,
or primitive family whose time is derived as `log p`. Counting it as one would
transfer a symbolic repeat to a different, unowned clock. Further, `X_p` has no
specified finite-dimensional smooth manifold, symplectic form, map, positive
roof, or primitive-orbit/repetition convention. It is distinct from record 014:
this route has symbolic recurrence, but its entire periodic core is degenerate
for arithmetic use.

## Controls and decision

- A density-matched binary word with arbitrarily long zero blocks has the same
  fixed point, so its presence is not a prime discriminator.
- No horseshoe, cotangent lift, determinant, or operator is borrowed.

| Gate | Evidence | Status | Decision |
| --- | --- | --- | --- |
| P0 | symbolic carrier only; no smooth symplectic map or roof | not admitted | stop |
| A0 | periodic core is nonarithmetic | scoped FAIL | no clock credit |
| A1 | exact absence of nonzero symbolic periodic points; zero point has no suspension ledger | scoped FAIL | do not promote |
| A2 | none | NOT EVALUATED | unassigned |
| Route B | no Route-A-ready candidate | NOT INVOKED | prohibited |

A future fork needs an intrinsic geometric realization that controls which
periodic words survive and derives an arithmetic roof without adding it by hand.

## Evidence index

- [Candidate scope card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Phase-I prior-work index](../../docs/prior_work/README.md)
