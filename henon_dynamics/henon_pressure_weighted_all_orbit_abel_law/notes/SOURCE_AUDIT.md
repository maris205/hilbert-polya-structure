# Source audit

## External source used in a proof

1. **Tomohiro Yamada, “A note on Laurent's paper on linear forms in two
   logarithms: the argument of an algebraic power,” Acta Arithmetica 221
   (2025), 153--163, DOI
   [10.4064/aa241112-2-6](https://doi.org/10.4064/aa241112-2-6),
   [arXiv:1906.00419](https://arxiv.org/abs/1906.00419).**

   The publisher metadata and arXiv manuscript were checked on 2026-08-14.
   Theorem 1.2 and consequence (15) give a lower bound for the principal
   argument of \(\alpha^n\) when \(\alpha\) is algebraic, has modulus one,
   and is not a root of unity.  The theorem's displayed parameter
   \(h=O_\alpha(1+\log n)\) yields
   \(\log|\arg(\alpha^n)|\ge
   -C_\alpha(1+\log n)^2\).  P53 uses only this consequence, followed by
   \(|1-e^{i\theta}|\ge2|\theta|/\pi\) for the principal argument.

2. **Tom M. Apostol, _Introduction to Analytic Number Theory_, Springer,
   1976, DOI
   [10.1007/978-1-4757-5579-4](https://doi.org/10.1007/978-1-4757-5579-4).**

   This is background for the classical summatory totient estimate.  P52
   already proved the exact Laplace consequence used here, so P53 does not
   outsource its Abel normalization to a citation.

## Internal source locks

- HCS-P49: inversion-fixed half-cyclotomic integers;
- HCS-P50: exact trace-field packet sentinels;
- HCS-P51: universal tagged Banach space, all-orbit pressure germ, degree and
  norm envelopes;
- HCS-P52: totient Laplace law, Gamma profile mechanism and tagged-space
  escape argument.

All seven dependency hashes are recomputed by the producer and independent
checker.

## Source ceiling

Yamada's theorem does **not** prove an all-orbit H6 asymptotic, a pressure
sum, a prime law, or a determinant.  It controls only the possible
unit-circle algebraic conjugates after the H6 packet has been constructed.
The all-orbit exchange is proved from the P51 source-native positive
envelope.

No external source was found or cited as proving the pressure-height series'
continuation, a pressure pole, a rational-prime von Mangoldt trace, or a
Hilbert--P\'olya operator.
