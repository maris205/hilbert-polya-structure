# HCS-C20 source and novelty audit

## 1. Dynamical source lock

The dynamical family is the area-preserving Hénon recurrence used in the
repository's foundational Paper 5,
[`../docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf`](../docs/prior_work/papers/5-An%20Area-Preserving%20Henon-Map%20Model.pdf),
written in Hamiltonian coordinates as

\[
x_{t+1}=a-x_t^2-x_{t-1}.
\]

The period-seven scalar equation and its apparent print-error diagnosis are
inherited, without alteration, from HCS-C19.  In particular:

- the literal formula printed by Endler--Gallas fails one exact
  \(\mathbb F_{103}\) orbit specialization;
- the adopted placement of the constant passes that fibre and is generically
  certified by the exact neighbor correspondence; and
- no publisher-issued erratum or exhaustion of the full saturated
  period-seven scheme is asserted.

This project does not refit the septic, use Riemann zeros, or choose parameters
from target arithmetic data.

## 2. Primary prior art

The specific source formula comes from Endler and Gallas,
[*Conjugacy classes and chiral doublets in the Hénon Hamiltonian
repeller*](https://doi.org/10.1016/j.physleta.2006.04.042), Physics Letters A
356 (2006), 1--7.

The general arithmetic geometry uncovered here is not new:

- Ellenberg's
  [*Endomorphism Algebras of Jacobians*](https://doi.org/10.1006/aima.2001.1994)
  constructs endomorphisms from double-coset algebras of Galois covers.
- Hoffman, Liang, Sakai, and Wang,
  [*Genus 3 curves whose Jacobians have endomorphisms by
  \(\mathbb Q(\zeta_7+\bar\zeta_7)\)*](https://doi.org/10.1016/j.jsc.2015.09.004),
  explicitly study genus-three reflection quotients of genus-eight
  (D_7\)-covers, prove the same real cubic multiplication, and explain the
  factorization of good-prime zeta numerators into three conjugate
  quadratics.
- Kani and Rosen,
  [*Idempotent relations and factors of Jacobians*](https://eudml.org/doc/164555),
  provide the general quotient-Jacobian isogeny mechanism.
- Lange and Ortega's work on
  [degree-seven étale cyclic covers](https://arxiv.org/abs/1604.01700)
  identifies the corresponding Prym as a product of two genus-three
  Jacobians.

These references were checked before framing the new claims.  HCS-C20 does
not present (D_7\)-covers, the genus (8/3/2\) quotient pattern, Prym
decomposition, or real cyclotomic multiplication as new general theory.

## 3. Specific contribution

The repository and the inspected primary sources did not already contain the
following source-locked identification for the adopted Hénon septic:

1. its ordered-edge curve is its geometrically connected (D_7\) splitting
   curve;
2. the sign quotient is the explicit hyperelliptic curve
   \(w^2=Q_6(\sigma)\);
3. the quadratic edge extension is
   \(\mathbb Q(C)(\sqrt{Q_6})\), with an explicit closed degree-six branch
   divisor;
4. the Hénon time correspondence gives the exact RM generator on the scalar
   Jacobian; and
5. a selected-prime tame-cover and simultaneous-normalization theorem
   upgrades the three frozen branch-corrected rows to genuine local
   Hasse--Weil numerators; and
6. all three certified scalar numerators obey the predicted norm law over the
   same real cubic field.

The novelty claim is therefore a concrete arithmetic-dynamical recognition
and certification theorem for this Hénon period-seven curve, plus its scoped
Hilbert--Pólya consequence.  It is not a new construction of the classical
RM locus.

## 4. Claim boundary

- (E\), (B\), and (C\) denote smooth projective normalizations, not their
  potentially singular affine plane images.
- The Jacobian product is a \(\mathbb Q\)-isogeny, not a polarized isomorphism.
- Real multiplication means an embedding of the real cubic field into
  \(\operatorname{End}_{\mathbb Q}^0(\operatorname{Jac}(C))\); equality of the
  full endomorphism algebra and absolute simplicity are open.
- The \(B,C,E\)-factors at \(5,11,13\) are certified by the exact
  selected-prime theorem in
  [SELECTED_PRIME_GOOD_REDUCTION.md](SELECTED_PRIME_GOOD_REDUCTION.md).
  No good-reduction claim is extrapolated to other primes.
- Fixed period seven and finite-dimensional self-adjoint correspondence data
  do not define a Riemann divisor, global dynamical determinant, or
  Hilbert--Pólya operator.
