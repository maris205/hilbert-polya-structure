# P120 paper plan — odd-fringe mirror dynamics on plane rooted trees

Status: **PROVABLE AS STATED / ANONYMOUS AUTHOR DRAFT / EXTERNAL HOLD**.

## One-sentence contribution

For the simultaneous plane-tree map that reverses precisely the child lists
whose fringe subtrees have odd order, we prove an involution law, a literal
twisted-palindrome fixed criterion, coupled parity generating functions, an
explicit degree-six equation for the fixed series, and the resulting exact
one-/two-cycle census.

## Frozen claim ceiling

The paper may claim only:

1. the map is well defined on the empty state and all finite plane rooted
   trees, preserves every fringe order and underlying rooted tree, and is an
   involution;
2. an even-order root is fixed exactly when every child is fixed, while an
   odd-order root is fixed exactly when its child list is an `M`-twisted
   palindrome;
3. if `E` and `O` count nonempty fixed trees of even and odd order, then
   `E=xO/((1-E)^2-O^2)` and `O=x(1+E)/(1-A(x^2))`;
4. `F=E+O` is the zero-constant branch of the displayed explicit degree-six
   polynomial `P(x,F)=0`;
5. for fixed order `n`, the carrier splits into exactly `f_n` fixed points
   and `(a_n-f_n)/2` two-cycles, giving the stated fixed-iterate counts and
   Artin--Mazur zeta factorization;
6. the separate conventions `a_0=f_0=1` make the empty lane a singleton
   identity, while the generating series `A,E,O,F` count nonempty trees.

The paper must not claim asymptotics, a minimal polynomial, irreducibility,
priority, an owner-clearance certificate, a general Catalan involution
theorem, or novelty for mirror symmetry, Catalan enumeration, context-free
algebraicity, resultant elimination, or zeta bookkeeping.

## Proof dependency map

1. Recursive size invariance shows that every old fringe parity survives one
   update.  Either recursive induction or commuting local reversals then
   proves `M^2=id`.
2. Comparing the ordered child tuple with its image gives the two root-local
   fixed criteria without enumeration.
3. At an even root, take the odd-size part of a sequence of fixed children.
   At an odd root, choose one arbitrary tree for each off-centre pair
   `(T,M(T))`; an optional central child must be fixed and even.  These two
   decompositions prove the coupled system.
4. Set `F=E+O`, `G=E-O`, and `B=A(x^2)`.  Two rational identities together
   with `B^2-B+x^2=0` have resultant `4x^2 P(x,F)`; the formal power-series
   domain has no zero divisors.  Since `P_y(0,0)=-3`, the zero-constant branch
   is unique.
5. An involution has only one- and two-cycles.  This gives every fixed-iterate
   count and the zeta product immediately.

## Section plan

1. Introduction: literal rule, why the fixed set is not ordinary mirror
   symmetry, exact claim package, and strict credit subtraction.
2. Definition and involution: empty lane, recursive update, invariant fringe
   orders, two involution routes, and the fixed criterion.
3. Fixed-tree grammar: derive `E/O` with the parity offsets and explain the
   twisted-palindrome pairs.
4. Elimination and coefficients: derive the explicit polynomial and record a
   compact coefficient table.
5. Complete temporal census: fixed/two-cycle counts, iterate-fixed counts,
   and fixed-order zeta.
6. Owner subtraction, objectwise firewalls, and exact controls.
7. Conclusion with no new claim.

No figure is needed.  The child-tuple examples, two boxed functional
equations, algebraic equation, and compact coefficient table carry the story.

## Owner and credit boundary

- Chen--Shapiro--Yang and Deutsch own direct plane-tree involution and
  bijection neighborhoods.
- Li--Lin--Zhao own recent binary/plane-tree mirror involutions.
- Claesson--Kitaev--Steingrímsson--Wang own the 2026 abstract Catalan
  involution framework, global reversal factorization, and Donaghey
  connection.  Their size is edge count: in the present vertex grading their
  fixed census is one object at order 1, `C_k` objects at order `2k+2`, and
  zero at odd orders at least 3.  This indexing translation is part of the
  owner subtraction, not a contribution.
- Bousquet-Mélou--Krattenthaler own current cyclic actions and fixed-set
  phenomena on rooted plane trees.
- Flajolet--Sedgewick own the Catalan/symbolic algebraic machinery, and
  Artin--Mazur own the zeta construction.
- Classical global mirror symmetry, resultant manipulation, and the
  one-/two-cycle formula for an involution receive zero credit.
- P114's forest leaf peeling is internally disjoint: it deletes vertices,
  has height-governed transients and Cayley basins, while P120 preserves all
  vertices/edges and every state is recurrent of period at most two.

The bounded search miss is not evidence of priority.  External circulation,
submission, and specialist contact remain **HOLD**.
