# A stationary prime-gap language has primitive words but imports its arithmetic rule

**Paper ID:** `041-prime-gap-language-screen`  
**Record ID:** `ASFS-SCOUT-20260914-30`  
**Date / status:** `2026-09-14; A1 SYMBOLIC POSITIVE CONTROL; PRE-P0 STOP — PRIME PREDICATE IS EXTERNAL TO THE SHIFT`  
**Route state:** `No classical candidate; Route A not evaluated; Route B NOT INVOKED`

## Abstract

Actual prime-indicator and consecutive-prime-gap orbit closures have no useful
periodic core (015, 027). This alternate stationary symbolic language permits
only prime-length zero gaps. It therefore has exact primitive words
`(10^p)^infty`, but the prime predicate was declared in advance. The shift does
not generate or test it. This is an A1 symbolic positive control and an A0
ownership stop, not a Hénon or symplectic candidate.

## 1. Object and lineage

Let

`X_P={x in {0,1}^Z : every finite zero-run between consecutive 1s has prime length}`

with shift `sigma`. This realizes only

```text
prime predicate -> symbolic admissibility.
```

It is not the actual consecutive-prime-gap word or its closure. It also owns
no smooth phase space, symplectic map, roof, suspension, or analytic object.

## 2. Exact primitive periodic words

For prime `p`, put `x_p=(10^p)^infty`. Every zero-run has length `p`, hence
`x_p` lies in `X_P` and `sigma^(p+1)x_p=x_p`. It has one `1` per block of
length `p+1`; any shift period must preserve the set of one-positions, whose
least positive spacing is `p+1`. Hence its least period is `p+1`.

Thus the shift has intrinsic symbolic primitive cycles and, under its own unit
suspension convention only, repetitions of length `r(p+1)`. This does not
create a prime-log clock or transfer any roof/zeta from another object.

## 3. A0 failure and controls

The map `sigma` merely translates a word. It neither computes primality nor
derives the permitted gap set from an internal state. Replacing primes by any
chosen infinite allowed-length set gives an equally stationary subshift with
the same kind of periodic construction. The arithmetic content is therefore
external language data.

Embedding selected `X_P` itineraries into a Hénon horseshoe would preserve
this defect: the language, rather than the map, selects arithmetic. That is
the ownership failure of 012. The contrast with 015 and 027 is intentional:
their actual arithmetic sequences have degenerate/no periodic cores, whereas
this artificial stationary language has cycles precisely because it relaxes
the requirement of reproducing those sequences.

## 4. Gate decision

| Gate | Evidence | Status |
| --- | --- | --- |
| A0 | primality is a supplied language predicate | `scoped FAIL` |
| A1 | exact symbolic primitive cycles and repetitions | `symbolic positive control only` |
| A2 | no same-object operator or analytic owner | `NOT EVALUATED` |
| Route B | no P0 or Route-A candidate | `NOT INVOKED` |

**Portfolio position: stop/fork.** Retain `X_P` only as a sharp control:
stationarity and periodic words are cheap once arithmetic is inserted into the
language. A viable candidate must derive its admissibility from the same
map/flow rather than predeclare primality.
