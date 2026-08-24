# Theorem and boundary package — C119

## Contraction theorem

For

```text
A=[[3/4,-1/4],[1/2,0]],
```

the eigenvalues are `1/2,1/4`, `det A=1/8`, and

```text
spec(A^T A)={(7+3 sqrt(5))/16,(7-3 sqrt(5))/16} subset (0,1).
```

Hence `||A||_2<1`. Also `A^n-I` is invertible for every `n>=1`, so the origin
is the only finite-period point over `C`.

## Fock nuclearity and Fredholm theorem

Let `F_s(C^2)=direct_sum Sym^m(C^2)` and
`Gamma(A)=direct_sum Sym^m(A)`. If `s_1,s_2` are the singular values of `A`,
then the singular values of `Gamma(A)` are `s_1^i s_2^j`, `i,j>=0`. Therefore

```text
||Gamma(A)||_1 = 1/((1-s_1)(1-s_2)) < infinity.
```

The operator is trace class. Its eigenvalues, with algebraic multiplicity, are
`2^(-i)4^(-j)`, and for every `n>=1`,

```text
Tr Gamma(A)^n = 1/((1-2^(-n))(1-4^(-n))).
```

Consequently its Fredholm determinant is the entire genus-zero product

```text
D(z)=product_{i,j>=0}(1-z 2^(-i)4^(-j)).
```

Its zeros are exactly `z=2^k`, `k>=0`, with multiplicity `floor(k/2)+1`.

## Boundary

The source-defined Fock determinant theorem is exact structural evidence, but
the strict Route-A evaluator asks for a primitive-orbit-owned determinant and
target-divisor checks.  Neither is present.  The canonical tuple is therefore
`(A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`: A1 records the absence of nontrivial
periodic orbits, A2 records the missing orbit/target bridge, and A3 records the
absence of target functional-equation, Gamma-factor, counting-law, and
continuation checks.  Overall status remains `ROUTE_A_EXPLORATORY`.
