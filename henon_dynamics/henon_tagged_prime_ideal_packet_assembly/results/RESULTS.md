# Results

## Exact finite ledger

For the three signed primitive H6 controls and indices `3..20`:

- packet rows: 54;
- tagged trace-field prime-ideal atoms: 125;
- distinct rational primes after norm pushforward: 95;
- free kernel rank of the rational-prime pushforward: 30;
- good-characteristic atoms with exact residue-order certification: 105;
- bad-characteristic atoms deliberately left uncertified: 20;
- collision primes: 12;
- cross-orbit collision primes: 11;
- cross-index collision primes: 11;
- distinct multi-order collision primes: 7;
- inherited P49 half-norm crosschecks: 30/30.

Canonical core digest:

```text
9cc40f4b8ed5f54e36c70cb1db15b509837aee264e86bcf39395f827e59153ba
```

## Decisive collisions

The same rational prime can carry incompatible intrinsic clocks:

| rational prime | tagged good residue orders | interpretation |
|---:|---|---|
| 29 | 7, 14, 15 | two period-three packets and one period-one packet |
| 131 | 5, 12 | period-three versus period-one |
| 38039 | 13, 19 | period-four versus period-three |
| 19 | 3, 10, 20 | period-one and period-four good rows; the period-three `n=19` row is bad characteristic |

At `p=109,n=11`, the period-one trace field contributes two distinct split
prime ideals, while the period-three trace field contributes a third.  This
single row proves that the orbit tag and prime-ideal tag cannot both be
discarded even when `p` and `n` are retained.

## Strongest positive result

The direct sum of tagged trace-field divisor groups gives a canonical,
lossless finite-cutoff packet ledger.  Its rational norm pushforward is exact.
At every atom of residue characteristic not dividing the cyclotomic index,
any extending multiplier-field prime has residue order exactly that index.

## Strongest obstruction

The untagged rational-prime pushforward is noninjective.  It loses orbit,
index, prime-ideal, and residue-clock data.  It cannot be treated as a unique
source-native H6 Euler clock.  This is HEN-O90.

## Open theorem

Construct a pressure-weighted all-primitive-orbit limit of the tagged ledger,
with a convergent vector-valued trace and a justified rational pushforward.
Nothing here proves a von Mangoldt main term, analytic continuation,
functional equation, or operator determinant.
