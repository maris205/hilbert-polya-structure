# SD-C10 Proof Package

## 1. Recurrent-base trace theorem

The matrix trace keeps closed base words. The canonical group trace keeps
identity monodromy. A positive free word is identity exactly when empty, so
only pure atom loops and their repetitions survive. Hence
`Phi(T_s^r)=sum_p p^(-rs)`.

## 2. Ideal theorem

Finite bandwidth reduces noncommutative `L^q` bounds to
`sum_p p^(-q Re(s))`. Diagonal conditional expectation supplies necessity.
Thus `T_s in L^q` exactly when `q Re(s)>1`.

## 3. Analytic tau determinant

The normalized trace-log series gives
`det_Phi(I-zT_s)=product_p(1-zp^(-s))` in the Euler trace-class domain and
the connected analytic component of its germ.

## 4. Label trilemma

- Distinct directed-positive free labels: exact ledger.
- Shared abelian-positive label: exact ledger, proving non-free specificity.
- Inverse reverse label: a base two-cycle becomes identity and creates the
  exact power-two defect `2 sum_n a_n(s)^2`.

## 5. Chiral backtracking

For `B_t=[[0,T_t],[T_t*,0]]`,

```text
Phi_2(B_t^2)=2[sum_n 1/p_n + 2 sum_n |a_n(t)|^2].
```

The mixed term `4 sum |a_n|^2` is positive and divergent. Therefore `B_t`
is not `L^2`; `det_1` and `det_2` fail, while every available `det_q`,
`q>=3`, deletes the first mixed term.

## 6. Exact two-atom fourth trace

For atoms 2 and 3 and `c=cos(t log(3/2))`,

```text
Phi_2(B_t^4)=c^2/6 + 25 sqrt(6)c/36 + 329/144.
```

It is strictly increasing on `c in [-1,1]`; `det_3` retains genuine motion at
order four, after deleting the divergent order-two recurrence.

## 7. Determinant boundary

The analytic tau determinant is holomorphic and Euler-exact but trace-blind
to positive nonidentity geometry. Fuglede--Kadison and Brown data see
magnitude/nonnormal geometry but do not supply the same holomorphic Euler
divisor. No unified determinant is established.
