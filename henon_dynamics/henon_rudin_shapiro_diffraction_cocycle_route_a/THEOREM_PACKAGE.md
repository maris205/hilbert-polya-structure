# Theorem package — HCS-C248

## Frozen object

Let \(\sigma\) be the constant-length-two substitution
\(a\to ab,b\to ac,c\to db,d\to dc\), with seed \(a\).  Code
\(a,b\) by \(+1\) and \(c,d\) by \(-1\).  Write
\(P_0=Q_0=1\) and, for \(N=2^k\),
\[
 P_{k+1}(z)=P_k(z)+z^NQ_k(z),\qquad
 Q_{k+1}(z)=P_k(z)-z^NQ_k(z).
\]

## Claims proved in the paper

1. The substitution matrix (columns are source letters) has a strictly
   positive third power.  Perron–Frobenius therefore gives the unique invariant
   frequency \((1/4,1/4,1/4,1/4)\).  The fixed point is aperiodic; a finite
   mismatch receipt is included, while the recognizability/desubstitution
   argument handles all putative periods.
2. The coded fixed-point prefix is the coefficient word of \(P_k\) on every
   dyadic length \(2^k\).  On \(|z|=1\),
   \[
   |P_{k+1}|^2+|Q_{k+1}|^2=2(|P_k|^2+|Q_k|^2)=2^{k+2},
   \]
   hence each polynomial is bounded by \(\sqrt{2^{k+1}}\).
3. Put \(R_k=P_kP_k^*,S_k=Q_kQ_k^*,T_k=P_kQ_k^*,U_k=Q_kP_k^*\),
   where \(^*\) means \(z\mapsto z^{-1}\).  Exact Laurent expansion gives
   \[
   \begin{aligned}
   R'&=R+S+z^{-N}T+z^NU,&S'&=R+S-z^{-N}T-z^NU,\\
   T'&=R-S-z^{-N}T+z^NU,&U'&=R-S+z^{-N}T-z^NU.
   \end{aligned}
   \]
4. For the canonical two-sided hull, the symmetric Cesàro/van Hove pair
   averages satisfy \(\eta(0)=1\), \(\eta(m)=0\) for \(m\ne0\).  Thus
   \(\gamma_{RS}=\delta_0\) and \(\widehat\gamma_{RS}=\lambda\) (Lebesgue
   measure).  This is a diffraction assertion, not a claim about the full
   dynamical spectrum.

The three sign-sensitive lines in the infinite recursion are taken from the
published erratum to the Baake–Grimm source and are independently locked in
the JSON checker.

## Route boundary

Finite blocks are not primitive periodic orbits.  The strict tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` and the overall verdict is
`ROUTE_A_REJECTED`.  No target primes/zeros, Euler factors, root numbers,
automorphy, target divisors, or Hilbert–Pólya operators occur.
