# Proof package

## 1. Unique sampler

For weights `sum_j w_j=1`, define

```text
L_w(f)=sum_j w_j f_j,       (D u)_j=u_j-u_(j+1).
```

Reindexing gives

```text
L_w(Du)=sum_j (w_j-w_(j-1))u_j.
```

This vanishes for every `u` exactly when all adjacent weights agree. Cyclic
connectivity and normalization force `w_j=1/n`. Conversely those weights
annihilate every coboundary. No positivity assumption is used. If `w` is
nonuniform, choose `k` with `w_k!=w_(k-1)` and `u=1_{k}`; the anomaly is the
nonzero difference.

Equivalently the cyclic incidence matrix has rank `n-1`, a one-dimensional
left kernel, and normalized kernel vector `(1/n,...,1/n)`.

## 2. Universal packet pressure

Let `A_n` be the odd primitive reflection-centered packet and

```text
nu_n^orb=(n D_n)^(-1) sum_(omega in A_n) sum_(j mod n) delta_(sigma^j omega).
```

P64 proves `nu_n^orb -> mu_B` weakly and `n^(-1)log D_n -> (1/2)log2`.
Therefore, for every fixed continuous `f` and real `s`,

```text
b_n(f)=int f d nu_n^orb -> int f d mu_B,
Z_n(s;f)=D_n exp(-s n b_n(f)),
P_f(s)=(1/2)log2-s int f d mu_B.
```

Finite cyclic telescoping gives `b_n(f+u-u o sigma)=b_n(f)` exactly. The same
holds in the limit. Since `mu_B` is a probability measure,

```text
|P_f(s)-P_g(s)| <= |s| ||f-g||_infinity.
```

## 3. Boundary

The functional is affine and has reflection-packet base entropy, so it is not
ordinary full-shift topological pressure in general. It has no intrinsic
prime-power semantics or determinant realization. Those remain open.
