# P156 proof package

## Claim

For `pi=pi_1...pi_n`, define

```text
W(pi)=std(pi_i : pi_i>=i).
```

For every target, resolve its exact source-rank image threshold and fibres;
classify recurrence; and prove the exact dynamics of the canonical
minimum-one-step-rank right section.  Do not claim a global maximum clock.

## Status

`PROVABLE AS STATED` under the reframed freeze contract.

## Assumptions and notation

- `sigma in S_m`, `d(sigma)=max_i(i-sigma_i)`, and source rank `n=m+h`.
- Selected values are `A={a_1<...<a_m}` and selected positions are
  `P={p_1<...<p_m}`.
- Complements are `B=[n]\A` and `Q=[n]\P={q_1<...<q_h}`.
- `tau` is first hitting time of an identity in the rank-varying carrier.

## Dependency map

1. Selected position/value inequalities prove image necessity.
2. The high-shift/low-tail section proves sufficiency and one-step minimality.
3. The deficient complement matching proves every target fibre.
4. Equal rank plus equal coordinate sums proves identity-only recurrence.
5. Direct maximum-drop calculation on the minimum section proves the resource
   update.
6. Fibonacci matrix powers and the forward section identity prove the tower
   formula and tail shift.

## Proof

### Lemma A: exact image threshold

If `W(pi)=sigma`, the entry at selected position `p_i` is
`a_(sigma_i)`.  Selection and ordering give

```text
i <= p_i <= a_(sigma_i).
```

Only `h` source values are outside `A`, hence `a_j<=h+j`.  Therefore

```text
i <= h+sigma_i,
```

so `d(sigma)<=h`.  Conversely, if `h>=d(sigma)`, then

```text
R_n(sigma)=(sigma_1+h,...,sigma_m+h,1,...,h)
```

has its first `m` entries on or above the diagonal and its low tail strictly
below it.  The retained word standardizes to `sigma`.  Thus the exact minimum
source rank is `m+d(sigma)`.

### Lemma B: every-target fibre

For `n<m`, rank alone makes the fibre empty. For `n=m`, the complement sets
are empty, the empty product is one, and admissibility forces `sigma=id_m`.
Assume below that `n>=m`.

Fix selected sets `A,P`.  The selected assignment is forced and is valid
exactly when `p_i<=a_(sigma_i)`.  Process complement positions increasingly.
At `q_j`, the number of eligible complement values is

```text
#{b in B:b<q_j}-(j-1).
```

All `j-1` values used earlier are included in the first term because they were
assigned below earlier, smaller positions.  Multiplication gives the number
of deficient bijections for this board.  Every source determines a unique
board and completion; conversely every admissible board and completion gives
a unique source.  Summing proves the formula, including zeros.

### Lemma C: recurrent states

Equal source and target rank means every source position was selected, so
`pi_i>=i` for every `i`.  Since the sums of the two permutation words are
equal, every inequality is equality and `pi=id_n`.  Identities are fixed, and
every other step drops rank.

### Lemma D: canonical inverse resource update

For nonidentity `sigma`, `d(sigma)>0`.  Apply the minimum-rank section with
`h=d`.  Each high entry has drop

```text
i-(sigma_i+d)<=0,
```

while low value `j` at position `m+j` has drop exactly `m`.  Hence

```text
(m,d) -> (m+d,m),       W(R(sigma))=sigma.
```

The image theorem proves this is minimum rank among all one-step preimages.

### Lemma E: Fibonacci tower and time shift

Iterating the matrix `[[1,1],[1,0]]` gives, for `t>=1`,

```text
m_t=F_(t+1)m+F_t d,
d_t=F_t m+F_(t-1)d.
```

Every lifted state is nonrecurrent and maps in one step to its predecessor,
so `tau(sigma^(t))=tau(sigma)+t`.

## Exact owner subtraction

The Bell enumeration

```text
sum_m |W_n^(-1)(id_m)|=B_n
```

is owned by Beyene–Backelin–Mantaci–Fufa Theorem 27 and receives zero credit,
as do the Baril transposition-array interface, weak-excedance statistics,
bounded-drop enumeration, tableau/Bruhat structures, and generic Ferrers
matching.

## Excluded interface and exact falsifier

The old pointwise statement `tau(W(pi))<=M(d(pi))` is false at

```text
pi=(11,10,9,4,1,2,3,8,5,6,7),
W(pi)=(5,4,3,1,2), d(pi)=4.
```

The target tail is three while the maximum tail in `S_4` is two.  No pointwise
drop clock, global maximum clock, or global `t`-step preimage minimum remains
in the proof package.
