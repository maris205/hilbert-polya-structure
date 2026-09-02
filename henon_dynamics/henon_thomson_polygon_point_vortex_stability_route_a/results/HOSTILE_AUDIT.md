# Hostile integrity and failure-mode audit

## Mathematical convention audit

- **Hamiltonian sign:** PASS.  Direct differentiation of
  `H=-(Gamma^2/(2*pi)) sum log|z_j-z_k|` with
  `Gamma z_dot=J grad H` gives
  `Omega=Gamma(N-1)/(4*pi R^2)` in the declared orientation.
- **Raw Hessian independence:** PASS.  The checker starts from Cartesian pair
  derivatives and never imports or copies the producer's row construction.
- **DFT sign:** PASS.  The reconstructed symbol is
  `c diag(2(N-1)-q_m,q_m)` and the Hamiltonian block squares to
  `-c^2 q_m(2(N-1)-q_m) I`.
- **Symmetry slice:** PASS.  The `m=0` rotation/scale Jordan block and the
  physical translation plane are identified; the centered first-harmonic
  complement remains elliptic.
- **Heptagon boundary:** PASS.  The conjugate `m=3,4` labels give a real
  four-dimensional nilpotent component with algebraic multiplicity four and
  geometric multiplicity two.  No nonlinear-stability claim is made.
- **Parameter faces:** PASS.  `N<3`, `R=0`, `Gamma=0`, `Gamma<0`, and
  `R` tending to infinity are stated with their distinct meanings.

## Rejected corruptions

An initial hostile review found that payload hashing alone did not reject raw
duplicate JSON keys, unknown/missing/wrongly typed fields, a corrupted
`reduced_role`, or every same-size duplicate/drop-replace row.  Those were
release-blocking integrity defects; none altered the mathematical trichotomy.

The repaired checker now uses a duplicate-reject loader, forbids nonstandard
JSON constants and bool-as-int confusion, and enforces exact top/nested/row
key sets, exact scalar/container types, complete row order, and unique semantic
keys.  It locks the full headline, audit, model, DFT, reduction, proof,
source-owner, obligation, nonclaim, Route-A, scope, count, row, and boundary
contracts, including every `reduced_role` value.

The mutation gate sends 73 schema/semantic/order/duplicate-drop attacks with
repaired payload hashes, then a stale-hash attack, a raw duplicate-key attack,
and a raw `NaN` attack.  Coverage includes unknown and missing keys at all
levels, bool/type confusion, all five row families, the heptagon and first
hyperbolic modes, slice dimensions/actions, scale law, boundary semantics, and
the complete Route-A firewall.  All **76/76** are rejected.

The root-sum and slice audits were strengthened at the same time.  SymPy now
coefficient-counts every root sum instead of inserting `N*m`, while both the
numeric checker and exact audit act on explicit rotation, scale, translation,
and centered first-harmonic vectors.

## Seven research failure modes

1. **Phantom target:** absent; the theorem concerns only the frozen vortex
   Hamiltonian.
2. **Post-hoc fitting:** absent; no prime or target-zero data enter.
3. **Train/test leakage:** inapplicable; the complete formulas precede the
   finite regression ledger.
4. **Computation as proof:** prevented by the all-`N` root-sum and sign proof.
5. **Citation laundering:** prevented by explicit classical ownership and
   claim-level source use; every proof is reconstructed in-package.
6. **Hidden singular boundary:** prevented by the symmetry and parameter-face
   ledger and the strict linear-only treatment of `N=7`.
7. **Cross-owner theorem assembly:** absent; no theorem from another package
   is imported as a premise.

## Route and release conclusion

The polygon family has no rational-prime carrier, logarithmic-prime clock,
isolated primitive-orbit census, target determinant, analytic target bridge,
or same-clock quantum lift.  The honest tuple is
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, the overall decision is
`ROUTE_A_REJECTED`, Route B is locked false, and the scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No mathematical, evidence, source, or
presentation release blocker remains.
