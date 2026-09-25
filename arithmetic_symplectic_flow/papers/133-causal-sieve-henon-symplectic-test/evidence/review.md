# Independent model review — ASFS-SCOUT-20260914-97

**Date:** 2026-09-14.

**Reviewed status:** PRE-P0 STOP — CANONICAL SYMPLECTICITY FAILS.

**Review result:** no mathematical correction required for the stated claims.

**Review type:** independent delegated model proof audit; not external peer
review, a novelty assessment, or a Route evaluation.

## Scope and inputs

The reviewer read the [frozen version-1 card](../candidate-card.md),
[paper](../paper.md), [claim ledger](../claim-ledger.md), and
[evidence record](README.md), and checked the defining binary rule against
[050](../../050-causal-binary-sieve-fixed-point-screen/paper.md). The assessed
objects are exactly the polynomial maps H_N and canonical forms omega_N in
the card, for N>=4. No alternate form, changed force, suspension, or restriction
to selected periodic points was used in the review.

## Exact checks

1. **Source and equilibrium.** On binary input, each factor 1-q_d is zero
   exactly when the candidate divisor d is active. Thus the product is exactly
   050's exclusion rule on coordinates 2 through N. Each coordinate reads only
   smaller coordinates. The equations q_n=G_n(q) therefore determine a unique
   real vector inductively. Prime coordinates have empty product, and each
   composite coordinate has an earlier prime divisor at most its square root.
   The resulting finite prime-indicator vector satisfies every equation.
   Neither arbitrary real equilibria nor additional diagonal equilibria are
   missed by this induction.
2. **Inverse, reversal, and volume.** Substitution in both orders verifies
   H_N^{-1}(u,v)=(2G(u)-v,u). The coordinate swap C is an involution and
   C H_N C=H_N^{-1}. The rotation has determinant +1 in every dimension 2m,
   as does the subsequent triangular shear. Therefore the stated global
   determinant +1 and polynomial invertibility are correct.
3. **Matrix identity and sign.** Writing B=DG(y), direct block multiplication
   gives A^T J A with blocks (0,I;-I,2B-2B^T). Independently, the pullback is
   sum_i dy_i wedge (2 sum_j B_ij dy_j-dx_i). The contribution B_4,2=-1 is
   -2 dy_4 wedge dy_2=+2 dy_2 wedge dy_4. The paired contribution B_2,4
   vanishes. Thus the paper's defect sign and factor 2 are correct, and this
   coefficient persists for every larger cutoff.
4. **General causal-force corollary.** Strictly preceding-coordinate
   dependence makes the derivative strictly triangular. A symmetric strictly
   triangular matrix is zero. Zero derivative on a connected open domain
   implies constancy there. The corollary is valid for the stated C^1 force,
   domain hypothesis, canonical form, and unchanged second-order formula.
5. **Control and stopping boundary.** N=3 indeed has constant force, and
   determinant one holds for arbitrary force. These are adequate exact checks
   against confusing invertibility or volume preservation with symplecticity.
   The first nontrivial divisor coupling is already sufficient for the stop.

## Ownership and claim audit

The arithmetic relation and proposed geometric map use the same polynomial
rule. The manuscript reports only finite arithmetic consistency at the unique
equilibrium and does not promote that state to a nontrivial prime orbit family
or global A0 passage. It explicitly leaves changed two-forms, cotangent lifts,
reciprocal/gradient forces, and infinite carriers outside this result.

The positive-dimensional full periodic-orbit ledger requirement is not bypassed:
no finite packet is thickened, no centre or section is selected, and no claim
about a full suspension ledger is made after the symplecticity failure.
Classical P0 remains unadmitted, A0/A1/A2 remain UNASSIGNED, and Route B remains
NOT INVOKED. The appropriate decision is **stop this scheme, portfolio fork**.

No numerical or finite-orbit experiment was required for this audit. The
all-N result follows from the unchanged two-coordinate differential defect,
not from extrapolation of a computed cutoff.
