# Classical realizations of the candidate's new limit-set conclusion

2026-09-06. Supplement to `PROOF_PACKAGE.md`; no new fixed-point formula is
claimed. All times below are native integer iterates, and `pi(N)` counts
primitive orbits of length at most `N`.

## 1. Two distortion primes on a genuine solenoid

Let `X` be the Pontryagin dual of the discrete additive group `Z[1/15]`,
and let `T:X -> X` be dual to multiplication by 2. This is the confined
`S`-integer system with `K=Q`, `S={3,5}`, and multiplier 2 in BCH
Definition 9.1.2. Proposition 9.1.4 supplies the classical count

`Fix(T^n) = (2^n-1) |2^n-1|_3 |2^n-1|_5`, for every `n>=1`.

Its specialized formula can also be checked directly from the finite
quotient `Z[1/15]/(2^n-1)Z[1/15]`: localization removes exactly the factors
3 and 5 from the positive integer `2^n-1`. This elementary explanation is
not promoted as an original result.

Classical lifting of valuations gives

`v_3(2^n-1) = 0` for odd `n`, and `1+v_3(n)` for even `n`;

`v_5(2^n-1) = 0` if `4` does not divide `n`, and `1+v_5(n)` otherwise.

Thus the FAD data may be taken to be

`A=[2], c=1, Lambda=2, w=4,`

`r_n = 3^(-1_{2|n}) 5^(-1_{4|n}),`

`s_{3,n}=1_{2|n}, s_{5,n}=1_{4|n}, t_{3,n}=t_{5,n}=0`.

The exponent periods 2 and 4 are coprime to 3 and 5 respectively; `r` is
a positive gcd sequence of period 4. There is one dominant root, 2, and
two active primes. The new candidate conclusion is that the accumulation
set of `N pi_T(N)/2^N` is a Cantor set and

`N_epsilon(L_T) <= C(1+log(1/epsilon))^4`.

## 2. A wild algebraic-group example

Fix an odd prime `p`, and let `U(x)=x^p+x` on `F_p`'s algebraic closure,
viewed as the points of the additive algebraic group. BCH Example 7.2.7
records the classical count (attributing it there to Bridy, Proposition 9)

`Fix(U^n)=p^(n-p^(v_p(n)))`.

For clarity, this also follows from the elementary additive-polynomial
calculation. Writing `F(x)=x^p` and `n=p^a m`, `p` not dividing `m`, the
first nonzero power of `F` in `(1+F)^n-1` is `F^(p^a)`, with nonzero
coefficient, and its highest power is `F^n`. The additive polynomial has
degree `p^n` and inseparable degree `p^(p^a)`; over the algebraic closure
its distinct-root count is their quotient. This is a verification of the
known input, not a candidate contribution. Bridy's original paper was not
separately read for this supplement, so attribution to it remains explicit
through BCH.

The FAD data are `A` the empty matrix, `c=Lambda=p`, `r=1`, `S={p}`,
`s=0`, `t=1`, and period 1. The wild term is genuinely nonzero. Corollary 2
therefore gives a Cantor accumulation set for `N pi_U(N)/p^N`, with
covering bound `C(1+log(1/epsilon))^2`.

BCH Example 7.2.6 gives the same count and FAD parameters, with a direct
computation, for the cellular automaton `(x_i) -> (x_{i+1}+x_i)` on
`F_p^Z`. These are two classical realizations, not two independent new
theorems and not an assertion of dynamical conjugacy.

## 3. Simultaneously multiprime and wild

Take the product of Example 1 with Example 2 at `p=7`. Product fixed-point
counts multiply, and BCH Example 7.1.3 records FAD closure under products.
For `V=T x U` on `X x overline(F_7)`,

`Fix(V^n) = (2^n-1)|2^n-1|_3|2^n-1|_5 7^(n-7^(v_7(n)))`.

Here `A=[2]`, `c=7`, `Lambda=14`, with dominant multiplicative sequence
`14^n-7^n`; `S={3,5,7}`. The 3/5 exponents and `r` are as above, and
`s_7=0,t_7=1`. The common period is 4 (the 7-exponent period is 1).
This is a genuine realized hyperbolic FAD system in both missing regimes,
not an arbitrary numerical sequence declared realizable.

The candidate yields a Cantor accumulation set for `N pi_V(N)/14^N`,
zero upper box dimension, and bound

`N_epsilon(L_V) <= C(1+log(1/epsilon))^6`.

These are applications of one theorem, not proposed separate papers.
Constants depend on the fixed system; the logarithmic exponents are upper
bounds and are not claimed sharp.

Source for all numbered BCH passages:
[Byszewski–Cornelissen–Houben, arXiv:2209.00085v2](https://arxiv.org/pdf/2209.00085v2).
The full source/version qualifications remain in `SOURCE_AUDIT.md`.
