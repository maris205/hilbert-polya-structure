# Paper plan — P132

## Literal system

For `w in {0,1}^n`, the simultaneous update is

```text
P_n(w)_i = 1 iff w_1+...+w_i >= i/2.
```

The weak tie convention is part of the definition.  Husfeldt--Rauhe already
own this exact coordinate predicate as a dynamic prefix-majority query; the
residual object is its repeated full-vector feedback.

## Claim spine

1. The fixed language consists of the two alternating--constant families and
   has `n+1` words.
2. A maximal fixed prefix amplifies by a factor two, giving global convergence
   and sharp maximum depth `ceil(log_2 n)`.
3. Every target fibre is an explicit product of Catalan excursions and one
   terminal meander; empty fibres are characterized by run parities.
4. The image has Fibonacci size and the all-one target is the unique largest
   fibre for `n>=2`, of size `binom(n,floor(n/2))`.

## Proof architecture

- Balance-state analysis proves the fixed language.
- Prefix compatibility plus a locked-tail amplifier proves the temporal
  theorem; `1 0^(n-1)` is the sharp witness.
- Crossing the edge between `-1` and zero cuts inverse walks into independent
  excursions and a meander.
- Absolute value injects every fibre into the meanders and gives strict
  extremality.

## Credit boundary

Prefix-majority queries, Catalan/ballot/reflection methods, sign-change theory,
Fibonacci regular languages, general majority networks, and generic finite-map
zeta notation are background.  The owner search is bounded and supports no
novelty or priority inference.  External status remains `HOLD_EXTERNAL`.
