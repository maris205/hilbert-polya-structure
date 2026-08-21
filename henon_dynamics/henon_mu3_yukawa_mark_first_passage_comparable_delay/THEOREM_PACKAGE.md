# Theorem package

Let `S_ij(k,l)=# {T_i>k and T_j>l}`.  Define `S_ij(-1,l)` and `S_ij(k,-1)` by the corresponding C88 marginal survival counts, and `S_ij(-1,-1)=16!`.  Then

`N_ij(a,b)=S_ij(a-1,b-1)-S_ij(a,b-1)-S_ij(a-1,b)+S_ij(a,b)`

is the exact permutation count for `(T_i,T_j)=(a,b)`.  If `H_i <= H_j`, monotonicity of generated subgroup containment gives `N_ij(a,b)=0` for `a>b`.  The delay `D_ij=T_j-T_i` has counts `sum_a N_ij(a,a+d)`.  Given `T_i=t`, its conditional probabilities divide the row `N_ij(t,t+d)` by `sum_d N_ij(t,t+d)`; all conditional means and variances are reduced rational numbers.  Summing rows or survival tails recovers each C88 marginal law.

These are exact finite identities over the frozen named-label model, not claims about arithmetic or spectral objects.
