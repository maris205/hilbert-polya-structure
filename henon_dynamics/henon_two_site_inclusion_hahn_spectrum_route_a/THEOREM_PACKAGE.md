# Complete theorem package

## Frozen generator

Fix an integer N>=0 and alpha>0. On S_N={0,...,N} set

'(L f)(x)=(N-x)(alpha+x)[f(x+1)-f(x)] + x(alpha+N-x)[f(x-1)-f(x)]',

where the unavailable endpoint term is zero. This is the displayed, unscaled continuous-time clock. State x is the occupancy of site one and N-x that of site two.

## Theorem

For N>=1, the chain is irreducible and its unique reversible probability is

'pi_alpha,N(x) = [(alpha)_x (alpha)_{N-x}/(x!(N-x)!)] / [(2alpha)_N/N!]'.

For j=0,...,N, define

'H_j(x) = _3F_2(-j,j+2alpha-1,-x; alpha,-N; 1)'

and the positive finite-sum norm

'h_j = sum_{x=0}^N pi_alpha,N(x) H_j(x)^2'.

Then 'L H_j=-lambda_j H_j', where 'lambda_j=j(j-1+2alpha)'. These eigenvalues are strictly increasing, the H_j are mutually orthogonal in L2(pi), and form a basis. Consequently

'p_t(x,y)=pi(y) sum_{j=0}^N exp(-lambda_j t) H_j(x)H_j(y)/h_j'.

The gap is 2alpha and every centered f obeys

'||exp(tL)f||_2 <= exp(-2alpha t)||f||_2'.

The constant is sharp, with equality on 'H_1=1-2x/N'.

For N=0 the chain is the singleton, the formula consists only of H_0=1, and a nonconstant spectral gap is inapplicable. For N=1, the spectrum is exactly {0,2alpha} and the stationary law is (1/2,1/2).

At alpha=0 and N>=1, 0 and N are absorbing. Starting from x, absorption occurs almost surely, X_t is a bounded martingale, and

'P_x(hit N)=x/N', 'P_x(hit 0)=1-x/N'.

All stationary probabilities at alpha=0 are exactly

'c delta_0+(1-c) delta_N', '0<=c<=1'.

As alpha decreases to zero, pi_alpha,N converges weakly to '(delta_0+delta_N)/2'. For N=0 the only boundary law is delta_0.

## Proof

Write 'b_x=(N-x)(alpha+x)' and 'd_x=x(alpha+N-x)'. Adjacent unnormalized masses satisfy 'w_x b_x=w_{x+1}d_{x+1}'. The Chu--Vandermonde coefficient identity gives the normalizer '(2alpha)_N/N!'. Thus detailed balance holds. Positivity of every interior adjacent rate gives irreducibility when N>=1, hence uniqueness and self-adjointness.

The generator preserves polynomials of degree at most j. For 'f(x)=x^j', the possible x^(j+1) terms cancel. The x^j coefficient is

'j[(N-alpha)-(N+alpha)] - 2 binom(j,2) = -j(j-1+2alpha)'.

Therefore the degree filtration makes L triangular with diagonal -lambda_j, whose increments are 'lambda_(j+1)-lambda_j=2(j+alpha)>0'.

Expand the terminating series

'H_j(x)=sum_{k=0}^j [(-j)_k(j+2alpha-1)_k(-x)_k]/[(alpha)_k(-N)_k k!]'.

Put 'phi_k(x)=(-x)_k'. Direct forward/backward differencing gives the explicit triangular identity

'L phi_k=-k(k-1+2alpha)phi_k-k(N-k+1)(alpha+k-1)phi_(k-1)'.

If 'H_j=sum_k c_k phi_k', the coefficient equation for an eigenvalue '-lambda_j' is

'c_(k+1)/c_k=[lambda_j-lambda_k]/[(k+1)(N-k)(alpha+k)]'.

The displayed hypergeometric coefficients have precisely this ratio, because both sides equal

'(j-k)(j+k+2alpha-1)/[(k+1)(N-k)(alpha+k)]'.

Thus, coefficient by coefficient,

'b_x[H_j(x+1)-H_j(x)] + d_x[H_j(x-1)-H_j(x)] = -j(j-1+2alpha)H_j(x)'.

All denominators are nonzero because j<=N and alpha>0, and the final coefficient is nonzero, so the degree is exactly j; also H_j(0)=1. This explicit recurrence supplies one eigenvector for every distinct diagonal value. Self-adjointness makes eigenvectors with different eigenvalues orthogonal. There are N+1 of them, so they are complete, and every h_j is a strictly positive finite sum.

Expanding in this orthogonal basis and applying exp(tL) proves the kernel formula. On the constants' orthogonal complement the smallest eigenvalue is lambda_1=2alpha; Parseval gives the contraction and H_1 proves sharpness.

At alpha=0, b_x=d_x=x(N-x). The endpoints absorb, while the embedded chain from every interior state is the finite simple symmetric nearest-neighbor walk, so absorption is almost sure. Since Lx=0, bounded optional stopping gives 'x=N P_x(hit N)'. Any invariant law gives zero mass to the transient interior states: invariance and almost-sure absorption prevent stationary mass from remaining there. Conversely both endpoint point masses are invariant. Hence all and only stationary laws are 'c delta_0+(1-c) delta_N' with '0<=c<=1'. Finally, for fixed N>=1, each endpoint beta-binomial weight is asymptotic to alpha/N, the normalizer to 2alpha/N, and every interior weight is O(alpha^2). This proves the half-endpoint weak limit. The singleton case is immediate.

## Evidence and scope boundary

Exact data cover 36 positive-parameter rows, 180 states, 180 Hahn vectors, and nine zero-face rows. They audit the formulas but do not establish the theorem by extrapolation. No multisite, open-boundary, or condensation-scaling result is claimed. No priority is claimed.

The Route-A tuple is (A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT), with overall ROUTE_A_REJECTED; Route B is false. Under NO_BAD_EULER_OR_ROOT_NUMBER, no target local datum, Euler factor, root number, automorphy, divisor, functional equation, zero match, or Hilbert--Polya operator is asserted.
