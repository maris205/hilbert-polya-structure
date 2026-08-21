# Theorem package

Let `T_H` be a C88 first-passage time and let
`N_H(k)=#{pi:T_H=k}` and `S_H(k)=#{pi:T_H>k}` on the uniform space of all
`16!` label permutations.

For `k=0,...,16`, C94 certifies

`A_H(k)=#{pi:T_H>=k}` with `A_H(0)=16!` and `A_H(k)=S_H(k-1)` for `k>=1`,

`h_H(k)=P(T_H=k | T_H>=k)=N_H(k)/A_H(k)` whenever `A_H(k)>0`, and
`1-h_H(k)=S_H(k)/A_H(k)`.

For every nonempty survival event `S_H(k)={T_H>k}`, define
`R_{H,k}=T_H-k | S_H(k)`.  For `0<=r<=16-k`,

`P(R_{H,k}>r)=S_H(k+r)/S_H(k)`,

`P(R_{H,k}=r)=N_H(k+r)/S_H(k)` for `r>=1`,

`E[R_{H,k}]=sum_r P(R_{H,k}>r)`, and
`E[R_{H,k}^2]=sum_r (2r+1)P(R_{H,k}>r)`.

The variance is the second moment minus the square of the mean.  If the
conditioning event is empty, the corresponding conditional grid and moments
are undefined and are emitted as `null`; no probability is assigned.

The producer evaluates these identities from C88 counts.  The independent
checker reconstructs the same counts from C88 hit bitsets, and SymPy checks all
defined rational cells and moments.
