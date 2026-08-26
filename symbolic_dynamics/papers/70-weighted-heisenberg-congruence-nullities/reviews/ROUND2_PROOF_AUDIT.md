# Round 2 proof audit

## Provenance and release posture

**Provenance:** same independent cross-agent reviewer as Round 1.  The
requested GPT-5.4 child remained unavailable because of the structural thread
cap; this report does not claim GPT-5.4 provenance.  External release remains
**HOLD**, and no priority conclusion is made.

## Verdict and score

**Verdict:** **INTERNAL THEOREM PASS WITH ONE MINOR PRECISION EDIT.**

**Score:** **9.0/10** after Round 1 revision.

The cross-characteristic and right-action gaps are closed.  A fresh trace from
the discrete group law to the full nullity formula found no missing
multiplicity, field, sign, or coefficient hypothesis.  One sentence in the
recurrence proof can now be made exact rather than saying “up to reversing.”

## Round 1 closure audit

1. **M1 closed.** Lemma `lem:irreducibles` constructs every module over the
   actual algebraic closure of `F_p`.  Distinct clock eigenlines plus the
   cyclic shift prove irreducibility; central scalars distinguish nonlinear
   types; the squared-degree sum closes completeness in the split semisimple
   algebra.
2. **M2 closed.** For
   `phi_(lambda,v)(q)=lambda(pi(q)v)`, the manuscript now computes
   `R_h phi_(lambda,v)=phi_(lambda,pi(h)v)`.  Hence the chosen operator has
   blocks `alpha I+beta pi(a)+gamma pi(b)` without a hidden dual.
3. **Dual convention closed.** Character pairs and nontrivial central
   characters are permuted by inversion, so the summed formula is unchanged.
4. **Block controls added.** Four direct blocks independently check the
   determinant and zero/one-nullity statements on both Fermat strata.

## Independent proof trace

### Quotient and convention

- The group law gives `ab=bac`, consistent with the clock--shift relation
  `UV=zeta VU`.
- `N_ell`-fixed points are constant on left cosets; normality identifies the
  coset set with `Q_ell`.
- The local equation becomes `alpha I+beta R_a+gamma R_b` on functions on
  `Q_ell`; the matrix-coefficient calculation fixes the exact block.
- Scalar extension preserves rank and nullity, and `p!=ell` is exactly the
  Maschke hypothesis.

### Character and nonlinear strata

- Eliminating `v` from `alpha+beta u+gamma v=0` gives
  `(alpha+beta u)^ell+gamma^ell=0` because `ell` is odd.
- `t^ell-1` is separable because `p!=ell`, so the gcd degree counts roots
  without multiplicity.
- In `diag(alpha+beta zeta^j)+gamma V`, a permutation using one cycle edge
  must use all of them.  The full cycle has positive sign for odd `ell`, and
  the cyclotomic product is `alpha^ell+beta^ell`.
- Because `gamma!=0`, the cyclic first-order equation determines every
  coordinate from one coordinate; singularity therefore means nullity
  exactly one.
- Each nonlinear type occurs `ell` times and there are `ell-1` types, giving
  the exact jump `ell(ell-1)`.

## CRITICAL issues

None.

## MAJOR issues

None.

## MINOR issues

### m1. Remove the unnecessary recurrence-orientation hedge

In `sections/5_nonlinear_blocks.tex`, the equation is said to hold “up to
reversing the cyclic indices.”  With the displayed convention
`V e_j=e_(j+1)`, one has exactly `(Vx)_j=x_(j-1)`, so the recurrence is

```text
(alpha+beta zeta^j)x_j + gamma x_(j-1)=0.
```

Delete the hedge and state this coordinate calculation explicitly.  No
formula changes.

## Source and ownership recheck

The complex/unitary scope of Gurevich--Hadani is now honestly described, and
the cross-characteristic result is proved locally.  Lind--Schmidt Example
4.4(a) remains only the owner for the integer `1+x+y` mixing example.
Zaidenberg and Ford--Jha are used for the correct abelian/resultant
neighborhood.  No exact-formula collision was found in the bounded audit;
this remains non-certifying.

## Control and build audit

- Four direct clock--shift blocks: PASS.
- Ten full quotient matrices: PASS.
- Round-1 build: 7 A4 pages.
- Log warnings/undefined references/undefined citations/box warnings: zero.

## Release recommendation

**INTERNAL GO AFTER m1 / EXTERNAL HOLD.** Apply the one precision edit, rerun
the controls and build, freeze Round 2, and retain the specialist-source hold.
