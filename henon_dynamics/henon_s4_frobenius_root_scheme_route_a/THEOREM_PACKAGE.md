# Theorem package

Let `f(x)=x^4-x-1`, let `L` be its splitting field over `Q`, and for a
rational prime `p` let `X_p` be the geometric roots of the reduction of
`f`.  Write `F_p(alpha)=alpha^p` for arithmetic Frobenius.

## Main theorem

1. `disc(f)=-283`, `f` is irreducible, and `Gal(L/Q)=S4`.
2. For every `p != 283`, the fiber is finite étale of degree four.  If its
   irreducible factor degrees form the partition `lambda_p`, then
   `lambda_p` is exactly the cycle partition of `F_p` on `X_p`.  Geometric
   Frobenius is the inverse permutation and has the same partition.
3. For every positive integer `r`,

   ```text
   N_p(r) = #Fix(F_p^r) = sum_{d in lambda_p, d|r} d.
   ```

   If `E_p(n)` is the number of points of exact period `n` and `C_p(n)` the
   number of primitive `n`-cycles, then

   ```text
   E_p(n) = sum_{d|n} mu(d) N_p(n/d),   C_p(n)=E_p(n)/n.
   ```

4. If `P_p` is the permutation matrix of `F_p` on `C[X_p]`, then as a
   formal identity at zero, hence as a rational function,

   ```text
   Z_p(u) = exp(sum_{r>=1} N_p(r)u^r/r)
          = det(I-uP_p)^(-1)
          = product_{d in lambda_p} (1-u^d)^(-1).
   ```

5. The five partitions and natural densities are

   | partition | class size | density | witness |
   |---|---:|---:|---:|
   | `1+1+1+1` | 1 | `1/24` | 83 |
   | `2+1+1` | 6 | `1/4` | 17 |
   | `2+2` | 3 | `1/8` | 71 |
   | `3+1` | 8 | `1/3` | 7 |
   | `4` | 6 | `1/4` | 2 |

6. At 283,
   `f=(x-115)(x-93)^2(x+18)`, so the fiber is non-étale.  It is the unique
   excluded rational prime.
7. `P_p` is a canonical unitary permutation realization.  It is
   self-adjoint exactly for partitions `1+1+1+1`, `2+1+1`, and `2+2`.

## Workspace ownership boundary

HCS-C12A already owns the universal zero-dimensional statement that
Frobenius on a reduced finite fiber is a permutation, that iterate counts are
traces of its powers, and that the corresponding finite zeta is a reciprocal
permutation determinant.  Items 3--4 specialize that inherited mechanism;
they do not transfer its workspace ownership to C369.  C369 owns precisely
the `x^4-x-1` `S4` Galois proof, the five-class all-good-prime
factor/fixed/primitive/density atlas, the non-étale prime-283 boundary, and
the convention-locked executable ledger.

## Proof chain

For a depressed quartic `x^4+qx+r`, the discriminant is
`256r^3-27q^4`; here it is `-283`.  Modulo 2, `f=x^4+x+1` has neither a
linear factor nor the sole irreducible quadratic factor, so it is
irreducible.  Thus the rational Galois group is transitive and the prime 2
supplies a 4-cycle.  Modulo 7 the displayed `3+1` factorization supplies a
3-cycle.  The group order is divisible by 12 and divides 24.  The order-12
alternative is `A4`, excluded by the odd 4-cycle and also by the nonsquare
discriminant.  Hence the group is `S4`.

At a good prime, finite-field irreducible factors are the orbits of the
power Frobenius.  A cycle of length `d` contributes `d` fixed points exactly
when `d|r`, which proves the fixed formula.  Möbius inversion proves the
primitive formula.  On a `d`-cycle,
`det(I-uP)=1-u^d`; multiplying the blocks and taking the formal logarithm
proves the zeta identity.  The `S4` conjugacy class sizes are
`1,6,3,8,6`, so Chebotarev gives the listed densities.  Direct factorization
at 283 proves the boundary statement.

## Route boundary

This proves genuine source arithmetic and applies the inherited exact
fiberwise primitive-orbit determinant mechanism throughout the quartic
atlas.  The local A1 verdict records exact applicability, not novelty or
ownership of the universal identity.  The package does not create one
autonomous dynamics across primes, a cross-prime Fredholm determinant, a
target Euler product, target zeros, or a Hilbert--Pólya operator.  The locked
tuple is
`(A0_STRUCTURAL_ARITHMETIC_RELATION,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`.
