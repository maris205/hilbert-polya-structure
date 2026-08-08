# HCS-C21 exact experiment plan

## 1. Research question

For the area-preserving Hénon recurrence

\[
x_{t+1}=A-x_t^2-x_{t-1},
\]

does the published period-six chiral doublet acquire a nontrivial
chronological sector after one restores ordered edges, and can any exact
period-six/period-seven algebraic relation survive as a primitive
chronology-preserving bridge?

The operational subquestions are:

1. What is the connected compactified geometry and Galois group of the
   period-six twelve-state ordered-edge cover?
2. How does the exact order-six time generator act on weight-one cohomology?
3. How does this compare with the certified HCS-C20 period-seven cover?
4. Is the shared quadratic marker field at periods six and seven primitive,
   or does it descend from lower period?

## 2. Prior-work boundary

The following are inputs, not claims of HCS-C21:

- the Paper-5 recurrence and its monic Hamiltonian rescaling;
- Endler--Gallas's factors
  $S_6=(C^{\mathrm{mark}}_6)^2D^{\mathrm{mark}}_6N^{\mathrm{mark}}_6$,
  $C^{\mathrm{mark}}_6=\sigma-2$, and
  $P_6=f_{\eta}f_{-\eta}$, $\eta^2=A-3$;
- Gallas's orbit-class counts through period seven;
- HCS-C12C's genus-zero coarse marker quotients;
- HCS-C20's connected genus-eight (D_7) ordered cover and genus-two
  rotation quotient.

The new target is the normalization and chronological cohomology of the
period-six ordered-edge object, followed by a scoped comparison.

## 3. Precommitted hypotheses and falsifiers

### H1: the ordered-edge scheme is a genuine connected (D_6)-cover

Required evidence:

- exact matching map between the two cubic root sets;
- all six recurrence equations reduced to zero;
- recovery of $\eta$ and all cubic roots from one ordered orbit;
- absolute irreducibility over $\overline{\mathbb Q}(\eta)$;
- nonsquare cubic discriminant and a free transitive twelve-state action.

Falsify H1 if the cover splits geometrically, the ordered edge does not
recover the radical, or the group has order below twelve.

### H2: point-level time survives but weight-one time collapses at period six

Required evidence:

- complete finite and infinite branch ledger;
- exact genus of the smooth projective normalization;
- exact fixed field of the order-six subgroup, not merely a candidate
  quotient equation;
- a Riemann--Hurwitz check on the quotient map;
- characteristic and minimal polynomials of $\tau^*|H^1$.

Falsify H2 if infinity adds ramification, the quotient has a different genus,
or a nontrivial time eigenvalue occurs on $H^1$.

### H3: the period-six/period-seven marker coincidence is lower-period aliasing

Required evidence:

- explicit identities through (D_1);
- full fiber-product factorization and normalization boundary;
- period-five and period-seven half-orbit base-change controls;
- a clock-equivariant divisibility theorem with dominance/free-locus
  hypotheses.

Falsify H3 if a primitive ordered-cover correspondence survives and respects
a faithful one-step time generator.

## 4. Exact computational design

The producer must use exact symbolic arithmetic only.  It computes:

1. the source polynomial product and its discriminant;
2. the base-changed cubic and its absolute irreducibility ledger;
3. the root matching and its inverse modulo the cubic;
4. the complete six-coordinate recurrence;
5. the twelve-state dihedral permutation action;
6. finite and infinite branch data and Riemann--Hurwitz genus;
7. the Vandermonde action, rotation fixed field, quotient genus, and
   $H^1$-character;
8. the $n=6$ versus $n=7$ chronology dimensions;
9. the lower-period marker factorization and half-orbit controls.

The independent checker may not import the producer or predecessor code.  It
must reconstruct the claims using alternative calculations where possible:

- Sylvester resultants rather than producer discriminant calls;
- a different Gröbner order for the ordered-root ideal;
- an independent projective singularity and infinity calculation;
- fresh enumeration of the permutation group;
- fresh half-orbit recurrence generation;
- byte locks on Paper 5, HCS-C12C, and HCS-C20.

## 5. Clock-preservation rule

The following indices may never be identified or averaged:

- primitive Hénon period (n);
- chronological phase (s);
- Frobenius extension degree (r_F).

The source radical is denoted $\eta$, even though Endler--Gallas and the
internal symbolic code call it (r).  No simple average of transition
matrices is an admissible substitute for chronological composition.

## 6. Claim gates

### Gate 1: geometry

Proceed only if geometric connectedness, exact group, compactified branch
data, and genus are all proved.  Generic numerical fibers are insufficient.

### Gate 2: cohomology

Proceed to comparison only after the rotation fixed field is proved by
inclusion plus degree equality.  A guessed quotient equation is insufficient.

### Gate 3: cross-period interpretation

Call a relation primitive only if it lives on exact-period marked covers and
respects a faithful time generator.  A coarse marker equality or common
quadratic field does not pass this gate.

### Gate 4: Route A

No zeta, Fredholm determinant, Riemann divisor, or Hilbert--Pólya operator is
claimed unless it is independently defined and tested.  Failure is recorded
rather than repaired by target fitting.

## 7. Stopping and switch rules

Stop the route as a negative result if any of the following occurs:

- the ordered cover is disconnected or dynamically redundant;
- the time action is cohomologically trivial with no all-period replacement;
- the cross-period field coincidence factors through lower period;
- no intrinsic repetition law exists;
- a determinant would require identifying (n,s,r_F) or fitting Riemann
  data.

HCS-C21 triggers the second and third stop conditions.  The fixed-period
geometry is retained, but further refinement of this same marker identity is
not the next breadth-first move.

## 8. Frozen outputs

- `results/c21_certificate.json` is the producer artifact.
- `results/c21_independent_check.json` binds the exact certificate bytes and
  records 133 passing named checks.
- `code/test_c21.py` contains 13 regression and fail-closed tests.
- The formal Route-A tuple is
  `(A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.
