# HCS-C336 source and claim audit

## Primary and official sources checked

1. E. Baake and H. Wagner, *Mutation--selection models solved exactly with
   methods of statistical mechanics*, Genetics Research 78 (2001), 93--117,
   DOI [10.1017/S0016672301005110](https://doi.org/10.1017/S0016672301005110).
   This is the primary continuous-time binary sequence-space and symmetric
   mutation framework used to identify the mutation operator with a spin/
   hypercube operator.
2. A. S. Bratus, A. S. Novozhilov and Y. S. Semenov, *Linear algebra of the
   permutation invariant Crow--Kimura model of prebiotic evolution*, primary
   author preprint [arXiv:1306.0111](https://arxiv.org/abs/1306.0111).  This
   owns the permutation-invariant linear-algebra reduction and the use of the
   mutation eigenbasis.
3. Y. S. Semenov and A. S. Novozhilov, *Exact solutions for the
   selection--mutation equilibrium in the Crow--Kimura evolutionary model*,
   primary author preprint [arXiv:1408.4417](https://arxiv.org/abs/1408.4417).
   This owns the Crow--Kimura equilibrium/eigenvalue formulation and its
   single-peak context.
4. J. F. Crow and M. Kimura, *An Introduction to Population Genetics Theory*,
   Harper & Row, 1970, ISBN 9780060414382.  This is the historical name owner;
   it is cited bibliographically rather than treated as evidence for the new
   finite-matrix derivation.

## What is reconstructed here

The package combines the exact projective semigroup identity with a full
finite-genome rank-one perturbation theorem.  The retained multiplicities,
all `L+1` secular roots, strict interlacing, and the exact projective gap are
proved in the frozen normalization and independently checked by exact code.
This is a self-contained reconstruction and synthesis, not a literature-
priority claim.

## Workspace collision audit

- C171: mutation-only Ehrenfest/hypercube spectrum; no selection spike.
- C253: finite-population Moran fixation and Green kernel.
- C200: Wright--Fisher diffusion.
- C271: network SIS threshold flow.

The new owner is the rank-one master-sequence selection perturbation and its
complete finite-length spectrum.  It is not a continuation of those packages.

## Explicit nonclaims

Finite-genome analytic crossover is not called a proved infinite-genome error
threshold.  The characteristic and secular polynomials remain source-side
linear algebra.  No target arithmetic local data, Euler factors, root number,
automorphy, target divisor/counting law or functional equation, target zero
match, Hilbert--Polya operator, literature priority, or Route-B authorization
is claimed.
