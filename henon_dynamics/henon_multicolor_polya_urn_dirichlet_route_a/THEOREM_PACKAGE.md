# Theorem package

Let `K>=1`, `a_i>=0`, `a_+=sum_i a_i>0`, and `c>=0`.  At each integer time a
color is drawn proportionally to its current mass, replaced, and receives
additional mass `c`.

**Theorem (multicolor Pólya--Dirichlet closure).** Suppose `c>0`, delete the
zero-mass colors, and set `alpha_i=a_i/c`, `A=sum_i alpha_i`.  If an ordered
word of length `n` has counts `n_i`, then

`Pr(word)=prod_i (alpha_i)^(rising n_i)/(A)^(rising n)`.

Consequently the count vector is Dirichlet--multinomial and each marginal is
beta--binomial.  With falling factorials and `R=sum_i r_i`,

`E prod_i (N_i)_[r_i]=(n)_[R] prod_i(alpha_i)^(rising r_i)/(A)^(rising R)`.

In particular,

- `E N_i=n alpha_i/A`;
- `Var N_i=n alpha_i(A-alpha_i)(A+n)/(A^2(A+1))`;
- `Cov(N_i,N_j)=-n alpha_i alpha_j(A+n)/(A^2(A+1))` for `i!=j`.

The normalized masses `P_i(n)=(alpha_i+N_i(n))/(A+n)` form a bounded vector
martingale.  They converge almost surely and in every finite `Lp` to a
Dirichlet vector on the active face.  Equivalently, the entire draw sequence
is conditionally iid categorical given that vector.  Dirichlet mixing yields
the displayed word law, and its posterior predictive probability yields the
urn update, so the equivalence is bidirectional.

For `c=0`, draws are iid with probabilities `a_i/a_+` and the counts are
multinomial; `alpha` is undefined and unused.  A zero initial mass stays zero,
and `K=1` is deterministic.

The increasing total mass prevents nontrivial recurrence.  The strict tuple
is `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, the verdict is
`ROUTE_A_REJECTED`, and Route B is false.
