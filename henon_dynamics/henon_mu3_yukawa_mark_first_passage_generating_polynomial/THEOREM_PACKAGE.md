# Theorem package

For target `i`, let `N_i(t)` be the number of permutations whose first hit occurs at time `t`.  Then

`G_i(z)=sum_t N_i(t)z^t` and `P_i(z)=G_i(z)/16!` satisfy

`P_i^(m)(1)=E[(T_i)_m]`.

Using Stirling numbers of the second kind,

`E[T_i^r]=sum_{m=0}^r {r\brace m} P_i^(m)(1)`.

The C99 receipt records every term of this conversion for `r=0,...,6` and checks equality with C89 raw moments.  The support gcd is the gcd of nonzero time indices, with the deterministic `{0}` convention equal to zero.
