# Theorem package

For C88 variables `T_i,T_j`, let
`J_ij(k,l)=#{pi:T_i(pi)>k and T_j(pi)>l}`.  C90 certifies all 17 by 17 cells
for all 400 ordered pairs.  If `k<=l`, a nested support pair contributes
`k!(l-k)!(16-l)!` permutations; the reverse case is transposed.

For `a,b <= 6`, with `Delta_a(k)=(k+1)^a-k^a`, the exact mixed moment is

`E[T_i^a T_j^b] = sum_{k,l=0}^{15} Delta_a(k) Delta_b(l) J_ij(k,l) / 16!`.

Orders `(a,0)` and `(0,b)` recover the C89 marginal raw moments, and
`Cov(T_i,T_j)=E[T_i T_j]-E[T_i]E[T_j]`.
