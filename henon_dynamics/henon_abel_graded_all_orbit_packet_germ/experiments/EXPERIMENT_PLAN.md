# HCS-P51 experiment and certificate plan

## Claims under test

1. The symbolic period census has growth at most \(3\varphi^m\).
2. The all-period fixed-algebra degree cap is \(2^m\), not \(1\).
3. The pressure-weighted outer geometric ratio contracts beyond the stated
   certified threshold.
4. The period-four packets agree exactly with HCS-P50 on their common range.
5. The \(u=1\) lower bound grows without bound.
6. Rational norm pushforward is contractive and packetwise isometric, but
   not injective.

## Inputs

Only hash-locked P31, P43, P46, P49, and P50 artifacts are admitted.  No
prime table, Riemann-zero table, fitted coefficient, or post-hoc cutoff is
used.

## Finite sentinels

- symbolic periods \(1\le m\le32\);
- period-four cyclotomic indices \(3\le n\le24\);
- pressure ratios at the exact threshold and a strict interior point;
- Flatters lower partial sums at \(|u|=0.90,0.97,0.99,1\) and
  \(N=20,40,80,160\).

## Adversarial controls

- drop the \(2^m\) degree cost and verify that the resulting threshold does
  not contract the true majorant;
- replace \(|u|<1\) by \(u=1\) and verify divergent lower growth;
- promote the norm pushforward to injective and reject against HCS-P50;
- promote any open continuation/operator claim and reject against the
  theorem ledger.

## Success rule

The paper advances only if the producer, independent checker, and all unit
tests pass and if the proof explicitly retains the degree and Abel costs.
