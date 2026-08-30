# P125 narrative report

Status: **ROUND-TWO FINAL NARRATIVE / GO_INTERNAL / EXTERNAL HOLD**.

## Why this map survives

The update

```text
Phi(x,y)=(y,x+Q(x)y)
```

is a minimal state-dependent shear: the outgoing vector decides, through its
quadratic state, whether the next pair is a swap or a Fibonacci-type shear.
It is basis-free and commutes with the diagonal orthogonal action, but it is
not a group action.  That combination creates a small quotient without
making the full map bijective.

The early signal is unusually clean.  The polar bit `B(x,y)` is invariant,
and the remaining quadratic bits evolve on four states.  This confines all
depths and periods.  The quotient is not the whole story because zero
coordinates and equal vectors shorten some cycles.  The round-one proof now
displays the matrix word or landing test for all eight quotient rows, so the
equal-vector and zero-coordinate shortenings are explicit rather than
compressed into prose.

## Reverse dynamics

The inverse equation has only two cases:

```text
Phi^{-1}(u,v)
 = {(v,u)       if Q(v)=0}
   union
   {(u+v,u)     if Q(u+v)=1}.
```

This formula does more than count indegrees.  It identifies every missing
target, proves that the second image is the recurrent core, and determines
the exact reverse tree attached to each cyclic type.  The global numbers of
zero and double fibres coincide because `(u,v) -> (v,u+v)` turns them into
the two products of the singular and nonsingular vector sets.

## Witt dependence

All dependence on the quadratic space enters through

```text
N=2^(2m),  S=epsilon*2^m.
```

A three-character Walsh expansion counts the eight `(Q(x),Q(y),B(x,y))`
types.  This gives exact formulas for the recurrent, depth-one, and depth-two
layers.  The smallest minus plane is a genuine boundary: its depth-two count
vanishes, while the plus plane already has depth two.

The pair census is classical finite-quadratic-geometry material and receives
zero contribution credit.  It is nevertheless proved in full so that the
functional-graph formulas do not depend on an imprecise source pointer.

## Six shapes

The forward quotient classifies cycles; the reverse fibres then decorate
them.  The two proof directions are complementary rather than logically
independent.  The only possible components are:

1. a bare fixed point;
2. a bare two-cycle;
3. a two-cycle with one leaf;
4. a two-cycle with one length-two tail at each cycle vertex;
5. a bare three-cycle;
6. a four-cycle with leaves at two alternating vertices.

The fibre ceiling and zero-fibre leaf types rule out all deeper trees.  Closed
counts for these six objects immediately give all cycle counts and the
standard finite-map zeta product.

## Ownership and internal position

An orthogonal or symplectic transvection uses a fixed root and a polar
coefficient and is invertible.  This map uses the moving state's quadratic
value and has many missing and double targets.  It is also not a hidden
Yang--Baxter solution: a hyperbolic plane supplies explicit failures of both
the braid and quantum conventions.  The bounded search found no literal or
conjugate-map owner, but the formula is short enough that owner risk remains
substantial.

Within the internal sequence, P106 is the closest temporal silhouette; its
polarity identity has only depth one and periods one or two.  P99 supplies
the word “shear” in a bijective arithmetic setting.  P103, P109, and P118
have exact finite functional-graph packages on unrelated carriers.  P125's
residual is therefore the Witt-sensitive functional graph of this literal
nonbijective ordered-pair update, not the generic package.

## Evidence boundary

The strengthened verifier exhausts both Witt signs through dimension ten.
It checks every state and target, asserts literal second-image equality, and
traverses actual components rather than only checking component-count mass.
Its directed-cycle signatures are canonicalized under rotation only, with an
asymmetric sentinel that rejects reflection identification.
The run is strong falsification evidence, not proof or ownership evidence.
External circulation remains HOLD.
