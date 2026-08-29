# Independent Proof Routes

Status: frozen two-route ledger; final mechanical QA passed; external release
**HOLD**.

The manuscript deliberately separates two primitive descriptions of the
same central coordinate. Their agreement at the exact biased variance is a
cross-check, not a novelty claim.

## Route I — finite words, matrices, and Gaussian polynomials

Primitive data: literal multiplication in the positive Heisenberg group.

1. The coordinate law
   `H(a,b,c)H(a',b',c')=H(a+a',b+b',c+c'+ab')` gives the two update
   identities under chronological left multiplication.
2. Those identities identify the central coordinate with the number of
   earlier `Y` letters seen by each later `X`.
3. Splitting a fixed-content word by its last letter gives
   `G_(n,j)=G_(n-1,j)+z^(n-j)G_(n-1,j-1)`, hence the Gaussian-binomial
   slice law.
4. Logarithmic derivatives of the normalized product at `z=e^t` give the
   conditional cumulants. Binomial mixing and total variance give the full
   biased moments.

This route controls every finite word and every bias but uses the owned
Gaussian-binomial inversion framework.

## Route II — iid centered pairs

Primitive data: independent Bernoulli variables and their shared-index
incidence pattern. No Gaussian polynomial is used.

1. Writing `Z_ij=(1-B_i)B_j`, disjoint pairs are independent. For each
   triple `i<j<k`, the three covariances are
   `p^3 q`, `p q^3`, and `-p^2 q^2`. Summing them gives the exact complete
   variance
   `binom(n,2)pq(1-pq)+2 binom(n,3)pq(1-3pq)`.
2. With `eta_k=B_k-p`, direct expansion gives
   `C_n-E C_n=sum_k(k-1-p(n-1))eta_k-sum_(i<j)eta_i eta_j`.
3. The ordinary strong law plus summation by parts makes both centered
   terms `o(n^2)` almost surely.
4. A triangular-array Lindeberg argument treats the linear term; the
   quadratic remainder is `O(n)` in `L^1`. This yields the explicit
   `n^(3/2)` CLT variance.

This route independently reaches the exact variance and both limit laws.

## Downstream route separation

- The norm exponent uses the exact positive normal form and the almost-sure
  area law. It has a direct endpoint proof and does not use pressure.
- The pressure kink uses exact extremizing words and their probabilities.
  It does not infer a rare-event limit from the CLT or from matrix norms.

The Python verifier mirrors the separation: raw matrices and Gaussian
recurrences form Lane A; shared-index covariance, centered decomposition,
and exponential-moment squeezes form Lane B.
