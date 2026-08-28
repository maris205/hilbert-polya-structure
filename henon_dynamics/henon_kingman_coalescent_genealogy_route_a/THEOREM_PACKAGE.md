# HCS-C215 theorem package: the partition-valued Kingman coalescent

## Frozen object and conventions

For each `n>=1`, start from the discrete partition of `[n]`.  Every unordered
pair of extant blocks merges at rate one.  The resulting process is the
partition-valued Kingman coalescent; its block count `K_t` starts at `n` and
decreases to the absorbing state `1`.  Write

```text
lambda_k = binom(k,2) = k(k-1)/2,   k>=2,
T_n = inf{t:K_t=1},
L_n = integral_0^{T_n} K_t dt = sum_{k=2}^n k E_k.
```

The family is coupled projectively by restricting a partition on `[n+1]` to
`[n]`.  This convention is important for the monotone `n->infinity` claim.

## Main theorem

For every `n>=1`:

1. **Block chain and all transitions.**  `K_t` is pure death with
   `Q_{k,k-1}=lambda_k`, `Q_{k,k}=-lambda_k`, and `Q_{1,1}=0`.  For
   `1<=j<=i`,

   ```text
   p_ij(t) = (prod_{m=j+1}^i lambda_m)
             sum_{ell=j}^i exp(-lambda_ell*t)
             / (prod_{m=j,m!=ell}^i (lambda_m-lambda_ell)),
   ```

   with `p_ii(t)=exp(-lambda_i*t)`, `p_ij=0` for `j>i`, and the identity row
   at `t=0`.  This is the all-`n` hypoexponential transition law.

2. **Independent holding/jump construction.**  At `k>=2`, the holding time
   `E_k` is `Exp(lambda_k)`, the next unordered block pair is uniform among
   `lambda_k` pairs, and the holding times are mutually independent and
   independent of the uniform merger jump chain.  Thus

   ```text
   T_n = sum_{k=2}^n E_k.
   ```

3. **MRCA transform and moments.**  For `s>=0`,

   ```text
   E[exp(-s*T_n)] = prod_{k=2}^n lambda_k/(lambda_k+s),
   E[T_n] = sum_{k=2}^n 1/lambda_k = 2(1-1/n),
   Var(T_n) = sum_{k=2}^n 1/lambda_k^2.
   ```

4. **Projective infinite-sample absorption.**  Under the standard projective
   coupling, `T_n` is nondecreasing and converges almost surely to a finite
   `T_infinity`.  Its mean is `2`, its variance is
   `4*(2*zeta(2)-3)=4*pi^2/3-12`, and its Laplace transform is the convergent
   product `prod_{k=2}^infinity lambda_k/(lambda_k+s)`.  The finite means and
   variances converge to these values; this is not a statement about
   independently resampled marginal sums.

5. **Total branch length.**  Since `k E_k` is `Exp((k-1)/2)`,

   ```text
   E[exp(-s L_n)] = prod_{j=1}^{n-1} (j/2)/(j/2+s),
   E[L_n]=2 H_{n-1},   Var(L_n)=4 H_{n-1}^{(2)}.
   ```

   The same Laplace product is the product of the spacings of the order
   statistics of `n-1` iid `Exp(1/2)` variables.  Therefore `L_n` has the law
   of their maximum and, for `ell>=0`,

   ```text
   P(L_n<=ell)=(1-exp(-ell/2))^(n-1).
   ```

6. **Boundary and determinant convention.**  At `n=1`, there is one partition,
   `T_1=L_1=0`, and every transform equals one.  A finite Markov transition
   determinant, trace-log, or Laplace product is not an Artin--Mazur dynamical
   zeta and is not used as one.

## Proof and evidence boundary

The pair-clock construction gives total exit rate `lambda_k` and uniform pair
selection; memorylessness yields independent holdings.  Resolving the pure
death forward equations by partial fractions gives the transition formula.
The MRCA transform and moments follow by multiplying the independent
exponential transforms.  In the standard projective construction, restriction
of the `(n+1)` process to `[n]` gives the `n` process, so adding a sampled leaf
can only delay the common ancestor and establishes monotone convergence.  The
summable rates give finite limiting moments and the convergent Laplace product.

For the tree length, scaling `E_k` by `k` changes its rate to `(k-1)/2`.
Exponential order-statistic spacings for `m=n-1` iid `Exp(1/2)` variables have
rates `m/2,(m-1)/2,...,1/2`; their sum has exactly the same Laplace product.
Thus the maximum CDF, not an empirical fit, is the displayed power law.

The producer evaluates a fixed grid through `n=12`.  The checker independently
recomputes partial fractions, row sums, Chapman--Kolmogorov, moments, Bell
numbers, and the maximum CDF.  SymPy verifies the rational identities and
beta-integral transform.  These finite checks do not replace the all-`n`
theorem.

## Scope and route verdict

The coalescent is a genealogical stochastic process with no intrinsic
rational-prime carrier, primitive periodic-orbit clock, arithmetic divisor,
or natural Hilbert--Pólya lift.  No target prime/zero table, local arithmetic,
Euler factor, root number, target divisor, functional equation, automorphy
assertion, or Route-B input is used.

```text
(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)
overall = ROUTE_A_REJECTED; route_b_invocation_allowed = false.
```

## Reference (attribution only)

* J. F. C. Kingman, *The coalescent*, Stochastic Processes and their
  Applications 13, 235--248 (1982), DOI
  `10.1016/0304-4149(82)90011-4`.
