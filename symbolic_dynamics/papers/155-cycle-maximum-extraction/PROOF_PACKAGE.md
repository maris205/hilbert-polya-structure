# P155 proof package

## Claim

For `pi in S_n`, order its disjoint-cycle supports `B_1,...,B_m` by increasing
minimum and define

```text
C(pi)=std(max B_1,...,max B_m).
```

The frozen theorem asks for the exact source-rank image threshold, a right
section at every admissible rank, all target fibres, and the recurrent-state
classification.  It does not ask for an absorption clock.

## Status

`PROVABLE AS STATED` under the reduced freeze contract.

## Assumptions and notation

- Permutations are bijections of `[n]`; cycle supports are nonempty and
  disjoint.
- `sigma in S_m`, `r=rlmin(sigma)`, and `mu(sigma)=2m-r`.
- `P_n(sigma)` is the set of ordered set partitions of `[n]` whose block
  minima increase and whose block maxima standardize to `sigma`.
- The map acts on `S_<=N`, the disjoint union of positive ranks.

## Dependency map

1. Singleton support necessity gives the lower image bound.
2. The opener/closer/simultaneous scheduler attains that bound.
3. Event splitting and interior insertion extend the minimum section to all
   larger ranks.
4. Unique support partitions and independent cyclic orders prove every fibre.
5. Output rank equal to cycle count proves strict descent and recurrence.
6. The image census is a corollary using the classical RTL-minimum Stirling
   distribution.

## Proof

### Lemma A: singleton capacity

If block `B_i` is singleton, then for every `j>i`,

```text
max B_j >= min B_j > min B_i = max B_i.
```

Thus `sigma_i` is a right-to-left minimum.  At most `r` blocks are singleton;
the remaining `m-r` blocks use at least two coordinates.  Every source rank
therefore satisfies

```text
n >= r+2(m-r)=2m-r=mu(sigma).
```

### Lemma B: minimum endpoint schedule

Use opener order `O_1<...<O_m` and closer order `K_1<...<K_m`, pairing
`O_i` with `K_(sigma_i)`.  At a state with `i` openers and `j` closers already
emitted:

1. if the next opener is an RTL-minimum position and its paired closer is
   `K_(j+1)`, emit them simultaneously;
2. else if the opener paired to `K_(j+1)` has appeared, emit that closer;
3. else emit the next opener.

The scheduler never stalls.  For an RTL-minimum position `i` with value `v`,
all values below `v` occur earlier, so their openers are available and closer
priority exhausts `K_1,...,K_(v-1)` before `O_i`.  Hence `O_i` and `K_v` are
simultaneous.  No other position is made simultaneous.  The schedule length
is `2m-r`.

Giving successive ground-set labels to the events produces ordered supports:
opener order gives increasing minima, closer order gives maxima of relative
order `sigma`.  Put an increasing canonical cycle on each support to obtain a
literal permutation source.

### Lemma C: every larger rank

Splitting one simultaneous event into adjacent opener and closer events adds
one coordinate and preserves both endpoint orders.  After all simultaneous
events are split, insert any further coordinate strictly inside one open
block.  Hence a support source exists at every `n>=mu(sigma)`.

### Lemma D: weighted fibres

A source determines its support family uniquely.  A fixed labelled support
of size `b` carries exactly `(b-1)!` cyclic orders.  Choices on disjoint
supports are independent.  Conversely, an ordered support family with the
required maxima, together with one cycle on each block, determines a unique
source.  Therefore

```text
|C_n^(-1)(sigma)| =
  sum_(B_1,...,B_m in P_n(sigma)) prod_i (|B_i|-1)!.
```

### Lemma E: recurrence

`|C(pi)|` equals the number of cycles of `pi`.  If it equals source rank `n`,
all cycles are singleton, so `pi=id_n`.  Identities are fixed.  Every other
step strictly decreases positive rank and cannot lie on a cycle.

### Corollaries

The number of targets in `C(S_n)` is

```text
sum_(m=1)^n sum_(r=max(1,2m-n))^m [m r],
```

because `[m r]` counts permutations with `r` right-to-left minima.  At the
minimum source rank all blocks have size one or two, so every fibre weight is
one and the minimum-rank fibre equals the number of feasible support families.

## Excluded interface

Finite maxima through rank ten suggest a power threshold, but there is no
all-parameter proof of the necessary lower bound.  The proof package therefore
contains no maximum clock, pointwise tail formula, or global iterated-preimage
minimality statement.

