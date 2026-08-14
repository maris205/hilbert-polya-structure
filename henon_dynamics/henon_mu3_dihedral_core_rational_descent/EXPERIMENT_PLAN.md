# HCS-C53 experiment plan

The experiments certify exact algebra and source provenance. They are not a
finite-prime trace-table project.

## B0. Provenance gate

- Record the C52 implementation commit and certificate hash exactly.
- Parse the source-ordered cubic and quadratic without reindexing.
- Fail on group order other than 24 or a Reynolds denominator other than 24.

## B1. Family descent gate

- Generate \(M_n\) from the parity rule.
- For a control range including \(n=2,3,4\), verify exactly
  \(C_n(M_nx)=C_n(x)\),
  \(Q_{n,\rho}(M_nx)=\rho Q_{n,\rho^2}(x)\), and
  \(M_n\tau(M_n)=I\) in \(\mathbf Q[\rho]/(\rho^2+\rho+1)\).
- Verify \(M_n\tau(B_n)=B_n\), the closed determinant formula, and the
  substitutions for \(C_{n,0},Q_{n,0}\).
- Keep the symbolic derivation in the proof package as the all-\(n\) proof.

## B2. Fourth-row group gate

- Reconstruct all \(r^k\) and \(r^ks\), \(0\le k<12\), and certify 24
  distinct elements.
- Check \(\delta(r)=r^{-1}\), \(\delta(s)=sr^{-1}\), and the homomorphism
  law on all \(24^2\) products.
- Check that \(\delta\) permutes all 24 graphs and that the averaged cycle
  uses coefficient \(1/24\).
- Report the descended object as a nonconstant finite étale group scheme
  split by \(K\), not as 24 individual rational automorphisms.

## B3. Local-factor gate

- Symbolically verify the quadratic split identity and exponent conversion
  \(2/n\mapsto4/n\).
- Emit the reduced denominator \(n/\gcd(n,4)\) only for certified rows
  \(n=2,3,4\); label later rows conditional.
- Verify the inert identity
  \(P_{K,v}(U^2)=P_p(U)P_p(-U)\) for generic exact test polynomials.
- For \(n=4\), emit exactly one rank-255/exponent-one rational split factor;
  never emit a rank-127.5 system or a global square root.

## Independent check

The producer writes a canonical JSON certificate. A checker independently
reconstructs all polynomial, matrix, group, and local-factor identities and
rejects undocumented fields. The \(p=7\) raw first core trace \(-469\)
(normalized \(-67/7\)) is labeled
PRE_C53_RECONNAISSANCE_REGRESSION_ANCHOR_UNCERTIFIED. The checker verifies
its recorded arithmetic consistency but does not independently reconstruct
the underlying fixed-locus point counts. No C52 provenance is asserted,
and C53 does not turn the anchor into a trace table.

## Kill gates

Stop release if any of the following occurs:

- source order or closing edge differs from C51;
- \(\det B_n\) vanishes or the \(n=4\) specialization is not \(24\theta\);
- group cardinality, transport, or Reynolds denominator differs from the
  frozen order-24 convention;
- an all-\(n\) smooth/motive claim appears;
- split-local clearing is written as an inert/global square root;
- integrality is inferred merely by clearing the projector denominator;
- producer and checker agree only by consuming the same derived output.
