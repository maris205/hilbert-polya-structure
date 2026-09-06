# Regular-variation universality for divisibility Gram matrices

Status: complete proposed proof, awaiting independent internal review and
paper-level admission. Unnumbered continuation research, 2026-09-05.

## 1. Contract and ownership boundary

Fix a real number sigma < 1/2 and write rho = 1 - 2 sigma > 0.
Let L: [1,infinity) -> (0,infinity) be measurable, slowly varying at
infinity, and bounded above and away from zero on every compact interval.
Set a(k) = k^(-sigma) L(k). No multiplicativity of a or L is assumed.
On ell^2(N) let T_N be the N by N matrix, extended by zero, with

    T_N(r,m) = a(r/m) if m divides r and 1 <= m <= r <= N;
               0 otherwise.

Define

    A_N = rho / (N^rho L(N)^2) T_N^* T_N,
    E_sigma(m,n) = (mn)^sigma / lcm(m,n).

THEOREM. For every real q > 0,

    ||A_N - E_sigma||_{S_q} -> 0  if q rho > 1.

Here S_q is a quasi-normed ideal when q < 1. If q rho <= 1,
A_N-E_sigma does not even belong to S_q for any N. Thus the range
is exact. Moreover, for every eta in (0,rho), there is a constant
C(sigma,L,eta), independent of N and j, such that

    lambda_j(A_N) <= C j^(-eta),
    lambda_j(E_sigma) <= C j^(-eta).

All eigenvalues are in decreasing order with multiplicity; A_N is
positive and finite rank, so its sequence is continued by zeros.

This is one universality question, not separate papers for each q or L.
The proposed increment is the nonmultiplicative, arbitrary slowly-varying
coefficient family together with convergence in the full sharp ideal range.
For L=1 the latter removes the even-integer restriction in the precise
2021 statement of Hilberdink--Pushnitski, Theorem 2.1. No claim is made
that that restriction remained an open problem after the accessed version.

CLASSICAL INPUTS, NOT OUR CONTRIBUTIONS:

- Hilberdink--Pushnitski, arXiv:2110.14323v1, Theorem 1.1, proves that
  E_s is compact, positive, injective for every s<1/2 and that
  lambda_j(E_s) ~ kappa(s,1) j^{-(1-2s)} with kappa(s,1)>0.
  In particular E_sigma lies in S_q iff q rho>1.
- Potter's bound and the uniform convergence theorem for measurable
  slowly-varying functions are classical regular-variation results.
- The min--max principle and the singular-value sum inequality are
  standard compact-operator facts.

Source-system arithmetic is the divisibility relation and the classical
LCM kernel. It is not target Euler factors, target zero ordinates, an
automorphic identification, or a Hilbert--Polya realization. No formal
Route A evaluation has run for this candidate.

Decisive failure conditions: a gap in the uniform Potter majorization,
the positive congruence estimate, or full-range singular-value summability;
or a primary source already proving this same nonmultiplicative theorem.
Finite matrix checks cannot close any of these quantified claims.

## 2. Two classical regular-variation facts used

For every epsilon>0 there is C_epsilon such that, for all x,y>=1,

    L(x)/L(y) <= C_epsilon max((x/y)^epsilon,(x/y)^(-epsilon)).    (RV1)

The compact-interval hypotheses extend the usual eventual Potter estimate
to the displayed global range. Also, for each fixed 0<c<C<infinity,

    sup_{t in [c,C]} |L(tN)/L(N)-1| -> 0.                         (RV2)

Only arguments tN>=1 are used. The measurable slow-variation and
positivity hypotheses are essential to these standard formulations.
The discrete averaging step needed below is proved explicitly rather
than hidden inside a statement of Karamata's theorem.

## 3. Exact Gram identity and uniform positive-entry bound

Put ell=lcm(m,n). Direct multiplication gives, if ell<=N,

    A_N(m,n) = rho (mn)^sigma / (N^rho L(N)^2)
               * sum_{k<=N/ell} (k ell)^(-2sigma)
                   L(k ell/m) L(k ell/n).                       (1)

If ell>N the entry is zero. The same convention treats m>N or n>N.
All entries are nonnegative and A_N is positive semidefinite.

Choose epsilon>0 with 2epsilon<rho. For a summation index r=k ell,
1<=r/m<=N and 1<=r/n<=N. Applying (RV1) with y=N gives

    L(r/m)/L(N) <= C_epsilon (mN/r)^epsilon,
    L(r/n)/L(N) <= C_epsilon (nN/r)^epsilon.

Consequently, with alpha=2sigma+2epsilon<1,

    A_N(m,n) <= C (mn)^(sigma+epsilon) N^(-rho+2epsilon)
                    ell^(-alpha) sum_{k<=N/ell} k^(-alpha).

For any real alpha<1 and X>=1,
sum_{k<=X} k^(-alpha) <= C_alpha X^(1-alpha); this follows by
comparison with the integral, treating alpha<0 and alpha>=0 separately.
Since 1-alpha=rho-2epsilon, all powers of N cancel and

    0 <= A_N(m,n) <= C E_{sigma+epsilon}(m,n)                     (2)

for all N,m,n. This is entrywise domination, NOT a claim that entrywise
domination implies an inequality in arbitrary Schatten ideals or in
positive-operator order.

## 4. Entrywise limit, including the small-index tail

Fix m,n and ell. Write t_k=k ell/N. Formula (1) becomes

    A_N(m,n) = rho (mn)^sigma/ell * (ell/N)
          * sum_{k<=N/ell} t_k^(-2sigma)
                   [L(N t_k/m)/L(N)] [L(N t_k/n)/L(N)].          (3)

For delta in (0,1), (RV2) implies uniform convergence of both ratios
to 1 for delta<=t_k<=1. The Riemann sum on this part therefore tends to
the integral from delta to 1 of t^(-2sigma) dt.

For t_k<delta, (RV1) bounds the product of ratios by
C(mn)^epsilon t_k^(-2epsilon). If delta N/ell<1, that part is empty.
Otherwise the power-sum estimate from section 3 bounds its absolute
contribution, before the fixed prefactor in (3), by

    C (ell/N) sum_{k<delta N/ell} t_k^(-alpha)
        <= C' delta^(1-alpha).

This bound is uniform in N and tends to zero with delta, since alpha<1.
The omitted integral from 0 to delta also tends to zero because 2sigma<1.
Let N tend to infinity and then delta tend to zero. Since
rho times the integral from 0 to 1 of t^(-2sigma) dt equals 1,

    A_N(m,n) -> E_sigma(m,n).                                   (4)

In particular, the case m=n=1 gives

    F(N):=sum_{k<=N}|a(k)|^2 ~ N^rho L(N)^2 / rho.                (5)

## 5. Positive congruence and period-independent spectral tails

Fix eta in (0,rho); choose epsilon>0 so eta+2epsilon<rho.
Let D_eta be the positive diagonal compact operator with entries
m^(-eta/2). Define the finite-rank positive matrix

    B_N(m,n) = (mn)^(eta/2) A_N(m,n),

again extended by zero. This is a finite-dimensional positive
congruence, so positivity requires no unbounded-domain argument.
By (2), its entries are bounded by C E_s(m,n), where

    s = sigma + epsilon + eta/2 < 1/2.

For finitely supported u,v, entrywise nonnegativity gives

    |<u,B_N v>| <= C <|u|,E_s |v|>
                 <= C ||E_s|| ||u|| ||v||.

The classical boundedness of E_s implies sup_N ||B_N|| <= M<infinity.
Therefore

    A_N = D_eta B_N D_eta,
    0 <= A_N <= M D_eta^2                                      (6)

in positive-operator order. By min--max,

    lambda_j(A_N) <= M j^(-eta).                                (7)

Passing to the limit in (6) on finitely supported quadratic forms,
using (4), yields 0<=E_sigma<=M D_eta^2 on a dense subspace and hence
on ell^2, since both sides are bounded. This proves the analogous
eigenvalue bound for E_sigma. There is no assertion of uniform
j^(-rho) decay for arbitrary L at the endpoint.

## 6. Operator-norm convergence

Let P_K project onto the first K coordinates and Q_K=I-P_K.
From the factorization in (6),

    ||Q_K A_N|| <= ||Q_K D_eta|| ||B_N|| ||D_eta||
                  <= M (K+1)^(-eta/2).

By self-adjointness the same holds for ||A_N Q_K||. Hence

    ||A_N-P_K A_N P_K|| <= 2M (K+1)^(-eta/2),                    (8)

uniformly in N. The classical compactness of E_sigma implies
||E_sigma-P_K E_sigma P_K||->0. For fixed K, (4) gives convergence
of the finite head in operator norm. The triangle inequality, first
N->infinity then K->infinity, proves

    ||A_N-E_sigma|| -> 0.                                      (9)

This proof does not infer operator-norm convergence from entrywise
convergence alone.

## 7. Full Schatten range and sharpness

Fix q>0 with q rho>1. Choose eta in (1/q,rho), and use the preceding
bounds with that eta. Put R_N=A_N-E_sigma. The standard singular-value
sum inequality yields, for every j>=1,

    s_{2j-1}(R_N) <= s_j(A_N)+s_j(E_sigma) <= 2M j^(-eta).

The even-indexed singular value is no larger than its preceding odd
one. For every fixed index k, s_k(R_N)<=||R_N||->0 by (9). Dominated
convergence for the counting measure on N, dominated by the summable
sequence C k^(-eta q), proves

    sum_k s_k(R_N)^q -> 0.

This argument applies without change to q<1 and makes no invalid
Banach-norm interpolation assumption in that range.

For q rho<=1, classical Theorem 1.1 gives E_sigma not in S_q. Since
A_N is finite rank, A_N-E_sigma in S_q would imply E_sigma in S_q
by the linearity of the ideal S_q, a contradiction. This proves the
exact negative statement, not merely failure of a particular bound.

## 8. Consequences and limits

Replacing the normalization by F(N)^(-1) leaves the same S_q limit:
by (5), the ratio of normalizing constants tends to 1, while section 7
gives uniform boundedness of ||A_N||_{S_q} (using singular-value tails
also when q<1). Thus

    F(N)^(-1) T_N^* T_N -> E_sigma in S_q,  q rho>1.

For each fixed j, positivity/injectivity of the classical E_sigma gives

    s_j(T_N)^2 / F(N) -> lambda_j(E_sigma)>0.

The convergence of eigenvalue errors is uniform over j after zero
extension by (9); it is an absolute-error statement, not a uniform
relative asymptotic when j grows with N. Also,

    sum_j [s_j(T_N)^2/F(N)]^q -> sum_j lambda_j(E_sigma)^q

for q rho>1, by the same dominated-convergence argument on ordered
eigenvalues. No new proof of the known asymptotic constant kappa is claimed.

Examples include L(x)=(1+log x)^beta for every real beta, and
L(x)=2+sin(log(log(e+x))). The latter is positive, slowly varying,
and has no limit at infinity. Both meet the local bounds. For generic
beta!=0 the former is not multiplicative as an arithmetic function;
already beta=1 gives L(6)!=L(2)L(3). Oscillation in a slowly varying
factor is therefore allowed, not replaced by an eventual constant.

No convergence rate uniform over all such L is asserted. The theorem
does not treat arbitrary arithmetic f solely from regular variation
of sum |f(n)|^2; its pointwise coefficient assumption is different
from, and complementary to, Hilberdink's multiplicative hypotheses.

No computation is being substituted for proof. No manuscript, C number,
formal evaluation, or completed five-paper batch is asserted here.
