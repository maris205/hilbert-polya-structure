# Proof package — P149

## Claim

Let `S_{<=N}` be the finite disjoint union of the symmetric groups of ranks
`1,...,N`.  Give a permutation fictitious neighbour value zero at both ends,
read its local-maximum values from left to right, and standardize the resulting
nonempty word.  Call this self-map `P`.

For every `n,k>=1`:

1. `P^k(S_n)` is the disjoint union of all `S_m` with
   `1<=m<=ceil(n/2^k)`, and its cardinality is the corresponding sum of
   factorials.  Every target has an explicit right section.
2. The singleton is the unique recurrent state and

   $$\max_{\pi\in S_n}\tau(\pi)=\lceil\log_2n\rceil.$$

3. For every target `sigma in S_m`, the one-step multiplicity from `S_n`
   equals the sum, over comparison words having `m` endpoint-inclusive peak
   positions, of the linear-extension counts of the adjacent-comparison
   posets augmented by the target peak-value order.

## Status

**PROVABLE AS STATED.**  The frozen claims survive unchanged.

## Assumptions

- Permutations use positive values `1,...,n`, so the fictitious boundary
  value zero is below every genuine entry.
- Standardization replaces the smallest selected value by one, the next by
  two, and so on.
- `tau(pi)` is the least number of iterations needed to reach the singleton.
- The carrier is the finite disjoint union `S_{<=N}`; the map does not preserve
  an individual rank.

## Notation

- `p(pi)=|P(pi)|`: output rank.
- `L_{n,m}(sigma)`: the explicit one-step lift of `sigma in S_m` to rank `n`.
- A comparison word has letter `U` at position `i` when `pi_i<pi_{i+1}` and
  `D` otherwise.
- `e(Q)`: number of linear extensions of a finite poset `Q`, read from
  smallest value to largest.

## Proof strategy

Prove a sharp one-step packing bound and an explicit section.  Compose that
section along a backward chain of minimal odd lengths to obtain every iterate
image.  Lift a deepest witness recursively to prove the sharp clock.  For the
fibre, partition sources by their unique comparison words and translate value
assignments into linear extensions.

## Dependency map

1. Carrier closure and strict descent depend on nonempty, nonadjacent peak
   positions.
2. Every iterate image depends on one-step packing, the explicit one-step
   section, and the ceiling/minimal-length equivalence.
3. The sharp clock depends on packing and a recursively lifted witness.
4. The fibre formula depends on the uniqueness of a comparison word and the
   standard rank-assignment/linear-extension bijection.

## Proof

### Step 1: nonempty output, packing, and recurrence boundary

The global maximum of a permutation exceeds both genuine neighbours; at an
endpoint it also exceeds the fictitious zero.  Thus the selected word is
nonempty.  Two peak positions cannot be adjacent, because adjacent entries
cannot each exceed the other.  Hence

$$1\le p(\pi)\le\left\lceil\frac n2\right\rceil.$$

If `n>1`, the upper bound is strictly below `n`, so rank decreases at every
nonsingleton state.  The one-letter permutation is fixed and is therefore the
unique recurrent state.

### Step 2: explicit one-step right section

Fix `sigma=sigma_1...sigma_m in S_m` and `n>=2m-1`.  Define the high values

$$h_i=n-m+\sigma_i\qquad(1\le i\le m).$$

They are exactly the values `n-m+1,...,n` in target relative order.  Form

$$
L_{n,m}(\sigma)=
h_1,1,h_2,2,\ldots,m-1,h_m,
n-m,n-m-1,\ldots,m,
$$

where the final decreasing block is omitted when empty.  The inequality
`n>=2m-1` makes all listed low-value sets disjoint and exhaustive.

The first high exceeds the fictitious left boundary and its following valley.
Every interior high lies between two smaller valleys.  The last high exceeds
its left valley and, if present, the first value of the decreasing tail; if no
tail is present it exceeds the fictitious right boundary.  Thus every high is
a peak.  Each inserted valley has a high neighbour, and every entry in the
terminal decreasing block has a larger left neighbour, so no low value is a
peak.  The peak-value word is `h_1...h_m`, whose standardization is `sigma`.
Therefore

$$P(L_{n,m}(\sigma))=\sigma.$$

Together with Step 1, this proves the exact one-step image.

### Step 3: all iterate images and sections

Repeated packing gives

$$
|P^k(\pi)|\le
\left\lceil\frac1{2}\left\lceil\cdots
 \left\lceil\frac n2\right\rceil\cdots\right\rceil\right\rceil
=\left\lceil\frac n{2^k}\right\rceil.
$$

For the reverse inclusion, fix `sigma in S_m` with
`m<=ceil(n/2^k)`.  This integer inequality is equivalent to

$$n\ge 2^k m-(2^k-1).$$

Set `a_k=m` and, backward for `j=k-1,...,1`, set
`a_j=2a_{j+1}-1`.  Then `a_1=2^(k-1)m-(2^(k-1)-1)` and the preceding
inequality says `n>=2a_1-1`.  Starting with `sigma_k=sigma`, define

$$
\sigma_j=L_{a_j,a_{j+1}}(\sigma_{j+1})
\quad (j=k-1,\ldots,1),
$$

and finally put `pi=L_{n,a_1}(sigma_1)`.  Step 2 gives
`P(sigma_j)=sigma_{j+1}` and `P(pi)=sigma_1`, so `P^k(pi)=sigma`.
This is an explicit right section for every feasible target and proves

$$P^k(S_n)=\bigsqcup_{1\le m\le\lceil n/2^k\rceil}S_m.$$

The ranks are disjoint in the carrier, hence the cardinality is

$$\sum_{m=1}^{\lceil n/2^k\rceil}m!.$$

### Step 4: sharp clock

Step 1 implies that every orbit from rank `n` reaches rank one by
`ceil(log2 n)` steps.  To attain the bound for every `n`, define recursively
`w_1=(1)` and, for `n>1`,

$$w_n=L_{n,\lceil n/2\rceil}
      (w_{\lceil n/2\rceil}).$$

The one-step section is feasible because
`n>=2ceil(n/2)-1`.  It satisfies

$$P(w_n)=w_{\lceil n/2\rceil}.$$

Consequently

$$
\tau(w_n)=1+\tau(w_{\lceil n/2\rceil})
=\lceil\log_2n\rceil,
$$

where the last identity follows by locating `n` between consecutive powers of
two.  This proves the sharp maximum.

### Step 5: comparison words and peak positions

For `n>1`, let `w=w_1...w_{n-1}` be a word over `{U,D}`.  Its
endpoint-inclusive peak positions are determined as follows:

- position one is a peak exactly when `w_1=D`;
- an interior position `i` is a peak exactly when
  `w_{i-1}=U` and `w_i=D`;
- position `n` is a peak exactly when `w_{n-1}=U`.

For `n=1`, the empty word has the unique position as its peak.  Every
permutation has one and only one such comparison word.

Let the peak positions of `w` be `p_1<...<p_m`.  Define the adjacent
comparison poset by the relations

$$
i<_Q i+1\quad\text{if }w_i=U,
\qquad
i+1<_Q i\quad\text{if }w_i=D.
$$

For a target `sigma in S_m`, add the chain

$$
p_{\sigma^{-1}(1)}<_Q p_{\sigma^{-1}(2)}<_Q\cdots
<_Q p_{\sigma^{-1}(m)}.
$$

Each base peak is maximal in the adjacent-comparison poset, so adding a total
order among peaks cannot create a directed cycle.  The result is a poset,
denoted `Q(w,sigma)`.

### Step 6: target-resolved fibre

A linear extension of `Q(w,sigma)`, listed from smaller to larger, assigns
values `1,...,n` to positions.  The adjacent relations force comparison word
`w`.  The added peak chain forces the left-to-right peak-value word to have
standardization `sigma`.  Conversely, a permutation with comparison word `w`
and extracted target `sigma` orders its positions by increasing value and
thereby gives a unique linear extension of `Q(w,sigma)`.

Thus the permutations in the target fibre having a fixed comparison word `w`
are counted by `e(Q(w,sigma))`.  Comparison words partition the fibre, so

$$
|P^{-1}(\sigma)\cap S_n|
=\sum_{\substack{w\in\{U,D\}^{n-1}\\
                  w\text{ has }m\text{ endpoint peaks}}}
 e(Q(w,\sigma)).
$$

If `m>ceil(n/2)`, the indexing set is empty and both sides are zero.  The
`n=m=1` case has one empty comparison word and one linear extension.  All
frozen claims follow.

## Corrections or missing assumptions

None.  The endpoint-zero convention and variable-rank carrier must remain
explicit.

## Open risks

- Static pinnacle sets and admissible pinnacle orderings are directly owned
  and must remain zero-credit background.
- The comparison-poset fibre is mathematically complete but uses standard
  technology; it must remain secondary to the iterate-image/section theorem.
- The primary-source audit is bounded and supplies no novelty or priority
  certificate.
