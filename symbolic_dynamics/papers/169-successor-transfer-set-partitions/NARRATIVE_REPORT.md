# P169 narrative report

## Outcome

Successor transfer is a literal self-map of canonically ordered set
partitions.  Every nonsingleton block simultaneously removes its maximum and
places that label in the next block around a directed cycle; singleton blocks
do nothing.  Canonical block order is preserved by the update.  In the
restricted-growth word, the same map simultaneously changes the final
occurrence of every repeated letter `i` to `i+1 mod k`.

The exact package has two information-theoretically different axes.  The
temporal proof first forgets all labels except the excess block loads and then
uses one canonical prefix or suffix window.  It yields a sharp clock in every
`(n,k)` stratum and a complete classification and census of recurrent states.
The inverse proof instead keeps the actual order of labels inside every target
block.  A five-state local product gives the fibre of every target and a
complete image test.  Targets with identical block size/minimum/maximum data
can have different fibres, so the second axis is not determined by the load
factor or by coarse endpoint data.

The internal gate classified the package as
`GREEN_OWNER_THIN / HOLD_EXTERNAL`.  Restricted-growth encodings and
whirling, directed-cycle chip firing, Bulgarian solitaire, promotion and jeu
de taquin, box-ball systems, set-partition stack sorting, Stirling counts, and
generic transfer-matrix algebra are treated as background.  The bounded owner
search does not authorize external circulation.

## Literal system

Let `[n]={0,...,n-1}` and write a partition in canonical minimum order as

```text
(B_0,...,B_(k-1)),  min B_0 < ... < min B_(k-1).
```

Every block of size at least two donates its maximum to its successor, with
indices modulo `k`.  Removal and addition are simultaneous.  A donating block
retains its minimum.  For adjacent output blocks, every element that may enter
the later block is larger than the retained minimum of the earlier block, so
the minimum order remains strict.  In particular, the cyclic transfer does not
silently induce a second permutation of block indices.

Under the standard restricted-growth encoding, block `i` is the set of
positions carrying letter `i`.  Removing its maximum changes its last
occurrence, and the destination is letter `i+1 mod k`.  The first occurrence
of every nonzero letter remains after a first occurrence of its predecessor,
so the result is again a restricted-growth word with exactly `k` letters.

## Temporal axis

Put `z_i=|B_i|-1` and `m=n-k`.  The load factor obeys

```text
z_i' = z_i - 1[z_i>0] + 1[z_(i-1)>0].
```

This is the threshold-one parallel chip-firing rule on a directed cycle and
receives no independent contribution credit.  A periodic height lift converts
it to

```text
H_i(t+1)=max(H_i(t)-1,H_(i-1)(t)).
```

The explicit max-plus solution proves that a mass `m<=k` becomes binary by
time `m-1`, whereas a mass `m>=k` becomes positive everywhere by time `k-1`.
The two regimes are invariant.

Labels then settle within at most `k-1` more steps.  In the dense regime, the
last `k` word positions evolve as a mass-`k` queue and become a permutation of
all letters.  In the sparse regime, the first `k` positions have occupancies in
`{0,1,2}`; excesses move clockwise into holes until that prefix is the
canonical word `01...(k-1)`.

For `1<k<n`, these two phases give the sharp stratum clock

```text
max tau on Pi_(n,k) = min(n-2, 2k-2).
```

The single family `0^(n-k+1)12...(k-1)` attains it in every nontrivial
stratum.  The one-block and all-singleton states are fixed.  Consequently the
global clock is `n-2` for `n>=2`, including the zero clock at `n=2`.

The recurrent classification is equally explicit.  When `n>=2k`, the first
`n-k` letters are a surjective restricted-growth word on all `k` letters and
the last `k` letters are a permutation.  When `n<=2k`, the first `k` letters
are `01...(k-1)` and the final `n-k` letters are distinct.  At `n=2k` the two
descriptions and counts agree.  Every nontrivial recurrent `k`-block state has
exact period `k`; its census is

```text
k! S(n-k,k)        if n>=2k,
(k)_(n-k)          if n<=2k.
```

For `n>=2` the possible periods across all strata are exactly
`1,...,n-1`; at `n=1` the unique state is fixed.

## Inverse axis

Fix a canonical target `C=(C_0,...,C_(k-1))`.  Let `x_i` be absent if source
block `i` is a singleton and otherwise be the maximum it donated into
`C_(i+1)`.  A predecessor must be

```text
B_i = (C_i minus {x_(i-1)}) union {x_i},
```

with absent deletion or addition omitted.  Relative to a target block, an
incoming token has five possible types: absent, the sole element, the minimum,
the maximum, or an interior element.  Deleting an element of a fixed type has
type-determined size and extrema.  This makes the predecessor conditions
local: an absent outgoing token requires a singleton retained part; a present
outgoing token must strictly exceed the retained maximum; and only the linear
adjacencies `i<k-1` compare retained minima.  The trace of the resulting five
by five matrices closes the cyclic token states without adding a false
last-to-first minimum comparison.

The manuscript prints both the complete entry rule and four numerical
matrices.  In state order `(absent,singleton,minimum,maximum,interior)`, they
give fibre two for `025|134` and fibre one for `035|124`.  The two targets have
identical ordered `(size,minimum,maximum)` block data.  Their literal
predecessors are respectively

```text
023|145, 024|135
```

and

```text
034|125.
```

This is the promised interlacing-sensitive target fibre axis.

## Evidence and scope

The standalone verifier uses only the Python standard library.  It checks all
set partitions through `n=10`, all 26,442 targets through `n=9`, 532,467
queue-cone cases, and the sharp family in every nontrivial stratum through
`n=50`.  Its frozen run contains 1,217,025 exact assertions.  Enumeration is
a control, not a premise of the all-parameter proofs.

The note is an anonymous Round-0 author freeze.  Its lifecycle remains
`HOLD_EXTERNAL` pending the coordinator's later specialist process.
