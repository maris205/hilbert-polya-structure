# C129 theorem package

## Frozen construction

Let `A=[[3/16,-1/32],[1/4,0]]` and
`phi_j(z)=A z+(t_j,0)` with `t=(-2,0,2)`. Let

```text
B = [[1,1,0],[1,0,1],[1,0,0]],   c=(1/2,1/3,1/5),
chi(m)=zeta_5^m,                  W_chi=B diag(c_j chi(t_j)).
```

On the direct sum of three copies of `H^2(D_3^2)`, define

```text
(L_chi f)_i(z) = sum_j B_ij c_j chi(t_j) f_j(phi_j(z)).
```

### Theorem 1: geometry and primitive coding

Each branch maps the closed radius-three bidisc strictly inside the open one.
The coordinate image radii are `21/32` and `3/4`, and adjacent first-coordinate
images have gap `2-2(21/32)=11/16`. Thus the images are pairwise disjoint.

For every admissible cyclic word `w`, the affine composition has linear part
`A^|w|` and a unique fixed point. Strong separation makes its itinerary unique.
Primitive admissible necklaces therefore correspond bijectively to primitive
geometric cycles at every period.

### Theorem 2: trace class and the all-order twisted trace

The compact-interior factorization of every composition block through a
smaller bidisc has a summable total-degree approximation majorant. Hence
`L_chi` is trace class. Translation terms lower polynomial degree, so the
diagonal graded blocks depend only on `A`. Since the eigenvalues of `A` are
`1/8` and `1/16`, for every `n>=1`,

```text
Tr(L_chi^n) = Tr(W_chi^n)/((1-8^(-n))(1-16^(-n))).
```

The numerator is exactly the weighted, phase-twisted sum over rooted closed
words of length `n`.

### Theorem 3: Fredholm and primitive identities

The trace-class determinant is entire and has the normally convergent product

```text
D_chi(z) = product_(r,s>=0) det(I-z 8^(-r)16^(-s) W_chi).
```

Normal convergence follows from summability of `8^(-r)16^(-s)` and the finite
dimension of `W_chi`. Grouping rooted words by primitive necklace and
repetition gives

```text
log D_chi(z) = -sum_[gamma] sum_(m>=1)
  (c_gamma chi(M_gamma) z^ell_gamma)^m
  /(m det(I-A^(m ell_gamma))).
```

Here `M_gamma` is the sum of the branch translations around the primitive
word. This is an all-period identity, not a period-eight extrapolation.

### Theorem 4: exact positive and negative controls

For the original assignment, exact arithmetic in `Q[Z/5]` gives

```text
det(I-z W_chi) = 1-(zeta_5^3/2)z-(zeta_5^3/6)z^2-z^3/30.
```

Use the control assignment `t'=(0,-2,2)`. It has the same unordered image
centers and the same untwisted operator data, but

```text
det(I-z W'_chi) = 1-z/2-(zeta_5^3/6)z^2-z^3/30.
```

Accordingly the linear Hardy Fredholm coefficient changes exactly from
`-(64/105)zeta_5^3` to `-64/105`. Conversely, augmentation of `Q[Z/5]`
(the trivial character) makes every all-order trace and determinant identical
and recovers C124 exactly. The positive conclusion is only sensitivity through
the frozen translation residue character and branch assignment.

## Progress over prior gate

- Over C124, the determinant is no longer blind to all translation
  assignments: the frozen phase distinguishes the displayed pair exactly.
- The same all-period primitive cycles and natural global Hardy owner remain in
  force; no finite-dimensional surrogate replaces them.
- The new phase is a formal U(1) lift, hence `A4_FORMAL_HINT`, but no natural
  unitary quantization is constructed.
- The remaining obstruction is sharp: one finite quotient does not recover
  geometry, and no target divisor, target functional equation, counting law,
  or arithmetic correspondence is tested.
