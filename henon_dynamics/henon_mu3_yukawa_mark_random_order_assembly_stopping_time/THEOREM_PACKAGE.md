# C83 theorem package

For a permutation of `L`, the first full prefix has a set `S` of size `k` and
one last label `ell` such that `Phi(S)=Q` but `Phi(S\\{ell}) != Q`.  Conversely,
every such pair `(S,ell)` gives `(k-1)!(16-k)!` permutations with stopping time
`k`.  Hence

```text
N_k = sum_{|S|=k} p(S) (k-1)! (16-k)!.
```

The finite closure enumeration supplies the exact `p(S)` totals.  The formula
partitions all `16!` permutations, yielding the receipt's probabilities and
mean `36499/3960`.  The statement is about a uniform ordering of a finite
named set, not a dynamical or arithmetic random process.
