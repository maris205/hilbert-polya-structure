# Derivation package: nullity-feedback Jordan powers

Status: `KILL_INTERNAL_P137_PLUS_ROOT_OWNER`  
External lifecycle: `HOLD_EXTERNAL`  
Date of bounded scout: 2026-09-03

This document records the mathematical ceiling reached before the ownership and
portfolio gates were applied.  A correct formula here is not a novelty claim.

## 1. Literal system and assumptions

Fix `n >= 1` and a field `K`.  The carrier is the set of similarity classes of
nilpotent `n x n` matrices over `K`.  Such classes are indexed by partitions

`lambda=(lambda_1 >= ... >= lambda_l > 0) |- n`.

The literal update is

`F([A]) = [A^(1+dim ker A)]`.

The map is well defined on similarity classes.  The use of a field is enough:
a nilpotent matrix has its usual rational/Jordan block decomposition with
polynomial `x^m`, so no algebraic-closure assumption is needed.

For `n=0`, if the empty matrix is admitted, the empty partition is a fixed
one-point system.  The remainder takes `n>=1`.

## 2. Fixed-power block calculation

Let `J_m` be one nilpotent block and fix `r>=1`.  Write

`m=q r+s`, with `0<=s<r`.

The chains of `J_m^r` are the residue classes of basis positions modulo `r`.
Consequently the powered type consists of

- `s` blocks of size `q+1`, and
- `r-s` blocks of size `q`,

with zero blocks omitted.  In particular, if `m<r`, the output is `m` blocks
of size one.  For a partition `lambda`, the type of `A^r` is the multiset union
of these contributions over all parts of `lambda`.

Also

`dim ker A^r = sum_i min(r,lambda_i)`.

These are classical Jordan-power facts and receive zero contribution credit.

## 3. Iterate exponents and point clocks

Define

`K_0=1`,

`K_(t+1)=K_t (1+sum_i min(K_t,lambda_i))`.                 (3.1)

Inductively,

`F^t([A])=[A^K_t]`.                                       (3.2)

Indeed, if the current representative is `A^K_t`, its nullity is the sum in
(3.1), and raising it to the new feedback exponent multiplies the accumulated
exponent.

The zero type `(1^n)` is the only recurrent type.  If `A` is nonzero and
nilpotent, `rank A^r < rank A` for every `r>=2`; every nonzero step therefore
strictly decreases rank.  The exact point absorption time is

`tau(lambda)=min{t>=0: K_t>=lambda_1}`.                    (3.3)

This includes `(1^n)`, for which `tau=0`.

## 4. Sharp global clock and the nonunique deepest boundary

Put `s_0=1` and

`s_(t+1)=s_t(s_t+1)`.

Thus

`s_0,...,s_6 = 1,2,6,42,1806,3263442,10650056950806`.

If `K_t<lambda_1`, then at least one Jordan block has size greater than `K_t`,
so `dim ker A^K_t >= K_t`; hence `K_(t+1)>=K_t(K_t+1)`.
The cyclic type `(n)` attains equality until it vanishes.  Therefore

`D(n)=max_(lambda|-n) tau(lambda)=min{t:s_t>=n}`.           (4.1)

The cyclic type is always deepest, but it is not always the unique deepest
type.  For an exact classification write `lambda=(L,mu)`, where `L` is a
largest part, and define

`q_0(mu)=1`,

`q_(j+1)(mu)=q_j(mu)(1+q_j(mu)+sum_(u in mu) min(q_j(mu),u))`.

Then, for every `t>=0`,

`tau(lambda)>t  iff  L>q_t(mu)`.                           (4.2)

In particular the deepest partitions of `n` are exactly those satisfying

`L=n-|mu| >= mu_1` and `L>q_(D(n)-1)(mu)`.                 (4.3)

For `D=D(n)>=1`, the cyclic type is the unique deepest type exactly when

`n <= 2^(2^(D-1))`.                                       (4.4)

The least nonempty tail is `mu=(1)`, for which
`q_t(mu)=2^(2^t)-1`; every other nonempty tail has no smaller
`|mu|+q_t(mu)`.  Thus `(n-1,1)` first ties the cyclic type at
`n=2^(2^(D-1))+1`.  Concrete boundary checks include the first ties `n=5`,
`17`, and `257` in depths `2`, `3`, and `4`.

## 5. One-step every-target inverse flow

Fix the feedback exponent `r`.  A source contributing to this slice must have
length `r-1`.  Let the target have multiplicities `c_j`.

For source parts `m>=r`, write `m=jr+s`, `0<=s<r`.  Let

- `A_j` be the number of source parts with quotient `j`;
- `B_j` be the sum of their residues `s`;
- `C` be the number of source parts below `r`;
- `W` be the sum of those `C` small parts.

Then a target belongs to the fixed-`r` image if and only if there are
nonnegative integers satisfying

`c_j = B_(j-1)+r A_j-B_j` for `j>=2`,                     (5.1)

`c_1 = W+r A_1-B_1`,                                      (5.2)

`C+sum_(j>=1) A_j=r-1`,                                   (5.3)

`0<=B_j<=(r-1)A_j`, and `C<=W<=(r-1)C`.                   (5.4)

Only finitely many `A_j,B_j` can be nonzero.  These equations are both
necessary and sufficient: choose residue multisets realizing each `(A_j,B_j)`
and a multiset of `C` small parts realizing `(C,W)`, then rebuild the source
parts `jr+s`.

Let

`R_r(A,B)=[u^A v^B] product_(s=0)^(r-1) (1-u v^s)^(-1)`

and

`S_r(C,W)=[u^C v^W] product_(s=1)^(r-1) (1-u v^s)^(-1)`.

The exact fixed-`r` fibre is

`sum_(feasible (A,B,C,W)) S_r(C,W) product_(j>=1) R_r(A_j,B_j)`.  (5.5)

Summing (5.5) over `r=2,...,n+1` gives the one-step fibre over every target,
including zero.  This is a cleaner integer-flow orientation of the standard
fixed-power nilpotent-root equations, but it does not escape that ownership.

## 6. Zero target and an extremal fibre

The target `(1^n)` is the zero matrix.  A source of length `ell` maps to it
exactly when `lambda_1<=ell+1`.  Subtracting one from each part leaves a Ferrers
diagram in an `ell x ell` rectangle, so its fibre size is

`Z_n=[q^n] sum_(ell>=1) q^ell [2ell choose ell]_q`.         (6.1)

This is also a largest one-step fibre.  If a source is nonterminal, then
`lambda_1>ell+1`; its conjugate partition has length `lambda_1` and largest
part `ell`, and is therefore terminal.  Conjugation injects all nonterminal
sources into the terminal sources.  Every nonzero target fibre is contained
in the nonterminal set, hence has size at most `Z_n`.

This extremal statement is mathematically valid, but its proof is a one-line
Ferrers/conjugation addition to a package already strongly occupied by P137.

## 7. All-time inverse attempt and threshold failure

For a prescribed time `t`, a source can be grouped by its exponent chain
`K_0,...,K_t`.  Conditional on that chain, the endpoint type is again obtained
by fixed-power block splitting with power `K_t`, while marker variables enforce

`K_(j+1)/K_j-1=sum_i min(K_j,lambda_i)`.

This gives a finite multivariate coefficient extraction for every endpoint.
It is exact and computationally useful, but no closed positivity criterion,
uniformity law, or target statistic independent of fixed-power root
classification emerged.  The requested second axis therefore stops at
coefficient computation and does not meet the P166 intake threshold.

## 8. Falsification controls

`verify_scout.py` uses two independent representations:

1. partitions and the residue-chain block formula;
2. literal matrices over `F_2` and `F_3`, matrix powering, row-reduced ranks,
   and Jordan types reconstructed solely from the nullities of all powers.

It additionally enumerates all partitions through `n=43` for temporal claims
and all targets through `n=24` for the inverse flow and extremal fibre.  The
frozen run has `7,124,325` assertions.

