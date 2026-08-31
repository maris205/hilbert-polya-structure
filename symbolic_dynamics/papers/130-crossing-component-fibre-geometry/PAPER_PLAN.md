# P130 paper plan and ownership contract

## One-sentence contract

For the specified cut-dependent crossing-component section, prove that every
fibre over a noncrossing target is an independent product of decorated
noncrossing partitions on immediate-sibling lists, then use strict
supermultiplicativity to identify the unique largest fibre.

## Theorem ladder

1. **Definition and factorization (background).**  The literal synchronous
   map is `Phi=s∘pi`, where `pi` records crossing-component supports and `s`
   pairs successive endpoints in every even block.
2. **Retraction census (background).**  Image=fixed set=noncrossing
   matchings; idempotence, Catalan count, depth-one/Garden census and fixed-n
   zeta follow formally.
3. **Sibling inverse (residual main theorem).**  A source over `T` is
   equivalent to an independent decorated noncrossing partition of every
   ordered immediate-sibling list in the nesting forest, including the
   virtual root.
4. **Pointwise fibres (residual main theorem).**  The bijection gives
   `|Phi^{-1}(T)|=product_v a_{d_T(v)}` in every size, including `n=0`.
5. **Unique maximum (residual main theorem).**  Strict
   `a_i a_j<a_{i+j}` and the child-degree sum show that the consecutive
   target alone has fibre `a_n`.
6. **Formal transform and mass (background).**  `A=1+C(uA)`, A111088 and
   the total fibre mass are stated only as owned consistency facts.

## Four-step inverse proof obligation

1. Forward: a component-support block sections into immediate siblings under
   one parent.  If two parents are comparable and distinct, the inner parent
   is a strict intermediate container between a section chord and its alleged
   outer immediate parent.  The induced groups are noncrossing in sibling
   order.
2. Converse: arbitrary noncrossing sibling groups first give disjoint
   even blocks covering every endpoint.  For a child selected by `Q`, its
   descendant interval is a gap of `B_Q`; for an unselected child, its closed
   support is a strict subinterval of one gap.  Disjoint child intervals and
   the same argument at the virtual root close the global noncrossing
   induction and section back to the target.
3. Decoration: connected diagrams transported to endpoint blocks have
   exactly those blocks as crossing components.
4. Mutual inverse: extraction and construction recover both grouping and
   standardized decoration, including repeated sizes and the virtual root.

## Two proof engines

- **Local-to-global inverse engine:** cyclic gaps of a noncrossing partition,
  forest induction and connected standardization prove the pointwise product.
- **Extremal injection engine:** juxtaposition plus an all-crossing diagram
  proves strict supermultiplicativity; a rooted-forest degree argument forces
  the unique maximizer.

These engines are logically different: the first classifies every source;
the second compares already-classified fibres without reusing the inverse.

## Ownership ceiling

Zero credit is assigned individually to Kreweras (noncrossing partitions),
Flajolet--Noy (connected chord decompositions), Nabergall (decorated
even-block decomposition), Acan (intersection graphs), Callan (noncrossing
transform), Igusa (the exact nonempty parallel-set specialization in
Definition 1.7 and compatible merging in Proposition 1.8, with degree zero
retained only as `A_0` bookkeeping), Thomas Lam (uncrossing poset),
and Alman--Lian--Tran (the all-size full-wiring sequence A111088: Theorem
4.1.6, Remark 4.1.7, Theorem 4.1.8 and Theorem 4.2.1).  The author
attribution of Lam's paper must remain Thomas Lam.  A bounded non-hit for the
residual conjunction is not a novelty claim.

## Presentation ceiling

Anonymous compact `amsart`; formal OGF only; no asymptotic, priority,
unrooted canonicity or complete novelty language.  External status is
`HOLD_EXTERNAL` throughout this package.
