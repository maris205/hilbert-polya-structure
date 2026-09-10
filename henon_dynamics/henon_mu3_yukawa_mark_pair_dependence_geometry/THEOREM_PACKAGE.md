# Theorem package

For each ordered pair define `S_ij(k,l)=#{T_i>k,T_j>l}` and complete the negative-threshold boundaries from C88.  The finite difference

`N_ij(a,b)=S(a-1,b-1)-S(a,b-1)-S(a-1,b)+S(a,b)`

is the exact joint PMF count.  All dependence metrics are finite sums of rational numbers.  Pearson `rho` is stored without floating approximation: `rho^2` is rational and an exact signed radical is retained when the square root is irrational.  The additional rational normalized-covariance proxy is `Cov/(Var_i+Var_j)`.  Frechet geometry records the sum of cellwise lower-upper widths and the exact violation slack (zero for every valid joint cell).
