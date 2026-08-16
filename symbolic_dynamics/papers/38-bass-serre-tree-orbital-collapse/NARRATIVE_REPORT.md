# Paper 38 narrative report — SD-C40

## 1. The final affine obligation

Paper 37 closed coefficient repairs on the affine Cayley relation ledger.  A
new matrix, rank, character, or grading was no longer eligible.  The sole
remaining affine question changed geometry: use the presentation-canonical
Bass--Serre tree of the original ascending HNN splitting and permit only its
canonical modular cocycle.

That change is real.  The tree-edge clock is not the old generator-step
clock, and the full tree is not the Cayley graph or its quotient.  Paper 38
therefore begins with no inherited object or marker credit.

## 2. The full-tree trilemma

The candidate stops for three independent reasons.

First, a tree has no positive reduced closed path.  The literal full-tree
geodesic shift has no periodic point and hence no primitive ledger.

Second, the absence of closed paths does not make the Hashimoto operator
small.  An infinite orthonormal edge family maps to pairwise orthogonal
vectors of norm `sqrt(r)`.  The operator is noncompact and not trace class,
so its ordinary Fredholm determinant is not defined.  The modular cocycle
only gives fixed nonzero weights to the two step orientations and retains the
same obstruction.

Third, the standard tree-lattice determinant cannot be borrowed as
same-object evidence.  For `r>=2`, the action is faithful and its image in
the automorphism group is non-discrete; its ascending common-end
signed-translation kernel contains `Z[1/r]`.  At `r=1`, the tree is a line,
the action kernel is `<u>`, and the translation image `Z` is discrete.  The
original `Z^2` action is nevertheless non-proper with infinite stabilizers
and fails the finite-stabilizer hypotheses; quotienting to the image changes
the acting group and orbital ledger.

These failures are separately sufficient.  Together they prevent a formal
zero trace from being presented as an honest determinant.

## 3. The orbital near miss

The strongest neighboring construction counts group conjugacy classes at
positive HNN height.  Writing

```text
G_r=Z[1/r] semidirect Z
```

reduces height-`k` conjugacy to multiplication-by-`r` orbits in
`Z/(r^k-1)Z`.  Those orbits are `r`-ary necklaces with the two endpoint words
identified.  Burnside and Möbius inversion give

```text
Z_{+,r}(z)=(1-z)/(1-rz).
```

The formula is exact and attractive, but it is not the failed object.  It
counts group orbits rather than full-tree periodic paths, and its rational
law is generic for every matched cyclic index-`r` ascending HNN control.  The
canonical modular cocycle merely rescales `z`:

```text
Z_{+,r,s}(z)=(1-r^{-s}z)/(1-r^{1-s}z).
```

At `r=1`, keeping group conjugacy gives infinitely many classes at every
positive height.  Quotienting the infinite kernel would change the object
again.

## 4. The marker cannot be inherited

Bass--Serre translation length is `|h(g)|`.  Every `u^m` is elliptic and has
tree length zero; every `u^m v` has tree length one.  The old generator paths
have lengths `m` and `m+1`.  Even the displayed defining relation has `r+3`
old steps and zero tree translation.

This many-to-one collapse is not a flaw in the new clock.  It proves that the
object changed and that Paper 38 cannot claim the old marker's analytic or
arithmetic obligations as already satisfied.

## 5. Exact evidence

The corrected authority evaluator passes `277/277` checks across 11
parameter rows, 18 deliberate GBS controls, 64 seeded random one-relator
eligibility controls, finite-tree witnesses, orthogonal-column certificates,
residue orbits, primitive/repetition identities, rational Euler products,
and marker collisions.  Fresh A/B and isolated cold C reproduce the science,
source packet, and Route bytes exactly; the cold copy is removed.  The
scientific SHA-256 is

```text
a9ffa66d826bcaf8eef0b00991aafa46cdbeaca7014430c68aacf070446adf24.
```

The independent integration passes `44/44` tests and `96/96` integrity
checks.  Its closed result set contains 28 files, the managed text layer has
44 files, and the immutable ledger verifies `42/42` entries with SHA-256
`af2db7457808bcb956c284d28387bf74bfda59f329b688e9491b5ef38066d309`.
Four transport-metadata states and two simulated future-manifest states leave
science and Route bytes unchanged.  A second primary materialization has
`changed_paths=[]`.

The 64 random words contain no eligible cyclic GBS relator.  They therefore
test eligibility discipline, not generic mathematical failure.  The 18
deliberate presentations supply eligible ascending, reversed, balanced, and
non-ascending controls.

Finite rows audit implementation.  The infinite statements remain
theorem-owned.

## 6. The paper's single story

The hero comparison is

```text
full-tree recurrence       -> empty primitive ledger
full-tree edge operator    -> noncompact / no ordinary Fredholm determinant
group-orbital replacement  -> generic necklace law or balanced divergence
old versus new clock       -> incompatible markers
```

No row supplies the missing selective primitive sector.  Switching rows is
not a repair because each row names a different object or ownership category.

## 7. Decision and successor

The HNN exponent is structural (`A0`).  The full-tree ledger is empty and the
orbital replacement is generic or divergent (`A1`).  The full-tree operator
owns no ordinary Fredholm determinant (`A2`).  No prime/composite or matched
presentation control isolates an arithmetic sector (`A3`).  The new marker
cannot inherit the old one (`A4`).

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)
```

Thus Route A is rejected, Route B remains locked, and the entire affine branch
closes.

Paper 39 may only synthesize Papers 35--38 into a typed affine obstruction
DAG and return control to the pre-existing non-affine candidate registry.  It
may not try another affine tree, quotient, representation, local system,
cocycle, damping, or marker.
