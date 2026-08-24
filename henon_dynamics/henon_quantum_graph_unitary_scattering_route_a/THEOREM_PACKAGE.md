# Theorem package — exact theta-graph unitary scattering

Let

```text
C = (2/3) 11^T - I_3,
S = [[0,C],[C,0]],
J = [[0,I_3],[I_3,0]].
```

The six basis vectors are the directed bonds of the theta graph.  If the three
undirected lengths are `ell=(1,2,3)`, put

```text
P_bb(k)=exp(i k ell_b/2),   U(k)=P(k) S P(k).
```

## Theorem 1 — source-derived unitary and reversal

For every real `k`, `U(k)` is unitary.  With coefficient conjugation `K` and
bond reversal `J`, the antiunitary `Theta=J K` satisfies

```text
Theta U(k) Theta^{-1}=U(k)^{-1}.
```

**Proof.** `C` is real symmetric with eigenvalue `1` on the constant vector
and `-1` on its orthogonal complement.  Hence `C^2=I`, `S^2=I`, and `S` is
orthogonal.  For real `k`, `P` is unitary.  Moreover `J` commutes with both
`S` and `P`, because reverse bonds have the same undirected length.  Therefore
`J overline(U) J=P^{-1}SP^{-1}=U^{-1}`.

## Theorem 2 — secular determinant

With `x_j=exp(i k ell_j)` and

```text
M(k)=S diag(x1,x2,x3,x1,x2,x3),
```

Sylvester's determinant identity gives

```text
det(I-rho U(k))=det(I-rho M(k)).
```

At `rho=1` the exact multivariate factorization is

```text
-(3*x1*x2*x3-x1*x2-x1*x3-x1-x2*x3-x2-x3+3)
 *(3*x1*x2*x3+x1*x2+x1*x3-x1+x2*x3-x2-x3-3)/9.
```

For the physical specialization `(x1,x2,x3)=(t,t^2,t^3)`, it becomes

```text
-(t-1)^3(t+1)(t^2+1)(t^2+t+1)
 *(3t^2-2t+3)(3t^2+5t+3)/9.
```

## Theorem 3 — all-period orbit product

For `|rho|` sufficiently small,

```text
det(I-rho M)
 = exp(-sum_{n>=1} rho^n Tr(M^n)/n)
 = product_[p] (1-rho^{n_p} A_p exp(i k L_p)),
```

where `[p]` runs over primitive cyclic directed-bond walks, `n_p` is the
topological period, `L_p` is the metric length accumulated once per bond, and
`A_p` is the ordered product of Kirchhoff scattering amplitudes.  Repetition,
orientation, multiplicity, phase, and stability/scattering amplitude are thus
kept rather than replaced by absolute values.

The finite certificate records 14,760 rooted walks and 1,905 primitive cycles
through period eight; these are replay sentinels, not the basis of the
all-period proof.

## Exact obstructions and boundary

The wrong coefficient `1/2` gives `C_bad^T C_bad-I=-(1/4)11^T`, so the bond
map is not unitary.  Direction-dependent reverse length `(1,2,4)` gives eight
nonzero entries in the `J K` reversal defect.  These controls show that the
positive result depends on the frozen Kirchhoff and metric-graph structure.

The strict tuple is

```text
(A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE).
```

No target divisor, functional equation, target counting law, or Hilbert--Pólya
operator is supplied.  `route_b_invocation_allowed` remains `false`.
