# Paper 38 source lock — presentation-canonical Bass–Serre candidate

Date frozen: 2026-08-15
Candidate: `SD-C40`
Family: Symbolic Dynamics
Route: strict Route A v0.2; Route B locked

## 1. New-object declaration

Paper 38 receives **no same-object and no same-marker credit** from Papers
35–37.  Its sole object is the full oriented-edge geodesic shift on the
presentation-canonical Bass–Serre tree of the original ascending HNN
splitting

\[
G_r=BS(1,r)=\langle u,v\mid vuv^{-1}=u^r\rangle,
\qquad r\geq 1,
\]

over the vertex group \(\langle u\rangle\cong\mathbb Z\).  The only allowed
coefficient is the canonical signed HNN height/modular cocycle.  Its sign
convention may be inverted, but no other representation, character, quotient,
basepoint, damping, or alternative divisor splitting may be substituted.

## 2. Frozen invariant and ownership target

The primary candidate invariant is the primitive-orbit Euler product of the
**full-tree** nonbacktracking/geodesic shift, together with an ordinary
Fredholm identity \(\det(I-zB)\) for the corresponding operator on
\(\ell^2(E^{\mathrm{or}}T_r)\).

The following are distinct objects and cannot be credited as that invariant:

1. a quotient graph or graph-of-groups edge operator;
2. a von Neumann/groupoid determinant;
3. a weighted infinite-graph determinant whose weight has finite total mass;
4. a group-conjugacy or hyperbolic-end Euler product;
5. an arbitrary finite-dimensional local system;
6. a radial/basepoint damping;
7. a different Bass–Serre tree arising from another divisor splitting.

Any such construction may be reported only as a typed boundary control.

## 3. Frozen theorem target and falsifiers

The theory-first target is the following terminal trilemma.

- **Empty:** a tree has no positive-length reduced closed path, so the literal
  full-tree primitive ledger is empty.
- **Non-Fredholm:** the undamped Hashimoto operator has an infinite
  orthogonal image family of constant nonzero norm and is noncompact, hence
  not trace class.
- **Wrong determinant category:** for \(r\geq2\), the action is faithful and
  its image in \(\operatorname{Aut}(T_r)\) is non-discrete.  For \(r=1\),
  \(G_1\cong\mathbb Z^2\), the kernel is \(\langle u\rangle\), and the image
  \(\langle v\rangle\cong\mathbb Z\) acts discretely by translations; however,
  the frozen \(G_1\)-action has infinite vertex and edge stabilizers, is
  non-proper, and fails the finite-stabilizer tree-lattice hypotheses.
  Passing to the discrete image would quotient the acting group and change
  the orbital ledger, so discrete tree-lattice formulas cannot be imported
  as same-object evidence.

Falsification requires one of the following on the frozen object itself:

1. an exact positive reduced closed path in \(T_r\);
2. a nonzero presentation-canonical modular weighting that makes the
   full-tree edge operator trace class without changing the object;
3. a proper finite-stabilizer action satisfying the discrete tree-lattice
   hypotheses without quotienting the acting group;
4. a nonempty, finite, source-selective primitive ledger with a determinant
   in the same ordinary Fredholm category.

## 4. Mandatory firewalls

- **Object:** full tree, quotient, group orbit, end, and graph-of-groups
  ledgers are separately typed.
- **Fredholm:** formal zero diagonal traces do not define an ordinary
  Fredholm determinant; trace class must be proved first.
- **Marker:** Bass–Serre translation length is a new unit graph-edge clock.
  It cannot inherit the old Cayley generator-step clock.
- **Primitive/repetition:** primitive conjugacy classes and their powers are
  counted separately and checked by Möbius inversion.
- **Positive/graded ownership:** a positive-height group-conjugacy substitute
  is not the two-sided full-tree geodesic ledger, and a modular weight is not
  a graded sign cancellation.
- **PROVES_TOO_MUCH:** interpreting \(1/|\mathbb Z|\) as zero annihilates every
  vertex/edge/end contribution, producing the same trivial answer for all
  infinite-stabilizer controls.  That convention is forbidden.

## 5. Frozen controls

1. balanced control \(r=1\);
2. prime controls \(r=2,3,5,7\);
3. composite baseline \(r=4\) and controls \(r=6,8,9,10,12\);
4. deliberate \(BS(p,q)\) presentations spanning ascending,
   reversed-ascending, balanced, and non-ascending GBS cases;
5. seeded random cyclically reduced two-generator one-relator presentations,
   with eligibility tested independently rather than silently assigning a
   Bass–Serre splitting;
6. empty-tree and finite rooted-tree controls;
7. orthogonal-column/noncompactness controls;
8. divergent \(r=1\) group-conjugacy control;
9. marker-collapse and same-tree-step/different-old-step controls;
10. fresh source/evaluator-separated double execution.

## 6. Precommitted decision rule

`GO` requires all of the following on the frozen full-tree object:

- nonempty and source-selective primitive cycles;
- an honest ordinary Fredholm determinant;
- a new, internally consistent tree-edge marker;
- survival of balanced, prime/composite, GBS, random-presentation, empty,
  divergent, and marker controls.

Any generic ledger, empty ledger, non-trace-class operator, incompatible
marker, or inapplicable determinant hypothesis is terminal:

`STOP_BASS_SERRE_TREE_BRANCH` and `CLOSE_ENTIRE_AFFINE_BRANCH`.

No repair search follows a terminal result.

## 7. Frozen result

The terminal trilemma is proved.  A separately typed group-conjugacy
calculation is finite for \(r\geq2\) but is the generic \(r\)-ary necklace
ledger, collapses to \((1-z)/(1-rz)\), and is not the full-tree Fredholm
object.  At \(r=1\) it is divergent.  The marker is many-to-one relative to
the old generator clock.

Decision:

`STOP_BASS_SERRE_TREE_BRANCH` / `CLOSE_ENTIRE_AFFINE_BRANCH`.

Strict tuple:

`(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`.

## 8. Paper 39 minimum obligation

Paper 39 has exactly one permitted direction: an **affine-branch closure
synthesis/audit**.  It must consolidate the typed obstructions from Papers
35–38 into an obstruction DAG, prove that no successor remains under the
current affine candidate contract, and return control to the already existing
global Symbolic Dynamics candidate registry.  It may not introduce another
affine representation, quotient, local system, cocycle, tree, damping, or
marker.  If no non-affine candidate is independently source-locked before
evaluation, Paper 39 must STOP without proposing a mechanism.
