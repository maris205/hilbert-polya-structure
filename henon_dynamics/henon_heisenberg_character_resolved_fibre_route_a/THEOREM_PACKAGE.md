# C151 proof package

## Status and notation

**Status: PROVABLE AS STATED.**  Let `H=R^3` have product

```text
(x,y,z)(X,Y,Z)=(x+X,y+Y,z+Z+xY),
```

let `Gamma=Z^3`, and work on the left quotient `N=Gamma\H`.  Put
`A=((2,1),(1,1))`,
`q(x,y)=x(x-1)+xy+y(y-1)/2`, and
`Phi(v,z)=(Av,z+q(v))`.  C146 proves that this is a lattice automorphism.
For `B=A^n`, set

```text
M=B-I,  q_n(v)=sum_(j=0)^(n-1)q(A^jv).
```

The matrix `M` is invertible because the eigenvalues of `A` are positive and
different from one.

## Theorem 1: exact fibre rotation

Horizontal fixed classes of the induced toral map are naturally indexed by
`Z^2/MZ^2`.  For a representative `m` choose `v=M^(-1)m` and define

```text
rho_n(v)=q_n(v)-m_1 v_2  (mod 1).                (1)
```

The class above `v` is a fixed central circle of `Phi^n` if and only if
`rho_n(v)=0`.  If the rotation is nonzero, that horizontal class contains no
fixed point.

**Proof.**  Iteration gives
`Phi^n(v,z)=(Bv,z+q_n(v))`.  It represents the same point as `(v,z)` on the
left quotient exactly when some `(m_1,m_2,k)` in `Gamma` satisfies

```text
(Bv,z+q_n(v))=(m_1,m_2,k)(v,z)
              =(v+m,z+k+m_1v_2).
```

The horizontal equation is `m=Mv`; the central equation is precisely
`q_n(v)-m_1v_2=k`.  It is independent of `z`, so when it holds the entire
central fibre is fixed, and otherwise no point in the fibre is fixed. ∎

## Lemma 2: representative invariance

Formula (1) depends only on the class of `m` modulo `MZ^2`.

**Proof.**  Replace `v` by `v+r`, where `r` is integral, and put `s=Mr`; then
`m` becomes `m+s`.  Because `Phi^n` is a group automorphism,

```text
q_n(v+r)-q_n(v)-q_n(r)=(Bv)_1(Br)_2-v_1r_2.     (2)
```

Using `Bv=v+m` and `Br=r+s`, subtraction in (1) first reduces the change to

```text
q_n(r)+det(v,s)+m_1s_2-s_1r_2.                 (3)
```

Area preservation gives
`det(v+m,r+s)=det(Bv,Br)=det(v,r)`, hence
`det(v,s)=-det(m,r)-det(m,s)`.  Substitution into (3) gives

```text
q_n(r)-m_1r_2+m_2r_1+s_1m_2-s_1r_2.
```

Every displayed term is integral: `m,r,s` are integral and `q_n(r)` is
integral because `Phi^n` preserves the lattice.  Thus the change is zero
modulo one. ∎

## Theorem 3: all-iterate central root-of-unity projector

Write `D_n=|det M|`.  Each coordinate of `M^(-1)m` has denominator dividing
`D_n`.  The polynomial `q_n` is quadratic with half-integral coefficients;
therefore every rotation in (1) belongs to `(1/Q_n)Z/Z`, where

```text
Q_n=2D_n^2.                                      (4)
```

If `C_n` is the number of clean fixed-circle components, then

```text
C_n=(1/Q_n) sum_(a=0)^(Q_n-1)
       sum_([m] in Z^2/MZ^2) exp(2 pi i a rho_n(m)).       (5)
```

**Proof.**  The denominator statement follows from the adjugate formula for
`M^(-1)` and the degree-two, half-integral form of `q_n`.  For a rotation
`k/Q_n`, the outer average in (5) is one when `k=0 mod Q_n` and zero
otherwise.  Theorem 1 identifies those zero terms exactly with fixed central
circles.  The generally quadratic map `rho_n` is not asserted to be a
homomorphism of the horizontal quotient; (5) is a central cyclic root-of-unity
filter, not a group-character formula for that quotient. ∎

Along a fixed fibre, the derivative of `Phi^n` is block lower triangular with
diagonal blocks `B` and `1`.  Since `I-B` is invertible, the kernel of
`I-DPhi^n` is exactly the central tangent.  Hence each counted circle is a
clean fixed component, not an isolated orbit.

## Exact cutoff certificate and rejected extrapolation

Column Hermite representatives reconstruct every class through `n=12`.
The pairs `(D_n,C_n)` are

```text
(1,1),(5,1),(16,4),(45,1),(121,21),(320,4),
(841,57),(2205,1),(5776,148),(15125,105),
(39601,397),(103680,144).
```

The checker rebuilds every rotation by direct cocycle iteration, while SymPy
rebuilds the first eight full histograms by a third method.  Early
Lucas/parity/modulo-three patterns fail at `n=10` and `n=12`; no all-`n`
closed form for `C_n` is asserted.

## Route-A boundary

The clean circles still prevent an isolated primitive-orbit ledger and make
the ordinary isolated stability factor singular.  The natural Haar Koopman
unitary is only a formal lift hint; (5) is not promoted to an operator trace
formula.  The strict tuple is
`(A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.  No target divisor, functional
equation, counting law, arithmetic/local datum, Euler factor, root number,
automorphy statement, Hilbert--Polya construction, or Route-B authorization is
claimed.
