# C98 theorem package

For targets `i,j`, let `N_ij(a,b)` be the number of the `16!` label
permutations for which `(T_i,T_j)=(a,b)`, and let
`m_i(a)=sum_b N_ij(a,b)`.

## Theorem

1. The C90 survival array and C88 boundary rows determine all joint PMFs by

   ```text
   N_ij(a,b)=S(a-1,b-1)-S(a,b-1)-S(a-1,b)+S(a,b).
   ```

   All 400 PMFs are nonnegative, normalize to `16!`, and recover both C88
   marginals.
2. Whenever `m_i(a)>0`,

   ```text
   K_ij(a,b)=N_ij(a,b)/m_i(a)
   ```

   is a normalized exact conditional kernel row.  Exactly 4980 of the 6800
   candidate rows are attainable.  The other 1820 rows and their moments are
   undefined and stored as `null`.
3. Every one of the 115600 cells satisfies Bayes balance:

   ```text
   P(T_i=a) K_ij(a,b) = P(T_j=b) K_ji(b,a)
                       = N_ij(a,b)/16!.
   ```

4. For all 400 ordered pairs, exact rational arithmetic verifies

   ```text
   E[E(T_j | T_i)] = E(T_j),
   E[Var(T_j | T_i)] + Var(E[T_j | T_i]) = Var(T_j).
   ```

5. Each of the twenty diagonal kernels is the identity on every attainable
   time: `K_ii(a,b)=1` exactly when `a=b`.

## Proof certificate

Two-dimensional Mobius inversion on the finite threshold grid gives the PMF
formula.  Row and column sums telescope to the C88 marginals.  Division by a
positive row mass proves conditional normalization; zero mass leaves no
conditional probability space and therefore yields `null`.  Joint transpose
`N_ij(a,b)=N_ji(b,a)` proves Bayes balance.  Weighted sums of the conditional
means and variances prove the two tower identities directly.  On the
diagonal, the two random variables coincide pointwise.

These are finite probability identities only.  The package makes no
arithmetic/local-data, Euler-factor, root-number, automorphy, full
Burnside/table-of-marks, or Hilbert--Polya operator claim.
