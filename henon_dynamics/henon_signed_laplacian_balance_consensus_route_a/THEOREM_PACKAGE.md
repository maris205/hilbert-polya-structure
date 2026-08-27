# Theorem package

## Frozen object

For each undirected edge `e={i,j}` choose an orientation, sign `sigma_e` in
`{+1,-1}` and weight `w_e>0`.  Set `b_e=e_i-sigma_e e_j`, `B=[b_e]`,
`W=diag(w_e)` and `L=B W B^T`.  The flow is `x_dot=-Lx`.

## Kernel, projector and exact rate

Because

```text
x^T L x = sum_e w_e (x_i-sigma_e x_j)^2,
```

a connected component has a one-dimensional kernel exactly when it is
structurally balanced; a switch vector `s_C in {+1,-1}^C` spans it.  An
unbalanced component has zero kernel.  Isolated vertices count as balanced.
Thus `nullity(L)` is the number of balanced components and

```text
P=sum_balanced_C s_C s_C^T/|C|,
exp(-tL) -> P.
```

If `L` has a positive eigenvalue, let `gamma` be its smallest one.  Symmetry
gives the exact identity

```text
||exp(-tL)-P||_2=exp(-gamma t).
```

If `L=0`, `P=I` and the difference is identically zero; `gamma` is not needed.

## Full pseudoforest theorem

For root set `R subset V`,

```text
det L[V\R] = sum_F 4^{u(F)} product_{e in F} w_e,
```

where every component of spanning `F` is either a tree containing exactly one
root or a root-free unbalanced (equivalently negative-cycle) unicycle, and
`u(F)` counts the latter.  Moreover

```text
det(lambda I+L) = sum_F 4^{u(F)} w(F) lambda^{t(F)}
                  product_{tree components T}|V(T)|,
```

over spanning pseudoforests whose components are trees or negative unicycles;
`t(F)` counts tree components.  Cauchy–Binet proves the minor formula because
rooted-tree incidence minors have squared determinant 1 and negative-unicycle
incidence determinants have squared determinant 4.  Summing each minor over
its root set proves the characteristic expansion.

## Sharp counterexamples and exclusions

In the positive bridge `0-1` plus signed triangle `1-2-3-1` of signs `-,+,+`,
the full determinant is 4.  Deleting root 0 gives cofactor 7: three ordinary
spanning trees plus weight 4 from the isolated root together with the root-free
negative triangle.  A tree-only formula is false.

The directed matrix `[[1,-1],[-2,2]]` has right zero vector `(1,1)` but
normalized left zero vector `(2/3,1/3)`, giving an oblique, nonuniform limit.
It is outside the symmetric theorem.

## Evidence and Route A

All 760 labelled signed simple graphs on `1<=n<=4` and all 11,894 root sets
are enumerated exactly at unit weights.  This validates implementation, not the
arbitrary-size/weight proof.

```text
(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
ROUTE_A_REJECTED; Route B false.
```
