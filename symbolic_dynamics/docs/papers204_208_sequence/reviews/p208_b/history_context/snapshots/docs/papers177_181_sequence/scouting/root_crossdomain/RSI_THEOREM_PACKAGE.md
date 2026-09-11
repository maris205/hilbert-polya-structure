# RSI theorem package — random singleton isolation on set partitions

**Status:** `THEOREM SPIKE / OWNER AMBER / HOLD_EXTERNAL`.

On a partition `pi` of `[n]`, choose `i` uniformly and make `{i}` a singleton,
leaving the other elements of its old block together.  The discrete partition
is the unique recurrent state.

Let `s(pi)` be the number of singleton blocks and let `B_m^*` count partitions
of `m` with no singleton blocks.

1. In any refinement-compatible ordering the transition matrix is triangular
   with diagonal `s(pi)/n`.  It is diagonalizable, with eigenvalue `s/n` of
   multiplicity `binom(n,s) B_{n-s}^*` for `s=0,...,n-2`, and eigenvalue one
   once.  No `s=n-1` layer exists.
2. If the initial block sizes are `b_1,...,b_k`, absorption by epoch `t`
   occurs exactly when at most one label in each old block has not appeared
   among the sampled labels.  Therefore

   ```text
   P(T<=t)=n^(-t) sum_{m=0}^k e_m(b_1,...,b_k)
                         (n-m)! S(t,n-m).
   ```

3. More generally, every target probability is a finite sum of the same
   exact-support term `(n-|M|)! S(t,n-|M|)/n^t`: in an old block supporting a
   nonsingleton target block `C`, the missing set must equal `C`; in a fully
   dissolved old block it may have size zero or one.
4. If a target `sigma` has `s` singleton blocks and `b` total blocks, it has
   no predecessor when `s=0`; otherwise its number of distinct one-step
   predecessors is

   ```text
   1 + s(b-s) + binom(s,2),
   ```

   while the number of labelled action pairs `(pi,i)` leading to it is `sb`.

Partition lattices, associated Bell numbers, generic fragmentation processes,
and coupon-collector occupancy are zero credit.  The literal isolation chain
plus the spectral, all-time, and target-local conjunction is the retained
object; direct ownership kills it.
