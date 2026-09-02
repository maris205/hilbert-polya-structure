# Theorem package

## Definitions

Fix `n >= 1`.  Let `P_n` be the labelled set partitions of `[n]`, and write
`pi <= sigma` when `sigma` refines `pi`.  In one update, every label receives
an independent fair bit; each block is replaced by its nonempty bit fibres.
Fresh bits are used at every update.  For `pi <= sigma`, let `r_B` count the
number of `sigma`-blocks inside `B in pi`, and write `(q)_r` for the falling
factorial with `(q)_0=1`.

## Global theorem

For `q=2^t`, every `pi,sigma in P_n` satisfy

`K_n^t(pi,sigma) = 1_{pi<=sigma} product_{B in pi} (q)_{r_B}/q^{|B|}`.

At one step this is `2^{|pi|-n}` exactly when every source block produces at
most two target blocks, and is zero otherwise.  From the one-block start,

`P(Pi_t=sigma)=(2^t)_{|sigma|}/2^{tn}`,

`P(|Pi_t|=k)=S(n,k)(2^t)_k/2^{tn}`,

`E|Pi_t|=2^t[1-(1-2^{-t})^n]`.

For `T_n=min{t: Pi_t is discrete}`,

`P(T_n<=t)=(2^t)_n/2^{tn}`,

`P(T_n=t)=P(T_n<=t)-1_{t>=1}P(T_n<=t-1)`,

`E T_n=sum_{t>=0}[1-(2^t)_n/2^{tn}]`.

The transition matrix has

`chi_n(x)=product_{k=1}^n (x-2^{k-n})^{S(n,k)}`,

`det(I-zK_n)=product_{k=1}^n (1-z2^{k-n})^{S(n,k)}`,

`tr(K_n^t)=sum_{k=1}^n S(n,k)2^{t(k-n)}`,

and the squarefree annihilator

`product_{k=1}^n (K_n-2^{k-n}I)=0`.

Thus `K_n` is diagonalizable over `Q`.  If `n_j -> infinity` and integer
`t_j` obey `n_j^2/2^{t_j} -> lambda in (0,infinity)`, then

`P(T_{n_j}<=t_j) -> exp(-lambda/2)`.

## Proof

After `t` rounds each label carries an independent uniform word in a set of
size `q`.  Within a starting block, a requested collection of `r_B` terminal
fibres is realized by an injection of those fibres into the word set, giving
`(q)_{r_B}` assignments.  Independence across starting blocks proves the
kernel.  With one starting block, summing the fixed-partition law over the
`S(n,k)` labelled partitions gives the block law; occupancy indicators give
the mean.  Absorption is precisely the no-collision event, proving its law and
tail-sum mean.  The union bound `P(T_n>t) <= binom(n,2)2^{-t}` proves finiteness.

Order partitions by rank.  Refinement makes the matrix triangular, and a
rank-`k` state stays unchanged under exactly `2^k` of the `2^n` bit vectors.
Hence its diagonal scalar is `lambda_k=2^{k-n}` and occurs `S(n,k)` times.
For the conventional column action, let `V_k` span ranks at most `k`.  Then
`(K-lambda_k I)V_k` lies in `V_{k-1}`.  The commuting factors applied from
rank `n` down to rank 1 kill the flag, proving the annihilator.  Its roots are
distinct, which proves diagonalizability; this is the step that diagonal
entries alone would not prove.

Finally,

`log((q)_n/q^n)=-n(n-1)/(2q)+O(n^3/q^2)`

when `n^2/q` is bounded.  The error vanishes and the leading term tends to
`-lambda/2`, proving the limit.

## Boundary conditions

- `n=1` gives the unique singleton partition and `T_1=0`.
- The package contract excludes `n=0`; no `0^0` convention is silently used.
- A shared bit per block, biased bits, persistent rather than fresh bits, or an
  unlabelled block-size quotient defines a different model.
- A phase-free law for `T_n-2 log_2 n` is not asserted: the dyadic lattice can
  retain a subsequence phase.
- Finite evidence is regression support, not the proof of the global theorem.
