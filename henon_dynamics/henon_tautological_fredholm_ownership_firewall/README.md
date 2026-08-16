# HCS-P77: Tautological Fredholm ownership firewall

P77 separates two operator constructions that answer different questions.
For each fixed `q>0`, on
`Omega_q={|z|<min(1,q^(-1))} minus Sigma_q`, set

    h_m(z,q)=c_m 2(qz)^m/[1-(1+q^(2m))z^(2m)],
    A(z,q)=diag(h_1,h_2,...).

The P75--P76 channel bounds imply that `A` is locally trace class.  Hence
`K=exp(A)-I` is trace class and

    det_F(I+K)=exp(Tr A)=Z_channel(z,q).

This statement is exact but tautological: for every nonvanishing holomorphic
scalar `F`, the rank-one family `K_F=(F-1)P` already satisfies
`det_F(I+K_F)=F`.

The source-native construction goes the other way.  Each primitive word
`omega` owns a finite weighted cyclic block

    B_omega e_j=q^(chi_j)e_(j+1),
    det(I-zB_omega)=1-z^n q^(S_n chi(omega)).

This determinant is the P70 Euler denominator polynomial; the corresponding
Euler factor is its reciprocal.

Its singular values are the edge weights in `{1,q}`.  Primitive singleton
reflection words exist at every odd `n>=3`, so the full orbit-block direct
sum has infinitely many singular values bounded below by `min(1,q)`.  It is
bounded but noncompact and belongs to no Schatten class.

**Status:** punctured analytic determinant PROVED_TAUTOLOGICAL; finite
source blocks PROVED; source-native direct-sum trace class REFUTED; genuine
transfer ownership OPEN; arithmetic advance NO; Route B not authorized.
Reproduce with `bash code/run_c77.sh` and see `paper/paper.pdf`.
