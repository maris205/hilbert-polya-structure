# Evidence — `ASFS-SCOUT-20260914-35`

The map is the standard sum of prime factors with repetition; its iteration is
catalogued at [OEIS A002217](https://oeis.org/A002217/internal).

For `n=product_{i=1}^r p_i` composite, `sum_i p_i <= product_i p_i`, with
equality only for `r=2` and `p_1=p_2=2`, i.e. `n=4`. One proof is induction
using `ab>=a+b` for integers `a,b>=2`, equality only at `(2,2)`; adding further
factors makes the inequality strict. Thus `A(n)<n` for composite `n>4`.
