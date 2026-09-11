# Proof Package

## Claim

For every integer `n>=1`, let `X_n={0,1}^{n x n}` and define

`F(A)_{ij}=1{i<=r_j(A)}` for `1<=i,j<=n`,

where `r_j(A)` is source row `j`'s sum.  The claimed package is:

1. exact formulas for `F(A),F^2(A),F^3(A),F^4(A)`, in particular
   `F^4=F^2`;
2. complete recurrent, fixed, strict-two-cycle, and exact depth-layer
   descriptions and counts;
3. exact every-target fibre formulas for `F` and `F^2`, including zero
   fibres, and image sizes `(n+1)^n` and `binom(2n,n)`;
4. the full `n=1` boundary.

## Status

**PROVABLE AS STATED.**  The original theorem contract survives unchanged.

## Assumptions

- Matrices are square, binary, and have fixed labelled row and column orders.
- The update is synchronous and deterministic.
- Indices are `1,...,n`; no sorting is part of the literal update.
- Partitions are padded by zeros to length `n` and fit in the `n x n` square.

## Notation

- `r(A)=(r_1,...,r_n)` is the labelled row-sum vector.
- `D(h)_{ij}=1{i<=h_j}` is the column-initial matrix of height vector `h`.
- `h^*=(#{j:h_j>=i})_{i=1}^n` is the threshold transform.
- `h^downarrow` is the decreasing rearrangement.
- `P_n` is the set of partitions in the `n x n` square, padded to length `n`.
- `m_k(lambda)` is the multiplicity of part `k`, including `k=0`.
- Depth is distance to the recurrent set.

## Proof Strategy

Factor the literal update as `F=D o r`.  Compute `r o D` independently as
the threshold transform.  Its double application sorts an arbitrary height
vector, and on partitions it is ordinary conjugation.  This proves the
temporal identity before any counting.  Count recurrent shapes by boundary
paths and fixed shapes by diagonal hooks.  For inverse laws, reconstruct
source rows directly, once with prescribed labelled sums and once with a
prescribed multiset of sums.

## Dependency Map

1. The four-iterate formula depends only on `F=D o r`, `r(D(h))=h^*`, and
   `(h^*)^*=h^downarrow`.
2. Recurrence and periods depend on `F^4=F^2` plus the characterization of
   `Fix(F^2)` as `D(P_n)`.
3. Depth layers depend on the separate equivalence
   `F(A) recurrent <=> r(A) is decreasing`.
4. Time-one fibres depend on independent support choices within labelled
   rows.
5. Time-two fibres depend on `r(A)^*=mu`, equivalently the row-sum multiset
   is `mu^*`, followed by multinomial assignment and independent supports.
6. Counts of recurrent and fixed shapes use the classical boundary-path and
   diagonal-hook bijections; both are also proved in the paper.

## Proof

### Step 1: height calculus

The map `D` is injective because each column height is recovered from its
initial run of ones.  Directly counting the ones in row `i` of `D(h)` gives

`r_i(D(h))=#{j:h_j>=i}=h_i^*`.

The vector `h^*` is decreasing.  Because threshold counts ignore coordinate
order, `h^*=(h^downarrow)^*`.  Applying the Ferrers-diagram conjugation twice
to the partition `h^downarrow` gives

`(h^*)^*=h^downarrow`.

### Step 2: all four iterates

Put `r=r(A)`.  The definition and Step 1 give successively

```text
F(A)   = D(r),
F^2(A) = D(r^*),
F^3(A) = D((r^*)^*) = D(r^downarrow),
F^4(A) = D((r^downarrow)^*) = D(r^*).
```

Thus `F^4=F^2`, and for every later time the two displayed recurrent phases
alternate.

### Step 3: recurrent dynamics

Identity `F^4=F^2` shows that every `F^2(A)` is fixed by `F^2`.  Conversely,
on a periodic orbit `F` is invertible; cancelling `F^2` from `F^4=F^2`
shows that every period divides two.  Hence the recurrent set is `Fix(F^2)`.

Every second image is `D(mu)` for the partition `mu=r(A)^*`.  Conversely, if
`mu` is any partition in the square, then

`F(D(mu))=D(mu^*)` and `F^2(D(mu))=D(mu)`.

Therefore recurrent states are exactly the Ferrers matrices `D(mu)`, and
conjugation is the recurrent action.  Boundary paths from northwest to
southeast give `|P_n|=binom(2n,n)`.  A recurrent state is fixed exactly when
`mu=mu^*`.  Diagonal hooks identify self-conjugate shapes in the square with
subsets of `{1,3,...,2n-1}`, so there are `2^n` fixed states.  The remaining
recurrent states pair into

`(binom(2n,n)-2^n)/2`

strict two-cycles.

### Step 4: exact depth sets and counts

The first image `D(r(A))` is recurrent exactly when the labelled vector
`r(A)` is decreasing.  Consequently:

- depth zero: the Ferrers matrices `D(mu)` with `mu in P_n`;
- depth one: matrices with decreasing row-sum vector that are not Ferrers;
- depth two: matrices whose row-sum vector has an ascent.

For a fixed decreasing row-sum vector `lambda`, row `i` has
`binom(n,lambda_i)` independent supports.  Hence

`W_n=sum_{lambda in P_n} product_i binom(n,lambda_i)`

counts all states of depth at most one.  Equivalently, encoding multiplicities
of the possible row sums gives

`W_n=[z^n] product_{k=0}^n (1-binom(n,k)z)^(-1)`.

Thus the exact populations are

```text
N_0=binom(2n,n),
N_1=W_n-binom(2n,n),
N_2=2^(n^2)-W_n.
```

For `n>=2`, a non-left-compressed first row of sum one followed by zero rows
realizes depth one, while row sums `(0,1,0,...,0)` realize depth two.  Thus the
height is exactly two.  For `n=1`, both matrices are Ferrers and fixed, so the
height is zero and `(N_0,N_1,N_2)=(2,0,0)`.

### Step 5: time-one every-target fibres

A target `B` has a predecessor exactly when every column is an initial
segment; then `B=D(h)` for a unique `h in {0,...,n}^n`.  The equation
`F(A)=D(h)` is equivalent to `r_j(A)=h_j` independently for each labelled
row.  Therefore

`|F^{-1}(B)|=product_j binom(n,h_j)`.

It is zero for every other target.  Injectivity of `D` gives
`|im F|=(n+1)^n`.

### Step 6: time-two every-target fibres

A target has a second predecessor exactly when it is `B=D(mu)` with
`mu in P_n`.  Since `F^2(A)=D(r(A)^*)`, the required condition is
`r(A)^*=mu`.  Applying the threshold transform again shows that the
decreasing rearrangement of `r(A)` must be `lambda=mu^*`, and this condition
is sufficient.

There are `n!/product_k m_k(lambda)!` ways to assign the multiset of parts of
`lambda` to the labelled rows.  For each assignment, the row supports can be
chosen in `product_i binom(n,lambda_i)` ways.  Hence

```text
|(F^2)^(-1)(D(mu))|
 = n! / product_k m_k(lambda)! * product_k binom(n,k)^(m_k(lambda)),
lambda=mu^*.
```

Every non-Ferrers target has fibre zero.  Since `D` is injective and `P_n`
has `binom(2n,n)` elements, `|im F^2|=binom(2n,n)`.

Therefore all parts of the claim follow. ∎

## Corrections or Missing Assumptions

None.  The attack did reject two tempting stronger statements:
`F^3=F` and `F^2=F` are both false already for `n=2`.  They are not claimed.

## Open Risks

- Ferrers diagrams, partition conjugation, and binary line-sum theory are
  classical and receive zero contribution credit.
- The owner search is bounded.  No external novelty, priority, or circulation
  claim is supported; status remains `OWNER_AMBER / HOLD_EXTERNAL`.
- Rectangular carriers, asynchronous row updates, relabelling quotients, and
  random schedulers are outside the theorem.
