# HCS-C62 theorem package

Status: **TARGET_LOCKED / IMPLEMENTATION_PENDING / PAPER_PENDING / NOT_RELEASED**

## Conditional theorem target

For (X_pm=G/H_pm), prove the exact character identities

\[
\chi_{\Lambda^2X_+}=\chi_{\Lambda^2X_-},\qquad
\chi_{\operatorname{Sym}^2X_+}=\chi_{\operatorname{Sym}^2X_-},
\]

and then independently compute the two complete orbit atlases.  The target
is that both pairs are nonisomorphic as G-sets; if one pair is isomorphic,
that branch is a certified obstruction and the paper must state the collapse
exactly rather than substitute a different operation.

The associated finite-etale algebras have dimensions 51,040 and 51,360.
Every simple factor must be represented by an exact fixed field in the common
C61 normal closure, with extension-of-isomorphism and core-freeness checks.

## Gates

* G0: byte-rebind the released C61 commit, machine/formal inputs, guard, and
  scope firewall.
* G1: independently enumerate 2-subsets and size-two multisets under the
  complete (W(E_6)) action.
* G2: reconstruct every orbit stabilizer, core, normalizer, conjugacy class,
  and fixed-field degree from element sets.
* G3: verify the two lambda character identities and the exact degree sums.
* G4: prove plus/minus nonisomorphism, or certify the precise collapse if a
  branch fails; no character-only inference is allowed.
* G5: build product-form orbit resolvents with evaluated noncollision at the
  released split prime (p=692717), without claiming expanded
  characteristic-zero coefficients.
* G6: compute signatures and discriminant/different data for all distinct
  factor types, with no maximal-order or local-field overclaim.
* G7: independent checker, deterministic replay, hostile semantic mutations,
  strict schema, self-excluding manifests, paper audit, and release closure.

## KILL controls

Kill C62 if C61 cannot be rebound, if the lambda action is incomplete, if a
  field dictionary is inferred only from subgroup orders, or if the paper
  replaces a collapsed branch with an unrelated claim.  The scope literal
  `NO_BAD_EULER_OR_ROOT_NUMBER` is mandatory.
