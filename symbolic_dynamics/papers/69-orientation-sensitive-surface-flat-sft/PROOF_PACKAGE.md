# Proof package

## 1. Local system

Let `A_i(g) in K` label the oriented edge from `g` to `g x_i`.  The reverse
edge receives the inverse label.  For every `g in Lambda`, impose

```text
A_1(g) A_1(gx_1)
A_2(gx_1^2) A_2(gx_1^2x_2)
A_3(gx_1^2x_2^2) A_3(gx_1^2x_2^2x_3) = 1.
```

Only six coordinates in a fixed finite subset are read, so the allowed set is
a subshift of finite type.

## 2. Gauge-count lemma

For a finite-index subgroup `H<=Lambda`, an `H`-fixed configuration descends
to a flat `K`-connection on the finite connected cover with vertex set
`H\Lambda`.  Let `V=[Lambda:H]`, choose a root and a spanning tree.  A based
gauge transformation is a vertex map equal to `1` at the root; there are
`|K|^(V-1)` such maps.  Its action on edge labels is free.  Every connection
has a unique based gauge transform for which every tree edge is `1`.

For a tree-trivial flat connection, holonomy of a based loop depends only on
its homotopy class and is multiplicative, hence gives `Hom(H,K)`.  Conversely,
a homomorphism assigns holonomy to the non-tree generators and flatness fills
the connection.  These maps are inverse.  Therefore

```text
|Fix_H(X_K)| = |K|^(V-1) |Hom(H,K)|.
```

## 3. Explicit topology of the families

The relation is killed by `f(x_1)=1,f(x_2)=-1,f(x_3)=0`, so `f` is a
well-defined epimorphism to `Z`.

- `H_n=ker(f mod n)` has index `n`.  It contains `x_3`, whose orientation
  character is odd; hence it is not contained in the orientation kernel and
  the cover is nonorientable.  Its Euler characteristic is `-n`, hence its
  nonorientable genus is `n+2`.
- `Lambda^+=ker omega` is the genus-two orientable surface group.  The
  restriction of `f` is onto because `x_1x_3^{-1}` lies in `Lambda^+` and has
  `f`-value `1`.  Thus `L_m=ker(f|Lambda^+ mod m)` has index `m` in
  `Lambda^+` and `2m` in `Lambda`.  Its Euler characteristic is `-2m`, hence
  its orientable genus is `m+1`.

## 4. Surface formulas and fixed spectra

For a finite group `K`, irreducible degree `d_chi`, and Frobenius--Schur
indicator `nu_chi`, the classical formulas are

```text
|Hom(pi_1 Sigma_g,K)| = |K|^(2g-1) sum_chi d_chi^(2-2g),
|Hom(pi_1 N_l,K)|     = |K|^(l-1)  sum_chi nu_chi^l d_chi^(2-l).
```

Substituting `g=m+1,V=2m` and `l=n+2,V=n` into the gauge lemma gives

```text
O_K(m)=|K|^(4m) sum_chi d_chi^(-2m),
N_K(n)=|K|^(2n) sum_chi nu_chi^(n+2)d_chi^(-n).
```

## 5. Finite moment lemma

If `z_1,...,z_r` are distinct nonzero numbers and
`u_m=sum_i a_i z_i^m` for every `m>=1`, then the full sequence determines the
unordered pairs `(z_i,a_i)` after zero coefficients are removed.  Indeed,

```text
sum_(m>=1) u_m t^(m-1) = sum_i a_i z_i/(1-z_i t),
```

and the poles and residues determine the data.  If the bases are already
known, any `r` consecutive moments at nonnegative indices
`m_0,...,m_0+r-1` determine all coefficients by the Vandermonde determinant;
in particular, `m_0=0` is explicitly allowed and zero coefficients cause no
problem.

## 6. Reconstruction

Let `t_d,c_d^+,c_d^-,c_d^0` denote respectively the total multiplicity and the
three indicator multiplicities among irreducibles of degree `d`.

1. Since the trivial representation exists,

   ```text
   lim_(m->infty) O_K(m)^(1/(4m)) = |K|.
   ```

2. `P_m=O_K(m)/|K|^(4m)=sum_d t_d(d^-2)^m` recovers every `d` and `t_d`.
3. `Q_m=N_K(2m)/|K|^(4m)=sum_d(c_d^++c_d^-)(d^-2)^m` recovers
   `s_d=c_d^++c_d^-`.
4. `R_m=N_K(2m+1)/|K|^(4m+2)` equals

   ```text
   sum_d (c_d^+-c_d^-) d^-1 (d^-2)^m,
   ```

   If `r` degrees occur, the known-base Vandermonde system applied to
   `R_0,...,R_(r-1)` first recovers
   `b_d=(c_d^+-c_d^-)/d`.  Multiplication by the already recovered degree `d`
   then gives `delta_d=d*b_d=c_d^+-c_d^-`.
5. Recover

   ```text
   c_d^+=(s_d+delta_d)/2,
   c_d^-=(s_d-delta_d)/2,
   c_d^0=t_d-s_d.
   ```

The reverse implication is immediate from the two count formulas.

## 7. `D_8/Q_8` certificate

Both groups have degrees `1,1,1,1,2`.  All four linear characters have
indicator `+1`.  The two-dimensional indicator is `+1` for `D_8` and `-1`
for `Q_8`.  Consequently

```text
O_D8(m)=O_Q8(m)=8^(4m)(4+2^(-2m)),
N_D8(n)=8^(2n)(4+2^(-n)),
N_Q8(n)=8^(2n)(4+(-1)^n 2^(-n)).
```

Even nonorientable levels agree; odd levels differ.

## 8. Proof-status statement

All internal steps above are symbolic and closed.  The two surface
homomorphism formulas are cited inputs, not new results.  The Python control
recomputes finite tuple counts directly but is not used to justify an
infinite statement.  External release remains on hold.
