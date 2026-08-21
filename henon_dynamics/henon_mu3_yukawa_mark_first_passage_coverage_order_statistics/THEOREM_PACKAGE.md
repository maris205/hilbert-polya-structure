# Theorem package

For a support `A`, let `C(A)` count all twenty C88 targets whose hit indicator is true.  For a random label permutation with prefix support `A_k`, define `K_r=min{k:C(A_k)>=r}`.  If `G_r(k)=#{A:|A|=k,C(A)>=r}`, then

`P(K_r<=k)=G_r(k)/binom(16,k)`

and the exact permutation mass at time `k` is `16!` times the difference between consecutive reduced CDF values.  Equivalently, for `k>=1`, every oriented Boolean-lattice boundary edge that first crosses coverage rank `r` has completion weight `(k-1)!(16-k)!`; time zero uses the empty support with `16!` completions.  The mean is both the first raw moment of this PMF and `sum_{k=0}^{15} P(K_r>k)`.  Since the event `C(A)>=r+1` is contained in `C(A)>=r`, `K_r<=K_{r+1}` pointwise and the rank CDFs decrease with `r`.

The trivial target is included: `C(empty)=1`, hence `K_1=0` for all permutations.
