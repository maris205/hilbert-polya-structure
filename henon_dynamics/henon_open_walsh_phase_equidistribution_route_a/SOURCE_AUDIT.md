# C163 source audit

## Source lock

The only dynamical input is the unchanged C148/C153/C158 open Walsh gate
`A=F3^*diag(1,0,1)`, its cyclic register shift, and the exact full-cycle
identity `B_k^k=A^(tensor k)`.  C158 supplies the already proved one-site
polynomial and modulus invariants.  C163 rederives the claim-bearing phase
algebra independently in both the checker and SymPy path.

No parameter is trained or fitted.  The register length `k` and Fourier mode
`m` are theorem variables; the finite bounds `k<=32` and `m<=24` apply only to
serialized receipts.

## Evidence provenance

- Claim-bearing algebra: exact radicals, rational polynomials, integers, and
  binomial coefficients.
- Decimal values: 60-place sentinels for the first 24 Fourier contraction
  factors; they do not establish non-resonance.
- Non-resonance: the exact primitive-irreducible-integer-polynomial and monic
  rational-minimal-polynomial argument.
- Controls: projector-order similarity, moved-hole order-four torsion, and an
  explicitly out-of-family three-phase closed parent.
- Literature/citations: none; this is a source-internal theorem certificate,
  and no external priority or novelty claim is made.

## Prohibited inputs and outputs

No target spectra, primes, arithmetic local data, Euler factors, root
numbers, automorphy, or Route-B artifacts are read.  The result is not a
self-adjoint/antiunitary limit and is not a target-spectrum construction.
